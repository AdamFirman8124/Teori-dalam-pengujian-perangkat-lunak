

# Generated at 2026-10-25 02:48:07.793952
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 02:48:15.955888
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2026-10-25 02:48:24.365678
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s')

# Generated at 2026-10-25 02:48:32.244166
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'ITV'
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-10-25 02:48:43.024566
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 02:48:49.373547
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012'
    ) == '2a4547a0012'

# Generated at 2026-10-25 02:48:57.558726
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)

    test_url = (
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == (
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 02:49:00.215220
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:02.630748
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:05.212033
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:07.627557
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:10.043096
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:12.463326
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:14.873531
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:17.289624
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:19.703989
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:22.301900
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:49:27.506085
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-25 02:49:33.700113
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert not ie.suitable('https://example.com/video/123')

# Generated at 2026-10-25 02:49:40.056423
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._match_id(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    ) == 'btcc-2018-all-the-action-from-brands-hatch'
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:49:48.597859
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not extractor.suitable('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-10-25 02:49:57.053177
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:49:59.473553
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:01.891539
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:04.508333
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:06.923276
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:09.338625
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:11.753565
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:14.169533
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:16.583315
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:18.999461
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:21.413273
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:23.828298
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:26.242877
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:28.657805
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:31.072534
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:33.488051
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:35.903860
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:50:37.575871
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 02:50:46.307899
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:50:55.398502
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:51:03.427226
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    assert isinstance(ie, ITVBTCCIE)
    assert ie._downloader is None
    assert ie.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')
    assert ie._match_id(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    ) == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s')

# Generated at 2026-10-25 02:51:11.602434
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:51:14.120581
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:16.536173
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:18.951400
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:21.527860
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:51:23.942288
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:51:26.358320
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:51:28.771699
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:31.366408
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:33.782922
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:36.196670
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:38.611175
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:41.025285
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:43.445140
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:45.855935
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:48.272062
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:50.685932
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:53.099526
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:55.513814
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:51:57.927859
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:00.341807
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:02.756326
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:05.168525
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:07.583793
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:09.998807
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:12.415000
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:14.829704
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:17.245080
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:19.671057
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:22.084874
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:24.498660
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:26.913506
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:29.325824
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:31.740979
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:34.154377
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:36.567712
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:38.982040
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:41.396164
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:43.810403
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:46.224856
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:52:48.639326
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:51.053344
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:53.469776
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:55.887114
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:52:58.308776
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:00.721163
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:03.137833
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:05.553008
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:07.968241
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:10.383767
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:12.797708
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:15.213814
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:17.633165
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:20.048857
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:22.465453
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:53:24.880058
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:53:27.295467
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:53:29.714043
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:53:32.128689
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:53:34.542302
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:53:36.956572
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:53:43.984650
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert not extractor.suitable('https://example.com/video/123')

# Generated at 2026-10-25 02:53:53.086815
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:54:01.179429
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 02:54:09.165788
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITV'
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')
    assert extractor._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

# Generated at 2026-10-25 02:54:17.866704
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert not ie.suitable('https://www.example.com/hub/liar/2a4547a0012')

# Generated at 2026-10-25 02:54:28.005542
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:54:30.423362
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:54:32.845641
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:54:35.427934
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:54:37.844806
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:54:40.261542
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:54:42.677647
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:54:45.095241
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:54:46.514322
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 02:54:55.407362
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:55:06.636905
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-25 02:55:15.006445
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 02:55:28.433280
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Default construction
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

    # Construction with a downloader
    downloader = object()
    extractor = ITVIE(downloader)

    assert extractor._downloader is downloader

# Generated at 2026-10-25 02:55:30.849659
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:55:33.266715
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:55:35.683936
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:55:38.100011
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:55:40.518396
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:55:42.934224
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:55:45.352071
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:55:47.767454
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:55:50.388780
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 02:55:59.727400
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')
    assert extractor._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

# Generated at 2026-10-25 02:56:06.401340
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-25 02:56:12.540025
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:56:19.414056
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()

    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 02:56:28.388225
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:30.802050
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:33.217528
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:35.632783
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:38.047213
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:40.462459
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:42.877107
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:45.423809
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:47.839461
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:50.254168
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:52.668950
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:55.083875
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:57.501547
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:59.915294
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:02.329346
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:04.744012
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:57:07.158304
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:57:09.573158
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:57:11.988126
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:14.402393
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:16.817191
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:26.081576
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-25 02:57:34.577786
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:57:42.488813
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 02:58:00.095044
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:02.481781
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:04.899736
# Unit test for constructor of class ITVIE