

# Generated at 2022-06-14 16:34:46.721863
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    print(ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE)

# Generated at 2022-06-14 16:34:48.455258
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert(ie == ITVBTCCIE)

# Generated at 2022-06-14 16:34:50.973583
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    ITVBTCCIE unit test
    """
    return ITVBTCCIE(ITVBTCCIE._TEST)

# Generated at 2022-06-14 16:34:59.663227
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    video_id = "btcc-2018-all-the-action-from-brands-hatch"

    instance = ITVBTCCIE(url)
    assert instance.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s"
    assert instance._match_id(url) == video_id
    assert instance.constructor_name == "ITVBTCCIE"
    assert instance.constructor_title == "ITV"

# Generated at 2022-06-14 16:35:02.198905
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    BTCCIE = ITVBTCCIE()
    assert isinstance(BTCCIE, ITVBTCCIE)

# Generated at 2022-06-14 16:35:05.715040
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """Test ITVIE constructor."""
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ITVIE(object())._real_extract(url)

# Generated at 2022-06-14 16:35:08.475985
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert ie.__name__ == 'ITVBTCC'

# Generated at 2022-06-14 16:35:16.189808
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    i = ITVBTCCIE(ITVIE())

    assert i.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

    assert i._VALID_URL == 'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:35:22.556381
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # test get_id
    assert ITVIE.get_id(r"https://www.itv.com/hub/liar/2a4547a0012") == "2a4547a0012"
    assert ITVIE.get_id(r"https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034") == "2a5159a0034"
    assert ITVIE.get_id(r"https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024") == "2a2898a0024"

# Generated at 2022-06-14 16:35:24.033847
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Check it does not raise an exception
    """
    ITVBTCCIE()

# Generated at 2022-06-14 16:35:56.416719
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:35:59.858535
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie_ITV = ITVIE()
    assert ie_ITV._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:36:03.860835
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:36:06.457591
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .test import test_btcc
    itvbtccie = ITVBTCCIE()
    test_btcc.test_btcc(itvbtccie)

# Generated at 2022-06-14 16:36:08.685609
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE("http://www.itv.com/hub/liar/2a4547a0012")
    assert ie is not None


# Generated at 2022-06-14 16:36:20.462134
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class Test(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, '_property_' + k, v)

# Generated at 2022-06-14 16:36:23.364638
# Unit test for constructor of class ITVIE
def test_ITVIE():
    if not ITVIE.working():
        return
    # Test to run with 'python -m youtube_dl.extractor.itv' command
    assert ITVIE().working()

# Generated at 2022-06-14 16:36:24.799132
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE()._VALID_URL == ITVIE._VALID_URL

# Generated at 2022-06-14 16:36:34.679051
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    video_id = ITVIE._match_id(url)
    webpage = ITVIE._download_webpage(url, video_id)
    params = extract_attributes(ITVIE._search_regex(
        r'(?s)(<[^>]+id="video"[^>]*>)', webpage, 'params'))
#    ios_playlist_url = params.get('data-video-playlist') or params['data-video-id']
    hmac = params['data-video-hmac']
    headers = ITVIE.geo_verification_headers()

# Generated at 2022-06-14 16:36:35.805572
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.ie_key() in IE_DESC

# Generated at 2022-06-14 16:37:15.327401
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_cases = [
        ['https://www.itv.com/hub/liar/2a4547a0012', '2a4547a0012',
            'Liar - Series 2 - Episode 6', 'md5:d0f91536569dec79ea184f0a44cca089',
            'Liar', 2, 6],
    ]
    for test_case in test_cases:
        ie = ITVIE()
        assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[^/?#&]+)'
        assert ie._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:37:16.719832
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test for constructor ITVIE
    iev = ITVIE()

# Generated at 2022-06-14 16:37:17.373891
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:37:26.484616
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Simple unit tests for ITVBTCCIE
    """
    # Test first case of if statement
    one = ITVBTCCIE(None, "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    # Test second case of if statement
    two = ITVBTCCIE(None, "https://www.itv.com/hub/liar/2a4547a0012")
    # Test third case of if statement
    three = ITVBTCCIE(None, "http://www.itv.com/btcc/races/btcc-2018")


# Generated at 2022-06-14 16:37:27.931052
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ie = ITVIE()
    assert ie.extract(url)

# Generated at 2022-06-14 16:37:30.637134
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:31.886889
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert(ie.__class__.__name__ == 'ITVBTCCIE')

# Generated at 2022-06-14 16:37:37.744411
# Unit test for constructor of class ITVIE
def test_ITVIE():
    unit = ITVIE('http://www.itv.com/hub/liar/2a4547a0012')
    assert unit._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert unit._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:37:40.469390
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None


# Generated at 2022-06-14 16:37:43.736753
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.ie_key() == 'ITVBTCC'
    assert ITVBTCCIE.ie_key() == 'ITVBTCC'
    assert ITVBTCCIE.ie_key() == 'ITVBTCC'

# Generated at 2022-06-14 16:38:48.408884
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE(None).BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:38:54.927001
# Unit test for constructor of class ITVIE
def test_ITVIE():

    test = ITVIE(ITVIE._downloader)

    assert(test.test_url("http://www.itv.com/hub/liar/2a4547a0012"))
    assert(test.test_url("http://www.itv.com/hub/liar/2a4547a0012", False))
    assert(test.test_url("http://www.itv.com/hub/liar/2a4547a0012", True))

# Generated at 2022-06-14 16:39:06.900026
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ios_playlist_url = 'https://vod-api.itv.com/api/v1/products/2a2271a0033/ios'
    hmac = 'BZ41MhZM0m3qxk9X34U6y/Ue/iU='
    headers = {
        'Accept': 'application/vnd.itv.vod.playlist.v2+json',
        'Content-Type': 'application/json',
        'hmac': hmac.upper(),
    }

# Generated at 2022-06-14 16:39:12.600822
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Create mock object of extractor class ITVIE
    itv_ie = ITVIE()
    assert itv_ie is not None
    # Create mock object of type 'InfoExtractor'
    info_extractor = InfoExtractor()
    # Test that InfoExtractor's __init__ was invoked correctly with 'ITVIE'
    # parameters i.e. that itv_ie is an instance of ITVIE
    info_extractor.initialize.assert_called_once_with(itv_ie, 'itv')

# Generated at 2022-06-14 16:39:15.465033
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE().ie_key() == 'itv:itv'


# Generated at 2022-06-14 16:39:23.999131
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ITVIE._download_webpage = lambda self, url, video_id: '{ "Playlist": { "Video": {}} }'
    x = ITVIE()
    extracted = x._real_extract(url)
    assert extracted.get('id') == '2a4547a0012', extracted.get('id') + ' is not ' + '2a4547a0012'
    assert extracted.get('title') == 'Liar - Series 2 - Episode 6', extracted.get('title') + ' is not ' + 'Liar - Series 2 - Episode 6'

# Generated at 2022-06-14 16:39:30.075492
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie_tv = ITVIE(None)
    assert ie_tv._IS_ITV_LANDING_PAGE.search(ie_tv._GEO_COUNTRIES[0]) == None, "ITVIE._IS_ITV_LANDING_PAGE.search(\"{}\") must return None".format(ie_tv._GEO_COUNTRIES[0])

# Generated at 2022-06-14 16:39:31.127378
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()



# Generated at 2022-06-14 16:39:34.421799
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ITVBTCCIE(None)._real_extract(test_url)

# Generated at 2022-06-14 16:39:37.907692
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    constructor = ITVBTCCIE.constructor('ITVBTCCIE')
    assert constructor('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == ITVBTCCIE

# Generated at 2022-06-14 16:42:08.510256
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE(None)

# Generated at 2022-06-14 16:42:15.862398
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    expected = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5544093564001&referrer=http%3A%2F%2Fwww.itv.com%2Fbtcc%2Fraces%2Fbtcc-2018-all-the-action-from-brands-hatch'
    actual = ITVBTCCIE().url_result('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')['url']
    assert actual == expected

# Generated at 2022-06-14 16:42:23.554522
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ITVIE._download_webpage = lambda self, url, video_id: ''
    ITVIE._search_regex = lambda self, pattern, string, name, default=NO_DEFAULT, group=None, fatal=True, flags=0: '<div class="a" data-video-id="{}" data-video-hmac="{}" data-video-playlist="{}"></div>'.format(
        video_id, hmac, playlist)

# Generated at 2022-06-14 16:42:24.273889
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()

# Generated at 2022-06-14 16:42:27.086771
# Unit test for constructor of class ITVIE
def test_ITVIE():
    class_name = "ITVIE"
    test_class = globals()[class_name]
    ins = test_class()
    name_field = ins.__class__.__name__
    assert name_field == class_name, \
        "Object of class {} should be called {}".format(name_field, class_name)


# Generated at 2022-06-14 16:42:29.152968
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.ie_key() == 'ITVBTCC'
    assert ITVBTCCIE.ie_key() in InfoExtractor._ies

# Generated at 2022-06-14 16:42:32.150101
# Unit test for constructor of class ITVIE
def test_ITVIE():
    content_url = "/hub/jeremy-kyle/2a5168a0005"
    _, _, result = ITVIE.suitable(content_url)
    assert result == "ITV"

# Generated at 2022-06-14 16:42:33.116616
# Unit test for constructor of class ITVIE
def test_ITVIE():

    assert ITVIE() != None

# Generated at 2022-06-14 16:42:37.858472
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE(
        'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')._real_extract(
        'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')


# Generated at 2022-06-14 16:42:40.689370
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

