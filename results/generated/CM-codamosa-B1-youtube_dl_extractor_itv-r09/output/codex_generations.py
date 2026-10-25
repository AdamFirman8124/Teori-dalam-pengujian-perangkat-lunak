

# Generated at 2026-10-25 02:55:21.151423
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITVBTCC'

    test_url = (
        'https://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    )
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == (
        'btcc-2018-all-the-action-from-brands-hatch'
    )

# Generated at 2026-10-25 02:55:29.957548
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert extractor._downloader is None

# Generated at 2026-10-25 02:55:32.375412
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:55:34.793554
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:55:37.208321
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:55:39.625228
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:55:42.041443
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:55:44.460000
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:55:46.880213
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:55:49.299299
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:55:54.417398
# Unit test for constructor of class ITVIE
def test_ITVIE():extractor = ITVIE()

# Generated at 2026-10-25 02:56:03.872733
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    downloader = object()
    extractor = ITVBTCCIE(downloader)

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 02:56:12.859848
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

# Generated at 2026-10-25 02:56:21.156788
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)

    test_url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == '2a4547a0012'

# Generated at 2026-10-25 02:56:23.577685
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:25.992880
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:28.409269
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:30.822308
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:33.237068
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:35.651208
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:38.066956
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:40.482280
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:42.897398
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:56:45.468601
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:47.884414
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:50.299076
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:52.714893
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:55.130365
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:57.546873
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:56:59.961356
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:02.385030
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:04.799908
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:07.214035
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:09.628653
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:12.043685
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:14.459204
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:57:16.876422
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:57:22.187608
# Unit test for constructor of class ITVIE
def test_ITVIE():extractor = ITVIE()

# Generated at 2026-10-25 02:57:31.270630
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 02:57:40.414209
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.suitable(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch')
    assert extractor._match_id(
        'http://www.itv.com/btcc/races/'
        'btcc-2018-all-the-action-from-brands-hatch'
    ) == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 02:57:43.057247
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:57:45.473701
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:57:47.890145
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:57:50.308069
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:52.886325
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:55.306107
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:57:57.730401
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:00.144103
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:02.559378
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:04.976882
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:07.390784
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:09.806556
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:12.221929
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:14.638697
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:17.055903
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:19.468965
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:21.885186
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:24.300300
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:26.716253
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:29.131258
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:31.548025
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:33.960122
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:36.375588
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:38.790810
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:41.205731
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:43.625663
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:46.040714
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:58:48.457678
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:50.871458
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:53.286975
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:58:56.045371
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:01.228885
# Unit test for constructor of class ITVIE
def test_ITVIE():extractor = ITVIE()

# Generated at 2026-10-25 02:59:10.221089
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_COUNTRIES == ['GB']
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 02:59:17.183813
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.BRIGHTCOVE_URL_TEMPLATE.endswith('videoId=%s')

# Generated at 2026-10-25 02:59:19.823049
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:22.238427
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:24.652989
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:27.070710
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:29.486837
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:31.903599
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:34.321263
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:59:36.735221
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:59:39.150257
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:59:41.564804
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:59:43.979329
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:59:46.393993
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 02:59:48.807425
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:51.221889
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:53.637201
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:56.052192
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 02:59:58.467425
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:00.882848
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:03.297229
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:05.713262
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:08.129974
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:10.543842
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:12.957643
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:15.371102
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:17.785758
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:20.198869
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:22.612133
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:25.025327
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:27.438303
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:29.851203
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:32.265562
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:34.678657
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:37.094852
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:39.507633
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:41.922127
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:44.336763
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:46.752118
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:49.164883
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:00:51.579822
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:00.837151
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'ITVBTCC'

# Generated at 2026-10-25 03:01:10.644841
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 03:01:18.733487
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

# Generated at 2026-10-25 03:01:27.039074
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.ie_key() == 'ITV'

# Generated at 2026-10-25 03:01:29.580905
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:31.994549
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:34.524621
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:36.938797
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:39.353352
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:41.769213
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:44.184206
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:46.599474
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:49.014163
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:51.429151
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:53.847509
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:56.266903
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:01:58.680625
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:01.096159
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:03.514105
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:05.926166
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:08.340505
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:10.754387
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:13.170142
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:15.584848
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:17.998674
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:22.981503
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:25.396299
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:27.811416
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:02:30.225859
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:32.639848
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:35.054558
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:37.468748
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:39.883670
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:42.298396
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:02:49.665797
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    assert isinstance(extractor, ITVIE)
    assert extractor._downloader is None
    assert extractor.suitable(
        'https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-10-25 03:02:59.815011
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert extractor._downloader is None
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2026-10-25 03:03:09.318429
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'ITV'

# Generated at 2026-10-25 03:03:11.844338
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:14.368252
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:16.783864
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:19.200609
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:21.615966
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:24.032712
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:26.612917
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:03:29.026330
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:03:31.439954
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:03:33.855681
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:36.269529
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:38.683253
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:03:47.516423
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:03:49.933678
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:03:52.348400
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:03:54.763230
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:03:57.178387
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:03:59.735380
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 03:04:09.395725
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor.suitable(ITVBTCCIE._TEST['url'])
    assert extractor._match_id(ITVBTCCIE._TEST['url']) == (
        'btcc-2018-all-the-action-from-brands-hatch')
    assert extractor.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/'
        'HkiHLnNRx_default/index.html?videoId=%s')

# Generated at 2026-10-25 03:04:17.190260
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    extractor = ITVBTCCIE()

    assert isinstance(extractor, ITVBTCCIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'ITVBTCC'
    assert extractor._downloader is None

# Generated at 2026-10-25 03:04:26.639996
# Unit test for constructor of class ITVIE
def test_ITVIE():
    downloader = object()
    extractor = ITVIE(downloader)

    assert isinstance(extractor, ITVIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None
    assert extractor._GEO_COUNTRIES == ['GB']

# Generated at 2026-10-25 03:04:29.059582
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:04:31.600664
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:04:34.015171
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:04:36.427114
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:38.844238
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:41.258185
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:43.674409
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:46.089103
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:48.503648
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:50.917671
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:53.332427
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:55.746354
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 03:04:58.161021
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:05:00.577622
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 03:05:02.991863
# Unit test for constructor of class ITVIE