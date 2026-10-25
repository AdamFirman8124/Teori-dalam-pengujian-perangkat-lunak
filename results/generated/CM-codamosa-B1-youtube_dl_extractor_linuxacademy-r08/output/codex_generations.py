

# Generated at 2026-10-24 20:07:26.051963
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:28.466182
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:30.889035
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:33.306936
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:35.722472
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:38.137684
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:40.554656
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:42.971778
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:45.389623
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:47.807556
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:07:55.809007
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():extractor = LinuxAcademyIE(None)

# Generated at 2026-10-24 20:08:06.368609
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

# Generated at 2026-10-24 20:08:14.340368
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:08:21.611815
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')

# Generated at 2026-10-24 20:08:30.623640
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:08:33.043007
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:35.465223
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:37.884163
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:40.482156
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:42.902021
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:45.320396
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:47.735776
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:50.153689
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:52.569281
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:54.990040
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:57.408210
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:08:59.823156
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:02.239370
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:04.656213
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:07.075901
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:09.491664
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:16.410463
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():extractor = LinuxAcademyIE()

# Generated at 2026-10-24 20:09:25.725668
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')

# Generated at 2026-10-24 20:09:36.008074
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'

    lesson_match = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert lesson_match is not None
    assert lesson_match.group('chapter_id') == '7971'
    assert lesson_match.group('lesson_id') == '2'
    assert lesson_match.group('course_id') is None

    course_match = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert course_match is not None
    assert course_match.group('course_id') == '154'

# Generated at 2026-10-24 20:09:38.427454
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:40.845561
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:43.261724
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:45.681658
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:48.106688
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:50.688552
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:53.103656
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:09:55.527511
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:01.860119
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():extractor = LinuxAcademyIE()

# Generated at 2026-10-24 20:10:14.296277
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:10:22.523991
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:10:24.943369
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:27.360438
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:29.777037
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:32.198325
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:34.613816
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:37.029955
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:39.446041
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:41.862865
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:44.279955
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:46.696430
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:49.112123
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:51.530016
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:53.945536
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:56.361210
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:10:58.779027
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:01.195987
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:09.753767
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():extractor = LinuxAcademyIE(None)

# Generated at 2026-10-24 20:11:23.579264
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

# Generated at 2026-10-24 20:11:32.076640
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor.suitable(
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
    assert extractor.suitable(
        'https://linuxacademy.com/cp/modules/view/id/154')
    assert not extractor.suitable('https://example.com/video/154')

# Generated at 2026-10-24 20:11:34.495523
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:36.926603
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:39.345927
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:41.763340
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:44.179348
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:46.599351
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:49.015448
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:51.431767
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:53.849829
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:56.268784
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:11:58.684435
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:01.099564
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:03.534032
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:05.936002
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:08.355764
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:10.775456
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:13.193021
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:15.609998
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:18.651218
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:21.065416
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:23.480846
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:25.897716
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:28.314481
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:30.733078
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:33.149491
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:35.566132
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:37.982545
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:40.398268
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:42.812869
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:45.229093
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:47.645910
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:50.064540
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:52.483292
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:54.899848
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:57.314103
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:12:59.731004
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:02.147720
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:04.565166
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:06.982369
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:09.400747
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:11.815535
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:14.235741
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:16.649721
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:19.067802
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:21.482571
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:23.897483
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:26.312202
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:28.727983
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:33.556139
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:35.974127
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:38.392861
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:40.811018
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:43.231095
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:45.648844
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:48.064391
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:50.481611
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:13:52.897887
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:00.165637
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():extractor = LinuxAcademyIE()

# Generated at 2026-10-24 20:14:08.373834
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()
    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:14:17.862607
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:14:26.873625
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:14:30.266010
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:32.695816
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:35.112998
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:37.534615
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:39.954775
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:42.378485
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:44.802046
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:47.217951
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:49.639675
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:14:58.993885
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:01.411485
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:03.826225
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:06.243814
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:08.659989
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:11.076574
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:13.493308
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:15.911783
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:18.329013
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:15:28.314854
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    downloader = object()

    extractor = LinuxAcademyIE(downloader)

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 20:15:39.270099
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    assert isinstance(ie, LinuxAcademyIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:15:48.588744
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor._NETRC_MACHINE == 'linuxacademy'
    assert extractor._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'

# Generated at 2026-10-24 20:15:57.497859
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    extractor = LinuxAcademyIE()

    assert isinstance(extractor, LinuxAcademyIE)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'LinuxAcademy'
    assert extractor._NETRC_MACHINE == 'linuxacademy'

# Generated at 2026-10-24 20:15:59.919777
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:02.495934
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:04.910882
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:07.334855
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:09.749226
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:12.167309
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:14.584753
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:17.189992
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:19.608655
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:35.666177
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:38.083612
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:40.501441
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:42.915740
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:45.333707
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:47.756994
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:50.171894
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:52.585734
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:55.001788
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:57.418662
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:16:59.836854
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:02.252866
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:04.667845
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:07.089619
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:09.504781
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:11.923278
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:14.343615
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:16.755413
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:19.174572
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 20:17:26.987383
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():ie = LinuxAcademyIE()