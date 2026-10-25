

# Generated at 2026-10-24 23:31:52.763038
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    extractor = FourTubeBaseIE()

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 23:31:55.183935
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:31:57.601644
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:32:00.016344
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:32:02.435914
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:32:04.852959
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:32:07.271629
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:32:09.687570
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:32:12.102938
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:32:14.519422
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:32:16.936955
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:32:19.357567
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:32:34.029362
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-24 23:32:43.860534
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-24 23:32:52.101818
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-24 23:33:07.515859
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Constructor should work with no args (downloader=None)
    ie = FourTubeIE()

    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level config specific to 4tube
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

    # _VALID_URL must be defined and match expected URL forms
    assert ie._VALID_URL
    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/video')
    assert m is not None
    assert m.group('id') == '209733'

# Generated at 2026-10-24 23:33:16.526029
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s'
    )

# Generated at 2026-10-24 23:33:26.868107
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-24 23:33:34.617213
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._VALID_URL == FuxIE._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-24 23:33:42.835535
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    downloader = object()

    extractor = FourTubeBaseIE(downloader)

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 23:33:54.721999
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None

# Generated at 2026-10-24 23:34:03.549256
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-24 23:34:05.968752
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:34:08.386019
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:34:10.804501
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:34:13.220765
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:34:15.635409
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:34:18.051245
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:34:20.466226
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:34:50.020064
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:34:58.721129
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():ie = FourTubeBaseIE()

    # Constructor creates a working instance of the extractor base class

# Generated at 2026-10-24 23:35:01.252362
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:03.670896
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:06.262249
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:08.684334
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:35:11.097922
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:35:13.514314
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:35:16.101221
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:35:18.520411
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:35:20.937473
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:35:23.357658
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:25.778626
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:28.195455
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:30.612929
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:35:33.040899
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:35:35.459853
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:35:37.878293
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:40.292469
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:42.707623
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:45.130614
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:47.545580
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:49.964778
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:35:52.382561
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:35:54.798948
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:35:57.214542
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:35:59.635495
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:02.051795
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:04.468365
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:06.888296
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:36:09.311526
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:36:11.724101
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:36:14.146164
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:16.560488
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:18.979174
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:21.398196
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:36:23.816496
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:36:26.236565
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:36:28.652680
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:36:31.068925
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:36:33.490154
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:36:35.909210
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:38.324280
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:40.744604
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:43.160418
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:45.582256
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:47.996543
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:36:50.411986
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:36:52.826708
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:36:55.245491
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:36:57.662750
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:00.078410
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:02.495497
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:04.910232
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:07.326876
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:09.742099
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:12.160492
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:14.575947
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:16.992348
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:37:19.408192
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:21.828485
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:24.244019
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:26.662255
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:29.079239
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:31.496108
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:33.912829
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:36.330278
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:38.749164
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:41.169349
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:37:43.589979
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:37:46.013759
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:37:48.433143
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:50.849864
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:53.267039
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:37:55.686420
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:37:58.101304
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:38:00.518854
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:38:02.936234
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:38:05.352756
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:38:07.769815
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:38:10.185776
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:12.600867
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:15.018363
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:17.433885
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:38:19.850180
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:38:22.267041
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:38:24.684014
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:27.101048
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:29.521047
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:31.936024
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:34.353885
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:36.773625
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:39.187866
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:41.606099
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:44.021474
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:38:46.438121
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:38:48.856948
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:38:51.272773
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:38:53.689945
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:38:56.108972
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:38:58.537059
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:39:00.952263
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:39:03.369848
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:39:05.789616
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:39:13.391907
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 23:39:21.379454
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.porntube.com/videos/video_%s')

# Generated at 2026-10-24 23:39:29.939631
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 23:39:38.889790
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert re.match(
        extractor._VALID_URL,
        'https://www.fux.com/video/195359/example-video',
    )

# Generated at 2026-10-24 23:39:40.944159
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Constructor should work with no args (downloader=None)
    ie = FourTubeIE()

    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level config specific to 4tube
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

    # _VALID_URL must be defined and match expected URL forms
    assert ie._VALID_URL
    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/video')
    assert m is not None
    assert m.group('id') == '209733'

# Generated at 2026-10-24 23:39:50.767772
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor.ie_key() == 'Fux'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-24 23:39:53.305083
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:39:55.722939
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:39:58.139211
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:40:00.556545
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:02.975361
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:05.603242
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:08.022719
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:10.440831
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:12.857431
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:15.273313
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:40:17.688761
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:40:20.106092
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:40:22.522190
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:24.937416
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:27.356600
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:29.772644
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:40:32.187875
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:40:34.603907
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 23:40:37.019642
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:40:39.435809
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:40:41.856263
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 23:40:44.272508
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:46.686633
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:49.103538
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 23:40:53.634449
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:40:56.053617
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:40:58.466878
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 23:41:00.883488
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:41:03.299434
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:41:05.714910
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:41:08.134621
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 23:41:09.729284
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-24 23:41:21.086841
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-24 23:41:22.519934
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Constructor should work with no args (downloader=None)
    ie = FourTubeIE()

    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level config specific to 4tube
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

    # _VALID_URL must be defined and match expected URL forms
    assert ie._VALID_URL
    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/video')
    assert m is not None
    assert m.group('id') == '209733'

# Generated at 2026-10-24 23:41:32.256382
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-24 23:41:39.721930
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor.suitable(
        'https://www.pornerbros.com/videos/example-video_181369')

# Generated at 2026-10-24 23:41:47.811819
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s'
    )