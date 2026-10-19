

# Generated at 2022-06-14 16:45:34.256165
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    script = 'var lesson = {"course_id": "3","course_name": "Test Course","course_image_url": "","course_url": "https://linuxacademy.com/test/test","lesson_id": "4","lesson_name": "test","lesson_slug": "test","lesson_url": "https://linuxacademy.com/test/test","lesson_image_url": "","lesson_type": "video","formats": [],};'
    re_test = re.search(r'window\.lesson\s*=\s*({.+?})\s*;', script)
    assert re_test

# Generated at 2022-06-14 16:45:43.440073
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Testing module as a whole
    # Youtube does not allow invoking a request without supplying required parameters
    assert LinuxAcademyIE.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')

    # Testing unit of the module
    assert LinuxAcademyIE._VALID_URL != None
    assert LinuxAcademyIE._AUTHORIZE_URL != None
    assert LinuxAcademyIE._ORIGIN_URL != None
    assert LinuxAcademyIE._CLIENT_ID != None
    assert LinuxAcademyIE._NETRC_MACHINE != None

# Generated at 2022-06-14 16:45:44.447404
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:45.957529
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:45:47.078565
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert isinstance(LinuxAcademyIE({})._login(), None)

# Generated at 2022-06-14 16:45:48.288059
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'linuxacademy'

# Generated at 2022-06-14 16:45:50.633118
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    crawler = LinuxAcademyIE()
    assert crawler.__class__.__name__ == 'LinuxAcademyIE'

# get name of class LinuxAcademyIE

# Generated at 2022-06-14 16:46:01.677731
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()
    assert obj.get_real_url("https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2") == "https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2"
    assert obj.get_real_url("https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2/module/675") == "https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2"
    assert obj.get_real_url("https://linuxacademy.com/cp/modules/view/id/154") == "https://linuxacademy.com/cp/modules/view/id/154"

# Generated at 2022-06-14 16:46:03.039066
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'



# Generated at 2022-06-14 16:46:06.489695
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        # Create a LinuxAcademyIE instance and run _login method
        l = LinuxAcademyIE()
        l._login()
    except Exception as e:
        print("Login method of class LinuxAcademyIE failed with exception : \"%s\"" % e)
        raise e

# Generated at 2022-06-14 16:46:26.749256
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    testclass = LinuxAcademyIE('LinuxAcademy')
    assert (testclass.IE_NAME == 'LinuxAcademy')

# Generated at 2022-06-14 16:46:33.040740
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    import sys
    sys.path.append('.')
    from youtube_dl.extractor import linuxacademy

    print(linuxacademy.LinuxAcademyIE)
    info_dict = linuxacademy.LinuxAcademyIE()._real_extract("https://www.linuxacademy.com/cp/modules/view/id/154")
    print(info_dict)
    #assert(info_dict.get('id') == '154')
    #assert(info_dict.get('title') == 'AWS Certified Cloud Practitioner')
    #assert(info_dict.get('duration') == 28835)
    #assert(info_dict.get('description') == 'AWS Certified Cloud Practitioner')


# Generated at 2022-06-14 16:46:33.900976
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()
    print(obj)

# Generated at 2022-06-14 16:46:39.476696
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()
    assert instance.IE_NAME == 'linuxacademy'
    assert instance._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''
    assert instance._TESTS[0]['url'] == 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'

# Generated at 2022-06-14 16:46:49.155162
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy_ie = LinuxAcademyIE('')

    assert linux_academy_ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''


# Generated at 2022-06-14 16:46:52.616444
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .test_linuxacademy import test_info_dict
    ie = LinuxAcademyIE()
    assert LinuxAcademyIE.ie_key() in ie.info_extractors

# Generated at 2022-06-14 16:46:54.857585
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    class_ = LinuxAcademyIE('linuxacademy', {}, {})
    class_._login()

# Generated at 2022-06-14 16:47:04.994782
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        from Crypto.Cipher import AES
    except ImportError:
        AES = None
    from .common import InfoExtractor
    from ..utils import compat_urllib_request
    import base64
    import hashlib
    import hmac
    import json
    import os
    import re
    import unittest
    import urlparse

    def get_real_locations(url):
        base_url = 'https://login.linuxacademy.com/authorize/callback'

        class MyOpener(compat_urllib_request.OpenerDirector):
            def __init__(self, *args, **kwargs):
                compat_urllib_request.OpenerDirector.__init__(self, *args, **kwargs)

# Generated at 2022-06-14 16:47:07.746553
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy_ie = LinuxAcademyIE()
    assert linux_academy_ie

# Generated at 2022-06-14 16:47:09.230228
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Constructor of class LinuxAcademyIE
    LinuxAcademyIE()

# Generated at 2022-06-14 16:47:43.262802
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()
    assert obj.ie_key() == 'linuxacademy'
    assert obj.IE_NAME == 'linuxacademy'
    assert obj.page_encoding == 'utf-8'
    assert obj._VALID_URL == LinuxAcademyIE._VALID_URL


# Generated at 2022-06-14 16:47:46.131308
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.__class__ == LinuxAcademyIE
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:47:53.656022
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    for ie_cls in (LinuxAcademyIE,):
        ie = ie_cls()
        ie._real_initialize()
        assert ie._login() is None
        url = 'https://linuxacademy.com/cp/modules/view/id/154'
        info_dict = ie._real_extract(url)
        assert(info_dict.get('id') == '154')
        assert(info_dict.get('title') == 'AWS Certified Cloud Practitioner')
        assert(info_dict.get('duration') == 28835)
        assert(len(info_dict.get('entries')) == 41)

# Generated at 2022-06-14 16:48:02.487839
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url_str = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    video_id = '7971-2'
    video_title = 'What Is Data Science'
    video_description = '''
        In this introductory lecture, you will learn what is data science and what data scientists do, what are the key skills and roles of data scientists, and why it is a great time to be a data scientist.
    '''
    video_duration = 304


# Generated at 2022-06-14 16:48:04.423401
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'

# Generated at 2022-06-14 16:48:14.838210
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    print(ie._CLIENT_ID)
    print(ie._ORIGIN_URL)
    print(ie._NETRC_MACHINE)

if __name__ == '__main__':
    # test LinuxAcademyIE()
    test_LinuxAcademyIE()
    # LinuxAcademyIE()._real_extract(url)
    # import doctest
    # doctest.testmod()

# Generated at 2022-06-14 16:48:16.697524
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE is not None

if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:48:20.158466
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if __name__ == '__main__':
        LinuxAcademyIE()

# Generated at 2022-06-14 16:48:31.160672
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    import logging
    import unittest
    import unittest.mock
    from youtube_dl.utils import youtube_dl_logger

    class LoggerMock(object):
        def __init__(self, level):
            self._level = level
            self._msg = None

        def setLevel(self, level):
            self._level = level

        def getEffectiveLevel(self):
            return self._level

        def debug(self, msg):
            self._msg = msg

        def isEnabledFor(self, level):
            return level >= self._level

    # Should not raise an error
    LinuxAcademyIE()._login()
    # Should raise an error

# Generated at 2022-06-14 16:48:43.260808
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:49:09.503407
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    if ie:
        # We only instantiate the class in order to call login code.
        ie._login()

# Generated at 2022-06-14 16:49:12.614753
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ies = []
    ies.append(LinuxAcademyIE())
    for ie in ies:
        ie.extract(ie.url)

if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:49:16.994159
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()
    assert instance._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert instance._ORIGIN_URL == 'https://linuxacademy.com'
    assert instance._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert instance._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:49:17.935465
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:49:26.565933
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:49:27.929162
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE('test')
    instance.test()

test_LinuxAcademyIE()

# Generated at 2022-06-14 16:49:32.154698
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    i = LinuxAcademyIE()
    assert LinuxAcademyIE._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert LinuxAcademyIE._NETRC_MACHINE == 'linuxacademy'
    assert LinuxAcademyIE._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert LinuxAcademyIE._ORIGIN_URL == 'https://linuxacademy.com'

# Generated at 2022-06-14 16:49:32.801291
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    x = LinuxAcademyIE()

# Generated at 2022-06-14 16:49:33.597128
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_instance = LinuxAcademyIE()
    assert test_instance

# Generated at 2022-06-14 16:49:40.272931
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    allowed_to_run = False
    try:
        import requests_cache
    except ImportError:
        pass
    else:
        requests_cache.install_cache()
        allowed_to_run = True

    if allowed_to_run:

        # Load auth info
        ie = LinuxAcademyIE()
        ie._login()

        # Test basic construction of object
        ie = LinuxAcademyIE()
        assert isinstance(ie, InfoExtractor)

        # Test basic video extraction
        ie = LinuxAcademyIE()
        entry = ie.extract('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
        assert entry.get('id') == '1498-2'

# Generated at 2022-06-14 16:50:37.058616
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE._login()

# Generated at 2022-06-14 16:50:37.830489
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:50:39.117531
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()

# Generated at 2022-06-14 16:50:41.346224
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._login == LinuxAcademyIE._login
    assert ie._real_extract == LinuxAcademyIE._real_extract

# Generated at 2022-06-14 16:50:44.412614
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'
    assert LinuxAcademyIE.ie_key() in LinuxAcademyIE.ies
    assert LinuxAcademyIE.ie_key() in LinuxAcademyIE.working_ies

# Generated at 2022-06-14 16:50:46.214427
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
        youtube_ie = LinuxAcademyIE()

if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:50:52.961790
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/modules/view/id/154'
    ie = LinuxAcademyIE(url)
    assert(ie.url == url)
    assert(ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    ''')
    assert(ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize')

# Generated at 2022-06-14 16:50:59.984015
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({'verbose': True})
    ie = ydl.extract_info('https://linuxacademy.com/cp/modules/view/id/154', download=False)
    # check fields
    assert ie['id'] == '154'
    assert ie['title'] == 'AWS Certified Cloud Practitioner'
    assert ie['description'] == 'md5:a68a299ca9bb98d41cca5abc4d4ce22c'
    assert ie['duration'] == 28835
    assert ie['_type'] == 'playlist'

if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:51:03.856382
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Basic test for YouTubeIE
    """
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.IE_DESC == 'Linux Academy'
    assert ie.VALID_URL == LinuxAcademyIE._VALID_URL
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:51:04.912521
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()


# Generated at 2022-06-14 16:53:02.208084
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert bool(re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154'))
    assert not bool(re.match(ie._VALID_URL, 'https://linuxacademy.com/'))

# Generated at 2022-06-14 16:53:04.710874
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxAcademyIE = LinuxAcademyIE()
    assert linuxAcademyIE._ORIGIN_URL == 'https://linuxacademy.com'

# Generated at 2022-06-14 16:53:09.782280
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.IE_DESC == 'Linux Academy courses'
    assert ie._VALID_URL == 'https?://(?:www\\.)?linuxacademy\\.com/cp/courses/lesson/course/(?P<chapter_id>\\d+)/lesson/(?P<lesson_id>\\d+)'
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:53:20.666784
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    import requests
    from .common import DEFAULT_HEADERS
    from .common import HEADERS as _headers
    from .common import HLS_HEADERS as _hls_headers
    from .common import get_content


# Generated at 2022-06-14 16:53:23.709049
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    mock_data = 's3cr3tT0k3n'
    info_extractor = LinuxAcademyIE(mock_data)
    assert info_extractor.token == mock_data

# Generated at 2022-06-14 16:53:24.447632
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:53:27.425580
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if LinuxAcademyIE:
        return

    class TestIE(LinuxAcademyIE):
        IE_NAME = 'test-linuxacademy'
        _VALID_URL = r'.*'

    ie = TestIE(TestIE.get_testcases()[0])
    assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:53:32.877617
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )'''

# Generated at 2022-06-14 16:53:42.512092
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    parse_duration("PT50M20S")
    parse_duration("PT1H50M20S")
    parse_duration("PT1H")
    parse_duration("PT1M")
    parse_duration("PT1S")
    parse_duration("PT50M20S")
    parse_duration("PT50S")
    parse_duration("PT1M50S")
    parse_duration("PT50M")
    parse_duration("PT50.5M")
    parse_duration("PT50M5.5S")
    parse_duration("PT50M5.55S")
    parse_duration("PT50M5.555S")
    parse_duration("PT50M5.5555S")
    parse_duration("PT50M5.55555S")
    parse_duration("PT50M5.555555S")

# Generated at 2022-06-14 16:53:43.567864
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()