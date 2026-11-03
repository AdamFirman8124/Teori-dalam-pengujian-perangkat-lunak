

# Generated at 2026-11-02 11:23:19.291257
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie is not None
    assert ie._VALID_URL is not None
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.ie_key() == 'LinuxAcademy'
    # URL matching
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert ie.suitable('http://www.linuxacademy.com/cp/modules/view/id/154')

# Generated at 2026-11-02 11:29:00.063328
# Unit test for constructor of class LinuxAcademyIE