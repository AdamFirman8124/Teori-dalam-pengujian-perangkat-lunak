

# Generated at 2026-11-02 21:55:26.450640
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Constructor should instantiate without arguments and be an InfoExtractor
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes
    assert ITVBTCCIE.ie_key() == 'ITVBTCC'
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')
    assert ITVBTCCIE._VALID_URL == (
        r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)')

    # URL matching
    test_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE.suitable(test_url)
    assert not ITVBTCCIE.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # ID extraction
    assert ie._match_id(test_url) == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ie._match_id('https://www.itv.com/btcc/btcc-2019-donington-park') == \
        'btcc-2019-donington-park'

    # Test definition sanity
    assert ITVBTCCIE._TEST['url'] == test_url
    assert ITVBTCCIE._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._TEST['info_dict']['title'] == \
        'BTCC 2018: All the action from Brands Hatch'

# Generated at 2026-11-02 21:57:02.687395
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()
    assert isinstance(extractor, ITVIE)

    # Class-level attributes set at construction
    assert extractor._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert extractor._GEO_COUNTRIES == ['GB']
    assert isinstance(extractor._TESTS, list) and len(extractor._TESTS) == 4

    # Extractor metadata helpers
    assert ITVIE.ie_key() == 'ITV'
    assert ITVIE.ie_name() == 'ITV'

    # URL matching behaviour
    test_url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert extractor.suitable(test_url)
    assert extractor._match_id(test_url) == '2a4547a0012'

    # Non-hub URLs of other ITV extractors must not match
    assert not extractor.suitable(
        'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2026-11-02 21:58:13.969517
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    # Constructor should produce an instance of the extractor
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class attributes should be intact after construction
    assert ie.ie_key() == 'ITVBTCC'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

    # _TEST is a dict describing the test case
    test = ie._TEST
    assert test['url'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert test['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert test['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert test['playlist_mincount'] == 9

    # _match_id should extract playlist id from valid URLs
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ie._match_id('https://www.itv.com/btcc') is None

    # Constructor with a downloader argument should also work
    ie2 = ITVBTCCIE(downloader=None)
    assert isinstance(ie2, ITVBTCCIE)

# Generated at 2026-11-02 21:59:27.101960
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Class identity / keys
    assert ITVBTCCIE.ie_key() == 'ITVBTCC'
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME is None or isinstance(ie.IE_NAME, str)

    # Brightcove URL template is correctly defined on the instance
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')

    # Valid URL: suitable + id extraction
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ie.suitable(url)
    assert ie._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'

    # Optional intermediate path segment
    url2 = 'https://www.itv.com/btcc/btcc-2018-all-the-action-from-brands-hatch'
    assert ie.suitable(url2)
    assert ie._match_id(url2) == 'btcc-2018-all-the-action-from-brands-hatch'

    # Trailing path segments are allowed by the (?:[^/]+/)* group
    url3 = 'https://www.itv.com/btcc/races/news/btcc-2018-all-the-action-from-brands-hatch'
    assert ie.suitable(url3)
    assert ie._match_id(url3) == 'btcc-2018-all-the-action-from-brands-hatch'

    # Non-matching URLs must not be suitable
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert not ie.suitable('https://www.itv.com/')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # Instance exposes the standard InfoExtractor API surface used by _real_extract
    assert callable(ie._download_webpage)
    assert callable(ie._og_search_title)
    assert callable(ie.playlist_result)
    assert callable(ie.url_result)

# Generated at 2026-11-02 22:02:35.762882
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor should initialize downloader as None
    assert ie._downloader is None

    # Class attributes set on the subclass
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == \
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

    # ie_key derived from the class name
    assert ie.ie_key() == 'ITVBTCC'

    # URL matching / id extraction
    test_url = ie._TEST['url']
    assert ie.suitable(test_url)
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie._match_id(test_url) == 'btcc-2018-all-the-action-from-brands-hatch'

    # Test definition sanity
    assert ie._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ie._TEST['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert ie._TEST['playlist_mincount'] == 9