

# Generated at 2022-06-14 17:16:39.918070
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Ref: http://www.tudou.com/listplay/zzdE77v6Mmo.html
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE._TESTS[0]['url'] = url
    TudouPlaylistIE._TESTS[0]['info_dict'] = {'id': 'zzdE77v6Mmo'}

    # Ref: http://www.tudou.com/listplay/xnCvf8gPsTM.html
    url = 'http://www.tudou.com/listplay/xnCvf8gPsTM.html'

# Generated at 2022-06-14 17:16:42.621986
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    tudou_album = TudouAlbumIE()
    assert tudou_album.suitable(url) == True
    assert tudou_album.extract(url) == True


# Generated at 2022-06-14 17:16:43.756122
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    x = TudouAlbumIE()


# Generated at 2022-06-14 17:16:47.048888
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert 'TudouAlbumIE' in TudouAlbumIE._download_json(url, 'id')



# Generated at 2022-06-14 17:16:49.295259
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    pass

# Generated at 2022-06-14 17:16:52.322991
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    def construct_and_assert(url):
        ie = TudouPlaylistIE(None)
        assert ie.suitable(url)

    construct_and_assert('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:17:00.748505
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:17:11.119826
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._WORKING == True
    assert ie.ie_key() == 'Tudou'
    assert ie.ie_name() == 'tudou:playlist'
    assert ie.info_urls() == ['http://www.tudou.com/listplay/zzdE77v6Mmo.html']
    assert ie.url == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert ie.valid_url() == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert ie

# Generated at 2022-06-14 17:17:14.397818
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():

    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"

    ie = TudouPlaylistIE(url)

    assert ie.test_suite() == True



# Generated at 2022-06-14 17:17:16.462981
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    pass

# Generated at 2022-06-14 17:17:22.179455
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE.suitable(url)
    playlist = TudouPlaylistIE(url)
    playlist.suitable(url)
    playlist.extract(url)


# Generated at 2022-06-14 17:17:26.261716
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Create an instance of class TudouPlaylistIE
    ie_obj = TudouPlaylistIE()
    # Check URL of instance ie_obj
    assert ie_obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

# Generated at 2022-06-14 17:17:27.616893
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:17:36.130278
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    i = TudouPlaylistIE()
    assert i.IE_NAME == 'tudou:playlist'
    assert i._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert i._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert i._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
    assert i._TESTS[0]['playlist_mincount'] == 209


# Generated at 2022-06-14 17:17:41.810528
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# test for download url of class TudouPlaylistIE

# Generated at 2022-06-14 17:17:42.804163
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	obj = TudouAlbumIE()

# Generated at 2022-06-14 17:17:53.063821
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = "v5qckFJvNJg";
    album_data = self._download_json(
        'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)
    entries = [self.url_result(
        'http://www.tudou.com/programs/view/%s' % item['icode'],
        'Tudou', item['icode'],
        item['kw']) for item in album_data['items']]
    return self.playlist_result(entries, album_id)

# Generated at 2022-06-14 17:18:03.306329
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert TudouPlaylistIE().IE_NAME == 'tudou:playlist'
    assert TudouPlaylistIE()._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:18:13.820032
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Futher test for method _real_extract
    from .common import fake_urlopen
    from .common import fake_head
    from .common import fake_data
    from .common import fake_json

    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    _, ext = TudouPlaylistIE._VALID_URL.split('.')
    playlist_id = 'zzdE77v6Mmo'
    request = 'http://www.tudou.com/tvp/plist.action?lcode=zzdE77v6Mmo'

# Generated at 2022-06-14 17:18:16.587876
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album = TudouAlbumIE(None)
    assert tudou_album._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert tudou_album._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg'


# Generated at 2022-06-14 17:18:23.939198
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE()
    assert tudouAlbumIE._VALID_URL is not None

# Generated at 2022-06-14 17:18:28.188189
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    constructor = TudouPlaylistIE
    url = 'http://www.tudou.com/listplay/n0TABtTb0aM.html'
    # test case: constructor, url
    test_case = [constructor,url]
    # test result: playlist_mincount
    test_result = 209
    # Check if test_case[0] and test_case[1] can create expected result
    # test_result
    assert test_case[0]._real_extract(test_case[1])['playlist_len'] >= test_result

# Generated at 2022-06-14 17:18:36.438290
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

# Generated at 2022-06-14 17:18:39.160680
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert ie.IE_NAME == 'tudou:album'
    assert ie.IE_DESC == '土豆 (tudou.com)'



# Generated at 2022-06-14 17:18:48.693773
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouplaylistIE = TudouPlaylistIE()
    assert tudouplaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudouplaylistIE.IE_NAME == 'tudou:playlist'
    assert tudouplaylistIE._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert tudouplaylistIE._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
    assert tudouplaylistIE._TESTS[0]['playlist_mincount'] == 209


# Generated at 2022-06-14 17:18:49.684521
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()


# Generated at 2022-06-14 17:18:53.566865
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_info = 'https://www.tudou.com/listplay/zzdE77v6Mmo.html'
    print(TudouPlaylistIE())
    a = TudouPlaylistIE()
    print(a.extract(test_info))


# Generated at 2022-06-14 17:18:58.829774
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    IE = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert IE.IE_NAME == 'tudou:album'
    assert IE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'


# Generated at 2022-06-14 17:18:59.675889
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	assert TudouPlaylistIE()


# Generated at 2022-06-14 17:19:02.564873
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == "tudou:playlist"
    assert ie._VALID_URL == r"https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html"


# Generated at 2022-06-14 17:19:16.764812
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE(None)

# Generated at 2022-06-14 17:19:18.902708
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """init instance of class TudouPlaylistIE"""
    extractor = TudouPlaylistIE()
    assert extractor.ie_key() == 'Tudou'


# Generated at 2022-06-14 17:19:22.105787
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    inst = TudouPlaylistIE()
    assert inst._match_id(inst._VALID_URL) != None

# Generated at 2022-06-14 17:19:26.422566
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    instance = TudouAlbumIE()
    try:
        assert (instance != None)
    except AssertionError as ae:
        print("Assertion Error: " + ae + " (test_TudouAlbumIE)")


# Generated at 2022-06-14 17:19:27.431901
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE == InfoExtractor

# Generated at 2022-06-14 17:19:31.736404
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:19:42.654708
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert TudouPlaylistIE._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]
    assert TudouPlaylistIE.IE_NAME == 'tudou:playlist'
    assert TudouPlaylistIE.BR_DESC == 'tudou.com'


# Generated at 2022-06-14 17:19:48.817015
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"

    tudou_playlist = TudouPlaylistIE()
    assert tudou_playlist._build_url(url) == url



# Generated at 2022-06-14 17:19:55.946983
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_playlist = TudouAlbumIE('https://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert tudou_playlist.ie_key() == 'TudouAlbum'
    assert tudou_playlist.ie_name() == 'tudou:album'
    assert tudou_playlist._VALID_URL == 'https?://(?:www\\.)?tudou\\.com/album(?:cover|play)/(?P<id>[\\w-]{11})'
    assert tudou_playlist.ie_id() == 'TudouAlbum'

# Generated at 2022-06-14 17:20:01.103559
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE()
    assert ie.suitable(url)
    _list = ie._real_extract(url)
    assert _list['id'] == 'zzdE77v6Mmo'
    

# Generated at 2022-06-14 17:20:37.456324
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE(None)
    assert len(re.findall(r'(http://www\.tudou\.com/tvp/plist\.action\?lcode=\w{11})', ie._download_webpage(ie._VALID_URL, ie._TESTS[0]['url']))) == 1


# Generated at 2022-06-14 17:20:45.844000
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    tudou_album_ie.IE_NAME
    tudou_album_ie.IE_DESC
    tudou_album_ie.IE_VERSION
    tudou_album_ie.VALID_URL
    tudou_album_ie.TEST
    tudou_album_ie._TEST
    tudou_album_ie._TEST_FILE
    tudou_album_ie._WORKING
    tudou_album_ie.BR_DESC
    tudou_album_ie.JP_TOKEN
    tudou_album_ie.config
    tudou_album_ie.report_warning

# Generated at 2022-06-14 17:20:52.276569
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = "_oX4i4nI4m4"
    album_data = "_1VZSd5Yjrc"

    url = "http://www.tudou.com/albumplay/%s.html" % album_id
    info_dict = {
        'id': album_id,
    }


# Generated at 2022-06-14 17:21:02.689198
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # test for initializing an item
    album = TudouAlbumIE()
    album.IE_NAME = 'tudou:album'
    
    # create an object for testing
    test_item = {
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }

    # test if the url is valid
    assert test_item['url'].encode('ascii') == album.suitable(test_item['url'])
    # test if the initializing is successful
    assert album.IE_NAME == 'tudou:album'



# Generated at 2022-06-14 17:21:04.799760
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t = TudouAlbumIE()
    assert(t.name == 'Tudou')

# Generated at 2022-06-14 17:21:13.820919
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test for valid URL
    valid_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    print(TudouPlaylistIE()._real_extract(valid_url))
    print(TudouAlbumIE()._real_extract(valid_url))

    # Test for invalid URL
    invalid_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    print(TudouPlaylistIE()._real_extract(invalid_url))
    print(TudouAlbumIE()._real_extract(invalid_url))


# Generated at 2022-06-14 17:21:15.467880
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    entry = TudouPlaylistIE()
    assert True

# Generated at 2022-06-14 17:21:20.181248
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('TudouAlbumIE','album','http://www.tudou.com/albumplay/v5qckFJvNJg.html','v5qckFJvNJg',{},None,None)

# Generated at 2022-06-14 17:21:27.631992
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_albumIE = TudouAlbumIE()
    assert tudou_albumIE.ie_key() == 'TudouAlbum'
    assert tudou_albumIE.ie_name() == 'tudou:album'
    assert tudou_albumIE.valid_url('http://www.tudou.com/albumcover/v5qckFJvNJg.html', 'TudouAlbum')
    assert tudou_albumIE.valid_url('http://www.tudou.com/albumplay/v5qckFJvNJg.html', 'TudouAlbum')


# Generated at 2022-06-14 17:21:32.993359
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():

    # Check for the output of playlist result
    assert 'tudou:playlist' == TudouPlaylistIE()._VALID_URL
    # Check for the result playlist
    assert [{'id': 'zzdE77v6Mmo'}] == TudouPlaylistIE()._TESTS
    # Check for the output of playlist result
    assert 'TudouAlbumIE' == TudouAlbumIE()._VALID_URL
    # Check for the result playlist
    assert [{'id': 'v5qckFJvNJg'}] == TudouAlbumIE()._TESTS   

    # Check for the output of playlist id

# Generated at 2022-06-14 17:22:50.363929
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .TudouAlbumIE import TudouAlbumIE
    #url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    url = "http://www.tudou.com/albumcover/v5qckFJvNJg.html"
    tudou_album_ie = TudouAlbumIE(url)

    #print tudou_album_ie.ie_name
    #print tudou_album_ie._VALID_URL
    #print tudou_album_ie._TESTS

    assert tudou_album_ie.ie_name == 'TudouAlbum'

# Generated at 2022-06-14 17:22:51.296443
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:22:52.276976
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    return TudouAlbumIE()


# Generated at 2022-06-14 17:22:55.597167
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE(_VALID_URL, _download_webpage)


# Generated at 2022-06-14 17:23:04.864568
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Create test cases
    print("Testing TudouPlaylistIE constructor...")
    # Given the url and _TEST values, a new instance of InfoExtractor is created
    ie = TudouPlaylistIE(True)
    ie._TESTS = [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]
    # The _TESTS is a list of dictionaries, each dictionary contains the 'url',
    # 'info_dict' and 'playlist_mincount'
    test_cases = ie._TESTS

# Generated at 2022-06-14 17:23:10.230989
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    constructor_object = TudouAlbumIE('TudouAlbumIE', 'http://www.tudou.com/albumplay/v5qckFJvNJg.html', 'TudouAlbumIE')
    assert constructor_object.__class__.__name__ == 'TudouAlbumIE'


# Generated at 2022-06-14 17:23:17.081367
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:23:22.232471
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .tudou import TudouAlbumIE
    ie = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:23:26.997475
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE('www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert tudou_playlist == 'Tudou Playlist zzdE77v6Mmo [tudou:playlist:zzdE77v6Mmo]'



# Generated at 2022-06-14 17:23:32.462303
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou_playlist_ie = TudouPlaylistIE(TudouPlaylistIE.ie_key(), url)
    result = tudou_playlist_ie._real_extract(url)

# Generated at 2022-06-14 17:26:03.981875
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    try:
        TudouAlbumIE(None)
        raise "Failed to encounter exception"
    except TypeError:
        assert True, "Failed to encounter exception"


# Generated at 2022-06-14 17:26:11.963054
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .TudouAlbumIE import TudouAlbumIE
    from .TudouIE import TudouIE
    assert TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert TudouAlbumIE.IE_NAME == 'tudou:album'
    

# Generated at 2022-06-14 17:26:18.105883
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_ie = TudouPlaylistIE()
    playlist_ie._match_id( 'http://www.tudou.com/listplay/YtMHq3tTnwI.html' )
    playlist_ie._real_extract('http://www.tudou.com/listplay/YtMHq3tTnwI.html')


# Generated at 2022-06-14 17:26:29.704474
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
	expected_result = "zzdE77v6Mmo"
	correct = td_playlistIE = TudouPlaylistIE(url)
	assert td_playlistIE.url == url, 'Expected url is %s, but get %s' % (url, td_playlistIE.url)
	assert td_playlistIE.name == "TudouPlaylistIE", 'Expected name is TudouPlaylistIE, but get %s' % td_playlistIE.name
	assert td_playlistIE.id == expected_result, 'Expected id is %s, but get %s' % (expected_result, td_playlistIE.id)
