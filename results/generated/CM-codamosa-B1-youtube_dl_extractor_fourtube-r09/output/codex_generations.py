

# Generated at 2026-10-25 02:11:33.146620
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:11:42.884636
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'

# Generated at 2026-10-25 02:11:44.224776
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:11:45.556786
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:11:56.288318
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 02:12:05.197255
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert extractor.suitable('https://www.fux.com/embed/195359')

# Generated at 2026-10-25 02:12:06.629881
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

# Generated at 2026-10-25 02:12:08.063037
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

# Generated at 2026-10-25 02:12:16.358731
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert extractor._TKN_HOST == 'tkn.porntube.com'

# Generated at 2026-10-25 02:12:17.902618
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:12:20.567894
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:12:23.091352
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:12:25.507132
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:12:27.920551
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 02:12:30.336256
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 02:12:36.735784
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():extractor = FourTubeIE()

# Generated at 2026-10-25 02:12:46.060757
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    class DummyDownloader(object):
        pass

    downloader = DummyDownloader()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')
    assert re.match(
        extractor._VALID_URL,
        'https://www.pornerbros.com/videos/example-video_181369')

# Generated at 2026-10-25 02:12:47.436637
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:12:48.927026
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

# Generated at 2026-10-25 02:12:50.257534
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:12:51.683486
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

# Generated at 2026-10-25 02:12:53.122495
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:13:02.535789
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 02:13:03.872499
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:13:16.598114
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

# Generated at 2026-10-25 02:13:18.025690
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:13:20.608087
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:13:23.132670
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:13:25.769287
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:13:28.301126
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 02:13:30.829509
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 02:13:33.246533
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 02:13:35.663308
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 02:13:38.077831
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 02:13:40.493854
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 02:13:42.906739
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:13:45.323098
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:13:48.005718
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 02:13:49.338193
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:13:58.349563
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

# Generated at 2026-10-25 02:14:06.187592
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-25 02:14:07.668217
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

# Generated at 2026-10-25 02:14:14.564559
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 02:14:16.145407
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:14:17.499810
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:14:18.918701
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:14:28.056733
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-25 02:14:37.285927
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:14:38.621377
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 02:14:41.241362
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:14:43.903560
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:14:46.430882
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:14:48.846699
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:14:50.178078
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():ie = FourTubeBaseIE()

    # Constructor creates a working instance of the extractor base class

# Generated at 2026-10-25 02:14:51.553350
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

# Generated at 2026-10-25 02:15:00.357225
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert extractor.suitable(
        'https://www.pornerbros.com/videos/example-video_181369')

# Generated at 2026-10-25 02:15:01.837387
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:15:11.261341
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 02:15:20.475086
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie.suitable(
        'https://www.pornerbros.com/videos/'
        'skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')

# Generated at 2026-10-25 02:15:29.112519
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert re.match(
        extractor._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-25 02:15:37.576817
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s'
    )

# Generated at 2026-10-25 02:15:39.996540
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:15:42.413684
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:15:44.828951
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:15:47.244246
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:15:49.660037
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:15:52.075263
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:16:02.007274
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie.ie_key() == 'PornTube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 02:16:03.401131
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

# Generated at 2026-10-25 02:16:11.265661
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-25 02:16:18.944833
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    ie = PornTubeIE(downloader)

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is downloader
    assert ie._ready is False
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 02:16:30.121114
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 02:16:42.396050
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 02:16:50.227292
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-25 02:17:25.197679
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:17:26.836768
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 02:17:28.169252
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:17:37.589645
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 02:17:38.924167
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:17:49.163476
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 02:17:56.636067
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert extractor.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 02:17:58.068519
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

# Generated at 2026-10-25 02:17:59.504552
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

# Generated at 2026-10-25 02:18:06.432892
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 02:18:07.815128
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:18:18.959156
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._match_id(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    ) == '195359'

# Generated at 2026-10-25 02:18:26.946219
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')

# Generated at 2026-10-25 02:18:35.138056
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/%s/video'

# Generated at 2026-10-25 02:18:44.607541
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:18:47.029183
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:18:49.441104
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:18:51.859249
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:18:54.271465
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:18:56.687000
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 02:19:09.649366
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')
    assert extractor.suitable(
        'https://www.pornerbros.com/videos/example-video_181369')

# Generated at 2026-10-25 02:19:11.305457
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

# Generated at 2026-10-25 02:19:24.802583
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._ready is False

    downloader = object()
    extractor_with_downloader = PornerBrosIE(downloader)

    assert extractor_with_downloader._downloader is downloader
    assert extractor_with_downloader._ready is False

# Generated at 2026-10-25 02:19:34.531456
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 02:19:45.487880
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert extractor._TKN_HOST == 'tkn.porntube.com'

# Generated at 2026-10-25 02:19:47.907235
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:19:50.322002
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:19:52.736364
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:19:55.151749
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:19:57.577181
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:20:05.147239
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():extractor = PornTubeIE(None)

# Generated at 2026-10-25 02:20:06.683777
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

# Generated at 2026-10-25 02:20:08.321921
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:20:09.755066
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

# Generated at 2026-10-25 02:20:11.267882
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

# Generated at 2026-10-25 02:20:12.725190
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

# Generated at 2026-10-25 02:20:22.066455
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-25 02:20:23.478560
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

# Generated at 2026-10-25 02:20:24.909866
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

# Generated at 2026-10-25 02:20:33.922108
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'PornTube'

# Generated at 2026-10-25 02:20:42.728388
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'PornerBros'
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-25 02:20:45.262275
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 02:20:47.678248
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 02:20:50.370828
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 02:20:52.786089
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:20:55.201078
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:20:57.615895
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 02:21:00.030767
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:21:02.445671
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 02:21:07.919677
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():ie = PornTubeIE()

# Generated at 2026-10-25 02:21:16.502207
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert extractor.suitable('https://www.porntube.com/embed/7089759')

# Generated at 2026-10-25 02:21:17.887007
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:21:19.526369
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:21:27.183892
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()

    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 02:21:28.800521
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    # Base class defines shared extraction logic, not site-specific config
    assert not hasattr(ie, 'IE_NAME')
    assert not hasattr(ie, '_VALID_URL')
    assert not hasattr(ie, '_TKN_HOST')
    # Site-specific config lives on subclasses
    sub = FourTubeIE()
    assert sub.IE_NAME == '4tube'
    assert sub._TKN_HOST == 'token.4tube.com'

# Generated at 2026-10-25 02:21:42.051161
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.porntube.com/videos/video_%s'
    )