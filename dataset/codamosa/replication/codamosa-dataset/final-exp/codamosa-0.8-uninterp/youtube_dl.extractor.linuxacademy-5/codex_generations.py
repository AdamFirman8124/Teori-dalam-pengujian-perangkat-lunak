

# Generated at 2022-06-14 16:45:27.573786
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:45:28.928009
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:35.837763
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    print("Testing LinuxAcademyIE() class constructor")
    url = "https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2"
    course_info = LinuxAcademyIE()._real_extract(url)
    video_info = course_info['entries'][0]
    video = LinuxAcademyIE()._real_extract(video_info['url'])
    print("Video Title: " + video['title'])
    print("Video Description: " + video['description'])

# Generated at 2022-06-14 16:45:46.404054
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = LinuxAcademyIE()
    assert downloader.ie_key() == 'LinuxAcademy'
    assert downloader.ie_name() == 'LinuxAcademy'
    assert downloader._VALID_URL == 'https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|https?://(?:www\.)?linuxacademy\.com/cp/modules/view/id/(?P<course_id>\d+)'
    assert downloader._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert downloader._ORIGIN_URL == 'https://linuxacademy.com'
    assert downloader._

# Generated at 2022-06-14 16:45:48.728985
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()



# Generated at 2022-06-14 16:45:50.253099
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    object = LinuxAcademyIE()
    assert False, "LinuxAcademyIE: Constructor test"


# Generated at 2022-06-14 16:45:54.505592
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675"
    instance = LinuxAcademyIE()
    instance._real_initialize()
    instance._real_extract(url)

# Generated at 2022-06-14 16:46:04.527527
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE('LinuxAcademy', 'https://www.linuxacademy.com/')
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'

# Generated at 2022-06-14 16:46:06.749569
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:12.146198
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # this test checks if the class instance is initialized correctly
    test_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    ie = LinuxAcademyIE()
    check = ie.suitable(test_url)
    assert check is True



# Generated at 2022-06-14 16:46:52.526326
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_LinuxAcademyIE.LE = LinuxAcademyIE()
    return test_LinuxAcademyIE.LE

# Generated at 2022-06-14 16:47:00.668932
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Create instance of class LinuxAcademyIE with dummy params
    linuxacademy_ie = LinuxAcademyIE(None, {}, 'Linux Academy')
    
    # Create instance of class LinuxAcademyIE
    # with valid values for params
    linuxacademy_ie = LinuxAcademyIE(
        compat_str,
        {'url':'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'},
        'Linux Academy')
    assert True


# Generated at 2022-06-14 16:47:08.180942
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert(ie.IE_NAME == 'linuxacademy')
    assert(ie.IE_DESC == 'Linux Academy')
    assert(ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    ''')
    assert(ie._NETRC_MACHINE == 'linuxacademy')
    assert(ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize')

# Generated at 2022-06-14 16:47:08.743088
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    pass

# Generated at 2022-06-14 16:47:18.938662
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'
    assert LinuxAcademyIE._NETRC_MACHINE == 'linuxacademy'
    assert LinuxAcademyIE._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''

# Generated at 2022-06-14 16:47:28.873927
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    x = LinuxAcademyIE()
    assert (x.ie_key() == 'linuxacademy')
    assert (x.ie_name() == 'linuxacademy')
    assert (x._VALID_URL == "(?x)https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|modules/view/id/(?P<course_id>\d+))")
    assert (x._AUTHORIZE_URL == "https://login.linuxacademy.com/authorize")
    assert (x._ORIGIN_URL == "https://linuxacademy.com")

# Generated at 2022-06-14 16:47:30.591294
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'

# Generated at 2022-06-14 16:47:41.148900
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        import httpretty
        from httpretty import HTTPretty
    except ImportError:
        import unittest
        raise unittest.SkipTest('httpretty is required to run the LinuxAcademyIE test cases')
    from httpretty import httprettified

    @httprettified
    def test_login_works_for_valid_credentials():
        HTTPretty.reset()
        HTTPretty.register_uri(HTTPretty.GET, 'https://login.linuxacademy.com/authorize',
                               body='', status=200, content_type='text/html')

# Generated at 2022-06-14 16:47:42.442765
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert (LinuxAcademyIE(None) is not None)

# Generated at 2022-06-14 16:47:51.784503
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:48:28.094456
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    pass

# Generated at 2022-06-14 16:48:32.518125
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test constructor of class LinuxAcademyIE"""
    # Load the class
    from youtube_dl.extractor import linuxacademy
    ie = linuxacademy.LinuxAcademyIE()
    # Check some properties
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.ie_name() == 'LinuxAcademy'

# Generated at 2022-06-14 16:48:37.150967
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .test import MockIE
    try:
        from .test import get_test_netrc_regex
    except ImportError:
        get_test_netrc_regex = lambda: ''
    assert LinuxAcademyIE._VALID_URL == get_test_netrc_regex()



# Generated at 2022-06-14 16:48:38.742403
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()


# Generated at 2022-06-14 16:48:40.159453
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # test constructor without any parameters
    assert LinuxAcademyIE() is not None

# Generated at 2022-06-14 16:48:42.038985
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE("LinuxAcademyIE")
    assert obj.login_failed

# Generated at 2022-06-14 16:48:45.912155
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test constructor of the class and its superclass
    test_case = LinuxAcademyIE(None)
    assert(test_case != None)
    assert(test_case.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == True)


# Generated at 2022-06-14 16:48:49.311964
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # test initialization of the class and methods in it
    try:
        LinuxAcademyIE(None, {})
    except ExtractorError as e:
        assert 'Please provide your Linux Academy username' in str(e)

# Generated at 2022-06-14 16:48:52.366772
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()


if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:48:55.785993
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
  ie = LinuxAcademyIE("LinuxAcademyIE", "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675", "LinuxAcademyIE", "LinuxAcademyIE")
  return ie


# Generated at 2022-06-14 16:50:59.845434
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.extract(None)['description'] == 'md5:a68a299ca9bb98d41cca5abc4d4ce22c'

# Generated at 2022-06-14 16:51:05.236817
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/modules/view/id/154'
    course = LinuxAcademyIE().extract_info(url)
    assert course['title'] == 'AWS Certified Cloud Practitioner'
    assert course['description'] == 'md5:a68a299ca9bb98d41cca5abc4d4ce22c'
    assert course['duration'] == 28835
    assert course['playlist_count'] == 41

# Generated at 2022-06-14 16:51:10.853819
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        ['https://learning.linuxacademy.com/cdn/secret/linuxacademy.com/course-7971/lesson-2/WhatIsDataScience-hls.m3u8'])

# Generated at 2022-06-14 16:51:12.924802
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    x = LinuxAcademyIE(LinuxAcademyIE.ie_key())
    assert isinstance(x, LinuxAcademyIE)

# Generated at 2022-06-14 16:51:14.503822
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'linuxacademy'


# Generated at 2022-06-14 16:51:23.580890
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if not os.path.exists(os.path.join(os.path.expanduser('~'),'Documents/.netrc')):
        print('Please create netrc file before testing. See: https://github.com/ytdl-org/youtube-dl/blob/master/README.md')
    assert(LinuxAcademyIE.ie_key() == 'LinuxAcademy')

if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:51:33.126691
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:51:33.910651
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:51:36.730372
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    unit_test(function_class=LinuxAcademyIE, function_module='LinuxAcademyIE.py',
              function_title='test_LinuxAcademyIE', function_description='Unit test for constructor of class LinuxAcademyIE')


# Generated at 2022-06-14 16:51:38.824114
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE().extractor_key() == 'LinuxAcademy'