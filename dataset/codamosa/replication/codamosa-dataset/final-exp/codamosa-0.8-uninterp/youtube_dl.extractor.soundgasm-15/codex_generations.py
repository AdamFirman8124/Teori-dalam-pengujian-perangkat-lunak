

# Generated at 2022-06-14 16:55:37.159883
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    instance = SoundgasmProfileIE()
    name = type(instance).__name__
    assert name == 'SoundgasmProfileIE'

# Generated at 2022-06-14 16:55:40.864652
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm_profile_ie = SoundgasmProfileIE()
    assert soundgasm_profile_ie == SoundgasmProfileIE()
    assert soundgasm_profile_ie is not SoundgasmProfileIE()


# Generated at 2022-06-14 16:55:44.784450
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()

    assert ie.IE_NAME == "soundgasm:profile"
    assert ie.TYPE == "playlist"

    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:55:46.969499
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    '''
    Function to test constructor of class SoundgasmIE
    '''
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'



# Generated at 2022-06-14 16:55:53.323723
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE("https://www.soundgasm.net/u/ytdl/Piano-sample")
    assert ie.display_id == "Piano-sample"
    assert ie.user == "ytdl"
    assert ie.url == "https://www.soundgasm.net/u/ytdl/Piano-sample"
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:56:00.642711
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = "http://soundgasm.net/u/ytdl/"
    #assert SoundgasmProfileIE(url)
    assert SoundgasmProfileIE("http://soundgasm.net/u/ytdl")
    assert SoundgasmProfileIE("http://soundgasm.net/u/ytdl/")
    assert SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#")
    assert SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#hello")
    assert SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#hello-world")
    assert SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#hello_world")



# Generated at 2022-06-14 16:56:03.555092
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()._real_extract('http://soundgasm.net/u/ytdl/Piano-sample')


# Generated at 2022-06-14 16:56:05.209566
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm_profile_ie = SoundgasmProfileIE();

# Generated at 2022-06-14 16:56:12.234438
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    import sys
    import os
    import re
    import urllib2
    import urlparse
    from HTMLParser import HTMLParser

    def get_url(url):
        return 'http://soundgasm.net/u/ytdl/'

    # this is our test URL.
    url = get_url(url)
    SoundgasmProfileIE()._downloader.urlopen(url)

# Generated at 2022-06-14 16:56:14.923469
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()

# Generated at 2022-06-14 16:56:24.102821
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('SoundgasmProfileIE')

# Generated at 2022-06-14 16:56:33.558323
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    soundgasm.info_dict
    soundgasm.download_webpage_handle
    soundgasm.download_webpage_handle(soundgasm.url)
    soundgasm.mobj.group(1)
    soundgasm.mobj.group(2)
    soundgasm.webpage
    soundgasm.audio_url
    soundgasm.title
    soundgasm.description
    soundgasm.audio_id
    soundgasm.ext
    soundgasm.vcodec
    soundgasm.uploader

# Generated at 2022-06-14 16:56:36.951621
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # soundgasm.net/u/ytdl
    profile_url = 'http://soundgasm.net/u/ytdl'
    # ytdl
    profile_id = 'ytdl'
    # Initialize object of class SoundgasmProfileIE
    SoundgasmProfileIE


# Generated at 2022-06-14 16:56:37.772952
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    pass

# Generated at 2022-06-14 16:56:39.625338
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE("test", "", "", "", "", "", "")


# Generated at 2022-06-14 16:56:42.207454
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_obj = SoundgasmProfileIE()
    assert test_obj._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:56:43.585337
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE()
    assert ['soundgasm'] == obj.IE_NAME

# Generated at 2022-06-14 16:56:49.878697
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    pass
#    # sample URL for profile page
    #url = 'http://soundgasm.net/u/ytdl'
    #ie = SoundgasmProfileIE(url, {});
    #assert(ie._match_id(url) == 'ytdl')
    

# Generated at 2022-06-14 16:56:51.308253
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	assert SoundgasmIE.__name__ == 'SoundgasmIE'

# Generated at 2022-06-14 16:56:52.948701
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    e = SoundgasmIE()
    assert e.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:57:03.539316
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('SoundgasmProfileIE')


# Generated at 2022-06-14 16:57:06.121478
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE('https://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:57:11.658054
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # valid url
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    # Try to create an instance of SoundgasmIE
    ie = SoundgasmIE()
    # verify that the url is valid
    assert(ie._match_id(url) == '88abd86ea000cafe98f96321b23cc1206cbcbcc9')

# Generated at 2022-06-14 16:57:19.147230
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Valid and correct url
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    result = SoundgasmIE()._real_extract(url)

    assert result['id'] == 'Piano-sample'
    assert result['display_id'] == 'Piano-sample'
    assert result['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample/Piano-sample.m4a'
    assert result['vcodec'] == 'none'
    assert result['title'] == 'Piano sample'
    assert result['description'] == 'Royalty Free Sample Music'
    assert result['uploader'] == 'ytdl'

    # Invalid and incorrect url

# Generated at 2022-06-14 16:57:21.799482
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE('https://soundgasm.net/u/ytdl/Piano-sample')
    assert obj.IE_NAME == 'soundgasm'
    assert obj.name == 'Soundgasm'


# Generated at 2022-06-14 16:57:29.625290
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE({})
    except:
        try:
            import sys
            import traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        finally:
            del exc_type, exc_value, exc_traceback

# Generated at 2022-06-14 16:57:31.855600
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()._real_extract('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:57:42.090478
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    audio_url = "http://soundgasm.net/u/ytdl/Piano-sample"
    obj = SoundgasmIE()._real_extract(audio_url)
    assert obj.get('id') == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert obj.get('display_id') == 'Piano-sample'
    assert obj.get('url') == 'http://s1.0.soundgasm.net/u/ytdl/Piano-sample.m4a'
    assert obj.get('title') == 'Piano sample'
    assert obj.get('description') == 'Royalty Free Sample Music'
    assert obj.get('uploader') == 'ytdl'
    assert obj.get('vcodec') == 'none'


# Generated at 2022-06-14 16:57:46.126820
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:57:49.010635
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert(SoundgasmProfileIE().ie_key() == 'Soundgasm')

# Generated at 2022-06-14 16:58:09.953355
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }

# Generated at 2022-06-14 16:58:18.463727
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    info_extractor = SoundgasmProfileIE()
    assert info_extractor.IE_NAME == 'soundgasm:profile'
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert info_extractor._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }

# Generated at 2022-06-14 16:58:30.149613
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    print("Testing SoundgasmIE constructor")
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:58:39.389122
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_cases = (
        ("http://soundgasm.net/u/ytdl/", "['http://soundgasm.net/u/ytdl/Piano-sample']"),
        ("http://soundgasm.net/u/ytdl", "['http://soundgasm.net/u/ytdl/Piano-sample']"),
        ("http://soundgasm.net/u/ytdl/#", "['http://soundgasm.net/u/ytdl/Piano-sample']"),
    )

    for (url, exp_playlist_entries_str) in test_cases:
        extractor = SoundgasmProfileIE()
        extracted = extractor._real_extract(url)
        playlist_entries = extracted["entries"]
        assert len(playlist_entries) == 1

# Generated at 2022-06-14 16:58:41.877816
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample') is not None


# Generated at 2022-06-14 16:58:52.484733
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Given a specific url of a profile in the Soundgasm website
    url = "http://soundgasm.net/u/ytdl"

    # And the SoundgasmProfileIE object
    ie = SoundgasmProfileIE()

    # When the url is parsed
    # Then:
    #  - the correct ID is obtained
    #  - the correct webpage is downloaded
    #  - the correct entries are obtained from the webpage
    assert ie._match_id(url) == "ytdl"
    webpage = ie._download_webpage(url, "ytdl")
    entries = [ie.url_result("http://soundgasm.net/u/ytdl/Piano-sample", "Soundgasm")]
    assert entries == ie.playlist_result(entries, "ytdl")

# Generated at 2022-06-14 16:59:04.788671
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    inst = SoundgasmIE()
    assert(inst.IE_NAME == "Soundgasm")
    assert(inst.IE_DESC == "Soundgasm")
    assert(inst._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')

# Generated at 2022-06-14 16:59:06.470652
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:59:10.197389
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')


# Generated at 2022-06-14 16:59:14.664130
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:59:51.913070
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE._build_url_result('a') == 'http://soundgasm.net/u/a'

# Generated at 2022-06-14 16:59:55.249645
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	info_extractor = SoundgasmIE(None)
	assert info_extractor.IE_NAME == 'soundgasm'
	assert info_extractor.description == 'Soundgasm: Audio Social Network'
	assert info_extractor.info_dict['title'] == 'Soundgasm'

# Generated at 2022-06-14 16:59:58.185237
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from ytdl.extractor import ExtractorTest
    from ytdl.extractor.soundgasm import SoundgasmProfileIE

    e = ExtractorTest(SoundgasmProfileIE)
    e.test()

# Generated at 2022-06-14 17:00:03.968894
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Create an instance of the class SoundgasmProfileIE and test it
    from soundgasm import SoundgasmProfileIE
    sgie = SoundgasmProfileIE()
    assert sgie.IE_NAME == "soundgasm"
    assert sgie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert sgie._TEST['url'] == 'http://soundgasm.net/u/ytdl'



# Generated at 2022-06-14 17:00:13.058609
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    class SoundgasmProfileIE(InfoExtractor):
        IE_NAME = 'soundgasm:profile'
        _VALID_URL = r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
        _TEST = {
            'url': 'http://soundgasm.net/u/ytdl',
            'info_dict': {
                'id': 'ytdl',
            },
            'playlist_count': 2,
        }

        def _real_extract(self, url):
            profile_id = self._match_id(url)

            webpage = self._download_webpage(url, profile_id)


# Generated at 2022-06-14 17:00:20.624171
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    myExtWindow = SoundgasmProfileIE()
    for URL in ['http://soundgasm.net/u/ytdl', 'http://soundgasm.net/u/ytdl/', 'http://soundgasm.net/u/ytdl/#', 'http://soundgasm.net/u/ytdl/blah', 'http://soundgasm.net/u/ytdl/blah?hey']:
        assert myExtWindow.isAllowedURL(URL) == True
    blah = myExtWindow.isAllowedURL('http://soundgasm.net/u/ytdl/?blah')
    assert blah  == True



# Generated at 2022-06-14 17:00:25.168558
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    assert ie.IE_NAME == 'soundgasm:profile'

    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl/')
    assert ie.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 17:00:29.278152
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE = SoundgasmIE('soundgasm:profile')
    # Assert that instance of SoundgasmIE has been created
    assert not IE is None

# Generated at 2022-06-14 17:00:30.292556
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE().IE_NAME == 'soundgasm'


# Generated at 2022-06-14 17:00:38.904897
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

    # "http://soundgasm.net/u/ytdl/Piano-sample" is used
    # as an example for testing

    assert(SoundgasmIE._VALID_URL ==
            r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')

    soundgasm_ie = SoundgasmIE()
    soundgasm_ie._VALID_URL = r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 17:02:11.147577
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 17:02:14.027961
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE()
    if obj.IE_NAME != 'soundgasm':
        raise Exception("Object of SoundgasmIE class has wrong IE_NAME!")


# Generated at 2022-06-14 17:02:22.080238
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    obj = SoundgasmIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:27.471136
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert isinstance(SoundgasmIE(), InfoExtractor)
    assert hasattr(SoundgasmIE(), "IE_NAME")
    assert hasattr(SoundgasmIE(), "_VALID_URL")
    assert hasattr(SoundgasmIE(), "_TEST")
    assert hasattr(SoundgasmIE(), "_real_extract")


# Generated at 2022-06-14 17:02:29.247188
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm = SoundgasmIE()

    assert soundgasm.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 17:02:36.959617
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """Test constructor of class SoundgasmProfileIE"""
    # Constructor w/o arguments
    ie = SoundgasmProfileIE()
    assert type(ie) is SoundgasmProfileIE
    # Constructor w/ arguments
    data = {'extractor': 'SoundgasmProfileIE', 'url': 'http://soundgasm.net/u/ytdl', 'info_dict': {'id': 'ytdl'}, 'playlist_count': 1}
    ie = SoundgasmProfileIE(data)
    assert type(ie) is SoundgasmProfileIE
    assert ie.data == data

# Generated at 2022-06-14 17:02:39.067837
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE()._match_id('http://soundgasm.net/u/ytdl') == 'ytdl'



# Generated at 2022-06-14 17:02:41.641495
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl#playlist_top')

# Generated at 2022-06-14 17:02:54.107256
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    class_ = SoundgasmIE
    instance = class_(None)
    assert instance.ie_key() == 'Soundgasm'
    assert class_._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert class_._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert class_._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'

# Generated at 2022-06-14 17:03:02.403899
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """"Constructor test"""
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert ie._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert ie._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'