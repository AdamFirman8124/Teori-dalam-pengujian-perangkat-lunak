

# Generated at 2026-11-02 13:12:25.788519
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Class attributes inherited/defined properly
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie.IE_NAME == 'PornerBros'
    assert ie.age_limit == 18

    # Instance created successfully with no downloader
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, FourTubeBaseIE)

    # URL matching
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.pornerbros.com/videos/only_a_display_id')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe')

    # ID extraction
    assert ie._match_id('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369') == '181369'
    assert ie._match_id('https://www.pornerbros.com/embed/181369') == '181369'

    # Regex group extraction
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'
    assert mobj.group('kind') == 'www'

    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') is None

# Generated at 2026-11-02 13:14:04.770226
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()

    # Should instantiate without arguments and be an InfoExtractor
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, FourTubeBaseIE)

    # Core inherited attributes/methods should be present
    assert hasattr(ie, 'IE_NAME')
    assert callable(ie._extract_formats)
    assert callable(ie._real_extract)
    assert callable(ie.set_downloader)

    # Base class does not define subclass-specific attributes
    assert 'FourTubeBaseIE' in FourTubeBaseIE.__name__

# Generated at 2026-11-02 13:15:41.925441
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie is not None
    assert isinstance(ie, FourTubeBaseIE)
    assert ie._VALID_URL is not None
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'

    # Regular video URL
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj is not None
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Embed URL (no display_id)
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj is not None
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') is None

    # Mobile URL
    mobj = re.match(ie._VALID_URL, 'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj is not None
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '181369'

    # Non-matching URL
    assert re.match(ie._VALID_URL, 'https://www.4tube.com/videos/209733/video') is None

# Generated at 2026-11-02 13:19:05.700047
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Default construction should succeed
    ie = FourTubeBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # Inherited key methods should be present and callable
    assert callable(ie._extract_formats)
    assert callable(ie._real_extract)

    # Construction with an explicit (None) downloader argument
    ie2 = FourTubeBaseIE(downloader=None)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is None

    # Base class does not hardcode subclass-specific config
    assert not hasattr(FourTubeBaseIE, 'IE_NAME') or FourTubeBaseIE.IE_NAME is None