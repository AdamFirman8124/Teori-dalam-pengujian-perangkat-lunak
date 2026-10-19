

# Generated at 2022-06-14 16:55:33.741773
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    a = SoundgasmIE()
    assert a == None


# Generated at 2022-06-14 16:55:36.586183
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    ie.extract("http://soundgasm.net/u/ytdl")

# Generated at 2022-06-14 16:55:45.974220
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    class TestSoundgasmIE(SoundgasmIE):
        def _download_webpage(self, url, display_id):
            return self._TEST.get('webpage') if url == 'http://soundgasm.net/u/ytdl/Piano-sample' else super(TestSoundgasmIE, self)._download_webpage(url, display_id)
    # test for SoundgasmIE._download_webpage
    ie = TestSoundgasmIE()

# Generated at 2022-06-14 16:55:53.668180
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert(SoundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')
    assert(SoundgasmProfileIE._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    })


# Generated at 2022-06-14 16:55:55.703381
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    ie.extract('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:55:57.548593
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert 'http://soundgasm.net/u/ytdl/Piano-sample' == SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample').url

# Generated at 2022-06-14 16:56:05.209440
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sg = SoundgasmIE()
    assert sg.ie_key() == 'Soundgasm'
    assert sg.ie_name() == 'Soundgasm'
    assert sg.ie_url() == 'http://soundgasm.net/'
    assert sg.extractor_key() == 'Soundgasm'
    assert sg.extractor_key() == sg.IE_KEY
    assert sg.IE_KEY == 'Soundgasm'

# Generated at 2022-06-14 16:56:10.924166
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = r'http://soundgasm.net/u/ytdl/Piano-sample'
    s_inst = SoundgasmIE({})
    pattern = re.compile(s_inst._VALID_URL)
    matches = pattern.match(url)
    assert matches


# Generated at 2022-06-14 16:56:17.033233
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # SoundgasmIE.__init__(self, url)
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    soundgasm_ie = SoundgasmIE(url)
    print('url: ' + soundgasm_ie.url)
    print('id: ' + soundgasm_ie.id)
    print('display_id: ' + soundgasm_ie.display_id)

if __name__ == '__main__':
    test_SoundgasmIE()

# Generated at 2022-06-14 16:56:20.516989
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    except:
        raise AssertionError('Cannot initialize SoundgasmIE')

# Generated at 2022-06-14 16:56:29.513138
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	profile = SoundgasmProfileIE(SoundgasmProfileIE._VALID_URL)
	assert profile.IE_NAME == 'soundgasm:profile'
	assert profile._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:56:31.724948
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE = SoundgasmIE(None)
    assert IE.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:56:33.656497
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    obj = SoundgasmProfileIE("id","url")
    assert obj.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:56:39.984745
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    print("Testing URL: http://soundgasm.net/u/ytdl/Piano-sample")
    test_download_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    soundgasm = SoundgasmIE(test_download_url)
    assert soundgasm.URL == test_download_url
    assert(soundgasm.re.pattern == SoundgasmIE._VALID_URL)
    assert(soundgasm.IE_NAME == "soundgasm")
    print("Test Passed!")

if __name__ == '__main__':
    # TEST SOUNDGASM EXTRACTOR
    test_SoundgasmIE()

# Generated at 2022-06-14 16:56:41.661369
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE("soundgasm:profile")


# Generated at 2022-06-14 16:56:44.155765
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    IE = SoundgasmProfileIE()
    assert isinstance(IE, InfoExtractor)
    assert IE.IE_NAME == 'soundgasm:profile'


# Generated at 2022-06-14 16:56:50.966953
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sgasm = SoundgasmIE()
    print(sgasm)
    assert(sgasm._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')

# Generated at 2022-06-14 16:56:59.067583
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    profile_id = 'ytdl'
    webpage = 'http://soundgasm.net/u/ytdl/$'
    entries = [
        'http://soundgasm.net/u/ytdl/Piano-sample',
        'http://soundgasm.net/u/ytdl/test-sound'
    ]
    print('contains url:', url)
    print('profile_id:', profile_id)
    print("webpage url:", webpage)
    print("entries:")
    for entry in entries:
        print(entry)

# Generated at 2022-06-14 16:57:01.498228
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    # The following should not raise an exception
    ie.url_result("http://soundgasm.net/u/profile_id/post_id", 'Soundgasm')

# Generated at 2022-06-14 16:57:08.735443
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie.entries
    assert ie.entries[0]['url'] == "http://d1g7oon0lxeek0.cloudfront.net/s/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a"

# Generated at 2022-06-14 16:57:22.295816
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # unit testing constructor of SoundgasmProfileIE
    # expected parameters are: ie_key, ie_name, ie_url, ie_description
    assert SoundgasmProfileIE._VALID_URL == SoundgasmProfileIE.ie_url
    assert SoundgasmProfileIE._TEST['url'] == SoundgasmProfileIE.ie_url
    assert SoundgasmProfileIE.IE_NAME == SoundgasmProfileIE.ie_name
    assert 'Soundgasm Profile IE' == SoundgasmProfileIE.ie_description



# Generated at 2022-06-14 16:57:28.974666
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    profile_id = 'ytdl'
    ie = SoundgasmProfileIE(SoundgasmProfileIE.ie_key(), url)
    profile_id_obtained = ie._match_id(url)
    assert profile_id == profile_id_obtained

# Generated at 2022-06-14 16:57:34.778974
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE = SoundgasmIE()
    assert IE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert IE.IE_NAME == 'soundgasm'


# Generated at 2022-06-14 16:57:38.382405
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    assert ie.playlist_mincount == 1
    assert ie.playlist_maxcount == 0
    assert ie.playlist_count == 1

# Generated at 2022-06-14 16:57:40.508626
# Unit test for constructor of class SoundgasmProfileIE

# Generated at 2022-06-14 16:57:42.063454
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    my_instance = SoundgasmIE()

    assert my_instance.ie_key() == 'Soundgasm'

# Generated at 2022-06-14 16:57:50.811300
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE()._VALID_URL == SoundgasmIE._VALID_URL
    assert SoundgasmIE().ie_key() == SoundgasmIE.ie_key()
    assert SoundgasmIE().extractor_key() == SoundgasmIE.extractor_key()
    assert SoundgasmIE()._TEST == SoundgasmIE._TEST
    assert SoundgasmIE()._download_webpage == SoundgasmIE._download_webpage
    assert SoundgasmIE()._search_regex == SoundgasmIE._search_regex
    assert SoundgasmIE()._real_extract == SoundgasmIE._real_extract
    assert SoundgasmIE()._match_id == SoundgasmIE._match_id
    assert SoundgasmIE()._html_search_regex == SoundgasmIE._html

# Generated at 2022-06-14 16:57:58.134636
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ig = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')

    new_instance = ig.test('http://soundgasm.net/u/test/test_id')

    #assert isinstance(new_instance, SoundgasmIE)
    assert 'test' == new_instance.extractor_key
    assert 'http://soundgasm.net/u/test/test_id' == new_instance.url

    new_instance = ig.test('ytdl', 'test')
    assert 'test' == new_instance.extractor_key
    assert 'ytdl' == new_instance.url

# Generated at 2022-06-14 16:58:01.990317
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    ie_name = ie.IE_NAME
    assert ie_name == 'Soundgasm'


# Generated at 2022-06-14 16:58:07.052968
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    app = SoundgasmIE.SoundgasmIE()
    filepath1 = 'test/test-data/test1.txt'
    assert app.validate_file(filepath1) is True

# Generated at 2022-06-14 16:58:22.381956
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    print("test_SoundgasmProfileIE:")
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:58:25.289259
# Unit test for constructor of class SoundgasmIE

# Generated at 2022-06-14 16:58:29.560810
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    insta = SoundgasmProfileIE("ytdl", "http://www.soundgasm.net/u/ytdl/")
    assert insta.name == "ytdl"
    assert insta.url == "http://www.soundgasm.net/u/ytdl/"

# Generated at 2022-06-14 16:58:37.249065
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # constructor test
    SoundgasmIE(common.FakeYDL())
    # successful regex test
    regex_test('http://soundgasm.net/u/ytdl/Piano-sample',
        SoundgasmIE.IE_NAME, 'Piano-sample', 'm4a')
    # successful regex test
    regex_test('http://soundgasm.net/u/ytdl/Test',
        SoundgasmIE.IE_NAME, 'Test', 'm4a', 'Test is a test. This is a description of the audio file.')


# Generated at 2022-06-14 16:58:39.066797
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert len(ie._downloader.params) == 1



# Generated at 2022-06-14 16:58:41.730330
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Constructor test
    """
    ie = SoundgasmIE('https://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:58:44.370211
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert issubclass(SoundgasmProfileIE, InfoExtractor)



# Generated at 2022-06-14 16:58:53.247984
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE()
    assert obj.IE_NAME == 'soundgasm'
    assert obj._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:58:55.773414
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    return ie


# Generated at 2022-06-14 16:58:57.570433
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie == SoundgasmIE()


# Generated at 2022-06-14 16:59:34.669745
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    extracted = SoundgasmProfileIE._real_extract('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:59:36.572285
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	# Constructor of SoundgasmIE class
	kek = SoundgasmIE()

# Generated at 2022-06-14 16:59:42.779624
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    # Check for the class attributes
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TEST')

    # Check for the _download_webpage function
    assert hasattr(ie, '_download_webpage')

    # Check for the _real_extract function
    assert hasattr(ie, '_real_extract')



# Generated at 2022-06-14 16:59:47.633280
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    return type('TestSoundgasmIE', (object,), {
        'a_property': 'this is a property',
    })

# Generated at 2022-06-14 16:59:55.761890
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	url = "http://soundgasm.net/u/ytdl"
	data = {}
	data["url"] = url
	data["id"] = "ytdl"
	data["display_id"] = "ytdl"
	profile = SoundgasmProfileIE(SoundgasmProfileIE._downloader)
	profile.url = url
	profile._downloader = SoundgasmProfileIE._downloader
	profile._match_id(url)
	profile._real_initialize()
	profile._real_extract(url)


# Generated at 2022-06-14 17:00:04.420684
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():

    # Test for playlist entries
    playlist_entries = ["http://soundgasm.net/u/ytdl/Piano-sample"]
    profile_id = "ytdl"
    webpage = """
    <a href="{0}"></a>
    """.format(playlist_entries[0])

    profile_info = SoundgasmProfileIE._real_extract(None, "http://soundgasm.net/u/%s" % profile_id)

    assert profile_info['_type'] == 'playlist'
    assert profile_info['id'] == profile_id
    assert len(profile_info['entries']) == len(playlist_entries)

    # Test for playlist entries using unicode

# Generated at 2022-06-14 17:00:08.531971
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    info_extractor = SoundgasmProfileIE(None, None)
    assert (info_extractor._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')

# Generated at 2022-06-14 17:00:09.777389
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    pass

# Generated at 2022-06-14 17:00:19.465180
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_ie = SoundgasmProfileIE()
    assert profile_ie.IE_NAME == 'soundgasm:profile'
    assert profile_ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert profile_ie._TEST['url'] == 'http://soundgasm.net/u/ytdl'
    assert profile_ie._TEST['info_dict']['id'] == 'ytdl'
    assert profile_ie._TEST['playlist_count'] == 1


# Generated at 2022-06-14 17:00:23.835539
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm_profile_ie = SoundgasmProfileIE()
    assert soundgasm_profile_ie.IE_NAME == 'soundgasm:profile'
    assert soundgasm_profile_ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 17:01:50.494000
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SOUNDGASM_PROFILE_URL = 'http://soundgasm.net/u/foo'
    info_dict = {
        'id': 'foo',
    }
    ie = SoundgasmProfileIE(SOUNDGASM_PROFILE_URL)
    assert ie.id == info_dict['id']
    assert ie.url == SOUNDGASM_PROFILE_URL


# Generated at 2022-06-14 17:01:52.699355
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    soundgasmIE = SoundgasmIE()
    soundgasmIE._real_extract(url)



# Generated at 2022-06-14 17:01:58.955201
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    i = SoundgasmProfileIE()
    assert i.IE_NAME == 'soundgasm:profile'
    assert i._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert i._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }



# Generated at 2022-06-14 17:02:06.640954
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # This test is complete.
    instance = SoundgasmProfileIE()
    assert instance._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert instance._TEST == {'url': 'http://soundgasm.net/u/ytdl', 'info_dict': {'id': 'ytdl'}, 'playlist_count': 1}

# Generated at 2022-06-14 17:02:10.570424
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    obj = SoundgasmProfileIE()
    obj._real_extract(obj._TEST)

# Generated at 2022-06-14 17:02:11.858839
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    tester = SoundgasmProfileIE()
    assert tester.get_pattern() == tester._VALID_URL

# Generated at 2022-06-14 17:02:16.121661
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    class ie(InfoExtractor):
        _VALID_URL = SoundgasmProfileIE._VALID_URL  # pylint: disable=protected-access
    instance = ie(SoundgasmProfileIE.IE_NAME, SoundgasmProfileIE.ie_key())
    assert instance is not None

# Generated at 2022-06-14 17:02:18.047359
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()

# Generated at 2022-06-14 17:02:28.789740
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Check that IEs are created properly
    i = SoundgasmProfileIE()
    assert i.IE_NAME == 'soundgasm:profile'
    assert i.name == 'Soundgasm (profile)'
    assert i.description == 'I\'m testing'
    assert i.age_limit == 0
    assert i.extractor == 'SoundgasmProfileIE'
    assert i.host == 'soundgasm.net'
    assert i.url_transparent == True
    assert i.ie == SoundgasmProfileIE
    assert i.url_regex == i._VALID_URL
    assert i.playlist_mincount == 1

# Generated at 2022-06-14 17:02:29.651559
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE() is not None