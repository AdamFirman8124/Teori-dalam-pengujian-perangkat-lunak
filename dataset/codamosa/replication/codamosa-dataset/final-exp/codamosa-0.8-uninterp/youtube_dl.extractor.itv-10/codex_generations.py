

# Generated at 2022-06-14 16:34:50.272756
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    # Test constructor of class ITVBTCCIE
    ITVBTCCIE(url, {
        'geo_ip_blocks': ['193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21'],
        'referrer': url
    })

# Generated at 2022-06-14 16:34:52.217321
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:34:53.031338
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:34:57.070153
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    "Make sure the constructor for ITVBTCCIE works"
    script_btcc_ie_obj = ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert(type(script_btcc_ie_obj) == ITVBTCCIE)

# Generated at 2022-06-14 16:34:58.151373
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()



# Generated at 2022-06-14 16:35:10.498162
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """Test constructor of class ITVBTCCIE."""
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    webpage = '<div data-video-id="605982637001" class="video-holder">'
    playlist_entries = [
        {
            '_type': 'url',
            'url': 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=605982637001',
            'ie_key': 'BrightcoveNew',
            'id': '605982637001'
        }
    ]
    playlist_id = 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:35:12.527732
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie._VALID_URL == ITVBTCCIE._VALID_URL

# Generated at 2022-06-14 16:35:21.594818
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Testing a real ITV programme by id. This id corresponds to Liar.
    # It should be functional as long as the programme is there
    itv = ITVIE()._real_extract('https://www.itv.com/hub/liar/2a4547a0012')
    assert itv['id'] == '2a4547a0012'
    assert itv['title'] == 'Liar - Series 2 - Episode 6'
    assert itv['description'] == 'md5:d0f91536569dec79ea184f0a44cca089'
    assert itv['series'] == 'Liar'
    assert itv['season_number'] == 2
    assert itv['episode_number'] == 6

# Generated at 2022-06-14 16:35:32.859196
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test = ITVBTCCIE()
    test.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert test.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert test._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:35:33.546792
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE({}, {})._VALID_URL == ITVIE._VALID_URL

# Generated at 2022-06-14 16:36:03.901823
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE._TEST['playlist_mincount'] = 9

if __name__ == '__main__':
    test_ITVBTCCIE()

# Generated at 2022-06-14 16:36:08.626594
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    t = ITVBTCCIE()
    t.BRIGHTCOVE_URL_TEMPLATE = "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s"
    assert t.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s"

# Generated at 2022-06-14 16:36:10.571447
# Unit test for constructor of class ITVIE
def test_ITVIE():
    d = ITVIE()
    assert d._VALID_URL == ITVIE._VALID_URL

# Generated at 2022-06-14 16:36:19.286184
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Should assert the ITVIE(InfoExtractor) constructor is working with valid url.
    url = 'http://www.itv.com/hub/liar/2a4547a0012'
    info_extractor = ITVIE(None)
    assert ITVIE._VALID_URL == re.compile(info_extractor._VALID_URL)
    info_extractor._real_initialize(url)
    assert info_extractor._match_id("") is None
    assert info_extractor._match_id(url) == '2a4547a0012'


# Generated at 2022-06-14 16:36:25.578661
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.IE_NAME == 'ITV'
    assert ie.IE_DESC == 'ITV'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']


# Generated at 2022-06-14 16:36:29.353734
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:36:30.699282
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_extractor_construction(ITVBTCCIE)

# Generated at 2022-06-14 16:36:38.078131
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/hub/the-chase/1a4191a0016'
    url_new = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    # test of _real_extract method
    itv = ITVIE()
    mobj = itv._real_extract(url)
    assert mobj['id'] == '1a4191a0016'
    # test of _real_extract method
    #itv_new = ITVBTCCIE()
    #mobj_new = itv_new._real_extract(url_new)
    #assert mobj_new['id'] == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:36:41.521662
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE._TEST['url'] == ITVBTCCIE(IE_NAME)._VALID_URL

# Generated at 2022-06-14 16:36:42.655019
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE(None).init()

# Generated at 2022-06-14 16:37:16.849627
# Unit test for constructor of class ITVIE
def test_ITVIE():
	ie = ITVIE()
	assert(ie._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)')
	assert(ie._GEO_COUNTRIES == ['GB'])
	assert(ie._TESTS[1]['url'] == 'https://www.itv.com/hub/through-the-keyhole/2a2271a0033')
	assert(ie._TESTS[1]['only_matching'] == True)


# Generated at 2022-06-14 16:37:26.063879
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    BTCC_URL = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    VIDEO_URL = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=6016962607001'

    BTCC_IE = ITVBTCCIE()
    assert BTCC_IE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:31.621636
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = "http://www.itv.com/hub/liar/2a4547a0012"
    ie = ITVIE(ITVIE.extract_info(ITVIE._extract_url(url), url))
    assert ie._VALID_URL == url

# Generated at 2022-06-14 16:37:33.205623
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvIE = ITVIE()
    itvIE._url_for_id('2a2898a0024')


# Generated at 2022-06-14 16:37:38.983527
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'http://www.itv.com/hub/love-your-garden/2a4547a0012'
    t = ITVIE(url)
    assert(t._match_id(url) == '2a4547a0012')
    assert(t.VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)')
    assert(t.GEO_COUNTRIES == ['GB'])

# Generated at 2022-06-14 16:37:41.330771
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE


# Generated at 2022-06-14 16:37:42.700499
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert isinstance(ie, ITVIE)

# Generated at 2022-06-14 16:37:44.748116
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()._real_extract('https://www.itv.com/hub/virals/2a4155a0009')

# Generated at 2022-06-14 16:37:54.947329
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """Unit test for constructor of class ITVBTCCIE"""
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    playlist_id = 'btcc-2018-all-the-action-from-brands-hatch'
    playlist_mincount = 9
    obj_test_ITVBTCCIE = ITVBTCCIE()
    obj_test_ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

    webpage = obj_test_ITVBTCCIE._download_webpage(url, playlist_id)

# Generated at 2022-06-14 16:38:03.981100
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE()
    assert itv._VALID_URL == "https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)"
    assert itv._GEO_COUNTRIES == ["GB"]

# Generated at 2022-06-14 16:39:05.900662
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvie = ITVIE()
    itvie._ITT_ID = '123'
    itvie._EMBED_TOKEN = 'abc'
    itvie._GEOLOCATION_TOKEN = 'def'

# Generated at 2022-06-14 16:39:08.165385
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    unit_test = ITVBTCCIE()
    assert unit_test.BASE_URL == 'BTCC_BASE_URL'


# Generated at 2022-06-14 16:39:11.830967
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # 'https://www.itv.com/hub/itv-racing/1a1598a0019'
    try:
        ITVBTCCIE('https://www.itv.com/hub/itv-racing/1a1598a0019')
    except:
        return False

    return True

# Generated at 2022-06-14 16:39:14.486795
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE()
    assert(itv._GEO_COUNTRIES == ['GB'])

# Generated at 2022-06-14 16:39:16.155458
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")

# Generated at 2022-06-14 16:39:24.722254
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE({})._real_extract({
        'url': 'https://www.itv.com/hub/liar/2a4547a0012',
        'info_dict': {
            'id': '2a4547a0012',
            'ext': 'mp4',
            'title': 'Liar - Series 2 - Episode 6',
            'description': 'md5:d0f91536569dec79ea184f0a44cca089',
            'series': 'Liar',
            'season_number': 2,
            'episode_number': 6,
        },
        'params': {
            # m3u8 download
            'skip_download': True,
        },
    })

# Generated at 2022-06-14 16:39:29.857714
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.geo_verification_headers() == {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Origin': 'http://www.itv.com',
        'Referer': 'http://www.itv.com',
    }

# Generated at 2022-06-14 16:39:32.816986
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Unit test for constructor of class ITVBTCCIE
    try:
        ITVBTCCIE()
    except Exception:
        assert False, 'Must not raise exception on creation of class ITVBTCCIE'

# Generated at 2022-06-14 16:39:36.511257
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    with open('tests/data/test_itv_btcc.json', 'r') as handle:
        data = json.loads(handle.read())
    assert len(data) == 1
    assert data[0]['url'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert data[0]['playlist_mincount'] == 9
    return True

# Generated at 2022-06-14 16:39:38.787250
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE({'geo_countries': []})._GEO_COUNTRIES == []
    assert ITVIE({})._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:42:03.162019
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    assert type(info_extractor) is type  # True if info_extractor is class ITVIE

# Generated at 2022-06-14 16:42:06.009731
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:42:07.961472
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE._TEST['info_dict']['title'] == ITVBTCCIE._TEST['url']

# Generated at 2022-06-14 16:42:09.068179
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:42:18.157592
# Unit test for constructor of class ITVIE
def test_ITVIE():
    _ITV_SAMPLE_URL = 'https://www.itv.com/hub/liar/2a4547a0012' # sample ITV url
    _ITV_SAMPLE_VIDEO_ID = '2a4547a0012' # sample video id
    _ITV_SAMPLE_TITLE = 'Liar - Series 2 - Episode 6'
    _ITV_SAMPLE_DESCRIPTION = 'md5:d0f91536569dec79ea184f0a44cca089'
    _ITV_SAMPLE_SERIES = 'Liar'
    _ITV_SAMPLE_SEASON_NUMBER = 2
    _ITV_SAMPLE_EPISODE_NUMBER = 6

# Generated at 2022-06-14 16:42:19.332504
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # ITVBTCCIE only exists for test purposes
    assert ITVBTCCIE

# Generated at 2022-06-14 16:42:20.778270
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE.__name__ == 'ITVIE'
    assert ITVIE.ie_key() == 'ITV'

# Generated at 2022-06-14 16:42:22.105435
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()
    assert isinstance(itvbtccie, ITVBTCCIE)

# Generated at 2022-06-14 16:42:22.643446
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE

# Generated at 2022-06-14 16:42:23.436821
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    x = ITVBTCCIE()