# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from types import SimpleNamespace
from urllib.parse import quote

from youtube_dl.extractor.fourtube import PornTubeIE


def test_porntube_real_extract_with_uploader_metadata(monkeypatch):
    ie = PornTubeIE(SimpleNamespace(params={"no_color": True}))
    url = "https://www.porntube.com/videos/example-video_12345"
    video = {
        "title": "Example Video",
        "mediaId": 9876,
        "encodings": [
            {"height": 720},
            {"height": 0},
            {"codec": "h264"},
            {"height": "480"},
        ],
        "masterThumb": "https://cdn.example.com/thumb.jpg",
        "user": {"username": "Uploader", "id": 42},
        "channel": {"name": "Channel Name", "id": 84},
        "likes": "15",
        "dislikes": "3",
        "playsQty": "1200",
        "durationInSeconds": "321",
        "publishedAt": "2020-01-02T03:04:05Z",
    }
    state = quote(json.dumps({"page": {"video": video}}), safe="")
    encoded_state = base64.b64encode(state.encode("utf-8")).decode("ascii")
    webpage = 'INITIALSTATE = "%s"' % encoded_state
    expected_formats = [
        {"url": "https://cdn.example.com/video-480.mp4", "format_id": "480p"},
        {"url": "https://cdn.example.com/video-720.mp4", "format_id": "720p"},
    ]
    format_call = {}

    def download_webpage(request_url, display_id):
        assert request_url == url
        assert display_id == "example-video"
        return webpage

    def extract_formats(request_url, video_id, media_id, sources):
        format_call.update(
            url=request_url,
            video_id=video_id,
            media_id=media_id,
            sources=sources,
        )
        return expected_formats

    monkeypatch.setattr(ie, "_download_webpage", download_webpage)
    monkeypatch.setattr(ie, "_extract_formats", extract_formats)

    result = ie._real_extract(url)

    assert format_call == {
        "url": url,
        "video_id": "12345",
        "media_id": 9876,
        "sources": ["720", "480"],
    }
    assert result == {
        "id": "12345",
        "title": "Example Video",
        "formats": expected_formats,
        "thumbnail": "https://cdn.example.com/thumb.jpg",
        "uploader": "Uploader",
        "uploader_id": "42",
        "channel": "Channel Name",
        "channel_id": "84",
        "timestamp": 1577934245,
        "like_count": 15,
        "dislike_count": 3,
        "view_count": 1200,
        "duration": 321,
        "age_limit": 18,
    }


def test_porntube_real_extract_falls_back_to_channel(monkeypatch):
    ie = PornTubeIE(SimpleNamespace(params={"no_color": True}))
    url = "https://www.porntube.com/embed/67890"
    video = {
        "title": "Embedded Video",
        "mediaId": "media-123",
        "encodings": [
            {"height": None},
            {"height": 360},
            {},
        ],
        "masterThumb": "not-a-valid-url",
        "user": {"username": ""},
        "channel": {"name": "Fallback Channel", "id": 77},
        "likes": None,
        "dislikes": "invalid",
        "playsQty": "0",
        "durationInSeconds": 0,
        "publishedAt": None,
    }
    state = quote(json.dumps({"page": {"video": video}}), safe="")
    encoded_state = base64.b64encode(state.encode("utf-8")).decode("ascii")
    webpage = "INITIALSTATE = '%s'" % encoded_state
    expected_formats = [{"url": "https://cdn.example.com/video-360.mp4"}]
    format_call = {}

    def download_webpage(request_url, display_id):
        assert request_url == url
        assert display_id is None
        return webpage

    def extract_formats(request_url, video_id, media_id, sources):
        format_call.update(
            url=request_url,
            video_id=video_id,
            media_id=media_id,
            sources=sources,
        )
        return expected_formats

    monkeypatch.setattr(ie, "_download_webpage", download_webpage)
    monkeypatch.setattr(ie, "_extract_formats", extract_formats)

    result = ie._real_extract(url)

    assert format_call == {
        "url": url,
        "video_id": "67890",
        "media_id": "media-123",
        "sources": ["360"],
    }
    assert result == {
        "id": "67890",
        "title": "Embedded Video",
        "formats": expected_formats,
        "thumbnail": None,
        "uploader": "Fallback Channel",
        "uploader_id": "77",
        "channel": "Fallback Channel",
        "channel_id": "77",
        "timestamp": None,
        "like_count": None,
        "dislike_count": None,
        "view_count": 0,
        "duration": 0,
        "age_limit": 18,
    }
