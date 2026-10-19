

# Generated at 2022-06-14 16:55:43.152498
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm_profileIE = SoundgasmProfileIE("http://soundgasm.net/u/ytdl")
    expected = r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    if soundgasm_profileIE._VALID_URL != expected:
        raise Exception("The regular expression did not match.")

# Generated at 2022-06-14 16:55:47.959374
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    info_dict = {
            'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9',
            'ext': 'm4a',
            'title': 'Piano sample',
            'description': 'Royalty Free Sample Music',
            'uploader': 'ytdl',
            }

    SoundgasmIE(info_dict).download(url)

# Generated at 2022-06-14 16:55:50.466930
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_url = 'http://soundgasm.net/u/ytdl'
    SoundgasmProfileIE()._real_extract(test_url)

# Generated at 2022-06-14 16:55:51.898889
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert 'Soundgasm' in globals()



# Generated at 2022-06-14 16:55:57.208756
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm_instance = SoundgasmIE()
    assert soundgasm_instance.IE_NAME == 'soundgasm'
    assert soundgasm_instance._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 16:56:00.113677
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    print (str(test.__dict__))


# Generated at 2022-06-14 16:56:07.871122
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    assert ie._VALID_URL == 'http://soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie.IE_DESC == 'Soundgasm user profiles'

# Generated at 2022-06-14 16:56:08.599333
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    constructor_test(SoundgasmIE, [])


# Generated at 2022-06-14 16:56:15.871595
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	ie = SoundgasmProfileIE()
	assert ie.IE_NAME == 'soundgasm:profile'
	assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
	assert ie._TEST['url'] == 'http://soundgasm.net/u/ytdl'
	assert ie._TEST['info_dict']['id'] == 'ytdl'
	assert ie._TEST['playlist_count'] == 1


# Generated at 2022-06-14 16:56:23.879417
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    about = "http://soundgasm.net/u/ytdl/Piano-sample"
    ie = SoundgasmIE(about)
    assert isinstance(ie, InfoExtractor), "Class structure is not valid"
    assert ie.IE_NAME == "soundgasm", "Name of class is not valid"
    assert ie._VALID_URL == "https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)", "Regular expression of URL is not valid"

# Generated at 2022-06-14 16:56:35.798629
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    testObj = SoundgasmIE()
    assert testObj.IE_NAME == 'soundgasm'
    assert testObj.testResult() == {'md5': '010082a2c802c5275bb00030743e75ad', 'info_dict': {'title': 'Piano sample', 'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9', 'ext': 'm4a', 'description': 'Royalty Free Sample Music', 'uploader': 'ytdl'}, 'url': 'http://soundgasm.net/u/ytdl/Piano-sample'}


# Generated at 2022-06-14 16:56:37.842048
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    print("Unit test for constructor of class SoundgasmProfileIE")
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:56:39.347015
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:56:41.464109
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:56:49.104858
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

    # Test the instance of SoundgasmIE
    sample_url = "http://soundgasm.net/u/ytdl/Piano-sample"
    t = SoundgasmIE()
    assert(t.suitable(sample_url))
    assert(SoundgasmIE.suitable(sample_url))

    # Test the video information extraction
    info_dict = t.extract(sample_url)
    assert("Piano sample" == info_dict["title"])
    assert("ytdl" == info_dict["uploader"])
    assert("88abd86ea000cafe98f96321b23cc1206cbcbcc9" == info_dict["id"])
    assert("m4a" == info_dict["ext"])
    assert("Royalty Free Sample Music" == info_dict["description"])

# Generated at 2022-06-14 16:56:56.225890
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert ie._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert ie._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'
    assert ie._TEST['info_dict']['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert ie._TEST['info_dict']['ext'] == 'm4a'

# Generated at 2022-06-14 16:57:03.563807
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE(SoundgasmIE.ie_key())
    assert ie.IE_NAME == 'soundgasm'
    assert ie.ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert ie.ie._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert ie.ie._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'

# Generated at 2022-06-14 16:57:06.120373
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    unit_test_url = SoundgasmIE._TEST['url']
    SoundgasmIE(unit_test_url)

# Generated at 2022-06-14 16:57:10.915592
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    import unittest
    class TestSoundgasmProfileIE(unittest.TestCase):
        def setUp(self):
            self.ie = SoundgasmProfileIE()

        def tearDown(self):
            pass

        def test_constructor_exists(self):
            self.assertTrue(self.ie)
    unittest.main()

# Generated at 2022-06-14 16:57:12.347767
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    i = SoundgasmProfileIE()
    assert i.IE_NAME == 'soundgasm:profile'
    assert i.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:57:16.811697
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE(): 
    pass

# Generated at 2022-06-14 16:57:20.380984
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_ie = SoundgasmProfileIE(_test_preload_results={
        'http://soundgasm.net/u/ytdl': 'data'})
    assert profile_ie.IE_NAME == 'soundgasm:profile'



# Generated at 2022-06-14 16:57:33.452993
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    from ..utils import urljoin
    import logging
    logging.disable(logging.CRITICAL)

    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    ie = SoundgasmIE()
    user = 'ytdl'
    display_id = 'Piano-sample'
    _VALID_URL = r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    mobj = re.match(ie._VALID_URL, url)
    id = mobj.group('display_id')
    webpage = ie._download_webpage(url, display_id)

    audio_url = ie._

# Generated at 2022-06-14 16:57:36.235432
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
   SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:57:37.523923
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    AudioDownloader(SoundgasmIE)


# Generated at 2022-06-14 16:57:40.738160
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    obj = SoundgasmProfileIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:57:46.297544
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    vid = SoundgasmIE()._real_extract('http://soundgasm.net/u/ytdl/Piano-sample')
    assert isinstance(vid['id'], basestring)
    assert isinstance(vid['uploader'], basestring)
    assert isinstance(vid['description'], basestring)
    assert isinstance(vid['url'], basestring)
    assert isinstance(vid['display_id'], basestring)
    assert isinstance(vid['title'], basestring)

# Generated at 2022-06-14 16:57:49.996697
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_ie=SoundgasmProfileIE()
    assert profile_ie.IE_NAME == 'soundgasm:profile'
    

# Generated at 2022-06-14 16:57:51.400460
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:57:56.949790
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE({'incognito': True})
    u = 'http://soundgasm.net/u/ytdl'
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert ie._real_extract(u) == {'_type': 'playlist', 'id': u, 'entries': [{'_type': 'url', 'url': url, 'ie_key': 'Soundgasm'}]}

# Generated at 2022-06-14 16:58:01.817627
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:58:09.287077
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    playlist_count = 1

    profile_id = SoundgasmProfileIE._match_id(url)
    print(profile_id)

    webpage = SoundgasmProfileIE._download_webpage(url, profile_id)

    entries = [
        SoundgasmProfileIE.url_result(audio_url, 'Soundgasm')
        for audio_url in re.findall(r'href="([^"]+/u/%s/[^"]+)' % profile_id, webpage)]

    playlist = SoundgasmProfileIE.playlist_result(entries, profile_id)
    print(playlist)
    assert len(playlist['entries']) == playlist_count

# Generated at 2022-06-14 16:58:11.146472
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Instantiate SoundgasmIE constructor
    SoundgasmIE()


# Generated at 2022-06-14 16:58:22.544782
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    Test = SoundgasmIE()
    Test._download_webpage = lambda url: url
    Test._search_regex = lambda name, url, a, b: url
    Test._html_search_regex = lambda name, url, a, b: url

    # Test string to ensure that the class is capable of handling URL's
    assert Test._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

    # Test string to test that the class is capable of extracting correct URL's from YouTube
    assert Test.suitable('http://soundgasm.net/u/ytdl/Piano-sample') == True
    assert Test.suitable

# Generated at 2022-06-14 16:58:25.746532
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # New instance of class SoundgasmIE
    SoundgasmIE(SoundgasmIE._VALID_URL)
    # New instance of class SoundgasmProfileIE
    SoundgasmProfileIE(SoundgasmProfileIE._VALID_URL)

# Generated at 2022-06-14 16:58:26.549240
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert {'Soundgasm': SoundgasmIE}

# Generated at 2022-06-14 16:58:33.688442
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	import json
	url = "http://soundgasm.net/u/ytdl/Piano-sample"
	ie = SoundgasmIE()
	ie.extract(url)
	test_data = [
					ie.extractor_key(),
					ie.extractor_key(url),
					str(ie.extract(url))
				]

# Generated at 2022-06-14 16:58:36.820325
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    _constructor_test(SoundgasmProfileIE, 'http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:58:41.026577
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    obj = SoundgasmProfileIE()
    obj._download_webpage("http://soundgasm.net/u/ytdl", "ytdl")
    obj._real_extract("http://soundgasm.net/u/ytdl")

# Generated at 2022-06-14 16:58:52.022063
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = "http://soundgasm.net/u/ytdl"
    url_result_get_url = "http://soundgasm.net/u/ytdl"
    url_result_get_ie_key = "Soundgasm"
    url_result_playlist_result_id = "ytdl"
    url_result_playlist_result_entries = "http://soundgasm.net/u/ytdl/Piano-sample"

    # create instance of SoundgasmProfileIE
    obj = SoundgasmProfileIE()

    # get the real extract of soundgasm
    obj._real_extract(url)

    # assert SoundgasmProfileIE instance is not none
    assert obj != None

    # assert the SoundgasmProfileIE instance is a SoundgasmProfileIE instance

# Generated at 2022-06-14 16:59:00.966569
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    I = SoundgasmIE.constructor()

# Generated at 2022-06-14 16:59:04.166233
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE("https://soundgasm.net/u/ytdl")
    assert ie.ie_key() == 'SoundgasmProfile'
    assert ie.ie_name() == 'Soundgasm'

# Generated at 2022-06-14 16:59:10.185918
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE.IE_NAME == 'soundgasm'
    assert SoundgasmIE.IE_DESC == 'Soundgasm'
    assert SoundgasmIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert SoundgasmIE._TYPE == 'audio'
    assert SoundgasmIE._downloader == None
    assert SoundgasmIE._WORKING == True


# Generated at 2022-06-14 16:59:14.664577
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TEST')
    assert hasattr(ie, '_real_extract')


# Generated at 2022-06-14 16:59:15.917612
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:59:28.355029
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from collections import namedtuple
    from ytdl import create_SoundgasmProfileIE
    from .common import BASE_URL
    from .common import fake_urlretrieve

    class soundgasm(object):
        def _download_webpage(self, url, video_id):
            Test = namedtuple('Test', ['url', 'video_id', 'result'])

# Generated at 2022-06-14 16:59:28.996306
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:59:35.957814
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	ie_mock = SoundgasmProfileIE()
	assert ie_mock.IE_NAME == 'Soundgasm'
	assert ie_mock._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 16:59:37.601254
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl', None)


# Generated at 2022-06-14 16:59:44.331239
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Test case for Constructor of SoundgasmIE
    """
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:00:03.159380
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	assert True

# Generated at 2022-06-14 17:00:08.820365
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    ie = SoundgasmIE(url)
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:00:16.436380
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    profile = SoundgasmProfileIE(url)
    assert profile.IE_NAME == 'soundgasm:profile'
    assert re.match(profile._VALID_URL, url)
    assert profile.IE_NAME == 'soundgasm:profile'
    assert profile._real_extract(url)


# Generated at 2022-06-14 17:00:20.071096
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # This test might fail because the page layout is subject to change.
    # The test is here to ensure the class is created and not just the method.
    extractor = SoundgasmProfileIE()
    assert extractor is not None

# Generated at 2022-06-14 17:00:23.820467
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 17:00:35.504120
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert(SoundgasmIE.__name__ == "SoundgasmIE")
    assert(SoundgasmIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')

# Generated at 2022-06-14 17:00:38.730852
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE('Soundgasm.netProfile')._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 17:00:39.197363
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    pass

# Generated at 2022-06-14 17:00:41.546926
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ifile = SoundgasmIE()
    assert ifile == SoundgasmIE()
    assert ifile is not SoundgasmIE()
    assert ifile == SoundgasmIE()


# Generated at 2022-06-14 17:00:47.748981
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert list(InfoExtractor._extractors.keys()) == ['Soundgasm', 'SoundgasmProfile']
    assert InfoExtractor._extractors['Soundgasm'] is SoundgasmIE
    assert InfoExtractor._extractors['SoundgasmProfile'] is SoundgasmProfileIE

# Generated at 2022-06-14 17:01:36.366111
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')._VALID_URL is not None


# Generated at 2022-06-14 17:01:37.734155
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()
    return 0


# Generated at 2022-06-14 17:01:42.155063
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profileIE = SoundgasmProfileIE()

    assert profileIE.suitable('http://soundgasm.net/u/ytdl') == True
    assert profileIE.suitable('http://soundgasm.net/u/ytdl/') == True
    assert profileIE.suitable('http://soundgasm.net/u/ytdl/#') == True
    assert profileIE.suitable('http://soundgasm.net/u/ytdl/abc') == False

# Generated at 2022-06-14 17:01:43.142508
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.name == 'Soundgasm'
    assert hasattr(ie, '_VALID_URL')



# Generated at 2022-06-14 17:01:46.875416
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()._check_constructor(
        u"",
        u"http://soundgasm.net/u/ytdl/Piano-sample"
    )

# Generated at 2022-06-14 17:01:54.974191
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert(SoundgasmIE.IE_NAME == 'soundgasm')
    assert(SoundgasmIE._VALID_URL is not None)
    m = re.match(SoundgasmIE._VALID_URL, 'http://soundgasm.net/u/ytdl/')
    assert(m.group('user') == 'ytdl')
    assert(m.group('display_id') == '')
    m = re.match(SoundgasmIE._VALID_URL, 'http://soundgasm.net/u/ytdl/test')
    assert(m.group('user') == 'ytdl')
    assert(m.group('display_id') == 'test')

# Generated at 2022-06-14 17:02:01.400390
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test = SoundgasmIE._TEST
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    test['url'] = url
    test['display_id'] = 'Piano-sample'
    test['profile_id'] = 'ytdl'
    ie = SoundgasmIE()
    print(ie._real_extract(url))
    print(test)
    ie = SoundgasmProfileIE()
    print(ie._real_extract('http://soundgasm.net/u/ytdl'))

    assert(ie._real_extract(url) == test)

if __name__ == '__main__':
    test_SoundgasmIE()

# Generated at 2022-06-14 17:02:02.480878
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    try:
        SoundgasmProfileIE()
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-14 17:02:03.519810
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()

# Generated at 2022-06-14 17:02:05.977580
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	from soundgasm.soundgasm import SoundgasmProfileIE
	soundgasm_scraper = SoundgasmProfileIE()
	result = soundgasm_scraper.extract(test_SoundgasmProfileIE.__annotations__['url'])
	assert result.get('id') == 'ytdl'
	assert len(result['entries']) == test_SoundgasmProfileIE.__annotations__['playlist_count']


# Generated at 2022-06-14 17:03:39.734339
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	from soundgasm_profile import SoundgasmProfileIE
	def testcase(url):
		print(url)
		ie = SoundgasmProfileIE(url)
		print(ie._VALID_URL)
		print(ie.IE_NAME)
		print(ie.name)
		print(ie.description)
		print(ie.ie_key())
		print(ie._extract_id)
		print(ie._TESTS)
		
	testcase('http://soundgasm.net/u/ytdl')
	# testcase('http://soundgasm.net/u/ytdl/Piano-sample')
	# testcase('http://soundgasm.net/u/ytdl/Piano-sample/')
	# testcase('http://soundg

# Generated at 2022-06-14 17:03:42.513331
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert(re.match(ie._VALID_URL, "http://soundgasm.net/u/ytdl/Piano-sample") != None)

# Generated at 2022-06-14 17:03:44.756831
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()._download_webpage('http://soundgasm.net/u/ytdl/Piano-sample', 'Piano-sample')


# Generated at 2022-06-14 17:03:46.011611
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE(SoundgasmProfileIE.ie_key())

# Generated at 2022-06-14 17:03:47.278321
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    inst = SoundgasmIE('url')
    assert inst is not None

# Generated at 2022-06-14 17:03:48.949707
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	import SoundgasmIE
	instance = SoundgasmIE.SoundgasmIE()


# Generated at 2022-06-14 17:03:49.827439
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 17:03:51.030456
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE() == SoundgasmProfileIE()



# Generated at 2022-06-14 17:03:52.515106
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	SoundgasmIE('https://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 17:04:02.348423
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """
    Unit test to check that the class constructor of SoundgasmProfileIE
    correctly creates a new instance of the class with the correct
    attributes.
    """

    # Create a new instance of this class
    soundgasm_profile = SoundgasmProfileIE()

    # Check that the instance '_VALID_URL' attribute is set.
    assert soundgasm_profile._VALID_URL

    # Check that the instance 'IE_NAME' attribute is set.
    assert soundgasm_profile.IE_NAME

    # Check that the instance '_TEST' attribute is set.
    assert soundgasm_profile._TEST

    # Check that the instance 'BR_DESC' attribute is set.
    assert soundgasm_profile.BR_DESC