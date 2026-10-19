

# Generated at 2022-06-14 17:16:27.894465
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:16:31.058953
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	assert(1 == 1)

# Generated at 2022-06-14 17:16:41.062070
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	ie = TudouPlaylistIE("http://www.tudou.com/listplay/zzdE77v6Mmo.html") # test url
	# assert url
	assert ie._VALID_URL == "https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html" # _VALID_URL
	assert ie._TESTS[0]['url'] == "http://www.tudou.com/listplay/zzdE77v6Mmo.html" # _TESTS
	
	# assert _match_id
	assert ie._match_id("http://www.tudou.com/listplay/zzdE77v6Mmo.html") == "zzdE77v6Mmo" # return playlist_id
	assert ie

# Generated at 2022-06-14 17:16:47.129980
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    obj = TudouPlaylistIE(url)
    assert obj.IE_NAME == "tudou:playlist"
    assert obj._VALID_URL == "https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html"
    assert obj._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]
    # test method _real_extract
    # obj._real

# Generated at 2022-06-14 17:16:52.500614
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():

	try:
		#constructor of class TudouPlaylistIE(class InfoExtractor,object)
		TudouPlaylistIE(InfoExtractor)
	except:
		print("Constructor Exception")


# Generated at 2022-06-14 17:16:55.915843
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album = "http://www.tudou.com/albumcover/w1G_sU6-3qE.html"
    album_id = "w1G_sU6-3qE"
    result = True
    try:
        album_ins = TudouAlbumIE(album)
    except:
        result = False
    
    assert result == True

# Generated at 2022-06-14 17:16:56.921613
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE._VALID_URL

# Generated at 2022-06-14 17:17:03.870483
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert TudouPlaylistIE._VALID_URL  == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

# Functional test for constructor

# Generated at 2022-06-14 17:17:08.408667
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import unittest
    import sys
    from  ykdl.extractors import tudou

    class TestTudouAlbumIE(unittest.TestCase):
        def setUp(self):
            sys.argv = ['ykdl', '-o', '../output/1.mp4', 'http://www.tudou.com/albumplay/v5qckFJvNJg.html']

        def test_TudouAlbumIE(self):
            tudou.TudouAlbumIE()

    t = TestTudouAlbumIE()
    t.setUp()
    t.test_TudouAlbumIE()

# Generated at 2022-06-14 17:17:16.716430
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	playlist_id = u'zzdE77v6Mmo'
	plist_url = u'http://www.tudou.com/listplay/%s.html' % playlist_id
	plist_obj = TudouPlaylistIE(plist_url)

	assert plist_obj.IE_NAME == 'tudou:playlist'
	assert plist_obj._VALID_URL == r'^https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html$'

# Generated at 2022-06-14 17:17:25.582841
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """
    Unit test for constructor of class TudouAlbumIE
    """
    try:
        tudou_album_ie = TudouAlbumIE()
        assert(tudou_album_ie.name == 'tudou:album')
        assert(tudou_album_ie.ie_key() == 'TudouAlbum')
    except:
        print("Error occurred when testing constructor of class TudouAlbumIE")


# Generated at 2022-06-14 17:17:31.073249
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """Unit test for the class TudouPlaylistIE"""
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist_id = 'zzdE77v6Mmo'
    assert(playlist_id == TudouPlaylistIE.create_playlist_id(url))


# Generated at 2022-06-14 17:17:33.282578
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE == InfoExtractor._make_test_class_named('TudouAlbumIE')(TudouAlbumIE)

# Generated at 2022-06-14 17:17:45.484602
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # type: () -> None
    IE_NAME = 'tudou:album'
    VALID_URL = r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    TESTS = [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:17:55.364381
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
    # Testing the constructor of the class
    ie = TudouAlbumIE()
    # Testing class variables of the class

# Generated at 2022-06-14 17:18:02.213238
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_ie = TudouPlaylistIE()
    assert tudou_playlist_ie is not None
    assert tudou_playlist_ie.IE_NAME == 'tudou:playlist'
    assert tudou_playlist_ie._VALID_URL == TudouPlaylistIE._VALID_URL
    assert tudou_playlist_ie._TESTS == TudouPlaylistIE._TESTS


# Generated at 2022-06-14 17:18:06.673132
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouplaylist = TudouPlaylistIE()
    tudouplaylist.initialize()
    assert tudouplaylist.IE_NAME == 'tudou:playlist'


# Generated at 2022-06-14 17:18:08.949504
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_ie = TudouAlbumIE()

# Generated at 2022-06-14 17:18:15.824390
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    list_play_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == "tudou:playlist"
    assert ie.test_url(list_play_url) == True
    assert ie.IE_URL_ID(list_play_url) == "zzdE77v6Mmo"


# Generated at 2022-06-14 17:18:23.226979
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	tudouPI = TudouPlaylistIE()
	assert tudouPI._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
	assert tudouPI.IE_NAME == 'tudou:playlist'
	assert tudouPI._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
	assert tudouPI._TESTS[0]['info_dict'] == {'id': 'zzdE77v6Mmo'}

# Generated at 2022-06-14 17:18:38.568591
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # this is a case that the url of album is
    # http://www.tudou.com/albumcover/v5qckFJvNJg.html
    tudou_album = TudouAlbumIE()
    assert tudou_album._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    assert tudou_album._match_id(url) == 'v5qckFJvNJg'
    # the album's name is 从新开始：2013年中国重要纪录片

# Generated at 2022-06-14 17:18:39.664851
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE

# Generated at 2022-06-14 17:18:42.153047
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:18:50.121431
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	tudou_album = TudouAlbumIE()
	expect_result = (
		r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})',
		'TudouAlbumIE',
		'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
		45
	)

# Generated at 2022-06-14 17:18:56.396575
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import pytest
    IE = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    # For example, IE._VALID_URL.match(...) should be not None
    with pytest.raises(TypeError):
        IE._VALID_URL.match('http://www.tudou.com/albumplay/v5qckFJvNJg.html')


# Generated at 2022-06-14 17:18:58.423511
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:19:04.407007
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t = TudouAlbumIE()
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    pattern = re.compile(TudouAlbumIE._VALID_URL)
    m = re.match(pattern, url)
    assert m
    album_id = m.group('id')
    assert album_id
    # Pass album_id to constructor
    t = TudouAlbumIE(album_id)
    assert t._match_id(url) == album_id
    # Pass invalid album_id to constructor
    assert TudouAlbumIE('invalid album id') == None

# Generated at 2022-06-14 17:19:09.395013
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import unittest
    import sys
    import os
    module_dir = os.path.dirname(sys.modules[__name__].__file__)
    album_test = __import__(module_dir + '.TudouAlbumIE')
    album = album_test.TUDOU_ALBUM
    unittest.main()



# Generated at 2022-06-14 17:19:12.925599
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:19:14.263022
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    try:
        TudouAlbumIE()
    except Exception as e:
        pass

# Generated at 2022-06-14 17:19:33.321347
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:19:35.592743
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert(TudouPlaylistIE()._VALID_URL == TudouPlaylistIE._VALID_URL)

# Generated at 2022-06-14 17:19:36.569635
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()
    assert True

# Generated at 2022-06-14 17:19:42.809931
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    #assert ie.get_identifier('http://www.tudou.com/albumplay/v5qckFJvNJg.html') == 'v5qckFJvNJg'
    assert ie.get_identifier('http://www.tudou.com/albumcover/v5qckFJvNJg.html') == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:19:46.531483
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    x = TudouAlbumIE()
    assert x.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:19:48.629476
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie

# Generated at 2022-06-14 17:19:50.433594
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        TudouPlaylistIE('test')
    except Exception as err:
        print (err)

# Generated at 2022-06-14 17:19:52.329872
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        TudouPlaylistIE()
    except:
        assert False, "Constructor of class TudouPlaylistIE failed"

# Generated at 2022-06-14 17:19:56.769004
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test for TudouPlaylistIE
    from .tudou import TudouPlaylistIE
    
    ie = TudouPlaylistIE()
    assert ie

# Generated at 2022-06-14 17:19:59.033096
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:20:34.947391
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    given_el = 'http://www.tudou.com/listplay/1tJ96l8.html'
    ie = TudouPlaylistIE(given_el, {})
    assert ie is not None


# Generated at 2022-06-14 17:20:36.641527
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE({})
    assert obj.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:20:40.871382
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    expected_id = "zzdE77v6Mmo"
    url = TudouPlaylistIE._real_extract(TudouPlaylistIE, test_url)
    assert url.find(expected_id) != -1

# Generated at 2022-06-14 17:20:47.024930
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album = TudouAlbumIE()
    assert tudou_album.IE_NAME == 'tudou:album'
    assert tudou_album._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:20:50.285812
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    info = TudouPlaylistIE._extract_info(url)
    assert info == {
        'id': 'zzdE77v6Mmo',
    }, info


# Generated at 2022-06-14 17:20:52.351355
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	obj = TudouAlbumIE("")

# Generated at 2022-06-14 17:21:01.038641
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:21:02.806884
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:21:11.440232
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>)(\w-]{11}).html'
    assert TudouPlaylistIE._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:21:20.328802
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    y = {'a':[1,6.5,10]}
    x = TudouAlbumIE()
    assert x._match_id("www.tudou.com/albumcover/eghol9CKxDQ") == 'eghol9CKxDQ'
    assert x._real_extract("www.tudou.com/albumcover/eghol9CKxDQ") == {'_type': 'playlist', 'id': 'eghol9CKxDQ', 'entries': [{'id': 'eghol9CKxDQ', 'ie_key': 'Tudou', 'title': '电影大海怪'}]}


# Generated at 2022-06-14 17:22:35.658992
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE()
    assert tudou_playlist.suitable('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert not tudou_playlist.suitable('http://www.zhihu.com/playlist')
    assert tudou_playlist.IE_NAME == 'tudou:playlist'


# Generated at 2022-06-14 17:22:45.956272
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert TudouAlbumIE._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]


# Generated at 2022-06-14 17:22:57.863767
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .tudou import tudou_url_result
    from .common import InfoExtractor
    from .tudou import TudouAlbumIE
    import re
    import unittest

    testURI = "http://www.tudou.com/albumcover/v5qckFJvNJg.html"
    assert (re.search(TudouAlbumIE._VALID_URL, testURI))
    tudou_urltest = tudou_url_result(
        'http://www.tudou.com/programs/view/%s' % "v5qckFJvNJg",
        'Tudou',
        "v5qckFJvNJg",
        "v5qckFJvNJg")

# Generated at 2022-06-14 17:23:06.527769
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist_id = ie._match_id(url)
    playlist_data = ie._download_json(
        'http://www.tudou.com/tvp/plist.action?lcode=%s' % playlist_id, playlist_id)
    entries = [ie.url_result(
        'http://www.tudou.com/programs/view/%s' % item['icode'],
        'Tudou', item['icode'],
        item['kw']) for item in playlist_data['items']]
    playlist = ie.playlist_result(entries, playlist_id)
    playlist_request = playlist['_type']


# Generated at 2022-06-14 17:23:07.677741
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:23:15.540338
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from xml.dom.minidom import parseString
    from .common import compat_urllib_request
    from .common import compat_urlparse
    from .common import compat_urllib_parse
    import sys

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'
    }

    request_url = 'http://www.tudou.com/tvp/alist.action?acode=NnKzFtNXlEo'
    request = compat_urllib_request.Request(request_url, headers=header)
    response = compat_urllib_request.urlopen(request)


# Generated at 2022-06-14 17:23:21.120037
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'

# Generated at 2022-06-14 17:23:27.813209
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    with open('test_TudouAlbumIE.txt', 'r') as f:
        html = f.read()
        f.close()
    url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    obj = TudouAlbumIE(0)
    obj._match_id(url)
    obj._real_extract(url)


# Generated at 2022-06-14 17:23:36.093279
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_albumIE = TudouAlbumIE()
    assert tudou_albumIE._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert tudou_albumIE._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg'
    assert tudou_albumIE._TESTS[0]['playlist_mincount'] == 45


# Generated at 2022-06-14 17:23:47.327907
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # check the type of the object is right.
    albums = TudouAlbumIE()
    assert type(albums) == TudouAlbumIE
    # check the attributes of the object are right
    assert albums._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert albums._TESTS == [{
            'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
            'info_dict': {
                    'id': 'v5qckFJvNJg',
            },
            'playlist_mincount': 45,
    }]
    assert albums._downloader == None

# Generated at 2022-06-14 17:26:22.851686
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html', {})
    TudouAlbumIE('http://www.tudou.com/albumcover/v5qckFJvNJg', {})