

# Generated at 2022-06-14 16:55:46.357209
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class SafariBaseTest(SafariBaseIE):
        pass

    SafariBaseTest()

# Generated at 2022-06-14 16:55:48.029234
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()._real_initialize()

# Generated at 2022-06-14 16:55:56.044826
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # The following url does not exit, only for testing
    url = 'https://techbus.safaribooksonline.com/9781449396459'
    expected_result = 'https://cdnapisec.kaltura.com/html5/html5lib/v2.37.1/mwEmbedFrame.php?wid=_1926081&uiconf_id=29375172&flashvars%5BreferenceId%5D=9781449396459-r65'
    info_dict = SafariIE()._real_extract(url)
    assert info_dict['url'] == expected_result


# Generated at 2022-06-14 16:56:01.414314
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from .test_utils import MockYDL
    from . import SafariApiIE
    with MockYDL({'extractor': 'safari:api', 'username': 'username', 'password': 'password'}) as ydl:
        ydl.params['nopart'] = True
        SafariApiIE._real_initialize(ydl)

# Generated at 2022-06-14 16:56:03.393358
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert isinstance(SafariApiIE().params,dict)

# Generated at 2022-06-14 16:56:15.243234
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    expected_course_id = '9781449396459'
    expected_course_title = 'Practical Data Science Cookbook '
    course_dict = {'title': expected_course_title}

    def download_json(*args, **kwargs):
        return course_dict

    def url_result(url, ie_key):
        return {'url': url, 'ie_key': ie_key}

    test_ie = SafariCourseIE(None)
    test_ie._download_json = download_json
    test_ie.url_result = url_result
    test_ie._API_BASE = 'https://www.safaribooksonline.com/api/v1'
    test_ie._API_FORMAT = 'json'


# Generated at 2022-06-14 16:56:21.263519
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    obj = SafariCourseIE(test_SafariCourseIE.__name__)
    if isinstance(obj, SafariCourseIE):
        pass
    else:
        assert False, "Failed to construct an object of type SafariCourseIE"

# Generated at 2022-06-14 16:56:26.183786
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    for url in [
               'https://learning.oreilly.com/api/v1/book/9780134664057/chapter/RHCE_Introduction.html',
               'https://www.safaribooksonline.com/api/v1/book/9780134664057/chapter/RHCE_Introduction.html'
             ]:
        assert SafariApiIE._match_id(url) == '9780134664057'

# Generated at 2022-06-14 16:56:34.430310
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    test_cases = (
        ('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314', SafariCourseIE),
        ('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/', SafariCourseIE),
        ('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json', SafariCourseIE),
        ('http://techbus.safaribooksonline.com/9780134426365', SafariCourseIE),
        ('https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838', SafariCourseIE),
        )

# Generated at 2022-06-14 16:56:35.415033
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    pass

# Generated at 2022-06-14 16:56:56.693331
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    """
    Test for SafariApiIE constructor
    """
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part02.html'
    obj = SafariApiIE()
    assert obj.suitable(url)
    assert obj._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'

# Generated at 2022-06-14 16:57:00.622565
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('/hadoop-fundamentals-livelessons/9780133392838/part00.html', 'Hadoop Fundamentals LiveLessons', '0_qbqx90ic')
    SafariCourseIE('/hadoop-fundamentals-livelessons/9780133392838', 'Hadoop Fundamentals LiveLessons')

# Generated at 2022-06-14 16:57:04.260523
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE(None);
    assert safari_base_ie.LOGGED_IN == False;

# Generated at 2022-06-14 16:57:14.631858
# Unit test for constructor of class SafariIE
def test_SafariIE():
    import logging
    import sys
    import unittest
    from contextlib import closing

    from .common import fake_httpd

    import yaml

    class TestSafariIE(unittest.TestCase):
        def _test_login(self, page):
            with closing(fake_httpd.FakeHttpRequestHandler(page)) as handler:
                httpd = handler.httpd

                self.ie = SafariIE('safari')

                with self.assertRaises(ExtractorError) as error:
                    self.ie.url = 'http://127.0.0.1:%d/failed_login' % httpd.port
                    self.ie._login()
                self.assertTrue(
                    'Unable to log in' in str(error.exception),
                    'Expected error message is not found')

                self.ie

# Generated at 2022-06-14 16:57:22.364564
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """
    Constructor test
    """

# Generated at 2022-06-14 16:57:26.881192
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE("safaribooksonline.com")
    assert ie is not None

# test if SafariBaseIE.suitable(url) is true for SafariIE with a suitable url

# Generated at 2022-06-14 16:57:28.875699
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    i = SafariApiIE()
    assert i.__class__ is SafariApiIE

# Generated at 2022-06-14 16:57:36.009867
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Fake URL
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/ch06.html'
    assert SafariApiIE._VALID_URL == SafariApiIE.VALID_URL, 'url_name not according to specification'
    ie = SafariApiIE(SafariApiIE.ie_key())
    ie.initialize()
    assert ie.suitable(url), 'url not recognized'

# Generated at 2022-06-14 16:57:40.542455
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'

    assert SafariApiIE.suitable(url), 'suitable() should return True'

    assert 1 == len(SafariApiIE._TESTS), 'Should have exactly 1 test'

# Generated at 2022-06-14 16:57:41.051443
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE()
    safari._login()

# Generated at 2022-06-14 16:58:08.483397
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Create a instance of class SafariBaseIE
    obj = SafariBaseIE()


# Generated at 2022-06-14 16:58:10.896030
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    inst = SafariCourseIE()
    # This is a class method with no implementation
    assert inst.suitable is None

# Generated at 2022-06-14 16:58:15.061307
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    _, method_type = (
        getattr(SafariBaseIE, '_login', None) or
        getattr(SafariBaseIE, '_real_initialize')).__self__.__code__.co_varnames
    assert method_type == 'initialize'

# Generated at 2022-06-14 16:58:21.270673
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # test constructor of class SafariBaseIE
    obj = SafariBaseIE()
    assert obj.LOGGED_IN == False
    obj._real_initialize()
    assert obj.LOGGED_IN == False
    obj.LOGGED_IN = True
    obj._real_initialize()
    assert obj.LOGGED_IN == True

# Generated at 2022-06-14 16:58:30.029252
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    """This test case checks if SafariApiIE constructor fails when
    safaribooksonline.com is unreachable.
    """
    import socket
    import unittest
    from ytdl_safari_common import \
        SafariBaseIE, compat_urlparse, compat_parse_qs, ExtractorError

    class MockSafariApiIE(SafariBaseIE):
        def _download_webpage(self, url, video_id, note, errnote):
            # This method is not tested, so we can return a dummy value.
            return ('{"foo": "bar"}', None)


# Generated at 2022-06-14 16:58:36.143117
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from ..compat import unittest

    class TestSafariApiIE(unittest.TestCase):
        def test_SafariApiIE_constructor(self):
            self.assertRaises(Exception, SafariApiIE)

    unittest.main(argv=[''])

if __name__ == '__main__':
    test_SafariApiIE()

# Generated at 2022-06-14 16:58:38.341917
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safari_course_ie = SafariCourseIE()
    instance = safari_course_ie._real_initialize()

# Generated at 2022-06-14 16:58:50.178078
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    course_id = '9780133392838'
    part = 'part00.html'
    web_url = ('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/'
               '9780133392838/part00.html')
    data = {'web_url': web_url}
    extractor = SafariApiIE(SafariApiIE.ie_key())

# Generated at 2022-06-14 16:58:54.622594
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from .test_downloader import FakeCustomDownloader
    from .test_utils import TestDownloader

    TestDownloader({'username': 'a', 'password': 'b'}, {},
                   SafariBaseIE({}, FakeCustomDownloader))

# Generated at 2022-06-14 16:58:56.653715
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # test SafariIE
    result = SafariIE()._real_initialize()
    assert result is None

# Generated at 2022-06-14 16:59:48.870924
# Unit test for constructor of class SafariIE
def test_SafariIE():
    test_case = SafariIE()

# Generated at 2022-06-14 16:59:51.780760
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    s = SafariBaseIE()
    assert s._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:59:53.420208
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    obj = SafariBaseIE(None) # pylint: disable=abstract-class-instantiated

# Generated at 2022-06-14 16:59:54.155144
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE('SafariCourseIE')

# Generated at 2022-06-14 17:00:02.609038
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html'
    mobj = re.match(SafariApiIE._VALID_URL, url)
    book_id = mobj.group('course_id')
    part_id = mobj.group('part')
    result = SafariApiIE()._download_json(url, '{}-{}'.format(book_id, part_id), 'Downloading JSON')
    assert result['web_url'] == 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'

# Generated at 2022-06-14 17:00:04.164923
# Unit test for constructor of class SafariIE
def test_SafariIE():
    i = SafariIE()
    assert isinstance(i, SafariBaseIE)
    return

# Generated at 2022-06-14 17:00:10.913411
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'
    

# Generated at 2022-06-14 17:00:20.921230
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Test with a valid URL
    IE = SafariCourseIE('safari:course', 'safaribooksonline.com online courses')
    course_id = '9781449396459'
    course_title = 'Learning Python'
    entries = ['http://techbus.safaribooksonline.com/9781449396459/toc.html']

    course_json = json.loads(open('test/test_data/techbus_toc.json', 'rb').read().decode('utf-8'))
    playlist = SafariCourseIE._real_extract(IE, 'http://techbus.safaribooksonline.com/9781449396459/')
    assert playlist['title'] == course_title
    assert playlist['id'] == course_id
    assert playlist['entries'] == entries
    assert playlist['_type']

# Generated at 2022-06-14 17:00:21.872005
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE(None, {}) != None



# Generated at 2022-06-14 17:00:23.875304
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assertNotRegex(SafariApiIE, "^safari:api$", "SafariApiIE must not be considered as compatible with SafariApiIE")

# Generated at 2022-06-14 17:02:44.569920
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE("http://techbus.safaribooksonline.com/9780134426365")

# Generated at 2022-06-14 17:02:55.789651
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import unittest
    from safaribooksonline import SafariApiIE
    from tests import FakeYDL

    class IncompleteDownloadError(Exception):
        pass

    class MockIE():
        def __init__(self):
            self._downloader = FakeYDL()

    class MockIE2():
        def __init__(self):
            self._downloader = FakeYDL()
            self.LOGGED_IN = True

    class MockIE3():
        def __init__(self):
            self._downloader = FakeYDL()

        def _get_login_info(self):
            return (None, None)


# Generated at 2022-06-14 17:03:03.607242
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert SafariIE().IE_NAME == 'safari'
    assert SafariIE()._VALID_URL == '^https?://(?:www\\.)?(?:safaribooksonline|(?:learning\\.)?oreilly)\\.com/(?:library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?#&]+)\\.html|videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?#&]+))$'
    assert SafariIE().IE_DESC == 'safaribooksonline.com online video'
    assert SafariIE()._PARTNER_ID == '1926081'
    assert SafariIE()._UICONF_ID == '29375172'

# Generated at 2022-06-14 17:03:04.597336
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    e = SafariApiIE()
    assert(e)


# Generated at 2022-06-14 17:03:11.924602
# Unit test for constructor of class SafariCourseIE

# Generated at 2022-06-14 17:03:13.316728
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    obj = SafariCourseIE(None)
    assert obj.name == 'safari:course'

# Generated at 2022-06-14 17:03:19.446822
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = "https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html"
    try:
        safari = SafariIE()
        print("Test succeeded")
    except ExtractorError:
        print("Test failed")

# Generated at 2022-06-14 17:03:26.272290
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from ..test.test_utils import get_testdata_file
    from ..utils import json_loads

    credentials_file_path = get_testdata_file('safari_cookies.json')
    with file(credentials_file_path, 'rb') as f:
        cookies = json_loads(f.read().decode('ascii'))

    # this only works if the user passed in the cookie. if user passed in the
    # username and password it won't work because safari doesn't allow login
    # with username and password
    se = SafariIE(cookies=cookies)
    se._real_initialize()
    assert se.LOGGED_IN

# Generated at 2022-06-14 17:03:29.742881
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # test constructors that do not throw exceptions
    SafariApiIE('safari')
    SafariApiIE(SafariIE.ie_key())
    SafariApiIE('Safari')
    SafariApiIE(SafariIE.ie_key().upper())


# Generated at 2022-06-14 17:03:31.068217
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE('test', 'www.safaribooksonline.com')