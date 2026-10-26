

# Generated at 2026-10-25 08:11:14.565852
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:11:15.970318
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:11:17.432885
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:11:20.200756
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:22.733343
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:25.147921
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:27.708044
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:30.126104
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:32.542526
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:34.958035
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:37.373131
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:39.786677
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:42.199895
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:45.145816
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:47.505965
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:49.923375
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:52.340829
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:54.759145
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:57.173158
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:11:59.594067
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:02.008107
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:04.422739
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:06.841457
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:09.259877
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:11.675909
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:14.090846
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:16.510959
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:18.923057
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:21.342285
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:23.755961
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:26.175933
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:28.592214
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:31.006408
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:33.420281
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:35.841503
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:38.259280
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:40.671798
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:43.087466
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:45.504801
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:47.987980
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:50.436857
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:52.825110
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:55.240424
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:12:57.655785
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:00.060987
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:02.477267
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:04.895680
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:07.309463
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:09.730611
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:12.144325
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:14.558273
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:16.974584
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:19.388056
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:21.805068
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:24.222492
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:26.637124
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:29.052852
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:31.482641
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:33.901331
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:36.313779
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:38.729229
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:41.145766
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:43.565483
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:45.978216
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:48.392943
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:50.812619
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:53.231229
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:55.643668
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:13:58.061665
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:00.477639
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:02.993645
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:05.416619
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:07.787212
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:10.201876
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:12.616404
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:15.030936
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:17.450965
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:19.865988
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:22.280157
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:24.693514
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:27.201967
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:29.618868
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:32.031189
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:34.445352
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:36.863046
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:39.280074
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:41.696837
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:44.111023
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:46.527969
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:48.943352
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:51.426843
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:53.844206
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:56.260775
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:14:58.676336
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:01.088232
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:03.503980
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:05.921669
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:08.335898
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:10.749046
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:13.167917
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:15.585053
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:17.998838
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:20.415282
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:22.828560
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:25.244568
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:27.658754
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:30.145526
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:32.547007
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:34.965094
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:37.417686
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:39.827012
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:42.243714
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:44.660596
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:47.074221
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:49.488405
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:51.905343
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:54.321302
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:56.734522
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:15:59.148836
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:01.564929
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:03.980888
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:06.392998
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:08.807503
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:11.221863
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:13.635324
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:16.050881
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:18.462425
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:20.874488
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:23.287670
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:25.699379
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:28.112813
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:30.526986
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:32.941721
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:35.354285
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:37.769567
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:40.186257
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:42.604293
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:16:45.599826
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():ie = UDNEmbedIE()

# Generated at 2026-10-25 08:16:46.961752
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:16:48.390480
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:16:49.824328
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:16:51.216599
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:16:52.792065
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:16:54.329388
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:16:55.761825
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:16:58.355291
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:16:59.749395
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:17:01.190847
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:17:02.632312
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:17:04.161324
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:17:05.592443
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:17:07.130608
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:17:10.013335
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:12.594588
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:15.012208
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:17.428924
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:19.841667
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:22.255875
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:24.675842
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:27.093011
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:29.600729
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:35.322811
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:37.739870
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:40.155363
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:42.570053
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:44.987581
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:47.403159
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:49.816434
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:52.230542
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:54.645317
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:57.060261
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:17:59.474124
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:01.891350
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:04.308191
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:06.721957
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:09.139279
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:11.557624
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:13.967776
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:16.383280
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:18.797595
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:21.212278
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:23.637897
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:26.048181
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:28.532015
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:30.949450
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:18:36.795645
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from youtube_dl.extractor.udn import UDNEmbedIE

    # Constructor should succeed with no arguments
    ie = UDNEmbedIE()
    assert ie is not None
    assert ie.IE_NAME == 'udn:embed'
    assert ie.ie_key() == 'UdnEmbed'

    # Working flag should default to True
    assert ie.working() is True

    # _PROTOCOL_RELATIVE_VALID_URL should capture the numeric id
    m = UDNEmbedIE._match_id(
        UDNEmbedIE, 'https://video.udn.com/embed/news/300040')
    assert m == '300040'

    m2 = UDNEmbedIE._match_id(
        UDNEmbedIE, 'https://video.udn.com/play/news/303776')
    assert m2 == '303776'

# Generated at 2026-10-25 08:18:38.222846
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:48.303856
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:49.673632
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:51.064651
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:52.498310
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:53.931629
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:55.309738
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:56.689080
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:58.090398
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:18:59.610756
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:00.998237
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:19.219602
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:20.659392
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:22.024076
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:23.424858
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:24.787177
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:26.152739
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:27.527854
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:28.901655
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:30.267639
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:19:31.648185
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # default constructor, no downloader
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # constructor with downloader
    dummy = object()
    ie2 = UDNEmbedIE(dummy)
    assert isinstance(ie2, InfoExtractor)
    assert ie2._downloader is dummy

    # class attributes preserved
    assert ie.IE_DESC == 'è¯åå½±é³'

    # URL matching still works on constructed instance
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-25 08:20:09.020781
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:11.436034
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:13.853767
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:16.270363
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:18.683114
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:21.098019
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:23.514851
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:25.927558
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:28.348021
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:30.765079
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:33.178894
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:35.625948
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:38.006735
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:40.420310
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:42.838753
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:45.255768
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:47.672541
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:50.085148
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:52.502743
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:54.917077
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:57.331679
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:20:59.748365
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:21:02.164726
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:21:04.578458
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:21:06.995102
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:21:09.470505
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:21:11.888152
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:21:14.303426
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:21:16.721610
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:21:19.148121
# Unit test for constructor of class UDNEmbedIE