# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from types import SimpleNamespace
from urllib.parse import quote

from youtube_dl.extractor.fourtube import PornTubeIE


def _encode_initial_state(video):
    state = json.dumps({"page": {"video": video}})
    quoted_state = quote(state, safe="")
    return base64.b64encode(quoted_state.encode("utf-8")).decode("ascii")


def test_porntube_real_extract_with_uploader(monkeypatch):
    url = "https://www.porntube.com/videos/example-video_12345"
    video = {
        "title": "Example Video",
        "mediaId": "media-123",
        "encodings": [
            {"height": 720},
            {"height": "480"},
            {"height": None},
            {},
            {"height": 0},
        ],
        "masterThumb": "https://cdn.example.com/thumb.jpg",
        "user": {"username": "Uploader", "id": 42},
        "channel": {"name": "Channel", "id": 84},
        "likes": "17",
        "dislikes": "3",
        "playsQty": "1001",
        "durationInSeconds": "125",
        "publishedAt": "2020-01-02T03:04:05Z",
    }
    webpage = 'window.INITIALSTATE = "%s";' % _encode_initial_state(video)

    ie = PornTubeIE(SimpleNamespace(params={"no_color": True}))
    formats = [
        {
            "url": "https://cdn.example.com/video.mp4",
            "format_id": "720p",
        }
    ]
    calls = {}

    def download_webpage(request_url, display_id):
        calls["webpage"] = (request_url, display_id)
        return webpage

    def extract_formats(request_url, video_id, media_id, sources):
        calls["formats"] = (request_url, video_id, media_id, sources)
        return formats

    monkeypatch.setattr(ie, "_download_webpage", download_webpage)
    monkeypatch.setattr(ie, "_extract_formats", extract_formats)

    result = ie._real_extract(url)

    assert calls == {
        "webpage": (url, "example-video"),
        "formats": (url, "12345", "media-123", ["720", "480"]),
    }
    assert result == {
        "id": "12345",
        "title": "Example Video",
        "formats": formats,
        "thumbnail": "https://cdn.example.com/thumb.jpg",
        "uploader": "Uploader",
        "uploader_id": "42",
        "channel": "Channel",
        "channel_id": "84",
        "timestamp": 1577934245,
        "like_count": 17,
        "dislike_count": 3,
        "view_count": 1001,
        "duration": 125,
        "age_limit": 18,
    }


def test_porntube_real_extract_falls_back_to_channel(monkeypatch):
    url = "https://www.porntube.com/embed/67890"
    video = {
        "title": "Embedded Video",
        "mediaId": 987,
        "encodings": [
            {"height": 360},
            {"height": ""},
            {},
        ],
        "masterThumb": "not-a-valid-url",
        "channel": {
            "name": "Fallback Channel",
            "id": 321,
        },
    }
    webpage = "INITIALSTATE = '%s'" % _encode_initial_state(video)

    ie = PornTubeIE(SimpleNamespace(params={"no_color": True}))
    formats = [
        {
            "url": "https://cdn.example.com/360.mp4",
            "format_id": "360p",
        }
    ]
    calls = {}

    def download_webpage(request_url, display_id):
        calls["webpage"] = (request_url, display_id)
        return webpage

    def extract_formats(request_url, video_id, media_id, sources):
        calls["formats"] = (request_url, video_id, media_id, sources)
        return formats

    monkeypatch.setattr(ie, "_download_webpage", download_webpage)
    monkeypatch.setattr(ie, "_extract_formats", extract_formats)

    result = ie._real_extract(url)

    assert calls == {
        "webpage": (url, None),
        "formats": (url, "67890", 987, ["360"]),
    }
    assert result == {
        "id": "67890",
        "title": "Embedded Video",
        "formats": formats,
        "thumbnail": None,
        "uploader": "Fallback Channel",
        "uploader_id": "321",
        "channel": "Fallback Channel",
        "channel_id": "321",
        "timestamp": None,
        "like_count": None,
        "dislike_count": None,
        "view_count": None,
        "duration": None,
        "age_limit": 18,
    }
