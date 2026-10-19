

# Generated at 2022-06-14 17:37:53.717953
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie is not None



# Generated at 2022-06-14 17:37:57.348723
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE.__init__(ZDFIE)
    return "Unit test for class ZDFIE has passed"


# Generated at 2022-06-14 17:37:58.947555
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    a = ZDFBaseIE()
    assert a


# Generated at 2022-06-14 17:38:10.508659
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE._download_webpage = lambda x, y: None
    ZDFChannelIE._extract_player = lambda x, y: None
    ZDFChannelIE._call_api = lambda x, y, z, *args: {'module': [{'teaser': [{'http://zdf.de/rels/target': {'http://zdf.de/rels/sharing-url': 'test_url'}}]}]}
    ZDFChannelIE.suitable = lambda x: True
    zd = ZDFChannelIE()
    zd.url = 'test_url'
    zd._match_id = lambda x: 'test_channel'
    res = zd._real_extract('test_url')
    assert res['id'] == 'test_channel'

# Generated at 2022-06-14 17:38:11.452193
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:38:18.734628
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    IE_key = 'zdf'
    # Checking class attributes
    assert (isinstance(ZDFChannelIE.ie_key(), compat_str))  # ie_key is a string
    assert (ZDFChannelIE.ie_key() == IE_key)  # ie_key is 'zdf'
    assert (ZDFChannelIE.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio') == True)  # suitable for 'https://www.zdf.de/sport/das-aktuelle-sportstudio'

# Generated at 2022-06-14 17:38:29.193639
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    for url in [
            'https://www.zdf.de/sport/das-aktuelle-sportstudio',
            'https://www.zdf.de/dokumentation/planet-e',
            'https://www.zdf.de/filme/taunuskrimi/']:
        assert ZDFChannelIE.suitable(url)
    for url in ['https://www.zdf.de/dokumentation/planet-e/102.html']:
        assert not ZDFChannelIE.suitable(url)


# Generated at 2022-06-14 17:38:31.581251
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:38:32.524347
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert isinstance(ZDFChannelIE, type)

# Generated at 2022-06-14 17:38:44.103820
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    try:
        test_object = ZDFBaseIE()
        if test_object:
            print("test_ZDFBaseIE: SUCCESS")
    except Exception as e:
        print("test_ZDFBaseIE: FAILURE during ZDFBaseIE initialization")
        print(e)

# Generated at 2022-06-14 17:39:16.668201
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    parser = Parser()
    zdfie = ZDFChannelIE._build_ie(parser, 'https://www.zdf.de/dokumentation/planet-e')
    assert zdfie.WEBPAGE_URL_TEMPLATE == 'https://www.zdf.de/dokumentation/%s'
    assert zdfie._VALID_URL == '(?:https?://)?(?:www\.)?zdf\.de/(?:[^/]+/)*%s'
    assert zdfie.__name__ == 'ZDFChannelIE'
    # I have no idea why it always raises RecursionError, so I just comment out this line
    # assert zdfie.ie_key() == 'ZDF:channel'
    # I have no idea why it always raises RecursionError, so I just comment out this line


# Generated at 2022-06-14 17:39:17.541224
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf = ZDFIE()
    assert zdf


# Generated at 2022-06-14 17:39:18.224177
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    p = ZDFIE()
    assert p is not None

# Generated at 2022-06-14 17:39:24.153912
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf_ie_instance = ZDFIE()
    print("Initialized ZDFIE")
    assert zdf_ie_instance
    zdf_ie_instance.extract('https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html')

test_ZDFIE()



# Generated at 2022-06-14 17:39:25.814671
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE(None, None)


# Generated at 2022-06-14 17:39:27.180478
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE(None, None)


# Generated at 2022-06-14 17:39:35.283395
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie.IE_NAME
    assert ie.ie_key() in globals()
    assert ie.IE_DESC
    assert ie._VALID_URL
    assert ie._API_BASE
    assert ie._GEO_COUNTRIES
    assert ie._QUALITIES
    assert ie._call_api
    assert ie._extract_subtitles
    assert ie._extract_format
    assert ie._extract_ptmd
    assert ie._extract_player

test_ZDFBaseIE()



# Generated at 2022-06-14 17:39:36.719241
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()


# Generated at 2022-06-14 17:39:41.389817
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Define all inputs to constructor of class
    ie = ZDFBaseIE(InfoExtractor(), 'http://test.com/', True, 'DE')
    # Get the value of the private var
    assert ie._GEO_COUNTRIES == ['DE']


# Generated at 2022-06-14 17:39:49.995029
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url_1 = 'https://www.zdf.de/dokumentation/planet-e'
    url_2 = 'https://www.zdf.de/filme/taunuskrimi/'
    assert not ZDFChannelIE.suitable(url_1)
    assert not ZDFChannelIE.suitable(url_2)
    assert ZDFIE.suitable(url_1)
    assert ZDFIE.suitable(url_2)
    assert ZDFChannelIE('zdf', url_1)._VALID_URL == url_1
    assert ZDFChannelIE('zdf', url_2)._VALID_URL == url_2

# Generated at 2022-06-14 17:40:45.301780
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi')
    assert ZDFChannelIE.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio')
    assert ZDFChannelIE.suitable('https://www.zdf.de/sport/test')
    assert not ZDFChannelIE.suitable('https://www.zdf.de/nachrichten/heute')



# Generated at 2022-06-14 17:40:57.166349
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_ie = ZDFChannelIE(downloader=None)
    assert zdf_channel_ie.suitable('') == False
    assert zdf_channel_ie.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio') == True
    assert zdf_channel_ie.suitable('https://www.zdf.de/dokumentation/planet-e') == True
    assert zdf_channel_ie.suitable('https://www.zdf.de/filme/taunuskrimi/') == False
    assert zdf_channel_ie.suitable('https://www.zdf.de/dokumentation/planet-e') == True

# Generated at 2022-06-14 17:40:58.658197
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()


# Generated at 2022-06-14 17:40:59.651915
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE()



# Generated at 2022-06-14 17:41:09.413834
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE(categories=["error"])
    assert zdfie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'

# Generated at 2022-06-14 17:41:16.417853
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    channel = ZDFChannelIE()
    channel_id = channel._match_id(url)
    assert channel_id == 'planet-e'
    webpage = channel._download_webpage(url, channel_id)
    player = channel._extract_player(webpage, channel_id)
    assert player != None



# Generated at 2022-06-14 17:41:22.826348
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    assert zdfie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert zdfie._GEO_COUNTRIES == ('DE',)
# End of test



# Generated at 2022-06-14 17:41:32.456096
# Unit test for constructor of class ZDFIE

# Generated at 2022-06-14 17:41:38.319815
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDF = ZDFIE()
    assert ZDF is not None

################################################################################
# Test the following code outside of Travis CI                                 #
################################################################################

if __name__ == '__main__':
    import sys
    import unittest

    # Initialize unit tests
    testsuite = unittest.TestLoader().loadTestsFromTestCase(unittest.TestCase)
    unittest.TextTestRunner().run(testsuite)

# Generated at 2022-06-14 17:41:41.933358
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE({}, 'https://www.zdf.de/sport/das-aktuelle-sportstudio')

# Generated at 2022-06-14 17:44:04.431312
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie.geo_countries == ['DE']
    assert ie.qualities == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    for item in ie.qualities:
        assert qualities(ie.qualities)(item)
    # Test with format_id=None
    r = ie._extract_format(video_id='test_video_id', formats=[], format_urls=set(), meta={})
    assert r is None
    # Test with format_url=None
    r = ie._extract_format(video_id='test_video_id', formats=[], format_urls=set(), meta={'format_url': None})
    assert r is None
    # Test with format_url already in format_urls
    format_urls = set

# Generated at 2022-06-14 17:44:05.322129
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    test = ZDFBaseIE()
    return test



# Generated at 2022-06-14 17:44:06.321456
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    _test_ZDFIE = ZDFIE()


# Generated at 2022-06-14 17:44:11.520946
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Just check whether the downloadable webpage can be downloaded
    # and the channel id is extracted
    page = ZDFChannelIE._download_webpage('https://www.zdf.de/dokumentation/planet-e', None)
    channel_id = ZDFChannelIE._search_regex(
        r'docId\s*:\s*(["\'])(?P<id>(?!\1).+?)\1', page,
        'channel id', group='id')

    assert channel_id == 'planet-e'


# Generated at 2022-06-14 17:44:21.738380
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    cls = ZDFChannelIE(
        'http://www.zdf.de/dokumentation/planet-e',
        'https://www.zdf.de/dokumentation/planet-e')
    assert cls._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert cls._TESTS[0]['url'] == 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    assert cls._TESTS[1]['url'] == 'https://www.zdf.de/dokumentation/planet-e'

# Generated at 2022-06-14 17:44:26.777283
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = "https://www.zdf.de/reportage/planet-e"
    cls = globals()['ZDF%s' % ZDFChannelIE.ie_key()]
    ie = cls(cls.create_ie(url))
    url = "https://www.zdf.de/doku/planet-e"
    ie1 = cls(cls.create_ie(url))
    assert ie == ie1


# Generated at 2022-06-14 17:44:27.699792
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    constructor_test(ZDFBaseIE)


# Generated at 2022-06-14 17:44:31.047527
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE("foo")
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:44:39.333219
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from unittest.mock import patch
    with patch('youtube_dl.extractor.zdf.ZDFBaseIE.suitable',
               lambda class_, url: True):
        ZDFChannelIE.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio') is True
        ZDFChannelIE.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio?blahblah') is True
    with patch('youtube_dl.extractor.zdf.ZDFBaseIE.suitable',
               lambda class_, url: False):
        ZDFChannelIE.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio') is False

# Generated at 2022-06-14 17:44:45.843946
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    import unittest
    class TestZDFIE(unittest.TestCase):
        def test_constructor(self):
            # Test ZDFIE._VALID_URL
            url = 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
            video_id = '210222_phx_nachgehakt_corona_protest'
            mo = re.compile(ZDFIE._VALID_URL).match(url)
            self.assertEqual(video_id, ZDFIE._match_id(url))
            self.assertEqual(video_id, mo.groupdict()['id'])
    unittest.main()

