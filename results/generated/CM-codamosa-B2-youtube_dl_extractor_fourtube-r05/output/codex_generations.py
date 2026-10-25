

# Generated at 2026-10-25 03:51:47.621524
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 03:51:50.035780
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 03:51:52.453991
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 03:51:54.866801
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 03:52:00.334166
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():extractor = PornTubeIE(None)

# Generated at 2026-10-25 03:52:12.417567
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._match_id(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen'
    ) == '195359'

# Generated at 2026-10-25 03:52:17.793365
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'

# Generated at 2026-10-25 03:52:25.842988
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

# Generated at 2026-10-25 03:52:27.252697
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

# Generated at 2026-10-25 03:52:28.584418
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

# Generated at 2026-10-25 03:52:37.404373
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
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-25 03:52:46.524047
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

# Generated at 2026-10-25 03:52:53.705150
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

# Generated at 2026-10-25 03:53:02.901284
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

# Generated at 2026-10-25 03:53:11.605431
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert isinstance(ie, FuxIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert re.match(
        ie._VALID_URL,
        'https://www.fux.com/video/195359/example-video')

# Generated at 2026-10-25 03:53:20.308998
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-10-25 03:53:22.729036
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 03:53:25.143280
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 03:53:27.560478
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 03:53:29.976084
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:53:32.391410
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:53:34.807143
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:53:36.283029
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

# Generated at 2026-10-25 03:53:46.328740
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
    assert not extractor.suitable('https://example.com/video/195359')

# Generated at 2026-10-25 03:53:47.661772
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

# Generated at 2026-10-25 03:53:58.504269
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 03:53:59.941007
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 03:54:08.642491
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'Fux'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 03:54:17.310390
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

# Generated at 2026-10-25 03:54:19.831707
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:54:22.248142
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:54:24.663827
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:54:27.081374
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 03:54:29.498587
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 03:54:31.914724
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 03:54:34.332723
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:54:36.747564
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:54:44.174824
# Unit test for constructor of class FuxIE
def test_FuxIE():extractor = FuxIE()

# Generated at 2026-10-25 03:54:45.616783
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

# Generated at 2026-10-25 03:54:54.416502
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._VALID_URL == PornTubeIE._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert extractor._TKN_HOST == 'tkn.porntube.com'

# Generated at 2026-10-25 03:55:03.534835
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'PornTube'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert extractor._TKN_HOST == 'tkn.porntube.com'

# Generated at 2026-10-25 03:55:04.970840
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

# Generated at 2026-10-25 03:55:06.394863
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

# Generated at 2026-10-25 03:55:15.922041
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    ie = PornTubeIE(downloader)

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is downloader
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert re.match(
        ie._VALID_URL,
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 03:55:24.418361
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 03:55:26.837636
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 03:55:29.254275
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 03:55:31.844134
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 03:55:34.260762
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 03:55:36.679657
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 03:55:39.368803
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 03:55:40.802341
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

# Generated at 2026-10-25 03:55:50.735686
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

# Generated at 2026-10-25 03:55:58.418391
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert extractor.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 03:56:06.198544
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

# Generated at 2026-10-25 03:56:14.288667
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
        'https://www.pornerbros.com/videos/video_%s'
    )

# Generated at 2026-10-25 03:56:24.220067
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()

    ie = PornerBrosIE(downloader)

    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is downloader
    assert ie._ready is False
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-25 03:56:26.779967
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:56:29.315245
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:56:31.750597
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 03:56:34.166907
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 03:56:36.583511
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 03:56:38.998917
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 03:56:47.919059
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 03:56:55.762226
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 03:56:57.190591
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 03:57:05.886431
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor.ie_key() == 'PornTube'
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 03:57:15.597513
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'Fux'
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 03:57:25.249078
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 03:57:34.569896
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 03:57:40.513275
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None

# Generated at 2026-10-25 03:57:51.659375
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

# Generated at 2026-10-25 03:57:53.055535
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

# Generated at 2026-10-25 03:58:01.645046
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie.ie_key() == 'PornTube'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 03:58:09.067549
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'

# Generated at 2026-10-25 03:58:16.963510
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 03:58:24.745638
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

# Generated at 2026-10-25 03:58:26.178588
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

# Generated at 2026-10-25 03:58:49.630869
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert isinstance(ie, FuxIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie.suitable(
        'https://www.fux.com/video/195359/'
        'awesome-fucking-kitchen-ends-cum-swallow'
    )

# Generated at 2026-10-25 03:59:01.918916
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

# Generated at 2026-10-25 03:59:03.350043
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

# Generated at 2026-10-25 03:59:11.952864
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

# Generated at 2026-10-25 03:59:22.165044
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None

    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert extractor._downloader is downloader

# Generated at 2026-10-25 03:59:23.523078
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

# Generated at 2026-10-25 03:59:25.776758
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

# Generated at 2026-10-25 03:59:27.210394
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

# Generated at 2026-10-25 03:59:28.643530
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

# Generated at 2026-10-25 03:59:30.079457
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

# Generated at 2026-10-25 03:59:42.564187
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-25 03:59:50.259717
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

# Generated at 2026-10-25 03:59:51.686473
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

# Generated at 2026-10-25 03:59:53.115656
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

# Generated at 2026-10-25 04:00:03.092348
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 04:00:13.085598
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()

    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 04:00:14.474714
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

# Generated at 2026-10-25 04:00:15.830253
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

# Generated at 2026-10-25 04:00:40.632542
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

# Generated at 2026-10-25 04:00:43.049893
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 04:00:45.464457
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 04:00:47.880320
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 04:00:59.698267
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

# Generated at 2026-10-25 04:01:01.111122
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

# Generated at 2026-10-25 04:01:07.764928
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 04:01:09.113674
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

# Generated at 2026-10-25 04:01:17.703122
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor.ie_key() == 'Fux'

# Generated at 2026-10-25 04:01:26.511315
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor.suitable(
        'https://www.pornerbros.com/videos/example-video_181369')

# Generated at 2026-10-25 04:01:27.939557
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

# Generated at 2026-10-25 04:01:30.360863
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 04:01:32.776903
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 04:01:35.193036
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 04:01:37.606547
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 04:01:40.022324
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 04:01:42.437458
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 04:01:44.853376
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 04:01:47.268741
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 04:01:49.685080
# Unit test for constructor of class FourTubeBaseIE