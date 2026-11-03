

# Generated at 2026-11-01 22:11:05.882642
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._ready is False
    assert ie._downloader is None
    assert ie.IE_NAME is None

# Generated at 2026-11-01 22:11:19.498774
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

    mobj = re.match(FourTubeIE._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert mobj.group('kind') == 'www'

    mobj = re.match(FourTubeIE._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    mobj = re.match(FourTubeIE._VALID_URL, 'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('id') == '209733'
    assert mobj.group('kind') == 'm'

    # Test URL_TEMPLATE
    assert FourTubeIE._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # Test that test cases are defined
    assert len(FourTubeIE._TESTS) == 3
    assert FourTubeIE._TESTS[0]['info_dict']['id'] == '209733'
    assert FourTubeIE._TESTS[1]['only_matching'] is True
    assert FourTubeIE._TESTS[2]['only_matching'] is True


test_FourTubeIE()

# Generated at 2026-11-01 22:12:07.326709
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie.IE_NAME == 'Fux'

    m = re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m.group('kind') is None
    assert m.group('id') == '195359'
    assert m.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    m = re.match(ie._VALID_URL, 'https://www.fux.com/embed/195359')
    assert m.group('kind') is None
    assert m.group('id') == '195359'
    assert m.group('display_id') is None

    m = re.match(ie._VALID_URL, 'https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m.group('kind') == 'm'
    assert m.group('id') == '195359'

# Generated at 2026-11-01 22:12:53.946447
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-11-01 22:13:37.850404
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Constructor should produce a working extractor instance
    assert ie is not None
    assert ie.ie_key() == 'PornerBros'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # _VALID_URL should match canonical video URLs and capture groups
    m = re.match(
        PornerBrosIE._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('id') == '181369'
    assert m.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Embed URLs
    m = re.match(PornerBrosIE._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert m is not None
    assert m.group('id') == '181369'
    assert m.group('kind') is None

    # Mobile URLs
    m = re.match(
        PornerBrosIE._VALID_URL,
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('kind') == 'm'

    # suitable() accepts supported URLs and rejects unsupported ones
    assert ie.suitable(
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels')

# Generated at 2026-11-01 22:14:48.568992
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Default construction should succeed with no downloader attached
    ie = FourTubeBaseIE()
    assert ie is not None
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.IE_NAME is None

    # Core extraction helpers should be available on the base class
    assert callable(getattr(ie, '_extract_formats', None))
    assert callable(getattr(ie, '_real_extract', None))

    # Construction with an explicit (None) downloader also works
    ie2 = FourTubeBaseIE(downloader=None)
    assert isinstance(ie2, FourTubeBaseIE)
    assert ie2._downloader is None

# Generated at 2026-11-01 22:15:33.561300
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie.IE_NAME == 'PornerBros'
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-11-01 22:17:21.288566
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert ie is not None
    assert isinstance(ie, FourTubeBaseIE)
    assert callable(getattr(ie, '_extract_formats', None))
    assert callable(getattr(ie, '_real_extract', None))

# Generated at 2026-11-01 22:19:42.052496
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME is None
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'

    # suitable() matches expected URLs
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')

    # suitable() rejects URLs belonging to other extractors
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.pornerbros.com/embed/181369')

    # _match_id extracts the video id
    assert ie._match_id('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') == '7089759'
    assert ie._match_id('https://www.porntube.com/embed/7089759') == '7089759'

    # named groups from the regular expression
    mobj = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    assert mobj.group('kind') == 'www'

    mobj = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') is None

    # _TESTS sanity checks
    assert isinstance(ie._TESTS, list)
    assert len(ie._TESTS) == 4
    for t in ie._TESTS:
        assert 'url' in t
    assert ie._TESTS[0]['info_dict']['id'] == '7089759'
    assert ie._TESTS[1]['info_dict']['id'] == '1331406'
    assert ie._TESTS[0]['info_dict']['age_limit'] == 18

# Generated at 2026-11-01 22:20:59.300414
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert ie.IE_NAME == 'PornTube'
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal')
    assert ie._match_id('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') == '7089759'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'