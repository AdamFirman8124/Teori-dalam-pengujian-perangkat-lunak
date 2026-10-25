

# Generated at 2026-10-24 02:31:51.474356
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 02:32:02.237391
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:32:12.773835
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

    default_extractor = UDNEmbedIE()
    assert default_extractor._downloader is None
    assert default_extractor._ready is False

# Generated at 2026-10-24 02:32:21.987387
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor.suitable(
        'https://video.udn.com/play/news/303776')

# Generated at 2026-10-24 02:32:30.396098
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

# Generated at 2026-10-24 02:32:38.066072
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'UDNEmbed'

    test_url = 'https://video.udn.com/embed/news/300040'
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == '300040'

# Generated at 2026-10-24 02:32:46.872750
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:32:55.287727
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:33:03.667777
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:33:11.243609
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:33:19.445321
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:33:27.116403
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://example.com/video/300040')

# Generated at 2026-10-24 02:33:38.482478
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

# Generated at 2026-10-24 02:33:46.367114
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    ie = UDNEmbedIE(downloader)

    assert isinstance(ie, UDNEmbedIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is downloader
    assert ie._ready is False
    assert ie.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:33:53.330003
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:34:06.347008
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 02:34:15.858416
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:34:24.154090
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:34:32.508038
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:34:40.436719
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:34:47.808955
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:34:56.624722
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')

# Generated at 2026-10-24 02:35:05.010019
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 02:35:12.996918
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 02:35:22.315499
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'

# Generated at 2026-10-24 02:35:33.886768
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:35:42.795852
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    assert isinstance(ie, UDNEmbedIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 02:35:50.578813
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://example.com/video/300040')

# Generated at 2026-10-24 02:35:57.554476
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 02:36:06.042132
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._downloader is None

# Generated at 2026-10-24 02:36:19.354565
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

    default_extractor = UDNEmbedIE()
    assert default_extractor._downloader is None

# Generated at 2026-10-24 02:36:27.646973
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:36:33.791562
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:36:44.952645
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:36:54.578297
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'

# Generated at 2026-10-24 02:37:12.852448
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

# Generated at 2026-10-24 02:37:22.126261
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'

    assert extractor.suitable('http://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-24 02:37:30.316065
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'

# Generated at 2026-10-24 02:37:38.621116
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 02:37:47.213704
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')

# Generated at 2026-10-24 02:37:55.416589
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

# Generated at 2026-10-24 02:38:03.801656
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class DummyDownloader(object):
        pass

    downloader = DummyDownloader()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 02:38:24.588397
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():from youtube_dl.extractor.udn import UDNEmbedIE


# Generated at 2026-10-24 02:38:35.034029
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

# Generated at 2026-10-24 02:38:43.339461
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'

# Generated at 2026-10-24 02:38:50.089704
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 02:38:59.008106
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-10-24 02:39:07.905361
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:39:23.486760
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class DummyDownloader(object):
        params = {}

    downloader = DummyDownloader()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

    test_url = 'https://video.udn.com/embed/news/300040'
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == '300040'

# Generated at 2026-10-24 02:39:30.485148
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-24 02:39:40.877117
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 02:39:57.067116
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:40:06.375533
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040'
    ) == '300040'
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776'
    ) == '303776'

# Generated at 2026-10-24 02:40:15.386716
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

# Generated at 2026-10-24 02:40:23.168676
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 02:40:31.564867
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 02:40:41.236504
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 02:40:51.233231
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 02:40:59.371321
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._downloader is None
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 02:41:06.176786
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:41:13.958801
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class DummyDownloader(object):
        params = {}

    downloader = DummyDownloader()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 02:41:25.837784
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'

    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor.suitable(
        'https://video.udn.com/play/news/303776')
    assert not extractor.suitable(
        'https://video.udn.com/news/303776')

    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 02:41:34.131553
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 02:41:42.128604
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 02:41:51.436979
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://example.com/embed/news/300040')