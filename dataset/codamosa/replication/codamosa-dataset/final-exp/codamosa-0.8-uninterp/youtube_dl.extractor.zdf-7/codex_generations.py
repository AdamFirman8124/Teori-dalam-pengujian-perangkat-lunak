

# Generated at 2022-06-14 17:38:00.750240
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    for url in ['http://www.zdf.de/sport/das-aktuelle-sportstudio',
                'http://www.zdf.de/dokumentation/planet-e']:
        assert ZDFChannelIE._match_id(url) is not None
        assert ZDFChannelIE._VALID_URL == ZDFIE._VALID_URL


# Generated at 2022-06-14 17:38:04.537737
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:38:10.829265
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    for proto in ('http://', 'https://'):
        for host in ('www.zdf.de', 'zdftivi.zdf.de'):
            for path in ('/node/321134', '/zdf/embed/a-very-strange-string'):
                yield (
                    ZDFBaseIE.test,
                    '%s%s%s' % (proto, host, path)
                )
# Must be the first IE

# Generated at 2022-06-14 17:38:14.655149
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    test = ZDFIE()
    test._VALID_URL
    test._TESTS
    test._extract_entry
    test._extract_regular

# Generated at 2022-06-14 17:38:19.378755
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    url = 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    video_id = '210222_phx_nachgehakt_corona_protest'
    webpage = '<html></html>'
    player_json = "{}"
    IE = ZDFIE
    info = IE._extract_regular(url, player_json, video_id)
    assert info == {}

# Generated at 2022-06-14 17:38:21.762792
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES==['DE']
    assert ie._QUALITIES==('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:38:22.561073
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE('ZDFBaseIE')


# Generated at 2022-06-14 17:38:29.364324
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

    player_json = '{"foo":1}'
    assert ie._parse_json(player_json, 'video_id') == {'foo': 1}


# Generated at 2022-06-14 17:38:37.154318
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE.suitable("https://www.zdf.de/dokumentation/planet-e")
    ZDFChannelIE.suitable("https://www.zdf.de/nachrichten/ausland/putin-russland-corona-pandemie-zr-100.html")
    ZDFChannelIE.suitable("https://www.zdf.de/nachrichten/heute/sendung-vom-21-04-2020-100.html")

# Generated at 2022-06-14 17:38:49.099369
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/filme/taunuskrimi/'
    assert ZDFChannelIE.suitable(url), 'URL should be suitable'
    assert not ZDFIE.suitable(url), 'URL should not be suitable'
    # matching of URL always returns 'das-aktuelle-sportstudio'
    assert ZDFChannelIE._match_id(url) == 'das-aktuelle-sportstudio'

# Unit (non-)test of class ZDFMobileIE.
# Normally, ZDFMobileIE is used as a fallback and ZDFIE as the preferred
# extractor.
# Since URLs for mobile and non-mobile content are identical,
# this fallback is not tested.
# https://github.com/ytdl-org/youtube-dl/issues/2848

# Generated at 2022-06-14 17:39:14.858458
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    pass


# Generated at 2022-06-14 17:39:23.811737
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    test_cases = [
        (1, 'https://www.zdf.de/filme/der-alte/mord-in-der-rosenlaube-103.html', 'der-alte'),
        (2, 'https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html', 'planet-e')
    ]
    for (test_no, test_url, expected_channel_id) in test_cases:
        print("Testing ZDFChannelIE.suitable() for test case %d..." % test_no)
        assert ZDFChannelIE.suitable(test_url)
        print("Test case %d passed." % test_no)
        ie = ZDFChannelIE

# Generated at 2022-06-14 17:39:31.972689
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf_base_ie = ZDFBaseIE()

    assert zdf_base_ie._GEO_COUNTRIES == ['DE'], 'ZDFBaseIE._GEO_COUNTRIES is not "DE"'
    assert zdf_base_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'), 'ZDFBaseIE._QUALITIES is not ("auto", "low", "med", "high", "veryhigh", "hd")'


# Generated at 2022-06-14 17:39:38.909507
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    is_match = ZDFChannelIE.suitable(url)
    assert is_match == True
    instance = ZDFChannelIE()
    assert instance._VALID_URL == ZDFChannelIE._VALID_URL
    assert instance._TESTS == ZDFChannelIE._TESTS
    assert instance.ie_key() == 'zdf:channel'
    assert instance.suitable(url) == True

# Generated at 2022-06-14 17:39:41.129390
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie.geo_countries == ['DE']


# Generated at 2022-06-14 17:39:44.033729
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == "ZDF"


# Generated at 2022-06-14 17:39:45.544255
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert isinstance(ZDFBaseIE('zdf'), InfoExtractor)


# Generated at 2022-06-14 17:39:48.027378
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # First test the case that suitable() returns False
    assert not ZDFChannelIE.suitable(ZDFIE._VALID_URL)
    # Then run the real test
    ZDFChannelIE()._real_extract(ZDFChannelIE._TESTS[0]['url'])



# Generated at 2022-06-14 17:39:55.401266
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    assert zdfie._VALID_URL == "https?://www\\.zdf\\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\\.html"

# Generated at 2022-06-14 17:40:03.456835
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf = ZDFChannelIE()
    assert zdf.suitable('https://www.zdf.de/filme/taunuskrimi/') is False
    assert zdf.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html') is True



# Generated at 2022-06-14 17:40:55.695263
# Unit test for constructor of class ZDFIE
def test_ZDFIE(): 
    assert ZDFIE._VALID_URL == re.compile(ZDFIE._VALID_URL)


# Generated at 2022-06-14 17:40:59.115770
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert hasattr(ZDFBaseIE, 'IE_NAME')
    assert hasattr(ZDFBaseIE, '_VALID_URL')



# Generated at 2022-06-14 17:41:00.452623
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf = ZDFBaseIE()
    assert zdf is not None


# Generated at 2022-06-14 17:41:09.976916
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    player = {
        'apiToken': '00000000000000000000',
        'content': 'https://zdf.de/path/to/content',
    }

# Generated at 2022-06-14 17:41:17.247236
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE is not None
    assert ZDFBaseIE.ie_key() is not None
    assert ZDFBaseIE._GEO_COUNTRIES is not None
    assert ZDFBaseIE._QUALITIES is not None
    assert ZDFBaseIE._call_api is not None
    assert ZDFBaseIE._extract_subtitles is not None
    assert ZDFBaseIE._extract_format is not None
    assert ZDFBaseIE._extract_ptmd is not None
    assert ZDFBaseIE._extract_player is not None



# Generated at 2022-06-14 17:41:22.675157
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    obj = ZDFBaseIE("https://www.zdf.de/dokumentation/die-deutschen/die-deutschen-das-ende-der-schuld-100.html")
    assert obj != None


# Generated at 2022-06-14 17:41:28.257627
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    z = ZDFChannelIE()
    # Method suitable should return False if ZDFIE.suitable(url) returns True
    assert z.suitable(ZDFIE._TESTS[0]['url']) is False
    # Method suitable should return True if ZDFIE.suitable(url) returns False
    assert z.suitable(ZDFChannelIE._TESTS[0]['url']) is True



# Generated at 2022-06-14 17:41:33.666824
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    base_ie = ZDFBaseIE()
    assert base_ie._GEO_COUNTRIES == ['DE']
    assert base_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')




# Generated at 2022-06-14 17:41:42.046972
# Unit test for constructor of class ZDFIE

# Generated at 2022-06-14 17:41:44.014162
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()  # pylint: disable=W0104



# Generated at 2022-06-14 17:43:48.168749
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE()


# Generated at 2022-06-14 17:43:52.599678
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFIE.ie_key() == 'zdf'
    assert ZDFChannelIE.ie_key() == 'zdf:channel'

ZDFMediathekBaseIE = ZDFBaseIE


# Generated at 2022-06-14 17:43:57.581858
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    obj = ZDFBaseIE()
    assert obj._GEO_COUNTRIES == ['DE']
    assert obj._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert obj._downloader is None
    assert obj._downloader_context is None


# Generated at 2022-06-14 17:44:07.033546
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_ie_ins = ZDFChannelIE()
    print(zdf_channel_ie_ins.__class__)
    print(zdf_channel_ie_ins._VALID_URL)
    print(zdf_channel_ie_ins.suitable(
        'https://www.zdf.de/dokumentation/planet-e'))
    print(zdf_channel_ie_ins.suitable(
        'https://www.zdf.de/filme/filme-sonstige/der-hauptmann-112.html'))



# Generated at 2022-06-14 17:44:14.255020
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert(ie._VALID_URL == 'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html')

# Generated at 2022-06-14 17:44:25.540361
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'ZDF'
    assert ZDFIE.ie_key() == ie.ie_key()
    assert ie.SUITES == [ZDFIE._VALID_URL]

# Generated at 2022-06-14 17:44:35.500791
# Unit test for constructor of class ZDFBaseIE

# Generated at 2022-06-14 17:44:36.804383
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    if __name__ == '__main__':
        zdfBaseIE = ZDFBaseIE()

# Generated at 2022-06-14 17:44:43.322722
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE # ZDFBaseIE is a class
    try:
        assert ZDFBaseIE._GEO_COUNTRIES == ['DE'], "ZDFBaseIE._GEO_COUNTRIES == ['DE']"
    except AttributeError as e:
        print("Error: ZDFBaseIE._GEO_COUNTRIES == ['DE']")
        print("  " + str(e))
    assert ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'), "ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')"
test_ZDFBaseIE()


# Generated at 2022-06-14 17:44:44.576192
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE()
