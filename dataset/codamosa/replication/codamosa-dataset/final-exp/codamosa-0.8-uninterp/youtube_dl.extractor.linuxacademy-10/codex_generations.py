

# Generated at 2022-06-14 16:45:27.913154
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from . import LinuxAcademyIE as test_class
    ie = test_class()
    ie.IE_NAME = 'LinuxAcademyIE'
    ie.ie_key()
    ie.ie_key()
    assert ie.num == 1 
    ie.num += 1
    assert ie.num == 2


# Generated at 2022-06-14 16:45:29.973340
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    return LinuxAcademyIE() # pylint: disable=no-value-for-parameter

# Generated at 2022-06-14 16:45:32.608664
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Import here to make sure the class is defined
    from ..classes import extractor_register
    extractor_register.check_constructor(LinuxAcademyIE)

# Generated at 2022-06-14 16:45:35.687252
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    example = LinuxAcademyIE("https://www.linuxacademy.com/cp/modules/view/id/154")
    example.login()
    assert(example._NETRC_MACHINE == "linuxacademy")

# Generated at 2022-06-14 16:45:46.368932
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    x = LinuxAcademyIE()
    assert(x._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize')
    assert(x._ORIGIN_URL == 'https://linuxacademy.com')
    assert(x._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx')
    assert(x._NETRC_MACHINE == 'linuxacademy')
    assert(re.match(x._VALID_URL, 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675') is not None)

# Generated at 2022-06-14 16:45:47.465568
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert 'LinuxAcademy' in LinuxAcademyIE.__name__

# Generated at 2022-06-14 16:45:54.265241
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Unit test for LinuxAcademyIE
    """
    IE = LinuxAcademyIE('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    print(IE._CLIENT_ID)
    assert IE._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    print("Passed test")

# Generated at 2022-06-14 16:45:56.348365
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .test import run_tests
    if not run_tests:
        return

    linuxacademy = LinuxAcademyIE(None)
    assert linuxacademy

# Generated at 2022-06-14 16:46:08.556103
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._VALID_URL == r'(?x)https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|modules/view/id/(?P<course_id>\d+))'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'

# Generated at 2022-06-14 16:46:16.753792
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    '''
        This test case check whether the unit test code for class LinuxAcademyIE
        is correctly working or not.
    '''
    url = 'https://linuxacademy.com/cp/modules/view/id/154'
    info_dict = {
        'id': '154',
        'title': 'AWS Certified Cloud Practitioner',
        'description': 'md5:a68a299ca9bb98d41cca5abc4d4ce22c',
        'duration': 28835,
    }
    return LinuxAcademyIE().suitable(url) == True and LinuxAcademyIE().extract(url)['id'] == info_dict['id']

# Generated at 2022-06-14 16:46:41.238893
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # pylint: disable=protected-access
    assert LinuxAcademyIE._VALID_URL == LinuxAcademyIE._TESTS[0]['url']
    assert LinuxAcademyIE._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert LinuxAcademyIE._NETRC_MACHINE == 'linuxacademy'
    assert LinuxAcademyIE._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert LinuxAcademyIE._ORIGIN_URL == 'https://linuxacademy.com'

# Generated at 2022-06-14 16:46:50.415442
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # test: LinuxAcademyIE has all needed methods and attributes
    assert hasattr(LinuxAcademyIE, 'login')
    assert hasattr(LinuxAcademyIE, '_login')
    assert hasattr(LinuxAcademyIE, '_real_initialize')
    assert hasattr(LinuxAcademyIE, '_real_extract')
    assert hasattr(LinuxAcademyIE, '_AUTHORIZE_URL')
    assert hasattr(LinuxAcademyIE, '_ORIGIN_URL')
    assert hasattr(LinuxAcademyIE, '_CLIENT_ID')
    assert hasattr(LinuxAcademyIE, '_NETRC_MACHINE')
    assert hasattr(LinuxAcademyIE, '_VALID_URL')

    # test: LinuxAcademyIE instance has all needed methods

# Generated at 2022-06-14 16:46:53.996819
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxAcademyIE = LinuxAcademyIE()
    assert linuxAcademyIE.ie_key() == 'LinuxAcademy'


# Generated at 2022-06-14 16:46:57.837823
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    import unittest

    class LinuxAcademyIETest(unittest.TestCase):
        def test_constructor(self):
            IE = LinuxAcademyIE()

    unittest.main()

# Generated at 2022-06-14 16:47:06.542505
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:47:13.672718
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        # Attempt to instantiate class LinuxAcademyIE with url argument
        LinuxAcademyIE(url='https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    except TypeError as e:
        # If the constructor fails, then test passes
        print('PASS: test_LinuxAcademyIE')
        pass
    else:
        # If constructor does not fail, then test fails
        print('FAIL: test_LinuxAcademyIE')

# Generated at 2022-06-14 16:47:15.773519
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.ie_key() == 'LinuxAcademy'

# Generated at 2022-06-14 16:47:26.001768
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_extractor = LinuxAcademyIE()
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    if test_extractor._login():
        webpage = test_extractor._download_webpage(url, None)
        mobj = re.match(test_extractor._VALID_URL, url)
        chapter_id, lecture_id, course_id = mobj.group('chapter_id', 'lesson_id', 'course_id')
        item_id = course_id if course_id else '%s-%s' % (chapter_id, lecture_id)
        test_extractor._real_extract(url)

# Generated at 2022-06-14 16:47:27.148853
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._login() == None

# Generated at 2022-06-14 16:47:33.954884
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if compat_str is not str:
        return
    # Using this class is not allowed right now
    return
    course_url = 'https://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    course_id = '1498-2'
    # Load Linux Academy
    instance = LinuxAcademyIE()
    instance._login()
    # Load course
    info = instance.extract(course_url)
    # Check if course is valid
    assert info['id'] == course_id, 'course id = %s' % (course_id)
    assert info['title'] == 'Course Index', 'course name = %s' % (info['title'])
    assert info['description'] == '', 'course description = %s' % (info['description'])
   

# Generated at 2022-06-14 16:48:15.106608
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()


# Generated at 2022-06-14 16:48:22.457395
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ok = True
    ie = LinuxAcademyIE()
    assert 'Linux Academy' == ie.IE_NAME
    # Unit test for '_VALID_URL'
    urls = (
        'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'https://linuxacademy.com/cp/modules/view/id/154',
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        'https://linuxacademy.com/cp/courses/lesson/course/0/lesson/0/module/675'
    )
    for url in urls:
        result = re.match(ie._VALID_URL, url)

# Generated at 2022-06-14 16:48:25.460084
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = info_extractor('https://linuxacademy.com/cp/modules/view/id/154')
    ie.initialize()
    ie


# Generated at 2022-06-14 16:48:28.708838
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert (isinstance(LinuxAcademyIE(), InfoExtractor))


if __name__ == "__main__":
    # auto run for test
    import sys
    from .test import test
    test(LinuxAcademyIE)

# Generated at 2022-06-14 16:48:32.430715
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    class TestLinuxAcademyIE(LinuxAcademyIE):
        def __init__(self):
            self._NETRC_MACHINE = None
            LinuxAcademyIE.__init__(self)

    ie = TestLinuxAcademyIE()
    assert ie._login() == None

# Generated at 2022-06-14 16:48:33.509115
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:48:36.308201
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    failure = False
    try:
        LinuxAcademyIE()._login()
    except (ImportError, ExtractorError):
        failure = True
    assert(not failure)

# Generated at 2022-06-14 16:48:43.619383
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE(None)
    assert(ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize')
    assert(ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx')
    assert(ie._NETRC_MACHINE == 'linuxacademy')
    assert(ie._ORIGIN_URL == 'https://linuxacademy.com')

# Generated at 2022-06-14 16:48:54.558210
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    lecture_url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    # Course path
    course_test = LinuxAcademyIE()._real_extract(course_url)
    assert course_test['_type'] == 'playlist'
    assert course_test['id'] == '154'
    assert course_test['title'] == 'AWS Certified Cloud Practitioner'
    assert course_test['description'] == 'md5:a68a299ca9bb98d41cca5abc4d4ce22c'
    assert course_test['duration'] == 28835
    assert len(course_test['entries']) == 41
    # Single video

# Generated at 2022-06-14 16:48:56.786842
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.login_required()
    assert ie.login()

# Generated at 2022-06-14 16:50:50.587394
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:50:52.454485
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:50:53.565413
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:51:00.909697
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.name == 'linuxacademy'
    assert ie.VALID_URL == LinuxAcademyIE._VALID_URL
    assert ie.TESTS == LinuxAcademyIE._TESTS
    assert ie.AUTHORIZE_URL == LinuxAcademyIE._AUTHORIZE_URL
    assert ie.ORIGIN_URL == LinuxAcademyIE._ORIGIN_URL
    assert ie.CLIENT_ID == LinuxAcademyIE._CLIENT_ID
    assert ie.NETRC_MACHINE == LinuxAcademyIE._NETRC_MACHINE
    assert ie.login == LinuxAcademyIE._login
    assert ie.EXTENTIONS == ['mp4']

test_LinuxAcademyIE()

# Generated at 2022-06-14 16:51:01.802695
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:51:04.055329
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    info_extractor= LinuxAcademyIE()
    assert(info_extractor.ie_key()=='LinuxAcademy')

# Generated at 2022-06-14 16:51:10.679698
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()._VALID_URL == \
        'https?://(?:www\\.)?linuxacademy\\.com/cp/' \
        '(?:courses/lesson/course/(?P<chapter_id>\\d+)/lesson/(?P<lesson_id>\\d+)|' \
        'modules/view/id/(?P<course_id>\\d+))'

# Generated at 2022-06-14 16:51:16.086220
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = ('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    instance = LinuxAcademyIE()
    # constructie class
    instance.initialize(url)
    print('test the initialize() function')
    # initialize the class with url
    instance.initialize(url)
    # test the constructor, it just open the website and do not try to download anything
    assert instance.course_id is None

# Generated at 2022-06-14 16:51:28.350340
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Constructor test for class LinuxAcademyIE
    """
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.ms_video_format == 'hls'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''
    # Test public variables

# Generated at 2022-06-14 16:51:38.752834
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Note: for testing purposes, one may use the following credentials:
    #       'username': 'test-user@linuxacademy.com',
    #       'password': 'LinuxAcademy',
    if sys.version_info[0] < 3:
        raise Exception('This unit test is not supposed to run under Python 2')

    import _netrc
    import os.path
    from ..utils import (
        sanitize_open,
        sanitize_url,
    )

    def cleanup(netrc_path):
        if os.path.isfile(netrc_path):
            os.remove(netrc_path)
