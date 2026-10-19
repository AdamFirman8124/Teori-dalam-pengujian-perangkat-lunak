

# Generated at 2022-06-14 17:27:08.352499
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Create the class UDNEmbedIE
    """
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn.com'

# Generated at 2022-06-14 17:27:16.727009
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import sys
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    IE = UDNEmbedIE()
    # Test valid URL using regular expressions
    assert IE._VALID_URL == 'https?:' + IE._PROTOCOL_RELATIVE_VALID_URL
    # Test valid URL for protocol-relative URL
    assert IE._match_id('//video.udn.com/embed/news/300040') == '300040'
    assert IE._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert IE._match_id('https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2022-06-14 17:27:21.935713
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # Success test
    assert ie._match_id(
        'http://video.udn.com/embed/news/300040') == '300040'
    # Fail test
    assert ie._match_id(
        'http://video.udn.com/embed/news/') == None

# Generated at 2022-06-14 17:27:32.265952
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import re
    import unittest
    from youtube_dl.utils import compile_regex_patterns

    class TestAsyncFD(unittest.TestCase):

        def test_one_pattern(self):
            pattern = r'http://video\.udn\.com/embed/news/(?P<id>\d+)'
            # it should compile a regex pattern
            regex = compile_regex_patterns(pattern)
            # we need it to return a list of patterns
            self.assertIsInstance(regex, list)
            # that list should contain one compiled regex
            self.assertEqual(len(regex), 1)
            # the regex should be a SRE_Pattern instance
            self.assertIsInstance(regex[0], type(re.compile('')))
            # the regex should match the test pattern
            self

# Generated at 2022-06-14 17:27:36.417775
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(re.compile(ie._PROTOCOL_RELATIVE_VALID_URL), type(re.compile('')))
    assert isinstance(re.compile(ie._VALID_URL), type(re.compile('')))

# Generated at 2022-06-14 17:27:40.118416
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE('UDNEmbedIE')
    assert obj.ie_key() == 'UDNEmbed'
    assert obj.ie_desc() == '聯合影音'



# Generated at 2022-06-14 17:27:41.228276
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:27:45.539567
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE("https://video.udn.com/embed/news/300040")
    assert obj.IE_NAME == 'udn'
    assert obj.IE_DESC == '聯合影音'
    assert obj._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:49.570943
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Instantiate object
    udne = UDNEmbedIE()

    assert udne._VALID_URL == r'https?:' + udne._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:27:57.980438
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert(UDNEmbedIE.IE_DESC == '聯合影音')
    target = UDNEmbedIE()
    assert(target._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    assert(target._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

# Generated at 2022-06-14 17:28:13.964574
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = InfoExtractor.get_info_extractor_by_name('UDNEmbed')
    assert isinstance(ie, UDNEmbedIE)
    assert ie.IE_NAME == 'UDNEmbed'

# Generated at 2022-06-14 17:28:26.441675
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    x = UDNEmbedIE()
    assert x.IE_NAME == 'udn.com'
    assert x.IE_DESC == '聯合影音'
    assert x._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert x._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert x._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:28:36.401118
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:28:38.552705
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	ie = UDNEmbedIE()
	print(ie)

# Generated at 2022-06-14 17:28:47.082641
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE().ie_key() == 'UDNEmbed'
    assert UDNEmbedIE()._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert UDNEmbedIE()._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert UDNEmbedIE()._match_id('//video.udn.com/embed/news/300040') == '300040'


# Generated at 2022-06-14 17:28:54.201869
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # Test for url validation
    url = 'https://video.udn.com/embed/news/300040'
    assert ie.suitable(url)
    # Test for url path
    url_path = '/embed/news/300040'
    assert ie.suitable(url_path)
    # Test for url_or_path
    url_or_path = '//video.udn.com/embed/news/300040'
    assert ie.suitable(url_or_path)


# Generated at 2022-06-14 17:29:02.358726
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:29:03.336968
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:29:08.452777
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:29:19.359086
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test the case when url's scheme is http
    assert UDNEmbedIE._VALID_URL.match('http://video.udn.com/embed/news/300040').group(1) == '300040'
    # Test the case when url's scheme is https
    assert UDNEmbedIE._VALID_URL.match('https://video.udn.com/embed/news/300040').group(1) == '300040'
    # Test the protocol-relative case
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL.match('//video.udn.com/embed/news/300040').group(1) == '300040'
    # Test the play case

# Generated at 2022-06-14 17:29:49.891868
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._match_id(url)

# Generated at 2022-06-14 17:29:58.142790
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    udn = UDNEmbedIE()
    assert udn.IE_DESC == '聯合影音'
    assert udn._VALID_URL == 'https?:' + udn._PROTOCOL_RELATIVE_VALID_URL
    assert udn._match_id(url) == '300040'



# Generated at 2022-06-14 17:30:04.905664
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import unittest
    import urllib
    class TestUDNEmbedIE(unittest.TestCase):
        def test_constrctor(self):
            """Test constructor"""
            UDNEmbedIE()
            self.assertTrue(True)
    # End of class TestUDNEmbedIE

    unittest.main()
    # Test case for constructor
    test_case = TestUDNEmbedIE('test_constrctor')
    test_case.test_constrctor()

# Generated at 2022-06-14 17:30:09.389837
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_ie = UDNEmbedIE({})
    assert (udn_ie._PROTOCOL_RELATIVE_VALID_URL ==
            r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

# Generated at 2022-06-14 17:30:21.865649
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    obj = UDNEmbedIE()
    assert obj._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:28.493521
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = '//video.udn.com/embed/news/300040'
    # return a UDNEmbedIE object
    ie = UDNEmbedIE()._build_ie_from_url(url)
    # assert the class is UDNEmbedIE
    assert ie.__class__ == UDNEmbedIE
    # assert the _VALID_URL of UDNEmbedIE is 'https?:' + _PROTOCOL_RELATIVE_VALID_URL
    assert ie._VALID_URL == 'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:30:35.531686
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE.IE_DESC == '聯合影音'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL


# Generated at 2022-06-14 17:30:41.556812
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE(UDNEmbedIE._downloader)._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE(UDNEmbedIE._downloader)._VALID_URL == UDNEmbedIE._VALID_URL
    assert UDNEmbedIE(UDNEmbedIE._downloader)._TESTS == UDNEmbedIE._TESTS


# Generated at 2022-06-14 17:30:44.918070
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    def test_class(extractor_class):
        print(extractor_class.IE_NAME)
    udne_ie = UDNEmbedIE()
    test_class(udne_ie)



# Generated at 2022-06-14 17:30:53.511450
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class_UDNEmbedIE = UDNEmbedIE()
    # Test _PROTOCOL_RELATIVE_VALID_URL
    _PROTOCOL_RELATIVE_VALID_URL = r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert class_UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == _PROTOCOL_RELATIVE_VALID_URL

# Test _VALID_URL

# Generated at 2022-06-14 17:31:28.205255
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from ..test import get_testcases
    testcases = get_testcases(UDNEmbedIE, '._VALID_URL', '._PROTOCOL_RELATIVE_VALID_URL', '._TESTS')
    instance = UDNEmbedIE()
    for url, expected in testcases:
        assert instance._VALID_URL_RE.search(url) is not None or instance._PROTOCOL_RELATIVE_VALID_URL_RE.search(url) is not None, (
            "The URL '%s' should be recognized by the constructor of class UDNEmbedIE" % url
        )


# Generated at 2022-06-14 17:31:30.129841
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:31:34.148585
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	u = UDNEmbedIE(None)
	assert(u.IE_DESC == '聯合影音')
	assert(u._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

# Generated at 2022-06-14 17:31:41.172321
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_o = UDNEmbedIE(UDNEmbedIE())
    assert test_o._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert test_o._VALID_URL == r'https?:' + test_o._PROTOCOL_RELATIVE_VALID_URL
    assert test_o._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert test_o._TESTS[0]['info_dict']['id'] == '300040'
    assert test_o._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:31:50.486548
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "https://video.udn.com/embed/news/300040"
    pattern = r'^https://video\.udn\.com/embed/news/\d+$'
    # Test _PROTOCOL_RELATIVE_VALID_URL
    assert re.search(pattern, url)
    # Test _VALID_URL
    assert UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

    return 0

# Test for _match_id

# Generated at 2022-06-14 17:32:02.929284
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from ..utils import makedirs
    from ..downloader.common import FileDownloader
    from ..downloader.http import HttpFD
    from ..downloader.https import HttpsFD
    from ..downloader.f4m import F4mFD
    import os
    import shutil
    import tempfile

    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-14 17:32:04.551116
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test class constructor with no parameter."""
    inst = UDNEmbedIE()
    assert inst is not None

# Generated at 2022-06-14 17:32:12.356597
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .test_common import TestCommon
    ie = UDNEmbedIE()
    assert ie._match_id('//video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('//video.udn.com/play/news/300040') == '300040'
    # For the next tests, we must not use https!
    url = 'http://video.udn.com/play/news/300040'
    TestCommon.test_video_id(ie, url)
    TestCommon._test_invalid_id(ie, url)
    TestCommon._test_url_exists(ie, url)

# Generated at 2022-06-14 17:32:19.856539
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert udne.SUFFIX == 'video.udn.com'
    assert udne.IE_NAME == 'udn'
    assert udne.IE_DESC == '聯合影音'
    assert udne.VALID_URL == r'%s://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)' % 'https?'
    assert udne.mobj == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udne.PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert u

# Generated at 2022-06-14 17:32:23.829262
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # Testing extract_url
    assert ie._match_id(ie._VALID_URL) is not None
    assert ie._match_id(ie._PROTOCOL_RELATIVE_VALID_URL) is not None
    assert ie._match_id('http://video.udn.com/news/300040') is None
    # Testing _real_extract
    assert ie._real_extract(ie._VALID_URL) is not None

# Generated at 2022-06-14 17:33:32.097006
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040', 'UDN-Video')

# Generated at 2022-06-14 17:33:36.846424
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.ie_key() == 'UDNEmbed'
    assert udn_embed_ie.ie_desc() == '聯合影音'


if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:33:45.974125
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from six import StringIO
    from .common import head_mark
    from .common import tail_mark
    from .common import extract_info
    from .common import file_count
    from .common import file_size
    from .common import save_testc

    class Test_UDNEmbedIE(object):
        def __init__(self):
            self.testc_dir = 'testc_udn'
            self.testc_video_id = '300040'
            self.testc_url = 'http://video.udn.com/embed/news/{0}'.format(self.testc_video_id)

# Generated at 2022-06-14 17:33:57.853706
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    m = UDNEmbedIE()
    assert m._VALID_URL=='https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert m._PROTOCOL_RELATIVE_VALID_URL=='//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert m._TESTS[0]['url']=='http://video.udn.com/embed/news/300040'
    assert m._TESTS[0]['info_dict']['id']=='300040'
    assert m._TESTS[0]['info_dict']['ext']=='mp4'

# Generated at 2022-06-14 17:34:07.678949
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    assert UDNEmbedIE._VALID_URL == 'https?:://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'

# Generated at 2022-06-14 17:34:13.453285
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # first test
    assert UDNEmbedIE()._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # second test
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')

# Generated at 2022-06-14 17:34:17.162463
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.IE_NAME == 'UDNEmbed'
    assert udn_embed_ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:34:18.228383
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

# Generated at 2022-06-14 17:34:24.644785
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == 'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:34:29.176825
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test the constructor of class UDNEmbedIE
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._downloader is not None
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'