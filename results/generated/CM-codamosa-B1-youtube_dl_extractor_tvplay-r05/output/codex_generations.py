

# Generated at 2026-10-24 15:19:45.782778
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:19:48.194281
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:19:50.607102
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:19:53.022607
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:19:55.435917
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:19:57.849325
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:00.262814
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:02.689629
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:05.102047
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:07.515375
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:20:09.928989
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:20:12.343451
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:20:14.756503
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:17.170174
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:19.583106
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:21.998504
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:24.415179
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:26.828504
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:29.241321
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:31.653437
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:34.067982
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:36.481168
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:38.895718
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:41.306263
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:20:43.718753
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:46.133615
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:48.545457
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:20:50.958192
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:20:52.429074
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-24 15:20:53.987167
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:20:55.309096
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:20:56.626569
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:20:57.950501
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:20:59.290268
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:21:00.745942
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:21:02.178282
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:21:03.577731
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:21:04.925196
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:21:06.303717
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:21:07.777463
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:21:09.245602
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:21:10.693967
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:21:12.047878
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:21:13.408748
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:21:14.753694
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:21:16.151410
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:21:17.468290
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:21:18.869643
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:21:20.209592
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:21:21.532461
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:21:23.947608
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:26.536837
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:28.949385
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:31.363367
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:33.778078
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:36.195026
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:38.604886
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:21:41.018032
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:21:43.432531
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:21:45.846789
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:48.260663
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:50.674661
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:21:53.088959
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:21:55.503709
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:21:57.921955
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:22:00.335538
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:22:02.751546
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:22:05.164936
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:22:07.576251
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:22:09.989374
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:22:20.270699
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()

# Generated at 2026-10-24 15:22:21.704176
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:22:23.137675
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:22:24.571354
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:22:26.008217
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:22:27.439167
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:22:28.758020
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:22:30.090306
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:22:31.536100
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:22:32.929993
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:22:35.345987
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:22:37.862183
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:22:40.275667
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:22:42.690757
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:22:45.332550
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:22:47.743218
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:22:50.158011
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:22:52.571291
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:22:54.987048
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:22:57.403394
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:22:59.815922
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:23:02.231790
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:23:04.643203
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:07.056519
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:09.467934
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:11.881767
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:14.301370
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:17.040807
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()

# Generated at 2026-10-24 15:23:18.367425
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:23:19.692621
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:23:21.523186
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:23:22.860343
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:23:24.248951
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:23:25.571909
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:23:26.961933
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:23:28.280437
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:23:29.739396
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:23:31.058464
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:23:32.378904
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:23:33.782352
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:23:37.232333
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:23:38.564929
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:23:39.941052
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:23:42.454890
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:23:44.870291
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:23:47.283668
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:23:49.896007
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:52.426620
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:54.843344
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:57.256892
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:23:59.668966
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:24:02.081818
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:24:04.493383
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:24:06.906745
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:24:09.319042
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:24:11.732055
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:14.143926
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:16.555795
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:18.966015
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:21.376819
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:23.789482
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:26.202205
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:24:28.613698
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:24:31.027205
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:24:37.916169
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:24:40.328289
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:24:42.741399
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:24:45.154847
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:47.568277
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:49.982393
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:24:52.395951
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:24:54.813805
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:24:57.229545
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:24:59.642166
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:25:02.054242
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:25:04.467268
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:25:06.881206
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:25:09.293303
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:25:11.705733
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:25:13.405493
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:25:14.768885
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:25:16.132783
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:25:17.462198
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:25:18.780916
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:25:29.736033
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:25:31.135877
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:25:32.620060
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:25:34.100099
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:25:35.419159
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:25:36.815745
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:25:38.133203
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:25:39.686036
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:25:42.108064
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:25:44.522778
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:25:46.936726
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:25:49.351408
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:25:51.766746
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:25:54.182230
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:26:19.354903
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:26:21.767477
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:26:33.444090
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

# Generated at 2026-10-24 15:26:34.848038
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:26:36.174609
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:26:37.492611
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:26:38.937149
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:26:40.262344
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:26:41.587455
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:26:43.051764
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:26:45.576721
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:26:47.986454
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:26:50.402189
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:26:52.817221
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:26:55.236689
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:26:57.647929
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:27:46.895662
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:27:48.225911
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 15:27:49.544656
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # Constructor creates a usable instance
    assert ie is not None
    assert ie.geo_verification_headers() is not None

    # _VALID_URL matches all supported viafree domains and captures country + path
    m = ie._match_valid_url('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    m = ie._match_valid_url('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert m is not None
    assert m.group('country') == 'dk'

    # suitable() defers to TVPlayIE (viafree URLs handled by TVPlayIE must be rejected here)
    assert not ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')


if __name__ == '__main__':
    test_ViafreeIE()
    print('test_ViafreeIE passed')

# Generated at 2026-10-24 15:27:50.969382
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert re.compile(TVPlayIE._VALID_URL)

    # constructor must set up matching via _VALID_URL
    assert ie._match_id('mtg:418113') == '418113'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

# Generated at 2026-10-24 15:27:53.489196
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:27:55.900182
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:27:58.312788
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:28:00.729060
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:28:03.305505
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:28:05.716017
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:28:08.278936
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:28:10.693523
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:28:13.105910
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:28:15.517867
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:28:17.931736
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:28:20.345094
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 15:28:22.756589
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:28:25.172397
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:28:27.582119
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 15:28:29.994137
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:28:32.407403
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 15:28:34.823020
# Unit test for constructor of class ViafreeIE