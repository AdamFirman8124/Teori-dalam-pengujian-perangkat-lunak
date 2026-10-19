

# Generated at 2022-06-14 16:45:23.732335
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()


if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:45:26.548599
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test if the constructor of LinuxAcademyIE class works."""
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:28.200015
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Unit test for constructor of class LinuxAcademyIE
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:45:35.123873
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    #
    # Test cases
    #
    # Test cases for course page
    course_test_object = {
        'url': 'https://linuxacademy.com/cp/modules/view/id/154',
        'only_matching': True,
    }
    LinuxAcademyIE.ie_key()
    LinuxAcademyIE._real_initialize()
    LinuxAcademyIE._real_extract(course_test_object['url'])
    #
    # Test cases for single video page
    single_video_test_object = {
        'url': 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        'only_matching': True,
    }
    LinuxAcademyIE.ie_key()
   

# Generated at 2022-06-14 16:45:43.964576
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/modules/view/id/220'
    netrc_machine = 'linuxacademy'
    username = 'UNIT_TEST_USERNAME'
    password = 'UNIT_TEST_PASSWORD'
    ie = LinuxAcademyIE()
    ie.login = lambda: ie._login()
    ie.login()
    ie._get_login_info = lambda: (username, password)
    ie._downloader = None
    ie._real_initialize()
    ie._real_extract(url)

# Generated at 2022-06-14 16:45:46.398386
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    
    # Construct an object of class LinuxAcademyIE
    ie = LinuxAcademyIE()

    # Confirm that the object is an instance of the class.
    assert isinstance(ie, LinuxAcademyIE)

# Test the LinuxAcademyIE class
if __name__ == '__main__':

    # Test constructor of class LinuxAcademyIE.
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:45:49.247924
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        username, password = LinuxAcademyIE._get_login_info()
    except ExtractorError:
        username = password = None
    if username is None or password is None:
        raise Exception('Requires Linux Academy account credentials')

    LinuxAcademyIE(None)._login()

# Generated at 2022-06-14 16:46:00.368036
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:46:10.586466
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert LinuxAcademyIE._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert LinuxAcademyIE._ORIGIN_URL == 'https://linuxacademy.com'
    assert LinuxAcademyIE._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert LinuxAcademyIE._NETRC_MACHINE == 'linuxacademy'
    assert hasattr(ie, '_real_initialize')
    assert hasattr(ie, '_login')
    assert hasattr(ie, '_real_extract')

# Generated at 2022-06-14 16:46:11.944960
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE().ie_key()=='LinuxAcademy'

# Generated at 2022-06-14 16:46:45.803585
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    mac = LinuxAcademyIE()
    assert mac.IE_NAME == "linuxacademy"

# Generated at 2022-06-14 16:46:46.819706
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:47.803462
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:48.624442
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('LinuxAcademy')

# Generated at 2022-06-14 16:47:00.796505
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .fake_oembed import FakeOEmbed
    from .test_embed import TestEmbedBase

    class TestLinuxAcademyIE(TestEmbedBase):
        IE = LinuxAcademyIE

        def _test_embed(self, name, expected_title, expected_description, video_id, **kwargs):
            oembed = FakeOEmbed(
                url='https://linuxacademy.com/cp/modules/view/id/%s' % video_id,
                provider_name='linuxacademy',
                provider_url='https://linuxacademy.com')
            super(TestLinuxAcademyIE, self)._test_embed(
                name, expected_title, expected_description, video_id,
                oembed=oembed, **kwargs)

        def test_url(self):
            self

# Generated at 2022-06-14 16:47:05.863544
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:47:08.825953
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    name = ie.IE_NAME
    assert name == 'linuxacademy', 'Expected "linuxacademy". ' + name

# Generated at 2022-06-14 16:47:09.877139
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()


# Generated at 2022-06-14 16:47:11.824012
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:47:22.181382
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy = LinuxAcademyIE()
    assert linux_academy._VALID_URL == r'''(?x)
                        https?://
                            (?:www\.)?linuxacademy\.com/cp/
                            (?:
                                courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                                modules/view/id/(?P<course_id>\d+)
                            )
                        '''
    
    assert linux_academy._ORIGIN_URL == 'https://linuxacademy.com'
    assert linux_academy._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    assert linux_

# Generated at 2022-06-14 16:48:48.386691
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    course_id = "154"
    lecture_id = "7971-2"
    course_url = "https://linuxacademy.com/cp/modules/view/id/154"
    lecture_url = "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675"

    # Testing course url
    mobj = re.match(ie._VALID_URL, course_url)
    assert mobj.group('course_id') == course_id
    mobj = re.match(ie._VALID_URL, lecture_url)
    assert mobj.group('course_id') == None

    # Testing valid urls
    assert ie._VALID_URL == ie.VALID_URL
    assert ie.su

# Generated at 2022-06-14 16:48:52.214182
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # test default constructor
    assert LinuxAcademyIE() is not None
    # test constructor with param
    assert LinuxAcademyIE(LinuxAcademyIE._NETRC_MACHINE) is not None

# Generated at 2022-06-14 16:48:53.222954
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:48:57.565671
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if not test_LinuxAcademyIE.is_call:
        test_LinuxAcademyIE.is_call=True
        test_LinuxAcademyIE.la = LinuxAcademyIE()
    return test_LinuxAcademyIE.la

test_LinuxAcademyIE.is_call = False

# Generated at 2022-06-14 16:49:04.732868
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Constructor
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''

# Generated at 2022-06-14 16:49:07.445156
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        LinuxAcademyIE(None)._login()
    except ExtractorError as e:
        msg = 'requires account credentials'
        assert msg in str(e), 'Mandatory error message not found'

# Generated at 2022-06-14 16:49:15.879677
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:49:18.217130
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .content import openload
    IEObject = openload.OpenloadIE()
    return IEObject


# Generated at 2022-06-14 16:49:20.134501
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        LinuxAcademyIE()
    except Exception:
        assert False


# Generated at 2022-06-14 16:49:22.622461
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Since LinuxAcademyIE is not a test case, we don't have a test for
    # its constructor yet. Test it here.
    LinuxAcademyIE('mocked_name', 'mocked_video_id')

# Generated at 2022-06-14 16:52:33.331046
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    i = LinuxAcademyIE()
    assert i.head != None

if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-14 16:52:34.291493
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:52:35.090277
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    sa = LinuxAcademyIE()

# Generated at 2022-06-14 16:52:35.959786
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()

# Generated at 2022-06-14 16:52:40.658068
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .test_download import test_download
    x = 'https://www.linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    y = test_download(LinuxAcademyIE(), x, skip_verification=True)
    assert y.get('title') is not None


# Generated at 2022-06-14 16:52:41.445179
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:52:42.364378
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:52:49.652636
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.IE_DESC == 'Linux Academy courses'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._VALID_URL == r'(?x)https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)'

# Generated at 2022-06-14 16:52:51.412867
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Try to log in but just skip the process
    ie = LinuxAcademyIE(None)._real_initialize()
    assert ie is not None


# Generated at 2022-06-14 16:52:58.217038
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from . import extractors

    try:
        LinuxAcademyIE()
        assert False, "We should have thrown an exception due to the necessity of having LinuxAcademy account's credentials"
    except EnvironmentError as e:
        assert e.args[0] == "The environment variable YOUTUBE_DL_LINUXACADEMY_USER or YOUTUBE_DL_LINUXACADEMY_PASS is not set"

    extractors.LinuxAcademyIE._login = lambda *args, **kwargs: None
    ie = LinuxAcademyIE()
    assert ie.extractor_key() == 'linuxacademy'