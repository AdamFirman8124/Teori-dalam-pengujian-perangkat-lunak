

# Generated at 2026-10-24 03:51:45.797736
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:51:48.210943
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:51:50.809099
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:51:53.224939
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:51:55.639381
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:51:58.054761
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:00.470972
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:02.886166
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:05.301175
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:07.718605
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:10.135447
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:12.549161
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:14.964939
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:17.380379
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:52:18.964593
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():from youtube_dl.extractor.udn import UDNEmbedIE


# Generated at 2026-10-24 03:52:28.873594
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 03:52:37.641003
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-10-24 03:52:46.807232
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:52:57.202930
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    ie = UDNEmbedIE(downloader)

    assert isinstance(ie, UDNEmbedIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is downloader
    assert ie._ready is False
    assert ie.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:52:59.715433
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:02.135253
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:04.551378
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:06.970059
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:09.387198
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:11.800426
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:14.216757
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:16.634055
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:19.047295
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:21.461767
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:23.877413
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:26.292738
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:28.717750
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:31.133645
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:33.548842
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:35.963502
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:38.378748
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:40.794150
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:43.212369
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:45.628777
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 03:53:53.862010
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():extractor = UDNEmbedIE(None)

# Generated at 2026-10-24 03:54:02.241859
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 03:54:09.780904
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:54:18.848425
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'

# Generated at 2026-10-24 03:54:28.371480
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:54:37.996362
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 03:54:47.829474
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 03:54:55.816115
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:55:04.317938
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 03:55:13.633543
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'

# Generated at 2026-10-24 03:55:22.336719
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 03:55:32.402096
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    assert isinstance(ie, UDNEmbedIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:55:39.071425
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-24 03:55:48.348826
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._downloader is None
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://example.com/video/300040')

# Generated at 2026-10-24 03:55:57.591603
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

    # Verify the constructed extractor recognizes supported URLs.
    url = 'https://video.udn.com/embed/news/300040'
    assert extractor.suitable(url)
    assert extractor._match_id(url) == '300040'

# Generated at 2026-10-24 03:56:04.984964
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('http://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://example.com/video/300040')

# Generated at 2026-10-24 03:56:10.057307
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._downloader is None
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://example.com/video/300040')

# Generated at 2026-10-24 03:56:18.768855
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._downloader is None

    assert extractor.suitable('http://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 03:56:29.615076
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:56:42.823425
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'UDNEmbed'

    downloader = object()
    extractor_with_downloader = UDNEmbedIE(downloader)

    assert extractor_with_downloader._downloader is downloader

# Generated at 2026-10-24 03:56:52.156337
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor.suitable(
        'https://video.udn.com/play/news/303776')

# Generated at 2026-10-24 03:56:57.539505
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')

# Generated at 2026-10-24 03:57:07.702911
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._x_forwarded_for_ip is None

# Generated at 2026-10-24 03:57:16.335827
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')

# Generated at 2026-10-24 03:57:24.918760
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 03:57:33.306744
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor.suitable(
        'https://video.udn.com/play/news/303776')
    assert not extractor.suitable(
        'https://video.udn.com/news/303776')

# Generated at 2026-10-24 03:57:41.806360
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:57:48.870697
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 03:57:56.298572
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-10-24 03:58:04.752119
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 03:58:14.670900
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'

    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor.suitable(
        'https://video.udn.com/play/news/303776')
    assert not extractor.suitable(
        'https://video.udn.com/news/303776')

# Generated at 2026-10-24 03:58:22.652364
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:58:31.295924
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'

# Generated at 2026-10-24 03:58:39.509995
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 03:58:47.862998
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._VALID_URL == (
        r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    )

# Generated at 2026-10-24 03:58:56.673574
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')

# Generated at 2026-10-24 03:59:05.262767
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:59:13.761566
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')

# Generated at 2026-10-24 03:59:23.569385
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 03:59:32.398646
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 03:59:46.529325
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor.suitable(
        'https://video.udn.com/play/news/303776')
    assert not extractor.suitable(
        'https://example.com/embed/news/300040')

# Generated at 2026-10-24 03:59:54.825046
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:00:03.733400
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:00:12.027124
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776'
    ) == '303776'

# Generated at 2026-10-24 04:00:19.093350
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:00:28.035296
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-10-24 04:00:37.251107
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:00:46.944487
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'

# Generated at 2026-10-24 04:00:57.227110
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'

    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor.suitable(
        'https://video.udn.com/play/news/303776')
    assert not extractor.suitable(
        'https://video.udn.com/news/303776')

# Generated at 2026-10-24 04:01:11.420700
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-10-24 04:01:32.245716
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:01:41.935945
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 04:01:50.641490
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776') == '303776'