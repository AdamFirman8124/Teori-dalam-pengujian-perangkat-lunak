

# Generated at 2022-06-14 16:34:45.232989
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itv_btcc_cie_obj = ITVBTCCIE()
    assert type(itv_btcc_cie_obj) == ITVBTCCIE

# Generated at 2022-06-14 16:34:48.127779
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('http://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:34:57.817653
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    playist_id = 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:35:10.237594
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Arrange
    expected_url = "https://www.itv.com/hub/liar/2a4547a0012"
    expected_video_id = "2a4547a0012"
    expected_countries = ["GB"]
    expected_matches = {"countries": expected_countries, "id": expected_video_id}

    # Act
    itv_extractor = ITVIE(expected_url)

    # Assert
    assert itv_extractor._URL_REGEX == ITVIE._VALID_URL
    assert itv_extractor._GEO_COUNTRIES == expected_countries
    assert itv_extractor._TESTS == ITVIE._TESTS
    assert itv_extractor._PATTERN == ITVIE._VALID_URL
    assert itv_extractor._

# Generated at 2022-06-14 16:35:10.869515
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:35:16.018515
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    result = ITVBTCCIE()
    assert result.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:35:19.539248
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvie = ITVIE(None)
    assert itvie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'


# Generated at 2022-06-14 16:35:20.751489
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE()

# Generated at 2022-06-14 16:35:29.735461
# Unit test for constructor of class ITVIE
def test_ITVIE():
    "ITVIE class constructor test"
    ITVIE_object = ITVIE()
    string1 = "http://www.itv.com/hub/jeremy-kyle/2a5195a0068"
    string2 = "https://www.itv.com/hub/jeremy-kyle/2a5195a0068"
    actual_result = ITVIE_object._is_js_url(string1)
    expected_result = ITVIE_object._is_js_url(string2)
    assert expected_result is True, "Expected True, Actual: %s" % actual_result

# Generated at 2022-06-14 16:35:33.568830
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .brightcove import BrightcoveNewIE
    from .itv import ITVBTCCIE

    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    id_ = 'btcc-2018-all-the-action-from-brands-hatch'
    # make sure ITVBTCCIE's constructor is valid
    ITVBTCCIE(BrightcoveNewIE())._real_initialize(url)
    ITVBTCCIE.suitable(url)
    ITVBTCCIE.IE_NAME = 'itv'

# Generated at 2022-06-14 16:36:08.646024
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._check_valid_url(url)
    assert ITVBTCCIE._check_valid_url(url, ie=BrightcoveNewIE())

    url = 'http://www.itv.com/btcc/races/not-valid'
    assert not ITVBTCCIE._check_valid_url(url)


# Generated at 2022-06-14 16:36:11.027627
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE(None)._real_extract(url="https://www.itv.com/hub/liar/2a4547a0012")

# Generated at 2022-06-14 16:36:22.446677
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    inst = ITVBTCCIE(ITVIE())
    match = inst._match_id(url)
    result = inst._real_extract(url)
    assert result['_type'] == 'playlist'
    result = result['entries']
    assert len(result) == 9
    assert result[0]['id'] == '5797427658001'
    assert result[0]['url'] == 're:http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html\?videoId=5797427658001'

# Generated at 2022-06-14 16:36:27.260209
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    #Test case 1
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    playlist_id = 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._valid_url(url) == True
    assert ITVBTCCIE._match_id(url) == playlist_id

# Generated at 2022-06-14 16:36:31.858126
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itv_btcc_ie = ITVBTCCIE()
    assert itv_btcc_ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:36:34.043373
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    d = ITVBTCCIE()
    assert d._VALID_URL == ITVBTCCIE._VALID_URL
    assert d._TEST == ITVBTCCIE._TEST

# Generated at 2022-06-14 16:36:39.201183
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    assert info_extractor._VALID_URL == ITVIE._VALID_URL
    assert info_extractor.IE_NAME == 'ITV'
    assert info_extractor.GEO_COUNTRIES == ITVIE._GEO_COUNTRIES
    # Test cases
    assert info_extractor._TESTS == ITVIE._TESTS

# Generated at 2022-06-14 16:36:41.521634
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie


# Generated at 2022-06-14 16:36:51.808525
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from unittest.mock import patch

    itvIE = ITVIE()

    assert itvIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert itvIE._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:36:53.305722
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:37:46.168932
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    obj = ITVBTCCIE("")
    assert obj.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s"


# Generated at 2022-06-14 16:37:48.878736
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:37:49.830485
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITBTCCIE = ITVBTCCIE()

# Generated at 2022-06-14 16:37:52.153579
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # make sure constructor does not raise exceptions
    ITVBTCCIE()

# Generated at 2022-06-14 16:37:55.575468
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    iet = ITVIE()
    assert iet.suitable(url)

# Generated at 2022-06-14 16:38:04.417716
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .brightcove import BrightcoveLegacyIE

    itvbtccie = ITVBTCCIE()

    # test for format extraction
    formats = [{
        'url': 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5925125630001',
        'ext': 'mp4',
        'width': 1280,
        'height': 720,
        'format_id': '5925125630001',
    }]
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:38:11.597533
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Ensure that the ITVIE constructor is able to handle a url to a
    # tv episode that is not available
    webpage = 'http://www.itv.com/hub/last-of-the-summer-wine/2a2898a0024'
    ITVEpi = ITVIE(webpage)
    
    # Check that parsing the webpage returns an error
    assert ITVEpi.parseWebpage() == False

# Generated at 2022-06-14 16:38:16.647328
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test for invalid constructor arguments
    with pytest.raises(TypeError):
        ITVIE(None)
    with pytest.raises(TypeError):
        ITVIE(None, None)
    with pytest.raises(TypeError):
        ITVIE(None, None, None)
    with pytest.raises(TypeError):
        ITVIE(None, None, None, None)
    with pytest.raises(TypeError):
        ITVIE(None, None, None, None, None)

    # Test for valid constructor arguments
    assert ITVIE('http://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:38:20.687975
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ie = ITVIE()
    ie._search_regex(ie._VALID_URL, test_url, 'videoId', default=None)

# Generated at 2022-06-14 16:38:21.269782
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    pass

# Generated at 2022-06-14 16:39:18.247614
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.name == 'itv.com'
    assert ie.ie_key() == 'itv'
    assert ie.ie_key() == ITVIE.ie_key()

# Generated at 2022-06-14 16:39:22.193113
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    inst = ITVBTCCIE()
    assert inst.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:28.823147
# Unit test for constructor of class ITVBTCCIE

# Generated at 2022-06-14 16:39:32.686703
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:41.532829
# Unit test for constructor of class ITVIE
def test_ITVIE():
    r = ITVIE(InfoExtractor())._real_extract('https://www.itv.com/hub/liar/2a4547a0012')
    assert r['id'] == '2a4547a0012'
    assert r['title'] == 'Liar - Series 2 - Episode 6'
    assert r['description'] == 'md5:d0f91536569dec79ea184f0a44cca089'
    assert r['series'] == 'Liar'
    assert r['season_number'] == 2
    assert r['episode_number'] == 6
    assert len(r['formats']) >= 2

# Generated at 2022-06-14 16:39:44.822547
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    i = ITVBTCCIE(None)
    assert i.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:48.101079
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:49.333788
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # just in case
    ITVIE(None)

# Generated at 2022-06-14 16:39:50.651505
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE()._VALID_URL == ITVIE._VALID_URL

# Generated at 2022-06-14 16:39:53.414767
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    class_name = info_extractor.__class__.__name__
    assert 'ITVIE' in class_name


# Generated at 2022-06-14 16:42:23.009708
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._downloader is not None
    assert ie.server_url == ie._VALID_URL
    assert ie._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:42:24.519410
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Arrange
    from youtube_dl.extractor.itv import ITVIE
    
    # Act
    ITVIE()
 

# Generated at 2022-06-14 16:42:26.283008
# Unit test for constructor of class ITVIE
def test_ITVIE():
    inst = ITVIE()
    assert isinstance(inst, ITVIE)
    assert isinstance(inst, InfoExtractor)

# Generated at 2022-06-14 16:42:33.531754
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Some ITV programming is made available after it has been broadcast and
    # is accessed via the ITV Hub
    url = "https://www.itv.com/hub/liar/2a4547a0012"

    # Initialise the ITVIE extractor class
    itvie = ITVIE()

    # Test whether the URL is recognised by the extractor
    assert itvie.suitable(url)

    # Test whether the URL returns the correct video ID
    video_id = itvie._match_id(url)
    assert video_id == "2a4547a0012"

# Generated at 2022-06-14 16:42:35.912329
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie_test = ITVIE()
    assert ie_test.get_info_extractor() == "ITVIE"


# Generated at 2022-06-14 16:42:39.422797
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itv_btcc_ie = ITVBTCCIE.ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert itv_btcc_ie is not None


# Generated at 2022-06-14 16:42:46.484358
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itv_btcc = ITVBTCCIE()
    itv_btcc._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    itv_btcc._match_id('http://www.itv.com/btcc/interviews/btcc-2018-interview-dave-newsham')
    itv_btcc._match_id('http://www.itv.com/btcc/races/btcc-2018-brands-hatch-race-three')
    itv_btcc._match_id('http://www.itv.com/btcc/races/btcc-2018-brands-hatch-race-one')

# Generated at 2022-06-14 16:42:47.029667
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:42:58.039373
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # example url and attributes
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    video_id = '2a4547a0012'

# Generated at 2022-06-14 16:42:58.594692
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()