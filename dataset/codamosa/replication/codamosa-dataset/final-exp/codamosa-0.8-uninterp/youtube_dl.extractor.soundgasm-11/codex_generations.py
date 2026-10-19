

# Generated at 2022-06-14 16:55:33.338772
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

test_SoundgasmIE()

# Generated at 2022-06-14 16:55:36.247504
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from .common import expectedFailure

    with expectedFailure(AssertionError, 'Unsupported URL'):
        SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample/')

# Generated at 2022-06-14 16:55:37.561685
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    obj = SoundgasmProfileIE()
    print(obj)


# Generated at 2022-06-14 16:55:43.069339
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	# Valid url
	url = 'http://soundgasm.net/u/ytdl/Piano-sample'
	assert SoundgasmIE().suitable(url), 'Invalid url: %s' % url

	# Incomplete urls
	url = 'http://soundgasm.net/'
	assert not SoundgasmIE().suitable(url), 'Invalid url: %s' % url


# Generated at 2022-06-14 16:55:45.178787
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Test SoundgasmProfileIE constructor
    SoundgasmProfileIE()
    SoundgasmProfileIE("soundgasm:profile")
    SoundgasmIE("soundgasm")

# Generated at 2022-06-14 16:55:53.709608
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert(SoundgasmProfileIE.IE_NAME == 'soundgasm:profile')
    assert(SoundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')
    assert(SoundgasmProfileIE._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    })

# Generated at 2022-06-14 16:55:54.933838
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Constructor of InfoExtractor
    SoundgasmProfileIE(InfoExtractor())


# Generated at 2022-06-14 16:55:56.846142
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    SoundgasmIE()._real_initialize() 
    ie = SoundgasmIE()._real_extract(url)

# Generated at 2022-06-14 16:56:08.203829
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    print(test)
    assert test == {'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9', 'display_id': 'Piano-sample', 'url': 'http://soundgasm.net/media/soundgasm/201605/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a', 'vcodec': 'none', 'title': 'Piano sample', 'description': 'Royalty Free Sample Music', 'uploader': 'ytdl'}

# Generated at 2022-06-14 16:56:09.312931
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE('Soundgasm:profile')

# Generated at 2022-06-14 16:56:15.890116
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Create object.
    instance = SoundgasmProfileIE()



# Generated at 2022-06-14 16:56:25.804576
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    ie.url = "http://soundgasm.net/u/ytdl"
    ie.downloader = ""
    data = ie._real_extract("http://soundgasm.net/u/ytdl")
    expected_data = {
        'id': "ytdl",
        'display_id': 'ytdl',
        'url': "http://soundgasm.net/u/ytdl/Piano-sample",
        'vcodec': 'none',
        'title': "Piano sample",
        'description': "Royalty Free Sample Music",
        'uploader': "ytdl"
    }
    if data['entries'][0] != expected_data:
        raise Exception("Test of constructor of class SoundgasmProfileIE failed")

#

# Generated at 2022-06-14 16:56:30.923676
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from soundgasmIE import SoundgasmIE

    expected_regex = r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

    assert SoundgasmIE._VALID_URL == expected_regex

# Generated at 2022-06-14 16:56:32.633966
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	assert SoundgasmIE()._VALID_URL == SoundgasmIE._VALID_URL

# Generated at 2022-06-14 16:56:40.233499
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sg = SoundgasmIE()
    assert sg.IE_NAME == 'soundgasm'
    assert sg._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:56:46.083730
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    user_name = 'user'
    profile_url = 'https://soundgasm.net/u/' + user_name
    e = SoundgasmProfileIE()
    e._call_download_webpage_handle = lambda url, _: url

    playlist_urls = e._real_extract(profile_url)['entries']
    assert len(playlist_urls) != 0
    for url in playlist_urls:
        assert user_name in url

# Generated at 2022-06-14 16:56:57.387518
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE(None)
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:57:04.404173
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    i = SoundgasmIE()
    i.url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    i.display_id = 'Piano-sample'
    i.title = 'Piano sample'
    i.description = 'Royalty Free Sample Music'
    i.uploader = 'ytdl'
    i.audio_url = 'http://audio.soundgasm.net/u/ytdl/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a'
    i.audio_id = '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    return i.url, i.display_id, i.title, i.description, i.uploader, i.audio_url

# Generated at 2022-06-14 16:57:07.014590
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl")


# Generated at 2022-06-14 16:57:09.041283
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")

# Generated at 2022-06-14 16:57:24.004249
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    for cls in [SoundgasmIE, SoundgasmProfileIE]:
        # Note: "extractor.SoundgasmIE" and "extractor.SoundgasmIE._download_webpage"
        #       do not exist in real life, they are mocks.
        extractor = cls(cls._downloader, cls._download_webpage)
        # Note: this is not the real url.
        url = 'http://soundgasm.net/u/ytdl/Piano-sample'
        # Note: "extractor.SoundgasmIE._match_id" does not exist in real life
        assert cls._match_id(url) == 'ytdl'
        # Note: "extractor.SoundgasmIE._real_extract" does not exist in real life
        info_dict = extractor._real_ext

# Generated at 2022-06-14 16:57:26.053440
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE(None).IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:57:34.174548
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    obj = SoundgasmProfileIE('ytdl')
    assert obj._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert obj._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }


# Generated at 2022-06-14 16:57:37.688922
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile = SoundgasmProfileIE()
    assert profile._VALID_URL == SoundgasmProfileIE._VALID_URL
    assert profile.IE_NAME == SoundgasmProfileIE.IE_NAME

# Generated at 2022-06-14 16:57:46.267288
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from .utils import get_testdata_video_url
    from .utils import fake_urlopen
    from .utils import unittest
    from .utils import MockUrlRequest

    # The response for this URL contains the video ID which will be used in
    # test_playlist_result()
    video_url = get_testdata_video_url("soundgasmie-home")

    # Getting playlist information from home page
    # https://soundgasm.net/
    req_mock = MockUrlRequest("https://soundgasm.net/", video_url)
    with fake_urlopen(req_mock) as f:
        page_content = f.read()

    # Getting playlist information from users page
    # https://soundgasm.net/u/lautsprecher

# Generated at 2022-06-14 16:57:57.585210
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE.IE_NAME = 'yt-dl.org/test_constructor'

    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

    # Test with correct URL
    ie._VALID_URL = ie._VALID_URL.replace('soundgasm.net', '\\soundgasm\\.net')
    url = 'http://soundgasm.net/u/ytdl'
    assert ie.suitable(url) == True
    assert ie.IE_NAME == 'yt-dl.org/test_constructor'
    assert ie._real_extract(url)['id'] == 'ytdl'
    assert ie._real

# Generated at 2022-06-14 16:57:58.682951
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE()

# Generated at 2022-06-14 16:57:59.815388
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE = end_test()


# Generated at 2022-06-14 16:58:03.559799
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    print ("Correctly created SoundgasmProfileIE")

if __name__ == '__main__':
    test_SoundgasmProfileIE()

# Generated at 2022-06-14 16:58:09.277878
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """
    Should construct an instance of SoundgasmProfileIE
    """
    soundgasm = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    assert soundgasm.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:58:27.396746
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	profile = SoundgasmProfileIE()
	assert isinstance(profile, SoundgasmProfileIE)

# Generated at 2022-06-14 16:58:31.113152
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()

    # Test the constructor of class SoundgasmIE
    assert ie.ie_key() == 'Soundgasm'
    assert ie.ie_name() == 'Soundgasm'
    assert ie.test()

# Generated at 2022-06-14 16:58:39.802981
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # SoundgasmIE(url, ie_key, video_id, video_url, video_title, video_description, video_uploader)
    # ie.download_webpage(url, video_id)
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    ie = SoundgasmIE(url, 'Soundgasm', '88abd86ea000cafe98f96321b23cc1206cbcbcc9', 'http://soundgasm.net/u/ytdl/Piano-sample.m4a', 'Piano sample', 'Royalty Free Sample Music', 'ytdl')
    webpage = ie.download_webpage(url, '88abd86ea000cafe98f96321b23cc1206cbcbcc9')
    assert webpage is not None

# Generated at 2022-06-14 16:58:44.624321
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == (
        'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')

# Generated at 2022-06-14 16:58:47.060987
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert(ie.IE_NAME == 'soundgasm:profile')


# Generated at 2022-06-14 16:58:48.873091
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test_Soundgasm_object=SoundgasmIE()
    assert test_Soundgasm_object is not None

# Generated at 2022-06-14 16:59:00.325893
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    '''Unit test for constructor of class SoundgasmProfileIE'''

# Generated at 2022-06-14 16:59:02.212865
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')


# Generated at 2022-06-14 16:59:10.467951
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:59:15.737590
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE(SoundgasmProfileIE._create_get_info())

    assert ie._TEST.get('url') == ie._VALID_URL
    assert ie._TEST.get('info_dict').get('id') == ie._VALID_URL.split('/')[-2]

# Generated at 2022-06-14 16:59:50.443167
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE.__new__(SoundgasmIE)
    print(obj.IE_NAME)


# Generated at 2022-06-14 17:00:00.802385
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl/', 'http://soundgasm.net/u/ytdl/')
    assert ie.url == 'http://soundgasm.net/u/ytdl/'
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl/', 'h://soundgasm.net/u/ytdl/')
    assert ie.url == 'http://soundgasm.net/u/ytdl/'
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl/', '://soundgasm.net/u/ytdl/')

# Generated at 2022-06-14 17:00:03.819550
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Tests for constructor of SoundgasmIE.
    # TODO
    assert 0

# Generated at 2022-06-14 17:00:12.931750
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	url = "http://soundgasm.net/u/ytdl/Piano-sample"
	valid_url = True

	# Check if URL is valid
	mobj = re.match(SoundgasmIE._VALID_URL, url)
	if mobj is None:
		valid_url = False
	else:
		display_id = mobj.group('display_id')
	
	# Download webpage
	if valid_url:
		webpage = SoundgasmIE._download_webpage(url, display_id)

# Generated at 2022-06-14 17:00:14.485568
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE(InfoExtractor()).IE_NAME == 'soundgasm'

# Generated at 2022-06-14 17:00:17.050336
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE()._real_initialize()
    except AttributeError:
        return False
    except:
        pass
    return True


# Generated at 2022-06-14 17:00:20.589225
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	profile_ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
	assert profile_ie.ie_key() == 'Soundgasm'
	assert profile_ie.ie_name() == 'Soundgasm'

# Generated at 2022-06-14 17:00:23.985293
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    import unittest
    from youtube_dl.extractor.soundgasm import SoundgasmIE

    class TestSoundgasmIE(unittest.TestCase):
        def setUp(self):
            self.ie = SoundgasmIE("")

    unittest.main()

# Generated at 2022-06-14 17:00:32.133000
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    d = SoundgasmIE()
    assert d.IE_NAME == 'soundgasm'
    assert d.IE_DESC == 'soundgasm.net'
    assert d._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 17:00:39.140083
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url='http://soundgasm.net/u/ytdl/Piano-sample'
    obj=SoundgasmIE()
    assert obj.IE_NAME=='soundgasm'
    assert obj.get_filename('http://soundgasm.net/u/ytdl/Piano-sample')=='88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a'

# Generated at 2022-06-14 17:02:10.409155
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 17:02:20.169864
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """Test SoundgasmIE"""
    # test_url = "http://soundgasm.net/u/ytdl/Piano-sample"
    # TEST = {'url' : '',
    #         'md5' : '010082a2c802c5275bb00030743e75ad',
    #         'info_dict': {'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9',
    #                       'ext': 'm4a',
    #                       'title' : 'Piano sample',
    #                       'description' : 'Royalty Free Sample Music',
    #                       'uploader' : 'ytdl'}
    #         }
    # Test the constructor.
    ie_object = SoundgasmIE()
    # Test the match function.
   

# Generated at 2022-06-14 17:02:21.698963
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    x = SoundgasmProfileIE()
    assert x is not None

# Generated at 2022-06-14 17:02:29.533417
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """Testing Soundgasm constructor"""
    # Constructor test
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    s = SoundgasmIE()
    # Checking if class SoundgasmIE can access to download_webpage function
    assert s.download_webpage != None

    # Checking if URL variable was properly assigned
    assert s._VALID_URL == SoundgasmIE._VALID_URL

    # Checking if working function works properly
    assert s.working() == True


# Generated at 2022-06-14 17:02:30.510629
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE()._VALID_URL

# Generated at 2022-06-14 17:02:31.369847
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE(None)

# Generated at 2022-06-14 17:02:36.196321
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	c = SoundgasmProfileIE()
	assert c.IE_NAME=='soundgasm:profile'
	assert c._VALID_URL==r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 17:02:44.380034
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """
    Unit test for constructor of class SoundgasmProfileIE
    """
    # pylint: disable=line-too-long
    test_url = 'http://soundgasm.net/u/ytdl'
    ie = SoundgasmProfileIE(test_url)
    # pylint: enable=line-too-long
    assert ie.url == test_url
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie.VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 17:02:47.240973
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    obj = ie.suitable('https://soundgasm.net/u/ytdl/Piano-sample')
    assert obj == True

# Generated at 2022-06-14 17:02:53.571471
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie.suitable('http://soundgasm.net/u/ytdl/Piano-sample')
    assert not ie.suitable('http://soundgasm.net/u/ytdl/')
    assert not ie.suitable('http://soundgasm.net/channel/ytdl/')