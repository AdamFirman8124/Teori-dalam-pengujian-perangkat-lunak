

# Generated at 2022-06-14 17:37:55.230458
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    module = sys.modules[__name__]
    class_ = getattr(module, 'ZDFChannelIE')
    instance = class_()
    url = 'https://www.zdf.de/dokumentation/planet-e'
    assert instance.suitable(url) == True


# Generated at 2022-06-14 17:37:57.083690
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
	initial_instance = ZDFIE()

# Generated at 2022-06-14 17:38:00.039683
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    x = ZDFChannelIE({})
    assert x.suitable
    assert ZDFChannelIE.suitable
    assert ZDFChannelIE.suitable({})


# Generated at 2022-06-14 17:38:04.272905
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    obj = ZDFBaseIE("https://www.zdf.de/foo")
    assert obj._GEO_COUNTRIES == ['DE']
    assert obj._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:38:08.712471
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE('https://www.zdf.de/service-und-hilfe/die-neue-zdf-mediathek/zdfmediathek-trailer-100.html')
    assert ie._VALID_URL == ie._VALID_URL



# Generated at 2022-06-14 17:38:20.416330
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    class TestZDFChannelIE(ZDFChannelIE):
        def __init__(self, *args, **kwargs):
            super(ZDFChannelIE, self).__init__(*args, **kwargs)
            self.player = None
            self.channel = None
            self.channel_id = None
            self.webpage = None

        def _extract_player(self, webpage, channel_id, fatal=True):
            self.webpage = webpage
            self.player = super(TestZDFChannelIE, self)._extract_player(webpage, channel_id, fatal)

            return self.player


# Generated at 2022-06-14 17:38:30.305990
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    """Unit test for constructor of class ZDFBaseIE"""
    from yt_dl.YoutubeDL import YoutubeDL
    from inspect import currentframe, getfile

    ydl = YoutubeDL({'verbose':True,'simulate':True,'writedescription':False})
    zdfbaseie = ZDFBaseIE(ydl)
    assert zdfbaseie.extractor_key == 'ZDF'
    assert zdfbaseie.IE_NAME == 'ZDF'
    assert zdfbaseie.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:38:36.504918
# Unit test for constructor of class ZDFChannelIE

# Generated at 2022-06-14 17:38:40.229038
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
  ie = ZDFBaseIE("ZDFBaseIE", {"geo_countries": ["DE"]})
  assert ie.geo_countries == ["DE"]



# Generated at 2022-06-14 17:38:43.899447
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    # constructor of class ZDFBaseIE
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:39:09.470531
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    tests = ZDFIE._TESTS
    for test in tests:
        yield (test,)


# Generated at 2022-06-14 17:39:11.442796
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    ie.assign_full_classpath()

# Test for method _extract_entry() of class ZDFIE

# Generated at 2022-06-14 17:39:19.867142
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE(None, {}, {'extractor': ZDFIE})
    assert ie
    assert hasattr(ie, '_call_api')
    assert hasattr(ie, '_extract_subtitles')
    assert hasattr(ie, '_extract_format')
    assert hasattr(ie, '_extract_ptmd')
    assert hasattr(ie, '_extract_player')



# Generated at 2022-06-14 17:39:24.311588
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_object = ZDFBaseIE(
        'https://www.zdf.de/comedy/extra-3/extra-3-vom-23-november-2017-100.html')
    assert test_object._GEO_COUNTRIES == ['DE']
    assert test_object._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:39:30.711671
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannelIE = ZDFChannelIE()
    assert zdfChannelIE.suitable(ZDFChannelIE._VALID_URL) == True
    assert ZDFChannelIE._VALID_URL == "https://www.zdf.de/(?:[^/]+/)*(?P<id>[^/?#&]+)"


# Generated at 2022-06-14 17:39:31.631267
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # TODO: Add tests
    return True



# Generated at 2022-06-14 17:39:36.810261
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    webpage = download_webpage(url, 'ZDFChannelIE unit test: Downloading webpage')
    ie = ZDFChannelIE(url, webpage)
    assert ie.id_ == 'planet-e'
    assert ie.title == 'planet e.'


# Generated at 2022-06-14 17:39:48.397528
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Dummy values for the test
    url = 'https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html'
    webpage = 'https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html'
    player = {
        'content': 'https://api.zdf.de/content/documents/151025_magie_farben2_tex?profile=player-ng&full=true',
        'apiToken': 'test'
    }

    # Testing for url

# Generated at 2022-06-14 17:39:58.438671
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf_base_ie = ZDFBaseIE()
    zdf_ie = ZDFIE()
    # Initialize the constructor of class ZDFIE with a mock object
    zdf_ie.params = zdf_base_ie.params
    assert isinstance(zdf_ie.params, ZDFBaseIE.__bases__[0].params)
    assert zdf_ie._GEO_COUNTRIES == ['DE']
    assert zdf_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert zdf_ie.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:39:59.573925
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:40:51.211153
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE.ie_key() == "zdf"


# Generated at 2022-06-14 17:41:00.536070
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_ie = ZDFChannelIE('sport/das-aktuelle-sportstudio')

    assert zdf_channel_ie._VALID_URL == 'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert zdf_channel_ie._REAL_URL == 'https://www.zdf.de/sport/das-aktuelle-sportstudio'

# Generated at 2022-06-14 17:41:10.041458
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    info_extractor = ZDFIE()
    assert info_extractor._VALID_URL == 'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'

# Generated at 2022-06-14 17:41:18.190258
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    """
    Unit test for constructor of class ZDFIE
    """
    from .common import InfoExtractor
    from .common import InfoExtractor
    from ..compat import compat_str
    from ..utils import (
        determine_ext,
        float_or_none,
        int_or_none,
        merge_dicts,
        NO_DEFAULT,
        orderedSet,
        parse_codecs,
        qualities,
        try_get,
        unified_timestamp,
        update_url_query,
        url_or_none,
        urljoin,
    )

    zdfie = ZDFIE(InfoExtractor)


# Generated at 2022-06-14 17:41:25.438469
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE.suitable(ZDFChannelIE._VALID_URL)
    ZDFChannelIE.suitable(ZDFIE._VALID_URL)
    assert not ZDFChannelIE.suitable(ZDFIE._VALID_URL)
    assert not ZDFChannelIE.suitable('https://www.zdf.de/politik/election-night-der-live-blog-100.html')


# Generated at 2022-06-14 17:41:28.383746
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zc = ZDFChannelIE()
    zc._VALID_URL = r'(?P<id>.+)'
    assert zc.suitable('https://www.zdf.de/serie/turnup')

# Generated at 2022-06-14 17:41:32.297781
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE("http://www.zdf.de/")
    assert ie.ie_key() == "ZDF"
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:41:38.371846
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    webpage = download_webpage(url, None)
    player = ZDFBaseIE._extract_player(webpage, url, fatal=False)
    channel_id = ZDFChannelIE._match_id(url)
    channel = ZDFBaseIE._call_api(
        'https://api.zdf.de/content/documents/%s.json' % channel_id,
        player, url, channel_id)
    items = []
    for module in channel['module']:
        for teaser in try_get(module, lambda x: x['teaser'], list) or []:
            t = try_get(
                teaser, lambda x: x['http://zdf.de/rels/target'], dict)
           

# Generated at 2022-06-14 17:41:50.700347
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'ZDF'
    assert ie.ie_key() == ZDFIE.ie_key()
    assert ie._VALID_URL == 'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'
    assert ie._TESTS[0]['url'] == 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    assert ie._TESTS[0]['md5'] == '34ec321e7eb34231fd88616c65c92db0'

# Generated at 2022-06-14 17:42:00.723389
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from youtube_dl.extractor import YoutubeDL
    ydl = YoutubeDL({'quiet': True})
    # Add the old constructor
    ZDFChannelIE.__init__(ZDFChannelIE, ydl)
    # Test ZDFChannelIE.suitable()
    assert ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/') is True
    assert ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html') is False

# Generated at 2022-06-14 17:44:13.228483
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf_ie = ZDFIE()
    assert zdf_ie._GEO_COUNTRIES == ['DE']
    assert zdf_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:44:19.979125
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'
    assert ie._TESTS[0]['url'] == 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    assert ie._TESTS[0]['md5'] == '34ec321e7eb34231fd88616c65c92db0'

# Generated at 2022-06-14 17:44:23.502156
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    instance = ZDFBaseIE()
    assert(instance._GEO_COUNTRIES == ['DE'])
    assert(instance._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'))


# Generated at 2022-06-14 17:44:24.763892
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfIE = ZDFIE()
    assert zdfIE != None


# Generated at 2022-06-14 17:44:29.816815
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE('www.zdf.com')
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:44:38.081134
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # pylint: disable=protected-access
    url_a = 'https://www.zdf.de/dokumentation/planet-e'
    url_b = 'https://www.zdf.de/dokumentation/planet-e.html'
    url_c = 'https://www.zdf.de/dokumentation/planet-e/'
    url_d = 'https://www.zdf.de/dokumentation/planet-e/test.html'
    result = ZDFChannelIE._match_id(url_a)
    assert result == 'planet-e'
    result = ZDFChannelIE._match_id(url_b)
    assert result == 'planet-e'
    result = ZDFChannelIE._match_id(url_c)
    assert result == 'planet-e'

# Generated at 2022-06-14 17:44:40.860570
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    return type('ZDFChannel', (object, ), {
        'suitable': staticmethod(lambda url: True)
    })().suitable('https://www.zdf.de/sendungen-a-z/alphabetische-liste-100.html')

# Generated at 2022-06-14 17:44:46.925999
# Unit test for constructor of class ZDFBaseIE

# Generated at 2022-06-14 17:44:48.028773
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()


# Generated at 2022-06-14 17:44:53.252633
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    info_extractor = zdfbase.ZDFBaseIE()
    assert info_extractor._GEO_COUNTRIES == ['DE']
    assert info_extractor._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

