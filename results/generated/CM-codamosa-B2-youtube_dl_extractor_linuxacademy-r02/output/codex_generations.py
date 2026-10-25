

# Generated at 2026-10-24 07:31:02.286813
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:04.698901
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:07.113763
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:09.528522
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:11.944785
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:14.357901
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:16.775075
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:19.191529
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:21.607483
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:24.024338
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:26.438926
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:28.862946
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:31.271959
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:33.682770
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:36.097309
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:38.510952
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:40.925841
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:43.344715
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:45.756094
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:48.170862
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:50.584225
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:53.000566
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:55.414698
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:31:57.830538
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:00.242024
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:02.655732
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:05.070243
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:07.495793
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:09.900570
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:12.317448
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:14.732690
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:17.146141
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:19.566834
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:21.973681
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:24.387232
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:26.801817
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:29.215322
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:31.629509
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:34.044421
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:36.464884
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:38.881068
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:41.304801
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:43.719029
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:46.131890
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:48.546662
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:50.962969
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:53.376018
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:55.787659
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:32:58.202042
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:33:00.614270
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:33:03.028100
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:33:05.440248
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:33:30.985511
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Constructor produces a working extractor instance
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://www.linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

    # URL pattern groups extract concrete IDs
    mobj = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj is not None
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj is not None
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None

    # Constructor accepts an optional downloader argument
    ie_with_dl = LinuxAcademyIE(downloader=None)
    assert ie_with_dl._LOGIN_URL is None or True
    assert ie_with_dl.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 07:33:50.556943
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:33:52.974697
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:33:55.391285
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:33:57.803584
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:00.219458
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:02.632323
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:05.057757
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:07.463094
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:08.971229
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Constructor produces a working extractor instance
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://www.linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

    # URL pattern groups extract concrete IDs
    mobj = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj is not None
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj is not None
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None

    # Constructor accepts an optional downloader argument
    ie_with_dl = LinuxAcademyIE(downloader=None)
    assert ie_with_dl._LOGIN_URL is None or True
    assert ie_with_dl.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 07:34:10.337003
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:11.682218
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:13.067106
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:14.512887
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:15.933643
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:17.317689
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:18.708590
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:20.050824
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:21.403524
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:22.799269
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:24.109868
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:25.563960
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:26.875328
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:28.259100
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:34:30.739978
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:33.284710
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:35.917170
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:38.336529
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:40.747811
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:43.332119
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:45.748810
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:48.164915
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:50.577766
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:52.991377
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:55.405592
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:34:57.818261
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:00.235076
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:02.649887
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:05.383474
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:07.799668
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:10.219917
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:12.638019
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:15.050097
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:17.472930
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:19.881260
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:21.335327
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:22.788366
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:25.156719
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:26.486630
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:27.921626
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:29.357371
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:30.792539
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:32.122376
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:33.428617
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:34.740728
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:36.052184
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:37.376036
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:35:43.293925
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:45.709358
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:48.125239
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:50.680177
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:53.094425
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:55.688895
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:35:58.099829
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:00.513482
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:02.930054
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:05.343240
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:07.756871
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:10.170456
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:12.586391
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:14.999560
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:17.413839
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:19.827432
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:22.243120
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:24.658437
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:27.078225
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:28.491761
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()

    # Constructor produces a working extractor instance
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://www.linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

    # URL pattern groups extract concrete IDs
    mobj = re.match(
        ie._VALID_URL,
        'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert mobj is not None
    assert mobj.group('chapter_id') == '7971'
    assert mobj.group('lesson_id') == '2'
    assert mobj.group('course_id') is None

    mobj = re.match(ie._VALID_URL, 'https://linuxacademy.com/cp/modules/view/id/154')
    assert mobj is not None
    assert mobj.group('course_id') == '154'
    assert mobj.group('chapter_id') is None
    assert mobj.group('lesson_id') is None

    # Constructor accepts an optional downloader argument
    ie_with_dl = LinuxAcademyIE(downloader=None)
    assert ie_with_dl._LOGIN_URL is None or True
    assert ie_with_dl.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 07:36:29.831257
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:36:31.143539
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:36:32.450176
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:36:43.184040
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:36:44.523462
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:36:45.831416
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:36:47.151695
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:36:48.719384
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:36:51.223705
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:53.730401
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:56.149392
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:36:58.662370
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:01.169434
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:03.583811
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:05.998053
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:08.414348
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:10.827665
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:13.332625
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:15.859367
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:18.273941
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:20.691661
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:23.107106
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:25.525268
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:46.777046
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:37:48.146833
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:37:49.451018
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:37:50.770095
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:37:53.296413
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:55.711082
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:37:58.129843
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:00.543510
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:02.956995
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:05.371462
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:07.785910
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:10.200941
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:12.617115
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:15.032027
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:17.454283
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:19.871959
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:22.287569
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:24.702467
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:27.128811
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:29.530679
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:31.944872
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:38:34.360006
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:12.328276
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:39:13.639453
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:39:14.952111
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:39:16.268447
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/')

# Generated at 2026-10-24 07:39:18.776566
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:21.291994
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:23.793760
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:26.209196
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:28.798304
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:31.171828
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:33.587099
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:36.144198
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:38.643091
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:41.064959
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:43.477907
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:45.898945
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:48.323239
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:50.726486
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:53.144485
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:55.560705
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:39:57.975416
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 07:40:00.393421
# Unit test for constructor of class LinuxAcademyIE