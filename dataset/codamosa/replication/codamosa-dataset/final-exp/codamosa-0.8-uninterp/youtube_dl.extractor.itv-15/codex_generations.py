

# Generated at 2022-06-14 16:34:47.623267
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itv_btcc_cie = ITVBTCCIE()
    assert itv_btcc_cie.BRIGHTCOVE_URL_TEMPLATE is not None

# Generated at 2022-06-14 16:34:55.788675
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    import urlparse
    url_path = urlparse.urlparse(url).path
    my_id = url_path.split('/')[-1]
    my_playlist_id = my_id
    assert my_id == 'btcc-2018-all-the-action-from-brands-hatch'
    assert my_playlist_id == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:34:57.372422
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """Test the constructor of class ITVIE"""
    assert ITVIE == type(ITVIE())

# Generated at 2022-06-14 16:35:09.757386
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()
    assert itv_ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:35:11.685066
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvBTCCIE = ITVBTCCIE()
    assert itvBTCCIE == ITVBTCCIE.ie_key()

# Generated at 2022-06-14 16:35:21.371637
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()
    assert itvbtccie._TEST['url'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert itvbtccie._TEST['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert itvbtccie._TEST['playlist_mincount'] == 9
    assert itvbtccie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'



# Generated at 2022-06-14 16:35:28.694437
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    ie = ITVBTCCIE(ITVBTCCIE._create_ie())
    ie._downloader.cache.remove(ie._cache_key(url))
    info = ie.extract(url)
    assert len(info['entries']) == 9
    assert_ok(info, 'entries', 'mincount')

# Generated at 2022-06-14 16:35:31.148356
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE(InfoExtractor())._ITVIE__video_id('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:35:33.585122
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE(InfoExtractor())._real_extract('https://www.itv.com/hub/liar/2a4547a0012')


# Generated at 2022-06-14 16:35:35.423567
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE().BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s', 'did not set BRIGHTCOVE_URL_TEMPLATE for ITVBTCCIE'

# Generated at 2022-06-14 16:36:07.209525
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ITVIE(ITVIE.create_geo_verification_headers)._real_extract(url)

# Generated at 2022-06-14 16:36:08.840209
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:36:12.361862
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from .brightcove import BrightcoveNewIE
    ITVIE.BRIGHTCOVE_URL_TEMPLATE = BrightcoveNewIE.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:36:15.203628
# Unit test for constructor of class ITVIE
def test_ITVIE():
    try:
        ITVIE()
        print('ITVIE constructor works!')
    except:
        print('ITVIE constructor not working properly!')


# Generated at 2022-06-14 16:36:19.286196
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:36:25.578611
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """
    Test for constructor of class ITVIE
    """
    # Test for constructor of class ITVIE
    constructor_test = ITVIE(downloader)
    assert_true(constructor_test)
    assert_equal(constructor_test.IE_NAME, 'itv')
    assert_equal(constructor_test.IE_DESC, 'ITV')


if __name__ == '__main__':
    from unittest import main
    main()

# Generated at 2022-06-14 16:36:26.176512
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:36:29.969691
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.suitable('http://www.itv.com/hub/liar/2a4547a0012') == True
    assert ie.suitable('http://www.google.com') == False

# Generated at 2022-06-14 16:36:33.477659
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    entries = ITVBTCCIE()._real_extract('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')['entries']
    assert len(entries) == 9
    assert entries[0]['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'

# Generated at 2022-06-14 16:36:35.170953
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE('https://www.itv.com/hub/liar/2a4547a0012').__class__ == ITVIE



# Generated at 2022-06-14 16:37:06.817653
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._match_id(url + '/') == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._match_id(url + '/thisfolderdoesnotexist') == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._match_id(url + '/thisfolderdoesnotexist/') == 'btcc-2018-all-the-action-from-brands-hatch'
   

# Generated at 2022-06-14 16:37:18.199837
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']
    assert ie._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ie._TESTS[0]['info_dict']['id'] == '2a4547a0012'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert ie._TESTS[0]['info_dict']['title'] == 'Liar - Series 2 - Episode 6'

# Generated at 2022-06-14 16:37:20.656765
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ie = ITVIE()
    assert ie.suitable(url)

# Generated at 2022-06-14 16:37:28.621009
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # test with an incomplete/partially filled dictionary for video_data
    incomplete_ios_playlist = {'Playlist': {'Video': {}}}
    # test with an empty dictionary for video_data
    empty_ios_playlist = {'Playlist': {'Video': {}}}
    # test with a complete dictionary for video_data
    complete_ios_playlist = {'Playlist': {'Video': {'MediaFiles': [{'Href': 'test.mp4'}]}}}

    # test the constructor with an input dictionary which is not a dictionary
    info = ITVIE._real_extract(ITVIE(), 'https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034', ['a'])
    assert info is None

    # test the constructor with an input dictionary

# Generated at 2022-06-14 16:37:32.758253
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    s = ITVBTCCIE('test', 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert s.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:33.517118
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    a = ITVBTCCIE()

# Generated at 2022-06-14 16:37:35.880596
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:37:40.684456
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:42.437259
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE("https://www.itv.com/hub/liar/2a4547a0012")

# Generated at 2022-06-14 16:37:42.930032
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE([]).construct_ie()

# Generated at 2022-06-14 16:38:33.513643
# Unit test for constructor of class ITVIE
def test_ITVIE():
    video_id = '2a4547a0012'
    url = 'https://www.itv.com/hub/liar/%s' % video_id
    _, play_list = ITVIE._get_video_info(url)
    assert play_list

# Generated at 2022-06-14 16:38:39.733987
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ITVBTCCIE._TEST == {
    'url': 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',
    'info_dict': {
        'id': 'btcc-2018-all-the-action-from-brands-hatch',
        'title': 'BTCC 2018: All the action from Brands Hatch',
    },
    'playlist_mincount': 9,
    }

# Generated at 2022-06-14 16:38:47.868594
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    a = ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert a.__class__.__name__ == "ITVBTCCIE"
    assert a.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:38:52.328843
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvBTCCIE = ITVBTCCIE('')
    assert itvBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:38:56.012813
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test = ITVBTCCIE()
    assert test.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:02.943627
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    result = ITVBTCCIE()._real_extract("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    # print("Found result: '" + str(result) + "'")
    if len(result) < 1:
        raise AssertionError("ITVBTCCIE._real_extract() returned " + str(len(result)) + ". Expecting at least 1.")

# Generated at 2022-06-14 16:39:10.303528
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._TESTS[0]['info_dict'] == {'id': '2a4547a0012',
                                         'ext': 'mp4',
                                         'title': 'Liar - Series 2 - Episode 6',
                                         'description': 'md5:d0f91536569dec79ea184f0a44cca089',
                                         'series': 'Liar',
                                         'season_number': 2,
                                         'episode_number': 6}
    assert ie._TESTS[0]['params'] == {'skip_download': True}

# Generated at 2022-06-14 16:39:14.111066
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    x = ITVBTCCIE('https://www.itv.com/hub/itv-racing-live-from-towcester-5803')
    assert x.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:24.503052
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'http://www.itv.com/hub/liar/2a4547a0012'

# Generated at 2022-06-14 16:39:35.890368
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVE = ITVIE()
    # Test with ITV Hub & ITV.com
    # ITV Hub was launched in 2016 & ITV.com was the old ITV Player
    url = "https://www.itv.com/hub/liar/2a4547a0012"
    req = ITVE._request_webpage(url, "2a4547a0012")
    assert isinstance(req, str)
    assert req.startswith("{") and req.endswith("}")
    assert ITVE._downloader.params['headers']['Accept'].startswith("application/vnd.itv.vod.playlist.v2+json")
    assert ITVE._downloader.params['headers']['Content-Type'] == "application/json"

# Generated at 2022-06-14 16:41:47.888758
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    try:
        ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    except:
        assert False

# Generated at 2022-06-14 16:41:55.858818
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    playlist_id = "btcc-2018-all-the-action-from-brands-hatch"

# Generated at 2022-06-14 16:41:56.366163
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:41:58.023375
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE(ITVBTCCIE._downloader)._VALID_URL == ITVBTCCIE._VALID_URL

# Generated at 2022-06-14 16:42:05.816475
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test class constructor
    # the itv.com site has been unstable and this test was failing
    # randomly. To avoid this, pass the test if the site is down.
    try:
        ie = ITVIE()
    except:
        print('Test aborted due to instability of itv.com site')
        return

    # Test backward compatibility with old URL format
    old_url = 'http://www.itv.com/itvplayer/video/?Filter=343762'
    new_url = 'http://www.itv.com/hub/lorraine/2a3938a0004'
    assert ie._match_id(old_url) == ie._match_id(new_url)

# Generated at 2022-06-14 16:42:10.248620
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    info = ITVBTCCIE._real_extract('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert info['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert info['playlist_mincount'] == 9

# Generated at 2022-06-14 16:42:15.980284
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    # Constructor does not require internet connection. Thus, no need to download webpage
    itvbtccie = ITVBTCCIE()
    itvbtccie._real_extract(url)
    # Just retrieve the class name and nothing else
    print(itvbtccie.__class__.__name__)

# Generated at 2022-06-14 16:42:18.236947
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    temp = ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")

# Generated at 2022-06-14 16:42:22.039013
# Unit test for constructor of class ITVIE
def test_ITVIE():
    s = ITVIE('ITVIE', 'http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034')
    assert s.name == 'ITVIE'
    assert s.url == 'http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034'

# Generated at 2022-06-14 16:42:30.941697
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie._TEST[0] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ie._TEST[1] == {
        'id': 'btcc-2018-all-the-action-from-brands-hatch',
        'title': 'BTCC 2018: All the action from Brands Hatch',
    }
    assert ie._TEST[2] == 'playlist'
    assert ie._TEST[3] == {'expected_count': 9}