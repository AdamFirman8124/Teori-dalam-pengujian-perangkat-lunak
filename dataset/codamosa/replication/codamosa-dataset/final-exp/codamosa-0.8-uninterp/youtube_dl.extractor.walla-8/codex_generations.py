

# Generated at 2022-06-14 17:37:41.058709
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._SUBTITLE_LANGS['עברית'] == 'heb'
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._TEST['info_dict']['id'] == '2642630'
    assert ie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert ie._TEST['params']['skip_download'] == True

# Generated at 2022-06-14 17:37:49.110032
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None, None)
    assert ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one') == True
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie.__str__() == ('WallaIE [http://vod.walla.co.il/movie/2642630/one-direction-all-for-one]')

if __name__ == '__main__':
    test_WallaIE()

# Generated at 2022-06-14 17:37:49.587858
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:37:57.660964
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_json = """
        {{
            "file": "0.flv",
            "link": "0.flv",
            "title": "thumbnailURL",
            "duration": "3600",
            "thumbnail": "thumbnailURL",
            "file_size": "0",
            "file_size_txt": "0MB",
            "quality": "0"
        }}
        """

    ie = WallaIE()
    ie._parse_json(test_json, "")

# Generated at 2022-06-14 17:37:58.117975
# Unit test for constructor of class WallaIE
def test_WallaIE():
    pass

# Generated at 2022-06-14 17:37:58.881978
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:38:05.696884
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla'
    assert ie.IE_DESC == 'Walla! video'
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._SUBTITLE_LANGS == {
        'עברית': 'heb',
    }

# Generated at 2022-06-14 17:38:08.020962
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(None, "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one") is not None

# Generated at 2022-06-14 17:38:09.057092
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:38:16.605855
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE_CLASS = WallaIE
    IE_NAME = "walla.co.il"
    WALLA_URL = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    test_ie = IE_CLASS(WALLA_URL)
    assert_equal(type(test_ie), IE_CLASS)

# Unit test to assert the tests are not empty

# Generated at 2022-06-14 17:38:23.140912
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.SUFFIX == '/video/flv_pl'

# Generated at 2022-06-14 17:38:27.436843
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'walla'
    assert ie.IE_NAME == 'Walla! VOD'
    assert ie.SEARCH_KEY == 'walla'


# Generated at 2022-06-14 17:38:32.395787
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    # This block call to constructor of class WallaIE
    WallaIE(url).extract(url,download=False)
    WallaIE(url).get_url()

# Generated at 2022-06-14 17:38:35.760735
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('WallaIE', 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie is not None

# Generated at 2022-06-14 17:38:41.100059
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    obj = ie._real_extract(ie._VALID_URL)
    assert obj['display_id'] == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:38:43.267186
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract(WallaIE._TEST['url'])

# Generated at 2022-06-14 17:38:44.451396
# Unit test for constructor of class WallaIE
def test_WallaIE():
  from WallaIE import WallaIE
  WallaIE()

# Generated at 2022-06-14 17:38:45.849195
# Unit test for constructor of class WallaIE
def test_WallaIE():
	assert WallaIE.__name__ == "WallaIE"

# Generated at 2022-06-14 17:38:49.308427
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://example.com').register_ie(WallaIE.ie_key(), WallaIE)
    WallaIE('http://example.com')

# Generated at 2022-06-14 17:38:49.931541
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:39:08.243028
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Check if url is valid
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    mobj = re.match(WallaIE._VALID_URL, url)
    assert mobj

    # Check video id and display id are extracted correctly
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert video_id == '2642630'
    assert display_id == 'one-direction-all-for-one'

    # Check if subtitles are correctly extracted from the subtitles xml

# Generated at 2022-06-14 17:39:11.881379
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    ie.extract()
    pass

# Generated at 2022-06-14 17:39:16.258962
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE()
    pass

# Unit test to verify name of the class

# Generated at 2022-06-14 17:39:18.596330
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.TEST



# Generated at 2022-06-14 17:39:22.747363
# Unit test for constructor of class WallaIE
def test_WallaIE():
    info_extractor = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert info_extractor.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one') == True

# Generated at 2022-06-14 17:39:27.556755
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie.ie_key() == 'Walla'
    assert ie.SUCCESS == {}
    assert ie.IE_DESC == 'Walla'

# Generated at 2022-06-14 17:39:28.607724
# Unit test for constructor of class WallaIE
def test_WallaIE():
	ie = WallaIE()

# Generated at 2022-06-14 17:39:31.671727
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    # Check that WallaIE has been invoked correctly
    assert(ie.ie_key() == 'Walla')


# Generated at 2022-06-14 17:39:37.804300
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test constructor
    ie = WallaIE()
    assert ie.__class__.__name__ == 'WallaIE'
    assert ie.ie_key() == 'walla'
    assert ie.ie_key_map() == {'walla': WallaIE()}
    assert ie.site_name() == 'Walla!'
    assert ie.description() == 'Walla!'
    assert ie.age_limit() is None

# Generated at 2022-06-14 17:39:47.735884
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """test WallaIE using WallaIE class"""

    import unittest
    
    class TestWallaIE(unittest.TestCase):
        
        def test_class(self):
            # First testing that the class loads and is properly instanciated
            ie = WallaIE("""<html>
            <body>
            """
            )
            assert ie.__class__.__name__ == "WallaIE"
            assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
   
    unittest.main()

# Generated at 2022-06-14 17:40:17.048933
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    print(ie)
    assert isinstance(ie, WallaIE)
    # Test parse URL
    url_input = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    res = ie.extract(url_input)
    assert isinstance(res, dict)

# Generated at 2022-06-14 17:40:22.722462
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:40:27.087792
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert obj._TEST == obj._real_extract(obj._TEST["url"])

# Generated at 2022-06-14 17:40:27.839460
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:40:34.118722
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.SUCCEEDED == ie.succeeded
    assert ie.FAILED == ie.failed
    assert ie.SKIPPED == ie.skipped
    assert ie.IETYPE == 'WallaIE'
    assert ie.IENAME == 'Walla'
    assert ie.SITE_NAME == 'Walla VOD'
    assert ie._VALID_URL == ie.valid_url
    assert ie._TEST == ie.test
    assert ie._SUBTITLE_LANGS == ie.subtitle_langs


# Generated at 2022-06-14 17:40:44.793603
# Unit test for constructor of class WallaIE
def test_WallaIE():

    # Test with url of site's index
    url = 'http://vod.walla.co.il/'
    assert WallaIE._VALID_URL.search(url)

    # Test with root URL of site and path of site's index
    url = 'http://vod.walla.co.il/wallavod'
    assert WallaIE._VALID_URL.search(url)

    # Test with URL of video
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert WallaIE._VALID_URL.search(url)

    # Test with URL of video.
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert Walla

# Generated at 2022-06-14 17:40:46.731964
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Create an instance of class WallaIE with
    # required parameters and run __init__
    w = WallaIE()

# Generated at 2022-06-14 17:40:50.045624
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:59.881874
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:41:07.869574
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.ie_key_name() == 'Walla'
    assert ie.extract('http://vod.walla.co.il/movie/2636375/one-direction-all-for-one')
    assert ie.extract('http://vod.walla.co.il/movie/2636375/one-direction-all-for-one?da')
    assert ie.extract('http://vod.walla.co.il/movie/2636375/one-direction-all-for-one?da?vbn')



# Generated at 2022-06-14 17:41:49.115415
# Unit test for constructor of class WallaIE
def test_WallaIE():
    pass

# Generated at 2022-06-14 17:41:50.477212
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, WallaIE)

# Generated at 2022-06-14 17:41:51.694800
# Unit test for constructor of class WallaIE
def test_WallaIE():
    pass

# Generated at 2022-06-14 17:41:53.525227
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download(_TEST)
    return True

# Unit test

# Generated at 2022-06-14 17:41:55.662836
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:41:58.502346
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla'

# Generated at 2022-06-14 17:42:03.487473
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .common import FakeYDL
    from .test import get_testcases

    testcases = get_testcases(WallaIE,
                             ie_key='Walla',
                             gen_extractors=True)

    ie = WallaIE()
    ie.extractor._initialize_geo_bypass({})

    for t in testcases:
        assert t.startswith('Walla:')
        yield (ie._real_extract, [t])

# Generated at 2022-06-14 17:42:08.195775
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:42:12.457897
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Try to initialize instance of WallaIE and get error if it failed.
    ie = WallaIE()
    if ie is None:
        raise AssertionError('Cannot initialize instance of WallaIE')
    if not isinstance(ie, WallaIE):
        raise AssertionError('Instance of WallaIE has wrong type')

# Generated at 2022-06-14 17:42:19.990112
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:44:15.081112
# Unit test for constructor of class WallaIE
def test_WallaIE():
    #Test: constructor of class WallaIE
    assert WallaIE._VALID_URL



# Generated at 2022-06-14 17:44:15.757476
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie

# Generated at 2022-06-14 17:44:18.012722
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:44:21.005472
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:44:26.779425
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Initialize the class object
    wie = WallaIE({})
    # Some random string
    not_a_url = 'This is a random string and not a URL'
    # Testing whether not_a_url matches the regular expression
    wie._match_id(not_a_url)
    # Testing whether the url input matches the regular expression
    wie._match_id('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:44:35.710146
# Unit test for constructor of class WallaIE
def test_WallaIE():
    i = WallaIE()
    assert i._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:44:36.643244
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from . import WallaIE
    assert WallaIE

# Generated at 2022-06-14 17:44:38.283884
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:44:46.392244
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    walla = WallaIE()
    mobj = re.match(walla._VALID_URL, url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    video = walla._download_xml(
        'http://video2.walla.co.il/?w=null/null/%s/@@/video/flv_pl' % video_id,
        display_id)
    assert video


# Unit test that checks that WallaIE._real_extract will return the expected dictionary

# Generated at 2022-06-14 17:44:58.322282
# Unit test for constructor of class WallaIE