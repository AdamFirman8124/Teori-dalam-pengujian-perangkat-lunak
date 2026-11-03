

# Generated at 2026-11-01 19:50:21.596912
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Unit test for the constructor of class UDNEmbedIE."""
    # Construct an instance with no downloader (default argument)
    ie = UDNEmbedIE()

    # Instance is created successfully and inherits from InfoExtractor
    assert isinstance(ie, UDNEmbedIE)
    assert isinstance(ie, InfoExtractor)

    # Class description metadata
    assert UDNEmbedIE.IE_DESC == u'聯合影音'

    # Protocol-relative valid URL regex matches embed and play variants
    assert re.match(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL,
                    u'//video.udn.com/embed/news/300040') is not None
    assert re.match(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL,
                    u'//video.udn.com/play/news/303776') is not None

    # Full valid URL handling via suitable()
    assert ie.suitable(u'http://video.udn.com/embed/news/300040')
    assert ie.suitable(u'https://video.udn.com/embed/news/300040')
    assert ie.suitable(u'https://video.udn.com/play/news/303776')

    # Invalid URLs should not match
    assert not ie.suitable(u'https://video.udn.com/embed/news/')
    assert not ie.suitable(u'https://video.udn.com/embed/movie/300040')
    assert not ie.suitable(u'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction from matched URLs
    assert ie._match_id(u'http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id(u'https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-01 19:50:58.930025
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-01 19:52:10.752515
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'

    # test _VALID_URL
    assert re.match(UDNEmbedIE._VALID_URL, 'http://video.udn.com/embed/news/300040')
    assert re.match(UDNEmbedIE._VALID_URL, 'https://video.udn.com/embed/news/300040')
    assert re.match(UDNEmbedIE._VALID_URL, 'https://video.udn.com/play/news/303776')
    assert not re.match(UDNEmbedIE._VALID_URL, 'http://video.udn.com/embed/news/')
    assert not re.match(UDNEmbedIE._VALID_URL, 'http://video.udn.com/embed/news/abc')
    assert not re.match(UDNEmbedIE._VALID_URL, 'ftp://video.udn.com/embed/news/300040')

    # test suitable
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')

    # test _match_id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-01 19:52:42.498136
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test the constructor of UDNEmbedIE."""
    ie = UDNEmbedIE()
    assert ie is not None
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == u'聯合影音'

    # Check URL suitability based on _VALID_URL
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('http://example.com/video/12345')

    # Check ID extraction from various URL forms
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'
    assert ie._match_id('//video.udn.com/embed/news/300040') == '300040'

# Generated at 2026-11-01 19:53:26.119948
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor should work without arguments (downloader defaults to None)
    ie = UDNEmbedIE()
    assert ie is not None

    # Constructor should also accept an explicit downloader argument
    ie2 = UDNEmbedIE(downloader=None)
    assert ie2 is not None

    # Basic class-level metadata
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'

    # Valid URLs should be recognized and yield the correct video id
    valid_urls = {
        'http://video.udn.com/embed/news/300040': '300040',
        'https://video.udn.com/embed/news/300040': '300040',
        'https://video.udn.com/play/news/303776': '303776',
    }
    for url, expected_id in valid_urls.items():
        assert ie.suitable(url), 'URL should be suitable: %s' % url
        assert ie._match_id(url) == expected_id

    # Protocol-relative URL pattern should match without a scheme
    assert re.match(
        UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL,
        '//video.udn.com/embed/news/300040') is not None
    assert re.match(
        UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL,
        '//video.udn.com/play/news/303776') is not None

    # Invalid URLs should not be recognized
    invalid_urls = (
        'https://video.udn.com/news/300040',
        'https://video.udn.com/embed/news/abc',
        'https://video.udn.com/embed/news/',
        'https://example.com/embed/news/300040',
        'ftp://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/other/300040',
    )
    for url in invalid_urls:
        assert not ie.suitable(url), 'URL should not be suitable: %s' % url

# Generated at 2026-11-01 19:54:22.547332
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Instance is created successfully and is an InfoExtractor subclass
    assert isinstance(ie, InfoExtractor)

    # Check class-level metadata attributes
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.ie_desc() == '聯合影音'
    assert ie.IE_DESC == '聯合影音'

    # Check URL matching behavior
    valid_urls = [
        'http://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/news/300040',
        'https://video.udn.com/play/news/303776',
    ]
    for url in valid_urls:
        assert ie.suitable(url), 'URL should match: %s' % url
        assert ie._match_id(url) == url.rsplit('/', 1)[-1]

    invalid_urls = [
        'http://video.udn.com/embed/news/',
        'https://video.udn.com/embed/news/abc',
        'ftp://video.udn.com/embed/news/300040',
        'https://video.udn.com/news/303776',
        '',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url), 'URL should not match: %s' % url

    # Working flag should be initialized to True
    assert ie.working() is True

    # _TESTS should be defined as a non-empty list of dicts
    assert isinstance(ie.get_testcases(False), list) and len(ie.get_testcases(False)) > 0

# Generated at 2026-11-01 19:55:11.390508
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Class-level attributes
    assert ie.IE_DESC == '聯合影音'
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'

    # Valid URLs should match and extract the correct id
    for url, video_id in [
        ('http://video.udn.com/embed/news/300040', '300040'),
        ('https://video.udn.com/embed/news/300040', '300040'),
        ('https://video.udn.com/play/news/303776', '303776'),
    ]:
        assert ie.suitable(url), url
        assert ie._match_id(url) == video_id, url

    # Invalid URLs should not match
    for url in [
        'https://video.udn.com/news/303776',
        'https://example.com/embed/news/300040',
        'ftp://video.udn.com/embed/news/300040',
    ]:
        assert not ie.suitable(url), url

# Generated at 2026-11-01 19:56:28.087712
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # Constructor should initialize with no downloader attached
    assert ie._downloader is None

    # Class-level metadata
    assert ie.IE_DESC == '聯合影音'
    assert UDNEmbedIE._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

    # The extractor is suitable for all documented URL forms
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')

    # ...and rejects unsuitable URLs
    assert not ie.suitable('http://video.udn.com/news/300040')
    assert not ie.suitable('http://video.udn.com/embed/news/abc')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')

    # Video id extraction from valid URLs
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # The protocol-relative pattern also matches scheme-less URLs
    mobj = re.match(
        UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL,
        '//video.udn.com/embed/news/300040')
    assert mobj is not None
    assert mobj.group('id') == '300040'

# Generated at 2026-11-01 19:57:08.026175
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert not ie.suitable('https://video.udn.com/embed/news/')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

# Generated at 2026-11-01 19:58:19.298542
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor should build a usable instance without arguments
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None

    # Class-level metadata
    assert ie.IE_DESC == '聯合影音'
    assert ie.ie_key() == 'UDNEmbed'

    # URL patterns as constructed in the class body
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    # Built-in test definitions
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 3
    first = ie._TESTS[0]
    assert first['url'] == 'http://video.udn.com/embed/news/300040'
    assert first['info_dict']['id'] == '300040'
    assert first['info_dict']['ext'] == 'mp4'
    assert first['info_dict']['title'] == '生物老師男變女 全校挺"做自己"'
    assert first['params']['skip_download'] is True
    for t in ie._TESTS[1:]:
        assert t.get('only_matching') is True
    assert ie._TESTS[1]['url'] == 'https://video.udn.com/embed/news/300040'
    assert ie._TESTS[2]['url'] == 'https://video.udn.com/play/news/303776'

    # URL suitability checks
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://video.udn.com/news/303776')
    assert not ie.suitable('http://video.udn.com/embed/news/')
    assert not ie.suitable('http://video.udn.com/embed/news/abcd')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # Video id extraction via the compiled pattern
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'
    assert ie._match_id('http://video.udn.com/embed/news/000123') == '000123'

# Generated at 2026-11-01 19:59:09.165446
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    # The extractor should carry its description
    assert ie.IE_DESC == '聯合影音'

    # _VALID_URL must accept http/https embed and play URLs
    for url in (
        'http://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/news/300040',
        'https://video.udn.com/play/news/303776',
    ):
        assert ie.suitable(url), '%r should be suitable' % url

    # Protocol-relative, non-embed/play and foreign URLs must not match
    assert not ie.suitable('//video.udn.com/embed/news/300040')
    assert not ie.suitable('http://video.udn.com/news/300040')
    assert not ie.suitable('https://example.com/embed/news/300040')

    # Video id extraction via _match_id
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/303776') == '303776'

    # The real extraction logic must be present and callable
    assert callable(ie._real_extract)

# Generated at 2026-11-01 19:59:49.202931
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_DESC == '聯合影音'
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/play/news/303776')
    assert not ie.suitable('https://video.udn.com/news/303776')
    assert not ie.suitable('https://video.udn.com/embed/news/')
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('http://video.udn.com/play/news/303776') == '303776'