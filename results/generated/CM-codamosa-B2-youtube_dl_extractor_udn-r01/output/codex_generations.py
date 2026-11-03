

# Generated at 2026-11-03 00:51:54.857189
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Basic attributes
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert UDNEmbedIE.ie_key() == 'UDNEmbed'

    # URL pattern constants
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == \
        r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == \
        r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

    # suitable() should accept valid URLs
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # suitable() should reject invalid URLs
    assert not ie.suitable('https://video.udn.com/news/300040')
    assert not ie.suitable('https://video.udn.com/embed/news/abc')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # _match_id() should extract the numeric video id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # Protocol-relative pattern matches protocol-relative URLs directly
    assert re.match(
        UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL,
        '//video.udn.com/embed/news/300040') is not None
    assert re.match(
        UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL,
        '//video.udn.com/play/news/303776') is not None

    # Working dir and working tests metadata sanity checks
    assert len(UDNEmbedIE._TESTS) == 3
    assert UDNEmbedIE._TESTS[0]['info_dict']['id'] == '300040'
    assert UDNEmbedIE._TESTS[1]['only_matching'] is True
    assert UDNEmbedIE._TESTS[2]['only_matching'] is True

# Generated at 2026-11-03 00:52:58.957614
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor should be callable with no arguments
    ie = UDNEmbedIE()
    assert ie is not None

    # Class-level metadata set at construction/definition time
    assert ie.IE_DESC == '聯合影音'
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.working()

    # URL matching wired up by the constructor's class attributes
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('http://video.udn.com/embed/news/')

    # ID extraction from valid URLs
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-03 00:54:17.604259
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Constructor creates a valid instance inheriting from InfoExtractor
    assert ie is not None
    assert isinstance(ie, InfoExtractor)

    # Default IE name is derived from the class name
    assert ie.IE_NAME == 'UDNEmbed'

    # Class-level attributes are correctly set
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == \
        r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == \
        r'https?://' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'.lstrip('/')

    # suitable() accepts valid URLs, including protocol-relative ones
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('//video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # suitable() rejects invalid URLs
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('http://video.udn.com/embed/news/abc')
    assert not ie.suitable('http://example.com/embed/news/300040')
    assert not ie.suitable('http://video.udn.com/news/300040')

    # _match_id extracts the numeric video id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # _match_id raises AssertionError on a non-matching URL
    try:
        ie._match_id('http://video.udn.com/news/300040')
        assert False, 'expected AssertionError for non-matching URL'
    except AssertionError:
        pass

# Generated at 2026-11-03 00:57:41.177265
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Constructor creates a usable extractor instance
    assert ie is not None

    # Class-level metadata
    assert ie.IE_DESC == '聯合影音'
    assert UDNEmbedIE.IE_NAME in (None, 'UDNEmbed')
    assert ie.ie_key() == 'UDNEmbed'

    # Valid URLs are recognized by the extractor
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # Invalid URLs are rejected
    assert not ie.suitable('http://video.udn.com/news/300040')
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # The video id is correctly extracted from matching URLs
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-03 00:58:27.917817
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie is not None
    assert ie._downloader is None
    assert ie.IE_DESC == '聯合影音'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-11-03 00:58:56.947240
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie is not None
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_DESC == '聯合影音'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('http://video.udn.com/news/300040')
    assert not ie.suitable('http://example.com/embed/news/300040')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-03 00:59:18.757099
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://video.udn.com/embed/news/')
    assert not ie.suitable('https://video.udn.com/embed/news/abc')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-03 01:00:10.394064
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
# nonce:e82e7f2a
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('http://video.udn.com/embed/news/abc')
    assert not ie.suitable('http://video.udn.com/news/300040')
    assert not ie.suitable('http://www.youtube.com/watch?v=12345')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'
    assert ie._downloader is None
    assert len(ie._TESTS) == 3
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert ie._TESTS[0]['info_dict']['title'] == '生物老師男變女 全校挺"做自己"'
    assert ie._TESTS[0]['expected_warnings'] == ['Failed to parse JSON Expecting value']
    assert ie._TESTS[1]['only_matching'] is True
    assert ie._TESTS[2]['only_matching'] is True