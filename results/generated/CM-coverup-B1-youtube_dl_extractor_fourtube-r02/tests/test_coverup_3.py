# file: project/youtube_dl/extractor/fourtube.py:25-41
# asked: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}
# gained: {"lines": [26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": []}

from types import SimpleNamespace

from youtube_dl.extractor.fourtube import FourTubeBaseIE


class TestFourTubeBaseExtractFormats:
    def test_extract_formats_builds_token_url_and_sorted_formats(self, monkeypatch):
        ie = FourTubeBaseIE()
        monkeypatch.setattr(ie, "_TKN_HOST", "token.example.com", raising=False)
        monkeypatch.setattr(ie, "_downloader", SimpleNamespace(params={}), raising=False)

        sources = ["720", "240", "1080"]
        tokens_json = {
            "240": {"token": "https://cdn.example.com/240.mp4"},
            "720": {"token": "https://cdn.example.com/720.mp4"},
            "1080": {"token": "https://cdn.example.com/1080.mp4"},
        }
        captured = {}

        def fake_download_json(token_url, video_id, data=b"", headers=None):
            captured["token_url"] = token_url
            captured["video_id"] = video_id
            captured["data"] = data
            captured["headers"] = headers
            return tokens_json

        monkeypatch.setattr(ie, "_download_json", fake_download_json, raising=False)

        url = "https://www.fourtube.com/videos/some-video"
        formats = ie._extract_formats(url, "vid123", "media456", sources)

        assert captured["token_url"] == "https://token.example.com/media456/desktop/720+240+1080"
        assert captured["video_id"] == "vid123"
        assert captured["data"] == b""
        assert captured["headers"]["Origin"] == "https://www.fourtube.com"
        assert captured["headers"]["Referer"] == url

        assert len(formats) == 3
        by_id = {f["format_id"]: f for f in formats}
        for src in sources:
            entry = by_id[src + "p"]
            assert entry["url"] == tokens_json[src]["token"]
            assert entry["format_id"] == src + "p"
            assert entry["resolution"] == src + "p"
            assert entry["quality"] == int(src)

        qualities = [f["quality"] for f in formats]
        assert qualities == sorted(qualities)
        assert qualities == [240, 720, 1080]

    def test_extract_formats_single_source(self, monkeypatch):
        ie = FourTubeBaseIE()
        monkeypatch.setattr(ie, "_TKN_HOST", "token.example.com", raising=False)
        monkeypatch.setattr(ie, "_downloader", SimpleNamespace(params={}), raising=False)

        tokens_json = {"360": {"token": "https://cdn.example.com/360.mp4"}}
        captured = {}

        def fake_download_json(token_url, video_id, data=b"", headers=None):
            captured["token_url"] = token_url
            captured["headers"] = headers
            return tokens_json

        monkeypatch.setattr(ie, "_download_json", fake_download_json, raising=False)

        url = "http://www.porntube.com/videos/other-video"
        formats = ie._extract_formats(url, "vid999", "media999", ["360"])

        assert captured["token_url"] == "https://token.example.com/media999/desktop/360"
        assert captured["headers"]["Origin"] == "http://www.porntube.com"
        assert captured["headers"]["Referer"] == url
        assert len(formats) == 1
        assert formats[0]["url"] == "https://cdn.example.com/360.mp4"
        assert formats[0]["format_id"] == "360p"
        assert formats[0]["resolution"] == "360p"
        assert formats[0]["quality"] == 360
