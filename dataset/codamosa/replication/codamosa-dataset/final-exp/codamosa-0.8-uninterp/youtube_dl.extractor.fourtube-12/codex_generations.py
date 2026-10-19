

# Generated at 2022-06-14 16:13:46.791546
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    demo_url = 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    ie = PornTubeIE()
    data = ie._download_webpage(demo_url, 'test')

    player_js = ie._search_regex(
        r'<script[^>]id=(["\'])playerembed\1[^>]+src=(["\'])(?P<url>.+?)\2',
        data, 'player JS', group='url')
    player_js = ie._download_webpage(player_js, 'test', data=b'')
    print(player_js)


# Generated at 2022-06-14 16:13:48.403985
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        FourTubeBaseIE()
    except:
        pass

# Generated at 2022-06-14 16:13:54.564589
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from .youtube import YoutubeIE
    
    my_str = 'https://www.porntube.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    my_obj = PornTubeIE(YoutubeIE())
    my_obj.ie._TESTS = my_obj.ie._TESTS[0:1]
    my_obj.ie._TESTS[0]['info_dict']['view_count'] = int

# Generated at 2022-06-14 16:13:57.296639
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE("FourTubeBaseIE", {})
    assert ie._VALID_URL == 0
    assert ie._URL_TEMPLATE == 0

# Generated at 2022-06-14 16:13:57.877202
# Unit test for constructor of class FuxIE
def test_FuxIE():
    pass

# Generated at 2022-06-14 16:14:01.687657
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert ie._VALID_URL is None
    assert ie._URL_TEMPLATE is None
    assert ie._TKN_HOST is None
    assert ie._TESTS == []

# Generated at 2022-06-14 16:14:03.770202
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    k = PornerBrosIE()
    assert k._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:14:12.601729
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .fux import FuxIE
    fux_ie = FuxIE()

    assert fux_ie._TESTS[0]['url'] == 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    assert fux_ie._TESTS[0]['md5'] == '15f6b0d9b93a8a1f01e23a20d14c7093'

    print('PASSED')



# Generated at 2022-06-14 16:14:21.079015
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    # Test constructor with valid URL
    instance = PornerBrosIE("https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369")
    assert isinstance(instance, PornerBrosIE)

    # Test constructor with invalid URL
    try:
        PornerBrosIE("https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole")
    except RegexNotFoundError:
        assert True
    except:
        assert False

# Generated at 2022-06-14 16:14:23.627168
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        PornTubeIE('1', '1', '1')
        assert True, 'Expected an exception'
    except:
        assert True, 'Expected no exception'

# Generated at 2022-06-14 16:14:40.339200
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE.PornTubeIE()

# Generated at 2022-06-14 16:14:42.285683
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try:
        FourTubeBaseIE
    except NameError:
        raise Exception('FourTubeBaseIE does not exist')

    try:
        FourTubeIE
    except NameError:
        raise Exception('FourTubeIE does not exist')

# Generated at 2022-06-14 16:14:48.187520
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    import tempfile
    from .common import download_webpage, parse_json
    from ..compat import compat_urllib_parse_unquote, compat_b64decode
    from ..utils import (
        int_or_none,
        try_get,
    )

    video_id = '7089066'
    url = 'https://www.porntube.com/videos/teen-gets-cock-ass-to-mouth_%s' % video_id
    webpage = download_webpage(url)

# Generated at 2022-06-14 16:14:49.023449
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE().IE_NAME == '4tube'

# Generated at 2022-06-14 16:14:56.977798
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE.__name__ == 'FuxIE'
    assert FuxIE.__doc__ == 'Information extractor for adult websites in the fux.com network.'
    f = FuxIE()
    assert f.name == 'Fux'
    assert f.ie_key() == 'Fux'
    assert f.logger.name == 'FuxIE'
    assert f._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert f._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'

# Generated at 2022-06-14 16:15:03.874058
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux_ie = FuxIE()
    assert fux_ie._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fux_ie._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:15:11.966320
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
	p = PornTubeIE()
	assert p.IE_NAME == 'PornTube'
	assert p._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
	#assert p._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'

# Generated at 2022-06-14 16:15:17.487962
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    class TestPornerBrosIE(PornerBrosIE):
       def __init__(self):
           ret = PornerBrosIE.__init__(self, 'pornerbros')
           assert ret == None
           assert self._TESTS
           assert self._VALID_URL
           assert self._URL_TEMPLATE
           assert self._TKN_HOST
    TestPornerBrosIE()


# Generated at 2022-06-14 16:15:21.093812
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert ie._VALID_URL == r"https?://(?:(?P<kind>www|m)\.)?porntube\.(?:com|org)/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)"

# Generated at 2022-06-14 16:15:21.946452
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    print(FourTubeIE)



# Generated at 2022-06-14 16:15:53.096032
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    print(ie)

# Generated at 2022-06-14 16:15:57.351961
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    video_id = "1331406"
    url = "https://www.porntube.com/videos/squirting-teen-ballerina-ecg_" + video_id
    pt = PornTubeIE(url)

# Generated at 2022-06-14 16:16:01.424974
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try:
        FourTubeIE()
        raise AssertionError("4tube constructor did not detect safelinking")
    except AssertionError:
        pass
    except:
        raise AssertionError("4tube constructor did not detect safelinking")


# Generated at 2022-06-14 16:16:10.829330
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert(PORNERBROS_EXAMPLE_URL is not None)
    assert(PORNERBROS_EXAMPLE_MD5 is not None)
    ie = PornerBrosIE()
    assert(PORNERBROS_EXAMPLE_URL in ie._VALID_URL)
    assert(PORNERBROS_EXAMPLE_MD5 in ie._TESTS)
    assert(PornTubeIE._TKN_HOST in ie._TKN_HOST)

PORNERBROS_EXAMPLE_URL = 'https://www.pornerbros.com/embed/181369'
PORNERBROS_EXAMPLE_MD5 = '6516c8ac63b03de06bc8eac14362db4f'

# Unit tests for constructor of class PornTubeIE

# Generated at 2022-06-14 16:16:21.552685
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        from .common import urlopen
    except:
        try:
            from urllib.request import urlopen
        except:
            from urllib2 import urlopen
    from .common import USER_AGENTS
    from .extractor import get_info_extractor


    url = "https://www.porntube.com/videos/teen-couple-doing-anal_7089759"
    html = urlopen(url, headers={"User-Agent": USER_AGENTS[0]}).read()

    clazz = get_info_extractor(PornTubeIE.ie_key(), PornTubeIE)
    o = clazz()
    o.extract(url, html)

# Generated at 2022-06-14 16:16:26.469766
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    """
    Test constructor of class FourTubeBaseIE.
    """
    fourtube_base_ie = FourTubeBaseIE()
    assert fourtube_base_ie._VALID_URL == None
    assert fourtube_base_ie._URL_TEMPLATE == None
    assert fourtube_base_ie._TKN_HOST == None


# Generated at 2022-06-14 16:16:28.276037
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
	# Test constructor of FourTubeIE
	assert(FourTubeIE() != None)


# Generated at 2022-06-14 16:16:29.356925
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    fourTubeIE = FourTubeIE();
    assert fourTubeIE._TKN_HOST == 'token.4tube.com';

# Generated at 2022-06-14 16:16:30.200663
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()


# Generated at 2022-06-14 16:16:32.514171
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    ie.extract(
        'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')

# Generated at 2022-06-14 16:17:37.656859
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    obj = FourTubeBaseIE()

# Generated at 2022-06-14 16:17:46.473227
# Unit test for constructor of class FuxIE
def test_FuxIE():
    testArgs = {
        'url': 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow',
        'id': 195359,
        'ext': 'mp4',
        'title': 'Awesome fucking in the kitchen ends with cum swallow',
        'uploader': 'alenci2342',
        'upload_date': '20131230',
        'timestamp': 1388361660,
        'duration': 289,
        'view_count': int,
        'like_count': int,
        'categories': list,
        'age_limit': 18,
    }

    # Test
    testInstance = FuxIE()
    assert testInstance._TESTS[0]['info_dict'] == testArgs

# Generated at 2022-06-14 16:17:47.710375
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    test = PornerBrosIE()
    assert test._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:17:50.355006
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE()
    assert fux._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

# Generated at 2022-06-14 16:17:54.495216
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    entry = PornTubeIE('PornTube', {})
    assert entry.IE_NAME == 'PornTube'
    assert entry('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert entry('https://www.porntube.com/videos/squirting-teen-ballerina-ecg_1331406')
    assert entry('https://www.porntube.com/embed/7089759')
    assert entry('https://m.porntube.com/videos/teen-couple-doing-anal_7089759')

# Generated at 2022-06-14 16:18:01.429610
# Unit test for constructor of class FuxIE
def test_FuxIE():
    f = FuxIE()
    assert(f._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
    assert(f._URL_TEMPLATE == 'https://www.fux.com/video/%s/video')
    assert(f._TKN_HOST == 'token.fux.com')

# Generated at 2022-06-14 16:18:04.891548
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE("http://www.pornerbros.com/embed/111479")
    assert ie.name == "PornerBros"


# Generated at 2022-06-14 16:18:13.782489
# Unit test for constructor of class FuxIE
def test_FuxIE():
    video_id = 195359
    video_url = 'https://www.fux.com/video/195359/'
    video_hash = 'md5_hash'
    video_data = {'id': video_id, 'url': video_url, 'md5': video_hash}
    
    # Test if FuxIE is initialised accordingly
    ie = FuxIE(video_data)
    assert ie.id == video_id
    assert ie.url == video_url
    assert ie.video_id == video_id
    assert ie.video_url == video_url
    assert ie.video_md5 == video_hash

# Generated at 2022-06-14 16:18:16.006688
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    url = 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    inst = FourTubeIE()
    inst.extract(url)

# Generated at 2022-06-14 16:18:17.109267
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .test_downloader import _test_downloader
    _test_downloader(FuxIE())

# Generated at 2022-06-14 16:21:33.782656
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        from . import PornTubeIE
    except:
        from .. import PornTubeIE
    url = 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    # Conversion to Python objects
    video = PornTubeIE._parse_json(
        PornTubeIE._search_regex(
            r'INITIALSTATE\s*=\s*(["\'])(?P<value>(?:(?!\1).)+)\1',
            PornTubeIE._download_webpage(url, display_id=None), 'data', group='value'), '7089759',
            transform_source=lambda x: compat_urllib_parse_unquote(
                compat_b64decode(x).decode('utf-8')))['page']['video']


# Generated at 2022-06-14 16:21:36.831354
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerBrosIE = PornerBrosIE()
    assert pornerBrosIE._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:21:42.154518
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    assert isinstance(FourTubeBaseIE("FourTubeIE"), InfoExtractor)
    assert isinstance(FourTubeBaseIE("FuxIE"), InfoExtractor)
    assert isinstance(FourTubeBaseIE("PornTubeIE"), InfoExtractor)
    assert isinstance(FourTubeBaseIE("PornerBrosIE"), InfoExtractor)

# Generated at 2022-06-14 16:21:42.844240
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE()

# Generated at 2022-06-14 16:21:43.766771
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    obj = FourTubeIE()
    assert obj is not None

# Generated at 2022-06-14 16:21:46.340409
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    instance = FourTubeBaseIE()
    assert instance._VALID_URL == None
    assert instance._URL_TEMPLATE == None
    assert instance._TKN_HOST == None
    assert instance._TESTS == []

# Generated at 2022-06-14 16:21:47.636187
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

# Generated at 2022-06-14 16:21:56.172892
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    print('Test #1 - Download video with uploader')
    ie = PornTubeIE(None)
    data = ie.extract('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    assert data['uploader'] == 'Alexy'
    assert data['uploader_id'] == '91488'

    print('Test #2 - Download video with channel')
    ie = PornTubeIE(None)
    data = ie.extract('https://www.porntube.com/videos/squirting-teen-ballerina-ecg_1331406')
    assert data['uploader'] == 'Exploited College Girls'
    assert data['uploader_id'] == '665'

# Generated at 2022-06-14 16:21:58.125240
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    inst = PornerBrosIE()
    assert inst.__class__.__name__ == PornerBrosIE.IE_NAME


# Generated at 2022-06-14 16:21:59.520188
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE('https://www.porntube.com/embed/7089759')

