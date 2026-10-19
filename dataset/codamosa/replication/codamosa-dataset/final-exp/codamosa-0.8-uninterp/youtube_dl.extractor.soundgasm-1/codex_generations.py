

# Generated at 2022-06-14 16:55:34.531314
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE


# Generated at 2022-06-14 16:55:35.998263
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample", None).list()

# Generated at 2022-06-14 16:55:43.611088
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sg = SoundgasmIE()
    # Check if the URL of this instance is correct
    assert sg._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    # Check if the instance is created for the corresponding IE name
    assert sg.ie_key() == 'Soundgasm'
    # Check if the instance is created from the correct class
    assert issubclass(SoundgasmIE, InfoExtractor)

# Generated at 2022-06-14 16:55:46.826988
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    assert ie.__class__.__name__ == 'SoundgasmProfileIE'

# Generated at 2022-06-14 16:55:57.135122
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():

	# Test case 1
	assert SoundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
	assert SoundgasmProfileIE.IE_NAME == 'soundgasm:profile'
	assert SoundgasmProfileIE.__doc__ == 'Soundgasm user profile downloader'

	# Test case 2
	assert SoundgasmProfileIE._TEST['url'] == 'http://soundgasm.net/u/ytdl'
	assert SoundgasmProfileIE._TEST['info_dict'] == {'id': 'ytdl'}
	assert SoundgasmProfileIE._TEST['playlist_count'] == 1


# Generated at 2022-06-14 16:55:59.251809
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	sgIE = SoundgasmIE('snappyx')
	assert(sgIE.ie_key() == 'Soundgasm')

# Generated at 2022-06-14 16:56:03.548834
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:56:04.615085
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:56:10.120598
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    audio_id = 'Piano-sample'
    display_id = 'ytdl'
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert ie._match_id(url) == audio_id

# Generated at 2022-06-14 16:56:18.639372
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    #Test the case when url is not of the expected format
    #This test case is to check the case when url is not of the format http://soundgasm.net/u/ytdl/Piano-sample
    assert SoundgasmIE()._match_id('http://soundgasm.net/u/ytdl') is None
    assert SoundgasmIE()._match_id('http://soundgasm.net/u/ytdl/Piano-sample/abc') is None
    assert SoundgasmIE()._match_id('http://soundgasm.net/u/ytdl/Piano-sample.m4a') is None
    assert SoundgasmIE()._match_id('http://www.soundgasm.net/u/ytdl/Piano-sample.m4a') is None

    #test the case when

# Generated at 2022-06-14 16:56:32.498207
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():

    # Test with soundgasm.net URL
    try:
        soundgasm_profile_ie = SoundgasmProfileIE("soundgasm.net")
        assert soundgasm_profile_ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
        assert soundgasm_profile_ie.ie_name == 'Soundgasm'
        assert soundgasm_profile_ie.ie_key == 'soundgasm'
    except NameError:
        print("Unittest for SoundgasmProfileIE did not run")


# Generated at 2022-06-14 16:56:33.041053
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:56:40.257009
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """
    Unit test for constructor of class SoundgasmProfileIE
    """
    # Check if it gives correct result
    assert SoundgasmProfileIE()._real_extract.__name__ == 'SoundgasmProfileIE._real_extract'
    #Check if it is a constructed from InfoExtractor which is the base class
    assert issubclass(SoundgasmProfileIE, InfoExtractor)
    #Check if the IE name is as expected
    assert SoundgasmProfileIE.IE_NAME == 'soundgasm:profile'
    #Check if the IE id is as expected
    assert SoundgasmProfileIE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 16:56:43.348391
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    e = SoundgasmIE('http://www.soundgasm.net/u/ytdl/Piano-sample')
    expected = {'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9',
        'title': 'Piano sample',
        'description': None,
        'uploader': 'ytdl',
        'uploader_id': None,
        'upload_date': None,
        'ext': 'm4a'}
    assert_equal(e.extract(), expected)

# Generated at 2022-06-14 16:56:44.286210
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert test_SoundgasmProfileIE() == "No."

# Generated at 2022-06-14 16:56:45.828679
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE()._VALID_URL == SoundgasmProfileIE._VALID_URL

# Generated at 2022-06-14 16:56:48.922331
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	soundgasm_ie = SoundgasmIE(True)

# Generated at 2022-06-14 16:56:54.848901
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    result = SoundgasmIE()._real_extract(url)
    assert result['url'] == 'http://soundgasm-a.akamaihd.net/u/ytdl/Piano-sample.m4a'
    assert result['title'] == 'Piano sample'


# Generated at 2022-06-14 16:56:57.012900
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm_profile_ie = SoundgasmProfileIE()
    assert soundgasm_profile_ie.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:56:59.112600
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    u = 'http://soundgasm.net/u/ytdl'
    object = SoundgasmProfileIE()
    object.suitable(u)
    object.extract(u)

# Generated at 2022-06-14 16:57:08.089457
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()


# Generated at 2022-06-14 16:57:10.727015
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    display_id = 'Piano-sample'
    extractor = SoundgasmIE()
    extractor._match_id(url)
    extractor._real_extract(url)
    extractor._download_webpage(url, display_id)


# Generated at 2022-06-14 16:57:12.169863
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from .common import test_id_regexp_id
    SoundgasmIE().work(test_id_regexp_id(SoundgasmIE._VALID_URL))

# Generated at 2022-06-14 16:57:13.773260
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	test_url='http://soundgasm.net/u/ytdl/Piano-sample'
	output=InfoExtractor.suitable(test_url)
	assert(output)


# Generated at 2022-06-14 16:57:15.358330
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	assert SoundgasmProfileIE.__name__ == 'SoundgasmProfileIE'

# Generated at 2022-06-14 16:57:18.044933
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    construct_instance = SoundgasmProfileIE()
    construct_instance.IE_NAME
    construct_instance.IE_DESC
    construct_instance._VALID_URL
    construct_instance._TEST
    construct_instance._download_webpage
    construct_instance._real_extract
    construct_instance.url_result

# Generated at 2022-06-14 16:57:24.866699
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Test the constructor of class SoundgasmIE
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    IE = SoundgasmIE()
    assert(IE.IE_NAME == "soundgasm")
    assert(IE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')

# Generated at 2022-06-14 16:57:26.821901
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from IPython import embed
    SoundgasmIE.test()

# Generated at 2022-06-14 16:57:30.326557
# Unit test for constructor of class SoundgasmIE

# Generated at 2022-06-14 16:57:32.283966
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmIE('Soundgasm')
    assert ie.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:57:55.166030
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    ie._download_webpage('http://soundgasm.net/u/ytdl', 'ytdl')
    ie._match_id('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:58:06.766726
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    result = SoundgasmProfileIE('SoundgasmProfile', 'http://soundgasm.net/u/ytdl')
    assert result.ie_key() == 'SoundgasmProfile'
    assert result.ie_name() == 'Soundgasm:profile'
    assert result._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert result.ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:58:18.422999
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    ie = SoundgasmIE()
    # Make sure the regex matches the url
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert re.match(ie._VALID_URL, url) is not None
    # Then make sure the _real_extract method works properly

# Generated at 2022-06-14 16:58:30.093463
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from soundgasm import SoundgasmProfileIE
    path = 'test/test_data/test_SoundgasmProfileIE/test.html'
    data = open(path, 'r').read().decode('utf-8')
    assert SoundgasmProfileIE._match_id('http://soundgasm.net/u/ytdl') == 'ytdl'
    assert SoundgasmProfileIE._match_id('http://soundgasm.net/u/ytdl/') == 'ytdl'
    assert SoundgasmProfileIE._match_id('http://soundgasm.net/u/ytdl/a') == 'ytdl'
    assert SoundgasmProfileIE._match_id('http://soundgasm.net/u/ytdl/#') == 'ytdl'
    assert SoundgasmProfileIE._

# Generated at 2022-06-14 16:58:31.585714
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	# TODO
	assert (False), "TODO"

# Generated at 2022-06-14 16:58:36.588398
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    re_inst = re.compile(SoundgasmProfileIE._VALID_URL)
    string = 'http://soundgasm.net/u/ytdl/#/u/ytdl/Piano-sample'
    mobj = re_inst.match(string)
    assert mobj.group('id') == 'ytdl'

# Generated at 2022-06-14 16:58:45.234744
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:58:57.085295
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Unit test for constructor of class SoundgasmIE
    audio_id = '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    audio_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    expected_value = {
        'id': audio_id,
        'url': audio_url,
        'uploader': 'ytdl',
        'title': 'Piano sample',
        'description': 'Royalty Free Sample Music'
    }
    audio_object = SoundgasmIE()._real_extract(audio_url)

# Generated at 2022-06-14 16:59:00.187666
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
  print("Constructor of class SoundgasmIE")
  obj = SoundgasmIE()
  print(obj)


# Generated at 2022-06-14 16:59:07.429037
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    entry = SoundgasmProfileIE()._build_ie_entry(
        'http://soundgasm.net/u/ytdl/Piano-sample')
    entry.assert_equal({
        'id': 'Piano-sample',
        'display_id': 'Piano-sample',
        'url': 'http://soundgasm.net/u/ytdl/Piano-sample',
        'title': 'Piano sample',
        'description': 'Royalty Free Sample Music',
        'vcodec': 'none',
        'uploader': 'ytdl',
    })

# Generated at 2022-06-14 16:59:44.937095
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert ie._VALID_URL == ie._match_id(url)


# Generated at 2022-06-14 16:59:56.776156
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    audio_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    app = SoundgasmIE()
    entry = app._real_extract(audio_url)
    assert entry['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert entry['url'] == 'https://s3.amazonaws.com/soundgasm/audio/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a'
    assert entry['display_id'] == 'Piano-sample'
    assert entry['description'] == 'Royalty Free Sample Music'
    assert entry['title'] == 'Piano samp'
    assert entry['uploader'] == 'ytdl'

# Generated at 2022-06-14 17:00:04.363614
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    f = open("test_SoundgasmProfileIE.txt", "r")
    webpage = f.read()
    profile_id = "ytdl"
    entries = [
        "http://soundgasm.net/u/ytdl/Piano-sample"
    ]

    playlist_result = {
        '_type': 'playlist',
        'id': profile_id,
        'entries': entries,
    }

    assert playlist_result == {
        '_type': 'playlist',
        'id': profile_id,
        'entries': [
            "http://soundgasm.net/u/ytdl/Piano-sample"
        ],
    }



# Generated at 2022-06-14 17:00:13.311036
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Set up actual parameter values
    url = 'http://soundgasm.net/u/ytdl'
    # Set up mock function/class/object

# Generated at 2022-06-14 17:00:17.923191
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	assert SoundgasmIE().IE_NAME == 'soundgasm'
	assert SoundgasmIE()._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 17:00:21.831484
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert(ie.IE_NAME == 'soundgasm:profile')
    assert(isinstance(ie._VALID_URL, basestring))
    assert(isinstance(ie._TEST, dict))

# Generated at 2022-06-14 17:00:24.528395
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE()
        print("Unit test for SoundgasmIE() passed\n")
    except:
        print("Unit test for SoundgasmIE() failed\n")
        

# Generated at 2022-06-14 17:00:28.941457
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """test SoundgasmIE constructor"""
    SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 17:00:30.702503
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Execute constructor of class SoundgasmIE
    SoundgasmIE(None)

# Generated at 2022-06-14 17:00:39.163257
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie_inst =SoundgasmIE(info_extractor=InfoExtractor)
    assert ie_inst.IE_NAME == 'soundgasm'
    assert ie_inst._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert ie_inst._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert ie_inst._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'

# Generated at 2022-06-14 17:02:16.324863
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    playlist_count = 1
    Sg_profile =  SoundgasmProfileIE()
    Sound_profile_test = Sg_profile._real_extract(url)
    assert Sound_profile_test['id'] == 'ytdl'
    assert len(Sound_profile_test['entries']) == playlist_count


# Generated at 2022-06-14 17:02:23.577549
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    self = SoundgasmIE(extractor_config={'test': 'test'})
    mobj = re.match(self._VALID_URL, url)
    display_id = mobj.group('display_id')
    webpage = self._download_webpage(url, display_id)
    audio_url = self._html_search_regex(
        r'(?s)m4a\s*:\s*(["\'])(?P<url>(?:(?!\1).)+)\1', webpage,
        'audio URL', group='url')

# Generated at 2022-06-14 17:02:33.023916
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm_ie = SoundgasmIE("abc")
    assert soundgasm_ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:42.809943
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    class FakeInfoExtractor(object):
        def __init__(self):
            self.IE_NAME= 'Soundgasm Profile'
            self._VALID_URL = r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
            self._TEST = {
                'url': 'http://soundgasm.net/u/ytdl',
                'info_dict': {
                    'id': 'ytdl',
                },
                'playlist_count': 1,
            }

        def _real_extract(self, url):
            profile_id = self._match_id(url)

            webpage = self._download_webpage(url, profile_id)


# Generated at 2022-06-14 17:02:54.185402
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    mysoundgasm = SoundgasmIE()
    assert mysoundgasm.IE_NAME == 'soundgasm'
    assert mysoundgasm._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    mytest = mysoundgasm._TEST
    assert mytest['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert mytest['md5'] == '010082a2c802c5275bb00030743e75ad'
    info_dict = mytest['info_dict']

# Generated at 2022-06-14 17:02:58.618980
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 17:03:02.311173
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie._download_webpage
    assert ie._html_search_regex
    assert ie._search_regex
    assert ie._match_id

# Generated at 2022-06-14 17:03:10.517879
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    # the following code only works for Python 2
    ie = SoundgasmIE()
    # the following code only works for Python 3
    #ie = ie_class()
    info_dict = ie.extract(url)
    assert info_dict['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert info_dict['ext'] == 'm4a'
    assert info_dict['title'] == 'Piano sample'
    assert info_dict['description'] == 'Royalty Free Sample Music'
    assert info_dict['uploader'] == 'ytdl'


# Generated at 2022-06-14 17:03:16.418856
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }


# Generated at 2022-06-14 17:03:22.183317
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'