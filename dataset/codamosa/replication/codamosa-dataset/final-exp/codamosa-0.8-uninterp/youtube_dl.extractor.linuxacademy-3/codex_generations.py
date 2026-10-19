

# Generated at 2022-06-14 16:45:27.336462
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    with LinuxAcademyIE() as ie:
        assert ie.IE_NAME == 'linuxacademy'

# Generated at 2022-06-14 16:45:34.903866
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Constructor of class LinuxAcademyIE
    linuxAcademyIE = LinuxAcademyIE()
    # Validate url
    url = "https://www.linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675"
    assert linuxAcademyIE._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?linuxacademy\.com/cp/
                        (?:
                            courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)|
                            modules/view/id/(?P<course_id>\d+)
                        )
                    '''
    # Validate result of initializing
    assert linuxAcademyIE._real_initial

# Generated at 2022-06-14 16:45:38.320819
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """Test constructor of class LinuxAcademyIE"""
    LinuxAcademyIE(InfoExtractor)

# Generated at 2022-06-14 16:45:40.228082
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    f = LinuxAcademyIE()
    f._real_initialize()


# Generated at 2022-06-14 16:45:42.203868
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'

# Generated at 2022-06-14 16:45:46.408046
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_url = 'https://linuxacademy.com/cp/modules/view/id/154'

# Generated at 2022-06-14 16:45:57.275396
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    infoextractors = [LinuxAcademyIE.ie_key()]

# Generated at 2022-06-14 16:46:01.824577
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Initialize
    instance = LinuxAcademyIE()
    assert instance.ie_key() is LinuxAcademyIE.ie_key()


# Generated at 2022-06-14 16:46:07.108714
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE._NETRC_MACHINE == 'linuxacademy'
    assert LinuxAcademyIE._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert LinuxAcademyIE._ORIGIN_URL == 'https://linuxacademy.com'
    assert LinuxAcademyIE._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'

# Generated at 2022-06-14 16:46:10.379842
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    try:
        import ClientCookie
    except ImportError:
        raise unittest.SkipTest('ClientCookie not installed.')
    assert LinuxAcademyIE()

# Generated at 2022-06-14 16:46:31.549736
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:46:33.353452
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()._login()

# Generated at 2022-06-14 16:46:35.108918
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linux_academy = LinuxAcademyIE()
    assert linux_academy is not None

# Generated at 2022-06-14 16:46:37.123046
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    linuxacademy_ie = LinuxAcademyIE()
    assert linuxacademy_ie._VALID_URL is not None
    assert linuxacademy_ie._TESTS is not None

test_LinuxAcademyIE()

# Generated at 2022-06-14 16:46:39.486731
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    print(LinuxAcademyIE)

# Generated at 2022-06-14 16:46:41.507785
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    le = LinuxAcademyIE()
    if le.get_username() is None:
        raise Exception('LinuxAcademyIE is not correctly configured!')

# Generated at 2022-06-14 16:46:43.110857
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    instance = LinuxAcademyIE()
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:46:45.474594
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test for malformed URL
    with pytest.raises(ExtractorError):
        LinuxAcademyIE('https://linuxacademy.com')

# Generated at 2022-06-14 16:46:49.396916
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Test LinuxAcademyIE.linuxacademy_ie()
    LinuxAcademyIE.linuxacademy_ie()
    # Test LinuxAcademyIE.linuxacademy_ie() again, the second time,
    # without creating a new class. This should not fail.
    LinuxAcademyIE.linuxacademy_ie()

# Generated at 2022-06-14 16:47:01.457195
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    git_url = 'https://github.com/ytdl-org/youtube-dl/blob/master/test/testdata/test_linuxacademy.com.py'
    IE_name = 'linuxacademy'

    ie = LinuxAcademyIE(test_url)
    # test _VALID_URL

# Generated at 2022-06-14 16:47:51.998593
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = "https://linuxacademy.com/cp/courses/lesson/course/223/lesson/1"
    content = LinuxAcademyIE()._real_extract(url)
    with open("./test/test_output.json", "w") as outfile:
        json.dump(content, outfile, indent=2)


# Generated at 2022-06-14 16:47:58.166818
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.get_domain() == "linuxacademy.com"
    assert ie.get_ie_key() == 'LinuxAcademy'
    assert ie.get_video_regex().match('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.get_playlist_regex().match('https://linuxacademy.com/cp/modules/view/id/154')

# Generated at 2022-06-14 16:47:59.124932
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    return LinuxAcademyIE()

# Generated at 2022-06-14 16:48:03.610645
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Tested with https://linuxacademy.com/cp/modules/view/id/154
    linuxacademy_ie = LinuxAcademyIE(None) 
    assert linuxacademy_ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert linuxacademy_ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2022-06-14 16:48:08.352398
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Without credential
    ie = LinuxAcademyIE()
    assert ie._downloader is None

    # With credential
    ie = LinuxAcademyIE(downloader=True)
    assert ie._downloader is not None

# Generated at 2022-06-14 16:48:09.768320
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

# Generated at 2022-06-14 16:48:15.454571
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():

    # Test for invalid URL
    assert LinuxAcademyIE.suitable('htp://linuxacademy.com/cp/modules/view/id/154') == False, "Invalid URL"

    # Test for valid URL
    assert LinuxAcademyIE.suitable('https://linuxacademy.com/cp/modules/view/id/154'), "Valid URL"

# Generated at 2022-06-14 16:48:17.206299
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE('mkv_2_m4a').ie_key() == 'LinuxAcademy'

# Generated at 2022-06-14 16:48:24.159446
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # pylint: disable=unused-variable
    # pylint: disable=unused-argument
    class TestLinuxAcademyIE(object):
        IE = LinuxAcademyIE

        def test_ie_key(self):
            assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'

# Generated at 2022-06-14 16:48:24.755616
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE

# Generated at 2022-06-14 16:49:58.377009
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/modules/view/id/154'
    LinuxAcademyIE()._real_extract(url)

# Generated at 2022-06-14 16:50:00.253825
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    '''
    Test for the constructor of LinuxAcademyIE
    '''
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    obj = LinuxAcademyIE(url);
    assert(obj.username is None)
    assert(obj.password is None)

# Generated at 2022-06-14 16:50:10.292443
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'linuxacademy'
    assert ie.IE_DESC == 'LinuxAcademy'
    assert ie._VALID_URL == 'https?://(?:www\.)?linuxacademy\.com/cp/(?:courses/lesson/course/(?P<chapter_id>\\d+)/lesson/(?P<lesson_id>\\d+)|modules/view/id/(?P<course_id>\\d+))'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'

# Generated at 2022-06-14 16:50:11.681596
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() == 'linuxacademy'

# Generated at 2022-06-14 16:50:21.662618
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE("https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2")
    LinuxAcademyIE("https://linuxacademy.com/cp/modules/view/id/154")
    LinuxAcademyIE("https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675")
    LinuxAcademyIE("https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675","90","45")

# Generated at 2022-06-14 16:50:23.183658
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    from .test_linuxacademy import test_linuxacademy
    test_linuxacademy()

# Generated at 2022-06-14 16:50:33.877907
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    test_cases = iter([
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675',
        'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2',
        'https://linuxacademy.com/cp/modules/view/id/154',
    ])
    test_LinuxAcademyIE = LinuxAcademyIE()
    for url in test_cases:
        expected_result = LinuxAcademyIE._VALID_URL
        actual_result = test_LinuxAcademyIE._VALID_URL
        assert expected_result == actual_result, 'Expected result: ' + expected_result + ' Actual result: ' + actual_result
        test_LinuxAcademyIE._real_ext

# Generated at 2022-06-14 16:50:34.876243
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE({})

# Generated at 2022-06-14 16:50:43.949458
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    course_url = 'https://linuxacademy.com/cp/modules/view/id/154'
    lesson_url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    info_extractor = LinuxAcademyIE()
    try:
        assert(info_extractor._download_webpage(course_url, '154') != '')
        assert(info_extractor._download_webpage(lesson_url, '7971-2') != '')
    except ExtractorError as e:
        print(e)
        if isinstance(e.cause, compat_HTTPError) and e.cause.code == 401:
            error = info_extractor._parse_json(e.cause.read(), None)
            message = error.get

# Generated at 2022-06-14 16:50:51.257027
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # pylint: disable=protected-access
    # test class constructor
    linux_academy = LinuxAcademyIE._build_search_page(None, 'hello')
    assert linux_academy._SEARCH_PAGE == 'https://linuxacademy.com/search/search?q={}'
    assert linux_academy._NETRC_MACHINE == LinuxAcademyIE._NETRC_MACHINE
    assert linux_academy._VALID_URL == LinuxAcademyIE._VALID_URL
    assert linux_academy._USER_AGENT in LinuxAcademyIE._USER_AGENT
    linux_academy = LinuxAcademyIE._build_search_page(None, 'world')

# Generated at 2022-06-14 16:54:11.204828
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # If the constructor is changed to require credentials, this test will fail
    # and will remind you to update the test.
    LinuxAcademyIE(None)

# Generated at 2022-06-14 16:54:11.969804
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:54:12.978177
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    assert LinuxAcademyIE.ie_key() in InfoExtractor._ies

# Generated at 2022-06-14 16:54:13.731933
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE()

# Generated at 2022-06-14 16:54:15.815927
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    """
    Unit test for LinuxAcademyIE
    """
    assert LinuxAcademyIE.__name__ == "LinuxAcademyIE"

# Generated at 2022-06-14 16:54:21.349342
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # pylint: disable=line-too-long
    # example url
    lecture_url = "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675"
    # test constructor
    lec_ie = LinuxAcademyIE(lecture_url)
    assert lec_ie.ie_key() == "LinuxAcademy"
    assert lec_ie.info_extractors() == None

# Generated at 2022-06-14 16:54:22.768169
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    LinuxAcademyIE('LinuxAcademy', 'LinuxAcademy', 'need to be updated')

# Generated at 2022-06-14 16:54:23.846134
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Check that constructor succeeds without any errors
    i = LinuxAcademyIE()

# Generated at 2022-06-14 16:54:24.725789
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    iev = LinuxAcademyIE()

# Generated at 2022-06-14 16:54:29.219400
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    ie = LinuxAcademyIE()
    course_id, item_id = ie._real_extract(url)
    assert course_id == '7971-2'
    assert item_id == '7971-2'