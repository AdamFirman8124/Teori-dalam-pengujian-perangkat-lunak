

# Generated at 2022-06-14 16:55:49.652775
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/hello_world_1.html?override_format=json'
    ie = SafariApiIE()
    ie._real_initialize()
    assert ie.suitable(url)
    ie.extract(url)

# Generated at 2022-06-14 16:56:00.499251
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    username = 'unittest@example.com'
    password = 'qwerty'
    desired_urlh = None
    url = 'http://www.youtube.com/watch?v=123'
    SafariBaseIE._download_webpage = lambda self, url, video_id, note, errnote: (None, desired_urlh)
    SafariBaseIE._download_json = lambda self, url, video_id, note, errnote: None
    SafariBaseIE._apply_first_set_cookie_header = lambda self, urlh, cookie_key: None
    SafariBaseIE._get_login_info = lambda self: (username, password)
    safari = SafariBaseIE()
    safari._LOGIN_URL = 'http://www.oreilly.com/'
    safari._NETRC_MACHINE = None
    saf

# Generated at 2022-06-14 16:56:02.687789
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # test SafariIE.LOGGED_IN
    assert not SafariIE.LOGGED_IN

# Generated at 2022-06-14 16:56:14.510964
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838'
    safari_course_ie = SafariCourseIE()
    match = safari_course_ie._VALID_URL_RE.match(url)
    id = match.group('id')
    course_json = safari_course_ie._download_json(
                    '%s/book/%s/?override_format=%s' % (safari_course_ie._API_BASE, id, safari_course_ie._API_FORMAT),
                    id, 'Downloading course JSON')
    course_title = course_json['title']
    assert course_title == 'Hadoop Fundamentals LiveLessons'

# Generated at 2022-06-14 16:56:21.696868
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    se = SafariApiIE()
    se.initialize()
    se.login()
    html_file = open('test_webpage_local')
    url = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838/9780133392838-00_SeriesIntro/'
    m = re.match(se._VALID_URL, url)
    se._real_extract(url)

# Generated at 2022-06-14 16:56:30.028193
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from .test_common import _get_testdata_video_url
    from .test_common import _test_internet
    from .test_common import _test_verify_ssl_certificates
    from .test_common import _test_unsafe_file
    from .test_common import _test_no_ssl
    from .test_common import _test_write
    from .test_common import _test_update_options
    from .test_common import _test_set_proxy
    from .test_common import _test_set_write_option
    from .test_common import _test_edit_mode
    from .test_common import _test_interact
    from .test_common import _test_small_download
    from .test_common import _test_continue
    from .test_common import _test_quiet
   

# Generated at 2022-06-14 16:56:35.277654
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """
    Constructor test. Assert that the expected methods are called.
    """

    class MockKalturaIE(object):
        def __init__(self, *args, **kwargs):
            return super(MockKalturaIE, self).__init__(*args, **kwargs)

        @staticmethod
        def suitable(url):
            return True

        @staticmethod
        def _real_extract(url):
            return {'id': url}

    class MockSafariApiIE(object):
        def __init__(self, *args, **kwargs):
            return super(MockSafariApiIE, self).__init__(*args, **kwargs)

        @staticmethod
        def suitable(url):
            return True


# Generated at 2022-06-14 16:56:45.828705
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/01.html'
    safari_api_ie_object = SafariApiIE()
    assert safari_api_ie_object._VALID_URL == 'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'

# Generated at 2022-06-14 16:56:57.330625
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # testing SafariIE class constructor
    test_obj = SafariIE()

    # testing existence of _VALID_URL
    assert hasattr(test_obj, '_VALID_URL') is True

    # testing existence of IE_NAME
    assert hasattr(test_obj, 'IE_NAME') is True

    # testing existence of IE_DESC
    assert hasattr(test_obj, 'IE_DESC') is True

    # testing existence of _TESTS
    assert hasattr(test_obj, '_TESTS') is True

    # testing existence of _PARTNER_ID
    assert hasattr(test_obj, '_PARTNER_ID') is True

    # testing existence of _UICONF_ID
    assert hasattr(test_obj, '_UICONF_ID') is True

    # testing instance of class

# Generated at 2022-06-14 16:57:02.522192
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE(None, None)
    assert safari_base_ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert safari_base_ie._NETRC_MACHINE == 'safari'
    assert safari_base_ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari_base_ie._API_FORMAT == 'json'
    assert not safari_base_ie.LOGGED_IN

# Generated at 2022-06-14 16:57:25.472633
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Test valid url
    url = 'http://techbus.safaribooksonline.com/9780134664057'
    assert SafariCourseIE(url) is not None
    url = 'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314'
    assert SafariIE(url) is not None
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    assert SafariIE(url) is not None
    # Test invalid url
    url = 'http://techbus.safaribooksonline.com/9780134664057/part00.html'
    assert SafariIE(url) is None

# Generated at 2022-06-14 16:57:26.821740
# Unit test for constructor of class SafariIE
def test_SafariIE():
    i = SafariIE()
    i._login()

# Generated at 2022-06-14 16:57:27.989043
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    obj = SafariCourseIE();

# Generated at 2022-06-14 16:57:38.978799
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Verifying username, password, partner_id and ui_conf_id
    # given non-empty arguments of SafariApiIE constructor
    partner_id = '1234'
    ui_conf_id = '4321'
    safari_api = SafariApiIE('username', 'password', partner_id, ui_conf_id)
    assert safari_api._PARTNER_ID == partner_id
    assert safari_api._UICONF_ID == ui_conf_id

    # Verifying object attributes given empty arguments
    # of SafariApiIE constructor
    safari_api = SafariApiIE()
    assert safari_api._PARTNER_ID == '1926081'
    assert safari_api._UICONF_ID == '29375172'

# Generated at 2022-06-14 16:57:45.861299
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from unittest import TestCase

    class TestSafariCourseIE(TestCase):
        def test_constructor(self):
            course_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
            ie = SafariCourseIE(course_url)
            self.assertEqual(ie.IE_NAME, 'safari:course')
            self.assertEqual(ie.IE_DESC, 'safaribooksonline.com online courses')

    # run unit test
    test = TestSafariCourseIE()
    test.test_constructor()

# Generated at 2022-06-14 16:57:49.640534
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # test that SafariBaseIE's constructor fails without being implemented
    # it's awkward, but seems to be the only way.
    ie = SafariBaseIE()
    try:
        ie._login()
    except TypeError:
        pass
    except Exception:
        raise Exception('SafariBaseIE._login() did not raise TypeError')
    else:
        raise Exception('SafariBaseIE._login() did not raise an exception')

# Generated at 2022-06-14 16:57:58.792375
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    class_ = SafariCourseIE
    assert class_.suitable('https://www.safaribooksonline.com/library/view/css-secrets/9781449372668/')
    assert class_.suitable('https://www.safaribooksonline.com/api/v1/book/9781449396459/')
    assert class_.suitable('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314')
    assert not class_.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')

# Generated at 2022-06-14 16:58:02.615789
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert (classmethod(SafariCourseIE.suitable).__get__(SafariCourseIE, SafariCourseIE)
            is not classmethod(SafariCourseIE.suitable).__get__(SafariCourseIE, SafariIE))

# Generated at 2022-06-14 16:58:09.463953
# Unit test for constructor of class SafariIE
def test_SafariIE():
    try:
        # Test SafariIE with a course ID
        sample_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
        SafariIE()._real_extract(sample_url)
    except ExtractorError:
        pass

    try:
        # Test SafariIE with a reference ID
        sample_url = 'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_00'
        SafariIE()._real_extract(sample_url)
    except ExtractorError:
        pass

# Generated at 2022-06-14 16:58:14.064493
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    #if hasattr(SafariBaseIE, 'LOGGED_IN'): delattr(SafariBaseIE, 'LOGGED_IN')
    base_instance = SafariBaseIE()
    assert(not base_instance.LOGGED_IN)

    #if hasattr(SafariApiIE, 'LOGGED_IN'): delattr(SafariApiIE, 'LOGGED_IN')
    api_instance = SafariApiIE()
    assert(api_instance.LOGGED_IN)


# Generated at 2022-06-14 16:58:47.301452
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class TestSafariBaseIE(SafariBaseIE):
        IE_NAME = 'safari'
        _VALID_URL = r'https://www\.safaribooksonline\.com/library/view/hadoop-fundamentals-livelessons/(?:[^/]+/)+part05\.html'

        _API_BASE = 'https://www.safaribooksonline.com/api/v1'

    TestSafariBaseIE()._real_initialize()

# Generated at 2022-06-14 16:58:58.651816
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    import requests
    from . import safari
    from .extractor import unescapeHTML

    # Test when the URL is invalid
    invalid_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    course = safari.SafariCourseIE(None)
    assert course.suitable(invalid_url) == False

    # Test constructor of class SafariCourseIE
    course = safari.SafariCourseIE(None)
    assert course.suitable(invalid_url) == False

    # Another course_id
    course_id = '9780134664057'
    course = safari.SafariCourseIE(None)
    course.course_id = course_id

# Generated at 2022-06-14 16:59:08.807287
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    course = SafariCourseIE("https://techbus.safaribooksonline.com/9780134426365")

    assert course._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert course._API_FORMAT == 'json'
    assert course._NETRC_MACHINE == 'safari'
    assert course._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+|api/v1/book|videos/[^/]+)/(?P<id>[^/]+)'

# Generated at 2022-06-14 16:59:14.919372
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    ie = SafariApiIE()
    assert ie.suitable(url)
    assert ie.IE_NAME == 'safari:api'
    assert ie.IE_DESC == 'safaribooksonline.com online video'

# Generated at 2022-06-14 16:59:27.949719
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    """Unit test for SafariApiIE"""

    url_for_test = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    safari_api_test = SafariApiIE()
    safari_course_test = SafariCourseIE()

    if not isinstance(safari_api_test, SafariApiIE):
        raise AssertionError('SafariApiIE constructor is not an instance of SafariApiIE')

    if not isinstance(safari_course_test, SafariCourseIE):
        raise AssertionError('SafariCourseIE constructor is not an instance of SafariCourseIE')


# Generated at 2022-06-14 16:59:30.951237
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE('SafariBaseIE', 'safaribooksonline.com')
    SafariBaseIE('SafariBaseIE', 'learning.oreilly.com')
    SafariBaseIE('SafariBaseIE', 'oreilly.com')

# Generated at 2022-06-14 16:59:32.090454
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('safari:api')

# Generated at 2022-06-14 16:59:33.176289
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE("test", "test", "test", "test")

# Generated at 2022-06-14 16:59:34.395889
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE("SafariIE", "safari")

# Generated at 2022-06-14 16:59:37.600692
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://learning.oreilly.com/library/view/c++-cookbook/9780596007973/'
    SafariApiIE()._get_login_info()

# Generated at 2022-06-14 17:00:34.575099
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    s = SafariApiIE()
    assert s.ie_key() == 'Safari:Api'
    assert s.ie_name == 'safari:api'
    assert s.ie_desc == 'safaribooksonline.com online video'


# Generated at 2022-06-14 17:00:40.225642
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert SafariIE()._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert SafariIE()._NETRC_MACHINE == 'safari'
    assert SafariIE()._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert SafariIE()._API_FORMAT == 'json'
    assert SafariIE().LOGGED_IN == False

# Generated at 2022-06-14 17:00:46.312817
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    parsed = compat_urlparse.urlparse(
        SafaribooksonlineIE._LOGIN_URL)
    assert SafaribooksonlineIE._NETRC_MACHINE == parsed.netloc

# Generated at 2022-06-14 17:00:55.232618
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    """Test constructor of class SafariApiIE"""
    # Fails if "class SafariApiIE(SafariBaseIE):" is removed (valid URL)
    url = 'https://www.safaribooksonline.com/api/v1/book/exploring-celery/chapter-content/01_intro-and-setup.html'
    SafariApiIE._real_extract(SafariApiIE(), url)
    # Fails if "class SafariApiIE(SafariBaseIE):" is removed (invalid URL)
    url = 'https://www.safaribooksonline.com/api/v1/book/exploring-celery/_chapter-content/01_intro-and-setup.html'

# Generated at 2022-06-14 17:00:56.406352
# Unit test for constructor of class SafariIE
def test_SafariIE():
    inst = SafariIE()
    return True

# Generated at 2022-06-14 17:01:03.111349
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    constructor_test(SafariApiIE, ['https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'])
    constructor_test(SafariApiIE, ['https://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_00'])
    constructor_test(SafariApiIE, ['https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838/9780133392838-00_SeriesIntro'])

# Generated at 2022-06-14 17:01:06.846380
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    username = 'safaritest'
    password = 'safaritest'

    ie = SafariBaseIE(username, password)

    assert ie.LOGGED_IN == False


# Generated at 2022-06-14 17:01:07.422491
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    pass

# Generated at 2022-06-14 17:01:10.730518
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    try:
        SafariBaseIE(None)._login()
    except ExtractorError as ee:
        assert ee.cause.__class__.__name__ == 'NoCredentialsError'

# Generated at 2022-06-14 17:01:11.932248
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('safaribooksonline', 'SafariOnline')

# Generated at 2022-06-14 17:03:45.619046
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari_ie = SafariIE()
    assert safari_ie.IE_NAME == 'safari'
    assert safari_ie.IE_DESC == 'safaribooksonline.com online video'
    assert safari_ie._VALID_URL == r'''(?x)
                                      https?://
                                      (?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/
                                        (?:
                                            library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?\#&]+)\.html|
                                            videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?\#&]+)
                                        )'''


# Generated at 2022-06-14 17:03:46.184847
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE({})

# Generated at 2022-06-14 17:03:50.962185
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    e = SafariBaseIE()
    assert(not e._LOGIN_URL)
    assert(not e._NETRC_MACHINE)
    assert(not e._API_BASE)
    assert(not e.LOGGED_IN)
    assert(not e._login())
    assert(not e._real_initialize())
    assert(not e._real_extract('http://example.com/'))

# Generated at 2022-06-14 17:03:51.641652
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    raise NotImplementedError()

# Generated at 2022-06-14 17:04:00.932905
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """Unit test for SafariCourseIE"""
    #The constructor of InfoExtractor is hard to test
    #You have to pass an url which gets processed by the extractor
    #That's why we create a dummy url which will not be processed by the extractor
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    course_infoExtractor = SafariCourseIE(url)
    assert(isinstance(course_infoExtractor, SafariCourseIE))
    assert(course_infoExtractor.IE_NAME == 'safari:course')

# Generated at 2022-06-14 17:04:01.774330
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()



# Generated at 2022-06-14 17:04:03.674376
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    return SafariApiIE('Safari')

# Unit tests for constructor of class SafariApiIE

# Generated at 2022-06-14 17:04:04.367088
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 17:04:07.603754
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    i = SafariBaseIE()
    assert i.IE_NAME

# Generated at 2022-06-14 17:04:11.479704
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """Test constructor of class SafariCourseIE."""
    from extractors.tests.test_safari import SafariCourseIE_Test
    object_SafariCourseIE = SafariCourseIE_Test()
    object_SafariCourseIE.assertTrue(SafariCourseIE)