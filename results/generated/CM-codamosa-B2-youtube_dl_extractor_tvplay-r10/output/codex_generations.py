

# Generated at 2026-10-24 14:14:59.789721
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

# Generated at 2026-10-24 14:15:02.210394
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:15:04.629151
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:15:07.045204
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:15:09.474094
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:15:11.889151
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:15:14.310308
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:15:16.731381
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:15:19.145899
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:15:21.563697
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:15:23.982530
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:15:32.147962
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()

# Generated at 2026-10-24 14:15:40.420179
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:15:51.296279
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

# Generated at 2026-10-24 14:15:52.731589
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

# Generated at 2026-10-24 14:15:54.266165
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

# Generated at 2026-10-24 14:15:55.593608
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

# Generated at 2026-10-24 14:16:12.800867
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # 1. Default constructor (no downloader)
    ie = TVPlayIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayIE)
    assert ie._downloader is None
    assert ie._downloader_params == {}
    assert ie._ready is False

    # 2. Constructor with downloader
    downloader = FakeDownloader()
    ie2 = TVPlayIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._downloader_params == {}

    # 3. Class attributes set up by construction path
    assert TVPlayIE.IE_NAME == 'mtg'
    assert TVPlayIE.IE_DESC == 'MTG services'

    # 4. URL matching works on a constructed instance
    assert ie.suitable('mtg:418113')
    assert ie.suitable(
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id(
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113') == '418113'
    assert not ie.suitable('https://www.google.com/')

# Generated at 2026-10-24 14:16:14.234424
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:16:15.601254
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:16:16.998800
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

# Generated at 2026-10-24 14:16:18.432276
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:16:19.865567
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

# Generated at 2026-10-24 14:16:22.509009
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:16:25.175859
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:16:43.009507
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-24 14:16:44.330556
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:16:45.773087
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:16:47.412069
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

# Generated at 2026-10-24 14:16:48.844855
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

# Generated at 2026-10-24 14:16:50.278254
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

# Generated at 2026-10-24 14:16:51.712102
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:16:53.036789
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:16:54.360298
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:16:55.682532
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

# Generated at 2026-10-24 14:16:57.089300
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

# Generated at 2026-10-24 14:16:58.410158
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

# Generated at 2026-10-24 14:16:59.741981
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

# Generated at 2026-10-24 14:17:01.237884
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

# Generated at 2026-10-24 14:17:02.671543
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

# Generated at 2026-10-24 14:17:04.054245
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

# Generated at 2026-10-24 14:17:05.553873
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

# Generated at 2026-10-24 14:17:06.937434
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

# Generated at 2026-10-24 14:17:08.405954
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

# Generated at 2026-10-24 14:17:11.069234
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:13.485099
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:16.027154
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:18.441566
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:20.856786
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:23.485807
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:25.901394
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:17:28.320907
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:17:30.736072
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:17:33.151564
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:35.565670
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:37.980693
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:40.393061
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:17:42.806578
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:17:45.223352
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:17:47.640044
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:17:50.054546
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:17:52.471381
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:17:54.891556
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:57.309869
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:17:59.733011
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:18:02.149588
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:04.574159
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:06.991886
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:09.415064
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:18:11.833511
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:18:14.245432
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:18:16.659563
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:19.073105
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:21.486507
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:24.171685
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:26.584473
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:27.961035
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-24 14:18:29.353101
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

# Generated at 2026-10-24 14:18:30.682706
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

# Generated at 2026-10-24 14:18:32.078010
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

# Generated at 2026-10-24 14:18:33.498234
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

# Generated at 2026-10-24 14:18:34.827865
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

# Generated at 2026-10-24 14:18:36.161520
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

# Generated at 2026-10-24 14:18:37.510472
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:18:38.823438
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

# Generated at 2026-10-24 14:18:40.148472
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

# Generated at 2026-10-24 14:18:44.917372
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

# Generated at 2026-10-24 14:18:46.402030
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

# Generated at 2026-10-24 14:18:47.703033
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:18:49.043990
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

# Generated at 2026-10-24 14:18:50.457720
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

# Generated at 2026-10-24 14:18:51.839065
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:18:54.340608
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:56.756012
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:18:59.289882
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:01.710072
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:04.146653
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:06.731776
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:09.146585
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:11.564572
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:13.983639
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:16.402043
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:18.817575
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:21.235589
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:30.139303
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:32.552333
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:34.965596
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:19:37.391677
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:19:48.769185
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():instance = TVPlayHomeIE()

# Generated at 2026-10-24 14:19:50.102360
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

# Generated at 2026-10-24 14:19:51.532399
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

# Generated at 2026-10-24 14:19:52.961831
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

# Generated at 2026-10-24 14:19:54.297863
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

# Generated at 2026-10-24 14:19:56.089712
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

# Generated at 2026-10-24 14:19:57.532548
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

# Generated at 2026-10-24 14:19:58.906982
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:20:00.248266
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

# Generated at 2026-10-24 14:20:18.050784
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

# Generated at 2026-10-24 14:20:20.469380
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:20:23.118688
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:20:25.534769
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:20:27.951659
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:20:30.367479
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:20:32.784383
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:20:35.201010
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:20:37.754232
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:20:40.171135
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:20:41.525243
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

# Generated at 2026-10-24 14:20:42.947877
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

# Generated at 2026-10-24 14:20:44.361093
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:20:45.675762
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:20:47.008759
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

# Generated at 2026-10-24 14:20:48.331238
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:21:16.009760
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:21:18.420969
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:21:20.836025
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:21:23.250904
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:21:25.663627
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:21:28.085182
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:21:30.501696
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:21:32.916594
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:21:35.335808
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:21:37.775274
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:21:40.191273
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:21:42.605141
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:21:45.020653
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:21:47.436290
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:21:49.851015
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:21:52.279442
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:21:54.719339
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:21:57.163814
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:21:59.577264
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:22:01.991933
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:22:04.405837
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:22:06.820545
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:22:09.237243
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:22:11.649966
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:22:14.065065
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:22:16.479328
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:22:18.893054
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 14:22:21.309257
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:22:23.724127
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:22:26.139715
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:23:24.934599
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:23:27.351063
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:23:29.768685
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 14:23:32.186646
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:23:34.600736
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:23:37.016368
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 14:23:38.343707
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:23:39.663630
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:23:41.110000
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

# Generated at 2026-10-24 14:23:42.748286
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

# Generated at 2026-10-24 14:23:44.183525
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

# Generated at 2026-10-24 14:23:45.502200
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance_ = TVPlayHomeIE()
    assert instance_ is not None

# Generated at 2026-10-24 14:23:46.817754
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

# Generated at 2026-10-24 14:23:48.178571
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