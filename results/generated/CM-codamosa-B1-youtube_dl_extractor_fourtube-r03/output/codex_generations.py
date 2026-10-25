

# Generated at 2026-10-24 13:48:39.922773
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:48:41.394981
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

# Generated at 2026-10-24 13:48:42.825952
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:48:44.266879
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

# Generated at 2026-10-24 13:48:45.709728
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

# Generated at 2026-10-24 13:48:47.233737
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

# Generated at 2026-10-24 13:48:56.954667
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'PornTube'
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.porntube.com/videos/video_%s')

# Generated at 2026-10-24 13:48:59.310163
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:49:00.675568
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:49:02.070914
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

# Generated at 2026-10-24 13:49:03.493006
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

# Generated at 2026-10-24 13:49:05.920854
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:08.336664
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:10.897973
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:13.317505
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:15.984584
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:18.399301
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:20.811530
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:49:23.231200
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:49:25.657488
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:49:28.069098
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:49:30.481636
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:49:36.594089
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-24 13:49:38.118529
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

# Generated at 2026-10-24 13:49:39.551583
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:49:40.951119
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:49:42.420735
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

# Generated at 2026-10-24 13:49:43.803542
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:49:45.287926
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:49:53.274442
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    downloader = object()
    extractor = FourTubeIE(downloader)

    assert isinstance(extractor, FourTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == '4tube'
    assert extractor._ready is False

# Generated at 2026-10-24 13:49:54.707181
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

# Generated at 2026-10-24 13:49:56.153512
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

# Generated at 2026-10-24 13:49:57.491538
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:49:59.017530
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

# Generated at 2026-10-24 13:50:00.442029
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:50:01.877568
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

# Generated at 2026-10-24 13:50:03.322500
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

# Generated at 2026-10-24 13:50:04.745026
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:50:06.130712
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:50:07.603511
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

# Generated at 2026-10-24 13:50:09.012081
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:50:10.401222
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:50:11.795119
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

# Generated at 2026-10-24 13:50:14.333803
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:50:16.747186
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:50:19.344150
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:50:21.883061
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:50:24.618152
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:50:27.032658
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:50:29.446883
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:50:31.860943
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:50:36.868187
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():extractor = PornTubeIE()

# Generated at 2026-10-24 13:50:38.308542
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

# Generated at 2026-10-24 13:50:39.710850
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:50:41.040979
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:50:42.531796
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:50:43.963133
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:50:45.387100
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

# Generated at 2026-10-24 13:50:46.831310
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

# Generated at 2026-10-24 13:50:48.262992
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

# Generated at 2026-10-24 13:50:49.696515
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:50:51.130507
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

# Generated at 2026-10-24 13:50:52.545527
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

# Generated at 2026-10-24 13:50:53.920618
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:50:55.294535
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:50:57.875175
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:00.290977
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:02.706990
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:05.129030
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:07.543952
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:09.960735
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:12.381973
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:14.798884
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:17.214221
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:19.628447
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:22.041872
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:24.456570
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:27.243608
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:29.660215
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:32.272141
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:34.684950
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:51:37.098688
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:51:39.511854
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:51:41.924697
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:51:44.338078
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:51:46.754811
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:51:49.175605
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:51.591420
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:54.004297
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:56.421270
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:58.834438
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:52:01.250324
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:52:12.089543
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-24 13:52:13.448830
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:52:14.898326
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

# Generated at 2026-10-24 13:52:16.874006
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:52:18.197060
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:52:21.625766
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

# Generated at 2026-10-24 13:52:23.211322
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

# Generated at 2026-10-24 13:52:24.604451
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

# Generated at 2026-10-24 13:52:26.047182
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

# Generated at 2026-10-24 13:52:27.389981
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:52:28.721550
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:52:31.235180
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:33.799771
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:36.397525
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:38.811025
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:41.229490
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:43.652257
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:46.248943
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:52:48.664567
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:52:51.079414
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:52:53.492912
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:52:55.912142
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:52:58.330753
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:53:05.311096
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:53:07.727650
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:53:10.142969
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:53:12.558784
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:14.974520
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:42.752003
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():ie = FourTubeBaseIE()

# Generated at 2026-10-24 13:53:44.314976
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:53:45.825137
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:53:47.566672
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:53:48.897396
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:53:50.293576
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:53:52.798342
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:55.214086
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:57.640008
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:54:00.055750
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:54:02.472419
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:54:04.889595
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:54:07.303165
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:54:09.720302
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:54:12.129584
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:54:22.287611
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:54:23.903642
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:25.239480
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:26.578023
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:28.116600
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:54:29.538909
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:54:30.989761
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:54:32.361423
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:54:33.715460
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:35.033170
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:53.398898
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:54.865308
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:56.206076
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:57.576654
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:54:59.043743
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

# Generated at 2026-10-24 13:55:01.586187
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:55:04.207460
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:55:06.619930
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:55:09.193428
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:55:11.607736
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:55:14.022391
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:55:16.573702
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:55:19.150702
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:55:21.568215
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:55:54.236893
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-24 13:55:55.670601
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

# Generated at 2026-10-24 13:56:49.838665
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:56:51.272601
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .fourtube import FourTubeIE, FourTubeBaseIE
    from .common import InfoExtractor

    # 1. default construction - no custom __init__, uses InfoExtractor.__init__(downloader=None)
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # 2. construction with downloader
    downloader = object()
    ie_with_dl = FourTubeIE(downloader)
    assert ie_with_dl._downloader is downloader

    # 3. class attributes correctly set on instance
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # 4. _VALID_URL is usable
    assert FourTubeIE.suitable('https://www.4tube.com/videos/209733/video')
    assert FourTubeIE.suitable('https://www.4tube.com/embed/209733')

# Generated at 2026-10-24 13:56:52.705972
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

# Generated at 2026-10-24 13:56:54.139533
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

# Generated at 2026-10-24 13:56:55.513922
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:56:56.904737
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Base class instantiates like any InfoExtractor (no downloader needed)
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)

    # Base class defines no IE_NAME of its own
    assert ie.ie_key() is None

    # _TKN_HOST is a per-site setting â base must NOT have it
    assert not hasattr(ie, '_TKN_HOST')

    # Concrete subclasses must set _TKN_HOST and _VALID_URL
    for cls in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub = cls()
        assert sub._TKN_HOST, '%s missing _TKN_HOST' % cls.__name__
        assert sub._VALID_URL, '%s missing _VALID_URL' % cls.__name__

# Generated at 2026-10-24 13:56:58.230706
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:56:59.562451
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:57:01.009383
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

# Generated at 2026-10-24 13:57:03.537308
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:57:05.951715
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:57:08.366834
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:58:37.872099
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:58:40.400324
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:58:59.279192
# Unit test for constructor of class PornTubeIE