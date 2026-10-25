# file: project/youtube_dl/extractor/tvplay.py:378-380
# asked: {"lines": [380], "branches": []}
# gained: {"lines": [380], "branches": []}

import pytest

from youtube_dl.extractor.tvplay import TVPlayIE, ViafreeIE


def test_viafree_suitable_false_when_tvplay_matches():
    # This URL matches both TVPlayIE and ViafreeIE patterns, so ViafreeIE
    # must yield to TVPlayIE and return False (executes the True branch).
    url = 'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869'
    assert TVPlayIE.suitable(url)
    assert ViafreeIE.suitable(url) is False


def test_viafree_suitable_true_when_only_viafree_matches():
    # This URL matches only ViafreeIE, so the super() call is executed
    # and its result (True) is returned.
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    assert not TVPlayIE.suitable(url)
    assert ViafreeIE.suitable(url) is True


def test_viafree_suitable_false_when_neither_matches():
    # Neither pattern matches, so the super() call is executed and its
    # result (False) is returned.
    url = 'http://www.example.com/programmer/something'
    assert not TVPlayIE.suitable(url)
    assert ViafreeIE.suitable(url) is False
