

# Generated at 2026-11-02 18:50:28.402360
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()
    assert extractor is not None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert extractor.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert extractor.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://linuxacademy.com/')
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert extractor._ORIGIN_URL == 'https://linuxacademy.com'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-11-02 18:52:36.518563
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()

    # Check class-level constants set in the constructor
    assert instance._NETRC_MACHINE == 'linuxacademy'
    assert instance._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert instance._ORIGIN_URL == 'https://linuxacademy.com'
    assert instance._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert instance.IE_NAME == 'linuxacademy'

    # Check that the extractor is suitable for its valid URLs
    assert instance.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert instance.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert instance.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert instance.suitable('https://www.linuxacademy.com/cp/modules/view/id/154')
    assert not instance.suitable('https://linuxacademy.com/cp/invalid/url')

    # Check _VALID_URL group extraction
    mobj = re.match(instance._VALID_URL, 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    mobj = re.match(instance._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None

# Generated at 2026-11-02 18:54:15.709352
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Check class identity and key
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie.ie_key() == 'LinuxAcademy'

    # Check constructor-initialized attributes
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # Check the URL pattern accepts valid URLs
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('http://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')

    # Check the URL pattern rejects invalid URLs
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://example.com/cp/courses/lesson/course/7971/lesson/2')

# Generated at 2026-11-02 18:56:31.221396
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie is not None
    assert ie.IE_NAME == 'LinuxAcademy'
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://www.example.com/cp/courses/lesson/course/7971/lesson/2')

# Generated at 2026-11-02 18:57:11.531036
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-11-02 18:57:54.171968
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # nonce:e174fce7
    ie = LinuxAcademyIE()
    assert ie is not None
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie._VALID_URL.match('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie._VALID_URL.match('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie._VALID_URL.match('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie._VALID_URL.match('https://linuxacademy.com/cp/other/path')

# Generated at 2026-11-02 18:59:18.566365
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Basic constructor attributes
    assert ie.IE_NAME == 'LinuxAcademy'
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

    # Valid URLs should match the _VALID_URL regex
    valid_urls = [
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        'http://www.linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'https://linuxacademy.com/cp/modules/view/id/154',
    ]
    for url in valid_urls:
        assert ie.suitable(url), url

    # Invalid URLs should not match
    invalid_urls = [
        'https://linuxacademy.com/',
        'https://example.com/cp/courses/lesson/course/7971/lesson/2',
        'https://linuxacademy.com/cp/courses/lesson/course/abc/lesson/2',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url), url

    # Regex group extraction for lesson URLs
    mobj = re.match(LinuxAcademyIE._VALID_URL, valid_urls[0])
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    # Regex group extraction for course (module) URLs
    mobj = re.match(LinuxAcademyIE._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None