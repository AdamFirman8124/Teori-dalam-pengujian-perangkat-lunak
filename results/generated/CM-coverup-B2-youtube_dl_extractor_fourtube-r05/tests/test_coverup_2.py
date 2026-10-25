# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from urllib.parse import quote

from youtube_dl.extractor.fourtube import PornTubeIE
from youtube_dl.utils import unified_timestamp


class _FakeYDL(object):
    """Minimal downloader stub: InfoExtractor only needs .params here."""

    def __init__(self):
        self.params = {'no_color': True}

    def report_warning(self, *args, **kwargs):
        pass

    def to_screen(self, *args, **kwargs):
        pass

    def trouble(self, *args, **kwargs):
        pass


def _build_webpage(video):
    """Build a fake porntube webpage whose INITIALSTATE decodes to `video`."""
    state = json.dumps({'page': {'video': video}})
    encoded = base64.b64encode(quote(state).encode('utf-8')).decode('ascii')
    return '<html><script>INITIALSTATE = "%s";</script></html>' % encoded


FULL_VIDEO = {
    'title': 'Test Video',
    'mediaId': '12345',
    'encodings': [{'height': 720}, {'height': 1080}, {'other': 1}],
    'masterThumb': 'https://img.example.com/thumb.jpg',
    'user': {'username': 'someuser', 'id': 42},
    'channel': {'name': 'somechannel', 'id': 7},
    'likes': 10,
    'dislikes': 2,
    'playsQty': 100,
    'durationInSeconds': 60,
    'publishedAt': '2015-06-06T12:00:00+00:00',
}


def _make_ie(monkeypatch, webpage, formats, expected_sources=None):
    ie = PornTubeIE(_FakeYDL())

    def fake_download_webpage(url, video_id, *args, **kwargs):
        assert isinstance(url, str)
        return webpage

    def fake_extract_formats(url, video_id, media_id, sources):
        if expected_sources is not None:
            assert sources == expected_sources
        return formats

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)
    return ie


def test_porntube_full_data(monkeypatch):
    expected_formats = [{'url': 'https://cdn.example.com/720.mp4', 'format_id': '720p'}]
    webpage = _build_webpage(FULL_VIDEO)
    ie = _make_ie(monkeypatch, webpage, expected_formats, expected_sources=['720', '1080'])

    url = 'https://www.porntube.com/videos/test-video_1111111'
    info = ie._real_extract(url)

    assert info['id'] == '1111111'
    assert info['title'] == 'Test Video'
    assert info['formats'] == expected_formats
    assert info['thumbnail'] == 'https://img.example.com/thumb.jpg'
    assert info['uploader'] == 'someuser'
    assert info['uploader_id'] == '42'
    assert info['channel'] == 'somechannel'
    assert info['channel_id'] == '7'
    assert info['like_count'] == 10
    assert info['dislike_count'] == 2
    assert info['view_count'] == 100
    assert info['duration'] == 60
    assert info['age_limit'] == 18
    assert info['timestamp'] == unified_timestamp('2015-06-06T12:00:00+00:00')


def test_porn_tube_fallbacks_and_missing_fields(monkeypatch):
    video = {
        'title': 'Fallback Video',
        'mediaId': '999',
        'encodings': [{'height': 360}, {}],
    }
    webpage = _build_webpage(video)
    ie = _make_ie(monkeypatch, webpage, [], expected_sources=['360'])

    url = 'https://www.porntube.com/videos/fallback_2222222'
    info = ie._real_extract(url)

    assert info['id'] == '2222222'
    assert info['title'] == 'Fallback Video'
    assert info['formats'] == []
    assert info['thumbnail'] is None
    assert info['uploader'] is None
    assert info['uploader_id'] is None
    assert info['channel'] is None
    assert info['channel_id'] is None
    assert info['timestamp'] is None
    assert info['like_count'] is None
    assert info['dislike_count'] is None
    assert info['view_count'] is None
    assert info['duration'] is None
    assert info['age_limit'] == 18


def test_porn_tube_channel_fallback(monkeypatch):
    video = {
        'title': 'Channel Only',
        'mediaId': '1',
        'encodings': [{'height': 480}],
        'channel': {'name': 'channame', 'id': 55},
    }
    webpage = _build_webpage(video)
    ie = _make_ie(monkeypatch, webpage, [], expected_sources=['480'])

    url = 'https://www.porntube.com/videos/channel-only_3333333'
    info = ie._real_extract(url)

    assert info['uploader'] == 'channame'
    assert info['uploader_id'] == '55'
    assert info['channel'] == 'channame'
    assert info['channel_id'] == '55'
    assert info['age_limit'] == 18


def test_porn_tube_embed_url(monkeypatch):
    webpage = _build_webpage(FULL_VIDEO)
    ie = _make_ie(monkeypatch, webpage, [], expected_sources=['720', '1080'])

    url = 'https://www.porntube.com/embed/1111111'
    info = ie._real_extract(url)

    assert info['id'] == '1111111'
    assert info['title'] == 'Test Video'
    assert info['age_limit'] == 18
