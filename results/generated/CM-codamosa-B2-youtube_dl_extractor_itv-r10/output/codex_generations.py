

# Generated at 2026-10-25 02:13:25.752173
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:28.272878
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:30.800012
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:33.216885
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:35.632768
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:38.049186
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:40.466729
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:42.879871
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:45.295312
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:13:52.285536
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Unit test for the constructor of class ITVBTCCIE.

    Verifies that:
    - The extractor can be instantiated without arguments (inherited from InfoExtractor).
    - Core class attributes are correctly defined.
    - The _VALID_URL regex matches a known BTCC hub URL and extracts the playlist id.
    """
    # Instantiate the extractor (constructor requires no arguments)
    ie = ITVBTCCIE()

    # The instance should be an InfoExtractor
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes must be present and non-empty
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'itv:btcc'
    assert ie._VALID_URL is not None

    # _WORKING should default to True (extractor marked as functional)
    assert ie._WORKING is True

    # The Brightcove URL template used by this extractor must be defined
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')

    # _VALID_URL must match the test URL and capture the playlist id
    test_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    match = ie._match_valid_url(test_url)
    assert match is not None
    assert match.group('id') == 'btcc-2018-all-the-action-from-brands-hatch'

    # _match_id convenience wrapper should return the same captured id
    assert ie._match_id(test_url) == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 02:14:02.650269
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITV'
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:14:11.470170
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    assert not extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012'
    )

# Generated at 2026-10-25 02:14:20.365207
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is None
    assert extractor.BRIGHTCOVE_URL_TEMPLATE
    assert extractor.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2026-10-25 02:14:28.967423
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2026-10-25 02:14:37.261957
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 02:14:44.635878
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:14:47.055327
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:14:49.753138
# Unit test for constructor of class ITVIE
def test_ITVIE():from youtube_dl.extractor.itv import ITVIE

# Generated at 2026-10-25 02:15:05.831363
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITV'
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')
    assert extractor._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

# Generated at 2026-10-25 02:15:14.228130
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

# Generated at 2026-10-25 02:15:21.293418
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:15:27.849682
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-25 02:15:34.196095
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None

# Generated at 2026-10-25 02:15:36.738162
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:15:39.285108
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:15:41.704465
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:15:44.226950
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:15:46.642459
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:15:49.059237
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:15:51.473933
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:15:52.884351
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 02:16:02.758494
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-10-25 02:16:16.166131
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 02:16:25.089784
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012'
    ) == '2a4547a0012'

# Generated at 2026-10-25 02:16:32.676955
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 02:16:40.643001
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-25 02:16:49.567174
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012'
    ) == '2a4547a0012'

# Generated at 2026-10-25 02:16:51.984129
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:16:53.634153
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 02:17:02.773020
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

    test_url = (
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    assert ie.suitable(test_url)
    assert ie._match_id(test_url) == (
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 02:17:11.272090
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 02:17:19.463949
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'

# Generated at 2026-10-25 02:17:26.959698
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.ie_key() == 'ITV'
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert not ie.suitable('https://www.example.com/video/123')

# Generated at 2026-10-25 02:17:35.131617
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-10-25 02:17:43.532058
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False

# Generated at 2026-10-25 02:17:51.689729
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    assert isinstance(ie, ITVBTCCIE)
    assert ie._downloader is None
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2026-10-25 02:17:59.810276
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-10-25 02:18:08.514628
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012'
    ) == '2a4547a0012'

# Generated at 2026-10-25 02:18:17.117976
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    assert isinstance(ie, ITVBTCCIE)
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:18:25.820345
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:18:34.925598
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

# Generated at 2026-10-25 02:18:43.228331
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 02:18:45.751385
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:18:48.169510
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:18:50.582096
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:18:52.998637
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:18:55.413872
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:18:58.035453
# Unit test for constructor of class ITVIE
def test_ITVIE():from youtube_dl.extractor.itv import ITVIE

# Generated at 2026-10-25 02:19:08.112966
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITV'
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-10-25 02:19:16.304327
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012'
    ) == '2a4547a0012'

# Generated at 2026-10-25 02:19:24.494923
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITV'
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:19:34.121851
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:19:42.722699
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()

    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is downloader
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:19:50.965506
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'

# Generated at 2026-10-25 02:19:53.383116
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:19:55.797840
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:19:58.212336
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:20:11.534585
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie.ie_key() == 'ITV'

    test_url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ie.suitable(test_url)
    assert ie._match_id(test_url) == '2a4547a0012'

# Generated at 2026-10-25 02:20:20.302532
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-25 02:20:28.126941
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:20:39.656764
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-25 02:20:48.564992
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()

    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'

# Generated at 2026-10-25 02:20:50.982406
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:20:53.397601
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:20:55.978780
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:20:58.393165
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:21:00.808065
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:21:09.559190
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 02:21:19.364139
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITV'
    assert extractor.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 02:21:29.109153
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'

    test_url = (
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == (
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 02:21:47.245217
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:21:52.668089
# Unit test for constructor of class ITVIE
def test_ITVIE():extractor = ITVIE()

# Generated at 2026-10-25 02:21:55.336003
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:21:57.751498
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:22:00.166015
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:22:02.581830
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:22:06.698038
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE(None)

# Generated at 2026-10-25 02:22:14.878630
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'

# Generated at 2026-10-25 02:22:23.021829
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2026-10-25 02:22:31.376762
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'ITVBTCC'

# Generated at 2026-10-25 02:22:39.877386
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor._match_id(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    ) == 'btcc-2018-all-the-action-from-brands-hatch'
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:22:49.579404
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')
    assert extractor._match_id(
        'https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

# Generated at 2026-10-25 02:22:55.638586
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:22:58.052474
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:23:00.468939
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:23:02.882220
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:23:05.299072
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:23:07.714117
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:23:10.131794
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:23:14.800803
# Unit test for constructor of class ITVIE
def test_ITVIE():extractor = ITVIE()

# Generated at 2026-10-25 02:23:24.359330
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'

    test_url = (
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == (
        'btcc-2018-all-the-action-from-brands-hatch'
    )