# file: project/youtube_dl/extractor/tvplay.py:378-380
# asked: {"lines": [380], "branches": []}
# gained: {"lines": [380], "branches": []}

from youtube_dl.extractor.tvplay import TVPlayIE, ViafreeIE


def test_viafree_suitable_returns_false_for_tvplay_compatible_url():
    url = "http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869"
    assert TVPlayIE.suitable(url) is True
    assert ViafreeIE.suitable(url) is False


def test_viafree_suitable_returns_true_for_viafree_only_url():
    url = "http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1"
    assert TVPlayIE.suitable(url) is False
    assert ViafreeIE.suitable(url) is True


def test_viafree_suitable_returns_false_for_unrelated_url():
    url = "https://www.youtube.com/watch?v=BaW_jenozKc"
    assert TVPlayIE.suitable(url) is False
    assert ViafreeIE.suitable(url) is False


def test_viafree_suitable_true_branch_mocked(monkeypatch):
    monkeypatch.setattr(TVPlayIE, "suitable", classmethod(lambda cls, url: True))
    assert TVPlayIE.suitable("http://www.viafree.se/program/reality/foo/sasong-1/avsnitt-1") is True
    assert ViafreeIE.suitable("http://www.viafree.se/program/reality/foo/sasong-1/avsnitt-1") is False


def test_viafree_suitable_else_branch_mocked(monkeypatch):
    monkeypatch.setattr(TVPlayIE, "suitable", classmethod(lambda cls, url: False))
    viafree_only_url = "http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1"
    unrelated_url = "https://example.com/not-matching-anything"
    assert TVPlayIE.suitable(viafree_only_url) is False
    assert ViafreeIE.suitable(viafree_only_url) is True
    assert ViafreeIE.suitable(unrelated_url) is False
