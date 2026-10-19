

# Generated at 2022-06-14 17:38:00.945121
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    url = 'https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html'
    cls = ZDFIE
    cls(url)

    assert len(cls._TESTS) == 8
    assert 'phoenix' in cls._TESTS[0]['url']
    assert 'ab-18' in cls._TESTS[1]['url']
    assert 'taunuskrimi' in cls._TESTS[3]['url']



# Generated at 2022-06-14 17:38:04.327890
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    obj = ZDFBaseIE()
    assert not obj._GEO_COUNTRIES
    assert obj._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:38:06.250148
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    result = ZDFIE()
    assert(result.ie_key() == 'ZDF')


# Generated at 2022-06-14 17:38:14.235063
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Test initialization of class ZDFIE
    video_id = '210222_phx_nachgehakt_corona_protest'
    url = 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    _ = ZDFIE(ZDFIE._create_ie_instance(), url, video_id)

# Generated at 2022-06-14 17:38:22.293953
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE.suitable({}) == False
    assert ZDFChannelIE.suitable({'url': 'https://www.zdf.de/dokumentation/planet-e'}) == True
    assert ZDFChannelIE.suitable({'url': 'https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html'}) == False
    assert ZDFChannelIE.suitable({'url': 'https://www.zdf.de/service-und-hilfe/die-neue-zdf-mediathek/zdfmediathek-trailer-100.html'}) == False

# Generated at 2022-06-14 17:38:34.956503
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie_key = ZDFIE.ie_key()
    assert ie_key == 'ZDF'
    tester = ZDFIE()
    assert tester._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'

# Generated at 2022-06-14 17:38:40.417550
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf = ZDFBaseIE()
    assert zdf._GEO_COUNTRIES == ['DE']
    assert zdf._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert isinstance(zdf._extract_subtitles({}), dict)


# Generated at 2022-06-14 17:38:51.636901
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    class DummyInfoExtractor(object):
        def __init__(self, ie_key):
            self._ie_key = ie_key

    class DummyInfoExtractorConstructor(object):
        def __init__(self):
            pass

        @staticmethod
        def suitable(url):
            return True

        @staticmethod
        def ie_key():
            return 'dummy'

    # Unit test for constructor of class ZDFChannelIE
    ie_key = 'ZDFChannelIE'
    dummy_ie = DummyInfoExtractor(ie_key)
    dummy_ie_constructor = DummyInfoExtractorConstructor()
    # No value
    url = 'https://www.zdf.de/dokumentation/planet-e'

# Generated at 2022-06-14 17:39:01.564233
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    cls = ZDFChannelIE
    for base_url, ie_key in [(ZDFIE.ie_key(), ZDFIE.ie_key()), (ZDFIE.ie_key(), ZDFChannelIE.ie_key())]:
        cls.BASE_URL = base_url
        assert cls.suitable(ZDFIE._VALID_URL.replace('(?P<id>[^/?#&]+)', 'politik/frontal21'))
        assert cls.ie_key() == ie_key
        assert cls.construct_url('politik/frontal21').startswith((ZDFIE.BASE_URL, ZDFIE._VALID_URL.replace('(?P<id>[^/?#&]+)', 'politik/frontal21')))

# Generated at 2022-06-14 17:39:02.283454
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()



# Generated at 2022-06-14 17:39:32.776027
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert not ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html')
    assert ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/')
    assert not ZDFChannelIE.suitable('https://www.zdf.de/')

# Generated at 2022-06-14 17:39:36.228481
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.IE_NAME == 'zdf'
    assert ie.IE_KEY == 'zdf.de'
    assert ie.GEO_COUNTRIES == ['DE']
    assert ie.QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:39:48.314905
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.extractor_key == 'ZDFChannel'
    assert ie.ie_key() == 'ZDF'
    assert ie.SUCCESS == 1
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 17:39:55.596461
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from .test import get_testcases
    from .zdf import ZDFSearchIE

    def _test(item):
        return isinstance(item, ZDFChannelIE)

    def get_playlist_count():
        return 0


# Generated at 2022-06-14 17:40:00.442830
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf_base_ie = ZDFBaseIE()
    assert zdf_base_ie._GEO_COUNTRIES == ['DE']
    assert zdf_base_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

test_ZDFBaseIE()



# Generated at 2022-06-14 17:40:13.950684
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    class MockIE(ZDFChannelIE):
        def _real_extract(self, url):
            pass
    assert MockIE.suitable(
        'https://www.zdf.de/service-und-hilfe/die-neue-zdf-mediathek/zdfmediathek-trailer-100.html') is True
    assert MockIE.suitable(
        'https://www.zdf.de/dokumentation/planet-e/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html') is False
    assert MockIE.suitable(
        'https://www.zdf.de/dokumentation/planet-e') is True

# Generated at 2022-06-14 17:40:17.552892
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    base = ZDFBaseIE()
    assert base._GEO_COUNTRIES == ['DE']
    assert base._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:40:30.405053
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    get_video_info = ZDFIE._extract_mobile
    video_id = '181113_zdf_tatort_schlangengrube'
    video = get_video_info(video_id)

    assert video['id'] == '181113_zdf_tatort_schlangengrube'
    assert video['title'] == 'Schlangengrube'

# Generated at 2022-06-14 17:40:31.302178
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    pass


# Generated at 2022-06-14 17:40:32.903688
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
	ZDFChannelIE()._real_extract('https://www.zdf.de/dokumentation/planet-e')

# Generated at 2022-06-14 17:41:00.733945
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    info_extractor = ZDFBaseIE()
    assert info_extractor._GEO_COUNTRIES == ['DE']
    assert info_extractor._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:41:01.345010
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    pass



# Generated at 2022-06-14 17:41:04.047325
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE(ZDFChannelIE.ie_key(), ZDFChannelIE._VALID_URL, {})


# Generated at 2022-06-14 17:41:06.519221
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE.ie_key() == 'zdf'
    assert ZDFIE().ie_key() == 'zdf'

# Generated at 2022-06-14 17:41:08.047857
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Test that constructor of class ZDFChannelIE gets correct
    # playlist_mincount
    assert ZDFChannelIE().playlist_mincount == 50

# Generated at 2022-06-14 17:41:15.589093
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE(None)
    # Check the values of _GEO_COUNTRIES and _QUALITIES
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    # Check the values of _VALID_URL and _TESTS
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'

# Generated at 2022-06-14 17:41:16.437127
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    a = ZDFBaseIE()


# Generated at 2022-06-14 17:41:17.726802
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    pass



# Generated at 2022-06-14 17:41:28.088289
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE._TESTS[0]['playlist_mincount'] = 1000
    ZDFChannelIE._TESTS[1]['playlist_mincount'] = 1000
    ZDFChannelIE.suitable = None
    ZDFChannelIE._real_extract = None
    channel_ie = ZDFChannelIE(ZDFChannelIE.ie_key())
    channel_ie.suitable = None
    channel_ie._real_extract = None
    channel_ie.info()
    assert channel_ie.extractor_key == 'zdf:channel'
    assert channel_ie.title == 'ZDF Channel'



# Generated at 2022-06-14 17:41:29.278975
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:42:44.350518
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """
    This unit test is called when you run `python setup.py test`
    or `python -m unittest discover -s tests`
    """
    # I haven't been able to work out exactly what a unit test is
    # so this is a stab in the dark.
    test_cases = {
        'https://www.zdf.de/sport/das-aktuelle-sportstudio': {},
        'https://www.zdf.de/dokumentation/planet-e': {},
        'https://www.zdf.de/filme/taunuskrimi': None,
    }
    for input_url, output_value in test_cases.items():
        ie = ZDFChannelIE(input_url)
        if output_value is None:
            assert not ie.suitable

# Generated at 2022-06-14 17:42:52.484038
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # constructor: ZDFChannelIE.__init__(self, name)
    #
    # method: ZDFChannelIE._real_extract(self, url)
    #
    # settings: self._downloader.params.get(param, default)
    # settings: self._downloader.params[param] = value
    # settings: self._downloader.params.pop(param, default)
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl_opts = {}
    zdf_ie = ZDFChannelIE('zdf')
    ydl = YoutubeDL(ydl_opts)
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(zdf_ie)

# Generated at 2022-06-14 17:42:54.596495
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    a = ZDFIE()
    assert a._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'


# Generated at 2022-06-14 17:43:01.328960
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'
    assert ie._TESTS[0]['url'] == 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    assert ie._TESTS[0]['md5'] == '34ec321e7eb34231fd88616c65c92db0'


# Generated at 2022-06-14 17:43:03.032638
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    instance = ZDFIE()
    assert isinstance(instance, InfoExtractor)


# Generated at 2022-06-14 17:43:11.572165
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'

    url_ZDF = 'https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html'

    assert ZDFChannelIE.suitable(url)
    assert not ZDFChannelIE.suitable(url_ZDF)

    zdfChannel = ZDFChannelIE()
    zdfChannel._match_id(url)

# Generated at 2022-06-14 17:43:13.310354
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert isinstance(
        ZDFChannelIE(),
        ZDFChannelIE
    )




# Generated at 2022-06-14 17:43:18.690303
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from youtube_dl.utils import SearchInfoExtractor
    ie = SearchInfoExtractor(
        {'ie': 'zdf', 'title': 'lololol', 'channel_id': 'lololol',
         'channel': 'lololol', 'categories': ['lololol']}
    )
    assert ie.main_url == 'https://www.zdf.de/suche/lololol'

# Generated at 2022-06-14 17:43:28.779772
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    input1 = 'http://www.zdf.de/ZDFmediathek/beitrag/video/2689718/Mann-fragt-400-Frauen-nach-einem-Date#/beitrag/video/2689718/Mann-fragt-400-Frauen-nach-einem-Date'
    input2 = 'https://www.zdf.de/comedy/die-anstalt/die-anstalt-vom-11-oktober-2017-100.html'
    ZDFBaseIE().suitable(input1)
    ZDFBaseIE().suitable(input2)


# Generated at 2022-06-14 17:43:29.812862
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE(None)


# Generated at 2022-06-14 17:45:35.541429
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE._GEO_COUNTRIES == ['DE']
    assert ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:45:38.040891
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    """
    Basic test of ZDFBaseIE class
    """
    class TestZDFBaseIE(ZDFBaseIE):
        pass

    # Test only class constructor
    TestZDFBaseIE('test')


# Generated at 2022-06-14 17:45:43.482924
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    return ZDFChannelIE(ZDFChannelIE._create_get_urls_request(['https://www.zdf.de/sport/das-aktuelle-sportstudio']))._GET

# Generated at 2022-06-14 17:45:48.667945
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    pnme = ie._GEO_COUNTRIES
    qlt = ie._QUALITIES
    assert pnme == ['DE']
    assert qlt == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:45:49.270276
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()

# Generated at 2022-06-14 17:45:50.574718
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE()



# Generated at 2022-06-14 17:45:53.221909
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    global ZDFIE
    ZDFIE = type('ZDFIE', (ZDFBaseIE,), dict(ZDFIE.__dict__, ie_key=lambda x: 'zdf'))


# Generated at 2022-06-14 17:45:54.858755
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannel = ZDFChannelIE()
    assert isinstance(zdfChannel, ZDFChannelIE)



# Generated at 2022-06-14 17:45:57.143412
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE()



# Generated at 2022-06-14 17:45:59.134072
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # get an instance of ZDFIE
    instance = ZDFIE()
    assert(instance)
