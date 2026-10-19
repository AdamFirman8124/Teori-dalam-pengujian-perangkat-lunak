

# Generated at 2022-06-14 17:16:34.250888
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(url)
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 17:16:41.407597
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_ie = TudouPlaylistIE()
    assert tudou_playlist_ie._download_json == InfoExtractor._download_json
    assert tudou_playlist_ie._match_id(
        'http://www.tudou.com/listplay/pF80sh4f4NA.html') == 'pF80sh4f4NA'
    assert tudou_playlist_ie._real_extract('http://www.tudou.com/listplay/pF80sh4f4NA.html') == {'id': 'pF80sh4f4NA'}

# Generated at 2022-06-14 17:16:43.288901
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:16:44.858169
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	assert TudouPlaylistIE is not None


# Generated at 2022-06-14 17:16:48.340224
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():  
    tudou_playlist_ie = TudouPlaylistIE()
    assert tudou_playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:16:58.648282
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
      url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
      # The constructor should be able to extract id from the url
      assert TudouAlbumIE._match_id(url) == 'v5qckFJvNJg'
      assert TudouAlbumIE(url)._match_id(url) == 'v5qckFJvNJg'
      # Try to __init__ a instance
      tudou_album = TudouAlbumIE(url)
      # Use the __init__'ed instance do some test work
      entries = tudou_album._real_extract(url)
      # Test if the result is correct
      assert len(entries['entries']) == 45
      assert entries['id'] == url[32:44]

# Generated at 2022-06-14 17:16:59.922014
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    res = TudouAlbumIE()


# Generated at 2022-06-14 17:17:03.285940
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:17:06.454978
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:17:09.087820
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    #assert(TudouPlaylistIE is not None)
    return True

# Generated at 2022-06-14 17:17:14.397468
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test that copied constructor of TudouAlbumIE works as expected
    TudouAlbumIE(test_TudouAlbumIE())

# Generated at 2022-06-14 17:17:20.156813
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t = TudouAlbumIE()
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    id = t._match_id(url)
    assert id == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:17:23.044887
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE = TudouPlaylistIE()
    # assert that instance is constructed correctly
    assert(isinstance(TudouPlaylistIE, InfoExtractor))

# Generated at 2022-06-14 17:17:29.883186
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    album_id = 'v5qckFJvNJg'
    album_data = util.download_json('http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)

# Generated at 2022-06-14 17:17:30.777252
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert(TudouPlaylistIE("zzdE77v6Mmo"))

# Generated at 2022-06-14 17:17:34.631908
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    ie = TudouPlaylistIE(url, "Tudou", "TudouPlaylistIE")
    assert ie.playlist_id == "zzdE77v6Mmo"

# Generated at 2022-06-14 17:17:38.054132
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .tudou import TudouAlbumIE
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie._match_id(url) == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:17:40.596763
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE(None)
    assert ie.__class__ == TudouPlaylistIE
# test for the case that input url is valid

# Generated at 2022-06-14 17:17:46.840411
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # test case 1:
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    pl = TudouPlaylistIE()
    assert pl._match_id(url) == 'zzdE77v6Mmo'
    assert pl._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert pl.IE_NAME == 'tudou:playlist'

# Generated at 2022-06-14 17:17:47.925000
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # done, cover
    pass


# Generated at 2022-06-14 17:17:58.317046
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    video = TudouPlaylistIE()
    video.url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    video.extract()

# Generated at 2022-06-14 17:18:00.614387
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:18:11.694679
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Create an instance of class TudouAlbumIE with default arguments
    tudouAlbum = TudouAlbumIE()

    # Assert attributes of instance
    assert tudouAlbum.ie_key == "Tudou:album"
    assert tudouAlbum.ie_name == "Tudou:album"
    assert tudouAlbum.name == "Tudou:album"
    assert (tudouAlbum.ie._VALID_URL == "https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})")

# Generated at 2022-06-14 17:18:12.863604
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    pass

# Generated at 2022-06-14 17:18:13.444981
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	assert True

# Generated at 2022-06-14 17:18:17.742620
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert TudouAlbumIE().IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:18:26.860565
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_albumIE = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert tudou_albumIE.IE_NAME == "tudou:album"
    assert tudou_albumIE.ie_key() == "TudouAlbumIE"
    assert tudou_albumIE._VALID_URL == "https?://(?:www\.)?tudou\.com/album(?:cover|play)/([\w-]{11})"
    assert tudou_albumIE.ie_key() == "TudouAlbumIE"


# Generated at 2022-06-14 17:18:37.964926
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	tudou_constructed_instance = TudouPlaylistIE({"username": "Ikram","password": "testing123"})
	assert isinstance(tudou_constructed_instance,TudouPlaylistIE) == True
	assert tudou_constructed_instance.IE_NAME == 'tudou:playlist'
	assert tudou_constructed_instance._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

# Generated at 2022-06-14 17:18:43.079762
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    x = TudouAlbumIE()
    assert_equals(TudouAlbumIE._VALID_URL, r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    assert_equals(x.IE_NAME, 'tudou:album')

# Generated at 2022-06-14 17:18:50.671922
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    obj = TudouPlaylistIE('id','url','extractor','keyword')
    assert obj.keyword == 'keyword'
    assert obj._match_id('http://www.tudou.com/tvp/plist.action?lcode=zzdE77v6Mmo') == 'zzdE77v6Mmo'
    assert obj._download_json('http://www.tudou.com/tvp/plist.action?lcode=zzdE77v6Mmo', 'zzdE77v6Mmo')['total'] == 209

# Generated at 2022-06-14 17:19:04.815919
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    frm = TudouAlbumIE()
    return frm


# Generated at 2022-06-14 17:19:09.325070
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE()
    assert isinstance(tudou_playlist, InfoExtractor)
    assert tudou_playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudou_playlist._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:19:09.935563
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert True

# Generated at 2022-06-14 17:19:15.346540
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = "http://www.tudou.com/albumplay/%s.html" % 'lhEZq3Iprhw'
    tudou = TudouAlbumIE(url)
    temp = tudou._real_extract()
    print(temp)


# Generated at 2022-06-14 17:19:20.298865
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE()
    t = ie._real_extract(url)

# Generated at 2022-06-14 17:19:27.609071
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE()
    assert tudouAlbumIE.IE_NAME == 'tudou:album'
    assert tudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudouAlbumIE._TESTS == [
        {
            'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
            'info_dict': {
                'id': 'v5qckFJvNJg',
            },
            'playlist_mincount': 45,
        }
    ]


# Generated at 2022-06-14 17:19:30.862802
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    
    #  Success test
    try:
        playlist = TudouPlaylistIE(1)
    except:
        playlist = None
    assert playlist is not None
    
    

# Generated at 2022-06-14 17:19:41.736804
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:19:42.771018
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudoualbum = TudouAlbumIE()

# Generated at 2022-06-14 17:19:49.201389
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('ie', 'name')
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:20:21.043236
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # test case for constructor of class TudouAlbumIE
    t = TudouAlbumIE()

# Generated at 2022-06-14 17:20:27.391277
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_id = u'zzdE77v6Mmo'
    playlist_data = {
        'items': [
            {
                'icode': u'5n5rTRj9eLs',
                'kw': u'神偷奶爸3',
                'rank': u'1',
                'type': u'4',
                'type_code': u'0',
            },
            {
                'icode': u'laQTm8-7WGg',
                'kw': u'神偷奶爸2',
                'rank': u'2',
                'type': u'4',
                'type_code': u'0',
            },
        ]
    }

# Generated at 2022-06-14 17:20:29.160713
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE()

# Generated at 2022-06-14 17:20:35.631489
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	albIE = TudouAlbumIE("https://www.tudou.com/albumplay/v5qckFJvNJg.html")
	assert albIE
	assert albIE.IE_NAME == "tudou:album"
	assert albIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
# end of unit test for constructor of class TudouAlbumIE


# Generated at 2022-06-14 17:20:39.895027
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    m = TudouPlaylistIE(TudouPlaylistIE.IE_NAME)
    assert m.__class__.__name__ == TudouPlaylistIE.IE_NAME
    assert m._VALID_URL == TudouPlaylistIE._VALID_URL
    assert m._TESTS == TudouPlaylistIE._TESTS


# Generated at 2022-06-14 17:20:50.077414
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .common import InfoExtractor
    from .tudou import _API_KEY, _API_URL
    # Assert that TudouAlbumIE can extract correct playlist
    ie = TudouAlbumIE('tudou')
    albumID = 'v5qckFJvNJg'
    api_url = _API_URL % (albumID, _API_KEY)
    # Capture JSON response and save it as a new testcase
    #url = 'http://www.tudou.com/tvp/alist.action?acode=v5qckFJvNJg'
    #import urllib2
    #content = urllib2.urlopen(url).read()
    #with open('test.json', 'wb') as fp:
    #    fp.write(content)

# Generated at 2022-06-14 17:21:01.891368
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Valid URL
    valid_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou_playlist = TudouPlaylistIE(url = valid_url)
    assert tudou_playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudou_playlist.IE_NAME == 'tudou:playlist'
    assert tudou_playlist.ie_key() == 'tudou:playlist'
    assert tudou_playlist.suitable(valid_url)
    # InValid URL
    invalid_url = 'http://www.tudou.com/'
    tudou_play

# Generated at 2022-06-14 17:21:04.874088
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    a = TudouAlbumIE()
    assert a._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert a.IE_NAME == 'tudou:album'



# Generated at 2022-06-14 17:21:09.952132
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert 'http://www.tudou.com/albumcover/v5qckFJvNJg.html' == TudouAlbumIE._TESTS[0]['url']
    assert 'v5qckFJvNJg' == TudouAlbumIE._TESTS[0]['info_dict']['id']

# Generated at 2022-06-14 17:21:16.918892
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:22:36.782112
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """
    Test TudouPlaylistIE constructor
    """
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    info = TudouPlaylistIE()._real_extract(url)
    assert info['id'] == 'zzdE77v6Mmo'
    assert len(info['entries']) >= 209
    assert info['entries'][0]['id'] == 'k5838gfPMS0'
    assert len(info['entries']) == info['_type']['page_data']['count']


# Generated at 2022-06-14 17:22:42.184794
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:22:50.641029
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie.IE_NAME == 'tudou:album'
    assert tudou_album_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudou_album_ie._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:22:55.409729
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:22:56.735906
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_IE = TudouAlbumIE()


# Generated at 2022-06-14 17:22:58.681556
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouPlaylistIE = TudouPlaylistIE()

# Generated at 2022-06-14 17:23:02.577434
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_ie = TudouPlaylistIE()
    tudou_playlist_ie.download('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:23:06.365071
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE()._real_extract(url)

# Generated at 2022-06-14 17:23:09.618736
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

# Generated at 2022-06-14 17:23:16.491632
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE(TudouAlbumIE._downloader)
    assert tudou_album_ie.suitable('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert tudou_album_ie.suitable('http://www.tudou.com/albumcover/v5qckFJvNJg.html')
    assert not tudou_album_ie.suitable('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert not tudou_album_ie.suitable('http://www.tudou.com/listplay/zzdE77v6Mmo.htm')

# Generated at 2022-06-14 17:25:51.583823
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouPlaylistIE = TudouPlaylistIE()
    playlistId = 'zzdE77v6Mmo'
    playlistUrl = 'http://www.tudou.com/listplay/' + playlistId + '.html'
    # Test for function _match_id
    assert playlistId == tudouPlaylistIE._match_id(playlistUrl)
    # Test for function _real_extract
    assert len(tudouPlaylistIE._real_extract(playlistUrl)['entries']) == 209


# Generated at 2022-06-14 17:25:52.886524
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    instance = TudouPlaylistIE()
    assert instance.__class__.__name__ == 'TudouPlaylistIE'

# Generated at 2022-06-14 17:25:57.878233
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_TudouPlaylistIE = TudouPlaylistIE()
    assert test_TudouPlaylistIE._match_id("http://www.tudou.com/listplay/zzdE77v6Mmo.html") == 'zzdE77v6Mmo'

if __name__ == '__main__':
    test_TudouPlaylistIE()

# Generated at 2022-06-14 17:26:00.378021
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouIA = TudouAlbumIE()
    assert tudouIA.ie_key() == 'TudouAlbum'
    assert tudouIA.ie_name() == 'Tudou'

# Generated at 2022-06-14 17:26:03.456205
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    item = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert item is not None


# Generated at 2022-06-14 17:26:04.999822
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE().IE_NAME == 'tudou:album'

test_TudouAlbumIE()

# Generated at 2022-06-14 17:26:10.974818
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert 'tudou:playlist' == TudouPlaylistIE().ie_key()
    assert 'zzdE77v6Mmo' in TudouPlaylistIE()._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')['_type']


# Generated at 2022-06-14 17:26:21.019376
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_id = 'zzdE77v6Mmo'
    playlist_url = 'http://www.tudou.com/listplay/%s.html' % playlist_id

# Generated at 2022-06-14 17:26:22.797956
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE(None)

# Generated at 2022-06-14 17:26:28.152979
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    print(TudouAlbumIE._TESTS[0]['url'])
    ie = TudouAlbumIE()
    print(ie._download_json)
    print(ie._match_id(ie._TESTS[0]['url']))
    print(ie._real_extract(ie._TESTS[0]['url']))