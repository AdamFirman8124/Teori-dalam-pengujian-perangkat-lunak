

# Generated at 2026-11-03 03:16:03.992251
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Check class attributes set at construction
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL is not None
    assert ie._TESTS is not None and len(ie._TESTS) > 0

    # It should be a subclass of FourTubeBaseIE / InfoExtractor
    assert issubclass(FourTubeIE, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # URL matching behavior for the main site
    match = re.match(
        ie._VALID_URL,
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert match is not None
    assert match.group('kind') == 'www'
    assert match.group('id') == '209733'
    assert match.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    # Embed URL: no kind, no display_id
    match = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert match is not None
    assert match.group('kind') is None
    assert match.group('id') == '209733'
    assert match.group('display_id') is None

    # Mobile URL: kind == 'm'
    match = re.match(
        ie._VALID_URL,
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert match is not None
    assert match.group('kind') == 'm'
    assert match.group('id') == '209733'

    # URL without display_id
    match = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733')
    assert match is not None
    assert match.group('id') == '209733'
    assert match.group('display_id') is None

    # Should not match URLs of sibling extractors
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')

# Generated at 2026-11-03 03:16:30.053600
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie is not None
    # Class-level attributes should be correctly defined
    assert PornerBrosIE._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )
    assert PornerBrosIE._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert PornerBrosIE._TKN_HOST == 'token.pornerbros.com'
    # Instance should inherit from the FourTubeBase extractor
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)
    # The _VALID_URL regex should match expected URLs
    mobj = re.match(PornerBrosIE._VALID_URL,
                    'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj is not None
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    mobj_embed = re.match(PornerBrosIE._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj_embed is not None
    assert mobj_embed.group('id') == '181369'
    mobj_mobile = re.match(PornerBrosIE._VALID_URL,
                           'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj_mobile is not None
    assert mobj_mobile.group('kind') == 'm'
    # Non-matching URL should not match
    assert re.match(PornerBrosIE._VALID_URL, 'https://www.4tube.com/videos/209733/hot-babe') is None

# Generated at 2026-11-03 03:16:55.488777
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Default construction without a downloader
    ie = FourTubeBaseIE()
    assert ie._downloader is None

    # Construction with an explicit (None) downloader argument
    ie2 = FourTubeBaseIE(downloader=None)
    assert ie2._downloader is None

    # The base extractor exposes the shared extraction helpers
    assert callable(ie._extract_formats)
    assert callable(ie._real_extract)

    # Base class itself does not define a token host; subclasses do
    assert not hasattr(FourTubeBaseIE, '_TKN_HOST')
    assert FourTubeIE._TKN_HOST == 'token.4tube.com'
    assert FuxIE._TKN_HOST == 'token.fux.com'
    assert PornTubeIE._TKN_HOST == 'tkn.porntube.com'
    assert PornerBrosIE._TKN_HOST == 'token.pornerbros.com'

    # Subclasses inherit the constructor behavior
    for subclass in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        sub_ie = subclass()
        assert sub_ie._downloader is None

# Generated at 2026-11-03 03:18:25.152690
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()

    # It should be an InfoExtractor (and inherit the shared 4Tube base logic)
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level configuration
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) > 0

    # URL matching behaviour
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/')

    # Extract video id from a sample URL
    mobj = re.match(ie._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'

# Generated at 2026-11-03 03:19:51.579913
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Class-level configuration attributes
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._VALID_URL
    assert ie._TESTS

    # URLs that should match
    for url in (
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',
        'https://www.pornerbros.com/embed/181369',
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',
        'https://pornerbros.com/embed/181369',
    ):
        assert ie.suitable(url), url

    # URLs that should NOT match
    for url in (
        'https://www.pornerbros.com/videos/181369',
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_',
        'https://www.pornerbros.com/other/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',
        'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759',
    ):
        assert not ie.suitable(url), url

    # Regex group extraction for a full video URL
    mobj = re.match(
        ie._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Regex group extraction for an embed URL (no display_id, no kind)
    mobj = re.match(ie._VALID_URL, 'https://pornerbros.com/embed/181369')
    assert mobj.group('kind') is None
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') is None

# Generated at 2026-11-03 03:21:32.855484
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'

    # Full video URL with display_id
    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert ie.suitable(url)
    mobj = re.match(FourTubeIE._VALID_URL, url)
    assert mobj.group('kind') is None
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    # Embed URL (only_matching)
    url = 'http://www.4tube.com/embed/209733'
    assert ie.suitable(url)
    mobj = re.match(FourTubeIE._VALID_URL, url)
    assert mobj.group('kind') is None
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    # Mobile URL
    url = 'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert ie.suitable(url)
    mobj = re.match(FourTubeIE._VALID_URL, url)
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '209733'

    # URL without display_id
    url = 'https://www.4tube.com/videos/209733'
    mobj = re.match(FourTubeIE._VALID_URL, url)
    assert mobj is not None
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    # URLs that should not match
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/other/209733')
    assert not ie.suitable('https://example.com/videos/209733')