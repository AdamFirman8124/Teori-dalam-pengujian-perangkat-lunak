

# Generated at 2022-06-14 17:16:32.290855
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	import tudou
	tudou.TudouPlaylistIE('https://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:16:33.446070
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t = TudouAlbumIE()

# Generated at 2022-06-14 17:16:35.193403
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE().IE_NAME == 'tudou:album'


# Generated at 2022-06-14 17:16:43.377692
# Unit test for constructor of class TudouPlaylistIE

# Generated at 2022-06-14 17:16:44.697581
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	from tudou import TudouPlaylistIE
	a = TudouPlaylistIE()
	assert(a is not None)


# Generated at 2022-06-14 17:16:46.554678
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie.__class__.__name__ == 'TudouAlbumIE'

# Generated at 2022-06-14 17:16:48.680329
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE();

# Generated at 2022-06-14 17:16:53.027290
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    Playlist = TudouPlaylistIE(1)
    assert Playlist.url == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert Playlist.playlist_id == 'zzdE77v6Mmo'

# Generated at 2022-06-14 17:16:54.072110
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()



# Generated at 2022-06-14 17:17:00.031263
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    r = TudouPlaylistIE()
    r.extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    r.extract('http://www.tudou.com/listplay/v5qckFJvNJg.html')
    r.extract('http://www.tudou.com/listplay/v5qckFJvNJg.html')
    r.extract('http://www.tudou.com/listplay/v5qckFJvNJg.html')


# Generated at 2022-06-14 17:17:09.085693
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    expected = 3
    actual = 1
    assert(expected == actual)

# Generated at 2022-06-14 17:17:12.110750
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE(url, 'Tudou')


# Generated at 2022-06-14 17:17:15.522601
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    try:
        TudouAlbumIE('Tudou', 'v5qckFJvNJg')
    except AssertionError as e:
        print(e.args[0])
        assert False
    assert True


# Generated at 2022-06-14 17:17:16.959256
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()


# Generated at 2022-06-14 17:17:27.045011
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    playlist_id = '559029'
    album_id = 'XXWjz8tBVLU'
    # [1] Single item

# Generated at 2022-06-14 17:17:36.555330
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'

    # Create the instance of class TudouPlaylistIE
    tudou_playlist_IE = TudouPlaylistIE()

    # Test whether the variables '_VALID_URL' and 'IE_NAME' were assigned correctly
    assert tudou_playlist_IE._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudou_playlist_IE.IE_NAME == 'tudou:playlist'

    # Test the method '_real_extract'
    # Call the method and get the result

# Generated at 2022-06-14 17:17:44.649154
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import sys
    import os.path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from ytdl_server.extractor import tudou as tudou_extract
    
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'

# Generated at 2022-06-14 17:17:49.209339
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist_id = TudouPlaylistIE._match_id(url)
    assert playlist_id == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:17:52.663096
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert(TudouAlbumIE(None)._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')


# Generated at 2022-06-14 17:18:04.711183
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    playlist_id = 'zzdE77v6Mmo'
    playlist_data = 'A dictionary about playlist.'
    entries = [{'url': 'www.baidu.com', 'key': 'one'},
               {'url': 'www.bing.com', 'key': 'two'}]
    playlist_result = {'id': playlist_id, 'entries': entries}
    ie = TudouPlaylistIE()
    ie._download_json = lambda a, b: playlist_data
    ie.url_result = lambda a, b, c, d: {'url': a, 'key': c}
    ie.playlist_result = lambda a, b: {'id': b, 'entries': a}

# Generated at 2022-06-14 17:18:13.201624
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	TudouPlaylistIE()


# Generated at 2022-06-14 17:18:22.808137
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = 'v5qckFJvNJg'
    url = 'http://www.tudou.com/albumplay/' + album_id +'.html'

# Generated at 2022-06-14 17:18:31.871383
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
    return True

# Generated at 2022-06-14 17:18:39.557776
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print("Testing constructor of class TudouPlaylistIE")
    tpi = TudouPlaylistIE("")
    if (not tpi._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'):
        print("Test failed.")
        print("  Expected: http://www.tudou.com/listplay/zzdE77v6Mmo.html")
        print("  Actual: " + tpi._TESTS[0]['url'])


# Generated at 2022-06-14 17:18:47.897222
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	x = TudouPlaylistIE("zzdE77v6Mmo")
	assert x._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
	assert x._TESTS[0].get("url") == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
	assert x._TESTS[0].get("info_dict").get("id") == 'zzdE77v6Mmo'
	assert x._TESTS[0].get("playlist_mincount") == 209


# Generated at 2022-06-14 17:18:52.165088
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_url='http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    extractor=TudouAlbumIE()

# Generated at 2022-06-14 17:18:56.355066
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	ie = TudouAlbumIE()
	assert ie.IE_NAME == 'tudou:album'
	assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:18:57.297063
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE()

# Generated at 2022-06-14 17:18:59.310119
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:19:00.144067
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()

# Generated at 2022-06-14 17:19:18.566440
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    klass = 'TudouPlaylistIE'
    instance = globals()[klass.replace('IE', '')](url)
    assert instance.__class__.__name__ == klass
    assert instance._VALID_URL == url


# Generated at 2022-06-14 17:19:25.978990
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Some testing urls
    test_urls = [
        {
            'url': 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
        },
        {
            'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
        }
    ]

# Generated at 2022-06-14 17:19:29.698409
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    tudou_playlistIE = TudouPlaylistIE()
    assert tudou_playlistIE._match_id(url) == 'zzdE77v6Mmo'
    assert tudou_playlistIE._real_extract(url) is not None
    assert tudou_playlistIE._real_extract(url)['entries'] is not None

# Generated at 2022-06-14 17:19:40.367604
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    info_dict = {
            'id': 'v5qckFJvNJg',
    }
    playlist_mincount = 45
    tudouAlbumIE = TudouAlbumIE()
    result = tudouAlbumIE._real_extract(url)
    assert result['_type'] == 'playlist', 'it should be playlist'
    assert result['id'] == info_dict['id'], 'the id of playlist should be same as given one'
    assert len(result.get('entries')) == playlist_mincount, 'the number of videos in the playlist should be 45'

# Generated at 2022-06-14 17:19:52.171524
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    cate_Str = "_VALID_URL, _TESTS"
    sep_Str = ": "
    (cate, Str) = cate_Str.split(sep_Str)
    cateDict = eval("dict({})".format(Str.replace(" ", "")))
    assert cate in cateDict
    sep_Str = ": "
    (cate, Str) = cateDict[cate].split(sep_Str)
    assert cate in ["_TESTS", "_VALID_URL"]
    assert Str in ["http://www.tudou.com/listplay/zzdE77v6Mmo.html", "["]

# Generated at 2022-06-14 17:19:55.345128
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert type(TudouPlaylistIE) == type


# Generated at 2022-06-14 17:20:03.943454
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou = TudouAlbumIE()
    assert tudou.IE_NAME == 'tudou:album'
    assert tudou._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudou._TESTS[0] == {'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html', 'info_dict': {'id': 'v5qckFJvNJg'}, 'playlist_mincount': 45}

# Generated at 2022-06-14 17:20:04.807922
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    pass

# Generated at 2022-06-14 17:20:08.769999
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    with TudouPlaylistIE() as test_case:
        test_case.assertEqual(test_case._VALID_URL, test_case._TESTS[0]['url'])


# Generated at 2022-06-14 17:20:13.798800
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert(TudouAlbumIE(TudouAlbumIE.IE_NAME) is not None)
    assert(TudouAlbumIE(TudouAlbumIE.IE_NAME).ie_key() == TudouAlbumIE.IE_NAME)


# Generated at 2022-06-14 17:20:41.359787
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    extractor = TudouAlbumIE()
    assert extractor._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert extractor._TESTS[0] == {'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html', 'info_dict': {'id': 'v5qckFJvNJg'}, 'playlist_mincount': 45}
    assert extractor._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:20:44.592474
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ret = TudouPlaylistIE()
    assert(isinstance(ret, InfoExtractor))


# Generated at 2022-06-14 17:20:49.282333
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert album._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert album.playlist_mincount == 45


# Generated at 2022-06-14 17:20:54.152274
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    ie.extract()

# Generated at 2022-06-14 17:20:55.204149
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()


# Generated at 2022-06-14 17:20:56.466649
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE(None)

# Generated at 2022-06-14 17:21:03.592398
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    
    # Test with a normal video
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    url_test = TudouPlaylistIE(url)

    assert url_test.IE_NAME == TudouPlaylistIE.IE_NAME
    assert url_test._VALID_URL == TudouPlaylistIE._VALID_URL
    assert url_test._TESTS == TudouPlaylistIE._TESTS
    assert url_test._real_extract(url) == 2
    # Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:21:05.410666
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    return TudouPlaylistIE()


# Generated at 2022-06-14 17:21:05.990409
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:21:11.233611
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('http://www.tudou.com/albumcover/v5qckFJvNJg.html')
    assert ie._match_id('http://www.tudou.com/albumplay/v5qckFJvNJg.html') == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:21:46.542585
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album = TudouAlbumIE(downloader=None)



# Generated at 2022-06-14 17:21:47.633014
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	t = TudouAlbumIE()

# Generated at 2022-06-14 17:21:49.822191
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert(TudouAlbumIE(None, {'tudou:album': [{}]}) is not None)

# Generated at 2022-06-14 17:21:52.352338
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    i = TudouPlaylistIE()
    assert i.IE_NAME == 'tudou:playlist'
    assert i._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'


# Generated at 2022-06-14 17:22:01.288477
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    obj = TudouAlbumIE()
    assert obj.suitable(url)

# Generated at 2022-06-14 17:22:07.434646
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # urls = [
    #     'http://www.tudou.com/albumcover/v5qckFJvNJg.html',
    #     'http://www.tudou.com/albumplay/v5qckFJvNJg',
    # ]
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudou_album_ie.IE_NAME == 'tudou:album'
    assert tudou_album_

# Generated at 2022-06-14 17:22:16.917667
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	pl = TudouPlaylistIE()
	assert(pl.IE_NAME == 'tudou:playlist')
	assert('zmnpXlBJWz8' in pl)
	assert(pl.ie_key() == 'tudou')
	assert(pl.valid_url('http://www.tudou.com/listplay/zmnpXlBJWz8.html'))
	assert(pl._match_id('http://www.tudou.com/listplay/zmnpXlBJWz8.html') == 'zmnpXlBJWz8')


# Generated at 2022-06-14 17:22:26.856241
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE(): 
    from .common import InfoExtractor 
    from .tudou import TudouPlaylistIE 
    from .tudou import TudouAlbumIE
    from .tudou import TudouIE
    
    testCase1 = InfoExtractor()
    testCase1.decode_format = lambda s, e: s
    testCase1.url_result = lambda s, e, i, t: s
    testCase1.playlist_result = lambda a, b: a

# Generated at 2022-06-14 17:22:30.615602
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Create an (unused) instance
    album_extractor = TudouAlbumIE(None)
    assert album_extractor is not None

# Generated at 2022-06-14 17:22:39.305685
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert ie._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
    assert ie._TESTS[0]['playlist_mincount'] == 209


# Generated at 2022-06-14 17:23:42.135765
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    instance = TudouAlbumIE()
    assert instance['IE_NAME'] == 'tudou:album'

# Generated at 2022-06-14 17:23:47.947468
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
   args = [
      (TudouAlbumIE(), (TudouAlbumIE.IE_NAME, )),
      (TudouAlbumIE(), (TudouAlbumIE.IE_NAME, TudouAlbumIE._VALID_URL)),
      (TudouAlbumIE(), (TudouAlbumIE.IE_NAME, TudouAlbumIE._TESTS)),
   ]
   for tester in args:
      tester[0].test(tester[1])


# Generated at 2022-06-14 17:23:50.999305
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    TudouAlbumIE()._real_extract(test_url)


# Generated at 2022-06-14 17:23:52.474311
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE(None)



# Generated at 2022-06-14 17:23:56.202888
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouIE = TudouPlaylistIE()
    assert tudouIE.playlist_result is not None and tudouIE.url_result is not None



# Generated at 2022-06-14 17:23:57.475692
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_obj = TudouAlbumIE(None)
    assert test_obj is not None

# Generated at 2022-06-14 17:24:02.637743
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()

    # Test case 1
    sample_url1 = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie.extract(sample_url1)

    # Test case 2
    sample_url2 = 'https://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie.extract(sample_url2)


# Generated at 2022-06-14 17:24:14.210546
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    album_id = ie._match_id(url)
    album_data = ie._download_json(
            'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)
    entries = [ie.url_result(
            'http://www.tudou.com/programs/view/%s' % item['icode'],
            'Tudou', item['icode'],
            item['kw']) for item in album_data['items']]

# Generated at 2022-06-14 17:24:15.850380
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert not hasattr(TudouAlbumIE, '__MODULE__')

# Generated at 2022-06-14 17:24:16.897238
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    pass
