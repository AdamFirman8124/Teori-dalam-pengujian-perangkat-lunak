

# Generated at 2022-06-14 17:16:32.353103
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouPlaylistIE = TudouPlaylistIE()
    print(str(tudouPlaylistIE))

# Generated at 2022-06-14 17:16:34.787409
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE("http://www.tudou.com/albumplay/v5qckFJvNJg.html");


# Generated at 2022-06-14 17:16:39.293610
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	ie = TudouAlbumIE(TudouAlbumIE.IE_NAME, TudouAlbumIE._VALID_URL, TudouAlbumIE._TESTS[0], 480)
	if ie.ie_key() != 'TudouAlbum' or ie.ie_name() != 'tudou:album':
		return False
	return True

# Generated at 2022-06-14 17:16:45.341084
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    t = TudouPlaylistIE()
    assert t.get_info_extractor_name() == TudouPlaylistIE.IE_NAME
    assert t.get_info_extractor_test_cases() == TudouPlaylistIE._TESTS
    assert t.get_url_regex() == TudouPlaylistIE._VALID_URL
    

# Generated at 2022-06-14 17:16:46.290401
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()

# Generated at 2022-06-14 17:16:46.771371
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    pass

# Generated at 2022-06-14 17:16:54.902688
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Case 1
    URL = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    ie = TudouPlaylistIE(URL)
    assert ie.url == URL
    # Case 2
    URL = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    ie = TudouPlaylistIE(URL, "faked_data.json")
    assert ie.url == URL


# Generated at 2022-06-14 17:16:58.588223
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:17:01.423158
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .tests.test_tudou import TestTudou
    TestTudou('tudou:album')


# Generated at 2022-06-14 17:17:11.608567
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_id = 'zzdE77v6Mmo'
    playlist_url = 'http://www.tudou.com/listplay/'+playlist_id+'.html'
    playlist_data = 'http://www.tudou.com/tvp/plist.action?lcode='+playlist_id

    entries = [{'icode':'Ab1c2d3E4F5g6H7i8', 'kw':'test video'},
               {'icode':'abcdefghijklmnop', 'kw':'test video 2'},
               {'icode':'qrsTUvWxyz123456', 'kw':'test video 3'}]
    playlist_data_json = {'items':entries}

    playlist = TudouPlaylistIE(playlist_url)


# Generated at 2022-06-14 17:17:18.685378
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_TudouPlaylistIE = TudouPlaylistIE()
    assert test_TudouPlaylistIE.ie_key() == 'tudou:playlist'



# Generated at 2022-06-14 17:17:22.077529
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('Tudou', 'http://www.tudou.com/albumcover/v5qckFJvNJg.html')
    assert(ie.name == 'Tudou')
    assert(ie.url == 'http://www.tudou.com/albumcover/v5qckFJvNJg.html')


# Generated at 2022-06-14 17:17:28.664488
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE().IE_NAME == 'tudou:album'
    assert TudouAlbumIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert TudouAlbumIE()._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:17:31.178704
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
        obj=TudouPlaylistIE()
        assert obj.IE_NAME=='tudou:playlist'


# Generated at 2022-06-14 17:17:37.054965
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
	tudouIE = TudouAlbumIE(url)
	print("TudouAlbumIE object:")
	print(tudouIE)


# Generated at 2022-06-14 17:17:46.910349
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:17:57.117524
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert TudouAlbumIE()._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]
    assert TudouAlbumIE()._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:18:07.738677
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TestClass = TudouPlaylistIE()
    assert TestClass.IE_NAME == "tudou:playlist"
    assert TestClass._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert TestClass._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:18:08.897554
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:18:20.120013
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .test_tudou import test_TudouIE
    global TudouPlaylistIE
    url='http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(test_TudouIE(), {}, url)
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    playlist_id = ie._match_id(url)
    assert playlist_id == 'zzdE77v6Mmo'
    # playlist_data = ie._download_json(
    #     'http://www.tudou.com/tvp/plist.action?lcode=%s' % playlist_id, playlist_id)

# Generated at 2022-06-14 17:18:31.845219
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert TudouPlaylistIE._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert TudouPlaylistIE._TESTS[0]['info_dict'] == {'id': 'zzdE77v6Mmo'}
    assert TudouPlaylistIE._TESTS[0]['playlist_mincount'] == 209



# Generated at 2022-06-14 17:18:32.856216
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:18:36.980659
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url_list = [
        "http://www.tudou.com/albumcover/v5qckFJvNJg.html",
        "http://www.tudou.com/albumplay/v5qckFJvNJg.html",
    ]
    extractor = TudouAlbumIE()
    for url in url_list:
        o_extractor = extractor.suitable(url)
        assert o_extractor._match_id(url) == "v5qckFJvNJg"

# Generated at 2022-06-14 17:18:39.710086
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou = TudouAlbumIE()
    expected = tudou._VALID_URL
    obtained = 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert expected == obtained


# Generated at 2022-06-14 17:18:40.802161
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    pass


# Generated at 2022-06-14 17:18:48.127059
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE(None)
    assert tudouAlbumIE.getIEName() == "tudou:album"
    assert tudouAlbumIE.getSiteName() == "TudouAlbumIE"
    assert tudouAlbumIE.getGitHubURL() == "https://github.com/sigma67/plugin.video.youtube"
    assert tudouAlbumIE.getHeadersURL() == "https://github.com/sigma67/plugin.video.youtube/blob/master/youtube_dl/extractor/common.py"


# Generated at 2022-06-14 17:18:52.413429
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = 'v5qckFJvNJg'
    expected_album_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'

    assert album_id == TudouAlbumIE._match_id(expected_album_url)

# Generated at 2022-06-14 17:18:58.543388
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert(TudouPlaylistIE.__name__ == "TudouPlaylistIE")
    assert(TudouPlaylistIE.__doc__ == "Information Extractor for Tudou playlist.")
    assert(TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert(TudouPlaylistIE.IE_NAME == 'tudou:playlist')


# Generated at 2022-06-14 17:18:59.929451
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import TudouPlaylistIE
    assert(isinstance(TudouPlaylistIE, object))


# Generated at 2022-06-14 17:19:01.513115
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:19:20.644068
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test 1: Normal case
    assert isinstance(TudouPlaylistIE, type)
    assert issubclass(TudouPlaylistIE, InfoExtractor)

    # Test 2: Normal case
    assert isinstance(TudouAlbumIE, type)
    assert issubclass(TudouAlbumIE, InfoExtractor)

# Generated at 2022-06-14 17:19:28.382858
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = {
        "url":           "http://www.tudou.com/listplay/zzdE77v6Mmo.html",
        "id":            "zzdE77v6Mmo",
        "playlist_mincount": 209
    }

    tudou_playlist_ie = TudouPlaylistIE()
    tudou_playlist_ie.initialize()
    tudou_playlist_ie.update_initialize()
    tudou_playlist_ie.extract(test["url"])


# Generated at 2022-06-14 17:19:30.646604
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:19:42.373385
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test = TudouAlbumIE()

# Generated at 2022-06-14 17:19:43.055721
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    pass

# Generated at 2022-06-14 17:19:48.629712
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:54.925089
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .common import HEADRequest
    from bs4 import BeautifulSoup
    from pprint import pprint
    import json

    album_id = 'JgBvubXWx8U'    
    opener = HEADRequest()
    raw_data = opener.open('http://www.tudou.com/tvp/alist.action?acode=%s' % album_id)
    raw_data = raw_data.read()
    bs = BeautifulSoup(json.loads(raw_data)['data']['html'])
    entries = bs.find_all('li')
    pprint(entries)



# Generated at 2022-06-14 17:19:56.407747
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert(TudouPlaylistIE())

# Generated at 2022-06-14 17:20:05.735689
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from pattern.web import URL
    from pattern.web import DOM
    from pattern.web import strip_between
    from pattern.web import strip_between
    from pattern.web import strip_tags
    import re

    # fetch and parse HTML
    url = URL("http://www.tudou.com/albumcover/v5qckFJvNJg.html")
    dom = DOM(url.download(cached=True))

# Generated at 2022-06-14 17:20:07.776530
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # 1. Test when playlist has no id.
    test_input = {}
    actual_output = TudouPlaylistIE(test_input, {})
    expected_output = {}
    assert actual_output == expected_output


# Generated at 2022-06-14 17:20:40.526808
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	playlist = TudouPlaylistIE(url="http://www.tudou.com/listplay/zzdE77v6Mmo.html")
	assert playlist.playlist_id == "zzdE77v6Mmo"


# Generated at 2022-06-14 17:20:44.684450
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .test_tudou import TudouAlbumIE as tdAlbum
    test = tdAlbum
    self = tdAlbum(1,2)
    return True

# Generated at 2022-06-14 17:20:50.136792
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    obj = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert obj._VALID_URL == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert obj.playlist_id == 'zzdE77v6Mmo'
    assert obj.url == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'

# Generated at 2022-06-14 17:20:54.206200
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie_TudouAlbumIE = TudouAlbumIE()
    assert(ie_TudouAlbumIE.IE_NAME == 'tudou:album')


# Generated at 2022-06-14 17:21:00.378079
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test a sample playlist
    playlist_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'

    # Create the playlist
    playlist = TudouPlaylistIE()

    # Try to download the playlist
    playlist_info = playlist._real_extract(playlist_url)

    # Check playlist id
    assert playlist_info['id'] == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:21:01.970125
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .tudou import TudouAlbumIE
    TudouAlbumIE('Tudou')

# Generated at 2022-06-14 17:21:13.526510
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    t = TudouPlaylistIE()
    # Test is_match
    url_False = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert not t._is_match(url_False)

    url_True = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert t._is_match(url_True)
    
    # Test _real_extract
    playlist_id = t._match_id(url_True)
    playlist_data = t._download_json(
        'http://www.tudou.com/tvp/plist.action?lcode=%s' % playlist_id, playlist_id)

# Generated at 2022-06-14 17:21:19.558832
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    '''
    Unit test for constructor of class TudouPlaylistIE
    '''
    info_extractor = TudouPlaylistIE()
    assert(info_extractor.IE_NAME == 'tudou:playlist')
    assert(info_extractor._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')

# Generated at 2022-06-14 17:21:23.155744
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	
	print("\n>>Running unit test for TudouAlbumIE ...")
	assert(TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html'))
	print(">>Passed\n")

# Generated at 2022-06-14 17:21:28.388050
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:22:48.012909
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    #Test an valid input
    tudouAlbumIE = TudouAlbumIE(['http://www.tudou.com/albumplay/v5qckFJvNJg.html'])
    assert tudouAlbumIE._test_valid_url('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    #Test an invalid input
    assert not tudouAlbumIE._test_valid_url('http://www.tudou.com')


# Generated at 2022-06-14 17:22:51.484128
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('url', 'album_id')
    assert ie.album_id == 'album_id'
    assert ie.ie_key() == 'Tudou:album'
    assert ie.ie_name == 'tudou:album'


# Generated at 2022-06-14 17:22:56.688436
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert(
        TudouPlaylistIE()._real_extract(
        'http://www.tudou.com/listplay/zzdE77v6Mmo.html')['id'] ==
        'zzdE77v6Mmo')


# Generated at 2022-06-14 17:22:57.572867
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()


# Generated at 2022-06-14 17:23:00.948407
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_ie = TudouPlaylistIE("", "", "")
    assert tudou_playlist_ie.IE_NAME == 'tudou:playlist'


# Generated at 2022-06-14 17:23:04.706024
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    try:
        TudouAlbumIE()
    except TypeError:
        pass
    else:
        return False
    return True



# Generated at 2022-06-14 17:23:10.027823
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	t = TudouAlbumIE()
	assert t._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
	assert t.IE_NAME == 'tudou:album'
	


# Generated at 2022-06-14 17:23:13.008680
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    x = TudouAlbumIE()
    assert x.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:23:14.481300
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	tudouPlaylistIE = TudouPlaylistIE(None, None, None)
	assert tudouPlaylistIE != None

# Generated at 2022-06-14 17:23:16.622234
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    print(TudouPlaylistIE._VALID_URL)
    print(TudouPlaylistIE._match_id(url))

# Generated at 2022-06-14 17:23:58.594580
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE()
    assert test


# Generated at 2022-06-14 17:24:02.425192
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    #print (url)
    tudou_playlist = TudouPlaylistIE()
    tudou_playlist._real_extract(url)
    #print tudou_playlist


# Generated at 2022-06-14 17:24:13.471083
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert tudou_album_ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudou_album_ie._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:24:22.116662
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test = TudouAlbumIE(None)
    assert test._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})' 
    assert test.IE_NAME == 'tudou:album'
    assert test.IE_DESC == '土豆 - 发现最有趣的视频'
    assert test.BR_DESC == 'aie4'  
    assert test.SUFFIX == '_480_200k'
    assert test.API_KEY == 'd7a60c3d2b724ea1a9b976fb91fbad10'
    assert test.APP_KEY == 'mytudou'

# Generated at 2022-06-14 17:24:23.911370
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    player = TudouPlaylistIE()
    return player


# Generated at 2022-06-14 17:24:28.890797
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(InfoExtractor())
    assert ie._match_id(url) == 'zzdE77v6Mmo'

# Generated at 2022-06-14 17:24:33.875719
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist_id = 'zzdE77v6Mmo'
    playlist = TudouPlaylistIE(url)
    assert playlist.playlist_id == playlist_id

test_TudouPlaylistIE()


# Generated at 2022-06-14 17:24:37.165035
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_url = 'www.tudou.com/listplay/zzdE77v6Mmo.html'
    actual_class_IE = TudouPlaylistIE(test_url)
    assert actual_class_IE == "TudouPlaylistIE"


# Generated at 2022-06-14 17:24:48.214978
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	album_id = 'v5qckFJvNJg'
	expect_result = [{
				'url' : 'http://www.tudou.com/programs/view/%s' % item['icode'],
				'_type' : 'Tudou',
				'ie_key' : item['icode'],
				'id' : item['icode'],
				'playlist_index' : index
			} for index,item in enumerate(album_data['items'])]
	assert_equal(expect_result,TudouAlbumIE.test_extract_info(TudouAlbumIE,album_id))

# Generated at 2022-06-14 17:24:53.525679
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Initialize
    tudouPlaylistIE = TudouPlaylistIE()
    # Assert url can be matched
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert(tudouPlaylistIE._match_id(url) == 'zzdE77v6Mmo')
    # Assert url can't be matched
    url = 'http://www.tudou.com/listplay/'
    assert(tudouPlaylistIE._match_id(url) is None)
