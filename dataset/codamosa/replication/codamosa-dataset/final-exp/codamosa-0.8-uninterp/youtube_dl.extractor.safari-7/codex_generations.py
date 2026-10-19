

# Generated at 2022-06-14 16:55:48.032214
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'http://techbus.safaribooksonline.com/9780133392838'
    SafariCourseIE._download_webpage = lambda *args, **kwargs: None
    i = SafariCourseIE(SafariCourseIE.ie_key())
    i.suitable(url)
    i._real_initialize()

# Generated at 2022-06-14 16:55:51.243369
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safariCourseIE=SafariCourseIE()
    assert safariCourseIE._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safariCourseIE._API_FORMAT=='json'

# Generated at 2022-06-14 16:55:55.703304
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from .common import USERNAME, PASSWORD, USER_AUTH
    url = 'https://www.safaribooksonline.com/api/v1/book/9780147518492/?override_format=json'
    SafariCourseIE(US_AUTH, USERNAME, PASSWORD)
    SafariCourseIE(url)

# Generated at 2022-06-14 16:56:00.905103
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """
    Unit test for constructor of class SafariCourseIE.
    """
    url = 'http://techbus.safaribooksonline.com/9780134426365'
    ie = SafariCourseIE(url, {})
    assert ie.suitable(url)
    assert 'id' in ie._real_extract(url)

# Generated at 2022-06-14 16:56:06.348535
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Generating class object
    obj = SafariIE()
    # Calling real_extract method of class object
    obj._real_extract('https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838/9780133392838-00_SeriesIntro')

# Generated at 2022-06-14 16:56:16.981737
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE('hadoop-fundamentals-livelessons')
    assert safari_base_ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari_base_ie._API_FORMAT == 'json'
    assert safari_base_ie._NETRC_MACHINE == 'safari'
    assert safari_base_ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'

# Generated at 2022-06-14 16:56:26.964941
# Unit test for constructor of class SafariIE
def test_SafariIE():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    from .test_utils import _get_testdata_file_path
    from .common import fake_headers
    # create mock object for the _download_webpage_handle method
    # when it's called to download login page,
    #   its return value is the content of file "Safari_login_page.html"
    # when it's called to download login check,
    #   its return value is the content of file "Safari_after_login.html"
    mock_download_page = patch(
        'youtube_dl.extractor.safari.SafariIE._download_webpage_handle')

# Generated at 2022-06-14 16:56:33.315400
# Unit test for constructor of class SafariIE
def test_SafariIE():
    try:
        from .test_utils import get_testdata_path
    except ImportError:
        print('Please install the bin/utils.py script')
        return

    _LOGIN_NOTE = 'SafariIE requires a valid account to get access to the videos'

    import os.path
    import requests

    requests.packages.urllib3.disable_warnings()

    safari_username = os.environ.get('SAFARI_USERNAME')
    safari_password = os.environ.get('SAFARI_PASSWORD')

    # check for supplied account
    if not safari_username or not safari_password:
        print(_LOGIN_NOTE)
        return

    from .utils import xpath_text
    from .compat import compat_etree_fromstring
    from .common import InfoExt

# Generated at 2022-06-14 16:56:34.362439
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert issubclass(SafariCourseIE , SafariBaseIE)

# Generated at 2022-06-14 16:56:45.364621
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    _json = """{
  "status": "ok",
  "web_url": "https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html?orpq",
  "title": "\u00a0",
  "duration_seconds": 0,
  "duration": "0 seconds",
  "intro": "",
  "transcript": null,
  "downloads": {
    "pdf": "",
    "video": ""
  },
  "chapter_number": "0"
}"""

    ie = SafariApiIE()
    assert ie.suitable('https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html')


# Generated at 2022-06-14 16:57:15.344870
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    if not hasattr(test_SafariApiIE, "test_url"):
        test_SafariApiIE.test_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
        test_SafariApiIE.test_course_id = '9780133392838'
        test_SafariApiIE.test_part = 'part00'
        test_SafariApiIE.test_safari_api_ie_instance = SafariApiIE()
        test_SafariApiIE.test_safari_api_ie_instance._real_extract(test_SafariApiIE.test_url)
    return test_SafariApi

# Generated at 2022-06-14 16:57:19.502737
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    course_title = 'Hadoop Fundamentals LiveLessons'
    course_url = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838'
    safari_base_ie = SafariBaseIE._build_request(course_url)
    assert safari_base_ie._VALID_URL == SafariCourseIE._VALID_URL
    assert safari_base_ie._API_FORMAT == SafariBaseIE._API_FORMAT



# Generated at 2022-06-14 16:57:20.514666
# Unit test for constructor of class SafariIE
def test_SafariIE():
    pass

# Generated at 2022-06-14 16:57:25.220967
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE()
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert ie._API_FORMAT == 'json'
    assert not ie.LOGGED_IN

# Generated at 2022-06-14 16:57:37.375868
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    url0 = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    url1 = 'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_00'


# Generated at 2022-06-14 16:57:41.655880
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari = SafariBaseIE('safari:base')

    assert safari._NETRC_MACHINE == 'safari'
    assert safari._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari._API_FORMAT == 'json'
    assert safari.LOGGED_IN == False

# Generated at 2022-06-14 16:57:49.099405
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class TestSafariBaseIE(SafariBaseIE):
        @classmethod
        def _download_webpage_handle(self, url, video_id, note='', errnote='', fatal=True, data=None, headers={}, query={}, expected_status=None):
            return url, None
        @classmethod
        def _download_json_handle(self, url, video_id, note='', errnote='', fatal=True, data=None, headers={}, query={}, expected_status=None):
            return {}, None
        @classmethod
        def _apply_first_set_cookie_header(self, urlh, cookie):
            return

# Generated at 2022-06-14 16:57:58.722053
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # This function is to check the constructor of class SafariCourseIE
    # Unit test for constructor of class SafariCourseIE
    # The idea is that SafariCourseIE is not to be chosen for extracting content
    # for the URL given in SafariApiIE.
    # This is because the on the webpage, the webpage will already have media content
    # and so SafariApiIE is chosen to download that content. SafariCourseIE is only used
    # when we want to download the course content.
    a = SafariCourseIE()
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    option_chosen = a.suitable(url)
    assert not option_chosen, 'The URL is not a suitable'

# Generated at 2022-06-14 16:58:08.099875
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from .. import _get_testcases as get_testcases
    from .common import MockTestCase
    args = ('username', 'password')

    testcases = get_testcases(SafariBaseIE, [SafariCourseIE], [], [SafariBaseIE._NETRC_MACHINE])
    for testcase in testcases:
        test = MockTestCase(*[None] * len(testcase))
        inst = testcase(test, SafariBaseIE)
        inst._get_login_info = lambda self: args
        inst._real_initialize()
        assert inst.LOGGED_IN == True
        assert inst._download_webpage_handle

        test = MockTestCase(*[None] * len(testcase))
        inst = testcase(test, SafariBaseIE)

# Generated at 2022-06-14 16:58:11.082820
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE(SafariBaseIE()).ie_key() == 'SafariApi'


# Generated at 2022-06-14 16:58:46.067205
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE('safari')
    assert ie.LOGGED_IN is False

    assert ie.IE_NAME == 'safari'
    assert ie.IE_DESC == None
    assert ie._VALID_URL == None
    assert ie._NETRC_MACHINE == 'safari'
    assert ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert ie._API_FORMAT == 'json'

# Generated at 2022-06-14 16:58:46.826023
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE()

# Generated at 2022-06-14 16:58:49.184909
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert isinstance(SafariBaseIE(), SafariBaseIE)

# Generated at 2022-06-14 16:59:00.501100
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """
    Unit test for constructor of class SafariCourseIE
    """
    assert SafariCourseIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/') == True
    assert SafariCourseIE.suitable('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json') == True
    assert SafariCourseIE.suitable('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314') == True
    assert SafariCourseIE.suitable('https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838') == True

# Generated at 2022-06-14 16:59:03.297232
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    try:
        # Test whether SafariApiIE has been correctly constructed.
        SafariApiIE()
    except:
        return False
    else:
        return True

# Generated at 2022-06-14 16:59:09.664776
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    login_url = 'https://learning.oreilly.com/accounts/login/'
    api_base = 'https://learning.oreilly.com/api/v1'
    api_format = 'json'

    # Test constructor
    safari_test = SafariBaseIE()
    assert safari_test._LOGIN_URL == login_url
    assert safari_test._NETRC_MACHINE == 'safari'
    assert safari_test._API_BASE == api_base
    assert safari_test._API_FORMAT == api_format
    assert not safari_test.LOGGED_IN

# Generated at 2022-06-14 16:59:10.644344
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE("abc")


# Generated at 2022-06-14 16:59:12.050694
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    obj = SafariBaseIE()
    assert obj != None

# Generated at 2022-06-14 16:59:20.835679
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE()

    assert safari_api_ie.IE_NAME == 'safari:api'
    assert safari_api_ie.IE_DESC == 'safaribooksonline.com online courses'
    assert safari_api_ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'
    assert safari_api_ie.LOGGED_IN == False
    assert safari_api_ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari_

# Generated at 2022-06-14 16:59:30.290536
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """
    Test if SafariIE constructor works properly.
    In other words test the regex that matches URLs.
    """

    # fmt: off

# Generated at 2022-06-14 17:00:29.472027
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE(SafariBaseIE())


# Generated at 2022-06-14 17:00:33.509275
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    safari_api_ie = SafariApiIE(SafariBaseIE())
    assert safari_api_ie.suitable(url) == True

# Generated at 2022-06-14 17:00:34.054117
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 17:00:37.705628
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE()
    instance = safari.IE_NAME
    assert instance == "safari"
    desc = safari.IE_DESC
    assert desc == 'safaribooksonline.com online video'

# Generated at 2022-06-14 17:00:38.779100
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # FIXME
    pass

# Generated at 2022-06-14 17:00:47.550662
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    i = SafariApiIE()
    i._download_json = lambda *args: {
        'web_url': 'https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html',
    }
    i._real_extract('https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html')

# Generated at 2022-06-14 17:00:48.134922
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()

# Generated at 2022-06-14 17:00:54.274244
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Test one of the constructors of SafariBaseIE
    parser = SafariBaseIE._build_kaltura_config_url('test')
    assert parser.scheme == 'https'
    assert parser.netloc == 'cdnapisec.kaltura.com'
    assert parser.path == '/html5/html5lib/v2.38.2/mwEmbedFrame.php'
    assert parser.params == ''
    assert parser.query == 'wid=_test&uiconf_id=29375172'
    assert parser.fragment == ''

# Generated at 2022-06-14 17:01:02.823136
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE()
    assert safari_base_ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/', 'do not change _LOGIN_URL'
    assert safari_base_ie._NETRC_MACHINE == 'safari', 'do not change _NETRC_MACHINE'
    assert safari_base_ie._API_BASE == 'https://learning.oreilly.com/api/v1', 'do not change _API_BASE'
    assert safari_base_ie._API_FORMAT == 'json', 'do not change _API_FORMAT'
    assert safari_base_ie.LOGGED_IN == False, 'do not change LOGGED_IN'

# Generated at 2022-06-14 17:01:05.959218
# Unit test for constructor of class SafariIE
def test_SafariIE():
    obj = SafariIE()
    print(obj.__dict__)
    assert obj.__dict__['_login_form'] is not None



# Generated at 2022-06-14 17:03:45.636912
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE.suitable(
        'http://techbus.safaribooksonline.com/9780134426365')
    assert SafariCourseIE.suitable(
        'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314')
    assert SafariCourseIE.suitable(
        'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838')
    assert SafariCourseIE.suitable(
        'https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')

# Generated at 2022-06-14 17:03:50.785184
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # non-ascii chars in course title
    test_url = 'https://www.safaribooksonline.com/api/v1/book/9780134216572/?override_format=json'
    api_ie = SafariApiIE('')
    course_json = api_ie._download_json(test_url, None, '', '')
    assert course_json['title'] == 'Beginning iOS 10 Programming with Swift 3'

# Generated at 2022-06-14 17:04:01.490413
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    def test_constructor(cls, url, expected_host, expected_server, expected_auth, expected_path, expected_query):
        host = expected_host
        server = expected_server
        auth = expected_auth
        path = expected_path
        query = expected_query

        if cls!= SafariBaseIE:
            host = server = auth = path = query = None

        params = (url, host, server, auth, path, query)

        test_obj = cls(*params)

    test_constructor(SafariBaseIE, 'https://domain.example.com/path/', 'domain.example.com', 'domain.example.com', None, 'path/', {})

# Generated at 2022-06-14 17:04:03.527229
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # check if the constructor of class SafariApiIE not fails
    SafariApiIE("safari:api")

# Generated at 2022-06-14 17:04:11.695623
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Check __init__
    assert(SafariBaseIE._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/')
    assert(SafariBaseIE._NETRC_MACHINE == 'safari')
    assert(SafariBaseIE._API_BASE == 'https://learning.oreilly.com/api/v1')
    assert(SafariBaseIE._API_FORMAT == 'json')


# Generated at 2022-06-14 17:04:14.092870
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # get instance of SafariBaseIE
    safariBase = SafariBaseIE()
    # see if safariBase is an object of type SafariBaseIE
    assert isinstance(safariBase, SafariBaseIE)

# Generated at 2022-06-14 17:04:22.457533
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE(None)
    assert ie.suitable('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314') == False
    assert ie.suitable('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json') == False
    assert ie.suitable('http://techbus.safaribooksonline.com/9780134426365') == False



# Generated at 2022-06-14 17:04:26.099104
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE('www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')

# Generated at 2022-06-14 17:04:27.523810
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert str(SafariApiIE.ie_key()) == 'SafariApiIE'

# Generated at 2022-06-14 17:04:30.762197
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert SafariBaseIE(SafariCourseIE()).__name__ == 'SafariCourseIE'
    assert SafariBaseIE(SafariApiIE()).__name__ == 'SafariApiIE'