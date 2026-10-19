

# Generated at 2022-06-14 17:37:57.543728
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdfbase = ZDFBaseIE()
    assert zdfbase._GEO_COUNTRIES == ['DE']
    assert zdfbase._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

# Generated at 2022-06-14 17:38:05.400886
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio')
    assert ie.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert not ie.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html')


# Generated at 2022-06-14 17:38:10.782435
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._call_api('http://example.com/api/videos/123', '123', 'video') == None
    assert ie._extract_format({}, {}, {}, {'url': 'valid_url'}) == None
    assert ie._extract_subtitles({}) == {}
    assert ie._extract_player('', '123', fatal=False) == {}


# Generated at 2022-06-14 17:38:17.459886
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    original_ZDFChannelIE = ZDFChannelIE
    ZDFChannelIE = type('ZDFChannelIE', (ZDFChannelIE,), {'ie_key': 'zdf_channel'})
    result = ZDFChannelIE({})
    assert result.ie_key() == 'zdf_channel'
    ZDFChannelIE = original_ZDFChannelIE

# Generated at 2022-06-14 17:38:25.910379
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE('https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html')
    assert ie.IE_NAME == 'ZDF'
    assert ie.ie_key() == 'ZDF'
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'
    assert ie._GEO_COUNTRIES == ['DE']

# Generated at 2022-06-14 17:38:33.779076
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.suitable(ZDFChannelIE._VALID_URL)
    assert ie.suitable('https://www.zdf.de/filme/taunuskrimi')
    assert not ie.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html')

# Generated at 2022-06-14 17:38:37.096520
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/filme/taunuskrimi/'
    # ZDFChannelIE should not be suitable(url)
    assert not ZDFChannelIE.suitable(url)



# Generated at 2022-06-14 17:38:44.673147
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Create a object of class ZDFIE
    zdf = ZDFIE()
    # Unit test case to extract video id from URL
    video = 'https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html'
    video_id = zdf._match_id(video)
    assert video_id == '151025_magie_farben2_tex'

# Generated at 2022-06-14 17:38:49.772279
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    dut = ZDFIE("https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html")
    assert dut is not None

# Unit tests for function _extract_regular

# Generated at 2022-06-14 17:38:53.525344
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:39:17.448153
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    return ZDFChannelIE('https://www.zdf.de/filme/taunuskrimi/')

# Generated at 2022-06-14 17:39:19.099548
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    instance = ZDFChannelIE()
    assertZDFChannelInstance(instance)


# Generated at 2022-06-14 17:39:28.312168
# Unit test for constructor of class ZDFIE
def test_ZDFIE():

    # Test normal video
    extractor = ZDFIE()
    extractor._extract_regular('https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html',
        {'content': 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.json',
         'apiToken': 'abc'}, 'wohin-fuehrt-der-protest-in-der-pandemie-100')

    # Test mobile video
    extractor = ZDFIE()
    extractor._extract_mobile('210222_phx_nachgehakt_corona_protest')

# Generated at 2022-06-14 17:39:33.005199
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'

    # Initialize an instance
    inst = ZDFChannelIE(url)

    res = inst.suitable(url)
    assert res

    res = inst._match_id(url)
    assert res == 'planet-e'

# Generated at 2022-06-14 17:39:37.250511
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    from .zdf import ZDFIE
    ie = ZDFIE()
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:39:41.335346
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    t = ZDFBaseIE()
    assert t._GEO_COUNTRIES == ['DE']
    assert t._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

# Generated at 2022-06-14 17:39:43.224291
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_ZDFBaseIE = ZDFBaseIE()

# Generated at 2022-06-14 17:39:52.568084
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    entries = [{'_type': 'url_transparent', 'url': 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'}]

    ie = ZDFChannelIE('https://www.zdf.de/sport/das-aktuelle-sportstudio')
    playlist = ie.extract('https://www.zdf.de/sport/das-aktuelle-sportstudio')
    assert len(playlist['entries']) == 23
    assert playlist['entries'] == entries
    assert playlist['id'] == 'das-aktuelle-sportstudio'

# Generated at 2022-06-14 17:39:54.419933
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()


# Generated at 2022-06-14 17:39:58.181827
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE()._VALID_URL == ZDFBaseIE._VALID_URL # make sure that the class is properly inherited
    assert ZDFIE()._TESTS == ZDFBaseIE._TESTS # make sure that the class is properly inherited



# Generated at 2022-06-14 17:40:52.554417
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    obj = ZDFBaseIE()
    if isinstance(obj, ZDFBaseIE):
        print('test_ZDFBaseIE() passed')
    else:
        print('test_ZDFBaseIE() failed')


# Generated at 2022-06-14 17:40:55.909050
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
	assert ZDFIE.ie_key() == 'ZDF'
	assert ZDFIE.ie_key() != 'zdf'
	assert ZDFIE.ie_key() != 'AVC'


# Generated at 2022-06-14 17:40:58.974072
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE(None)._real_extract("https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html")



# Generated at 2022-06-14 17:41:01.780980
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    info_extractor = ZDFBaseIE()
    assert (info_extractor.ie_key(), info_extractor.IE_NAME) == ('zdf', 'ZDF')


# Generated at 2022-06-14 17:41:02.829752
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:41:08.906882
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfchannel_class = ZDFChannelIE.get_class()
    zdfchannel_instance = zdfchannel_class('https://www.zdf.de/sport/das-aktuelle-sportstudio')

    assert isinstance(zdfchannel_instance, ZDFChannelIE)
    assert isinstance(zdfchannel_instance, InfoExtractor)



# Generated at 2022-06-14 17:41:11.457727
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """
    Test for constructor of class ZDFChannelIE
    """
    assert_equal(str(ZDFChannelIE()), "Class ZDFChannelIE")


# Generated at 2022-06-14 17:41:23.367701
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE.suitable("https://www.zdf.de/dokumentation/planet-e")
    assert ZDFChannelIE.suitable("https://www.zdf.de/filme/taunuskrimi")
    assert not ZDFChannelIE.suitable("https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html")
    assert not ZDFChannelIE.suitable("https://www.zdf.de/sport/das-aktuelle-sportstudio/20.11.19-neuer-das-aktuelle-sportstudio-100.html")

# Generated at 2022-06-14 17:41:25.151950
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    instance = ZDFBaseIE()
    if '_call_api' not in dir(instance):
        raise AssertionError('_call_api not in dir(instance)')
        

# Generated at 2022-06-14 17:41:25.823277
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    pass



# Generated at 2022-06-14 17:42:36.180504
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    constructor_test({
        'url': 'https://www.zdf.de/dokumentation/planet-e',
        'only_matching': True,
        'func_name': 'ZDFChannelIE._real_extract'
    })
    constructor_test({
        'url': 'https://www.zdf.de/filme/taunuskrimi/',
        'only_matching': True,
        'func_name': 'ZDFChannelIE._real_extract'
    })
    constructor_test({
        'url': 'https://www.zdf.de/sport/das-aktuelle-sportstudio',
        'only_matching': True,
        'func_name': 'ZDFChannelIE._real_extract'
    })


# Generated at 2022-06-14 17:42:38.414161
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # no exception should be raised
    ZDFIE('test')


# Generated at 2022-06-14 17:42:40.632570
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    x = ZDFIE()
    assert x.ie_key() == 'ZDF'

# Generated at 2022-06-14 17:42:48.436104
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from  calibre.ebooks.metadata.opf2 import OPFCreator
    import datetime

# Generated at 2022-06-14 17:42:52.999539
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE().ie_key()


# Generated at 2022-06-14 17:42:54.619530
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # First test whether constructor of class ZDFIE is working
    zdf = ZDFIE()
    assert zdf != None
# Test for private function _extract_player

# Generated at 2022-06-14 17:42:59.223436
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """Test ZDFChannelIE constructor."""
    class dummy(ZDFChannelIE):
        def _real_extract(self, url):
            raise NotImplementedError()
    assert (dummy(ZDFChannelIE._VALID_URL, {}).channel_id
            == 'dokumentation/planet-e')


# Generated at 2022-06-14 17:43:02.479694
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE.ie_key() == 'zdf'

# Generated at 2022-06-14 17:43:04.114260
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf = ZDFIE()
    assert zdf == ZDFIE()



# Generated at 2022-06-14 17:43:09.746300
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    url = "https://www.zdf.de/dokumentation/zdf-history/b1364=thc-das-geheimnis-der-heilpflanze-100.html"
    result = ZDFBaseIE._call_api(url, url, "test1", "test", "test")
    assert result == {}

# Generated at 2022-06-14 17:45:19.949267
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    raise NotImplementedError("Unit test not implemented")



# Generated at 2022-06-14 17:45:21.486181
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert issubclass(ZDFBaseIE, InfoExtractor)



# Generated at 2022-06-14 17:45:23.398266
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    x = ZDFBaseIE()
    print(x._GEO_COUNTRIES)
    print(x._QUALITIES)
       


# Generated at 2022-06-14 17:45:30.482961
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    for u in (
            # Expect error when download webpage
            'https://www.zdf.de/sport/das-aktuelle-sportstudio',
            # Expect error when parse JSON
            'https://www.zdf.de/dokumentation/planet-e',
    ):
        try:
            ZDFChannelIE(u)
        except ExtractorError:
            pass


# Generated at 2022-06-14 17:45:40.156806
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Test normal constructor of class ZDFBaseIE
    # ZDFBaseIE does not have a method
    assert ZDFBaseIE()._GEO_COUNTRIES == ['DE']
    # Test constructor with assignment of attribute _GEO_COUNTRIES
    assert ZDFBaseIE('AR')._GEO_COUNTRIES == ['AR']
    # Test constructor with assignment of argument geo_countries
    assert ZDFBaseIE(geo_countries=['AR'])._GEO_COUNTRIES == ['AR']
    # A problem has been found with the test of constructor with both,
    # assignment of attribute _GEO_COUNTRIES, and argument geo_countries
    assert ZDFBaseIE('AR', 'AR')._GEO_COUNTRIES == ['AR','AR']
    # Test constructor with invalid argument _G

# Generated at 2022-06-14 17:45:43.983525
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    """
    Test if YouTubeIE constructor works
    """
    info_extractor = ZDFBaseIE()
    assert (info_extractor is not None)


# Generated at 2022-06-14 17:45:51.772026
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_IE = ZDFChannelIE()
    assert zdf_channel_IE._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)', 'zdf_channel_IE._VALID_URL must be "%s", not "%s"' % (r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)', zdf_channel_IE._VALID_URL)

# Generated at 2022-06-14 17:45:59.354168
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'
    assert ie._TESTS[0]['url'] == 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'

# Generated at 2022-06-14 17:46:09.400852
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # The class ZDFIE works with a ZDFIE object parameter
    zdfie = ZDFIE()
    # _GEO_COUNTRIES of class ZDFIE contains 'DE' 
    assert(zdfie._GEO_COUNTRIES[0] == 'DE')
    # _QUALITIES of class ZDFIE are 'auto', 'low', 'med', 'high', 'veryhigh', and 'hd'
    # The following unit test checks all qualities are part of the qualities
    assert(all(x in ['auto', 'low', 'med', 'high', 'veryhigh', 'hd'] for x in zdfie._QUALITIES))
    # _VALID_URL of class ZDFIE starts with 'https?://www.zdf.de/'

# Generated at 2022-06-14 17:46:12.205925
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdfbase = ZDFBaseIE()
    assert zdfbase._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert zdfbase._GEO_COUNTRIES == ('DE',)

