

# Generated at 2026-11-02 17:32:09.573439
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Unit test for constructor of class LinuxAcademyIE"""
    ie = LinuxAcademyIE()

    # netrc machine and extractor key
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert LinuxAcademyIE.ie_key() == 'linuxacademy'

    # authentication endpoints and client id
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # URLs that must match _VALID_URL
    for url in (
            'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
            'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
            'https://linuxacademy.com/cp/modules/view/id/154',
            'http://www.linuxacademy.com/cp/modules/view/id/154'):
        assert re.match(ie._VALID_URL, url) is not None, url

    # URLs that must not match _VALID_URL
    for url in (
            'https://linuxacademy.com/',
            'https://linuxacademy.com/cp/courses/lesson/course/7971',
            'https://example.com/cp/courses/lesson/course/1498/lesson/2'):
        assert re.match(ie._VALID_URL, url) is None, url

    # lesson URL group extraction
    mobj = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    # course URL group extraction
    mobj = re.match(
        ie._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None

# Generated at 2026-11-02 17:33:55.109166
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')

# Generated at 2026-11-02 17:35:15.088036
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()

    # Class attributes should be properly initialized
    assert instance._NETRC_MACHINE == 'linuxacademy'
    assert instance._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert instance._ORIGIN_URL == 'https://linuxacademy.com'
    assert instance._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert instance.IE_NAME == 'LinuxAcademy'
    assert instance.ie_key() == 'LinuxAcademy'

    # _VALID_URL should match supported URL forms
    assert instance.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert instance.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert instance.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert instance.suitable('https://www.linuxacademy.com/cp/modules/view/id/154')

    # _VALID_URL should reject unsupported URL forms
    assert not instance.suitable('https://linuxacademy.com/other/path')
    assert not instance.suitable('https://example.com/cp/modules/view/id/154')

# Generated at 2026-11-02 17:37:02.988797
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Constructor should initialize a working extractor instance
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # Lesson URL should match with chapter/lesson ids captured
    m = ie._match_valid_url(
        'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert m.group('chapter_id') == '1498'
    assert m.group('lesson_id') == '2'
    assert m.group('course_id') is None

    # Lesson URL with module suffix should also match
    m = ie._match_valid_url(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert m.group('chapter_id') == '7971'
    assert m.group('lesson_id') == '2'

    # Course/module URL should match with course id captured
    m = ie._match_valid_url(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert m.group('course_id') == '154'
    assert m.group('chapter_id') is None
    assert m.group('lesson_id') is None

    # www. prefix should be accepted
    assert ie.suitable('https://www.linuxacademy.com/cp/modules/view/id/154')

    # Non-matching URLs should be rejected
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')
    assert not ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971')

# Generated at 2026-11-02 17:38:56.299794
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Class-level attributes set in the constructor path
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._WORKING is not False

    # URLs that must match _VALID_URL
    valid_urls = [
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        'https://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'http://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'https://linuxacademy.com/cp/modules/view/id/154',
        'https://www.linuxacademy.com/cp/modules/view/id/154',
    ]
    for url in valid_urls:
        assert re.match(ie._VALID_URL, url) is not None, url

    # URLs that must not match _VALID_URL
    invalid_urls = [
        'https://linuxacademy.com/',
        'https://linuxacademy.com/cp/courses/lesson/course/7971',
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/',
        'https://example.com/cp/courses/lesson/course/7971/lesson/2',
        'https://linuxacademy.com/cp/modules/view/id/',
    ]
    for url in invalid_urls:
        assert re.match(ie._VALID_URL, url) is None, url

    # Named groups for the lesson path
    mobj = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert mobj.group('chapter_id') == '1498'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    # Named groups for the course (module) path
    mobj = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None

# Generated at 2026-11-02 17:41:19.837365
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Basic extractor attributes
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'

    # URLs that must match _VALID_URL
    valid_urls = [
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'https://linuxacademy.com/cp/modules/view/id/154',
        'http://www.linuxacademy.com/cp/modules/view/id/154',
    ]
    for url in valid_urls:
        assert ie.suitable(url), url

    # URLs that must NOT match _VALID_URL
    invalid_urls = [
        'https://linuxacademy.com/',
        'https://linuxacademy.com/cp/',
        'https://linuxacademy.com/cp/courses/lesson/course/',
        'https://example.com/cp/modules/view/id/154',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url), url

    # Regex group extraction for the lesson/course path
    mobj = re.match(
        LinuxAcademyIE._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj is not None
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    # Regex group extraction for the module (course) path
    mobj = re.match(
        LinuxAcademyIE._VALID_URL,
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj is not None
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None