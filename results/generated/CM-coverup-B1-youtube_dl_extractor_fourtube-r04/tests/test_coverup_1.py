# file: project/youtube_dl/extractor/fourtube.py:43-114
# asked: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}
# gained: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}

import pytest
from youtube_dl import YoutubeDL
from youtube_dl.extractor.fourtube import FourTubeBaseIE
from youtube_dl.utils import parse_iso8601


class _TestFourTubeIE(FourTubeBaseIE):
    _VALID_URL = r'https?://(?:www\.)?example\.com/(?P<kind>[a-z])/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    _URL_TEMPLATE = 'https://example.com/m/%s'
    IE_NAME = 'TestFourTube'


WEBPAGE_DIRECT = """<html><head>
<meta itemprop="name" content="Test Title Direct">
<meta itemprop="uploadDate" content="2019-01-02T03:04:05+00:00">
<meta itemprop="thumbnailUrl" content="https://example.com/thumb.jpg">
<meta itemprop="duration" content="5:30">
<meta itemprop="interactionCount" content="UserPlays:1,234">
<meta itemprop="interactionCount" content="UserLikes:56">
</head><body>
<a class="item-to-subscribe" href="https://example.com/channels/uploader123" title="Go to Test Uploader page">x</a>
<span><i class="icon icon-tag"></i> Categories / Tags <div><ul class="foo list bar"><li><a href="/c1">Cat One</a></li><li><a href="/c2">Cat Two</a></li></ul></div></span>
<button data-id="99999" data-quality="720p">720</button>
<button data-id="99999" data-quality="480p">480</button>
</body></html>"""

WEBPAGE_NO_CATS = """<html><head>
<meta itemprop="name" content="No Cats Title">
<meta itemprop="uploadDate" content="2019-01-02T03:04:05+00:00">
<meta itemprop="thumbnailUrl" content="https://example.com/thumb2.jpg">
<meta itemprop="duration" content="5:30">
<meta itemprop="interactionCount" content="UserPlays:2,000">
<meta itemprop="interactionCount" content="UserLikes:10">
</head><body>
<a class="item-to-subscribe" href="https://example.com/channels/uploader123" title="Go to Test Uploader page">x</a>
<button data-id="88888" data-quality="720p">720</button>
</body></html>"""

WEBPAGE_FALLBACK = """<html><head>
<meta itemprop="name" content="Fallback Title">
<meta itemprop="uploadDate" content="2019-01-02T03:04:05+00:00">
<meta itemprop="thumbnailUrl" content="https://example.com/thumb3.jpg">
<meta itemprop="duration" content="5:30">
<meta itemprop="interactionCount" content="UserPlays:3,000">
<meta itemprop="interactionCount" content="UserLikes:20">
</head><body>
<a class="item-to-subscribe" href="https://example.com/channels/uploader123" title="Go to Test Uploader page">x</a>
<span><i class="icon icon-tag"></i> Categories / Tags <div><ul class="x list y"><li><a href="/c1">Cat One</a></li></ul></div></span>
<script id="playerembed" src="https://example.com/player.js"></script>
</body></html>"""

WEBPAGE_QUALITY_ONLY = """<html><head>
<meta itemprop="name" content="Quality Only Title">
<meta itemprop="uploadDate" content="2019-01-02T03:04:05+00:00">
<meta itemprop="thumbnailUrl" content="https://example.com/thumb4.jpg">
<meta itemprop="duration" content="5:30">
<meta itemprop="interactionCount" content="UserPlays:4,000">
<meta itemprop="interactionCount" content="UserLikes:30">
</head><body>
<a class="item-to-subscribe" href="https://example.com/channels/uploader123" title="Go to Test Uploader page">x</a>
<button data-quality="720p">720</button>
<script id="playerembed" src="https://example.com/player.js"></script>
</body></html>"""

PLAYER_JS = "var a=1; $.ajax(url, opts);} })(12345, [0], [720, 480])"


def _make_ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True, 'no_color': True})
    return _TestFourTubeIE(ydl)


def test_direct_kind_m_rewrite_with_categories(monkeypatch):
    ie = _make_ie()
    calls = []
    captured = {}

    def fake_download(self, url, video_id, *args, **kwargs):
        calls.append((url, video_id))
        return WEBPAGE_DIRECT

    def fake_formats(self, url, video_id, media_id, sources):
        captured['url'] = url
        captured['video_id'] = video_id
        captured['media_id'] = media_id
        captured['sources'] = sources
        return [{'url': 'https://example.com/v.mp4', 'format_id': '720p'}]

    monkeypatch.setattr(_TestFourTubeIE, '_download_webpage', fake_download)
    monkeypatch.setattr(_TestFourTubeIE, '_extract_formats', fake_formats)

    res = ie._real_extract('https://example.com/m/99999/some-title')

    assert calls == [('https://example.com/m/99999', '99999')]
    assert captured['media_id'] == '99999'
    assert captured['sources'] == ['720p', '480p']
    assert captured['url'] == 'https://example.com/m/99999'
    assert captured['video_id'] == '99999'
    assert res['id'] == '99999'
    assert res['title'] == 'Test Title Direct'
    assert res['formats'] == [{'url': 'https://example.com/v.mp4', 'format_id': '720p'}]
    assert res['categories'] == ['Cat One', 'Cat Two']
    assert res['thumbnail'] == 'https://example.com/thumb.jpg'
    assert res['uploader'] == 'Test Uploader'
    assert res['uploader_id'] == 'uploader123'
    assert res['timestamp'] == parse_iso8601('2019-01-02T03:04:05+00:00')
    assert res['view_count'] == 1234
    assert res['like_count'] == 56
    assert res['duration'] == 330
    assert res['age_limit'] == 18


def test_direct_no_display_id_rewrite_no_categories(monkeypatch):
    ie = _make_ie()
    calls = []
    captured = {}

    def fake_download(self, url, video_id, *args, **kwargs):
        calls.append((url, video_id))
        return WEBPAGE_NO_CATS

    def fake_formats(self, url, video_id, media_id, sources):
        captured['media_id'] = media_id
        captured['sources'] = sources
        captured['url'] = url
        return [{'url': 'https://example.com/v2.mp4'}]

    monkeypatch.setattr(_TestFourTubeIE, '_download_webpage', fake_download)
    monkeypatch.setattr(_TestFourTubeIE, '_extract_formats', fake_formats)

    res = ie._real_extract('https://example.com/v/88888')

    assert calls == [('https://example.com/m/88888', '88888')]
    assert captured['media_id'] == '88888'
    assert captured['sources'] == ['720p']
    assert res['id'] == '88888'
    assert res['title'] == 'No Cats Title'
    assert res['categories'] is None
    assert res['thumbnail'] == 'https://example.com/thumb2.jpg'
    assert res['uploader'] == 'Test Uploader'
    assert res['uploader_id'] == 'uploader123'
    assert res['timestamp'] == parse_iso8601('2019-01-02T03:04:05+00:00')
    assert res['view_count'] == 2000
    assert res['like_count'] == 10
    assert res['duration'] == 330
    assert res['age_limit'] == 18


def test_fallback_no_buttons_uses_player_js(monkeypatch):
    ie = _make_ie()
    calls = []
    captured = {}

    def fake_download(self, url, video_id, *args, **kwargs):
        calls.append((url, video_id))
        if 'player.js' in url:
            return PLAYER_JS
        return WEBPAGE_FALLBACK

    def fake_formats(self, url, video_id, media_id, sources):
        captured['media_id'] = media_id
        captured['sources'] = sources
        captured['url'] = url
        return [{'url': 'https://example.com/fb.mp4'}]

    monkeypatch.setattr(_TestFourTubeIE, '_download_webpage', fake_download)
    monkeypatch.setattr(_TestFourTubeIE, '_extract_formats', fake_formats)

    res = ie._real_extract('https://example.com/v/77777/my-video')

    assert len(calls) == 2
    assert calls[0] == ('https://example.com/v/77777/my-video', '77777')
    assert calls[1][0] == 'https://example.com/player.js'
    assert calls[1][1] == '77777'
    assert captured['media_id'] == 12345
    assert captured['sources'] == ['720', '480']
    assert res['id'] == '77777'
    assert res['title'] == 'Fallback Title'
    assert res['categories'] == ['Cat One']
    assert res['thumbnail'] == 'https://example.com/thumb3.jpg'
    assert res['view_count'] == 3000
    assert res['like_count'] == 20
    assert res['duration'] == 330
    assert res['timestamp'] == parse_iso8601('2019-01-02T03:04:05+00:00')
    assert res['age_limit'] == 18


def test_fallback_media_id_missing_but_sources_present(monkeypatch):
    ie = _make_ie()
    calls = []
    captured = {}

    def fake_download(self, url, video_id, *args, **kwargs):
        calls.append((url, video_id))
        if 'player.js' in url:
            return PLAYER_JS
        return WEBPAGE_QUALITY_ONLY

    def fake_formats(self, url, video_id, media_id, sources):
        captured['media_id'] = media_id
        captured['sources'] = sources
        return [{'url': 'https://example.com/q.mp4'}]

    monkeypatch.setattr(_TestFourTubeIE, '_download_webpage', fake_download)
    monkeypatch.setattr(_TestFourTubeIE, '_extract_formats', fake_formats)

    res = ie._real_extract('https://example.com/v/66666/other-title')

    assert len(calls) == 2
    assert calls[0] == ('https://example.com/v/66666/other-title', '66666')
    assert captured['media_id'] == 12345
    assert captured['sources'] == ['720', '480']
    assert res['id'] == '66666'
    assert res['title'] == 'Quality Only Title'
    assert res['categories'] is None
    assert res['view_count'] == 4000
    assert res['like_count'] == 30
    assert res['uploader'] == 'Test Uploader'
    assert res['uploader_id'] == 'uploader123'
    assert res['age_limit'] == 18
    assert res['duration'] == 330
