

# Generated at 2026-11-03 04:55:50.098324
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert UDNEmbedIE.ie_key() == 'UDNEmbed'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-03 04:58:27.865906
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Instance should be created successfully and inherit from InfoExtractor
    assert isinstance(ie, UDNEmbedIE)

    # Class attributes should be set correctly
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    # suitable() should accept valid URLs
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # suitable() should reject invalid URLs
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('http://video.udn.com/embed/news/abc')

    # _match_id() should extract the correct video id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # Test URLs from _TESTS should all be suitable
    for t in ie._TESTS:
        assert ie.suitable(t['url'])

# Generated at 2026-11-03 05:02:52.707668
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Constructor should initialize with no downloader
    assert ie._downloader is None

    # Class attributes are set correctly
    assert ie.IE_DESC == u'聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    # suitable() should accept embed and play URLs over http/https
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # suitable() should reject URLs that don't match the pattern
    assert not ie.suitable('http://video.udn.com/news/303776')
    assert not ie.suitable('http://video.udn.com/embed/news/abc')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('')

    # _match_id() should extract the numeric video id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # All test URLs declared in _TESTS must be handled by this extractor
    for t in ie._TESTS:
        assert ie.suitable(t['url'])