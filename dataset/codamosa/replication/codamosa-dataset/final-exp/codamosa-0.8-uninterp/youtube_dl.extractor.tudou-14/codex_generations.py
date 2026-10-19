

# Generated at 2022-06-14 17:16:27.964939
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    a = TudouAlbumIE()
    print(a)

# Generated at 2022-06-14 17:16:40.244353
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    id = 'v5qckFJvNJg'
    expectent_entries = {'url': 
        'http://www.tudou.com/programs/view/v5qckFJvNJg',
        'ie_key': 'Tudou',
        'playlist_index': None, '_type': 'url_transparent',
        'id': 'v5qckFJvNJg', 'ext': 'mp4', 'title': '与神同行'}
    tudou_album_ie = TudouAlbumIE()
    tudou_album_ie._real_extract(url)
    entries = tudou_album_ie._ent

# Generated at 2022-06-14 17:16:42.832644
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # As class TudouAlbumIE has no __init__(), it uses the default
    # constructor (with no parameters) of its parent class.
    tudou = TudouAlbumIE()

# Generated at 2022-06-14 17:16:50.696246
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .tudou import TudouAlbumIE

    # A valid URL
    assert bool(TudouAlbumIE._VALID_URL.match('http://www.tudou.com/albumplay/v5qckFJvNJg.html'))

    # Invalid URL (albumcover instead of albumplay)
    assert not bool(TudouAlbumIE._VALID_URL.match('http://www.tudou.com/albumcover/v5qckFJvNJg.html'))

    # Invalid URL (missing album ID)
    assert not bool(TudouAlbumIE._VALID_URL.match('http://www.tudou.com/albumplay/.html'))

# Generated at 2022-06-14 17:16:57.471613
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	input_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
	ie = TudouPlaylistIE(input_url,'Tudou', 'zzdE77v6Mmo')
	assert ie.get_id() == 'zzdE77v6Mmo'
	assert ie.get_url() == input_url
	assert ie.get_name() == 'Tudou'
	#assert ie.get_video_id() == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:17:00.335018
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	TudouAlbumIE = TudouAlbumIE()
	assert TudouAlbumIE is not None
	print("Test completed: TudouAlbumIE")

# Generated at 2022-06-14 17:17:01.028204
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE([])

# Generated at 2022-06-14 17:17:03.739669
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:17:07.590483
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:17:09.189176
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .tudou import TudouPlaylistIE
    test_obj = TudouPlaylistIE()

# Generated at 2022-06-14 17:17:16.239391
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .common import expected_warnings 
    with expected_warnings(['192.168.1.1:8080']):
        url1 = 'http://192.168.1.1:8080/listplay/zzdE77v6Mmo.html'
        TudouPlaylistIE(url1)

# Generated at 2022-06-14 17:17:23.779584
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
    from YoutubeDL import YoutubeDL

    dl = YoutubeDL({"verbose": True})
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    playlist = dl.extract_info(url, download=False)
    assert playlist['id'] == "zzdE77v6Mmo"

# Generated at 2022-06-14 17:17:30.450590
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """
    Unit test for TudouPlaylistIE
    """
    instance = TudouPlaylistIE()
    assert (instance._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')


# Generated at 2022-06-14 17:17:40.430644
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    obj = TudouPlaylistIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert obj._TESTS[0] == {'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html', 'info_dict': {'id': 'zzdE77v6Mmo'}, 'playlist_mincount': 209, }
    assert obj.IE_NAME == 'tudou:playlist'
    assert obj.ie_key() == 'TudouPlaylist'


# Generated at 2022-06-14 17:17:48.788166
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou_playlist_ie_instance = TudouPlaylistIE(test_url)
    test_url_handler_instance = tudou_playlist_ie_instance._build_url_handler(test_url)
    assert(hasattr(tudou_playlist_ie_instance, '_VALID_URL') == True)
    assert(isinstance(tudou_playlist_ie_instance._VALID_URL, (str, unicode)) == True)
    assert(isinstance(tudou_playlist_ie_instance._VALID_URL, unicode) == True)

# Generated at 2022-06-14 17:17:58.497538
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE(None)._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert TudouAlbumIE(None).IE_NAME == 'tudou:album'
    assert TudouAlbumIE(None)._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert TudouAlbumIE(None)._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg'
    assert TudouAlbumIE(None)._TESTS[0]['playlist_mincount'] == 45

# Generated at 2022-06-14 17:18:00.829069
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    IE_test_object = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html');

# Generated at 2022-06-14 17:18:08.153588
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album = TudouAlbumIE('abcd1234')

    assert album.IE_NAME == 'tudou:album'
    assert album.IE_DESC == '土豆网 - 专辑'
    assert album._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:18:13.199966
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie_obj = TudouAlbumIE('www.tudou.com')
    assert ie_obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
 

# Generated at 2022-06-14 17:18:18.147426
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE().ie_name == \
        'tudou:playlist'
    assert TudouPlaylistIE()._VALID_URL == \
        r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert TudouPlaylistIE()._TESTS == \
        [{'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
          'info_dict': {'id': 'zzdE77v6Mmo'},
          'playlist_mincount': 209,
          }]
    assert TudouPlaylistIE()._default_extractor_id() == \
        'tudou:playlist'
    assert TudouPlaylistIE()._

# Generated at 2022-06-14 17:18:26.980136
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie_TudouAlbumIE = TudouAlbumIE()
    assert ie_TudouAlbumIE

# Generated at 2022-06-14 17:18:29.366324
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    # Expected value
    ie_expected = ie
    # Obtained value
    ie_obtained = TudouAlbumIE()
    # Comparison
    assert ie == ie_obtained


# Generated at 2022-06-14 17:18:38.685747
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE('tudou')
    assert tudou_playlist.ie_key() == 'tudou:playlist'
    assert tudou_playlist.ie_name() == 'tudou:playlist'
    assert tudou_playlist.IE_NAME == 'tudou:playlist'
    assert tudou_playlist.test() == False
    assert tudou_playlist.test_url() == False
    assert tudou_playlist.test_url('https://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert tudou_playlist.test_url('https://www.tudou.com/listplay/zzdE77v6Mmo.html', False)
    assert tud

# Generated at 2022-06-14 17:18:41.493822
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # test constructor of class TudouAlbumIE
    # fail if expected exception thrown
    try:
        t = TudouAlbumIE()
    except:
        assert False
    assert True

# Generated at 2022-06-14 17:18:44.017707
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	tudou_playlist_ie = TudouPlaylistIE()

# Generated at 2022-06-14 17:18:50.000862
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


# Generated at 2022-06-14 17:18:51.864610
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	TudouPlaylistIE()

# Generated at 2022-06-14 17:18:59.930260
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	result = TudouPlaylistIE("http://www.tudou.com/listplay/zzdE77v6Mmo.html")
	assert result != None
	assert result.playlist_id == "zzdE77v6Mmo"
	assert result.query_data() == "lcode=zzdE77v6Mmo"
	assert result.ie_key() == "TudouPlaylist"
	assert result.result_type() == "playlist"
	assert result.format_url() == "http://www.tudou.com/tvp/plist.action?lcode=zzdE77v6Mmo"
	assert result.format_data() == "json"


# Generated at 2022-06-14 17:19:04.008405
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    res = TudouAlbumIE()._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert res['id'] == 'v5qckFJvNJg'
    assert res['entries']
    assert len(res['entries']) == 45

# Generated at 2022-06-14 17:19:07.065657
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	# Test invalid URL
	assert TudouPlaylistIE._build_url(None) == None

	# Test valid URL
	assert TudouPlaylistIE._build_url('http://www.tudou.com/listplay/zzdE77v6Mmo.html') == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'


# Generated at 2022-06-14 17:19:23.962226
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert(TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert(TudouPlaylistIE.IE_NAME == 'tudou:playlist')
    

# Generated at 2022-06-14 17:19:25.392090
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	tudou = TudouAlbumIE()


# Generated at 2022-06-14 17:19:27.036343
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_TudouAlbumIE = TudouAlbumIE()

# Generated at 2022-06-14 17:19:33.818496
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """ Test cases for TudouPlaylistIE constructor """

    # Test the url 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(TudouPlaylistIE._VALID_URL)
    assert ie.name == TudouPlaylistIE.IE_NAME
    assert ie.url == TudouPlaylistIE._VALID_URL
    assert ie.valid
    assert ie.playlist_id == 'zzdE77v6Mmo'

    # Test the url 'https://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(TudouPlaylistIE._VALID_URL.replace('http', 'https'))
    assert ie.name == TudouPlaylistIE.IE

# Generated at 2022-06-14 17:19:38.155506
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:47.321048
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert(TudouPlaylistIE._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert(TudouPlaylistIE._TESTS[0] == {
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    })
    return 0


# Generated at 2022-06-14 17:19:51.605308
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # URL of album cover
    url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    # Instance of class InfoExtractor
    i = InfoExtractor()
    # Verify if the URL is supported
    assert i.suitable(url)

# Generated at 2022-06-14 17:19:58.220111
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:20:02.682008
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:20:10.820885
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    playlist_id = 'zzdE77v6Mmo'
    playlist_data = ie._download_json(
        'http://www.tudou.com/tvp/plist.action?lcode=%s' % playlist_id, playlist_id)
    entries = [ie.url_result(
        'http://www.tudou.com/programs/view/%s' % item['icode'],
        'Tudou', item['icode'],
        item['kw']) for item in playlist_data['items']]
    ie.playlist_result(entries, playlist_id)

# Generated at 2022-06-14 17:20:41.116817
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert str(TudouAlbumIE()) == 'tudou:album'

# Generated at 2022-06-14 17:20:51.013694
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	info = TudouPlaylistIE()
	info._VALID_URL = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'

# Generated at 2022-06-14 17:20:54.048716
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert(ie.logger().name == 'tudou:playlist')


# Generated at 2022-06-14 17:21:03.802820
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test example
    valid_url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    test_album_ex = TudouAlbumIE()
    match_test_ex = test_album_ex._match_id(valid_url)
    assert match_test_ex == 'v5qckFJvNJg', 'Should be "v5qckFJvNJg"'
    assert test_album_ex._VALID_URL == test_album_ex._TESTS[0]['url'] == valid_url, "Test should be invalid"

    # Test another example
    valid_url = "http://www.tudou.com/albumcover/fhcudX9ybk4.html"
    test_album_ex = TudouAlbumIE()

# Generated at 2022-06-14 17:21:08.680148
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """Unit test for constructor of class TudouPlaylistIE"""
    assert 'http://www.tudou.com/listplay/zzdE77v6Mmo.html' \
                == TudouPlaylistIE._VALID_URL[0]


# Generated at 2022-06-14 17:21:09.737495
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:21:19.033416
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # test with invalid url
    assert (TudouAlbumIE._VALID_URL ==
            r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    assert (TudouAlbumIE._VALID_URL ==
            'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    assert TudouAlbumIE._VALID_URL == (
        r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')

# Generated at 2022-06-14 17:21:28.777474
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Arrange
    videoUrl = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    tudouIe = TudouAlbumIE(TudouAlbumIE._WORKER, TudouAlbumIE._UPLOADER)

    # Act
    info = tudouIe._real_extract(videoUrl)
    print(info)

    # Assert

# Generated at 2022-06-14 17:21:38.994966
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]


# Generated at 2022-06-14 17:21:43.675039
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album = TudouAlbumIE()
    url = 'http://www.tudou.com/albumcover/gW_n8n2kmrY.html'
    return album.suitable(url)


# Generated at 2022-06-14 17:22:57.232223
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Extract playlist without crash
    TudouAlbumIE().extract(
        'http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:23:00.377363
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    info = TudouAlbumIE()._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert info['id'] == 'v5qckFJvNJg'
    assert len(info['entries']) == 45


# Generated at 2022-06-14 17:23:02.173053
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == 'tudou:album'



# Generated at 2022-06-14 17:23:08.300524
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE();
    assert tudou_album_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'



# Generated at 2022-06-14 17:23:13.765339
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    newurl = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tudou_album_instance = TudouAlbumIE()
    expected_url = tudou_album_instance._real_extract(url)
    print(expected_url)

    assert(expected_url==newurl)


# Generated at 2022-06-14 17:23:17.254973
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_IE = TudouAlbumIE('')
    assert tudou_album_IE.IE_NAME == 'tudou:album'
    assert tudou_album_IE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:23:22.649036
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie =TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert ie._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
    assert ie._TESTS[0]['playlist_mincount'] == 209


# Generated at 2022-06-14 17:23:32.599874
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = 'v5qckFJvNJg'

# Generated at 2022-06-14 17:23:34.794716
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE()
    assert tudou_playlist.ie_key() == 'TudouPlaylist'

# Generated at 2022-06-14 17:23:44.851390
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE()
    assert (test.IE_NAME == 'tudou:playlist')
    assert (test._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert (test._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }])
    