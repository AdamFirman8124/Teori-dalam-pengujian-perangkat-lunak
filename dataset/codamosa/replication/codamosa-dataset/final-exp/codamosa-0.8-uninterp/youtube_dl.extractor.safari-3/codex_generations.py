

# Generated at 2022-06-14 16:55:45.129409
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    class TestSafariApiIE(SafariApiIE):
        def _login(self):
            pass
    test_SafariApiIE().to_screen('http://example.com')

# Generated at 2022-06-14 16:55:48.786518
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE.suitable('https://www.safaribooksonline.com/library/view/cooking-for-geeks/9781449313939/')

# Generated at 2022-06-14 16:55:58.561246
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    TestInfoExtractor = SafariBaseIE.make_test_ie(SafariApiIE)
    TestInfoExtractor.test({
        'url': 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html',
        'md5': 'dcc5a425e79f2564148652616af1f2a3',
        'info_dict': {
            'id': '0_qbqx90ic',
            'ext': 'mp4',
            'title': 'Introduction to Hadoop Fundamentals LiveLessons',
            'timestamp': 1437758058,
            'upload_date': '20150724',
            'uploader_id': 'stork',
        },
    })

# Generated at 2022-06-14 16:56:00.011507
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    instance = SafariBaseIE()
    assert isinstance(instance, SafariBaseIE)
    assert instance.ie_key() == "SafariBaseIE"

# Generated at 2022-06-14 16:56:01.749318
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE.suitable(SafariCourseIE._VALID_URL)

# Generated at 2022-06-14 16:56:03.288359
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('')
    SafariIE('', {})

# Generated at 2022-06-14 16:56:10.871730
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Check for the attributes of SafariBaseIE class
    assert hasattr(SafariBaseIE, '_LOGIN_URL')
    assert hasattr(SafariBaseIE, '_NETRC_MACHINE')
    assert hasattr(SafariBaseIE, '_API_BASE')
    assert hasattr(SafariBaseIE, '_API_FORMAT') 
    assert hasattr(SafariBaseIE, 'LOGGED_IN')

# Generated at 2022-06-14 16:56:13.192903
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    inst = SafariApiIE.ie_key()
    assert inst.ie_key() == 'SafariApi'


# Generated at 2022-06-14 16:56:15.109152
# Unit test for constructor of class SafariIE
def test_SafariIE():
    i = SafariIE()

# Generated at 2022-06-14 16:56:19.960290
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # This test is in the SafariCourseIE class because it uses the
    # SafariBaseIE class constructor, which none of the other
    # extractors can use.
    safari = SafariCourseIE()
    msg = "Expected to be in True/False"
    assert safari.LOGGED_IN == False, msg

# Generated at 2022-06-14 16:56:44.068378
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    test_class = type('TestClass', (object,), {
        '_download_webpage': lambda self, url: compat_urlparse.urlparse(url).netloc,
        '_download_json': lambda self, url: compat_urlparse.urlparse(url).netloc,
        '_login_slug': 'test',
        '_LOGIN_URL': 'http://login_url',
        '_NETRC_MACHINE': 'safari',
    })

    obj = test_class()
    # test username and password in arguments
    obj.login('testuser1', 'testpass1')
    assert obj._download_webpage.call_count == 1

# Generated at 2022-06-14 16:56:50.577315
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'

    if len(sys.argv) < 2:
        print('Usage: --login <your user name> <your password>')
        sys.exit(1)

    username = sys.argv[2]
    password = sys.argv[3]
    
    ie = SafariCourseIE(SafariCourseIE.ie_key())
    ie.set_login_info(SafariBaseIE._NETRC_MACHINE, username, password)
    ie.initialize()

    response = ie.extract(url)
    
    print(response)

# Generated at 2022-06-14 16:56:52.178338
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('http://example.org')._real_initialize()

# Generated at 2022-06-14 16:56:59.892951
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # The following cases should raise an exception
    SafariCourseIE("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/")
    SafariCourseIE("https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json")
    SafariCourseIE("https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838")

    # The following cases should be processed properly
    SafariCourseIE("http://techbus.safaribooksonline.com/9780134426365")
    SafariCourseIE("https://www.safaribooksonline.com/videos/python-programming-language/9780134217314")
   

# Generated at 2022-06-14 16:57:06.036608
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    cls = type('temp', (SafariBaseIE,), dict())
    try:
        cls(None)
    except ExtractorError:
        pass
    else:
        raise Exception('Expected exception when login info is missing')

# Generated at 2022-06-14 16:57:07.562588
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert SafariIE().ie_key() == 'Safari'



# Generated at 2022-06-14 16:57:11.823017
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE('https://video.oreilly.com/learning-paths/0134664057-red-hat/RHCE_Introduction.html')
    assert ie.LOGGED_IN == False
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:57:13.211006
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE()
    assert safari_api_ie._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:57:14.360809
# Unit test for constructor of class SafariIE
def test_SafariIE():
    instance = SafariIE()
    # Running constructor
    instance.suitable(None)

# Generated at 2022-06-14 16:57:15.882620
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()

# Generated at 2022-06-14 16:57:48.874419
# Unit test for constructor of class SafariIE
def test_SafariIE():
    result = SafariIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    assert result == True
    result = SafariIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons')
    assert result == False
    result = SafariIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/')
    assert result == False
    result = SafariIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/97801333928383/part00.html')


# Generated at 2022-06-14 16:57:58.834826
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Initialize class with extracted url
    url = 'https://www.safaribooksonline.com/library/view/sass-and-compass/9781430264489/ch01.html'
    obj = SafariBaseIE(SafariIE.IE_NAME, url)

    # Validate extractor for the given url
    assert obj.suitable(url)

    # Test case for SafariBaseIE._download_json_handle
    query_params = {'foo': 'bar'}
    query_str = '?foo=bar'
    url_str = 'https://www.safaribooksonline.com/library/view/sass-and-compass/9781430264489/ch01.html'
    url_str += query_str

# Generated at 2022-06-14 16:58:05.864712
# Unit test for constructor of class SafariCourseIE

# Generated at 2022-06-14 16:58:07.234139
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Just check that it's constructed without errors
    SafariApiIE('SafariApiIE')

# Generated at 2022-06-14 16:58:19.173646
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # The following codes are used for unit test
    from .test import get_testcases, list_testcases
    from .common import initialize_downloader, get_suitable_downloader
    from .extractor.common import list_extractors

    class SafariCourseUnitTest(SafariCourseIE):
        IE_NAME = 'safari:unit_test'

    class SafariUnitTest(SafariCourseUnitTest):
        IE_NAME = 'safari:unit_test'

    # Prepare downloader and extractor
    downloader = initialize_downloader({'prefer_insecure': True})
    SafariCourseUnitTest.downloader = downloader
    SafariUnitTest.downloader = downloader
    downloader.add_info_extractor(SafariCourseUnitTest)

# Generated at 2022-06-14 16:58:22.053121
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/learning-path-red/9780134664057/RHCE_Introduction.html'
    SafariCourseIE().suitable(url)

# Generated at 2022-06-14 16:58:30.643866
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    import unittest
    import requests
    import requests_mock
    from requests.adapters import HTTPAdapter

    # Mock requests to use the comptable JSON
    with requests_mock.Mocker(real_http=True) as m:
        # mock the request to return the test JSON
        m.get(requests.Request(
            # set up HTTP adapter
            url="https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json").prepare().url,
              text=open('test/test_data/test_course/9781449396459.json', 'r').read())

        # Mock the session object to use the adapter
        with requests.Session() as s:
            s.mount('https://', HTTPAdapter())
            # Mock the result to use

# Generated at 2022-06-14 16:58:33.903639
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    req = SafariCourseIE()
    assert req.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')

# Generated at 2022-06-14 16:58:37.259542
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    IE = SafariCourseIE('www.safaribooksonline.com', {})
    assert IE._VALID_URL != SafariCourseIE._VALID_URL

# Generated at 2022-06-14 16:58:38.708599
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE()._VALID_URL == SafariCourseIE._VALID_URL

# Generated at 2022-06-14 16:59:31.466073
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safaribase_ie = SafariBaseIE(10)
    assert safaribase_ie.LOGGED_IN == False

# Generated at 2022-06-14 16:59:34.778767
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE('safari')
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert ie._API_FORMAT == 'json'

# Generated at 2022-06-14 16:59:37.288540
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert isinstance(SafariCourseIE(), SafariCourseIE)
    assert isinstance(SafariCourseIE(), SafariBaseIE)

# Generated at 2022-06-14 16:59:47.080908
# Unit test for constructor of class SafariIE
def test_SafariIE():
    import sys
    sys.stderr.write("Invoke unit test for safaribooksonline.com extractor\n")
    safari_ie = SafariIE()
    video_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    sys.stderr.write("Unit test for %s\n" % video_url)
    safari_ie.extract('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    sys.stderr.write("Unit test finished\n")

# Generated at 2022-06-14 16:59:48.939240
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE


__all__ = ['SafariApiIE']


# vim:ts=4:sw=4:et

# Generated at 2022-06-14 16:59:50.056986
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838'
    assert SafariCourseIE.suitable(url)

# Generated at 2022-06-14 17:00:00.492378
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE()
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:
                            (?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/
                            (?:
                                library/view/[^/]+|
                                api/v1/book|
                                videos/[^/]+
                            )|
                            techbus\.safaribooksonline\.com
                        )
                        /(?P<id>[^/]+)
                    '''
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert ie._API_FORMAT == 'json'
    assert ie._NETRC_MACHINE == 'safari'
    assert ie.IE_

# Generated at 2022-06-14 17:00:12.039547
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """
    Constructor test
    """
    ie = SafariIE()
    assert ie.IE_NAME == 'safari'
    assert ie.IE_DESC == 'safaribooksonline.com online video'
    assert ie._VALID_URL == r'''(?x)
                        https?://
                            (?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/
                            (?:
                                library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?\#&]+)\.html|
                                videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?\#&]+)
                            )
                    '''



# Generated at 2022-06-14 17:00:15.344812
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # These lines create an instance of the SafariBaseIE class
    # and test its constructor
    ie = SafariBaseIE()
    ie._real_initialize()
    assert ie._NETRC_MACHINE == 'safari'

# Generated at 2022-06-14 17:00:20.577733
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    def get_login_info(self):
        return None    # Don't authenticate

    safaribase = SafariBaseIE()
    safaribase._get_login_info = get_login_info.__get__(safaribase)
    safaribase._real_initialize()
    assert safaribase.LOGGED_IN == False

# Generated at 2022-06-14 17:01:42.519478
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from ..compat import compat_urllib_parse_urlparse
    from ..test.test_safaribooksonline import fake_login_info
    from ..test.test_safaribooksonline import fake_login_info_encoded
    from ..test.test_safaribooksonline import fake_login_info_encoded_password_only

    for fake_login_info in [fake_login_info, fake_login_info_encoded, fake_login_info_encoded_password_only]:
        ie = SafariBaseIE()
        ie._get_login_info = fake_login_info
        result_url, result_data = ie._login()
        
        parsed_url = compat_urllib_parse_urlparse(result_url)
        # The urlq.query should be a string, e.

# Generated at 2022-06-14 17:01:49.393470
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # testing safaribooksonline without explicit login credentials
    try:
        SafariBaseIE('safari')
    except TypeError as e:
        assert(e.message == '__init__() takes at least 5 arguments (4 given)')
    else:
        assert(False)

    # testing oreillycom with explicit login credentials
    try:
        SafariBaseIE('oreillycom', 'test@example.com', 'password')
    except TypeError as e:
        assert(e.message == '__init__() takes at least 5 arguments (6 given)')
    else:
        assert(False)

    # testing safaribooksonline with explicit login credentials

# Generated at 2022-06-14 17:01:56.494851
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base = SafariBaseIE()
    assert safari_base._LOGIN_URL == "https://learning.oreilly.com/accounts/login/"
    assert safari_base._NETRC_MACHINE == "safari"
    assert safari_base._API_BASE == "https://learning.oreilly.com/api/v1"
    assert safari_base._API_FORMAT == "json"
    assert safari_base.LOGGED_IN == False

# Generated at 2022-06-14 17:02:02.077815
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # first test if all modules imported correctly
    SafariBaseIE._download_webpage_handle('http://www.google.com', None, 'Downloading login page')
    SafariBaseIE._download_json('http://www.google.com', 'Downloading login page')
    SafariBaseIE._apply_first_set_cookie_header('', '')
    SafariBaseIE._get_login_info()
    SafariBaseIE._login()
    SafariBaseIE.LOGGED_IN
    SafariBaseIE.IE_NAME
    SafariBaseIE.IE_DESC
    SafariBaseIE._VALID_URL
    SafariBaseIE._TESTS
    SafariBaseIE._real_initialize()

# Generated at 2022-06-14 17:02:02.737051
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 17:02:10.543853
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    import os
    from ..utils import (
        prepend_extension,
        remove_start,
    )

    # test SafariBaseIE.get_video_info
    # no credentials
    SafariBaseIE.get_video_info('https://www.safaribooksonline.com/library/view/data-science-from/9781491901410/')

    # with credentials
    login = os.environ.get('SAFARI_LOGIN')
    password = os.environ.get('SAFARI_PASSWORD')
    if login is None or password is None:
        raise Exception('Please set %s and %s environment variables' % ('SAFARI_LOGIN', 'SAFARI_PASSWORD'))

# Generated at 2022-06-14 17:02:12.637990
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """
    Test creation of class SafariIE.
    """
    ie = SafariIE()
    return ie

# Generated at 2022-06-14 17:02:18.377648
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    with open('test/testdata/unicode_filename.json') as f:  
        data = json.load(f)
    
    course_id = data["course_id"]
    part = data["part"]
    course_title = data["course_title"]
    title = data["title"]
    ext = data["ext"]
    reference_id = data["reference_id"]
    partner_id = data["partner_id"]
    ui_id = data["ui_id"]
    session = data["session"]
    query = data["query"]

    SafariBaseIE.IE_NAME = 'safari'
    SafariBaseIE.IE_DESC = 'safaribooksonline.com online video'
    SafariBaseIE.LOGGED_IN = True

# Generated at 2022-06-14 17:02:20.641579
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE();

# Generated at 2022-06-14 17:02:30.319121
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safaribooksonline_course = SafariCourseIE({})
    safaribooksonline_api = SafariApiIE({})
    assert safaribooksonline_api.IE_NAME == 'safari:api'
    assert safaribooksonline_api.IE_DESC is None
    assert safaribooksonline_api._VALID_URL == SafariApiIE._VALID_URL
    assert safaribooksonline_api._TESTS == SafariApiIE._TESTS
    assert safaribooksonline_api.IE_NAME == 'safari:api'
    assert safaribooksonline_api._downloader == safaribooksonline_course._downloader

# Generated at 2022-06-14 17:05:12.022508
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('http://www.safaribooksonline.com/library/view/mongodb-in-action/9781617290219/')


# Generated at 2022-06-14 17:05:16.706606
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Test case:
    #  - SafariApiIE does not construct object, when KeyError occurs
    #  - SaafiApiIE constructor always returns None
    results = {'id': None}
    ie = SafariApiIE()
    ie._download_json = lambda *args, **kwargs: results
    assert ie.extract('url') is None

# Generated at 2022-06-14 17:05:17.646474
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    instance = SafariBaseIE()


# Generated at 2022-06-14 17:05:19.428986
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():

    # Test constructor of SafariCourseIE
    test_course_ie = SafariCourseIE()

    # test object of class SafariCourseIE
    assert isinstance(test_course_ie, SafariCourseIE)

# Generated at 2022-06-14 17:05:25.478431
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from .test_utils import MockIE
    ie = MockIE('safari:api', r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/9781449396459/chapter/(?:content/)?part.*\.html')
    # the constructor should not raise an exception
    assert isinstance(ie, SafariApiIE)