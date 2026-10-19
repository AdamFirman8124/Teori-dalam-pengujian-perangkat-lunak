

# Generated at 2022-06-14 16:55:37.831800
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert(SoundgasmProfileIE.IE_NAME == 'soundgasm:profile')
    assert(SoundgasmProfileIE(SoundgasmProfileIE.IE_NAME, 'test') != None)
    assert(SoundgasmProfileIE(SoundgasmProfileIE.IE_NAME, 'test').test() != None)


# Generated at 2022-06-14 16:55:39.712314
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

    # Test constructor of SoundgasmIE 
    SoundgasmIE(None)

# Generated at 2022-06-14 16:55:45.287905
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE_TEST = SoundgasmIE._TEST
    e = SoundgasmIE(IE_TEST)
    assert e.IE_NAME == 'soundgasm'
    assert e._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert e._TEST == IE_TEST

# Generated at 2022-06-14 16:55:49.387688
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    info = SoundgasmIE().extract(r'http://soundgasm.net/u/ytdl/Piano-sample')
    assert info.get('title') == 'Piano sample'

# Generated at 2022-06-14 16:55:50.414953
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    sProfile = SoundgasmProfileIE()

# Generated at 2022-06-14 16:55:55.659055
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	ie = SoundgasmIE("")
	assert ie.NI_NAME == 'soundgasm'
	assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 16:55:58.250896
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url='http://soundgasm.net/u/ytdl'
    soundgasm_profile = SoundgasmProfileIE()
    soundgasm_profile.url = url
    assert isinstance(soundgasm_profile, InfoExtractor)

# Generated at 2022-06-14 16:55:59.100214
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:56:12.074132
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:56:24.004404
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    ie = SoundgasmIE()._real_extract(url)
    assert ie['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert ie['display_id'] == 'Piano-sample'
    assert ie['url'] == 'http://sgs2.sgs.ovh/sgs/88abd86ea000cafe98f96321b23cc1206cbcbcc9/Piano-sample.m4a'
    assert ie['vcodec'] == 'none'
    assert ie['title'] == 'Piano sample'
    assert ie['description'] == 'Royalty Free Sample Music'
    assert ie['uploader'] == 'ytdl'

# Generated at 2022-06-14 16:56:32.248978
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:56:39.984512
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	import unittest
	class Test(unittest.TestCase):
		def test(self):
			info_extractor = SoundgasmIE('Soundgasm')
			assert info_extractor.ie_key() == 'Soundgasm'
			assert info_extractor.suitable('https://soundgasm.net/u/ytdl/Piano-sample')
			assert info_extractor.suitable('http://soundgasm.net/u/ytdl/Piano-sample')
			assert not info_extractor.suitable('https://soundgasm.net/u/ytdl/Piano-sample.mp3')
			assert not info_extractor.suitable('https://soundgasm.net/u/ytdl/')
			assert not info

# Generated at 2022-06-14 16:56:45.323966
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_url = 'http://soundgasm.net/u/ytdl'
    ie = SoundgasmProfileIE()

    if not ie.suitable(profile_url) or ie.IE_NAME != 'soundgasm:profile':
        # The profile url is not on the list of supported sites?
        raise Exception('Unit test failed!')

    playlist = ie._real_extract(profile_url)


# Generated at 2022-06-14 16:56:47.997453
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	assert isinstance(SoundgasmProfileIE(), InfoExtractor)

# Generated at 2022-06-14 16:56:55.111967
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    class_ie = SoundgasmIE()
    assert(class_ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')
    assert(class_ie.IE_NAME == 'soundgasm')
    assert(class_ie._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample')
    assert(class_ie._TEST['md5'] == '010082a2c802c5275bb00030743e75ad')

# Generated at 2022-06-14 16:56:56.128220
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:57:00.820611
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

if __name__ == '__main__':
    test_SoundgasmIE();

# Generated at 2022-06-14 16:57:10.776646
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST['url'] == 'http://soundgasm.net/u/ytdl'
    assert ie._TEST['info_dict'] == {
        'id': 'ytdl',
    }
    assert ie._TEST['playlist_count'] == 1
# end of unit test for constructor of class SoundgasmProfileIE


# Generated at 2022-06-14 16:57:12.624137
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('SoundgasmProfileIE','http://soundgasm.net/u/ytdl','ytdl','ytdl','ytdl')

    assert(ie.playlist_mincount == 1)

# Generated at 2022-06-14 16:57:14.140979
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE('soundgasm')
    except KeyError:
        pass

# Generated at 2022-06-14 16:57:26.869610
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    print("\nTest SoundgasmIE constructor, should not raise exception...")
    print("\nUnit test for SoundgasmIE passed.\n")


# Generated at 2022-06-14 16:57:31.754956
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # For constructor of class SoundgasmIE
    # Given the arguments are nominal values
    # When construct a new SoundgasmIE
    # Then the instance should be created
    # noinspection PyTypeChecker
    SoundgasmIE(None, {})


# Generated at 2022-06-14 16:57:33.937836
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm_ie = SoundgasmIE()
    assert soundgasm_ie.IE_NAME == 'Soundgasm'


# Generated at 2022-06-14 16:57:42.545375
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    filename = 'test_SoundgasmIE.xml'
    try:
        # read xml file
        with open(filename, 'r') as fp:
            data = fp.read()
    except:
        print("can not find file " + filename)
        assert(0)
    # write json file
    js = SoundgasmIE()._json_ld(data, 'http://soundgasm.net/', transform_source=None)
    print('js: ' + js)
    assert(js is not None)


# Generated at 2022-06-14 16:57:46.355594
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Check that the constructor's signature is correct
    instance = SoundgasmProfileIE('soundgasm:profile')
    instance = SoundgasmProfileIE(ie='soundgasm:profile')
    instance = SoundgasmProfileIE(ie_key='soundgasm:profile')
    instance = SoundgasmProfileIE(name='soundgasm:profile')

# Generated at 2022-06-14 16:57:52.722762
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert SoundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 16:57:54.461155
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = SoundgasmProfileIE._TEST['url']
    assert SoundgasmProfileIE._VALID_URL == url

# Generated at 2022-06-14 16:57:57.934193
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Testing constructor of class SoundgasmIE
    assert not SoundgasmIE._download_webpage(None, None)

    # Testing class SoundgasmIE
    SoundgasmIE()._real_extract('http://soundgasm.net/u/ytdl/Piano-sample')


# Generated at 2022-06-14 16:57:59.914325
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    instance = SoundgasmProfileIE()
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:58:01.975244
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert isinstance(SoundgasmProfileIE(), InfoExtractor)
# End Unit test for constructor of class SoundgasmProfileIE

# Generated at 2022-06-14 16:58:27.053541
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Test constructor of SoundgasmIE class
    """
    x = SoundgasmIE()
    assert x.name == "Soundgasm"
    assert x.ie_key == "Soundgasm"
    assert x.ie_name == "Soundgasm"
    assert x._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert x.player_url == None

# Generated at 2022-06-14 16:58:34.663267
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        S = SoundgasmIE()
    except TypeError:
        print("TypeError: Wrong constructor for SoundgasmIE class was called")
        raise Exception
    test_url = "http://soundgasm.net/u/ytdl/Piano-sample"
    test_video_id = '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    test_video_title = 'Piano sample'
    test_video_description = 'Royalty Free Sample Music'
    test_video_uploader = 'ytdl'
    test_video_vcodec = 'none'
    # Test _real_extract method on SoundgasmIE class

# Generated at 2022-06-14 16:58:36.570590
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    my_object = SoundgasmProfileIE()
    assert my_object is not None

# Generated at 2022-06-14 16:58:37.478717
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:58:49.468550
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():

    from soundgasm_profile_ie import SoundgasmProfileIE
    soundgasm_profile_ie = SoundgasmProfileIE()
    print("\nTesting for URL: http://soundgasm.net/u/ytdl:\n")
    print("\nURL: " + soundgasm_profile_ie._VALID_URL)
    print("\nExpression: " + soundgasm_profile_ie._TEST['url'])
    print("\nRegex searches: \n"
          "\nid: " + str(soundgasm_profile_ie._TEST['info_dict'].get('id')) +
          "\nplaylist_count: " + str(soundgasm_profile_ie._TEST.get('playlist_count')) + "\n")

# Generated at 2022-06-14 16:58:53.801495
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """
    Basic test for SoundgasmProfileIE.
    """
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    # ie.download()

# Generated at 2022-06-14 16:59:04.963820
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('soundgasm.net', '8701880e0f9831d7ff8b8a75c8718d9ceeb38e7a',
                     'http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert ie._downloa
    assert ie.IE_NAME == 'soundgasm'
    assert ie.display_id == 'Piano-sample'



# Generated at 2022-06-14 16:59:07.283043
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from .common import _make_valid_url
    _make_valid_url("http://soundgasm.net/u/ytdl/Piano-sample")

# Generated at 2022-06-14 16:59:11.201566
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    ie = SoundgasmIE()
    ie.download(url)


# Generated at 2022-06-14 16:59:19.818859
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():

    assert SoundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert SoundgasmProfileIE._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }
    assert SoundgasmProfileIE.IE_NAME == 'soundgasm:profile'
    assert SoundgasmProfileIE._real_extract('http://soundgasm.net/u/superjeenius')


# Generated at 2022-06-14 16:59:58.825611
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Returns the total number of audios on the profile page
    # Test with two different profile pages
    test_profiles = ['http://soundgasm.net/u/ytdl', 
                     'http://soundgasm.net/u/lady-fucks']
    
    for test_profile in test_profiles:
        x = SoundgasmProfileIE()
        audio_total = len(x._extract_playlist(test_profile))
        y = SoundgasmIE()
        
        assert y.suitable(test_profile), 'Invalid links'
        assert audio_total > 0, 'Profile is empty'

# Generated at 2022-06-14 17:00:01.918419
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_obj = SoundgasmProfileIE(id='ytdl')
    assert test_obj._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/ytdl/?(?:\#.*)?$'

# Generated at 2022-06-14 17:00:02.673005
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile = SoundgasmProfileIE()
    assert profile

# Generated at 2022-06-14 17:00:11.768515
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    m = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert m.name == 'Soundgasm'
    assert m.url == 'http://soundgasm.net/u/ytdl/Piano-sample'

# Generated at 2022-06-14 17:00:16.635114
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    pattern = re.compile(r'^http://soundgasm\.net/u/ytdl/Piano-sample$')
    assert pattern.match(url) is not None, 'URL "{0}" did not match!'.format(url)

# Generated at 2022-06-14 17:00:25.676324
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    mobj = re.match(SoundgasmIE._VALID_URL, url)
    assert SoundgasmIE._TEST['url'] == url
    display_id = mobj.group('display_id')
    webpage = SoundgasmIE._download_webpage(url, display_id)
    audio_url = SoundgasmIE._html_search_regex(
        r'(?s)m4a\s*:\s*(["\'])(?P<url>(?:(?!\1).)+)\1', webpage,
        'audio URL', group='url')

# Generated at 2022-06-14 17:00:31.236985
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	# temporary: use __main__.test_SoundgasmProfileIE to test
	#test = SoundgasmProfileIE()
	try:
		assert 1/0
	except AssertionError:
		raise AssertionError


# Generated at 2022-06-14 17:00:36.066655
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.name == 'soundgasm:profile'
    assert ie.url == 'http://soundgasm.net/u/ytdl'

# Generated at 2022-06-14 17:00:43.692469
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from nose.tools import assert_equal
    class TestSoundgasmProfileIE:
        def test_unit_test_soundgasm_profile_ie(self):
            test_url_with_one_result = 'http://soundgasm.net/u/ytdl'
            test_url_with_no_result = 'http://soundgasm.net/u/ytdl/no_sound_here'

            # set up test
            test_object_to_test = SoundgasmProfileIE()

            # run method to test
            test_result_one_result = test_object_to_test._real_extract(test_url_with_one_result)
            test_result_no_result = test_object_to_test._real_extract(test_url_with_no_result)

            # test result


# Generated at 2022-06-14 17:00:52.346475
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    assert ie._real_extract(url) == {'display_id': 'Piano-sample', 'description': 'Royalty Free Sample Music', 'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9', 'title': 'Piano sample', 'uploader': 'ytdl', 'vcodec': 'none', 'url': 'https://s3-us-west-2.amazonaws.com/soundgasm-mp3/u/ytdl/Piano-sample.m4a'}


# Generated at 2022-06-14 17:02:17.379766
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    _ = SoundgasmIE('https://soundgasm.net/u/ytdl/Piano-sample').extract()

# Generated at 2022-06-14 17:02:21.339250
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    #The code of this unit test is in the constructor
    SoundgasmProfileIE('SoundgasmProfile')

# Generated at 2022-06-14 17:02:31.715593
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    i = SoundgasmIE()
    vid_url = 'https://soundgasm.net/u/ytdl/Piano-sample'
    md5 = '010082a2c802c5275bb00030743e75ad'
    m4a_url = 'http://soundgasm.net/sound/88abd86ea000cafe98f96321b23cc1206cbcbcc9.' \
              'm4a?dl=1'
    title = 'Piano sample'
    desc = 'Royalty Free Sample Music'
    uploader = 'ytdl'

# Generated at 2022-06-14 17:02:35.841004
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

	# Testing empty constructor
	# assert(SoundgasmIE)
	# Testing non-empty constructor
	# assert(SoundgasmIE(['valid_url']))
	print("Constructor of SoundgasmIE passed unit tests")



# Generated at 2022-06-14 17:02:37.225514
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE(None, None)


# Generated at 2022-06-14 17:02:38.547854
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE(None)
    str(obj)


# Generated at 2022-06-14 17:02:40.226853
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE = SoundgasmIE()
    SoundgasmProfileIE = SoundgasmProfileIE()

# Generated at 2022-06-14 17:02:41.145393
# Unit test for constructor of class SoundgasmIE

# Generated at 2022-06-14 17:02:54.027185
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE = SoundgasmIE()

    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    display_id = 'Piano-sample'
    webpage = IE._download_webpage(url, display_id)

    audio_url = IE._html_search_regex(
        r'(?s)m4a\s*:\s*(["\'])(?P<url>(?:(?!\1).)+)\1', webpage,
        'audio URL', group='url')

    title = IE._search_regex(
        r'<div[^>]+\bclass=["\']jp-title[^>]+>([^<]+)',
        webpage, 'title', default=display_id)


# Generated at 2022-06-14 17:02:58.471979
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
  ie = SoundgasmIE()
  assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'