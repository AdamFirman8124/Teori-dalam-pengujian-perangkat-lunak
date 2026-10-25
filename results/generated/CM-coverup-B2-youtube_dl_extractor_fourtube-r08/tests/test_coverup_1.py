# file: project/youtube_dl/extractor/fourtube.py:43-114
# asked: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}
# gained: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}

import calendar

import pytest

from youtube_dl import YoutubeDL
from youtube_dl.extractor.fourtube import FourTubeIE

VIDEO_ID = '209733'

FULL_WEBPAGE = """<html>
<head>
<title>Test</title>
<meta name="name" content="Hot Babe Test Video">
<meta name="uploadDate" content="2013-10-31T21:18:12Z">
<meta name="thumbnailUrl" content="https://img.example.com/thumb.jpg">
<meta name="duration" content="09:43">
<meta itemprop="interactionCount" content="UserPlays:1,234">
<meta itemprop="interactionCount" content="UserLikes:56">
</head>
<body>
<a class="item-to-subscribe" href="https://www.4tube.com/users/wcp-club" title="Go to WCP Club page">Subscribe</a>
<span><i class="icon icon-tag"></i> Categories / Tags
<ul class="list inline">
<li><a href="/tags/one"> Category One </a></li>
<li><a href="/tags/two">Category Two</a></li>
</ul>
</span>
<button data-id="209733" data-quality="360">360p</button>
<button data-id="209733" data-quality="720">720p</button>
</body>
</html>"""

FALLBACK_WEBPAGE = """<html>
<head>
<meta name="name" content="Fallback Video">
<meta name="uploadDate" content="2015-06-06T12:34:56Z">
<meta name="thumbnailUrl" content="https://img.example.com/fallback.jpg">
<meta name="duration" content="1:24:12">
</head>
<body>
<script id='playerembed' src='https://www.4tube.com/static/player.js'></script>
</body>
</html>"""

PLAYER_JS = """
var config = {};
$.ajax(url, opts);
    }
})(209733, 0, [360, 720]);
"""


def _make_ie(monkeypatch, webpage, player_js=None):
    ie = FourTubeIE(YoutubeDL({
        'quiet': True,
        'no_warnings': True,
        'no_color': True,
    }))
    downloaded = []

    def fake_download_webpage(url, video_id, *args, **kwargs):
        downloaded.append((url, video_id))
        if player_js is not None and len(downloaded) > 1:
            return player_js
        return webpage

    format_calls = []

    def fake_extract_formats(url, video_id, media_id, sources):
        format_calls.append((url, video_id, media_id, list(sources)))
        return [{'format_id': 'test-format', 'url': 'https://example.com/fake.mp4'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)
    return ie, downloaded, format_calls


def test_real_extract_full_webpage(monkeypatch):
    url = 'https://www.4tube.com/videos/209733/hot-babe-test-video'
    ie, downloaded, format_calls = _make_ie(monkeypatch, FULL_WEBPAGE)

    info = ie._real_extract(url)

    assert downloaded == [(url, VIDEO_ID)]
    assert format_calls == [(url, VIDEO_ID, '209733', ['360', '720'])]
    assert info['id'] == VIDEO_ID
    assert info['title'] == 'Hot Babe Test Video'
    assert info['timestamp'] == calendar.timegm((2013, 10, 31, 21, 18, 12, 0, 0, 0))
    assert info['thumbnail'] == 'https://img.example.com/thumb.jpg'
    assert info['uploader'] == 'WCP Club'
    assert info['uploader_id'] == 'wcp-club'
    assert info['categories'] == ['Category One', 'Category Two']
    assert info['view_count'] == 1234
    assert info['like_count'] == 56
    assert info['duration'] == 583
    assert info['age_limit'] == 18
    assert info['formats'] == [{'format_id': 'test-format',
                                'url': 'https://example.com/fake.mp4'}]


@pytest.mark.parametrize('url,expected_page_url', [
    ('https://www.4tube.com/embed/209733',
     'https://www.4tube.com/videos/209733/video'),
    ('https://m.4tube.com/videos/209733/some-slug',
     'https://www.4tube.com/videos/209733/video'),
])
def test_real_extract_rewrites_url(monkeypatch, url, expected_page_url):
    ie, downloaded, format_calls = _make_ie(monkeypatch, FULL_WEBPAGE)

    info = ie._real_extract(url)

    assert downloaded[0][0] == expected_page_url
    assert downloaded[0][1] == VIDEO_ID
    assert format_calls[0][0] == expected_page_url
    assert info['id'] == VIDEO_ID
    assert info['title'] == 'Hot Babe Test Video'
    assert info['age_limit'] == 18


def test_real_extract_player_js_fallback(monkeypatch):
    url = 'https://www.4tube.com/videos/209733/no-buttons'
    ie, downloaded, format_calls = _make_ie(
        monkeypatch, FALLBACK_WEBPAGE, player_js=PLAYER_JS)

    info = ie._real_extract(url)

    assert downloaded == [(url, VIDEO_ID),
                          ('https://www.4tube.com/static/player.js', VIDEO_ID)]
    assert format_calls == [(url, VIDEO_ID, 209733, ['360', '720'])]
    assert info['id'] == VIDEO_ID
    assert info['title'] == 'Fallback Video'
    assert info['timestamp'] == calendar.timegm((2015, 6, 6, 12, 34, 56, 0, 0, 0))
    assert info['thumbnail'] == 'https://img.example.com/fallback.jpg'
    assert info['duration'] == 5052
    assert info['categories'] is None
    assert info['uploader'] is None
    assert info['uploader_id'] is None
    assert info['view_count'] is None
    assert info['like_count'] is None
    assert info['age_limit'] == 18
    assert info['formats'] == [{'format_id': 'test-format',
                                'url': 'https://example.com/fake.mp4'}]
