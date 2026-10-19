

# Generated at 2022-06-14 17:37:39.629013
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test for WallaIE.__init__(self, url)
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')


# Generated at 2022-06-14 17:37:42.123798
# Unit test for constructor of class WallaIE
def test_WallaIE():
    i = WallaIE()
    if not i:
        print('Constructor of WallaIE not working')


# Generated at 2022-06-14 17:37:47.257336
# Unit test for constructor of class WallaIE
def test_WallaIE():
	class Info:
	    def __init__(self):
	        self.IE_NAME = 'walla'
	info = Info()
	wallaIE = WallaIE(info)
	assert wallaIE
	assert wallaIE.ie_key() == 'walla'
	assert wallaIE.ie_name() == 'walla'


# Generated at 2022-06-14 17:37:52.009087
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie is not None

# Generated at 2022-06-14 17:37:53.457792
# Unit test for constructor of class WallaIE
def test_WallaIE():
    e = WallaIE()
    print(e._VALID_URL)

# Generated at 2022-06-14 17:37:56.606278
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla'
    assert ie.IE_DESC == 'Walla!'
    assert ie._VALID_URL == WallaIE._VALID_URL
    assert ie._TEST == WallaIE._TEST

# Generated at 2022-06-14 17:37:59.429270
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE({'params': {'verbose': True, 'forceurl': True, 'forcetitle': True, 'forceid': True, 'forcethumbnail': True}})

# Generated at 2022-06-14 17:38:02.374491
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE().extract_url('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:38:09.020751
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:38:11.080105
# Unit test for constructor of class WallaIE
def test_WallaIE():
	try:
		assert(type(WallaIE())==WallaIE)
	except AssertionError as e:
		return e

# Generated at 2022-06-14 17:38:22.573407
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # test constructor
    ie = WallaIE(None)

# Generated at 2022-06-14 17:38:35.170654
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Run this unit test to check if WallaIE()._VALID_URL can match with http://vod.walla.co.il/movie/2642630/one-direction-all-for-one
    from .common import get_testdata_file
    from .common import WallaIE
    from .common import urlopen
    import unittest

    class TestWallaIE(unittest.TestCase):
        def setUp(self):
            self.ie = WallaIE()
            self.fixture_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
            self.fixture_file = get_testdata_file('walla-2642630.html')


# Generated at 2022-06-14 17:38:38.155089
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Create an instance of WallaIE to test it
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:38:42.120837
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert isinstance(ie, WallaIE)

# Generated at 2022-06-14 17:38:52.462495
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.get_domain() == 'vod.walla.co.il'
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert WallaIE._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:38:57.050651
# Unit test for constructor of class WallaIE
def test_WallaIE():
    d = WallaIE()
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    d.url_result(test_url)
    d.suitable(test_url)

# Generated at 2022-06-14 17:39:03.404641
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Simple test for constructor of class WallaIE
    """
    walla_test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    walla_test_url_obj = WallaIE(walla_test_url)
    assert walla_test_url_obj.IE_NAME == 'walla'
    assert walla_test_url_obj.VALID_URL ==  r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert walla_test_url_obj.IE_DESC == 'Walla! video'

# Generated at 2022-06-14 17:39:07.036455
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.initialize_server_handler()
    assert ie._VALID_URL
    assert ie._TEST
    assert ie._SUBTITLE_LANGS

# Generated at 2022-06-14 17:39:08.645341
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ydl = WallaIE()

# Generated at 2022-06-14 17:39:14.445995
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:27.467401
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("WallaIE")
    ie._VALID_URL

# Generated at 2022-06-14 17:39:31.740539
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:34.357841
# Unit test for constructor of class WallaIE
def test_WallaIE():
    wallaie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert wallaie.name == 'Walla'


# Generated at 2022-06-14 17:39:36.072956
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:39:38.455673
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('')
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:39:39.536847
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie

# Generated at 2022-06-14 17:39:50.317257
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test = WallaIE()
    assert test._VALID_URL == "https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)"

# Generated at 2022-06-14 17:39:52.633729
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    # Test with valid URL
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:56.294019
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.IS_IE
    assert ie._VALID_URL == WallaIE._VALID_URL
    assert ie._TEST == WallaIE._TEST
    assert ie._SUBTITLE_LANGS == WallaIE._SUBTITLE_LANGS
    assert ie._test_suite == WallaIE._test_suite

# Generated at 2022-06-14 17:40:05.434160
# Unit test for constructor of class WallaIE
def test_WallaIE():

    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    w = WallaIE()
    w._VALID_URL = r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    mobj = re.match(w._VALID_URL, test_url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    video = w._download_xml(
        'http://video2.walla.co.il/?w=null/null/%s/@@/video/flv_pl' % video_id,
        display_id)
    item = video.find

# Generated at 2022-06-14 17:40:44.438765
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test WallaIE class constructor
    # 
    # Input:
    #   url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    #   ie = WallaIE(url)
    # Output:
    #   'id' = 2642630
    #   'display_id' = 'one-direction-all-for-one'
    #   'url' = url
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE(url)
    assert ie.id == '2642630'
    assert ie.display_id == 'one-direction-all-for-one'
    assert ie.url == url


# Generated at 2022-06-14 17:40:49.153863
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print("Unit test for constructor of class WallaIE")
    
    new_WallaIE = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert(new_WallaIE)
    
    print("Unit test for constructor of class WallaIE - ok")    
    

# Generated at 2022-06-14 17:40:51.709683
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:40:54.396100
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:41:02.642568
# Unit test for constructor of class WallaIE
def test_WallaIE():
    downloader = InfoExtractor()
    ie = WallaIE()
    ie.to_screen = downloader.to_screen
    ie.post_process = downloader._post_process
    ie.process_info = downloader._process_info
    ie.add_default_callback = downloader.add_default_callback
    ie.info_processors = downloader.info_processors
    ie._prepare_format = downloader._prepare_format
# End unit test

# Generated at 2022-06-14 17:41:15.491249
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # check constructor input
    assert WallaIE(
        walla_ie.common.InfoExtractor(walla_ie.common.InfoExtractor._downloader, {}))._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\\d+)/(?P<display_id>.+)'
    # check constructor output

# Generated at 2022-06-14 17:41:23.535594
# Unit test for constructor of class WallaIE
def test_WallaIE():
	info_dict = {
		'id': '2642630',
		'display_id': 'one-direction-all-for-one',
		'ext': 'flv',
		'title': 'וואן דיירקשן: ההיסטריה',
		'description': 'md5:de9e2512a92442574cdb0913c49bc4d8',
		'thumbnail': 're:^https?://.*\.jpg',
		'duration': '3600',
	}

	url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one',
	ie = WallaIE()
	ie.extract(url)
	# ie.ext

# Generated at 2022-06-14 17:41:26.862760
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE("www.walla.co.il")._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:41:35.120364
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:41:39.204037
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:42:39.574595
# Unit test for constructor of class WallaIE
def test_WallaIE():
	# Create an instance of class WallaIE
	walla = WallaIE()
	assert walla

# Generated at 2022-06-14 17:42:41.139909
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # test for constructor of class WallaIE
    WallaIE()

# Generated at 2022-06-14 17:42:44.942629
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert (ie.VALID_URL == ie._VALID_URL)

# Generated at 2022-06-14 17:42:46.206129
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_WallaIE = WallaIE()

# Generated at 2022-06-14 17:42:53.724580
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)' 

# Generated at 2022-06-14 17:42:57.229738
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ies = [WallaIE()]
    for ie in ies:
        ie._extract_formats('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:43:00.344872
# Unit test for constructor of class WallaIE
def test_WallaIE():

    # test WallaIE's constructor (smoke test)
    ie = WallaIE()
    ie.extract(url='http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')


# Generated at 2022-06-14 17:43:12.363864
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla'
    assert ie.IE_DESC == 'Walla! VOD'
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:43:20.878179
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:43:32.185643
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test WallaIE class
    file = __file__
    if file[-1] in 'oc':
        file = file[:-1]
    filename = file.split('/')[-1]

    ie = WallaIE(filename, {}, {}, {})
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:45:28.390918
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one');
    assert ie is not None

# Generated at 2022-06-14 17:45:33.835448
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    # Test constructor
    ie = WallaIE(url)
    # Test method extract_videos
    ie.extract_videos()



# Generated at 2022-06-14 17:45:34.290042
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:45:38.041599
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url1 = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    result = WallaIE()._match_id(url1)
    assert isinstance(result, tuple)
    assert result == ('2642630', 'one-direction-all-for-one')

# Generated at 2022-06-14 17:45:43.649495
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:45:52.191105
# Unit test for constructor of class WallaIE
def test_WallaIE():
    exp = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert exp == WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert exp != WallaIE('http://vod.walla.co.il/movie/2642630/one-direct1ion-all-for-one')
    assert exp != WallaIE('http://vod.walla.co.il/movie/2642631/one-direction-all-for-one')

# Generated at 2022-06-14 17:45:53.338084
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE.__name__ == 'WallaIE'

# Generated at 2022-06-14 17:46:00.464799
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:46:09.835325
# Unit test for constructor of class WallaIE
def test_WallaIE():
    wallaie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert wallaie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert wallaie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert wallaie._TEST['info_dict']['id'] == '2642630'
    assert wallaie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:46:16.477959
# Unit test for constructor of class WallaIE
def test_WallaIE():
    inst = WallaIE(None)
    assert inst._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'