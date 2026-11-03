

# Generated at 2026-11-02 19:18:46.214674
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # nonce:989385f3
    ie = LinuxAcademyIE(downloader=None)

    # Constructor should initialize the base state correctly
    assert ie._downloader is None
    assert ie._cache == {}

    # IE_NAME / ie_key derived from the class name
    assert ie.IE_NAME == 'LinuxAcademyIE'
    assert ie.ie_key() == 'LinuxAcademyIE'

    # Class-level configuration attributes
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'

    # _VALID_URL should be set and accept valid URLs
    assert ie._VALID_URL is not None
    valid_urls = [
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        'http://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'https://linuxacademy.com/cp/modules/view/id/154',
    ]
    for url in valid_urls:
        assert ie.suitable(url)

    # ...and reject unrelated URLs
    invalid_urls = [
        'https://linuxacademy.com/',
        'https://linuxacademy.com/cp/unknown/1',
        'https://example.com/cp/modules/view/id/154',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url)

# Generated at 2026-11-02 19:19:27.479970
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie is not None

    # Class/instance constants set at construction time
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # URLs that should match _VALID_URL
    for url in (
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'https://linuxacademy.com/cp/modules/view/id/154',
        'http://www.linuxacademy.com/cp/modules/view/id/154',
    ):
        assert ie.suitable(url), url

    # URLs that should NOT match _VALID_URL
    for url in (
        'https://linuxacademy.com/',
        'https://linuxacademy.com/cp/',
        'https://example.com/cp/courses/lesson/course/7971/lesson/2',
    ):
        assert not ie.suitable(url), url

    # Lesson URL capture groups
    mobj = re.match(LinuxAcademyIE._VALID_URL,
                    'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    # Course URL capture groups
    mobj = re.match(LinuxAcademyIE._VALID_URL,
                    'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None

# Generated at 2026-11-02 19:20:04.984837
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie.ie_key() == 'linuxacademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('http://www.linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')

# Generated at 2026-11-02 19:22:18.535657
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-11-02 19:24:05.616304
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-11-02 19:25:30.977025
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-11-02 19:27:35.301511
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():ie = LinuxAcademyIE()

    # Lesson URL should match and extract chapter/lesson ids