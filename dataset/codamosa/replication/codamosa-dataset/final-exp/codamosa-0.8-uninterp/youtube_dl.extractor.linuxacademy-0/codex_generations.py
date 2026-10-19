

# Generated at 2022-06-14 16:45:22.599188
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:24.438585
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert type(LinuxAcademyIE({})) is LinuxAcademyIE

# Generated at 2022-06-14 16:45:26.706819
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
	obj = LinuxAcademyIE("LinuxAcademyIE", True)

# Generated at 2022-06-14 16:45:29.030737
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Constructor for class LinuxAcademyIE
    LinuxAcademyIE('linuxacademy')

# Generated at 2022-06-14 16:45:37.604044
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_cases = [
        {
            'url_str': 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
            'chapter_id': '7971',
            'lecture_id': '2',
            'course_id': None,
        },
        {
            'url_str': 'https://linuxacademy.com/cp/modules/view/id/154',
            'chapter_id': None,
            'lecture_id': None,
            'course_id': '154',
        }
    ]

    for test_case in test_cases:
        test_obj = LinuxAcademyIE()
        mobj = re.match(test_obj._VALID_URL, test_case['url_str'])
       

# Generated at 2022-06-14 16:45:42.339593
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    global LinuxAcademyIE
    # Test without login
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    info = LinuxAcademyIE()._real_extract(url)
    assert info['id'] == '7971-2'
    assert info['duration'] == 304

# Generated at 2022-06-14 16:45:43.265643
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:45:44.624971
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy_obj = LinuxAcademyIE()

# Generated at 2022-06-14 16:45:45.857604
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.login() is None

# Generated at 2022-06-14 16:45:46.962020
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:46:27.897260
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.__name__ == 'LinuxAcademy'
    assert ie._VALID_URL == 'https?://(?:www\\.)?linuxacademy\\.com/cp/courses/lesson/course/(?P<chapter_id>\\d+)/lesson/(?P<lesson_id>\\d+)'
    assert ie._TTL == 86400


# Generated at 2022-06-14 16:46:29.240551
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():

    print(LinuxAcademyIE)


# Generated at 2022-06-14 16:46:36.943944
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == "linuxacademy"
    assert ie._VALID_URL == "https?://(?:www\\.)?linuxacademy\\.com/cp/courses/lesson/course/(?P<chapter_id>\\d+)/lesson/(?P<lesson_id>\\d+)"
    assert ie._TESTS == [{'url': 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'only_matching': True}]

# Generated at 2022-06-14 16:46:48.050208
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    e = LinuxAcademyIE()
    assert(e.IE_NAME == 'linuxacademy')
    assert(e.IE_DESC == 'LinuxAcademy')
    assert(e._VALID_URL == r'^https?://(?:www\.)?linuxacademy\.com/cp/'
                           r'courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|'
                           r'modules/view/id/(?P<course_id>\d+)$')
    assert(e.NETRC_MACHINE == 'linuxacademy')

    e = LinuxAcademyIE(None)
    assert(e.IE_NAME == 'linuxacademy')

# Generated at 2022-06-14 16:46:48.924066
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:46:49.963569
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()._login()

# Generated at 2022-06-14 16:46:55.129829
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():

    # Test for class LinuxAcademyIE
    instance = LinuxAcademyIE()
    assert isinstance(instance, LinuxAcademyIE) == True

    # Test for method _login of class LinuxAcademyIE
    assert LinuxAcademyIE._login(instance) == None

# Generated at 2022-06-14 16:46:56.157386
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:46:59.310896
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    def t(x):
        return x.lower()
    assert t(ie.ie_key()) == 'linuxacademy'

# Generated at 2022-06-14 16:47:01.505733
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    i = LinuxAcademyIE()
    assert i._CLIENT_ID is not None
    assert i._CLIENT_ID.strip() != ''

# Generated at 2022-06-14 16:48:28.392221
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy_ie = LinuxAcademyIE()
    assert not linux_academy_ie.login_page
    assert not linux_academy_ie.username
    assert not linux_academy_ie.password

# Generated at 2022-06-14 16:48:30.297892
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie_ = LinuxAcademyIE()
    assert str(ie_) == 'LinuxAcademy'

# Generated at 2022-06-14 16:48:37.674688
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test LinuxAcademyIE"""
    class Mock_LinuxAcademyIE_Download_Webpage_Handle(object):
        def geturl(self):
            return 'https://login.linuxacademy.com/login/callback'

    class Mock_LinuxAcademyIE_Download_Webpage(object):
        def __init__(self, *args, **kwargs):
            self.webpage = 'webpage'

        def __call__(self, *args, **kwargs):
            return self.webpage

    class Mock_LinuxAcademyIE_Parse_JSON(object):
        def __init__(self, *args, **kwargs):
            self.json = 'json'

        def __call__(self, *args, **kwargs):
            return self.json


# Generated at 2022-06-14 16:48:40.455785
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE('linuxacademyIE', 'LinuxAcademy Account Login').IE_NAME == 'linuxacademy'


# Generated at 2022-06-14 16:48:42.879248
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert ('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
            == LinuxAcademyIE()._VALID_URL)

# Generated at 2022-06-14 16:48:43.727055
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:48:50.158393
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.__class__.__name__ == 'LinuxAcademyIE'
    assert ie._menu_path == 'https://linuxacademy.com/cp/menu/raw_html'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2022-06-14 16:48:57.905019
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        import gcloud
    except ImportError:
        pass

    try:
        from google.cloud import storage
    except ImportError:
        pass

    try:
        import boto3
    except ImportError:
        pass

    try:
        import keyring
    except ImportError:
        pass

    try:
        import Credentials
    except ImportError:
        pass

    try:
        import ConfigParser
    except ImportError:
        pass

    LinuxAcademyIE()


if __name__ == '__main__':
    test_LinuxAcademyIE()

# Generated at 2022-06-14 16:49:04.966722
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    ie = LinuxAcademyIE(url)
    assert ie.is_logged_in() == False

    # Test: Login
    ie.authenticate()
    assert ie.is_logged_in() == True

    # Get the title of the video
    title = ie._get_title(url)
    assert title == 'What Is Data Science'

    # Get the description of the video
    description = ie._get_description(url)
    assert description == 'A little bit of history and an introduction to the course'

    # Get the duration of the video
    duration = ie._get_duration(url)
    assert duration == 304

    # Get the timestamp of the video

# Generated at 2022-06-14 16:49:08.341623
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Unit test for constructor of class LinuxAcademyIE
    """
    ie = LinuxAcademyIE(None)
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.thumbnail == 're:https?://.*\.png'

# Generated at 2022-06-14 16:50:59.103103
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_object = LinuxAcademyIE()
    try:
        test_object._login()
    except:
        print('Unit test for LinuxAcademyIE._login failed!')
    try:
        test_object._real_extract('https://linuxacademy.com/cp/modules/view/id/154')
    except:
        print('Unit test for LinuxAcademyIE._real_extract with URL https://linuxacademy.com/cp/modules/view/id/154 failed!')

# Generated at 2022-06-14 16:51:01.969031
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Create instance
    linux_academy_ie = LinuxAcademyIE()
    # Test
    linux_academy_ie._real_initialize()
    linux_academy_ie._real_extract("https://linuxacademy.com/cp/modules/view/id/154")

# Generated at 2022-06-14 16:51:10.111135
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # The only way to test info extraction is to provide credentials.
    # But no credentials should be provided to constructor by default.
    ies = LinuxAcademyIE._build_extractors()
    assert ies[0]._login_info is None

    # To test info extraction provide credentials
    ies = LinuxAcademyIE._build_extractors(
        username='INVALID_USERNAME', password='INVALID_PASSWORD')
    assert ies[0]._login_info == ('INVALID_USERNAME', 'INVALID_PASSWORD')

# Generated at 2022-06-14 16:51:11.981679
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'

# Generated at 2022-06-14 16:51:17.239981
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    la_ie = LinuxAcademyIE()
    assert la_ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert la_ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert la_ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert la_ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:51:20.624364
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE(None).IE_NAME == 'linuxacademy'


# Generated at 2022-06-14 16:51:23.220575
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Constructor test
    """
    ie = LinuxAcademyIE()


# Generated at 2022-06-14 16:51:24.142116
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE(None)

# Generated at 2022-06-14 16:51:25.093419
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:51:34.311089
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert 'a68a299ca9bb98d41cca5abc4d4ce22c' == LinuxAcademyIE() \
                                                ._download_webpage(
        'https://linuxacademy.com/cp/modules/view/id/154', None,
        'Downloading callback page')['__class__']['_module_dict']['md5'] \
        (LinuxAcademyIE()._search_regex(r'courseDescription\s(=|:)\s(["\'])(?P<value>(?:(?!\2).)+)\2',
        LinuxAcademyIE()._download_webpage('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2', None, 'Downloading authorize page'),
        'courseDesc', group='value'))