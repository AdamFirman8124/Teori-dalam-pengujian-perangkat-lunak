# file: project/youtube_dl/extractor/udn.py:41-102
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}

from youtube_dl.extractor.udn import UDNEmbedIE
from youtube_dl import YoutubeDL


def _make_ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True})
    ie = UDNEmbedIE()
    ie.set_downloader(ydl)
    return ie


def test_udn_youtube_via_options(monkeypatch):
    ie = _make_ie()
    test_url = 'http://video.udn.com/embed/news/300040'
    yt_url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    page = (
        '<html><script>'
        'var options = {"video": {"youtube": "%s", "mp4": "/api/mp4"}, '
        '"title": "My Title", "poster": "http://example.com/poster.jpg"};'
        '</script></html>' % yt_url
    )

    def fake_dl(url, video_id, *args, **kwargs):
        assert video_id == '300040'
        assert url == test_url
        return page

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(test_url)
    assert result['_type'] == 'url'
    assert result['url'] == yt_url
    assert result['ie_key'] == 'Youtube'


def test_udn_formats_all_branches(monkeypatch):
    ie = _make_ie()
    test_url = 'http://video.udn.com/embed/news/300041'
    page = (
        '<html><script>var options = {"video": {'
        '"empty": "", '
        '"hls": "/api/hls", '
        '"hds": "/api/hds", '
        '"mp4_high": "/api/video_720p_2000.mp4", '
        '"mp4_plain": "/api/plain.mp4"}, '
        '"title": "Full Title", "poster": "http://example.com/poster.jpg"};'
        '</script></html>'
    )

    def fake_dl(url, video_id, *args, **kwargs):
        assert video_id == '300041'
        if url == test_url:
            return page
        if 'api/hls' in url:
            return 'http://cdn.example.com/stream.m3u8'
        if 'api/hds' in url:
            return 'http://cdn.example.com/stream.f4m'
        if 'video_720p_2000.mp4' in url:
            return 'http://cdn.example.com/video_720p_2000.mp4'
        if 'plain.mp4' in url:
            return 'http://cdn.example.com/plain.mp4'
        raise AssertionError('unexpected url %s' % url)

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)

    def fake_m3u8(m3u8_url, video_id, ext='mp4', m3u8_id='hls', *args, **kwargs):
        assert m3u8_url == 'http://cdn.example.com/stream.m3u8'
        assert ext == 'mp4'
        assert m3u8_id == 'hls'
        return [{'url': m3u8_url, 'format_id': 'hls', 'ext': 'mp4'}]

    def fake_f4m(f4m_url, video_id, f4m_id='hds', *args, **kwargs):
        assert f4m_url == 'http://cdn.example.com/stream.f4m'
        assert f4m_id == 'hds'
        return [{'url': f4m_url, 'format_id': 'hds', 'ext': 'flv'}]

    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_m3u8)
    monkeypatch.setattr(ie, '_extract_f4m_formats', fake_f4m)

    result = ie._real_extract(test_url)
    assert result['id'] == '300041'
    assert result['title'] == 'Full Title'
    assert result['thumbnail'] == 'http://example.com/poster.jpg'
    formats = result['formats']
    assert isinstance(formats, list)
    assert len(formats) == 4
    by_id = {f['format_id']: f for f in formats}
    assert 'hls' in by_id
    assert 'hds' in by_id
    assert 'http-mp4_high' in by_id
    assert 'http-mp4_plain' in by_id
    high = by_id['http-mp4_high']
    assert high['url'] == 'http://cdn.example.com/video_720p_2000.mp4'
    assert high['height'] == 720
    assert high['tbr'] == 2000
    plain = by_id['http-mp4_plain']
    assert plain['url'] == 'http://cdn.example.com/plain.mp4'
    assert 'height' not in plain
    assert 'tbr' not in plain


def test_udn_fallback_with_poster(monkeypatch):
    ie = _make_ie()
    test_url = 'http://video.udn.com/embed/news/300042'
    page = (
        "<html><script>var options = {\"video\": {\"mp4\": \"/api/fallback.mp4\"}, "
        "title:'Fallback Title', "
        "poster:'http://example.com/fallback.jpg', foo:1} + BROKEN;</script></html>"
    )

    def fake_dl(url, video_id, *args, **kwargs):
        assert video_id == '300042'
        if url == test_url:
            return page
        assert 'api/fallback.mp4' in url
        return 'http://cdn.example.com/clip_480p_1000.mp4'

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(test_url)
    assert result['id'] == '300042'
    assert result['title'] == 'Fallback Title'
    assert result['thumbnail'] == 'http://example.com/fallback.jpg'
    formats = result['formats']
    assert len(formats) == 1
    f = formats[0]
    assert f['url'] == 'http://cdn.example.com/clip_480p_1000.mp4'
    assert f['format_id'] == 'http-mp4'
    assert f['height'] == 480
    assert f['tbr'] == 1000


def test_udn_fallback_no_poster_plain_mp4(monkeypatch):
    ie = _make_ie()
    test_url = 'https://video.udn.com/play/news/303776'
    page = (
        "<html><script>var options = {\"video\": {\"mp4\": \"/api/noposter.mp4\"}, "
        "title:'NoPoster Title', dummy:1} + BROKEN;</script></html>"
    )

    def fake_dl(url, video_id, *args, **kwargs):
        assert video_id == '303776'
        if url == test_url:
            return page
        assert 'api/noposter.mp4' in url
        return 'http://cdn.example.com/noposter.mp4'

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(test_url)
    assert result['id'] == '303776'
    assert result['title'] == 'NoPoster Title'
    assert result['thumbnail'] is None
    formats = result['formats']
    assert len(formats) == 1
    f = formats[0]
    assert f['url'] == 'http://cdn.example.com/noposter.mp4'
    assert f['format_id'] == 'http-mp4'
    assert 'height' not in f
    assert 'tbr' not in f


def test_udn_fallback_youtube(monkeypatch):
    ie = _make_ie()
    test_url = 'http://video.udn.com/embed/news/300043'
    yt_url = 'https://www.youtube.com/watch?v=abc123XYZ'
    page = (
        "<html><script>var options = {\"video\": {\"youtube\": \"%s\"}, "
        "title:'YT Fallback', "
        "poster:'http://example.com/p.jpg', foo:1} + BROKEN;</script></html>" % yt_url
    )

    def fake_dl(url, video_id, *args, **kwargs):
        assert video_id == '300043'
        assert url == test_url
        return page

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(test_url)
    assert result['_type'] == 'url'
    assert result['url'] == yt_url
    assert result['ie_key'] == 'Youtube'
