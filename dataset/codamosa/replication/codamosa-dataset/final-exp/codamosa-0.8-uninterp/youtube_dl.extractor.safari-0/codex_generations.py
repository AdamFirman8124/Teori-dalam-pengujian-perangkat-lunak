

# Generated at 2022-06-14 16:55:54.141991
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    course_json = {
        'chapters' : [
            'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html',
            'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part01.html',
        ],
        'title': 'Hello World',
    }

    course_id = '9781449396459'

    course_title = 'Hello World'

    safari_course_info_extractor = SafariCourseIE()

    entries = [
        SafariApiIE().url_result(chapter, SafariApiIE.ie_key())
        for chapter in course_json['chapters']]

    for index in range(1, len(entries)):
        assert saf

# Generated at 2022-06-14 16:55:58.555334
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():

    # input URL
    url = 'https://techbus.safaribooksonline.com/9781783286693'
    # create instance of SafariCourseIE
    i = SafariCourseIE()
    # example of class method
    assert(i.suitable(url) == True);

# Generated at 2022-06-14 16:56:04.359327
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE()
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    assert isinstance(safari._download_webpage_handle(url, None, 'Downloading login page'), tuple)

# Generated at 2022-06-14 16:56:15.941996
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE()
    assert safari.IE_NAME == 'safari'
    assert safari.IE_DESC == 'safaribooksonline.com online video'
    assert safari._VALID_URL == r'''(?x)
                        https?://
                            (?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/
                            (?:
                                library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?\#&]+)\.html|
                                videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?\#&]+)
                            )
                    '''

# Generated at 2022-06-14 16:56:25.882280
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .test_utils import (
        FakeCookieJar, FakeCookieJarHandler, sanity_check_cookies,
        FakeHTTPServer, extract_fake_response, mock_kaltura_response,
        urlopen, match_expected_title,
    )

    safari_ie = SafariBaseIE()


# Generated at 2022-06-14 16:56:30.900694
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .test_downloader import g_testdownloader
    dl = object.__new__(g_testdownloader)
    dl.to_screen = lambda *x: None
    ie = SafariIE(dl)
    # Force login
    ie._download_webpage_handle('https://www.safaribooksonline.com/library/view/linux-system-programming/9781449346172/part00.html', None, 'Downloading login page')
    assert ie.LOGGED_IN

# Generated at 2022-06-14 16:56:32.001724
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .test_safari import test_SafariIE as safariIE_test
    safariIE_test()

# Generated at 2022-06-14 16:56:43.617237
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Case 1:
    # Logging in with safaribooksonline.com account credentials
    # If a NetworkError is raised, the LOGGED_IN flag of the instance
    # of class SafariBaseIE is set to False
    # NOTE: This test can not check whether the login was successfull
    #       (that is, the check in _login() whether the user is logged in)
    o = SafariBaseIE()
    o._download_webpage = lambda *a, **k: raise_NetworkError()
    o._real_initialize()
    if o.LOGGED_IN == True:
        raise assert_fail('Case 1: LOGGED_IN flag of the SafariBaseIE instance is not set to False')
    # Case 2:
    # Login with a non-existing account:
    # The stored exception should be re-raised to

# Generated at 2022-06-14 16:56:48.417767
# Unit test for constructor of class SafariIE
def test_SafariIE():
    class TestSafariIE(SafariIE):
        def _download_json(self, *args, **kwargs):
            return kwargs["url"], None

        def _download_webpage(self, *args, **kwargs):
            return "", None

        @classmethod
        def _get_login_info(cls, *args, **kwargs):
            return "", ""

    TestSafariIE._LOGIN_URL = "https://learning.oreilly.com/accounts/login/"
    TestSafariIE._NETRC_MACHINE = "safari"
    TestSafariIE._TESTS[0]['url'] = "https://learning.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html"


# Generated at 2022-06-14 16:56:49.322595
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()

# Generated at 2022-06-14 16:57:14.265078
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ies = SafariIE()

# Generated at 2022-06-14 16:57:17.866745
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from .test import gettestcases

    for t in gettestcases():
        # only testing constructor of class SafariApiIE
        # because it is called while importing module safari.py
        if not hasattr(t, 'url') or 'safaribooksonline' not in t.url:
            continue
        SafariApiIE(t.ie, t.url)

# Generated at 2022-06-14 16:57:20.222066
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    a = SafariCourseIE()
    a.suitable(url)
    a.extract(url)

# Generated at 2022-06-14 16:57:21.584631
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert type(SafariCourseIE({})) == SafariCourseIE

# Generated at 2022-06-14 16:57:22.944384
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE(None)

# Generated at 2022-06-14 16:57:29.070402
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    safari_course = SafariCourseIE()
    safari_course.suitable(url)
    safari_course._real_extract(url)
    return True

# Generated at 2022-06-14 16:57:34.218332
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/1_1_1_.html'
    safariApiIE = SafariApiIE(SafariApiIE.ie_key())
    safariApiIE._real_extract(url)

# Generated at 2022-06-14 16:57:44.043742
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Test for setting both user and password for SafariBaseIE
    safari_base_IE = SafariBaseIE('user', 'password')
    assert safari_base_IE.username == 'user'
    assert safari_base_IE.password == 'password'
    # Test for setting only user for SafariBaseIE
    safari_base_IE = SafariBaseIE('user')
    assert safari_base_IE.username == 'user'
    assert safari_base_IE.password == None
    # Test for setting SafariBaseIE as class variable
    safari_base_IE = SafariBaseIE()
    safari_base_IE.username = 'user'
    safari_base_IE.password = 'password'
    assert safari_base_IE.username == 'user'
    assert safari_base_IE.password == 'password'

# Generated at 2022-06-14 16:57:47.683091
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = 'http://techbus.safaribooksonline.com/9780133392838/00_SeriesIntro'
    mobj = re.match(SafariIE._VALID_URL, url)
    part = SafariIE()._real_extract(url)
    assert part.get('id') == '0_qbqx90ic'

# Generated at 2022-06-14 16:57:58.104186
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    format_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    course_id = '9781449396459'
    video_id = '9781449396459-part00'

    # Test for SafariApiIE constructor
    ie = SafariApiIE()
    assert ie.suitable(format_url)

    # Test for SafariApiIE._real_extract method
    part = ie._download_json(
        format_url, video_id,
        'Downloading part JSON')
    assert part['web_url'] == 'https://www.safaribooksonline.com/library/view/learning-python-5e/9781449396459/part00.html'

# Generated at 2022-06-14 16:58:31.171958
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE('http://www.safaribooksonline.com/library/view/javascript-the-good/9781305256561/part02.html')
    assert ie.url == 'https://www.safaribooksonline.com/library/view/javascript-the-good/9781305256561/part02.html'
    assert ie.video_id == '9781305256561-part02'
    assert ie._PARTNER_ID == '1926081'
    assert ie._UICONF_ID == '29375172'

# Generated at 2022-06-14 16:58:39.843869
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    import json
    import re

    class MockMgrDownload:
        def __init__(self, response):
            self._response = response

        def retrieve(self, url, filename, *args, **kwargs):
            return (filename, self._response)

    class MockHTTPDownloadHandler(object):
        def __init__(self, url, response, headers):
            self.url = url
            self.response = response
            self.headers = headers

        def get_url(self):
            return self.url

        def read(self, _):
            return self.response

        def geturl(self):
            return self.url

        def info(self):
            return self.headers


# Generated at 2022-06-14 16:58:41.478103
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE()
    assert ie.IE_NAME == 'safari:course'

# Generated at 2022-06-14 16:58:47.107300
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api=SafariApiIE()
    # pylint: disable=W0212
    assert(safari_api._TESTS[0]['url']=='https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')

# Generated at 2022-06-14 16:58:54.574380
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    for url, expected in [
        ('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json', 'https://www.safaribooksonline.com/library/view/9781449396459/'),
        ('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json&foobar=baz', 'https://www.safaribooksonline.com/library/view/9781449396459/'),
        ('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=xml', None),
    ]:
        assert SafariApiIE._build_url(url) == expected

# Generated at 2022-06-14 16:59:05.008203
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """ Minimal test of SafariBaseIE constructor. """
    # Do only a minimal test of the SafariBaseIE constructor.
    # None of the other tests use it, because there is no
    # working extractor that inherits from it.
    from ydl.youtube_dl.extractor.common import InfoExtractor
    from ydl.youtube_dl.options import opts
    class MockSafariBaseIE(SafariBaseIE):
        def __init__(self, url):
            InfoExtractor.__init__(self)
            self.url = url
    ie = MockSafariBaseIE('http://example.com/foo')
    ie.initialize()
    assert ie.opts == opts

# Generated at 2022-06-14 16:59:07.611667
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE(SafariCourseIE._create_ie())
    assert ie.name() == 'safari:course'
    assert ie.ie_key() == 'SafariCourse'

# Generated at 2022-06-14 16:59:09.869370
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE()
    assert ie.LOGGED_IN == False

# Generated at 2022-06-14 16:59:14.358894
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    SafariApiIE(SafariBaseIE.ie_key()).suitable(url)

# Generated at 2022-06-14 16:59:27.541370
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """Unit test for constructor of class SafariIE"""
    safari_ie_test_object = SafariIE(
        compat_urllib_request.Request("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html"),
        compat_urllib_request.urlopen("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html"))
    assert_equal(
        safari_ie_test_object._LOGIN_URL,
        'https://learning.oreilly.com/accounts/login/')
    assert_equal(safari_ie_test_object._NETRC_MACHINE, 'safari')


# Generated at 2022-06-14 16:59:57.831208
# Unit test for constructor of class SafariIE
def test_SafariIE():
    global IE_NAME, IE_DESC
    IE_NAME = 'SafariIE'
    IE_DESC = 'safaribooksonline.com online video'
    SafariIE()

# Generated at 2022-06-14 17:00:05.293438
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    test_SafariApiIE = SafariApiIE()
    expected_attributes = ['_API_BASE',
                           '_API_FORMAT',
                           '_VALID_URL',
                           'IE_DESC',
                           'IE_NAME',
                           '_TEST',
                           '_LOGIN_URL',
                           '_NETRC_MACHINE']
    test_attributes = vars(test_SafariApiIE)
    # Check that all expected attributes are present
    assert set(expected_attributes) == set(test_attributes.keys())
    # Check that the attribute types are correct
    assert type(test_SafariApiIE._API_BASE) is str
    assert type(test_SafariApiIE._API_FORMAT) is str
   

# Generated at 2022-06-14 17:00:09.193347
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """
    Constructor test for class SafariBaseIE
    """

    safariBaseIE = SafariBaseIE(SafariBaseIE.ie_key())
    # Assertion: class name should be SafariBaseIE
    assert safariBaseIE.ie_key() == 'SafariBase'

# Generated at 2022-06-14 17:00:11.885510
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE is not None

# Generated at 2022-06-14 17:00:13.914055
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari_ie = SafariIE()
    assert safari_ie.LOGGED_IN == False


# Generated at 2022-06-14 17:00:14.542230
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    instance = SafariApiIE()

# Generated at 2022-06-14 17:00:22.791025
# Unit test for constructor of class SafariBaseIE

# Generated at 2022-06-14 17:00:25.432517
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # pylint: disable=no-member
    assert(SafariCourseIE.suitable(
        'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'))


# Generated at 2022-06-14 17:00:26.041113
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('Kaltura')

# Generated at 2022-06-14 17:00:30.847750
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE(SafariBaseIE(), 'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html')

# Generated at 2022-06-14 17:01:47.872589
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE(None)

# Generated at 2022-06-14 17:01:53.029802
# Unit test for constructor of class SafariIE
def test_SafariIE():
    #
    # Testing code
    #
    test_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    instance = SafariIE()
    video_id = instance._match_id(test_url)
    assert instance.ie_key() == 'Safari'
    assert video_id == '9780133392838/part00'

# Generated at 2022-06-14 17:01:58.926466
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    SafariCourseIE('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    SafariApiIE('https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html')

# Generated at 2022-06-14 17:02:02.926979
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE('www.safaribooksonline.com/api/v1/book')._VALID_URL == SafariApiIE._VALID_URL

# Generated at 2022-06-14 17:02:03.502170
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    t = SafariBaseIE()
    assert t is not None

# Generated at 2022-06-14 17:02:06.938497
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9780134664057/chapter/RHCE_Introduction/'
    SafariApiIE().url_result(url, 'Safari')

# Generated at 2022-06-14 17:02:19.255534
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert SafariIE('SafariBaseIE')._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert SafariIE('SafariBaseIE')._API_FORMAT == 'json'
    assert SafariIE('SafariBaseIE').IE_NAME == 'SafariBaseIE'
    assert SafariIE('SafariBaseIE').IE_DESC == 'safaribooksonline.com Base Class'
    assert SafariIE('SafariBaseIE')._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert SafariIE('SafariBaseIE')._NETRC_MACHINE == 'safari'
    assert SafariIE('SafariBaseIE').LOGGED_IN == False
    assert SafariIE('SafariBaseIE')._VALID_URL

# Generated at 2022-06-14 17:02:22.009521
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE()
    assert safari_api_ie.IE_NAME == 'safari:api'



# Generated at 2022-06-14 17:02:26.037213
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """ Test to check the constructor of SafariCourseIE class """
    SafCourse = SafariCourseIE()
    assert SafCourse.IE_NAME == 'safari:course'
    assert SafCourse.IE_DESC == 'safaribooksonline.com online courses'

    return SafCourse

# Generated at 2022-06-14 17:02:28.311123
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    instance = SafariBaseIE()
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 17:05:22.188097
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    import pprint
    import sys


# Generated at 2022-06-14 17:05:32.781985
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from tempfile import NamedTemporaryFile
    from ..utils import USER_AGENTS, USER_AGENT

    # Test with an empty netrc file
    with NamedTemporaryFile(delete=True) as f:
        ie = SafariBaseIE(f.name)
        assert ie.NETRC_MACHINE == ie._NETRC_MACHINE

    # Test with a non-existing netrc file
    with NamedTemporaryFile(delete=True) as f:
        f.close()
        ie = SafariBaseIE(f.name)
        assert ie.NETRC_MACHINE == ie._NETRC_MACHINE

    # Test with a fake netrc file
    with NamedTemporaryFile(delete=True) as f:
        f.write(b'fake:login:pass')
        f.flush()
        ie = SafariBase