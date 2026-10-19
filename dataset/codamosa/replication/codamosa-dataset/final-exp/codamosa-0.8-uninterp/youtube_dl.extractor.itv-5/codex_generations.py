

# Generated at 2022-06-14 16:34:55.618886
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ie.GEO_COUNTRIES == ['GB']
    assert ie.GEO_BYPASS == False
    assert ie.GEO_COUNTRIES == ['GB']
    assert ie.IE_NAME == 'itv'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:35:07.998574
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'http://www.itv.com/hub/emmerdale/2a4548a0021'
    video_id = ITVIE._match_id(url)
    webpage = ITVIE._download_webpage(url, video_id)
    params = extract_attributes(ITVIE._search_regex(
            r'(?s)(<[^>]+id="video"[^>]*>)', webpage, 'params'))
    ios_playlist_url = params.get('data-video-playlist') or params['data-video-id']
    hmac = params['data-video-hmac']

# Generated at 2022-06-14 16:35:09.122404
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()


# Generated at 2022-06-14 16:35:13.216143
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    expr = ITVBTCCIE()    
    expr.url = url
    expr._real_extract(url)

# Generated at 2022-06-14 16:35:21.274074
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # default values
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

    # alternative values
    ie.BRIGHTCOVE_URL_TEMPLATE = 'http://some.url/some.flash.player?video=%s'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://some.url/some.flash.player?video=%s'

# Generated at 2022-06-14 16:35:28.641869
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._TESTS[0]['info_dict']['episode_number'] == 6
    assert ITVIE._TESTS[0]['info_dict']['season_number'] == 2
    assert ITVIE._TESTS[0]['info_dict']['series'] == 'Liar'
    assert ITVIE._TESTS[0]['info_dict']['title'] == 'Liar - Series 2 - Episode 6'

# Generated at 2022-06-14 16:35:32.005528
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    test = ie.BRIGHTCOVE_URL_TEMPLATE % '3570380633001'
    assert('?videoId=3570380633001' in test)



# Generated at 2022-06-14 16:35:33.965322
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()
    assert itv_ie.BRIGHTCOVE_URL_TEMPLATE is None

# Generated at 2022-06-14 16:35:35.652695
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE()
    assert isinstance(instance, ITVBTCCIE)
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:35:37.876964
# Unit test for constructor of class ITVIE
def test_ITVIE():
    parser = ITVIE()
    assert parser.__class__.__name__ == 'ITVIE'
    #parser = ITVBTCCIE()
    #assert parser.__class__.__name__ == 'ITVBTCCIE'

# Generated at 2022-06-14 16:35:58.400033
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test = ITVIE(None)
    assert test.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s"

# Generated at 2022-06-14 16:36:00.136254
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE()
    assert isinstance(instance, ITVBTCCIE)

# Generated at 2022-06-14 16:36:02.098398
# Unit test for constructor of class ITVIE
def test_ITVIE():
	ie = ITVIE()
	assert ie.IE_NAME == 'itv'


# Generated at 2022-06-14 16:36:04.885289
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()._extract_info('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:36:05.883995
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE == ITVBTCCIE()

# Generated at 2022-06-14 16:36:07.492863
# Unit test for constructor of class ITVIE
def test_ITVIE():
    infoExtractor = ITVIE()
    assert infoExtractor.IE_NAME == 'ITV'


# Generated at 2022-06-14 16:36:12.954060
# Unit test for constructor of class ITVIE
def test_ITVIE():
    a = ITVIE()
    assert a._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert len(a._TESTS) == 4

# Generated at 2022-06-14 16:36:16.793977
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert ie.__class__ is ITVBTCCIE

# Generated at 2022-06-14 16:36:28.295846
# Unit test for constructor of class ITVIE
def test_ITVIE():
    video_id = '2a4547a0012'
    webpage = '<script type="application/ld+json">'

# Generated at 2022-06-14 16:36:29.115696
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()


# Generated at 2022-06-14 16:37:00.620702
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    inst = ITVBTCCIE()
    assert inst.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:06.769638
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_ITVBTCCIE = ITVBTCCIE()
    assert test_ITVBTCCIE._TEST == {
        'url': 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',
        'info_dict': {
            'id': 'btcc-2018-all-the-action-from-brands-hatch',
            'title': 'BTCC 2018: All the action from Brands Hatch',
        },
        'playlist_mincount': 9,
    }

# Generated at 2022-06-14 16:37:18.150848
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # test 1
    url = 'https://www.itv.com/hub/liar/2a4547a0012';
    itvIE = ITVIE(url);
    assert itvIE._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:37:24.172756
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()
    assert itvbtccie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert itvbtccie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:29.982713
# Unit test for constructor of class ITVIE
def test_ITVIE():
	test_ITV = ITVIE('https://www.itv.com/hub/liar/2a4547a0012')
	assert test_ITV.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:36.463978
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test = ITVBTCCIE()
    assert test._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert test._TEST == {
        'url': 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',
        'info_dict': {
            'id': 'btcc-2018-all-the-action-from-brands-hatch',
            'title': 'BTCC 2018: All the action from Brands Hatch',
        },
        'playlist_mincount': 9,
    }

# Generated at 2022-06-14 16:37:38.599128
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test code here
    IE = ITVIE()
    assertIE()

# Generated at 2022-06-14 16:37:39.203421
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:37:48.743219
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'http://www.itv.com/hub/liar/2a4547a0012'
    ie = ITVIE()
    ie._download_webpage = lambda url, video_id: '<html></html>'
    ie._extract_m3u8_formats = lambda url, video_id, ext, entry_protocol, m3u8_id, fatal: [
        {'url': 'http://video_url', 'ext': 'mp4'}
    ]
    ie._search_json_ld = lambda webpage, video_id, default: {}
    ie._search_regex = lambda pattern, string, name, default, group: '<html></html>'

# Generated at 2022-06-14 16:37:51.089999
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test that the ITVIE class is instantiated correctly
    ie = ITVIE()
    assert ie

# Generated at 2022-06-14 16:38:59.547059
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:00.830329
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE()
    assert itv.geo_verification_headers() != {}

# Generated at 2022-06-14 16:39:11.031816
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    webpage = '<html><head><title>BTCC 2018: All the action from Brands Hatch - Watch live - ITV Hub</title></head><body><script>data-video-id="5849876095001"</script></body></html>'
    ie = ITVBTCCIE()
    assert(ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')
    assert(ie._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:39:12.345944
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE()
    assert isinstance(instance, ITVBTCCIE)

# Generated at 2022-06-14 16:39:17.191554
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    ie = ITVBTCCIE()
    assert ie.url_result(url).url == url

# Generated at 2022-06-14 16:39:24.086721
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # print('Testing ITVIE class')
    videodata = ITVIE._real_extract(ITVIE, 'https://www.itv.com/hub/liar/2a4547a0012')
    print('\nVideo data:', videodata)
    print('\nVideo url:', videodata.get('url'))
    # if videodata.get('url'):
    #     print('\nDownloading video...')
    #     ydl.download([videodata.get('url')])


# Generated at 2022-06-14 16:39:35.534147
# Unit test for constructor of class ITVIE
def test_ITVIE():
    videos = [
        ('https://www.itv.com/hub/liar/2a4547a0012', {
            'url': 'https://www.itv.com/hub/liar/2a4547a0012',
            'id': '2a4547a0012',
            'title': 'Liar - Series 2 - Episode 6',
            'description': 'md5:d0f91536569dec79ea184f0a44cca089',
            'series': 'Liar',
            'season_number': 2,
            'episode_number': 6,
            'thumbnail': 're:^https?://.*\.jpg$',
        }),
    ]

    for video in videos:
        video_url, video_info = video

        assert video_url == video_info['url']

        video

# Generated at 2022-06-14 16:39:42.988773
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Get page to test on
    page_example = 'https://www.itv.com/hub/liar/2a4547a0012'
    webpage = ITVIE._download_webpage(ITVIE(), page_example, '2a4547a0012')

    params = extract_attributes(ITVIE._search_regex(
        r'(?s)(<[^>]+id="video"[^>]*>)', webpage, 'params'))

    ios_playlist_url = params.get('data-video-playlist') or params['data-video-id']
    hmac = params['data-video-hmac']
    headers = ITVIE.geo_verification_headers()

# Generated at 2022-06-14 16:39:44.866094
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    IE = ITVBTCCIE()
    assert IE.BRIGHTCOVE_URL_TEMPLATE is not None

# Generated at 2022-06-14 16:39:54.946614
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from . import ITVIE as ITVIE_module
    ITVIE_module._VALID_URL = 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)/?(?:[?#&]|$)'

# Generated at 2022-06-14 16:42:26.225682
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from ytdl.creator import Creator
    from ytdl.creator import Item
    from ytdl.creator import set_creator

    x = Creator(info_extractors=[ITVIE])
    y = Item(url)
    assert x.IE_NAME == y._transformer_for(x).IE_NAME

    set_creator(Creator(info_extractors=[ITVIE]))

# Generated at 2022-06-14 16:42:36.324791
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

# Generated at 2022-06-14 16:42:44.344825
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_cases = [
        [
            'http://www.itv.com/hub/liar/2a4547a0012',
            'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5897242275001',
        ],
        [
            'http://www.itv.com/hub/through-the-keyhole/2a2271a0033',
            'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5848121865001',
        ],
    ]

    for test_case in test_cases:
        url = test_case[0]
        expected_brighcove_url = test_case[1]

# Generated at 2022-06-14 16:42:47.247805
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    BTCCIE = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    BTCCIE.extract_info()

# Generated at 2022-06-14 16:42:50.559869
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_class = ITVBTCCIE()
    assert test_class.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:43:02.019674
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    result = ITVBTCCIE(None)._opf_extract_video(
        r'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert result == {'_type': 'url', 'url': 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5949356114001', 'ie_key': 'BrightcoveNew', 'id': '5949356114001', 'referrer': 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'}

# Generated at 2022-06-14 16:43:11.138700
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ITVIE_instance = ITVIE()
    ITVIE_result = ITVIE_instance.extract(url)
    assert ITVIE_result.keys() == {
        'id',
        'ext',
        'title',
        'description',
        'series',
        'season_number',
        'episode_number',
        'formats',
        'subtitles'
        }
    assert ITVIE_result.get('id') == '2a4547a0012'
    assert ITVIE_result.get('ext') == 'mp4'
    assert ITVIE_result.get('title') == 'Liar - Series 2 - Episode 6'

# Generated at 2022-06-14 16:43:14.618422
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ie = ITVIE()
    th = ie.test()
    assert th['url'] == url


# Generated at 2022-06-14 16:43:22.526365
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE._TEST['url'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._TEST['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert ITVBTCCIE._TEST['playlist_mincount'] == 9
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'




# Generated at 2022-06-14 16:43:31.768910
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .common import assertEquals
    from .test_brightcove import test_brightcove
    from .test_brightcove import test_brightcove_smart_player
    from .test_brightcove import test_brightcove_new

    import sys
    original_stdout = sys.stdout
