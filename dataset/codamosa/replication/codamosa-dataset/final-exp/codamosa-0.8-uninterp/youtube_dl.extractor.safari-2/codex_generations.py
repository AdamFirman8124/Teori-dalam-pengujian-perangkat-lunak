

# Generated at 2022-06-14 16:55:45.037777
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('Safari')

# Generated at 2022-06-14 16:55:56.220122
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import os
    import tempfile

    def write_file(filename, contents):
        with open(filename, 'wb') as f:
            f.write(contents)

    tmp = tempfile.mkdtemp()

    # Create a ~/.netrc file that only contains the necessary login information:
    # account=<username>
    # password=<password>
    write_file(os.path.join(tmp, '.netrc'), b'''
machine learning.oreilly.com login test_username password test_password
''')

    # Create a .cookies.lwp file that only contains the necessary login information:
    # learning.oreilly.com	FALSE	/	TRUE	10000000	groot_sessionid	SESSd4234ebc9b903c4d4df400004b93a37=kp6

# Generated at 2022-06-14 16:56:02.682839
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safariApi = SafariApiIE()
    assert safariApi._VALID_URL == 'https?://(?:www\\.)?(?:safaribooksonline|(?:learning\\.)?oreilly)\\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\\.html'

# Generated at 2022-06-14 16:56:13.049886
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    with open('test/test_data/safari.txt') as f:
        data = f.read()
    login_data = json.loads(data)
    safari_base_ie = SafariBaseIE(None)
    safari_base_ie._get_login_info = lambda: (login_data['username'], login_data['password'])
    safari_base_ie._real_initialize()
    safari_base_ie.real_extract('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')

# Generated at 2022-06-14 16:56:15.311473
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE._login()

# Generated at 2022-06-14 16:56:25.447070
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari = SafariApiIE()
    safari_course = SafariCourseIE()
    assert safari._VALID_URL == 'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'
    assert safari.IE_NAME == 'safari:api'
    assert safari.IE_DESC == 'safaribooksonline.com online courses'

# Generated at 2022-06-14 16:56:27.275405
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE._real_initialize()

# Tests for constructor of class SafariCourseIE

# Generated at 2022-06-14 16:56:29.209105
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .common import FakeLoginTestCase
    from .test_login import test_login_safari

    test_login_safari()

    FakeLoginTestCase()

# Generated at 2022-06-14 16:56:30.181566
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE().IE_NAME == 'safari:course'

# Generated at 2022-06-14 16:56:30.869011
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base = SafariBaseIE()

# Generated at 2022-06-14 16:56:43.551479
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    s = SafariApiIE()

# Generated at 2022-06-14 16:56:44.122903
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariBaseIE()

# Generated at 2022-06-14 16:56:51.041285
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    test_url = 'http://safaribooksonline.com/test/test_safari_api'
    test_id = 'test'
    test_webpage = '<div data-reference-id="test"></div>'

    # Build fake webpage for test
    test_course_webpage = '<div data-reference-id="test"></div>'
    with open('course.html', 'w') as f:
        f.write(test_course_webpage)
    # Build fake webpage for test
    # test_part_webpage = '<div data-reference-id="test"></div>'
    # with open('part.html', 'w') as f:
    #     f.write(test_part_webpage)

    # Test for course_id only in url


# Generated at 2022-06-14 16:57:00.782725
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Assign the SafariIE class to a variable so it can be easily instantiated
    safari_ie = SafariIE()
    assert safari_ie.IE_NAME == 'safari'
    assert safari_ie.IE_DESC == 'safaribooksonline.com online video'
    assert safari_ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?\#&]+)\.html|videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?\#&]+))'

# Generated at 2022-06-14 16:57:04.683684
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE()
    assert ie._API_FORMAT == 'json'
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:57:12.723371
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """Test the constructor of class SafariBaseIE."""
    safari_base_ie = SafariBaseIE()
    assert safari_base_ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert safari_base_ie._NETRC_MACHINE == 'safari'
    assert safari_base_ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari_base_ie._API_FORMAT == 'json'
    assert safari_base_ie.LOGGED_IN == False

# Generated at 2022-06-14 16:57:14.843534
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')

# Generated at 2022-06-14 16:57:21.630909
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE()
    assert ie.IE_NAME == 'safari:course'
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+|api/v1/book|videos/[^/]+)/(?P<id>[^/]+)'
    assert ie.LOGGED_IN == False
    assert ie._NETRC_MACHINE == 'safari'
    assert ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert ie.IE_DESC == 'safaribooksonline.com online courses'

# Generated at 2022-06-14 16:57:24.662399
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari = SafariBaseIE('safari')
    assert safari.LOGGED_IN == False

# Generated at 2022-06-14 16:57:26.213397
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()
    ie._login()

# Generated at 2022-06-14 16:57:51.543692
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE('safari', 'safari')

# Generated at 2022-06-14 16:57:57.970761
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # check that course detected
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    assert SafariCourseIE._VALID_URL.match(url) is not None
    # check that course not detected
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    assert SafariCourseIE._VALID_URL.match(url) is None

# Generated at 2022-06-14 16:58:02.665285
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from .test_html import test_SafariBaseIE
    # Override static field LOGGED_IN to skip login at first time
    SafariBaseIE.LOGGED_IN = True
    # Call test suite of class SafariBaseIE
    test_SafariBaseIE(__name__, SafariCourseIE)

# Generated at 2022-06-14 16:58:06.766224
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = 'https://www.safaribooksonline.com/library/view/python-for-beginners/9781484212493/'
    ie = SafariIE()
    instance = ie.ie_key()
    assert instance == SafariIE.ie_key()
    assert ie.suitable(url)
    assert ie.LOGGED_IN == False

# Generated at 2022-06-14 16:58:07.577459
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base = SafariBaseIE()
    assert safari_base

# Generated at 2022-06-14 16:58:19.627427
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    import unittest
    class TestSafariCourseIE(unittest.TestCase):
        def test_constructor(self):
            safari_course_ie = SafariCourseIE()
            self.assertEqual('safari:course', safari_course_ie.IE_NAME)
            self.assertEqual('safaribooksonline.com online courses', safari_course_ie.IE_DESC)
            self.assertEqual('https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/([^/]+)/chapter(?:-content)?/([^/?#&]+).html', safari_course_ie._VALID_URL)
    test_cases = [
        TestSafariCourseIE
    ]
    suite

# Generated at 2022-06-14 16:58:21.009164
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:58:23.619434
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    s = SafariCourseIE()
    assert s.module_name == 'SafariBaseIE'
    assert s.module_name == 'SafariBaseIE'

# Generated at 2022-06-14 16:58:33.124354
# Unit test for constructor of class SafariIE
def test_SafariIE():
    course_id = '/home/techninja/Desktop/sample_course.json'
    part = '/home/techninja/Desktop/sample_part.json'
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    test_SafariIE = SafariIE(course_id,part,url)
    assert isinstance(test_SafariIE,SafariIE)


# Generated at 2022-06-14 16:58:35.704330
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()

# Generated at 2022-06-14 16:59:23.590175
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    mytest = SafariCourseIE()

# Generated at 2022-06-14 16:59:29.214621
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    import sys
    if sys.version_info >= (2, 7, 9):
        import ssl
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    else:
        ssl_context = None

    safari_base_ie = SafariBaseIE({'ssl_verify': True})
    safari_base_ie._downloader = ssl_context
    safari_base_ie._real_initialize()

# Generated at 2022-06-14 16:59:31.185575
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert isinstance(SafariIE()._build_login_form(None, None), str)

# Generated at 2022-06-14 16:59:31.973111
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE()

# Generated at 2022-06-14 16:59:33.350848
# Unit test for constructor of class SafariIE
def test_SafariIE():
    try:
        a = SafariIE()
    except Exception as e:
        print(e)

# Generated at 2022-06-14 16:59:36.288270
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE()
    safari_base_ie._real_initialize()

# Generated at 2022-06-14 16:59:38.772465
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    file = '.safaribooksonline.netrc'
    unit_test = SafariBaseIE(file)
    assert unit_test._NETRC_MACHINE == 'safari'

# Generated at 2022-06-14 16:59:47.360781
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    def check_assertions(self):
        assert self._downloader.params['username'] == 'testuser'
        assert self._downloader.params['password'] == 'testpassword'

    ie = SafariCourseIE(
        downloader=type('DummyDownloader', (object,), {
            'params': {},
        })(),
        url='https://techbus.safaribooksonline.com/9780134426365',
    )

    ie._downloader.params['username'] = ie._downloader.params['password'] = 'testuser'
    ie._downloader.add_password = check_assertions
    ie._get_login_info()

# Generated at 2022-06-14 16:59:57.176959
# Unit test for constructor of class SafariIE
def test_SafariIE():
    input_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    input_course_id = '9780133392838'
    input_part = 'part00.html'
    expected_kaltura_url = 'https://cdnapisec.kaltura.com/html5/html5lib/v2.37.1/mwEmbedFrame.php?wid=_1926081&uiconf_id=29375172&flashvars[referenceId]=9780133392838-part00.html'
    expected_video_id = '9780133392838-part00.html'

    m = re.match(SafariIE._VALID_URL, input_url)

# Generated at 2022-06-14 17:00:05.072630
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """Test if SafariCourseIE correctly throws an exception if no chapters are found"""
    if not hasattr(InfoExtractor, '_download_json'):
        return

    def download_json(url):
        """Mock of _download_json. Always throw an exception"""
        raise Exception()

    # Override with mock
    InfoExtractor._download_json = download_json

    course_id = '9781449396459'
    url = 'http://www.safaribooksonline.com/api/v1/book/' + course_id + '/?override_format=json'

    safari_course_ie = SafariCourseIE(InfoExtractor())

    raised_exception = False
    try:
        safari_course_ie.extract(url)
    except ExtractorError:
        raised_exception = True

# Generated at 2022-06-14 17:02:07.028554
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    test = SafariCourseIE()

# Generated at 2022-06-14 17:02:10.194499
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()


# Generated at 2022-06-14 17:02:20.037862
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .common import InfoExtractor
    from .common import unescapeHTML
    from .common import download_json
    from .common import ExtractorError
    from .kaltura import KalturaIE
    instance = InfoExtractor()
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    result = unescapeHTML(download_json(url, None))
    assert result['id'] == '0_qbqx90ic'
    assert result['ext'] == 'mp4'
    assert result['title'] == 'Introduction to Hadoop Fundamentals LiveLessons'
    assert result['timestamp'] == 1437758058
    assert result['upload_date'] == '20150724'
   

# Generated at 2022-06-14 17:02:26.234394
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    s = SafariIE(url)
    assert s.url == 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'



# Generated at 2022-06-14 17:02:29.492495
# Unit test for constructor of class SafariIE
def test_SafariIE():
    test_obj = SafariIE()
    assert test_obj.SUFFIX == 'com'
    assert test_obj.ie_key() == 'Safari'


# Generated at 2022-06-14 17:02:31.495222
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_apiIE = SafariApiIE()
    assert safari_apiIE.name == 'safari:api'


# Generated at 2022-06-14 17:02:41.754212
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # valid URL
    assert SafariIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    # invalid URLs:
    assert not SafariIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    assert not SafariIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838')

# Generated at 2022-06-14 17:02:45.115447
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    try:
        import webbrowser
        test_instance = SafariApiIE()
        test_instance._login()
    except:
        raise

# Generated at 2022-06-14 17:02:51.542809
# Unit test for constructor of class SafariIE
def test_SafariIE():
    try:
        from requests.exceptions import ConnectionError
        from httpie.compat import is_local_ip
        if is_local_ip():
            raise ConnectionError()
    except ImportError:
        pass
    except ConnectionError:
        import pytest
        pytest.skip('Test needs a connection to the internet', allow_module_level=True)
    SafariIE()

# Generated at 2022-06-14 17:02:52.660776
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE(SafariBaseIE(), 'safaribooksonline.com:api')
    assert True