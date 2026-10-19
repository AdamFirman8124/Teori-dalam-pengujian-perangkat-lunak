

# Generated at 2022-06-14 16:55:31.245784
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:55:32.018242
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    dir(SoundgasmIE)

# Generated at 2022-06-14 16:55:32.529982
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    pass

# Generated at 2022-06-14 16:55:35.848979
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	print("testing SoundgasmIE class constructor")
	instance = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
	print("testing SoundgasmIE class constructor done")


# Generated at 2022-06-14 16:55:37.486367
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE = SoundgasmIE();
    assert(IE.IE_NAME == "Soundgasm")

# Generated at 2022-06-14 16:55:40.150678
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE()
    assert isinstance(obj, InfoExtractor)
    assert obj.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:55:41.364024
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:55:45.832162
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    # Assert parameters of IE.__init__ are the same as IE_NAME and IE_DESC
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 16:55:56.799610
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Create a new instance of SoundgasmIE
    youtube_dl = __import__('youtube_dl')
    ie = youtube_dl.YoutubeDL({}).build_ie()
    assert isinstance(ie, SoundgasmIE)
    # Check if it is the right class
    assert ie.IE_NAME == 'soundgasm'
    # Check if the regex of the class is right
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/[0-9a-zA-Z_-]+/[0-9a-zA-Z_-]+'
    # Check if it accepts an URL

# Generated at 2022-06-14 16:55:58.656569
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    class_ = SoundgasmIE()
    assert class_.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:56:06.407618
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
  """
  Unit test for constructor of class SoundgasmProfileIE
  """
  try:
    SoundgasmProfileIE()
  except Exception as e:
    print(e)
    return False

  return True

# Generated at 2022-06-14 16:56:12.354367
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE(None, None, None)
    # Test for _match_id
    assert ie._match_id('http://soundgasm.net/u/ytdl') == 'ytdl'
    # Test for _real_extract
    ie._real_extract('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:56:16.049480
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Test if the constructor of class SoundgasmProfileIE can be called without errors.
    try:
        SoundgasmProfileIE()
        # If this line was reached, the test was successful.
        return True
    except Exception as e:
        # If this line was reached, the test failed.
        return e

# Generated at 2022-06-14 16:56:25.955733
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Test a URL that can be recognized by the SoundgasmIE
    ie = SoundgasmIE()
    assert ie.suitable(IE_NAME, 'http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie.suitable(IE_NAME, 'https://soundgasm.net/u/ytdl/Piano-sample')
    assert ie.suitable(IE_NAME, 'http://www.soundgasm.net/u/ytdl/Piano-sample')
    assert ie.suitable(IE_NAME, 'https://www.soundgasm.net/u/ytdl/Piano-sample')
    assert ie.suitable(IE_NAME, 'http://soundgasm.net/u/ytdl/coffeeandcock')

# Generated at 2022-06-14 16:56:29.716148
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Constructor of SoundgasmIE can only be used to check whether URL is valid or not
    # The following test cases can be used to check the test cases in SoundgasmIE
    assert SoundgasmIE._VALID_URL == SoundgasmIE('')._VALID_URL

# Generated at 2022-06-14 16:56:31.438558
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:56:35.162250
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    info = SoundgasmIE()._call_downloader({'url': url})
    assert info['url'] == 'http://soundgasm.net/play/ytdl/Piano-sample.m4a'

# Generated at 2022-06-14 16:56:37.539322
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()
    print("Test for class SoundgasmIE passed")


# Generated at 2022-06-14 16:56:42.084113
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('soundgasm:profile')
    # Test that URL is valid
    assert ie.suitable('https://soundgasm.net/u/ytdl?order=listened')
    # Test that URL is invalid
    assert not ie.suitable('https://soundcloud.com/ytdl')

# Generated at 2022-06-14 16:56:45.522568
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    import urlparse
    url = urlparse.urljoin('http://soundgasm.net/u', 'ytdl')
    ie = SoundgasmProfileIE(url)
    name = ie.IE_NAME
    assert name == 'soundgasm:profile'


# Generated at 2022-06-14 16:57:02.117584
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from .test_downloader import skip_download_tests
    from .test_downloader import expectedFailure
    from .test_downloader import expectedSuccess
    from .test_downloader import toolong
    from .test_downloader import get_testcases
    from .test_downloader import all_tests

    class SoundgasmProfile_TestCase(object):
        class XCase(object):
            def __init__(self, link, expected, skiptest=False):
                self.link = link
                self.expected = expected
                self.skiptest = skiptest

            def check_soundgasm_profile_IE(self):
                # The actual unit test
                if self.skiptest:
                    skip_download_tests()
                result, expected = self.expected, self.link
                realresult = SoundgasmProfileIE._

# Generated at 2022-06-14 16:57:12.344549
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    import unittest
    from .common import TestCase
    from .test_soundgasm import SoundgasmIE

    class TestSoundgasm(TestCase):
        def test_SoundgasmProfileIE(self):
            TestCase._run_IE_test_for_class(self, SoundgasmProfileIE, [
                {
                    'url': 'http://soundgasm.net/u/ytdl',
                    'playlist_mincount': 1,
                    'skip': 'Regular Soundgasm profile pages no longer exist',
                },
            ])

    test = unittest.TestLoader().loadTestsFromTestCase(TestSoundgasm)
    unittest.TextTestRunner(verbosity=2).run(test)

# Generated at 2022-06-14 16:57:19.612270
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm = SoundgasmIE()
    audio_url = 'http://files.soundgasm.net/u/ytdl/Piano-sample.m4a'
    webpage = '''
    <div id="page">
    <audio
        src="'''+ audio_url +'''">
        </audio>

    '''

    audio_id = 'Piano-sample'
    title = 'Piano sample'
    description = 'Royalty Free Sample Music'
    uploader = 'ytdl'

    audio_url_re = r'(?s)m4a\s*:\s*(["\'])(?P<url>(?:(?!\1).)+)\1'

# Generated at 2022-06-14 16:57:24.555704
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE  # Works during development only
    assert SoundgasmIE()._download_webpage.__name__ == '_download_webpage'
    assert SoundgasmIE()._real_extract.__name__ == '_real_extract'

# Generated at 2022-06-14 16:57:36.944939
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """Create an instance of SoundgasmIE and test attributes"""
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    soundgasmIE = SoundgasmIE({})
    assert soundgasmIE.IE_NAME == "Soundgasm"
    assert soundgasmIE.ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert soundgasmIE.ie._TEST['url'] == url
    assert soundgasmIE.ie._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'


# Generated at 2022-06-14 16:57:37.886931
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE()


# Generated at 2022-06-14 16:57:39.910056
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm_ie = SoundgasmIE("test_SoundgasmIE")
    print("constructor of class SoundgasmIE")


# Generated at 2022-06-14 16:57:41.569243
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE().extract(url='http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:57:44.689324
# Unit test for constructor of class SoundgasmProfileIE

# Generated at 2022-06-14 16:57:45.674984
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE

# Generated at 2022-06-14 16:58:07.673050
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test = SoundgasmIE()
    assert test.name == 'soundgasm'
    assert test._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert test._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert test._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'
    assert test._TEST['info_dict']['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'

# Generated at 2022-06-14 16:58:18.727966
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    fallback_urls = ie._fallback_urls()
    assert(len(fallback_urls) == 2)
    assert(fallback_urls[0] == ie._VALID_URL)
    assert(fallback_urls[1] == 'http://soundgasm.net/u/$1/')
    assert(ie._valid_url('http://soundgasm.net/u/ytdl', 'Soundgasm') == True)
    assert(ie._valid_url('http://soundgasm.net/u/ytdl/', 'Soundgasm') == True)
    assert(ie._valid_url('http://soundgasm.net/u/ytdl/bla-bla', 'Soundgasm') == False)

# Generated at 2022-06-14 16:58:20.821711
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sg_ie = SoundgasmIE()
    assert(sg_ie.IE_NAME == 'Soundgasm')


# Generated at 2022-06-14 16:58:24.478214
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    obj = SoundgasmProfileIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 16:58:26.192236
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:58:36.942419
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:58:38.761721
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie == "SoundgasmProfile"


# Generated at 2022-06-14 16:58:39.986119
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	SoundgasmProfileIE()

# Generated at 2022-06-14 16:58:42.188171
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl")

# Generated at 2022-06-14 16:58:44.934725
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_ie = SoundgasmProfileIE()
    assert isinstance(profile_ie, SoundgasmProfileIE)

# Generated at 2022-06-14 16:59:19.207391
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()._download_webpage('https://soundgasm.net/u/ytdl/Piano-sample', 'Piano-sample')

# Generated at 2022-06-14 16:59:24.947169
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    res = SoundgasmProfileIE()._real_extract("http://soundgasm.net/u/ytdl")
    print("this test is expected to fail")
    print("urls:")
    print(res.get("entries"))
    print("id:")
    print(res.get("id"))
    assert(res.get("id") == "ytdl")

# Generated at 2022-06-14 16:59:26.013623
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:59:27.131629
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie

# Generated at 2022-06-14 16:59:28.033963
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE.suite()

# Generated at 2022-06-14 16:59:30.619081
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    i = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    print("Evaluation result: " + str(eval("1+1")))

# Generated at 2022-06-14 16:59:32.132252
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm = SoundgasmProfileIE()
    assert soundgasm != None

# Generated at 2022-06-14 16:59:33.211221
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    obj = SoundgasmProfileIE()
    assert obj


# Generated at 2022-06-14 16:59:35.746513
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('soundgasm:profile')

# Generated at 2022-06-14 16:59:37.773903
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    IE = SoundgasmProfileIE("http://soundgasm.net/u/ytdl")
    assert IE.playlist_count == 1



# Generated at 2022-06-14 17:01:02.577276
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

    # test url
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    # test patterns
    valid_url_pattern = r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    audio_url_pattern = r'(?s)m4a\s*:\s*(["\'])(?P<url>(?:(?!\1).)+)\1'
    title_pattern = r'<div[^>]+\bclass=["\']jp-title[^>]+>([^<]+)'

# Generated at 2022-06-14 17:01:13.138281
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """Unit test for constructor of class SoudgasmProfileIE"""
    unit_test_url = 'http://soundgasm.net/u/ytdl'
    unit_test_profile_id = 'ytdl'

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


# Generated at 2022-06-14 17:01:20.969751
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm_ie = SoundgasmIE()
    mobj = re.match(soundgasm_ie._VALID_URL, 'https://soundgasm.net/u/ytdl/Piano-sample')
    assert mobj.group('user') == 'ytdl'
    assert mobj.group('display_id') == 'Piano-sample'


test_SoundgasmIE()

# Generated at 2022-06-14 17:01:24.164010
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    InfoExtractor(SoundgasmIE.IE_NAME)._real_extract(url)


# Generated at 2022-06-14 17:01:27.977296
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Create an instance of the class under test
    profile = SoundgasmIE('url', {'id': 'id'})

    # Check the properties of the instance were set correctly
    assert profile.ie_key() == 'Soundgasm'
    assert profile.url == 'url'
    assert profile.playlist_title == 'id'


# Generated at 2022-06-14 17:01:29.038881
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    instance = SoundgasmIE()
    print(instance)

# Generated at 2022-06-14 17:01:33.150607
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_SoundgasmProfileIE.exception_caught = False

    try:
        SoundgasmProfileIE()
    except:
        test_SoundgasmProfileIE.exception_caught = True

    assert test_SoundgasmProfileIE.exception_caught == False

# Generated at 2022-06-14 17:01:37.353250
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie._VALID_URL == SoundgasmIE._VALID_URL
    assert ie.__name__ == SoundgasmIE.IE_NAME
    assert ie.ie_key() == SoundgasmIE.ie_key()

# Generated at 2022-06-14 17:01:39.863107
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE(InfoExtractor())

# Generated at 2022-06-14 17:01:43.605696
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE(InfoExtractor())

# Generated at 2022-06-14 17:04:47.564954
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert(ie.__class__ == SoundgasmProfileIE)


# Generated at 2022-06-14 17:04:59.713872
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Creates and initializes an instance of SoundgasmIE
    """
    ie = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    assert ie.IE_NAME == "soundgasm"
    assert ie.IE_DESC == "Soundgasm.net"
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert len(ie._TESTS) == 1
    test = ie._TESTS[0]

# Generated at 2022-06-14 17:05:07.653617
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:05:09.354724
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # TODO
    pass


# Generated at 2022-06-14 17:05:18.482833
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	print("\nConstructor for class SoundgasmIE \n")
	url = "http://soundgasm.net/u/ytdl/Piano-sample"
	#url = "http://soundgasm.net/u/ytdl"
	#url = "http://soundgasm.net/u/ytdl/Piano-sample"
	#url = "http://soundgasm.net/u/ytdl/Piano-sample"
	#url = "http://soundgasm.net/u/ytdl/Piano-sample"
	url == SoundgasmIE._VALID_URL
	SoundgasmIE()

test_SoundgasmIE()

# Generated at 2022-06-14 17:05:27.816380
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Instance of class SoundgasmIE
    ie = SoundgasmIE()

    # match the regex (url) of SoundgasmIE
    mobj = re.match(ie._VALID_URL, ie._TEST['url'])

    # assert that the values of the group are equal to the values in the entry example
    assert mobj.group('user') == ie._TEST['info_dict']['uploader']
    assert mobj.group('display_id') == ie._TEST['info_dict']['display_id']
