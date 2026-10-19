

# Generated at 2022-06-14 16:55:44.125676
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """
    Basic test for constructor of class SoundgasmProfileIE
    """
    test_dict = {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }
    test_url = test_dict['url']
    # test_dict['info_dict']['id'] = 'ytdl'
    # test_dict['playlist_count'] = 1
    assert_test_dicts_equal(SoundgasmProfileIE._download_webpage(test_url), test_dict)


# Generated at 2022-06-14 16:55:54.988390
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Create object of class SoundgasmIE
    soundgasm_ie = SoundgasmIE()
    # Check if audio_id is set to display_id passed to _real_extract function
    audio_id = soundgasm_ie._real_extract(soundgasm_ie._TEST['url'])['id']
    assert audio_id == soundgasm_ie._TEST['info_dict']['display_id']
    # Check if display_id is set to display_id passed to _real_extract function
    display_id = soundgasm_ie._real_extract(soundgasm_ie._TEST['url'])['display_id']
    assert display_id == soundgasm_ie._TEST['info_dict']['display_id']


# Generated at 2022-06-14 16:55:58.418302
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('Soundgasm')
    ie._match_id(ie._VALID_URL) == 'ytdl'
    ie._match_id(ie.IE_NAME) is None
    assert(ie._VALID_URL == ie.VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')

# Generated at 2022-06-14 16:56:00.689415
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")

# Generated at 2022-06-14 16:56:13.466167
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE.IE_NAME == 'soundgasm:profile'
    assert SoundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert SoundgasmProfileIE._TEST == {'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {'id': 'ytdl',},
        'playlist_count': 1,
    }


# Generated at 2022-06-14 16:56:18.868697
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    i = SoundgasmProfileIE()
    assert i.IE_NAME == 'soundgasm:profile'
    assert i._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert i._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }


# Generated at 2022-06-14 16:56:28.120100
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	# Check that the url is parsed correctly
	audio_id = "Piano-sample"
	url = "http://soundgasm.net/u/ytdl/Piano-sample"
	
	# This is the same test from soundgasm.py
	assert SoundgasmIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
	assert SoundgasmIE._TEST['url'] == "http://soundgasm.net/u/ytdl/Piano-sample"
	assert SoundgasmIE._TEST['md5'] == "010082a2c802c5275bb00030743e75ad"


# Generated at 2022-06-14 16:56:32.491423
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    i = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert i.ie_key() == 'Soundgasm'
    assert i.display_id() == 'Piano-sample'


# Generated at 2022-06-14 16:56:33.380636
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    inst = SoundgasmProfileIE()

# Generated at 2022-06-14 16:56:37.103474
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	test_url = "http://soundgasm.net/u/ytdl"
	assert(SoundgasmProfileIE()._match_id(test_url) == "ytdl")
	assert(SoundgasmProfileIE()._real_extract(test_url)['id'] == "ytdl")


# Generated at 2022-06-14 16:56:43.800936
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE('Soundgasm:profile')._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:56:50.453061
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    try:
        SoundgasmProfileIE()
    except Exception as e:
        print("test_SoundgasmProfileIE() FAILED!")
        print("Exception: {0}".format(str(e)))
        return False
    else:
        print("test_SoundgasmProfileIE() OK!")
        return True



# Generated at 2022-06-14 16:56:51.450795
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:56:59.111677
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    assert SoundgasmIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:57:00.548800
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Unit test to check if SoundgasmIE is valid.
    """
    SoundgasmIE()

# Generated at 2022-06-14 16:57:06.559201
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    result = SoundgasmProfileIE._soundgasm_profile_ie()

    assert result.IE_NAME == 'Soundgasm:Profile'
    result = SoundgasmProfileIE._soundgasm_profile_ie()

    assert result.IE_NAME == 'Soundgasm:Profile'

# Generated at 2022-06-14 16:57:15.900939
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Check if audio URL contains valid data
    test_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    expected_id = '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert(SoundgasmIE._search_regex(SoundgasmIE._VALID_URL, test_url, 'audio id', default=display_id) == expected_id)
    # Check if audio ID is extracted properly
    assert(SoundgasmIE._search_regex(r'/([^/]+)\.m4a', 'http://f.soundgasm.net/sounds/d2efa2a0a7b2e0411f42/dinosaur.m4a', 'audio id', default=display_id) == 'dinosaur')
   

# Generated at 2022-06-14 16:57:17.737213
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    x = SoundgasmIE()
    assert x.__class__.__name__ == 'SoundgasmIE'

# Generated at 2022-06-14 16:57:19.632922
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE()
    assert obj is not None


# Generated at 2022-06-14 16:57:24.554824
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    ie.download("http://soundgasm.net/u/ytdl/Piano-sample")


# Generated at 2022-06-14 16:57:33.316860
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Create instance of class SoundgasmProfileIE, and test for correct instantiation
    instance = SoundgasmProfileIE()
    assert isinstance(instance, SoundgasmProfileIE)


# Generated at 2022-06-14 16:57:44.812980
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    url2 = 'http://soundgasm.net/u/Mazbo/The-Slutty-Slave-Femdom-Degradation-Fantasy'
    webpage = '<div class="jp-title">Piano sample</div>'
    webpage2 = '<div class="jp-title">The Slutty Slave </div>'
    match = SoundgasmIE._VALID_URL.match(url)
    match2 = SoundgasmIE._VALID_URL.match(url2)
    print(SoundgasmIE._real_extract(SoundgasmIE(), match, webpage))
    print(SoundgasmIE._real_extract(SoundgasmIE(), match2, webpage2))


# Generated at 2022-06-14 16:57:53.006931
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Testing SoundgasmIE
    test_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    test_url_results = "http://media.soundgasm.net/sounds/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a"

    assert(SoundgasmIE()._real_extract(test_url)['url'] == test_url_results)


# Generated at 2022-06-14 16:57:56.106892
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from soundgasm import SoundgasmProfileIE
    SoundgasmProfileIE("soundgasm:profile", SoundgasmProfileIE._VALID_URL, None)._match_id("http://soundgasm.net/u/ytdl")


# Generated at 2022-06-14 16:57:59.225824
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'


# Generated at 2022-06-14 16:58:02.137868
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    a = SoundgasmProfileIE('http://soundgasm.net/u/ytdl','')
    assert isinstance(a, SoundgasmProfileIE)
    return True

# Generated at 2022-06-14 16:58:08.258815
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert(ie.IE_NAME == 'soundgasm:profile')
    assert(ie._TEST['url'] == 'http://soundgasm.net/u/ytdl')
    assert(ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')
    assert(ie._TEST['info_dict']['id'] == 'ytdl')
    assert(ie._TEST['playlist_count'] == 1)

# Generated at 2022-06-14 16:58:10.617188
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	sg_profile_ie = SoundgasmProfileIE()

# Generated at 2022-06-14 16:58:12.709837
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")


# Generated at 2022-06-14 16:58:24.013410
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    import unittest
    class TestSoundgasmIE(unittest.TestCase):

        def test_SoundgasmIE(self):
            obj = SoundgasmIE()
            self.assertEqual(obj.IE_NAME, 'soundgasm')
            self.assertIsInstance(obj, InfoExtractor)
            self.assertEqual(obj._VALID_URL, r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')
            self.assertIsInstance(obj._TEST, dict)

# Generated at 2022-06-14 16:58:47.158662
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():

    # test construction
    ie = SoundgasmProfileIE('Soundgasm')

    # test instance
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST == {'url': 'http://soundgasm.net/u/ytdl', 'info_dict': {'id': 'ytdl'}, 'playlist_count': 1}
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie.ie_key() == 'SoundgasmProfile'
    assert ie.get_host_from_url('http://soundgasm.net/u/ytdl') == 'soundgasm.net'

# Generated at 2022-06-14 16:58:51.658863
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url_test_str = "http://soundgasm.net/u/ytdl/Piano-sample"
    obj = SoundgasmIE(url_test_str)
    assert(obj.name == "SoundgasmIE")
    assert(obj.ie_key() == "SoundgasmIE")
    assert(obj.valid_url(url_test_str) == True)

# Generated at 2022-06-14 16:59:01.970433
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """Unit test for constructor of class SoundgasmProfileIE"""
    url = "http://soundgasm.net/u/ytdl"
    soundgasm_profile_ie = SoundgasmProfileIE(url)

    assert soundgasm_profile_ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert soundgasm_profile_ie._TEST['url'] == "http://soundgasm.net/u/ytdl"

    assert soundgasm_profile_ie._match_id("something") is None
    assert soundgasm_profile_ie._match_id("http://soundgasm.net/u/ytdl") == "ytdl"


# Generated at 2022-06-14 16:59:04.756571
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    i = SoundgasmIE(url)
    assert i != None


# Generated at 2022-06-14 16:59:05.700580
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ydl = SoundgasmProfileIE(InfoExtractor)

# Generated at 2022-06-14 16:59:06.777485
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE()

# Generated at 2022-06-14 16:59:13.924902
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample';
    o = SoundgasmIE();
    info = o.extract(url);
    assert(info['video_id'] == info['display_id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9');

# Generated at 2022-06-14 16:59:19.004174
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 16:59:23.784376
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:59:24.893974
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    new_SoundgasmProfileIE()


# Generated at 2022-06-14 16:59:50.586047
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    print(SoundgasmIE._TEST)


# Generated at 2022-06-14 17:00:00.843079
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.utils import DateRange
    SoundgasmProfileIE.downloader_factory = FileDownloader
    test_instance = SoundgasmProfileIE()
    test_instance.url = 'http://soundgasm.net/u/ytdl'
    test_instance.download(None)
    assert test_instance.id == 'ytdl'
    assert test_instance.url == 'http://soundgasm.net/u/ytdl'
    assert isinstance(test_instance.age_limit, int) == True
    assert isinstance(test_instance.params, dict) == True
    assert isinstance(test_instance.filepath, str) == True
    assert isinstance(test_instance.available, bool) == True

# Generated at 2022-06-14 17:00:04.215746
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE().IE_NAME == 'SoundgasmProfileIE'


# Generated at 2022-06-14 17:00:08.460562
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	mock_url = "http://soundgasm.net/u/ytdl/Piano-sample"
	mock_display_id = "Piano-sample"
	mock_webpage = "content of webpage"
	mock_audio_url = "http://soundgasm.net/audio/u/sampled/piano.m4a"
	mock_title = "Piano sample"
	mock_description = "Royalty Free Sample Music"
	mock_audio_id = "0123456789abcdef"

	info_extractor = SoundgasmIE()
	info_extractor._download_webpage = lambda url, display_id: mock_webpage

# Generated at 2022-06-14 17:00:20.489866
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Test for valid url
    ie = SoundgasmIE()
    audio_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    audio_url_result = ie.extract(audio_url)
    audio_url_expected = {
        'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9',
        'ext': 'm4a',
        'title': 'Piano sample',
        'description': 'Royalty Free Sample Music',
        'uploader': 'ytdl',
    }
    assert audio_url_result.items() >= audio_url_expected.items()
    # Test for invalid url
    audio_url_invalid = 'http://soundgasm.net/u/ytdl/'

# Generated at 2022-06-14 17:00:27.881674
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:00:29.081264
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 17:00:30.798978
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	print(SoundgasmIE().extract("http://soundgasm.net/u/ytdl/Piano-sample"))

# Generated at 2022-06-14 17:00:33.266342
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    mainTest('soundgasm', 'https://soundgasm.net/u/ytdl', 'SoundgasmProfileIE', 'Piano-sample')

# Generated at 2022-06-14 17:00:36.023746
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # TODO: write test cases here
    pass

if __name__ == "__main__":
    test_SoundgasmIE()

# Generated at 2022-06-14 17:01:42.126753
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    user_name = 'ytdl'
    display_id = 'Piano-sample'
    ie = SoundgasmIE(url, user_name, display_id)

# Generated at 2022-06-14 17:01:46.687851
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST == {'url': 'http://soundgasm.net/u/ytdl',
                         'info_dict': {'id': 'ytdl'},
                         'playlist_count': 1}

test_SoundgasmProfileIE()

# Generated at 2022-06-14 17:01:54.888284
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    given_parameters = 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert(given_parameters.__class__ == str)
    given_parameters = SoundgasmIE._VALID_URL
    assert(given_parameters.__class__ == str)
    given_parameters = SoundgasmIE._TEST
    assert(given_parameters.__class__ == dict)
    given_parameters = SoundgasmIE._TEST['url']
    assert(given_parameters.__class__ == str)
    given_parameters = SoundgasmIE._TEST['info_dict']
    assert(given_parameters.__class__ == dict)
    given_parameters = SoundgasmIE._TEST['info_dict']['id']

# Generated at 2022-06-14 17:01:56.624592
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl', '')

# Generated at 2022-06-14 17:01:57.501412
# Unit test for constructor of class SoundgasmProfileIE

# Generated at 2022-06-14 17:02:07.613028
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	# Test the constructor of class SoundgasmProfileIE
	assert SoundgasmProfileIE().ie_key() == 'Soundgasm'
	assert SoundgasmProfileIE().ie_key() == 'Soundgasm:profile'
	assert SoundgasmProfileIE().suitable('http://soundgasm.net/u/ytdl')
	assert not SoundgasmProfileIE().suitable('http://soundgasm.net/u/ytdl/Piano-sample')
	# Test the _real_extract() method of class SoundgasmProfileIE

# Generated at 2022-06-14 17:02:10.838495
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE()._VALID_URL == SoundgasmIE._VALID_URL

# Generated at 2022-06-14 17:02:20.418929
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    a = SoundgasmIE('Soundgasm', 'http://soundgasm.net/u/ytdl/Piano-sample')
    assert a.ie_key() == 'Soundgasm'
    assert a._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:22.300037
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')


# Generated at 2022-06-14 17:02:29.331569
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    try:
        from ..utils import test
        from .common import SoundgasmProfileIE

        ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
        assert isinstance(ie, InfoExtractor)
        assert isinstance(ie, SoundgasmProfileIE)
        assert ie.IE_NAME == 'Soundgasm'

    except Exception as e:
        print("Unable to import modules")
        print(e)


# Generated at 2022-06-14 17:04:48.223845
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    extractor = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    assert extractor._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:04:54.439256
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	ie = SoundgasmProfileIE()
	ie.url = 'http://soundgasm.net/u/ytdl'
	ie.info_dict['id'] = 'ytdl'
	ie.playlist_count = 1
	assert ie.url == 'http://soundgasm.net/u/ytdl'
	assert ie.info_dict['id'] == 'ytdl'
	assert ie.playlist_count == 1

# Generated at 2022-06-14 17:05:04.773336
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Unit test for the constructor of class SoundgasmIE.
    """

    # Test with a valid URL.
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:05:08.087444
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        # User passes an object of class str
        assert SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample') is not None
    except Exception:
        assert False  # An unexpected exception is raised!


# Generated at 2022-06-14 17:05:14.329233
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'



# Generated at 2022-06-14 17:05:19.858632
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    # SoundgasmIE(InfoExtractor)._real_extract is a private method
    result = SoundgasmIE(InfoExtractor)._real_extract(url)
    assert 'id' in result
    assert 'display_id' in result
    assert 'url' in result
    assert 'vcodec' in result
    assert 'title' in result
    assert 'description' in result
    assert 'uploader' in result


# Generated at 2022-06-14 17:05:22.111747
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE(None)._VALID_URL == SoundgasmIE._VALID_URL


# Generated at 2022-06-14 17:05:24.026660
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ytdl = SoundgasmProfileIE()
    ytdl._match_id('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 17:05:26.698873
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Test if SoundgasmProfileIE is constructed properly
    # with key 'ytdl' and its url 'http://soundgasm.net/u/ytdl'
    assert SoundgasmProfileIE._match_id(SoundgasmProfileIE._TEST["url"]) is \
        SoundgasmProfileIE._TEST["info_dict"]["id"]

# Generated at 2022-06-14 17:05:29.338672
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'