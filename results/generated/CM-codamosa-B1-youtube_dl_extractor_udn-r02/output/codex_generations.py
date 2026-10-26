

# Generated at 2026-10-25 11:31:51.771500
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:31:54.185439
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:31:56.600656
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:31:59.014818
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:01.431406
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:03.848296
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:06.262293
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:08.675880
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:11.089792
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:13.503655
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:15.917238
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:18.338612
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:20.749307
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:23.164707
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:25.577743
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:27.992630
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:30.409305
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:32.827432
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:35.241181
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:37.654486
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:40.070008
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:42.483916
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:32:45.009767
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

# Generated at 2026-10-25 11:32:46.476423
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:32:47.968050
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:32:49.463171
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:32:51.887232
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:33:19.607885
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:33:21.044766
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:33:23.602079
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:33:26.019166
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:28.599667
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:31.015810
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:33.434452
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:35.848154
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:38.261853
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:40.677274
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:43.092383
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:45.508988
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:47.921749
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:50.458209
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:52.852298
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:55.266473
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:33:57.680418
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:00.095051
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:02.509514
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:04.923197
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:07.338171
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:09.752583
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:12.167000
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:14.582031
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:16.997094
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:19.414272
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:21.834631
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:24.254725
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:26.782327
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:29.162218
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:31.576265
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:33.993949
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:36.409270
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:34:39.003185
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

# Generated at 2026-10-25 11:34:40.403902
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:41.838843
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:43.187127
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:44.529899
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:46.043210
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:47.442863
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:48.801902
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:50.277555
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:53.209234
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:54.782025
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:56.179902
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:57.604785
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:34:59.038483
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:35:01.575085
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:03.989151
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:06.403700
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:09.127722
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:11.541152
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:13.957636
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:16.374960
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:18.788658
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:21.528721
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:24.160619
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:26.574996
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:28.988677
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:31.402275
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:33.816144
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:36.229372
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:38.644901
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:41.063156
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:43.473557
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:45.887407
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:48.306756
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:50.715003
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:53.127962
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:55.541394
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:35:58.082826
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:36:00.471989
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:36:02.885627
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:36:05.299578
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:36:07.714667
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:36:09.164186
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

# Generated at 2026-10-25 11:36:12.767367
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:14.136690
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:15.504857
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:16.864590
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:18.195187
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:19.614504
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:21.269589
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:22.703372
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:24.030979
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:36:31.913621
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:26.399653
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:27.933090
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:29.478176
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:30.798966
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:35.295735
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:37.355263
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:41.582928
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:42.940591
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:45.913510
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:37:48.611118
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:37:51.028805
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:37:53.570135
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:37:55.984758
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:37:58.397583
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:00.810322
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:03.228137
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:05.904537
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:08.321720
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:10.740459
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:13.316182
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:15.730265
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:18.146021
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:20.559273
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:22.971117
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:25.384627
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:27.801340
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:30.218176
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:32.627488
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:35.039911
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:37.454750
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:44.220555
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:46.635297
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:49.048536
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:51.462505
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:53.876381
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:56.290683
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:38:58.704926
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:01.119770
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:03.534850
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:05.947461
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:08.360956
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:10.776889
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:13.342540
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:15.706051
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:18.371522
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():ie = UDNEmbedIE()

# Generated at 2026-10-25 11:39:19.858767
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:39:21.594838
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:39:22.994495
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:39:24.348152
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:39:26.014874
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:39:42.386042
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor must not touch the network or require a downloader
    UDNEmbedIE(None)

# Generated at 2026-10-25 11:39:44.917948
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:47.436766
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:49.854580
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:52.266371
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:54.958162
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:57.372064
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:39:59.788636
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:02.559309
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:04.971330
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:07.385972
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:09.801500
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:12.214088
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:14.627471
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:17.040582
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:19.454247
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:21.869456
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:24.282579
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:26.697039
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:29.110655
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:31.522277
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:33.934820
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:36.365749
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:38.778460
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:41.193191
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:43.607123
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:46.022322
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:40:48.438568
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:11.177941
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:13.591134
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:16.006717
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:18.421659
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:20.835771
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:23.248690
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:25.661738
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:28.076494
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:30.491157
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:32.905907
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:35.321006
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:37.734739
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:40.148592
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:42.702382
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:45.072568
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:47.488257
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:49.902320
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 11:41:52.317377
# Unit test for constructor of class UDNEmbedIE