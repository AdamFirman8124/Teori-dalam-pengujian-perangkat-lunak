

# Generated at 2026-11-02 08:05:32.521720
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')
    assert LinuxAcademyIE._match_valid_url('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2') is not None
    assert LinuxAcademyIE._match_valid_url('https://www.linuxacademy.com/cp/modules/view/id/154') is not None
    mobj = LinuxAcademyIE._match_valid_url('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert mobj.group('chapter_id') == '1498'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None
    mobj = LinuxAcademyIE._match_valid_url('https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('course_id') == '154'

# Generated at 2026-11-02 08:06:26.732100
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test that the extractor can be instantiated
    ie = LinuxAcademyIE()

    # Test class attributes set in constructor/class body
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # Test _VALID_URL matching for lesson/course URLs
    m = re.match(LinuxAcademyIE._VALID_URL, 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert m is not None
    assert m.group('chapter_id') == '7971'
    assert m.group('lesson_id') == '2'
    assert m.group('course_id') is None

    # Test URL without trailing module
    m = re.match(LinuxAcademyIE._VALID_URL, 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert m is not None
    assert m.group('chapter_id') == '1498'
    assert m.group('lesson_id') == '2'

    # Test www prefix
    m = re.match(LinuxAcademyIE._VALID_URL, 'https://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert m is not None

    # Test module (course) URL
    m = re.match(LinuxAcademyIE._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert m is not None
    assert m.group('course_id') == '154'
    assert m.group('chapter_id') is None
    assert m.group('lesson_id') is None

    # Test http scheme
    m = re.match(LinuxAcademyIE._VALID_URL, 'http://linuxacademy.com/cp/modules/view/id/154')
    assert m is not None

    # Test suitable() classmethod
    assert LinuxAcademyIE.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert LinuxAcademyIE.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not LinuxAcademyIE.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')
    assert not LinuxAcademyIE.suitable('https://linuxacademy.com/other/path')

    # Test ie_key
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'

# Generated at 2026-11-02 08:10:23.747888
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._VALID_URL is not None
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')

# Generated at 2026-11-02 08:12:19.807030
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test the constructor of LinuxAcademyIE with a valid URL."""
    ie = LinuxAcademyIE('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://example.com/not/linuxacademy')
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-11-02 08:13:06.477518
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Class-level attributes set at construction time
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.working() is True

    # _VALID_URL matching for lesson URLs
    mobj = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj is not None
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    mobj = re.match(
        ie._VALID_URL,
        'https://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert mobj is not None
    assert mobj.group('chapter_id') == '1498'
    assert mobj.group('lesson_id') == '2'

    # _VALID_URL matching for course (module) URLs
    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj is not None
    assert mobj.group('course_id') == '154'

    # _VALID_URL should reject unrelated URLs
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')
    assert not ie.suitable('https://linuxacademy.com/cp/modules/other/id/154')

    # newly constructed instance has no cookies / auth material yet
    assert ie._get_login_info() == (None, None)

# Generated at 2026-11-02 08:14:05.178785
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Class-level attributes are set correctly
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # The extractor recognizes its supported URL forms
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://www.linuxacademy.com/cp/modules/view/id/154')
    assert ie.suitable('http://linuxacademy.com/cp/modules/view/id/154')

    # And rejects unrelated URLs
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')
    assert not ie.suitable('https://linuxacademy.com/')

    # Regex groups extract the expected IDs
    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert mobj.group('chapter_id') == '1498'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None