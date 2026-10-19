

# Generated at 2022-06-14 17:16:31.561537
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:16:32.649723
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    print("test_TudouAlbumIE")

# Generated at 2022-06-14 17:16:39.999030
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url_1 = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    url_2 = 'http://www.tudou.com/listplay/ejm0W2grCiI.html'
    url_3 = 'http://www.tudou.com/listplay/4x4nTglTfKc.html'
    TudouPlaylistIE(url_1)
    TudouPlaylistIE(url_2)
    TudouPlaylistIE(url_3)

    return True

# Generated at 2022-06-14 17:16:44.183750
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test case of invalid URL
    invalid_album_ie = IE_NAME(False, 'https://www.tudou.com/')
    assert invalid_album_ie.valid_url(False, invalid_album_ie._VALID_URL)


# Generated at 2022-06-14 17:16:54.954172
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_url = "http://www.tudou.com/albumcover/K9wlU6nZU6I.html"
    album_id = "K9wlU6nZU6I"
    album_title = "江南路口3 - 韩国"
    album_items_cnt = 46

    ie = TudouAlbumIE(None)

    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    # Initialization
    assert ie.construct_url(album_url, None) == album_url
    assert ie.construct_url(album_url, album_id) == album_url

    # Get album information
    album

# Generated at 2022-06-14 17:16:57.452948
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert TudouPlaylistIE._match_url(url)

# Generated at 2022-06-14 17:16:59.448679
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	assert isinstance(TudouPlaylistIE, InfoExtractor)
	

# Generated at 2022-06-14 17:17:00.754840
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()

# Generated at 2022-06-14 17:17:06.772547
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
        url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
        album_id = "v5qckFJvNJg"
        playlist_mincount = 45
        album_data = {'items': [{'icode': 'BzK4uVJq3zI', 'kw': 'TV'},
                                {'icode': 'DwP0oR-0oQs', 'kw': 'TV'},
                                {'icode': 'v5qckFJvNJg', 'kw': 'TV'}]}

        assert(get_tudou_album_data() == album_data)
        assert(get_tudou_album_id() == album_id)

# Generated at 2022-06-14 17:17:09.533825
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist = TudouPlaylistIE()
    a = playlist.url_result()
    print(a)


# Generated at 2022-06-14 17:17:15.519319
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = ""
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    tudou = TudouAlbumIE()

# Generated at 2022-06-14 17:17:20.262330
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from . import _tests_base as tests_base
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tests_base.test_construtctor_results(TudouAlbumIE, [url])

# Generated at 2022-06-14 17:17:21.491303
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()

# Generated at 2022-06-14 17:17:28.783868
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    # Constructor of class TudouPlaylistIE should initialize Name of ie.
    ie.IE_NAME
    # Constructor of class TudouPlaylistIE should initialize _VALID_URL.
    ie._VALID_URL
    # Constructor of class TudouPlaylistIE should initialize _TESTS.
    ie._TESTS
    # Constructor of class TudouPlaylistIE should initialize _TESTS[0]['url']
    # with expected_url
    expected_url = r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    ie._TESTS[0]['url'] == expected_url


# Generated at 2022-06-14 17:17:35.721495
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """Test constructor of class TudouPlaylistIE"""
    test_obj = TudouPlaylistIE()
    assert test_obj.IE_NAME == 'tudou:playlist'
    assert test_obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert test_obj._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'



# Generated at 2022-06-14 17:17:45.932849
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE('www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert TudouAlbumIE('http://www.tudou.com/albumcover/v5qckFJvNJg.html')
    assert TudouAlbumIE('www.tudou.com/albumcover/v5qckFJvNJg.html')
    assert TudouAlbumIE('http://www.tudou.com/albumcover/v5qckFJvNJg')
    assert TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg')
    assert Tud

# Generated at 2022-06-14 17:17:49.645757
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert isinstance(ie, InfoExtractor)
    assert hasattr(ie, 'IE_NAME') and ie.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:17:53.602094
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    try:
        tudou_album_ie = TudouAlbumIE()
    except Exception as e:
        assert str(e) == 'The tudou:album extractor is broken. Please report this issue on https://github.com/rg3/youtube-dl/issues/new with the link of the video and this log.'

# Generated at 2022-06-14 17:17:57.748483
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(url)

# Generated at 2022-06-14 17:18:00.024616
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert isinstance(TudouPlaylistIE(), TudouPlaylistIE)
    assert isinstance(TudouAlbumIE(), TudouAlbumIE)

# Generated at 2022-06-14 17:18:11.174182
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    class_name = "TudouAlbumIE"
    ie = TudouAlbumIE()
    assert ie.IE_NAME == "tudou:album"
    assert ie._VALID_URL == "https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})"
    assert len(ie._TESTS) == 1

# Generated at 2022-06-14 17:18:13.199925
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()


# Generated at 2022-06-14 17:18:14.984523
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE(TudouAlbumIE._downloader, TudouAlbumIE._VALID_URL)

# Generated at 2022-06-14 17:18:24.077249
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('http://www.tudou.com/albumcover/gFV7XpHnzo8.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/gFV7XpHnzo8.html',
        'info_dict': {
            'id': 'gFV7XpHnzo8',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:18:24.788009
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert str(TudouPlaylistIE)

# Generated at 2022-06-14 17:18:37.182578
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert(TudouAlbumIE.IE_NAME == 'tudou:album')
    assert(TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    print('Test class TudouAlbumIE with url: http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    print(TudouAlbumIE()._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html'))
    print(TudouAlbumIE()._real_extract('http://www.tudou.com/albumcover/v5qckFJvNJg'))


# Generated at 2022-06-14 17:18:42.981000
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .common import FakeYDL
    from .test_common import expected
    from . import TudouPlaylistIE

    ydl = FakeYDL()
    TudouPlaylistIE.TudouPlaylistIE().go(ydl, {
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'name_convert_fun': expected(ydl, 'tudou_playlist', 'zzdE77v6Mmo'),
    })


# Generated at 2022-06-14 17:18:48.842123
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE.IE_NAME == 'tudou:playlist'
    assert TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

    # Test changing class name
    td = TudouPlaylistIE(TudouPlaylistIE._VALID_URL)
    assert td.ie_key() == 'Tudou'
    assert td.ie_name() == 'tudou:playlist'


# Generated at 2022-06-14 17:18:58.663251
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # prepare sample data
    import json
    import os

    SAMPLE_FILE_JSON = 'tudou_albuminfo_test.js'
    SAMPLE_FILE_TEXT = 'tudou_albuminfo_test.txt'

    if not os.path.exists(SAMPLE_FILE_JSON):
        data = json.load(open(SAMPLE_FILE_TEXT))
        with open(SAMPLE_FILE_JSON, 'w') as f:
            json.dump(data, f)

    # call constructor and check the returned value
    from .common import TudouAlbumIE
    ie = TudouAlbumIE()

    data_json = json.load(open(SAMPLE_FILE_JSON))

# Generated at 2022-06-14 17:19:03.884959
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print("Testing TudouPlaylistIE")
    info = TudouPlaylistIE(None)
    assert("tudou:playlist" == info.ie_key())
    assert("tudou" == info.host)
    assert("zzdE77v6Mmo" == info._match_id("http://www.tudou.com/listplay/zzdE77v6Mmo.html"))
    assert(info._VALID_URL == info._VALID_URL)
    assert(info._TESTS == info._TESTS)
    print("Testing TudouPlaylistIE success")


# Generated at 2022-06-14 17:19:19.966418
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test download playlist
    playlist_id = 'zzdE77v6Mmo'
    playlist_url = 'http://www.tudou.com/listplay/%s.html' % playlist_id
    TudouPlaylistIE().download([playlist_url])


# Generated at 2022-06-14 17:19:24.033189
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url_listplay = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    data_listplay = 'DllLlrDoom8'
    tudou_listplay = TudouPlaylistIE()
    assert tudou_listplay._match_id(url_listplay) == data_listplay


# Generated at 2022-06-14 17:19:27.294886
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ydl = TudouPlaylistIE()
    assert ydl._real_extract(url)

# Generated at 2022-06-14 17:19:32.748314
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # URL: http://www.tudou.com/listplay/zzdE77v6Mmo.html
    # URL: http://www.tudou.com/albumcover/zzdE77v6Mmo
    playlist_id = "zzdE77v6Mmo"

    playlist_download_url = "http://www.tudou.com/tvp/plist.action?lcode=" + playlist_id
    playlist_data = json.loads(urllib2.urlopen(playlist_download_url).read())
    items = playlist_data["items"]

    playlist = {}
    playlist["id"] = playlist_id
    playlist["title"] = playlist_data["listName"]
    playlist["description"] = ""
    playlist["thumbnail"] = ""


# Generated at 2022-06-14 17:19:34.716697
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    extractor = TudouAlbumIE()
    assert extractor



# Generated at 2022-06-14 17:19:38.154821
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:19:40.388712
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    testIE = InfoExtractor()
    assert testIE.IE_NAME == "TudouPlaylistIE"
    assert type(testIE.IE_NAME) is str


# Generated at 2022-06-14 17:19:43.101718
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    TudouAlbumIE(url)
# End of unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:19:53.321346
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # test valid case
    playlist = TudouPlaylistIE()
    assert playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert playlist.IE_NAME == r'tudou:playlist'
    assert playlist._TESTS == [{
            'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
            'info_dict': {
                'id': 'zzdE77v6Mmo',
            },
            'playlist_mincount': 209,
        }]

 # Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:19:57.929110
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist = TudouPlaylistIE({})
    assert playlist.ie_key() == 'Tudou:playlist'
    assert playlist.test() == None #TODO


# Generated at 2022-06-14 17:20:31.458241
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    albumIE = TudouAlbumIE()
    assert (albumIE is not None)

# Generated at 2022-06-14 17:20:33.600813
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:20:43.409801
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_IE = TudouPlaylistIE()
    if tudou_playlist_IE is not None:
        assert tudou_playlist_IE.IE_NAME == "tudou:playlist"
        # Test if the field _VALID_URL is properly set
        if tudou_playlist_IE._VALID_URL is not None:
            assert "https?://(?:www\\.)?tudou\\.com/listplay/(?P<id>[\\w-]{11})\\.html" == tudou_playlist_IE._VALID_URL
            # Test if the field _TESTS is properly set

# Generated at 2022-06-14 17:20:47.901637
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tudou_album_ie = TudouAlbumIE()
    info_dict = tudou_album_ie._real_extract(url)
    assert info_dict['id'] == 'v5qckFJvNJg'
    assert info_dict['playlist_mincount'] == 45
    assert len(info_dict['entries']) == 45



# Generated at 2022-06-14 17:20:49.867327
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/ZZdE77v6Mmo.html'
    tudouPlaylistIE = TudouPlaylistIE(url)
    assert tudouPlaylistIE


# Generated at 2022-06-14 17:21:00.866918
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Construct basic object
    tudou_playlist = TudouPlaylistIE("http://www.tudou.com/listplay/zzdE77v6Mmo.html")
    # Check if object has valid name
    assert tudou_playlist.IE_NAME == "tudou:playlist"
    # Check if object has valid url
    assert tudou_playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    # Check if object has valid function
    assert tudou_playlist._real_extract == TudouPlaylistIE._real_extract


# Generated at 2022-06-14 17:21:06.839871
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print("Testing constructor of class TudouPlaylistIE")
    ie = TudouPlaylistIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie._TESTS[0] == {
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }
    assert ie.IE_NAME == 'tudou:playlist'


# Generated at 2022-06-14 17:21:07.404219
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert(True)

# Generated at 2022-06-14 17:21:08.960017
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	assert True == True



# Generated at 2022-06-14 17:21:19.365997
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print("Running unit test for constructor of class TudouPlaylistIE")
    tudou_playlist_ie = TudouPlaylistIE()
    assert tudou_playlist_ie.get_IE_name() == 'tudou:playlist'
    assert tudou_playlist_ie.get_IE_valid_url() == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

# Generated at 2022-06-14 17:22:03.557522
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    response = requests.get("http://www.tudou.com/albumcover/DmU2J6U0P6c.html")
    if response.status_code != 200:
        raise ValueError("Bad request: status_code = {0}".format(response.status_code))
    soup = BeautifulSoup(response.content)
    assert len(soup.fi) == 1
    assert soup.find_all('div', class_='album-pic')[0].find('img')['alt'] == '辣条小说'


# Generated at 2022-06-14 17:22:09.054150
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE().IE_NAME == 'tudou:playlist'
    assert TudouPlaylistIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    t = TudouPlaylistIE()
    assert t._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert t._TESTS[0]['playlist_mincount'] == 209


# Generated at 2022-06-14 17:22:15.368758
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = TudouPlaylistIE._VALID_URL

    # constructor of class InfoExtractor
    # ie = InfoExtractor(url)
    # assert ie._downloader is not None

    # constructor of class YoutubeIE
    ie = TudouPlaylistIE(url)
    assert ie._VALID_URL == url
    #print(ie._TESTS[0])

# Generated at 2022-06-14 17:22:17.554623
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE(InfoExtractor())._real_initialize()
    TudouPlaylistIE(InfoExtractor())._real_extract()



# Generated at 2022-06-14 17:22:22.034036
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    if (ie.check_url('http://www.tudou.com/albumplay/v5qckFJvNJg.html')):
        assert True
    else:
        assert False
        

# Generated at 2022-06-14 17:22:26.024816
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE()
    td_playlist = tudou_playlist.extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert td_playlist['id'] == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:22:38.187103
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Get album id and playlist.
    tudou_album = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert tudou_album._match_id('http://www.tudou.com/albumplay/v5qckFJvNJg.html') == 'v5qckFJvNJg'
    assert tudou_album._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')['_type'] == 'playlist'
    assert tudou_album._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')['id'] == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:22:42.076906
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE._VALID_URL == 'https?://(www\.)?tudou\.com/album(cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:22:50.583108
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:22:55.363725
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    m = TudouPlaylistIE()
    assert(m.IE_NAME == 'tudou:playlist')
    assert(m.IE_DESC == '土豆网 - 专辑/列表')

# Generated at 2022-06-14 17:24:00.540093
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert TudouAlbumIE._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert TudouAlbumIE._TESTS[0]['info_dict'] == {'id': 'v5qckFJvNJg'}

# Generated at 2022-06-14 17:24:08.943101
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TUDOU_PLAYLIST_URL = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou_playlist_ie = TudouPlaylistIE()
    info_dict = tudou_playlist_ie.suitable(TUDOU_PLAYLIST_URL)
    assert info_dict is not None
    tudou_playlist_id = tudou_playlist_ie._match_id(TUDOU_PLAYLIST_URL)
    assert tudou_playlist_id is not None

# Generated at 2022-06-14 17:24:15.624147
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Initialize the instance for testing
    tudouAlbumIE = TudouAlbumIE()

    # Check if url is correctly matched
    url_valid = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    url_valid_bool = tudouAlbumIE._VALID_URL_RE.match(url_valid)
    assert url_valid_bool is not None

    # Example data for input
    input_1 = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'

    # Check if input is properly extracted
    match_id_1 = tudouAlbumIE._match_id(input_1)
    assert match_id_1 is not None
    assert len(match_id_1) == 11



# Generated at 2022-06-14 17:24:19.357928
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    instance = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert instance.IE_NAME is 'tudou:playlist'
    assert instance.playlist_id == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:24:23.258492
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouIE = TudouAlbumIE()
    assert tudouIE.ie_key() == "TudouAlbum"
    assert tudouIE.ie_name() == "Tudou"

# Generated at 2022-06-14 17:24:28.257499
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    td = TudouAlbumIE()
    assert td != None
    assert td._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert td._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]
    assert td._match_id(url) == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:24:33.637137
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE()
    assert tudou_playlist._match_id('http://www.tudou.com/listplay/zzdE77v6Mmo.html') == 'zzdE77v6Mmo'
    assert tudou_playlist._match_id('this is a invalid url') == ''


# Generated at 2022-06-14 17:24:34.598411
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()



# Generated at 2022-06-14 17:24:41.989397
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ins = TudouPlaylistIE()
    assert ins._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ins.IE_NAME == 'tudou:playlist'
    assert ins._TESTS == [{'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html', 'info_dict': {'id': 'zzdE77v6Mmo'}, 'playlist_mincount': 209}]
    assert ins._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html') == True

# Generated at 2022-06-14 17:24:53.151936
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .common import InfoExtractor
    img_url = 'http://g4.tdimg.com/1/337/401/43652342.jpg'
    video_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo/pD1V01UV8Yk.html'
    playlist_id = 'zzdE77v6Mmo'