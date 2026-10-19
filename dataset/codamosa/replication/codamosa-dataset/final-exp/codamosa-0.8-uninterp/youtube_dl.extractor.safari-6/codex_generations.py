

# Generated at 2022-06-14 16:55:56.418365
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safariie = SafariIE()
    assert safariie.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    assert not safariie.suitable('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_00')
    assert safariie.IE_NAME == 'safari'
    assert safariie.IE_DESC == 'safaribooksonline.com online video'

# Generated at 2022-06-14 16:56:01.853188
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # SafariApiIE doesn't have __init__ method, so we call constructor of
    # superclass
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    SafariApiIE(lambda *x, **y: None)._real_extract(url)

# Generated at 2022-06-14 16:56:08.154792
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Unit test for constructor of class SafariIE
    sample_url = SafariIE._TESTS[0]['url']
    ie = SafariIE(None)
    assert ie is not None
    assert ie.LOGGED_IN == False
    ie.initialize()
    assert ie.LOGGED_IN == True

# Generated at 2022-06-14 16:56:13.098401
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE()
    if ie._NETRC_MACHINE:
        username, password = ie._get_login_info()
        html = ie._download_webpage(ie._LOGIN_URL, None, 'Logging in as %s' % username, None)
        assert 'O\'Reilly Home' in html, 'Could not log in!'

# Generated at 2022-06-14 16:56:23.754912
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Test if it initializes correctly
    course = SafariCourseIE()

    # Test if it raise an error for an invalid webpage
    webpage = None
    with pytest.raises(TypeError) as excinfo:
        course._parse_page(webpage)
    assert ('webpage must be a string or a list of bytes' in str(excinfo.value))

    # Test if it returns a False boolean for a wrong webpage
    webpage = '<html></html>'
    assert course._parse_page(webpage) is False

    # Test if it returns a False boolean for a wrong webpage
    webpage = '<html><p>This is not a Safari webpage</p></html>'
    assert course._parse_page(webpage) is False

# Generated at 2022-06-14 16:56:31.463914
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE(SafariBaseIE)
    assert safari_api_ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari_api_ie._API_FORMAT == 'json'
    assert safari_api_ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'

# Generated at 2022-06-14 16:56:39.729730
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Instantiation with valid url
    assert isinstance(SafariCourseIE('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'), SafariCourseIE)

    # Instantiation with invalid url
    assert not isinstance(SafariCourseIE('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'), SafariCourseIE)

# Generated at 2022-06-14 16:56:41.411929
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safe_construct(SafariBaseIE, ['safari'])

# Generated at 2022-06-14 16:56:46.988689
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Test course created on website has chapters
    url = 'https://www.safaribooksonline.com/api/v1/book/9780134426365/?override_format=json'
    safari_course_ie = SafariCourseIE()
    # Call method to extract information about course (course_id, title, etc.)
    result = safari_course_ie._real_extract(url)
    # Verify that course has chapters
    assert result['_type'].lower() == 'playlist'

# Generated at 2022-06-14 16:56:48.548770
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Test to see if we can instantiate this class
    safari_ie = SafariIE()

# Generated at 2022-06-14 16:57:14.979564
# Unit test for constructor of class SafariIE
def test_SafariIE():
    s_ie = SafariIE()
    assert s_ie.LOGGED_IN == False
    assert s_ie == SafariIE()
    assert s_ie != SafariCourseIE()



# Generated at 2022-06-14 16:57:21.405158
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE()
    assert ie.IE_NAME == 'safari:course'
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+|api/v1/book|videos/[^/]+)/(?P<id>[^/]+)'

# Generated at 2022-06-14 16:57:34.791773
# Unit test for constructor of class SafariApiIE

# Generated at 2022-06-14 16:57:35.653976
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    instance = SafariApiIE()
    assert instance._VALID_URL == SafariApiIE._VALID_URL

# Generated at 2022-06-14 16:57:44.799552
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    if not (SafariBaseIE._downloader is None):
        SafariBaseIE._downloader.cache.remove()
        SafariBaseIE._downloader.params.update({
            'username': '',
            'password': '',
            'nopart': True,
            'forcetitle': True,
            'forceurl': True,
            'forcethumbnail': True,
            'quiet': True
        })

    # logged out
    safari_api_ie = SafariApiIE()
    assert not safari_api_ie.LOGGED_IN

    # logged in
    SafariBaseIE._downloader.cache.remove()
    SafariBaseIE._downloader.params.update({
        'username': 'example',
        'password': 'example'
    })
    safari_api_ie = SafariApiIE

# Generated at 2022-06-14 16:57:51.219595
# Unit test for constructor of class SafariIE
def test_SafariIE():
    import youtube_dl.utils
    url1 = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    assert youtube_dl.utils.url_basename(url1) == 'part00.html'
    assert youtube_dl.utils.url_basename(url1, remove_query=True) == 'part00'
    assert youtube_dl.utils.url_basename(url1, fail_if_no_match=False) == 'part00'
    se  = SafariIE()
    result = se._real_extract('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')


# Generated at 2022-06-14 16:57:55.524061
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safariApiIE = SafariApiIE()
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    course_id = safariApiIE._match_id(url)
    print(course_id)  # 9781449396459

# Generated at 2022-06-14 16:57:59.226184
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    instance = SafariCourseIE()
    assert isinstance(instance, SafariCourseIE)


# Generated at 2022-06-14 16:58:08.383807
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .common import fake_urlopen
    from .subtitles import SubtitlesInfoExtractor
    from .kaltura import KalturaIE

    def open(url, *args, **kwargs):
        if not isinstance(url, compat_str):
            url = url.get_full_url()
        ie = SafariIE()
        if url == 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html':
            return compat_fake_urlopen(
                bytes('<div data-reference-id="ref_id"></div>', 'utf-8'),
                headers={'Content-Type': 'text/html'})

# Generated at 2022-06-14 16:58:09.095599
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:58:37.352541
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Test constructor
    obj = SafariIE('Safari')
    assert obj.LOGGED_IN == False



# Generated at 2022-06-14 16:58:38.763207
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE('test', 'safaribooksonline.com')

# Generated at 2022-06-14 16:58:41.779792
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safari_course_ie = SafariCourseIE()
    assert safari_course_ie.suitable(SafariCourseIE._VALID_URL)


# Generated at 2022-06-14 16:58:51.939116
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """
    Test for the constructor of the class SafariIE
    """
    import json
    import unittest

    from ytdl.extractor import safari

    class TestSafariIE(unittest.TestCase):
        def test_SafariIE_success(self):
            IE = safari.SafariIE()

            self.assertIsNotNone(IE)

            IE2 = safari.SafariIE()

            self.assertEqual(IE, IE2)

    test_suite = unittest.TestSuite()
    test_suite.addTest(TestSafariIE('test_SafariIE_success'))

    unittest.TextTestRunner().run(test_suite)

# Generated at 2022-06-14 16:58:53.453595
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    instance = SafariBaseIE()
    assert isinstance(instance._downloader, InfoExtractor)


# Generated at 2022-06-14 16:59:02.722584
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    _init = SafaribooksonlineBaseIE(SafariApiIE.ie_key(),
            SafariApiIE.ie_key())._initialize
    _init()
    _init(SafariApiIE.ie_key())
    _init(SafariApiIE.ie_key(), SafariApiIE.ie_key())
    _init(SafariApiIE.ie_key(), SafariApiIE.ie_key(),
            'https://www.safaribooksonline.com/')

# Generated at 2022-06-14 16:59:04.209045
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    x = SafariBaseIE()
    assert not x.LOGGED_IN

# Generated at 2022-06-14 16:59:11.517729
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    ie = SafariCourseIE('test')
    assert ie.IE_NAME == 'safari:course'
    assert ie.IE_DESC == 'safaribooksonline.com online courses'
    assert ie._VALID_URL == r'(?x)https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+|api/v1/book|videos/[^/]+)*/(?P<id>[^/]+)'

# Generated at 2022-06-14 16:59:17.388505
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert (str(SafariBaseIE._login_return_either(lambda: None)) ==
            '<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)>')
    assert (str(SafariBaseIE._login_return_either(lambda: 'OREILLY')) ==
            'OREILLY')

# Generated at 2022-06-14 16:59:23.539027
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE('SafariBaseIE', 'safaribooksonline.com')
    ie._download_webpage_handle = lambda x,y,z : '<html><head></head><body></body></html>'
    ie.LOGGED_IN = None
    ie._real_initialize()
    assert(ie.LOGGED_IN == False)

# Generated at 2022-06-14 17:00:19.201204
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # No need to test this
    pass

# Generated at 2022-06-14 17:00:22.069275
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """
    Unit testing for SafariIE
    """

    # Test pristine constructor
    safari = SafariBaseIE()

    # Test constructor with parameters
    safari = SafariBaseIE(None, None)


# Generated at 2022-06-14 17:00:23.904645
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html")


# Generated at 2022-06-14 17:00:30.983468
# Unit test for constructor of class SafariIE
def test_SafariIE():
    class MockSafariBaseIE(SafariBaseIE):
        _NETRC_MACHINE = 'safari'

        def _real_initialize(self):
            self._login()


# Generated at 2022-06-14 17:00:32.667875
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()
    assert ie._VALID_URL == SafariIE._VALID_URL

# Generated at 2022-06-14 17:00:41.903075
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    course_id = '9781449396459'
    course_title = 'Programming Foundations with Python'
    mobj = re.match(
        SafariCourseIE._VALID_URL,
        'https://www.safaribooksonline.com/api/v1/book/%s/' % course_id)
    course = SafariCourseIE._real_extract(
        SafariCourseIE(),
        'https://www.safaribooksonline.com/api/v1/book/%s/' % course_id)

    api = SafariApiIE()
    first_chapter_id = mobj.group('id')

# Generated at 2022-06-14 17:00:48.512348
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9780134664057/chapter-content/RHCE_Introduction.html'
    Safapi_api_ie = SafariApiIE()
    test1 = Safapi_api_ie.suitable(url)
    assert test1 is True

# Generated at 2022-06-14 17:00:49.107161
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 17:00:56.647750
# Unit test for constructor of class SafariIE
def test_SafariIE():
    course_id = '9780134217314'
    course_title = 'Python Programming Language'
    # Create object of SafariCourseIE
    safarie = SafariCourseIE()
    # Call _real_extract to get JSON for course_id and test that
    # course_id is present in course_json
    course_json = safarie._download_json(
        '%s/book/%s/?override_format=%s' % (safarie._API_BASE, course_id, safarie._API_FORMAT),
        course_id, 'Downloading course JSON')
    assert course_json['id'] == course_id
    # Call _real_extract to get JSON for course_id and test that
    # course_title is present in course_json

# Generated at 2022-06-14 17:00:58.332211
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safari_course_ie = SafariCourseIE()
    assert safari_course_ie


# Generated at 2022-06-14 17:03:20.054959
# Unit test for constructor of class SafariIE
def test_SafariIE():
    """ Simple unit test for checking SafariIE constructor works """
    ie = SafariIE("")
    assert ie is not None

# Generated at 2022-06-14 17:03:23.491569
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    URL = 'https://www.safaribooksonline.com/library/view/python-crash-course/9781491937952/'
    safari_course = SafariCourseIE()
    assert (safari_course._match_id(URL) == '9781491937952')

# Generated at 2022-06-14 17:03:30.771001
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE()
    assert ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert ie._NETRC_MACHINE == 'safari'
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert ie._API_FORMAT == 'json'
    assert ie.LOGGED_IN is False

# Generated at 2022-06-14 17:03:39.184233
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Test safari video constructor
    video = SafariIE('http://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    assert video.IE_NAME == 'safari'
    assert video.IE_DESC == 'safaribooksonline.com online video'
    assert not video.LOGGED_IN

    # Test safari course constructor
    course = SafariCourseIE('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    assert course.IE_NAME == 'safari:course'
    assert course.IE_DESC == 'safaribooksonline.com online courses'
    assert not course.LOGG

# Generated at 2022-06-14 17:03:42.666737
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert re.match(SafariApiIE._VALID_URL, 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html')

# Generated at 2022-06-14 17:03:44.040107
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    print("pytest safaribooksonline.py")
    assert SafariApiIE()

# Generated at 2022-06-14 17:03:55.403034
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    """ Test class SafariApiIE. """

    # Test extractor class SafariApiIE
    test_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    extractor = SafariApiIE(SafariBaseIE)
    assert extractor._match_id('https://www.safaribooksonline.com/api/v1/book/9781449396459') == '9781449396459'
    assert extractor._match_id('https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html') == '9781449396459/chapter/part00.html'

    # Test SafariApiIE.suitable

# Generated at 2022-06-14 17:04:01.336762
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    test_cases = (SafariIE, SafariApiIE)
    for test_case in test_cases:
        assert isinstance(SafariCourseIE(), test_case)
        # Ensure the test is correct
        assert issubclass(test_case, SafariCourseIE)
        # Ensure that class SafariCourseIE is not being modified (eg. by
        # adding a second base class)
        assert SafariCourseIE.__bases__ == (SafariBaseIE,)

# Generated at 2022-06-14 17:04:02.290453
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()

# Generated at 2022-06-14 17:04:07.553921
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    SafariIE().suitable(url)