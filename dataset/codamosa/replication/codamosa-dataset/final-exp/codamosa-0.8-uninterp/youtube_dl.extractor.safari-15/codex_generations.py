

# Generated at 2022-06-14 16:55:50.057854
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert issubclass(SafariApiIE, InfoExtractor)
    assert issubclass(SafariApiIE, SafariBaseIE)
    assert not issubclass(SafariApiIE, SafariIE)
    assert not issubclass(SafariApiIE, SafariCourseIE)
    assert issubclass(SafariCourseIE, InfoExtractor)
    assert issubclass(SafariCourseIE, SafariBaseIE)
    assert not issubclass(SafariCourseIE, SafariIE)

# Generated at 2022-06-14 16:55:58.898457
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE('safari:api')
    # This is a set of unique strings that were extracted from SafariApiIE
    # during creation of this unit test. They were extracted from:
    #     SafariApiIE._VALID_URL = ...
    #     SafariBaseIE._LOGIN_URL = ...
    #     SafariBaseIE._NETRC_MACHINE = ...
    #     SafariBaseIE._API_BASE = ...
    #     SafariBaseIE._API_FORMAT = ...

# Generated at 2022-06-14 16:56:00.906234
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    info_extractor = SafariApiIE()
    return info_extractor


# Generated at 2022-06-14 16:56:02.480544
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    IE = SafariBaseIE()
    assert IE.LOGGED_IN is False

# Generated at 2022-06-14 16:56:14.107528
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # From this link, we see that first page of chapter's content is
    # https://learning.oreilly.com/library/view/cracking-codes-with/9781593276848/
    # from which we can get referenceId and partnerId and uiConfId
    chapter_content_url = 'https://www.safaribooksonline.com/api/v1/book/9781593276848/chapter/cracking-codes-with-python.html'
    safari_api_ie = SafariApiIE(SafariApiIE.create_ie())
    safari_api_ie._download_webpage = lambda url, video_id: None
    safari_api_ie._real_extract(chapter_content_url)

# Generated at 2022-06-14 16:56:20.746816
# Unit test for constructor of class SafariIE
def test_SafariIE():
    tester = SafariIE()
    assert tester.IE_NAME == 'safari'
    assert tester.IE_DESC == 'safaribooksonline.com online video'
    assert tester._VALID_URL == r'''(?x)
                        https?://
                            (?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/
                            (?:
                                library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?\#&]+)\.html|
                                videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?\#&]+)
                            )
                    '''

# Generated at 2022-06-14 16:56:24.174562
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # It's difficult to unittest SafariBaseIE, because login to safaribooksonline is required
    if True:
        pass
    else:
        safari_api_ie = SafariApiIE()
        safari_api_ie._real_initialize()

# Generated at 2022-06-14 16:56:28.754097
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Tests that SafariApiIE class is created with a valid url
    m_url = 'https://www.safaribooksonline.com/api/v1/book/9780134664057/chapter/RHCE_Introduction.html'
    safari_api_ie = SafariApiIE(SafariApiIE.create_ie(m_url))
    return safari_api_ie


# Generated at 2022-06-14 16:56:29.507515
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()



# Generated at 2022-06-14 16:56:32.528222
# Unit test for constructor of class SafariIE
def test_SafariIE():
    class TestSafariIE(SafariIE):
        def _download_webpage(self, *args, **kwargs):
            raise Exception

        def _download_json(self, *args, **kwargs):
            raise ExtractorError('test error')

    test_ie = TestSafariIE()
    assert test_ie._download_obj(test_ie._login)

# Generated at 2022-06-14 16:56:47.033816
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class TestSafariBaseIE(SafariBaseIE):
        IE_NAME = 'test'
        _VALID_URL = r'https?://example\.com/'
    assert TestSafariBaseIE(TestSafariBaseIE.ie_key())._NETRC_MACHINE == TestSafariBaseIE._NETRC_MACHINE

# Generated at 2022-06-14 16:56:47.755881
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 16:56:51.164033
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .content import Content

    expected_class = Content

    obj = SafariIE()

    assert(isinstance(obj,expected_class))
    assert(obj.__class__ is expected_class)

# Generated at 2022-06-14 16:56:54.047918
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    m = SafariBaseIE(SafariIE)
    assert m.LOGGED_IN == False
    assert m._NETRC_MACHINE == 'safari'

# Generated at 2022-06-14 16:56:56.234116
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """Basic unit test for the SafariBaseIE."""
    IE = SafariBaseIE()
    assert IE.IE_NAME == 'safari'

# Generated at 2022-06-14 16:56:59.623399
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert SafariBaseIE(test_SafariBaseIE.test_url)

test_SafariBaseIE.test_url = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838/9780133392838-00_SeriesIntro'

# Generated at 2022-06-14 16:57:08.339857
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    class_ = SafariApiIE()

    actual = class_._VALID_URL
    expected = 'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'
    assert actual == expected

# Generated at 2022-06-14 16:57:16.881246
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    test_cases = [
        'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json',
        'http://techbus.safaribooksonline.com/9780134426365',
        'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314',
        'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838',
        'https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/',
    ]

    for test_case in test_cases:
        assert SafariCourseIE.suitable(test_case)


# Generated at 2022-06-14 16:57:21.266542
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    try:
        import pytest
    except ImportError:
        pytest = None

    if pytest is None:
        return

    def test_SafariCourseIE_instantiation():
        """Tests instantiation of SafariCourseIE object."""
        safari_course_ie = SafariCourseIE()
        assert safari_course_ie

    test_SafariCourseIE_instantiation()

# Generated at 2022-06-14 16:57:21.897839
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE()

# Generated at 2022-06-14 16:57:45.445989
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    type(SafariCourseIE)

# Generated at 2022-06-14 16:57:46.767700
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie_ = SafariApiIE()
    assert ie_.IE_NAME == 'safari:api'

# Generated at 2022-06-14 16:57:49.042999
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class TestSafariBaseIE(SafariBaseIE):
        IE_NAME = 'test_safari_base'
        _VALID_URL = r'https?://.+'

    TestSafariBaseIE()._login()

# Generated at 2022-06-14 16:57:50.970046
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE(SafariBaseIE._create_get_method('username', 'password'))
    print(ie.IE_NAME)


test_SafariIE()

# Generated at 2022-06-14 16:58:00.400181
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Fake URL
    test_url = "https://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_00"
    # Intantiate class
    safari = SafariBaseIE()
    assert safari.suitable(test_url)
    assert safari.IE_NAME == 'safari'
    assert safari.IE_DESC == 'safaribooksonline.com online video'
    assert safari._VALID_URL == SafariIE._VALID_URL
    assert safari._TESTS == SafariIE._TESTS

test_SafariBaseIE()

# Generated at 2022-06-14 16:58:07.457026
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    safari_ie = SafariIE()
    safari_ie._real_initialize()
    safari_ie._LOGIN_URL = 'https://learning.oreilly.com/accounts/login/'
    safari_ie._NETRC_MACHINE = 'safari'
    safari_ie._API_BASE = 'https://learning.oreilly.com/api/v1'
    safari_ie._API_FORMAT = 'json'
    safari_ie.LOGGED_IN = False
    safari_ie._login()
    safari_ie._real_extract(url)

# Generated at 2022-06-14 16:58:10.949823
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')

# Generated at 2022-06-14 16:58:11.658394
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 16:58:16.391164
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    test_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    test_title = 'Hadoop Fundamentals LiveLessons'
    assert test_title == SafariCourseIE()._real_extract(test_url)['_type']

# Generated at 2022-06-14 16:58:17.978370
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    S = SafariBaseIE()

# Generated at 2022-06-14 16:58:43.735076
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    inst = SafariApiIE()
    assert inst

# Generated at 2022-06-14 16:58:44.779221
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE('', test=True)

# Generated at 2022-06-14 16:58:53.488501
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    safariIE = SafariIE(url)
    assert safariIE.api_base_url == 'https://learning.oreilly.com/api/v1/'
    assert safariIE.login_url == 'https://learning.oreilly.com/accounts/login/'
    assert safariIE.partner_id == '1926081'
    assert safariIE.ui_id == '29375172'
    assert safariIE.reference_id == '9780133392838-part00'

# Generated at 2022-06-14 16:59:01.369288
# Unit test for constructor of class SafariIE
def test_SafariIE():
    tst = SafariIE()
    assert tst._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert tst._NETRC_MACHINE == 'safari'
    assert tst._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert tst._API_FORMAT == 'json'
    assert tst.LOGGED_IN is False


# Generated at 2022-06-14 16:59:05.642485
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """Test constructor of class SafariBaseIE"""
    # Test empty username and password hashes
    safari_base_ie = SafariBaseIE()
    assert safari_base_ie._username is None
    assert safari_base_ie._password is None
    assert safari_base_ie.LOGGED_IN is False

# Generated at 2022-06-14 16:59:10.153753
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE('safari')
    # Ensure we are not logged in (must be overriden)
    assert ie.LOGGED_IN is False
    assert ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert ie._NETRC_MACHINE == 'safari'
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert ie._API_FORMAT == 'json'

# Generated at 2022-06-14 16:59:18.529015
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    api_base = "https://learning.oreilly.com/api/v1"
    api_format = 'json'
    login_url = "https://learning.oreilly.com/accounts/login/"
    netrc_machine = 'safari'


# Generated at 2022-06-14 16:59:19.612972
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:59:22.676567
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE()
    assert ie.IE_NAME == 'safari:course'
    assert ie.IE_DESC == 'safaribooksonline.com online courses'

# Generated at 2022-06-14 16:59:31.142245
# Unit test for constructor of class SafariIE
def test_SafariIE():
    constructor = SafariIE("safari")

    assert constructor.ie_key() == "safari"
    assert constructor._VALID_URL == r'''(?x)
                        https?://
                            (?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/
                            (?:
                                library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?\#&]+)\.html|
                                videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?\#&]+)
                            )
                    '''


# Generated at 2022-06-14 17:00:22.068128
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE(SafariIE.ie_key(), {})

# Generated at 2022-06-14 17:00:23.456664
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    credentials = {}
    obj = SafariBaseIE(credentials)
    assert obj.LOGGED_IN == False

# Generated at 2022-06-14 17:00:27.500944
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .common import test_info_dicts, test_urls, unittest
    from .test_utils import FakeLoginSession

    class SafariIETest(unittest.TestCase):
        def setUp(self):
            self.ie = SafariIE(FakeLoginSession())

        def test_SafariIE(self):
            test_info_dicts(self, test_urls.items(), self.ie)

    unittest.main(argv=[''])

# Generated at 2022-06-14 17:00:30.991743
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    module = __import__('safari')
    instance = module.SafariCourseIE(module.SafariCourseIE.ie_key())
    assert isinstance(instance, module.SafariCourseIE)

# Generated at 2022-06-14 17:00:32.360518
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    inst = SafariApiIE()
    assert inst._VALID_URL is not None

# Generated at 2022-06-14 17:00:33.928214
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safarie = SafariIE()
    return safarie

# Generated at 2022-06-14 17:00:37.527603
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safaribooksonline = SafariIE()
    assert isinstance(safaribooksonline, SafariIE)
    assert safaribooksonline.ie_key() == 'Safari'


# Generated at 2022-06-14 17:00:38.563937
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert repr(SafariCourseIE)

# Generated at 2022-06-14 17:00:39.740884
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    assert isinstance(ie, SafariApiIE)

# Generated at 2022-06-14 17:00:40.610993
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE()
    assert ie



# Generated at 2022-06-14 17:02:48.582230
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert not SafariBaseIE().LOGGED_IN

# Generated at 2022-06-14 17:02:59.169463
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Arrange
    url = 'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_00'
    # Act
    sut = SafariIE()
    # Assert

# Generated at 2022-06-14 17:03:09.196004
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import json
    from .common import compat_urlparse
    from .common import ExtractorError
    from .common import PyqueryExtractor
    from .common import compat_str
    from .common import compat_urllib_parse

    url = 'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html'
    mobj = re.match(SafariApiIE._VALID_URL, url)
    id = '%s/%s' % (mobj.group('course_id'), mobj.group('part'))
    part = json.loads(PyqueryExtractor()._download_webpage_handle(url, id).text)

# Generated at 2022-06-14 17:03:10.871937
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    assert ie.LOGGED_IN == False


# Generated at 2022-06-14 17:03:12.659158
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert SafariIE()._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'

# Generated at 2022-06-14 17:03:13.283293
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE()

# Generated at 2022-06-14 17:03:15.164981
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE('')
    assert ie._NETRC_MACHINE == 'safari'

# Generated at 2022-06-14 17:03:17.764643
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 17:03:19.542509
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 17:03:26.334020
# Unit test for constructor of class SafariIE
def test_SafariIE():
    if True:
        # Manual testing of SafariIE
        import pprint
        # pprint.pprint(safariIE.check_login())
        # pprint.pprint(safariIE.extract_entries(
        #     'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838/9780133392838-00_SeriesIntro'))
        pprint.pprint(SafariIE()._real_extract(
            'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'))