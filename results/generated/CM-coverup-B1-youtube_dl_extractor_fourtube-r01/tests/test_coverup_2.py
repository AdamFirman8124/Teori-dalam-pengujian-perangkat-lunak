# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from types import SimpleNamespace
from urllib.parse import quote

from youtube_dl.extractor.fourtube import PornTubeIE


def _make_webpage(video, quote_char='"'):
    state = quote(
        json.dumps({"page": {"video": video}}),
        safe="",
    )
    encoded_state = base64.b64encode(state.encode("utf-8")).decode("ascii")
    return (
        "<script>INITIALSTATE = {quote}{state}{quote}</script>".format(
            quote=quote_char,
            state=encoded_state,
        )
    )


def test_porntube_real_extract_with_uploader(monkeypatch):
    url = "https://www.porntube.com/videos/example-video_12345"
    video = {
        "title": "Example Video",
        "mediaId": 9876,
        "encodings": [
            {"height": 720},
            {"height": "480"},
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
    webpage = _make_webpage(video)
    expected_formats = [
        {
            "url": "https://cdn.example.com/video.mp4",
            "format_id": "720p",
        }
    ]
    calls = {}

    def fake_download_webpage(requested_url, requested_id):
        calls["download_webpage"] = (requested_url, requested_id)
        return webpage

    def fake_extract_formats(requested_url, video_id, media_id, sources):
        calls["extract_formats"] = (
            requested_url,
            video_id,
            media_id,
            sources,
        )
        return expected_formats

    downloader = SimpleNamespace(params={"no_color": True})
    extractor = PornTubeIE(downloader)
    monkeypatch.setattr(
        extractor, "_download_webpage", fake_download_webpage
    )
    monkeypatch.setattr(extractor, "_extract_formats", fake_extract_formats)

    result = extractor._real_extract(url)

    assert calls == {
        "download_webpage": (url, "example-video"),
        "extract_formats": (url, "12345", 9876, ["720", "480"]),
    }
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


def test_porntube_real_extract_embed_uses_channel_fallback(monkeypatch):
    url = "https://www.porntube.com/embed/67890"
    video = {
        "title": "Embedded Video",
        "mediaId": "media-123",
        "encodings": [
            {"height": None},
            {"height": 360},
            {"width": 640},
        ],
        "masterThumb": "not-a-url",
        "user": {},
        "channel": {"name": "Fallback Channel", "id": 99},
        "likes": None,
        "dislikes": "invalid",
        "playsQty": None,
        "durationInSeconds": "invalid",
        "publishedAt": None,
    }
    webpage = _make_webpage(video, quote_char="'")
    expected_formats = [{"format_id": "360p"}]
    calls = {}

    def fake_download_webpage(requested_url, requested_id):
        calls["download_webpage"] = (requested_url, requested_id)
        return webpage

    def fake_extract_formats(requested_url, video_id, media_id, sources):
        calls["extract_formats"] = (
            requested_url,
            video_id,
            media_id,
            sources,
        )
        return expected_formats

    downloader = SimpleNamespace(params={"no_color": True})
    extractor = PornTubeIE(downloader)
    monkeypatch.setattr(
        extractor, "_download_webpage", fake_download_webpage
    )
    monkeypatch.setattr(extractor, "_extract_formats", fake_extract_formats)

    result = extractor._real_extract(url)

    assert calls == {
        "download_webpage": (url, None),
        "extract_formats": (url, "67890", "media-123", ["360"]),
    }
    assert result == {
        "id": "67890",
        "title": "Embedded Video",
        "formats": expected_formats,
        "thumbnail": None,
        "uploader": "Fallback Channel",
        "uploader_id": "99",
        "channel": "Fallback Channel",
        "channel_id": "99",
        "timestamp": None,
        "like_count": None,
        "dislike_count": None,
        "view_count": None,
        "duration": None,
        "age_limit": 18,
    }
