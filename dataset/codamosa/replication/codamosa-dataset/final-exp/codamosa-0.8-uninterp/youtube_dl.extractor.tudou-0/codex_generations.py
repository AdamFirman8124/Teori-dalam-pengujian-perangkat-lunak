

# Generated at 2022-06-14 17:16:32.084350
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()


# Generated at 2022-06-14 17:16:41.710025
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_url = TudouPlaylistIE._VALID_URL
    playlist_url = playlist_url.replace('listplay', 'listplay/zzdE77v6Mmo.html')
    tudou_playlist_ie = TudouPlaylistIE(playlist_url)
    assert tudou_playlist_ie.IE_NAME == 'tudou:playlist'
    assert tudou_playlist_ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert tudou_playlist_ie._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert tudou_playlist

# Generated at 2022-06-14 17:16:48.475287
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TEST == [{
        'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
        'info_dict': {
            'id': 'v5qckFJvNJg',
        },
        'playlist_mincount': 45,
    }]

# Generated at 2022-06-14 17:16:51.709911
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE(url)


# Generated at 2022-06-14 17:17:00.364205
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist_id = 'zzdE77v6Mmo'
    playlist_data = 'http://www.tudou.com/tvp/plist.action?lcode=%s' % playlist_id
    entry = 'http://www.tudou.com/programs/view/%s'
    tudou_playlist = TudouPlaylistIE()
    play_json = tudou_playlist._download_json(playlist_data, playlist_id)
    mincount = 0
    for item in play_json['items']:
        mincount = mincount + 1
        entries = tudou_playlist.url_result(
                entry % item['icode'],
                'Tudou', item['icode'],
                item['kw'])

# Generated at 2022-06-14 17:17:03.537728
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    result = TudouPlaylistIE(TudouPlaylistIE._downloader)
    result._downloader.urlopen(test_url)
    result._real_extract(test_url)
    result._match_id(test_url)

# Generated at 2022-06-14 17:17:06.649674
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    TudouPlaylistIE(url)

# Generated at 2022-06-14 17:17:15.787752
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

# Generated at 2022-06-14 17:17:23.453652
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .common import FakeHtml
    from .tudou import TudouPlaylistIE
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    # Test for empty page
    page = FakeHtml(url, '<html><head><title>Page not found</title></head><body></body></html>')
    playlist = TudouPlaylistIE()
    assert playlist is not None
    assert playlist._real_extract(page) is None



# Generated at 2022-06-14 17:17:35.720902
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    init_url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html'
    album_id = 'v5qckFJvNJg'
    album_path = 'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id
    album_data = {'items': [
        {'icode': 'v5qckFJvNJg', 'kw': '第16季 第11集'}
    ]}

# Generated at 2022-06-14 17:17:45.598648
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .common import InfoExtractor
    from .tudou import TudouAlbumIE
    
    def test(cls):
        print(cls.__name__)
        ins = cls()
        print(repr(ins.ie_key()))
        print(repr(ins.ie_name()))
        print(repr(ins._VALID_URL))
        print(repr(ins._TESTS))

    test(TudouAlbumIE)
    #test(InfoExtractor) 
    

# Generated at 2022-06-14 17:17:53.142041
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    assert ie._TESTS ==[{'url': 'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
                         'info_dict': {'id': 'v5qckFJvNJg'},
                         'playlist_mincount': 45}]

# Generated at 2022-06-14 17:17:55.454254
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	assert TudouPlaylistIE()



# Generated at 2022-06-14 17:18:05.338223
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print('This is the unit test of TudouPlaylistIE class constructor')

    # Input invalid url
    assert (TudouPlaylistIE._VALID_URL == '')
    print('Invalid Url:')
    result = TudouPlaylistIE._real_extract('http://www.tudou.com/listplay/listplay.html')
    assert (result == False)
    print('    case 1 passed')
    result = TudouPlaylistIE._real_extract('http://www.tudou.com/listplay/listplay/')
    assert (result == False)
    print('    case 2 passed')

    # Input valid url
    print('Valid Url:')

# Generated at 2022-06-14 17:18:14.615122
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    '''
    test_TudouAlbumIE
    '''
    album_id = TudouAlbumIE._match_id(TudouAlbumIE._VALID_URL)
    album_data = TudouAlbumIE._download_json(
        'http://www.tudou.com/tvp/alist.action?acode=%s' % album_id, album_id)
    entries = [TudouAlbumIE.url_result(
        'http://www.tudou.com/programs/view/%s' % item['icode'],
        'Tudou', item['icode'],
        item['kw']) for item in album_data['items']]
    assert len(entries) > 0

# Generated at 2022-06-14 17:18:25.397597
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """
    Example for test, generate asserts.
    """
    import re
    from .common import InfoExtractor
    from .tudou import TudouAlbumIE
    from .youtube import YoutubePlaylistIE, YoutubeIE
    from .vimeo import VimeoIE
    from .brightcove import BrightcoveLegacyIE
    from .common import InfoExtractor, SearchInfoExtractor
    from .zdf import ZDFChannelIE
    from .cbsnews import CBSNewsIE
    from .generic import GenericIE
    from .bollywoodhungama import BollywoodHungamaIE
    from .kankan import KankanIE
    from .tbs import TBSIE
    from .tube8 import Tube8IE
    from .mtv import MTVServicesInfoExtractor
    from .theplatform import ThePlatformIE
    from .pbs import PBSIE


# Generated at 2022-06-14 17:18:29.878130
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    ie = TudouPlaylistIE(use_cformat=False)
    url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
    ext = ie.extract(url)
    assert len(ext) == 1
    assert ext[0]["id"] == "zzdE77v6Mmo"
    assert ext[0]["url"] == url


# Generated at 2022-06-14 17:18:38.930723
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	test_url = "http://www.tudou.com/listplay/zzdE77v6Mmo.html"
	tudou_playlist = TudouPlaylistIE()
	tudou_playlist.extract(test_url)

	assert tudou_playlist.IE_NAME == 'tudou:playlist'
	assert tudou_playlist._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
	assert tudou_playlist._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'

# Generated at 2022-06-14 17:18:41.280792
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlist = TudouPlaylistIE()
    assert playlist.IE_NAME == 'tudou:playlist'



# Generated at 2022-06-14 17:18:42.548458
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	TudouPlaylistIE()


# Generated at 2022-06-14 17:18:51.814248
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    instance = TudouPlaylistIE()
    assert instance.__class__.__name__ == 'TudouPlaylistIE'
    assert instance.IE_NAME == 'tudou:playlist'


# Generated at 2022-06-14 17:19:00.729062
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .common import BaseIE
    from .tudou import TudouAlbumIE
    from .youtube import YoutubePlaylistIE
    from .youtube import YoutubeChannelIE
    from .youtube import YoutubeIE

    # Create a dictionary with few Youtube Playlist object:
    obj_yt_playlist = {
        YoutubePlaylistIE,
        YoutubeChannelIE
    }

    # Create a dictionary with few Youtube object:
    obj_yt = {
        YoutubeIE
    }

    # Create a dictionary with few Youtube object:
    obj_tudou = {
        TudouAlbumIE,
        TudouPlaylistIE
    }

    # Case: Not a Youtube Playlist object.
    assert not (obj_yt_playlist).__contains__(BaseIE)

    # Case: Not a Youtube object.

# Generated at 2022-06-14 17:19:06.810234
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test_TudouPlaylistIE = TudouPlaylistIE()
    assert test_TudouPlaylistIE.IE_NAME == 'tudou:playlist'
    assert test_TudouPlaylistIE._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert len(test_TudouPlaylistIE._TESTS) == 1
    assert test_TudouPlaylistIE._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert test_TudouPlaylistIE._TESTS[0]['info_dict'] == {'id': 'zzdE77v6Mmo'}
   

# Generated at 2022-06-14 17:19:08.733163
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    obj = TudouAlbumIE()
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    assert obj._match_id(url) == 'v5qckFJvNJg'


# Generated at 2022-06-14 17:19:12.732671
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    test = TudouPlaylistIE()
    assert(test.__class__.__name__ == 'TudouPlaylistIE')


# Generated at 2022-06-14 17:19:20.312053
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    t = TudouPlaylistIE()
    assert t.IE_NAME == 'tudou:playlist'
    assert t._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert t._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert t._TESTS[0]['info_dict'] == {'id': 'zzdE77v6Mmo'}
    assert t._TESTS[0]['playlist_mincount'] == 209


# Generated at 2022-06-14 17:19:24.033535
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE('tudou:album')
    assert ie.IE_NAME == 'tudou:album'
    assert ie._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'

# Generated at 2022-06-14 17:19:25.048194
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    TudouPlaylistIE()


# Generated at 2022-06-14 17:19:29.169050
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t = TudouAlbumIE()
    assert t.IE_NAME == 'tudou:album'
    assert t._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'


# Generated at 2022-06-14 17:19:34.873537
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    # Test constructor of class TudouPlaylistIE
    # Create the test url
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    mp2 = TudouPlaylistIE()
    assert(mp2._match_id(url)) == 'zzdE77v6Mmo'


# Generated at 2022-06-14 17:19:50.818187
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    album_url = "http://www.tudou.com/albumcover/v5qckFJvNJg.html"
    test_album_ie = TudouAlbumIE(album_url)
    assert test_album_ie.ie_key() == "TudouAlbum"

# Generated at 2022-06-14 17:20:00.028241
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():

    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    playlistIE = TudouPlaylistIE()
    assert playlistIE._VALID_URL == 'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert playlistIE.IE_NAME == 'tudou:playlist'
    assert playlistIE.report_download_page == 'tudou_listplay_download'
    playlistIE.extract(url)

# Generated at 2022-06-14 17:20:07.750915
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'

# Generated at 2022-06-14 17:20:13.660804
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .test_downloader import Result

    video_link = 'http://www.tudou.com/programs/view/b4J0aWyb5mg/'
    video_title = '【剑侠世界】新手抓虾2'
    video_id = 'b4J0aWyb5mg'
    video_keyword = 'BT'
    playlist_id = 'zzdE77v6Mmo'
    playlist_mincount = 209

    tudou_playlist = TudouPlaylistIE()

    td = {'id': playlist_id}
    td_items = [{'icode': video_id, 'kw': video_keyword}]
    td['items'] = td_items

    info = tudou_playlist._real

# Generated at 2022-06-14 17:20:15.648533
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t=TudouAlbumIE('tudou:album')
    assert t.IE_NAME == 'tudou:album'

# Generated at 2022-06-14 17:20:16.852515
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE("test")

# Generated at 2022-06-14 17:20:17.722731
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    pass


# Generated at 2022-06-14 17:20:24.818874
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    """TudouAlbumIE can create instance as required."""
    assert TudouAlbumIE.ie_key() == 'Tudou:album'
    assert TudouAlbumIE.ie_key(example_url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html') == 'Tudou:album'
    assert TudouAlbumIE.ie_key(example_url = 'http://www.tudou.com/albumcover/v5qckFJvNJg.html') == 'Tudou:album'
    assert not TudouAlbumIE.suitable('http://www.tudou.com/listplay/zzdE77v6Mmo.html')


# Generated at 2022-06-14 17:20:35.470444
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    from .common import mock_urlopen
    from .common import make_new_instance
    import re

    def tudou_mock_urlopen(request):
        return tudou_mock_urlopen.page

    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou_mock_urlopen.page = {'id': 'zzdE77v6Mmo'}
    playlist = make_new_instance(
        TudouPlaylistIE, url, mock_urlopen(tudou_mock_urlopen))

    m = re.search(r'http://www.tudou.com/tvp/plist\.action\?lcode=([\w-]{11})',
        playlist.url)
    assert m != None

# Generated at 2022-06-14 17:20:44.234347
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
	# Test for invalid URLs
	assert TudouPlaylistIE._VALID_URL is not None
	invalid_urls = [
		'http://list.youku.com/show/id_z8e66a0a630311e3ac86.html',
		'http://www.tudou.com/albumplay/v5qckFJvNJg.html',
		'http://www.tudou.com/programs/view/qGZF7iZNJbc/',
		'http://www.tudou.com/plcover/aKjq3rAxGYA/'
	]
	for invalid_url in invalid_urls:
		assert TudouPlaylistIE._WORKING_URL_RE.match(invalid_url) is None

	# Test for valid

# Generated at 2022-06-14 17:21:03.258971
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    import sys
    import os
    import json
    import pytest
    import yaml
    test_cases_file_name = sys.argv[1]
    with open(test_cases_file_name, 'r') as f:
        test_cases = yaml.load(f)
        test_funcs = dict()
        for case in test_cases:
            if case['function'] is not None and case['function'] not in test_funcs:
                test_funcs[case['function']] = list()
                test_funcs[case['function']].append(case)
            elif case['function'] is not None:
                test_funcs[case['function']].append(case)

# Generated at 2022-06-14 17:21:06.161931
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    print(TudouPlaylistIE._VALID_URL)
    print(TudouPlaylistIE._TESTS)


# Generated at 2022-06-14 17:21:17.513156
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    obj = TudouPlaylistIE(id = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert obj.id == 'zzdE77v6Mmo'
    assert obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    assert obj._TESTS[0]['url'] == 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    assert obj._TESTS[0]['info_dict']['id'] == 'zzdE77v6Mmo'
    assert obj._TESTS[0]['playlist_mincount'] == 209


# Generated at 2022-06-14 17:21:22.179608
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    assert TudouPlaylistIE()._VALID_URL == TudouPlaylistIE._VALID_URL
    assert TudouPlaylistIE._TESTS == [{
        'url': 'http://www.tudou.com/listplay/zzdE77v6Mmo.html',
        'info_dict': {
            'id': 'zzdE77v6Mmo',
        },
        'playlist_mincount': 209,
    }]


# Generated at 2022-06-14 17:21:25.336368
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Given
    a = TudouAlbumIE
    # When
    b = TudouAlbumIE()
    # Then
    assert a == verify_object(TudouAlbumIE, b)

# Generated at 2022-06-14 17:21:31.651347
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    t = TudouAlbumIE()
    t = TudouAlbumIE(downloader=None)
    t = TudouAlbumIE(downloader=None, downloader_options=None)
    t = TudouAlbumIE(downloader=None, downloader_options=None, params=None)
    t = TudouAlbumIE(downloader=None, downloader_options=None, params=None, youtube_ie=None)
    t = TudouAlbumIE(downloader=None, downloader_options=None, params=None, youtube_ie=None, ie=None)
    t = TudouAlbumIE(downloader=None, downloader_options=None, params=None, youtube_ie=None, ie=None, ie_key=None)

# Generated at 2022-06-14 17:21:37.969451
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Make sure it can parse standard album link
    TudouAlbumIE()._match_id('http://www.tudou.com/albumcover/v5qckFJvNJg.html')
    # Make sure it can parse album link without cover
    TudouAlbumIE()._match_id('http://www.tudou.com/albumplay/v5qckFJvNJg.html')


# Generated at 2022-06-14 17:21:39.333278
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	tudouAlbumIE = TudouAlbumIE()
	assert tudouAlbumIE

# Generated at 2022-06-14 17:21:42.623221
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """
    Unit test for constructor of class TudouPlaylistIE
    """
    TudouPlaylistIE()


# Generated at 2022-06-14 17:21:47.473969
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
  word = 'python'
  tudou = TudouPlaylistIE(word)
  assert tudou.Playlist_ID is None
  assert tudou.Playlist_lcode is None
  assert tudou.Playlist_URL is None
  assert tudou.Playlist_mincount is 0


# Generated at 2022-06-14 17:22:32.343748
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    
    # init class TudouPlaylistIE
    tudou_playlist_ie = TudouPlaylistIE('test')
    
    # test empty attribute
    assert not tudou_playlist_ie._TESTS



# Generated at 2022-06-14 17:22:40.128414
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from .TudouAlbumIE import TudouAlbumIE
    from .TudouPlaylistIE import TudouPlaylistIE
    from .TudouIE import TudouIE
    from . import compat_urllib_parse

    album_ie = TudouAlbumIE(compat_urllib_parse.quote_plus('http://www.tudou.com/albumplay/v5qckFJvNJg.html'))
    playlist_ie = TudouPlaylistIE(compat_urllib_parse.quote_plus('http://www.tudou.com/listplay/zzdE77v6Mmo.html'))

# Generated at 2022-06-14 17:22:41.485431
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    object = TudouAlbumIE()



# Generated at 2022-06-14 17:22:45.085165
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    try:
        TudouPlaylistIE('www', 'tudou:playlist', 'http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    except:
        assert False


# Generated at 2022-06-14 17:22:52.134279
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    url = "http://www.tudou.com/albumplay/v5qckFJvNJg.html"
    assert TudouAlbumIE._TESTS[0]['url'] == url
    obj = TudouAlbumIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/album(?:cover|play)/(?P<id>[\w-]{11})'
    obj._VALID_URL = r'https?://(?:www\.)?tudou\.com/albumplay/(?P<id>[\w-]{11})'
    assert obj._VALID_URL == r'https?://(?:www\.)?tudou\.com/albumplay/(?P<id>[\w-]{11})'
    assert obj._match_

# Generated at 2022-06-14 17:22:53.761131
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    TudouAlbumIE()

# Generated at 2022-06-14 17:22:57.526786
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    """
    Unit test for constructor of class TudouPlaylistIE
    """
    testIE = TudouPlaylistIE()
    assert testIE.ie_key() == "TudouPlaylistIE"


# Generated at 2022-06-14 17:23:05.439536
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    # Test a special URL:
    # http://www.tudou.com/albumcover/5qckFJvNJg.html
    testurl = 'http://www.tudou.com/albumcover/5qckFJvNJg.html'
    expected = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
    resulturl = TudouAlbumIE._match_id(testurl)
    if resulturl == expected:
        print("success")
    else:
        print("expected: " + expected)
        print("got: " + resulturl)
        print("test failed")

test_TudouAlbumIE()

# Generated at 2022-06-14 17:23:13.407989
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    from . import main
    main({
        'Tudou': {
            'unit_test': {
                'assert': 'TudouAlbumIE.suitable(url)(url)',
                'urls': [
                    # Suitable for TudouAlbumIE
                    'http://www.tudou.com/albumcover/3qM3mgXktDc.html',
                    'http://www.tudou.com/albumplay/3qM3mgXktDc.html',
                ],
                'results': lambda x: '_match_id' in x,
            },
        },
    })



# Generated at 2022-06-14 17:23:16.320309
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    list_url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    tudou = TudouPlaylistIE()
    tudou.initialize()
    tudou._build_url(list_url)
    tudou._download_webpage(list_url)

# Generated at 2022-06-14 17:24:26.895390
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert True

# Generated at 2022-06-14 17:24:30.240853
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
	ie = TudouAlbumIE('http://www.tudou.com/albumcover/xxxxxxx.html')
	assert ie

# Generated at 2022-06-14 17:24:33.582938
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    playlistIE = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert playlistIE.playlist_mincount == 209

# Generated at 2022-06-14 17:24:38.819480
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    f = TudouPlaylistIE('http://www.tudou.com/listplay/zzdE77v6Mmo.html')
    assert f.IE_NAME == 'tudou:playlist'
    assert f._VALID_URL == r'https?://(?:www\.)?tudou\.com/listplay/(?P<id>[\w-]{11})\.html'
    return f


# Generated at 2022-06-14 17:24:39.913060
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    assert(TudouAlbumIE.__name__ == 'TudouAlbumIE')

# Generated at 2022-06-14 17:24:40.739291
# Unit test for constructor of class TudouAlbumIE
def test_TudouAlbumIE():
    ie = TudouAlbumIE()
    assert ie

# Generated at 2022-06-14 17:24:42.226919
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    tudouplaylistie = TudouPlaylistIE()
    assert tudouplaylistie.IE_NAME == 'tudou:playlist'

# Generated at 2022-06-14 17:24:51.183415
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():
    url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    constructor = TudouPlaylistIE(url)
    assert(constructor.url == url)
    assert(constructor.ie == 'Tudou')
    assert(constructor.ext == 'listplay/zzdE77v6Mmo')
    assert(constructor.pkg == 'listplay/zzdE77v6Mmo')
    assert(constructor._type == 'url_transparent')
    assert(constructor.playlist == [])


# Generated at 2022-06-14 17:25:02.111243
# Unit test for constructor of class TudouAlbumIE

# Generated at 2022-06-14 17:25:04.385105
# Unit test for constructor of class TudouPlaylistIE
def test_TudouPlaylistIE():    
    ie = TudouPlaylistIE()
    assert(isinstance(ie, TudouPlaylistIE))
