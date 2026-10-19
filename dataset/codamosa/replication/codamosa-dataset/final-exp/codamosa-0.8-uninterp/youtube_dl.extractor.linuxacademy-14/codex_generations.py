

# Generated at 2022-06-14 16:45:24.603328
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(None)

# Generated at 2022-06-14 16:45:35.763615
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie._VALID_URL == 'https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\\d+)/lesson/(?P<lesson_id>\\d+)|modules/view/id/(?P<course_id>\\d+))'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._NETRC

# Generated at 2022-06-14 16:45:46.380946
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Arrange
    extracted_obj = {
        'id': '7971-2',
        'ext': 'mp4',
        'title': 'What Is Data Science',
        'description': 'md5:c574a3c20607144fb36cb65bdde76c99',
        'timestamp': 1607387907,
        'upload_date': '20201208',
        'duration': 304,
    }

    # Act
    linux_academy = LinuxAcademyIE()

    # Assert

# Generated at 2022-06-14 16:45:47.953099
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()
    assert extractor is not None


# Generated at 2022-06-14 16:45:52.799999
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Tests for LinuxAcademy
    test_linuxAcademy = [
        # LinuxAcademy course
        ('https://linuxacademy.com/cp/modules/view/id/154', 'LinuxAcademy'),
        # LinuxAcademy lesson
        ('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675', 'LinuxAcademy'),
    ]

    for test in test_linuxAcademy:
        yield unit_test(LinuxAcademyIE(), test[0], test[1])



# Generated at 2022-06-14 16:45:57.778024
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()._real_initialize()

# Generated at 2022-06-14 16:46:05.990858
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert(LinuxAcademyIE.ie_key() == 'LinuxAcademy')
    assert(LinuxAcademyIE._NETRC_MACHINE == 'linuxacademy')
    assert(LinuxAcademyIE.VERSION == '1.0.4')
    assert(LinuxAcademyIE._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    ''')

# Generated at 2022-06-14 16:46:07.495208
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    print('Constructor...')
    print(LinuxAcademyIE(None)._VALID_URL)

# Generated at 2022-06-14 16:46:09.366603
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy_ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:46:14.028412
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    course =  LinuxAcademyIE()
    lesson = course.extract("https://linuxacademy.com/cp/modules/view/id/154")
    lesson["entries"][0]["title"] == 'AWS Certified Cloud Practitioner'
    assert lesson["entries"][0]["title"] == "AWS Certified Cloud Practitioner", "Test LinuxAcademyIE"

# Generated at 2022-06-14 16:46:50.882542
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.SITE

# Generated at 2022-06-14 16:47:03.034175
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # this test will fail if the developer doesn't include
    # his credentials in the test environment
    #    export LA_USER='<username>'
    #    export LA_PASSWORD='<password>'
    import os
    import unittest

    class LinuxAcademyTests(unittest.TestCase):
        user = os.getenv('LA_USER', None)
        password = os.getenv('LA_PASSWORD', None)

        def setUp(self):
            if not (self.user and self.password):
                raise unittest.SkipTest('Credentials are not available, skipping.')

        def tearDown(self):
            pass


# Generated at 2022-06-14 16:47:04.813944
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'linuxacademy'
    assert LinuxAcademyIE in InfoExtractor._ALL_CLASSES

# Generated at 2022-06-14 16:47:16.213944
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:47:23.969340
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
	import sys
	from unittest import TestCase

	class ConstructorTest(TestCase):
		def test_constructor(self):
			config = {
				'_login': lambda x: None
			}
			try:
				LinuxAcademyIE(config)
			except TypeError:
				if sys.version_info[0] > 2:
					raise
			else:
				if sys.version_info[0] < 3:
					raise

	return ConstructorTest


# Generated at 2022-06-14 16:47:27.575443
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    This test is to check constructor of class LinuxAcademyIE
    """
    expected_result = LinuxAcademyIE
    real_result = LinuxAcademyIE.__bases__
    assert real_result == expected_result, "LinuxAcademyIE constructor is not as expected"

# Generated at 2022-06-14 16:47:29.272528
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE("test_LinuxAcademyIE", "", {})._NETRC_MACHINE == "linuxacademy"

# Generated at 2022-06-14 16:47:30.160718
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(dict())

# Generated at 2022-06-14 16:47:31.521519
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ieClass = LinuxAcademyIE()
    return ieClass

# Generated at 2022-06-14 16:47:32.373449
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()._login() is None

# Generated at 2022-06-14 16:48:18.086368
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE(None, 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675') == 'LinuxAcademyIE'
    assert LinuxAcademyIE(None, 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') == 'LinuxAcademyIE'
    assert LinuxAcademyIE(None, 'https://linuxacademy.com/cp/modules/view/id/154') == 'LinuxAcademyIE'

# Generated at 2022-06-14 16:48:21.992534
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        linuxAcademyIE = LinuxAcademyIE()
    except Exception as e:
        assert False
    assert True

# Generated at 2022-06-14 16:48:32.515217
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Unit test for LinuxAcademyIE"""
    assert LinuxAcademyIE().ie_key() == 'LinuxAcademy'
    assert LinuxAcademyIE()._VALID_URL == '^https?://(?:www\\\.)?linuxacademy\\\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\\\d+)/lesson/(?P<lesson_id>\\\d+)|modules/view/id/(?P<course_id>\\\d+))$'

# Generated at 2022-06-14 16:48:34.054787
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:48:35.878152
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    # has_login_token is False
    ie._login()

# Generated at 2022-06-14 16:48:42.679721
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert len(LinuxAcademyIE._TESTS) != 0
    assert len(LinuxAcademyIE._NETRC_MACHINE) != 0
    assert len(LinuxAcademyIE._AUTHORIZE_URL) != 0
    assert len(LinuxAcademyIE._CLIENT_ID) != 0
    assert len(LinuxAcademyIE._ORIGIN_URL) != 0
    assert len(LinuxAcademyIE._TESTS) != 0

# Generated at 2022-06-14 16:48:47.042479
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # pylint: disable=redefined-outer-name
    # pylint: disable=line-too-long
    ie = LinuxAcademyIE("https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675")
    result = ie._real_initialize()
    assert result is None

# Generated at 2022-06-14 16:48:49.353505
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if not LinuxAcademyIE.working():
        return
    ie = LinuxAcademyIE()
    ie._pre_login(False)

# Generated at 2022-06-14 16:48:51.066480
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:48:52.161429
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE();

# Generated at 2022-06-14 16:50:44.722841
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:50:47.338218
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    IE_NAME = 'LinuxAcademy'
    instance = LinuxAcademyIE()
    assert instance.IE_NAME == IE_NAME
    assert instance.ie_key() == IE_NAME
    assert instance.ie_key() == 'linuxacademy'

# Generated at 2022-06-14 16:50:58.005476
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:51:02.024862
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE('linuxacademy')
    assert ie.ie_key() == 'LinuxAcademy'

# Generated at 2022-06-14 16:51:03.196582
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:51:13.754283
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test using a temporary file and then deleting it
    import tempfile
    import os
    import shutil

    # Create a temporary file
    f = tempfile.NamedTemporaryFile(mode='w', suffix='.netrc', dir=tempfile.gettempdir())
    f.write('machine linuxacademy login dgmdbz password cpT_TEWV7YAA')
    f.flush()


# Generated at 2022-06-14 16:51:20.148574
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    info_dict = LinuxAcademyIE()._real_extract(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert (info_dict['id'] == '7971-2')
    assert (info_dict['title'] == 'What Is Data Science')
    assert (info_dict['description'] == 'md5:c574a3c20607144fb36cb65bdde76c99')
    assert (info_dict['timestamp'] == 1607387907)
    assert (info_dict['upload_date'] == '20201208')
    assert (info_dict['duration'] == 304)

# Generated at 2022-06-14 16:51:21.243385
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:51:30.928929
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():

    ie = LinuxAcademyIE()
    assert hasattr(ie, '_login')
    assert hasattr(ie, '_real_initialize')
    assert hasattr(ie, '_real_extract')
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, '_AUTHORIZE_URL')
    assert hasattr(ie, '_ORIGIN_URL')
    assert hasattr(ie, '_CLIENT_ID')
    assert hasattr(ie, '_NETRC_MACHINE')

    assert ie._real_extract('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')


# Generated at 2022-06-14 16:51:36.732873
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test without login
    constructor_test(LinuxAcademyIE, [
        ('https://linuxacademy.com/cp/modules/view/id/154', {
            'id': '154',
            'title': 'AWS Certified Cloud Practitioner',
            'description': 'md5:a68a299ca9bb98d41cca5abc4d4ce22c',
            'duration': 28835,
        }, 'playlist', 41),
    ])