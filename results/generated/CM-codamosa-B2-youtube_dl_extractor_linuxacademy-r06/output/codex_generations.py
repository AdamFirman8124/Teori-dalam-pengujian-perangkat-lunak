

# Generated at 2026-11-03 03:18:04.161295
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie is not None
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie.IE_NAME is None
    assert ie.ie_name() == 'LinuxAcademy'
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie._VALID_URL is not None
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://example.com/cp/modules/view/id/154')

# Generated at 2026-11-03 03:19:34.682563
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/courses')
    assert not ie.suitable('https://example.com/cp/modules/view/id/154')
    assert ie._match_id('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2') == '7971-2'
    assert ie._match_id('https://linuxacademy.com/cp/modules/view/id/154') == '154'

# Generated at 2026-11-03 03:21:20.670871
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Constructor should initialize class attributes correctly
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # URLs that should match _VALID_URL
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('http://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert ie.suitable('http://www.linuxacademy.com/cp/modules/view/id/154')

    # URLs that should NOT match _VALID_URL
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://linuxacademy.com/cp/courses/lesson')
    assert not ie.suitable('https://example.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/modules/view/id/')

    # Verify regex group extraction for lesson URLs
    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    # Verify regex group extraction for course URLs
    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None
    assert mobj.group('course_id') == '154'

# Generated at 2026-11-03 03:23:41.267330
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # URL matching via _VALID_URL
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert ie.suitable('http://www.linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://linuxacademy.com/cp/')

    mobj = re.match(LinuxAcademyIE._VALID_URL,
                    'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    mobj = re.match(LinuxAcademyIE._VALID_URL,
                    'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None