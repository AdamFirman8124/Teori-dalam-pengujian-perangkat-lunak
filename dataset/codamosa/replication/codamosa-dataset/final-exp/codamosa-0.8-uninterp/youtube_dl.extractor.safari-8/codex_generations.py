

# Generated at 2022-06-14 16:55:49.702696
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # check if SafariIE can be properly created
    ie = SafariIE()
    # check if necessary functions are implemented
    ie._real_initialize()

# Generated at 2022-06-14 16:55:50.713853
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE('SafariCourse')

# Generated at 2022-06-14 16:55:54.483505
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """Test the SafariBaseIE construction"""
    # test invalid URL
    invalid_url = "http://www.twitter.com"
    ie = SafariBaseIE(invalid_url)
    obj = ie._real_initialize()
    assert obj == None



# Generated at 2022-06-14 16:56:01.440285
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # strings used in assert statements
    assert_course_id = "9780133392838"
    assert_course_title = "Hadoop Fundamentals LiveLessons"
    assert_entries_length = 22

    # instantiate class SafariBaseIE()
    sb_ie = SafariBaseIE()

    # instantiate class SafariApiIE()
    sa_ie = SafariApiIE()

    # instantiate class SafariCourseIE()
    sc_ie = SafariCourseIE()

    # Test course_json id
    course_json = sc_ie._download_json(
        '%s/book/%s/?override_format=%s' % (sc_ie._API_BASE, assert_course_id, sc_ie._API_FORMAT),
        assert_course_id, 'Downloading course JSON')

# Generated at 2022-06-14 16:56:04.297285
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Checking the construction of SafariApiIE
    ie = SafariApiIE()
    assert_equal(ie.IE_NAME, 'safari:api')

# Generated at 2022-06-14 16:56:06.006503
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    instance = SafariBaseIE()
    assert isinstance(instance, SafariBaseIE)

# Generated at 2022-06-14 16:56:14.729469
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()
    assert ie.LOGGED_IN == False
    assert ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert ie._NETRC_MACHINE == 'safari'
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert ie._API_FORMAT == 'json'
    assert ie._PARTNER_ID == '1926081'
    assert ie._UICONF_ID == '29375172'


# Generated at 2022-06-14 16:56:20.702294
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Test SafariCourseIE initialization
    test_course_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    course_url_extractor = SafariCourseIE()
    course_url_extractor.suitable(test_course_url)
    course_url_extractor.extract(test_course_url)

# Generated at 2022-06-14 16:56:21.319699
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()

# Generated at 2022-06-14 16:56:23.314638
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE(None)._make_instance(
        SafariBaseIE,
        'safaribooksonline',
        'safaribooksonline:course',
        'Course name')
    assert ie.ie_key() == 'safari:course'
    assert ie.title == 'Course name'

# Generated at 2022-06-14 16:56:51.405255
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    s = SafariBaseIE()
    s._login()

# Generated at 2022-06-14 16:57:01.034945
# Unit test for constructor of class SafariIE
def test_SafariIE():
    def get_comparison(func):
        def wrapper(*args):
            return getattr(func(*args), '__name__', func(*args))
        return wrapper

    safari = SafariIE.__new__(SafariIE)

    assert get_comparison(safari.suitable)('http://unsuitable_url') == 'False'

    assert get_comparison(safari.suitable)('http://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html') == 'True'

# Generated at 2022-06-14 16:57:06.272449
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    _SafariApiIE = SafariApiIE()
    _SafariApiIE.extract('https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part04.html')

# Generated at 2022-06-14 16:57:10.730197
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class TestSafariBaseIE(SafariBaseIE):
        IE_NAME = 'test'
        _VALID_URL = r'https?://example\.com/(?P<id>.*)'

    assert TestSafariBaseIE(SafariBaseIE.test_handle)._match_id('Example')

# Generated at 2022-06-14 16:57:18.528217
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class SafariBaseIETest(SafariBaseIE):
        _SUBTITLE_URL = 'https://learning.oreilly.com/videos/%s/cfi/%s.vtt'
        _SUBTITLE_EXT = '.vtt'

# Generated at 2022-06-14 16:57:20.547416
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():

    api_ie = SafariApiIE()

    assert api_ie.IE_NAME == 'safari:api'


# Generated at 2022-06-14 16:57:31.177604
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    import sys
    import os
    import re
    import json
    from .common import InfoExtractor
    from ..compat import (
        compat_parse_qs,
        compat_urlparse,
    )
    from ..utils import (
        ExtractorError,
        update_url_query,
    )
    # Test the login functionality of this class
    TestClass = type('TestClass', (SafariBaseIE, ), {})
    b = TestClass('', '')
    b._real_initialize()

if __name__ == '__main__':
    test_SafariBaseIE()

# Generated at 2022-06-14 16:57:36.686090
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE('https://cdnapisec.kaltura.com/html5/html5lib/v2.37.1/mwEmbedFrame.php?wid=_1926081&uiconf_id=29375172&flashvars[referenceId]=0_g8hykfai&showHover=true')
    assert ie.mobj is not None

# Generated at 2022-06-14 16:57:45.484235
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    url = 'https://learning.oreilly.com/videos/javascript-the-good-parts/9780134712755/9780134712755-01_Introduction'
    course_url = 'https://learning.oreilly.com/videos/javascript-the-good-parts'
    urlh = {'url': url, 'status': '401', 'version': 'HTTP/1.1'}
    course_urlh = {'url': course_url, 'status': '200', 'version': 'HTTP/1.1'}

    site = SafariIE('test')
    site.LOGGED_IN = False

    courses = site._download_webpage_handle(
        'https://learning.oreilly.com/courses', None, 'Downloading course page')

# Generated at 2022-06-14 16:57:49.023068
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    webpage_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    webpage_content = '{"id": "9781449396459"}'
    expected_result = {'id': '9781449396459'}
    assert SafariCourseIE._call_api(webpage_url, webpage_content) == expected_result


# Generated at 2022-06-14 16:58:45.187004
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    class_instance = SafariCourseIE()
    assert SafariBaseIE.suitable(class_instance) is True

# Generated at 2022-06-14 16:58:46.811012
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base = SafariBaseIE()
    assert safari_base is not None

# Generated at 2022-06-14 16:58:51.975572
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    if hasattr(safari,'SafariApiIE'):
        x = safari.SafariApiIE('test name')
        assert(x.ie_key() == 'SafariApi')
        assert(x.ie_name() == 'test name')
        assert(x._API_BASE == 'https://learning.oreilly.com/api/v1')
        assert(x._API_FORMAT == 'json')

# Generated at 2022-06-14 16:58:56.176227
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safari_course_ie = SafariCourseIE()
    safari_course_ie.IE_NAME
    safari_course_ie.IE_DESC
    safari_course_ie._VALID_URL
    safari_course_ie._TESTS

# Generated at 2022-06-14 16:58:59.685146
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')

# Generated at 2022-06-14 16:59:02.108673
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url_not_supported = SafariIE._VALID_URL

    assert(SafariCourseIE.suitable(url_not_supported) == False)

# Generated at 2022-06-14 16:59:03.248462
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ts = SafariBaseIE()
    assert ts is not None

# Generated at 2022-06-14 16:59:04.302027
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    t = SafariBaseIE()
    t._login()

# Generated at 2022-06-14 16:59:05.280714
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariBaseIE().initialize()

# Generated at 2022-06-14 16:59:06.629692
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE(SafariBaseIE._downloader)

# Generated at 2022-06-14 17:01:27.053661
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Test exception for wrong account credentials
    account_credentials = ('', '')
    exc_msg = 'Please provide valid username and password for safari in the format ' + \
        '--username USERNAME --password PASSWORD'
    try:
        SafariBaseIE(account_credentials)
    except ExtractorError as e:
        assert e.args[0] == exc_msg
    else:
        raise Exception('Expected an ExtractorError')

    # Test exception for non-existent machine in netrc
    account_credentials = (None, None)
    exc_msg = 'You must put safari login info in either --username and --password or ' + \
        'in your .netrc file'

# Generated at 2022-06-14 17:01:27.584224
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()

# Generated at 2022-06-14 17:01:29.475922
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert SafariIE(SafariIE.ie_key())._VALID_URL == SafariIE._VALID_URL

# Generated at 2022-06-14 17:01:39.936763
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import unittest
    from .test_html import test_smuggle_url

    def get_testcases(url):
        return [{
            'url': url,
        }]

    class TestSafariApiIE(unittest.TestCase):
        @test_smuggle_url
        def test_smuggle_url(self):
            for test in get_testcases(SafariApiIE._VALID_URL):
                SafariApiIE(test['url'])

        def test_extract_url(self):
            for test in get_testcases(SafariApiIE._VALID_URL):
                self.assertTrue(SafariApiIE.suitable(test['url']))


# Generated at 2022-06-14 17:01:52.598039
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from ..utils import NO_DEFAULT

    safari_base_ie = SafariBaseIE()

    # Test case for _real_initialize:
    safari_base_ie._real_initialize()

    # Test case for _login:
    safari_base_ie._login()

    # Test case for _real_initialize:
    safari_base_ie._real_initialize()

    # Test case for _login:
    safari_base_ie._login()

    # Test case for _real_initialize:
    safari_base_ie._real_initialize()

    # Test case for _login:
    safari_base_ie._login()

    # Test case for _real_initialize:
    safari_base_ie._real_initialize()

    # Test case for _login:
    safari

# Generated at 2022-06-14 17:01:53.453171
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert issubclass(SafariIE, KalturaIE) is True

# Generated at 2022-06-14 17:01:57.327817
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # a non-unicode string for url
    url = "https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json"
    SafariApiIE._real_initialize()
    SafariApiIE._real_extract(url)

# Generated at 2022-06-14 17:02:00.656560
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class test(SafariBaseIE):
        pass
    test()

# Generated at 2022-06-14 17:02:02.362031
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    a = SafariBaseIE()

# Generated at 2022-06-14 17:02:04.293442
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    obj = SafariApiIE()
    assert obj._VALID_URL
    assert obj.IE_NAME

# Generated at 2022-06-14 17:04:49.197446
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert(SafariApiIE(SafariApiIE.ie_key()) is not None)

# Generated at 2022-06-14 17:04:51.039536
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE('SafariBaseIE', 'safaribooksonline.com')

# Generated at 2022-06-14 17:04:55.497714
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # pylint: disable=protected-access
    # Test for the static method _add_ns
    assert SafariIE._add_ns(None, 'test') == 'test'

    # Test for the static method _x
    assert SafariIE._x(SafariIE._add_ns('{http://foo}bar', 'test'), 'y') == 'y'

# Generated at 2022-06-14 17:04:59.100998
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    assert ie.name == 'safari:api'
    assert ie.description == 'safaribooksonline.com online courses'

# Generated at 2022-06-14 17:05:07.351232
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
                            )
                    '''
    assert safari_ie._T

# Generated at 2022-06-14 17:05:09.793648
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()
    assert ie.LOGGED_IN is False # pylint: disable=E1103

# Generated at 2022-06-14 17:05:10.597934
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('', '')

# Generated at 2022-06-14 17:05:20.370443
# Unit test for constructor of class SafariBaseIE

# Generated at 2022-06-14 17:05:21.822531
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """
    Test class SafariBaseIE construction.
    """
    instance = SafariBaseIE('username', 'password')


# Generated at 2022-06-14 17:05:32.446332
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    try:
        type(SafariCourseIE)
    except NameError:
        print("Error: Failed to load the SafariCourseIE module")
        raise

    safari_course_ie = SafariCourseIE()
    assert safari_course_ie.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    assert safari_course_ie.suitable('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')
    assert safari_course_ie.suitable('http://techbus.safaribooksonline.com/9780134426365')