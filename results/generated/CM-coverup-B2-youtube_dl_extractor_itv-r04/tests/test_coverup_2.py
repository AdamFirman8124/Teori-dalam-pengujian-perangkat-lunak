# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import json
from urllib.parse import parse_qs, urlsplit

from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.extractor.itv import ITVBTCCIE


def test_itv_btcc_extracts_brightcove_playlist(monkeypatch):
    url = "https://www.itv.com/btcc/races/season-highlights"
    webpage = """
        <div data-video-id="123456789"></div>
        <div data-video-id='987654321'></div>
        <div data-video-id="not-numeric"></div>
    """
    extractor = ITVBTCCIE()
    download_calls = []
    title_calls = []

    def fake_download_webpage(request_url, video_id):
        download_calls.append((request_url, video_id))
        return webpage

    def fake_og_search_title(html, fatal=True):
        title_calls.append((html, fatal))
        return "BTCC Season Highlights"

    monkeypatch.setattr(extractor, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(extractor, "_og_search_title", fake_og_search_title)

    result = extractor._real_extract(url)

    assert download_calls == [(url, "season-highlights")]
    assert title_calls == [(webpage, False)]
    assert result["_type"] == "playlist"
    assert result["id"] == "season-highlights"
    assert result["title"] == "BTCC Season Highlights"
    assert len(result["entries"]) == 2

    for entry, expected_video_id in zip(
        result["entries"], ("123456789", "987654321")
    ):
        parsed_url = urlsplit(entry["url"])
        smuggled_data = json.loads(
            parse_qs(parsed_url.fragment)["__youtubedl_smuggle"][0]
        )

        assert entry["_type"] == "url"
        assert entry["id"] == expected_video_id
        assert entry["ie_key"] == BrightcoveNewIE.ie_key()
        assert (
            parsed_url._replace(fragment="").geturl()
            == extractor.BRIGHTCOVE_URL_TEMPLATE % expected_video_id
        )
        assert smuggled_data == {
            "geo_ip_blocks": [
                "193.113.0.0/16",
                "54.36.162.0/23",
                "159.65.16.0/21",
            ],
            "referrer": url,
        }


def test_itv_btcc_returns_empty_untitled_playlist(monkeypatch):
    url = "http://www.itv.com/btcc/archive/no-videos"
    webpage = '<div data-video-id="invalid"></div>'
    extractor = ITVBTCCIE()
    download_calls = []
    title_calls = []

    def fake_download_webpage(request_url, video_id):
        download_calls.append((request_url, video_id))
        return webpage

    def fake_og_search_title(html, fatal=True):
        title_calls.append((html, fatal))
        return None

    monkeypatch.setattr(extractor, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(extractor, "_og_search_title", fake_og_search_title)

    result = extractor._real_extract(url)

    assert download_calls == [(url, "no-videos")]
    assert title_calls == [(webpage, False)]
    assert result == {
        "_type": "playlist",
        "id": "no-videos",
        "entries": [],
    }
