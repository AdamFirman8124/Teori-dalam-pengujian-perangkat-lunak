

# Generated at 2022-06-14 16:45:28.671381
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
     assert LinuxAcademyIE(None)._NETRC_MACHINE == 'linuxacademy'
     assert True

# Generated at 2022-06-14 16:45:31.075268
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    info_extractor = LinuxAcademyIE()
    assert LinuxAcademyIE._VALID_URL is not None
    assert LinuxAcademyIE._TESTS is not None

# Generated at 2022-06-14 16:45:32.953897
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:45:44.406946
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:45:51.914960
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    if LinuxAcademyIE()._downloader is None:
        return

    ie = LinuxAcademyIE()
    page = ie._download_webpage_handle(
        "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675", None, 'Downloading authorize page')
    login_data_json = ie._search_regex(
        r'atob\(\s*(["\'])(?P<value>(?:(?!\1).)+)\1', page.read().decode(),
        'login info', group='value')

    login_data_raw = compat_b64decode(login_data_json).decode()
    login_data = ie._parse_json(login_data_raw, None)
    assert login_data is not None
   

# Generated at 2022-06-14 16:45:53.178289
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    inst = LinuxAcademyIE()
    return len(inst.IE_NAME) > 0

# Generated at 2022-06-14 16:46:04.576020
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    course_base_url = 'https://linuxacademy.com/cp/modules/view/id/%s'
    test_cases = [
        ('154', 'AWS Certified Cloud Practitioner'),
        ('1756', 'Docker Fundamentals'),
        ('445', 'RHCSA Rapid Track'),
    ]
    for case_idx, (course_id, expected_title) in enumerate(test_cases):
        course_url = course_base_url % course_id
        course = LinuxAcademyIE()._real_extract(course_url)
        if not isinstance(course, dict):
            raise TypeError('%d-th course: %s' % (case_idx, course_url))

# Generated at 2022-06-14 16:46:06.818109
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    print(LinuxAcademyIE())

# Generated at 2022-06-14 16:46:08.191768
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:19.210290
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.IE_DESC == 'Linux Academy'
    assert ie.VALID_URL == LinuxAcademyIE._VALID_URL
    assert ie.TEST == LinuxAcademyIE._TESTS
    assert ie._AUTHORIZE_URL == LinuxAcademyIE._AUTHORIZE_URL
    assert ie._ORIGIN_URL == LinuxAcademyIE._ORIGIN_URL
    assert ie._CLIENT_ID == LinuxAcademyIE._CLIENT_ID
    assert ie._NETRC_MACHINE == LinuxAcademyIE._NETRC_MACHINE
    assert ie._real_initialize() == None
    assert ie._login() == None

# Generated at 2022-06-14 16:47:07.860776
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test Headless Chrome as browser
    try:
        # pylint: disable=import-error
        from selenium.webdriver.chrome.options import Options
    except ImportError:
        return False
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    # TODO - change the test to not use login info
    info = LinuxAcademyIE._login_info()
    username = info['username']
    password = info['password']
    from .linuxacademy import LinuxAcademyCourseIE
    ie = LinuxAcademyIE(opts, 'tl959393', 'tl959393', username, password)
    assert ie.GetBrowser()



# Generated at 2022-06-14 16:47:17.553825
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.__class__.__name__ == 'LinuxAcademyIE'
    assert ie._LOGIN_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''

# Generated at 2022-06-14 16:47:20.212566
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    name = "test"
    password = "testtest123!"
    ie = LinuxAcademyIE()
    ie.username = name
    ie.password = password
    ie._real_initialize()

# Generated at 2022-06-14 16:47:29.811002
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

# Generated at 2022-06-14 16:47:31.112786
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.__class__.__name__ == 'LinuxAcademyIE'

# Generated at 2022-06-14 16:47:32.332682
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()
    assert obj is not None

# Generated at 2022-06-14 16:47:39.839086
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    infoExtractor = LinuxAcademyIE()
    # Unit test # 1
    url = "https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2"
    infoExtractor._real_initialize()
    infoExtractor._real_extract(url)
    # Unit test # 2
    url = "https://linuxacademy.com/cp/modules/view/id/154"
    infoExtractor._real_initialize()
    infoExtractor._real_extract(url)

# Generated at 2022-06-14 16:47:49.009278
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        from mutagen.mp4 import MP4
        from mutagen.mp3 import MP3
    except ImportError:
        return
    ie = LinuxAcademyIE()
    info = ie._real_extract(r'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert info['id'] == '7971-2'
    assert info['ext'] == 'mp4'
    assert info['title'] == 'What Is Data Science'
    assert info['description'] == 'md5:c574a3c20607144fb36cb65bdde76c99'
    assert info['timestamp'] == 1607387907
    assert info['upload_date'] == '20201208'
    assert info['duration'] == 304
   

# Generated at 2022-06-14 16:47:56.798875
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Test a regular and a lecture link
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675') == True
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154') == True
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/223/lesson/12') == True

    # Test that the NetrcMachine is correct
    assert ie._NETRC_MACHINE == "linuxacademy"

# Generated at 2022-06-14 16:48:04.733907
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .test_login import MockLoginIE
    args = [
        {
            'username': 'username1',
            'password': 'password1',
            'url': 'https://linuxacademy.com/cp/modules/view/id/154',
        },
        {
            'username': 'username2',
            'password': 'password2',
            'url': 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2',
        },
    ]
    for a in args:
        ie = MockLoginIE(LinuxAcademyIE, a['username'], a['password'])
        info = ie._real_extract(a['url'])
        assert info['title']
        assert info['description']
        assert info['id']
        assert info['duration']

# Generated at 2022-06-14 16:49:36.357642
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:49:37.185207
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:49:43.803417
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)'

# Generated at 2022-06-14 16:49:45.794393
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # just verify if constructor of class LinuxAcademyIE works properly
    login_info = {'login': '', 'password': ''}
    ie = LinuxAcademyIE(login_info)
    assert ie.ie_key() == 'LinuxAcademy'

# Generated at 2022-06-14 16:49:46.395931
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    pass

# Generated at 2022-06-14 16:49:50.862619
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_AUTHORIZE_URL')
    assert hasattr(ie, '_ORIGIN_URL')
    assert hasattr(ie, '_CLIENT_ID')
    assert hasattr(ie, '_NETRC_MACHINE')
    course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    video_url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    course_info = ie._real_extract(course_url)
    assert hasattr(course_info, 'get')
    assert course_info.get('_type') == 'playlist'

# Generated at 2022-06-14 16:49:56.953665
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    course_url = ('https://linuxacademy.com/cp/modules/view/id/154')
    course_id = '154'
    expected_course_title = 'AWS Certified Cloud Practitioner'
    expected_course_desc = 'md5:a68a299ca9bb98d41cca5abc4d4ce22c'
    expected_course_duration = 28835
    expected_course_modules_count = 41

    course_ie = LinuxAcademyIE()
    course_ie.extract(course_url)
    assert course_ie.get_course_title() == expected_course_title
    assert course_ie.get_course_description() == expected_course_desc
    assert course_ie.get_course_duration() == expected_course_duration
    assert course_ie.get_course_modules_

# Generated at 2022-06-14 16:50:08.956237
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie._LOGIN_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._VALID_URL == r'(?x)https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)'
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:50:16.933686
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._VALID_URL == 'https?://(?:www\\.)?linuxacademy\\.com/cp/courses/lesson/course/(?P<chapter_id>\\d+)/lesson/(?P<lesson_id>\\d+)'

# Generated at 2022-06-14 16:50:18.817467
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Function to construct an object of class LinuxAcademyIE
    """
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:52:06.434550
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:52:06.944114
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:52:09.247240
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Create an instance of class LinuxAcademyIE
    test_ie = LinuxAcademyIE()
    assert test_ie.ie_key() == 'linuxacademy'
    # Call method _real_initialize
    test_ie._real_initialize()
    # Call method _login
    test_ie._login()


# Generated at 2022-06-14 16:52:13.780498
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    '''
    Demonstration of how to check if a class can be constructed
    '''
    raise RuntimeError("Unit test for class LinuxAcademyIE is not implemented")
    # Check if LinuxAcademyIE was initialized successfully
    # assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:52:23.943994
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()
    assert obj.ie_key() == 'LinuxAcademy'
    assert obj.ie_name() == 'LinuxAcademy'
    assert obj._VALID_URL == r'https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|modules/view/id/(?P<course_id>\d+))'

# Generated at 2022-06-14 16:52:26.886924
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test LinuxAcademyIE
    # 1. Instantiate
    ie = LinuxAcademyIE()
    # 2. Check type
    assert (isinstance(ie, InfoExtractor))

if __name__ == "__main__":
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:52:32.516427
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    '''
    Constructor for the LinuxAcademyIE
    '''
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    ie = LinuxAcademyIE()

    # Create ChromeDriver instance.
    driver = ie._make_driver()

    # Open url
    driver.get(url)

    # Find and click username field
    for el in driver.find_elements_by_xpath('//input'):
        if el.get_attribute('type') == 'email':
            el.send_keys(ie._username)
            break

    # Find and click password field

# Generated at 2022-06-14 16:52:34.291982
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    x = LinuxAcademyIE()
    assert x.IE_NAME == 'linuxacademy'

# Generated at 2022-06-14 16:52:35.728513
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    info_extract = LinuxAcademyIE(InfoExtractor())
    assert info_extract is not None

# Generated at 2022-06-14 16:52:39.642150
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert LinuxAcademyIE._NETRC_MACHINE == 'linuxacademy'