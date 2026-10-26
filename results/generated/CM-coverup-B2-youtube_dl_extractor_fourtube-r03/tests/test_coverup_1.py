# file: project/youtube_dl/extractor/fourtube.py:43-114
# asked: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}
# gained: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}

import re
from youtube_dl import YoutubeDL
from youtube_dl.extractor.fourtube import FourTubeBaseIE
from youtube_dl.utils import parse_iso8601


class _TestFourTubeIE(FourTubeBaseIE):
    _VALID_URL = r'(?P<kind>v|m)/(?P<id>\d+)(?:/(?P<display_id>[^/]+))?'
    _URL_TEMPLATE = 'http://example.com/videos/%s'


_DIRECT_WEBPAGE = """<html><head>
<meta itemprop="name" content="Test Title">
<meta itemprop="uploadDate" content="2020-01-02T03:04:05+00:00">
<meta itemprop="thumbnailUrl" content="http://example.com/thumb.jpg">
<meta itemprop="interactionCount" content="UserPlays:1,234">
<meta itemprop="interactionCount" content="UserLikes:56">
<meta itemprop="duration" content="PT2M10S">
</head><body>
<a class="item-to-subscribe" href="http://example.com/channel/uploader123" title="Go to MyUploader page">sub</a>
<span><i class="icon icon-tag"></i> Categories / Tags <ul class="my list"><li><a href="/c1">Cat One</a></li><li><a href="/c2">Cat Two</a></li></ul></span>
<button data-id="9999" data-quality="720p">720p</button>
<button data-id="9999" data-quality="480p">480p</button>
</body></html>"""

_FALLBACK_WEBPAGE = """<html><head>
<meta itemprop="name" content="Fallback Title">
<meta itemprop="uploadDate" content="2021-05-06T00:00:00+00:00">
<meta itemprop="thumbnailUrl" content="http://example.com/thumb2.jpg">
<meta itemprop="interactionCount" content="UserPlays:9,999">
<meta itemprop="interactionCount" content="UserLikes:11">
<meta itemprop="duration" content="01:23">
</head><body>
<script id="playerembed" src="http://example.com/player.js"></script>
</body></html>"""

_PLAYER_JS = "xxx $.ajax(url, opts); } })(777, [0], [720, 480]) yyy"


def _make_ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True, 'no_color': True})
    ie = _TestFourTubeIE()
    ie.set_downloader(ydl)
    return ie


def test_direct_media_buttons_no_player_js(monkeypatch):
    ie = _make_ie()
    captured = {}

    def fake_download(self, url, video_id, *args, **kwargs):
        captured['url'] = url
        captured['video_id'] = video_id
        return _DIRECT_WEBPAGE

    def fake_formats(self, url, video_id, media_id, sources):
        captured['formats_url'] = url
        captured['media_id'] = media_id
        captured['sources'] = sources
        return [{'url': 'http://example.com/v.mp4', 'format_id': '720p'}]

    monkeypatch.setattr(_TestFourTubeIE, '_download_webpage', fake_download)
    monkeypatch.setattr(_TestFourTubeIE, '_extract_formats', fake_formats)

    orig_url = 'v/1234/some-display'
    result = ie._real_extract(orig_url)

    assert captured['url'] == orig_url
    assert captured['video_id'] == '1234'
    assert captured['media_id'] == '9999'
    assert captured['sources'] == ['720p', '480p']
    assert captured['formats_url'] == orig_url
    assert result['id'] == '1234'
    assert result['title'] == 'Test Title'
    assert result['thumbnail'] == 'http://example.com/thumb.jpg'
    assert result['uploader'] == 'MyUploader'
    assert result['uploader_id'] == 'uploader123'
    assert result['timestamp'] == parse_iso8601('2020-01-02T03:04:05+00:00')
    assert result['view_count'] == 1234
    assert result['like_count'] == 56
    assert result['duration'] == 130
    assert result['categories'] == ['Cat One', 'Cat Two']
    assert result['formats'] == [{'url': 'http://example.com/v.mp4', 'format_id': '720p'}]
    assert result['age_limit'] == 18


def test_kind_m_rewrites_url_and_uses_player_js(monkeypatch):
    ie = _make_ie()
    captured = {}
    calls = []

    def fake_download(self, url, video_id, *args, **kwargs):
        calls.append(url)
        if url == 'http://example.com/player.js':
            return _PLAYER_JS
        captured['webpage_url'] = url
        captured['video_id'] = video_id
        return _FALLBACK_WEBPAGE

    def fake_formats(self, url, video_id, media_id, sources):
        captured['formats_url'] = url
        captured['media_id'] = media_id
        captured['sources'] = sources
        return [{'url': 'http://example.com/f.mp4'}]

    monkeypatch.setattr(_TestFourTubeIE, '_download_webpage', fake_download)
    monkeypatch.setattr(_TestFourTubeIE, '_extract_formats', fake_formats)

    result = ie._real_extract('m/5555/some-display')

    assert captured['webpage_url'] == 'http://example.com/videos/5555'
    assert captured['video_id'] == '5555'
    assert 'http://example.com/player.js' in calls
    assert captured['media_id'] == 777
    assert captured['sources'] == ['720', '480']
    assert captured['formats_url'] == 'http://example.com/videos/5555'
    assert result['id'] == '5555'
    assert result['title'] == 'Fallback Title'
    assert result['thumbnail'] == 'http://example.com/thumb2.jpg'
    assert result['uploader'] is None
    assert result['uploader_id'] is None
    assert result['categories'] is None
    assert result['timestamp'] == parse_iso8601('2021-05-06T00:00:00+00:00')
    assert result['view_count'] == 9999
    assert result['like_count'] == 11
    assert result['duration'] == 83
    assert result['age_limit'] == 18
    assert result['formats'] == [{'url': 'http://example.com/f.mp4'}]


def test_no_display_id_rewrites_url_direct(monkeypatch):
    ie = _make_ie()
    captured = {}

    def fake_download(self, url, video_id, *args, **kwargs):
        captured['url'] = url
        captured['video_id'] = video_id
        return _DIRECT_WEBPAGE

    def fake_formats(self, url, video_id, media_id, sources):
        captured['media_id'] = media_id
        captured['sources'] = sources
        return [{'url': 'http://example.com/g.mp4'}]

    monkeypatch.setattr(_TestFourTubeIE, '_download_webpage', fake_download)
    monkeypatch.setattr(_TestFourTubeIE, '_extract_formats', fake_formats)

    result = ie._real_extract('v/9999')

    assert captured['url'] == 'http://example.com/videos/9999'
    assert captured['video_id'] == '9999'
    assert captured['media_id'] == '9999'
    assert result['id'] == '9999'
    assert result['title'] == 'Test Title'
    assert result['categories'] == ['Cat One', 'Cat Two']
    assert result['age_limit'] == 18
