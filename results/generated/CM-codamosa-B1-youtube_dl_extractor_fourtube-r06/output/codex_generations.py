

# Generated at 2026-10-24 13:46:47.220797
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:46:49.633947
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:46:52.047822
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:46:54.460875
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:46:56.874676
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:46:59.287865
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:47:01.704878
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:47:04.114620
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:47:06.528454
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:47:08.951064
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:47:11.365635
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:47:13.788101
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:47:16.211106
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:47:18.623551
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:47:21.043473
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:47:23.463854
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:47:25.874072
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:47:28.287659
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:47:30.701784
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:47:33.116021
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:47:35.529486
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:47:37.942842
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:47:40.356785
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:47:42.771658
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:47:45.186849
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:47:47.606167
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:47:50.028227
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:47:52.442480
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:47:54.861947
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:47:57.276393
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:47:59.690812
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:48:02.104713
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:48:04.524045
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:48:06.932602
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:48:09.346360
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:48:11.762531
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:48:14.199930
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:48:16.639510
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:48:19.066959
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:48:21.505851
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:48:23.934168
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:48:45.803198
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:48:47.225687
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

# Generated at 2026-10-24 13:48:48.875355
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

# Generated at 2026-10-24 13:48:50.411336
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

# Generated at 2026-10-24 13:48:51.842005
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

# Generated at 2026-10-24 13:48:53.390119
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

# Generated at 2026-10-24 13:48:54.991716
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

# Generated at 2026-10-24 13:48:56.544729
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

# Generated at 2026-10-24 13:48:59.319414
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

# Generated at 2026-10-24 13:49:00.749471
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

# Generated at 2026-10-24 13:49:02.170643
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

# Generated at 2026-10-24 13:49:03.523229
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:49:05.949357
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:49:08.367088
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:49:10.924998
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:49:13.348294
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:49:15.973676
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:49:18.387076
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:49:20.804540
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:23.222258
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:25.639298
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:49:28.054321
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:49:30.473953
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:49:37.401944
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():extractor = PornerBrosIE()

# Generated at 2026-10-24 13:49:38.973052
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

# Generated at 2026-10-24 13:49:40.311531
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:49:41.907513
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

# Generated at 2026-10-24 13:49:43.399272
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

# Generated at 2026-10-24 13:49:44.877885
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

# Generated at 2026-10-24 13:50:24.207279
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')
    assert extractor._TKN_HOST == 'token.pornerbros.com'

# Generated at 2026-10-24 13:50:26.626460
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:50:29.042326
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:50:31.455545
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:50:33.016171
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

# Generated at 2026-10-24 13:50:34.551009
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

# Generated at 2026-10-24 13:50:36.088954
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

# Generated at 2026-10-24 13:50:37.509736
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

# Generated at 2026-10-24 13:50:38.944899
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

# Generated at 2026-10-24 13:50:40.381078
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

# Generated at 2026-10-24 13:50:42.018260
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

# Generated at 2026-10-24 13:50:43.333396
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

# Generated at 2026-10-24 13:50:44.730095
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:50:46.218283
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:50:47.544776
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:50:48.956377
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

# Generated at 2026-10-24 13:50:50.288310
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:50:51.624452
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:50:53.009030
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

# Generated at 2026-10-24 13:50:54.511778
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

# Generated at 2026-10-24 13:50:56.929745
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:50:59.346497
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:01.767945
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:04.186611
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:06.602222
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:09.018492
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:51:11.440113
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:13.858326
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:16.272518
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:18.688734
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:21.104759
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:23.521475
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:25.939085
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:28.356143
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:30.954528
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:33.367975
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:35.782177
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:38.194957
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:40.608306
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:43.021321
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:45.435202
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:51:47.855890
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:50.273931
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:52.689860
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:51:55.102558
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:57.518736
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:51:59.931250
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:52:02.348784
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-24 13:52:09.171270
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():extractor = PornTubeIE()

# Generated at 2026-10-24 13:52:10.514480
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:52:12.026732
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

# Generated at 2026-10-24 13:52:13.421894
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

# Generated at 2026-10-24 13:52:17.462309
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

# Generated at 2026-10-24 13:52:18.890766
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

# Generated at 2026-10-24 13:52:20.272127
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

# Generated at 2026-10-24 13:52:21.707371
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

# Generated at 2026-10-24 13:52:23.393407
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

# Generated at 2026-10-24 13:52:24.729659
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:52:26.151430
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

# Generated at 2026-10-24 13:52:27.535115
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

# Generated at 2026-10-24 13:52:28.973140
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

# Generated at 2026-10-24 13:52:31.393268
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:52:33.809701
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:52:36.391909
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:52:44.119534
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:46.533598
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:48.948646
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:52:51.362877
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:52:53.776878
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:52:56.196218
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:52:58.615777
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:01.034492
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:03.448799
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:05.863648
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:08.280943
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:10.697807
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-24 13:53:13.114370
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:53:15.532112
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-24 13:53:23.299906
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-24 13:53:24.630350
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

# Generated at 2026-10-24 13:53:25.966813
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

# Generated at 2026-10-24 13:53:27.302873
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:53:28.666570
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:53:29.991851
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

# Generated at 2026-10-24 13:53:42.572621
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

# Generated at 2026-10-24 13:53:44.014250
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

# Generated at 2026-10-24 13:53:45.518992
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

# Generated at 2026-10-24 13:53:47.038182
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

# Generated at 2026-10-24 13:53:48.390614
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:53:49.820537
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

# Generated at 2026-10-24 13:53:51.224512
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

# Generated at 2026-10-24 13:53:53.732771
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:53:56.252847
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:53:58.670649
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:54:01.100811
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:54:03.518316
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:54:05.933283
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-24 13:54:08.347104
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:54:10.760884
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:54:13.175443
# Unit test for constructor of class FuxIE

# Generated at 2026-10-24 13:54:35.285672
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:36.908509
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:54:38.277504
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

# Generated at 2026-10-24 13:54:39.997089
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

# Generated at 2026-10-24 13:54:41.449073
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

# Generated at 2026-10-24 13:54:42.964504
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

# Generated at 2026-10-24 13:54:44.500317
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

# Generated at 2026-10-24 13:54:45.934400
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

# Generated at 2026-10-24 13:54:47.367305
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

# Generated at 2026-10-24 13:54:51.921605
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:55:37.825836
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

# Generated at 2026-10-24 13:55:39.218197
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

# Generated at 2026-10-24 13:55:40.632004
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

# Generated at 2026-10-24 13:55:42.058417
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

# Generated at 2026-10-24 13:55:46.603284
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('http://m.fux.com/video/195359')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/')

# Generated at 2026-10-24 13:55:48.047624
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

# Generated at 2026-10-24 13:55:49.934463
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

# Generated at 2026-10-24 13:55:51.462135
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

# Generated at 2026-10-24 13:55:53.048530
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert ie.IE_NAME == '4tube'  # inherited from FourTubeBaseIE
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # video URL with display_id
    m = ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m
    match = ie._match_valid_url('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert match.group('kind') is None

    # embed URL
    match = ie._match_valid_url('https://www.pornerbros.com/embed/181369')
    assert match.group('id') == '181369'
    assert match.group('display_id') is None

    # mobile URL
    match = ie._match_valid_url('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert match.group('kind') == 'm'
    assert match.group('id') == '181369'

    # invalid URLs must not match
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')


test_PornerBrosIE()
print('All PornerBrosIE constructor tests passed')

# Generated at 2026-10-24 13:55:54.357285
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