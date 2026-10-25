# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
import urllib.parse

from youtube_dl import YoutubeDL
from youtube_dl.extractor.fourtube import PornTubeIE


def _build_webpage(video_dict, quote_char='"'):
    payload = {"page": {"video": video_dict}}
    json_str = json.dumps(payload)
    quoted = urllib.parse.quote(json_str, safe="")
    b64 = base64.b64encode(quoted.encode("utf-8")).decode("utf-8")
    return "<html><script>INITIALSTATE=%s%s%s;</script></html>" % (quote_char, b64, quote_char)


def _make_ie():
    ie = PornTubeIE()
    ydl = YoutubeDL({"quiet": True, "no_warnings": True, "no_color": True})
    ie.set_downloader(ydl)
    return ie


def test_porntube_full_videos_www_double_quote(monkeypatch):
    ie = _make_ie()
    url = "https://www.porntube.com/videos/teen-couple-doing-anal_7089759"
    video = {
        "title": "Teen couple doing anal",
        "mediaId": "media123",
        "encodings": [{"height": 360}, {"height": 720}, {"height": None}, {}],
        "masterThumb": "https://example.com/thumb.jpg",
        "user": {"username": "Alexy", "id": 91488},
        "channel": {"name": "Exploited College Girls", "id": 665},
        "likes": 123,
        "dislikes": 4,
        "playsQty": 9999,
        "durationInSeconds": 5052,
        "publishedAt": "2015-06-06T12:00:00+00:00",
    }
    webpage = _build_webpage(video, quote_char='"')
    tokens = {
        "360": {"token": "https://cdn.example.com/v360.mp4"},
        "720": {"token": "https://cdn.example.com/v720.mp4"},
    }

    def fake_download_webpage(self, url_arg, video_id_arg, *args, **kwargs):
        assert url_arg == url
        assert video_id_arg == "teen-couple-doing-anal"
        return webpage

    def fake_download_json(self, url_arg, video_id_arg, *args, **kwargs):
        assert video_id_arg == "7089759"
        assert "media123" in url_arg
        assert "360+720" in url_arg
        assert url_arg.startswith("https://tkn.porntube.com/")
        return tokens

    monkeypatch.setattr(PornTubeIE, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(PornTubeIE, "_download_json", fake_download_json)

    result = ie._real_extract(url)

    assert result["id"] == "7089759"
    assert result["title"] == "Teen couple doing anal"
    assert result["thumbnail"] == "https://example.com/thumb.jpg"
    assert result["uploader"] == "Alexy"
    assert result["uploader_id"] == "91488"
    assert result["channel"] == "Exploited College Girls"
    assert result["channel_id"] == "665"
    assert result["like_count"] == 123
    assert result["dislike_count"] == 4
    assert result["view_count"] == 9999
    assert result["duration"] == 5052
    assert result["age_limit"] == 18
    assert isinstance(result["timestamp"], int)
    assert len(result["formats"]) == 2
    by_id = {f["format_id"]: f for f in result["formats"]}
    assert set(by_id.keys()) == {"360p", "720p"}
    assert by_id["360p"]["url"] == "https://cdn.example.com/v360.mp4"
    assert by_id["720p"]["url"] == "https://cdn.example.com/v720.mp4"


def test_porntube_embed_single_quote_fallback_to_channel(monkeypatch):
    ie = _make_ie()
    url = "https://www.porntube.com/embed/1331406"
    video = {
        "title": "Fallback Title",
        "mediaId": "mediaFallback",
        "encodings": [{"height": 480}, {"foo": "bar"}],
        "masterThumb": None,
        "channel": {"name": "FallbackChannel", "id": 777},
        "likes": None,
        "dislikes": None,
        "playsQty": None,
        "durationInSeconds": None,
        "publishedAt": None,
    }
    webpage = _build_webpage(video, quote_char="'")
    tokens = {
        "480": {"token": "https://cdn.example.com/fallback480.mp4"},
    }

    def fake_download_webpage(self, url_arg, video_id_arg, *args, **kwargs):
        assert url_arg == url
        assert video_id_arg is None
        return webpage

    def fake_download_json(self, url_arg, video_id_arg, *args, **kwargs):
        assert video_id_arg == "1331406"
        assert "mediaFallback" in url_arg
        assert "480" in url_arg
        return tokens

    monkeypatch.setattr(PornTubeIE, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(PornTubeIE, "_download_json", fake_download_json)

    result = ie._real_extract(url)

    assert result["id"] == "1331406"
    assert result["title"] == "Fallback Title"
    assert result["thumbnail"] is None
    assert result["uploader"] == "FallbackChannel"
    assert result["uploader_id"] == "777"
    assert result["channel"] == "FallbackChannel"
    assert result["channel_id"] == "777"
    assert result["like_count"] is None
    assert result["dislike_count"] is None
    assert result["view_count"] is None
    assert result["duration"] is None
    assert result["timestamp"] is None
    assert result["age_limit"] == 18
    assert len(result["formats"]) == 1
    assert result["formats"][0]["format_id"] == "480p"
    assert result["formats"][0]["url"] == "https://cdn.example.com/fallback480.mp4"


def test_porntube_mobile_no_channel_invalid_thumb(monkeypatch):
    ie = _make_ie()
    url = "https://m.porntube.com/videos/some-video_9999999"
    video = {
        "title": "Mobile Title",
        "mediaId": "mediaMobile",
        "encodings": [{"height": 240}, {"height": 0}, {"height": None}],
        "masterThumb": "not a url",
        "user": {"username": "MobileUser", "id": 12345},
        "likes": 42,
        "dislikes": 1,
        "playsQty": 100,
        "durationInSeconds": 60,
        "publishedAt": "2013-09-20T00:00:00+00:00",
    }
    webpage = _build_webpage(video, quote_char='"')
    tokens = {
        "240": {"token": "https://cdn.example.com/mobile240.mp4"},
    }

    def fake_download_webpage(self, url_arg, video_id_arg, *args, **kwargs):
        assert url_arg == url
        assert video_id_arg == "some-video"
        return webpage

    def fake_download_json(self, url_arg, video_id_arg, *args, **kwargs):
        assert video_id_arg == "9999999"
        assert "mediaMobile" in url_arg
        return tokens

    monkeypatch.setattr(PornTubeIE, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(PornTubeIE, "_download_json", fake_download_json)

    result = ie._real_extract(url)

    assert result["id"] == "9999999"
    assert result["title"] == "Mobile Title"
    assert result["thumbnail"] is None
    assert result["uploader"] == "MobileUser"
    assert result["uploader_id"] == "12345"
    assert result["channel"] is None
    assert result["channel_id"] is None
    assert result["like_count"] == 42
    assert result["dislike_count"] == 1
    assert result["view_count"] == 100
    assert result["duration"] == 60
    assert isinstance(result["timestamp"], int)
    assert result["age_limit"] == 18
    assert len(result["formats"]) == 1
    assert result["formats"][0]["format_id"] == "240p"
    assert result["formats"][0]["url"] == "https://cdn.example.com/mobile240.mp4"
