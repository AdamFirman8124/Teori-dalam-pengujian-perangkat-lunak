# file: project/youtube_dl/extractor/udn.py:41-102
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}

import json
from types import SimpleNamespace

from youtube_dl.extractor.udn import UDNEmbedIE


def make_ie():
    return UDNEmbedIE(SimpleNamespace(params={"no_color": True}))


def test_real_extract_returns_youtube_url(monkeypatch):
    ie = make_ie()
    url = "https://video.udn.com/embed/news/100001"
    page = """
        <script>
        var options = {
            "video": {"youtube": "https://www.youtube.com/watch?v=abc123"},
            "title": "YouTube video"
        };
        </script>
    """

    monkeypatch.setattr(
        ie,
        "_download_webpage",
        lambda requested_url, video_id, **kwargs: page,
    )

    result = ie._real_extract(url)

    assert result == {
        "_type": "url",
        "url": "https://www.youtube.com/watch?v=abc123",
        "ie_key": "Youtube",
    }


def test_real_extract_handles_all_format_branches(monkeypatch):
    ie = make_ie()
    url = "https://video.udn.com/embed/news/100002"
    page = """
        <script>
        var options = {
            "video": {
                "empty": "",
                "hls": "/api/hls",
                "hds": "/api/hds",
                "mp4": "/api/mp4",
                "source": "/api/source"
            },
            "title": "All formats",
            "poster": "https://img.example.com/poster.jpg"
        };
        </script>
    """
    resolved_urls = {
        "https://video.udn.com/api/hls": "https://cdn.example.com/master.m3u8",
        "https://video.udn.com/api/hds": "https://cdn.example.com/manifest.f4m",
        "https://video.udn.com/api/mp4": (
            "https://cdn.example.com/video_720p_1500.mp4"
        ),
        "https://video.udn.com/api/source": "https://cdn.example.com/video.mp4",
    }
    download_calls = []

    def fake_download_webpage(requested_url, video_id, note=None, **kwargs):
        download_calls.append((requested_url, video_id, note))
        if requested_url == url:
            return page
        return resolved_urls[requested_url]

    m3u8_calls = []

    def fake_extract_m3u8_formats(video_url, video_id, **kwargs):
        m3u8_calls.append((video_url, video_id, kwargs))
        return [{"url": video_url, "format_id": "hls-test"}]

    f4m_calls = []

    def fake_extract_f4m_formats(video_url, video_id, **kwargs):
        f4m_calls.append((video_url, video_id, kwargs))
        return [{"url": video_url, "format_id": "hds-test"}]

    sort_calls = []

    def fake_sort_formats(formats):
        sort_calls.append(list(formats))

    monkeypatch.setattr(ie, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(ie, "_extract_m3u8_formats", fake_extract_m3u8_formats)
    monkeypatch.setattr(ie, "_extract_f4m_formats", fake_extract_f4m_formats)
    monkeypatch.setattr(ie, "_sort_formats", fake_sort_formats)

    result = ie._real_extract(url)

    expected_formats = [
        {
            "url": "https://cdn.example.com/master.m3u8",
            "format_id": "hls-test",
        },
        {
            "url": "https://cdn.example.com/manifest.f4m",
            "format_id": "hds-test",
        },
        {
            "url": "https://cdn.example.com/video_720p_1500.mp4",
            "format_id": "http-mp4",
            "height": 720,
            "tbr": 1500,
        },
        {
            "url": "https://cdn.example.com/video.mp4",
            "format_id": "http-source",
        },
    ]

    assert result == {
        "id": "100002",
        "formats": expected_formats,
        "title": "All formats",
        "thumbnail": "https://img.example.com/poster.jpg",
    }
    assert m3u8_calls == [
        (
            "https://cdn.example.com/master.m3u8",
            "100002",
            {"ext": "mp4", "m3u8_id": "hls"},
        )
    ]
    assert f4m_calls == [
        (
            "https://cdn.example.com/manifest.f4m",
            "100002",
            {"f4m_id": "hds"},
        )
    ]
    assert sort_calls == [expected_formats]
    assert download_calls == [
        (url, "100002", None),
        (
            "https://video.udn.com/api/hls",
            "100002",
            "retrieve url for hls video",
        ),
        (
            "https://video.udn.com/api/hds",
            "100002",
            "retrieve url for hds video",
        ),
        (
            "https://video.udn.com/api/mp4",
            "100002",
            "retrieve url for mp4 video",
        ),
        (
            "https://video.udn.com/api/source",
            "100002",
            "retrieve url for source video",
        ),
    ]


def test_real_extract_falls_back_when_options_json_cannot_be_parsed(monkeypatch):
    ie = make_ie()
    url = "https://video.udn.com/play/news/100003"
    page = """
        <script>
        var options = {
            "video": {"mp4": "/api/fallback"},
            title: 'Fallback title',
            broken: undefined
        };
        </script>
    """
    parse_calls = []
    download_calls = []

    def fake_parse_json(source, name, fatal=True, **kwargs):
        parse_calls.append((source, name, fatal))
        if name == "options":
            return None
        return json.loads(source)

    def fake_download_webpage(requested_url, video_id, note=None, **kwargs):
        download_calls.append((requested_url, video_id, note))
        if requested_url == url:
            return page
        assert requested_url == "https://video.udn.com/api/fallback"
        return "https://cdn.example.com/fallback.mp4"

    sort_calls = []

    def fake_sort_formats(formats):
        sort_calls.append(list(formats))

    monkeypatch.setattr(ie, "_parse_json", fake_parse_json)
    monkeypatch.setattr(ie, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(ie, "_sort_formats", fake_sort_formats)

    result = ie._real_extract(url)

    expected_formats = [
        {
            "url": "https://cdn.example.com/fallback.mp4",
            "format_id": "http-mp4",
        }
    ]

    assert result == {
        "id": "100003",
        "formats": expected_formats,
        "title": "Fallback title",
        "thumbnail": None,
    }
    assert len(parse_calls) == 2
    assert parse_calls[0][1:] == ("options", False)
    assert parse_calls[1][1:] == ("video urls", True)
    assert json.loads(parse_calls[1][0]) == {"mp4": "/api/fallback"}
    assert download_calls == [
        (url, "100003", None),
        (
            "https://video.udn.com/api/fallback",
            "100003",
            "retrieve url for mp4 video",
        ),
    ]
    assert sort_calls == [expected_formats]
