

# Generated at 2026-10-24 16:02:27.235969
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:02:56.933469
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # default constructor must not raise
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # base-class initial state
    assert ie._downloader is None

    # downloader passthrough from InfoExtractor.__init__
    sentinel = object()
    ie_with_dl = ITVBTCCIE(sentinel)
    assert isinstance(ie_with_dl, ITVBTCCIE)
    assert ie_with_dl._downloader is sentinel

# Generated at 2026-10-24 16:02:59.879748
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:03:02.768129
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:03:27.165402
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:03:43.730013
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:03:46.144865
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:03:48.557982
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:03:50.971157
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:03:53.385732
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:04:09.533726
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-24 16:04:25.981130
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # default constructor must not raise
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # base-class initial state
    assert ie._downloader is None

    # downloader passthrough from InfoExtractor.__init__
    sentinel = object()
    ie_with_dl = ITVBTCCIE(sentinel)
    assert isinstance(ie_with_dl, ITVBTCCIE)
    assert ie_with_dl._downloader is sentinel

# Generated at 2026-10-24 16:04:28.868824
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:04:31.283844
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:33.699271
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:36.116925
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:38.525236
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:40.940479
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:43.353850
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:45.898006
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:48.310980
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:50.723603
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:53.136613
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:55.549646
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:04:57.962351
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:05:00.374950
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:05:02.788426
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:05:05.202596
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:05:07.835335
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:05:09.335635
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:05:10.768809
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # default constructor must not raise
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # base-class initial state
    assert ie._downloader is None

    # downloader passthrough from InfoExtractor.__init__
    sentinel = object()
    ie_with_dl = ITVBTCCIE(sentinel)
    assert isinstance(ie_with_dl, ITVBTCCIE)
    assert ie_with_dl._downloader is sentinel

# Generated at 2026-10-24 16:05:13.635305
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:05:16.539542
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:05:19.252964
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:05:20.603927
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:05:23.482531
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:05:26.297267
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:05:27.666675
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:05:30.647280
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:05:47.122784
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:05:49.539217
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:05:51.950912
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:05:54.565230
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:05:56.977708
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:05:59.391011
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:01.803598
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:04.216619
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:06.633918
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:09.044883
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:11.457578
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:13.910488
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:16.313003
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:18.730316
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:21.143200
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:23.557774
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:25.971350
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:28.384057
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:30.797771
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:33.211174
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:35.628684
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:38.037022
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:40.450148
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:42.862260
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:45.274861
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:47.699007
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:50.110926
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:52.528565
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:06:54.945928
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:06:57.362048
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:07:00.235157
# Unit test for constructor of class ITVIE
def test_ITVIE():from youtube_dl.extractor.itv import ITVIE

# Generated at 2026-10-24 16:07:01.671964
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:07:04.740500
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:07.575198
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:09.043607
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # default constructor must not raise
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # base-class initial state
    assert ie._downloader is None

    # downloader passthrough from InfoExtractor.__init__
    sentinel = object()
    ie_with_dl = ITVBTCCIE(sentinel)
    assert isinstance(ie_with_dl, ITVBTCCIE)
    assert ie_with_dl._downloader is sentinel

# Generated at 2026-10-24 16:07:11.852619
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:14.610635
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:17.370894
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:20.203721
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:21.528685
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:07:24.299860
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:25.700695
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:07:28.702632
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:31.570827
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:07:44.779702
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:08:20.568240
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-24 16:08:37.206120
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:08:38.533954
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:08:41.371482
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:08:44.273765
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:08:45.607220
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:08:47.047230
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # default constructor must not raise
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # base-class initial state
    assert ie._downloader is None

    # downloader passthrough from InfoExtractor.__init__
    sentinel = object()
    ie_with_dl = ITVBTCCIE(sentinel)
    assert isinstance(ie_with_dl, ITVBTCCIE)
    assert ie_with_dl._downloader is sentinel

# Generated at 2026-10-24 16:08:48.366425
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:08:49.694468
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:08:52.525948
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:08:55.435205
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:08:58.302777
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:09:14.790072
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:09:17.211834
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:09:19.626227
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:09:22.039159
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:09:24.452535
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:09:26.865638
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:09:29.279853
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:09:31.693207
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:09:34.106395
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:09:36.519667
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:09:38.930184
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:09:41.343366
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:09:43.757746
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:09:46.386351
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:09:49.298668
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:10:05.698086
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:10:07.027578
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:10:09.880140
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:10:11.313667
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # default constructor must not raise
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # base-class initial state
    assert ie._downloader is None

    # downloader passthrough from InfoExtractor.__init__
    sentinel = object()
    ie_with_dl = ITVBTCCIE(sentinel)
    assert isinstance(ie_with_dl, ITVBTCCIE)
    assert ie_with_dl._downloader is sentinel

# Generated at 2026-10-24 16:10:14.166504
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:10:15.615247
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # default constructor must not raise
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # base-class initial state
    assert ie._downloader is None

    # downloader passthrough from InfoExtractor.__init__
    sentinel = object()
    ie_with_dl = ITVBTCCIE(sentinel)
    assert isinstance(ie_with_dl, ITVBTCCIE)
    assert ie_with_dl._downloader is sentinel

# Generated at 2026-10-24 16:10:16.936692
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:10:20.979419
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:10:22.346601
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:10:25.139493
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:10:26.560940
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # default constructor must not raise
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # base-class initial state
    assert ie._downloader is None

    # downloader passthrough from InfoExtractor.__init__
    sentinel = object()
    ie_with_dl = ITVBTCCIE(sentinel)
    assert isinstance(ie_with_dl, ITVBTCCIE)
    assert ie_with_dl._downloader is sentinel

# Generated at 2026-10-24 16:10:29.391773
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-24 16:10:31.807487
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:10:34.219723
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:10:36.630972
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:10:39.043631
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:10:41.459971
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:10:43.872866
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:10:46.284439
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-24 16:11:13.576076
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-24 16:11:30.168539
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2026-10-24 16:11:32.699193
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:11:35.208100
# Unit test for constructor of class ITVIE

# Generated at 2026-10-24 16:11:37.620379
# Unit test for constructor of class ITVIE