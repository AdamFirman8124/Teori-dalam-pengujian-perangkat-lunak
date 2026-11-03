

# Generated at 2026-11-02 15:48:20.223244
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Check extractor metadata
    assert ie.IE_DESC == '聯合影音'
    assert ie.ie_key() == 'UDNEmbed'

    # Check URL patterns compiled correctly
    assert ie._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

    # suitable() accepts both 'embed' and 'play' paths with http(s)
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # suitable() rejects malformed/foreign URLs
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('http://video.udn.com/embed/news/abc')
    assert not ie.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')

    # _match_id extracts numeric video ids
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-02 15:49:39.029530
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Instantiate the extractor (constructor takes an optional downloader)
    ie = UDNEmbedIE()
    assert ie is not None
    assert isinstance(ie, InfoExtractor)

    # Check class metadata
    assert UDNEmbedIE.IE_DESC == '聯合影音'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == \
        r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    # Constructor should set the downloader to None when not provided
    assert ie._downloader is None

    # URL matching should work with both embed and play paths
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')

    # ID extraction from valid URLs
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-02 15:51:31.926585
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructing without arguments should succeed
    ie = UDNEmbedIE()

    # No downloader attached by default
    assert ie._downloader is None

    # IE_NAME is derived from the class name with the trailing 'IE' stripped
    assert ie.IE_NAME == 'UDNEmbed'

    # Class-level metadata
    assert ie.IE_DESC == '聯合影音'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == \
        r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == \
        r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

    # Constructor should also accept an optional downloader argument
    downloader = object()
    ie_with_downloader = UDNEmbedIE(downloader)
    assert ie_with_downloader._downloader is downloader

    # URLs matching the valid URL pattern should be deemed suitable
    for url in (
        'http://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/news/300040',
        'https://video.udn.com/play/news/303776',
    ):
        assert ie.suitable(url)

    # Unrelated URLs should not be suitable
    for url in (
        'http://video.udn.com/news/300040',
        'https://video.udn.com/embed/news/abc',
        'http://video.udn.com/embed/news/',
        'http://example.com/embed/news/300040',
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    ):
        assert not ie.suitable(url)

    # _match_id should extract the numeric video id
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-02 15:53:15.351320
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie.working()
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert not UDNEmbedIE.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')