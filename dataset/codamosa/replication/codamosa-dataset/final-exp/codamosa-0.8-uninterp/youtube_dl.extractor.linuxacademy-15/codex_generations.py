

# Generated at 2022-06-14 16:45:31.675238
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE_instance = LinuxAcademyIE()
    LinuxAcademyIE_instance._login()
    LinuxAcademyIE_instance._real_extract('https://linuxacademy.com/cp/modules/view/id/154')

# Generated at 2022-06-14 16:45:33.680730
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:45:44.923813
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Initialize LinuxAcademy class
    l = LinuxAcademyIE()
    # Make sure the classes are initialized correctly
    assert l._VALID_URL == r'https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)'
    assert l._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert l._ORIGIN_URL == 'https://linuxacademy.com'
    assert l._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert l._NETRC_MACHINE == 'linuxacademy'
   

# Generated at 2022-06-14 16:45:45.807438
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:45:46.658696
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE.new()

# Generated at 2022-06-14 16:45:57.376729
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
	assert LinuxAcademyIE.__name__ == 'LinuxAcademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'
	assert LinuxAcademyIE.ie_key() == 'linuxacademy'


# Generated at 2022-06-14 16:46:03.184255
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test that "instance.subtitle" value is replaced by _subtitle
    class SubtitleTest(LinuxAcademyIE):
        def _real_initialize(self):
            pass
    instance = SubtitleTest('subtitle')
    assert instance.subtitle == 'subtitle'
    assert instance._subtitle == 'subtitle'
    assert instance.subtitle is None

# Generated at 2022-06-14 16:46:03.992725
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE._real_initialize()

# Generated at 2022-06-14 16:46:15.486386
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if not LinuxAcademyIE._login():
        print('Login failed!')
    overall_tests = 0
    success_tests = 0
    for test in LinuxAcademyIE._TESTS:
        overall_tests += 1
        if 'skip' in test:
            print('Test %d: skipping test because: %s' % (overall_tests, test['skip']))
            continue

        # create new instance of LinuxAcademyIE instance
        la_ie = LinuxAcademyIE(True)

# Generated at 2022-06-14 16:46:21.417434
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # This assert should not fail
    assert isinstance(LinuxAcademyIE(), LinuxAcademyIE)
    # These asserts should fail
    assert not isinstance(LinuxAcademyIE(), InfoExtractor)
    assert not isinstance(InfoExtractor(), LinuxAcademyIE)
    assert not isinstance('LinuxAcademyIE', LinuxAcademyIE)

# Generated at 2022-06-14 16:46:45.845837
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.LOGIN_URL == 'https://login.linuxacademy.com/authorize'
    assert ie.NETRC_MACHINE == 'linuxacademy'
    assert ie.VALID_URL.startswith('https?://(?:www\.)?linuxacademy\.com/')

# Generated at 2022-06-14 16:46:46.807964
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    _ = LinuxAcademyIE()

# Generated at 2022-06-14 16:46:49.822367
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # testing the exception
    try:
        inst = LinuxAcademyIE()
        inst.extract()
    except ExtractorError as expected:
        assert expected.cause.code == 401
    else:
        assert False

        # testing return values from _login()

# Generated at 2022-06-14 16:47:01.903280
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.__dict__.get('ie_key') == 'LinuxAcademy'
    assert LinuxAcademyIE.__dict__.get('_VALID_URL') == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''.replace(' ', '')
    assert LinuxAcademyIE.__dict__.get('_TESTS')[1].get('info_dict').get('id') == '7971-2'
    assert LinuxAcademyIE.__dict__

# Generated at 2022-06-14 16:47:04.508554
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    # Test constructor
    assert extractor.IE_NAME == "linuxacademy"
    assert extractor.NETRC_MACHINE == "LinuxAcademy"

# Generated at 2022-06-14 16:47:05.306931
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:47:07.304826
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:47:12.112362
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    LinuxAcademyIE()._extract_urls(url)

# Unit test script
if __name__ == "__main__":
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:47:13.124185
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE('')

# Generated at 2022-06-14 16:47:15.977937
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Constructor of class LinuxAcademyIE
    ie = LinuxAcademyIE()
    # test of class LinuxAcademyIE has no error
    assert ie

# Generated at 2022-06-14 16:48:11.097470
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    x = LinuxAcademyIE()
    assert x._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert x._ORIGIN_URL == 'https://linuxacademy.com'
    assert x._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert x._NETRC_MACHINE == 'linuxacademy'


# Generated at 2022-06-14 16:48:12.833455
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('LinuxAcademy')

# Generated at 2022-06-14 16:48:13.815739
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('linuxacademy')

# Generated at 2022-06-14 16:48:18.736289
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    for video_url, video_title in (
            ('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2', 'Introduction to Programming with Python'),
            ('https://linuxacademy.com/cp/modules/view/id/154', 'AWS Certified Cloud Practitioner')):
        assert LinuxAcademyIE().extract_info(video_url)['title'] == video_title

# Generated at 2022-06-14 16:48:30.614490
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie._VALID_URL == (r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    ''')

# Generated at 2022-06-14 16:48:37.890608
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Create object
    res = LinuxAcademyIE()
    assert res._VALID_URL == r"(?x)https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|modules/view/id/(?P<course_id>\d+))"

# Generated at 2022-06-14 16:48:40.609734
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME in globals()
    assert ie.IE_NAME in globals()

# Generated at 2022-06-14 16:48:41.625159
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()
    return True

# Generated at 2022-06-14 16:48:44.652080
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    test_ie = LinuxAcademyIE(None)
    test_ie.initialize()
    test_ie.login()
    assert test_ie.extract(test_url).__class__ is dict
    return

# Generated at 2022-06-14 16:48:48.110212
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie.IE_DESC == 'Linux Academy'

# Generated at 2022-06-14 16:50:45.969594
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:50:50.378994
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()
    assert obj._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert obj._ORIGIN_URL == 'https://linuxacademy.com'
    assert obj._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert obj._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:50:55.775439
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert ie.suitable('linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('linuxacademy.com/cp/settings/password')

# Generated at 2022-06-14 16:50:57.294073
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, LinuxAcademyIE)


# Generated at 2022-06-14 16:51:02.507487
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxAcademyIE = LinuxAcademyIE()
    assert linuxAcademyIE is not None, "Couldn't create an instance of LinuxAcademyIE"

# Generated at 2022-06-14 16:51:03.408960
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:51:04.392884
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()

# Generated at 2022-06-14 16:51:06.192931
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:51:08.662854
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Unit test for constructor of class LinuxAcademyIE
    """
    i = LinuxAcademyIE()
    assert i is not None

# Generated at 2022-06-14 16:51:10.273551
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        LinuxAcademyIE()
        raise Exception('Exception not raised')
    except TypeError:
        pass