

# Generated at 2022-06-14 17:37:56.538265
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert(ZDFIE)


# Generated at 2022-06-14 17:37:58.469265
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Unit test for the class constructor
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 17:38:10.050129
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.get_geo_countries() == ie._GEO_COUNTRIES
    assert ie.get_quality_order() == ie._QUALITIES
    assert ie.has_valid_url() == False
    assert ie.can_extract_id('https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html') == True
    assert ie.can_extract_id('https://www.zdf.de/politik/phoenix/wohin-fuehrt-der-protest-in-der-pandemie-100.html') == True

# Generated at 2022-06-14 17:38:17.457240
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE("https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html")
    assert isinstance(zdfie, ZDFIE)
    assert zdfie._VALID_URL
    assert zdfie._TESTS


# Generated at 2022-06-14 17:38:26.762131
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    obj = ZDFIE('https://www.zdf.de/nachrichten/heute/nach-schiedsrichter-attacke-tim-wiese-ich-bin-im-falschen-beruf-100.html')
    assert obj is not None
    assert obj.ZDFIE('https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html')


# Generated at 2022-06-14 17:38:39.601726
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/kinder/sander'
    webpage = download_webpage(
        url, 'ZDFChannel', headers={
            'Accept-Encoding': 'identity',
            'Accept-Language': 'en-US,en;q=0.5',
        }).decode()
    ie = ZDFChannelIE()
    r = ie.suitable(url)
    assert r == False
    # Test for matching
    r = ie._real_extract(url)
    assert r['id'] == 'sander'
    assert type(r['entries'][0]) is dict
    assert type(r['entries'][0]['url']) is compat_str

# Generated at 2022-06-14 17:38:40.674719
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE(InfoExtractor(), {})



# Generated at 2022-06-14 17:38:44.297090
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert hasattr(ie, 'report_warning')
    assert hasattr(ie, 'extract_url')
    assert hasattr(ie, '_LOGGER_NAME')
    assert hasattr(ie, '_VALID_URL')


# Generated at 2022-06-14 17:38:45.849165
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    i = ZDFIE()
    print(i)


# Generated at 2022-06-14 17:38:57.709840
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannelIE = ZDFChannelIE()
    assert zdfChannelIE.suitable("https://www.zdf.de/dokumentation/planet-e") is True
    assert zdfChannelIE.suitable("https://www.zdf.de/filme/taunuskrimi/") is True
    assert zdfChannelIE.suitable("https://www.zdf.de/dokumentation/planet-e/") is True
    assert zdfChannelIE.suitable("https://www.zdf.de/sport/das-aktuelle-sportstudio") is True
    assert zdfChannelIE.suitable("https://www.zdf.de/sport/das-aktuelle-sportstudio/") is True



# Generated at 2022-06-14 17:39:35.510761
# Unit test for constructor of class ZDFChannelIE

# Generated at 2022-06-14 17:39:37.917535
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    i = ZDFBaseIE()
    return i

# Generated at 2022-06-14 17:39:40.013739
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
	try:
		ZDFBaseIE()
	except:
		assert False
	assert True



# Generated at 2022-06-14 17:39:45.309003
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_ie = ZDFChannelIE()
    assert zdf_channel_ie.suitable(ZDFChannelIE._VALID_URL) != ZDFIE.suitable(ZDFChannelIE._VALID_URL)
    assert zdf_channel_ie.IE_NAME.startswith('ZDF') == True

# Generated at 2022-06-14 17:39:52.898802
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    pattern = re.compile(ZDFIE._VALID_URL)
    assert pattern.match("http://www.zdf.de/filme/filme-sonstige/der-hauptmann-112.html")
    assert pattern.match("https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html")
    assert pattern.match("https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html")


# Generated at 2022-06-14 17:39:55.390822
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Makes sure that the class ZDFBaseIE is not abstract
    ZDFBaseIE()


# Generated at 2022-06-14 17:40:00.628581
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    """
    Check if ZDFIE is initialized with only one argument
    """
    # arrange
    url = "https://www.zdf.de/filme/filme-sonstige/der-hauptmann-112.html"
    ie = ZDFIE()

    # act
    ie._real_extract(url)

    # assert



# Generated at 2022-06-14 17:40:14.109104
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """Test the constructor of class ZDFChannelIE."""
    zdfchannel_ie = ZDFChannelIE()
    assert zdfchannel_ie.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio') == True
    assert zdfchannel_ie.suitable('https://www.zdf.de/dokumentation/planet-e') == True
    assert zdfchannel_ie.suitable('https://www.zdf.de/filme/taunuskrimi/') == True
    assert zdfchannel_ie.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html') == False
    assert zdfchannel_

# Generated at 2022-06-14 17:40:16.215973
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE('zdf.de/filme')._real_extract('https://www.zdf.de/filme/taunuskrimi/')


# Generated at 2022-06-14 17:40:21.458973
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE(None)
    assert zdfie.ie_key() == 'ZDF'
    assert zdfie.IE_DESC == 'ZDF Mediathek'
    assert zdfie._GEO_COUNTRIES == ['DE']
    assert zdfie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert zdfie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'



# Generated at 2022-06-14 17:41:21.990407
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    video_id = '210222_phx_nachgehakt_corona_protest'
    webpage = 'http://www.zdf.de/serie/phoenix-sendungen/sendungen/zu-gast-bei-phoenix/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    api_url = 'https://zdf-cdn.live.cellular.de/mediathekV2/document/%s' % video_id

    # Test a normal case
    info = ZDFIE()._extract_mobile(video_id)
    assert info['id'] == video_id
    assert info['url'] == api_url
    assert info['title'] == 'Wohin führt der Protest in der Pandemie?'

# Generated at 2022-06-14 17:41:27.258974
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test = ZDFBaseIE("https://www.zdf.de/doku/das-geheimnis-der-biberspringerin-100.html")
    assert test._GEO_COUNTRIES == ["DE"]
    assert test._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:41:28.257575
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    return ZDFIE()



# Generated at 2022-06-14 17:41:34.721864
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf_base_ie = ZDFBaseIE()
    assert zdf_base_ie._GEO_COUNTRIES == ['DE']
    assert zdf_base_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:41:36.951163
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie.ie_key() == 'zdf'

# Test for _GEO_COUNTRIES

# Generated at 2022-06-14 17:41:40.206189
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie.name == 'ZDF'
    assert ie.ie_key() == 'zdf'
    assert ie.host == 'zdf.de'
    assert ie.test()
    assert ie.api_host == 'api.zdf.de'
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert ie._VALID_URL == None


# Generated at 2022-06-14 17:41:47.122099
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    print(ZDFChannelIE.suitable(
        'https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html'))
    print(ZDFChannelIE.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio'))


# Generated at 2022-06-14 17:41:48.203235
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE.suite()

# Generated at 2022-06-14 17:41:53.337299
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannelIE = ZDFChannelIE()
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    channel_id = 'das-aktuelle-sportstudio'
    assert zdfChannelIE._match_id(url) == channel_id

# Generated at 2022-06-14 17:41:54.621312
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE('', None)


# Generated at 2022-06-14 17:44:22.405384
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    inst = ZDFIE()
    assert inst.go_geo_bypass
    assert inst.geo_countries == inst._GEO_COUNTRIES
    assert inst.qualities == inst._QUALITIES
    assert ZDFIE.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:44:24.624718
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    import doctest

    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)


# Generated at 2022-06-14 17:44:27.527415
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdfBaseIE = ZDFBaseIE(None)



# Generated at 2022-06-14 17:44:33.875435
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    url = 'https://www.zdf.de/filme/filme-sonstige/der-hauptmann-112.html'
    ie = ZDFIE(url)
    assert (ie.url == url)
    assert (ie.video_id == '100100_dok_hauptmann_film')
    assert (ie._VALID_URL == 'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html')


# Generated at 2022-06-14 17:44:44.581149
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    # test for _call_api
    headers = {}
    api_token = 'abcdef'
    referrer = 'http://www.zdf.de/anzeige'
    headers['Api-Auth'] = 'Bearer %s' % api_token
    headers['Referer'] = referrer
    assert ie._call_api('http://www.zdf.de/api/animals', 'video_id', 'Downloading JSON', headers=headers)
    # test for _extract_subtitles
    src = {'captions': [{'uri': 'http://subtitle1.de/subtitle'}, {'uri': 'http://subtitle2.de/subtitle'}, {'uri': 'http://subtitle3.de/subtitle', 'language': 'eng'}]}


# Generated at 2022-06-14 17:44:47.192736
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'zdf'


# Generated at 2022-06-14 17:44:53.251727
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf = ZDFIE()
    zdf.url = "http://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html"
    zdf._real_extract(zdf.url)



# Generated at 2022-06-14 17:44:59.334358
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    i=ZDFBaseIE()
    i.extract("https://www.zdf.de/comedy/die-anstaendigen/die-anstaendigen-episoden-100.html")
    i.extract("https://www.zdf.de/nachrichten/heute-journal/heute-journal-aktuelle-ausgabe-vom-3.-januar-2019-100.html")


# Generated at 2022-06-14 17:45:00.693228
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    assert zdfie != None

# Generated at 2022-06-14 17:45:06.026381
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Test empty constructor
    ie = ZDFChannelIE()
    assert ie.ie_key() == 'ZDFChannel'
    assert ie.http_headers == {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    }  # default http headers

