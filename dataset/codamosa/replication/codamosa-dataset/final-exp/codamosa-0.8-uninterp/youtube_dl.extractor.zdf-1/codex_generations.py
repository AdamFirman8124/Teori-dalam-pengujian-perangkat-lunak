

# Generated at 2022-06-14 17:38:06.361913
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    import unittest
    import inspect
    from .dummy import DummyIE

    class TestZDFChannelIE(unittest.TestCase, DummyIE):
        url = 'https://www.zdf.de/politik/phoenix-sendungen'
        module = ZDFChannelIE
        expected_title = 'Phoenix'

        def setUp(self):
            self.assertTrue(hasattr(self.module, 'suitable'), 'suitable method is missing')

        def test_classes_suitable(self):
            clazzes = [getattr(self.module, n) for n in dir(self.module)
                       if isinstance(getattr(self.module, n), type) and issubclass(getattr(self.module, n), InfoExtractor)]

# Generated at 2022-06-14 17:38:13.572284
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """
    Unit test for testing ZDFChannelIE
    """
    ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/terra-x')

zdf_url_result = namedtuple(
    'zdf_url_result',
    ['url', 'ie_key', 'video_id', 'video_data'])

# Generated at 2022-06-14 17:38:16.090232
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    cls = type('ZDFIE', (ZDFIE,), {})
    instance = cls()
    assert instance


# Generated at 2022-06-14 17:38:25.172212
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    channel_url = 'https://www.zdf.de/politik/phoenix-sendungen'
    item_url = 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    expected_video_id = '210222_phx_nachgehakt_corona_protest'
    zdfchannelie = ZDFChannelIE()
    assert zdfchannelie.suitable(channel_url)
    assert zdfchannelie.suitable(item_url)
    assert expected_video_id == zdfchannelie._extract_video_id(item_url)
    assert not zdfchannelie.suitable('https://www.zdf.de')


# Generated at 2022-06-14 17:38:32.308777
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdfie = ZDFBaseIE("http://www.zdf.de/ZDFmediathek/hauptnavigation/politik/politik-aktuell/280598?in=zdf-fernsehen")

    assert zdfie._GEO_COUNTRIES == ['DE']
    assert zdfie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

# Generated at 2022-06-14 17:38:33.919688
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    obj = ZDFIE



# Generated at 2022-06-14 17:38:41.585206
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE('dummy')
    ie.suitable('http://www.zdf.de/dokumentation/planet-e')
    ie.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html')
    ie.suitable('https://www.zdf.de/dokumentation/planet-e')

# Generated at 2022-06-14 17:38:45.931197
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    test_cases = [
        u'http://www.zdf.de/dokumentation/planet-e',
        u'https://www.zdf.de/sport/das-aktuelle-sportstudio',
    ]
    for test_case in test_cases:
        yield check_valid_channel, test_case


# Generated at 2022-06-14 17:38:56.971668
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    try:
        input_ = dict(extractor_key=ZDFIE.ie_key(),
                      id='foo',
                      duration='bar',
                      formats='baz',
                      subtitles='qux')
        v = ZDFBaseIE(**input_)

        # Verify all instance attributes have been set correctly
        assert v.extractor_key == 'ZDF'
        assert v.id == 'foo'
        assert v.duration == 'bar'
        assert v.formats == 'baz'
        assert v.subtitles == 'qux'
    except AssertionError as e:
        raise AssertionError(str(e) + '\nUnit test for constructor of class ZDFBaseIE failed.')
    else:
        print('Unit test for constructor of class ZDFBaseIE passed.')


# Generated at 2022-06-14 17:38:59.859837
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    channel = ZDFChannelIE("https://www.zdf.de/sport/das-aktuelle-sportstudio")
    assert channel.channel_id == "das-aktuelle-sportstudio"



# Generated at 2022-06-14 17:39:46.889701
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    channel = ZDFChannelIE()
    channel._real_initialize()


# Generated at 2022-06-14 17:39:48.190865
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf_base_ie = ZDFBaseIE()



# Generated at 2022-06-14 17:39:49.467095
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE().ie_key() == ZDFIE.ie_key()


# Generated at 2022-06-14 17:39:57.249194
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES is not None
    assert ie._QUALITIES is not None
    assert ie._call_api() is None
    assert ie._extract_subtitles() is not None
    assert ie._extract_format() is None
    assert ie._extract_ptmd() is None
    assert ie._extract_player() is None
    


# Generated at 2022-06-14 17:39:59.245996
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    class TestZDFBaseIE(ZDFBaseIE):
        ie_key = 'testZDFBaseIE'
        def _real_extract(self, url):
            pass

    assert TestZDFBaseIE().ie_key() == 'testZDFBaseIE'


# Generated at 2022-06-14 17:40:04.176970
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:40:14.965333
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf = ZDFBaseIE('test', {}, 'test')
    assert zdf._GEO_COUNTRIES is not None
    assert zdf._QUALITIES is not None

    assert zdf._call_api('test', 'test', 'test') is not None
    assert zdf._extract_subtitles({'captions': 'test'}) is not None

    formats, track_uris = [], set()
    zdf._extract_format('test', formats, track_uris, {'url': 'test'})
    assert formats

    assert zdf._extract_ptmd('test', 'test', 'test', 'test') is not None
    assert zdf._extract_player('test', 'test') is not None



# Generated at 2022-06-14 17:40:17.679030
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE('http://www.zdf.de/sport/das-aktuelle-sportstudio')
    assert ie.channel_id == u'das-aktuelle-sportstudio'



# Generated at 2022-06-14 17:40:27.879485
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    """
    Constructor test case of class ZDFBaseIE
    """
    # Set class attributes to specific values as temporal result
    ZDFBaseIE._GEO_COUNTRIES = ['DE', 'AT', 'CH']
    ZDFBaseIE._QUALITIES = ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

    assert ZDFBaseIE._GEO_COUNTRIES == ['DE', 'AT', 'CH']
    assert ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:40:29.130559
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Test class is being constructed without errors
    ZDFBaseIE()


# Generated at 2022-06-14 17:42:08.367502
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE(' ')
    assert ie.name == 'ZDF'
    assert ie.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:42:13.331580
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    class TestZDFBaseIE(ZDFBaseIE):
        _VALID_URL = r'.*'
        IE_NAME = 'test'
        _TEST = {
            'url': 'http://ich.zdf.de',
            'info_dict': {
                'name': 'test',
            },
        }
    ie = TestZDFBaseIE()
    assert ie.ie_key() == 'ZDFBase'



# Generated at 2022-06-14 17:42:18.310657
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE.suitable('https://www.zdf.de/serien/tatort')
    assert not ZDFChannelIE.suitable('https://www.zdf.de/babylotse')


# Generated at 2022-06-14 17:42:19.268157
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()

# Generated at 2022-06-14 17:42:21.410499
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    tester = ZDFBaseIE()
    assert tester is not None


# Generated at 2022-06-14 17:42:33.636643
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    from .common import Environment
    from .zdfbase import ZDFBaseIE
    from .zdf import ZDFIE

    env = Environment()
    zdf_ie = ZDFIE()
    zdf_base_ie = ZDFBaseIE()
    env.register_ie(ZDFBaseIE.ie_key(), zdf_base_ie)
    env.register_ie(ZDFIE.ie_key(), zdf_ie)

    assert zdf_ie.suitable('https://www.zdf.de/comedy/die-anstalt/video-die-anstalt-vom-27-maerz-2019-100.html')

# Generated at 2022-06-14 17:42:34.841118
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE(None)


# Generated at 2022-06-14 17:42:37.176706
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.__class__ == ZDFIE


# Generated at 2022-06-14 17:42:38.705153
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()

# Generated at 2022-06-14 17:42:47.362418
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    ie = ZDFChannelIE()
    obj = ie._real_initialize()
    assert obj is ie
    assert ie.suitable(url) is True
    assert ie.IE_NAME == 'ZDF:channel'
    assert ie.IE_DESC == 'ZDF: channel'
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 17:47:24.365875
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    try:
        construct = ZDFBaseIE('test', 'test')
        assert isinstance(construct, InfoExtractor)
    except:
        raise AssertionError('expected a InfoExtractor, but got a false.')
    return
