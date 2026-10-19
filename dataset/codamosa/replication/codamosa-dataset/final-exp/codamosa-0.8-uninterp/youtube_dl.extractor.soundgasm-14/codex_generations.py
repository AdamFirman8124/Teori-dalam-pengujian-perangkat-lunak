

# Generated at 2022-06-14 16:55:41.839079
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile = SoundgasmProfileIE()
    # Ensure that SoundgasmProfileIE, an instance of class InfoExtractor, is
    # correctly constructed. (This test, though small, might catch like
    # errors early on.)
    assert profile.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:55:43.108966
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:55:50.466785
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from . import _mock_download
    _mock_download.mock_download(
        'http://soundgasm.net/u/ytdl/Piano-sample',
        'play_page.html')
    _mock_download.mock_download(
        'http://d1.soundgasm.net/sounds/88abd86ea000cafe98f96321b23cc1206cbcbcc9/2.m4a',
        'audio.m4a')

    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    ie = SoundgasmIE()
    ie._download_webpage = _mock_download.mock_download_webpage(ie, [url])

    # download audio in the webpage

# Generated at 2022-06-14 16:55:52.711176
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    c = ie.build_url('http://soundgasm.net/u/ytdl/Piano-sample')
    assert c == 'http://soundgasm.net/u/ytdl/Piano-sample'


# Generated at 2022-06-14 16:55:53.704884
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE._VALID_URL

# Generated at 2022-06-14 16:55:54.218347
# Unit test for constructor of class SoundgasmIE

# Generated at 2022-06-14 16:55:59.949081
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    unit_test_object = SoundgasmIE(None)

# Generated at 2022-06-14 16:56:12.955841
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    To test constructor of class SoundgasmIE
    """
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    IE_NAME = 'soundgasm'
    mobj = re.match(SoundgasmIE._VALID_URL, url)
    display_id = mobj.group('display_id')
    webpage = SoundgasmIE._download_webpage(SoundgasmIE(), url, display_id)
    audio_url = SoundgasmIE._html_search_regex(
        SoundgasmIE(), r'(?s)m4a\s*:\s*(["\'])(?P<url>(?:(?!\1).)+)\1', webpage,
        'audio URL', group='url')

# Generated at 2022-06-14 16:56:17.041456
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Unit test for constructor of class SoundgasmIE
    """
    obj = SoundgasmIE()
    assert obj.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:56:18.840653
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE().IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:56:26.183893
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    sgpIE = SoundgasmProfileIE('SoundgasmProfile')
    assert sgpIE.ie_key() == 'SoundgasmProfile'



# Generated at 2022-06-14 16:56:36.112803
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm_ie = SoundgasmIE()
    assert soundgasm_ie.IE_NAME == 'soundgasm'
    assert soundgasm_ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert soundgasm_ie._TEST["url"] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert soundgasm_ie._TEST["md5"] == '010082a2c802c5275bb00030743e75ad'

# Generated at 2022-06-14 16:56:38.191235
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    testObj = SoundgasmIE()
    assert testObj.IE_NAME == 'SoundgasmIE'

# Generated at 2022-06-14 16:56:44.292029
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    info_extractor = SoundgasmIE('soundgasm', 'http://www.soundgasm.net/u/ytdl/Piano-sample')

    assert info_extractor._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:56:48.354633
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test = 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert SoundgasmIE._VALID_URL == test

# Generated at 2022-06-14 16:56:49.620337
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()



# Generated at 2022-06-14 16:56:50.657095
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sIE = SoundgasmIE()
    assert sIE

# Generated at 2022-06-14 16:57:00.452738
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE_NAME = 'soundgasm'
    _VALID_URL = r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:57:12.849665
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)/?'

# Generated at 2022-06-14 16:57:22.423601
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm_IE = SoundgasmIE()
    assert soundgasm_IE.IE_NAME == 'soundgasm' \
        and soundgasm_IE.IE_DESC == 'Soundgasm' \
        and soundgasm_IE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)' \
        and soundgasm_IE._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample' \
        and soundgasm_IE._TEST['md5'] == '010082a2c802c5275bb00030743e75ad' \
        and soundg

# Generated at 2022-06-14 16:57:40.879018
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    display_id = 'Piano-sample'
    mobj = re.match(SoundgasmIE._VALID_URL, url)
    assert mobj.group('user') == 'ytdl'
    audio_id = '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    webpage = SoundgasmIE._download_webpage(url, display_id)
    audio_url = SoundgasmIE._html_search_regex(r'(?s)m4a\s*:\s*(["\'])(?P<url>(?:(?!\1).)+)\1', webpage,
                                               'audio URL', group='url')
    equal_mobj = re.match

# Generated at 2022-06-14 16:57:41.915175
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sg = SoundgasmIE(InfoExtractor())
    assert sg is not None


# Generated at 2022-06-14 16:57:49.793279
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_cases = [
        {
            'url': 'http://soundgasm.net/u/ytdl',
            'info_dict': {
                'id': 'ytdl',
            },
            'playlist_count': 1,
        }
    ]
    for t_case in test_cases:
        ie = SoundgasmProfileIE()
        ie.extract(t_case['url'])

# Generated at 2022-06-14 16:57:52.371375
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    x = SoundgasmProfileIE()
    assert (x.IE_NAME) == "soundgasm:profile"


# Generated at 2022-06-14 16:57:54.270462
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE('ytdl', 'http://soundgasm.net/u/ytdl/', 'Soundgasm') != None

# Generated at 2022-06-14 16:57:57.786009
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie._VALID_URL == "https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)"

# Generated at 2022-06-14 16:58:07.558513
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    #set the value of url
    url = 'http://soundgasm.net/u/ytdl'
    assert url == 'http://soundgasm.net/u/ytdl'
    #create a object soundgasmProfileIE
    soundgasmProfileIE = SoundgasmProfileIE()
    assert soundgasmProfileIE.IE_NAME == 'SoundgasmProfileIE'
    assert soundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

    #test the function _real_extract
    #give the parameter url
    audio_url = soundgasmProfileIE._real_extract(url)
    #dict the value of entries

# Generated at 2022-06-14 16:58:19.583835
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE._TEST['url'] == "http://soundgasm.net/u/ytdl"
    assert SoundgasmProfileIE._TEST['info_dict']['id'] == "ytdl"
    assert SoundgasmProfileIE._TEST['playlist_count'] == 1
    assert SoundgasmProfileIE._VALID_URL == "https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$"
    assert SoundgasmProfileIE.IE_NAME == "soundgasm:profile"
   # assert SoundgasmProfileIE._real_extract(http://soundgasm.net/u/ytdl)

    #assert SoundgasmProfileIE._real_extract(http://soundgasm.net/u/y

# Generated at 2022-06-14 16:58:22.828114
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm_profile_ie = SoundgasmProfileIE()
    assert_equals(soundgasm_profile_ie.IE_NAME, 'soundgasm:profile')
    

# Generated at 2022-06-14 16:58:26.276493
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    testDict={"status":"1","comments":[],"path":"\/u\/ytdl\/Piano-sample"}
    soundgasmInstance=SoundgasmIE()
    soundgasmInstance.extract()
    assert(testDict==soundgasmInstance.extract())

# Generated at 2022-06-14 16:58:49.534017
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert SoundgasmIE(SoundgasmIE())._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:58:54.920546
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:58:58.607345
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_url = "http://soundgasm.net/u/ytdl"
    test_result = SoundgasmProfileIE(test_url)
    assert isinstance(test_result, InfoExtractor)


# Generated at 2022-06-14 16:59:01.215987
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    instance = SoundgasmProfileIE('Soundgasm')
    assert instance.ie_key() == 'SoundgasmProfile'

# Generated at 2022-06-14 16:59:03.572583
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    the_test = SoundgasmProfileIE()
    assert the_test.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:59:07.996612
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile = SoundgasmProfileIE(None)._real_extract(u'http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:59:15.737972
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    l = SoundgasmProfileIE()

    assert l._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert l._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }

# Generated at 2022-06-14 16:59:21.957426
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    instance = SoundgasmProfileIE()
    assert  instance is not None
    assert instance.IE_NAME == 'soundgasm:profile'
    assert instance.VALID_URL == SoundgasmProfileIE._VALID_URL
    assert instance.VALID_URL == SoundgasmProfileIE._VALID_URL

# Generated at 2022-06-14 16:59:25.150336
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 16:59:27.052744
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    e = SoundgasmProfileIE()
    assert e.IE_NAME == 'SoundgasmProfileIE'

# Generated at 2022-06-14 17:00:12.102129
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sample_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    expected_md5 = '010082a2c802c5275bb00030743e75ad'
    sample_ie = SoundgasmIE()
    assert sample_ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert sample_ie._TEST['url'] == sample_url
    assert sample_ie._TEST['md5'] == expected_md5

# Generated at 2022-06-14 17:00:13.280640
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 17:00:14.160854
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert isinstance(SoundgasmProfileIE(), SoundgasmProfileIE)

# Generated at 2022-06-14 17:00:15.065076
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_ie = SoundgasmProfileIE(None)

# Generated at 2022-06-14 17:00:16.870737
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 17:00:24.084148
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    import unittest
    import pprint
    class TestSoundgasmIE(unittest.TestCase):
        def test_soundgasmie(self):
            soundgasmIE = SoundgasmIE()
            mobj = re.match(soundgasmIE._VALID_URL, soundgasmIE._TEST.get('url'))
            pprint.pprint(soundgasmIE._real_extract(soundgasmIE._TEST.get('url')))

            self.assertEqual(mobj.group('display_id'), soundgasmIE._TEST.get('info_dict').get('display_id'))
            self.assertEqual(mobj.group('display_id'), soundgasmIE._TEST.get('info_dict').get('title'))

# Generated at 2022-06-14 17:00:31.133541
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """
    Unit test for constructor of class SoundgasmProfileIE
    """
    IE = SoundgasmProfileIE()

    assert IE.IE_NAME == 'soundgasm:profile'
    assert IE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 17:00:33.641939
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    except Exception as e:
        print(e)
        assert False

# Generated at 2022-06-14 17:00:36.451369
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    SoundgasmProfileIE().suitable(url) is True


# Generated at 2022-06-14 17:00:43.938597
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie.VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:13.929021
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE()
    except:
        return False
    return True

# Generated at 2022-06-14 17:02:18.455740
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = "https://soundgasm.net/u/ytdl"
    obj = SoundgasmProfileIE()
    assert obj._VALID_URL == "https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$"


# Generated at 2022-06-14 17:02:30.435906
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
        # Test to ensure URL is good
        u = SoundgasmIE()
        assert u._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

        # Test to ensure regular expressions are good

# Generated at 2022-06-14 17:02:31.326768
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    instance = SoundgasmProfileIE()

# Generated at 2022-06-14 17:02:35.039817
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    try:
        soundgasm_profile_unit_test = SoundgasmProfileIE()
    except:
        soundgasm_profile_unit_test = None

    assert soundgasm_profile_unit_test is not None

# Generated at 2022-06-14 17:02:36.780925
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl', 'Soundgasm')

# Generated at 2022-06-14 17:02:38.548699
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Construct object for class SoundgasmIE
    SoundgasmIE(None, None)


# Generated at 2022-06-14 17:02:39.521876
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    instance = SoundgasmIE(InfoExtractor())

# Generated at 2022-06-14 17:02:46.243316
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    r = SoundgasmIE()
    assert r.IE_NAME == 'soundgasm'
    assert r._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:48.483095
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile = SoundgasmProfileIE()
    assert profile.IE_NAME == 'soundgasm:profile'