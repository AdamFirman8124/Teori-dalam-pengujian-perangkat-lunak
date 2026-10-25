# file: project/youtube_dl/extractor/udn.py:41-102
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}

from youtube_dl import YoutubeDL
from youtube_dl.extractor.udn import UDNEmbedIE


def _make_ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True})
    ie = UDNEmbedIE(ydl)
    return ie


def test_udn_options_direct_youtube(monkeypatch):
    ie = _make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    page = (
        '<html><script>'
        'var options = {"video": {"youtube": "https://www.youtube.com/watch?v=BaW_jenozKc"}, '
        '"title": "YT Title", "poster": "http://example.com/p.jpg"};'
        '</script></html>'
    )
    monkeypatch.setattr(ie, '_download_webpage', lambda *a, **k: page)
    result = ie._real_extract(url)
    assert result['_type'] == 'url'
    assert result['url'] == 'https://www.youtube.com/watch?v=BaW_jenozKc'
    assert result['ie_key'] == 'Youtube'


def test_udn_options_direct_mixed_formats(monkeypatch):
    ie = _make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    page = (
        '<html><script>'
        'var options = {"video": {'
        '"empty": "", '
        '"hls": "/api/hls", '
        '"hds": "/api/hds", '
        '"mp4_high": "http://example.com/video_720p_1000.mp4", '
        '"mp4_low": "http://example.com/video_low.mp4"}, '
        '"title": "Mixed Title", "poster": "http://example.com/poster.jpg"};'
        '</script></html>'
    )

    def fake_download(url_or_request, video_id, note=None, errnote=None, fatal=True, **kwargs):
        s = url_or_request if isinstance(url_or_request, str) else url_or_request.get_full_url()
        if 'embed/news' in s or 'play/news' in s:
            return page
        if 'hls' in s:
            return 'http://example.com/stream.m3u8'
        if 'hds' in s:
            return 'http://example.com/stream.f4m'
        return s

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    monkeypatch.setattr(
        ie, '_extract_m3u8_formats',
        lambda m3u8_url, video_id, ext='mp4', m3u8_id='hls', **k: [
            {'url': m3u8_url, 'format_id': m3u8_id, 'ext': ext}]
    )
    monkeypatch.setattr(
        ie, '_extract_f4m_formats',
        lambda f4m_url, video_id, f4m_id='hds', **k: [
            {'url': f4m_url, 'format_id': f4m_id, 'ext': 'flv'}]
    )
    result = ie._real_extract(url)
    assert result['id'] == '300040'
    assert result['title'] == 'Mixed Title'
    assert result['thumbnail'] == 'http://example.com/poster.jpg'
    formats = result['formats']
    assert isinstance(formats, list)
    assert len(formats) == 4
    urls = [f['url'] for f in formats]
    assert 'http://example.com/stream.m3u8' in urls
    assert 'http://example.com/stream.f4m' in urls
    assert 'http://example.com/video_720p_1000.mp4' in urls
    assert 'http://example.com/video_low.mp4' in urls
    high = next(f for f in formats if f['url'] == 'http://example.com/video_720p_1000.mp4')
    assert high['format_id'] == 'http-mp4_high'
    assert high['height'] == 720
    assert high['tbr'] == 1000
    low = next(f for f in formats if f['url'] == 'http://example.com/video_low.mp4')
    assert low['format_id'] == 'http-mp4_low'
    assert 'height' not in low
    assert 'tbr' not in low


def test_udn_fallback_branch_with_poster(monkeypatch):
    ie = _make_ie()
    url = 'https://video.udn.com/play/news/303776'
    page = (
        '<html><script>'
        'var options = {"video": {"mp4": \'/api/mp4fallback\'}, '
        'title: \'Fallback Title\', '
        'poster: \'http://example.com/fb.jpg\',} INVALID;'
        '</script></html>'
    )

    def fake_download(url_or_request, video_id, note=None, errnote=None, fatal=True, **kwargs):
        s = url_or_request if isinstance(url_or_request, str) else url_or_request.get_full_url()
        if 'play/news' in s or 'embed/news' in s:
            return page
        if 'mp4fallback' in s:
            return 'http://example.com/fb_480p_500.mp4'
        return s

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    result = ie._real_extract(url)
    assert result['id'] == '303776'
    assert result['title'] == 'Fallback Title'
    assert result['thumbnail'] == 'http://example.com/fb.jpg'
    assert len(result['formats']) == 1
    fmt = result['formats'][0]
    assert fmt['url'] == 'http://example.com/fb_480p_500.mp4'
    assert fmt['format_id'] == 'http-mp4'
    assert fmt['height'] == 480
    assert fmt['tbr'] == 500


def test_udn_fallback_branch_without_poster(monkeypatch):
    ie = _make_ie()
    url = 'https://video.udn.com/embed/news/300040'
    page = (
        '<html><script>'
        'var options = {"video": {"mp4": \'/api/mp4noposter\'}, '
        'title: \'No Poster Title\', } INVALID;'
        '</script></html>'
    )

    def fake_download(url_or_request, video_id, note=None, errnote=None, fatal=True, **kwargs):
        s = url_or_request if isinstance(url_or_request, str) else url_or_request.get_full_url()
        if 'embed/news' in s or 'play/news' in s:
            return page
        if 'mp4noposter' in s:
            return 'http://example.com/noposter.mp4'
        return s

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    result = ie._real_extract(url)
    assert result['id'] == '300040'
    assert result['title'] == 'No Poster Title'
    assert result['thumbnail'] is None
    assert len(result['formats']) == 1
    fmt = result['formats'][0]
    assert fmt['url'] == 'http://example.com/noposter.mp4'
    assert fmt['format_id'] == 'http-mp4'
    assert 'height' not in fmt
    assert 'tbr' not in fmt
