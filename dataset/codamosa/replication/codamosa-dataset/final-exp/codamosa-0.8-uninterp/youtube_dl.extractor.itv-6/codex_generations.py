

# Generated at 2022-06-14 16:34:44.378165
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE(None).BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'


# Generated at 2022-06-14 16:34:56.038246
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_url = "https://www.itv.com/hub/liar/2a4547a0012"
    itv_url2 = "https://www.itv.com/hub/liar/2a4547a0013"
    itv_url3 = "https://www.itv.com/hub/through-the-keyhole/2a2271a0033"
    itv_url4 = "https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034"
    itv_url5 = "https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024"

    # Testing 1 constructor of ITVIE, using valid URLs
    ITVIE(itv_url)
    ITVIE

# Generated at 2022-06-14 16:35:08.585938
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE({}).BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ITVBTCCIE({})._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:35:09.651134
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()

# Generated at 2022-06-14 16:35:16.076925
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._valid_url(url)
    assert ITVBTCCIE._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'


# Generated at 2022-06-14 16:35:22.321609
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE()
    assert itv.IE_NAME == 'itv'
    assert 'itv.com' in itv._VALID_URL
    assert '^' not in itv._VALID_URL
    assert '$' not in itv._VALID_URL
    assert 'g.co' not in itv._VALID_URL
    assert 'itv.com' in itv.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:35:25.500052
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:35:29.688318
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """Tests for ITVBTCCIE class constructor."""
    ITVBTCCIE(None)._test_valid_url('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:35:37.790791
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    result = ITVBTCCIE("https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert result.BRIGHTCOVE_URL_TEMPLATE ==  'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert result._TEST == {'url': 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch', 'info_dict': {'id': 'btcc-2018-all-the-action-from-brands-hatch', 'title': 'BTCC 2018: All the action from Brands Hatch'}, 'playlist_mincount': 9}

# Generated at 2022-06-14 16:35:40.553842
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # TODO: write it
    # Below is the excerpt of the code in question (line numbers added):
    #    # Unit test for constructor of class ITVBTCCIE
    #    def test_ITVBTCCIE():
    #        # TODO: write it
    #    test_ITVBTCCIE()
    assert True

# Generated at 2022-06-14 16:36:05.638864
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    result = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:36:06.638236
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .itvbtccie import ITVBTCCIE
    ITVBTCCIE()

# Generated at 2022-06-14 16:36:08.381574
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()
    assert itvbtccie.__class__ == ITVBTCCIE


# Generated at 2022-06-14 16:36:15.366015
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .brightcove import BrightcoveNewIE
    url = ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE % '5788706594001'
    assert ITVBTCCIE.suitable(url)
    assert BrightcoveNewIE.suitable(url)
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE is not None
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE is not ''

# Generated at 2022-06-14 16:36:17.079367
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Tests that the constructor doesn't raise an error
    ITVBTCCIE()

# Generated at 2022-06-14 16:36:28.528615
# Unit test for constructor of class ITVIE

# Generated at 2022-06-14 16:36:36.789704
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    def assertResult(url, playlist_id, title):
        assert ITVBTCCIE('')._real_extract(url) == {
            '_type': 'playlist',
            'id': playlist_id,
            'entries': [
                {
                    '_type': 'url',
                    'url': 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s' % video_id,
                    'ie_key': 'BrightcoveNew',
                    'ie_key': 'BrightcoveNew'
                }
                for video_id in re.findall(r'data-video-id=["\'](\d+)', webpage)
            ],
            'title': title
        }

    webpage = ''

# Generated at 2022-06-14 16:36:37.362880
# Unit test for constructor of class ITVIE
def test_ITVIE():
    pass

# Generated at 2022-06-14 16:36:40.675212
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    temp = ITVBTCCIE()
    assert temp.BRIGHTCOVE_URL_TEMPLATE != None

# Generated at 2022-06-14 16:36:44.070877
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE(None)

    # Failure if constructor doesn't create proper instance
    if not isinstance(ie,(ITVBTCCIE)):
        print("Failure of constructor of ITVBTCCIE")

# Generated at 2022-06-14 16:37:21.560607
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE('https://www.itv.com/hub/liar/2a4547a0012').video_id == '2a4547a0012'
    assert ITVIE('https://www.itv.com/hub/through-the-keyhole/2a2271a0033').video_id == '2a2271a0033'
    assert ITVIE('https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034').video_id == '2a5159a0034'
    assert ITVIE('https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024').video_id == '2a2898a0024'

# Generated at 2022-06-14 16:37:23.179384
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE('', {'url': ''})
    assert isinstance(itv_ie, ITVIE)

# Generated at 2022-06-14 16:37:25.414518
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE(InfoExtractor())._VALID_URL(ITVBTCCIE(InfoExtractor())._TEST['url'])


# Generated at 2022-06-14 16:37:26.843331
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE("https://www.itv.com/hub/liar/2a4547a0012")

# Generated at 2022-06-14 16:37:28.538140
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE()
    assert(instance._VALID_URL, ITVBTCCIE._VALID_URL)
    assert(instance._TEST, ITVBTCCIE._TEST)

# Generated at 2022-06-14 16:37:29.946780
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()._extract_info('2a4547a0012')

# Generated at 2022-06-14 16:37:30.445461
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:37:31.181584
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE()

# Generated at 2022-06-14 16:37:37.272797
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvIE = ITVIE(123)
    assert itvIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert itvIE._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert itvIE._GEO_COUNTRIES == ['GB']
    assert itvIE._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'

# Generated at 2022-06-14 16:37:44.007388
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()
    expected_output = '{}/hub/liar/2a4547a0012'
    itv_url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert itv_ie._VALID_URL == expected_output, 'Unexpected output'
    assert itv_ie._valid_url(itv_url, itv_ie._VALID_URL), 'Unexpected output'

# Generated at 2022-06-14 16:38:49.198934
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    import ITVBTCCIE
    ITVBTCCIE.ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:38:50.714836
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Just check whether the class constructor does not raise any exceptions.
    ITVBTCCIE()

# Generated at 2022-06-14 16:38:59.903761
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert(ITVIE.suitable('https://www.itv.com/hub/liar/2a4547a0012'))
    assert not (ITVIE.suitable('http://www.google.com/'))
    assert not (ITVIE.suitable(
        'https://www.itv.com/hub/through-the-keyhole/2a2271a0033'))
    assert not (ITVIE.suitable(
        'https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034'))
    assert not (ITVIE.suitable(
        'https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024'))



# Generated at 2022-06-14 16:39:02.229799
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')


# Generated at 2022-06-14 16:39:03.799092
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert isinstance(ie, ITVIE)

# Generated at 2022-06-14 16:39:07.377167
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    result = ITVBTCCIE()
    assert result._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:39:11.469498
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE()._BUILD_TEMPLATE_URL('http://www.itv.com/hub/david-attenboroughs-great-barrier-reef/2a8567a0002', {}) == 'http://www.itv.com/hub/david-attenboroughs-great-barrier-reef/2a8567a0002'
    assert ITVIE()._BUILD_TEMPLATE_URL('https://www.itv.com/hub/david-attenboroughs-great-barrier-reef/2a8567a0002', {}) == 'https://www.itv.com/hub/david-attenboroughs-great-barrier-reef/2a8567a0002'

# Generated at 2022-06-14 16:39:12.345806
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_ITVBTCCIE = ITVBTCCIE()

# Generated at 2022-06-14 16:39:23.870161
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = ITVBTCCIE._test_video_url(
        'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert 'players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5768563492001' in url
    assert '&referrer=http%3A//www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch' in url
    assert '&geo_ip_blocks=193.113.0.0%2F16%2C54.36.162.0%2F23%2C159.65.16.0%2F21' in url

# Generated at 2022-06-14 16:39:28.387897
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_unit = ITVIE()
    assert test_unit.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:41:59.358552
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test case for ITVIE
    ITVIE().extract(ITVIE().try_url(ITVIE()._TESTS[0]['url']))
    ITVIE().extract(ITVIE().try_url(ITVIE()._TESTS[1]['url']))
    ITVIE().extract(ITVIE().try_url(ITVIE()._TESTS[2]['url']))
    ITVIE().extract(ITVIE().try_url(ITVIE()._TESTS[3]['url']))

# Generated at 2022-06-14 16:42:03.578296
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_result = ITVIE('https://www.itv.com/hub/liar/2a4547a0012')
    assert test_result.video_id == '2a4547a0012'
    assert test_result.url == 'https://www.itv.com/hub/liar/2a4547a0012'

# Generated at 2022-06-14 16:42:05.268927
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Run test for ITVIE
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:42:08.985255
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)
    assert hasattr(ie, '_real_extract')
    assert callable(ie._real_extract)
    return


# Generated at 2022-06-14 16:42:12.239658
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    IE = ITVBTCCIE(None) # None = downloader
    IE._real_extract('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    return True

# Generated at 2022-06-14 16:42:16.224804
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    assert info_extractor._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert info_extractor._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:42:17.439972
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie_ITV = ITVIE()
    assert ie_ITV
    

# Generated at 2022-06-14 16:42:20.191091
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:42:21.808307
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    func = ITVBTCCIE

    # The following test should not raise an error
    func()



# Generated at 2022-06-14 16:42:22.333332
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITV = ITVIE()