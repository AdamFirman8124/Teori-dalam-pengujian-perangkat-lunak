

# Generated at 2026-10-25 03:59:10.314586
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 03:59:18.608376
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-25 03:59:59.247283
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is None
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 04:00:07.966266
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._match_id(
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    ) == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 04:00:15.777634
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

# Generated at 2026-10-25 04:00:26.143118
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2026-10-25 04:00:28.690659
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:00:31.110297
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:00:33.526261
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:00:35.943468
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:00:38.366509
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:00:40.954569
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:00:43.482548
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:00:45.896283
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:00:48.320860
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:00:50.926730
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

# Generated at 2026-10-25 04:01:01.831061
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 04:01:12.274145
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 04:01:19.239984
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 04:01:28.000596
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 04:01:30.416232
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:01:32.831056
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:01:35.246635
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:01:37.662616
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:01:40.076842
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:01:42.492832
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:01:44.908612
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:01:47.323751
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:01:49.741592
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:01:52.153280
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:01:54.569015
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:01:57.331670
# Unit test for constructor of class ITVIE
def test_ITVIE():from youtube_dl.extractor.itv import ITVIE

# Generated at 2026-10-25 04:02:03.986815
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 04:03:15.768092
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-25 04:03:26.418880
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()

    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 04:03:35.559573
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

# Generated at 2026-10-25 04:03:45.669245
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None

# Generated at 2026-10-25 04:03:48.204352
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:03:50.727938
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:03:53.145197
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:03:55.697867
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:03:58.113273
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:04:00.728774
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 04:04:10.551789
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2026-10-25 04:04:19.255668
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s')

# Generated at 2026-10-25 04:04:28.379845
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-25 04:04:36.736847
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()

    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'

# Generated at 2026-10-25 04:04:39.266328
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:04:41.680052
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:04:44.209359
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:04:46.623750
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:04:49.037533
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:04:51.454100
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:04:53.868570
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:04:56.289300
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:04:58.886049
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:05:01.303162
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:05:03.719880
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:05:06.141673
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:05:08.555828
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:05:10.970523
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:05:13.386153
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:05:22.846910
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 04:05:32.474256
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

    test_url = (
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == (
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    assert extractor.BRIGHTCOVE_URL_TEMPLATE % '12345' == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=12345'
    )

# Generated at 2026-10-25 04:05:38.918424
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-25 04:05:49.556383
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Constructor uses the default downloader when none is supplied
    extractor = ITVBTCCIE()
    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is None

    # An explicitly supplied downloader is retained
    downloader = object()
    extractor = ITVBTCCIE(downloader)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'

# Generated at 2026-10-25 04:05:52.102053
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:05:54.508749
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:05:56.923693
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:05:59.343921
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:01.757596
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:04.172720
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:06.589815
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:09.005432
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:11.419376
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:13.834285
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:16.249256
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:18.666189
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:21.082178
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:23.499395
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:25.915851
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:28.334797
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:30.751382
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:33.172851
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:35.586981
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:06:38.002042
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:06:40.421588
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:06:42.836549
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:06:45.251260
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:06:47.665617
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:06:50.080825
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:52.495668
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:54.909927
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:57.325234
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:06:59.739536
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:02.154047
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:04.570314
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:06.985699
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:09.404644
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:11.828958
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:14.244803
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:16.670502
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:19.078104
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:21.492899
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:23.907713
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:26.323935
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:28.736905
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:31.153170
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:33.568691
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:35.982337
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:38.396860
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:40.818357
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:43.236739
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:45.656468
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:07:48.079544
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:50.497242
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:52.912036
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:55.847623
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:07:58.271045
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:08:00.692603
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 04:08:03.151136
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:08:05.568008
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:08:07.981130
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:08:10.395654
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:08:12.810666
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:08:15.225160
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:08:17.640145
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:08:20.054557
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 04:08:22.971796
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 04:08:32.494094
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 04:08:41.162985
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

# Generated at 2026-10-25 04:08:49.901837
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 04:09:00.142007
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()

    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader