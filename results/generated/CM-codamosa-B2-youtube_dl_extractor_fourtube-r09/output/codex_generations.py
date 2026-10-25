

# Generated at 2026-10-25 01:37:01.645266
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

# Generated at 2026-10-25 01:37:10.803016
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'PornerBros'
    assert extractor._TKN_HOST == 'token.pornerbros.com'

# Generated at 2026-10-25 01:37:18.991532
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

# Generated at 2026-10-25 01:37:27.489850
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.porntube.com/videos/video_%s'
    )
    assert extractor.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    )

# Generated at 2026-10-25 01:37:34.306031
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-25 01:37:36.724715
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:37:39.139978
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:37:41.553730
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:37:43.975880
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 01:37:46.388392
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 01:37:48.800742
# Unit test for constructor of class PornTubeIE

# Generated at 2026-10-25 01:37:51.214283
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:37:52.633847
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()

# Generated at 2026-10-25 01:38:04.968290
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 01:38:13.468310
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'PornerBros'

# Generated at 2026-10-25 01:38:25.141028
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-25 01:38:34.460327
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-10-25 01:38:44.256682
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:38:46.800610
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:38:49.215305
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:38:51.630011
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:38:54.044280
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:38:56.462520
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:39:05.384845
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:39:20.948508
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 01:39:22.382533
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

# Generated at 2026-10-25 01:39:23.770137
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

# Generated at 2026-10-25 01:39:39.176782
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:39:40.609589
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 01:39:48.598517
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    ie = PornTubeIE(downloader)

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is downloader
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 01:39:51.120420
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:39:53.535950
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:39:55.950336
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:39:58.367612
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:40:00.781233
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:40:03.196281
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:40:05.615814
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:40:22.697698
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:40:28.135463
# Unit test for constructor of class FuxIE
def test_FuxIE():extractor = FuxIE()

# Generated at 2026-10-25 01:40:29.470291
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

# Generated at 2026-10-25 01:40:39.700935
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

# Generated at 2026-10-25 01:40:45.740670
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._URL_TEMPLATE == \
        'https://www.porntube.com/videos/video_%s'
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor.IE_NAME == 'porntube'

# Generated at 2026-10-25 01:40:47.164428
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

# Generated at 2026-10-25 01:40:55.941395
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
    assert not extractor.suitable('https://www.4tube.com/videos/209733/video')

# Generated at 2026-10-25 01:41:05.052056
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'PornTube'
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.porntube.com/videos/video_%s')

# Generated at 2026-10-25 01:41:06.483772
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

# Generated at 2026-10-25 01:41:14.779126
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    extractor = PornerBrosIE()

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == (
        'https://www.pornerbros.com/videos/video_%s')

# Generated at 2026-10-25 01:41:25.246895
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 01:41:32.127129
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:41:33.472656
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 01:41:42.428335
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 01:41:43.882466
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

# Generated at 2026-10-25 01:41:52.463519
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()
    extractor = PornTubeIE(downloader)

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 01:41:59.772468
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:42:01.205714
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 01:42:03.730854
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:42:06.246379
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:42:08.779438
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:42:20.047657
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    assert isinstance(ie, PornerBrosIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is None
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-25 01:42:27.477560
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 01:42:36.234341
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:42:37.593332
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 01:42:46.268622
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

# Generated at 2026-10-25 01:42:53.942477
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()

    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'Fux'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 01:42:55.581285
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

# Generated at 2026-10-25 01:43:03.468050
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    downloader = object()
    extractor = PornerBrosIE(downloader)

    assert isinstance(extractor, PornerBrosIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._TKN_HOST == 'token.pornerbros.com'
    assert extractor._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2026-10-25 01:43:04.904029
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

# Generated at 2026-10-25 01:43:13.249219
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    downloader = object()

    ie = PornTubeIE(downloader)

    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._downloader is downloader
    assert ie._ready is False

# Generated at 2026-10-25 01:43:21.858019
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

# Generated at 2026-10-25 01:43:23.330692
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

# Generated at 2026-10-25 01:43:24.764446
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

# Generated at 2026-10-25 01:43:26.199551
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

# Generated at 2026-10-25 01:43:36.330172
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'PornTube'
    assert extractor._TKN_HOST == 'tkn.porntube.com'

# Generated at 2026-10-25 01:43:42.993153
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )
    assert extractor._URL_TEMPLATE == (
        'https://www.porntube.com/videos/video_%s'
    )
    assert extractor._TKN_HOST == 'tkn.porntube.com'

# Generated at 2026-10-25 01:43:51.697763
# Unit test for constructor of class FuxIE
def test_FuxIE():
    downloader = object()
    extractor = FuxIE(downloader)

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is downloader
    assert extractor._VALID_URL == FuxIE._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 01:43:54.114042
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:43:56.529837
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:43:59.122269
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:44:01.537100
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:44:03.951130
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:44:06.365961
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:44:08.952524
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:44:11.367128
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:44:12.741893
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 01:44:22.831343
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:44:24.168593
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():ie = PornerBrosIE()

# Generated at 2026-10-25 01:44:25.503328
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

# Generated at 2026-10-25 01:44:32.152798
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    extractor = PornTubeIE()

    assert isinstance(extractor, PornTubeIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'tkn.porntube.com'
    assert extractor._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2026-10-25 01:44:40.542432
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

# Generated at 2026-10-25 01:44:48.119483
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

# Generated at 2026-10-25 01:44:50.540140
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:44:52.954776
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:44:55.373810
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:44:57.784245
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:45:00.199931
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:45:02.782533
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:45:05.197704
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:45:07.613101
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:45:10.030191
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:45:12.448427
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:45:14.862419
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:45:17.276803
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:45:21.330970
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:45:23.745596
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:45:26.161590
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:45:28.577531
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:45:30.991725
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:45:33.406086
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:45:34.840346
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

# Generated at 2026-10-25 01:45:44.023510
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
    assert extractor.suitable('https://www.fux.com/embed/195359')

# Generated at 2026-10-25 01:45:45.463350
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

# Generated at 2026-10-25 01:45:46.788201
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

# Generated at 2026-10-25 01:45:56.098427
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._downloader is None
    assert extractor._TKN_HOST == 'token.fux.com'
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2026-10-25 01:45:57.435002
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

# Generated at 2026-10-25 01:46:04.308821
# Unit test for constructor of class FuxIE
def test_FuxIE():
    extractor = FuxIE()

    assert isinstance(extractor, FuxIE)
    assert isinstance(extractor, FourTubeBaseIE)
    assert extractor._VALID_URL
    assert extractor._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert extractor._TKN_HOST == 'token.fux.com'

# Generated at 2026-10-25 01:46:05.738250
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

# Generated at 2026-10-25 01:46:12.823875
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:46:15.239741
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:46:17.653404
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:46:20.070485
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:46:22.488034
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:46:24.899910
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:46:27.315067
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:46:29.730196
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:46:32.145549
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:46:34.561309
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:46:36.973270
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:46:39.388920
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:46:41.803147
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:46:44.218365
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:46:46.634378
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-10-25 01:46:49.049599
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:46:51.477414
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:46:53.904171
# Unit test for constructor of class FuxIE

# Generated at 2026-10-25 01:46:56.319027
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:46:58.734635
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:47:01.149199
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2026-10-25 01:47:03.564815
# Unit test for constructor of class FourTubeIE

# Generated at 2026-10-25 01:47:05.271250
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():ie = FourTubeIE()