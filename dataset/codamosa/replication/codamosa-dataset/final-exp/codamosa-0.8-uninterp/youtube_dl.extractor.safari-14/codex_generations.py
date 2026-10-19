

# Generated at 2022-06-14 16:55:44.817608
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE(InfoExtractor())

# Generated at 2022-06-14 16:55:56.055508
# Unit test for constructor of class SafariCourseIE

# Generated at 2022-06-14 16:55:58.504758
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Unit test for constructor of class SafariCourseIE
    # Checks if class SafariCourseIE is instantiable
    SafariCourseIE()
    assert True

# Generated at 2022-06-14 16:56:00.747211
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Test _login function
    mocker = SafariBaseIE._login()
    assert(mocker == None)

# Generated at 2022-06-14 16:56:03.658931
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    i = SafariApiIE()
    i._initialize(test_suitable = False)
    assert i.LOGGED_IN

# Generated at 2022-06-14 16:56:15.442056
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE.suitable('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')
    assert SafariCourseIE.suitable('http://techbus.safaribooksonline.com/9780134426365')
    assert SafariCourseIE.suitable('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314')
    assert SafariCourseIE.suitable('https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838')
    assert SafariCourseIE.suitable('https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    assert not SafariCourse

# Generated at 2022-06-14 16:56:19.047859
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from .common import FakeIE

    assert (SafariApiIE({
        'web_url': 'foo',
    }) ==
        FakeIE({
            'url': 'foo',
        })
    )

# Generated at 2022-06-14 16:56:20.131262
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    constructor_test(SafariBaseIE, [])

# Generated at 2022-06-14 16:56:28.919694
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    import os
    import requests
    import tempfile
    import unittest
    from io import open

    class SafariBaseTest(unittest.TestCase):
        def setUp(self):
            self.username = os.environ.get('SAFARI_LOGIN')
            self.password = os.environ.get('SAFARI_PASSWORD')

        def test_authentication(self):
            if not self.username or not self.password:
                self.skipTest('Provide account credentials to use this test')
            ie = SafariBaseIE()
            ie._login()
            self.assertTrue(ie.LOGGED_IN)
            self.assertTrue(requests.cookies.get('orm-jwt'))
            self.assertTrue(requests.cookies.get('orm-rt'))
            self

# Generated at 2022-06-14 16:56:29.656675
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    obj = SafariBaseIE()


# Generated at 2022-06-14 16:56:46.382847
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari_ie = SafariIE('test', 'test')
    assert safari_ie.LOGGED_IN == False
    assert safari_ie._PARTNER_ID == '1926081'
    assert safari_ie._UICONF_ID == '29375172'
    assert safari_ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari_ie._API_FORMAT == 'json'

# Generated at 2022-06-14 16:56:57.460829
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    t0 = SafariBaseIE(
        'http://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_00', {})
    assert isinstance(t0, SafariBaseIE)
    t1 = SafariBaseIE(
        'http://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838/9780133392838-00_SeriesIntro', {})
    assert isinstance(t1, SafariBaseIE)
    t2 = SafariBaseIE(
        'http://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json', {})
    assert isinstance(t2, SafariBaseIE)


# Generated at 2022-06-14 16:57:02.877633
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # It's a private function but we need to use it
    import sys
    import os
    import unittest
    from safari import SafariApiIE

    # Class to hold unit tests
    class TestPath(unittest.TestCase):

        def test_real_extract(self):

            safari_api = SafariApiIE()
            result = safari_api._real_initialize()

            self.assertTrue(result)

    # Run unit tests
    sys.argv = [sys.argv[0]]
    sys.exit(unittest.main())

# Generated at 2022-06-14 16:57:11.000715
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """Test constructor of class SafariCourseIE."""
    safari = SafariCourseIE()
    assert safari._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert safari._NETRC_MACHINE == 'safari'
    assert safari._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari._API_FORMAT == 'json'
    assert safari.LOGGED_IN is False
    return safari


# Generated at 2022-06-14 16:57:18.722524
# Unit test for constructor of class SafariIE
def test_SafariIE():

    test_url = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838'
    test_result_url = 'https://cdnapisec.kaltura.com/html5/html5lib/v2.37.1/mwEmbedFrame.php?wid=_1926081&uiconf_id=29375172&flashvars[referenceId]=9780133392838-00_SeriesIntro'

    # Test without login
    kaltura_url = SafariIE._build_url(test_url)
    assert kaltura_url == test_result_url

    # Test login
    class MockSafariBaseIE(SafariBaseIE):
        LOGGED_IN = True


# Generated at 2022-06-14 16:57:26.613245
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    result = SafariIE().extract(url)
    assert isinstance(result, dict)
    assert 'webpage_url' in result
    assert isinstance(result['webpage_url'], unicode)
    assert 'kaltura' in result['webpage_url']

# Generated at 2022-06-14 16:57:38.297172
# Unit test for constructor of class SafariIE

# Generated at 2022-06-14 16:57:46.735629
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    course_id = '9780132942370'
    url = 'https://www.safaribooksonline.com/api/v1/book/' + course_id + '/chapter/part00.html'

# Generated at 2022-06-14 16:57:47.195580
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 16:57:47.591252
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 16:58:16.306336
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    IE = SafariBaseIE()
    if not IE.LOGGED_IN:
        raise ValueError("Unit test for SafariBaseIE failed to log in user!")

# Generated at 2022-06-14 16:58:19.133396
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """Unit test for SafariCourseIE"""
    extractor = SafariCourseIE()
    assert isinstance(extractor, SafariBaseIE)

# Generated at 2022-06-14 16:58:22.479490
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import os
    import sys
    sys.path.append('./downloader/')
    from kaltura_downloader import kdl
    instance = kdl.Kdl()
    assert instance

# Generated at 2022-06-14 16:58:28.652914
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safari_course_ie = SafariCourseIE()

    assert safari_course_ie.IE_NAME == 'safari:course'
    assert safari_course_ie.IE_DESC == 'safaribooksonline.com online courses'
    assert safari_course_ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+|api/v1/book|videos/[^/]+)/(?P<id>[^/]+)'

# Generated at 2022-06-14 16:58:30.261451
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari = SafariBaseIE()
    assert safari.LOGGED_IN == False

# Generated at 2022-06-14 16:58:36.552594
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Testing the constructor
    ie = SafariApiIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'
    assert ie.IE_NAME == 'safari:api'

# Generated at 2022-06-14 16:58:37.174703
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 16:58:49.216907
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    url2 = 'https://techbus.safaribooksonline.com/9780134426365'
    url3 = 'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314'
    url4 = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838'
    url5 = 'https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'

# Generated at 2022-06-14 16:59:00.543149
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """Test for class SafariIE."""
    safariIE = SafariIE("https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838/9780133392838-00_SeriesIntro")
    assert safariIE.IE_NAME == 'safari'
    assert safariIE.IE_DESC == 'safaribooksonline.com online video'

# Generated at 2022-06-14 16:59:02.000634
# Unit test for constructor of class SafariIE
def test_SafariIE():
    try:
        SafariIE('a', 'b')
    except:
        assert False

# Generated at 2022-06-14 16:59:35.845086
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    mocker = Mocker()
    simple_dl = mocker.replace("youtube_dl.cached_http.SimpleDownloader")
    extractor = SafariApiIE(MockYDL())
    assert isinstance(extractor, InfoExtractor)
    assert extractor._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert extractor._API_FORMAT == 'json'
    assert extractor._NETRC_MACHINE == 'safari'
    assert extractor._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'


# Generated at 2022-06-14 16:59:46.421261
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safariIE = SafariIE()
    assert safariIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    assert safariIE.suitable('https://www.safaribooksonline.com/library/view/create-a-nodejs/100000006A0210/part00.html')
    assert safariIE.suitable('https://www.safaribooksonline.com/library/view/learning-path-red/9780134664057/RHCE_Introduction.html')

# Generated at 2022-06-14 16:59:56.109594
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Create a subclass with the same constructor as the base class
    class SafariSubclass(SafariApiIE):
        _VALID_URL = SafariApiIE._VALID_URL
        def _real_initialize(self):
            return SafariApiIE._real_initialize(self)
    # Create an instance of the base class and check the constructor
    ie_instance = SafariApiIE('http://techbus.safaribooksonline.com/9780134426365')
    expected_class_name = 'SafariApiIE'
    actual_class_name = ie_instance.__class__.__name__
    assert actual_class_name == expected_class_name, "Expected: %s. Actual: %s" % (expected_class_name, actual_class_name)
    # Create an instance of the

# Generated at 2022-06-14 17:00:04.599239
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    def test_uiconf_id(notebook_url, expected_value):
        course_id = SafariApiIE._VALID_URL_RE.match(notebook_url).group('course_id')
        course_json = SafariApiIE._download_json(
            SafariApiIE,
            '%s/book/%s/' % (SafariBaseIE._API_BASE, course_id),
            '',
            'Downloading course JSON')
        assert course_json.get('web_uiconf_id') == expected_value
    course_id = '9780134664057'

# Generated at 2022-06-14 17:00:07.899498
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    obj = SafariBaseIE()
    assert obj._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert obj._NETRC_MACHINE == 'safari'

# Generated at 2022-06-14 17:00:09.607184
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    c = SafariCourseIE()
    assert 0, "TODO: Test constructed SafariCourseIE object"

# Generated at 2022-06-14 17:00:13.224498
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Check that SafariApiIE(None) accepts None as an url
    SafariApiIE(None)

# Generated at 2022-06-14 17:00:20.164288
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    info_dict = {
        'id': '00',
        'ext': 'mp4',
        'timestamp': 1437758058,
        'upload_date': '20150724',
        'uploader': 'stork',
    }
    url = 'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html'
    ie = SafariApiIE()
    assert ie.suitable(url) == True
    assert ie.extract(url) == info_dict


# Generated at 2022-06-14 17:00:25.427380
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Test template for any inherited class
    # The test succeeds for SafariBaseIE, but fails for SafariIE.
    # This happens because SafariBaseIE._login() doesn't set self.LOGGED_IN
    # to True, as it is done by SafariIE._real_initialize().
    # Any inherited class should overwrite _real_initialize() method to
    # either invoke super method or set self.LOGGED_IN to True
    # (the latter is essential for inheritance of SafariBaseIE).
    SafariBaseIE._real_initialize()

# Generated at 2022-06-14 17:00:27.831822
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'

# Generated at 2022-06-14 17:01:16.712172
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+|api/v1/book|videos/[^/]+)/(?P<id>[^/]+)'
    assert ie._TESTS[0]['url'] == 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'

# Generated at 2022-06-14 17:01:18.310213
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE

# Generated at 2022-06-14 17:01:19.808527
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('Safari', 'safaribooksonline.com');

# Generated at 2022-06-14 17:01:21.324531
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    info_extractor = SafariBaseIE()
    assert info_extractor != None

# Generated at 2022-06-14 17:01:27.234346
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari = SafariApiIE()
    safari._download_json = lambda *args: args
    url = "https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html"

    ret = safari._real_extract(url)
    assert(ret == u'https://www.safaribooksonline.com/library/view/python-in-a/9781449396459/part00.html')

# Generated at 2022-06-14 17:01:27.870043
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()

# Generated at 2022-06-14 17:01:28.915715
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE('safari:course')

# Generated at 2022-06-14 17:01:30.834047
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert (
        type(SafariApiIE({})) is SafariApiIE)


# Generated at 2022-06-14 17:01:32.504833
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    import types
    inst = types.InstanceType
    SafariCourseIE(inst)

# Generated at 2022-06-14 17:01:41.670958
# Unit test for constructor of class SafariIE

# Generated at 2022-06-14 17:02:54.184398
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safarie = SafariBaseIE()
    assert safarie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert safarie._NETRC_MACHINE == 'safari'
    assert safarie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safarie._API_FORMAT == 'json'
    assert not safarie.LOGGED_IN

# Generated at 2022-06-14 17:03:02.452328
# Unit test for constructor of class SafariCourseIE

# Generated at 2022-06-14 17:03:03.611556
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE('SafariApiIE')

# Generated at 2022-06-14 17:03:04.900088
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    return SafariApiIE('SafariCourseIE')

# Generated at 2022-06-14 17:03:12.094229
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Create an instance of the SafariIE
    ie = SafariIE(None)

    # Check that the attributes of the instance are the same as the ones in the class
    assert ie._VALID_URL == r'''(?x)
                                    https?://
                                        (?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/
                                        (?:
                                            library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?\#&]+)\.html|
                                            videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?\#&]+)
                                        )
                                '''

# Generated at 2022-06-14 17:03:19.051689
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    class MockSafariCourseIE(SafariCourseIE):
        def _login(self):
            return

    course_id = '9780133392838' # course 'Hadoop Fundamentals LiveLessons' has 22 chapters
    course_title = 'Hadoop Fundamentals LiveLessons'
    course_url = 'https://www.safaribooksonline.com/library/view/{}/'.format(course_id)

    ied = MockSafariCourseIE(course_url)
    # test course _real_extract()
    entries = ied._real_extract(course_url)['entries']
    assert len(entries) == 22

# Generated at 2022-06-14 17:03:20.887226
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safariIE = SafariIE()
    assert safariIE._VALID_URL == SafariIE._VALID_URL

# Generated at 2022-06-14 17:03:22.917237
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE()
    assert safari_api_ie.IE_NAME == 'safari:api'

# Generated at 2022-06-14 17:03:28.773266
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    try:
        from youtube_dl.utils import ExtractorError
    except ImportError:
        ExtractorError = ValueError

    class MockSafariBaseIE(SafariBaseIE):
        def _real_initialize(self):
            pass

    safari = MockSafariBaseIE('safari', 'safari.com')
    safari.ie_key()
    safari.to_screen(None)
    safari.report_warning(None)

    try:
        safari.report_warning('test')
    except ExtractorError as exc:
        assert exc.args == ('test',)

    safari.to_screen('test')
    safari.raise_login_required('test')

# Generated at 2022-06-14 17:03:31.067879
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE._VALID_URL == SafariApiIE.VALID_URL
    assert SafariApiIE._TESTS == SafariApiIE.TESTS

# Generated at 2022-06-14 17:05:10.545950
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from .test_safari import test_SafariCourseIE
    test_SafariCourseIE(SafariCourseIE)

# Generated at 2022-06-14 17:05:13.510866
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    import os
    os.environ.pop("NETRC_MACHINE", None)
    assert SafariBaseIE()


if __name__ == '__main__':
    test_SafariBaseIE()

# Generated at 2022-06-14 17:05:20.076278
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    test_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    mobj = re.match(SafariApiIE._VALID_URL, test_url)
    assert mobj is not None and mobj.group('id') is not None

    test_url = 'https://techbus.safaribooksonline.com/9780134426365'
    mobj = re.match(SafariApiIE._VALID_URL, test_url)
    assert mobj is not None and mobj.group('id') is not None

# Generated at 2022-06-14 17:05:24.497587
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    iframe_url = 'https://cdnapisec.kaltura.com/p/1926081/sp/192608100/embedIframeJs/uiconf_id/29375172/partner_id/1926081?iframeembed=true&playerId=kaltura-player-9999999999-80390430747963899&entry_id=0_qbqx90ic&flashvars[referenceId]=0_qbqx90ic&flashvars[streamerType]=auto'
    safari = SafariIE()
    safari.extract(iframe_url)