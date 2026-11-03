

# Generated at 2026-11-02 08:02:35.248458
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Constructor should produce an instance of InfoExtractor
    from .common import InfoExtractor
    assert isinstance(ie, InfoExtractor)

    # Basic extractor metadata
    assert ie.ie_key() == 'ITV'
    assert ie.ie_name() == 'itv'
    assert ie._GEO_COUNTRIES == ['GB']

    # _VALID_URL should match hub URLs and capture the video id
    m = ie._match_valid_url('https://www.itv.com/hub/liar/2a4547a0012')
    assert m is not None
    assert m.group('id') == '2a4547a0012'

    # www prefix is optional
    m = ie._match_valid_url('http://itv.com/hub/through-the-keyhole/2a2271a0033')
    assert m is not None
    assert m.group('id') == '2a2271a0033'

    # Non-hub URLs must not match
    assert ie._match_valid_url('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') is None
    assert ie._match_valid_url('https://www.example.com/hub/liar/2a4547a0012') is None

    # _match_id should return the captured group
    assert ie._match_id('https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Suitable instances should be available
    assert ITVIE.suitable('https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024')
    assert not ITVIE.suitable('https://www.itv.com/hub/')

# Generated at 2026-11-02 08:03:04.900576
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie is not None
    assert ie.ie_key() == 'ITV'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie.suitable('http://itv.com/hub/through-the-keyhole/2a2271a0033')
    assert not ie.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

# Generated at 2026-11-02 08:03:27.940434
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.ie_key() == 'ITV'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ie.suitable(url)
    assert ie._match_id(url) == '2a4547a0012'
    assert not ie.suitable('https://www.itv.com/hub/liar/')

# Generated at 2026-11-02 08:04:12.633335
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'ITV'
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie.suitable('http://itv.com/hub/through-the-keyhole/2a2271a0033')
    assert not ie.suitable('https://www.itv.com/hub/liar/')
    assert not ie.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'

# Generated at 2026-11-02 08:04:29.172497
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Instance should be created successfully and be an InfoExtractor
    assert isinstance(ie, ITVIE)
    assert isinstance(ie, InfoExtractor)

    # Geo restriction configuration
    assert ie._GEO_COUNTRIES == ['GB']

    # Suitable URLs should match
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie.suitable('http://www.itv.com/hub/through-the-keyhole/2a2271a0033')
    assert ie.suitable('https://itv.com/hub/james-martins-saturday-morning/2a5159a0034')

    # Unsuitable URLs should not match
    assert not ie.suitable('https://www.itv.com/hub/liar/')
    assert not ie.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.youtube.com/watch?v=1234')

    # ID extraction from valid URLs
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'

# Generated at 2026-11-02 08:04:47.712532
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Constructor should succeed and expose the expected extractor identity
    assert ITVIE.ie_key() == 'ITV'
    assert ie.ie_key() == 'ITV'

    # Class-level attributes set at construction
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 4

    # URL suitability checks
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie.suitable('http://itv.com/hub/through-the-keyhole/2a2271a0033')
    assert not ie.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.youtube.com/watch?v=abc')

    # ID extraction from valid URLs
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024') == '2a2898a0024'

# Generated at 2026-11-02 08:06:33.187769
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Check class-level attributes
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'itv:btcc'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')

    # Check the valid URL pattern matches and extracts the correct playlist id
    test_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    mobj = re.match(ie._VALID_URL, test_url)
    assert mobj is not None
    assert mobj.group('id') == 'btcc-2018-all-the-action-from-brands-hatch'

    # Check URL variants also match
    for variant in (
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',
        'https://www.itv.com/btcc/btcc-2018-all-the-action-from-brands-hatch',
        'http://itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',
    ):
        mobj = re.match(ie._VALID_URL, variant)
        assert mobj is not None, variant
        assert mobj.group('id') == 'btcc-2018-all-the-action-from-brands-hatch'

    # Check non-matching URLs
    for bad_url in (
        'https://www.itv.com/hub/liar/2a4547a0012',
        'https://www.example.com/btcc/races/test',
    ):
        assert re.match(ie._VALID_URL, bad_url) is None, bad_url

    # Check the Brightcove URL template formats correctly
    assert ie.BRIGHTCOVE_URL_TEMPLATE % '123456789' == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=123456789')

    # Check suitable() helper works with the class
    assert ITVBTCCIE.suitable(test_url)
    assert not ITVBTCCIE.suitable('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2026-11-02 08:08:39.549167
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.ie_key() == 'ITV'
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie.geo_verification_headers()['geo-verifier'] == 'GB' if hasattr(ie, 'geo_verification_headers') else True

# Generated at 2026-11-02 08:11:14.413361
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # constructor produces a working extractor instance
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'ITVBTCC'

    # _VALID_URL handling
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ie.suitable(url)
    assert ie._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'

    # variant URL shapes that must still match
    assert ie.suitable('https://www.itv.com/btcc/btcc-2018-all-the-action-from-brands-hatch')
    assert ie._match_id('https://www.itv.com/btcc/races/2018/brands-hatch') == 'brands-hatch'

    # URLs that must not match
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert not ie.suitable('https://www.itv.com/btcc/')
    assert not ie.suitable('http://www.example.com/btcc/races/some-race')

    # Brightcove URL template used to build playlist entries
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')
    assert ie.BRIGHTCOVE_URL_TEMPLATE % '5392716637001' == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5392716637001')

    # declared test metadata is consistent with the extractor
    assert ITVBTCCIE._TEST['url'] == url
    assert ITVBTCCIE._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._TEST['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert ITVBTCCIE._TEST['playlist_mincount'] == 9