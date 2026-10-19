

# Generated at 2022-06-14 16:55:50.916595
# Unit test for constructor of class SafariIE
def test_SafariIE():
    code = """
    class TestSafariIE(SafariIE):
        def __init__(self):
            self._LOGIN_URL = 'https://example.com/login/'
            SafariIE.__init__(self, True)
    """

    ns = {}
    exec(code, globals(), ns)
    TestSafariIE = ns['TestSafariIE']
    TestSafariIE()

# Generated at 2022-06-14 16:55:52.743930
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE('site-user', 'password')
    assert ie.login == ('site-user', 'password')

# Generated at 2022-06-14 16:56:00.534895
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """Verify that SafariIE constructor doesn't crash for test URLs."""

# Generated at 2022-06-14 16:56:07.571043
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    obj = SafariBaseIE()
    assert obj._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert obj._NETRC_MACHINE == 'safari'
    assert obj._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert obj._API_FORMAT == 'json'

# Generated at 2022-06-14 16:56:09.156411
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE(SafariIE({}), 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')

# Generated at 2022-06-14 16:56:09.830293
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # just test that it's constructing without exception
    SafariBaseIE()

# Generated at 2022-06-14 16:56:13.050671
# Unit test for constructor of class SafariIE
def test_SafariIE():
    obj = SafariIE('username', 'password')
    assert obj._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert obj._NETRC_MACHINE == 'safari'

# Generated at 2022-06-14 16:56:14.016570
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Test for constructor of class SafariIE
    assert SafariIE

# Generated at 2022-06-14 16:56:20.516935
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """
    Basic unit test for SafariBaseIE class to ensure its members are
    initialised properly
    """
    safari = SafariBaseIE()
    assert safari.login_page is None
    assert safari._login is None
    assert safari._real_initialize is None
    assert safari._real_initialize() is None
    assert safari.LOGGED_IN is False

# Generated at 2022-06-14 16:56:29.209438
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    test_urls = [
        "https://www.safaribooksonline.com/api/v1/book/9781782167521/chapter/part01.html",
        "https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html",
        "https://www.safaribooksonline.com/api/v1/book/9780134664057/chapter/RHCE_Introduction.html"
    ]
    ie = SafariApiIE()
    for url in test_urls:
        if not ie.suitable(url):
            raise AssertionError("failed test_suitable, url=%s" % url)

        ie._real_initialize()
        ie._real_extract(url)

# Generated at 2022-06-14 16:56:43.432749
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE().suitable('')

# Generated at 2022-06-14 16:56:47.945498
# Unit test for constructor of class SafariIE
def test_SafariIE():
    course_id = '9780133392838'
    part_id = 'part00'
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    obj = SafariIE()
    result = obj._real_extract(url)
    assert result['id'] == '0_qbqx90ic', 'Unexpected course id'
    assert result['title'] == 'Introduction to Hadoop Fundamentals LiveLessons', 'Unexpected course title'
    assert result['upload_date'] == '20150724', 'Unexpected upload date'
    assert result['timestamp'] == 1437758058, 'Unexpected timestamp'

# Generated at 2022-06-14 16:56:49.736649
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    i = SafariCourseIE()
    assert i.LOGGED_IN == False

# Generated at 2022-06-14 16:56:53.064863
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safariBase = SafariBaseIE()
    assert safariBase._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safariBase._API_FORMAT == 'json'

# Generated at 2022-06-14 16:56:57.517280
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    with open('test/data/test_SafariApiIE.json') as test_json_file:
        test_json = json.load(test_json_file)
    test_SafariApiIE = SafariApiIE()
    test_SafariApiIE._real_extract(test_json['url'])

# Generated at 2022-06-14 16:57:02.428225
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE()
    assert safari_api_ie.IE_NAME == 'safari:api'
    assert safari_api_ie._VALID_URL == 'https?://(?:www\\.)?(?:safaribooksonline|(?:learning\\.)?oreilly)\\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\\.html'

# Generated at 2022-06-14 16:57:03.302741
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert SafariBaseIE

# Generated at 2022-06-14 16:57:04.827623
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    sb_ie = SafariBaseIE(None)
    assert sb_ie._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:57:07.015357
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE(SafariBaseIE, 'SafariApiIE')

# Generated at 2022-06-14 16:57:10.546563
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    test_url = 'http://techbus.safaribooksonline.com/9780134426365'
    safari_base_ie = SafariBaseIE()
    assert(safari_base_ie.suitable(test_url))

# Generated at 2022-06-14 16:57:37.830080
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safari = SafariCourseIE(None)
    assert safari._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:57:39.112036
# Unit test for constructor of class SafariIE
def test_SafariIE():
    instance = SafariIE()
    assert isinstance(instance, SafariIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:57:41.227196
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    instance = SafariCourseIE('/home/user/path/to/file.mp4')
    assert isinstance(instance, SafariCourseIE)

# Generated at 2022-06-14 16:57:42.528669
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Skip test for SafariCourseIE since it requires safaribooksonline account credentials
    pass

# Generated at 2022-06-14 16:57:43.644419
# Unit test for constructor of class SafariIE
def test_SafariIE():
    instance = SafariBaseIE()
    assert isinstance(instance, SafariBaseIE)

# Generated at 2022-06-14 16:57:46.008818
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE()
    ie.set_downloader(None)
    ie.set_downloader(None)
    assert ie.extractor_key() == 'SafariCourseIE'

# Generated at 2022-06-14 16:57:48.400962
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safari_course_ie_test1 = SafariCourseIE(None)
    safari_course_ie_test2 = SafariCourseIE(None)

    assert(safari_course_ie_test1 == safari_course_ie_test2)

# Generated at 2022-06-14 16:57:50.847327
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    ie = SafariApiIE(url)
    assert ie._VALID_URL == url

# Generated at 2022-06-14 16:57:51.603264
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE()

# Generated at 2022-06-14 16:57:52.564642
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    IE = SafariBaseIE()

# Generated at 2022-06-14 16:58:44.133177
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE()

# Generated at 2022-06-14 16:58:48.677659
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    safari_course = SafariCourseIE(url)
    assert safari_course.suitable(url) is True

# Generated at 2022-06-14 16:59:00.234376
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    import requests
    url = 'https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    safari = SafariCourseIE()
    username = None
    password = None
    if (username is None) and (password is None):
        from ..compat import compat_urllib_request
        try:  # python 3
            import _netrc as netrc
        except ImportError:  # python 2
            import netrc

# Generated at 2022-06-14 16:59:07.654228
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """Tests whether SafariBaseIE.__init__ works as expected."""
    import os

    import mockserver

    # pylint: disable=protected-access
    with mockserver.patch('http://mock/accounts/login/') as login_page:
        with mockserver.patch('https://api.oreilly.com/auth/login/') as login_check:
            with mockserver.patch('https://learning.oreilly.com/home/') as home:
                login_page.status = 200
                login_check.status = 200
                home.status = 200

                # successful login
                SafariBaseIE._login()


# Generated at 2022-06-14 16:59:09.864003
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert len(SafariBaseIE._TEST) == 1

# Generated at 2022-06-14 16:59:11.541493
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    """Test class SafariApiIE"""
    ie = SafariApiIE()

# Generated at 2022-06-14 16:59:12.127214
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE()

# Generated at 2022-06-14 16:59:17.463597
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/PYMC_00_00.html'
    # Instance created in SafariApiIE.__new__
    instance = SafariApiIE._new_instance(url)
    assert isinstance(instance, SafariApiIE)

# Generated at 2022-06-14 16:59:19.510184
# Unit test for constructor of class SafariIE
def test_SafariIE():
    test_instance = SafariIE()
    assert test_instance.IE_NAME == 'safari'
    assert test_instance.IE_DESC == 'safaribooksonline.com online video'


# Generated at 2022-06-14 16:59:29.723252
# Unit test for constructor of class SafariIE
def test_SafariIE():
    test = SafariIE(params={})
    assert test._TESTS[0]['md5'] == 'dcc5a425e79f2564148652616af1f2a3'
    assert test._TESTS[0]['url'] == 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    assert test._TESTS[0]['info_dict']['id'] == '0_qbqx90ic'
    assert test._TESTS[0]['info_dict']['title'] == 'Introduction to Hadoop Fundamentals LiveLessons'
    assert test._TESTS[0]['info_dict']['timestamp'] == 1437758058

# Generated at 2022-06-14 17:01:36.172195
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 17:01:43.451069
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    instance = SafariCourseIE('SafariCourseIE', 'safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    assert (instance.IE_NAME == 'SafariCourseIE')
    assert (instance.IE_DESC == 'safaribooksonline.com online courses')
    assert (instance._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+|api/v1/book|videos/[^/]+)/(?P<id>[^/]+)')

# Generated at 2022-06-14 17:01:52.314444
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import sys
    import youtube_dl.extractor.common
    import youtube_dl.extractor.kaltura

    sys.modules['youtube_dl.extractor.common'] = youtube_dl.extractor.common
    sys.modules['youtube_dl.extractor.kaltura'] = youtube_dl.extractor.kaltura

    assert(SafariApiIE.__doc__)
    assert(SafariApiIE._VALID_URL)

    ext = SafariApiIE()
    assert(isinstance(ext._LOGIN_URL, str))
    assert(isinstance(ext._NETRC_MACHINE, str))

    assert(isinstance(ext._API_BASE, str))
    assert(isinstance(ext._API_FORMAT, str))


# Generated at 2022-06-14 17:01:58.989562
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import unittest
    import sys

    class TestSafariApiIE(unittest.TestCase):
        def test_constructor_class(self):
            safariApiIE = SafariApiIE()
            self.assertIsNotNone(safariApiIE)

    testSuite = unittest.TestSuite()
    testSuite.addTest(unittest.makeSuite(TestSafariApiIE))
    result = unittest.TextTestRunner().run(testSuite)
    if result.errors or result.failures:
        sys.exit(1)

# Generated at 2022-06-14 17:02:01.682974
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    saf_IE = SafariApiIE()



# Generated at 2022-06-14 17:02:05.642710
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():

    safari_base_ie = SafariBaseIE()
    assert safari_base_ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert safari_base_ie._NETRC_MACHINE == 'safari'

# Generated at 2022-06-14 17:02:06.503655
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()


# Generated at 2022-06-14 17:02:14.981081
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE('http://techbus.safaribooksonline.com/9780134426365', '', '')
    assert(safari.url == 'http://techbus.safaribooksonline.com/9780134426365')
    try:
        safari._login()
    except:
        pass
    assert(safari.url == 'http://techbus.safaribooksonline.com/9780134426365')

# Generated at 2022-06-14 17:02:16.071231
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE(SafariIE.ie_key())

# Generated at 2022-06-14 17:02:17.379626
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    course_IE = SafariCourseIE(None)
    return course_IE