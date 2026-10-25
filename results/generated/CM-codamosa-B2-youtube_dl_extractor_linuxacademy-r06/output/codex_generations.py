

# Generated at 2026-10-24 20:36:39.193455
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:36:41.609357
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:36:44.024598
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:36:46.442267
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:36:54.053846
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():extractor = LinuxAcademyIE()

# Generated at 2026-10-24 20:37:02.979196
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    ie = LinuxAcademyIE(downloader)

    assert isinstance(ie, LinuxAcademyIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is downloader

    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._NETRC_MACHINE == 'linuxacademy'

    assert ie.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert ie.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:37:16.767256
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-24 20:37:26.208556
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:37:34.809612
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:37:41.465268
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._VALID_URL == LinuxAcademyIE._VALID_URL
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:37:50.614469
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:37:58.454315
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:38:07.170683
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._ORIGIN_URL == 'https://linuxacademy.com'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:38:17.817992
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:38:27.353612
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:38:35.634361
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    assert isinstance(ie, LinuxAcademyIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert ie.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:38:44.030748
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
    )

# Generated at 2026-10-24 20:38:53.763939
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert extractor._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert extractor._ORIGIN_URL == 'https://linuxacademy.com'

# Generated at 2026-10-24 20:39:02.165511
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:39:12.119226
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    assert isinstance(ie, LinuxAcademyIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert ie.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:39:22.419436
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-24 20:39:30.725608
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
    )

# Generated at 2026-10-24 20:39:40.147234
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:39:49.055753
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:39:58.886528
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:40:14.349094
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
    )

# Generated at 2026-10-24 20:40:23.564377
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-24 20:40:32.679390
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:40:42.419513
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:40:51.728571
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:41:01.130710
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:41:10.364554
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:41:16.900995
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor.IE_NAME == 'linuxacademy'
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')

# Generated at 2026-10-24 20:41:27.469771
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID
    assert re.match(
        extractor._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
    )

# Generated at 2026-10-24 20:41:35.565097
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    assert isinstance(ie, LinuxAcademyIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:41:44.665745
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID
    assert extractor._VALID_URL

# Generated at 2026-10-24 20:41:53.167083
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:42:00.742949
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:42:09.960537
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:42:19.175842
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'

    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable(
        'https://example.com/cp/modules/view/id/154')

# Generated at 2026-10-24 20:42:26.444675
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID

# Generated at 2026-10-24 20:42:36.208634
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:42:44.673866
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:42:47.097053
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:42:49.722672
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:42:52.145982
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:43:00.135345
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():extractor = LinuxAcademyIE()

# Generated at 2026-10-24 20:43:05.566482
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 20:43:14.271067
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-24 20:43:24.103014
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is None
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
    )
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154'
    )
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:43:39.155811
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:43:46.518098
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:43:49.051202
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:43:51.468545
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:43:53.886721
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:44:02.087155
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():downloader = object()

# Generated at 2026-10-24 20:44:13.269084
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.IE_NAME == 'linuxacademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:44:22.532689
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:44:38.030995
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable(
        'https://example.com/cp/modules/view/id/154')

# Generated at 2026-10-24 20:44:46.941573
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 20:44:56.155393
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:45:05.370952
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert extractor._ORIGIN_URL == 'https://linuxacademy.com'

# Generated at 2026-10-24 20:45:14.691036
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    assert isinstance(ie, LinuxAcademyIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID
    assert re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
    )

# Generated at 2026-10-24 20:45:24.147734
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is None
    assert extractor._match_valid_url(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
    ) is not None

# Generated at 2026-10-24 20:45:38.753215
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:45:49.300810
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:45:51.838670
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:45:54.257121
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:45:56.680751
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:46:06.579701
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:46:16.028182
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:46:29.563305
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:46:39.374989
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert extractor._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert extractor._ORIGIN_URL == 'https://linuxacademy.com'