

# Generated at 2026-10-24 04:17:24.634166
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:17:27.051311
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:17:29.468810
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:17:31.883378
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:17:34.302336
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:17:35.615979
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():from youtube_dl.extractor.udn import UDNEmbedIE


# Generated at 2026-10-24 04:17:47.060072
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    default_ie = UDNEmbedIE()
    assert isinstance(default_ie, UDNEmbedIE)
    assert default_ie._downloader is None

    downloader = object()
    configured_ie = UDNEmbedIE(downloader)
    assert isinstance(configured_ie, UDNEmbedIE)
    assert configured_ie._downloader is downloader

# Generated at 2026-10-24 04:17:56.583911
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._VALID_URL == (
        r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    )

# Generated at 2026-10-24 04:18:04.477381
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:18:14.099274
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
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:18:16.634742
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:19.153416
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:21.673808
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:24.096056
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:26.555889
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:28.950212
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:31.365826
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:33.783787
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:36.202274
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:38.623000
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:41.033316
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:18:42.401065
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():from youtube_dl.extractor.udn import UDNEmbedIE


# Generated at 2026-10-24 04:18:57.408905
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:19:07.343580
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:19:15.845481
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'

    # Verify that initialization leaves the extractor usable.
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:19:23.742073
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:19:34.066199
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 04:19:45.024336
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 04:19:51.820722
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 04:19:59.476622
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:20:10.478706
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'

    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'
    assert extractor._match_id(
        'https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-10-24 04:20:18.422283
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:20:27.418491
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:20:34.486814
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:20:36.904647
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:20:39.319516
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:20:41.746885
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:20:51.663166
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # The extractor should instantiate successfully
    assert ie is not None
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == 'è¯åå½±é³'

    # Check the URL patterns are intact
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

    # The extractor should recognize its own test URLs
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # And extract the correct video id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # URLs from other extractors should not match
    assert not ie.suitable('https://www.youtube.com/watch?v=dummy')
    assert not ie.suitable('http://video.udn.com/news/300040')

# Generated at 2026-10-24 04:21:01.262127
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

# Generated at 2026-10-24 04:21:10.352721
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:21:18.721978
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 04:21:28.023061
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:21:37.871877
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    assert isinstance(ie, UDNEmbedIE)
    assert ie._downloader is None
    assert ie._ready is False

    downloader = object()
    ie_with_downloader = UDNEmbedIE(downloader)

    assert ie_with_downloader._downloader is downloader
    assert ie_with_downloader._ready is False

# Generated at 2026-10-24 04:21:40.287892
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:21:42.701236
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:21:45.118620
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:21:47.535759
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:21:53.377780
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():extractor = UDNEmbedIE()

# Generated at 2026-10-24 04:22:02.776187
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-24 04:22:11.885257
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:22:21.805399
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:22:30.606261
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 04:22:39.282532
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:22:41.706149
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:22:44.269632
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:22:46.786669
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:22:49.204082
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:22:51.620346
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:22:54.033988
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:23:08.662810
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:23:18.427134
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://example.com/embed/news/300040')

# Generated at 2026-10-24 04:23:27.278198
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
    assert not extractor.suitable('https://video.udn.com/news/303776')

# Generated at 2026-10-24 04:23:34.813511
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:23:43.924901
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert not extractor.suitable('https://example.com/embed/news/300040')

# Generated at 2026-10-24 04:23:52.518126
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:23:59.402339
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:24:13.727565
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

# Generated at 2026-10-24 04:24:23.045276
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None

# Generated at 2026-10-24 04:24:32.915800
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'

    assert extractor.suitable(
        'https://video.udn.com/embed/news/300040')
    assert extractor.suitable(
        'https://video.udn.com/play/news/303776')
    assert not extractor.suitable(
        'https://video.udn.com/news/303776')

# Generated at 2026-10-24 04:24:42.375890
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.suitable('https://video.udn.com/embed/news/300040')
    assert extractor.suitable('https://video.udn.com/play/news/303776')
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:24:50.553473
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:24:53.070796
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:24:55.483254
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:01.952340
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():extractor = UDNEmbedIE()

# Generated at 2026-10-24 04:25:10.600808
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:25:18.855528
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'UDNEmbed'
    assert extractor.IE_DESC == 'è¯åå½±é³'

# Generated at 2026-10-24 04:25:27.042170
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 04:25:37.079670
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
    assert extractor._match_id(
        'https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-10-24 04:25:39.499447
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:42.061292
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:44.477144
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:46.891192
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:49.307821
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:51.721885
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:54.138708
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:56.691523
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:25:59.107138
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:01.524159
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:03.939597
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:06.353983
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:08.768258
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:11.181205
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:18.406373
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():extractor = UDNEmbedIE(None)

# Generated at 2026-10-24 04:26:27.120369
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()
    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 04:26:35.365028
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_DESC == 'è¯åå½±é³'
    assert extractor.ie_key() == 'UDNEmbed'

# Generated at 2026-10-24 04:26:44.351485
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    downloader = object()

    extractor = UDNEmbedIE(downloader)

    assert isinstance(extractor, UDNEmbedIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 04:26:46.856593
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:49.274219
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:51.871620
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:26:58.763812
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:27:01.178291
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:27:03.597015
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:27:06.011801
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:27:08.425458
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:27:10.840676
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:27:13.255961
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:27:15.675144
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-24 04:27:18.088792
# Unit test for constructor of class UDNEmbedIE