

# Generated at 2026-11-02 00:32:25.203511
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Check class attributes set by constructor / class definition
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 3

    # Check URL matching
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.example.com/videos/123/video')

    # Check ID extraction from matched URLs
    assert ie._match_id('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black') == '209733'
    assert ie._match_id('http://www.4tube.com/embed/209733') == '209733'

# Generated at 2026-11-02 00:32:52.645720
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie.ie_key() == 'PornerBros'
    assert ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie.suitable('https://www.pornerbros.com/embed/181369')
    assert ie.suitable('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2026-11-02 00:33:27.050802
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

    # Class-level attributes
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/'
        r'(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    )

    # Standard www video URL with display_id
    m = re.match(
        ie._VALID_URL,
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('kind') is None
    assert m.group('id') == '181369'
    assert m.group('display_id') == 'skinny-brunette-takes-big-cock-down-her-anal-hole'

    # Embed URL without display_id
    m = re.match(ie._VALID_URL, 'https://www.pornerbros.com/embed/181369')
    assert m is not None
    assert m.group('kind') is None
    assert m.group('id') == '181369'
    assert m.group('display_id') is None

    # Mobile subdomain
    m = re.match(
        ie._VALID_URL,
        'https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m is not None
    assert m.group('kind') == 'm'
    assert m.group('id') == '181369'

    # URL template formatting yields a canonical URL
    assert ie._URL_TEMPLATE % '181369' == 'https://www.pornerbros.com/videos/video_181369'

# Generated at 2026-11-02 00:33:58.384118
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    instance = FourTubeIE()
    assert instance.IE_NAME == '4tube'
    assert instance._TKN_HOST == 'token.4tube.com'
    assert instance._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

    # Verify _VALID_URL matches regular video URLs and extracts groups correctly
    mobj = re.match(
        instance._VALID_URL,
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    # Embed URL variant
    mobj = re.match(instance._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    # Mobile URL variant
    mobj = re.match(
        instance._VALID_URL,
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '209733'

    # Video ID from URL template should resolve to canonical video page URL
    assert instance._URL_TEMPLATE % '209733' == \
        'https://www.4tube.com/videos/209733/video'

# Generated at 2026-11-02 00:34:19.682915
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert ie.suitable('http://www.4tube.com/embed/209733')
    assert ie.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    mobj = re.match(FourTubeIE._VALID_URL, 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert FourTubeIE._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert FourTubeIE._TKN_HOST == 'token.4tube.com'
    assert issubclass(FourTubeIE, FourTubeBaseIE)

# Generated at 2026-11-02 00:34:53.581537
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    # Constructor creates instance inheriting from FourTubeBaseIE
    assert isinstance(ie, FourTubeBaseIE)

    # Verify class-level configuration attributes
    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?fux\.com/'
        r'(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'

    # Regular www video URL with display_id
    mobj = re.match(
        ie._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('kind') is None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

    # Embed URL without display_id
    mobj = re.match(ie._VALID_URL, 'https://www.fux.com/embed/195359')
    assert mobj is not None
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') is None

    # Mobile ("m") kind URL
    mobj = re.match(
        ie._VALID_URL,
        'https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj is not None
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '195359'

    # URL from a different site must not match
    assert re.match(
        ie._VALID_URL,
        'https://www.4tube.com/videos/209733/hot-babe-holly-michaels') is None

    # Extraction test cases are defined for this extractor
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) > 0
    assert ie._TESTS[0]['url'] == (
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie._TESTS[0]['info_dict']['id'] == '195359'
    assert ie._TESTS[0]['info_dict']['age_limit'] == 18

# Generated at 2026-11-02 00:35:28.409578
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    instance = FourTubeIE(None)

# Generated at 2026-11-02 00:36:23.899252
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Class-level attributes set correctly
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

    # Subclasses the shared base extractor
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

    # _VALID_URL matches supported URL forms
    video_url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert ie.suitable(video_url)
    mobj = re.match(ie._VALID_URL, video_url)
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    # Embed URL variant
    embed_url = 'http://www.4tube.com/embed/209733'
    assert ie.suitable(embed_url)
    mobj = re.match(ie._VALID_URL, embed_url)
    assert mobj.group('kind') is None
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    # Mobile URL variant
    mobile_url = 'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert ie.suitable(mobile_url)
    mobj = re.match(ie._VALID_URL, mobile_url)
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '209733'

    # URL without display_id still matches
    bare_url = 'https://4tube.com/videos/209733'
    assert ie.suitable(bare_url)
    mobj = re.match(ie._VALID_URL, bare_url)
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    # URLs from other sites in the family are rejected
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.pornerbros.com/embed/181369')

    # Unrelated URLs are rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert not ie.suitable('http://www.4tube.com/videos/abc/not-a-video')
    assert not ie.suitable('https://www.4tube.com/other/209733/foo')

# Generated at 2026-11-02 00:37:22.986508
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert ie is not None
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/videos/squirting-teen-ballerina-ecg_1331406')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal')
    assert not ie.suitable('https://www.porntube.com/embed/')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('http://www.example.com/videos/12345')
    assert PornTubeIE._match_id('https://www.porntube.com/videos/teen-couple-doing-anal_7089759') == '7089759'
    assert PornTubeIE._match_id('https://www.porntube.com/embed/7089759') == '7089759'

# Generated at 2026-11-02 00:38:47.568655
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

    assert ie._VALID_URL == (
        r'https?://(?:(?P<kind>www|m)\.)?fux\.com/'
        r'(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    )
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert isinstance(ie, FourTubeBaseIE)

    m = re.match(
        ie._VALID_URL,
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert m is not None
    assert m.group('kind') == 'www'
    assert m.group('id') == '195359'
    assert m.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

# Generated at 2026-11-02 00:39:45.613109
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Constructor should build a working instance with no arguments
    ie = FourTubeIE()
    assert isinstance(ie, FourTubeIE)
    assert isinstance(ie, FourTubeBaseIE)

    # Optional downloader argument is accepted
    ie_with_downloader = FourTubeIE(downloader=None)
    assert isinstance(ie_with_downloader, FourTubeIE)

    # Class-level configuration
    assert ie.IE_NAME == '4tube'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL.startswith('https?://')

    # Instance recognizes its own URLs via _VALID_URL
    valid_urls = [
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'http://www.4tube.com/embed/209733',
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
    ]
    for url in valid_urls:
        assert ie.suitable(url), 'should suit: %s' % url

    # Other sites / malformed URLs must not match
    invalid_urls = [
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow',
        'https://www.porntube.com/videos/teen-couple-doing-anal_7089759',
        'https://www.pornerbros.com/embed/181369',
        'http://example.com/videos/209733/some-title',
        'not a url',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url), 'should not suit: %s' % url

    # Regex groups extracted from a canonical URL
    mobj = re.match(
        ie._VALID_URL,
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('kind') == 'www'
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') == 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

    # Embed URL: no display_id, kind defaults to None
    mobj = re.match(ie._VALID_URL, 'http://www.4tube.com/embed/209733')
    assert mobj.group('id') == '209733'
    assert mobj.group('display_id') is None

    # Mobile URL: kind is 'm'
    mobj = re.match(
        ie._VALID_URL,
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert mobj.group('kind') == 'm'
    assert mobj.group('id') == '209733'

# Generated at 2026-11-02 00:40:32.014558
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME is None
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    # suitable() should accept fux.com video/embed URLs
    assert ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert ie.suitable('https://www.fux.com/embed/195359')
    assert ie.suitable('https://m.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    # non-fux URLs should not match
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    # match ids extracted correctly
    mobj = re.match(ie._VALID_URL, 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert mobj.group('id') == '195359'
    assert mobj.group('display_id') == 'awesome-fucking-kitchen-ends-cum-swallow'

# Generated at 2026-11-02 00:41:32.846342
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert ie.IE_NAME == 'porntube'
    assert ie.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert ie.suitable('https://www.porntube.com/embed/7089759')
    assert ie.suitable('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert not ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not ie.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert not ie.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    # check URL template and token host
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    # check _match_id extraction
    mobj = re.match(PornTubeIE._VALID_URL, 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') == 'teen-couple-doing-anal'
    mobj = re.match(PornTubeIE._VALID_URL, 'https://www.porntube.com/embed/7089759')
    assert mobj.group('id') == '7089759'
    assert mobj.group('display_id') is None
    print('test_PornTubeIE passed')


if __name__ == '__main__':
    test_PornTubeIE()