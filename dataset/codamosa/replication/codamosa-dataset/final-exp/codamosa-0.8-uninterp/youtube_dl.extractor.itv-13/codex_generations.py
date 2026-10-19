

# Generated at 2022-06-14 16:34:53.078684
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test = ITVIE()._test_extract_info(
        'https://www.itv.com/hub/liar/2a4547a0012',
        'https://www.itv.com/hub/liar/2a4547a0012',
        {}
    )
    assert test.get('id') == '2a4547a0012'
    assert test.get('title') == 'Liar - Series 2 - Episode 6'
    assert test.get('thumbnail') == 'https://itv.scene7.com/is/image/itv/2019-09-03_liar_series_2_episode_6_desktop_5_tablet_6_mobile_6_landscape_1280x720_2x'
    assert test.get('series') == 'Liar'
    assert test.get

# Generated at 2022-06-14 16:34:54.906927
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('test', 'http://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:35:01.038579
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    obj = ITVIE(url)
    assert obj.URL == url
    url2 = 'https://www.itv.com/hub/through-the-keyhole/2a2271a0033'
    obj2 = ITVIE(url2)
    assert obj2.URL == url2

# Generated at 2022-06-14 16:35:13.169825
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    expected_url = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5770178349001'
    expected_id = '5770178349001'
    assert_equals(BrightcoveNewIE.suitable(ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % expected_id), True)
    assert_equals(ITVBTCCIE.suitable(url), True)
    assert_equals(ITVBTCCIE._VALID_URL, ITVBTCCIE._TEST['url'])

# Generated at 2022-06-14 16:35:16.189648
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:35:20.831743
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
	url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
	assert ITVBTCCIE(None)._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:35:21.886516
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert isinstance(ITVIE(), ITVIE)

# Generated at 2022-06-14 16:35:33.089177
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from ..compat import compat_str
    ITVIE("https://www.itv.com/hub/liar/2a4547a0012")
    ITVIE("https://www.itv.com/hub/through-the-keyhole/2a2271a0033")
    ITVIE("https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034")
    ITVIE("https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024")\
    .extract("https://www.itv.com/hub/liar/2a4547a0012",compat_str("1"))

# Generated at 2022-06-14 16:35:33.605600
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE().suitable()

# Generated at 2022-06-14 16:35:35.062643
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """ITvBTCCIE checks if ITVBTCCIE's constructor is working"""
    ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:36:04.050747
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE()._VALID_URL == ITVBTCCIE._VALID_URL

# Generated at 2022-06-14 16:36:08.247062
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """
    Unit test for constructor of class ITVIE
    """
    ITVIEobj = ITVIE(None)
    assert ITVIEobj._VALID_URL == "https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)"
    assert ITVIEobj._GEO_COUNTRIES == ['GB']
    ITVIEobj._downloader = None



# Generated at 2022-06-14 16:36:12.144030
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # A non-video variant of the ITVIE constructor (namely ITVBTCCIE) is tested
    # in _test_ITVBTCCIE in test_itv.py.
    assert ITVIE.__name__ == 'ITVIE'

# Generated at 2022-06-14 16:36:15.841693
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
	video_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
	assert ITVBTCCIE()._real_extract(video_url) is not None

# Generated at 2022-06-14 16:36:21.739254
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ITVBTCCIE(
        id = 'btcc-2018-all-the-action-from-brands-hatch',
        title = 'BTCC 2018: All the action from Brands Hatch'
    )

# Generated at 2022-06-14 16:36:22.442901
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:36:23.796369
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE

# Generated at 2022-06-14 16:36:33.929294
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .test import make_test_item
    from .brightcove import BrightcoveNewIE
    assert ITVBTCCIE.ie_key() == 'itv:btcc'
    assert ITVBTCCIE.test() == False
    assert ITVBTCCIE.test({'url': 'http://www.itv.com/hub/'}) == False
    assert ITVBTCCIE.test({'url': 'http://www.itv.com/btcc/'}) == False
    assert ITVBTCCIE.test({'url': 'http://www.itv.com/hub/'}, test_url=True) == False
    assert ITVBTCCIE.test({'url': 'http://www.itv.com/btcc/'}, test_url=True) == True

# Generated at 2022-06-14 16:36:45.692366
# Unit test for constructor of class ITVIE
def test_ITVIE():
    _TVIE = ITVIE()
    assert _TVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert _TVIE._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:36:46.942373
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    unittest.main()

# Generated at 2022-06-14 16:37:18.939540
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test URL and YoutubeID of ITVIE
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    youtube_id = '2a4547a0012'
    # Check if URL and YoutubeID is correct
    assert youtube_id == ITVIE._match_id(url)

# Generated at 2022-06-14 16:37:26.102772
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtcc = ITVBTCCIE()
    assert itvbtcc.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert itvbtcc._VALID_URL == 'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert itvbtcc._GEO_COUNTRIES == ['GB']
    assert itvbtcc.playlist_mincount == 9

# Generated at 2022-06-14 16:37:26.862497
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE('BTCC 2018: All the action from Brands Hatch')

# Generated at 2022-06-14 16:37:28.651449
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:37:29.094398
# Unit test for constructor of class ITVIE
def test_ITVIE():
    m = ITVIE()

# Generated at 2022-06-14 16:37:31.921157
# Unit test for constructor of class ITVIE
def test_ITVIE():
    instance = ITVIE({'url': 'http://youtube.com/watch?v=XvnYK'})
    instance._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:37:33.242577
# Unit test for constructor of class ITVIE
def test_ITVIE():
    obj = ITVIE('http://www.itv.com')
    assert obj.geo_countries == ['GB']

# Generated at 2022-06-14 16:37:39.003409
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from . import broadcity
    from . import thedailyshow

    ie = ITVIE()

    assert ie.geo_verification_headers().get('X-Forwarded-For') == '185.93.3.123'
    assert ie.BROADCITY_URL_TEMPLATE == 'https://link.theplatform.com/s/NnzsPC/media/guid/2410887629/%s?mbr=true'
    assert ie.THEDAILYSHOW_URL_TEMPLATE == 'http://media.mtvnservices.com/embed/mgid:arc:video:comedycentral.com:%s'

    assert isinstance(ie._ies[0], broadcity.ComedyCentralIE)
    assert isinstance(ie._ies[1], thedailyshow.TheDailyShowIE)

# Generated at 2022-06-14 16:37:43.604381
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ie = ITVBTCCIE()
    ie._download_webpage = lambda url: None
    ie._real_extract(url)

# Generated at 2022-06-14 16:37:47.617884
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class Constructor(ITVBTCCIE):
        def __init__(self, *args, **kwargs):
            pass

    assert Constructor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:38:56.361986
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # tests for ITVIE class with a video id
    video_id = '2a4547a0012'
    i = ITVIE()

# Generated at 2022-06-14 16:38:57.058819
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:39:01.146009
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    import yaml
    yaml.warnings({'error': False})

    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch/1'
    playlist_id = ITVBTCCIE._match_id(url)
    assert playlist_id == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:39:08.844409
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor_object = ITVIE()
    assert info_extractor_object._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert info_extractor_object._TESTS[1]['url'] == 'https://www.itv.com/hub/through-the-keyhole/2a2271a0033'
    assert info_extractor_object._TESTS[1]['only_matching'] == True

# Generated at 2022-06-14 16:39:12.735368
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class_instance = ITVBTCCIE()
    assert class_instance.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'


# Generated at 2022-06-14 16:39:15.778678
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ie = ITVBTCCIE()
    assert ie._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:39:17.627943
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE('https://www.itv.com/hub/liar/2a4547a0012') is not None

# Generated at 2022-06-14 16:39:19.419507
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test = ITVIE(IE=None)
    assert isinstance(test, ITVIE)



# Generated at 2022-06-14 16:39:20.092857
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:39:30.292632
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Test with a valid URL:
    # Test with an invalid URL:
    invalid_url = 'http://www.itv.com/BTCC/races/BTCC-2018-Race-2-highlights-Brands-Hatch-Indy'
    with pytest.raises(ExtractorError) as err:
        ITVBTCCIE()._real_extract(invalid_url)
    assert err.value.cause.__name__ == 'RegexNotFoundError'

    # Test with an invalid URL:
    invalid_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch?sdfs'
    assert ITVBTCCIE()._real_extract(invalid_url)

# Generated at 2022-06-14 16:41:56.033591
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:41:59.467504
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE.find('{player}') == -1 and \
        ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE.find('{account}') == -1 and \
        ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE.find('{policy}') == -1

# Generated at 2022-06-14 16:42:03.273649
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvie= ITVIE()
    url = "http://www.itv.com/hub/liar/2a4547a0012"
    # id = itvie._match_id(url)
    # print(id)
    # assert id == '2a4547a0012', "Unexpected ID"

# Generated at 2022-06-14 16:42:05.856590
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE(None)._real_extract({'url': 'https://www.itv.com/hub/liar/2a4547a0012', 'display_id': '2a4547a0012'})

# Generated at 2022-06-14 16:42:07.844253
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('http://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:42:10.858208
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Test ITVBTCCIE constructor
    """
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    ITVBTCCIE(url)

# Generated at 2022-06-14 16:42:12.482549
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    obj_instance = ITVBTCCIE()
    assert obj_instance is not None



# Generated at 2022-06-14 16:42:20.953860
# Unit test for constructor of class ITVIE
def test_ITVIE():
  video = ITVIE("https://www.itv.com/hub/liar/2a4547a0012")
  assert video.__class__.__name__ == ITVIE.__name__
  assert video.url == "https://www.itv.com/hub/liar/2a4547a0012"
  assert video.video_id == "2a4547a0012"
  assert video.title == "Liar - Series 2 - Episode 6"
  assert video.description == "LIAR is back, and Laura and DI Renton are in a race against time to discover the truth behind Who Killed Andrew Earlham?"
  assert video.duration == 2590
  assert video.series == "Liar"
  assert video.season_number == 2
  assert video.episode_number == 6
  assert video._type == "video"


# Generated at 2022-06-14 16:42:27.748639
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    itv = ITVIE()
    res = itv.suitable(url)
    assert res

    res = itv._real_extract(url)
    assert res

    assert res['id'] == '2a4547a0012'
    assert res['description'] == 'md5:d0f91536569dec79ea184f0a44cca089'
    assert res['episode_number'] == 6
    assert res['series'] == 'Liar'
    assert res['season_number'] == 2
    assert res['title'] == 'Liar - Series 2 - Episode 6'

# Generated at 2022-06-14 16:42:32.607633
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    try:
        ITVBTCCIE(TestInfoExtractor())._request_webpage(
            'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    except ExtractorError as e:
        assert "The downloaded webpage is not a HTML page" in str(e)
        return
    assert False