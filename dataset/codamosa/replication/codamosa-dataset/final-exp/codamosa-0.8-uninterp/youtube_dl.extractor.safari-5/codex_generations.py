

# Generated at 2022-06-14 16:55:51.545169
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    def get_sample_url():
        return 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'

    class MockSafariIE(SafariBaseIE):
        _VALID_URL = r'MOCK_URL'

    safari_api = MockSafariIE(MockSafariIE.ie_key())
    assert(safari_api)

# Generated at 2022-06-14 16:55:52.931017
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Creating a SafariIE class object for testing
    ob = SafariIE()



# Generated at 2022-06-14 16:55:53.524597
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:55:56.642098
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    import safari_test as safari
    # set up
    test_class = SafariBaseIE()
    # test
    result = test_class.__class__.__name__
    # assert
    assert result == 'SafariBaseIE'

# Generated at 2022-06-14 16:55:58.143429
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    class SafariEmptyIE(SafariBaseIE):
        pass
    SafariEmptyIE()

# Generated at 2022-06-14 16:56:01.298514
# Unit test for constructor of class SafariIE
def test_SafariIE():
    obj1 = SafariIE()
    assert obj1._NETRC_MACHINE == "safari"
    assert obj1.LOGGED_IN == False


# Generated at 2022-06-14 16:56:04.562142
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari = SafariBaseIE()
    safari.suitable("https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838")

# Generated at 2022-06-14 16:56:07.817561
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    '''
    Test the constructor of class SafariCourseIE.
    '''
    SafariCourseIE()


# Generated at 2022-06-14 16:56:09.578384
# Unit test for constructor of class SafariIE
def test_SafariIE():
    import datetime
    extractor = SafariIE('foo', 'bar', datetime.datetime(2014, 1, 1))
    assert extractor._api_base_url == 'https://learning.oreilly.com/api/v1'
    assert extractor._api_format == 'json'

# Generated at 2022-06-14 16:56:15.973857
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    assert (SafariCourseIE.suitable(url)
            == (False if SafariIE.suitable(url) or SafariApiIE.suitable(url)
                else super(SafariCourseIE, SafariCourseIE).suitable(url)))
    SafariCourseIE(SafariBaseIE)._real_extract(url) == None

# Generated at 2022-06-14 16:56:34.398470
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from .common import HEADRequest
    from ..utils import HEADRequest

    from .common import HEADRequest
    from ..utils import HEADRequest

    from .common import HEADRequest
    from ..utils import HEADRequest

    import json
    import re

    from .common import InfoExtractor
    from ..compat import (
        compat_parse_qs,
        compat_urlparse,
    )
    from ..utils import (
        ExtractorError,
        update_url_query,
    )

    from .common import InfoExtractor
    from ..compat import (
        compat_parse_qs,
        compat_urlparse,
    )
    from ..utils import (
        ExtractorError,
        update_url_query,
    )

    from .common import InfoExtractor

# Generated at 2022-06-14 16:56:38.838297
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert issubclass(SafariCourseIE, InfoExtractor)
    assert issubclass(SafariCourseIE, SafariBaseIE)
    assert issubclass(SafariCourseIE, SafariIE)
    assert issubclass(SafariCourseIE, SafariApiIE)

# Generated at 2022-06-14 16:56:44.602507
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safariIE = SafariIE()
    # testing whether object is instance of SafariBaseIE
    safariBaseIE = SafariBaseIE()
    assert safariIE.__class__ == SafariIE()
    assert safariIE.__class__ != safariBaseIE
    assert safariIE.__class__ != "safariIE"
    assert safariIE.__class__ != "safariBaseIE"


# Generated at 2022-06-14 16:56:49.371837
# Unit test for constructor of class SafariIE
def test_SafariIE():
        TestSafariIE = SafariIE('test')
        TestSafariIE.LOGGED_IN = False
        assert TestSafariIE.LOGGED_IN == False

# Generated at 2022-06-14 16:56:50.019688
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:56:58.362962
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert SafariCourseIE('SafariCourseIE', 'handler.safaribooksonline.com').get_name() == 'safaribooksonline.com'
    assert SafariCourseIE('SafariCourseIE', 'techbus.safaribooksonline.com').get_name() == 'techbus.safaribooksonline.com'
    assert SafariCourseIE('SafariCourseIE', 'learning.oreilly.com').get_name() == 'learning.oreilly.com'
    assert SafariCourseIE('SafariCourseIE', 'www.oreilly.com').get_name() == 'safaribooksonline.com'

# Generated at 2022-06-14 16:56:59.544886
# Unit test for constructor of class SafariIE
def test_SafariIE():
    instance = SafariIE()
    assert isinstance(instance, object)

# Generated at 2022-06-14 16:57:01.840353
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:57:04.684431
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Parameter-less constructor should pass
    # https://github.com/ytdl-org/youtube-dl/issues/18378
    SafariBaseIE()

# Generated at 2022-06-14 16:57:06.833481
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert isinstance(SafariCourseIE(), InfoExtractor)

# Generated at 2022-06-14 16:57:22.943559
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html")

# Generated at 2022-06-14 16:57:35.587600
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE()
    assert ie.LOGGED_IN == False
    assert ie._NETRC_MACHINE == 'safari'
    assert ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert ie._API_FORMAT == 'json'
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'
    assert ie.name == 'safari:api'
    assert ie.ie_key() == 'SafariApi'


# Generated at 2022-06-14 16:57:44.762550
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    x = SafariBaseIE()
    assert x._VALID_URL == '^https?://(?:www\\.)?(?:safaribooksonline|(?:learning\\.)?oreilly)\\.com/(?:library/view/[^/]+/(?P<course_id>(?:(?!/).)+)/(?P<part>(?:(?!\\.html)[^/?#&])+)\\.html|videos/[^/]+/[^/]+/(?P<reference_id>(?:(?!-[^/?#&])[^/?#&])+-[^/?#&]+)|api/v1/book|techbus\\.safaribooksonline\\.com)/.*$'
    assert x._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:57:45.596043
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()._real_initialize()

# Generated at 2022-06-14 16:57:46.901982
# Unit test for constructor of class SafariIE
def test_SafariIE():
    safariIE = SafariIE(SafariBaseIE(),SafariBaseIE._VALID_URL)

# Generated at 2022-06-14 16:57:58.007592
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    with open(os.path.join(os.path.dirname(__file__), 'test_data', 'test_data.json'), 'r') as test_json_file:
        test_json = json.load(test_json_file)
    test_json = test_json['test_json']

    s = SafariBaseIE()
    conn = s._downloader.http.cookies._cookies['learning.oreilly.com']['/']['groot_sessionid'].value
    assert conn.strip() == test_json['cookies']['conn'].strip()
    ks = s._downloader.http.cookies._cookies['learning.oreilly.com']['/']['orm-jwt'].value
    assert ks.strip() == test_json['cookies']['ks'].strip

# Generated at 2022-06-14 16:58:02.716443
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    class Mock(SafariBaseIE):
        """
        Mock fetching the login page and therefore avoiding the
        safaribooksonline login.
        """
        def _real_initialize(self):
            pass

    instance = SafariApiIE()

    assert isinstance(instance, type(SafariApiIE))

# Generated at 2022-06-14 16:58:09.032689
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # The __init__ method of SafariApiIE is being called to test
    # the conditions of ExtractorError, because it is not possible
    # to instantiate SafariApiIE directly
    SafariApiIE(SafariApiIE.ie_key())


# Generated at 2022-06-14 16:58:21.119850
# Unit test for constructor of class SafariBaseIE

# Generated at 2022-06-14 16:58:29.896740
# Unit test for constructor of class SafariIE
def test_SafariIE():
    import requests
    from ..compat import compat_urllib_parse

    with requests.Session() as session:
        safari = SafariIE(session)

# Generated at 2022-06-14 16:59:03.024649
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # This test could fail without network connection
    # The test would fail if the safaribooksonline.com website change its
    # login mechanism to be incompatible with current implementation.
    from .. import core
    i = core.InfoExtractor(SafariBaseIE._VALID_URL)
    assert i
    # assert the _download_json call to be successful
    # The test would fail if the safaribooksonline.com website change its
    # login mechanism to be incompatible with current implementation.
    i.login()

# Generated at 2022-06-14 16:59:05.187628
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safariCourse = SafariCourseIE()
    assert safariCourse != None
    assert safariCourse != "SafariCourseIE()"


# Generated at 2022-06-14 16:59:06.522287
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # Test instantiation of SafariIE class
    SafariIE()



# Generated at 2022-06-14 16:59:10.593187
# Unit test for constructor of class SafariIE
def test_SafariIE():

    new_SafariIE = SafariIE("SafariIE")
    print (new_SafariIE)

test_SafariIE()

# Generated at 2022-06-14 16:59:13.335385
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safaricourseie = SafariCourseIE(SafariCourseIE.ie_key())
    return safaricourseie

# Generated at 2022-06-14 16:59:25.841176
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    try:
        from unittest import mock
    except ImportError:
        import mock
    from . import extractors

    # Mock assertions for InfoExtractor constructor
    with mock.patch.object(extractors.InfoExtractor, '__init__') as m:
        m.return_value = None
        # Check for expected input values to InfoExtractor constructor
        test = SafariApiIE('https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part00.html')
        assert m.called
        c_args, c_kwargs = m.call_args
        assert c_args[1:] == ()  # no positional arguments other than 'self'

# Generated at 2022-06-14 16:59:31.583362
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    course_url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    safari_course_ie = SafariCourseIE(SafariCourseIE.ie_key())
    safari_course_ie.suitable(course_url)
    safari_course_ie._real_initialize()
    safari_course_ie._real_extract(course_url)

# Generated at 2022-06-14 16:59:33.457001
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE()
    assert safari_api_ie.IE_NAME == 'safari:api'

# Generated at 2022-06-14 16:59:34.414521
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE()

# Generated at 2022-06-14 16:59:40.355321
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part03.html'
    course_id = '9781449396459'
    part = 'part03.html'

# Generated at 2022-06-14 17:00:37.372783
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    # Step 1: Create a SafariApiIE object
    api_ie = SafariApiIE()
    # Step 2: Call _real_extract using test video URL
    api_ie._real_extract('http://techbus.safaribooksonline.com/9780134426365')

# Generated at 2022-06-14 17:00:40.346889
# Unit test for constructor of class SafariIE
def test_SafariIE():
    instance = SafariIE()
    assert instance.ie_key() == 'Safari'
    assert instance.ie_name() == 'safari'
    assert instance.ie_desc() == 'safaribooksonline.com online video'


# Generated at 2022-06-14 17:00:52.736162
# Unit test for constructor of class SafariIE

# Generated at 2022-06-14 17:01:02.579469
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    course_url = 'https://learning.oreilly.com/videos/python-programming-language/9780134217314'
    course_id = '9781449396459'
    course_title = 'Learning Processing: A Beginner\'s Guide to Programming Images, Animation, and Interaction, Second Edition'
    login = 'username', 'password'
    expect_url = 'https://www.safaribooksonline.com/library/view/python-programming-language/9780134217314/'

    test_video_id = '9780134217314-PYMC_25_01'

# Generated at 2022-06-14 17:01:05.470774
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE(object)
    assert ie.IE_NAME == 'safari:api'

# Generated at 2022-06-14 17:01:07.499204
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    assert(SafariCourseIE._TESTS[0]['info_dict']['id']=='9780133392838')

# Generated at 2022-06-14 17:01:12.080642
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    # Create object of class SafariCourseIE
    safari_course = SafariCourseIE()
    # Call _real_extract method of class SafariCourseIE
    safari_course._real_extract(url)

# Generated at 2022-06-14 17:01:13.213157
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('username', 'password')._real_initialize()

# Generated at 2022-06-14 17:01:26.033043
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """
    Unit test for the constructor of class SafariBaseIE
    """

    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    mobj = re.match(SafariIE._VALID_URL, url)
    ie = SafariIE()
    video_id = '%s-%s' % (mobj.group('course_id'), mobj.group('part'))
    webpage, urlh = ie._download_webpage_handle(url, video_id)

# Generated at 2022-06-14 17:01:28.693313
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    import os
    import netrc
    try:
        netrc.netrc(os.devnull)
    except OSError:
        # Non existent netrc file
        return
    # This should not raise an error
    ie = SafariBaseIE('')

# Generated at 2022-06-14 17:03:57.477192
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    ie = SafariBaseIE({"username": "foo", "password": "bar"})
    url = "https://www.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838"
    ie.extract(url)

# Generated at 2022-06-14 17:04:02.046381
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    try:
        from .test import get_testcases
        for test in get_testcases(SafariApiIE):
            test.run_test()
            break
        else:
            return 0
    except AttributeError:
        from .test import raise_error_and_return_one
        return raise_error_and_return_one(SafariApiIE, "test_SafariApiIE")

# Generated at 2022-06-14 17:04:03.091435
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    t = SafariBaseIE()
    t._login()

# Generated at 2022-06-14 17:04:05.550048
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safarie = SafariBaseIE()
    safarie._real_initialize()

# Generated at 2022-06-14 17:04:08.764668
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari = SafariBaseIE()
    assert safari._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 17:04:10.095215
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE('Safari', 'safaribooksonline.com online video')

# Generated at 2022-06-14 17:04:11.866285
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from ytdl.extractor.safariextract import SafariBaseIE
    safari = SafariBaseIE()

# Generated at 2022-06-14 17:04:15.772509
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    course_id = '9781449396459'
    SafariCourseIE._real_extract(SafariCourseIE(), url)
    SafariCourseIE._real_extract(SafariCourseIE(), url)
    SafariCourseIE._real_extract(SafariCourseIE(), url)

# Generated at 2022-06-14 17:04:17.759037
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():

    IE = SafariApiIE()
    assert isinstance(IE, SafariBaseIE)

# Generated at 2022-06-14 17:04:29.238072
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()
    assert ie.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html')
    assert ie.suitable('https://www.safaribooksonline.com/library/view/create-a-nodejs/100000006A0210/part00.html')
    assert ie.suitable('https://www.safaribooksonline.com/library/view/learning-path-red/9780134664057/RHCE_Introduction.html')
    assert ie.suitable('https://www.safaribooksonline.com/videos/python-programming-language/9780134217314/9780134217314-PYMC_13_00')