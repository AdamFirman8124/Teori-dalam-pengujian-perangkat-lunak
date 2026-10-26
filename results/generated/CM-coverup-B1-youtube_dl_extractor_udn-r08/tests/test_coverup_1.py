# file: project/youtube_dl/extractor/udn.py:41-102
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}

from youtube_dl import YoutubeDL
from youtube_dl.extractor.udn import UDNEmbedIE


def _make_ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True, 'no_color': True})
    return UDNEmbedIE(ydl)


def test_udn_youtube_branch(monkeypatch):
    ie = _make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    fake_page = (
        '<html><script>var options = {"video": '
        '{"youtube": "https://www.youtube.com/watch?v=abc123"}, '
        '"title": "Test Title", '
        '"poster": "http://example.com/poster.jpg"};</script></html>'
    )

    def fake_dl(url_arg, video_id, *args, **kwargs):
        assert video_id == '300040'
        return fake_page

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(url)
    assert result['_type'] == 'url'
    assert result['url'] == 'https://www.youtube.com/watch?v=abc123'
    assert result['ie_key'] == 'Youtube'


def test_udn_all_formats_branches(monkeypatch):
    ie = _make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    fake_page = (
        '<html><script>var options = {"video": '
        '{"empty": "", "hls": "/hls_api", "hds": "/hds_api", '
        '"mp4_high": "/api/video_720p_1000.mp4", '
        '"mp4_plain": "/api/video.mp4"}, '
        '"title": "Multi Title", '
        '"poster": "http://example.com/poster.jpg"};</script></html>'
    )

    def fake_dl(url_arg, video_id, *args, **kwargs):
        note = kwargs.get('note', '')
        if 'retrieve url' in note:
            if url_arg.endswith('/hls_api'):
                return 'http://example.com/video.m3u8'
            if url_arg.endswith('/hds_api'):
                return 'http://example.com/video.f4m'
            if '720p' in url_arg:
                return 'http://example.com/video_720p_1000.mp4'
            return 'http://example.com/video.mp4'
        return fake_page

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    monkeypatch.setattr(
        ie, '_extract_m3u8_formats',
        lambda url_arg, video_id, *a, **k: [{'url': url_arg, 'format_id': k.get('m3u8_id', 'hls'), 'ext': 'mp4'}])
    monkeypatch.setattr(
        ie, '_extract_f4m_formats',
        lambda url_arg, video_id, *a, **k: [{'url': url_arg, 'format_id': k.get('f4m_id', 'hds'), 'ext': 'flv'}])

    result = ie._real_extract(url)
    assert result['id'] == '300040'
    assert result['title'] == 'Multi Title'
    assert result['thumbnail'] == 'http://example.com/poster.jpg'
    formats = result['formats']
    # empty entry skipped: hls(1) + hds(1) + 2 mp4 = 4
    assert len(formats) == 4
    urls = [f['url'] for f in formats]
    assert 'http://example.com/video.m3u8' in urls
    assert 'http://example.com/video.f4m' in urls
    assert 'http://example.com/video_720p_1000.mp4' in urls
    assert 'http://example.com/video.mp4' in urls
    high = next(f for f in formats if f['url'] == 'http://example.com/video_720p_1000.mp4')
    assert high['format_id'] == 'http-mp4_high'
    assert high['height'] == 720
    assert high['tbr'] == 1000
    plain = next(f for f in formats if f['url'] == 'http://example.com/video.mp4')
    assert plain['format_id'] == 'http-mp4_plain'
    assert 'height' not in plain
    assert 'tbr' not in plain


def test_udn_fallback_with_poster(monkeypatch):
    ie = _make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    page = (
        '<html><script>var options = {"video": {"mp4": "/api/fb.mp4"}, '
        "title: 'Fallback Title', "
        "poster: 'http://example.com/fb.jpg',};</script></html>"
    )
    orig_parse = ie._parse_json

    def fake_parse(s, name, *args, **kwargs):
        if name == 'options':
            return None
        return orig_parse(s, name, *args, **kwargs)

    monkeypatch.setattr(ie, '_parse_json', fake_parse)

    def fake_dl(url_arg, video_id, *args, **kwargs):
        if kwargs.get('note', '').startswith('retrieve url'):
            return 'http://example.com/fb_video_480p_500.mp4'
        return page

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(url)
    assert result['id'] == '300040'
    assert result['title'] == 'Fallback Title'
    assert result['thumbnail'] == 'http://example.com/fb.jpg'
    assert len(result['formats']) == 1
    fmt = result['formats'][0]
    assert fmt['url'] == 'http://example.com/fb_video_480p_500.mp4'
    assert fmt['format_id'] == 'http-mp4'
    assert fmt['height'] == 480
    assert fmt['tbr'] == 500


def test_udn_fallback_without_poster(monkeypatch):
    ie = _make_ie()
    url = 'https://video.udn.com/play/news/303776'
    page = (
        '<html><script>var options = {"video": {"mp4": "/api/fb2.mp4"}, '
        "title: 'No Poster Title',};</script></html>"
    )
    orig_parse = ie._parse_json

    def fake_parse(s, name, *args, **kwargs):
        if name == 'options':
            return None
        return orig_parse(s, name, *args, **kwargs)

    monkeypatch.setattr(ie, '_parse_json', fake_parse)

    def fake_dl(url_arg, video_id, *args, **kwargs):
        if kwargs.get('note', '').startswith('retrieve url'):
            return 'http://example.com/plain.mp4'
        return page

    monkeypatch.setattr(ie, '_download_webpage', fake_dl)
    result = ie._real_extract(url)
    assert result['id'] == '303776'
    assert result['title'] == 'No Poster Title'
    assert result['thumbnail'] is None
    assert len(result['formats']) == 1
    fmt = result['formats'][0]
    assert fmt['url'] == 'http://example.com/plain.mp4'
    assert fmt['format_id'] == 'http-mp4'
    assert 'height' not in fmt
    assert 'tbr' not in fmt
