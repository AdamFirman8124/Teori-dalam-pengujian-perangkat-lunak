

# Generated at 2022-06-14 16:45:27.780895
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:29.133872
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:36.487320
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    inst = LinuxAcademyIE()
    assert inst.name == 'linuxacademy'
    assert inst.ie_key() == 'LinuxAcademy'
    assert inst.description == 'Linux Academy account required'
    assert inst._VALID_URL == r'(?x)https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|modules/view/id/(?P<course_id>\d+))'
    assert inst._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:45:38.635488
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('LinuxAcademy', 'LinuxAcademy')

# Generated at 2022-06-14 16:45:41.824530
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy_ie = LinuxAcademyIE()
    assert linux_academy_ie is not None

# Test a lecture from course "Hands-On Deep Learning with PyTorch"

# Generated at 2022-06-14 16:45:43.538552
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test login
    LinuxAcademyIE._login()
    # Test initialization
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:46.738730
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxacademy_ie = LinuxAcademyIE('linuxacademy', 'Linux Academy', 'linuxacademy')
    assert linuxacademy_ie.ie_key() == 'LinuxAcademy'
    assert linuxacademy_ie.IE_NAME == 'LinuxAcademy'

# Generated at 2022-06-14 16:45:48.806770
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:53.345899
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    testurl = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    # Using constructor to create instance and then running tests
    test = LinuxAcademyIE(None)
    test._login()
    test._real_extract(testurl)

# Generated at 2022-06-14 16:46:03.390463
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()
    instance.initialize()
    # Test return values
    # unit test doesn't use real account infomation
    instance._login()
    assert isinstance(instance._real_initialize(), None)
    url_transparent_playlist = instance._real_extract('https://linuxacademy.com/cp/modules/view/id/154')
    assert isinstance(url_transparent_playlist, dict)
    assert url_transparent_playlist.get('_type') == 'playlist'
    assert isinstance(url_transparent_playlist.get('entries'), list)
    assert len(url_transparent_playlist.get('entries')) > 0
    assert isinstance(url_transparent_playlist.get('entries')[0], dict)

# Generated at 2022-06-14 16:46:41.070747
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test for constructor of class LinuxAcademyIE"""
    from .. import LinuxAcademyIE
    print(LinuxAcademyIE())

# Generated at 2022-06-14 16:46:42.816887
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        test = LinuxAcademyIE()
    except Exception as e:
        print (e)

# Generated at 2022-06-14 16:46:45.926358
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .common import InfoExtractor

    ie = InfoExtractor()
    assert ie.get_info_extractor(LinuxAcademyIE.ie_key()) is ie.get_info_extractor('linuxacademy')

# Generated at 2022-06-14 16:46:46.940952
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:47.940030
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(None, None)

# Generated at 2022-06-14 16:46:49.951688
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    expected_IE = LinuxAcademyIE()
    actual_IE = LinuxAcademyIE.ie_key()
    assert expected_IE == actual_IE

# Generated at 2022-06-14 16:46:58.637287
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    testIE = LinuxAcademyIE()
    assert testIE._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert testIE._ORIGIN_URL == 'https://linuxacademy.com'
    assert testIE._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert testIE._NETRC_MACHINE == 'linuxacademy'


# Generated at 2022-06-14 16:47:01.911675
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    with open('linuxacademy-login.json', 'r') as f:
        test_json = f.read()
    instance_test = LinuxAcademyIE()
    instance_test.to_screen(test_json)

# Generated at 2022-06-14 16:47:06.863302
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    a = LinuxAcademyIE()
    assert a.get_id
    assert a.get_id()
    assert a.get_id() == r'https://linuxacademy.com/cp/login/tokenValidateLogin/token/%s'
    b = a.get_id() % 'your_access_token'
    assert type(b) == str
    assert b
    assert b == 'https://linuxacademy.com/cp/login/tokenValidateLogin/token/your_access_token'

# Generated at 2022-06-14 16:47:07.746683
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:48:29.621881
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:48:37.343827
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2022-06-14 16:48:39.705529
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()
    assert isinstance(instance, InfoExtractor)


# Generated at 2022-06-14 16:48:41.551509
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    obj = object()
    assert ie.obj is obj
    return ie.obj


# Generated at 2022-06-14 16:48:44.433990
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = LinuxAcademyIE.construct_url('7971-2')
    assert url == 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'

# Generated at 2022-06-14 16:48:49.258682
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    video_id = '8059-2'
    url = 'https://linuxacademy.com/cp/courses/lesson/course/8059/lesson/2' #url of the video
    username, password = '', ''
    video = LinuxAcademyIE()
    video._login()
    video_info = video._real_extract(url)
    result_video_id = video_info['id'] #id of the video
    assert result_video_id == video_id #compare the video ids for equality


# Generated at 2022-06-14 16:48:54.935813
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():

    url = "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675"
    ie = LinuxAcademyIE("LinuxAcademyIE")
    ie._real_initialize()
    item = ie._real_extract(url)
    # print("title =", item.get("title"))
    

# Generated at 2022-06-14 16:49:02.004578
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert (ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize')
    assert (ie._ORIGIN_URL == 'https://linuxacademy.com')
    assert (ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx')
    assert (ie._NETRC_MACHINE == 'linuxacademy')
    assert (ie._real_initialize == LinuxAcademyIE._login)
    assert (ie._real_extract == LinuxAcademyIE._real_extract)

# Generated at 2022-06-14 16:49:11.858285
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .test_common import Test_LinuxAcademyIE
    ie = Test_LinuxAcademyIE(LinuxAcademyIE)
    module_info = ie.extract('https://linuxacademy.com/cp/modules/view/id/154')
    assert module_info['playlist_count'] == 41
    assert module_info['_type'] == 'playlist'
    # check if the URLs are valid
    for entry in module_info['entries']:
        assert entry['_type'] == 'url_transparent'
        assert entry['url']
        assert entry['ie_key'] == 'LinuxAcademy'
        assert entry['title']
        assert entry['id']
        assert entry['chapter']
        assert entry['chapter_id']
        assert entry['chapter_number']
    lesson_info = ie.ext

# Generated at 2022-06-14 16:49:15.999258
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test sending data to constructor of LinuxAcademyIE
    try:
        LinuxAcademyIE(username='invalid', password='invalid')
        assert False
    except Exception as e:
        assert isinstance(e, ExtractorError)
        assert e.args[0] == 'LinuxAcademy said: Your username and/or password were invalid. If you need help, email us at support@linuxacademy.com.'

# Generated at 2022-06-14 16:51:06.428548
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_ie = LinuxAcademyIE()
    assert isinstance(test_ie, object)

# Generated at 2022-06-14 16:51:07.963488
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('LinuxAcademyIE').Extractor('LinuxAcademyIE')

# Generated at 2022-06-14 16:51:09.456100
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:51:17.814731
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        from .common import _download
    except ImportError:
        from youtube_dl.compat import _download
    from youtube_dl import YoutubeDL
    from urllib.error import HTTPError
    from urllib.request import Request
    class MockYoutubeDL(YoutubeDL):
        def _opener_downloader_factory(self, *args, **kwargs):
            opener = super(MockYoutubeDL, self)._opener_downloader_factory(
                *args, **kwargs)
            return lambda *args, **kwargs: MockOpener(opener, *args, **kwargs)
    class MockOpener(object):
        def __init__(self, opener, *args, **kwargs):
            self.opener = opener
            self._args = args
            self._kwargs

# Generated at 2022-06-14 16:51:20.054650
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:51:21.198749
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE()

# Generated at 2022-06-14 16:51:23.875092
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, LinuxAcademyIE)

# Generated at 2022-06-14 16:51:33.365650
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?linuxacademy\.com/cp/courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)'
    assert ie._TESTS
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._real_initialize == ie._login
   

# Generated at 2022-06-14 16:51:42.519287
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from credentials import linuxacademy as linuxacademy_credentials
    LinuxAcademyIE._download_webpage = lambda self, url, video_id, note, errnote: 'response'
    info_extractor = LinuxAcademyIE({'username': linuxacademy_credentials['username'], 'password': linuxacademy_credentials['password']}, {'video_id': 'test'})

# Generated at 2022-06-14 16:51:49.631555
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_LinuxAcademyIE1 = LinuxAcademyIE()
    test_LinuxAcademyIE2 = LinuxAcademyIE()
    assert test_LinuxAcademyIE1 == test_LinuxAcademyIE2


# Pythonic class LinuxAcademyIE inherits from abstract class common
class_dict = LinuxAcademyIE.__dict__
for key, value in class_dict.items():
    print("%s : %s" % (key, value))


# Print the docstring of class LinuxAcademyIE
print("LinuxAcademyIE.__doc__ :",LinuxAcademyIE.__doc__)


# Print the name of the class LinuxAcademyIE
print("LinuxAcademyIE.__name__ :",LinuxAcademyIE.__name__)


# Print the module name

# Generated at 2022-06-14 16:53:49.651117
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxAcademyIE = LinuxAcademyIE()


# Generated at 2022-06-14 16:53:51.068606
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()
    assert instance is not None

# Generated at 2022-06-14 16:53:54.844151
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Create an instance of class LinuxAcademyIE
    linuxacademy_ie = LinuxAcademyIE()
    # Call a method to ensure instance was created
    linuxacademy_ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/')

# Generated at 2022-06-14 16:53:55.694109
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:54:03.438592
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from . import IETest
    # Test to create object

# Generated at 2022-06-14 16:54:05.480413
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    nm = LinuxAcademyIE()
    assert(nm is not None)  # Make pylint happy

# Generated at 2022-06-14 16:54:08.210233
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        LinuxAcademyIE(Username='username', Password='password')
    except Exception as e:
        log.debug(e)
        raise

# Generated at 2022-06-14 16:54:09.622768
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(LinuxAcademyIE.IE_NAME)

# Generated at 2022-06-14 16:54:12.751669
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE().get_info('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.get('id') == '1498-2'
    assert ie.get('title') == 'Introduction to Docker'

# Generated at 2022-06-14 16:54:21.627406
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():

    # Check creation of class LinuxAcademyIE
    linuxacademyIE = LinuxAcademyIE()

    # Check correct creation of instance of class LinuxAcademyIE and
    # method _real_initialize
    assert isinstance(linuxacademyIE, LinuxAcademyIE), 'linuxacademyIE is not an instance of class LinuxAcademyIE'
    assert hasattr(linuxacademyIE, '_real_initialize'), 'class LinuxAcademyIE has not method _real_initialize'
    assert callable(linuxacademyIE._real_initialize), 'method _real_initialize of class LinuxAcademyIE is not callable'

    # Check correct creation of instance of class LinuxAcademyIE and
    # method _login