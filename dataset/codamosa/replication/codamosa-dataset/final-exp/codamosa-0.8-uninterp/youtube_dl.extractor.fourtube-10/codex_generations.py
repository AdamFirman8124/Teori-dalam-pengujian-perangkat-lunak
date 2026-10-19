

# Generated at 2022-06-14 16:13:50.194011
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from .common import InfoExtractor
    from ..compat import (
        compat_b64decode,
        compat_str,
        compat_urllib_parse_unquote,
        compat_urlparse,
    )
    from ..utils import (
        int_or_none,
        parse_duration,
        parse_iso8601,
        str_or_none,
        str_to_int,
        try_get,
        unified_timestamp,
        url_or_none,
    )
    from ..jsinterp import JSInterpreter
    import re
    import json

    four_tube = FourTubeBaseIE(4,4,4,4)

    assert four_tube._real_initialize() == None


# Generated at 2022-06-14 16:13:51.274308
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()


# Generated at 2022-06-14 16:13:59.349583
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():

    # Instantiation of the class is possible with a valid URL
    yt_ie = FourTubeIE('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert yt_ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # But not without
    try:
        FourTubeIE('https://www.4tube.com')
    except Exception as err:
        assert 'is not a valid' in str(err)

    # Test extraction with particular video URL
    yt_ie = FourTubeIE

# Generated at 2022-06-14 16:14:06.039794
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try_count = 0
    success = False
    while True:
        try:
            test = FourTubeIE()._TESTS[0]
            success = True
            break
        except:
            try_count += 1
            if try_count > 3:
                raise
    if success is False:
        raise Exception("Unit test for FourTubeIE failed")

# Generated at 2022-06-14 16:14:07.453382
# Unit test for constructor of class FuxIE
def test_FuxIE():
    t = FuxIE()

# Generated at 2022-06-14 16:14:08.786231
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()



# Generated at 2022-06-14 16:14:17.460662
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    ie2 = FourTubeIE()
    ie4 = FourTubeIE()
    ie5 = FourTubeIE()
    ie6 = FourTubeIE()
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie2._TKN_HOST == 'token.4tube.com'
    assert ie4._TKN_HOST == 'token.4tube.com'
    assert ie5._TKN_HOST == 'token.4tube.com'
    assert ie6._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:14:22.334604
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    """
    Test constructor of class PornTubeIE
    """
    assert PornTubeIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'

# Generated at 2022-06-14 16:14:26.105239
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    ie.FuxIE._VALID_URL
    ie.FuxIE._URL_TEMPLATE
    ie.FuxIE._TKN_HOST
    ie.FuxIE._TESTS
    ie.FuxIE._EXTRACTOR = 'fux'


# Generated at 2022-06-14 16:14:27.562010
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE()
    assert fux == FuxIE()

# Generated at 2022-06-14 16:14:48.341389
# Unit test for constructor of class FuxIE
def test_FuxIE():
    print("Entered test_FuxIE")
    span_list = list()
    span_list.append(re.compile(r'<span[^>]+class="rating-rating"[^>]*>([^<]+)<'))
    span_list.append(re.compile(r'<span[^>]+class="rating-count"[^>]*>([^<]+)<'))
    span_list.append(re.compile(r'<span[^>]+class="rating-pornstars"[^>]*>([^<]+)<'))
    span_list.append(re.compile(r'<span[^>]+class="rating-studios"[^>]*>([^<]+)<'))

# Generated at 2022-06-14 16:14:49.239583
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    import PornTubeIE
    PornTubeIE()

# Generated at 2022-06-14 16:14:51.910376
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE(None)._extract_formats('', '', '', [])
    PornTubeIE(None)._real_extract('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')


# Generated at 2022-06-14 16:14:52.714312
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:15:02.242748
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert ie._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:15:05.283068
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # constructor of class FourTubeBaseIE
    test = FourTubeBaseIE()
    # assert result is not None
    assert test is not None

# Generated at 2022-06-14 16:15:16.617632
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    video_id = "https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black"
    assert ie.match_url(video_id) is not None
    # Test URL when vieo_id is appended to url
    url_template_1 = "https://www.4tube.com/videos/%s/video"
    video_id_1 = "209733"
    assert ie._url_regex_not_match_video_id(url_template_1, video_id_1) is None
    # Test URL when vieo_id is not appended to url
    url_template_2 = "https://www.4tube.com/videos/%s"
   

# Generated at 2022-06-14 16:15:17.213814
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()

# Generated at 2022-06-14 16:15:18.148710
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()


# Generated at 2022-06-14 16:15:19.390533
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    assert not hasattr(FourTubeBaseIE(), '_TKN_HOST')

# Generated at 2022-06-14 16:15:51.560030
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE(FourTubeIE.ie_key()) == FourTubeIE()

# Generated at 2022-06-14 16:15:53.004984
# Unit test for constructor of class FuxIE
def test_FuxIE():
    info_extractor = FuxIE()

# Generated at 2022-06-14 16:15:58.453129
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    assert FourTubeBaseIE.IE_NAME in ['4tube', 'fux']
    assert FourTubeBaseIE.IE_DESC in [
        '4tube.com',
        'fux.com',
        'porntube.com',
        'pornerbros.com',
    ]

# Generated at 2022-06-14 16:15:59.985385
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert issubclass(PornerBrosIE, FourTubeBaseIE)

# Generated at 2022-06-14 16:16:09.973589
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    import youtube_dl
    options = {'proxy': '127.0.0.1:8118', 'verbose': True, 'force_generic_extractor': True}
    # Test for extracting formats for a video
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.extract_info('https://www.porntube.com/videos/teen-couple-doing-anal_7089759', download=False)
        ydl.extract_info('https://www.porntube.com/videos/squirting-teen-ballerina-ecg_1331406', download=False)
        ydl.extract_info('https://www.porntube.com/embed/7089759', download=False)

# Generated at 2022-06-14 16:16:11.166590
# Unit test for constructor of class FuxIE
def test_FuxIE():
    try:
        FuxIE()
    except:
        assert False

# Generated at 2022-06-14 16:16:17.016927
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    x = FourTubeIE('FourTube', 'fourtube.com')
    assert x.ie_key() == '4tube'
    assert x.ie_name() == '4Tube'
    assert x.ie_url() == '4tube.com'
    assert x.site_url() == '4tube.com'


# Generated at 2022-06-14 16:16:18.301012
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE();

# Generated at 2022-06-14 16:16:19.722959
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    ie.extract(ie._VALID_URL)

# Generated at 2022-06-14 16:16:21.145441
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE()



# Generated at 2022-06-14 16:17:04.669580
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Test for constructor excepting explicit URL
    URL = "https://www.porntube.com/videos/teen-couple-doing-anal_7089759"
    ies = PornTubeIE(URL)
    assert ies.url == URL
    assert ies.video_id == '7089759'
    assert ies.display_id == 'teen-couple-doing-anal'
    assert repr(ies) == 'PornTubeIE(URL=https://www.porntube.com/videos/teen-couple-doing-anal_7089759, video_id=7089759, display_id=teen-couple-doing-anal)'

    # Test for constructor with explicit invalid video id
    ies = PornTubeIE(None, '12345')
    assert ies.url is None

# Generated at 2022-06-14 16:17:05.941569
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros_ie = PornerBrosIE()

# Generated at 2022-06-14 16:17:06.602477
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE()

# Generated at 2022-06-14 16:17:08.891764
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    my_instant = FourTubeBaseIE()
    assert my_instant.IE_NAME == '4tube'

# Generated at 2022-06-14 16:17:09.490437
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:17:11.055297
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    try:
        PornerBrosIE()
    except:
        return 1
    return 0



# Generated at 2022-06-14 16:17:20.471426
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    class testIE(FourTubeBaseIE):
        _VALID_URL = r'https?://(?:(?P<kind>www|m)\.)?(?P<domain>4tube|fux|porntube|pornerbros)\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
        _URL_TEMPLATE = 'https://www.%s.com/videos/%s/video'
        _TKN_HOST = 'token.%s.com'
        _TESTS = None
    testIE(None)._downloader.cache.delete('token.4tube.com')
    testIE(None)._downloader.cache.delete('token.fux.com')
    testIE(None)._downloader

# Generated at 2022-06-14 16:17:22.056163
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert isinstance(PornerBrosIE(), FourTubeBaseIE)

# Generated at 2022-06-14 16:17:26.694210
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Class constructor should take no arguments
    try:
        class Dummy(FourTubeBaseIE):
            _VALID_URL = 'http://example.com'
        Dummy()
    except:
        raise AssertionError('FourTubeBaseIE constructor takes too many arguments')



# Generated at 2022-06-14 16:17:35.945035
# Unit test for constructor of class FuxIE
def test_FuxIE():
    import requests
    from .common import InfoExtractor
    from .extractor import get_info_extractor
    from .utils import ExtractorError

    def test(self, *args, **kwargs):
        pass
    
    InfoExtractor.__init__ = test
    FuxIE.__init__ = test
    ie = get_info_extractor("Fux")
    assert type(ie) == FuxIE

    # Test extracts
    res = ie._real_extract("https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow")
    assert res['formats'][0]['format_id'] == '720p'

    # Test error handling

# Generated at 2022-06-14 16:19:19.772540
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    p = PornTubeIE()
    assert(p.ie_key() == 'Porntube')
    assert(p.ie_name() == 'Porntube')
    assert(p._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
    assert(p._NETRC_MACHINE == 'porntube')

    # check that class is inherited from FourTubeBaseIE
    assert(issubclass(PornTubeIE, FourTubeBaseIE))



# Generated at 2022-06-14 16:19:23.961427
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        PornTubeIE('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
    except ValueError as e:
        assert e.args[0] == 'Unsupported url: %s' % 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'

# Generated at 2022-06-14 16:19:31.408183
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    four_tube = FourTubeIE('https://www.4tube.com/videos/272559/amazing-interracial-unit-codi-bryant')
    assert four_tube._TKN_HOST == 'token.4tube.com'
    assert four_tube._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert four_tube._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'


# Generated at 2022-06-14 16:19:32.520049
# Unit test for constructor of class FourTubeIE

# Generated at 2022-06-14 16:19:33.413477
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()._TESTS[0]

# Generated at 2022-06-14 16:19:34.305794
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()

# Generated at 2022-06-14 16:19:42.184717
# Unit test for constructor of class PornerBrosIE

# Generated at 2022-06-14 16:19:46.209417
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE('4Tube')
    FourTubeIE('4Tube')
    FuxIE('Fux')
    PornTubeIE('PornTube')
    PornerBrosIE('PornerBros')

# Generated at 2022-06-14 16:19:47.207409
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()  # no exception

# Generated at 2022-06-14 16:19:57.586904
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie.IE_DESC == '4tube.com, fux.com, porntube.com and pornerbros.com'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._TESTS == test_FourTubeIE._TESTS
