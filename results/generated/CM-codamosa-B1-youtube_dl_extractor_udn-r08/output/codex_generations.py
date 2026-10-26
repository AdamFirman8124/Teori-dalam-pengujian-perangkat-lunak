

# Generated at 2026-10-25 07:24:06.263827
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

# Generated at 2026-10-25 07:24:07.698928
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

# Generated at 2026-10-25 07:24:09.129666
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

# Generated at 2026-10-25 07:24:10.665791
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

# Generated at 2026-10-25 07:24:13.199302
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:15.617341
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:18.028600
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:20.550480
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:22.964534
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:25.378456
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:27.791904
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:30.204482
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:32.621018
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:35.034452
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:37.448915
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:39.862680
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:42.275327
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:44.687736
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:47.103844
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:49.517346
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:51.933965
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:54.349216
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:56.762335
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:24:59.192086
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:16.202101
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():ie = UDNEmbedIE()

# Generated at 2026-10-25 07:25:17.637519
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

# Generated at 2026-10-25 07:25:19.048642
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

# Generated at 2026-10-25 07:25:20.505829
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

# Generated at 2026-10-25 07:25:22.059669
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

# Generated at 2026-10-25 07:25:23.475610
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

# Generated at 2026-10-25 07:25:25.007813
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

# Generated at 2026-10-25 07:25:26.444646
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

# Generated at 2026-10-25 07:25:28.860124
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:31.421876
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:33.788175
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:36.198313
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:38.714309
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:41.129133
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:43.871265
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:46.404254
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:48.819426
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:51.234299
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:53.648418
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:56.065750
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:25:58.477909
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:00.892112
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:03.306762
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:05.721819
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:08.135832
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:10.549398
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:12.011891
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

# Generated at 2026-10-25 07:26:13.399776
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

# Generated at 2026-10-25 07:26:14.877608
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

# Generated at 2026-10-25 07:26:16.312295
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

# Generated at 2026-10-25 07:26:17.744257
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

# Generated at 2026-10-25 07:26:19.176962
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

# Generated at 2026-10-25 07:26:20.612099
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

# Generated at 2026-10-25 07:26:22.055791
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

# Generated at 2026-10-25 07:26:23.426810
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

# Generated at 2026-10-25 07:26:24.919755
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

# Generated at 2026-10-25 07:26:26.327876
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

# Generated at 2026-10-25 07:26:27.780620
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

# Generated at 2026-10-25 07:26:29.302347
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

# Generated at 2026-10-25 07:26:30.858983
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

# Generated at 2026-10-25 07:26:32.286803
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

# Generated at 2026-10-25 07:26:33.719071
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

# Generated at 2026-10-25 07:26:36.304088
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:38.828949
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:41.248145
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:43.770284
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:46.185985
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:48.599005
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:51.012348
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:53.425867
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:55.839885
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:26:58.254895
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:00.669726
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:03.083215
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:05.498473
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:07.912126
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:10.326344
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:12.743623
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:15.171354
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:17.591662
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:20.001200
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:22.414833
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:24.831356
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:27.244818
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:29.659402
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:32.077262
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:34.488395
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:36.901761
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:39.315401
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:41.840066
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:44.226055
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:46.639980
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:49.054767
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:51.467957
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:53.882522
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:56.331206
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:27:58.738826
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:01.152436
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:03.567598
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:05.985360
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:08.398608
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:10.812159
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:13.226401
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:15.641448
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:18.055893
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:20.468359
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:22.882705
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:26.387764
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:28.801554
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:31.216209
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:33.630369
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:28:35.063082
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert not ie.suitable('https://video.udn.com/news/303776')
    assert UDNEmbedIE._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2026-10-25 07:28:36.430061
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

# Generated at 2026-10-25 07:28:37.832594
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

# Generated at 2026-10-25 07:28:39.476689
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

# Generated at 2026-10-25 07:28:41.019278
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

# Generated at 2026-10-25 07:28:42.449428
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

# Generated at 2026-10-25 07:28:43.879706
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

# Generated at 2026-10-25 07:28:45.311151
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

# Generated at 2026-10-25 07:28:46.805609
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

# Generated at 2026-10-25 07:28:51.959899
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

# Generated at 2026-10-25 07:28:53.403324
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

# Generated at 2026-10-25 07:28:54.826286
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

# Generated at 2026-10-25 07:28:56.372948
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

# Generated at 2026-10-25 07:28:57.796110
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

# Generated at 2026-10-25 07:28:59.228114
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

# Generated at 2026-10-25 07:29:00.661512
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

# Generated at 2026-10-25 07:29:02.096203
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

# Generated at 2026-10-25 07:29:03.529175
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

# Generated at 2026-10-25 07:29:05.178356
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

# Generated at 2026-10-25 07:29:14.077118
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

# Generated at 2026-10-25 07:29:15.510718
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

# Generated at 2026-10-25 07:29:16.950057
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

# Generated at 2026-10-25 07:29:18.480576
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

# Generated at 2026-10-25 07:29:20.033592
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

# Generated at 2026-10-25 07:29:22.565655
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:29:25.001771
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:29:27.426689
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:29:29.845268
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:29:32.258385
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:29:34.671189
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:29:36.103362
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

# Generated at 2026-10-25 07:29:37.527625
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

# Generated at 2026-10-25 07:29:38.946867
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

# Generated at 2026-10-25 07:29:56.185447
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

# Generated at 2026-10-25 07:29:57.597584
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

# Generated at 2026-10-25 07:29:58.988519
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

# Generated at 2026-10-25 07:30:00.468013
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

# Generated at 2026-10-25 07:30:01.898046
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

# Generated at 2026-10-25 07:30:03.445676
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

# Generated at 2026-10-25 07:30:05.017722
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

# Generated at 2026-10-25 07:30:06.303774
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

# Generated at 2026-10-25 07:30:07.735822
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

# Generated at 2026-10-25 07:30:09.273508
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

# Generated at 2026-10-25 07:30:45.724654
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

# Generated at 2026-10-25 07:30:47.260494
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

# Generated at 2026-10-25 07:30:48.693667
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

# Generated at 2026-10-25 07:30:50.128125
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

# Generated at 2026-10-25 07:30:51.561367
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

# Generated at 2026-10-25 07:30:52.994798
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

# Generated at 2026-10-25 07:30:54.531645
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

# Generated at 2026-10-25 07:30:55.964689
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

# Generated at 2026-10-25 07:30:57.398065
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

# Generated at 2026-10-25 07:30:58.839873
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

# Generated at 2026-10-25 07:32:14.200349
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

# Generated at 2026-10-25 07:32:15.634030
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

# Generated at 2026-10-25 07:32:17.030798
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

# Generated at 2026-10-25 07:32:18.502723
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

# Generated at 2026-10-25 07:32:19.937492
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

# Generated at 2026-10-25 07:32:21.368266
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

# Generated at 2026-10-25 07:32:22.802727
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

# Generated at 2026-10-25 07:32:25.230501
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:32:27.785355
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:32:30.362650
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:32:32.777312
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:32:35.192735
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:32:37.609792
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:32:40.022726
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:32:42.436175
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 07:32:44.850524
# Unit test for constructor of class UDNEmbedIE