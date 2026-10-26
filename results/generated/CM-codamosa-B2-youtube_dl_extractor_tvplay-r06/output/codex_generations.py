

# Generated at 2026-10-25 08:52:57.210795
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:52:59.634061
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:53:02.052380
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:53:04.768885
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:07.332218
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:09.665008
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:12.078582
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:14.495432
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:16.913629
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:19.400378
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:21.815812
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:24.231160
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:26.663749
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:53:29.078584
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:53:31.496152
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:53:33.912404
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:53:49.081797
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 08:54:24.388163
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayIE)
    assert TVPlayIE.IE_NAME == 'mtg'
    assert TVPlayIE.IE_DESC == 'MTG services'
    assert TVPlayIE._VALID_URL is not None
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385?autostart=true') == '395385'

# Generated at 2026-10-25 08:54:26.806917
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:54:29.224186
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:54:31.663245
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:54:34.081996
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:54:36.497538
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:54:38.916654
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:54:56.757264
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:54:58.171893
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

    # Constructor takes no arguments and yields a usable extractor instance

# Generated at 2026-10-25 08:54:59.603832
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.IE_NAME == 'tvplayhome'
    assert tvplayhome._VALID_URL is not None

# Generated at 2026-10-25 08:55:15.987010
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    # The class has no custom constructor, so it should initialize normally
    assert isinstance(extractor, ViafreeIE)

    # Verify inherited extractor metadata and class configuration
    assert extractor.ie_key() == 'Viafree'
    assert extractor._GEO_BYPASS is False

    # Ensure a valid Viafree URL is recognized
    assert extractor.suitable(
        'https://www.viafree.se/program/reality/'
        'sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    )

# Generated at 2026-10-25 08:55:18.637078
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:55:21.051996
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:55:23.469236
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:55:25.885527
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:55:28.489278
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:55:30.910962
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:55:33.329928
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:55:35.747399
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:55:38.164483
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:55:40.584846
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:55:43.004193
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:55:45.420246
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:55:47.891414
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:55:50.308888
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:55:52.727862
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:55:55.144123
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:55:57.563194
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:55:59.982256
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:56:02.402291
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:56:04.817314
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:56:07.233875
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:56:09.651500
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:56:12.071747
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:56:14.488692
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:56:16.904705
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:56:19.329145
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:56:21.747443
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:56:24.168289
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:56:26.587362
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:56:29.005230
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:56:31.424127
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:56:48.249528
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE(None)

# Generated at 2026-10-25 08:57:09.961451
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayIE)
    assert TVPlayIE.IE_NAME == 'mtg'
    assert TVPlayIE.IE_DESC == 'MTG services'
    assert TVPlayIE._VALID_URL is not None
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385?autostart=true') == '395385'

# Generated at 2026-10-25 08:57:51.944042
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

# Generated at 2026-10-25 08:59:11.713037
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

# Generated at 2026-10-25 08:59:13.145379
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.IE_NAME == 'tvplayhome'
    assert tvplayhome._VALID_URL is not None

# Generated at 2026-10-25 08:59:15.566022
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:59:18.146939
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:59:20.920856
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 08:59:23.332033
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:59:25.751389
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:59:28.166929
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:59:30.588351
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:59:33.008132
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:59:35.424843
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 08:59:37.840571
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 08:59:39.207372
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

    # Constructor takes no arguments and yields a usable extractor instance

# Generated at 2026-10-25 08:59:58.270785
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    assert isinstance(ie, ViafreeIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._GEO_BYPASS is False
    assert ie._VALID_URL

    # The constructor should initialize the extractor without errors.
    assert ie._downloader is None

# Generated at 2026-10-25 09:00:13.767011
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    assert isinstance(ie, ViafreeIE)
    assert ie._GEO_BYPASS is False

    url = (
        'https://www.viafree.se/program/reality/'
        'sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    )

    assert ViafreeIE.suitable(url)

    country, path = re.match(ViafreeIE._VALID_URL, url).groups()
    assert country == 'se'
    assert path == (
        'program/reality/'
        'sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    )

# Generated at 2026-10-25 09:00:38.203948
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, TVPlayIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('mtg:418113')
    assert not ie.suitable('http://www.example.com/video/418113')
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'

# Generated at 2026-10-25 09:00:40.975556
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayIE)
    assert TVPlayIE.IE_NAME == 'mtg'
    assert TVPlayIE.IE_DESC == 'MTG services'
    assert TVPlayIE._VALID_URL is not None
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385?autostart=true') == '395385'

# Generated at 2026-10-25 09:00:42.653800
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.IE_NAME == 'tvplayhome'
    assert tvplayhome._VALID_URL is not None

# Generated at 2026-10-25 09:01:19.508220
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, TVPlayIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('mtg:418113')
    assert not ie.suitable('http://www.example.com/video/418113')
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'

# Generated at 2026-10-25 09:01:20.946052
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.IE_NAME == 'tvplayhome'
    assert tvplayhome._VALID_URL is not None

# Generated at 2026-10-25 09:01:37.229650
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    # The inherited InfoExtractor constructor should work
    assert isinstance(ie, ViafreeIE)

    # Class configuration
    assert ie._GEO_BYPASS is False

    # A valid Viafree URL should be accepted
    assert ie.suitable(
        'https://www.viafree.no/programmer/'
        'underholdning/det-beste-vorspielet/sesong-2/episode-1'
    )

    # A TVPlay URL should be handled by TVPlayIE instead
    assert not ie.suitable(
        'https://tvplay.skaties.lv/vinas-melo-labak/418113/'
    )

# Generated at 2026-10-25 09:01:39.643586
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 09:01:56.782204
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

# Generated at 2026-10-25 09:02:21.984359
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # constructor without arguments
    ie = ViafreeIE()
    assert isinstance(ie, ViafreeIE)
    assert ie._downloader is None

    # constructor with downloader
    downloader = object()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader

    # class configuration
    assert ie._GEO_BYPASS is False
    assert ie._VALID_URL is not None

# Generated at 2026-10-25 09:02:25.556704
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.IE_NAME == 'tvplayhome'
    assert tvplayhome._VALID_URL is not None

# Generated at 2026-10-25 09:02:28.313110
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 09:02:30.734313
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 09:02:33.152317
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 09:02:35.753117
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 09:02:38.171197
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 09:02:40.592708
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 09:02:58.356582
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, TVPlayIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('mtg:418113')
    assert not ie.suitable('http://www.example.com/video/418113')
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'