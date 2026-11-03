

# Generated at 2026-11-02 07:37:13.556327
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # Constructor: inherits from FourTubeBaseIE / InfoExtractor
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # Class attributes
    assert ie.IE_NAME is None
    assert ie.ie_key() == 'Fux'
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?fux\.com/'
        r'(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    )

    # URL matching
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://fux.com/embed/195359')
    assert ie.suitable('https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://www.fux.com/video/')

    m = re.match(ie._VALID_URL, 'https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m.group('kind') == 'm'
    assert m.group('id') == '195359'
    assert m.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    # Test definitions
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 3
    assert ie._TESTS[0]['info_dict']['id'] == '195359'
    assert ie._TESTS[0]['info_dict']['age_limit'] == 18
    assert ie._TESTS[1]['url'] == 'https://www.fux.com/embed/195359'
    assert ie._TESTS[1]['only_matching'] is True

# Generated at 2026-11-02 07:37:34.832609
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Verify class attributes set at definition
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/'
        r'(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')

    # Base class initialization
    assert ie._downloader is None
    assert ie.gecko_proxy is None

    # URL matching based on _VALID_URL
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('https://www.4tube.com/videos/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/embed/181369')

    # Group extraction
    mobj = ie._match_id('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj == '209733'
    mobj = ie._match_id('http://www.4tube.com/embed/209733')
    assert mobj == '209733'

# Generated at 2026-11-02 07:37:54.180397
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
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/embed/181369')

# Generated at 2026-11-02 07:38:58.585174
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
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    m = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert m.group('id') == '209733'
    assert m.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    m = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert m.group('id') == '209733'
    assert m.group('display_id') is None

# Generated at 2026-11-02 07:40:09.617094
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    # nonce:50c0280e
    ie = PornerBrosIE()

    # Constructor should initialize the downloader reference to None
    assert ie._downloader is None

    # The extractor should inherit from the 4tube family base class
    assert isinstance(ie, FourTubeBaseIE)

    # Class configuration attributes
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'

    # URL matching: standard video page
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj is not None
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # URL matching: embed page
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj is not None
    assert mobj.group('kind') is None
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') is None

    # URL matching: mobile page
    mobj = re.match(ie._VALID_URL, 'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj is not None
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '181369'

    # suitable() delegates to _VALID_URL
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.pornerbros.com/videos/181369')

# Generated at 2026-11-02 07:40:32.040835
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Instance is created successfully and inherits from the base extractor
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Default IE_NAME is derived from the class name
    assert ie.IE_NAME == 'PornTube'

    # Class-specific configuration attributes
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )

    # The extractor recognizes its supported URL forms
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')

    # URL groups are extracted correctly
    m = re.match(
        ie._VALID_URL,
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'
    assert m.group('kind') == 'www'

    m_embed = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m_embed.group('id') == '7089759'
    assert m_embed.group('display_id') is None

    # Non-matching URLs are rejected
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://www.porntube.com/videos/invalid_id')

# Generated at 2026-11-02 07:41:57.074714
# Unit test for constructor of class PornerBrosIE

# Generated at 2026-11-02 07:42:49.810062
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():import re

    # Constructor should work without network access

# Generated at 2026-11-02 07:43:08.657226
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    instance = PornerBrosIE()

    assert isinstance(instance, FourTubeBaseIE)

    assert instance._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com'
        r'/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
    assert instance._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert instance._TKN_HOST == 'token.pornerbros.com'

    # URL matching
    assert instance.suitable(
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert instance.suitable('https://www.pornerbros.com/embed/181369')
    assert instance.suitable(
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not instance.suitable(
        'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

    # Group extraction
    mobj = re.match(
        instance._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    mobj = re.match(instance._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') is None

# Generated at 2026-11-02 07:44:01.185326
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # The base class defines no extractor-specific attributes itself
    assert ie.IE_NAME is None
    assert ie._VALID_URL is None
    assert ie.ie_key() == 'FourTubeBaseIE'

    # Downloader wiring inherited from InfoExtractor
    assert getattr(ie, '_downloader', None) is None
    ie.set_downloader(None)
    assert getattr(ie, '_downloader', None) is None

    # Subclasses must supply their own configuration
    assert FourTubeIE.IE_NAME == '4tube'
    assert FourTubeIE._TKN_HOST == 'token.4tube.com'
    assert FourTubeIE._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert FourTubeIE.ie_key() == '4tube'

    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

    assert PornTubeIE._TKN_HOST == 'tkn.porntube.com'
    assert PornTubeIE._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    assert PornerBrosIE._TKN_HOST == 'token.pornerbros.com'
    assert PornerBrosIE._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # Inherited helper methods are available on instances
    assert callable(ie._extract_formats)
    assert callable(ie._real_extract)
    assert callable(ie._sort_formats)
    assert callable(ie._download_webpage)
    assert callable(ie._download_json)
    assert callable(ie._search_regex)
    assert callable(ie._html_search_meta)

# Generated at 2026-11-02 07:44:11.209092
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor creates a valid extractor instance
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, FourTubeBaseIE)

    # Class-level attributes
    assert ie.IE_NAME == 'PornTube'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # _VALID_URL matches standard video URL
    mobj = re.match(
        ie._VALID_URL,
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj is not None
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    assert mobj.group('kind') is None

    # _VALID_URL matches embed URL
    mobj = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert mobj is not None
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') is None
    assert mobj.group('kind') is None

    # _VALID_URL matches mobile URL
    mobj = re.match(
        ie._VALID_URL,
        'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj is not None
    assert mobj.group('id') == '7089759'
    assert mobj.group('kind') == 'm'

    # suitable() accepts valid URLs and rejects unrelated ones
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert not ie.suitable('https://www.porntube.com/videos/invalid')
    assert not ie.suitable('https://www.4tube.com/videos/209733/foo')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

# Generated at 2026-11-02 07:44:45.127304
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()

    # Constructor should produce a usable instance of the base extractor
    assert isinstance(ie, FourTubeBaseIE)

    # Shared helper methods must be present and callable
    assert hasattr(ie, '_extract_formats')
    assert callable(ie._extract_formats)
    assert hasattr(ie, '_real_extract')
    assert callable(ie._real_extract)

    # Site-specific configuration belongs to subclasses, not the base class
    assert not hasattr(ie, '_TKN_HOST')
    assert not hasattr(ie, '_URL_TEMPLATE')
    assert not hasattr(ie, '_VALID_URL')

    # The constructor accepts the optional downloader argument like InfoExtractor
    ie2 = FourTubeBaseIE(downloader=None)
    assert isinstance(ie2, FourTubeBaseIE)

# Generated at 2026-11-02 07:45:09.180731
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Check class attributes set by the constructor/class definition
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie.IE_NAME == 'PornerBros'
    assert ie.ie_key() == 'PornerBros'

    # Check URL matching behavior
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

    # Check that video id and display id are extracted correctly
    mobj = re.match(PornerBrosIE._VALID_URL,
                    'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert mobj.group('kind') == 'www'

# Generated at 2026-11-02 07:45:37.750730
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # The extractor should be an instance of the base class
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class attributes should be properly set
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'

    # URL suitability checks
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/invalid')

    # Matching should extract the video id correctly
    assert ie._match_id('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') == '7089759'
    assert ie._match_id('https://www.porntube.com/embed/7089759') == '7089759'

    # Regex group extraction (display_id)
    mobj = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'

    # _real_extract must be overridden (not the base implementation)
    assert PornTubeIE._real_extract is not FourTubeBaseIE._real_extract

# Generated at 2026-11-02 07:45:45.848565
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert isinstance(ie, FourTubeBaseIE)
    assert ie.IE_NAME == 'PornerBros'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2026-11-02 07:46:02.837410
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
    assert ie._match_id('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black') == '209733'
    assert ie._match_id('http://www.4tube.com/embed/209733') == '209733'
    assert ie._match_id('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black') == '209733'