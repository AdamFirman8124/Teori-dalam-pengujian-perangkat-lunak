

# Generated at 2026-11-01 20:25:59.225909
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # Class attributes set correctly
    assert ie.IE_NAME is None  # inherited default; ie_key falls back to class name
    assert ie.ie_key() == 'Fux'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?fux\.com/'
        r'(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    )
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'

    # Suitable URL matching
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://fux.com/video/195359')
    assert ie.suitable('https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert ie.suitable('https://m.fux.com/embed/195359')

    # Non-matching URLs
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.fux.com/videos/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.fux.com/channel/195359')

    # Regex group extraction
    mobj = re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('kind', 'id', 'display_id') == (
        'www', '195359', 'awesome-fucking-kitchen-ends-cum-swallow')

    mobj = re.match(ie._VALID_URL, 'https://fux.com/embed/195359')
    assert mobj.group('kind', 'id', 'display_id') == (None, '195359', None)

    # URL template builds the canonical URL
    assert ie._URL_TEMPLATE % '195359' == 'https://www.fux.com/video/195359/video'

# Generated at 2026-11-01 20:26:45.214140
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Constructor should work with no arguments
    ie = FourTubeBaseIE()
    assert ie is not None

    # Default

# Generated at 2026-11-01 20:27:08.752485
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'FourTubeBase'
    assert hasattr(ie, '_extract_formats')
    assert hasattr(ie, '_real_extract')
    assert ie._TKN_HOST is None
    assert ie._URL_TEMPLATE is None

# Generated at 2026-11-01 20:27:43.794906
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.IE_NAME is None
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert ie.suitable('https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/other/195359')

# Generated at 2026-11-01 20:28:02.201108
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    """Unit test for constructor of class PornerBrosIE."""
    ie = PornerBrosIE()

    # Constructor should produce an instance with expected class attributes
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie.IE_NAME == 'PornerBrosIE'
    assert ie.suitable(
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')

    # Regular www URL with display_id
    m = re.match(
        ie._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '181369'
    assert m.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Embed URL (no display_id)
    m = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '181369'
    assert m.group('display_id') is None

    # Mobile subdomain URL
    m = re.match(
        ie._VALID_URL,
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('kind') == 'm'
    assert m.group('id') == '181369'

    # Non-matching URLs should not suit
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not ie.suitable('https://pornerbros.com/some-other-page')

# Generated at 2026-11-01 20:28:21.453896
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-11-01 20:28:43.367546
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Class attributes
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

    # Valid URLs should match
    valid_urls = [
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'https://www.4tube.com/videos/209733',
        'http://www.4tube.com/embed/209733',
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
    ]
    for url in valid_urls:
        assert ie.suitable(url), 'should match: %s' % url

    # Invalid URLs should not match
    invalid_urls = [
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow',
        'https://www.4tube.com/videos/',
        'https://www.4tube.com/videos/abc/some-title',
        'https://www.4tube.com/',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url), 'should not match: %s' % url

    # Regex group extraction
    mobj = re.match(
        ie._VALID_URL,
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert mobj.group('kind') is None

    mobj = re.match(ie._VALID_URL, 'http://m.4tube.com/embed/209733')
    assert mobj.group('id') == '209733'
    assert mobj.group('kind') == 'm'
    assert mobj.group('display_id') is None

    # _match_id helper
    assert ie._match_id('http://www.4tube.com/embed/209733') == '209733'

# Generated at 2026-11-01 20:29:07.232247
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/'
        r'(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    )
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 3
    assert issubclass(FourTubeIE, FourTubeBaseIE)

    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert ie.suitable(url)
    mobj = re.match(ie._VALID_URL, url)
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert mobj.group('kind') == 'www'

    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2026-11-01 20:29:34.264306
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # Constructor should produce a working InfoExtractor instance
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, FourTubeBaseIE)

    # Class-level configuration attributes
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'

    # suitable() should accept porntube.com URLs only
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

    # Regex group extraction
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'
    assert m.group('kind') == 'www'

    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m.group('id') == '7089759'
    assert m.group('display_id') is None

# Generated at 2026-11-01 20:30:01.514495
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
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 3

# Generated at 2026-11-01 20:30:24.333746
# Unit test for constructor of class FuxIE
def test_FuxIE():
    """Test the constructor and class attributes of FuxIE."""
    ie = FuxIE()

    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'

    # The extractor recognizes fux.com video and embed URLs
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert ie.suitable('https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

    # URLs from other sites in the family must not match
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')

    # Regex groups extracted for a canonical video URL
    mobj = ie._match_valid_url('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    # Embed URL has no display_id
    mobj = ie._match_valid_url('https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') is None

# Generated at 2026-11-01 20:31:14.924114
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, FourTubeBaseIE)
    # Core helper methods must be present and callable
    assert callable(getattr(ie, '_extract_formats', None))
    assert callable(getattr(ie, '_real_extract', None))
    # Base extractor does not define its own VALID_URL (subclasses do)
    assert getattr(ie, 'IE_NAME', None) is None
    # Default attribute state after construction
    assert ie.age_limit is None
    assert ie._downloader is None

# Generated at 2026-11-01 20:31:29.260552
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
    assert not ie.suitable('http://www.4tube.com/videos/notanid')

# Generated at 2026-11-01 20:31:44.205451
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert ie.IE_NAME == 'FourTubeBase'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

    # Regular video URL
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') == 'teen-couple-doing-anal'
    assert m.group('kind') is None

    # Embed URL
    m = re.match(ie._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert m is not None
    assert m.group('id') == '7089759'
    assert m.group('display_id') is None

    # Mobile URL
    m = re.match(ie._VALID_URL, 'https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert m is not None
    assert m.group('kind') == 'm'
    assert m.group('id') == '7089759'

    # Non-matching URL should not match
    assert re.match(ie._VALID_URL, 'https://www.porntube.com/videos/invalid') is None

# Generated at 2026-11-01 20:32:25.373479
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Check class attributes set by the constructor/class definition
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._VALID_URL is not None

    # Valid URLs should match _VALID_URL
    valid_urls = [
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',
        'https://www.pornerbros.com/embed/181369',
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',
        'http://pornerbros.com/embed/181369',
    ]
    for url in valid_urls:
        assert re.match(ie._VALID_URL, url) is not None

    # Invalid URLs should not match _VALID_URL
    invalid_urls = [
        'https://www.pornerbros.com/videos/181369',
        'https://www.pornerbros.com/videos/title_no-id',
        'https://www.pornerbros.com/other/181369',
        'https://porntube.com/embed/181369',
    ]
    for url in invalid_urls:
        assert re.match(ie._VALID_URL, url) is None

    # Group extraction for a full video URL
    mobj = re.match(
        ie._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Group extraction for an embed URL
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') is None

    # Mobile subdomain sets kind to 'm'
    mobj = re.match(
        ie._VALID_URL,
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '181369'

# Generated at 2026-11-01 20:32:41.453024
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Basic class attributes set correctly
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL is not None

    # Extractor accepts URLs it should handle
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('https://www.4tube.com/videos/209733/video')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

    # Extractor rejects URLs of sibling extractors / invalid URLs
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/embed/181369')
    assert not ie.suitable('http://www.4tube.com/videos/not_a_number/slug')
    assert not ie.suitable('http://example.com/videos/209733/slug')

    # Regex named groups extract expected values
    mobj = re.match(
        FourTubeIE._VALID_URL,
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('id') == '209733'
    assert mobj.group('kind') == 'www'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    mobj = re.match(FourTubeIE._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert mobj.group('id') == '209733'
    assert mobj.group('kind') is None
    assert mobj.group('display_id') is None

    mobj = re.match(
        FourTubeIE._VALID_URL,
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '209733'

# Generated at 2026-11-01 20:33:13.819964
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # nonce:871b6e23
    import re

    ie = FuxIE()
    assert ie is not None

    # Class-level configuration attributes
    assert FuxIE._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?fux\.com/'
        r'(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert FuxIE.IE_NAME is None
    assert ie.ie_key() == 'Fux'

    # URL template produces the canonical video URL
    assert FuxIE._URL_TEMPLATE % '195359' == 'https://www.fux.com/video/195359/video'

    # _VALID_URL matching (full URL with display_id)
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    # Embed URL: no kind, no display_id
    mobj = re.match(FuxIE._VALID_URL, 'https://fux.com/embed/195359')
    assert mobj.group('kind') is None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') is None

    # Mobile URL
    mobj = re.match(
        FuxIE._VALID_URL,
        'https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '195359'

    # Suitability checks
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://fux.com/embed/195359')
    assert FuxIE.suitable('https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not FuxIE.suitable('https://www.pornerbros.com/embed/181369')
    assert not FuxIE.suitable('https://www.fux.com/other/195359')

# Generated at 2026-11-01 20:33:35.617898
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    instance = PornerBrosIE()
    assert instance is not None
    assert isinstance(instance, PornerBrosIE)
    assert isinstance(instance, FourTubeBaseIE)
    assert instance._TKN_HOST == 'token.pornerbros.com'
    assert instance._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert re.match(
        instance._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert re.match(
        instance._VALID_URL,
        'https://www.pornerbros.com/embed/181369')
    mobj = re.match(
        instance._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    kind, video_id, display_id = mobj.group('kind', 'id', 'display_id')
    assert video_id == '181369'
    assert display_id == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    mobj = re.match(instance._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj.group('id') == '181369'
    mobj = re.match(
        instance._VALID_URL,
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '181369'

# Generated at 2026-11-01 20:34:01.633384
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Check class attributes set by the constructor
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/'
        r'(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    )

    # Check that the extractor accepts its supported URL forms
    assert ie.suitable(
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable(
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

    # Check that URLs of sibling extractors are not matched
    assert not ie.suitable(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable(
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://example.com/videos/209733')

    # Check URL group extraction
    mobj = re.match(
        ie._VALID_URL,
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    mobj = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    mobj = re.match(
        ie._VALID_URL,
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '209733'

    # Check test cases are declared
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 3
    assert ie._TESTS[0]['info_dict']['id'] == '209733'
    assert ie._TESTS[1]['only_matching'] is True
    assert ie._TESTS[2]['only_matching'] is True

# Generated at 2026-11-01 20:35:10.440452
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Class-level configuration inherited/defined on subclass
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'

    # Extractor identity
    assert ie.ie_key() == 'PornerBros'
    assert ie.ie_name() == 'PornerBros'

    # URL suitability checks
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.pornerbros.com/other/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    # Regex group extraction
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    mobj_embed = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj_embed.group('id') == '181369'
    assert mobj_embed.group('display_id') is None

# Generated at 2026-11-01 20:35:42.085255
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # IE_NAME should be set correctly
    assert ie.IE_NAME == '4tube'

    # Class-level configuration attributes
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # suitable() should accept valid URLs
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('https://www.4tube.com/videos/209733')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

    # suitable() should reject invalid URLs / other sites
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/notvideos/209733')

    # _match_id should extract the video id
    assert ie._match_id('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black') == '209733'
    assert ie._match_id('http://www.4tube.com/embed/209733') == '209733'

    # _real_extract URL rewriting logic (kind == 'm' uses URL_TEMPLATE)
    mobj = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/some-title')
    kind, video_id, display_id = mobj.group('kind', 'id', 'display_id')
    assert kind == 'm'
    assert video_id == '209733'
    assert display_id == 'some-title'
    assert ie._URL_TEMPLATE % video_id == 'https://www.4tube.com/videos/209733/video'