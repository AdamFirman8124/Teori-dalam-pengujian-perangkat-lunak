

# Generated at 2026-10-25 08:48:00.711633
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

# Generated at 2026-10-25 08:48:02.837412
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

# Generated at 2026-10-25 08:48:05.095741
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

# Generated at 2026-10-25 08:48:20.138372
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:48:21.674770
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

# Generated at 2026-10-25 08:48:23.312174
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

# Generated at 2026-10-25 08:48:24.750967
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:48:26.384923
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:48:27.781557
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

# Generated at 2026-10-25 08:48:29.156791
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

# Generated at 2026-10-25 08:48:30.582831
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

# Generated at 2026-10-25 08:48:32.012924
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

# Generated at 2026-10-25 08:48:33.484238
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

# Generated at 2026-10-25 08:48:34.985858
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

# Generated at 2026-10-25 08:48:36.419311
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

# Generated at 2026-10-25 08:48:38.058219
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

# Generated at 2026-10-25 08:48:40.663266
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:48:43.081266
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:48:45.497370
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:48:47.914497
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:48:50.334710
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:48:52.750239
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:48:55.166238
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:48:57.696721
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:00.084837
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:02.502711
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:04.920915
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:07.337441
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:09.806597
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:12.225543
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:14.639698
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:17.055371
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:19.472304
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:21.894781
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:24.313400
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:26.731382
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:29.144759
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:31.564775
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:33.980776
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:36.441517
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:38.862550
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:41.278664
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:43.695451
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:46.113944
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:48.527791
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:50.949264
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:53.366797
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:55.812472
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:49:58.232063
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:00.652972
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:03.072876
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:05.490045
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:07.909136
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:10.326270
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:12.742693
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:15.163177
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:17.580232
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:19.998995
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:22.413040
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:24.863798
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:27.286367
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:29.714347
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:32.130169
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:34.549017
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:37.127493
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:39.422052
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:41.835207
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:44.252650
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:46.669373
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:49.087660
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:51.519868
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:53.937793
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:56.356387
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:50:58.774369
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:51:01.190881
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:51:03.605791
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:51:33.573865
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert UDNEmbedIE.IE_DESC == 'è¯åå½±é³'
    assert UDNEmbedIE._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert UDNEmbedIE._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert UDNEmbedIE._match_id('https://video.udn.com/play/news/303776') == '303776'
    assert re.match(UDNEmbedIE._VALID_URL, 'http://video.udn.com/embed/news/300040')
    assert re.match(UDNEmbedIE._VALID_URL, 'https://video.udn.com/embed/news/300040')
    assert re.match(UDNEmbedIE._VALID_URL, 'https://video.udn.com/play/news/303776')
    assert not re.match(UDNEmbedIE._VALID_URL, 'https://video.udn.com/news/303776')
    assert not re.match(UDNEmbedIE._VALID_URL, 'https://video.udn.com/embed/news/')
    assert isinstance(UDNEmbedIE._TESTS, list)

# Generated at 2026-10-25 08:51:37.363172
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

# Generated at 2026-10-25 08:51:38.898523
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:51:40.432955
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

# Generated at 2026-10-25 08:51:41.970378
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

# Generated at 2026-10-25 08:51:43.505585
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

# Generated at 2026-10-25 08:51:45.041192
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

# Generated at 2026-10-25 08:51:46.564117
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

# Generated at 2026-10-25 08:51:48.009236
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:51:49.652389
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:51:51.082730
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

# Generated at 2026-10-25 08:51:52.620787
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

# Generated at 2026-10-25 08:51:55.262646
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:51:57.926254
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:00.346044
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:02.763443
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:05.369563
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:07.787569
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:10.203506
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:12.691459
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:15.060409
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:17.475740
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:20.152926
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():ie = UDNEmbedIE()

# Generated at 2026-10-25 08:52:21.722976
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

# Generated at 2026-10-25 08:52:23.116944
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

# Generated at 2026-10-25 08:52:24.671464
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

# Generated at 2026-10-25 08:52:27.844237
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

# Generated at 2026-10-25 08:52:29.417884
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

# Generated at 2026-10-25 08:52:31.019332
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

# Generated at 2026-10-25 08:52:32.456601
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

# Generated at 2026-10-25 08:52:33.888310
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:52:35.424546
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

# Generated at 2026-10-25 08:52:36.871234
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

# Generated at 2026-10-25 08:52:39.533202
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:41.951224
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:44.368209
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:46.997368
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:49.413580
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:51.830451
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:54.248222
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:56.663544
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:52:59.079538
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:06.067404
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:08.531540
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:10.947699
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:13.365192
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:15.781204
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:18.230552
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:20.641902
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:23.057445
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:25.474351
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:27.889457
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:30.305879
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:32.722672
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:35.136552
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:53:43.725089
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

# Generated at 2026-10-25 08:53:45.265029
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

# Generated at 2026-10-25 08:53:46.732349
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:53:48.441419
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 08:53:49.818300
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

# Generated at 2026-10-25 08:53:52.736217
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

# Generated at 2026-10-25 08:54:05.040051
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

# Generated at 2026-10-25 08:54:07.704256
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:10.126492
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:12.544626
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:14.962721
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:17.380855
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:19.797210
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:22.317509
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:24.850044
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:27.268120
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:29.685594
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:32.103862
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:34.546473
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:36.961619
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:39.379022
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:54:42.268018
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():ie = UDNEmbedIE()

# Generated at 2026-10-25 08:54:43.703920
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

# Generated at 2026-10-25 08:54:45.368759
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

# Generated at 2026-10-25 08:54:47.313593
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

# Generated at 2026-10-25 08:54:48.765374
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

# Generated at 2026-10-25 08:55:14.905228
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:17.599001
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:20.025376
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:22.443564
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:24.858006
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:27.271199
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:29.691825
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:32.113532
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:34.527882
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:36.946401
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:39.403096
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:41.786073
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:44.203957
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:46.710588
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:49.097088
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:51.514410
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:53.929643
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:56.348022
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:55:58.770206
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:01.187602
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:03.606146
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:06.023312
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:08.437944
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:10.859917
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:13.274973
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:15.693960
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:18.108222
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:20.528301
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:22.946566
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:56:25.362840
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:57:12.825883
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

# Generated at 2026-10-25 08:57:15.897980
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

# Generated at 2026-10-25 08:57:21.017354
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

# Generated at 2026-10-25 08:57:22.552810
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

# Generated at 2026-10-25 08:57:23.988917
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

# Generated at 2026-10-25 08:57:26.675725
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:57:29.095011
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:57:31.674603
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:57:34.091039
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 08:57:48.666829
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():ie = UDNEmbedIE(None)

# Generated at 2026-10-25 08:57:52.148125
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

# Generated at 2026-10-25 08:57:54.015012
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

# Generated at 2026-10-25 08:57:55.526369
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