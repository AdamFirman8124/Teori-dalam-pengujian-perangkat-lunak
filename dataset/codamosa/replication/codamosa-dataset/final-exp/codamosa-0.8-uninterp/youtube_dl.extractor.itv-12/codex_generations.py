

# Generated at 2022-06-14 16:34:45.289660
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()

# Generated at 2022-06-14 16:34:56.661074
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    playlist_id = 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:35:09.229834
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

# Generated at 2022-06-14 16:35:14.878710
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE()
    assert instance.__doc__.split('\n')[0].count('ITVBTCCIE') == 1
    assert instance._VALID_URL == 'https?://(?:www\\.)?itv\\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:35:23.169351
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()
    assert ITVBTCCIE._VALID_URL.match('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert ITVBTCCIE._VALID_URL.match('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch-1')
    assert ITVBTCCIE._VALID_URL.match('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch-2')

# Generated at 2022-06-14 16:35:26.363882
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ITVIE(url, 'Liar - Series 2 - Episode 6')

# Generated at 2022-06-14 16:35:27.657846
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:35:34.613898
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    IE = ITVBTCCIE()
    assert IE.get_url_re().match('https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert IE.get_url_re().match('https://www.itv.com/btcc/brands-hatch/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not IE.get_url_re().match('https://www.itv.com/btcc/')

# Generated at 2022-06-14 16:35:39.635770
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    data = ITVIE()._real_extract(url)
    assert data['id'] == '2a4547a0012'
    assert data['title'] == 'Liar - Series 2 - Episode 6'
    assert data['description'] == 'md5:d0f91536569dec79ea184f0a44cca089'
    assert data['series'] == 'Liar'
    assert data['season_number'] == 2
    assert data['episode_number'] == 6


# Generated at 2022-06-14 16:35:45.688241
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    r = ITVBTCCIE()._real_extract('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert r['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert r['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert r['entries'][0]['id'] == '5867938053001'


# Generated at 2022-06-14 16:36:22.909691
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from class_name import ClassName
    from extractor_class_template import ExtractorClassTemplate
    from unittest import mock

    et_mock = mock.MagicMock()
    et_mock.return_value = et_mock
    et_mock.suitable.return_value = False
    et_mock.IE_NAME = None
    et_mock.webpage.return_value = 'webpage'
    et_mock.js_to_json.return_value = 'js_to_json'
    et_mock.url_result.return_value = 'url_result'
    url = 'url'

    ie = ClassName(et_mock)
    ie._real_extract(url)
    et_mock.assert_called_once_with()

# Generated at 2022-06-14 16:36:28.352096
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE('https://www.itv.com/hub/liar/2a4547a0012')
    assert isinstance(ie, ITVIE)
    assert ie.url == 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ie.video_id == '2a4547a0012'


# Generated at 2022-06-14 16:36:28.998612
# Unit test for constructor of class ITVIE
def test_ITVIE():
    InfoExtractor(ITVIE())


# Generated at 2022-06-14 16:36:30.215849
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # without the explicit __init__ call, ITVIE.__init__ would not be called
    ITVIE(ITVIE._downloader)._real_initialize()

# Generated at 2022-06-14 16:36:32.290520
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'ITV'

# Generated at 2022-06-14 16:36:35.548488
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ITVIE._TESTS[0]['id'] == '2a4547a0012'

# Generated at 2022-06-14 16:36:41.363525
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ie._REAL_EXTENSION == '.com'

# Generated at 2022-06-14 16:36:42.124609
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE("")
    assert info_extractor._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:36:45.602226
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE("https://www.itv.com/hub/liar/2a4547a0012")
    assert ie.getId() == "2a4547a0012"


# Generated at 2022-06-14 16:36:46.852947
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Initialize
    ITVIE()


# Generated at 2022-06-14 16:37:18.444322
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itv_btcc_ie = ITVBTCCIE()
    assert itv_btcc_ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:27.148689
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    video_id = '5717285424001'
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    playlist_id = 'btcc-2018-all-the-action-from-brands-hatch'
    obj = ITVBTCCIE(None)

# Generated at 2022-06-14 16:37:28.996762
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    ITVBTCCIE(url)

# Generated at 2022-06-14 16:37:29.868618
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:37:31.694934
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvBTCCIE = ITVBTCCIE(ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE)
    assert (itvBTCCIE is not None)

# Generated at 2022-06-14 16:37:35.012480
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert (ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch').BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')

# Generated at 2022-06-14 16:37:35.622644
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:37:43.419664
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    really_long_string = ('0123456789' * 100)[:-9]
    assert ITVBTCCIE._valid_url(
        'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',
        ITVBTCCIE)
    assert ITVBTCCIE._valid_url(
        'http://www.itv.com/btcc/{0}'.format(really_long_string),
        ITVBTCCIE)



# Generated at 2022-06-14 16:37:44.335381
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_obj = ITVBTCCIE()
    assert test_obj._TEST['url'] == test_obj._VALID_URL

# Generated at 2022-06-14 16:37:46.681998
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # This test is for the constructor of ITVBTCCIE class.
    # The verify_ssl=False is for the requests.get to download pages.
    # It does not affect HTTPS URL extraction.
    instance = ITVBTCCIE(ITVIE().suitable, verify_ssl=False)
    assert instance is not None

# Generated at 2022-06-14 16:38:49.247284
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('http://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:38:52.026683
# Unit test for constructor of class ITVIE
def test_ITVIE():
    i = ITVIE()
    assert i._VALID_URL == ITVIE._VALID_URL
    assert i._GEO_COUNTRIES == ITVIE._GEO_COUNTRIES

# Generated at 2022-06-14 16:39:00.740969
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    web_page_contents = "whatever"
    title_format = "Liar - Series 2 - Episode 6"
    description_format = "md5:d0f91536569dec79ea184f0a44cca089"
    assert ITVIE()._real_extract(url)["title"] == title_format
    assert ITVIE()._real_extract(url)["description"] == description_format
    assert ITVIE()._real_extract(url)["series"] == "Liar"
    assert ITVIE()._real_extract(url)["season_number"] == 2
    assert ITVIE()._real_extract(url)["episode_number"] == 6


# Generated at 2022-06-14 16:39:05.208058
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._GEO_COUNTRIES == ['GB']


# Generated at 2022-06-14 16:39:08.625457
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'


# Generated at 2022-06-14 16:39:09.220624
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:39:11.479488
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")

# Generated at 2022-06-14 16:39:22.992360
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    class _UnitTestITVBTCCIE(ITVBTCCIE):
        def __init__(self):
            super(_UnitTestITVBTCCIE, self).__init__()

    xtest = _UnitTestITVBTCCIE()
    assert xtest.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:34.476570
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    itv = ITVIE(InfoExtractor())

    # Check the video id of the ITVIE
    assert itv._match_id(url) == '2a4547a0012'

    # Check the match of the regex of ITV_url
    assert ITVIE._VALID_URL == 'https?://(?:www\\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

    # Check the match of the regex of ITV_url

# Generated at 2022-06-14 16:39:35.802351
# Unit test for constructor of class ITVBTCCIE

# Generated at 2022-06-14 16:41:13.786384
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """Unit test for constructor of class ITVIE"""
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    instance = ITVIE(url)
    assert instance._test_urls(url, [url]) == url
    assert instance.valid_url(url) == url
    assert instance.valid_url('https://www.itv.com/hub/the-voice-uk/the-voice-uk-series-7/videos/the-voice-uk-series-7-trailer') == None
    assert instance.valid_url('https://www.any.com/hub/the-voice-uk/the-voice-uk-series-7/videos/the-voice-uk-series-7-trailer') == None

# Generated at 2022-06-14 16:41:22.185736
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"

    inst = ITVBTCCIE()
    playlist = inst._real_extract(url)
    assert len(playlist.keys()) == 3
    assert 'entries' in playlist
    assert 'id' in playlist
    assert 'title' in playlist

    entries = playlist['entries']
    assert len(entries) == 9

    playlist1 = entries[0]
    assert len(playlist1.keys()) == 2
    assert 'ie_key' in playlist1
    assert 'url' in playlist1
    assert playlist1['ie_key'] == 'BrightcoveNew'

# Generated at 2022-06-14 16:41:27.866392
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/gallery/btcc-2018-a-season-full-of-surprises'
    video = ITVBTCCIE()(url)
    video_url = video[0]['url']
    video_id = video[0]['id']
    assert video_url.startswith('http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=')
    assert video_id.startswith('http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=')

# Generated at 2022-06-14 16:41:30.698603
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE('https://www.itv.com/hub/liar/2a4547a0012')
    assert ie.site == 'ITV'


# Generated at 2022-06-14 16:41:37.035825
# Unit test for constructor of class ITVIE
def test_ITVIE():
    infoextractor = ITVIE("https://www.itv.com/hub/liar/2a4547a0012")
    assert infoextractor._match_id("https://www.itv.com/hub/liar/2a4547a0012") == "2a4547a0012"
    assert infoextractor._match_id("https://www.itv.com/hub/liar/2a4547a0012") == "2a4547a0012"

# Generated at 2022-06-14 16:41:44.018887
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ie = ITVBTCCIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:41:46.266960
# Unit test for constructor of class ITVIE
def test_ITVIE():
    extractor = ITVIE()

# Generated at 2022-06-14 16:41:47.223810
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVExtractor = ITVBTCCIE()

# Generated at 2022-06-14 16:41:50.344760
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    video_id = '5788641316001'
    url = ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % video_id
    _ = ITVBTCCIE()(url)

# Generated at 2022-06-14 16:42:01.371769
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE('https://www.itv.com/hub/liar/2a4547a0012')._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ITVIE('https://www.itv.com/hub/liar/2a4547a0012')._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:44:16.390841
# Unit test for constructor of class ITVIE
def test_ITVIE():
    instance = ITVIE()
    assert instance


# Generated at 2022-06-14 16:44:18.301966
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()
    # just a simple example to test if class ITVIE can be initialised
    assert itv_ie != ''


# Generated at 2022-06-14 16:44:22.372399
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from .itv import ITVIE
    ITVIE('http://www.itv.com/hub/liar/2a4547a0012')
    ITVIE('http://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024')
    ITVIE('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034')

# Generated at 2022-06-14 16:44:22.845202
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE(None)

# Generated at 2022-06-14 16:44:25.892882
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_url = 'https://www.itv.com/hub/liar/2a4547a0012'
    # Constructor of ITVIE class
    instance = ITVIE()
    # The _match_id method should return a string which is not empty
    assert instance._match_id(test_url)

