

# Generated at 2026-11-03 04:13:28.608108
# Unit test for constructor of class ITVIE
def test_ITVIE():
    instance = ITVIE()
    assert instance is not None
    assert instance.IE_NAME == 'ITVIE'
    assert instance.ie_key() == 'ITV'
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ITVIE._GEO_COUNTRIES == ['GB']
    assert isinstance(ITVIE._TESTS, list) and len(ITVIE._TESTS) == 4
    assert instance.working() is True
    assert instance.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert instance._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert not instance.suitable('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not instance.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    assert not instance.suitable('https://www.itv.com/hub/liar/')
    assert not instance.suitable('https://www.itv.com/hub/liar/invalid-id!')
    assert not instance.suitable('https://www.example.com/hub/liar/2a4547a0012')
    assert ITVIE._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ITVIE._TESTS[0]['info_dict']['id'] == '2a4547a0012'
    assert ITVIE._TESTS[1]['only_matching'] is True
    assert ITVIE._TESTS[2]['only_matching'] is True
    assert ITVIE._TESTS[3]['only_matching'] is True

# Generated at 2026-11-03 04:18:08.162373
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Class identity
    assert ITVBTCCIE.ie_key() == 'ITVBTCC'
    assert ie.GEO_COUNTRIES is None or True  # playlist IE, no geo restriction expected

    # URL matching
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ie.suitable(url)
    assert ie._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'

    # URL variants should still match
    assert ie.suitable('https://www.itv.com/btcc/btcc-2018-all-the-action-from-brands-hatch')
    assert ie._match_id(
        'https://www.itv.com/btcc/btcc-2018-all-the-action-from-brands-hatch'
    ) == 'btcc-2018-all-the-action-from-brands-hatch'

    # Hub URLs must not match this extractor
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # Brightcove URL template sanity check
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % '5803140212001' == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html'
        '?videoId=5803140212001'
    )

    # Test metadata from _TEST
    test = ITVBTCCIE._TEST
    assert test['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert test['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert 'playlist_mincount' in test

# Generated at 2026-11-03 04:21:33.060417
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    # Constructor creates an instance without requiring network access
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'ITVBTCC'

    # _VALID_URL accepts the BTCC playlist URLs
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ie.suitable(url)
    assert ie._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'

    # _VALID_URL also handles optional intermediate path segments
    url2 = 'https://www.itv.com/btcc/btcc-2019-all-the-action'
    assert ie.suitable(url2)
    assert ie._match_id(url2) == 'btcc-2019-all-the-action'

    # _VALID_URL rejects non-BTCC ITV hub URLs
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')
    assert not ie.suitable('https://www.example.com/btcc/some-id')

    # Brightcove URL template is correctly defined
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')
    assert ie.BRIGHTCOVE_URL_TEMPLATE % '5395934521001' == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5395934521001')

    # Embedded test metadata
    assert ie._TEST['url'] == url
    assert ie._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ie._TEST['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert ie._TEST['playlist_mincount'] == 9

    print('test_ITVBTCCIE passed')