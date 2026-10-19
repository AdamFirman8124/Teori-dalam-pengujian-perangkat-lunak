

# Generated at 2022-06-14 17:16:41.061828
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .common import TudouAlbumIE
    from .common import url_result
    from .common import playlist_result
    from .common import InfoExtractor
    from .common import ExtractorError
    from .common import unescapeHTML


    # Constructor of class TudouAlbumIE
    def _real_extract(url):
        from .common import InfoExtractor
        from .common import ExtractorError
        from .common import unescapeHTML

        # match_id

        # assert True

        # assert False

        # assert False

        # assert False

        # assert False

        # assert True
        # assert False
        # assert True
        # assert False
        # assert True
        # assert False
        # assert True
        # assert False
        # assert False
        # assert True
        # assert False
        # assert True
       

# Generated at 2022-06-14 17:16:45.781605
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """Test for constructor of class TudouAlbumIE"""
    print('Running tests for class "TudouAlbumIE"')
    assert (TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')

# Generated at 2022-06-14 17:16:46.246172
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    pass

# Generated at 2022-06-14 17:16:51.243275
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    TudouPlaylistIE(url, "Tudou", "zzdE77v6Mmo", "3-13-1-8")

# Generated at 2022-06-14 17:16:53.549534
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie is not None


# Generated at 2022-06-14 17:16:55.113574
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:16:58.115365
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test = TudouAlbumIE()
    check = test._match_id("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    assert check == 'v5qckFJvNJg'
# End of the test

# Generated at 2022-06-14 17:17:04.594730
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie.IE_NAME == 'tudou:album'
    album_id = ie._match_id("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    assert album_id == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:17:13.411376
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """Unit tests for constructor of class TudouPlaylistIE"""
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie._TESTS == [{'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html', 'info_dict': {'id': 'zzdE77v6Mmo'}, 'playlist_mincount': 209}]

# Generated at 2022-06-14 17:17:20.453876
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert ie._TESTS[0]['info_dict'] == {'id': 'v5qckFJvNJg'}
    assert ie._TESTS[0]['playlist_mincount'] == 45

# Generated at 2022-06-14 17:17:26.466482
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:17:32.333414
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj1 = TudouAlbumIE()
    obj2 = TudouAlbumIE()
    obj1.extract('https://www.tudou.com/albumcover/v5qckFJvNJg.html')
    obj2.extract('https://www.tudou.com/albumcover/v5qckFJvNJg.html')


# Generated at 2022-06-14 17:17:33.278059
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE

# Generated at 2022-06-14 17:17:37.563218
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tpIE = TudouPlaylistIE()
    assert tpIE.IE_NAME in InfoExtractor._available_ies


# Generated at 2022-06-14 17:17:44.674722
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_ie = TudouPlaylistIE()
    assert tudou_ie.IE_NAME == 'tudou:playlist'
    assert tudou_ie.IE_DESC == '土豆 - 发现更大的世界'
    assert tudou_ie.FILE_EXTENSIONS == ['f4v', 'flv', 'mp4', 'mov', 'hlv', 'hdmp4', 'hdflv', 'mts', 'webm']
    assert tudou_ie.IE_KEY == 'Tudou'
    assert tudou_ie.valid_urls == [TudouPlaylistIE._VALID_URL]

# Generated at 2022-06-14 17:17:51.438018
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test for listplay of tudou, session is not None
    tudou_playlist_ie = TudouPlaylistIE()
    # Test for constructor of class TudouPlaylistIE
    assert tudou_playlist_ie.IE_NAME == 'tudou:playlist'
    assert tudou_playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudou_playlist_ie._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'

# Generated at 2022-06-14 17:17:54.974343
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE()
    assert obj is not None

# Generated at 2022-06-14 17:17:55.672870
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert True

# Generated at 2022-06-14 17:18:01.830909
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url='http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    urlIE='tudou:playlist'
    info_dict={'id': u'zzdE77v6Mmo',}
    playlist_mincount=209
    assert TudouPlaylistIE(url,urlIE,info_dict,playlist_mincount)


# Generated at 2022-06-14 17:18:06.356109
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        tudou_playlistIE = TudouPlaylistIE()
    except:
        assert False, 'Constructor of class TudouPlaylistIE should not return exception'


# Generated at 2022-06-14 17:18:22.165651
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # test1: test constructor of class TudouAlbumIE
    ie = TudouAlbumIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie.IE_NAME == 'tudou:album'
    assert ie._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert ie._TESTS[0]['info_dict'] == {'id': 'v5qckFJvNJg'}
    assert ie._TESTS[0]['playlist_mincount'] == 45
    return 0


# Generated at 2022-06-14 17:18:27.669237
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import TudouPlaylistIE

    # This test simply verifies that the class TudouPlaylistIE is defined,
    # and has the expected name, so that the test runner doesn't skip it.
    sample_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    expected_IE_name = 'tudou:playlist'
    test_object = TudouPlaylistIE(sample_url, None)
    assert test_object is not None
    result_IE_name = test_object.IE_NAME
    assert expected_IE_name == result_IE_name
    print('Successfully constructed %s' % result_IE_name)


# Generated at 2022-06-14 17:18:37.819981
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumcover/gblv0AJz2UQ.html'
    ied_info = InfoExtractor.for_site('tudou')._extract_VIDEO_ID_RE.findall(url)[0]
    ied_id = ied_info.split('=')[1]
    ied_cls = type(ied_info.split('=')[0] + 'IE', (InfoExtractor,), {'IE_NAME': 'tudou'})
    ied_instance = ied_cls(ied_id, url)
    ie = TudouAlbumIE(ied_instance)
    assert ie.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:18:47.896357
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    playlist_id = 'v5qckFJvNJg'
    album_id = 'v5qckFJvNJg'
    album_data = {
        'items': [{'icode': 'h0345288kcr', 'kw': ''}, {'icode': 't0345289t7k', 'kw': ''}, {'icode': 'f0345290u4g', 'kw': ''}],
        'total': 45
    }

# Generated at 2022-06-14 17:18:53.325969
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	infoExtractor=InfoExtractor()
	tudouPlaylistIE=infoExtractor.tudou_playlist_ie()
	assert tudouPlaylistIE.ie_name == 'tudou:playlist'
	assert tudouPlaylistIE.valid_url('https://www.tudou.com/listplay/zzdE77v6Mmo.html') 


# Generated at 2022-06-14 17:18:56.024919
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouPlaylistIE = TudouPlaylistIE()

# Generated at 2022-06-14 17:18:59.906604
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou = TudouPlaylistIE()
    assert tudou._match_id(url)
    assert tudou._real_extract(url)
    return


# Generated at 2022-06-14 17:19:00.659893
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	pass


# Generated at 2022-06-14 17:19:03.403658
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.ie_key() == 'tudou:album'
    assert ie.ie_name() == 'tudou:album'
    assert ie.match('http://www.tudou.com/albumcover/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:19:05.194574
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tu = TudouPlaylistIE()
    assert tu._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:19:20.298170
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE.suite()
    pass


# Generated at 2022-06-14 17:19:21.865736
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou = TudouAlbumIE();
    tudou.extract()
    #assert False

# Generated at 2022-06-14 17:19:24.751502
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE("http://www.tudou.com/listplay/zzdE77v6Mmo.html")
    
    

# Generated at 2022-06-14 17:19:28.589770
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    TudouAlbumIE('http://www.tudou.com/albumcover/v5qckFJvNJg.html')


# Generated at 2022-06-14 17:19:30.399014
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('tudou:album')
    assert ie.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:19:32.533975
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    a = TudouPlaylistIE()

# Generated at 2022-06-14 17:19:43.702454
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():

    # create a new TudouAlbumIE object with valid url
    album = TudouAlbumIE('https://www.tudou.com/albumcover/v5qckFJvNJg.html')

    # check if it is the right object
    assert album._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert album._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]


# Generated at 2022-06-14 17:19:48.675500
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist = TudouPlaylistIE()._real_initialize(playlist_url)
    assert playlist != None


# Generated at 2022-06-14 17:19:53.025474
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tudou = TudouAlbumIE()

# Generated at 2022-06-14 17:19:56.664831
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album = TudouAlbumIE('album')
    assert album != None

# Generated at 2022-06-14 17:20:30.850852
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    IE = TudouAlbumIE()
    assert IE.ie_key() == 'TudouAlbum'
    assert IE.ie_name() == 'tudou:album'
    assert IE.ie_type() == 'playlist'


# Generated at 2022-06-14 17:20:32.476702
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test = TudouAlbumIE()
    assert test._TESTS[0]

# Generated at 2022-06-14 17:20:42.998447
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_id = 'zzdE77v6Mmo'
    playlist_data = InfoExtractor._download_json(
        'http://www.tudou.com/tvp/plist.action?lcode=%s' % playlist_id, playlist_id)
    entries = [InfoExtractor.url_result(
        'http://www.tudou.com/programs/view/%s' % item['icode'],
        'Tudou', item['icode'],
        item['kw']) for item in playlist_data['items']]
    playlist = InfoExtractor.playlist_result(entries, playlist_id)

    assert playlist.get('_type') == 'playlist'
    assert playlist.get('id') == playlist_id
    assert playlist.get('entries') == entries

# Generated at 2022-06-14 17:20:46.916525
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	# initialise play list
	url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
	info_dict = {'id':'zzdE77v6Mmo'}
	playlist_mincount = 209
	# create object
	TudouPlaylistIE(url, info_dict, playlist_mincount)


# Generated at 2022-06-14 17:20:51.766965
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    IE_TEST = TudouAlbumIE(InfoExtractor())
    with open('album.html', 'r') as f:
        html = f.read()
    sample_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    sample_IE = IE_TEST.url_result(sample_url, 'Tudou', 'v5qckFJvNJg')
    assert sample_IE._type == 'playlist'
    assert sample_IE._title == '春晚'
    assert sample_IE._id == 'v5qckFJvNJg'
    assert str(sample_IE) == sample_url

# Generated at 2022-06-14 17:21:02.338948
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	# Create an instance of TudouPlaylistIE
	tudou_playlist_ie=TudouPlaylistIE()
	# Test if the corresponding type of IE is TudouPlaylistIE
	assert tudou_playlist_ie._type=="tudou:playlist"
	# Test if the constructor works
	assert tudou_playlist_ie.IE_NAME=="tudou:playlist"
	# Test if the regular expression is right
	assert tudou_playlist_ie._VALID_URL==r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
	# Test if the count of entries is right
	assert len(tudou_playlist_ie._TESTS)==1
	# Test if the count

# Generated at 2022-06-14 17:21:11.757292
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    testUrl = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    testUrl2 = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    IE = TudouAlbumIE()
    assert IE._match_id(testUrl) == IE._match_id(testUrl2)
    # Check if TudouAlbumIE is a subclass of InfoExtractor and if it's the
    # right subclass
    assert isinstance(IE, InfoExtractor) and isinstance(IE, TudouAlbumIE)


# Generated at 2022-06-14 17:21:12.753678
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	pass


# Generated at 2022-06-14 17:21:16.182079
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url='http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    TudouAlbumIE()

# Generated at 2022-06-14 17:21:19.072066
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE("url")
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:22:35.811980
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	from .. import k_before_python2_7_3
	from .. import TudouAlbumIE

	album_id = '6Y0U7Nnf64Q'
	album_data = k_before_python2_7_3._download_json(
		'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)
	assert len(album_data['items']) == 45


# Generated at 2022-06-14 17:22:43.457204
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
        TudouPlaylistIE(url)
        print('constructor of class TudouPlaylistIE passed.')
        return True
    except:
        print('constructor of class TudouPlaylistIE failed.')
        return False


# Generated at 2022-06-14 17:22:51.329433
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():

    file_path = "https://www.tudou.com/albumplay/v5qckFJvNJg.html"

# Generated at 2022-06-14 17:22:55.741017
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    info = TudouPlaylistIE()
    assert info.name == 'tudou:playlist'
    assert info.description == 'tudou.com tv playlist extractor'


# Generated at 2022-06-14 17:22:56.688854
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tu = TudouPlaylistIE()

# Generated at 2022-06-14 17:23:00.291544
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test = TudouAlbumIE()
    assert test._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:23:02.740190
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    return TudouPlaylistIE()._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:23:04.409857
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	TudouAlbumIE(None, None)

# Generated at 2022-06-14 17:23:05.809391
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE()
    test.suite()


# Generated at 2022-06-14 17:23:10.459998
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    i = TudouPlaylistIE()
    assert i.IE_NAME == 'Tudou:playlist'
    assert i._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert i._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]

# Unit testing for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:25:32.470021
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    '''
    Test case for constructor of class TudouAlbumIE
    '''
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie.name == 'tudou:album'
    assert tudou_album_ie.ie_key() == 'TudouAlbum'


# Generated at 2022-06-14 17:25:42.241755
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    a = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    # test _VALID_URL
    assert a._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    # test _TESTS
    assert a._TESTS == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]
    # test _real_extract()
    assert a._real_

# Generated at 2022-06-14 17:25:43.562095
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	assert type(TudouAlbumIE) == type


# Generated at 2022-06-14 17:25:48.276089
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    '''
    test to see whether the URL is matched
    '''
    ie = InfoExtractor('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    if ie.IE_NAME == 'tudou:playlist':
        assert True
    else:
        assert False


# Generated at 2022-06-14 17:25:52.981522
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    info_dict = dict()
    from urllib.parse import urlparse
    url = urlparse(TudouAlbumIE()._VALID_URL)
    info_dict['id'] = url.path.split('/')[-1]
    assert info_dict == TudouAlbumIE()._real_extract(TudouAlbumIE()._VALID_URL)


# Generated at 2022-06-14 17:26:04.630413
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    global album_id
    album_id = 'v5qckFJvNJg'
    album_data = {
        'items': [{'icode': 'paz1l6_8yLM', 'kw': '1'}, {'icode': 'ZoW3qwp3_aU', 'kw': '2'}]
    }

# Generated at 2022-06-14 17:26:09.052314
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album = TudouAlbumIE()

# Generated at 2022-06-14 17:26:20.077732
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE(TudouAlbumIE.ie_key())
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert ie._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg'
    assert ie._TESTS[0]['playlist_mincount'] == 45
    # TODO: Add other fields test


# Generated at 2022-06-14 17:26:29.437822
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE('TudouAlbumIE', 'www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert obj.ie_key() == 'TudouAlbumIE'
    assert obj.ie_name() == 'TudouAlbumIE'
    assert obj.valid_url() == 'www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert obj.extract_id() == 'v5qckFJvNJg'
