# file: project/youtube_dl/extractor/udn.py:41-102
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}

from youtube_dl import YoutubeDL
from youtube_dl.extractor.udn import UDNEmbedIE


def make_ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True})
    return UDNEmbedIE(ydl)


def test_udn_youtube_branch(monkeypatch):
    ie = make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    page = (
        '<html><script>'
        'var options = {"video": {"youtube": "https://www.youtube.com/watch?v=BaW_jenozKc", '
        '"mp4": "/api/mp4"}, "title": "MyTitle", "poster": "http://example.com/poster.jpg"};'
        '</script></html>'
    )

    def fake_dl(url_or_request, video_id, note=None, **kwargs):
        assert video_id == '300040'
        assert str(url_or_request) == url
        return page

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(url)
    assert result['_type'] == 'url'
    assert result['url'] == 'https://www.youtube.com/watch?v=BaW_jenozKc'
    assert result['ie_key'] == 'Youtube'


def test_udn_if_branch_all_formats(monkeypatch):
    ie = make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    page = (
        '<html><script>var options = {"video": {'
        '"empty": "", '
        '"hls": "/api/hls", '
        '"hds": "/api/hds", '
        '"mp4_high": "/api/high", '
        '"mp4_plain": "/api/plain"'
        '}, "title": "DirectTitle", "poster": "http://example.com/p.jpg"};'
        '</script></html>'
    )

    def fake_dl(url_or_request, video_id, note=None, **kwargs):
        s = str(url_or_request)
        if s == url:
            return page
        if '/api/hls' in s:
            return 'http://example.com/video.m3u8'
        if '/api/hds' in s:
            return 'http://example.com/video.f4m'
        if '/api/high' in s:
            return 'http://example.com/path_720p_1500.mp4'
        if '/api/plain' in s:
            return 'http://example.com/path/video.mp4'
        raise AssertionError('unexpected api url: %s' % s)

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)

    def fake_m3u8(m_url, video_id, **kwargs):
        assert m_url == 'http://example.com/video.m3u8'
        assert video_id == '300040'
        return [{'url': m_url, 'format_id': 'hls-test', 'ext': 'mp4'}]

    def fake_f4m(f_url, video_id, **kwargs):
        assert f_url == 'http://example.com/video.f4m'
        assert video_id == '300040'
        return [{'url': f_url, 'format_id': 'hds-test', 'ext': 'flv'}]

    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_m3u8)
    monkeypatch.setattr(ie, '_extract_f4m_formats', fake_f4m)

    result = ie._real_extract(url)
    assert result['id'] == '300040'
    assert result['title'] == 'DirectTitle'
    assert result['thumbnail'] == 'http://example.com/p.jpg'
    formats = result['formats']
    assert isinstance(formats, list)
    assert len(formats) == 4
    by_url = {f['url']: f for f in formats}
    assert 'http://example.com/video.m3u8' in by_url
    assert 'http://example.com/video.f4m' in by_url
    high = by_url['http://example.com/path_720p_1500.mp4']
    assert high['format_id'] == 'http-mp4_high'
    assert high['height'] == 720
    assert high['tbr'] == 1500
    plain = by_url['http://example.com/path/video.mp4']
    assert plain['format_id'] == 'http-mp4_plain'
    assert 'height' not in plain
    assert 'tbr' not in plain


def test_udn_else_branch_with_poster(monkeypatch):
    ie = make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    page = (
        '<html><script>'
        'var options = {"video": {"mp4": "/api/fallback_mp4"}, '
        "title: 'Fallback Title', "
        "poster: 'http://example.com/fallback.jpg', "
        'bad: undefined};'
        '</script></html>'
    )

    def fake_dl(url_or_request, video_id, note=None, **kwargs):
        s = str(url_or_request)
        if s == url:
            return page
        assert '/api/fallback_mp4' in s
        return 'http://example.com/fallback_480p_800.mp4'

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(url)
    assert result['id'] == '300040'
    assert result['title'] == 'Fallback Title'
    assert result['thumbnail'] == 'http://example.com/fallback.jpg'
    assert len(result['formats']) == 1
    fmt = result['formats'][0]
    assert fmt['url'] == 'http://example.com/fallback_480p_800.mp4'
    assert fmt['format_id'] == 'http-mp4'
    assert fmt['height'] == 480
    assert fmt['tbr'] == 800


def test_udn_else_branch_no_poster_skip_and_plain(monkeypatch):
    ie = make_ie()
    url = 'https://video.udn.com/play/news/303776'
    page = (
        '<html><script>'
        'var options = {"video": {"mp4": "/api/plain2", "empty2": null}, '
        "title: 'NoPoster Title', "
        'bad: undefined};'
        '</script></html>'
    )

    def fake_dl(url_or_request, video_id, note=None, **kwargs):
        s = str(url_or_request)
        if s == url:
            return page
        assert '/api/plain2' in s
        return 'http://example.com/nopattern.mp4'

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(url)
    assert result['id'] == '303776'
    assert result['title'] == 'NoPoster Title'
    assert result['thumbnail'] is None
    assert len(result['formats']) == 1
    fmt = result['formats'][0]
    assert fmt['url'] == 'http://example.com/nopattern.mp4'
    assert fmt['format_id'] == 'http-mp4'
    assert 'height' not in fmt
    assert 'tbr' not in fmt
