

# Generated at 2022-06-14 16:13:39.586088
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    class_PornTubeIE = PornTubeIE()
    assert "transform_source" in class_PornTubeIE._real_extract(
        "https://www.porntube.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369")



# Generated at 2022-06-14 16:13:41.209400
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    instance = FourTubeBaseIE()
    assert isinstance(instance._TESTS, type(list()))

# Generated at 2022-06-14 16:13:44.737833
# Unit test for constructor of class FuxIE
def test_FuxIE():
    test_case = FuxIE(None)
    assert test_case
    assert test_case._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

# Generated at 2022-06-14 16:13:47.808605
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:13:57.261397
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    #This is how PornerBrosIE is called in the code, don't ask why
    #It is a trick to keep things consistent with the other tests, without
    #breaking the code
    from .fourtube import PornerBrosIE
    tmp = PornerBrosIE()
    assert(tmp._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
    assert(tmp._TKN_HOST == 'token.pornerbros.com')

# Generated at 2022-06-14 16:13:59.486530
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux_ie = FuxIE()
    assert fux_ie._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:14:03.399300
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    ie.extract('http://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')


# Generated at 2022-06-14 16:14:05.465442
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:14:13.710616
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    TestClass = type('FourTubeBaseIE', (FourTubeBaseIE,), {
        '_VALID_URL': r'https?://(?:(?P<kind>www|m)\.)?example\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)',
        '_URL_TEMPLATE': 'https://www.example.com/videos/video_%s',
        '_TKN_HOST': 'token.example.com',
    })
    TestClass()

# Generated at 2022-06-14 16:14:14.742706
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()

# Generated at 2022-06-14 16:14:40.544899
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Try different download methods
    for method in range(1, 5):
        # Get list of available videos that can be extracted
        videos = []
        for ie in _WORKING_IES:
            url = ie._TESTS[0]['url']
            video_id = ie._VALID_URL.match(url).group('id')
            webpage = ie._download_webpage(url, video_id)
            media_id = ie._search_regex(
                r'<button[^>]+data-id=(["\'])(?P<id>\d+)\1[^>]+data-quality=', webpage,
                'media id', group='id')
            videos.append({'ie': ie, 'method': method, 'id': media_id})

        # Extract videos simultaneously
        extractor = FourTubeBaseIE()

# Generated at 2022-06-14 16:14:45.958148
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    porntube_ie = PornTubeIE()
    assert porntube_ie.IE_NAME == 'porntube'
    assert porntube_ie._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert porntube_ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert porntube_ie._TKN_HOST == 'tkn.porntube.com'
    assert len(porntube_ie._TESTS) == 3



# Generated at 2022-06-14 16:14:52.539932
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # This tests the private method _initialize_video_info which is called in the
    # private method _download_webpage
    pytest.importorskip("cryptography")

    # These are the private variables that get set by the method of interest
    video_id = None
    title = None
    thumbnail = None
    uploader = None
    timestamp = None
    like_count = None
    view_count = None
    duration = None

    def _initialize_video_info(self, page, video_id):
        nonlocal video_id, title, thumbnail, uploader, timestamp, like_count, view_count, duration
        video_id = video_id

# Generated at 2022-06-14 16:14:55.053231
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    pass
    # self=FourTubeIE()
    # self.extract('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2022-06-14 16:15:08.388946
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'

# Generated at 2022-06-14 16:15:09.786109
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    obj = FourTubeIE()

# Generated at 2022-06-14 16:15:12.883664
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie._TKN_HOST == 'token.4tube.com' and ie.IE_NAME == '4tube'


# Generated at 2022-06-14 16:15:21.913340
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from . import FuxIE
    
    info_dict = FuxIE()._real_extract("https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow")
    assert info_dict["id"] == "195359"
    assert info_dict["ext"] == "mp4"
    assert info_dict["title"] == "Awesome fucking in the kitchen ends with cum swallow"
    assert info_dict["uploader"] == "alenci2342"
    assert info_dict["uploader_id"] == "alenci2342"
    assert info_dict["upload_date"] == "20131230"
    assert info_dict["timestamp"] == 1388361660
    assert info_dict["duration"] == 289
    assert info_dict["view_count"] > 0

# Generated at 2022-06-14 16:15:24.116855
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE().to_screen('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')

# Generated at 2022-06-14 16:15:30.190332
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    from .test_com import test_html
    porner_bros_ie = PornerBrosIE()
    assert porner_bros_ie.__class__ == PornerBrosIE
    assert porner_bros_ie._VALID_URL == PornerBrosIE._VALID_URL
    assert porner_bros_ie._TKN_HOST == PornerBrosIE._TKN_HOST
    assert porner_bros_ie._TESTS == PornerBrosIE._TESTS
    import os

# Generated at 2022-06-14 16:15:46.632271
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie is not None


# Generated at 2022-06-14 16:15:58.698238
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from youtube_dl import YoutubeDL
    from youtube_dl.extractor import gen_extractors_by_id
    from youtube_dl.extractor import unescapeHTML

    ydl = YoutubeDL(params= {'debug_printtraffic': 'true'}, auto_init=False)
    ydl.add_default_info_extractors()
    gen_extractors_by_id(ydl)
    extractor = ydl._downloader.extractor_manager.get_info_extractor_for_url('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2022-06-14 16:16:08.675588
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    infoextractor = FourTubeIE()
    assert infoextractor.IE_NAME == '4tube'
    assert infoextractor.IE_DESC == '4tube and other porn sites'
    assert infoextractor.ie_key() == '4tube'
    assert infoextractor.WEBPAGE_URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert infoextractor.VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert infoextractor.TKN_HOST == 'token.4tube.com'



# Generated at 2022-06-14 16:16:10.691545
# Unit test for constructor of class FuxIE
def test_FuxIE():
	obj = FuxIE('http://www.fux.com/video/')
	assert obj.IE_NAME == '4tube'

# Generated at 2022-06-14 16:16:12.449671
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()._download_webpage

# Generated at 2022-06-14 16:16:13.657867
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:16:17.268043
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE('FourTubeIE', 'http://www.4tube.com/', 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2022-06-14 16:16:21.188068
# Unit test for constructor of class FuxIE
def test_FuxIE():
    try:
        # print FuxIE.__bases__
        # print FourTubeBaseIE.__bases__
        assert FuxIE.__bases__[0] == FourTubeBaseIE
    except Exception:
        assert False


# Generated at 2022-06-14 16:16:28.075131
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert FuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert FuxIE._TKN_HOST == 'token.fux.com'



# Generated at 2022-06-14 16:16:29.029735
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:17:01.930775
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Constructor of class FourTubeBaseIE
    assert issubclass(FourTubeBaseIE, InfoExtractor)
    assert issubclass(FourTubeBaseIE, FourTubeBaseIE)


# Generated at 2022-06-14 16:17:09.014087
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    pornTubeIE = PornTubeIE()
    assert pornTubeIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert pornTubeIE._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert pornTubeIE._TKN_HOST == 'tkn.porntube.com'

# Generated at 2022-06-14 16:17:17.198985
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    video_id = '209733'
    url = 'http://www.4tube.com/videos/%s/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black' % video_id
    # request for constructor of class FourTubeIE with url
    req = FourTubeIE._request_webpage(url, video_id)
    # download from url
    html = compat_urllib_request.urlopen(req).read()
    # Get the first token occurs in html
    token = re.search('<button[^>]+data-token="(?P<token>[^"]+)"', html).group("token")
    # Get mediaId

# Generated at 2022-06-14 16:17:28.742195
# Unit test for constructor of class PornTubeIE

# Generated at 2022-06-14 16:17:29.901305
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    return PornerBrosIE()._TESTS

# Generated at 2022-06-14 16:17:38.101862
# Unit test for constructor of class FuxIE

# Generated at 2022-06-14 16:17:43.872504
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Create an object of FourTubeIE
    ie = FourTubeIE()
    assert hasattr(ie, '_DOWNLOAD_WEBPAGE_HANDLER')
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, 'IE_NAME')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, '_TKN_HOST')
    assert hasattr(ie, '_URL_TEMPLATE')
    assert hasattr(ie, '_html_search_regex')
    assert hasattr(ie, '_search_regex')
    assert hasattr(ie, '_html_search_meta')
    assert hasattr(ie, '_download_json')
    assert hasattr(ie, '_download_webpage')

# Generated at 2022-06-14 16:17:50.413585
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._TESTS[0]['url'] == 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

# Generated at 2022-06-14 16:17:53.821097
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:17:55.168183
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    p = PornerBrosIE()
    assert p.IE_NAME == '4tube'



# Generated at 2022-06-14 16:19:22.040906
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    obj = FourTubeIE()
    assert obj._TKN_HOST == 'token.4tube.com'


# Generated at 2022-06-14 16:19:30.115153
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Test with wild card patterns
    url = 'https://www.4tube.com/videos/397612/lexi-belle-and-skin-diamond-kiss-and-suck-dick'
    ie = FourTubeIE(url)
    assert ie._url == url
    assert ie.name == '4tube'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

    # Test without wild card patterns
    url = 'https://www.4tube.com/videos/397612/lexi-belle-and-skin-diamond-kiss-and-suck-dick'
    ie

# Generated at 2022-06-14 16:19:31.203091
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE('PornTube')

# Generated at 2022-06-14 16:19:39.620448
# Unit test for constructor of class FuxIE
def test_FuxIE():
    instance = FuxIE()
    url = "https://www.fux.com/video/33000/russian-teen-gets-fucked"
    webpage = instance._download_webpage(url, None)
    video = instance._parse_json(instance._search_regex(r'INITIALSTATE\s*=\s*(["\'])(?P<value>(?:(?!\1).)+)\1',
                                                        webpage, 'data', group='value'), None,
                                 transform_source=lambda x: compat_urllib_parse_unquote(compat_b64decode(x).decode('utf-8')))['page']['video']
    print(webpage)
    print(video)

# Generated at 2022-06-14 16:19:46.524494
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE('4tube.com')
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:19:49.269175
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE(None)
    f = ie._extract_formats(None, None, None, None)
    assert len(f) > 0
    assert f[0]['url']

# Generated at 2022-06-14 16:19:57.495753
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # test PornTubeIE constructor function
    assert PornTubeIE(PornTubeIE.ie_key()).extract('http://www.porntube.com/videos/teen-couple-doing-anal_7089759') == {
        'id': '7089759', 'ext': 'mp4', 'title': 'Teen couple doing anal', 'uploader': 'Alexy', 'uploader_id': '91488', 'upload_date': '20150606', 'timestamp': 1433595647, 'duration': 5052, 'view_count': int, 'like_count': int, 'age_limit': 18}

# Generated at 2022-06-14 16:20:05.825557
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    test_case = FourTubeIE()
    assert test_case._VALID_URL == re.compile(r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
    assert test_case._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert test_case._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:20:08.293332
# Unit test for constructor of class FuxIE
def test_FuxIE():
    result = FuxIE()._extract_formats('', '', '', [])
    assert len(result) == 0



# Generated at 2022-06-14 16:20:11.645748
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
	print("In test_PornTubeIE function")
	ie = PornTubeIE()
	assert ie.IE_NAME == 'PornTube'
	