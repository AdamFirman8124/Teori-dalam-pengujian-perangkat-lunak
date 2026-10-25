

# Generated at 2026-10-25 00:27:41.574148
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:27:43.998783
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:27:46.412448
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:27:48.827255
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:27:51.241955
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:27:53.657222
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:28:10.340513
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

# Generated at 2026-10-25 00:28:19.561621
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    downloader = object()
    extractor = TVPlayHomeIE(downloader)

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'

# Generated at 2026-10-25 00:28:20.901149
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

# Generated at 2026-10-25 00:28:22.232193
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

# Generated at 2026-10-25 00:28:23.574048
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

# Generated at 2026-10-25 00:28:24.983913
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

# Generated at 2026-10-25 00:28:26.426167
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

# Generated at 2026-10-25 00:28:27.854717
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

# Generated at 2026-10-25 00:28:43.342410
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._VALID_URL
    assert extractor._TESTS

    # Verify that the inherited constructor initialized the extractor
    assert extractor._downloader is None

    # Verify that the extractor can parse its custom URL scheme
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 00:28:45.867499
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:28:48.283490
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:28:50.698048
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:28:53.113771
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:28:55.529248
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:28:57.945250
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:29:21.199828
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()

    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-25 00:29:42.318406
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._VALID_URL
    assert extractor._downloader is None

# Generated at 2026-10-25 00:29:43.668793
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

# Generated at 2026-10-25 00:29:45.002502
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

# Generated at 2026-10-25 00:30:06.728815
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 00:30:30.627424
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None

# Generated at 2026-10-25 00:30:37.843905
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-25 00:30:40.378913
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:30:42.903332
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:30:45.317895
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:30:47.735299
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:30:50.345081
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:30:52.763840
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:30:55.181261
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:30:57.598841
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:31:00.017273
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:31:02.437945
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:31:04.853166
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:31:07.270085
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:31:09.692606
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:31:12.109730
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:31:14.526133
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:31:16.940718
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:31:19.359908
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:31:21.775747
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:31:31.660774
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.suitable(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    )

# Generated at 2026-10-25 00:31:39.323311
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    downloader = object()
    extractor = TVPlayHomeIE(downloader)

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 00:32:05.246078
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor.ie_key() == 'TVPlay'

# Generated at 2026-10-25 00:32:27.032869
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 00:32:44.857238
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:32:47.270794
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:32:49.685240
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:32:52.100598
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:32:54.516677
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:32:57.135192
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:32:59.544751
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:01.960613
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:04.381210
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:06.790726
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:09.207787
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:11.623661
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:14.035304
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:33:16.450986
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:33:18.867087
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:33:21.282124
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:23.696795
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:26.109746
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:28.525423
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:33:30.941398
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:33:33.356071
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:33:35.770891
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:38.187402
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:40.601371
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:43.016840
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:33:45.432147
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:33:47.847802
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:33:50.264471
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:52.681005
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:55.092964
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:33:57.508140
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:33:59.922352
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:34:08.489556
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Constructor takes no required arguments and initializes core attributes
    ie = TVPlayIE()
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('mtg:418113')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'
    assert ie._match_id('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true') == '238551'

# Generated at 2026-10-25 00:34:18.470215
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-25 00:34:35.363207
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

# Generated at 2026-10-25 00:34:37.781859
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:34:40.200196
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:02.397349
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:03.736638
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

# Generated at 2026-10-25 00:35:13.968699
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    downloader = object()
    extractor = TVPlayHomeIE(downloader)

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 00:35:16.635263
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:19.048218
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:21.463626
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:23.878687
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:26.305385
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:28.722401
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:31.288373
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:33.705686
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:36.120552
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:38.535980
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:40.952251
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:43.367605
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:35:45.793468
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:35:54.519137
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():downloader = object()

# Generated at 2026-10-25 00:36:01.175975
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-25 00:36:07.735157
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._VALID_URL
    assert extractor._TESTS

# Generated at 2026-10-25 00:36:14.692342
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'TVPlayHome'
    assert extractor.suitable(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    )

# Generated at 2026-10-25 00:36:39.781486
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-25 00:36:44.376084
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:36:46.795344
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:36:49.209180
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:36:51.625986
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:36:54.041531
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:36:56.458954
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:36:58.875539
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:37:01.293258
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:37:03.709822
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 00:37:06.125355
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:37:08.540048
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:37:10.956206
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 00:37:13.372793
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 00:37:39.939622
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():downloader = object()

# Generated at 2026-10-25 00:37:50.024681
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    assert isinstance(extractor, TVPlayHomeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._match_id(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ) == '10047125'