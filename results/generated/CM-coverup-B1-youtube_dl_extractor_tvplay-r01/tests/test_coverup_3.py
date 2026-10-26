# file: project/youtube_dl/extractor/tvplay.py:378-380
# asked: {"lines": [380], "branches": []}
# gained: {"lines": [380], "branches": []}

from youtube_dl.extractor.common import InfoExtractor
from youtube_dl.extractor.tvplay import TVPlayIE, ViafreeIE


def test_viafree_suitable_returns_false_when_tvplay_suitable():
    # 'mtg:418113' is a known TVPlayIE match (see TVPlayIE._TESTS)
    url = 'mtg:418113'
    assert TVPlayIE.suitable(url)
    result = ViafreeIE.suitable(url)
    assert result is False


def test_viafree_suitable_delegates_to_super_when_tvplay_not_suitable(monkeypatch):
    url = 'https://example.com/not-a-tvplay-url'
    # real precondition: chosen URL is not suitable for TVPlayIE
    assert not TVPlayIE.suitable(url)
    monkeypatch.setattr(
        InfoExtractor, 'suitable',
        classmethod(lambda cls, u: True),
    )
    monkeypatch.setattr(
        TVPlayIE, 'suitable',
        classmethod(lambda cls, u: False),
    )
    result = ViafreeIE.suitable(url)
    # postcondition: else-branch delegates to super(), so mocked True propagates
    assert result is True


def test_viafree_suitable_short_circuits_without_calling_super(monkeypatch):
    url = 'https://example.com/anything'

    def _fail(cls, u):
        raise AssertionError('super().suitable should not be called when TVPlayIE matches')

    monkeypatch.setattr(TVPlayIE, 'suitable', classmethod(lambda cls, u: True))
    monkeypatch.setattr(InfoExtractor, 'suitable', classmethod(_fail))
    result = ViafreeIE.suitable(url)
    assert result is False


def test_viafree_suitable_falsy_for_unrelated_url():
    url = 'https://example.com/not-matching-anything-12345'
    assert not TVPlayIE.suitable(url)
    expected = super(ViafreeIE, ViafreeIE).suitable(url)
    result = ViafreeIE.suitable(url)
    assert result == expected
    assert not result
