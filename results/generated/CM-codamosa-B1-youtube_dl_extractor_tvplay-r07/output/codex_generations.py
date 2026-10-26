

# Generated at 2026-10-25 14:08:17.579135
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:08:30.935260
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:08:47.046965
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 14:09:02.135731
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:09:18.445984
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert extractor._downloader is None
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-25 14:09:31.416737
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-25 14:09:43.894744
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:10:00.209901
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    assert isinstance(ie, InfoExtractor)
    assert ie._GEO_BYPASS is False
    assert ie.suitable(
        'https://www.viafree.se/program/reality/'
        'sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    )

# Generated at 2026-10-25 14:10:10.331742
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()


# Generated at 2026-10-25 14:10:23.845206
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    assert isinstance(ie, ViafreeIE)
    assert ie._GEO_BYPASS is False
    assert ie._VALID_URL

    url = (
        'https://www.viafree.no/programmer/underholdning/'
        'det-beste-vorspielet/sesong-2/episode-1'
    )
    assert ViafreeIE.suitable(url)

# Generated at 2026-10-25 14:10:37.142807
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():ie = ViafreeIE()

# Generated at 2026-10-25 14:10:38.588431
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:10:40.022790
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 14:10:42.892659
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

# Generated at 2026-10-25 14:10:46.396852
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:10:49.239226
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

# Generated at 2026-10-25 14:10:50.787699
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:11:03.679336
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 14:11:07.469722
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 14:11:10.111371
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 14:11:12.526273
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 14:11:14.941817
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 14:11:17.359280
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 14:11:19.776340
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 14:11:22.190746
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 14:11:24.608044
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 14:11:27.026418
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 14:11:28.561204
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:11:44.441818
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor._GEO_BYPASS is False
    assert extractor._VALID_URL

# Generated at 2026-10-25 14:12:09.930562
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 14:12:11.466859
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:12:13.555049
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 14:12:32.612974
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:12:50.354511
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:13:02.965761
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:13:10.773569
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:13:23.228877
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 14:13:43.124692
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 14:13:56.835906
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:14:25.406038
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 14:14:39.229837
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    assert isinstance(ie, InfoExtractor)
    assert ie._GEO_BYPASS is False
    assert ie._VALID_URL

# Generated at 2026-10-25 14:14:56.128171
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:14:57.558955
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:14:58.934517
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:15:16.618038
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 14:15:19.196354
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 14:15:21.944313
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 14:15:24.362000
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 14:15:26.778328
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 14:15:29.193812
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 14:15:31.613189
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-25 14:15:34.033879
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 14:15:36.503980
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 14:15:38.916327
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-25 14:15:41.332580
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-25 14:15:55.109751
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:16:09.854762
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert extractor._downloader is None
    assert extractor._GEO_BYPASS is False
    assert extractor._VALID_URL

# Generated at 2026-10-25 14:16:33.135178
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    instance = ViafreeIE()
    assert instance is not None
    assert isinstance(instance, ViafreeIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2026-10-25 14:16:43.851886
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 14:16:47.435119
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

# Generated at 2026-10-25 14:16:48.868770
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:16:58.289288
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

# Generated at 2026-10-25 14:17:01.156375
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:17:02.591161
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:17:11.193821
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-25 14:17:12.597660
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:17:23.072539
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-25 14:17:24.810999
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL is not None

    # constructor with default downloader
    ie2 = TVPlayHomeIE(None)
    assert ie2._downloader is None

# Generated at 2026-10-25 14:17:41.707524
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-25 14:17:51.130070
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

# Generated at 2026-10-25 14:18:09.766087
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()


# Generated at 2026-10-25 14:18:24.306046
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    assert isinstance(ie, ViafreeIE)
    assert ie._GEO_BYPASS is False

    url = (
        'https://www.viafree.no/programmer/underholdning/'
        'det-beste-vorspielet/sesong-2/episode-1'
    )
    assert ViafreeIE.suitable(url)