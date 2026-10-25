

# Generated at 2026-10-24 15:09:30.361419
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    # URL pattern compiles and matches expected forms
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

# Generated at 2026-10-24 15:09:48.489051
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Act: constructor should work with no args (downloader=None)
    ie = LinuxAcademyIE()

    # Assert: instance created correctly
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, LinuxAcademyIE)

    # Assert: class-level configuration preserved on instance
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert isinstance(ie._VALID_URL, str)

    # Assert: downloader defaults to None
    assert ie._downloader is None

# Generated at 2026-10-24 15:09:50.902934
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:09:53.314247
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:09:55.890918
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:09:58.303606
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:00.717423
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:03.290761
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:05.702206
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:08.114875
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:10.530356
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:12.942641
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:15.357866
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:17.771456
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:20.187250
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:22.597771
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:25.010681
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:27.423092
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:29.838616
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:32.252792
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:34.667487
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:37.081375
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:39.491798
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:41.906066
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:44.319159
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:46.734379
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:49.148117
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:51.562975
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:53.978116
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:56.390875
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:10:58.806264
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:01.220705
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:03.637123
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:06.053538
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:17.266081
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():ie = LinuxAcademyIE()

# Generated at 2026-10-24 15:11:33.855017
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    # URL pattern compiles and matches expected forms
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

# Generated at 2026-10-24 15:11:36.270247
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:38.683852
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:41.097794
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:43.509612
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:45.923588
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:48.492279
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:50.909028
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:53.325094
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:55.740341
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:11:58.154285
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:00.568853
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:02.982925
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:05.410751
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:07.822247
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:10.235060
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:12.648271
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:15.062400
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:17.474412
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:19.888630
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:22.301601
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:24.714778
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:27.127043
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:29.542155
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:31.954749
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:12:48.710372
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    # URL pattern compiles and matches expected forms
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

# Generated at 2026-10-24 15:13:05.299222
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Act: constructor should work with no args (downloader=None)
    ie = LinuxAcademyIE()

    # Assert: instance created correctly
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, LinuxAcademyIE)

    # Assert: class-level configuration preserved on instance
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert isinstance(ie._VALID_URL, str)

    # Assert: downloader defaults to None
    assert ie._downloader is None

# Generated at 2026-10-24 15:13:07.714428
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:10.126859
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:12.684732
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:15.102705
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:17.514135
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:19.928907
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:22.344407
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:24.759400
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:27.174854
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:29.742473
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:32.155746
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:34.568947
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:36.980849
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:39.393012
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:41.808441
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:44.219714
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:46.633698
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:49.050554
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:51.458730
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:53.872232
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:56.285525
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:13:58.698900
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:01.120270
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:03.533565
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:05.950647
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:08.365619
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:10.781616
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:13.197109
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:15.612356
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:18.025766
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:20.437803
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:22.851454
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:25.267987
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:27.675060
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:30.092791
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:32.506090
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:14:49.274454
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Act: constructor should work with no args (downloader=None)
    ie = LinuxAcademyIE()

    # Assert: instance created correctly
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, LinuxAcademyIE)

    # Assert: class-level configuration preserved on instance
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert isinstance(ie._VALID_URL, str)

    # Assert: downloader defaults to None
    assert ie._downloader is None

# Generated at 2026-10-24 15:15:05.721998
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    # Act: constructor should work with no args (downloader=None)
    ie = LinuxAcademyIE()

    # Assert: instance created correctly
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, LinuxAcademyIE)

    # Assert: class-level configuration preserved on instance
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert isinstance(ie._VALID_URL, str)

    # Assert: downloader defaults to None
    assert ie._downloader is None

# Generated at 2026-10-24 15:15:08.136861
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:10.548983
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:12.961680
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:15.375439
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:17.788351
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:20.201032
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:22.615150
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:25.027334
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:27.440004
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:29.853016
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:32.266121
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:34.677157
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:37.090475
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:39.503736
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:41.919232
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:44.335253
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:46.750171
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:49.164486
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:51.576875
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:53.990310
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:15:56.401735
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:33.608471
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, LinuxAcademyIE)
    assert hasattr(ie, '_downloader')
    assert LinuxAcademyIE.ie_key() == 'LinuxAcademy'
    assert ie.ie_key() == 'LinuxAcademy'
    assert ie._VALID_URL
    assert ie._AUTHORIZE_URL == 'https://login.linuxacademy.com/authorize'
    assert ie._ORIGIN_URL == 'https://linuxacademy.com'
    assert ie._CLIENT_ID == 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 3
    ie2 = LinuxAcademyIE(None)
    assert isinstance(ie2, LinuxAcademyIE)
    assert ie2.ie_key() == 'LinuxAcademy'

# Generated at 2026-10-24 15:16:36.022933
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:38.435634
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:41.162372
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:43.573825
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:46.167978
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:48.549824
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:50.967467
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:53.381503
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:55.794793
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:16:58.207888
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:00.620844
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:03.033905
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:05.447399
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:07.860762
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:10.272891
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:12.685503
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:15.099048
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:17.511154
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:19.921954
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:22.335936
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:24.747825
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:27.159538
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:29.845844
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():ie = LinuxAcademyIE()

# Generated at 2026-10-24 15:17:46.388993
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    # URL pattern compiles and matches expected forms
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

# Generated at 2026-10-24 15:17:51.076642
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:53.644770
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:56.057758
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:17:58.471144
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:00.884706
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:03.301865
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:05.715019
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:08.326081
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:10.736110
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:13.150712
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:15.563924
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:17.976746
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:20.390261
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:22.803089
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:25.216112
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:27.629248
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:30.047830
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:32.457857
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:34.880869
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:37.283009
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:39.697567
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:42.108766
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:44.524331
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:46.939575
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:49.352411
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:51.765284
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:18:54.179273
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:01.065205
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():ie = LinuxAcademyIE()

# Generated at 2026-10-24 15:19:08.412859
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    # URL pattern compiles and matches expected forms
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

# Generated at 2026-10-24 15:19:09.854089
# Unit test for constructor of class LinuxAcademyIE
def test_LinuxAcademyIE():
    ie = LinuxAcademyIE()
    assert ie.IE_NAME == 'LinuxAcademy'
    assert ie._NETRC_MACHINE == 'linuxacademy'
    # URL pattern compiles and matches expected forms
    assert ie.suitable('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675')
    assert ie.suitable('https://linuxacademy.com/cp/modules/view/id/154')
    assert not ie.suitable('https://linuxacademy.com/cp/other/page')

# Generated at 2026-10-24 15:19:12.365979
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:14.779945
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:17.193003
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:19.606299
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:22.019944
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:24.432585
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:26.848137
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:29.260511
# Unit test for constructor of class LinuxAcademyIE

# Generated at 2026-10-24 15:19:31.673951
# Unit test for constructor of class LinuxAcademyIE