

# Generated at 2026-11-02 11:11:15.254103
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'
    assert ie.gecko is None if hasattr(ie, 'gecko') else True

    valid_urls = [
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'http://www.4tube.com/embed/209733',
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'https://www.4tube.com/videos/209733',
    ]
    for url in valid_urls:
        assert ie.suitable(url), url

    invalid_urls = [
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow',
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759',
        'https://www.pornerbros.com/embed/181369',
        'http://www.4tube.com/videos/abc/foo',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url), url

    mobj = re.match(
        FourTubeIE._VALID_URL,
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    mobj = re.match(FourTubeIE._VALID_URL, 'http://4tube.com/embed/209733')
    assert mobj.group('kind') is None
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    assert FourTubeIE._TESTS
    assert len(FourTubeIE._TESTS) == 3
    assert FourTubeIE._TESTS[0]['info_dict']['id'] == '209733'
    assert FourTubeIE._TESTS[0]['info_dict']['age_limit'] == 18
    assert FourTubeIE._TESTS[1]['url'] == 'http://www.4tube.com/embed/209733'
    assert FourTubeIE._TESTS[1].get('only_matching') is True
    assert FourTubeIE._TESTS[2]['url'] == 'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert FourTubeIE._TESTS[2].get('only_matching') is True

# Generated at 2026-11-02 11:13:38.073094
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert isinstance(ie, FuxIE)
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?fux\.com/'
        r'(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    # URL matching via the class-level _VALID_URL
    assert FuxIE.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert FuxIE.suitable('https://www.fux.com/embed/195359')
    assert FuxIE.suitable('https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not FuxIE.suitable('https://www.4tube.com/videos/209733/hot-babe')
    assert not FuxIE.suitable('https://www.fux.com/video/abc/foo')
    assert not FuxIE.suitable('https://www.fux.com/other/195359')

# Generated at 2026-11-02 11:14:45.551767
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'

    # Full URL with display_id
    m = re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m.group('kind') == 'www'
    assert m.group('id') == '195359'
    assert m.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    # Embed URL without display_id
    m = re.match(ie._VALID_URL, 'https://www.fux.com/embed/195359')
    assert m.group('kind') == 'www'
    assert m.group('id') == '195359'
    assert m.group('display_id') is None

    # Mobile URL
    m = re.match(ie._VALID_URL, 'https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m.group('kind') == 'm'
    assert m.group('id') == '195359'

    # suitable() checks
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert not ie.suitable('https://www.fux.com/videos/195359')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2026-11-02 11:17:23.965588
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Constructor should instantiate without error and expose class attributes
    assert ie.ie_key() == 'PornerBros'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._TESTS is not None and len(ie._TESTS) == 3
    assert ie._TESTS[0]['url'].startswith('https://www.pornerbros.com/videos/')

    # Regular video URL
    mobj = re.match(
        ie._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj is not None
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Embed URL
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert mobj is not None
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '181369'
    assert mobj.group('display_id') is None

    # Mobile URL
    mobj = re.match(
        ie._VALID_URL,
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj is not None
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '181369'

    # Suitable / not suitable
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/videos/invalid_abc')
# nonce:f9b03eb4

# Generated at 2026-11-02 11:19:11.385500
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Class attributes
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

    # Regular video URL
    mobj = re.match(
        ie._VALID_URL,
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj is not None
    assert mobj.group('kind') is None
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    # Embed URL
    mobj = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert mobj is not None
    assert mobj.group('kind') is None
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    # Mobile URL
    mobj = re.match(
        ie._VALID_URL,
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj is not None
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '209733'

    # URL template expansion
    assert ie._URL_TEMPLATE % '209733' == 'https://www.4tube.com/videos/209733/video'

    # Non-matching URL (different site handled by another extractor)
    assert re.match(
        ie._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow') is None