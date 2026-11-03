

# Generated at 2026-11-02 22:39:06.118338
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie is not None
    assert ie.ie_key() == 'PornerBros'
    assert ie.ie_name() == 'PornerBros'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

    # Valid URLs should match
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')

    # Invalid URLs should not match
    assert not ie.suitable('https://www.pornerbros.com/videos/')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

    # _match_id extracts correct groups
    mobj = ie._match_id('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert mobj[0] == '181369'
    mobj = ie._match_id('https://www.pornerbros.com/embed/181369')
    assert mobj[0] == '181369'

# Generated at 2026-11-02 22:40:29.370000
# Unit test for constructor of class FourTubeIE

# Generated at 2026-11-02 22:42:26.514113
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():import re

ie = FourTubeIE()

# Constructor / class attributes
assert isinstance(ie, FourTubeBaseIE)
assert issubclass(FourTubeIE, FourTubeBaseIE)
assert ie.IE_NAME == '4tube'
assert ie._TKN_HOST == 'token.4tube.com'
assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

# _VALID_URL matching: full video URL
match = re.match(ie._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
assert match is not None
assert match.group('id') == '209733'
assert match.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
assert match.group('kind') is None

# _VALID_URL matching: embed URL
match_embed = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
assert match_embed is not None
assert match_embed.group('id') == '209733'
assert match_embed.group('display_id') is None
assert match_embed.group('kind') == 'www'

# _VALID_URL matching: mobile URL
match_mobile = re.match(ie._VALID_URL, 'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
assert match_mobile is not None
assert match_mobile.group('id') == '209733'
assert match_mobile.group('kind') == 'm'

# suitable() accepts 4tube URLs and rejects non-4tube URLs
assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black') is True
assert ie.suitable('http://www.4tube.com/embed/209733') is True
assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black') is True
assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow') is False
assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') is False
assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369') is False
assert ie.suitable('http://www.4tube.com/some/other/path/123') is False

# Generated at 2026-11-02 22:45:32.680934
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert len(ie._TESTS) == 3
    assert ie._TESTS[0]['info_dict']['id'] == '209733'
    assert ie._TESTS[0]['info_dict']['age_limit'] == 18
    assert ie._TESTS[1]['only_matching'] is True
    assert ie._TESTS[2]['only_matching'] is True

# Generated at 2026-11-02 22:47:29.112435
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Constructor should produce an instance with expected class attributes
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'

    # Matches standard www video URL with display_id
    m = re.match(ie._VALID_URL, 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '181369'
    assert m.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Matches embed URL without display_id
    m = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert m is not None
    assert m.group('id') == '181369'
    assert m.group('display_id') is None

    # Matches mobile (m.) video URL
    m = re.match(ie._VALID_URL, 'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('kind') == 'm'
    assert m.group('id') == '181369'

    # URL_TEMPLATE substitution yields canonical video URL
    assert ie._URL_TEMPLATE % '181369' == 'https://www.pornerbros.com/videos/video_181369'