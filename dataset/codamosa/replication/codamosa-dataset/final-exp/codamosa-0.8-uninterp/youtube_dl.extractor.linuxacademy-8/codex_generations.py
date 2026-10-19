

# Generated at 2022-06-14 16:45:32.561296
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
	try:
		assert LinuxAcademyIE.__init__(LinuxAcademyIE, None) == None
	except AssertionError:
		raise AssertionError("Test of constructor of class LinuxAcademyIE: FAILED")
	else:
		print("Test of constructor of class LinuxAcademyIE: PASSED")

# Generated at 2022-06-14 16:45:33.810120
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy = LinuxAcademyIE()

# Generated at 2022-06-14 16:45:36.502417
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    down = LinuxAcademyIE()
    print(down.download_webpage('http://www.linuxacademy.com', None))

# Generated at 2022-06-14 16:45:38.646575
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Should not fail even without parameters.
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:39.577958
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:45:47.606574
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie._VALID_URL == '''(?x)
                            https?://
                                (?:www\.)?linuxacademy\.com/cp/
                                (?:
                                    courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                                    modules/view/id/(?P<course_id>\d+)
                                )
                            '''
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2022-06-14 16:45:48.882701
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    print(LinuxAcademyIE)

# Generated at 2022-06-14 16:45:50.087754
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert isinstance(LinuxAcademyIE(), LinuxAcademyIE)

# Generated at 2022-06-14 16:45:52.225610
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    iae = LinuxAcademyIE()
    assert iae is not None

# Generated at 2022-06-14 16:45:55.222516
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if discover.have_run('test_LinuxAcademyIE'):
        return
    discover.register_event('test_LinuxAcademyIE')
    test = LinuxAcademyIE()
    test.real_initialize()

# Generated at 2022-06-14 16:46:34.742959
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    import unittest
    from youtube_dl.utils import SearchInfoExtractor
    from youtube_dl.extractor import YoutubeIE

    class LinuxAcademyIETest(unittest.TestCase):
        def test_init(self):
            ie = LinuxAcademyIE()
            self.assertTrue(isinstance(ie, SearchInfoExtractor))
            self.assertTrue(isinstance(ie, YoutubeIE))

    LinuxAcademyIETest().test_init()

# Generated at 2022-06-14 16:46:35.900576
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    global LinuxAcademyIE
    # Test abstract class
    LinuxAcademyIE('linuxacademy')

# Generated at 2022-06-14 16:46:36.781218
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:42.337155
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test for constructor of class LinuxAcademyIE."""
    # Test for invalid url
    linuxAcademy = LinuxAcademyIE(
        LinuxAcademyIE.create_ie('LinuxAcademy', 'https://linuxacademy.com/'))
    assert linuxAcademy is None

# Generated at 2022-06-14 16:46:50.994762
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:47:03.034654
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    username = 'username'
    password = 'password'
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    from .test_common import _tst
    from .test_common import _tst_err
    _tst(LInuxAcademyIE())
    _tst_err(LInuxAcademyIE(), username, 'Error password is None')
    _tst_err(LInuxAcademyIE(), None, password, 'Error username is None')
    _tst_err(LInuxAcademyIE(), '', 'Error password is empty')
    _tst_err(LInuxAcademyIE(), '', password, 'Error username is empty')

# Generated at 2022-06-14 16:47:03.910813
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:47:04.733733
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()

# Generated at 2022-06-14 16:47:08.512179
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = "https://linuxacademy.com/cp/modules/view/id/154"
    jd = LinuxAcademyIE()
    jd._real_extract(url)


# Generated at 2022-06-14 16:47:14.312833
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE(None)._CLIENT_ID is not None
    assert LinuxAcademyIE(None)._NETRC_MACHINE is not None
    assert LinuxAcademyIE(None)._ORIGIN_URL is not None
    assert LinuxAcademyIE(None)._AUTHORIZE_URL is not None
    assert LinuxAcademyIE(None)._VALID_URL is not None

# Generated at 2022-06-14 16:48:35.743877
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    constructor = LinuxAcademyIE('LinuxAcademyIE')
    assert isinstance(constructor, LinuxAcademyIE)

# Generated at 2022-06-14 16:48:39.196476
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert(LinuxAcademyIE.ie_key() == 'LinuxAcademy')
    assert(LinuxAcademyIE.ie_key() == 'LinuxAcademy')

# Generated at 2022-06-14 16:48:41.885119
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.login_name == ie._NETRC_MACHINE
    assert ie.login_password == ""
    return

# Generated at 2022-06-14 16:48:44.006969
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert issubclass(LinuxAcademyIE, InfoExtractor)
    assert classmethod(LinuxAcademyIE.ie_key)


# Generated at 2022-06-14 16:48:47.374998
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test constructor of LinuxAcademyIE class"""
    youtube_ie = LinuxAcademyIE()
    # without login
    assert youtube_ie._login is None
    # with login
    youtube_ie = LinuxAcademyIE(username='anyusername', password='anypassword')
    assert youtube_ie._login is not None

# Generated at 2022-06-14 16:48:48.458247
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie=LinuxAcademyIE()
    return

# Generated at 2022-06-14 16:48:59.081778
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:48:59.914402
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()._real_initialize()

# Generated at 2022-06-14 16:49:01.936546
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Create a LinuxAcademyIE instance"""
    LinuxAcademyIE()


if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:49:11.859962
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test constructor of class LinuxAcademyIE"""
    ies = [LinuxAcademyIE]
    # Test regular expressions
    for ie in ies:
        assert ie._VALID_URL != ''
        assert ie._VALID_URL.find('(?P<id>[0-9]+)') != -1
        assert ie._TESTS != []
        assert ie._TESTS[0]['url'] != ''
        assert ie._TESTS[0]['playlist'] == False
    # Test methods
    for ie in ies:
        ie = ie(IE_NAME)
        ie_info = ie.extract('http://www.youtube.com/watch?v=BaW_jenozKc')
        assert ie_info['id'] != ''
    return
# End of test

# Test functions

# Generated at 2022-06-14 16:52:37.021082
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:52:43.599258
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .linuxacademy import (
        LinuxAcademyIE,
    )
    # Test constructor of class LinuxAcademyIE
    ie = LinuxAcademyIE()
    assert 'LinuxAcademyIE' == ie.ie_key()
    assert 'LinuxAcademy' == ie.IE_NAME
    assert 'linuxacademy.com' == ie._NETRC_MACHINE
    assert 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx' == ie._CLIENT_ID
# End of unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:52:45.175077
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Unit test act as a constructor of LinuxAcademyIE
    obj = LinuxAcademyIE()

# Generated at 2022-06-14 16:52:47.069081
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()
    print(obj.get_info('https://linuxacademy.com/cp/modules/view/id/154'))

# Generated at 2022-06-14 16:52:48.884762
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test LinuxAcademyIE class constructor
    test_linuxacademyIE = LinuxAcademyIE('test', '2020-12-25', 'test', 'test', 'test', None)

# Generated at 2022-06-14 16:52:49.695145
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:52:57.426770
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.HOST == 'linuxacademy.com'
    assert ie.DOMAIN == 'linuxacademy.com'
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.VALID_URL == r'https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/\d+/lesson/\d+'

# Generated at 2022-06-14 16:52:58.570755
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:53:00.191629
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # TODO: This unit test needs to be implemented.
    assert False

# Generated at 2022-06-14 16:53:05.354930
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Constructor of class needs to be tested individually
    # otherwise it will use cached info and fail the test
    try:
        LinuxAcademyIE()._login()
    except ExtractorError as e:
        if isinstance(e.cause, compat_HTTPError) and e.cause.code == 401:
            return
        raise
    else:
        raise Exception('LinuxAcademyIE._login didn\'t fail with a 401')
