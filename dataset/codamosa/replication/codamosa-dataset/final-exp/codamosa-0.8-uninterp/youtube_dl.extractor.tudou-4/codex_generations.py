

# Generated at 2022-06-14 17:16:31.561038
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:16:33.970658
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	# Init
	a = TudouPlaylistIE()
	assert a

# Generated at 2022-06-14 17:16:42.748314
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_id = 'zzdE77v6Mmo'
    playlist_url = 'http://www.tudou.com/listplay/%s.html' % playlist_id
    playlist_url_static = 'http://www.tudou.com/listplay/static/%s.xml' % playlist_id

# Generated at 2022-06-14 17:16:46.877118
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # test for constructor of class TudouAlbumIE
    album_id = 'v5qckFJvNJg'
    album_data = 'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id
    entries = 'http://www.tudou.com/programs/view/%s' % album_data['items']['icode']
    tudou = TudouAlbumIE()
    tudou.playlist_result(entries, album_id)


# Generated at 2022-06-14 17:16:50.461539
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
        album = TudouAlbumIE()
        assert album.IE_NAME == 'tudou:album'


# Generated at 2022-06-14 17:16:55.258932
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	print("testing TudouAlbumIE")
	o = TudouAlbumIE()
	o.extract("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
	o.extract("http://www.tudou.com/albumcover/v5qckFJvNJg.html")

# Generated at 2022-06-14 17:16:57.147595
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
   TudouAlbumIE('https://www.tudou.com/albumcover/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:16:59.446692
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._VALID_URL is not None


# Generated at 2022-06-14 17:17:03.297189
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	album = TudouAlbumIE()
	url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
	assert album._match_id(url) == "v5qckFJvNJg"

# Generated at 2022-06-14 17:17:11.748275
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert TudouPlaylistIE.IE_NAME == 'tudou:playlist'
    assert TudouPlaylistIE._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:17:18.685045
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    a =  TudouPlaylistIE()

# Generated at 2022-06-14 17:17:20.330325
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	TudouPlaylistIE("http://www.tudou.com/listplay/zzdE77v6Mmo.html")


# Generated at 2022-06-14 17:17:24.104416
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .test_common import test_template
    test_template('http://www.tudou.com/albumplay/v5qckFJvNJg.html',
                  expected_title='Drama - 日剧')

# Generated at 2022-06-14 17:17:28.022606
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:17:37.120762
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    # Test ie._real_extract()
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    ie.url = url
    playlist_id = ie._match_id(url)
    data = ie._download_json(
        'http://www.tudou.com/tvp/alist.action?acode=%s' % playlist_id, playlist_id)
    entries = [ie.url_result(
        'http://www.tudou.com/programs/view/%s' % item['icode'],
        'Tudou', item['icode'],
        item['kw']) for item in data['items']]

# Generated at 2022-06-14 17:17:43.386230
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    expected_id = 'v5qckFJvNJg'
    TudouAlbumIE(test_url)
    actual_id = TudouAlbumIE._real_extract(TudouAlbumIE, test_url)
    assert expected_id == actual_id


# Generated at 2022-06-14 17:17:54.834442
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test playlist which only contains one video
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    extractor = TudouPlaylistIE()
    assert extractor.suits(url) is True
    result = extractor.extract(url)
    assert result['id'] == 'zzdE77v6Mmo'
    assert len(result['entries']) == 1
    assert result['entries'][0]['id'] == 'jBCV7-k3qyk'
    assert result['entries'][0]['url'] == 'http://www.tudou.com/programs/view/jBCV7-k3qyk/'

# Generated at 2022-06-14 17:17:58.321588
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .test_tudou import TudouIE
    TudouIE()._test_tudou_albumn_constructor(TudouAlbumIE)


# Generated at 2022-06-14 17:17:59.667141
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE, "TudouAlbumIE"  # basic smoke test

# Generated at 2022-06-14 17:18:01.146296
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	print('test_TudouAlbumIE')
	assert 1 == 1

# Generated at 2022-06-14 17:18:18.049326
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    print('\nUnit test for constructor of class TudouAlbumIE')
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    albumIE = TudouAlbumIE(url)
    assert albumIE.IE_NAME == 'tudou:album', 'IE_NAME shoulde be tudou:album'
    assert albumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})', '_VALID_URL shoulde be https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:18:19.022816
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:18:24.080282
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'


# Generated at 2022-06-14 17:18:24.740302
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:18:31.972364
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.tudou_playlist_url_regex.match('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert ie.tudou_playlist_url_regex.match('http://www.tudou.com/listplay/12345678999.html') is None

# Generated at 2022-06-14 17:18:39.702084
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ## Get all playlist_mincount of test cases, add them to total_mincount
    total_mincount = 0
    for testcase in TudouPlaylistIE._TESTS:
        total_mincount = total_mincount + testcase['playlist_mincount']

# Generated at 2022-06-14 17:18:40.802563
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()


# Generated at 2022-06-14 17:18:44.574718
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert (TudouAlbumIE._VALID_URL
            == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')


# Generated at 2022-06-14 17:18:47.198606
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouPlaylistIE = TudouPlaylistIE()
    tudouPlaylistIE.download('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:18:50.103321
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html') is not None


# Generated at 2022-06-14 17:19:12.429194
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_url = 'http://www.tudou.com/albumplay/6U9-VbvRCws.html'
    album_id = '6U9-VbvRCws'

# Generated at 2022-06-14 17:19:18.567045
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	Test = TudouAlbumIE('http://www.tudou.com/albumcover/v5qckFJvNJg.html', 'Tudou', 'v5qckFJvNJg', 'http://www.tudou.com/albumplay/v5qckFJvNJg.html')
	Result = Test.test_TudouAlbumIE()
	if (Result == 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'):
		print("Unit test passed")

# Generated at 2022-06-14 17:19:27.287797
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:19:31.006228
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert [
        TudouPlaylistIE
    ] == [
        cls
        for cls in (
            InfoExtractor,
        )
        if cls.__module__.endswith('.tudou') and cls._VALID_URL
    ]


# Generated at 2022-06-14 17:19:42.694133
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from urlparse import urlparse
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    #url = 'http://www.tudou.com/tvp/alist.action?aCode=F4uX7VSPW_4'
    #url = 'http://www.tudou.com/albumplay/F4uX7VSPW_4.html'
    #url = 'http://www.tudou.com/albumcover/F4uX7VSPW_4.html'
    uri = urlparse(url)
    ie = TudouPlaylistIE._get_ie(uri.hostname)
    assert ie is not None, 'Unsupported/Invalid hostname in url(%s)' % url

# Generated at 2022-06-14 17:19:49.584123
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE(None)._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert TudouPlaylistIE(None).IE_NAME == 'tudou:playlist'


# Generated at 2022-06-14 17:19:54.814822
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_IE = TudouPlaylistIE()
    tudou_playlist_IE.IE_NAME = 'tudou:playlist'

# Generated at 2022-06-14 17:19:59.771954
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:20:03.118155
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test for class constructor
    ie = TudouAlbumIE("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    assert ie.IE_NAME == 'tudou:album'



# Generated at 2022-06-14 17:20:06.203278
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert (ie.IE_NAME == 'tudou:playlist')


# Generated at 2022-06-14 17:20:36.370836
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_test = TudouAlbumIE()
    assert tudou_album_test


# Generated at 2022-06-14 17:20:43.486602
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
   ie = TudouAlbumIE()
   playlist_id = 'v5qckFJvNJg'
   playlist_data = ie._download_json(
            'http://www.tudou.com/tvp/alist.action?acode=%s' % playlist_id, playlist_id)
   entries = [ie.url_result(
            'http://www.tudou.com/programs/view/%s' % item['icode'],
            'Tudou', item['icode'],
            item['kw']) for item in playlist_data['items']]
   ie.playlist_result(entries, playlist_id)

# Generated at 2022-06-14 17:20:49.093782
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]
    assert isinstance (ie, InfoExtractor) == True


# Generated at 2022-06-14 17:20:53.153470
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:20:59.267346
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	from extractors import TudouPlaylistIE
	# This test is to test the constructor of class TudouPlaylistIE
	# Arrange
	TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

	# Act
	# Nothing needs to act in this case

	# Assert
	# Nothing needs to assert in this case


# Generated at 2022-06-14 17:21:00.182794
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
  TudouAlbumIE()

# Generated at 2022-06-14 17:21:03.070380
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE()._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'


# Generated at 2022-06-14 17:21:09.268681
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    creator = TudouAlbumIE
    album_id = 'v5qckFJvNJg'
    assert creator._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert creator._TESTS is None


# Generated at 2022-06-14 17:21:11.953803
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    s = ie._real_extract("https://www.tudou.com/listplay/zzdE77v6Mmo.html")

# Generated at 2022-06-14 17:21:21.545577
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_ie = TudouPlaylistIE()
    assert tudou_playlist_ie.IE_NAME == 'tudou:playlist'
    assert tudou_playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudou_playlist_ie._TESTS == [
        {
            'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
            'info_dict': {
                'id': 'zzdE77v6Mmo',
            },
            'playlist_mincount': 209,
        }
    ]
    assert tudou_playlist_ie._downloader

# Generated at 2022-06-14 17:22:31.499233
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_TudouAlbumIE = TudouAlbumIE()

# Generated at 2022-06-14 17:22:36.413045
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	# The test data is the url of the video below.
	# https://www.tudou.com/listplay/dPlw6sSLsck/cjKGdX9v_0o.html
	url = 'http://www.tudou.com/listplay/dPlw6sSLsck.html'
	TudouPlaylistIE().suitable(url)

# Generated at 2022-06-14 17:22:48.088220
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    #创建一个tudou.com网站的播放列表对象
    ie = TudouPlaylistIE()
    #测试URL是否符合正则表达式
    assert ie._is_valid_url('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert ie._is_valid_url('http://www.tudou.com/listplay/zzdE77v6Mmo/')
    assert ie._is_valid_url('http://www.tudou.com/listplay/zzdE77v6Mmo')

# Generated at 2022-06-14 17:22:50.455118
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE(url)


# Generated at 2022-06-14 17:22:56.736770
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_obj = TudouAlbumIE(KalturaIE(), "http://www.tudou.com/albumplay/v5qckFJvNJg.html", "id")
    assert test_obj.suitable("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    assert test_obj.valid

# Generated at 2022-06-14 17:23:01.607329
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    Playlist = TudouPlaylistIE('playlist')
    assert Playlist.IE_NAME == 'tudou:playlist'
    assert Playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

# Generated at 2022-06-14 17:23:06.745985
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:23:08.175566
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .TudouIE import TudouAlbumIE
    assert TudouAlbumIE(1,2,3)



# Generated at 2022-06-14 17:23:09.405656
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:23:12.274093
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    entry = ie._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    print(entry)



# Generated at 2022-06-14 17:25:32.142464
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/tvp/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(url, "Tudou")
    assert ie.url == url
    assert ie.ie_key == "Tudou"


# Generated at 2022-06-14 17:25:35.597404
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE(None)._real_extract("http://www.tudou.com/albumplay/v5qckFJvNJg.html")

# Generated at 2022-06-14 17:25:44.156832
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	t = TudouPlaylistIE()
	# Test case 1:
	assert len(t.ie_key()) == 1
	# Test case 2:
	assert t.ie_key()[0] == 'tudou:playlist'
	# Test case 3:
	assert len(t.extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')) == 3
	# Test case 4:
	assert t.extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')[0] == 'zzdE77v6Mmo'
	# Test case 5:

# Generated at 2022-06-14 17:25:53.296718
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    valid_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    valid_url2 = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    invalid_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html/invalid'
    assert(TudouAlbumIE._match_id(valid_url) == 'v5qckFJvNJg')
    assert(TudouAlbumIE._match_id(valid_url2) == 'v5qckFJvNJg')
    assert(TudouAlbumIE._match_id(invalid_url) is None)


# Generated at 2022-06-14 17:26:04.731018
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test valid url
    result = TudouAlbumIE()._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:26:10.304841
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('tudou:album')
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:26:19.151273
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouplaylist_ie = TudouPlaylistIE()
    assert tudouplaylist_ie._VALID_URL == "https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html"
    assert tudouplaylist_ie._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:26:23.450956
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._get_video_id('https://www.tudou.com/listplay/zzdE77v6Mmo.html') == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:26:31.458816
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
  inst = TudouPlaylistIE()
  assert inst._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11}).html'
  assert inst.IE_NAME == r'tudou:playlist'
  assert inst._TESTS[0] == {'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
  'info_dict': {'id': 'zzdE77v6Mmo'},
  'playlist_mincount': 209}
