

# Generated at 2022-06-14 17:37:32.702753
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE(None)._get_video_info()

# Generated at 2022-06-14 17:37:36.024636
# Unit test for constructor of class WallaIE
def test_WallaIE():
    VIDEO_URL = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    ie = WallaIE()
    ie.extract(VIDEO_URL)
    assert ie.IE_NAME == "walla"

# Generated at 2022-06-14 17:37:38.133213
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = type('obj', (object,), {'WallaIE': WallaIE})
    obj.WallaIE(None)

# Generated at 2022-06-14 17:37:43.880114
# Unit test for constructor of class WallaIE
def test_WallaIE():
    '''
    Test if WallaIE constructor works
    '''

    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

    # Souldn't raise any exception
    test_walla = WallaIE(url)
    assert test_walla is not None

# Generated at 2022-06-14 17:37:45.443867
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.__class__ == WallaIE

# Generated at 2022-06-14 17:37:48.210950
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Initializing the object.
    video = WallaIE()

    # Checking whether the object has been initialized or not
    assert video is not None, "Failed to initialize video object for WallaIE"


# Generated at 2022-06-14 17:37:49.881146
# Unit test for constructor of class WallaIE
def test_WallaIE():
    e = WallaIE()

# Generated at 2022-06-14 17:37:53.923029
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:37:57.301086
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("WallaIE")
    assert ie is not None, "Unit test for WallaIE failed."

# Generated at 2022-06-14 17:37:59.772467
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:38:10.053875
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE() is not None

# Generated at 2022-06-14 17:38:13.630250
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    if ie:
        pass #TODO - need to implement this test

# Generated at 2022-06-14 17:38:15.587144
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie._VALID_URL == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:38:23.375428
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:25.114604
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE(WallaIE._downloader)
    assert w is not None

# Generated at 2022-06-14 17:38:26.352925
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, InfoExtractor)
    return ie


# Generated at 2022-06-14 17:38:31.219138
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.ie_name() == 'walla.co.il'
    assert ie.ie_info() == ie.ie_key() + " - " + ie.ie_name()

# Generated at 2022-06-14 17:38:43.175612
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:53.677634
# Unit test for constructor of class WallaIE
def test_WallaIE():
    import unittest
    class TestWallaIE(unittest.TestCase):
        def test_WallaIE_constructor(self):
            """ Test WallaIEConstructor  """
            TestWallaIE = WallaIE("test")
            self.assertEqual(TestWallaIE._VALID_URL,"https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)")
            self.assertEqual(len(TestWallaIE._TEST),4)
            self.assertEqual(TestWallaIE._TEST['url'],'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:03.245774
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:39:24.312913
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(WallaIE.ie_key()).ie_key() == 'Walla'

# Generated at 2022-06-14 17:39:27.279353
# Unit test for constructor of class WallaIE
def test_WallaIE():
	test = WallaIE()
	assert test.IE_NAME == 'walla'


# Generated at 2022-06-14 17:39:32.447452
# Unit test for constructor of class WallaIE
def test_WallaIE():
    t = WallaIE()
    assert t.url_result('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert t.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:33.386825
# Unit test for constructor of class WallaIE
def test_WallaIE():
	assert WallaIE()._VALID_URL

# Generated at 2022-06-14 17:39:36.952677
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE("url")._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:42.127163
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.SUCCESS == ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:51.893034
# Unit test for constructor of class WallaIE
def test_WallaIE():
    c = WallaIE()
    c.set_url('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    c.extract()
    title = c.get('title')
    assert(title == 'וואן דיירקשן: ההיסטריה')
    url = c.get('url')
    assert(url == 'rtmp://wafla.walla.co.il/vod')
    play_path = c.get('play_path')
    assert(play_path == '/wallavod/walla/production/mp4/264/2642/2642630.mp4')

# Generated at 2022-06-14 17:39:54.937294
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, WallaIE)

# Generated at 2022-06-14 17:39:57.804104
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_WallaIE = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:40:06.723359
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Unit test for WallaIE
    from six.moves import urllib
    from six.moves import reload_module
    from ytdl_server.info_extractors import WallaIE
    import ytdl_server.utils
    reload_module(ytdl_server.utils)
    from ytdl_server.server import MODE, MODES
    if MODE not in MODES:
        MODE = "test"
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"

# Generated at 2022-06-14 17:40:54.200852
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Subclass of YoutubeIE
    assert issubclass(WallaIE, InfoExtractor)

# Generated at 2022-06-14 17:40:56.317001
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj.ie_key() == "Walla"
    assert obj.ie_name() == "Walla"

# Generated at 2022-06-14 17:40:59.527093
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    WallaIE(url)

# Generated at 2022-06-14 17:41:03.909436
# Unit test for constructor of class WallaIE
def test_WallaIE():
	# Create an instance of WallaIE
	TestWallaIEInstance = WallaIE()
	# Check if the video link is correct
	assert TestWallaIEInstance._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:41:05.164426
# Unit test for constructor of class WallaIE
def test_WallaIE():
   video = WallaIE()
test_WallaIE()

# Generated at 2022-06-14 17:41:08.261327
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE('WallaIE', 'http://video2.walla.co.il/?w=null/null/%s/@@/video/flv_pl')
    assert instance.__class__.__name__ == 'WallaIE'



# Generated at 2022-06-14 17:41:12.443671
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert isinstance(WallaIE({}, {'url': 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'}),
                      WallaIE)

# Generated at 2022-06-14 17:41:13.977004
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == WallaIE._VALID_URL

# Generated at 2022-06-14 17:41:19.882288
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    match_obj = re.match(WallaIE._VALID_URL, test_url)
    if match_obj is not None:
        video_id = str(match_obj.group('id'))
        display_id = str(match_obj.group('display_id'))
        assert video_id == "2642630"
        assert display_id == "one-direction-all-for-one"

# Generated at 2022-06-14 17:41:30.849657
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    test_display_id = 'one-direction-all-for-one'
    test_video_id = '2642630'
    walla_instance = WallaIE()
    walla_instance._real_extract(test_url)

    # Tests for url verification
    assert re.match(walla_instance._VALID_URL, test_url), \
        'The url is not recognized as valid Walla url'

    # Tests for parent methods
    assert walla_instance._download_xml(test_url, test_display_id), \
        'Failed to download xml from Walla.co.il'


# Generated at 2022-06-14 17:43:29.854689
# Unit test for constructor of class WallaIE
def test_WallaIE():
    papa = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    # we use two variables to test two different things:
    # 1) that the _VALID_URL regex works
    # 2) that the mobj object has the wanted info
    assert papa._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert papa.video_url == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert papa.video_id == '2642630'

# Generated at 2022-06-14 17:43:39.495425
# Unit test for constructor of class WallaIE
def test_WallaIE():

    # inputs
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()

    # behavior
    mobj = re.match(extractor._VALID_URL, url)

    # validation
    # mobj.group('id') is a string
    assert(isinstance(mobj.group('id'), str))
    # mobj.group('display_id') is a string
    assert(isinstance(mobj.group('display_id'), str))
    # mobj.group('id') == '2642630'
    assert(mobj.group('id') == '2642630')
    # mobj.group('display_id') == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:43:42.526387
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie, url = WallaIE(), "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    assert ie.suitable(url)
    # Tests for class WallaIE
    ie.download(url)

# Generated at 2022-06-14 17:43:45.872840
# Unit test for constructor of class WallaIE
def test_WallaIE():
    constructor_test(WallaIE.__name__, WallaIE._TEST['url'])

# Generated at 2022-06-14 17:43:48.209011
# Unit test for constructor of class WallaIE
def test_WallaIE():
    info = WallaIE()._real_extract("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:43:54.884602
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL.match('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert WallaIE._SUBTITLE_LANGS.keys() == ['עברית']

# Generated at 2022-06-14 17:43:59.837569
# Unit test for constructor of class WallaIE
def test_WallaIE():
    info = WallaIE()._extract_info(WallaIE()._TEST['url'])
    assert info['url'] == WallaIE()._TEST['url']
    assert info['id'] == WallaIE()._TEST['id']
    assert info['title'] == WallaIE()._TEST['title']
    assert info['duration'] == WallaIE()._TEST['duration']

# Generated at 2022-06-14 17:44:03.323766
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'Walla'

# Generated at 2022-06-14 17:44:10.467476
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie = WallaIE('https://example.com')
    ie = WallaIE('https://example.com/video.mp4')
    assert ie.url == 'https://example.com/video.mp4'
    ie = WallaIE('https://example.com/video.mp4', 'my_ie')
    ie = WallaIE('https://example.com/video.mp4', 'my_ie', 'My IE')
    assert ie.url == 'https://example.com/video.mp4'
    assert ie.ie_key == 'my_ie'
    assert ie.ie_key == 'my_ie'

# Generated at 2022-06-14 17:44:11.020051
# Unit test for constructor of class WallaIE
def test_WallaIE():
    pass

# Generated at 2022-06-14 17:46:00.231123
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Create instance of the class WallaIE
    video = WallaIE()
    
    mobj = re.match(video._VALID_URL, video._TEST['url'])
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    
    video_xml = video._download_xml(
        'http://video2.walla.co.il/?w=null/null/%s/@@/video/flv_pl' % video_id,
        display_id)

    video_item = video_xml.find('./items/item')

    title = video._html_search_regex(video._TEST['url'],
                                     video._TEST['info_dict']['title'],
                                     'title', default=None)
    description

# Generated at 2022-06-14 17:46:09.756322
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:46:10.602529
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert 1 == 1


# Generated at 2022-06-14 17:46:17.028716
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:46:25.506237
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()._build_url_result(WallaIE()._VALID_URL, "2642630", "one-direction-all-for-one")
    assert w.get('url') == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert w.get('id') == '2642630'
    assert w.get('display_id') == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:46:26.627945
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_WallaIE = WallaIE()

# Generated at 2022-06-14 17:46:32.934093
# Unit test for constructor of class WallaIE
def test_WallaIE():
	assert WallaIE(InfoExtractor)._VALID_URL=='https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:46:34.072498
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:46:36.650191
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Create a WallaIE object
    ie = WallaIE()
    # Check that it is a correct IExtractor object
    assert ie.get_test() is not None and isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:46:41.881871
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla_ie = WallaIE()
    assert walla_ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'