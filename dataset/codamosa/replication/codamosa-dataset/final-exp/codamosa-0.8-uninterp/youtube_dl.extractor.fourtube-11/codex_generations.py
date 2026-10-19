

# Generated at 2022-06-14 16:13:38.115308
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pb = PornerBrosIE()
    assert pb

# Generated at 2022-06-14 16:13:38.880494
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:13:46.966490
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    url = 'http://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    PornTubeIE._download_webpage = lambda x, y, z: '<html></html>'

# Generated at 2022-06-14 16:13:47.714809
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:13:55.879310
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert 'PornerBrosIE' in ie.IE_NAME
    # _VALID_URL has one sub URL matching group, id
    mobj = re.match(ie._VALID_URL, 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    video_id = mobj.group('id')
    assert video_id == '181369'



# Generated at 2022-06-14 16:14:08.353803
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    # Test presence of required attributes
    assert ie.IE_NAME == '4tube'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'
    # Test presence of required methods
    assert callable(ie.extract)
    # Test presence of class attributes
    assert hasattr(ie, '_TESTS')

# Generated at 2022-06-14 16:14:17.851305
# Unit test for constructor of class FuxIE
def test_FuxIE():
    expected_FuxIE = FuxIE
    # Can we initialize the FuxIE class instance?
    assert FuxIE is not None
    # Is the class of the instance the expected one?
    assert isinstance(FuxIE(), expected_FuxIE)
    # Is FuxIE() a subclass of the superclass FourTubeBaseIE?
    assert issubclass(FuxIE(), FourTubeBaseIE)
    # Is the class of the superclass the expected one?
    assert FuxIE.__base__ == FourTubeBaseIE
    # Is the class of the superclass of the superclass the expected one?
    assert FuxIE.__base__.__base__ == InfoExtractor


# Generated at 2022-06-14 16:14:27.056595
# Unit test for constructor of class PornTubeIE

# Generated at 2022-06-14 16:14:28.620648
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE().IE_NAME == '4tube'


# Generated at 2022-06-14 16:14:36.439709
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    instance = FourTubeBaseIE()
    instance._TKN_HOST = 'token.4tube.com'
    instance._extract_formats(
    url='https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
    video_id='209733', media_id='209733', sources=['1080', '720', '540', '360', '240'])
    instance.constructor_test()


# Generated at 2022-06-14 16:15:07.970944
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    """
    Test the FourTubeIE constructor
    """
    ie = FourTubeIE('FourTube')
    assert ie.IE_NAME == '4tube'

# Generated at 2022-06-14 16:15:08.658428
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:15:19.105957
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    """
    Testing the constructor for class PornerBrosIE
    """

    pornerbros_instance = PornerBrosIE()

# Generated at 2022-06-14 16:15:23.139245
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # smoke test for FourTubeBaseIE
    # Skip due to undetermined failure
    # https://travis-ci.org/ytdl-org/youtube-dl/jobs/185144179#L633
    raise unittest.SkipTest('FourTubeBaseIE is not yet tested')
    # Please put your code of test here
    assert False, 'FourTubeBaseIE is not yet tested'

# Generated at 2022-06-14 16:15:28.874633
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    import sys
    import unittest
    from unittest import TestCase

    class TestPornTubeIE(TestCase):
        def test_url(self):
            url = 'https://www.porntube.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
            result = PornTubeIE()._VALID_URL.match(url)
            self.assertIsNotNone(result)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPornTubeIE)
    result = unittest.TestResult()
    suite.run(result)
    print(result)
    if not result.wasSuccessful():
        sys.exit(1)

# Generated at 2022-06-14 16:15:33.398429
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie_instance = PornerBrosIE()
    assert ie_instance._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie_instance._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie_instance._TKN_HOST == 'token.pornerbros.com'


# Generated at 2022-06-14 16:15:38.425801
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert ie._TKN_HOST == 'token.4tube.com'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

# Generated at 2022-06-14 16:15:39.602947
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    """Test VideoInfoExtractor subclasses can be instantiated."""
    PornTubeIE()

# Generated at 2022-06-14 16:15:44.371068
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._TKN_HOST == 'token.pornerbros.com'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'

# Generated at 2022-06-14 16:15:44.889645
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:16:15.822596
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()._extract_formats('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black', 5, 3, [])

# Generated at 2022-06-14 16:16:19.277448
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    
    porner_bros_ie = PornerBrosIE()

    assert porner_bros_ie is not None
    assert porner_bros_ie.IE_NAME == 'pornerbros'

# Generated at 2022-06-14 16:16:20.671337
# Unit test for constructor of class FuxIE
def test_FuxIE():
    foo = FuxIE()
    print("Unit test of FuxIE is successful")


# Generated at 2022-06-14 16:16:30.540216
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    parser = PornTubeIE()
    assert parser.IE_NAME == 'porntube.com'
    assert parser._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert parser._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert parser._TKN_HOST == 'tkn.porntube.com'
    #assert parser._TESTS == [{
    #    'url': 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759',
    #    'info_dict': {
    #        'id

# Generated at 2022-06-14 16:16:37.255934
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    for ie in [FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE]:

        # Check that the constructor of FourTubeBaseIE hasn't been
        # deleted or renamed in any of the subclasses
        ie.__name__
        ie.__name__

        # Check that all the attributes have been copied in all the
        # subclasses
        for attr in ['_VALID_URL', '_TKN_HOST', '_TESTS']:
            if not hasattr(ie, attr):
                raise AssertionError("Attribute '%s' not found in %s" % (attr, ie.__name__))

    # Check that all the subclasses are inside the namespace of
    # youtubedl.extractor

# Generated at 2022-06-14 16:16:42.889269
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    x = PornTubeIE()
    assert x._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert x._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert x._TKN_HOST == 'tkn.porntube.com'

# Generated at 2022-06-14 16:16:49.497978
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE();
    assert(ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?')
    assert(ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video')
    assert(ie._TKN_HOST == 'token.fux.com')


# Generated at 2022-06-14 16:16:50.870371
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE('FuxIE', 'fux.com')

# Generated at 2022-06-14 16:16:52.132977
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:17:01.745623
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2022-06-14 16:18:16.911501
# Unit test for constructor of class FuxIE
def test_FuxIE():
    import youtube_dl.extractor
    youtube_dl.extractor.default_downloader.params.update({'cookiefile': None})
    cookies = {'initi': 'true'}
    fuxIE = FuxIE(youtube_dl.extractor.default_downloader,
                  "https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow", cookies)
    assert fuxIE.download() == None


# Generated at 2022-06-14 16:18:18.847696
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try:
        FourTubeIE()
    except:
        print('Failed to create class FourTubeIE')
        raise


# Generated at 2022-06-14 16:18:21.945925
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    """
    Unit test for constructor of class FourTubeIE
    """
    assert FourTubeIE.ie_key() == '4tube'
    assert FourTubeIE(None)._TKN_HOST == 'token.4tube.com'


# Generated at 2022-06-14 16:18:27.179301
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    url = PornerBrosIE._VALID_URL
    mobj = re.match(url, 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
    PornerBrosIE(PornerBrosIE.ie_key(), url)



# Generated at 2022-06-14 16:18:27.992209
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()
    # should not raise an exception

# Generated at 2022-06-14 16:18:29.670619
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    f = FourTubeBaseIE()
    assert(f._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video')
    assert(f._TKN_HOST == 'token.4tube.com')

# Generated at 2022-06-14 16:18:30.957701
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    class Porntube(PornTubeIE):
        pass
    assert Porntube == PornTubeIE
    assert Porntube._VALID_URL == PornTubeIE._VALID_URL

# Generated at 2022-06-14 16:18:32.910860
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Test if the constructor successfully parses the PornTubeIE object
    p = PornTubeIE()
    # Test if the PornTubeIE object is an instance of class FourTubeBaseIE
    assert isinstance(p, FourTubeBaseIE)

# Generated at 2022-06-14 16:18:35.377448
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'

    # will raise KeyError if no match for `url`
    _ = re.match(FourTubeBaseIE._VALID_URL, url).groupdict()

# Generated at 2022-06-14 16:18:36.661740
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE(): 
    extractedVideo = PornerBrosIE()
    assert extractedVideo._TKN_HOST == 'token.pornerbros.com' 



# Generated at 2022-06-14 16:20:14.775088
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert isinstance(ie, FuxIE)


# Generated at 2022-06-14 16:20:16.290633
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Check of constructor for class FourTubeBaseIE
    assert True

# Unit tests for class FourTubeIE

# Generated at 2022-06-14 16:20:18.532721
# Unit test for constructor of class FuxIE
def test_FuxIE():
    _FuxIE = FuxIE(object)
    assert _FuxIE is not None

# Generated at 2022-06-14 16:20:23.635750
# Unit test for constructor of class FuxIE
def test_FuxIE():
    x = FuxIE()
    info = x._extract_formats('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow', '195359', '195359', ['360','480','720','1080'])
    assert info[0]['res'] == '360'
    assert info[0]['format_id'] == '360p'

# Generated at 2022-06-14 16:20:29.555480
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from .youtube import YoutubeIE

    old_constructor = YoutubeIE.__init__

    def new_constructor(self, *args, **kwargs):
        old_constructor(self, *args, **kwargs)
        self.server = "gvo"
    try:
        YoutubeIE.__init__ = new_constructor
        a = FourTubeBaseIE()
        print(a.server)
    finally:
        YoutubeIE.__init__ = old_constructor

# Generated at 2022-06-14 16:20:31.093214
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE()
    FuxIE()
    PornTubeIE()
    PornerBrosIE()

# Generated at 2022-06-14 16:20:32.273641
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE is FourTubeBaseIE


# Generated at 2022-06-14 16:20:32.830435
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:20:39.356139
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    sub_test_cases = [
        # Test case with bad video id.
        {'url': 'https://www.pornerbros.com/videos/video_xxx',
         'failed': True},
        {'url': 'https://www.pornerbros.com/videos/video_1',
         'failed': True}
    ]
    for sub_test_case in sub_test_cases:
        yield (check_result, sub_test_case)


# Generated at 2022-06-14 16:20:41.732813
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE(None)
    assert ie // 0 == ie._parse_json(r'{"page":{"video":{"mediaId":"1"}}}', "1")['page']['video']