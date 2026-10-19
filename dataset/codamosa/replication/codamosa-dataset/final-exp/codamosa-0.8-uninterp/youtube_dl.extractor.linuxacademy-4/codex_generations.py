

# Generated at 2022-06-14 16:45:36.199461
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Initialize an instance of class LinuxAcademyIE
    # using a string as the first argument
    test_laie = LinuxAcademyIE("https://linuxacademy.com/cp/modules/view/id/154")
    assert test_laie.get_authorize_url() == "https://login.linuxacademy.com/authorize"

# Generated at 2022-06-14 16:45:38.003606
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:39.879767
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    info_extractor = LinuxAcademyIE()
    print(info_extractor._real_initialize())

# Generated at 2022-06-14 16:45:48.745450
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._VALID_URL == r'(?x)https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|https?://(?:www\.)?linuxacademy\.com/cp/modules/view/id/(?P<course_id>\d+)'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'

# Generated at 2022-06-14 16:45:51.875273
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE("")
    assert ie.IE_NAME == "LinuxAcademy"
    assert ie.__class__.__name__ == "LinuxAcademyIE"

# Generated at 2022-06-14 16:45:52.804627
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    login = LinuxAcademyIE(context, '');

# Generated at 2022-06-14 16:45:57.726427
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._vali

# Generated at 2022-06-14 16:46:10.424120
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    def test_url(url):
        if not hasattr(LinuxAcademyIE, '_download_webpage'):
            LinuxAcademyIE._download_webpage = lambda self, url, video_id, note, errnote: None
        return LinuxAcademyIE(url)._real_extract(url)

    # single video
    url1 = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    res1 = test_url(url1)
    assert isinstance(res1, dict)

    # course
    url2 = 'https://linuxacademy.com/cp/modules/view/id/154'
    res2 = test_url(url2)
    assert isinstance(res2, dict)

# Generated at 2022-06-14 16:46:11.185358
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:12.068827
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    constructor(LinuxAcademyIE)

# Generated at 2022-06-14 16:46:49.288607
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE(None, None)._CLIENT_ID is not None

# Generated at 2022-06-14 16:46:50.160413
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:52.191195
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:55.217694
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2022-06-14 16:46:58.118024
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    data = LinuxAcademyIE()
    assert type(data) is LinuxAcademyIE
# test_LinuxAcademyIE

# Generated at 2022-06-14 16:46:59.091376
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()


# Generated at 2022-06-14 16:47:07.301115
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:47:08.238415
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:47:14.030231
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_infoExtractor = LinuxAcademyIE()
    test_infoExtractor._login()
    test_infoExtractor._real_extract('https://linuxacademy.com/cp/modules/view/id/154')
    test_infoExtractor._real_extract('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')

# Generated at 2022-06-14 16:47:24.226487
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE().IE_NAME == 'linuxacademy'
    assert LinuxAcademyIE()._VALID_URL == LinuxAcademyIE._VALID_URL
    assert LinuxAcademyIE()._build_url_result(8079, 1, 0) == 'https://linuxacademy.com/cp/courses/lesson/course/8079/lesson/1/module/0'
    assert LinuxAcademyIE()._build_url_result(8079, 1, 0, '8079-1') == 'https://linuxacademy.com/cp/courses/lesson/course/8079/lesson/1/module/0'

# Generated at 2022-06-14 16:48:45.274531
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Arrange
    linux_academy_ie = LinuxAcademyIE(None)

    # Act
    # Nothing to do with act phase

    # Assert
    assert linux_academy_ie.IE_NAME == 'LinuxAcademy'

# Generated at 2022-06-14 16:48:48.559391
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    print("TEST")
    url = 'https://linuxacademy.com/cp/modules/view/id/154'
    print(LinuxAcademyIE()._real_extract(url))

# Generated at 2022-06-14 16:48:51.484262
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.__class__.__name__ == 'LinuxAcademyIE'


# Generated at 2022-06-14 16:48:59.314953
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    la = LinuxAcademyIE()
    #assert la._VALID_URL == r'''(?x)
    #https?://
    #(?:www\.)?linuxacademy\.com/cp/
    #(?:
    #courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
    #modules/view/id/(?P<course_id>\d+)
    #)'''

# Generated at 2022-06-14 16:49:03.242798
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():

    def test_get_login_info():
        if not isinstance(LinuxAcademyIE._get_login_info.func_code, types.FunctionType):
            return None
        else:
            raise AssertionError("requires Linux Academy account credentials")

    # print(test_get_login_info.__doc__)
    print(test_get_login_info())

test_LinuxAcademyIE()

# Generated at 2022-06-14 16:49:12.545314
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test subscribing to a course and getting the course's chapters and lectures
    course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    course_ie = LinuxAcademyIE()
    course_ie.extract(course_url)

    # Test subscribing to a course and getting a chapter's lectures
    #   This can also be done by adding chapter_id to the url
    chapter_url = 'https://linuxacademy.com/cp/modules/view/id/154/chapter/36'
    chapter_ie = LinuxAcademyIE()
    chapter_ie.extract(chapter_url)

    # Test subscribing to a course and getting a lecture
    lecture_url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'


# Generated at 2022-06-14 16:49:15.296884
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Unit test for constructor of class LinuxAcademyIE
    """
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie.NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:49:24.598255
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Without any netrc file
    linuxAcademy = LinuxAcademyIE()
    assert linuxAcademy._NETRC_MACHINE == 'linuxacademy'
    try:
        linuxAcademy._login()
    except ExtractorError as e:
        if isinstance(e.cause, compat_HTTPError) and e.cause.code == 401:
            error = linuxAcademy._parse_json(e.cause.read(), None)
            message = error.get('description') or error['code']
            assert message == 'access_denied'
        else:
            raise
    # With netrc file
    linuxAcademy = LinuxAcademyIE()
    linuxAcademy.to_screen('Linux Acacemy login')
    assert linuxAcademy._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:49:25.470504
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE().IE_NAME

# Generated at 2022-06-14 16:49:26.842348
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Unit test for LinuxAcademyIE
    """
    LA = LinuxAcademyIE()

# Generated at 2022-06-14 16:53:02.941847
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE("test", "test")
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

# Generated at 2022-06-14 16:53:04.668817
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:53:09.510869
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:53:10.219771
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:53:15.129359
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._AUTHORIZE_URL
    assert ie._ORIGIN_URL
    assert ie._CLIENT_ID
    assert ie._NETRC_MACHINE
    assert ie._VALID_URL
    assert ie._TESTS

# Generated at 2022-06-14 16:53:17.906703
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
	
	# Constructor of class LinuxAcademyIE
	linuxacademyIE = LinuxAcademyIE()
	

# Generated at 2022-06-14 16:53:21.287658
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Constructor for this class
    class_ie = LinuxAcademyIE(None)
    assert class_ie.SUID is None
    assert class_ie.NAME is None
    assert class_ie.DESC is None
    assert class_ie.BUILD is not None
    assert class_ie.webpage_url_has_rdir is None

# Generated at 2022-06-14 16:53:21.901165
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()._login()

# Generated at 2022-06-14 16:53:28.701171
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''

# Generated at 2022-06-14 16:53:31.353237
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
        Constructor test for Linux AcademyIE
    """
    ie = LinuxAcademyIE()
    assert ie.get_info_extractor().IE_NAME == 'LinuxAcademy'