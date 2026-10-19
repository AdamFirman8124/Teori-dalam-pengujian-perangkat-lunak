

# Generated at 2022-06-14 16:13:46.053865
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie.IE_NAME == 'Fux'

# Generated at 2022-06-14 16:13:51.454127
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    newly_built_instance = FourTubeBaseIE()
    assert newly_built_instance is not None

# Unit tests for class FourTubeIE
# def test_FourTubeIE():
#     newly_built_instance = FourTubeIE()
#     assert newly_built_instance is not None
#
# def test_FourTubeIE_can_download_video():
#     # Arrange
#     url = 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
#
#     # Act
#     results = newly_built_instance.download_video(url)
#
#     # Assert
#     assert results is not None
#
# def test_FourTubeIE_can_get_video_info():
#    

# Generated at 2022-06-14 16:13:55.914634
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    try:
        pb = PornerBrosIE()
        return pb
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    pb = test_PornerBrosIE()
    print(pb.extract('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'))

# Generated at 2022-06-14 16:14:01.687384
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    test_ins = PornTubeIE();
    assert (test_ins._TKN_HOST == 'tkn.porntube.com')
    assert (test_ins._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s')
    assert (test_ins._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)')
    assert (test_ins._TESTS != []);

# Generated at 2022-06-14 16:14:14.329480
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:14:15.770738
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    porner_bros_ie = PornerBrosIE()

# Generated at 2022-06-14 16:14:17.407129
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    test = FourTubeBaseIE()

# Generated at 2022-06-14 16:14:18.710796
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:14:20.475042
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    ie._VALID_URL
    ie._URL_TEMPLATE

# Generated at 2022-06-14 16:14:22.406379
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try:
        import requests
        import requests_toolbelt
        print("Pass")
    except ImportError:
        print("Failed")

test_FourTubeIE()

# Generated at 2022-06-14 16:14:44.537148
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeIE()
    assert ie._TKN_HOST == 'token.4tube.com'
    ie = FuxIE()
    assert ie._TKN_HOST == 'token.fux.com'
    ie = PornTubeIE()
    assert ie._TKN_HOST == 'tkn.porntube.com'
    ie = PornerBrosIE()
    assert ie._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:14:51.686383
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # the domain is '.fux.com'
    # the url is 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    # the video id is '195359'
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    # the expected output is 
    # {'id': '195359', 'ext': 'mp4', 'title': 'Awesome fucking in the kitchen ends with cum swallow', 'uploader': 'alenci2342', 'uploader_id': 'alenci2342', 'upload_date': '20131230', 'timestamp': 1388361660, 'duration': 289, 'view_count': int, 'like_count': int, 'c

# Generated at 2022-06-14 16:14:54.212219
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    porn_url = 'https://www.porntube.com/embed/7089759'
    expected_class = PornTubeIE
    assert type(info_extractor.get_info_extractor(porn_url)) == expected_class

# Generated at 2022-06-14 16:14:55.514983
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    c = PornerBrosIE()
    assert c.domain_name == 'pornerbros.com'

# Generated at 2022-06-14 16:14:58.991811
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    t = FourTubeIE()
    assert t._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'


# Generated at 2022-06-14 16:14:59.857616
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    pass

# Generated at 2022-06-14 16:15:01.170259
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    a = PornerBrosIE();


# Generated at 2022-06-14 16:15:02.775625
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()


# Generated at 2022-06-14 16:15:06.352117
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    import pytest
    from youtube_dl.extractor import FourTubeIE
    with pytest.raises(TypeError):
        FourTubeIE()
    FourTubeIE('FourTube')

# Generated at 2022-06-14 16:15:08.081156
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert issubclass(PornerBrosIE, FourTubeBaseIE)


# Generated at 2022-06-14 16:15:26.184770
# Unit test for constructor of class FuxIE
def test_FuxIE():
    video_id = 'tiny-japanese-teen-creampied-by-teen-couple'
    url = 'https://www.fux.com/video/%s/video' % video_id
    FuxIE()._real_initialize(url)

# Generated at 2022-06-14 16:15:28.649026
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    fetcher = FourTubeBaseIE()
    assert fetcher._TKN_HOST == 'token.4tube.com'
    assert fetcher._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

# Unit tests for methods of class FourTubeBaseIE

# Generated at 2022-06-14 16:15:30.279123
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Make sure we use class PornTubeIE in this test
    PornTubeIE()
    # Make sure we use class FourTubeBaseIE in this test
    FourTubeBaseIE()

# Generated at 2022-06-14 16:15:31.809348
# Unit test for constructor of class FuxIE
def test_FuxIE():
    expected = FourTubeBaseIE
    instance = FuxIE(4)
    assert isinstance(instance, expected)

test_FuxIE()

# Generated at 2022-06-14 16:15:35.782834
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    for ieclass in (FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE):
        ie = ieclass()
        ie._VALID_URL # pylint: disable=protected-access
        ie._TKN_HOST # pylint: disable=protected-access
        ie._URL_TEMPLATE # pylint: disable=protected-access

# Generated at 2022-06-14 16:15:40.706175
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Check attributes
    assert FourTubeBaseIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?(?P<site>.*?)\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert FourTubeBaseIE._URL_TEMPLATE == 'https://www.%s.com/videos/%s/video'
    assert FourTubeBaseIE._TKN_HOST == 'token.%s.com'

# Generated at 2022-06-14 16:15:41.857298
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE(FuxIE._downloader)
    assert True

# Generated at 2022-06-14 16:15:44.340907
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    ie._real_extract("http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")


# Generated at 2022-06-14 16:15:54.463050
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .test_downloader import MockYDL
    from .test_htmlparser import MockSoup
    from .test_extractor import (
        TEST_CASES, get_testcases_from_module, get_testcases_from_yaml)

    class VideoInfo(object):
        """
        Simple stub for the video info object
        """
        def __init__(self, *args, **kwargs):
            super(VideoInfo, self).__init__(*args, **kwargs)
            self.title = kwargs.get('title')
            self.url = kwargs.get('url')

    class TestFuxIE(FuxIE):
        """
        Dummy subclass for unit testing
        """


# Generated at 2022-06-14 16:16:05.923616
# Unit test for constructor of class PornTubeIE

# Generated at 2022-06-14 16:16:40.687709
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite((
        unittest.FunctionTestCase(test_PornTubeIE),
    )))

# Generated at 2022-06-14 16:16:41.676731
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:16:51.201658
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    class TestFourTubeBaseIE(FourTubeBaseIE):
        _VALID_URL = r'http://www.example.com/(?P<kind>m)\.(?P<display_id>www)\.(?P<id>com)/(?P<extra_data>\d+)'
        _URL_TEMPLATE = 'http://www.example.com/%s.%s.%s'
        _TKN_HOST = 'token.example.com'

# Generated at 2022-06-14 16:16:53.128396
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    """ Test constructor of class FourTubeIE"""
    ie = FourTubeIE()
    ie.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')

# Generated at 2022-06-14 16:17:02.605801
# Unit test for constructor of class FuxIE
def test_FuxIE():
    print('\n----------------')
    print('Running test of FuxIE')
    test_ie = FuxIE('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    fux_dict = test_ie._extract_fux('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow', '195359', '195359', ["8000", "6000", "4000", "2000"])
    assert('title' in fux_dict)
    print('Title of the FuxIE video:', fux_dict['title'])
    assert('uploader' in fux_dict)
    print('Uploader of the FuxIE video:', fux_dict['uploader'])

# Generated at 2022-06-14 16:17:04.301484
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try:
        FourTubeIE()
        # If the constructor succeeds the test has succeeded.
        assert True
    except Exception:
        # The test has failed if an exception has been thrown.
        assert False

# Generated at 2022-06-14 16:17:06.241523
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Test case: invalid url
    assert PornTubeIE()._VALID_URL is None

# Generated at 2022-06-14 16:17:06.896130
# Unit test for constructor of class FuxIE
def test_FuxIE():
	pass

# Generated at 2022-06-14 16:17:16.151860
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    f = FourTubeIE()
    assert f.ie_key() == '4tube'
    assert f._TKN_HOST == 'token.4tube.com'
    assert f._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert f._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

# Generated at 2022-06-14 16:17:17.214867
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()


# Generated at 2022-06-14 16:18:40.845269
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # instantiate a FuxIE object
    fux_ie_object = FuxIE();

    # checks if the object has useful attributes
    assert fux_ie_object.IE_NAME == "4tube"
    assert fux_ie_object._VALID_URL == r"https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?"
    assert fux_ie_object._URL_TEMPLATE == "https://www.fux.com/video/%s/video"
    assert fux_ie_object._TKN_HOST == "token.fux.com"

    # checks if the instance has the correct type

# Generated at 2022-06-14 16:18:41.586760
# Unit test for constructor of class FuxIE
def test_FuxIE():
  ie = FuxIE()

# Generated at 2022-06-14 16:18:47.388630
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
  # Constructor of FourTubeIE
  ie = FourTubeIE()
  # Exercise __init__() by setting up video_id, display_id, and url
  ie.video_id = '209733'
  ie.display_id = 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
  ie.url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'


# Generated at 2022-06-14 16:18:57.103338
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    for kind in ['www', 'm']:
        for vid in [181369, 194195]:
            # http://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369
            # http://www.pornerbros.com/videos/beautiful-lesbian-couple-get-it-on_194195
            url = 'https://{}.pornerbros.com/videos/{}_{}'.format(kind,
                    'skinny-brunette-takes-big-cock-down-her-anal-hole' if vid == 181369 else 'beautiful-lesbian-couple-get-it-on',
                    vid)

# Generated at 2022-06-14 16:18:58.507555
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE(FourTubeIE)._VALID_URL == FourTubeIE._VALID_URL

# Generated at 2022-06-14 16:19:07.508336
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    info_dict = {
        'id': '181369',
        'ext': 'mp4',
        'title': 'Skinny brunette takes big cock down her anal hole',
        'uploader': 'PornerBros HD',
        'uploader_id': 'pornerbros-hd',
        'upload_date': '20130130',
        'timestamp': 1359527401,
        'duration': 1224,
        'view_count': int,
        'categories': list,
        'age_limit': 18,
        }
    obj = PornerBrosIE()
    result = obj._real_extract(url=obj._URL_TEMPLATE % info_dict['id'])
    assert result['id'] == info_dict['id']

# Generated at 2022-06-14 16:19:08.371932
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE()

# Generated at 2022-06-14 16:19:08.940953
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    pass

# Generated at 2022-06-14 16:19:12.753094
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    """ Unit test for updated constructor.
    """
    # create instance of class PornTubeIE
    instance = PornTubeIE()
    # check if instance is of type class PornTubeIE
    if isinstance(instance, PornTubeIE):
        print('\nclass PornTubeIE and its instance are of type class PornTubeIE\n')

# Generated at 2022-06-14 16:19:21.135970
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    m = PornerBrosIE._VALID_URL
    assert PornerBrosIE._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert PornerBrosIE._TKN_HOST == 'token.pornerbros.com'
    
    assert m.match('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m.match('https://m.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    assert m.match('https://www.pornerbros.com/embed/181369')
    assert m.match

# Generated at 2022-06-14 16:22:43.188953
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        PornTubeIE()
    except Exception:
        return False
    return True

# Generated at 2022-06-14 16:22:44.271943
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:22:50.919349
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fuxIE = FuxIE()
    assert fuxIE._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fuxIE._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fuxIE._TKN_HOST == 'token.fux.com'


# Generated at 2022-06-14 16:22:52.329987
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert hasattr(ie, '_TKN_HOST')



# Generated at 2022-06-14 16:22:53.292232
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE.__init__(PornTubeIE)

# Generated at 2022-06-14 16:22:54.729493
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE()._TKN_HOST == 'token.fux.com'


# Generated at 2022-06-14 16:22:56.236110
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert issubclass(PornerBrosIE, InfoExtractor)

# Generated at 2022-06-14 16:22:58.939809
# Unit test for constructor of class FuxIE
def test_FuxIE():
    return FuxIE(None).extract('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')



# Generated at 2022-06-14 16:22:59.838483
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:23:05.436671
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    class PornerBrosIE_test(PornerBrosIE):
        def __init__(self):
            self.assertTrue(hasattr(self,'_TKN_HOST') and self._TKN_HOST == 'token.pornerbros.com')
            self.assertTrue(hasattr(self,'_URL_TEMPLATE') and self._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s')
            return
    
    self_test = PornerBrosIE_test()