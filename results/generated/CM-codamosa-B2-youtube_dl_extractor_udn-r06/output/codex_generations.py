

# Generated at 2026-11-02 20:44:18.935477
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    '''
    Unit test for constructor of class UDNEmbedIE
    '''
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://video.udn.com/news/303776')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-02 20:47:18.926955
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Default construction should succeed and leave the downloader unset
    ie = UDNEmbedIE()
    assert ie._downloader is None

    # Construction with an explicit downloader should store it
    fake_downloader = object()
    ie_with_dl = UDNEmbedIE(downloader=fake_downloader)
    assert ie_with_dl._downloader is fake_downloader

    # IE metadata
    assert UDNEmbedIE.IE_DESC == '聯合影音'
    assert UDNEmbedIE._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

    # The extractor should claim the URLs listed in its tests
    for test in UDNEmbedIE._TESTS:
        assert UDNEmbedIE.suitable(test['url'])

    # Protocol-relative forms must not be claimed by the https? pattern
    assert not UDNEmbedIE.suitable('//video.udn.com/embed/news/300040')

    # Invalid URLs must be rejected
    assert not UDNEmbedIE.suitable('http://video.udn.com/embed/news/')
    assert not UDNEmbedIE.suitable('http://video.udn.com/embed/news/notanumber')
    assert not UDNEmbedIE.suitable('https://example.com/embed/news/300040')

    # _match_id should return the numeric video id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # The instance must expose the extraction entry point
    assert callable(getattr(ie, '_real_extract'))

# Generated at 2026-11-02 20:48:43.003173
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
# nonce:ffa0b20e
    ie = UDNEmbedIE()
    assert isinstance(ie, UDNEmbedIE)
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-11-02 20:51:56.075249
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    # suitable() should accept http/https embed and play URLs
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    # non-matching URLs
    assert not ie.suitable('https://video.udn.com/embed/news/')
    assert not ie.suitable('https://video.udn.com/embed/news/notanumber')
    assert not ie.suitable('https://www.youtube.com/watch?v=12345')
    # id extraction
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'