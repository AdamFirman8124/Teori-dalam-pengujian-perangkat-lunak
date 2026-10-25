# file: project/youtube_dl/extractor/udn.py:41-102
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 86, 88, 89, 90, 91, 93, 95, 97, 98, 99, 100, 101], "branches": [[50, 51], [50, 55], [62, 63], [62, 65], [66, 67], [66, 95], [67, 68], [67, 70], [75, 76], [75, 78], [78, 79], [78, 82], [88, 89], [88, 93]]}

import json
from types import SimpleNamespace

from youtube_dl.extractor.udn import UDNEmbedIE


def make_ie():
    return UDNEmbedIE(SimpleNamespace(params={"no_color": True}))


def test_udn_extracts_all_format_types_and_skips_empty_urls(monkeypatch):
    ie = make_ie()
    page_url = "https://video.udn.com/embed/news/123"
    page = """
        <script>
        var options = {
            "video": {
                "hls": "/hls-api",
                "hds": "/hds-api",
                "mp4": "/mp4-api",
                "source": "/source-api",
                "empty": ""
            },
            "title": "Test title",
            "poster": "https://img.example.com/poster.jpg"
        };
        </script>
    """
    responses = {
        "https://video.udn.com/hls-api": "https://cdn.example.com/master.m3u8",
        "https://video.udn.com/hds-api": "https://cdn.example.com/manifest.f4m",
        "https://video.udn.com/mp4-api": "https://cdn.example.com/video_720p_1500.mp4",
        "https://video.udn.com/source-api": "https://cdn.example.com/video.mp4",
    }
    download_calls = []

    def fake_download_webpage(url, video_id, **kwargs):
        download_calls.append((url, video_id, kwargs))
        if url == page_url:
            return page
        return responses[url]

    m3u8_calls = []

    def fake_extract_m3u8_formats(url, video_id, **kwargs):
        m3u8_calls.append((url, video_id, kwargs))
        return [{"url": url, "format_id": "hls-test", "ext": "mp4"}]

    f4m_calls = []

    def fake_extract_f4m_formats(url, video_id, **kwargs):
        f4m_calls.append((url, video_id, kwargs))
        return [{"url": url, "format_id": "hds-test", "ext": "flv"}]

    sort_calls = []

    def fake_sort_formats(formats):
        sort_calls.append(list(formats))

    monkeypatch.setattr(ie, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(ie, "_extract_m3u8_formats", fake_extract_m3u8_formats)
    monkeypatch.setattr(ie, "_extract_f4m_formats", fake_extract_f4m_formats)
    monkeypatch.setattr(ie, "_sort_formats", fake_sort_formats)

    result = ie._real_extract(page_url)

    expected_formats = [
        {
            "url": "https://cdn.example.com/master.m3u8",
            "format_id": "hls-test",
            "ext": "mp4",
        },
        {
            "url": "https://cdn.example.com/manifest.f4m",
            "format_id": "hds-test",
            "ext": "flv",
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
        "id": "123",
        "formats": expected_formats,
        "title": "Test title",
        "thumbnail": "https://img.example.com/poster.jpg",
    }
    assert m3u8_calls == [
        (
            "https://cdn.example.com/master.m3u8",
            "123",
            {"ext": "mp4", "m3u8_id": "hls"},
        )
    ]
    assert f4m_calls == [
        (
            "https://cdn.example.com/manifest.f4m",
            "123",
            {"f4m_id": "hds"},
        )
    ]
    assert sort_calls == [expected_formats]
    assert download_calls == [
        (page_url, "123", {}),
        (
            "https://video.udn.com/hls-api",
            "123",
            {"note": "retrieve url for hls video"},
        ),
        (
            "https://video.udn.com/hds-api",
            "123",
            {"note": "retrieve url for hds video"},
        ),
        (
            "https://video.udn.com/mp4-api",
            "123",
            {"note": "retrieve url for mp4 video"},
        ),
        (
            "https://video.udn.com/source-api",
            "123",
            {"note": "retrieve url for source video"},
        ),
    ]


def test_udn_uses_fallback_fields_when_options_parsing_fails(monkeypatch):
    ie = make_ie()
    page_url = "https://video.udn.com/play/news/456"
    page = """
        <script>
        var options = {
            video: {'mp4': '/fallback-api'},
            title: 'Fallback title',
        };
        </script>
    """
    parse_calls = []

    def fake_parse_json(source, label, **kwargs):
        parse_calls.append((source, label, kwargs))
        if label == "options":
            return None
        return json.loads(source)

    download_calls = []

    def fake_download_webpage(url, video_id, **kwargs):
        download_calls.append((url, video_id, kwargs))
        if url == page_url:
            return page
        assert url == "https://video.udn.com/fallback-api"
        return "https://cdn.example.com/fallback_360p_800.mp4"

    sort_calls = []

    monkeypatch.setattr(ie, "_parse_json", fake_parse_json)
    monkeypatch.setattr(ie, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(
        ie, "_sort_formats", lambda formats: sort_calls.append(list(formats))
    )

    result = ie._real_extract(page_url)

    expected_formats = [
        {
            "url": "https://cdn.example.com/fallback_360p_800.mp4",
            "format_id": "http-mp4",
            "height": 360,
            "tbr": 800,
        }
    ]

    assert result == {
        "id": "456",
        "formats": expected_formats,
        "title": "Fallback title",
        "thumbnail": None,
    }
    assert [call[1] for call in parse_calls] == ["options", "video urls"]
    assert parse_calls[0][2] == {"fatal": False}
    assert parse_calls[1][2] == {}
    assert json.loads(parse_calls[1][0]) == {"mp4": "/fallback-api"}
    assert sort_calls == [expected_formats]
    assert download_calls == [
        (page_url, "456", {}),
        (
            "https://video.udn.com/fallback-api",
            "456",
            {"note": "retrieve url for mp4 video"},
        ),
    ]


def test_udn_returns_youtube_url_without_retrieving_formats(monkeypatch):
    ie = make_ie()
    page_url = "https://video.udn.com/embed/news/789"
    page = """
        <script>
        var options = {
            "video": {
                "youtube": "https://www.youtube.com/watch?v=abc123"
            },
            "title": "YouTube title",
            "poster": "https://img.example.com/youtube.jpg"
        };
        </script>
    """
    download_calls = []

    def fake_download_webpage(url, video_id, **kwargs):
        download_calls.append((url, video_id, kwargs))
        assert url == page_url
        assert video_id == "789"
        return page

    monkeypatch.setattr(ie, "_download_webpage", fake_download_webpage)

    result = ie._real_extract(page_url)

    assert result == {
        "_type": "url",
        "url": "https://www.youtube.com/watch?v=abc123",
        "ie_key": "Youtube",
    }
    assert download_calls == [(page_url, "789", {})]
