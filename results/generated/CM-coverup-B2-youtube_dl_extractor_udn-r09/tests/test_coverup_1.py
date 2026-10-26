# file: project/youtube_dl/extractor/udn.py:41-102
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}

import pytest

from youtube_dl.extractor.udn import UDNEmbedIE


class FakeYDL(object):
    def __init__(self):
        self.params = {}
        self.warnings = []

    def report_warning(self, msg):
        self.warnings.append(msg)

    def to_screen(self, msg):
        pass


def _make_ie(monkeypatch, pages):
    """Build a UDNEmbedIE whose _download_webpage serves canned pages.

    ``pages`` maps URL -> response body; unknown URLs return ''.
    Returns (ie, calls) where calls records every requested URL.
    """
    ie = UDNEmbedIE()
    ie.set_downloader(FakeYDL())
    calls = []

    def fake_download_webpage(self, url_or_request, video_id, *args, **kwargs):
        url = url_or_request if isinstance(url_or_request, str) else str(url_or_request)
        calls.append(url)
        return pages.get(url, '')

    monkeypatch.setattr(UDNEmbedIE, '_download_webpage', fake_download_webpage)
    return ie, calls


def _embed_page(options_js):
    return '<html><script>var options = %s;</script></html>' % options_js


def _fallback_page(title, poster=None, api='/api/fb'):
    """Page whose options string is NOT valid JSON even after js_to_json.

    ``broken: @@@`` survives js_to_json unquoted, so _parse_json fails and
    the regex fallback path (lines 55-60) is taken.  Commas are required by
    the fallback regexes.
    """
    parts = ["title: '%s'" % title]
    if poster is not None:
        parts.append("poster: '%s'" % poster)
    parts.append("video: {'mp4': '%s'}" % api)
    parts.append('broken: @@@')
    return _embed_page('{%s}' % ', '.join(parts))


def test_udn_embed_json_options_mp4_formats(monkeypatch):
    """Lines 50-53, 66-68, 70-74, 82-93, 95-101: JSON options path,
    empty api_url skipped, mp4 with and without _720p_1000.mp4 pattern."""
    page = _embed_page(
        "{'title':'Test Title',"
        "'poster':'http://thumb.example/poster.jpg',"
        "'video':{"
        "'mp4':'/api/720',"
        "'empty':'',"
        "'other':'/api/low'"
        "}}")
    ie, calls = _make_ie(monkeypatch, {
        'http://video.udn.com/embed/news/300040': page,
        'http://video.udn.com/api/720':
            'http://media.example/video_720p_1000.mp4',
        'http://video.udn.com/api/low':
            'http://media.example/video_low.mp4',
    })

    info = ie._real_extract('http://video.udn.com/embed/news/300040')

    assert info['id'] == '300040'
    assert info['title'] == 'Test Title'
    assert info['thumbnail'] == 'http://thumb.example/poster.jpg'
    formats = info['formats']
    assert len(formats) == 2
    by_id = {f['format_id']: f for f in formats}
    assert 'http-mp4' in by_id
    assert 'http-other' in by_id
    assert by_id['http-mp4']['height'] == 720
    assert by_id['http-mp4']['tbr'] == 1000
    assert by_id['http-other'].get('height') is None
    assert by_id['http-other'].get('tbr') is None
    # the empty api_url must not trigger a download
    assert 'http://video.udn.com/api/720' in calls
    assert 'http://video.udn.com/api/low' in calls
    assert not any(c.endswith('/empty') for c in calls)


def test_udn_embed_m3u8_and_f4m(monkeypatch):
    """Lines 75-81: m3u8 and f4m branches dispatch to the format extractors."""
    page = _embed_page(
        "{'title':'Streams',"
        "'video':{"
        "'hls':'/api/hls',"
        "'hds':'/api/hds'"
        "}}")
    ie, calls = _make_ie(monkeypatch, {
        'http://video.udn.com/embed/news/300040': page,
        'http://video.udn.com/api/hls':
            'http://media.example/master.m3u8',
        'http://video.udn.com/api/hds':
            'http://media.example/manifest.f4m',
    })

    m3u8_formats = [{
        'url': 'http://media.example/index_1.m3u8',
        'format_id': 'hls-1',
        'ext': 'mp4',
    }, {
        'url': 'http://media.example/index_2.m3u8',
        'format_id': 'hls-2',
        'ext': 'mp4',
    }]
    f4m_formats = [{
        'url': 'http://media.example/f4m_stream',
        'format_id': 'hds-0',
        'ext': 'flv',
    }]

    def fake_m3u8(self, m3u8_url, video_id, *args, **kwargs):
        assert m3u8_url == 'http://media.example/master.m3u8'
        assert video_id == '300040'
        assert kwargs.get('ext') == 'mp4'
        assert kwargs.get('m3u8_id') == 'hls'
        return list(m3u8_formats)

    def fake_f4m(self, manifest_url, video_id, *args, **kwargs):
        assert manifest_url == 'http://media.example/manifest.f4m'
        assert video_id == '300040'
        assert kwargs.get('f4m_id') == 'hds'
        return list(f4m_formats)

    monkeypatch.setattr(UDNEmbedIE, '_extract_m3u8_formats', fake_m3u8)
    monkeypatch.setattr(UDNEmbedIE, '_extract_f4m_formats', fake_f4m)

    info = ie._real_extract('http://video.udn.com/embed/news/300040')

    assert info['id'] == '300040'
    assert info['title'] == 'Streams'
    assert info['thumbnail'] is None
    assert len(info['formats']) == 3
    assert m3u8_formats[0] in info['formats']
    assert m3u8_formats[1] in info['formats']
    assert f4m_formats[0] in info['formats']


def test_udn_embed_youtube_redirect(monkeypatch):
    """Lines 62-63: youtube key short-circuits with a url_result."""
    page = _embed_page(
        "{'title':'YT',"
        "'video':{'youtube':'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}}")
    ie, calls = _make_ie(monkeypatch, {
        'http://video.udn.com/embed/news/300040': page,
    })

    result = ie._real_extract('http://video.udn.com/embed/news/300040')

    assert result == {
        '_type': 'url',
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'ie_key': 'Youtube',
    }
    # no format resolution downloads happened
    assert calls == ['http://video.udn.com/embed/news/300040']


def test_udn_embed_fallback_regex_path_with_poster(monkeypatch):
    """Lines 55-60: unparseable options fall back to regex extraction
    (poster present)."""
    page = _fallback_page(
        'Fallback Title', poster='http://thumb.example/fb.jpg', api='/api/fb')
    ie, calls = _make_ie(monkeypatch, {
        'http://video.udn.com/embed/news/300040': page,
        'http://video.udn.com/api/fb':
            'http://media.example/fb_360p_500.mp4',
    })

    info = ie._real_extract('http://video.udn.com/embed/news/300040')

    assert info['id'] == '300040'
    assert info['title'] == 'Fallback Title'
    assert info['thumbnail'] == 'http://thumb.example/fb.jpg'
    assert len(info['formats']) == 1
    fmt = info['formats'][0]
    assert fmt['format_id'] == 'http-mp4'
    assert fmt['height'] == 360
    assert fmt['tbr'] == 500
    assert fmt['url'] == 'http://media.example/fb_360p_500.mp4'
    assert 'http://video.udn.com/api/fb' in calls


def test_udn_embed_fallback_regex_path_no_poster(monkeypatch):
    """Lines 55-60 with the poster regex defaulting to None."""
    page = _fallback_page('No Poster', poster=None, api='/api/np')
    ie, calls = _make_ie(monkeypatch, {
        'http://video.udn.com/embed/news/300040': page,
        'http://video.udn.com/api/np':
            'http://media.example/np_480p_800.mp4',
    })

    info = ie._real_extract('http://video.udn.com/embed/news/300040')

    assert info['id'] == '300040'
    assert info['title'] == 'No Poster'
    assert info['thumbnail'] is None
    assert len(info['formats']) == 1
    assert info['formats'][0]['height'] == 480
    assert info['formats'][0]['tbr'] == 800
    assert 'http://video.udn.com/api/np' in calls


def test_udn_embed_fallback_malformed_options(monkeypatch):
    """Lines 55-60: options string is not valid JSON even after
    js_to_json, so the regex fallback path is used."""
    page = _fallback_page(
        'Malformed', poster='http://thumb.example/m.jpg', api='/api/mal')
    ie, calls = _make_ie(monkeypatch, {
        'http://video.udn.com/embed/news/300040': page,
        'http://video.udn.com/api/mal':
            'http://media.example/mal_1080p_2000.mp4',
    })

    info = ie._real_extract('http://video.udn.com/embed/news/300040')

    assert info['id'] == '300040'
    assert info['title'] == 'Malformed'
    assert info['thumbnail'] == 'http://thumb.example/m.jpg'
    assert len(info['formats']) == 1
    assert info['formats'][0]['height'] == 1080
    assert info['formats'][0]['tbr'] == 2000
    assert 'http://video.udn.com/api/mal' in calls
