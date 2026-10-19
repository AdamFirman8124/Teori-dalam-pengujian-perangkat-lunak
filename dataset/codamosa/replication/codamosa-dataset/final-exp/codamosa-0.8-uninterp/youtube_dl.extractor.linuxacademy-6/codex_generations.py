

# Generated at 2022-06-14 16:45:23.877620
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:31.307490
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Fake url, just for testing
    url = "https://linuxacademy.com/cp/modules/view/id/154"
    # Create an instance of class LinuxAcademyIE
    ie = LinuxAcademyIE()
    # Test instance
    assert ie.suitable(url) is True

    # Create an instance of class LinuxAcademyIE
    ie = LinuxAcademyIE(url)
    # Test instance
    assert ie.suitable(url) is True

# Generated at 2022-06-14 16:45:33.043849
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'

# Generated at 2022-06-14 16:45:39.726889
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxacademy = LinuxAcademyIE()
    assert linuxacademy.IE_NAME == "linuxacademy"
    assert linuxacademy.AUTHORIZED == True
    assert linuxacademy.IE_DESC == "Linux Academy"
    assert linuxacademy._VALID_URL == r'(?x)https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|modules/view/id/(?P<course_id>\d+))'
    assert linuxacademy._AUTHORIZE_URL == "https://login.linuxacademy.com/authorize"

# Generated at 2022-06-14 16:45:42.000857
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance_LinuxAcademyIE = LinuxAcademyIE()
    assert isinstance(instance_LinuxAcademyIE, InfoExtractor)

# Generated at 2022-06-14 16:45:42.911879
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(None)

# Generated at 2022-06-14 16:45:43.842441
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test = LinuxAcademyIE()

# Generated at 2022-06-14 16:45:45.807553
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    class_object = LinuxAcademyIE()
    assert class_object.__class__.__name__ == "LinuxAcademyIE"

# Generated at 2022-06-14 16:45:46.923160
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    la = LinuxAcademyIE()
    print('username is :' + la.username)

# Generated at 2022-06-14 16:45:57.420643
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Success case
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.IE_DESC == 'LinuxAcademy'
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''
    # Error case

# Generated at 2022-06-14 16:46:35.120987
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Call constructor of class LinuxAcademyIE with argument True
    assert isinstance(LinuxAcademyIE(True), LinuxAcademyIE)
    # Call constructor of class LinuxAcademyIE with argument False
    assert isinstance(LinuxAcademyIE(False), LinuxAcademyIE)

# Generated at 2022-06-14 16:46:36.346547
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert type(LinuxAcademyIE({})) == LinuxAcademyIE

# Generated at 2022-06-14 16:46:37.153581
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('LinuxAcademy')

# Generated at 2022-06-14 16:46:42.069927
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Right now, this just checks that the Linux Academy constructor is
    # error-free, and that it returns an instance of the correct class.
    IE = LinuxAcademyIE(None)
    assert IE.__class__.__name__ == 'LinuxAcademyIE'

# Generated at 2022-06-14 16:46:44.218588
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        LinuxAcademyIE()
    except Exception as e:
        print(e)


# Generated at 2022-06-14 16:46:51.772188
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'

    # Construct a instance of class LinuxAcademyIE
    lai = LinuxAcademyIE(url)

    # Check attributes of instance
    assert lai.ie_key() == 'LinuxAcademy'
    assert lai.suitable(url)
    assert lai._VALID_URL == r'(?x)https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)'

# Generated at 2022-06-14 16:46:52.977856
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:46:54.445658
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()._login()

# Generated at 2022-06-14 16:46:56.707161
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, LinuxAcademyIE)


# Generated at 2022-06-14 16:46:58.729787
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Just run constructor of class LinuxAcademyIE and print outputs
    assert LinuxAcademyIE(None, None)

# Generated at 2022-06-14 16:48:24.348464
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # The following test can be used in unit testing to test the constructor of the class LinuxAcademyIE.
    ie = LinuxAcademyIE()
    return ie

if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:48:28.314343
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    x = LinuxAcademyIE()
    assert x._CLIENT_ID == "KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx"
    assert x._NETRC_MACHINE == "linuxacademy"
    assert x._ORIGIN_URL == "https://linuxacademy.com"
    assert x._AUTHORIZE_URL == "https://login.linuxacademy.com/authorize"


# Generated at 2022-06-14 16:48:36.451426
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Override parameters for test
    LinuxAcademyIE._AUTHORIZE_URL = 'https://example.com/authorize'
    LinuxAcademyIE._CLIENT_ID = 'Your client ID'
    LinuxAcademyIE._NETRC_MACHINE = 'linuxacademy'

    # Override methods for test
    _download_webpage = LinuxAcademyIE._download_webpage
    _download_webpage_handle = LinuxAcademyIE._download_webpage_handle
    _parse_json = LinuxAcademyIE._parse_json


# Generated at 2022-06-14 16:48:39.704886
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        LinuxAcademyIE()
        status = 0
    except Exception as e:
        print(e)
        status = 1
    assert status == 0


# Generated at 2022-06-14 16:48:41.180073
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()
    assert obj is not None


# Generated at 2022-06-14 16:48:43.754312
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.ie_key() == 'LinuxAcademy'

# Generated at 2022-06-14 16:48:44.560763
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:48:47.042342
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # test whether constructor successfully initialized.
    ie = LinuxAcademyIE()
    assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:48:48.159466
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:48:49.644247
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    t = LinuxAcademyIE()
    t._login()

# Generated at 2022-06-14 16:52:14.217423
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE().download_webpage('https://linuxacademy.com/cp/modules/view/id/154', '154')

# Generated at 2022-06-14 16:52:15.075113
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:52:18.279981
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    randomString = random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz-._~')
    linuxAcademyIE = LinuxAcademyIE(randomString, randomString, randomString)

# Generated at 2022-06-14 16:52:26.638200
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .youtube import YouTubeIE
    from .common import InfoExtractor

    # Assert that class is main class of IE
    assert LinuxAcademyIE == LinuxAcademyIE.ie_key()
    
    # Assert that ie_key and ie_key_regex are defined
    assert LinuxAcademyIE.ie_key() and LinuxAcademyIE.ie_key_regex()
    
    # Assert that embed_webpage is defined
    assert callable(LinuxAcademyIE._embed_webpage)

    # Assert that _LOGIN_URL is defined
    assert LinuxAcademyIE._LOGIN_URL


# Generated at 2022-06-14 16:52:27.626273
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert isinstance(LinuxAcademyIE(), LinuxAcademyIE)

# Generated at 2022-06-14 16:52:28.563898
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:52:29.333344
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE.ie_key()

# Generated at 2022-06-14 16:52:33.156342
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_case = {
        'url': 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
    }
    obj = LinuxAcademyIE()
    obj.test(test_case)

# Generated at 2022-06-14 16:52:34.033185
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('')

# Generated at 2022-06-14 16:52:40.136931
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Arrange
    test_url = "https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2"

    # Act
    chapter_id, lecture_id, course_id = re.match(LinuxAcademyIE._VALID_URL, test_url).group('chapter_id', 'lesson_id', 'course_id')

    # Assert
    assert chapter_id is not None
    assert lecture_id is not None
    assert course_id is None