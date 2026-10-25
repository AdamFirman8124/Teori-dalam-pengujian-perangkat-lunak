

# Generated at 2026-10-25 00:20:50.997982
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:20:52.352418
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:20:53.695367
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:20:55.037849
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:20:56.364436
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:20:57.674777
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:20:59.117098
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:21:00.562176
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:21:02.999704
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:05.510945
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:07.925913
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:10.340867
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:12.755871
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:15.171308
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:17.587520
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:20.001773
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:22.577772
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:24.993239
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:27.411465
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:29.825901
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:32.241426
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:34.656230
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:37.073046
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:21:50.025983
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, UDNEmbedIE)
    assert isinstance(ie, InfoExtractor)
    assert ie._ready is False
    assert ie._downloader is None
    assert ie._x_forwarded_for_ip is None
    assert ie.IE_NAME == 'UDNEmbed'
    assert UDNEmbedIE.IE_DESC == 'è¯åå½±é³'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://video.udn.com/news/303776')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'
    ie2 = UDNEmbedIE(downloader=None)
    assert ie2._downloader is None
    fake_downloader = type('FakeDownloader', (), {'params': {}})()
    ie3 = UDNEmbedIE(downloader=fake_downloader)
    assert ie3._downloader is fake_downloader

# Generated at 2026-10-25 00:21:51.352001
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:21:52.686042
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:21:54.220550
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:21:55.541009
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:21:56.858156
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:21:58.177395
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:21:59.497903
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:22:00.839854
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:22:02.172647
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:22:03.501398
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:22:05.923982
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:08.356034
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:10.768962
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:13.183560
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:15.597850
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:18.012962
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:20.428710
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:22.843626
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:25.274282
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:27.689847
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:30.106806
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:32.521506
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:34.935442
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:37.350169
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:39.764980
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:42.195088
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:44.614942
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:47.030469
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:49.443512
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:51.860578
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:54.297693
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:56.715160
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:22:59.139193
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:01.571599
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:03.982195
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:06.397293
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:08.810657
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:11.224884
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:13.638911
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:16.052255
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:18.468277
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:20.881279
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:23.296247
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:25.713188
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:28.128902
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:30.544527
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:32.959712
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:35.568228
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:23:36.887101
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

# Generated at 2026-10-25 00:23:38.223583
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:39.553498
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:40.881773
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:42.232047
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:43.575269
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:44.901011
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:46.213438
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:47.576655
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:48.924567
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:50.245918
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:51.566314
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:52.937980
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:54.257943
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:55.588239
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:56.908988
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:58.225132
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:23:59.555503
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:24:00.916464
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:24:03.558499
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:24:06.092225
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:08.509687
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:10.927426
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:13.342215
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:15.757353
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:18.171376
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:20.782422
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:23.198852
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:25.614816
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:28.027344
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:30.441112
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:32.873155
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:35.309172
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:37.752359
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:40.194852
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:42.639671
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:45.056823
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:47.475630
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:49.905984
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:52.316710
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:54.758996
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:57.196497
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:24:59.639117
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:02.080946
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:04.508567
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:06.923865
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:09.338204
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:15.252843
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:17.668172
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:20.082451
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:21.503477
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:22.857061
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:24.196124
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:25.526086
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:26.851287
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:28.238820
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:29.561285
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:30.941877
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:32.264228
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:43.392596
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:44.825783
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:46.161184
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:47.489203
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:25:49.907485
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:52.430126
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:54.844614
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:57.258918
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:25:59.673038
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:02.087941
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:04.502842
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:06.918098
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:09.332331
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:11.751316
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:14.174550
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:16.588787
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:19.004988
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:21.423764
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:23.837422
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:25.149172
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:26:46.308079
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:26:47.590101
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:26:48.916218
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:26:50.362120
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:26:51.695611
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:26:54.231094
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:56.783190
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:26:59.314168
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:01.729760
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:04.146506
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:06.573042
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:08.987089
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:11.415475
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:13.820340
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:16.235892
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:18.651478
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:21.068735
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:23.486013
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:25.904068
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:27:28.318656
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:28:06.969753
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:08.299391
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:09.722653
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:11.160261
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:12.472927
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:13.797754
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:15.125902
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:16.449681
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:17.785263
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:28:19.103509
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:29:47.245975
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:29:48.563014
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:29:51.136043
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:29:53.660230
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:29:56.180555
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:29:58.702605
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:30:01.123136
# Unit test for constructor of class UDNEmbedIE

# Generated at 2026-10-25 00:30:02.580948
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

# Generated at 2026-10-25 00:30:03.989980
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:30:05.435461
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:30:06.784798
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:30:08.199762
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:30:09.534428
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set

# Generated at 2026-10-25 00:30:10.857589
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == 'è¯åå½±é³'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.GEO_COUNTRIES is None  # no geo-restriction set