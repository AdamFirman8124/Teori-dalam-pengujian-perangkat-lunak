

# Generated at 2022-06-14 17:16:39.752836
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    print("[test_TudouAlbumIE] start testing")
    IE_NAME = 'tudou:album'
    _VALID_URL = 'https://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tudou_albumIE = TudouAlbumIE()
    playlist_id = tudou_albumIE._match_id( _VALID_URL)
    print("[test_TudouAlbumIE] playlist_id=%s" % playlist_id)
    assert(  playlist_id == 'v5qckFJvNJg')
    print("[test_TudouAlbumIE] passed")


# Generated at 2022-06-14 17:16:42.845150
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	t = TudouAlbumIE(tudou.tudou_downloader)
	assert t.IE_NAME == 'tudou:album'


# Generated at 2022-06-14 17:16:43.222096
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	assert True

# Generated at 2022-06-14 17:16:47.037330
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test normal case
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    ie = TudouAlbumIE()
    assert ie._match_id(url) == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:16:51.243891
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:16:55.147582
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert TudouAlbumIE._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg'
    assert TudouAlbumIE._TESTS[0]['playlist_mincount'] == 45


# Generated at 2022-06-14 17:16:56.721654
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE(None)
    assert ie.IE_NAME == 'Tudou:album'

# Generated at 2022-06-14 17:16:57.588215
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    a = TudouAlbumIE()

# Generated at 2022-06-14 17:17:02.801556
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import re
    import time
    import json
    import urllib
    from multiprocessing import Process
    from .common import InfoExtractor
    from .tudou import TudouAlbumIE

    assert re.match(TudouAlbumIE._VALID_URL, 'http://www.tudou.com/albumcover/ihSHgS2QJP0.html')
    url = 'http://www.tudou.com/albumplay/ihSHgS2QJP0.html'
    ie = InfoExtractor()
    return ie._real_extract(url)


# Generated at 2022-06-14 17:17:06.746136
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
#     url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist = TudouPlaylistIE()

# Generated at 2022-06-14 17:17:11.506496
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_object = TudouAlbumIE()
    assert album_object


# Generated at 2022-06-14 17:17:14.059682
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_obj = TudouPlaylistIE()
    assert test_obj.__class__.__name__ == "TudouPlaylistIE"


# Generated at 2022-06-14 17:17:15.162197
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()


# Generated at 2022-06-14 17:17:25.733296
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import urlparse, urlunparse
    test_cases = (
        'http://www.tudou.com/albumcover/v5qckFJvNJg.html',
        'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'http://www.tudou.com/albumcover/v5qckFJvNJg',
        'http://www.tudou.com/albumplay/v5qckFJvNJg',
    )
    for test_case in test_cases:
        url = urlunparse(urlparse.urlparse(test_case))
        assert url == TudouAlbumIE._VALID_URL


# Generated at 2022-06-14 17:17:28.418980
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:17:29.684729
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    a = TudouPlaylistIE()

# Generated at 2022-06-14 17:17:31.612794
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == "tudou:album"

# Generated at 2022-06-14 17:17:42.491678
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE.IE_NAME == 'tudou:album'
    assert TudouAlbumIE._VALID_URL == \
        'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    for test in TudouAlbumIE._TESTS:
        assert test['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
        assert test['info_dict']['id'] == 'v5qckFJvNJg'
        assert test['playlist_mincount'] == 45

# Generated at 2022-06-14 17:17:45.193775
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    return TudouAlbumIE()

# Generated at 2022-06-14 17:17:54.660680
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    IE = TudouPlaylistIE(TudouPlaylistIE.ie_key(), 'http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert IE._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert IE.IE_NAME == 'tudou:playlist'
    assert IE._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert IE._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:18:05.959424
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    try:
        TudouPlaylistIE._real_extract(TudouPlaylistIE(), url)
        assert True
    except:
        assert False


# Generated at 2022-06-14 17:18:09.890533
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url_playlist = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist_IE = TudouPlaylistIE()
    assert playlist_IE._real_extract(url_playlist) is not None


# Generated at 2022-06-14 17:18:15.429858
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    args = err_msg = None

# Generated at 2022-06-14 17:18:18.313697
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:18:20.924031
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
	TudouPlaylistIE(url)


# Generated at 2022-06-14 17:18:29.119769
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    list = ['http://www.tudou.com/listplay/zzdE77v6Mmo.html']
    tudouplaylist = TudouPlaylistIE()
    for url in list:
        tudouplaylist.match(url)

# Generated at 2022-06-14 17:18:37.363488
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playList = TudouPlaylistIE();
    assert playList.IE_NAME == 'tudou:playlist';
    assert playList._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html';
    assert playList._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }];

# Generated at 2022-06-14 17:18:47.785972
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_id = 'zzdE77v6Mmo'
    playlist_data = '{'\
                    '"items": ['\
                    '{"title": "test playlist 1", "icode": "test icode 1", "kw": "test kw 1"},'\
                    '{"title": "test playlist 2", "icode": "test icode 2", "kw": "test kw 2"}'\
                    ']'\
                    '}'
    entry_list = [('http://www.tudou.com/programs/view/test icode 1', 'Tudou', 'test icode 1', 'test kw 1'),
                  ('http://www.tudou.com/programs/view/test icode 2', 'Tudou', 'test icode 2', 'test kw 2')]
    playlist_mincount

# Generated at 2022-06-14 17:18:50.052541
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print("Enter test_TudouPlaylistIE")
    # test = TudouPlaylistIE.TudouPlaylistIE()
    # assert test

# Generated at 2022-06-14 17:18:51.517504
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE().IE_NAME == 'tudou:playlist'

# Generated at 2022-06-14 17:19:10.876454
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test with valid url
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert TudouAlbumIE._VALID_URL.match(url) != None
    test_obj = TudouAlbumIE(url)
    assert test_obj.IE_NAME == 'tudou:album'

    # Test with invalid url
    invalid_url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    assert TudouAlbumIE._VALID_URL.match(invalid_url) == None
    try:
        test_obj = TudouAlbumIE(invalid_url)
    except Exception as e:
        assert e.args[0] == 'Invalid URL: %s' % invalid_url

# Generated at 2022-06-14 17:19:12.784021
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	TudouAlbumIE()

# Generated at 2022-06-14 17:19:13.743076
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()

# Generated at 2022-06-14 17:19:14.321819
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	pass

# Generated at 2022-06-14 17:19:18.604601
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    output = ie.ie_key()
    expected = 'TudouAlbum'
    assert output == expected
    output = ie._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert len(output['entries']) == 45


# Generated at 2022-06-14 17:19:27.286517
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .TudouAlbumIE import TudouAlbumIE
    tudouAlbumIE = TudouAlbumIE("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    assert tudouAlbumIE.ie_key() == 'TudouAlbum'
    assert tudouAlbumIE.ie_name() == 'Tudou'
    assert tudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:31.961263
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()

    assert tudou_album_ie.IE_NAME == 'tudou:album'

    assert tudou_album_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

    assert isinstance(tudou_album_ie._TESTS, list)



# Generated at 2022-06-14 17:19:35.954837
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:45.846432
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	album_id = 'abc123'
	assert(TudouAlbumIE._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
	assert(album_id.__class__ is str)
	assert(TudouAlbumIE._VALID_URL.__class__ is str)
	assert(TudouAlbumIE.IE_NAME == 'tudou:album')
	assert(TudouAlbumIE.IE_NAME.__class__ is str)
	assert(TudouAlbumIE._TESTS.__class__ is list)
	assert(TudouAlbumIE._TESTS[0]['url'].__class__ is str)

# Generated at 2022-06-14 17:19:49.339332
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	from .common import InfoExtractor
	extractor = InfoExtractor()
	assert(extractor._get_info_extractor(TudouPlaylistIE.IE_NAME) == TudouPlaylistIE)

# Generated at 2022-06-14 17:20:23.841902
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    _TESTS = [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]
    assert ie.VALID_URL == _VALID_URL
    assert ie.TESTS == _TESTS

# Generated at 2022-06-14 17:20:27.637689
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(url)
    ie.test()


# Generated at 2022-06-14 17:20:31.416935
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():

    # Create a class for testing
    class TestTudouPlaylistIE(TudouPlaylistIE):
        pass

    t = TestTudouPlaylistIE()
    assert t.get_metadata('zzdE77v6Mmo') == {}

# Generated at 2022-06-14 17:20:40.349288
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tpIE = TudouPlaylistIE()
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    info_dict = {'id': 'zzdE77v6Mmo'}
    # Get the match_id for the given URL
    playlist_id = tpIE._match_id(url)
    playlist_info = tpIE._download_json(
        'http://www.tudou.com/tvp/plist.action?lcode=%s' % playlist_id, playlist_id)

# Generated at 2022-06-14 17:20:44.415023
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    TudouAlbumIE(url)


# Generated at 2022-06-14 17:20:50.591902
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album = TudouAlbumIE()
    assert tudou_album.name == 'tudou:album'
    assert tudou_album.IE_NAME == 'tudou:album'
    assert tudou_album._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudou_album._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert tudou_album._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:20:55.668508
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test with TudouAlbumIE.__init__
    loader = unittest.TestLoader()
    test_suite = loader.loadTestsFromTestCase(TudouAlbumIE)
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

# Generated at 2022-06-14 17:20:59.353908
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE('zzdE77v6Mmo')
    assert test.name() == 'Tudou: Playlist'
    assert test.match('zzdE77v6Mmo') is True


# Generated at 2022-06-14 17:21:06.552593
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import unittest
    from .common import TestCase
    try:
        from .test_tudou import generate_random_string
    except ImportError:
        from test_tudou import generate_random_string

    t = TestCase(TudouAlbumIE)
    t.test_entries_count(TudouAlbumIE, 'v5qckFJvNJg', 45)
    # Test the constructor of class TudouAlbumIE
    try:
        from .test_tudou import TestTudouIE
    except ImportError:
        from test_tudou import TestTudouIE
    t = TestTudouIE()
    t.test_album_entries_count(TudouAlbumIE, 'v5qckFJvNJg', 45)

# Generated at 2022-06-14 17:21:08.421695
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE()
    assert obj != None


# Generated at 2022-06-14 17:22:20.406187
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_TudouPlaylistIE = TudouPlaylistIE(InfoExtractor)
    test_TudouPlaylistIE._downloader = InfoExtractor._downloader
    test_TudouPlaylistIE._download_webpage = InfoExtractor._download_webpage
    test_TudouPlaylistIE._search_regex = InfoExtractor._search_regex
    test_TudouPlaylistIE._download_json = InfoExtractor._download_json
    test_TudouPlaylistIE._real_extract = InfoExtractor._real_extract

# Generated at 2022-06-14 17:22:28.299313
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Initial test playlist_id for Tudou.
    playlist_id = 'zzdE77v6Mmo'

    # Initial video_id for Tudou.
    video_id = 'XMTMzNzY5NDMwMA=='

    # Initial title for Tudou.
    title = '【放学后】梦见死去的人活了'

    # Generate test url.
    test_url = 'http://www.tudou.com/listplay/%s.html' % playlist_id

    # Initial test instance of TudouPlaylistIE.
    test = TudouPlaylistIE(test_url)

    # Generate expected playlist_id.
    expected_playlist_id = test._match_id(test_url)

    # Generate expected

# Generated at 2022-06-14 17:22:38.249388
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	test_obj = TudouPlaylistIE(InfoExtractor())
	assert test_obj.IE_NAME == 'tudou:playlist'
	assert test_obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
	test_test = [{
		'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
		'info_dict': {
			'id': 'zzdE77v6Mmo',
		},
		'playlist_mincount': 209,
	}]
	test_obj._TESTS = test_test


# Generated at 2022-06-14 17:22:40.996367
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE.__name__ == 'TudouAlbumIE'

# Test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:22:49.807349
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	
	playlist_ie = TudouPlaylistIE()
	playlist_ie.add_default_info_extractors()
	assert playlist_ie.IE_NAME == 'tudou:playlist'
	assert playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
	assert playlist_ie._TESTS[0] == {
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }


# Generated at 2022-06-14 17:22:51.022659
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE == TudouPlaylistIE


# Generated at 2022-06-14 17:22:56.568478
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .test import get_testcases

    test_cases = get_testcases(TudouAlbumIE.IE_NAME)

    for test in test_cases:
        if test.get('test_constructor', False):
            yield check_test_cases, vars(TudouAlbumIE), test


# Generated at 2022-06-14 17:23:00.999404
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    playlist = TudouAlbumIE().extract(url)
    assert playlist['entries'][0]['id'] == 'XMTIxNjkyNTI0OA==', "Test case passed"

# Generated at 2022-06-14 17:23:07.250238
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        from .tudou_playlist_ie import TudouPlaylistIE
        from .tudou_album_ie import TudouAlbumIE
    except ImportError:
        print("Error: module tudou_playlist_ie.py or tudou_album_ie.py not found.")
        exit(1)
    instance = TudouPlaylistIE()
    assert(instance != None)
    assert(isinstance(instance, InfoExtractor))
    instance = TudouAlbumIE()
    assert(instance != None)
    assert(isinstance(instance, InfoExtractor))
    print("Success: the class TudouPlaylistIE init correct.")


# Generated at 2022-06-14 17:23:13.442438
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    Playlist = TudouPlaylistIE("https://www.tudou.com/listplay/zzdE77v6Mmo.html")
    assert(Playlist.playlist_id == "zzdE77v6Mmo")
    assert(Playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert(Playlist.IE_NAME == 'tudou:playlist')


# Generated at 2022-06-14 17:25:45.855690
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(url)
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._TESTS[0]['url'] == url


# Generated at 2022-06-14 17:25:55.141370
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import unittest
    import logging
    import traceback
    logging.basicConfig(level=logging.INFO)

    class Test(unittest.TestCase):
        url="http://www.tudou.com/albumplay/v5qckFJvNJg.html"
        playlist = None

        def setUp(self):
            self.playlist = TudouAlbumIE(logger=logging.getLogger("Test"))

        def tearDown(self):
            self.playlist = None

        def test_extract_url(self):
            try:
                self.playlist.extract_url(self.url)
            except:
                logging.error(traceback.format_exc())
                self.assertTrue(False)


# Generated at 2022-06-14 17:25:57.615990
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import tudou_playlist
    tudou_playlist.TudouPlaylistIE.suite()
    pass

# Generated at 2022-06-14 17:26:03.758958
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist = TudouPlaylistIE()
    assert playlist.IE_NAME == 'tudou:playlist'
    assert playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert playlist._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]

# Generated at 2022-06-14 17:26:06.377519
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE();
    obj.url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    obj.params = {}
    obj.context = {}
    obj.extract()
    return obj

# Generated at 2022-06-14 17:26:16.352121
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    PLI=TudouPlaylistIE()
    assert PLI.IE_NAME == 'tudou:playlist'
    assert PLI._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert PLI._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]



# Generated at 2022-06-14 17:26:17.299518
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE(None)

# Generated at 2022-06-14 17:26:18.428870
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE();


# Generated at 2022-06-14 17:26:23.741991
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tudou = TudouAlbumIE(url)
    assert tudou._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudou._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:26:32.827520
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print('\nUnit test for TudouPlaylistIE:\n')

    tudou_playlist_IE = TudouPlaylistIE()
    good_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    bad_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo'
    assert tudou_playlist_IE.check_valid_url(good_url),'Good URL is validated by function \'check_valid_url\' !'
    print('Good URL is validated by function \'check_valid_url\' !')
    assert not tudou_playlist_IE.check_valid_url(bad_url), 'Bad URL is not validated by function \'check_valid_url\'!'