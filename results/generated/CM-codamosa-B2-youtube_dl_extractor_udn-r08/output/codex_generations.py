

# Generated at 2026-11-02 13:13:38.407729
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, UDNEmbedIE)
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    # suitable() should accept valid URLs from all test cases
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # suitable() should reject invalid URLs
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('http://video.udn.com/embed/news/abc')
    assert not ie.suitable('https://video.udn.com/news/300040')
    assert not ie.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')

    # _match_id should extract the correct id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # Constructor should also accept an optional downloader argument
    ie2 = UDNEmbedIE(None)
    assert isinstance(ie2, UDNEmbedIE)
    assert ie2.IE_DESC == '聯合影音'

# Generated at 2026-11-02 13:15:15.254773
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Instance should be created and be an InfoExtractor subclass
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'

    # Valid URL matching
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert ie.suitable('//video.udn.com/embed/news/300040')

    # ID extraction
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # Invalid URLs should not match
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('http://video.udn.com/embed/news/abc')
    assert not ie.suitable('http://other.example.com/embed/news/300040')

# Generated at 2026-11-02 13:21:52.553700
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Class-level attributes
    assert ie.IE_DESC == '聯合影音'
    assert UDNEmbedIE.ie_key() == 'UDNEmbedIE'
    assert UDNEmbedIE.working()

    # URL matching via suitable()
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # Non-matching URLs
    assert not ie.suitable('https://video.udn.com/news/303776')
    assert not ie.suitable('https://video.udn.com/embed/news/')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('')

    # ID extraction
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'