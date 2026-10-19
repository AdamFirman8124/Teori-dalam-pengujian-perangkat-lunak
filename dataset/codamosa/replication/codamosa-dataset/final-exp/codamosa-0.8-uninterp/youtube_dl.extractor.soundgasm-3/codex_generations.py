

# Generated at 2022-06-14 16:55:40.118180
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    passed = True

    # Test case 1
    assert_message = 'Test case 1 failed'
    result = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    expected_result = {'id': 'ytdl'}
    assert result.__dict__ == expected_result, assert_message

    # Test case 2
    assert_message = 'Test case 2 failed'
    result = SoundgasmProfileIE('http://soundgasm.net/u/ytdl/')
    expected_result = {'id': 'ytdl'}
    assert result.__dict__ == expected_result, assert_message

    # Test case 3
    assert_message = 'Test case 3 failed'
    result = SoundgasmProfileIE('http://soundgasm.net/u/ytdl/#')
    expected

# Generated at 2022-06-14 16:55:48.022214
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	from urlparse import urljoin
	from urlparse import urlparse
	from urlparse import urlunparse
	from urlparse import urlsplit
	from urlparse import urlunsplit
	from os.path import basename
	from posixpath import dirname
	soundgasm_ie = SoundgasmIE()
	result = soundgasm_ie.ie_key()
	assert result == 'Soundgasm'
	result = soundgasm_ie._real_initialize()
	assert result == None
	result = soundgasm_ie._login()
	assert result == False
	result = soundgasm_ie._real_initialize()
	assert result == None
	result = soundgasm_ie._real_extract(url='http://soundgasm.net/u/ytdl/Piano-sample')
	assert len

# Generated at 2022-06-14 16:55:52.500737
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    name = 'Soundgasm'
    filename = 'test/test.py'
    args = {'display_id': 'boo', 'webpage':'blah'}
    sg = SoundgasmIE(name, filename, args)
    sg.test_downloader()


# Generated at 2022-06-14 16:55:54.125421
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = "http://soundgasm.net/u/ytdl"
    ie = SoundgasmProfileIE(url)
    ie.extract()


# Generated at 2022-06-14 16:56:00.194889
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile = SoundgasmProfileIE('https://soundgasm.net/u/ytdl')
    assert profile.IE_NAME == 'soundgasm:profile'
    assert profile._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert profile._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }

# Generated at 2022-06-14 16:56:00.908311
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE

# Generated at 2022-06-14 16:56:10.816754
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert not ie.suitable('http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie.suitable('http://soundgasm.net/u/ytdl/Piano-sample/')
    assert not ie.suitable('http://soundgasm.net/u/ytdl/Piano-sample/?a=b&c=d')
    assert ie.suitable('http://soundgasm.net/u/ytdl/Piano-sample/?a=b&c=d#')

# Generated at 2022-06-14 16:56:13.510734
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """Testing SoundgasmIE constructor"""

    SoundgasmIE('www.soundgasm.net/u/ytdl/Piano-sample')



# Generated at 2022-06-14 16:56:22.334500
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    mp = SoundgasmProfileIE()
    assert mp._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert mp.IE_NAME == 'soundgasm:profile'
    assert mp._TEST['url'] == 'http://soundgasm.net/u/ytdl'
    assert mp._TEST['info_dict']['id'] == 'ytdl'
    assert mp._TEST['playlist_count'] == 1
    return mp

# Generated at 2022-06-14 16:56:29.078945
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    ie.download('http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie.get_info('url') == 'http://media02.soundgasm.net/u/ytdl/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a'

# Generated at 2022-06-14 16:56:36.305066
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    SoundgasmIE().suitable(url)
    SoundgasmIE().extract(url)
    print("passed test_SoundgasmIE")


# Generated at 2022-06-14 16:56:39.294477
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    info = SoundgasmIE()._real_extract(url)
    print (info)

# Generated at 2022-06-14 16:56:42.596476
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:56:47.467454
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    possible_url_formats = [
        'http://soundgasm.net/u/ytdl',
        'http://soundgasm.net/u/ytdl/',
        'http://soundgasm.net/u/ytdl/#',
        'http://soundgasm.net/u/ytdl/#/',
    ]
    ie = SoundgasmProfileIE()
    for url in possible_url_formats:
        assert ie.suitable(url)

# Generated at 2022-06-14 16:56:50.453720
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('SoundgasmProfile', 'https://soundgasm.net/u/ytdl', {'id':'ytdl'}, '1')

# Generated at 2022-06-14 16:56:52.486778
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE('Soundgasm', 'Soundgasm')
    assert obj


# Generated at 2022-06-14 16:56:53.517967
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    print(SoundgasmIE())

# Generated at 2022-06-14 16:56:58.674856
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    #create instance from class SoundgasmProfileIE
    a = SoundgasmProfileIE()
    # test the function _match_id
    match_id_test(a)
    # if _match_id is correct test _real_extract
    if match_id_correct == True:
        real_extract_test(a)
    # test the title of the current instance
    title_test(a)


# Generated at 2022-06-14 16:57:00.437057
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_ie = SoundgasmProfileIE('SoundgasmProfileIE', 'soundgasm:profile')
    assert profile_ie.playlist_mincount == 1

# Generated at 2022-06-14 16:57:04.630129
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()
    SoundgasmProfileIE.ie_key()
    SoundgasmProfileIE.ie_key() # check cache
    SoundgasmProfileIE._build_config()

# Generated at 2022-06-14 16:57:15.191028
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert(SoundgasmProfileIE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?')

# Generated at 2022-06-14 16:57:16.038918
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    pass


# Generated at 2022-06-14 16:57:17.500846
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE(None, None)._real_extract(None)

# Generated at 2022-06-14 16:57:19.289284
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE().extract(test_SoundgasmIE._TEST['url'])

# Generated at 2022-06-14 16:57:25.254916
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from .html import html_to_clean_dict
    from .html import clean_html
    from .html import get_element_by_id
    from .html import get_elements_by_attribute
    from .html import get_element_by_attribute
    from .html import get_elements_by_class
    from .html import get_element_by_class
    from .html import search_regex
    from .html import remove_quotes
    from .html import unescapeHTML
    from .html import url_basename
    from .html import unescapeEntities
    from .html import get_element_by_tag
    from .html import js_to_json
    from .html import ExtractorError
    from .html import hidden_inputs
    from .html import urljoin
    from .html import int_or_none

# Generated at 2022-06-14 16:57:27.040124
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    try:
        SoundgasmProfileIE()
    except:
        assert False

# Generated at 2022-06-14 16:57:31.439320
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Test the constructor class
    ie = SoundgasmProfileIE()
    test_url = 'http://soundgasm.net/u/ytdl'
    res = ie.suitable(test_url)
    assert res == True



# Generated at 2022-06-14 16:57:38.800999
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = "http://soundgasm.net/u/ytdl"
    audio_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    SoundgasmProfileIE(IE_NAME, url)._real_extract(url) # pylint: disable=protected-access
    SoundgasmIE(IE_NAME, audio_url)._real_extract(audio_url) # pylint: disable=protected-access

# Generated at 2022-06-14 16:57:45.722179
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE("http://soundgasm.net/u/ytdl")
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST['url'] == 'http://soundgasm.net/u/ytdl'
    assert ie._TEST['info_dict']['id'] == 'ytdl'
    assert ie._TEST['playlist_count'] == 1


# Generated at 2022-06-14 16:57:51.700646
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # test with url that has a trailing slash
    url = "http://soundgasm.net/u/ytdl/"
    ie = SoundgasmProfileIE('Soundgasm')
    # tests if url is valid according to IE regex
    assert ie._match_id(url) is not None


# Generated at 2022-06-14 16:58:12.045323
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	url = 'http://soundgasm.net/u/ytdl/Piano-sample'
	downloader = InfoExtractor()
	sg = SoundgasmIE(downloader)
	assert(sg.suitable(url) == 1)

# Generated at 2022-06-14 16:58:23.379023
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    '''
    Unit test to test constructors of class SoundgasmIE
    '''
    #Instantiate SoundgasmIE constructor with a url
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

    #Instantiate SoundgasmIE constructor with a url and video_id
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample', 'Piano-sample')

# Generated at 2022-06-14 16:58:36.481739
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    video = SoundgasmIE()._real_extract(url)
    assert video['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert video['display_id'] == 'Piano-sample'
    assert video['url'] == 'http://audio.cdn.soundgasm.net/0/d/4/0d4b4d2c24bf7d1538a9a9b7abf5b5e8d5cdc1e1.m4a'
    assert video['vcodec'] == 'none'
    assert video['title'] == 'Piano sample'
    assert video['description'] == 'Royalty Free Sample Music'
    assert video

# Generated at 2022-06-14 16:58:37.848625
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:58:39.257435
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert(isinstance(SoundgasmIE, IE_NAME))

# Generated at 2022-06-14 16:58:41.076185
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE()._VALID_URL == SoundgasmIE._VALID_URL

# Generated at 2022-06-14 16:58:44.678293
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Unit test for constructor of class SoundgasmProfileIE
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:58:45.453783
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    tester = SoundgasmIE()

# Generated at 2022-06-14 16:58:46.282801
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	sound = SoundgasmIE()


# Generated at 2022-06-14 16:58:48.915866
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = "http://soundgasm.net/u/ytdl"
    soundgasm_profile_ie = SoundgasmProfileIE(url)
    return soundgasm_profile_ie

# Generated at 2022-06-14 16:59:24.926782
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    instance = SoundgasmIE()
    assert instance._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 16:59:25.970625
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE()

# Generated at 2022-06-14 16:59:36.524461
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """
    Test SoundgasmProfileIE constructor.
    """
    obj = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    assert obj._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1
    }
    assert obj.IE_NAME == 'soundgasm:profile'
    assert obj._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:59:46.035885
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    tests = [
        {
            "url": "http://soundgasm.net/u/ytdl",
            "info_dict": {
                "id": "ytdl",
            },
            "playlist_count": 1,
        },
        {
            "url": "http://soundgasm.net/u/Riddance",
            "info_dict": {
                "id": "Riddance",
            },
            "playlist_count": 1,
        }
    ]

    for test in tests:
        profile = SoundgasmProfileIE()._real_initialize(test['url'])
        assert profile._match_id(test['url']) == test['info_dict']['id']

# Generated at 2022-06-14 16:59:48.905841
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert(ie._TEST['url'] == 'http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:59:57.242592
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_input = 'https://soundgasm.net/u/ytdl'

    # Create instance of SoundgasmProfileIE to initialize
    soundgasm_profile_object = SoundgasmProfileIE()

    # Test if object is created
    assert soundgasm_profile_object is not None

    # Call to _match_id to set the profile_id
    soundgasm_profile_object._match_id(test_input)

    # Test if _match_id has set the profile_id
    assert soundgasm_profile_object.profile_id == test_input

# Generated at 2022-06-14 17:00:01.818287
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

    # Download an audio file for testing
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    self = SoundgasmIE()
    self.assertIsInstance(self._real_extract(url), dict)
    self.assertEqual(self._real_extract(url)["id"], "88abd86ea000cafe98f96321b23cc1206cbcbcc9")

# Generated at 2022-06-14 17:00:11.456980
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    _test = {
        'playlist_mincount': 1,
        'url': 'http://soundgasm.net/u/ytdl',
        }
    _result = {
        '_type': 'playlist',
        'id': 'ytdl',
        'entries': [
            {
                '_type': 'url',
                'url': 'http://soundgasm.net/u/ytdl/Piano-sample',
                'ie_key': 'Soundgasm',
            },
        ],
    }
    ie = SoundgasmProfileIE(_test['url'])
    ie.download = lambda url: _test['url']
    playlist = ie.extract()
    assert playlist == _result

# Generated at 2022-06-14 17:00:13.914028
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    s = SoundgasmProfileIE()
    s._real_extract("http://soundgasm.net/u/ytdl")

# Generated at 2022-06-14 17:00:15.346163
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE().IE_NAME == SoundgasmIE.IE_NAME

# Generated at 2022-06-14 17:01:50.981393
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    sg = SoundgasmProfileIE()
    if (sg.IE_NAME != 'soundgasm:profile'):
        raise NameError('Test failed: IE_NAME')
    if (sg._VALID_URL != 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?'):
        raise NameError('Test failed: _VALID_URL')


# Generated at 2022-06-14 17:01:57.243346
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Creating Instance of class SoundgasmIE
    inst = SoundgasmIE()
    assert isinstance(inst, SoundgasmIE)
    # Testing _VALID_URL
    url = 'http://soundgasm.net/u/ytdl/to_be_or_not_to_be'
    assert inst._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:08.911608
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    IE_NAME = 'SoundgasmIE'
    VALID_URL = r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:15.547761
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie.IE_DESC == 'Soundgasm.net profile'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 17:02:22.736710
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert(ie.IE_NAME == 'soundgasm')
    assert(ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')

# Generated at 2022-06-14 17:02:32.639814
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from .common import FakeYDL
    from .extractor.soundgasm import SoundgasmProfileIE

    url = 'http://soundgasm.net/u/ytdl'
    info_dict = {
        'id': 'ytdl',
        'entries': [
            {
                'url': 'http://soundgasm.net/u/ytdl/Piano-sample',
                '_type': 'url_transparent',
                'ie_key': 'Soundgasm',
                'title': 'Piano sample',
            },
        ]
    }

    ydl = FakeYDL()
    # First call of playlists method
    # In this call, we don't have 'entries' from previous call.

# Generated at 2022-06-14 17:02:34.555771
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	SoundgasmIE(InfoExtractor)

# Generated at 2022-06-14 17:02:37.426189
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	soundgasm_profile_ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl', 'ytdl')
	assert isinstance(soundgasm_profile_ie, SoundgasmProfileIE)

# Generated at 2022-06-14 17:02:41.866935
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    # to pass the test, ie.IE_NAME must be 'soundgasm:profile' and
    # ie.IE_DESC must be "Soundgasm user's profile"
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie.IE_DESC == "Soundgasm user's profile"

# Generated at 2022-06-14 17:02:44.662880
# Unit test for constructor of class SoundgasmProfileIE