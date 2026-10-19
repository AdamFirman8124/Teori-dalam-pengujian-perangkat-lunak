

# Generated at 2022-06-14 17:16:33.917064
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    video_obj = TudouPlaylistIE('Test', 'http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert video_obj != None


# Generated at 2022-06-14 17:16:35.419321
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    IE_NAME = 'TudouPlaylistIE'
    pass

# Generated at 2022-06-14 17:16:37.021691
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE('zzdE77v6Mmo')



# Generated at 2022-06-14 17:16:37.972819
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	tudou_playlist = TudouPlaylistIE()

# Generated at 2022-06-14 17:16:44.042749
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(url)
    assert ie.url, "url can't be None"
    assert ie.url == url


# Generated at 2022-06-14 17:16:52.226411
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """This unit test will most likely fail because the constructor of
    InfoExtractor class (which is parent of TudouAlbumIE) is not thread safe
    and hence the exception must be raised here.
    """
    import threading
    from multiprocessing import Pool
    from functools import partial
    # Create a InfoExtractor object in the main thread
    partial_create = partial(
        InfoExtractor, ie_name="TudouAlbumIE", ie_key="TudouAlbumIE")
    try:
        info_extractor = partial_create()
    except Exception as e:
        raise e
    # create an InfoExtractor object in another thread, this should raise an exception
    def extract(partial_create):
         try:
             partial_create()
         except Exception as e:
             raise e

# Generated at 2022-06-14 17:16:54.541311
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE(None, 'http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:16:56.879166
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # test for normal situation
    TudouAlbumIE()

    # test for TypeError: 'NoneType' object is not iterable
    TudouAlbumIE()

# Generated at 2022-06-14 17:16:59.173671
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
        ae = TudouAlbumIE()
        # Some of the private function are tested already in
        # test_TudouPlaylistIE
        # For the extraction of the video is tested in test_TudouIE.

# Generated at 2022-06-14 17:17:02.194177
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    #This function is used to test the class TudouAlbumIE 
    #print ('unit test!')
    #assert(False)
    assert(test_TudouAlbumIE)

# Generated at 2022-06-14 17:17:06.697505
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    pass


# Generated at 2022-06-14 17:17:10.831785
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    try:
        TudouAlbumIE('TudouAlbumIE','TudouAlbumIE', 'TudouAlbumIE')
        assert True
    except:
        assert False


# Generated at 2022-06-14 17:17:14.479631
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie._match_id('http://www.tudou.com/albumplay/v5qckFJvNJg.html') == 'v5qckFJvNJg'

# Generated at 2022-06-14 17:17:20.634950
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE()
    t = ie.extract(url)
    assert len(ie._extract_playlist(url, 'Tudou')) == 209


# Generated at 2022-06-14 17:17:22.512574
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    playlist = TudouAlbumIE()
    assert_equals(playlist.IE_NAME, 'tudou:album')

# Generated at 2022-06-14 17:17:28.222540
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = r'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist_ie = TudouPlaylistIE(url)
    assert playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert playlist_ie.IE_NAME == 'tudou:playlist'
    assert playlist_ie.playlist_id == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:17:33.235612
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:17:36.161634
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:17:38.661021
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE().set_url('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:17:45.487263
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Given
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    # When
    try:
        tae = TudouAlbumIE()
        tae._real_extract(url)
        actual_result = 'test_TudouAlbumIE_success'
    # Then
    except AssertionError:
        actual_result = 'test_TudouAlbumIE_fail'

    assert actual_result == 'test_TudouAlbumIE_success'


# Generated at 2022-06-14 17:17:53.677987
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE(): 
    TudouPlaylistIE()._get_videos_info_from_url_(url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html")



# Generated at 2022-06-14 17:17:59.050369
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'

# Generated at 2022-06-14 17:18:05.371147
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    T = TudouPlaylistIE()
    assert T._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert T._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:18:08.152947
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    a = TudouPlaylistIE()
    a.extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:18:17.577919
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE(None)
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert(ie._TESTS[0] == 
        {
            'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
            'info_dict': {
                'id': 'zzdE77v6Mmo',
            },
            'playlist_mincount': 209,
        })


# Generated at 2022-06-14 17:18:23.282740
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = "http://www.tudou.com/albumcover/v5qckFJvNJg.html"
    obj = TudouAlbumIE(url)
    # test the first 11 characters of string returned by method _match_id
    assert "v5qckFJvNJg" == obj._match_id(url)[:11]

# Generated at 2022-06-14 17:18:31.172840
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert(TudouPlaylistIE().ie_key() == 'Tudou')
    assert(TudouPlaylistIE().ie_key() == 'tudou')
    assert(TudouPlaylistIE().ie_key() == 'Tudou:playlist')
    assert(TudouPlaylistIE().ie_key() == 'TudouPlaylist')
    assert(TudouPlaylistIE().ie_key() == 'tudou:playlist')
    assert(TudouPlaylistIE().ie_key() == 'tudouplaylist')
    assert(TudouPlaylistIE().ie_key() == 'Tudouplaylist')

    class_name = 'TudouPlaylistIE'

# Generated at 2022-06-14 17:18:36.155683
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    import unittest
    from tudou_albumIE import TudouAlbumIE
    class test_TudouAlbumIE(unittest.TestCase):
        def test_TudouAlbumIE(self):
            url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
            album = TudouAlbumIE(url)
            self.assertEqual(album.id, 'v5qckFJvNJg')
    unittest.main()

# Generated at 2022-06-14 17:18:43.133627
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    test_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    test_obj = ie._real_extract(test_url)
    assert test_obj['id'] == 'v5qckFJvNJg'
    assert len(test_obj['entries']) == 45

# Generated at 2022-06-14 17:18:50.467660
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_id = '6Cvbnoj_hY0'
    album_data = InfoExtractor()._download_json(
        'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)
    entries = [InfoExtractor().url_result(
        'http://www.tudou.com/programs/view/%s' % item['icode'],
        'Tudou', item['icode'],
        item['kw']) for item in album_data['items']]
    playlist = InfoExtractor().playlist_result(entries, album_id)

# Generated at 2022-06-14 17:19:06.733500
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert isinstance(TudouAlbumIE(), InfoExtractor)
    assert TudouAlbumIE().IE_NAME is 'tudou:album'



# Generated at 2022-06-14 17:19:07.755728
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:19:09.477143
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    IE_TEST = TudouPlaylistIE()
    print(IE_TEST._VALID_URL)

# Generated at 2022-06-14 17:19:12.148638
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE()
    pass
test_TudouPlaylistIE()

# Generated at 2022-06-14 17:19:18.718781
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Init
    result = TudouAlbumIE("http://www.tudou.com/albumplay/v5qckFJvNJg.html")
    # Testing for URL
    assert result.URL == "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    # Testing for _VALID_URL
    assert result._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:21.214963
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE()
    print("tudouAlbumIE:",tudouAlbumIE)

if __name__ == "__main__":
    test_TudouAlbumIE()

# Generated at 2022-06-14 17:19:27.191107
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    i = TudouPlaylistIE()

# Generated at 2022-06-14 17:19:32.646161
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE('https://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert ie.ie_key() == 'tudou:playlist'
    assert ie.ie_name() == 'tudou:playlist'
    assert ie.valid_url('https://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert ie.valid_url('https://www.tudou.com/listplay/zzdE77v6Mmo.html', True)
    assert ie.valid_url('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:19:38.658461
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    n = TudouAlbumIE(None)
    assert n.IE_NAME == 'tudou:album'
    assert n._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:50.378234
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	from .common import InfoExtractor
	ie = InfoExtractor()
	# ----------------------------------------------------------------
	# test expected attributes
	tudou_album_ie_obj = ie._ies['tudou:album']
	
	assert tudou_album_ie_obj.IE_NAME == 'tudou:album'
	assert tudou_album_ie_obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:20:20.134157
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	pass



# Generated at 2022-06-14 17:20:26.769755
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_ie = TudouPlaylistIE()
    assert tudou_playlist_ie.IE_NAME == 'tudou:playlist'
    assert tudou_playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert len(tudou_playlist_ie._TESTS) == 1
    assert tudou_playlist_ie._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert tudou_playlist_ie._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
   

# Generated at 2022-06-14 17:20:36.472770
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    info = ie.extract('http://www.tudou.com/tvp/plist.action?lcode=agl4X4JvDMo')
    assert info.get('id') == 'agl4X4JvDMo'

# Generated at 2022-06-14 17:20:45.062933
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE().IE_NAME == 'tudou:playlist'
    assert TudouPlaylistIE()._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert len(TudouPlaylistIE()._TESTS) == 1
    assert TudouPlaylistIE()._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert len(TudouPlaylistIE()._TESTS[0]['info_dict']) == 1
    assert TudouPlaylistIE()._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
   

# Generated at 2022-06-14 17:20:51.365304
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
        id = 'zzdE77v6Mmo'
        info_dict = {'id': 'zzdE77v6Mmo'}
        playlist_mincount = 209
        assert (TudouPlaylistIE._TESTS[0]['url'] == url)
        assert (TudouPlaylistIE._TESTS[0]['info_dict'] == info_dict)
        assert (TudouPlaylistIE._TESTS[0]['playlist_mincount'] == playlist_mincount)
        return True
    except:
        return False


# Generated at 2022-06-14 17:20:53.100934
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert type(TudouAlbumIE(None)) == TudouAlbumIE

# Generated at 2022-06-14 17:20:57.050152
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'


# Generated at 2022-06-14 17:21:05.377046
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlist_ie = TudouPlaylistIE()
    assert playlist_ie.ie_key() == 'tudou:playlist'
    assert playlist_ie.ie_name() == 'tudou:playlist'
    assert playlist_ie.expected_suitable(url) == True
    # test for real_extract
    playlist = playlist_ie._real_extract(url)
    assert playlist['_type'] == 'playlist'
    assert playlist['title'] == 'V系番'
    assert playlist['id'] == 'zzdE77v6Mmo'
    assert len(playlist['entries']) == 209
    program = playlist['entries'][0]

# Generated at 2022-06-14 17:21:13.633999
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	instance = TudouAlbumIE()
	assert instance._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
	assert instance.IE_NAME == 'tudou:album'
	assert instance._TESTS == [{'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html', 'info_dict': {'id': 'v5qckFJvNJg'}, 'playlist_mincount': 45}]

# Generated at 2022-06-14 17:21:22.641311
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE('example.com','http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert [True, True, True] == [ie.ie_key() == 'Tudou', ie.suitable('http://www.tudou.com/listplay/zzdE77v6Mmo.html'), ie.suitable('https://www.tudou.com/listplay/zzdE77v6Mmo.html')]
    assert ie.ie_key() == 'TudouPlaylist'
    assert ie.suitable('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:22:35.217243
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    result = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert result.extractor == 'tudou:album'
    assert result.playlist_mincount == 45

# Generated at 2022-06-14 17:22:47.458005
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE(TudouAlbumIE.ie_key())
    assert(ie.ie_key() == 'Tudou:album')
    assert(ie.IE_NAME == 'tudou:album')
    assert(ie.name() == 'Tudou:album')
    assert(ie.ie() == 'Tudou')
    assert(ie.ie_key() == 'Tudou:album')
    assert(ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    assert(ie._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:22:58.398860
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert(repr(TudouAlbumIE) == 'TudouAlbumIE')
    assert(TudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    assert(TudouAlbumIE.IE_NAME == 'tudou:album')
    assert(TudouAlbumIE._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    assert(TudouAlbumIE._TESTS[0]['info_dict'] == {
            'id': 'v5qckFJvNJg',
    })

# Generated at 2022-06-14 17:23:04.608557
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    obj = TudouPlaylistIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert obj.suitable(url) == True
    assert obj._real_initialize() == None
    #assert obj._download_json() == None


# Generated at 2022-06-14 17:23:05.627475
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	TudouAlbumIE()

# Generated at 2022-06-14 17:23:11.197950
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE();
    assert tudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudouAlbumIE.IE_NAME == 'tudou:album'


# Generated at 2022-06-14 17:23:15.252583
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE()
    assert test is not None


# Generated at 2022-06-14 17:23:17.972358
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_ie = TudouAlbumIE()
    assert_equal(album_ie.ie_key(), 'tudou:album')
    assert_equal(album_ie.ie_name(), 'Tudou')

# Generated at 2022-06-14 17:23:23.028620
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

    assert tudouAlbumIE.ie_key() == 'TudouAlbum'



# Generated at 2022-06-14 17:23:32.727278
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from ..utils import TestIE
    import re
    print("\n==============Unit Test for TudouPlaylistIE=================")
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo/acV7sFnQq3s.html'
    ie = TudouPlaylistIE()
    match = ie._VALID_URL
    m = re.match(match, url)
    if m:
        playlist_id = m.groupdict()['id']
        print("%s: %s" % ('playlist_id', playlist_id))
        # print("%s: %s" % ('whole_url', ie._get_whole_url()))

# Generated at 2022-06-14 17:26:00.720436
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:26:04.072556
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist = TudouPlaylistIE()
    tudou_playlist._real_extract(tudou_playlist._TESTS[0]['url'])


# Generated at 2022-06-14 17:26:11.635160
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """Unit test for constructor of class TudouAlbumIE"""
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    album = TudouAlbumIE(url)
    # It should be accepted
    assert album.is_valid()
    # It should have exactly one entry
    assert len(album.entries)==45


# Generated at 2022-06-14 17:26:18.106849
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    sub_obj_jbk=TudouPlaylistIE()
    sub_obj_load_jbk=sub_obj_jbk._real_extract(url)
    assert  sub_obj_load_jbk['_type']=='playlist'


# Generated at 2022-06-14 17:26:27.275180
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    IE = TudouPlaylistIE("https://www.tudou.com/listplay/zzdE77v6Mmo.html")
    # Test value of parameter url
    url = IE._TESTS[0]['url']
    assert IE.url == url
    # Test value of parameter valid_url
    valid_url = IE._TESTS[0]['valid_url']
    assert IE._VALID_URL == valid_url
    # Test value of parameter ie_key
    ie_key = IE.ie_key()
    assert ie_key == IE.IE_NAME
