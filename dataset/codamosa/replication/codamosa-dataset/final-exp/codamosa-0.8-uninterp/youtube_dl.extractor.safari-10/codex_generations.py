

# Generated at 2022-06-14 16:55:55.392988
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    # we use a valid url and course id
    url = "https://techbus.safaribooksonline.com/9780133392838"
    id = "9780133392838"
    SafariCourseIE(SafariCourseIE.ie_key())
    ie = SafariCourseIE(SafariCourseIE.ie_key())
    assert ie.suitable(url)
    # we assert that the course id is correctly extracted from the url
    assert ie._match_id(url) == id
    #we assert that the playlist count of the extracted course id is correct
    assert len(ie._real_extract(url)['entries']) == 22

# Generated at 2022-06-14 16:55:59.098399
# Unit test for constructor of class SafariIE
def test_SafariIE():
    setattr(SafariIE, '_download_webpage_handle', lambda *args, **kwargs: (None, None))
    setattr(SafariIE, '_download_json_handle', lambda *args, **kwargs: (None, None))

# Generated at 2022-06-14 16:56:01.623005
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari = SafariBaseIE()
    assert safari._API_BASE == 'https://learning.oreilly.com/api/v1'

# Generated at 2022-06-14 16:56:03.603843
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()
    assert ie is not None

# Generated at 2022-06-14 16:56:12.500970
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safaribooksonline_api_url = "https://www.safaribooksonline.com/api/v1/book/9781491977241/chapter/part00.html"
    safari = SafariApiIE()
    try:
        r = safari._real_extract(safaribooksonline_api_url)
        print("Test1: SafariApiIE Unit Test Passed, SafariApiIE._real_extract")
    except:
        print("Test1: Error: SafariApiIE Unit Test Failed.")


# Generated at 2022-06-14 16:56:17.196106
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    i = SafariCourseIE()
    assert i.suitable('http : //www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    assert i.suitable('http://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/')
    assert i.suitable('http://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json')
    assert i.suitable('http://techbus.safaribooksonline.com/9780134426365')

# Generated at 2022-06-14 16:56:26.845946
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    safari_course = SafariCourseIE(url, downloader=None)
    course_id = safari_course._match_id(url)
    course_json = safari_course._download_json(
            '%s/book/%s/?override_format=%s' % (SafariBaseIE._API_BASE, course_id, SafariBaseIE._API_FORMAT),
            course_id, 'Downloading course JSON')
    assert course_json["id"] == "9780133392838"
    assert course_json["title"] == "Hadoop Fundamentals LiveLessons"

# Generated at 2022-06-14 16:56:31.806185
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    filename = "data/safaribooksonline.com/9780133392838/part00.json"
    import os.path
    data = open(os.path.join(os.path.dirname(__file__), filename))
    json_data = json.load(data)
    url = json_data['web_url']
    safari_api_ie = SafariApiIE(SafariIE())
    safari_api_ie.suitable(url)
    safari_api_ie.extract(url)
    return True

#======================================================================

# Generated at 2022-06-14 16:56:43.616754
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from youtube_dl.utils import SearchInfo
    this_class = SafariCourseIE

    # check that it's the right class
    assert this_class.IE_NAME == 'safari:course'
    assert this_class.IE_DESC == 'safaribooksonline.com online courses'

    # exercise __init__()
    this_object = this_class()

    # check that it's the right object
    assert isinstance(this_object, this_class)
    assert this_object.ie_key() == 'Safari'
    assert this_object.suitable('http://example.com/') == False
    assert this_object.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/') == True
   

# Generated at 2022-06-14 16:56:44.155765
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    course_ie = SafariCourseIE()

# Generated at 2022-06-14 16:57:09.793404
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    SafariBaseIE()

# Generated at 2022-06-14 16:57:15.705971
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .test_search import TestSearchIE
    from .test_youtube import TestYoutubeIE
    from .test_kaltura import TestKalturaIE

    for ie_class in [SafariIE, SafariApiIE, SafariCourseIE]:
        ie_instance = ie_class()

        for class_2 in [TestSearchIE, TestYoutubeIE, TestKalturaIE]:
            yield (ie_instance.suitable, class_2.suitable)
            yield (ie_instance.suitable, class_2.suitable)

# Generated at 2022-06-14 16:57:17.067769
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    c = SafariCourseIE()
    c._real_initialize()
    assert c.LOGGED_IN == False


# Generated at 2022-06-14 16:57:18.257443
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    r = SafariApiIE('safari')
    assert(r!=None)


# Generated at 2022-06-14 16:57:30.747019
# Unit test for constructor of class SafariIE
def test_SafariIE():
    uic = '29375172'
    rid = '11914443'
    key = 'kaltura'
    c_id = '9780134217314'

    inst = SafariIE()
    inst.initialize()

    query = {
        'wid': '_1926081',
        'uiconf_id': uic,
        'flashvars[referenceId]': rid,
    }


# Generated at 2022-06-14 16:57:40.150538
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    from ..utils import opts_json_dumps
    from unittest import TestCase
    import mock

    class SafariBaseIETest(SafariBaseIE, TestCase):
        def test_login(self):
            test_opts = {
                'username': 'foouser',
                'password': 'foopass',
            }
            with mock.patch('os.getenv', return_value=opts_json_dumps(test_opts)):
                super(SafariBaseIETest, self).__init__()
                self.test_login()

    test_safari_base_ie = SafariBaseIETest()
    test_safari_base_ie.test_login()

# Generated at 2022-06-14 16:57:48.091584
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    ie = SafariApiIE('safari:api')
    assert ie._VALID_URL == 'https?://(?:www\\.)?(?:safaribooksonline|(?:learning\\.)?oreilly)\\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\\.html'

    ie = SafariApiIE('safari:api', 'SafariApiIE')
    assert ie._VALID_URL == 'https?://(?:www\\.)?(?:safaribooksonline|(?:learning\\.)?oreilly)\\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\\.html'

# Generated at 2022-06-14 16:57:58.104063
# Unit test for constructor of class SafariIE

# Generated at 2022-06-14 16:58:06.692362
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from .common import fake_urlopen
    with fake_urlopen('') as (urlopen_mock, mock_response):
        SafariCourseIE()._real_extract('http://techbus.safaribooksonline.com/9780134426365')
    assert urlopen_mock.urls[0] == 'https://api.safaribooksonline.com/v2/course_ids?slugs=9780134426365&verbose=true'
    assert urlopen_mock.urls[1] == 'https://api.safaribooksonline.com/v2/courses/9780134426365?verbose=true'

# Generated at 2022-06-14 16:58:10.566126
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    SafariCourseIE('safari:course').suitable('https://www.safaribooksonline.com/library/view/drupal-for-designers/9780321767365/')


# Generated at 2022-06-14 16:59:04.428693
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    import pytest

    # dummy url
    url = 'https://dummyurl.com'

    # initialize object
    safari = SafariCourseIE(pytest.DummyIE())

    # no url

# Generated at 2022-06-14 16:59:06.875018
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # If signature of constructor of class SafariIE changes, this test will fail
    assert  'safaribooksonline.com online video' == SafariIE.IE_DESC

# Generated at 2022-06-14 16:59:18.944240
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safariBaseInstance = SafariBaseIE()
    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
    mobj = re.match(safariBaseInstance._VALID_URL, url)
    course_id = mobj.group('id')
    chapterUrl = 'https://www.safaribooksonline.com/api/v1/book/' + course_id + '/chapter/part00.html'
    
    safariApiInstance = SafariApiIE(safariBaseInstance)
    part = safariApiInstance._download_json(chapterUrl, '%s/%s' % (course_id, 'part00'), 'Downloading part JSON')

# Generated at 2022-06-14 16:59:29.125862
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from ydl.utils import make_HTTPS_handler
    from ydl.compat import urlopen

    url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/chapter/part02.html'
    handler = make_HTTPS_handler(False)
    html = urlopen(url, timeout=10, cafile=handler.get_ca_certs()).read()

    expected = b'<html>\n<head>\n<meta http-equiv="refresh" content="0; URL=https://learning.oreilly.com/videos/learning-path-red/9780134664057/9780134664057-00_SeriesIntro"></head>\n<body></body></html>'
    assert expected in html

# Generated at 2022-06-14 16:59:31.387024
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    s = SafariCourseIE('a', 'b', 'c')
    assert s.LOGGED_IN == False
    s._login()
    assert s.LOGGED_IN == True

# Generated at 2022-06-14 16:59:34.397098
# Unit test for constructor of class SafariIE
def test_SafariIE():
    class TestSafariIE(SafariIE):
        def _real_initialize(self):
            pass

        def _login(self):
            pass

    test_SafariIE()._initialize()

# Generated at 2022-06-14 16:59:35.430414
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    SafariApiIE()


# Generated at 2022-06-14 16:59:35.982899
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    pass

# Generated at 2022-06-14 16:59:37.203290
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safaricourse_ie = SafariCourseIE()
    assert safaricourse_ie is not None

# Generated at 2022-06-14 16:59:47.675191
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # Test constructor arguments
    SafariBaseIE(SafariIE(), 'url')
    SafariBaseIE(SafariIE(), 'url', 'video_id')
    SafariBaseIE(SafariIE(), 'url', 'video_id', {'key': 'value'})
    SafariBaseIE(SafariIE(), 'url', 'video_id', {'key': 'value'}, 'note')
    # Test constructor with safari:api
    SafariBaseIE(SafariApiIE(), 'url')
    SafariBaseIE(SafariApiIE(), 'url', 'video_id')
    SafariBaseIE(SafariApiIE(), 'url', 'video_id', {'key': 'value'})

# Generated at 2022-06-14 17:00:55.595277
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    msgs = []
    def msg_cb(msg):
        msgs.append(msg)
    from inspect import getmembers
    from .common import ie_key
    from ..compat import urljoin
    for name, cls in getmembers(SafariBaseIE, lambda m: getattr(m, 'IE_NAME', None)):
        ie = cls()
        safari_ie_name = ie.IE_NAME
        if not safari_ie_name.startswith(ie_key('safari')):
            continue
        safari_ie_key = ie_key(safari_ie_name)
        # Skip if not suitable
        if not ie.suitable('http://techbus.safaribooksonline.com/9781449363374'):
            continue
        # Check info_dict attribute
       

# Generated at 2022-06-14 17:00:56.664603
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    s = SafariCourseIE()

# Generated at 2022-06-14 17:01:03.031193
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    from .common import get_testdata_file
    with open(get_testdata_file('Hadoop Fundamentals LiveLessons.json')) as f:
        course_json = json.load(f)
    assert SafariCourseIE(None)._real_extract(
        'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/',
        course_json)

# Generated at 2022-06-14 17:01:05.698094
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()
    assert ie.__class__.__name__ == 'SafariIE'

# Generated at 2022-06-14 17:01:14.694159
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    safari_api_ie = SafariApiIE()
    assert safari_api_ie._VALID_URL == r'https?://(?:www\.)?(?:safaribooksonline|(?:learning\.)?oreilly)\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\.html'
    assert safari_api_ie.IE_DESC == 'safaribooksonline.com online courses'
    assert safari_api_ie.IE_NAME == 'safari:api'
    assert safari_api_ie.LOGGED_IN == False

# Generated at 2022-06-14 17:01:23.187173
# Unit test for constructor of class SafariIE
def test_SafariIE():
    # this is used to test if the given SafariIE URL is in correct format of a URL
    # if given URL is in correct format then it will return True, otherwise it will return False
    try:
        assert SafariIE._VALID_URL == re.compile(SafariIE._VALID_URL)
    except TypeError:
        assert False, 'SafariIE._VALID_URL cannot compile to regular expression!'

test_SafariIE()

# Generated at 2022-06-14 17:01:28.903217
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    safari_base_ie = SafariBaseIE()
    assert safari_base_ie._LOGIN_URL == 'https://learning.oreilly.com/accounts/login/'
    assert safari_base_ie._NETRC_MACHINE == 'safari'
    assert safari_base_ie._API_BASE == 'https://learning.oreilly.com/api/v1'
    assert safari_base_ie._API_FORMAT == 'json'
    assert safari_base_ie.LOGGED_IN == False


# Generated at 2022-06-14 17:01:29.610026
# Unit test for constructor of class SafariCourseIE
def test_SafariCourseIE():
    safariCrsIE = SafariCourseIE()

# Generated at 2022-06-14 17:01:36.638624
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    info_extractors = [
        SafariApiIE.ie_key(),
        SafariBaseIE.ie_key(),
        SafariCourseIE.ie_key(),
        SafariIE.ie_key()
    ]

    for ie in info_extractors:
        ie = globals()[ie + 'IE']
        ie_obj = ie(info_extractors=info_extractors)
        assert ie_obj._downloader.params.get('noplaylist') is True

# Generated at 2022-06-14 17:01:38.329027
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE()
    assert ie.__class__.__name__ == "SafariIE"

# Generated at 2022-06-14 17:04:27.431038
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE("https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/00_SeriesIntro.html")
    SafariIE("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html")
    SafariIE("https://learning.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html")
    SafariIE("https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html")

# Generated at 2022-06-14 17:04:35.386101
# Unit test for constructor of class SafariIE
def test_SafariIE():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/part00.html'
    info_dict = {
        'id': '0_qbqx90ic',
        'ext': 'mp4',
        'title': 'Introduction to Hadoop Fundamentals LiveLessons',
        'timestamp': 1437758058,
        'upload_date': '20150724',
        'uploader_id': 'stork',
    }
    obj = SafariIE()
    assert obj._real_extract(url)["title"] == info_dict["title"]

# Generated at 2022-06-14 17:04:38.265572
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    url = 'https://learning.oreilly.com/videos/hadoop-fundamentals-livelessons/9780133392838'
    ie = SafariBaseIE()
    ie.extract(url)

# Generated at 2022-06-14 17:04:47.202989
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    from . import BaseTest

    class TestSafariApiIE(SafariApiIE, BaseTest):
        pass

    course_id = '9780133392838'
    part_id = 'part00'
    course_url = 'https://www.safaribooksonline.com/api/v1/book/%s/chapter/%s.html' % (course_id, part_id)
    kaltura_url = 'https://cdnapisec.kaltura.com/html5/html5lib/v2.37.1/mwEmbedFrame.php?wid=_1926081&uiconf_id=29375172&flashvars[referenceId]=%s-%s' % (course_id, part_id)


# Generated at 2022-06-14 17:04:50.669945
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    """Return an instance of class SafariBaseIE"""
    return SafariBaseIE()


# Generated at 2022-06-14 17:04:51.259056
# Unit test for constructor of class SafariApiIE
def test_SafariApiIE():
    pass

# Generated at 2022-06-14 17:05:01.657017
# Unit test for constructor of class SafariIE
def test_SafariIE():
    ie = SafariIE('http://safaribooksonline.com/test_url')
    assert ie._VALID_URL is not None
    assert ie.IE_NAME is not None
    assert ie.IE_DESC is not None
    assert ie.js_to_json is not None
    assert ie._TESTS is not None
    assert ie._download_webpage is not None
    assert ie._download_json is not None
    assert ie._extract_urls is not None
    assert ie._extract_count is not None
    assert ie._real_extract is not None
    assert ie._real_initialize is not None

    safari_course_obj = SafariCourseIE('http://safaribooksonline.com/test_url')
    assert safari_course_obj._VALID_URL is not None
   

# Generated at 2022-06-14 17:05:03.536371
# Unit test for constructor of class SafariBaseIE
def test_SafariBaseIE():
    # test empty url
    url = ''
    course = SafariBaseIE()
    assert course.suitable(url)



# Generated at 2022-06-14 17:05:04.652670
# Unit test for constructor of class SafariIE
def test_SafariIE():
    SafariIE()

# Generated at 2022-06-14 17:05:09.151570
# Unit test for constructor of class SafariIE
def test_SafariIE():
    from .common import read_test_modules_ids
    ie = SafariIE()
    ie._login()
    patterns = read_test_modules_ids(ie)

    for pattern in patterns:
        result = ie._real_extract(pattern)
        assert result['id'] is not None