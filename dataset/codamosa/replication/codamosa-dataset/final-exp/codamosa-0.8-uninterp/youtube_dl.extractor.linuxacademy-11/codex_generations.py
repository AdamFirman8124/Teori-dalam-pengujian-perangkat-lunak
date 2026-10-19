

# Generated at 2022-06-14 16:45:28.670832
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    module = LinuxAcademyIE()
    assert module

# Generated at 2022-06-14 16:45:29.660212
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(None).test()

# Generated at 2022-06-14 16:45:30.985365
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    print(ie)

# Generated at 2022-06-14 16:45:33.432063
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE(context={'_downloader': {}})
    # expect no exception here
    assert ie is not None

# Generated at 2022-06-14 16:45:34.261421
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:36.326275
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test if constructor works
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:45:38.854591
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:45:42.119018
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == "linuxacademy"

    module = LinuxAcademyIE()
    assert module._NETRC_MACHINE == 'linuxacademy'


# Generated at 2022-06-14 16:45:43.396571
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
  l = LinuxAcademyIE()
  l._login()

# Generated at 2022-06-14 16:45:45.728597
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Basic test for LinuxAcademyIE constructor.

    """
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'

# Generated at 2022-06-14 16:46:24.298485
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie_instance = LinuxAcademyIE()
    ie_instance._login()

# Generated at 2022-06-14 16:46:27.076587
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE('linuxacademy', {})
    assert(ie.IE_NAME == 'linuxacademy')
    assert(ie.IE_DESC == 'Linux Academy')

# Generated at 2022-06-14 16:46:29.943733
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Constructor test, must be called from constructor of class.
    """
    linuxAcademyIE = LinuxAcademyIE()
    if linuxAcademyIE is not None:
        print("Unit test for class LinuxAcademyIE passed.")


# Generated at 2022-06-14 16:46:31.730543
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from . import LinuxAcademyIE as ieu
    ieu_test = ieu(None)

# Generated at 2022-06-14 16:46:33.544217
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()


# Generated at 2022-06-14 16:46:35.974794
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:46:37.217527
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()._LOGIN_REQUIRED

# Generated at 2022-06-14 16:46:40.358991
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'

# Generated at 2022-06-14 16:46:44.081020
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = LinuxAcademyIE._VALID_URL
    assert LinuxAcademyIE.suitable(url)
    assert LinuxAcademyIE.IE_NAME == 'LinuxAcademy'

# Unit testing
test_LinuxAcademyIE()

# Generated at 2022-06-14 16:46:45.102300
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    obj = LinuxAcademyIE()


# Generated at 2022-06-14 16:48:20.605771
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie_objs = LinuxAcademyIE._build_ie_list()
    assert ie_objs[0].ie_key() == 'LinuxAcademy'
    assert ie_objs[0].ie_key() == LinuxAcademyIE.ie_key()
    assert ie_objs[0]._VALID_URL == LinuxAcademyIE._VALID_URL
    assert ie_objs[0]._NETRC_MACHINE == LinuxAcademyIE._NETRC_MACHINE
    assert ie_objs[0]._CLIENT_ID == LinuxAcademyIE._CLIENT_ID
    assert ie_objs[0]._AUTHORIZE_URL == LinuxAcademyIE._AUTHORIZE_URL
    assert ie_objs[0]._ORIGIN_URL == LinuxAcademyIE._

# Generated at 2022-06-14 16:48:24.876974
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    class_constructor = getattr(LinuxAcademyIE, '__init__')
    obj = LinuxAcademyIE()
    assert class_constructor.__code__ == class_constructor.__closure__[0].cell_contents

# Generated at 2022-06-14 16:48:27.297629
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test without credentials
    LinuxAcademyIE()
    # Test with credentials
    LinuxAcademyIE(username='foo', password='bar')



# Generated at 2022-06-14 16:48:35.757071
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    _VALID_URL = r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''
    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    chapter_id, lecture_id, course_id = mobj.group('chapter_id', 'lesson_id', 'course_id')
    item_id

# Generated at 2022-06-14 16:48:38.798376
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(InfoExtractor)

if __name__ == "__main__":
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:48:39.860570
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()


# Generated at 2022-06-14 16:48:41.775022
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    infoExtractor = LinuxAcademyIE()
    assert(infoExtractor.IE_NAME == 'linuxacademy')

# Generated at 2022-06-14 16:48:43.165353
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert(LinuxAcademyIE.ie_key() == 'LinuxAcademy')

# Generated at 2022-06-14 16:48:45.112235
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """ Test LinuxAcademyIE class constructor with only mandatory arguments """
    LinuxAcademyIE(test_LinuxAcademyIE.__name__)

# Generated at 2022-06-14 16:48:49.187832
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    This unit test checks the initialisation of the class LinuxAcademyIE
    """

    test = LinuxAcademyIE("LinuxAcademyIE")
    # check if the instance test is of class LinuxAcademyIE
    assert isinstance(test, LinuxAcademyIE)

# Generated at 2022-06-14 16:50:50.009934
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')

# Generated at 2022-06-14 16:50:50.875523
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()._real_initialize()

# Generated at 2022-06-14 16:50:52.778496
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE

# Generated at 2022-06-14 16:50:58.970415
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    uuid = '7971-2'
    title = 'What Is Data Science'
    description = 'md5:c574a3c20607144fb36cb65bdde76c99'
    timestamp = 1607387907
    duration = 304

    ie = LinuxAcademyIE()
    ie.extract_info(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        {'id': uuid, 'title': title, 'description': description, 'timestamp': timestamp, 'duration': duration},
    )

# Generated at 2022-06-14 16:51:01.708684
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'linuxacademy'



# Generated at 2022-06-14 16:51:07.882778
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    lec_url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    instance = LinuxAcademyIE()
    instance._download_webpage = lambda *a, **k: '{"name" : "hls", "url" : "http://www.example.com"}'
    assert instance.suitable(lec_url)

# Generated at 2022-06-14 16:51:13.051542
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test constructor of class LinuxAcademyIE"""
    # Test empty constructor
    try:
        LinuxAcademyIE()
    except Exception:
        assert False, 'Empty constructor of LinuxAcademyIE must not fail'

    # Test empty arguments
    try:
        LinuxAcademyIE(None)
    except Exception:
        assert False, 'Empty arguments of LinuxAcademyIE must not fail'

# Generated at 2022-06-14 16:51:14.977819
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    CloudShellIE = cloudshell_ie.CloudShellIE()
    assert isinstance(CloudShellIE, cloudshell_ie.CloudShellIE)

# Generated at 2022-06-14 16:51:17.280598
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    lec = LinuxAcademyIE()
    lec._initialize()
    return lec

# Generated at 2022-06-14 16:51:21.816908
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        assert isinstance(LinuxAcademyIE("LinuxAcademyIE", "LinuxAcademyIE"), InfoExtractor)
    except AssertionError:
        warnings.warn("It is not InfoExtractor")

# Generated at 2022-06-14 16:53:22.297229
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    podcast = LinuxAcademyIE()
    assert isinstance(podcast, InfoExtractor)

# Generated at 2022-06-14 16:53:24.597479
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/modules/view/id/154'
    _, course_id = LinuxAcademyIE._extract_url(url)
    assert course_id == '154'

# Generated at 2022-06-14 16:53:25.500088
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:53:26.438561
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        ie = LinuxAcademyIE()
    except Exception:
        assert False

# Generated at 2022-06-14 16:53:27.597223
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    IE = LinuxAcademyIE('LinuxAcademy', 'linuxacademy.com')
    assert IE is not None

# Generated at 2022-06-14 16:53:37.960715
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie.IE_DESC == 'LinuxAcademy for Business'

# Generated at 2022-06-14 16:53:41.314551
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        LinuxAcademyIE()
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e)

if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:53:49.463436
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Unit test for constructor of class LinuxAcademyIE
    """
    ie = LinuxAcademyIE()
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2022-06-14 16:53:50.531361
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from . import LinuxAcademyIE
    IE = LinuxAcademyIE()

# Generated at 2022-06-14 16:53:53.409096
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Unit test for constructor of class LinuxAcademyIE"""
    try:
        LinuxAcademyIE('test')
    except Exception:
        assert False, 'Initialization failed'

