

# Generated at 2026-10-24 06:15:34.715599
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert extractor.suitable('https://www.fux.com/embed/195359')
    assert not extractor.suitable('https://www.example.com/video/195359')

# Generated at 2026-10-24 06:15:43.765444
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    downloader = object()
    extractor = FourTubeIE(downloader)

    assert isinstance(extractor, FourTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == '4tube'
    assert extractor._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert extractor._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-24 06:15:46.392316
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:15:48.808634
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:15:51.230106
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:15:53.816277
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:15:56.231167
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:15:58.646829
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:16:01.063549
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:16:12.127388
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-24 06:16:21.878393
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    downloader = object()

    extractor = FourTubeBaseIE(downloader)

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-24 06:16:39.164685
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'

    assert ie.suitable(
        'https://www.pornerbros.com/videos/example-video_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable(
        'https://m.pornerbros.com/videos/example-video_181369')
    assert not ie.suitable('https://www.4tube.com/videos/181369/example-video')

# Generated at 2026-10-24 06:16:48.117999
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    extractor = FourTubeBaseIE()

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-24 06:17:02.918313
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:17:13.056632
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    downloader = object()
    extractor = FourTubeIE(downloader)

    assert isinstance(extractor, FourTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == '4tube'
    assert extractor._TKN_HOST == 'token.4tube.com'
    assert extractor._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

# Generated at 2026-10-24 06:17:14.489749
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:17:22.957825
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-24 06:17:32.923701
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 06:17:34.354527
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:17:43.166670
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    downloader = object()
    extractor = FourTubeIE(downloader)

    assert isinstance(extractor, FourTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == '4tube'
    assert extractor._TKN_HOST == 'token.4tube.com'
    assert extractor._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

# Generated at 2026-10-24 06:17:52.486842
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    extractor = FourTubeBaseIE()

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 06:18:13.180021
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-24 06:18:31.599579
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()

    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'PornerBros'
    assert extractor._TKN_HOST == 'token.pornerbros.com'

# Generated at 2026-10-24 06:18:41.633118
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:18:47.021164
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-24 06:18:56.686649
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie.suitable(
        'https://www.pornerbros.com/videos/example-video_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')

# Generated at 2026-10-24 06:19:04.392101
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    downloader = object()
    extractor = FourTubeBaseIE(downloader)

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 06:19:14.373295
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-24 06:19:24.325315
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 06:19:25.848602
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:19:27.419393
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:19:34.985496
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-24 06:19:36.521301
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:19:57.105105
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()

    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 06:20:07.037126
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()

    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 06:20:17.302099
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-24 06:20:18.811721
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:20:25.663135
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    downloader = object()
    extractor = FourTubeBaseIE(downloader)

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-24 06:20:33.867631
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    downloader = object()
    extractor = FourTubeBaseIE(downloader)

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-24 06:20:42.261173
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')
    assert extractor._TKN_HOST == 'token.pornerbros.com'

# Generated at 2026-10-24 06:20:57.928036
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-24 06:21:11.971151
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    downloader = object()

    extractor = FourTubeBaseIE(downloader)

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-24 06:21:21.317728
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 06:21:22.914901
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:21:34.250069
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    downloader = object()
    extractor = FourTubeBaseIE(downloader)

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-24 06:21:35.786465
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:21:37.456653
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:21:48.719158
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:21:53.548720
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-24 06:21:55.967746
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:21:58.464922
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:22:00.877862
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:22:03.293823
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:22:10.431181
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-24 06:22:11.813539
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:22:13.209401
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:22:23.340895
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s'
    )
    assert extractor.suitable(
        'https://www.pornerbros.com/videos/example-video_181369'
    )

# Generated at 2026-10-24 06:22:42.274153
# Unit test for constructor of class FuxIE
def test_FuxIE():
    class DummyDownloader:
        params = {}

    downloader = DummyDownloader()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow'
    )

# Generated at 2026-10-24 06:22:52.956288
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:22:55.373627
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:22:57.876565
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:23:00.291206
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:23:02.716346
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:23:05.120466
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:23:07.534768
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:23:09.949026
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:23:12.368412
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:23:14.784221
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:23:28.377478
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE(None)

# Generated at 2026-10-24 06:23:36.546646
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    downloader = object()

    extractor = FourTubeBaseIE(downloader)

    assert isinstance(extractor, FourTubeBaseIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 06:23:45.865023
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 06:23:55.244367
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert extractor.suitable('https://www.fux.com/embed/195359')
    assert not extractor.suitable('https://www.4tube.com/videos/209733/video')

# Generated at 2026-10-24 06:23:56.728422
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # constructor should work with and without downloader
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornTubeIE(downloader=None)
    assert isinstance(ie_with_none, PornTubeIE)

    # class configuration
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._VALID_URL, str)

    # _VALID_URL matching
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'

    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('kind') == 'm'

    # should not match other sites
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None
    assert re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369') is None

# Generated at 2026-10-24 06:24:05.489494
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-24 06:24:08.010777
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:24:10.512719
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:24:12.925931
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:24:15.343061
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:24:17.758202
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:24:41.729596
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():extractor = PornTubeIE()

# Generated at 2026-10-24 06:24:51.840911
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 06:25:01.744275
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-24 06:25:04.160106
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:25:06.578012
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:25:09.085930
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:25:11.499646
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 06:25:13.914166
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 06:25:16.329851
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 06:25:18.743264
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 06:25:21.161017
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 06:25:23.572787
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 06:25:25.987480
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:25:28.400943
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:25:36.150113
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()