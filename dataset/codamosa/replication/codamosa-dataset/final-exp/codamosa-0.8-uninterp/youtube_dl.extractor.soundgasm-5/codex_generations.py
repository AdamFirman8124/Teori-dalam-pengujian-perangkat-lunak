

# Generated at 2022-06-14 16:55:36.642988
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE();
    assert ie.IE_NAME == 'soundgasm';

# Generated at 2022-06-14 16:55:40.030174
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm = SoundgasmIE()
    assert hasattr(soundgasm, 'SoundgasmIE') is not None
    assert isinstance(soundgasm.SoundgasmIE, type) is True

# Generated at 2022-06-14 16:55:43.073770
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL is not None
    assert ie._TEST is not None
    assert ie._TEST['url'] is not None

# Generated at 2022-06-14 16:55:55.125322
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    info = SoundgasmProfileIE()._real_extract('http://soundgasm.net/u/ytdl')
    assert 'playlist' in info
    assert 'entries' in info
    assert 'id' in info
    assert 'playlist_count' in info
    assert 'playlist_mincount' in info
    assert 'playlist_type' in info
    assert 'playlist_title' in info
    assert 'uploader' in info
    assert 'description' in info
    assert 'extractor' in info
    assert 'playlist_uploader' in info
    assert 'playlist_upload_date' in info
    assert 'playlist_last_updated' in info
    assert 'thumbnail' in info
    assert 'age_limit' in info
    assert 'subtitles' in info

# Generated at 2022-06-14 16:55:57.320498
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = "http://soundgasm.net/u/ytdl"
    profile = SoundgasmProfileIE()
    profile._real_extract(url)

# Generated at 2022-06-14 16:56:10.443410
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

    # Test for functionality of SoundgasmIE
    assert SoundgasmIE()._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    
    # Test for functionality of test

# Generated at 2022-06-14 16:56:18.813534
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """The unit test for SoundgasmIE constructor."""
    from soundgasm import SoundgasmIE
    from utils import check_test

    test_video = SoundgasmIE(None)
    test_video._test('http://soundgasm.net/u/ytdl/Piano-sample', '010082a2c802c5275bb00030743e75ad', '88abd86ea000cafe98f96321b23cc1206cbcbcc9')
    test_video._test('http://soundgasm.net/u/ytdl/Piano-sample', '010082a2c802c5275bb00030743e75ad', '88abd86ea000cafe98f96321b23cc1206cbcbcc9')


# Generated at 2022-06-14 16:56:24.253480
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    unit_test_instance = SoundgasmProfileIE('')
    assert(unit_test_instance.name == 'Soundgasm')
    assert(unit_test_instance.IE_NAME == 'soundgasm:profile')
    assert(unit_test_instance._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')

# Generated at 2022-06-14 16:56:27.805497
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie  = SoundgasmProfileIE()

# Generated at 2022-06-14 16:56:32.161386
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE()._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:56:41.526110
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    isinstance(SoundgasmProfileIE(None), InfoExtractor)

# Generated at 2022-06-14 16:56:42.930738
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert type(SoundgasmIE({})) == SoundgasmIE

# Generated at 2022-06-14 16:56:45.901230
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie_obj = SoundgasmIE()
    ie_obj.IE_NAME.encode('ascii')
    ie_obj._VALID_URL.encode('ascii')
    ie_obj._TEST.encode('ascii')

# Generated at 2022-06-14 16:56:57.331363
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    obj = SoundgasmProfileIE(url)
    
    assert obj.IE_NAME == 'soundgasm:profile'
    assert obj._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert obj._TEST.get('url') == 'http://soundgasm.net/u/ytdl'
    assert obj._TEST.get('info_dict').get('id') == 'ytdl'
    assert obj._TEST.get('playlist_count') == 1
    assert obj.IE_NAME == 'soundgasm:profile'
    # Other values (ie_key and info_dict) are tested in other unit

# Generated at 2022-06-14 16:57:04.375513
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    e = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert e._VALID_URL == '^https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)$'
    assert e._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert e._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'
    assert e._TEST['info_dict']['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
   

# Generated at 2022-06-14 16:57:10.731030
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._TEST['url'] == 'http://soundgasm.net/u/ytdl'


# Generated at 2022-06-14 16:57:11.123025
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
   SoundgasmIE()

# Generated at 2022-06-14 16:57:14.634438
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie_profile = SoundgasmProfileIE()
    assert ie_profile.IE_NAME == 'soundgasm:profile' and ie_profile._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:57:22.453439
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm = SoundgasmProfileIE()
    assert soundgasm.IE_NAME == 'soundgasm:profile'
    assert soundgasm._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert soundgasm._TEST['url'] == 'http://soundgasm.net/u/ytdl'
    assert soundgasm._TEST['info_dict']['id'] == 'ytdl'
    assert soundgasm._TEST['playlist_count'] == 1


# Generated at 2022-06-14 16:57:25.409452
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE.suitable('http://soundgasm.net/u/ytdl/')

# Generated at 2022-06-14 16:57:41.682536
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:57:43.720327
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:57:55.321233
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('https://soundgasm.net/u/ytdl/Piano-sample')
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:58:02.616702
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE('soundgasm', 'http://soundgasm.net/u/ytdl/Piano-sample')
    assert obj.url == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert obj.display_id == 'Piano-sample'
    assert obj.user == 'ytdl'
    assert obj.re == re.compile(r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')
    assert obj.video_id == 'http://soundgasm.net/u/ytdl/Piano-sample'

# Generated at 2022-06-14 16:58:08.539781
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    Test = SoundgasmIE()
    Test._VALID_URL = 'http://soundgasm.net/u/ytdl/Piano-sample'
    Test._real_extract(Test._VALID_URL)

# Generated at 2022-06-14 16:58:10.951062
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE().extract('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:58:21.676245
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test_object_1 = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    test_object_2 = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample", 1)
    test_object_3 = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample", 1, 'abc')
    test_object_4 = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample", 1, 'abc', 'def')
    test_object_5 = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample", 1, 'abc', 'def', True)

# Generated at 2022-06-14 16:58:23.586644
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    a = SoundgasmIE()
    assert a.IE_NAME == 'Soundgasm'


# Generated at 2022-06-14 16:58:36.481943
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

    test_label1 = [
        'SoundgasmIE.line_end',
        'SoundgasmIE.line_start',
        'SoundgasmIE.line_no'
    ]

    test_result1 = [
        'line:294',
        'line:292',
        'line:293'
    ]

    test_label2 = [
        'SoundgasmIE.line_end',
        'SoundgasmIE.line_start',
        'SoundgasmIE.line_no'
    ]

    test_result2 = [
        'line:294',
        'line:292',
        'line:293'
    ]

    with open("soundgasm.py", "r", encoding='utf-8') as file:
        file_content = file.read().splitlines()
        test_class_

# Generated at 2022-06-14 16:58:38.709203
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # I should create an instance of SoundgasmIE
    instance = SoundgasmIE()
    assert(isinstance(instance, SoundgasmIE))

# Generated at 2022-06-14 16:59:12.262673
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie=SoundgasmProfileIE()
    print(ie.extract('http://soundgasm.net/u/ytdl'))


# Generated at 2022-06-14 16:59:15.584623
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE({})
    assert ie.ie_key() == 'Soundgasm'
    assert ie.ie_name() == 'Soundgasm'
    assert ie.suitable(None) == False
    assert ie.suitable([]) == False
    assert ie.suitable({}) == False
    assert ie.suitable('http://soundgasm.net/u/ytdl/Piano-sample') == True
    assert ie.suitable('http://soundgasm.net/u/ytdl') == False

# Generated at 2022-06-14 16:59:27.577604
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Incorrect URL
    incorrect_url = 'http://soundgasm.net/'
    incorrect_url_info = SoundgasmIE()._real_extract(incorrect_url)
    assert incorrect_url_info is None
    # URL of profile
    url = 'http://soundgasm.net/u/ytdl/#'
    assert not SoundgasmIE._VALID_URL(url)
    # URL of audio
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    mobj = re.match(SoundgasmIE._VALID_URL, url)
    assert mobj.group('user') == 'ytdl'
    assert mobj.group('display_id') == 'Piano-sample'

# Generated at 2022-06-14 16:59:29.129711
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    result = SoundgasmIE()
    assert result.IE_NAME == 'soundgasm.net'

# Generated at 2022-06-14 16:59:35.269767
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    obj = SoundgasmIE()
    test_SoundgasmIE.asserts = obj
    test_SoundgasmIE.asserts.run(url)


# Generated at 2022-06-14 16:59:39.881835
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from .common import FakeYDL
    ydl = FakeYDL()
    IE = SoundgasmIE(ydl)
    assert IE.suitable('http://soundgasm.net/u/ytdl/Piano-sample')
    assert IE.suitable('http://www.soundgasm.net/u/ytdl/Piano-sample')
    assert IE.suitable('http://soundgasm.net/u/ytdl')
    assert not IE.suitable('http://soundgasm.net/')


# Generated at 2022-06-14 16:59:41.829080
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	sg = SoundgasmIE()
	assert sg != None

# Unit test SoundgasmIE.extract method

# Generated at 2022-06-14 16:59:43.637806
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE()
    except:
        assert False

# Generated at 2022-06-14 16:59:49.099792
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    info = SoundgasmIE()._real_extract({'url': 'http://soundgasm.net/u/ytdl/Piano-sample'})
    assert info['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'

# Generated at 2022-06-14 16:59:52.983320
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sound_class = SoundgasmIE()
    assert sound_class.IE_NAME == 'soundgasm'
    assert sound_class.extract('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 17:01:14.903157
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test = SoundgasmProfileIE()
    assert test



# Generated at 2022-06-14 17:01:21.805926
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE._VALID_URL=='https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 17:01:26.338264
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_ie = SoundgasmProfileIE()
    assert profile_ie.IE_NAME == 'soundgasm:profile'
    assert profile_ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'



# Generated at 2022-06-14 17:01:29.610231
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	url = 'http://soundgasm.net/u/ytdl/'
	test = {
		'url': url,
		'info_dict': {
			'id': 'ytdl',
		},
		'playlist_count': 1,
	}
	SoundgasmProfileIE()._real_extract(url)

# Generated at 2022-06-14 17:01:40.004402
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	valid_url1 = 'https://soundgasm.net/u/ytdl/Piano-sample'
	valid_url2 = 'http://soundgasm.net/u/ytdl/Piano-sample'
	valid_url3 = 'https://soundgasm.net/u/ytdl/Piano-sample/'
	valid_url4 = 'http://soundgasm.net/u/ytdl/Piano-sample/'
	invalid_url1 = 'http://www.soundgasm.net/u/ytdl'
	invalid_url2 = 'http://soundgasm.net/u/ytdl'
	invalid_url3 = 'https://soundgasm.net/u/ytdl/Piano-sample#'

# Generated at 2022-06-14 17:01:51.154437
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE("http://soundgasm.net/u/ytdl")
    assert(ie.IE_NAME == 'soundgasm:profile')
    assert(ie.IE_DESC == 'Soundgasm profiles')
    assert(ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')
    assert(ie._TEST == {'url': 'http://soundgasm.net/u/ytdl', 'info_dict': {'id': 'ytdl'}, 'playlist_count': 1})

# Generated at 2022-06-14 17:01:53.505079
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    inst = SoundgasmProfileIE('id', 'url', 'title')
    assert isinstance(inst, SoundgasmProfileIE)


# Generated at 2022-06-14 17:01:55.503350
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE(SoundgasmProfileIE.IE_NAME, SoundgasmProfileIE._VALID_URL, SoundgasmProfileIE._TEST)

# Generated at 2022-06-14 17:02:00.150138
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    inst = SoundgasmProfileIE()
    assert inst._VALID_URL is not None
    info = inst._real_extract(inst._TEST['url'])
    assert info['id'] == inst._TEST['info_dict']['id']
    assert len(info['entries']) == inst._TEST['playlist_count']
    assert info['entries'][0]['id'] is not None
    assert info['entries'][0]['title'] is not None

# Generated at 2022-06-14 17:02:02.727355
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Test constructor
    SoundgasmProfileIE('http://www.soundgasm.net/u/ytdl')

# Generated at 2022-06-14 17:03:32.760209
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    util.initialize_test_module()

    # check that the constructor does not raise any exception (for #4126)
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 17:03:35.263049
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE()
    except:
        return False
    else:
        return True


# Generated at 2022-06-14 17:03:37.640653
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    downloader = InfoExtractor()
    assert  unicode(downloader) == "Soundgasm.net content downloader"


# Generated at 2022-06-14 17:03:40.485247
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    result = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert len(result) == 9

# Generated at 2022-06-14 17:03:42.156143
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE()._VALID_URL == SoundgasmIE._VALID_URL

# Generated at 2022-06-14 17:03:49.425426
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """Tests the Video Search Engine."""
    from unittest import TestCase, TextTestRunner, TestLoader, main

    class TestSoundgasmProfileIE(TestCase):
        def setUp(self):
            """Set up some variables to be used by the tests."""
            self.test_urls = {
                'ytdl': 'http://soundgasm.net/u/ytdl',
            }

            self.urls = {
                'Profiles': {
                    'ytdl': 'http://soundgasm.net/u/ytdl',
                },
            }


# Generated at 2022-06-14 17:04:00.181442
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    IE_NAME = 'soundgasm:profile'
    test_url = 'http://soundgasm.net/u/ytdl'
    test_id = 'ytdl'
    test_result = ['http://soundgasm.net/u/ytdl/Piano-sample', 'http://soundgasm.net/u/ytdl/Piano']

    sound_gasm_profile_ie = SoundgasmProfileIE()
    sound_gasm_profile_ie.IE_NAME = IE_NAME

    assert sound_gasm_profile_ie._match_id(test_url) == test_id

    result = sound_gasm_profile_ie.url_result('http://soundgasm.net/u/ytdl/Piano-sample', 'Soundgasm')
    assert result['url'] == test_result

# Generated at 2022-06-14 17:04:01.631876
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    print(__file__)


if __name__ == '__main__':
    test_SoundgasmIE()

# Generated at 2022-06-14 17:04:04.780484
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    _test = SoundgasmProfileIE(SoundgasmProfileIE._VALID_URL, SoundgasmProfileIE._TEST)
    assert _test.test_result() == False

# Generated at 2022-06-14 17:04:08.716032
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('SoundgasmProfileIE')
    assert ie.IE_NAME == 'soundgasm:profile'