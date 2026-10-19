

# Generated at 2022-06-14 17:37:40.140528
# Unit test for constructor of class WallaIE
def test_WallaIE():
	import sys

	# create an instance of WallaIE.
	walla = WallaIE()

	# create a url for test.
	url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

	# create a dictionary for the output of the test.

# Generated at 2022-06-14 17:37:42.551554
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # noinspection PyTypeChecker
    ie = WallaIE(WallaIE._downloader)
    assert ie.SUCCESS

# Generated at 2022-06-14 17:37:46.657507
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('https://vod.walla.co.il/item/2643658/one-direction-all-for-one')
    WallaIE('https://vod.walla.co.il/item/2643658/one-direction-all-for-one', {})

# Generated at 2022-06-14 17:37:52.820364
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Check that WallaIE's constructor doesn't throw an exception
    # when WallaIE class constants are used as parameters
    assert WallaIE(WallaIE.ie_key(), WallaIE._VALID_URL) is not None



# Generated at 2022-06-14 17:37:55.555126
# Unit test for constructor of class WallaIE
def test_WallaIE():
    wallaIE = WallaIE()
    wallaIE._real_extract("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert(True)

# Generated at 2022-06-14 17:38:00.693833
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """Unit test for the constructor of the class WallaIE"""
    ie = WallaIE(None)
    assert ie.SUCCESS == 'SUCCESS'
    ie.SUCCESS = 'FAIL'
    ie = WallaIE(None)
    assert ie.SUCCESS == 'SUCCESS'

# Generated at 2022-06-14 17:38:01.816289
# Unit test for constructor of class WallaIE
def test_WallaIE():
    tester = WallaIE()


# Generated at 2022-06-14 17:38:04.272102
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE.suitable("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:38:06.385933
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        assert WallaIE
    except:
        assert False

# Generated at 2022-06-14 17:38:16.010671
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE.__name__ == 'WallaIE'
    assert WallaIE.__doc__ == 'WallaTV video extractor'
    assert WallaIE._VALID_URL == \
        r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:23.989499
# Unit test for constructor of class WallaIE
def test_WallaIE():

    # Test general call
    WallaIE()

    # Test general case
    url='http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie_tester = InfoExtractor(WallaIE)
    ie_tester.extract(url)

# Generated at 2022-06-14 17:38:27.376418
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')


# Generated at 2022-06-14 17:38:38.637141
# Unit test for constructor of class WallaIE
def test_WallaIE():
  # Setup variables
  video_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

  # Create object
  ie = WallaIE()

  # Run function
  mobj = ie._real_extract(video_url)

  # Test
  assert mobj['id'] == '2642630'
  assert mobj['display_id'] == 'one-direction-all-for-one'
  assert mobj['title'] == 'וואן דיירקשן: ההיסטריה'

# Generated at 2022-06-14 17:38:50.181704
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .walla import WallaIE

    import unittest
    import sys
    class TestWallaIE(unittest.TestCase):
        def setUp(self):
            self.maxDiff = None
            self.IE = WallaIE()
        def test_constructor(self):
            self.assertEqual(self.IE.IE_NAME, 'walla:vod')
            self.assertEqual(self.IE.IE_DESC, 'Walla! VOD')
            self.assertEqual(self.IE._VALID_URL,
                r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)')


# Generated at 2022-06-14 17:38:53.523838
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE(None)

# Generated at 2022-06-14 17:38:57.211621
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    WallaIE(WallaIE._downloader).extract(url)

# Generated at 2022-06-14 17:38:58.118122
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()


# Generated at 2022-06-14 17:38:59.413317
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE(1)
    assert w.test() == True

# Generated at 2022-06-14 17:39:08.169098
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:39:14.920713
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    w = WallaIE(url)
    assert(w._VALID_URL == WallaIE._VALID_URL)
    assert(w._TEST == WallaIE._TEST)
    assert(w._SUBTITLE_LANGS == WallaIE._SUBTITLE_LANGS)

# Generated at 2022-06-14 17:39:28.517472
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == "%s.%s" % (ie.__module__, ie.__class__.__name__)



# Generated at 2022-06-14 17:39:32.823289
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test using WallaIE constructor
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie != None, 'Video should not be None'


# Generated at 2022-06-14 17:39:34.717516
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_instance = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    return test_instance

# Generated at 2022-06-14 17:39:35.643448
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()

# Generated at 2022-06-14 17:39:42.938298
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    regex = ie._VALID_URL
    exp = re.match(regex,"""http://vod.walla.co.il/movie/2642630/one-direction-all-for-one""")
    print (exp.group('id'))
    print (exp.group('display_id'))
    print (exp.groups())

# Generated at 2022-06-14 17:39:45.798186
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # https://github.com/rg3/youtube-dl/issues/5391
    assert WallaIE._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:39:47.281477
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'

# Generated at 2022-06-14 17:39:48.233177
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla = WallaIE();

# Generated at 2022-06-14 17:39:53.813520
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.url_result('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.url_result('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert False == ie.url_result('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert False == ie.url_result('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:57.239199
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._TEST['url'] == ie._VALID_URL
    assert ie._TEST['info_dict']['id'] == ie._VALID_URL

# Generated at 2022-06-14 17:40:21.788460
# Unit test for constructor of class WallaIE
def test_WallaIE():
    pass


###############################################################################
# Test for _real_extract method of class WallaIE

# Generated at 2022-06-14 17:40:24.182670
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test = WallaIE()
    test._VALID_URL = WallaIE._VALID_URL
    test._TEST = WallaIE._TEST
    test.test()

# Generated at 2022-06-14 17:40:27.449759
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = WallaIE()
    url._real_initialize({})
    assert url._real_extract({})


# Generated at 2022-06-14 17:40:28.081724
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE("")

# Generated at 2022-06-14 17:40:29.725050
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie.SUCCESS_CODES == (1, 0)

# Generated at 2022-06-14 17:40:41.417510
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_WallaIE.url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    test_WallaIE.display_id = "one-direction-all-for-one"
    test_WallaIE.video_id = "2642630"
    test_WallaIE.title = "וואן דיירקשן: ההיסטריה"
    test_WallaIE.description = "md5:de9e2512a92442574cdb0913c49bc4d8"
    test_WallaIE.thumbnail = r're:^https?://.*\.jpg'
    test_WallaIE.duration = 3600

# Generated at 2022-06-14 17:40:44.287294
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE();
    ie._real_extract(urllib.urlopen(ie._TEST['url']));

# Generated at 2022-06-14 17:40:46.226885
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(WallaIE._VALID_URL)

# Generated at 2022-06-14 17:40:49.433887
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Unit test for constructor of class WallaIE.
    """
    ie = WallaIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:40:59.356614
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE = WallaIE()
    assert re.match(IE._VALID_URL, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert re.match(IE._VALID_URL, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one/')
    assert re.match(IE._VALID_URL, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one/%D7%9E%D7%A9%D7%A4%D7%95%D7%AA')

# Generated at 2022-06-14 17:41:41.332348
# Unit test for constructor of class WallaIE
def test_WallaIE():
	w = WallaIE()
	assert w._TEST['info_dict']['ext'] == 'flv'

# Generated at 2022-06-14 17:41:53.290714
# Unit test for constructor of class WallaIE
def test_WallaIE():

    # Input data to simulate created object

    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    ie = InfoExtractor()
    ie.add_info_extractor(WallaIE())

    # Expected result for test
    result = ie.extract(url)
    assert result["id"] == "2642630"
    assert result["display_id"] == "one-direction-all-for-one"
    assert result["ext"] == "flv"
    assert result["title"] == "וואן דיירקשן: ההיסטריה"

# Generated at 2022-06-14 17:41:56.468068
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('rtmp://wafla.walla.co.il/vod/_definst_/mp4:flv_pl/2642630/2642630_1.mp4')

# Generated at 2022-06-14 17:41:58.244213
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Create an instance of WallaIE (up until this point, it doesn't
    # perform any downloads)
    WallaIE()

# Generated at 2022-06-14 17:42:00.685405
# Unit test for constructor of class WallaIE
def test_WallaIE():
    i = WallaIE()
    assert i.ie_key() == 'Walla'
    assert i.ie_name() == 'Walla'
    assert i.thumbnail() == ''


# Generated at 2022-06-14 17:42:02.643614
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:42:10.189888
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_cases = [ (
                    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'),
                    r'WallaIE\(\'http://vod.walla.co\.il/movie/2642630/one-direction-all-for-one\'\)',
                    'WallaIE(\'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one\')'
                ), ]
    for t in test_cases:
        assert str(t[0]) == t[1]
        assert repr(t[0]) == t[2]

# Generated at 2022-06-14 17:42:11.457139
# Unit test for constructor of class WallaIE
def test_WallaIE():
	# Check that importer can be initialized from this file
	from . import walla
	walla.WallaIE()

# Generated at 2022-06-14 17:42:12.500339
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """Test that we can construct an WallaIE object."""
    ie = WallaIE()

# Generated at 2022-06-14 17:42:23.768261
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # test extractor
    #initialized_ie = WallaIE()

    # test output
    #print "Subtitles lang: %s" % initialized_ie._SUBTITLE_LANGS

    test_url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"

# Generated at 2022-06-14 17:44:23.078579
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert(ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)')

# Generated at 2022-06-14 17:44:33.720822
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    video_id = '2642630'
    display_id = 'one-direction-all-for-one'
    try:
        assert (ie.suitable(url) == True)
    except:
        print ("Test that function suitable() returns True for argument %s failed" % url)
        return

# Generated at 2022-06-14 17:44:35.813508
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:44:37.125027
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE(None)._real_extract(WallaIE._TEST['url'])

# Generated at 2022-06-14 17:44:38.357632
# Unit test for constructor of class WallaIE
def test_WallaIE():
	"""Test constructor of class WallaIE"""
	WallaIE()

# Generated at 2022-06-14 17:44:43.592993
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # pylint: disable=protected-access
    assert WallaIE(None) # None or 'url' or 'ie_key'
    assert WallaIE(None, 'url')
    assert WallaIE(None, 'ie_key')
    assert WallaIE._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:44:45.072642
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ydl = WallaIE()

# Generated at 2022-06-14 17:44:57.204427
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """Test constructor of WallaIE"""
    test_object = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    expected_result = {
        'id': '2642630',
        'display_id': 'one-direction-all-for-one',
        'ext': 'flv',
        'title': 'וואן דיירקשן: ההיסטריה',
        'description': 'md5:de9e2512a92442574cdb0913c49bc4d8',
        'thumbnail': 're:^https?://.*\.jpg',
        'duration': 3600,
        'skip_download': None
    }
    assert test_object._TEST

# Generated at 2022-06-14 17:44:59.737772
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == WallaIE._VALID_URL
    assert WallaIE()._TEST == WallaIE._TEST
    assert WallaIE()._SUBTITLE_LANGS == WallaIE._SUBTITLE_LANGS

# Generated at 2022-06-14 17:45:02.042383
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')