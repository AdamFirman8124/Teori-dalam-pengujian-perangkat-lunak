

# Generated at 2022-06-14 17:16:35.364033
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """test template of class constructor"""
    # You can not create an instance of abstract class
    IE_NAME = 'TudouPlaylistIE'
    ie = InfoExtractor(IE_NAME)
    if ie is None:
        print("TudouPlaylistIE can not be instance") 


# Generated at 2022-06-14 17:16:36.481451
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    return ie

# Generated at 2022-06-14 17:16:41.477346
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test constructor of class TudouAlbumIE
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudou_album_ie.IE_NAME == 'TudouAlbumIE'


# Generated at 2022-06-14 17:16:42.283040
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    return TudouAlbumIE()

# Generated at 2022-06-14 17:16:42.900555
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE

# Generated at 2022-06-14 17:16:44.857426
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    instance = TudouAlbumIE()
    print(instance)
    assert True


# Generated at 2022-06-14 17:16:45.942279
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()

# Generated at 2022-06-14 17:16:52.026197
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	import re
	
	albumIE = TudouAlbumIE(None, re.compile('https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'), 'TudouAlbumIE')
	assert albumIE is not None
    

# Generated at 2022-06-14 17:16:58.425013
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(url)

    assert ie.ie_name == 'tudou:playlist'
    assert ie.url == url
    assert ie.valid_url == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert ie.valid_id == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:17:08.513846
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Unit test for constructor by passing the wrong url
    wrong_url = 'http://www.tudou.com/listplay/fadsgfdgdasgd.html'
    ie = TudouPlaylistIE()
    if not ie.suitable(wrong_url):
        print('Pass the wrong url test!')

    # Unit test for constructor by passing the correct url
    correct_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE(correct_url)
    if ie.suitable(correct_url):
        print('Pass the correct url test!')

test_TudouPlaylistIE()

# Generated at 2022-06-14 17:17:24.788619
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # check attributes of instance created by constructor.
    url = u'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    ie = TudouPlaylistIE()
    assert ie.IE_NAME == 'tudou:playlist'
    assert ie.VALID_URL == url
    assert ie._TESTS[0]['url'] == url
    assert ie._TESTS[0]['info_dict']['id'] == u'zzdE77v6Mmo'
    assert ie._TESTS[0]['playlist_mincount'] == 209


# Generated at 2022-06-14 17:17:35.795309
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .common import assertHttpRequests
    # Test for videos (exists)

# Generated at 2022-06-14 17:17:41.493881
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou_playlist_ie = TudouPlaylistIE(downloader=None)
    assert tudou_playlist_ie.suitable(url)
    assert tudou_playlist_ie._real_extract(url)


# Generated at 2022-06-14 17:17:49.117095
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    module = __import__('youtube_dl.extractor.tudou')
    tudoualbum = module.TudouAlbumIE()
    assert tudoualbum.IE_NAME == 'tudou:album'
    assert tudoualbum._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudoualbum._TESTS == [{'info_dict': {'id': 'v5qckFJvNJg'},
                                 'playlist_mincount': 45,
                                 'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'}]

# Generated at 2022-06-14 17:17:50.307734
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()

# Generated at 2022-06-14 17:17:53.143633
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE(url=None,
                         params={'lcode': 'zzdE77v6Mmo'})

    print(ie._VALID_URL)


# Generated at 2022-06-14 17:17:55.883085
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	x = TudouPlaylistIE()
	print(x)


# Generated at 2022-06-14 17:17:58.316330
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    assert ie.ie_key() == 'Tudou'


# Generated at 2022-06-14 17:18:05.546595
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url1 = 'http://www.tudou.com/albumcover/KlVH0nla-BA.html'
    url2 = 'http://www.tudou.com/albumplay/KlVH0nla-BA.html'
    assert TudouAlbumIE._real_extract(TudouAlbumIE(), url1)
    assert TudouAlbumIE._real_extract(TudouAlbumIE(), url2)

# Generated at 2022-06-14 17:18:08.300518
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    a = TudouPlaylistIE()
    a.to_screen(url='http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:18:16.167833
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    i_e = IE()
    assert i_e.get_case_


# Generated at 2022-06-14 17:18:18.743605
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    print('----------test TudouAlbumIE----------')
    IE = TudouAlbumIE()
    assert IE.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:18:22.556052
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():

    class TestExtractor(TudouPlaylistIE):

        def _real_initialize(self):
            self._match_id = lambda x: x

    extractor = TestExtractor('http://www.tudou.com/listplay/zzdE77v6Mmo.html')

# Generated at 2022-06-14 17:18:25.567196
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    test_TudouAlbumIE = TudouAlbumIE('http://www.tudou.com/albumplay/v5qckFJvNJg.html')
    test_TudouAlbumIE.extract()


# Generated at 2022-06-14 17:18:27.625273
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()._real_extract('http://www.tudou.com/albumplay/v5qckFJvNJg.html')

# Generated at 2022-06-14 17:18:29.673486
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE

# Generated at 2022-06-14 17:18:33.148416
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    i = TudouPlaylistIE(None)
    for test in i._TESTS:
        print(test['url'])
        assert i._match_id(test['url']) == 'zzdE77v6Mmo'

# Generated at 2022-06-14 17:18:34.882272
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou_album_ie = TudouAlbumIE()
    assert tudou_album_ie.IE_NAME == "tudou:album"

# Generated at 2022-06-14 17:18:39.134273
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE()
    assert tudouAlbumIE.IE_NAME == 'tudou:album'


# Generated at 2022-06-14 17:18:42.049006
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:19:02.106287
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t = TudouAlbumIE()
    playlist_id = 'v5qckFJvNJg'
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    album_data = t._download_json(
            'http://www.tudou.com/tvp/alist.action?acode=%s' % playlist_id, playlist_id)
    entries = [t.url_result(
            'http://www.tudou.com/programs/view/%s' % item['icode'],
            'Tudou', item['icode'],
            item['kw']) for item in album_data['items']]
    assert t._real_extract(url) == t.playlist_result(entries, playlist_id)

# Generated at 2022-06-14 17:19:12.582030
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    # test _VALID_URL & _TESTS
    assert ie._VALID_URL == TudouPlaylistIE._VALID_URL
    assert ie._TESTS == TudouPlaylistIE._TESTS
    # test name IE_NAME
    assert ie.IE_NAME == TudouPlaylistIE.IE_NAME
    # test _download_webpage
    webpage = ie._download_webpage('http://www.tudou.com/albumplay/v5qckFJvNJg.html', 'album_id')
    assert webpage == ''
    # test _download_json

# Generated at 2022-06-14 17:19:14.981594
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudou_playlist_ie = TudouPlaylistIE()
    assert tudou_playlist_ie.IE_NAME == 'tudou:playlist'


# Generated at 2022-06-14 17:19:17.916598
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:24.067346
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'


# Generated at 2022-06-14 17:19:25.098117
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	from youtube_dl.downloader.common import FileDownloader

# Generated at 2022-06-14 17:19:27.849801
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    a = TudouAlbumIE()
    if a.IE_NAME == 'tudou:album':
    	return True
    return False


# Generated at 2022-06-14 17:19:30.361841
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
  ie = TudouPlaylistIE(TudouPlaylistIE._VALID_URL, 'Tudou', 'tudou:playlist')
  assert ie.name == 'Tudou'


# Generated at 2022-06-14 17:19:31.272432
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	ie = TudouAlbumIE()


# Generated at 2022-06-14 17:19:35.645918
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    func_name = 'test_TudouPlaylistIE'
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE(url)

# Generated at 2022-06-14 17:20:06.348887
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE()
    print('test_TudouPlaylistIE:ie: %s' % ie)
    url = ie.extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    print('test_TudouPlaylistIE:url: %s' % url)
    assert 'http://www.tudou.com/listplay/zzdE77v6Mmo.html' == url


# Generated at 2022-06-14 17:20:08.236123
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE._real_extract("http://www.tudou.com/albumplay/v5qckFJvNJg.html")

# Generated at 2022-06-14 17:20:08.774328
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    pass

# Generated at 2022-06-14 17:20:12.729423
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    TudouPlaylistIE(url)


# Generated at 2022-06-14 17:20:19.227081
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # playing tudou video from playlist by id
    tudou_video_info = {'url':u'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
                        'info_dict':{'id':'zzdE77v6Mmo'},
                        'playlist_mincount':209,
                        }
    ie = InfoExtractor()
    ie_result = ie.extract(tudou_video_info['url'])
    assert(ie_result['_type']=='playlist')


# Generated at 2022-06-14 17:20:24.968916
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    obj = TudouPlaylistIE()
    assert obj.IE_NAME == 'tudou:playlist'
    assert obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert obj._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]

# Generated at 2022-06-14 17:20:34.466570
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Create a test object of class TudouPlaylistIE
    tudou = TudouPlaylistIE()
    # Unit test the _match_id function
    assert tudou._match_id('http://www.tudou.com/listplay/ZZD77v6Mmo.html') == 'zzdE77v6Mmo', '_match_idFunction Error!'
    # Unit test the _real_extract function
    assert tudou._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')['id'] == 'zzdE77v6Mmo', '_real_extractFunction Error!'


# Generated at 2022-06-14 17:20:43.557319
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE()
    assert tudouAlbumIE.IE_NAME == 'tudou:album'
    assert tudouAlbumIE._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert tudouAlbumIE._TESTS[0]['url'] == 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert tudouAlbumIE._TESTS[0]['info_dict']['id'] == 'v5qckFJvNJg'
    assert tudouAlbumIE._TESTS[0]['playlist_mincount'] == 45

#

# Generated at 2022-06-14 17:20:46.892812
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	t = TudouAlbumIE() # Constructor
	assert t._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
	assert t._TESTS[0]['playlist_mincount'] == 45


# Generated at 2022-06-14 17:20:52.231454
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_playlist = TudouPlaylistIE('www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert test_playlist.bookmarks == []
    assert test_playlist._TEMPLATE_URL == 'http://www.tudou.com/listplay/%s.html'
    assert test_playlist._TITLE_RE == r'<title>(?P<title>.*)</title>'
    assert test_playlist._SUFFIX == '.html'

# Generated at 2022-06-14 17:21:53.486656
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('Tudou', 'abc')
    assert(ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})')
    assert(ie.IE_NAME == 'tudou:album')

# Generated at 2022-06-14 17:21:55.308287
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE('v5qckFJvNJg')

# Generated at 2022-06-14 17:21:56.092907
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    i = TudouAlbumIE()

# Generated at 2022-06-14 17:22:00.121183
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	test = TudouPlaylistIE()

# Generated at 2022-06-14 17:22:01.788823
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	tt = TudouAlbumIE()
	assert(tt.IE_NAME == "tudou:album")


# Generated at 2022-06-14 17:22:02.969986
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	tudou_album = TudouAlbumIE()

# Generated at 2022-06-14 17:22:07.056963
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert TudouAlbumIE._VALID_URL == "https?://(?:www\\.)?tudou\.com/album(?:cover|play)/(?P<id>[\\w-]{11})"
    assert TudouAlbumIE._TESTS[0]["url"] == "http://www.tudou.com/albumplay/v5qckFJvNJg.html"


# Generated at 2022-06-14 17:22:11.742636
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    instance = TudouPlaylistIE()
    assert instance.IE_NAME == 'tudou:playlist'
    assert instance._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert instance._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:22:14.901647
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """Test class TudouAlbumIE"""

    instance = TudouAlbumIE()
    assert isinstance(instance, InfoExtractor)



# Generated at 2022-06-14 17:22:15.812349
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    f = TudouAlbumIE()

# Generated at 2022-06-14 17:24:23.960067
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE(TudouAlbumIE._VALID_URL)
    assert ie._VALID_URL == 'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:24:33.729975
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_class = type('TestClass', (object,), {
        'assertEqual': lambda s, a, b: a == b,
        '_match_id': lambda s, a: a[32:43],
    })
    tudouPlaylistIE = TudouPlaylistIE(test_class())
    tudouPlaylistIE._download_json = lambda a, b: {"items": [{"kw": "testkw", "icode": "testicode"}]}
    tudouPlaylistIE._real_extract('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:24:41.898049
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import sys

    if '--list' in sys.argv:
        IE_NAME = 'tudou:playlist'

        import os
        home = os.path.expanduser('~')
        f = open('%s/%s' % (home, 'playlist.txt'), 'w')
        mp3 = 'http://www.tudou.com/listplay/-aLcjseHk-4.html'
        mp4 = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
        mp = [
            {'url': mp3, 'only_matching': True},
            {'url': mp4, 'only_matching': True},
        ]
        for i in mp:
            ie = TudouPlaylistIE(i)
            info_

# Generated at 2022-06-14 17:24:46.350725
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudou = TudouAlbumIE()
    assert isinstance(tudou, InfoExtractor)


# Generated at 2022-06-14 17:24:50.378980
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_cases = [
        ('http://www.tudou.com/listplay/zzdE77v6Mmo.html', 'zzdE77v6Mmo'),
    ]
    for tc in test_cases:
        assert tc[1] == TudouPlaylistIE()._match_id(tc[0])


# Generated at 2022-06-14 17:24:56.212695
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	print("Testing TudouPlaylistIE constructor....")
	print("Test should pass...")
	TudouPlaylistIE("https://www.tudou.com/listplay/zzdE77v6Mmo.html")
	print("Test passed")



# Generated at 2022-06-14 17:24:57.854620
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    tudouAlbumIE = TudouAlbumIE()

# Generated at 2022-06-14 17:24:59.122680
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	print("Testing TudouAlbumIE class constructor")
	TudouAlbumIE()
	print("Success")


# Generated at 2022-06-14 17:25:04.922602
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # (None, None, None)
    # (None, 'https://www.tudou.com/listplay/zzdE77v6Mmo.html', None)
    # ('https://www.tudou.com/listplay/zzdE77v6Mmo.html', None, None)
    obj = TudouPlaylistIE(None, 'https://www.tudou.com/listplay/zzdE77v6Mmo.html', None)
    assert obj._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    # ("zzdE77v6Mmo",)
    # ("zzdE77v6Mmo", "zzdE77v6Mmo", "zzdE77

# Generated at 2022-06-14 17:25:08.032280
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
  assert TudouAlbumIE(None, None, None)("http://www.tudou.com/albumplay/v5qckFJvNJg.html") != None
