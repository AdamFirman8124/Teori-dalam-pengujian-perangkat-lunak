

# Generated at 2026-10-24 20:47:16.708722
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:47:18.033267
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:47:19.430479
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:47:20.751372
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:47:22.152918
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:47:38.325494
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

# Generated at 2026-10-24 20:47:39.677453
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:47:41.001478
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:48:06.875565
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-24 20:48:31.403203
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Constructor produces a usable instance
    assert ie.IE_NAME == 'ITV'
    assert ie.ie_key() == 'ITV'

    # Class-level config intact after construction
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']

    # URL pattern extracts the ID correctly
    assert ITVIE._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

    # Rejects non-hub ITV URLs
    assert not ITVIE.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ITVIE.suitable('https://www.itv.com/hub/')

# Generated at 2026-10-24 20:48:32.790796
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:48:34.120796
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:48:50.652285
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Constructor produces a usable instance
    assert ie.IE_NAME == 'ITV'
    assert ie.ie_key() == 'ITV'

    # Class-level config intact after construction
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']

    # URL pattern extracts the ID correctly
    assert ITVIE._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

    # Rejects non-hub ITV URLs
    assert not ITVIE.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ITVIE.suitable('https://www.itv.com/hub/')

# Generated at 2026-10-24 20:48:51.977564
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:48:53.306926
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:49:02.118677
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:49:08.879092
# Unit test for constructor of class ITVIE
def test_ITVIE():extractor = ITVIE(None)

# Generated at 2026-10-24 20:49:10.311484
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:49:11.640450
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:49:28.130486
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Constructor produces a usable instance
    assert ie.IE_NAME == 'ITV'
    assert ie.ie_key() == 'ITV'

    # Class-level config intact after construction
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']

    # URL pattern extracts the ID correctly
    assert ITVIE._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

    # Rejects non-hub ITV URLs
    assert not ITVIE.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ITVIE.suitable('https://www.itv.com/hub/')

# Generated at 2026-10-24 20:49:52.194173
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 20:49:54.714581
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:49:57.131405
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:49:59.548596
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:01.965578
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:04.382594
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:06.800193
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:09.216328
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:11.631491
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:14.049152
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:16.467163
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:18.884600
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:21.298642
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:23.715376
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:26.130486
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:28.551419
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:30.963558
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:33.379648
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:35.794205
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:38.212005
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:40.628997
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:43.046091
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:45.464079
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:47.879306
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:50.295656
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:50:52.715109
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:50:55.132578
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:51:00.482601
# Unit test for constructor of class ITVIE
def test_ITVIE():extractor = ITVIE()

# Generated at 2026-10-24 20:51:01.929839
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:51:26.132882
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'ITV'
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-24 20:51:32.549965
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:51:37.871761
# Unit test for constructor of class ITVIE
def test_ITVIE():extractor = ITVIE()

# Generated at 2026-10-24 20:51:50.469206
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert ie._VALID_URL == (
        r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    )
    assert ie._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-24 20:51:52.889954
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:51:55.312462
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:51:57.863293
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:52:00.281169
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:52:02.818099
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:52:05.360291
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:52:07.803658
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:52:10.225413
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:52:12.641429
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:52:15.057422
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:52:17.477639
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:52:19.893022
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:52:22.311891
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:52:24.728750
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:52:26.109543
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-24 20:52:27.434149
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:52:51.893899
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-10-24 20:53:08.681128
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Constructor produces a usable instance
    assert ie.IE_NAME == 'ITV'
    assert ie.ie_key() == 'ITV'

    # Class-level config intact after construction
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']

    # URL pattern extracts the ID correctly
    assert ITVIE._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

    # Rejects non-hub ITV URLs
    assert not ITVIE.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ITVIE.suitable('https://www.itv.com/hub/')

# Generated at 2026-10-24 20:53:11.101309
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:13.669935
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:16.090022
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:18.504840
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:53:20.922462
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:53:23.505485
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:53:25.923121
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:28.344588
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:30.793644
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:33.178860
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:35.597681
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:38.013975
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:53:53.757679
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert ie._downloader is None
    assert ie.ie_key() == 'ITV'

# Generated at 2026-10-24 20:54:18.138331
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 20:54:20.559851
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:54:22.977360
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:54:25.394917
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:54:27.811851
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:54:29.239873
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-24 20:54:53.567150
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITV'
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')
    assert not extractor.suitable(
        'https://www.example.com/hub/liar/2a4547a0012')

# Generated at 2026-10-24 20:54:54.894305
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:55:08.840546
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert isinstance(ie, ITVIE)

# Generated at 2026-10-24 20:55:11.264127
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:13.684581
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:16.201899
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:18.712576
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:21.127446
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:23.547282
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:25.964450
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:28.379330
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:30.796847
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:55:58.071286
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 20:55:59.392602
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:56:00.728720
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:56:03.149238
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:05.565652
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:08.091233
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:10.510138
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:12.926439
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:15.342447
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:17.790060
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:20.175007
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:22.590888
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:25.007045
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:56:27.426309
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:56:29.843652
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:56:32.262188
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:34.680598
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:37.098286
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:39.514544
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:56:41.932300
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:56:44.349432
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 20:56:46.766457
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:49.214593
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:56:51.597645
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:57:00.914683
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:57:03.331804
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 20:57:08.213181
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 20:57:09.647552
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 20:57:31.463775
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert extractor._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012'
    ) == '2a4547a0012'