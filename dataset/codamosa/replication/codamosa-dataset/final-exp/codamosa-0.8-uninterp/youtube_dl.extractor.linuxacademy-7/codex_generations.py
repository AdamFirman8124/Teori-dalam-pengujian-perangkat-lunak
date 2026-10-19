

# Generated at 2022-06-14 16:45:33.429774
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
   assert LinuxAcademyIE._VALID_URL != ""
   assert LinuxAcademyIE._TESTS != ""
   assert LinuxAcademyIE._AUTHORIZE_URL != ""
   assert LinuxAcademyIE._ORIGIN_URL != ""
   assert LinuxAcademyIE._CLIENT_ID != ""
   assert LinuxAcademyIE._NETRC_MACHINE != ""

# Generated at 2022-06-14 16:45:34.551453
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'

# Generated at 2022-06-14 16:45:36.741579
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # type: () -> None
    LinuxAcademyIE('username', 'password')

# Generated at 2022-06-14 16:45:38.365514
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:40.286913
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # pylint: disable=protected-access
    assert LinuxAcademyIE._CLIENT_ID

# Generated at 2022-06-14 16:45:40.823302
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:41.868258
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()

# Generated at 2022-06-14 16:45:49.930446
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    import unittest
    from .common import TestCase

    class LinuxAcademyIETest(TestCase):
        def setUp(self):
            self.ie = LinuxAcademyIE
            self.ie._login = lambda *args : None

        def test_constructor(self):
            self.assertIsInstance(
                self.ie,
                type
            )
            self.assertEqual(
                self.ie.ie_key(),
                'LinuxAcademy'
            )
            self.assertEqual(
                self.ie.ie_key(),
                self.ie('').ie_key()
            )
            self.assertEqual(
                self.ie.name(),
                'Linux Academy'
            )

# Generated at 2022-06-14 16:45:51.367802
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()._login()

# Generated at 2022-06-14 16:46:01.924451
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'linuxacademy'
    assert LinuxAcademyIE.ie_key() == LinuxAcademyIE.ie_key()
    assert LinuxAcademyIE._VALID_URL
    assert LinuxAcademyIE._TESTS
    assert LinuxAcademyIE._AUTHORIZE_URL
    assert LinuxAcademyIE._ORIGIN_URL
    assert LinuxAcademyIE._CLIENT_ID
    assert LinuxAcademyIE._NETRC_MACHINE
    assert LinuxAcademyIE._login
    assert LinuxAcademyIE._real_initialize
    assert LinuxAcademyIE._real_extract

# Generated at 2022-06-14 16:46:24.341785
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    u = LinuxAcademyIE()
    assert u.name == "linuxacademy"
    assert u.ie_key() == "linuxacademy"
    assert u.has_login()
    assert u.has_capability("bulk_extraction")
    assert u.has_capability("playlist")
    assert u.has_capability("subtitles")

# Generated at 2022-06-14 16:46:34.975851
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxacademy_ie = LinuxAcademyIE()

    assert(linuxacademy_ie.IE_NAME == 'linuxacademy')
    assert(linuxacademy_ie.IE_DESC == 'Linux Academy')

    assert(linuxacademy_ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize')
    assert(linuxacademy_ie._ORIGIN_URL == 'https://linuxacademy.com')
    assert(linuxacademy_ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx')
    assert(linuxacademy_ie._NETRC_MACHINE == 'linuxacademy')

# Generated at 2022-06-14 16:46:36.225373
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert isinstance(LinuxAcademyIE(), LinuxAcademyIE)


# Generated at 2022-06-14 16:46:39.454597
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    i = LinuxAcademyIE()
    try:
        import netrc
        netrc = netrc.netrc()
        username, _, password = netrc.authenticators(i._NETRC_MACHINE)
    except (IOError, ImportError, TypeError):
        username = None
    i._login(username, password)

# Generated at 2022-06-14 16:46:42.673080
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE._TESTS[0].get("url") == 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'



# Generated at 2022-06-14 16:46:48.470275
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    # raise Exception if the code does not reach a breakpoint
    ie._real_initialize()
    assert(ie._real_extract({
        'url': 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'only_matching': True
    }, '1498-2') == {'id': '1498-2'})

# Generated at 2022-06-14 16:46:53.952228
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test instantiations of the classes that inherit from LinuxAcademyIE
    class TestLinuxAcademyIE(LinuxAcademyIE):
        def _real_initialize(self):
            self.skipTest('Not a real test')

    assert TestLinuxAcademyIE.ie_key() == 'linuxacademy'

# Generated at 2022-06-14 16:47:00.211283
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.__bases__[0].__name__ == 'InfoExtractor'
    assert LinuxAcademyIE.IE_NAME == 'linuxacademy'
    assert LinuxAcademyIE.IE_DESC == 'LinuxAcademy'
    assert LinuxAcademyIE._VALID_URL is not None
    assert LinuxAcademyIE._NETRC_MACHINE is not None

# Generated at 2022-06-14 16:47:01.499799
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('www.linuxacademy.com')

# Generated at 2022-06-14 16:47:02.867441
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert isinstance(LinuxAcademyIE(), InfoExtractor)

# Generated at 2022-06-14 16:48:01.525989
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie=LinuxAcademyIE()
    print(ie.IE_NAME)
    print(ie.SSL_VERIFY)
    print(ie.ages)
    print(ie._downloader)
    print(ie._downloader_download)
    print(ie._downloader.params)
    print(ie._downloader.to_screen)
    print(ie._downloader.params)
    print(ie._downloader.default_outtmpl)
    print(ie._downloader.default_outtmpl)
    print(ie.REQUEST_HEADERS)
    print(ie.params)
    print(ie.params)
    print(ie.params)
    print(ie.params)
    print(ie.working_template)
    print(ie.working_template)
    print(ie.working_template)


# Generated at 2022-06-14 16:48:03.763483
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxacademy_ie = LinuxAcademyIE()
    assert isinstance(linuxacademy_ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:48:04.809875
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()

# Generated at 2022-06-14 16:48:10.247771
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()
    assert hasattr(LinuxAcademyIE, '_login')
    assert hasattr(LinuxAcademyIE, '_real_initialize')
    assert hasattr(LinuxAcademyIE, '_real_extract')

# Generated at 2022-06-14 16:48:19.749044
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxacademy_ie = LinuxAcademyIE()
    assert linuxacademy_ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''
    assert linuxacademy_ie._TESTS[0]['url'] == 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'

# Generated at 2022-06-14 16:48:21.132586
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:48:23.184871
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(InfoExtractor())._login()

# Generated at 2022-06-14 16:48:32.923846
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    test = """
        <script type="text/javascript">
            var authorizationResponse = {
                "state": "state",
                "nonce": "nonce",
                "access_token": "access_token",
                "id_token": "id_token",
                "token_type": "token_type",
                "expires_in": expires_in
            };
        </script>
    """
    ie._search_regex(
        r'authorizationResponse\s*=\s*({.+?})\s*;', test,
        'authorization response')
    test.replace('"state": "state",', '"state": state,')

# Generated at 2022-06-14 16:48:36.632624
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    print("Login test for Linux Academy")
    la_ie = LinuxAcademyIE()
    assert la_ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2022-06-14 16:48:39.813338
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME != ''
    assert ie._VALID_URL != ''
    assert ie.__name__ == 'LinuxAcademy'

# Generated at 2022-06-14 16:50:34.262937
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE([], [])

# Generated at 2022-06-14 16:50:35.334691
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:50:37.697770
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    testIE = LinuxAcademyIE()
    assert testIE._CLIENT_ID == "KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx"

# Generated at 2022-06-14 16:50:38.738209
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:50:41.424063
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try_get_login_info()
    # Test that the constructor detects an invalid login
    test_linux_academy_instance = LinuxAcademyIE()
    test_linux_academy_instance._login()

# Generated at 2022-06-14 16:50:47.741481
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    expected = {
        'id': '7971-2',
        'ext': 'mp4',
        'title': 'What Is Data Science',
        'description': 'md5:c574a3c20607144fb36cb65bdde76c99',
        'duration': 304,
        'timestamp': 1607387907,
        'upload_date': '20201208',
    }
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    result = LinuxAcademyIE().extract_info(url)
    assert result == expected

# Generated at 2022-06-14 16:50:51.626580
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # test the constructor of class LinuxAcademyIE
    assert LinuxAcademyIE._NETRC_MACHINE is not None
    assert LinuxAcademyIE._CLIENT_ID is not None

# Generated at 2022-06-14 16:50:57.480020
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._VALID_URL == r'(?x)https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|modules/view/id/(?P<course_id>\d+))'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'

# Generated at 2022-06-14 16:51:03.523013
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LAIE = LinuxAcademyIE()
    assert LAIE.__class__.__name__ == 'LinuxAcademyIE'
    assert LAIE.ie_key() == 'LinuxAcademy'
    assert LAIE.ie_key() in LinuxAcademyIE._ies

# Generated at 2022-06-14 16:51:04.217514
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    pass