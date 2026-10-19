

# Generated at 2022-06-14 17:16:34.133929
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert tudou.download == tudou.real_download


# Generated at 2022-06-14 17:16:40.755088
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_IE = TudouPlaylistIE()
    print("tudou_playlist_IE = TudouPlaylistIE()")
    assert tudou_playlist_IE
    print("isinstance(tudou_playlist_IE, InfoExtractor) = ", isinstance(tudou_playlist_IE, InfoExtractor))
    print("assert isinstance(tudou_playlist_IE, InfoExtractor)")
    assert isinstance(tudou_playlist_IE, InfoExtractor)
    print("")


# Generated at 2022-06-14 17:16:45.266236
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Arrange
    tudou_playlist_video_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou_playlist_id = 'zzdE77v6Mmo'

    # Action
    tudou_playlist_ie = TudouPlaylistIE(tudou_playlist_video_url, tudou_playlist_id)
    # Assert
    assert tudou_playlist_ie != None

# Generated at 2022-06-14 17:16:48.100669
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Constructor for test
    assert TudouPlaylistIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    

# Generated at 2022-06-14 17:16:58.610538
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # First instance to test constructor of different key words
    test_instance_0 = TudouPlaylistIE()
    assert(test_instance_0._VALID_URL == r'https?://(?:www\.)?tudou\.com/(?:listplay|album(?:cover|play))/(?P<id>[\w-]{11})')
    assert(test_instance_0._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert(test_instance_0._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo')
    assert(test_instance_0._TESTS[0]['playlist_mincount'] == 209)


    # Second instance to test constructor of

# Generated at 2022-06-14 17:17:07.547450
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Given
    expected_IE_NAME = 'tudou:playlist'
    expected_VALID_URL = r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

    # When
    tudouPlaylistIE = TudouPlaylistIE(expected_IE_NAME)

    # Then
    assert tudouPlaylistIE._VALID_URL == expected_VALID_URL
    assert tudouPlaylistIE.IE_NAME == expected_IE_NAME


# Generated at 2022-06-14 17:17:16.238562
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


# Generated at 2022-06-14 17:17:25.094403
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:17:28.175880
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        TudouPlaylistIE()
    except Exception as err:
        assert False, err
    TudouPlaylistIE()

# Generated at 2022-06-14 17:17:29.898457
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()
    pass


# Generated at 2022-06-14 17:17:33.770458
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()

# Generated at 2022-06-14 17:17:45.484844
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    playlist = TudouAlbumIE(TudouAlbumIE._download_xml, 'http://www.tudou.com/albumcover/PLg-Dyjvfmg.html')
    # test for album_id
    assert playlist.album_id == 'PLg-Dyjvfmg'

    xml_data = playlist._download_xml('PLg-Dyjvfmg')
    assert playlist._get_album_title(xml_data) != u'极限挑战之十里追击'

    xml_data = playlist._get_album_data('PLg-Dyjvfmg')
    assert playlist._get_album_title(xml_data) == u'极限挑战之十里追击'



# Generated at 2022-06-14 17:17:49.065479
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE("zzdE77v6Mmo.html")
    assert ie.ie_key() == 'Tudou:playlist'
    assert ie.working_as_expected()



# Generated at 2022-06-14 17:17:52.927372
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = ['http://www.tudou.com/listplay/zzdE77v6Mmo.html']
    obj = TudouPlaylistIE()
    assert(obj._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert(obj._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:18:04.710560
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:18:11.173527
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    # test when input url is valid
    tudou_album_ie.tudou_album_ie._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    # test when input url is invalid
    tudou_album_ie.tudou_album_ie._real_extract('http://www.tudou.com/albumplay/v5qc.html')

# Generated at 2022-06-14 17:18:16.819290
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    x = TudouAlbumIE()
    a = x.extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    print(a)
    assert(isinstance(a, dict) and a['id'] == 'v5qckFJvNJg')


# Generated at 2022-06-14 17:18:27.664371
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    result = TudouPlaylistIE()._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert result['id'] == 'zzdE77v6Mmo'

# Generated at 2022-06-14 17:18:38.328863
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert len(ie._TESTS) == 1
    assert ie._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert len(ie._TESTS[0]['info_dict']) == 1
    assert ie._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
    assert ie._TESTS[0]['playlist_mincount'] == 209

#

# Generated at 2022-06-14 17:18:39.395428
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE([])

# Generated at 2022-06-14 17:18:46.860678
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    try:
        TudouAlbumIE(None,None,None,None,None)
        assert False
    except:
        assert True

# Generated at 2022-06-14 17:18:49.254229
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert (TudouPlaylistIE.__bases__ ==
            (InfoExtractor,))

# Generated at 2022-06-14 17:18:53.086482
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE("tudou:album")
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:18:59.568471
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    test = TudouPlaylistIE()
    test_result = test._real_extract(url)
    expected_result = "zzdE77v6Mmo", "209"
    assert test_result[0] == expected_result[0] and test_result[1]["_type"] == expected_result[1]


# Generated at 2022-06-14 17:19:05.046021
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Invalid URL
    invalid_urls = ['http://tudou.com/listplay/',
                    'http://www.tudou.com/listplay/',
                    'http://www.tudou.com/listplay/some-id']
    for url in invalid_urls:
        try:
            TudouPlaylistIE.from_url(url)
            assert False, "expected ValueError"
        except ValueError:
            pass

    # Valid URL
    valid_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE.from_url(valid_url)



# Generated at 2022-06-14 17:19:10.929105
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert('TudouAlbumIE' == TudouAlbumIE.IE_NAME)
    assert('tudou:album' == TudouAlbumIE.IE_NAME)
    assert(TudouAlbumIE._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    assert(TudouAlbumIE._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert(TudouAlbumIE._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg')

# Generated at 2022-06-14 17:19:15.440740
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE.__name__ == 'TudouAlbumIE'
    assert TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'


# Generated at 2022-06-14 17:19:25.979387
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():

    # test a valid url
    tudou_playlist_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE()
    #test property url
    assert ie.url == tudou_playlist_url
    #test property _VALID_URL
    pattern = re.compile(ie._VALID_URL)
    assert pattern.match(ie._VALID_URL)
    #test property _TESTS
    for test in ie._TESTS:
        assert pattern.match(test['url'])
    #test property _TESTS[0]['info_dict']['id']
    assert ie._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
   

# Generated at 2022-06-14 17:19:30.980015
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tdalbum = TudouAlbumIE(url)
    assert tdalbum.IE_NAME == 'tudou:album'
    assert tdalbum._VALID_URL == r'https?://(?:www\.)?tudou.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:38.258715
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE().IE_NAME == 'tudou:playlist'
    assert TudouPlaylistIE().IE_DESC == '土豆网 - 列表'
    assert TudouPlaylistIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

# Generated at 2022-06-14 17:19:51.132490
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert type(TudouAlbumIE()) == type(TudouPlaylistIE())

# Generated at 2022-06-14 17:19:56.669285
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    for url in (m for m in dir(TudouAlbumIE) if m.startswith('_VALID_URL')):
        for value in getattr(TudouAlbumIE, url):
            print(value)

# Generated at 2022-06-14 17:19:59.323879
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('test')
    ie.url = 'http://www.tudou.com/albumcover/jU2N_hiIy6I.html'

# Generated at 2022-06-14 17:20:02.165415
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    t = TudouPlaylistIE.TudouPlaylistIE(TudouPlaylistIE)
    assert t.name == "tudou:playlist"


# Generated at 2022-06-14 17:20:08.318211
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    tudou_album = TudouAlbumIE(url)
    assert tudou_album._real_extract(url) == tudou_album.playlist_result(tudou_album.entries, "v5qckFJvNJg")

# Generated at 2022-06-14 17:20:13.058588
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE()
    tudouAlbumIE._download_json()
    assert tudouAlbumIE._match_id() is not None
    tudouAlbumIE._real_extract()

# Generated at 2022-06-14 17:20:20.778952
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE.create_from_url('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert(ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html')
    assert(ie._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }])


# Generated at 2022-06-14 17:20:32.648278
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:20:37.503822
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE('tudou.com')
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'



# Generated at 2022-06-14 17:20:39.172447
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .common import InfoExtractor
    test_TudouAlbumIE = InfoExtractor()

# Generated at 2022-06-14 17:21:13.628893
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_ie = TudouPlaylistIE()
    assert tudou_playlist_ie
    assert tudou_playlist_ie.IE_NAME == 'tudou:playlist'
    assert tudou_playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudou_playlist_ie._TESTS == [
        {
            'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
            'info_dict': {
                'id': 'zzdE77v6Mmo'
            },
            'playlist_mincount': 209
        }
    ]

# Generated at 2022-06-14 17:21:22.641733
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # I don't know how to initialize a object by calling __init__
    # So I just call the method of the class to test it
    # I just want to get a object of class TudouAlbumIE
    test_tudou_album_ie = TudouAlbumIE()
    # I don't know how to write a test
    # All I know is if the result is expected, the test is pass
    # The result I get is:
    # {'_type': 'url_transparent',
    # 'id': 'v5qckFJvNJg',
    # 'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
    # 'ie_key': 'TudouAlbum'}
    # and I think it is the expected result
    result = test

# Generated at 2022-06-14 17:21:27.264029
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouPlaylistIE = TudouPlaylistIE('http://www.tudou.com/listplay/l1467ltsf7w.html')
    assert tudouPlaylistIE.IE_NAME == 'tudou:playlist', \
    "TudouPlaylistIE is expected to return tudou:playlist to IE_NAME"



# Generated at 2022-06-14 17:21:31.791345
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert playlist.__class__.__name__ == 'TudouPlaylistIE'
    assert playlist.name == 'tudou:playlist'
    assert playlist.valid_url == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert playlist.url_regex == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:21:38.063572
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	metadata = "id=v5qckFJvNJg, url=http://www.tudou.com/albumplay/v5qckFJvNJg.html"
	i = TudouAlbumIE(metadata)
	assert(i.id == "v5qckFJvNJg")
	assert(i.url == "http://www.tudou.com/albumplay/v5qckFJvNJg.html")

# Generated at 2022-06-14 17:21:42.625330
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE()
    # should not raise error
    test._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:21:43.948272
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE("http://www.tudou.com/listplay/zzdE77v6Mmo.html")


# Generated at 2022-06-14 17:21:45.909518
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    testobj = TudouPlaylistIE();


# Generated at 2022-06-14 17:21:47.024813
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	assert TudouAlbumIE.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:21:51.241531
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # The url is a playlist url.
    url = r'https://www.tudou.com/listplay/zzdE77v6Mmo.html'

# Generated at 2022-06-14 17:23:04.478030
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    i = TudouPlaylistIE('tudou:playlist', 'http://www.tudou.com/listplay/zzdE77v6Mmo.html', 'zh-CN')
    assert i.extract_url == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert i.video_id == 'zzdE77v6Mmo'
    assert i.url == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert i.ie_key() == 'Tudou'
    

# Generated at 2022-06-14 17:23:05.910210
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album = TudouAlbumIE()
    assert tudou_album

# Generated at 2022-06-14 17:23:06.713181
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()

# Generated at 2022-06-14 17:23:09.514506
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie.ie_key() == 'tudou:album'
    assert ie.ie_name() == 'Tudou'



# Generated at 2022-06-14 17:23:10.585200
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:23:21.292116
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    #TODO: Add unit test case
    if False:
        _TESTS = [{
            'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
            'info_dict': {
                'id': 'v5qckFJvNJg',
            },
            'playlist_mincount': 45,
        }]
        album_id = _match_id(url)
        album_data = _download_json(
            'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)

# Generated at 2022-06-14 17:23:26.203056
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import sys, os.path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from tests.test_downloader import TestDownloader
    test = TestDownloader()
    test.test_TudouPlaylistIE()


# Generated at 2022-06-14 17:23:32.497234
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from tudou.extractor import TudouAlbumIE

    assert TudouAlbumIE._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert TudouAlbumIE._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg'
    assert TudouAlbumIE._TESTS[0]['playlist_mincount'] == 45



# Generated at 2022-06-14 17:23:41.433001
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    '''
    Unit test for constructor of class TudouPlaylistIE(InfoExtractor).
    '''
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    u = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    r = u.extract()
    assert r is not None
    assert r['id'] == 'zzdE77v6Mmo'
    assert len(r['entries']) >= 209


# Generated at 2022-06-14 17:23:43.338538
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	tudou = TudouAlbumIE()

# Generated at 2022-06-14 17:26:17.283134
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	test_object = TudouPlaylistIE()
	assert test_object.IE_NAME == 'tudou:playlist'
	assert test_object._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:26:19.711086
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE(TudouAlbumIE.IE_NAME, 'http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:26:31.429464
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import urllib2
    from urlparse import urlparse
    
    def _download_json_old(self, url_or_request, video_id, transform_source=None, fatal=True):
        if isinstance(url_or_request, basestring):
            request = urllib2.Request(url_or_request)
        else:
            request = url_or_request
        request.add_header('User-Agent', self._ua)