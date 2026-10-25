import pytest

from youtube_dl.extractor.tvplay import TVPlayIE, ViafreeIE


class TestViafreeIESuitable:
    """Cover both branches of ViafreeIE.suitable (line 380)."""

    def test_suitable_false_when_tvplay_ie_matches(self):
        # A viafree.se URL ending in a numeric id also matches TVPlayIE,
        # so ViafreeIE must yield to it and return False.
        url = 'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869'
        assert TVPlayIE.suitable(url) is True
        assert ViafreeIE.suitable(url) is False

    def test_suitable_false_for_plain_tvplay_url(self):
        # A pure TVPlay URL is claimed by TVPlayIE, not ViafreeIE.
        url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
        assert TVPlayIE.suitable(url) is True
        assert ViafreeIE.suitable(url) is False

    def test_suitable_true_when_tvplay_ie_does_not_match(self):
        # Non-numeric final path segment: matches ViafreeIE only,
        # exercising the super().suitable(url) branch with a True result.
        url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
        assert TVPlayIE.suitable(url) is False
        assert ViafreeIE.suitable(url) is True

    def test_suitable_true_for_danish_viafree_url(self):
        url = 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
        assert TVPlayIE.suitable(url) is False
        assert ViafreeIE.suitable(url) is True

    def test_suitable_false_for_unrelated_url(self):
        # Matches neither extractor: super().suitable() branch returns False.
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        assert TVPlayIE.suitable(url) is False
        assert ViafreeIE.suitable(url) is False
