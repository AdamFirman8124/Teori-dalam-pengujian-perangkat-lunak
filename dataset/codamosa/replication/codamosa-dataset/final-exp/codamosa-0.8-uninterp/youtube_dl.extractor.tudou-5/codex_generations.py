

# Generated at 2022-06-14 17:16:40.337193
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.name == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    # Test first test case
    tes = ie._TESTS[0]
    assert tes['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert tes['info_dict'] == {'id': 'v5qckFJvNJg'}
    assert tes['playlist_mincount'] == 45
#print "TEST ALBUM PASSED"


# Generated at 2022-06-14 17:16:47.011299
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    playlist = ie.extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:16:52.077278
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        TudouPlaylistIE()
        print('TudouPlaylistIE() Test Passed.')
    except Exception:
        print('TudouPlaylistIE() Test Failed.')


# Generated at 2022-06-14 17:16:55.206497
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert TudouAlbumIE._TEST_URL_RE.match(url)

# Generated at 2022-06-14 17:17:02.509655
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import sys
    from urllib2 import URLError

    a_albumIE = TudouAlbumIE()
    album_id = 'v5qckFJvNJg'
    a_album_data = a_albumIE._download_json(
        'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)
    album_count = len(a_album_data['items'])

# Generated at 2022-06-14 17:17:06.836053
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    album = TudouAlbumIE(url)
    print(album.album_name)
    print(album.album_id)

# Generated at 2022-06-14 17:17:09.583902
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    try:
        x = TudouAlbumIE()
    except:
        assert False
    assert True

# Generated at 2022-06-14 17:17:15.079860
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    info_extractor = TudouAlbumIE()
    test_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    test_expected_result = 'v5qckFJvNJg'
    test_result = info_extractor._match_id(test_url)
    assert test_result == test_expected_result


# Generated at 2022-06-14 17:17:26.262396
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """
    For testing the constructor of this class
    """
    video = TudouAlbumIE('test')
    video.extract('http://www.tudou.com/albumcover/v5qckFJvNJg.html')
    video.extract('http://www.tudou.com/albumcover/v5qckFJvNJg')
    video.extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    video.extract('http://www.tudou.com/albumplay/v5qckFJvNJg')
    video.extract('http://www.tudou.com/albumplay/v5qckFJvNJg/')

# Generated at 2022-06-14 17:17:35.998169
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    testPre = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    testObj = TudouPlaylistIE()

    print(testObj.IE_NAME)
    assert testObj.IE_NAME == 'tudou:playlist'

    print(testObj._VALID_URL)
    assert testObj._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

    # Testing function _real_extract
    print(testObj._real_extract(testPre))
    assert testObj._real_extract(testPre) == {'id': 'zzdE77v6Mmo'}


# Generated at 2022-06-14 17:17:42.888353
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t = TudouAlbumIE()

# Generated at 2022-06-14 17:17:50.193463
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = 'g5qckFJvNJg'

# Generated at 2022-06-14 17:18:00.025679
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	playlist_id = 'zzdE77v6Mmo'

# Generated at 2022-06-14 17:18:04.793545
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
  str1="http://www.tudou.com/listplay/zzdE77v6Mmo.html"
  tpi=TudouPlaylistIE()
  tpi._real_extract(str1)


# Generated at 2022-06-14 17:18:11.205541
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    expected_result = {
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'id': 'zzdE77v6Mmo',
}
    ie = TudouPlaylistIE(url)
    actual_result = ie.ie_key()
    assert expected_result == actual_result


# Generated at 2022-06-14 17:18:15.141773
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE()

    tudou_playlist_test_input = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert tudou_playlist.suitable(tudou_playlist_test_input) == True


# Generated at 2022-06-14 17:18:16.054476
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    pass

# Generated at 2022-06-14 17:18:20.637687
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    urlList=["http://www.tudou.com/listplay/zzdE77v6Mmo.html"]
    for url in urlList:
        info = TudouPlaylistIE()._real_extract(url)
        print(info)

if __name__ == '__main__':
    test_TudouPlaylistIE()

# Generated at 2022-06-14 17:18:24.904924
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert ie.url == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert ie.ie_key == 'tudou:playlist'
    assert ie.match_id == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:18:26.544597
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    try:
        assert(ie.IE_NAME) == 'tudou:playlist'
    except Exception:
        print('Error:')
        raise



# Generated at 2022-06-14 17:18:39.449985
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:18:48.847801
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    album_id = 'v5qckFJvNJg'
    album_data = tudou_album_ie._download_json(
            'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)
    entries = [tudou_album_ie.url_result(
            'http://www.tudou.com/programs/view/%s' % item['icode'],
            'Tudou', item['icode'],
            item['kw']) for item in album_data['items']]

    assert tudou_album_

# Generated at 2022-06-14 17:18:49.867864
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()



# Generated at 2022-06-14 17:18:55.806858
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = 'v5qckFJvNJg'
    album_test_url = 'http://www.tudou.com/albumplay/%s.html' % album_id
    albumIE = TudouAlbumIE()
    playlist_info = albumIE._real_extract(album_test_url)
    assert playlist_info['id'] == album_id
    assert len(playlist_info['entries']) == 45

# Generated at 2022-06-14 17:18:59.821891
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_TudouPlaylistIE = TudouPlaylistIE()
    assert test_TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:19:02.685590
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE(None)
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie.IE_NAME == 'tudou:playlist'


# Generated at 2022-06-14 17:19:07.502699
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE(0, 'http://www.tudou.com/albumplay/v5qckFJvNJg.html', 0)
    assert_true(isinstance(ie, TudouAlbumIE))


# Generated at 2022-06-14 17:19:08.517709
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert True


# Generated at 2022-06-14 17:19:19.548719
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE()
    assert(tudou_playlist.IE_NAME == "tudou:playlist")
    assert(tudou_playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert(tudou_playlist._TESTS[0]['url'] == "http://www.tudou.com/listplay/zzdE77v6Mmo.html")
    assert(tudou_playlist._TESTS[0]['info_dict']['id'] == "zzdE77v6Mmo")
    assert(tudou_playlist._TESTS[0]['playlist_mincount'] == 209)


# Generated at 2022-06-14 17:19:23.514418
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:38.409192
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE(None).ie_key() == 'Tudou:album'


# Generated at 2022-06-14 17:19:50.111139
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert not TudouAlbumIE().suitable("")
    assert not TudouAlbumIE().suitable("it's not an url.com")
    assert not TudouAlbumIE().suitable("https://itsthewrongformat.com")
    assert not TudouAlbumIE().suitable("https://www.tudou.com/albumplay/z1sTcS8BjJk\
.html")
    # Returns an error for this.
    #assert TudouAlbumIE().suitable("https://www.tudou.com/albumcover/z1sTcS8BjJk\
#.html")
    assert TudouAlbumIE().suitable("https://www.tudou.com/albumplay/z1sTcS8BjJk.html\
")

# Generated at 2022-06-14 17:19:51.210359
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_TudouAlbumIE = TudouAlbumIE()

# Generated at 2022-06-14 17:20:02.278298
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('https://www.tudou.com/albumcover/v5qckFJvNJg.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:20:11.713735
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():

    if __name__ == '__main__':

        tudou_playlist_ie = TudouPlaylistIE()
        print (tudou_playlist_ie.__name__)
        assert TudouPlaylistIE.__name__ is tudou_playlist_ie.__name__


        print (tudou_playlist_ie.ie_name)
        assert TudouPlaylistIE.IE_NAME is tudou_playlist_ie.ie_name

        print (tudou_playlist_ie._VALID_URL)
        assert TudouPlaylistIE._VALID_URL is tudou_playlist_ie._VALID_URL

        print (tudou_playlist_ie._TESTS)
        assert TudouPlaylistIE._TESTS is tudou_playlist_ie._TES

# Generated at 2022-06-14 17:20:15.327163
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE()
    assert obj._VALID_URL
    assert obj._TESTS
    assert obj.IE_NAME
    assert obj._real_extract

# Generated at 2022-06-14 17:20:21.221762
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	obj = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
	assert obj._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
	assert obj._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
	assert obj._TESTS[0]['info_dict'] == {'id': 'v5qckFJvNJg'}
	assert obj._TESTS[0]['playlist_mincount'] == 45

# Generated at 2022-06-14 17:20:26.103475
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    a = TudouPlaylistIE()
    assert a.IE_NAME == 'tudou:playlist'
    assert a._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:20:31.101821
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test if the class was created properly
    playlist = TudouPlaylistIE('TudouPlaylist', True)
    assert playlist.name == 'TudouPlaylist'
    assert playlist.ie_key() == 'TudouPlaylist'
    assert playlist._WORKING


# Generated at 2022-06-14 17:20:34.466730
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert ie._match_id(ie.IE_NAME) == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:21:00.602284
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert isinstance(TudouPlaylistIE(), InfoExtractor)


# Generated at 2022-06-14 17:21:03.969803
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    class Test(object):
        assert_raises_regexp = lambda self, *args, **kwargs: None
    ie = TudouAlbumIE(Test())
    assert isinstance(ie, TudouAlbumIE)
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 17:21:11.234501
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    ie.url = url
    # Test for the class properties
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:21:16.226836
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE().IE_NAME == 'Tudou:Album'
    assert TudouAlbumIE()._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:21:22.494395
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    example_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tudou_album_ie = TudouAlbumIE(example_url)
    assert tudou_album_ie.ie_name == 'tudou:album'
    assert tudou_album_ie.album_id == 'v5qckFJvNJg'
    assert tudou_album_ie.match(example_url) == True
    assert tudou_album_ie.match('http://www.tudou.com/albumplay/v5qckFJvNg.html') == False

# Generated at 2022-06-14 17:21:30.031859
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
   # Test url
   url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
   # Test constructor
   tudou_playlist_ie = TudouPlaylistIE(url)
   assert tudou_playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
   assert tudou_playlist_ie._match_id('zzdE77v6Mmo') == 'zzdE77v6Mmo'
   assert tudou_playlist_ie._real_extract(url) == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:21:35.385448
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	print('---[TudouAlbumIE]---')
	t = TudouAlbumIE(TudouAlbumIE._TESTS[0])
	print(t.IE_NAME)
	print(t.IE_NAME == 'tudou:album')



# Generated at 2022-06-14 17:21:36.396085
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:21:37.378714
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:21:42.906143
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    #TudouAlbumIE(InfoExtractor):
    assert (TudouAlbumIE.IE_NAME == 'tudou:album')
    assert (TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    assert (TudouAlbumIE._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert (TudouAlbumIE._TESTS[0]['playlist_mincount'] == 45)

# Generated at 2022-06-14 17:22:59.078340
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = "v5qckFJvNJg"
    album_data = "{}"
    test_dict = {
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }
    #assert(TudouAlbumIE(test_dict) is not None)
    #assert(TudouAlbumIE(test_dict)._real_extract(album_id) is not None)
    #print(TudouAlbumIE(test_dict)._real_extract(album_id))

# Generated at 2022-06-14 17:23:07.216716
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE.IE_NAME == 'tudou:album'
    assert TudouAlbumIE.IE_DESC == '土豆网专辑'
    assert TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert TudouAlbumIE._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:23:08.403940
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    pass


# Generated at 2022-06-14 17:23:19.504792
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylist = TudouPlaylistIE()
    #get InfoExtractor for class TudouPlaylistIE
    print(TudouPlaylist.IE_NAME)
    #get name of InfoExtractor for class TudouPlaylistIE
    assert True == TudouPlaylist.suitable('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    #test whether this InfoExtractor can analyze this URL
    assert 'zzdE77v6Mmo' == TudouPlaylist._match_id('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    #test the private method _match_id

# Generated at 2022-06-14 17:23:30.471879
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouPlaylistIE = TudouPlaylistIE()
    playlist_id = "zzdE77v6Mmo"
    playlist_url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    assert tudouPlaylistIE._TESTS[0]['info_dict']['id'] == playlist_id
    assert tudouPlaylistIE._TESTS[0]['url'] == playlist_url
    assert tudouPlaylistIE._TESTS[0]['playlist_mincount'] == 209
    assert tudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudouPlaylistIE._VAL

# Generated at 2022-06-14 17:23:41.140051
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]
    assert ie._real_extract == 'function'


# Generated at 2022-06-14 17:23:42.235911
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()


# Generated at 2022-06-14 17:23:47.092869
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    alb_ie = TudouAlbumIE('1')
    assert alb_ie.IE_NAME == 'tudou:album'
    assert alb_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'



# Generated at 2022-06-14 17:23:57.071435
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print("Testing TudouPlaylistIE")
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    download_url = "http://www.tudou.com/tvp/plist.action?lcode=zzdE77v6Mmo"
    playlist_id = "zzdE77v6Mmo"
    playlist_mincount = 209
    # Constructor
    tudou = TudouPlaylistIE()
    # Method
    playlist = tudou._real_extract(url)

# Generated at 2022-06-14 17:24:04.952126
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE.IE_NAME == 'tudou:playlist'
    assert TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert TudouPlaylistIE.__doc__ == 'tudou:playlist video downloader'
    assert TudouPlaylistIE._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert TudouPlaylistIE._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
    assert TudouPlaylistIE._TESTS[0]['playlist_mincount'] == 209

#