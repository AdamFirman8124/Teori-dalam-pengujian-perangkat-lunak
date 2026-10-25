# file: project/youtube_dl/extractor/tvplay.py:378-380
# asked: {"lines": [380], "branches": []}
# gained: {"lines": [380], "branches": []}

import pytest

from youtube_dl.extractor.tvplay import TVPlayIE, ViafreeIE


class TestViafreeIESuitable:
    """Cover both branches of ViafreeIE.suitable (line 380)."""

    def test_suitable_false_when_tvplay_ie_matches(self):
        # TVPlayIE._VALID_URL matches viafree.* URLs whose final path
        # segment is numeric, so the `False` branch must be taken.
        url = 'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869'
        assert TVPlayIE.suitable(url) is True
        assert ViafreeIE.suitable(url) is False

    def test_suitable_true_when_tvplay_ie_does_not_match(self):
        # Non-numeric final path segment: TVPlayIE does not match, so
        # super().suitable() is evaluated and returns True.
        url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
        assert TVPlayIE.suitable(url) is False
        assert ViafreeIE.suitable(url) is True

    def test_suitable_true_dk_domain(self):
        # Same branch via the .dk domain variant.
        url = 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
        assert TVPlayIE.suitable(url) is False
        assert ViafreeIE.suitable(url) is True

    def test_suitable_false_for_unrelated_url(self):
        # Neither TVPlayIE nor ViafreeIE matches: the else branch of the
        # conditional expression is evaluated and super() returns False.
        url = 'http://www.example.com/programmer/something/episode-1'
        assert TVPlayIE.suitable(url) is False
        assert ViafreeIE.suitable(url) is False
