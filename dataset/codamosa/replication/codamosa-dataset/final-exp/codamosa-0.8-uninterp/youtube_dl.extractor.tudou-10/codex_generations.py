

# Generated at 2022-06-14 17:16:34.249567
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._valid_url(
        'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'TudouAlbum')

# Generated at 2022-06-14 17:16:35.649846
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:16:42.226300
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/xIa0fAO1OQQ.html'
    ie = TudouPlaylistIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]
    assert ie.IE_NAME == 'tudou:playlist'

# Generated at 2022-06-14 17:16:43.755668
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE()._constructor(None, None)

# Generated at 2022-06-14 17:16:54.071396
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import unittest
    test = unittest.TestCase("__init__")

    # test.assertEquals("test", "test", "test_locastie error")

    # def setUp(self):
    print("test_TudouPlaylistIE setup")

    tudouplaylistie = TudouPlaylistIE()

    # def test_valid_url(self):
    print("test_TudouPlaylistIE test_valid_url")
    test.assertTrue("test_valid_url" in tudouplaylistie._VALID_URL)

    # def test_valid_playlist_id(self):
    print("test_TudouPlaylistIE test_valid_playlist_id")

# Generated at 2022-06-14 17:17:01.283897
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:17:02.189506
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE()
    assert isinstance(obj, InfoExtractor)

# Generated at 2022-06-14 17:17:03.233772
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()

# Generated at 2022-06-14 17:17:11.426390
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME=='tudou:album'
    assert ie._VALID_URL==r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS==[{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:17:13.088426
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tp = TudouPlaylistIE("")
    assert tp is not None


# Generated at 2022-06-14 17:17:21.440339
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_test = TudouPlaylistIE.test()
    assert tudou_test['playlist_mincount'] == 209



# Generated at 2022-06-14 17:17:23.831340
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	from tests import test_TudouPlaylistIE
	test_TudouPlaylistIE.test_constructor()


# Generated at 2022-06-14 17:17:27.207733
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    return ie


# Generated at 2022-06-14 17:17:33.461046
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('www.tudou.com', 'albumplay/v5qckFJvNJg.html')
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert len(ie._TESTS) == 1

# Generated at 2022-06-14 17:17:38.875123
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    name = "tudou:album"
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    TudouAlbumIE(name, url)
    #assert True


# Generated at 2022-06-14 17:17:47.210588
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:17:51.348664
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    album_ie = TudouAlbumIE()
    album_ie.extract(album_url)

# Generated at 2022-06-14 17:17:53.897810
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print("Testing constructor of class TudouPlaylistIE")
    ie = TudouPlaylistIE()
    assert ie is not None, "Failed to create instance of TudouPlaylistIE"


# Generated at 2022-06-14 17:17:58.263535
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    __import__('sys').modules['tudou_extractors'] = tudou_extractors
    tudou_extractors.TudouAlbumIE()


# Generated at 2022-06-14 17:18:05.153272
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import unittest;
    class TestTudouAlbumIE(unittest.TestCase):
        def runTest(self):
            self.assertEqual(TudouAlbumIE._VALID_URL, r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
            # self.assertEqual(TudouAlbumIE._TESTS, )
    test_TudouAlbumIE = TestTudouAlbumIE();
    test_TudouAlbumIE.runTest();


# Generated at 2022-06-14 17:18:22.200673
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    cover_url = 'http://www.tudou.com/albumcover/n_crA2c1e8Y.html'
    play_url = 'http://www.tudou.com/albumplay/n_crA2c1e8Y.html'

    for url in [cover_url, play_url]:
        _, ie, _ = TudouAlbumIE._extract_id(url)
        assert ie == TudouAlbumIE.ie_key()

# Generated at 2022-06-14 17:18:23.517435
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	tudou = TudouPlaylistIE()
	assert tudou is not None


# Generated at 2022-06-14 17:18:29.830811
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_TudouPlaylistIE.test_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    test_TudouPlaylistIE.test_info_dict = {'id': 'zzdE77v6Mmo'}
    test_TudouPlaylistIE.test_playlist_mincount = 209

# Generated at 2022-06-14 17:18:33.752159
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_obj = TudouAlbumIE("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    assert test_obj.ie_key() == 'Tudou'
    assert test_obj.ie_name() == 'tudou:album'
    assert test_obj.valid_url() == "http://www.tudou.com/albumplay/v5qckFJvNJg.html"


# Generated at 2022-06-14 17:18:40.040625
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	album_url = 'http://www.tudou.com/albumcover/0K0XoDL5xE4.html'
	try:
		TudouAlbumIE(album_url)
	except:
		assert False, 'Failed to initialize class TudouAlbumIE, when creating object with url: ' + album_url

# Generated at 2022-06-14 17:18:43.447878
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'

if __name__ == '__main__':
    test_TudouPlaylistIE()

# Generated at 2022-06-14 17:18:44.666381
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_obj = TudouAlbumIE()


# Generated at 2022-06-14 17:18:48.515427
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert album.album_id == 'v5qckFJvNJg'
    assert album.url == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    

# Generated at 2022-06-14 17:18:54.311328
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE("http://www.tudou.com/albumcover/v5qckFJvNJg.html")
    assert ie.IE_NAME == "tudou:album"
    assert ie.VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    

# Generated at 2022-06-14 17:18:57.208595
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	test = TudouPlaylistIE()
	test.test_playlist()


# Generated at 2022-06-14 17:19:24.293541
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_instance = TudouPlaylistIE("TudouPlaylistIE")
    if test_instance:
        return True
    else:
        return False


# Generated at 2022-06-14 17:19:28.547167
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    info_extractor = InfoExtractor();
    TudouPlaylistIE_test = info_extractor.infoExtractors[2];
    if(TudouPlaylistIE_test.IE_NAME != 'tudou:playlist'): return 1;
    return;
# Test complete


# Generated at 2022-06-14 17:19:34.175673
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:19:43.152859
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert(ie.IE_NAME == 'tudou:playlist')
    # Regression test for https://github.com/rg3/youtube-dl/issues/5925,
    # IE did not call constructor on child class
    assert(not hasattr(ie, 'IE_NAME'))
    ie = TudouAlbumIE()
    assert(ie.IE_NAME == 'tudou:album')
    # Regression test for https://github.com/rg3/youtube-dl/issues/5925,
    # IE did not call constructor on child class
    assert(not hasattr(ie, 'IE_NAME'))

# Generated at 2022-06-14 17:19:49.773523
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	'''
	Function to test if the constructor of class TudouPlaylistIE initializes correctly.

	Returns:
		False if there is a problem with the initialization.
	'''
	try:
		tudou_playlistIE = TudouPlaylistIE()
	except:
		return False

	return True


# Generated at 2022-06-14 17:19:59.730180
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    instance = TudouPlaylistIE()
    assert_equal(instance.IE_NAME, 'tudou:playlist')
    assert_equal(instance._VALID_URL, r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert_equal(instance._TESTS, [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
            },
        'playlist_mincount': 209,
        }])


# Generated at 2022-06-14 17:20:02.795592
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .tudou import TudouAlbumIE
    assert TudouAlbumIE('http://www.tudou.com/albumcover/v5qckFJvNJg.html') != None


# Generated at 2022-06-14 17:20:08.791216
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url_list = [
        'http://www.tudou.com/listplay/mTsA8cgWZd4/a4Ymzmn-Jqg.html',
        'http://www.tudou.com/listplay/mTsA8cgWZd4/?page=2',
        'http://www.tudou.com/listplay/mTsA8cgWZd4/',
        'http://www.tudou.com/listplay/mTsA8cgWZd4',
    ]
    assert_all = True
    try:
        test_TudouPlaylistIE = TudouPlaylistIE()
    except:
        assert_all = False
    finally:
        assert assert_all


# Generated at 2022-06-14 17:20:17.526637
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    IE_NAME = 'tudou:album'
    _VALID_URL = r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    _TESTS = [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]
    test_Album = TudouAlbumIE()

# Generated at 2022-06-14 17:20:22.903099
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """
    Unit test for constructor of class TudouAlbumIE
    """
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    ie = TudouAlbumIE(url)
    assert ie.url == url
    assert ie.album_id == 'v5qckFJvNJg'
    assert ie.extractor_name == "Tudou"
    assert ie.min_entry_number == 45

# Generated at 2022-06-14 17:21:12.323947
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    d = TudouPlaylistIE()

# Generated at 2022-06-14 17:21:17.890253
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    obj = TudouPlaylistIE()
    assert len(obj._TESTS) == 1
    assert isinstance(obj._TESTS[0]['url'], basestring)
    assert not isinstance(obj._TESTS[0]['info_dict'], basestring)
    assert isinstance(obj._TESTS[0]['playlist_mincount'], int)

# Generated at 2022-06-14 17:21:23.124624
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('tudou:album', 'http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._match_id('http://www.tudou.com/albumplay/v5qckFJvNJg.html') == 'v5qckFJvNJg'


# Generated at 2022-06-14 17:21:27.450140
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	testurl = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
	res = TudouPlaylistIE()._real_extract(testurl)
	assert 'id' in res
	assert res['id'] == 'zzdE77v6Mmo'




# Generated at 2022-06-14 17:21:39.269901
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	
	import unittest
	
	class TestTudouAlbumIE(unittest.TestCase):
		
		def setUp(self):
			self.tudou_album_ie = TudouAlbumIE()
		
		def test_valid_url(self):
			
			url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
			assert self.tudou_album_ie.suitable(url) == True
			
			url = "http://www.tudou.com/albumcover/v5qckFJvNJg.html"
			assert self.tudou_album_ie.suitable(url) == True
			
			url

# Generated at 2022-06-14 17:21:43.343390
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    URL = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(URL)
    assert ie.url == URL

# Generated at 2022-06-14 17:21:51.945794
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:21:55.270038
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbum = TudouAlbumIE()
    assert tudouAlbum.IE_NAME == "tudou:album"
    

# Generated at 2022-06-14 17:21:59.040361
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_input = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    expected_output = ('zzdE77v6Mmo',)
    ie = TudouPlaylistIE(test_input)
    output = ie._match_id(test_input)
    assert output == expected_output



# Generated at 2022-06-14 17:22:00.118012
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE.__name__ == 'TudouAlbumIE'

# Generated at 2022-06-14 17:23:07.860685
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    info_extractor = TudouPlaylistIE()
    info_extractor.report_warning = lambda _: None

# Generated at 2022-06-14 17:23:10.858283
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('TudouAlbumIE')
    assert ie.ie_key() == 'TudouAlbumIE'
    assert ie.ie_key() == 'Tudou:album'

# Generated at 2022-06-14 17:23:14.651934
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()
    return True

# Generated at 2022-06-14 17:23:16.375388
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'

# Generated at 2022-06-14 17:23:22.727828
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = 'v5qckFJvNJg'

# Generated at 2022-06-14 17:23:28.192911
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .common import list_equal
    from .tudou import *
    try:
        if not list_equal(['Tudou'], [TudouAlbumIE(False).suitable('http://www.tudou.com/albumplay/v5qckFJvNJg.html')[0]]):
            return False
    except:
        return False
    return True


# Generated at 2022-06-14 17:23:31.151522
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	tplst = TudouPlaylistIE(None)

# Generated at 2022-06-14 17:23:33.783611
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	test = TudouAlbumIE()
	#Unit test for constructor of class TudouAlbumIE
	assert test == test

test_TudouAlbumIE()

# Generated at 2022-06-14 17:23:35.611419
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert 'tudou:playlist' == TudouPlaylistIE._VALID_URL


# Generated at 2022-06-14 17:23:42.666801
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    if __name__ == '__main__':
        url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
        TudouPlaylistIE()._real_extract(url)
        url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
        TudouAlbumIE()._real_extract(url)

# Generated at 2022-06-14 17:26:13.433325
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # If constructor of class TudouPlaylistIE is OK, then the following line will run with no exception.
    TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:26:23.265561
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    obj = TudouPlaylistIE()

    func_name = '_download_webpage'
    assert hasattr(obj, func_name)
    func = getattr(obj, func_name)

    expected = 'http://www.tudou.com/tvp/plist.action?lcode=%s' % 'zzdE77v6Mmo'
    assert func.__defaults__[1] == expected

    func_name = '_real_extract'
    assert hasattr(obj, func_name)
    func = getattr(obj, func_name)

    r = func(url)
    assert isinstance(r, dict)

# Generated at 2022-06-14 17:26:30.185882
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    api_url = ie._downloader.urlopen(
        'http://www.tudou.com/tvp/alist.action?acode=%s' % 'v5qckFJvNJg')
    try:
        playlist_data = json.load(api_url)
        assert playlist_data is not None
    except ValueError as e:
        raise Exception('Not a valid JSON')
