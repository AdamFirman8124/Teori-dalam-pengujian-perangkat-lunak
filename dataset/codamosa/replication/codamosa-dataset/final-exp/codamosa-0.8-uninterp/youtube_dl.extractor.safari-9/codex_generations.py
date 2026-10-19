

# Generated at 2022-06-14 16:55:45.580105
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    i = SafariBaseIE()
    assert i.LOGGED_IN is False

# Generated at 2022-06-14 16:55:56.603887
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    test_cases = [
        # Test no credentials supplied
        {
            'netrc_data': None,
            'expected_success': False
        },
        # Test invalid credentials supplied
        {
            'netrc_data': {
                'machine': 'safari',
                'login': 'invalidusername',
                'password': 'InvalidPassword'
            },
            'expected_success': True
        },
        # Test valid credentials supplied
        {
            'netrc_data': {
                'machine': 'safari',
                'login': 'a@b.com',
                'password': 'ValidPassword'
            },
            'expected_success': True
        }
    ]

    for test_case in test_cases:
        safari_ie = SafariBaseIE()
        safari_ie._login_info = test_

# Generated at 2022-06-14 16:56:08.470165
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Test that a SafariCourseIE raises a correct error when 'chapters' key
    # is not present in the course Json.
    safari = SafariCourseIE()
    test_url = 'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314'
    course_id = '9780134217314'

    course_json = '{"title": "Python Programming Language"}'
    course_json = json.loads(course_json)
    assert course_json['title'] == 'Python Programming Language'
    if 'chapters' not in course_json:
        raise ExtractorError(
            'No chapters found for course %s' % course_id, expected=True)

# Generated at 2022-06-14 16:56:15.158379
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from ykdl.extractors.safari import SafariIE

    course_id = "9781449396459"
    url="https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/"
    ie = SafariIE()
    ie.extract(url)
    ie.tempdir
    url = ie.url_result(url, ie.ie_key())
    ie.__class__.__name__

# Generated at 2022-06-14 16:56:18.257928
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class TestSafariBaseIE(SafariBaseIE):
        _VALID_URL = r'https?://.+'
    TestSafariBaseIE('username', 'password')

# Generated at 2022-06-14 16:56:22.065317
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from ytdl.extractor import gen_extractors
    def check_module_available(module_name):
        return module_name in globals()
    youtube_ie = gen_extractors(check_module_available)['youtube']()

    assert type(youtube_ie) is type

# Generated at 2022-06-14 16:56:23.668101
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    if not(SafariCourseIE._LOGIN_URL):
        raise AssertionError('Expected value not found')

# Generated at 2022-06-14 16:56:26.106171
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    s = SafariBaseIE()
    assert s.IE_NAME == 'safari'
    assert s.IE_DESC == 'safaribooksonline.com online video'


# Generated at 2022-06-14 16:56:28.786355
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    exampleUrl = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    SafariCourseIE.suitable(exampleUrl)

# Generated at 2022-06-14 16:56:31.444449
# Unit test for constructor of class SafariIE
def test_SafariIE():
    class_ = SafariIE
    fields = [
        '_API_BASE', '_API_FORMAT', '_NETRC_MACHINE', '_LOGIN_URL']
    for field in fields:
        assert hasattr(class_, field) and getattr(class_, field) is not None

# make sure SafariIE does not require an account

# Generated at 2022-06-14 16:56:48.474808
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    url = 'https://www.safaribooksonline.com/member/login/'
    username = 'some_username'
    password = 'some_password'
    ie = SafariBaseIE()
    ie._login()
    assert ie.LOGGED_IN == False
    credentials = {'username': username, 'password': password}
    ie.login(username, password)
    assert ie.LOGGED_IN == False

# Generated at 2022-06-14 16:56:50.203188
# Unit test for constructor of class SafariIE
def test_SafariIE():
    import doctest
    doctest.testmod(SafariIE)

# Generated at 2022-06-14 16:56:50.823061
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    pass

# Generated at 2022-06-14 16:56:55.268780
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    t = SafariBaseIE()
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    t.url = url
    t.initialize()
    return t

# Generated at 2022-06-14 16:56:58.228434
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Check that the constructor doesn't raise an exception (it did, see https://github.com/rg3/youtube-dl/issues/13240)
    inst = SafariApiIE()
    assert inst is not None

# Generated at 2022-06-14 16:57:01.988683
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    sce = SafariCourseIE()
    assert SafariCourseIE.suitable('https://www.safaribooksonline.com/api/v1/book/9781449396459')
    assert not SafariCourseIE.suitable('https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')

# Generated at 2022-06-14 16:57:13.316804
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    cls = SafariCourseIE
    # Following lines of the constructor are not tested:
    #     cls.js_to_json = staticmethod(js_to_json)
    #     cls.suitable = staticmethod(lambda url: False if SafariIE.suitable(url) or SafariApiIE.suitable(url) else cls._VALID_URL.match(url) is not None)

    # Test _real_extract with URL that does not match regex
    url = 'http://techbus.safaribooksonline.com/book/9780134426365'
    obj = cls()
    with pytest.raises(ExtractorError) as excinfo:
        obj._real_extract(url)
    assert excinfo.match("No chapter URLs found on page")


# Generated at 2022-06-14 16:57:19.489025
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari_ie = SafariIE('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314', '9780134217314')
    assert safari_ie.IE_NAME == 'safari'
    assert safari_ie.IE_DESC == 'safaribooksonline.com online video'

# Generated at 2022-06-14 16:57:21.631278
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert(SafariCourseIE._VALID_URL == SafariCourseIE._VALID_URL)

# Generated at 2022-06-14 16:57:24.194474
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE(SafariCourseIE.ie_key())
    

# Generated at 2022-06-14 16:57:46.370122
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE(None)
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
    assert IE_NAME == 'safari'

# Generated at 2022-06-14 16:57:54.212072
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():

    # Test case with safaribooksonline account credentials
    from ..compat import compat_urllib_request, compat_cookielib
    from ..utils import unified_strdate

    account_email = 'test@test'
    account_passwd = 'testP$ss'

    cookie_handler = compat_urllib_request.HTTPCookieProcessor(
        compat_cookielib.CookieJar())

    # First, login SafariBaseIE with safaribooksonline account (test@test:testP$ss)
    # to get a valid session cookie so that SafariBaseIE can access restricted
    # resources.
    safari_base = SafariBaseIE(cookie_handler)
    safari_base._downloader.troubleshoot = True

    safari_base.report_login = True
    safari_base

# Generated at 2022-06-14 16:57:55.138567
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    a = SafariCourseIE()
    assert a

# Generated at 2022-06-14 16:57:56.023872
# Unit test for constructor of class SafariIE
def test_SafariIE():
    test_SafariIE.ie = SafariIE()

# Generated at 2022-06-14 16:58:01.476777
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    test_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    i = SafariCourseIE()
    result = i.suitable(test_url)
    assert result

# Generated at 2022-06-14 16:58:02.343260
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:58:02.986795
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:58:10.851740
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Testing URL without the redirects and with the videos_noredirects IE get
    # from the normal URL
    SafariIE().url_result(
        'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838/9780133392838-00_SeriesIntro',
        'Kaltura')

# Generated at 2022-06-14 16:58:13.778868
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    assert ie.IE_NAME == 'SafariApi'
    assert ie.ie_key() == 'SafariApi'

# Generated at 2022-06-14 16:58:16.795326
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html")



# Generated at 2022-06-14 16:58:44.969506
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    instance = SafariApiIE()

# Generated at 2022-06-14 16:58:49.003366
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():

    # Initialize with invalid username and password
    safariBaseIE = SafariBaseIE('username', 'password')

    # Try to log in
    safariBaseIE._login()

    # Check if not logged in
    assert safariBaseIE.LOGGED_IN == False


# Generated at 2022-06-14 16:59:00.368619
# Unit test for constructor of class SafariIE
def test_SafariIE():
    import sys
    from .utils import set_cookie

    # constructors aren't run on import, so do it here
    safari = SafariIE(SafariBaseIE)

    # check for no login data
    safari.to_screen = lambda *x: None
    safari.to_stdout = lambda *x: None
    safari._login()
    assert safari.LOGGED_IN is False

    # check for bad login data
    set_cookie(safari._downloader, 'learning.oreilly.com', 'the_user', 'the_pass')
    err = None
    try:
        safari._login()
    except ExtractorError as e:
        err = e
    assert err
    assert not safari.LOGGED_IN

    # check for good login data

# Generated at 2022-06-14 16:59:04.387536
# Unit test for constructor of class SafariIE
def test_SafariIE():
    urlh = SafariIE()._download_webpage_handle('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html', '9780133392838/part00.html')

# Generated at 2022-06-14 16:59:11.596169
# Unit test for constructor of class SafariBaseIE

# Generated at 2022-06-14 16:59:16.322964
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    expected_value = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Host': 'api.oreilly.com',
        'Pragma': 'no-cache',
        'Referer': 'https://api.oreilly.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    test_instance = SafariBaseIE()
    assert test_instance._headers() == expected_value

# Generated at 2022-06-14 16:59:27.013543
# Unit test for constructor of class SafariIE
def test_SafariIE():
    obj = SafariIE()
    assert obj.IE_NAME == 'safari'
    assert obj.IE_DESC == 'safaribooksonline.com online video'
    assert obj._VALID_URL == '(?x)https?://(?:www\\.)?(?:safaribooksonline|(?:learning\\.)?oreilly)\\.com/library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?#&]+)\\.html'
    assert obj._UICONF_ID == '29375172'
    assert obj._PARTNER_ID == '1926081'

# Generated at 2022-06-14 16:59:34.616912
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .test_safarie import Response
    import os

    ids = [
        # Oreilly
        'hadoop-fundamentals-livelessons',
        '9780133392838',
        '9780133392838_2',
        '9780133392838-part00',
        '9780133392838-part00_2',

        # Safari
        'hadoop-fundamentals-livelessons',
        '9780133392838',
        '9780133392838_1',
        '9780133392838-part00',
        '9780133392838-part00_1',
    ]
    for id in ids:
        assert SafariIE()._match_id(id) == '9780133392838'
        assert SafariIE()._match

# Generated at 2022-06-14 16:59:40.355779
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert SafariIE._parse_reference_id('reference_id') == 'reference_id'
    assert SafariIE._parse_reference_id('/reference_id') == 'reference_id'
    assert SafariIE._parse_reference_id('/reference_id/') == 'reference_id'
    assert SafariIE._parse_reference_id('/reference_id/more') == 'reference_id'
    assert SafariIE._parse_reference_id('/reference_id.more') == 'reference_id'
    assert SafariIE._parse_reference_id('/reference_id.more/') == 'reference_id'
    assert (SafariIE._parse_reference_id(
        'https://example.com/reference_id/more') == 'reference_id')

# Generated at 2022-06-14 16:59:50.096387
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    inst = SafariCourseIE('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    isinstance(inst, SafariCourseIE)
    assert inst.__name__ == 'SafariCourseIE'
    assert inst.__sizeof__() == 56
    assert inst.__str__() == '<SafariCourseIE>'
    assert inst.__hash__()

    inst = SafariCourseIE('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')
    isinstance(inst, SafariCourseIE)
    assert inst.__name__ == 'SafariCourseIE'
    assert inst.__sizeof__() == 56
    assert inst.__str__

# Generated at 2022-06-14 17:00:55.941801
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    obj = SafariApiIE()
    assert obj.LOGGED_IN is False

# Generated at 2022-06-14 17:01:03.754354
# Unit test for constructor of class SafariApiIE

# Generated at 2022-06-14 17:01:12.521529
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Test old URL
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    ie = SafariCourseIE(SafariBaseIE())
    assert ie.suitable(url)
    assert ie.IE_NAME == 'safari:course'
    # Test new URL
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    ie = SafariCourseIE(SafariBaseIE())
    assert ie.suitable(url)
    assert ie.IE_NAME == 'safari:course'

# Generated at 2022-06-14 17:01:16.189258
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from tests import BaseTest
    from .safaribooksonline import SafariBaseIE
    url = 'http://foo.bar'
    obj = SafariBaseIE(BaseTest.dict2context([{
        'url': url,
        'username': 'foo',
        'password': 'bar'
    }])).suitable(url)
    assert obj == True, 'constructor of class SafariBaseIE failed'

# Generated at 2022-06-14 17:01:27.623355
# Unit test for constructor of class SafariIE

# Generated at 2022-06-14 17:01:38.458316
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    try:
        SafariCourseIE('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')
    except:
        assert False
    try:
        SafariCourseIE('https://www.safaribooksonline.com/api/v1/book/9781449396459')
    except:
        assertFalse
    try:
        SafariCourseIE('https://www.safaribooksonline.com/api/v1/book/9781449396459/')
    except:
        assertFalse
    try:
        SafariCourseIE('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    except:
        assertFalse

# Generated at 2022-06-14 17:01:40.476562
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    instance = InfoExtractor()
    # Create an instance of class SafariBaseIE
    instance = SafariBaseIE()
    # Check if instance created successfully
    assert isinstance(instance, SafariBaseIE)

# Generated at 2022-06-14 17:01:52.597061
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    api_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    error_msg_1 = 'Unable to download video webpage'
    error_msg_2 = 'Unable to extract video url'

# Generated at 2022-06-14 17:02:00.613402
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from .common import fake_urlopen
    from ..utils import compat_urllib_request, compat_urllib_error

    IE = SafariBaseIE.__bases__[0]
    IE._download_webpage = staticmethod(lambda *args, **kargs: (args, kargs))
    IE._download_json = staticmethod(lambda *args, **kargs: (args, kargs))

    # No authentication
    ie = SafariBaseIE()
    assert ie._login() is None
    assert ie._real_initialize() is None
    assert ie.LOGGED_IN is False

    # test authentication
    # success
    ie = SafariBaseIE()
    ie._get_tfa_token = lambda _: ''
    ie._get_login_info = lambda: ('', '')
    ie._download_webpage_

# Generated at 2022-06-14 17:02:08.823578
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE(); assert ie.ie_key() == 'SafariCourse'
    ie = SafariCourseIE(SafariCourseIE._VALID_URL); assert ie.ie_key() == 'SafariCourse'
    ie = SafariCourseIE('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314'); assert ie.ie_key() == 'SafariCourse'
    ie = SafariCourseIE('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'); assert ie.ie_key() == 'SafariCourse'

# Generated at 2022-06-14 17:04:56.644325
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://learning.oreilly.com/api/v1/book/9781449396459/chapter-content/ch06.html/'
    SafariApiIE(SafariBaseIE._downloader, url)

# Generated at 2022-06-14 17:04:58.176238
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
	print(SafariCourseIE('safari:course'))

# Generated at 2022-06-14 17:05:00.537796
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE('safari:api')
    assert ie.ie_name() == 'safari:api'

# Generated at 2022-06-14 17:05:02.417299
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE()
    assert safari_base_ie is not None

# Generated at 2022-06-14 17:05:03.535756
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE()
    assert ie.LOGGED_IN == False

# Generated at 2022-06-14 17:05:05.952497
# Unit test for constructor of class SafariIE
def test_SafariIE():
    global test_SafariIE
    test_SafariIE = True
    #SafariIE(SafariBaseIE(), "")

# Generated at 2022-06-14 17:05:17.259940
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from .. import inheriting_classes

# Generated at 2022-06-14 17:05:24.427391
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class safaribooksonlineIE_test(SafariBaseIE):
        IE_NAME = 'test'
        _VALID_URL = r'https?://localhost/'

    assert safaribooksonlineIE_test('Test').IE_NAME == 'test'
    assert safaribooksonlineIE_test('Test')._VALID_URL == r'https?://localhost/'

# Generated at 2022-06-14 17:05:29.773326
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    course_id = '9781617291935'
    chapter_id = 'part45'

    url = str(
        'https://www.safaribooksonline.com/api/v1/book/'
        '{course_id}/chapter/'
        '{chapter_id}'
        '.html'.format(
            course_id=course_id,
            chapter_id=chapter_id
    ))

    # Check that safari api IE is able to extract the safari video URL from the
    # safari api URL.
    video_url = SafariApiIE()._real_extract(url)