

# Generated at 2022-06-14 17:27:20.760525
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    test_string = 'http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true'
    tvplayie = TVPlayIE()
    tvplayie._match_id(test_string)

# Generated at 2022-06-14 17:27:21.721397
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('mtg:418113')

# Generated at 2022-06-14 17:27:24.285251
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)


# Generated at 2022-06-14 17:27:28.632193
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplayie = TVPlayIE()
    assert tvplayie.ie_key() == 'TVPlay'
    assert tvplayie.ie_name() == 'MTG'
    assert tvplayie.ie_desc() == 'MTG services'
    assert tvplayie.supported_ie() == ['MTG']


# Generated at 2022-06-14 17:27:35.135865
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    a = TVPlayIE()
    assert a != None
    assert a._VALID_URL == r'(?x)mtg:(?P<id>\d+)'
    assert a.IE_NAME == 'mtg'
    assert a.IE_DESC == 'MTG services'
    assert a._TESTS == [{
        'url': 'mtg:418113',
        'only_matching': True}]


# Generated at 2022-06-14 17:27:46.581014
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie._VALID_URL is ViafreeIE._VALID_URL
    assert ie._TESTS is ViafreeIE._TESTS
    assert ie._GEO_BYPASS is ViafreeIE._GEO_BYPASS
    assert ie.SUITABLE is ViafreeIE.SUITABLE
    assert ie.IE_NAME is ViafreeIE.IE_NAME
    assert ie.geo_countries is ViafreeIE.geo_countries
    assert ie.geo_verification_headers is ViafreeIE.geo_verification_headers
    assert ie.GEO_COUNTRIES is ViafreeIE.GEO_COUNTRIES
    assert ie.GEO_VERIFICATION_HEADERS is ViafreeIE.GEO_VERIFICATION_HEADERS
    assert ie.extract is Viafree

# Generated at 2022-06-14 17:27:58.606013
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie.IE_NAME # 'mtg'
    ie.IE_DESC # 'MTG services'
    ie._VALID_URL # r'(?x)
                  # (?:mtg:|
                  # https?://
                  # (?:www\.)?
                  # (?:tvplay(?:\.skaties)?\.lv(?:/parraides)?|
                  # (?:tv3play|play\.tv3)\.lt(?:/programos)?|
                  # tv3play(?:\.tv3)?\.ee/sisu|
                  # (?:tv(?:3|6|8|10)play|viafree)\.se/program|
                  # (?:(?:tv3play|viasat4play|tv6play|viafree)\.no|
                  # (?:tv3

# Generated at 2022-06-14 17:28:06.472455
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """ Run unit test for constructor of class TVPlayHomeIE """
    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.name == 'TVPlayHome'
    assert ie.IE_NAME == 'TVPlayHome'
    assert ie.IE_DESC == 'TVPlayHome'
    assert ie.info_dict is None
    assert ie.params is None



# Generated at 2022-06-14 17:28:17.780448
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    tv3play_lt = 'http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    tv3play_lt_geo = ie.extract(tv3play_lt)
    assert tv3play_lt_geo['id'] == '409229'
    play_tv3_lt_1 = 'https://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    play_tv3_lt_2 = 'https://play.tv3.lt/moterys-meluoja-geriau/409229/?autostart=true'

# Generated at 2022-06-14 17:28:24.643823
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    VIAFREEIE = ViafreeIE()
    assert VIAFREEIE._VALID_URL == r'https?://(?:www\.)?viafree\.(dk|no|se)/(program(?:mer)?/(?:[^/]+/)+[^/?#&]+)'
    assert VIAFREEIE.IE_DESC == 'Viafree and TV3 Play'
    assert VIAFREEIE._TESTS == [{
        'url': 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1',
        'only_matching': True,
    }]


# Generated at 2022-06-14 17:29:01.174909
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """ TestCase for TVPlayIE """
    e = TVPlayIE()



# Generated at 2022-06-14 17:29:10.419843
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    def test(video_url, expected_result):
        assert TVPlayHomeIE.suitable(video_url) == expected_result
        assert (TVPlayHomeIE.ie_key() == 'TVPlayHome') == expected_result

    test(None, False)
    test('', False)
    test('URL_WITHOUT_DOMAIN', False)
    test('tv3play.skaties.lv', False)
    test('https://tv3play.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/', True)
    test('https://tv3play.skaties.lv/vinas-melo-labak-10280317', True)

# Generated at 2022-06-14 17:29:13.408369
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ex = TVPlayHomeIE()
    assert ex.IE_NAME == 'TVPlayHome.lv'
    assert ex.IE_DESC == 'TVPlayHome.lv'


# Generated at 2022-06-14 17:29:22.372438
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert not ViafreeIE.suitable('https://tvplay.skaties.lv/parraides/tv3-zinas/760183')
    # Only works for Denmark as of now
    assert ViafreeIE.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert not TVPlayIE.suitable('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true')
    assert ViafreeIE.suitable('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2')

# Generated at 2022-06-14 17:29:23.574077
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()


# Generated at 2022-06-14 17:29:24.269408
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:29:29.145704
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie.suitable('http://play.mtgx.tv/program/husraddarna/sesong-2/avsnitt-1-1400597156') == False
    assert ie.suitable('http://viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2') == True
    assert ie.suitable('mtg:418113') == False


# Generated at 2022-06-14 17:29:35.236580
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-10047125')
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie._NETRC_MACHINE == 'tv3'
    assert ie._GEO_COUNTRIES == ['LT', 'LV', 'EE']
    assert ie._GEO_BYPASS == False



# Generated at 2022-06-14 17:29:47.034093
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie._VALID_URL.match('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') is not None
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie._VALID_URL.match('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/') is not None

# Generated at 2022-06-14 17:29:48.876800
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from . import TVPlayHomeIE

    # Test if class can be instantiated
    with pytest.raises(TypeError):
        TVPlayHomeIE()


# Generated at 2022-06-14 17:31:10.879789
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'), 'Unsuitable'
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125'), 'Unsuitable'
    assert TVPlayHomeIE.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317'), 'Unsuitable'
    assert TVPlayHomeIE.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354'), 'Unsuitable'

# Generated at 2022-06-14 17:31:24.651840
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'https://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2'
    assert ViafreeIE.suitable(url) == True
    test = ViafreeIE()
    test.geo_verification_headers = lambda: {}
    test.geo_bypass = lambda x: False
    test.link = lambda x: x
    test.set_cookie = lambda x, y: None
    test.cookies = lambda x: False
    test.cache = lambda x: None
    test.update_url_query = lambda x, y: x
    test.int_or_none = lambda x: x
    test.try_get = lambda x, y: x
    test.match_id = lambda x: x

# Generated at 2022-06-14 17:31:26.517724
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE(None)._real_initialize()



# Generated at 2022-06-14 17:31:32.310080
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    global request
    request = compat_urllib_request.Request(
        'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869?autostart=true'
    )
    test_ViafreeIE.ie = ViafreeIE()
    test_ViafreeIE.ie._real_extract(request)

# Generated at 2022-06-14 17:31:37.072681
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    _TVPlayHomeIE = TVPlayHomeIE()
    assert _TVPlayHomeIE.IE_NAME == 'tvplay'
    assert _TVPlayHomeIE._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'



# Generated at 2022-06-14 17:31:43.323853
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    quality = qualities(['hls', 'medium', 'high'])
    form_id = 'http://tvplay.tv3.lt/sb/public/asset/912006'
    asset = '{ "assetId": "912006", "movie": {"contentUrl": "http://playertest.longtailvideo.com/adaptive/oceans_aes/oceans_aes.m3u8", "encryption": "none", "movieFormat": "hls", "streamFormat": "hls" }, "title": {"titleBrief": "Okeanai"} }'

    extractor = TVPlayHomeIE(create_mock_extractor(asset, form_id, 'm3u8_native'))

    result = extractor.get_video()

# Generated at 2022-06-14 17:31:44.159077
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert(ie != None)

# Generated at 2022-06-14 17:31:50.923280
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    ie.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    # Since this test method is called before GeoRestrictedTestCase, the dict '_GEO_COUNTRIES' is empty
    ie.suitable('http://playapi.mtgx.tv/v3/videos/395328')
    test_class_GeoRestrictedTestCase()
    ie.suitable('http://playapi.mtgx.tv/v3/videos/395328') # Since '_GEO_COUNTRIES' is populated, TVPlayIE is suitable

# Generated at 2022-06-14 17:31:56.973168
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE(None)
    assert viafree._VALID_URL == ViafreeIE._VALID_URL
    assert viafree._TESTS == ViafreeIE._TESTS
    assert viafree._GEO_BYPASS == ViafreeIE._GEO_BYPASS

# Generated at 2022-06-14 17:31:59.769719
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    success = False
    # Constructor should not throw an exception
    try:
        ViafreeIE()
        success = True
    except:
        pass
    assert success

# Generated at 2022-06-14 17:33:31.276073
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie.geo_verification_headers() == {'x-country': 'SE'}
    ie = ViafreeIE(geo_verification_headers=None)
    assert ie.geo_verification_headers() == None
    ie = ViafreeIE(geo_verification_headers={'x-country': 'NO'})
    assert ie.geo_verification_headers() == {'x-country': 'NO'}


# Generated at 2022-06-14 17:33:33.321926
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie._TESTS[0]['info_dict']


# Generated at 2022-06-14 17:33:42.310134
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:33:51.366319
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    print("Temporary directory = %s" % temp_dir)

    # Create a temporary file
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, dir=temp_dir)
    print("f.name = %s" % f.name)

    _VALID_URL = r'''(?x)
                    https?://
                        (?:www\.)?
                        viafree\.(?P<country>dk|no|se)
                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
                    '''
    # Write data to the temporary file
    json.dump(mb, f)

    f.close()
    # Open the temporary file

# Generated at 2022-06-14 17:34:00.436808
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    a = TVPlayIE();
    assert a.IE_NAME == 'mtg';
    assert a.IE_DESC == 'MTG services';

# Generated at 2022-06-14 17:34:03.855305
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    for url in ['https://tv3play.skaties.lv/vinas-melo-labak-10280317',
                'https://tvplay.tv3.ee/cool-d-ga-mehhikosse-10044354',
                'https://tvplay.tv3.lt/aferistai-10047125']:
        assert isinstance(TVPlayHomeIE._iframe_ref(None, url), TVPlayHomeIE)


# Generated at 2022-06-14 17:34:14.816754
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Test empty URL
    with pytest.raises(ValueError):
        TVPlayHomeIE()
    # Test invalid URL
    with pytest.raises(ExtractorError):
        TVPlayHomeIE("http://www.youtube.com/watch?v=BaW_jenozKc")
    # Test valid URL

# Generated at 2022-06-14 17:34:22.858259
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    def media_info(filename):
        with open(filename) as f:
            return f.read()
    url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    ie = TVPlayIE()
    media = ie._real_extract(url)
    media_info_file = media_info('media_info_418113')
    media_info_tuple = media_info('media_info_418113_tuple')
    assert media['id'] == '418113'
    assert media['ext'] == 'mp4'
    assert media['title'] == media_info_tuple[0]
    assert media['description'] == media_info_tuple[1]
    assert media['series'] == media_info_tuple[2]

# Generated at 2022-06-14 17:34:24.945171
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        TVPlayIE('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true')
        return False
    except ExtractorError:
        return True



# Generated at 2022-06-14 17:34:27.815556
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    inst = ViafreeIE('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert 'ViafreeIE' == inst.ie_key()



# Generated at 2022-06-14 17:36:22.264411
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    class TestTVPlayHomeIE(TVPlayHomeIE):
        pass
    inst = TestTVPlayHomeIE({})
    assert inst.IE_NAME == 'TVPlayHome'

# Generated at 2022-06-14 17:36:28.051670
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    url = TVPlayHomeIE._VALID_URL

    class IE(TVPlayHomeIE):
        def _real_extract(self, url):
            pass

    ie = IE(url)
    ie.suitable(url)
    assert ie.IE_NAME == ie.suitable.__name__ == 'TVPlayHomeIE'

# Generated at 2022-06-14 17:36:36.814214
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:36:38.585355
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE()


# Generated at 2022-06-14 17:36:48.066397
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE(None)
    assert ie._VALID_URL == r'(?x)(?:mtg:|https?://(?:www\.)?(?:tvplay(?:\.skaties)?\.lv(?:/parraides)?|(?:tv3play|play\.tv3)\.lt(?:/programos)?|tv3play(?:\.tv3)?\.ee/sisu|(?:tv(?:3|6|8|10)play|viafree)\.se/program|(?:(?:tv3play|viasat4play|tv6play|viafree)\.no|(?:tv3play|viafree)\.dk)/programmer|play\.nova(?:tv)?\.bg/programi)/(?:[^/]+/)+)'

# Generated at 2022-06-14 17:36:53.834593
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Simple URL without instance
    TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    # Simple URL with instance
    TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/',
                 TVPlayHomeIE('https://tvplay.tv3.lt'))
