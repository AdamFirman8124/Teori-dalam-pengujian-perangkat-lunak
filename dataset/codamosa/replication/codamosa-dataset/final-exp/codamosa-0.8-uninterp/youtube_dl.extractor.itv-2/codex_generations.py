

# Generated at 2022-06-14 16:34:52.168924
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012', {
        "id": '2a4547a0012',
        "ext": 'mp4',
        "title": 'Liar - Series 2 - Episode 6',
        "description": 'md5:d0f91536569dec79ea184f0a44cca089',
        "series": 'Liar',
        "season_number": 2,
        "episode_number": 6,
    })

# Generated at 2022-06-14 16:34:59.130671
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    i = ITVBTCCIE()
    assert i.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    i = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert i.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'


# Generated at 2022-06-14 16:35:03.412263
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ITVIE(None)._match_id(url) == '2a4547a0012'


# Generated at 2022-06-14 16:35:05.158140
# Unit test for constructor of class ITVIE
def test_ITVIE():
    instance = ITVIE(ITVIE())
    assert isinstance(instance, ITVIE)

# Generated at 2022-06-14 16:35:05.832836
# Unit test for constructor of class ITVIE
def test_ITVIE():
    a = ITVIE()

# Generated at 2022-06-14 16:35:06.719906
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:35:08.803686
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from .common import InfoExtractor
    print ("testing ITVIE constructor")
    ITVIE = ITVIE()

# Generated at 2022-06-14 16:35:12.092956
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITU = ITVBTCCIE()
    ITU._match_id(r'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:35:15.405864
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()
    assert extractor.ITVIE.__name__ == "ITVIE"


# Generated at 2022-06-14 16:35:19.735220
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    itvbtccie = ITVBTCCIE()
    assert itvbtccie._real_extract == ITVBTCCIE.__bases__[0]._real_extract

# Generated at 2022-06-14 16:35:53.010647
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034')
    ITVIE('https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024')

# Generated at 2022-06-14 16:35:59.626055
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._TEST['url'] == url
    ie = ITVBTCCIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie._TEST['url'] == url

# Generated at 2022-06-14 16:36:05.684925
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    assert info_extractor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert info_extractor.BTCC_URL_TEMPLATE == 'http://www.itv.com/btcc/races/%s'

# Generated at 2022-06-14 16:36:08.464927
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    inst = ITVBTCCIE()
    assert inst.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s"

# Generated at 2022-06-14 16:36:14.976832
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    test = ITVBTCCIE._TEST
    class FakeIPGeoHeader(object):
        def __init__(self):
            self.headers = test['info_dict']['headers']

    ie.geo_verification_headers = FakeIPGeoHeader
    res = ie._real_extract(test['url'])
    res.pop('upload_date')
    assert res == test['info_dict']

# Generated at 2022-06-14 16:36:18.608305
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:36:28.985242
# Unit test for constructor of class ITVIE
def test_ITVIE():
    class TestITVIE(ITVIE):
        def _download_json_impl(self, *args, **kargs):
            if args[0] == 'https://mercury.itv.com/api/video/%s' % TestITVIE._TEST['info_dict']['id']:
                return json.loads(TestITVIE._TEST['info_dict']['json_data'])
            return ITVIE._download_json_impl(self, *args, **kargs)

    ie = TestITVIE()
    ie.extract('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie.title() == 'Liar - Series 2 - Episode 6'

# Generated at 2022-06-14 16:36:32.540109
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    cIE = ITVBTCCIE()
    assert cIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:36:34.640233
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._TESTS[0]['info_dict']['id'] == ITVIE._match_id(ITVIE._TESTS[0]['url'])

# Generated at 2022-06-14 16:36:37.752855
# Unit test for constructor of class ITVIE
def test_ITVIE():
    try:
        unit_test_ITVIE = ITVIE('')
    except Exception as e:
        unit_test_ITVIE = None
        raise e
    assert unit_test_ITVIE is not None


# Generated at 2022-06-14 16:37:18.455569
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    class_ = ITVIE()
    assert(class_.suitable(url))
    assert (class_.IE_NAME == 'ITV')
    assert (class_.ie_key() == 'ItvCom:Itv')
    assert (class_.url_re == ITVIE._VALID_URL)
    assert (class_.valid_url(url))
    assert (class_.video_id == '2a4547a0012')
    assert (class_.valid_url('https://www.itv.com/hub/liar/2a4547a0012'))
    assert (class_.valid_url('http://www.itv.com/hub/liar/2a4547a0012'))

# Generated at 2022-06-14 16:37:26.630462
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Test constructor of class ITVBTCCIE
    # Test constructor of class ITVBTCCIE
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    ivt = ITVBTCCIE()
    assert ivt.url_result == BrightcoveNewIE.url_result
    assert ivt.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ivt._match_id == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:37:28.101951
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itv_btcc_ie = ITVBTCCIE()

    assert itv_btcc_ie.__class__.__name__ == 'ITVBTCCIE'

# Generated at 2022-06-14 16:37:28.804986
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
	obj = ITVBTCCIE()

# Generated at 2022-06-14 16:37:35.879496
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """Tests constructor of ITVBTCCIE class."""
    class_under_test = ITVBTCCIE
    class_under_test._download_json = lambda _, __, headers=None, data=None: {'Playlist': {'Video': {'MediaFiles': [{'DeliveryMethod':'http','Href':'http://static.video.itv.com/rms/GT_TOUR_DONINGTON_180709_HIGH/4bdd6a3f-a9f6-4b86-bf08-d78bfe27b2ed/VIDEO.mp4'}]}}}
    instance = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:37:44.407812
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .test_download import _test_download, _test_extract
    
    # ITVBTCCIE for IFE
    _test_extract(ITVBTCCIE, 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

    # ITVBTCCIE for Video
    _test_extract(ITVBTCCIE, 'http://www.itv.com/btcc/john-cleland-recreates-big-moment-for-itv-s-btcc')

# Generated at 2022-06-14 16:37:49.358378
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    # Testing ITV video
    # https://www.itv.com/hub/liar/2a4547a0012
    assert ie.IE_NAME == 'ITV'
    assert ie.IE_DESC == 'ITV Player'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:37:55.232271
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()
    assert itvbtccie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:38:04.151413
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():

    test_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    match = ITVBTCCIE._match_id(test_url)
    list_urls = ITVBTCCIE._extract_urls(test_url)
    print(match)
    print(list_urls)

    _test_instance = ITVBTCCIE(ITVBTCCIE.ie_key())
    print(_test_instance)

    # print("\n\n\n")

    # for _test_url in list_urls:
    #     print("\n\n\n")
    #     print("Test URL: " + _test_url)
    #     print("\n\n\n")

    #     _test_

# Generated at 2022-06-14 16:38:10.579313
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    class_type = ITVIE.__bases__[2]
    instance = class_type(ITVIE, ITVIE._download_webpage)
    assert instance._match_id(url) == '2a4547a0012'

# Generated at 2022-06-14 16:39:19.001054
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class_meta = ITVBTCCIE.__class__.__dict__
    i = ITVBTCCIE(class_meta['YOUTUBE_URL'], class_meta['YOUTUBE_IE_NAME'])
    assert(i.name == ITVBTCCIE.YOUTUBE_IE_NAME)
    assert(i._VALID_URL == class_meta['YOUTUBE_URL'])

# Generated at 2022-06-14 16:39:20.037669
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE()

# Generated at 2022-06-14 16:39:24.437270
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    i = ITVIE()
    i._downloader.params['geo_verification_headers'] = {
        'X-Forwarded-For': '42.42.42.42'
    }
    i._real_extract(url)

# Generated at 2022-06-14 16:39:31.342158
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert('btcc-2018-all-the-action-from-brands-hatch' == ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")._match_id("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"), "Failed to get playlist id")

# Generated at 2022-06-14 16:39:33.133713
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE("https://www.itv.com/hub/liar/2a4547a0012")

# Generated at 2022-06-14 16:39:39.635570
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Full url
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    # Constructor of class ITVBTCCIE
    ITVBTCCIE(url)
    # Full url
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    # Constructor of class ITVBTCCIE
    ITVBTCCIE(url)


# Generated at 2022-06-14 16:39:48.425700
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    for url in ['http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch']:
        ie = ITVBTCCIE(url)
        assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
        assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:39:49.995275
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """Check constructor of ITVIE class"""
    ITVIE('whatever', {})

# Generated at 2022-06-14 16:39:59.165528
# Unit test for constructor of class ITVIE
def test_ITVIE():
    class TestITVIE(ITVIE):
        def _download_webpage(self, url, video_id):
            res = {}
            
            def _search_regex(*args, **kwargs):
                return res.get('_search_regex')

            def _html_search_meta(*args, **kwargs):
                return res.get('_html_search_meta')

            def _search_json_ld(*args, **kwargs):
                return res.get('_search_json_ld')

            def _parse_json(*args, **kwargs):
                return res.get('_parse_json')

            def _download_json(*args, **kwargs):
                return res.get('_download_json')

            def _extract_m3u8_formats(*args, **kwargs):
                return

# Generated at 2022-06-14 16:40:01.416346
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % '5678501384001'
    assert BrightcoveNewIE.suitable(url)

# Generated at 2022-06-14 16:42:37.529897
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:42:38.729126
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Running this constructor should not fail
    ITVIE()



# Generated at 2022-06-14 16:42:40.884441
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._TESTS[0]['url'] == ITVIE(
        ITVIE._TESTS[0])._TEST.getURL()

# Generated at 2022-06-14 16:42:43.797723
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    print("\nTest ITVBTCCIE constructor")
    valid_url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    assert ITVBTCCIE._VALID_URL == valid_url

# Generated at 2022-06-14 16:42:49.940177
# Unit test for constructor of class ITVIE
def test_ITVIE(): 
    ie = ITVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:42:55.935585
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/[^/]+/[^/]+/index.html?videoId=%s'
    assert 'btcc' in ie.IE_NAME
    assert 'itv.com' in ie.VALID_URL

# Generated at 2022-06-14 16:42:56.924042
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # we need this check, because we have to have a test
    # which uses class name
    assert ITVIE.__name__ == 'ITVIE'

# Generated at 2022-06-14 16:43:00.466735
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    brcc = ITVBTCCIE()
    brcc._match_id(url)

# Generated at 2022-06-14 16:43:03.357550
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()
    assert itv_ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:43:13.322777
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    constructor = ITVBTCCIE

    # Test for BTCCIE.__init__()
    instance = constructor()

    assert instance._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert instance._TEST == {
        'url': 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',
        'info_dict': {
            'id': 'btcc-2018-all-the-action-from-brands-hatch',
            'title': 'BTCC 2018: All the action from Brands Hatch',
        },
        'playlist_mincount': 9,
    }
    assert instance.BRIGHTC