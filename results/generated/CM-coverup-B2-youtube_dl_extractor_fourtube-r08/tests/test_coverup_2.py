# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from types import SimpleNamespace
from urllib.parse import quote

from youtube_dl.extractor.fourtube import PornTubeIE


def make_ie():
    return PornTubeIE(SimpleNamespace(params={"no_color": True}))


def encode_initial_state(video, quote_char='"'):
    state = json.dumps({"page": {"video": video}})
    encoded = base64.b64encode(
        quote(state).encode("utf-8")
    ).decode("ascii")
    return "<script>INITIALSTATE = {0}{1}{0};</script>".format(
        quote_char, encoded
    )


def test_porntube_real_extract_with_uploader(monkeypatch):
    url = "https://www.porntube.com/videos/example-video_12345"
    video = {
        "title": "Example Video",
        "mediaId": 9876,
        "encodings": [
            {"height": 720},
            {"height": 1080},
            {"height": 0},
            {},
        ],
        "masterThumb": "https://cdn.example.com/thumb.jpg",
        "user": {"username": "Uploader", "id": 42},
        "channel": {"name": "Channel", "id": 84},
        "likes": "12",
        "dislikes": "3",
        "playsQty": "456",
        "durationInSeconds": "78",
        "publishedAt": "2020-01-02T03:04:05Z",
    }
    webpage = encode_initial_state(video)
    ie = make_ie()
    download_calls = []
    format_calls = []
    expected_formats = [
        {"url": "https://cdn.example.com/video.mp4", "height": 720}
    ]

    def download_webpage(request_url, display_id):
        download_calls.append((request_url, display_id))
        return webpage

    def extract_formats(request_url, video_id, media_id, sources):
        format_calls.append((request_url, video_id, media_id, sources))
        return expected_formats

    monkeypatch.setattr(ie, "_download_webpage", download_webpage)
    monkeypatch.setattr(ie, "_extract_formats", extract_formats)

    result = ie._real_extract(url)

    assert download_calls == [(url, "example-video")]
    assert format_calls == [(url, "12345", 9876, ["720", "1080"])]
    assert result == {
        "id": "12345",
        "title": "Example Video",
        "formats": expected_formats,
        "thumbnail": "https://cdn.example.com/thumb.jpg",
        "uploader": "Uploader",
        "uploader_id": "42",
        "channel": "Channel",
        "channel_id": "84",
        "timestamp": 1577934245,
        "like_count": 12,
        "dislike_count": 3,
        "view_count": 456,
        "duration": 78,
        "age_limit": 18,
    }


def test_porntube_real_extract_falls_back_to_channel(monkeypatch):
    url = "https://m.porntube.com/videos/channel-fallback_67890"
    video = {
        "title": "Channel Fallback",
        "mediaId": "media-1",
        "encodings": [
            {"height": None},
            {"width": 1920},
        ],
        "masterThumb": "not-a-url",
        "channel": {"name": "Fallback Channel", "id": 135},
        "likes": "invalid",
        "dislikes": None,
        "playsQty": {},
        "durationInSeconds": "",
        "publishedAt": None,
    }
    webpage = encode_initial_state(video, quote_char="'")
    ie = make_ie()
    download_calls = []
    format_calls = []

    def download_webpage(request_url, display_id):
        download_calls.append((request_url, display_id))
        return webpage

    def extract_formats(request_url, video_id, media_id, sources):
        format_calls.append((request_url, video_id, media_id, sources))
        return []

    monkeypatch.setattr(ie, "_download_webpage", download_webpage)
    monkeypatch.setattr(ie, "_extract_formats", extract_formats)

    result = ie._real_extract(url)

    assert download_calls == [(url, "channel-fallback")]
    assert format_calls == [(url, "67890", "media-1", [])]
    assert result == {
        "id": "67890",
        "title": "Channel Fallback",
        "formats": [],
        "thumbnail": None,
        "uploader": "Fallback Channel",
        "uploader_id": "135",
        "channel": "Fallback Channel",
        "channel_id": "135",
        "timestamp": None,
        "like_count": None,
        "dislike_count": None,
        "view_count": None,
        "duration": None,
        "age_limit": 18,
    }
