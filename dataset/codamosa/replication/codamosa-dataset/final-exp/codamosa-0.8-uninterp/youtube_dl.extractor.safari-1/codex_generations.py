

# Generated at 2022-06-14 16:55:44.730353
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE(None)

# Generated at 2022-06-14 16:55:45.868522
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert SafariBaseIE(None)

# Generated at 2022-06-14 16:55:48.630702
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    obj = SafariApiIE()
    assert obj.IE_NAME == "safari:api"


# Generated at 2022-06-14 16:55:51.795126
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE._LOGIN_URL == "https://learning.oreilly.com/accounts/login/"
    assert SafariCourseIE._UICONF_ID == "29375172"

# Generated at 2022-06-14 16:55:52.463029
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:56:00.367875
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # Test case of a URL which is matched by SafariCourseIE
    assert issubclass(SafariCourseIE, InfoExtractor)
    assert SafariCourseIE.suitable(
        'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')

    # Test case of a URL which is suited by SafariCourseIE
    assert not SafariCourseIE.suitable(
        'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    assert not SafariCourseIE.suitable(
        'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html')

# Generated at 2022-06-14 16:56:03.340808
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE(SafariBaseIE())
    assert safari_api_ie != None
    assert True

# Generated at 2022-06-14 16:56:15.243400
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    data = {
        'url': 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part01.html',
        'part': 'part01.html',
        'mobj': re.match(SafariApiIE._VALID_URL, 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part01.html'),
        'course_id': '9781449396459',
        'video_id': '9781449396459/part01.html'
    }
    safari_api_ie = SafariApiIE()
    safari_api_ie._match_id = lambda x: data['course_id']

# Generated at 2022-06-14 16:56:20.138412
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    assert hasattr(SafariApiIE, "suitable")
    assert hasattr(SafariApiIE, "_real_extract")
    assert hasattr(SafariApiIE, "_VALID_URL")
    assert hasattr(SafariApiIE, "_TESTS")


# Generated at 2022-06-14 16:56:21.878639
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safari_course = SafariCourseIE({})
    assert safari_course.IE_NAME == 'safari:course'

# Generated at 2022-06-14 16:56:38.576083
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # test Safari base class extractor
    t = SafariBaseIE()
    assert t._API_FORMAT == 'json'
    assert t._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:56:47.033156
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    test_cases = {
        'http://techbus.safaribooksonline.com/9780134426365': 'SafariCourseIE',
        'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json': 'SafariApiIE',
        'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html': 'SafariIE'
    }
    for url, ie in test_cases.items():
        inst = SafariIE._build_video_ie(url)
        assert inst.IE_NAME == ie

# Generated at 2022-06-14 16:56:57.892882
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # test 1
    url = "https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html"
    # extractor = SafariApiIE()
    # extractor._real_extract(url)
    # print extractor.url_result("https://www.safaribooksonline.com/library/view/python-crash-course/9781491919521/part00.html", "Safari")
    # extractor.url_result("https://www.safaribooksonline.com/library/view/python-crash-course/9781491919521/part00.html", "Safari")
    # extractor.url_result("https://www.safaribooksonline.com/library/view/python-crash-

# Generated at 2022-06-14 16:56:58.787106
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    import safaribooksonline

# Generated at 2022-06-14 16:56:59.929808
# Unit test for constructor of class SafariIE
def test_SafariIE():
    instance = SafariIE(None)

    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:57:02.632317
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # constructor of class SafariCourseIE
    SafariCourseIE()

# Generated at 2022-06-14 16:57:13.589552
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from .common import HEADRequest
    from ..utils import HEADRequestHandler
    from ..compat import urllib_error
    from ..utils import compat_urllib_request
    import time
    import socket

    with \
        HEADRequestHandler(HEADRequest) as handler, \
        compat_urllib_request.build_opener(handler) as opener, \
        compat_urllib_request.install_opener(opener), \
        handler.test_serve():
        # Test for safari course
        safari_course = SafariBaseIE()
        safari_course._login()
        assert not safari_course.LOGGED_IN
        # Test for safari api
        safari_api = SafariBaseIE()
        safari_api._login()
        assert not safari_api.LOGGED_IN

# Generated at 2022-06-14 16:57:14.265470
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    assert SafariBaseIE()


# Generated at 2022-06-14 16:57:16.255623
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE()
    result = False
    try:
        # if __init__ of class SafariIE was successfull returns True
        result = safari.LOGGED_IN
    except:
        pass
    assert result

# Generated at 2022-06-14 16:57:22.302555
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    SafariCourseIE._TESTS[0]['url'] = url
    ie = SafariCourseIE()
    assert ie._real_extract('https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part01.html')
    assert ie._real_extract('https://www.safaribooksonline.com/api/v1/book/9781449396459/chaptercontent/part01.html')
    assert ie._real_extract('https://www.safaribooksonline.com/api/v1/book/9781449396459/')
    assert ie._real_extract

# Generated at 2022-06-14 16:57:49.370891
# Unit test for constructor of class SafariIE
def test_SafariIE():
    try:
        course = SafariCourseIE()
        course.suitable('foo')  # raises RuntimeError
    except RuntimeError as e:
        if e.args[0] != 'No Suitable IE found for the given URL':
            raise

# Generated at 2022-06-14 16:57:52.327923
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_01')

# Generated at 2022-06-14 16:58:00.248818
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safaribase = SafariIE()
    assert 'safari' == safaribase.IE_NAME
    assert 'safaribooksonline.com online video' == safaribase.IE_DESC
    assert safaribase.IE_DESC == SafariIE.ie_key()
    assert safaribase._VALID_URL
    assert safaribase._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert safaribase._NETRC_MACHINE == 'safari'
    assert safaribase._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safaribase._API_FORMAT == 'json'
    assert safaribase.LOGGED_IN == False
    assert safaribase._search_

# Generated at 2022-06-14 16:58:03.841255
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    test_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    SafariApiIE(SafariApiIE.suitable, test_url)

# Generated at 2022-06-14 16:58:07.106564
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    """Test SafariCourseIE constructor."""
    # SafariCourseIE constructor should not raise an exception.
    SafariCourseIE()

# Generated at 2022-06-14 16:58:11.011616
# Unit test for constructor of class SafariIE
def test_SafariIE():
    try:
        SafariIE()
    except Exception as e:
        assert False, "Exception " + str(e) + " thrown"
        return
    assert True, "No exception thrown"


# Generated at 2022-06-14 16:58:13.926860
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE()
    assert isinstance(safari, SafariIE)

if __name__ == '__main__':
    test_SafariIE()

# Generated at 2022-06-14 16:58:24.962559
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # This assert fails
    assert SafariCourseIE._VALID_URL == r'''(?x)
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
    # This assert passes

# Generated at 2022-06-14 16:58:29.090005
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838'
    c = SafariCourseIE(url)
    assert 'SafariBaseIE' in str(c)

# Generated at 2022-06-14 16:58:34.117655
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE._VALID_URL == (
        'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/'
        '(?:library/view/[^/]+|api/v1/book|videos/[^/]+)/(?P<id>[^/]+)')

# Generated at 2022-06-14 16:59:25.895981
# Unit test for constructor of class SafariIE
def test_SafariIE():
    e = SafariIE()

# Generated at 2022-06-14 16:59:27.910271
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safariapiie = SafariApiIE('test');
    assert safariapiie is not None

# Generated at 2022-06-14 16:59:31.507043
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    actual_ret = SafariApiIE()
    expected_ret = SafariApiIE(url)
    assert actual_ret == expected_ret

# Generated at 2022-06-14 16:59:40.419521
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE()
    assert safari._VALID_URL == 'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/(?:library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?#&]+)\.html|videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?#&]+))'
    assert safari._PARTNER_ID == '1926081'
    assert safari._UICONF_ID == '29375172'

# Generated at 2022-06-14 16:59:45.694253
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    """
    Tests for constructor of class SafariApiIE
    """
    id = '9781449396459'
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    result = SafariApiIE._build_url(id)
    assert result == url


# Generated at 2022-06-14 16:59:47.239052
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    assert ie.IE_NAME == 'safari:api'



# Generated at 2022-06-14 16:59:57.039596
# Unit test for constructor of class SafariIE
def test_SafariIE():
    args = ['']
    kwargs = {'username': 'foo', 'password': 'bar'}

    get_extractor_kwargs = lambda: {'username': 'foo', 'password': 'bar'}

    class TestSafariIE(SafariIE):
        def __init__(self, *args, **kwargs):
            super(TestSafariIE, self).__init__(*args, **kwargs)

            self.get_extractor_kwargs = get_extractor_kwargs

    inst = TestSafariIE(*args, **kwargs)

    assert inst._get_login_info() == (
        'foo', 'bar', 'https://learning.oreilly.com/accounts/login/')

    assert inst._download_webpage_handle.call_count == 1
    assert inst._d

# Generated at 2022-06-14 16:59:58.866097
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    assert ie.__name__ == 'safari:api'

# Generated at 2022-06-14 17:00:01.670380
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    base_ie = SafariBaseIE('random')
    assert base_ie.IE_NAME == 'safari'
    assert base_ie._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 17:00:05.822029
# Unit test for constructor of class SafariIE
def test_SafariIE():
    assert SafariIE({})._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert SafariIE({})._NETRC_MACHINE == 'safari'


# Generated at 2022-06-14 17:02:26.182652
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari = SafariIE()
    assert safari.LOGGED_IN == False


# Generated at 2022-06-14 17:02:28.086256
# Unit test for constructor of class SafariIE
def test_SafariIE():
    my_constructor = SafariIE()

# Generated at 2022-06-14 17:02:31.496861
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base = SafariBaseIE()
    assert safari_base._NETRC_MACHINE == 'safari'
    assert safari_base._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari_base._API_FORMAT == 'json'

# Generated at 2022-06-14 17:02:41.755170
# Unit test for constructor of class SafariIE
def test_SafariIE():
    instance = SafariIE()
    instance._download_json = lambda url, video_id, note, err_note: {
        'session': 'session_key'
    }
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    # Extract video id
    mobj = re.match(instance._VALID_URL, url)
    video_id = '%s-%s' % (mobj.group('course_id'), mobj.group('part'))
    # Fake login
    instance.LOGGED_IN = True


# Generated at 2022-06-14 17:02:47.292698
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE()
    safari_base_ie._download_webpage_handle('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html', None, None)

# Generated at 2022-06-14 17:02:49.759663
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safari_ie = SafariIE()
    assert safari_ie is not None


# Generated at 2022-06-14 17:02:51.435355
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('abc', 'abc')

# Generated at 2022-06-14 17:02:52.686434
# Unit test for constructor of class SafariIE
def test_SafariIE():
    e = SafariIE()
    assert e.LOGGED_IN == False

# Generated at 2022-06-14 17:02:59.021764
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    class_constructed = SafariApiIE(SafariBaseIE._create_getinfo())
    test_url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html'
    assert(class_constructed._VALID_URL == SafariApiIE._VALID_URL)
    assert(class_constructed._real_initialize() is None)
    assert(class_constructed._real_extract(test_url) is not None)

# Generated at 2022-06-14 17:03:07.889125
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Does not work for some reason
    # SafariApiIE.suitable('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')
    # The constructor of the super class of SafariApiIE, InfoExtractor, requires a url argument
    # SafariApiIE()._real_extract('https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')
    # So call the constructor of the super class
    InfoExtractor._real_initialize(SafariApiIE())