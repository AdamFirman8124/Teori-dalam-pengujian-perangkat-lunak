# file: project/youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.extractor.itv import ITVBTCCIE
from youtube_dl.utils import unsmuggle_url


def test_itv_btcc_real_extract_builds_brightcove_playlist(monkeypatch):
    extractor = ITVBTCCIE()
    url = "https://www.itv.com/btcc/races/2024/race-highlights"
    webpage = """
        <div data-video-id="123456789"></div>
        <div data-video-id='987654321'></div>
    """

    def fake_download_webpage(requested_url, video_id):
        assert requested_url == url
        assert video_id == "race-highlights"
        return webpage

    def fake_og_search_title(downloaded_webpage, fatal=True):
        assert downloaded_webpage == webpage
        assert fatal is False
        return "Race Highlights"

    monkeypatch.setattr(extractor, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(extractor, "_og_search_title", fake_og_search_title)

    result = extractor._real_extract(url)

    assert result["_type"] == "playlist"
    assert result["id"] == "race-highlights"
    assert result["title"] == "Race Highlights"
    assert len(result["entries"]) == 2

    for entry, video_id in zip(
        result["entries"], ("123456789", "987654321")
    ):
        clean_url, smuggled_data = unsmuggle_url(entry["url"], {})

        assert entry["_type"] == "url"
        assert entry["id"] == video_id
        assert entry["ie_key"] == BrightcoveNewIE.ie_key()
        assert clean_url == extractor.BRIGHTCOVE_URL_TEMPLATE % video_id
        assert smuggled_data == {
            "geo_ip_blocks": [
                "193.113.0.0/16",
                "54.36.162.0/23",
                "159.65.16.0/21",
            ],
            "referrer": url,
        }


def test_itv_btcc_real_extract_handles_no_videos_or_title(monkeypatch):
    extractor = ITVBTCCIE()
    url = "http://itv.com/btcc/empty-race"
    webpage = '<div data-video-id="not-numeric"></div>'

    def fake_download_webpage(requested_url, video_id):
        assert requested_url == url
        assert video_id == "empty-race"
        return webpage

    def fake_og_search_title(downloaded_webpage, fatal=True):
        assert downloaded_webpage == webpage
        assert fatal is False
        return None

    monkeypatch.setattr(extractor, "_download_webpage", fake_download_webpage)
    monkeypatch.setattr(extractor, "_og_search_title", fake_og_search_title)

    result = extractor._real_extract(url)

    assert result == {
        "_type": "playlist",
        "entries": [],
        "id": "empty-race",
    }
