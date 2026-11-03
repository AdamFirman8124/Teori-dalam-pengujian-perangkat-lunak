

# Generated at 2026-11-03 02:52:58.975686
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Constructor should produce a valid InfoExtractor instance
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, UDNEmbedIE)

    # Class attributes
    assert UDNEmbedIE.IE_DESC == '聯合影音'
    assert UDNEmbedIE.ie_key() == 'UDNEmbed'
    assert UDNEmbedIE.ie_name() == 'UDNEmbed'

    # Valid URLs should be matched
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/embed/news/300040')
    assert UDNEmbedIE.suitable('https://video.udn.com/play/news/303776')
    assert UDNEmbedIE.suitable('//video.udn.com/embed/news/300040')

    # Invalid URLs should not be matched
    assert not UDNEmbedIE.suitable('https://video.udn.com/news/300040')
    assert not UDNEmbedIE.suitable('https://www.udn.com/news/300040')
    assert not UDNEmbedIE.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')

    # ID extraction
    assert UDNEmbedIE._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert UDNEmbedIE._match_id('https://video.udn.com/play/news/303776') == '303776'

    # Instance methods should be available
    assert hasattr(ie, '_real_extract')
    assert callable(ie._real_extract)

# Generated at 2026-11-03 02:57:37.737001
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

    valid_urls = [
        'http://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/news/300040',
        'https://video.udn.com/play/news/303776',
    ]
    for url in valid_urls:
        assert ie.suitable(url), url
        m = re.match(ie._VALID_URL, url)
        assert m is not None, url
        assert m.group('id') == url.rsplit('/', 1)[-1]

    invalid_urls = [
        'http://video.udn.com/news/300040',
        'https://video.udn.com/embed/news/',
        'https://video.udn.com/embed/news/notanumber',
        'https://www.youtube.com/watch?v=BaW_jenozKc',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url), url

    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-03 02:59:48.060069
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    '''
    Test the constructor of class UDNEmbedIE
    '''
    ie = UDNEmbedIE()

    # Instance is created successfully
    assert ie is not None
    assert isinstance(ie, InfoExtractor)

    # Class-level metadata
    assert ie.IE_DESC == '聯合影音'
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_NAME == 'UDNEmbedIE'

    # URL matching based on _VALID_URL
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://video.udn.com/news/303776')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')

    # ID extraction from valid URLs
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-03 03:01:10.188110
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Class description and registry key
    assert ie.IE_DESC == '聯合影音'
    assert UDNEmbedIE.ie_key() == 'UDNEmbed'

    # Valid URLs should be suitable
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # Invalid URLs should not be suitable
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('http://video.udn.com/embed/news/notanumber')
    assert not ie.suitable('http://video.udn.com/other/news/300040')

    # ID extraction
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'