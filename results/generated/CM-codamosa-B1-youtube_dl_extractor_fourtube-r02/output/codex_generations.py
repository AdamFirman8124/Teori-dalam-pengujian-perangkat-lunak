

# Generated at 2026-10-24 06:55:36.663174
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

# Generated at 2026-10-24 06:55:39.080345
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:55:41.646978
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:55:44.062329
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 06:55:46.601327
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:55:49.013943
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:55:51.431012
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:55:52.848500
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

# Generated at 2026-10-24 06:55:54.480431
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

# Generated at 2026-10-24 06:56:25.919106
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    from .fourtube import PornerBrosIE, FourTubeBaseIE

    # No custom __init__ - uses InfoExtractor / FourTubeBaseIE constructor
    assert PornerBrosIE.__init__ is FourTubeBaseIE.__init__

    # Can construct with no args and with explicit downloader
    ie = PornerBrosIE()
    assert isinstance(ie, FourTubeBaseIE)

    ie_with_none = PornerBrosIE(None)
    assert isinstance(ie_with_none, PornerBrosIE)

    class DummyDownloader(object):
        pass

    ie_with_dl = PornerBrosIE(DummyDownloader())
    assert isinstance(ie_with_dl, PornerBrosIE)

    # Class-level config set correctly
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._VALID_URL is not None

    # _VALID_URL matches expected forms
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://www.pornerbros.com/videos/test-video_181369')
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')

# Generated at 2026-10-24 06:56:28.338810
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:56:30.751870
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:56:33.258756
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 06:56:35.674001
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:56:38.089834
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:56:40.504820
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:56:42.919426
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:56:45.333276
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:56:47.748975
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:56:50.166942
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:56:52.581343
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:56:54.997480
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:56:57.416575
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:57:16.658618
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 06:57:28.791249
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():ie = FourTubeBaseIE()

# Generated at 2026-10-24 06:57:30.125987
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

# Generated at 2026-10-24 06:57:31.554616
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

# Generated at 2026-10-24 06:57:58.589584
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie.IE_NAME == 'PornerBros'
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.pornerbros.com/videos/')

    mobj = ie._match_id('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj == '181369'

    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-24 06:58:15.114494
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie.IE_NAME == 'PornerBros'
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.pornerbros.com/videos/')

    mobj = ie._match_id('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj == '181369'

    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-24 06:58:16.610062
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

# Generated at 2026-10-24 06:58:31.869271
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # 1. constructor / inheritance
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # 2. class configuration
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # 3. URL matching
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'

# Generated at 2026-10-24 06:58:44.164302
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # 1. constructor / inheritance
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # 2. class configuration
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # 3. URL matching
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'

# Generated at 2026-10-24 06:58:55.018855
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

# Generated at 2026-10-24 06:58:57.629077
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:59:00.043093
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 06:59:02.456493
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 07:00:14.790921
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 07:00:16.215769
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-24 07:00:17.648697
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

# Generated at 2026-10-24 07:00:19.082552
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # 1. constructor / inheritance
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # 2. class configuration
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # 3. URL matching
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'

# Generated at 2026-10-24 07:00:26.036087
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

# Generated at 2026-10-24 07:00:52.602358
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():assert FourTubeBaseIE.ie_key() == 'FourTubeBase'

# Generated at 2026-10-24 07:01:12.960898
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():ie = FourTubeBaseIE()

# Generated at 2026-10-24 07:01:34.444603
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # 1. constructor / inheritance
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # 2. class configuration
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # 3. URL matching
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'

# Generated at 2026-10-24 07:03:13.266703
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Constructor returns a usable instance
    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level configuration is intact
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie.ie_key() == 'PornerBros'

    # URL matching via _VALID_URL
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole')

    # Regex group extraction
    mobj = re.match(
        PornerBrosIE._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Does not match sibling extractors' sites
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-24 07:03:14.584471
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

# Generated at 2026-10-24 07:04:02.609774
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie.IE_NAME == 'PornerBros'
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.pornerbros.com/videos/')

    mobj = ie._match_id('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj == '181369'

    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-24 07:04:04.033065
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # 1. constructor / inheritance
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # 2. class configuration
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # 3. URL matching
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'

# Generated at 2026-10-24 07:04:06.458311
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 07:04:08.985646
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 07:04:11.403587
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 07:04:13.821870
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 07:04:16.236034
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 07:04:23.785958
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():ie = PornTubeIE()

# Generated at 2026-10-24 07:04:42.875060
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

# Generated at 2026-10-24 07:04:59.310244
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

# Generated at 2026-10-24 07:05:00.739840
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

# Generated at 2026-10-24 07:05:02.192268
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # 1. constructor / inheritance
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # 2. class configuration
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # 3. URL matching
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'

# Generated at 2026-10-24 07:05:03.636775
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # 1. constructor / inheritance
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # 2. class configuration
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # 3. URL matching
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    mobj = re.match(FuxIE._VALID_URL, 'https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'

# Generated at 2026-10-24 07:05:06.170727
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 07:05:08.695244
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 07:05:11.192626
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 07:05:13.607466
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 07:05:16.022720
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 07:05:24.056749
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE(None)