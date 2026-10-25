# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from types import SimpleNamespace
from urllib.parse import quote

from youtube_dl.extractor.fourtube import PornTubeIE


def _initial_state_webpage(video):
    serialized_state = json.dumps({"page": {"video": video}})
    url_encoded_state = quote(serialized_state)
    encoded_state = base64.b64encode(
        url_encoded_state.encode("utf-8")
    ).decode("ascii")
    return 'INITIALSTATE = "{}"'.format(encoded_state)


def test_porntube_real_extract_with_complete_metadata(monkeypatch):
    url = "https://www.porntube.com/videos/sample-video_12345"
    video = {
        "title": "Sample video",
        "mediaId": 9876,
        "encodings": [
            {"height": 720},
            {"height": None},
            {},
            {"height": "1080"},
        ],
        "masterThumb": "https://cdn.example.com/thumbnail.jpg",
        "user": {"username": "Uploader", "id": 42},
        "channel": {"name": "Channel", "id": 84},
        "likes": "15",
        "dislikes": "3",
        "playsQty": "1200",
        "durationInSeconds": "65",
        "publishedAt": "2020-01-02T03:04:05Z",
    }
    webpage = _initial_state_webpage(video)
    expected_formats = [
        {
            "url": "https://cdn.example.com/video.mp4",
            "format_id": "720p",
        }
    ]
    calls = {}

    ie = PornTubeIE(SimpleNamespace(params={"no_color": True}))

    def download_webpage(request_url, display_id):
        calls["download_webpage"] = (request_url, display_id)
        return webpage

    def extract_formats(request_url, video_id, media_id, sources):
        calls["extract_formats"] = (
            request_url,
            video_id,
            media_id,
            list(sources),
        )
        return expected_formats

    monkeypatch.setattr(ie, "_download_webpage", download_webpage)
    monkeypatch.setattr(ie, "_extract_formats", extract_formats)

    result = ie._real_extract(url)

    assert calls["download_webpage"] == (url, "sample-video")
    assert calls["extract_formats"] == (
        url,
        "12345",
        9876,
        ["720", "1080"],
    )
    assert result == {
        "id": "12345",
        "title": "Sample video",
        "formats": expected_formats,
        "thumbnail": "https://cdn.example.com/thumbnail.jpg",
        "uploader": "Uploader",
        "uploader_id": "42",
        "channel": "Channel",
        "channel_id": "84",
        "timestamp": 1577934245,
        "like_count": 15,
        "dislike_count": 3,
        "view_count": 1200,
        "duration": 65,
        "age_limit": 18,
    }


def test_porntube_real_extract_uses_channel_fallbacks(monkeypatch):
    url = "https://www.porntube.com/embed/67890"
    video = {
        "title": "Fallback metadata video",
        "mediaId": "media-123",
        "encodings": [
            {},
            {"height": None},
            {"height": 0},
        ],
        "masterThumb": "not-a-valid-url",
        "channel": {"name": "Fallback Channel", "id": 321},
        "likes": "invalid",
        "dislikes": None,
        "playsQty": {},
        "durationInSeconds": "unknown",
        "publishedAt": None,
    }
    webpage = _initial_state_webpage(video)
    calls = {}

    ie = PornTubeIE(SimpleNamespace(params={"no_color": True}))

    def download_webpage(request_url, display_id):
        calls["download_webpage"] = (request_url, display_id)
        return webpage

    def extract_formats(request_url, video_id, media_id, sources):
        calls["extract_formats"] = (
            request_url,
            video_id,
            media_id,
            list(sources),
        )
        return []

    monkeypatch.setattr(ie, "_download_webpage", download_webpage)
    monkeypatch.setattr(ie, "_extract_formats", extract_formats)

    result = ie._real_extract(url)

    assert calls["download_webpage"] == (url, None)
    assert calls["extract_formats"] == (
        url,
        "67890",
        "media-123",
        [],
    )
    assert result == {
        "id": "67890",
        "title": "Fallback metadata video",
        "formats": [],
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
