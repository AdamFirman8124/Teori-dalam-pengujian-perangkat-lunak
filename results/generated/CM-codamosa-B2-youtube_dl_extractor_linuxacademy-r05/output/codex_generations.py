

# Generated at 2026-11-02 15:05:38.283616
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-11-02 15:07:41.451279
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._downloader is None
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie.ie_name() == 'LinuxAcademy'
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'
    assert ie.GEO_BYPASS is True

    lesson_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    assert ie.suitable(lesson_url)
    mobj = re.match(LinuxAcademyIE._VALID_URL, lesson_url)
    assert mobj.group('chapter_id', 'lesson_id', 'course_id') == ('7971', '2', None)

    course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    assert ie.suitable(course_url)
    mobj = re.match(LinuxAcademyIE._VALID_URL, course_url)
    assert mobj.group('chapter_id', 'lesson_id', 'course_id') == (None, None, '154')

    assert ie.suitable('http://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert not ie.suitable('https://linuxacademy.com/cp/something/else')
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')

    class FakeDownloader(object):
        pass

    downloader = FakeDownloader()
    ie2 = LinuxAcademyIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._NETRC_MACHINE == ie._NETRC_MACHINE

# Generated at 2026-11-02 15:12:01.074491
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Class-level configuration attributes
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.ie_name() == 'LinuxAcademy'
    assert ie._VALID_URL is not None

    # Lesson URL matching
    lesson_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    m = re.match(ie._VALID_URL, lesson_url)
    assert m is not None
    assert m.group('chapter_id') == '7971'
    assert m.group('lesson_id') == '2'
    assert m.group('course_id') is None

    # Lesson URL without trailing module
    lesson_url2 = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    m = re.match(ie._VALID_URL, lesson_url2)
    assert m is not None
    assert m.group('chapter_id') == '1498'
    assert m.group('lesson_id') == '2'

    # Course (module) URL matching
    course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    m = re.match(ie._VALID_URL, course_url)
    assert m is not None
    assert m.group('course_id') == '154'

    # www-prefixed URL
    assert re.match(ie._VALID_URL, 'https://www.linuxacademy.com/cp/modules/view/id/154') is not None

    # suitable() behavior
    assert ie.suitable(lesson_url)
    assert ie.suitable(course_url)
    assert not ie.suitable('https://example.com/video/123')
    assert not ie.suitable('https://linuxacademy.com/other/path')

    # Instance state initialization
    assert ie._downloader is None
    assert ie._login is not None
    assert ie._real_initialize is not None
    assert ie._real_extract is not None