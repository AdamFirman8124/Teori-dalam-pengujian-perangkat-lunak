

# Generated at 2026-11-02 17:44:08.288078
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert not ie.suitable('https://www.itv.com/hub/liar/')
    assert not ie.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie.ie_key() == 'ITV'

# Generated at 2026-11-02 17:46:46.274508
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ie._TEST['url'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ie._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ie._TEST['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert ie._TEST['playlist_mincount'] == 9
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ie._match_id('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-11-02 17:48:31.436261
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

    # Check the extractor instantiates correctly and exposes its key
    assert extractor.ie_key() == 'ITV'
    assert ITVIE.ie_key() == 'ITV'

    # Check class-level attributes survived initialization
    assert extractor._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert extractor._GEO_COUNTRIES == ['GB']

    # Check URL matching behavior
    assert extractor.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert extractor.suitable('http://itv.com/hub/through-the-keyhole/2a2271a0033')
    assert not extractor.suitable('https://www.itv.com/hub/liar/')
    assert not extractor.suitable('https://www.example.com/hub/liar/2a4547a0012')

    # Check ID extraction
    assert extractor._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ITVIE._match_id('https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

# Generated at 2026-11-02 17:50:27.299632
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Constructor should build a usable instance with the expected metadata
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) == 4

    # URL suitability checks
    assert ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie.suitable('http://itv.com/hub/through-the-keyhole/2a2271a0033')
    assert not ie.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction from valid URLs
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'
    assert ie._match_id('https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024') == '2a2898a0024'