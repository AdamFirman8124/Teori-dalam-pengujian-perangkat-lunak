

# Generated at 2022-06-14 16:55:45.532141
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE(None)
    assert not ie.LOGGED_IN

# Generated at 2022-06-14 16:55:55.888703
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    course_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    course_id = "9780133392838"

    course_instance = SafariCourseIE(SafariCourseIE.ie_key())
    course_info = course_instance.extract(course_url)

    assert(course_id == course_info.get("id"))
    assert("Hadoop Fundamentals LiveLessons" == course_info.get("title"))
    assert("playlist" == course_info.get("_type"))
    assert("22" == str(len(course_info.get("entries"))))


# Generated at 2022-06-14 16:56:09.100188
# Unit test for constructor of class SafariIE

# Generated at 2022-06-14 16:56:12.747638
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    try:
        # Test the constructor of SafariCourseIE
        ie = SafariCourseIE('http://techbus.safaribooksonline.com/9780134426365')
        validate_ie(ie)
    except Exception:
        pass


# Generated at 2022-06-14 16:56:14.061286
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE({})
    assert ie._login is not None



# Generated at 2022-06-14 16:56:20.890849
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import sys
    import os
    import unittest

    api_ie = SafariApiIE('www.safaribooksonline.com', 'Some title')

    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part01.html'

    api_ie.extract(url)


# Test that the class constructor can be called
test_SafariApiIE()

# Generated at 2022-06-14 16:56:24.931607
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE('http://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    if safari._downloader != None:
        print("Test Success")
    else:
        print("Test failed")




# Generated at 2022-06-14 16:56:25.457362
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariBaseIE()

# Generated at 2022-06-14 16:56:30.589918
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html'
    safari_api_ie = SafariApiIE()
    mobj = re.match(safari_api_ie._VALID_URL, url)
    safari_api_ie._real_extract('https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html')

# Generated at 2022-06-14 16:56:32.193170
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE.suitable(SafariCourseIE._VALID_URL)
    SafariCourseIE(SafariCourseIE._VALID_URL)

# Generated at 2022-06-14 16:56:57.588156
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    inst = SafariCourseIE({})
    verifyClass(IE_KEY, SafariCourseIE)

test_SafariCourseIE()

# Generated at 2022-06-14 16:57:01.687417
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safariBase = SafariBaseIE()
    assert safariBase._NETRC_MACHINE == 'safari'
    assert safariBase._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert safariBase._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safariBase._API_FORMAT == 'json'

# Generated at 2022-06-14 16:57:03.281889
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_ie = SafariBaseIE()

# Generated at 2022-06-14 16:57:13.981195
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from .test_utils import mock
    from .common import ExtractorError
    from .common import compat_http_client

    import os
    import io

    def mock_open(filename, mode, encoding=None):
        if 'r' in mode:
            lines = ['golden_username', 'golden_password']
            if filename == '.netrc':
                lines += ['machine learning.oreilly.com login golden_username password golden_password']
            return io.StringIO('\n'.join(lines))
        elif 'a' in mode:
            return io.BytesIO(b'')
        else:
            raise UnicornifyError

    def mock_raise_HTTPError(HTTPError, code, text, headers, results):
        if code == 401:
            return compat_http_client.UnauthorizedHandler()

# Generated at 2022-06-14 16:57:15.314889
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Verify safari api can be constructed
    try:
        SafariApiIE()
        assert True
    except Exception:
        assert False


# Generated at 2022-06-14 16:57:16.361626
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    inst = SafariCourseIE()
    assert inst.IE_NAME == 'safari:course'

# Generated at 2022-06-14 16:57:20.822390
# Unit test for constructor of class SafariIE
def test_SafariIE():
    path = 'test.txt'

    from .test_common import FakeDownloader
    downloader = FakeDownloader()
    SafariIE(downloader)._login()

    with open(path, 'r') as f:
        text = f.read()

    assert 'chrome-extension://' not in text
    assert '"password":' not in text
    assert '"email":' not in text
    assert '"session"' in text

# Generated at 2022-06-14 16:57:33.851437
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    if not hasattr(SafariBaseIE, '_download_webpage_handle') or not hasattr(SafariBaseIE, '_download_json'):
        raise ImportError("Test is not applicable for legacy youtube-dl")

    # https://gist.github.com/anonymous/1388eccb6d82b6c3b1ef
    # unit test for safaribooksonline e12a5a5a099e8287f2d7d4e4c5e7a213743693e3

    safari = SafariBaseIE()

    # Test _login() before login
    safari._login()
    assert safari.LOGGED_IN is False

    # Test _login() after login
    safari.LOGGED_IN = True
    safari._login()
    assert safari

# Generated at 2022-06-14 16:57:39.207290
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class MockSafariBaseIE(SafariBaseIE):
        def __init__(self, *args, **kwargs):
            super(MockSafariBaseIE, self).__init__(*args, **kwargs)
            self._downloader = None

    assert MockSafariBaseIE(SafariIE.ie_key()).LOGGED_IN is False

# Generated at 2022-06-14 16:57:42.680335
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from .test_utils import make_mocked_request

    safari_api_ie = SafariApiIE()
    safari_api_ie._download_webpage = make_mocked_request('', '{}')
    safari_api_ie._real_initialize()

# Generated at 2022-06-14 16:58:08.783172
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert(SafariIE() != None)

# Unit Test for constructor of class SafariApiIE

# Generated at 2022-06-14 16:58:18.158622
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .test_youtube_dl import FakeYDL
    ydl = FakeYDL()
    s = SafariIE()
    s.add_default_info_extractors()
    s._downloader = ydl
    s.ie_key = 'add_ie_key'

    # Test with no config
    ydl.params['safaribooksonline-username'] = None
    ydl.params['safaribooksonline-password'] = None
    ydl.options.nopassword = None

    assert isinstance(s, SafariIE)

    # Test with empty config
    ydl.params['safaribooksonline-username'] = ''
    ydl.params['safaribooksonline-password'] = ''
    ydl.options.nopassword = None


# Generated at 2022-06-14 16:58:19.224717
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE('SafariBaseIE')

# Generated at 2022-06-14 16:58:20.231162
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    course = SafariApiIE()

# Generated at 2022-06-14 16:58:21.488315
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    course = SafariCourseIE()

# Generated at 2022-06-14 16:58:27.096452
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    course_id = '9781449396459'
    SafariApiIE(SafariApiIE.ie_key())
    resp = SafariApiIE._download_json(SafariApiIE(), url, course_id, 'test', 'test')
    assert(resp['title'] is not None)

# Generated at 2022-06-14 16:58:28.143200
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()


# Generated at 2022-06-14 16:58:29.704550
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Create an instance of class SafariApiIE
    SafariApiIE()

# Generated at 2022-06-14 16:58:33.151445
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE()._VALID_URL == 'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'

# Generated at 2022-06-14 16:58:37.605943
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    constructor = SafariApiIE.ie_key()
    assert constructor == 'Safari:api'
    assert sys.getrefcount(constructor) == 2


# Generated at 2022-06-14 16:59:27.610975
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    e = SafariApiIE('test')
    assert e is not None


# Generated at 2022-06-14 16:59:31.226851
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class testSafariBaseIE(SafariBaseIE):
        _VALID_URL = 'http://safaribooksonline.com/test/'
    testSafariBaseIE(testSafariBaseIE.suitable, 'http://safaribooksonline.com/test/')

# Generated at 2022-06-14 16:59:41.297712
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    '''
    Test case for a constructor of SafariBaseIE class
    '''
    import os
    import shutil
    from ..utils import fake_netrc

    netrc_file_path = fake_netrc()
    home_path = os.path.expanduser(os.path.join('~', '.config', 'youtube-dl'))
    if os.path.exists(home_path):
        shutil.rmtree(home_path)
    try:
        safari_base_ie = SafariBaseIE()
    finally:
        if os.path.exists(home_path):
            shutil.rmtree(home_path)
        os.remove(netrc_file_path)

# Generated at 2022-06-14 16:59:42.392121
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    _ = SafariApiIE

# Generated at 2022-06-14 16:59:52.630374
# Unit test for constructor of class SafariIE
def test_SafariIE():
    course_id = '9780133392838'
    part = 'part00'
    reference_id = '{}-{}'.format(course_id, part)
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/{}/{}.html'.format(
        course_id, part)

    url_info = SafariIE.url_result(
        url,
        reference_id,
        partner_id=SafariIE._PARTNER_ID,
        ui_id=SafariIE._UICONF_ID)

    flashvars = url_info.query['flashvars']

    # Test 'flashvars[referenceId]'
    assert flashvars['referenceId'] == reference_id

    # Test 'flash

# Generated at 2022-06-14 17:00:00.726294
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    base_ie_class = SafariBaseIE
    # Check that `_LOGIN_URL` class attribute is no empty string
    assert len(base_ie_class._LOGIN_URL) > 0
    # Check that `_NETRC_MACHINE` class attribute is no empty string
    assert len(base_ie_class._NETRC_MACHINE) > 0
    # Check that `_API_BASE` class attribute is no empty string
    assert len(base_ie_class._API_BASE) > 0
    # Check that `LOGGED_IN` class attribute is a `bool`
    assert isinstance(base_ie_class.LOGGED_IN, bool)

# Generated at 2022-06-14 17:00:03.431329
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE("test name", "test description")

# Generated at 2022-06-14 17:00:05.872325
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    try:
        SafariApiIE()
    except:
        raise AssertionError("It is expected no errors will be thrown by SafariApiIE()")

# Generated at 2022-06-14 17:00:10.153524
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safariBase = SafariBaseIE()
    assert safariBase._NETRC_MACHINE == 'safari'
    assert safariBase._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safariBase._API_FORMAT == 'json'
    assert safariBase.LOGGED_IN == False

# Generated at 2022-06-14 17:00:12.333735
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE('', '')

# Generated at 2022-06-14 17:02:34.408764
# Unit test for constructor of class SafariIE
def test_SafariIE():
    import unittest
    import re
    import sys


# Generated at 2022-06-14 17:02:38.316233
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE('safari:api')
    example_url = 'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html'
    assert ie._match_id(example_url) == '9780133392838'

# Generated at 2022-06-14 17:02:44.962643
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import os
    path = os.path.abspath(os.path.expanduser('~/Desktop/test_SafariApiIE.out'))
    print("SafariApiIE test. Please check file:", path)
    s = SafariApiIE()

    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    print("url:", url)
    content = s._download_webpage(url)
    with open(path, "w") as f:
        f.write(content)
    print("Done")

# Test SafariApiIE
# test_SafariApiIE()

# Generated at 2022-06-14 17:02:47.340788
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    _SafariBaseIE = SafariBaseIE(SafariIE.IE_NAME)
    assert _SafariBaseIE.LOGGED_IN is False

# Generated at 2022-06-14 17:02:48.834533
# Unit test for constructor of class SafariIE
def test_SafariIE():
    pass


# Generated at 2022-06-14 17:02:50.069495
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE('safari:api')

# Generated at 2022-06-14 17:02:53.490188
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari_ie = SafariIE()
    assert safari_ie.IE_DESC == 'safaribooksonline.com online video'
    assert safari_ie.IE_NAME == 'safari'

# Generated at 2022-06-14 17:03:01.989731
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    _, urlh = SafariBaseIE._download_webpage_handle(
        'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html',
        SafariIE.ie_key(), 'Downloading test page')
    SafariBaseIE._apply_first_set_cookie_header(urlh, 'groot_sessionid')
    SafariBaseIE._apply_first_set_cookie_header(urlh, 'orm-jwt')
    SafariBaseIE._apply_first_set_cookie_header(urlh, 'orm-rt')
    ie = SafariApiIE()

# Generated at 2022-06-14 17:03:04.183051
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert SafariApiIE(SafariBaseIE).ie_key() == 'safari:api'

# Generated at 2022-06-14 17:03:07.383367
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari = SafariIE("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html")