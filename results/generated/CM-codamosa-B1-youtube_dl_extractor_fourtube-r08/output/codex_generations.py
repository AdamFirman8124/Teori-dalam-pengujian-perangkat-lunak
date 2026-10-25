

# Generated at 2026-10-24 04:03:46.867410
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')
    assert re.match(
        extractor._VALID_URL,
        'https://www.pornerbros.com/videos/example-video_181369')

# Generated at 2026-10-24 04:04:59.876397
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:05:13.187179
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # 1. Default construction (inherited InfoExtractor.__init__)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False

    # 2. Construction with a downloader
    downloader = unittest.mock.Mock(params={})
    ie2 = FourTubeBaseIE(downloader=downloader)
    assert ie2._downloader is downloader

    # 3. All subclasses use the same constructor
    for cls, host in [
        (FourTubeIE, 'token.4tube.com'),
        (FuxIE, 'token.fux.com'),
        (PornTubeIE, 'tkn.porntube.com'),
        (PornerBrosIE, 'token.pornerbros.com'),
    ]:
        sub = cls(downloader=downloader)
        assert isinstance(sub, FourTubeBaseIE)
        assert sub._TKN_HOST == host
        assert sub._downloader is downloader

# Generated at 2026-10-24 04:05:16.333425
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:05:54.584154
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor instantiates without a downloader
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes are set correctly
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # IE_NAME is inherited from the base class (not overridden)
    assert ie.IE_NAME == 'FourTubeBase'

    # _VALID_URL matches real URLs and rejects other sites
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/not-a-video-id')

    # Group extraction from a valid URL
    mobj = re.match(PornTubeIE._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    assert mobj.group('kind') is None

# Generated at 2026-10-24 04:06:18.934288
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-24 04:06:21.354224
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:06:23.771375
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:06:49.167193
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():extractor = FourTubeBaseIE()

# Generated at 2026-10-24 04:07:14.747548
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.porntube.com/videos/video_%s')
    assert re.match(
        extractor._VALID_URL,
        'https://www.porntube.com/videos/example-video_12345')

# Generated at 2026-10-24 04:07:42.492388
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    print('test_FourTubeIE passed')


test_FourTubeIE()

# Generated at 2026-10-24 04:07:43.810569
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    print('test_FourTubeIE passed')


test_FourTubeIE()

# Generated at 2026-10-24 04:07:45.121973
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:08:07.678521
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-24 04:08:09.111564
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:08:10.447436
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    print('test_FourTubeIE passed')


test_FourTubeIE()

# Generated at 2026-10-24 04:08:11.777994
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # 1. Default construction (inherited InfoExtractor.__init__)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False

    # 2. Construction with a downloader
    downloader = unittest.mock.Mock(params={})
    ie2 = FourTubeBaseIE(downloader=downloader)
    assert ie2._downloader is downloader

    # 3. All subclasses use the same constructor
    for cls, host in [
        (FourTubeIE, 'token.4tube.com'),
        (FuxIE, 'token.fux.com'),
        (PornTubeIE, 'tkn.porntube.com'),
        (PornerBrosIE, 'token.pornerbros.com'),
    ]:
        sub = cls(downloader=downloader)
        assert isinstance(sub, FourTubeBaseIE)
        assert sub._TKN_HOST == host
        assert sub._downloader is downloader

# Generated at 2026-10-24 04:08:13.113576
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:08:14.448434
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    print('test_FourTubeIE passed')


test_FourTubeIE()

# Generated at 2026-10-24 04:08:15.780643
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:08:25.265717
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'

# Generated at 2026-10-24 04:08:27.682964
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:08:30.099857
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:08:32.600210
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:08:35.016344
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:08:37.433210
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:08:39.846851
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:08:41.211443
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # 1. Default construction (inherited InfoExtractor.__init__)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False

    # 2. Construction with a downloader
    downloader = unittest.mock.Mock(params={})
    ie2 = FourTubeBaseIE(downloader=downloader)
    assert ie2._downloader is downloader

    # 3. All subclasses use the same constructor
    for cls, host in [
        (FourTubeIE, 'token.4tube.com'),
        (FuxIE, 'token.fux.com'),
        (PornTubeIE, 'tkn.porntube.com'),
        (PornerBrosIE, 'token.pornerbros.com'),
    ]:
        sub = cls(downloader=downloader)
        assert isinstance(sub, FourTubeBaseIE)
        assert sub._TKN_HOST == host
        assert sub._downloader is downloader

# Generated at 2026-10-24 04:08:57.854630
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor instantiates without a downloader
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes are set correctly
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # IE_NAME is inherited from the base class (not overridden)
    assert ie.IE_NAME == 'FourTubeBase'

    # _VALID_URL matches real URLs and rejects other sites
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/not-a-video-id')

    # Group extraction from a valid URL
    mobj = re.match(PornTubeIE._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    assert mobj.group('kind') is None

# Generated at 2026-10-24 04:08:59.172020
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    print('test_FourTubeIE passed')


test_FourTubeIE()

# Generated at 2026-10-24 04:09:00.504364
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:09:10.859401
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')
    assert extractor.suitable(
        'https://www.pornerbros.com/videos/example-video_181369')
    assert extractor.suitable(
        'https://www.pornerbros.com/embed/181369')

# Generated at 2026-10-24 04:09:12.192585
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:09:13.527456
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # 1. Default construction (inherited InfoExtractor.__init__)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False

    # 2. Construction with a downloader
    downloader = unittest.mock.Mock(params={})
    ie2 = FourTubeBaseIE(downloader=downloader)
    assert ie2._downloader is downloader

    # 3. All subclasses use the same constructor
    for cls, host in [
        (FourTubeIE, 'token.4tube.com'),
        (FuxIE, 'token.fux.com'),
        (PornTubeIE, 'tkn.porntube.com'),
        (PornerBrosIE, 'token.pornerbros.com'),
    ]:
        sub = cls(downloader=downloader)
        assert isinstance(sub, FourTubeBaseIE)
        assert sub._TKN_HOST == host
        assert sub._downloader is downloader

# Generated at 2026-10-24 04:09:16.031924
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:09:18.546287
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:09:20.963731
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:09:23.383177
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 04:09:25.803089
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 04:09:28.325184
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 04:09:30.742036
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 04:09:33.157713
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 04:09:35.574969
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 04:09:44.550134
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():extractor = PornTubeIE()

# Generated at 2026-10-24 04:09:45.867662
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:09:58.373845
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor.ie_key() == 'PornerBros'

# Generated at 2026-10-24 04:10:08.202989
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-24 04:10:09.541728
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:10:10.865797
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:10:27.353342
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor instantiates without a downloader
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes are set correctly
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # IE_NAME is inherited from the base class (not overridden)
    assert ie.IE_NAME == 'FourTubeBase'

    # _VALID_URL matches real URLs and rejects other sites
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/not-a-video-id')

    # Group extraction from a valid URL
    mobj = re.match(PornTubeIE._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    assert mobj.group('kind') is None

# Generated at 2026-10-24 04:10:37.388415
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 04:10:50.592350
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-24 04:11:03.619731
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 04:11:05.011008
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-24 04:11:06.345927
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:11:07.653880
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # 1. Default construction (inherited InfoExtractor.__init__)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False

    # 2. Construction with a downloader
    downloader = unittest.mock.Mock(params={})
    ie2 = FourTubeBaseIE(downloader=downloader)
    assert ie2._downloader is downloader

    # 3. All subclasses use the same constructor
    for cls, host in [
        (FourTubeIE, 'token.4tube.com'),
        (FuxIE, 'token.fux.com'),
        (PornTubeIE, 'tkn.porntube.com'),
        (PornerBrosIE, 'token.pornerbros.com'),
    ]:
        sub = cls(downloader=downloader)
        assert isinstance(sub, FourTubeBaseIE)
        assert sub._TKN_HOST == host
        assert sub._downloader is downloader

# Generated at 2026-10-24 04:11:08.963193
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    print('test_FourTubeIE passed')


test_FourTubeIE()

# Generated at 2026-10-24 04:11:10.275565
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # 1. Default construction (inherited InfoExtractor.__init__)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False

    # 2. Construction with a downloader
    downloader = unittest.mock.Mock(params={})
    ie2 = FourTubeBaseIE(downloader=downloader)
    assert ie2._downloader is downloader

    # 3. All subclasses use the same constructor
    for cls, host in [
        (FourTubeIE, 'token.4tube.com'),
        (FuxIE, 'token.fux.com'),
        (PornTubeIE, 'tkn.porntube.com'),
        (PornerBrosIE, 'token.pornerbros.com'),
    ]:
        sub = cls(downloader=downloader)
        assert isinstance(sub, FourTubeBaseIE)
        assert sub._TKN_HOST == host
        assert sub._downloader is downloader

# Generated at 2026-10-24 04:11:19.984469
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-24 04:11:22.491865
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:11:24.904928
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:11:27.319312
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:11:29.742645
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 04:11:32.160058
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 04:11:34.578528
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 04:11:37.153167
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:11:39.567841
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:11:41.986775
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:11:44.400665
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:11:46.817533
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:11:49.236694
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 04:11:51.649821
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 04:11:54.067899
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 04:11:56.483005
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 04:12:22.757761
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 04:12:24.081362
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # 1. Default construction (inherited InfoExtractor.__init__)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False

    # 2. Construction with a downloader
    downloader = unittest.mock.Mock(params={})
    ie2 = FourTubeBaseIE(downloader=downloader)
    assert ie2._downloader is downloader

    # 3. All subclasses use the same constructor
    for cls, host in [
        (FourTubeIE, 'token.4tube.com'),
        (FuxIE, 'token.fux.com'),
        (PornTubeIE, 'tkn.porntube.com'),
        (PornerBrosIE, 'token.pornerbros.com'),
    ]:
        sub = cls(downloader=downloader)
        assert isinstance(sub, FourTubeBaseIE)
        assert sub._TKN_HOST == host
        assert sub._downloader is downloader

# Generated at 2026-10-24 04:12:45.795833
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:12:52.045836
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():extractor = PornTubeIE()

# Generated at 2026-10-24 04:12:53.359156
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:12:54.672602
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor instantiates without a downloader
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes are set correctly
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # IE_NAME is inherited from the base class (not overridden)
    assert ie.IE_NAME == 'FourTubeBase'

    # _VALID_URL matches real URLs and rejects other sites
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/not-a-video-id')

    # Group extraction from a valid URL
    mobj = re.match(PornTubeIE._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    assert mobj.group('kind') is None

# Generated at 2026-10-24 04:12:56.126516
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:12:57.442107
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie.IE_NAME == 'Fux'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    m = ie._match_id('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # _match_id returns (id, display_id, ...) tuple depending on version;
    # safer to test the regex directly:
    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('kind') is None  # 'www' host doesn't capture kind
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    print("test_FuxIE passed")


test_FuxIE()

# Generated at 2026-10-24 04:13:07.307689
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()

    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s'
    )
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor.suitable(
        'https://www.pornerbros.com/videos/example-video_181369'
    )

# Generated at 2026-10-24 04:13:08.634486
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    print('test_FourTubeIE passed')


test_FourTubeIE()

# Generated at 2026-10-24 04:13:09.953431
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor instantiates without a downloader
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Class attributes are set correctly
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # IE_NAME is inherited from the base class (not overridden)
    assert ie.IE_NAME == 'FourTubeBase'

    # _VALID_URL matches real URLs and rejects other sites
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    assert not ie.suitable('https://www.porntube.com/videos/not-a-video-id')

    # Group extraction from a valid URL
    mobj = re.match(PornTubeIE._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    assert mobj.group('kind') is None

# Generated at 2026-10-24 04:13:11.275130
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/foo')
    print('test_FourTubeIE passed')


test_FourTubeIE()

# Generated at 2026-10-24 04:13:13.830548
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:13:16.246536
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:13:18.663823
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 04:13:21.082111
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:13:23.497492
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:13:25.913929
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:13:28.332555
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:13:30.749604
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 04:13:33.322510
# Unit test for constructor of class PornTubeIE