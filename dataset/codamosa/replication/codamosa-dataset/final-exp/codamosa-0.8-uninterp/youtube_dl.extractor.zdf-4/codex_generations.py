

# Generated at 2022-06-14 17:37:52.682410
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE(ZDFBaseIE.ie_key())



# Generated at 2022-06-14 17:38:06.398450
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    obj = ZDFChannelIE()
    assert obj.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio') is True
    assert obj.suitable('https://www.zdf.de/dokumentation/planet-e') is True
    assert obj.suitable('https://www.zdf.de/filme/taunuskrimi/') is True
    assert obj.suitable('https://www.zdf.de/politik/ausland/mea-culpa-deutsche-buerger-entschuldigen-sich-in-suedkorea-100.html') is False

# Generated at 2022-06-14 17:38:19.095760
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Example for wiki page
    wikipage = """
    {{#widget:Iframe
      |url=http://www.zdf.de/ZDFmediathek/beitrag/video/1727246/Gem%C3%BCsesorten-die-fast-verschwunden-waren#/beitrag/video/1727246/Gem%C3%BCsesorten-die-fast-verschwunden-waren
      |width=95%
      |height=500
      |border=1
    }}
    """

# Generated at 2022-06-14 17:38:23.176124
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    '''
    Unit test for ZDFIE
    '''
    zdfie = ZDFIE()
    assert zdfie

# Generated at 2022-06-14 17:38:26.554216
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'ZDF'
    assert ie.extractor.ie_key() == 'ZDF'



# Generated at 2022-06-14 17:38:38.323094
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdfBaseIE = ZDFBaseIE()
    assert zdfBaseIE._GEO_COUNTRIES == ['DE']
    assert zdfBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert callable(zdfBaseIE._call_api), 'Call class method _call_api failed.'
    assert ZDFBaseIE._extract_subtitles({'captions': [{'uri': 'https://www.zdf.de/srt', 'language': 'deu'}]}), 'Call class method _extract_subtitles failed.'
    assert callable(zdfBaseIE._extract_format), 'Call class method _extract_format failed.'

# Generated at 2022-06-14 17:38:40.580005
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    return ZDFChannelIE.suitable('')



# Generated at 2022-06-14 17:38:41.784902
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:38:47.744298
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE._extract_subtitles({}) == {}
    assert ZDFBaseIE._extract_subtitles({'captions': []}) == {}
    assert ZDFBaseIE._extract_subtitles({'captions': [{
        'language': 'deu',
        'uri': 'http://example.com'
    }]}) == {'deu': [{'url': 'http://example.com'}]}



# Generated at 2022-06-14 17:38:52.625068
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf = ZDFBaseIE('zdf')
    assert zdf._GEO_COUNTRIES == ['DE']
    assert zdf._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:39:17.107417
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'ZDF'

# Generated at 2022-06-14 17:39:25.539434
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert not ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/ab-18/10-wochen-sommer-102.html')
    assert ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html')
    assert not ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html')

# Generated at 2022-06-14 17:39:28.982910
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE('https://www.zdf.de/politik/phoenix-sendungen/die-gesten-der-maechtigen-100.html')



# Generated at 2022-06-14 17:39:39.251982
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE("http://www.zdf.de/ZDFmediathek/nachrichten/heute-nachrichten/30-jahre-mauerfall-der-tag-der-deutschen-einheit-100.html?documentId=25749768", {})._GEO_COUNTRIES == ['DE']
    assert ZDFBaseIE("http://www.zdf.de/ZDFmediathek/nachrichten/heute-nachrichten/30-jahre-mauerfall-der-tag-der-deutschen-einheit-100.html?documentId=25749768", {})._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:39:41.022854
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfIE = ZDFIE()
    assert zdfIE is not None


# Generated at 2022-06-14 17:39:51.277150
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.IE_NAME == 'ZDF'
    expected = 'https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html'
    assert ie._VALID_URL == expected
    expected = 'https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html'
    assert ie.sanitize_url(expected) == expected
    assert ie.extract_id(expected) == '100'

# Generated at 2022-06-14 17:39:58.697166
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    ie._GEO_COUNTRIES = ['DE']
    ie._QUALITIES = ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert(ie._GEO_COUNTRIES == ['DE'])
    assert(ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'))



# Generated at 2022-06-14 17:40:00.273307
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    try:
        ZDFChannelIE()
    except Exception as e:
        assert str(e) == 'class ZDFChannelIE must be subclassed, this constructor is only for unit test!'
    else:
        assert False


# Generated at 2022-06-14 17:40:05.210936
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    import inspect
    member_functions = inspect.getmembers(ZDFBaseIE, predicate=inspect.ismethod)
    for (name, function) in member_functions:
        print(name)



# Generated at 2022-06-14 17:40:07.684175
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE.suitable(ZDFChannelIE._VALID_URL)



# Generated at 2022-06-14 17:41:09.861098
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    channel = ZDFChannelIE(ZDFChannelIE.ie_key())

    assert channel.INFO_TEMPLATE % 'zdf_id' == \
        'https://api.zdf.de/content/documents/zdf_id.json'


# Generated at 2022-06-14 17:41:13.902305
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    result = ZDFIE()

    assert result
    assert isinstance(result, InfoExtractor)
    assert isinstance(result, ZDFBaseIE)

# Test for method _extract_entry of class ZDFIE

# Generated at 2022-06-14 17:41:17.921695
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # SUT
    ie = ZDFChannelIE("https://www.zdf.de/sport/das-aktuelle-sportstudio")
    # Assertions
    assert ie.__class__.__name__ == "ZDFChannelIE"
#


# Generated at 2022-06-14 17:41:26.221362
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    obj = ZDFIE(None)
    expected_zdf_base = ZDFBaseIE(None)
    assert obj._GEO_COUNTRIES == expected_zdf_base._GEO_COUNTRIES
    assert obj._VALID_URL == ZDFIE._VALID_URL
    assert obj._TESTS == ZDFIE._TESTS
    assert obj.ie_key() == 'ZDF'
    assert obj.SUCCESS == True



# Generated at 2022-06-14 17:41:34.742389
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfchannelie = ZDFChannelIE()
    print(zdfchannelie.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio'))    
    print(zdfchannelie.suitable('https://www.zdf.de/dokumentation/planet-e'))
    print(zdfchannelie.suitable('https://www.zdf.de/filme/taunuskrimi'))
    print(zdfchannelie.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio'))
    print(zdfchannelie.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio'))
    print('\n')


# Generated at 2022-06-14 17:41:42.581996
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    url = 'http://www.zdf.de/ZDFmediathek/hauptnavigation/startseite#/beitrag/video/2061146/Volle%20Kraft%20vorraus%20-%20Auf%20Hoher%20See%20-%20ZDFinfo%20Doku'
    ie = ZDFBaseIE()
    # set self.url
    ie.url = url
    assert ie.url == url
    # self._GEO_COUNTRIES is protected/immutable
    try:
        ie._GEO_COUNTRIES.append('US')
        assert False
    except AttributeError:
        assert True
    # self._QUALITIES is protected/immutable

# Generated at 2022-06-14 17:41:46.531424
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE('ZDF', 'DE')
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:41:47.824501
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE(2, 3)


# Generated at 2022-06-14 17:41:49.622095
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    """
    Make sure the ZDFIE class has been defined
    """
    assert ZDFIE(None) is not None


# Generated at 2022-06-14 17:41:59.984963
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    url = 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    video_id = ZDFIE._match_id(url)
    webpage = ZDFIE._download_webpage(url, video_id, fatal=False)
    player = ZDFIE._extract_player(webpage, url, fatal=False)
    content = ZDFIE._call_api(player['content'], video_id, 'content', player['apiToken'], url)
    entry = ZDFIE._extract_entry(player['content'], player, content, video_id)
    formats_list = entry.get('formats')

# Generated at 2022-06-14 17:44:14.980103
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    from .common import InfoExtractor
    # ZDFBaseIE is a subclass of InfoExtractor
    assert issubclass(ZDFBaseIE, InfoExtractor)
    # Create an instance of class ZDFIE
    # Now we have a custom video downloader
    ie = ZDFIE()
    ie.ie_key()
    ie._VALID_URL
    ie._TESTS
    ie._extract_regular()
    ie._extract_mobile()

# Generated at 2022-06-14 17:44:16.355459
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE.constructor()
    assert isinstance(ie, ZDFBaseIE)


# Generated at 2022-06-14 17:44:20.351786
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    from tests import BaseTest
    obj = BaseTest()
    zdfbase = ZDFBaseIE(obj)
    assert zdfbase


# Generated at 2022-06-14 17:44:26.143055
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Construct an instance of class ZDFChannelIE
    z = ZDFChannelIE()
    # Execute the function _real_extract of class ZDFChannelIE
    z._real_extract('https://www.zdf.de/dokumentation/planet-e')
    # Execute the function _real_extract of class ZDFChannelIE
    z._real_extract('https://www.zdf.de/sport/das-aktuelle-sportstudio')

# Generated at 2022-06-14 17:44:35.536610
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Test the constructor of ZDFIE class
    ie = ZDFIE()
    ie = ZDFIE('https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html')
    assert ie.ie_key() == 'ZDF'
    assert ie.info_dict == dict()
    assert isinstance(ie._GEO_COUNTRIES, list)
    assert ie.options
    assert isinstance(ie.quality, qualities)
    assert isinstance(ie.video_id, compat_str)
    assert isinstance(ie.params, dict)
    assert isinstance(ie.headers, dict)
    assert isinstance(ie.destination, compat_str)

# Generated at 2022-06-14 17:44:36.633276
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert issubclass(ZDFChannelIE, ZDFBaseIE)



# Generated at 2022-06-14 17:44:43.944717
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Static class calls not possible in python 2
    ZDFChannelIE._download_webpage = lambda a, b: str(a + b)
    ZDFChannelIE._og_search_title = lambda a, b: str(a + b)
    ZDFChannelIE._search_regex = lambda a, b, c, d: str(a + b + c + d)
    ZDFChannelIE._call_api = lambda a, b, c, d, e: str(a + b + c + d + e)
    ZDFChannelIE.url_result = lambda a, b, c: str(a + b + str(c))
    ZDFChannelIE.playlist_result = lambda a, b, c: str(a + b + c)
    ZDFChannelIE.ie_key = lambda: "test_ie"

    assert Z

# Generated at 2022-06-14 17:44:46.217956
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:44:58.272698
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # url = 'http://www.zdf.de/ZDFmediathek/beitrag/video/2656234/Sturm-auf-den-Reichstag'
    url = 'http://www.zdf.de/ZDFmediathek/beitrag/video/2656234/Sturm-auf-den-Reichstag'
    ie = ZDFBaseIE()
    ie._search_regex(r'''(?s)data-zdfplayer-jsb=(["\'])(?P<json>{.+?})\1''', '', 'player JSON')
    #print(ie._search_regex(r'''(?s)data-zdfplayer-jsb=(["\'])(?P<json>{.+?})\1''', webpage,
    #    'player JSON

# Generated at 2022-06-14 17:44:59.466054
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    return ZDFBaseIE
