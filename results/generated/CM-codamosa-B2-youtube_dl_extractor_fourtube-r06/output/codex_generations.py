

# Generated at 2026-11-02 15:59:28.048356
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Instance is created and inherits from FourTubeBaseIE
    assert ie is not None
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )

    # URL suitability checks
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal')
    assert not ie.suitable('https://www.porntube.com/videos/')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

    # Regular video URL: captures id, display_id, kind is None
    mobj = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    assert mobj.group('kind') is None

    # Embed URL: no display_id
    mobj = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') is None

    # Mobile URL: kind is 'm'
    mobj = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '7089759'

    # _match_id helper resolves the video id
    assert ie._match_id('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') == '7089759'
    assert ie._match_id('https://www.porntube.com/embed/7089759') == '7089759'

    # URL template formats correctly with a video id
    assert ie._URL_TEMPLATE % '7089759' == 'https://www.porntube.com/videos/video_7089759'

# Generated at 2026-11-02 16:01:07.198014
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/embed/181369')
    assert len(ie._TESTS) == 3
    assert ie._TESTS[0]['info_dict']['id'] == '209733'
    assert ie._TESTS[0]['info_dict']['age_limit'] == 18

# Generated at 2026-11-02 16:02:55.213154
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Should be an instance of the shared base extractor
    assert isinstance(ie, FourTubeBaseIE)

    # Class-specific configuration attributes
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie.ie_key() == 'PornerBros'

    # _VALID_URL should match regular video URLs, capturing id and display_id
    m = re.match(ie._VALID_URL, 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('id') == '181369'
    assert m.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert m.group('kind') is None

    # _VALID_URL should match embed URLs (no display_id)
    m = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert m is not None
    assert m.group('id') == '181369'
    assert m.group('display_id') is None

    # _VALID_URL should match mobile URLs, capturing the kind group
    m = re.match(ie._VALID_URL, 'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('kind') == 'm'
    assert m.group('id') == '181369'

    # suitable() accepts supported URLs and rejects unsupported ones
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2026-11-02 16:04:55.604279
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE(downloader=None)
    assert ie._downloader is None
    assert ie._VALID_URL is not None
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.porntube.com/some/other/page')
    assert isinstance(PornTubeIE._TESTS, list) and len(PornTubeIE._TESTS) > 0

# Generated at 2026-11-02 16:06:03.552570
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    # Constructor should initialize without a downloader
    ie = PornerBrosIE()
    assert ie._downloader is None
    assert ie._cache == {}

    # Class-level configuration attributes
    assert PornerBrosIE.IE_NAME == 'PornerBros'
    assert PornerBrosIE._TKN_HOST == 'token.pornerbros.com'
    assert PornerBrosIE._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # URL suitability checks
    url = 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    assert PornerBrosIE.suitable(url)
    assert PornerBrosIE.suitable('https://www.porntube.com/embed/7089759') is False
    assert PornerBrosIE.suitable('https://www.pornerbros.com/embed/181369')
    assert PornerBrosIE.suitable(
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not PornerBrosIE.suitable('https://www.pornerbros.com/videos/181369')
    assert not PornerBrosIE.suitable('https://www.example.com/videos/some-video_181369')

    # _VALID_URL group extraction

# Generated at 2026-11-02 16:07:42.062406
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Class-level attributes set by the constructor
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert isinstance(ie._VALID_URL, str)
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 3

    # Inheritance
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # _VALID_URL: standard video URL with display_id
    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert m.group('kind') is None

    # _VALID_URL: embed URL (no display_id)
    m = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m is not None
    assert m.group('id') == '209733'
    assert m.group('display_id') is None
    assert m.group('kind') is None

    # _VALID_URL: mobile URL (kind == 'm')
    m = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m is not None
    assert m.group('id') == '209733'
    assert m.group('kind') == 'm'

    # _VALID_URL: https scheme
    m = re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733')
    assert m is not None
    assert m.group('id') == '209733'
    assert m.group('display_id') is None

    # _VALID_URL: non-matching URLs
    assert re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/x') is None
    assert re.match(ie._VALID_URL, 'http://www.4tube.com/channels/foo') is None