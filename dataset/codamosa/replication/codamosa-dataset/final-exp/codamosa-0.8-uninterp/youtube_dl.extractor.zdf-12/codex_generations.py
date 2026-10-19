

# Generated at 2022-06-14 17:38:06.398436
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from .test import get_testcases
    from .zdf import ZDFIE

    # Not using .json suffix, but using .html suffix
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    webpage = get_testcases()[url]
    player = ZDFChannelIE._extract_player(webpage, url)
    assert player

    # Not using .json suffix, but not using .html suffix
    url = 'https://www.zdf.de/politik/phoenix-sendungen'
    webpage = get_testcases()[url]
    player = ZDFChannelIE._extract_player(webpage, url)
    assert player

    # Using .json suffix, and using .html suffix

# Generated at 2022-06-14 17:38:19.096063
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf_ie = ZDFIE()
    zdf_ie.suitable('https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html')
    # don't extract live video - not implemented
    zdf_ie.suitable('https://www.zdf.de/nachrichten/heute-live/heute-live-100.live.html')
    # don't extract podcast - not implemented
    zdf_ie.suitable('https://www.zdf.de/kultur/morgenmagazin/podcast-morgenmagazin-vom-2-september-2020-104.html')
    # don't extract tv show - not implemented
    zdf

# Generated at 2022-06-14 17:38:20.215350
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    l = ZDFBaseIE()
    return l
#

# Generated at 2022-06-14 17:38:30.317297
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfchannel_ie = ZDFChannelIE()
    assert zdfchannel_ie.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert zdfchannel_ie.suitable('https://www.zdf.de/filme/taunuskrimi/')
    assert not zdfchannel_ie.suitable('https://zdf.de/filme/treffpunkt-flughafen/treffpunkt-flughafen-0709-100.html')


# Generated at 2022-06-14 17:38:40.959116
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Function to test if an instance of a class is constructed as expected
    def test_constructor(cls):
        instance = cls()
        assert hasattr(instance, '_GEO_COUNTRIES')
        assert hasattr(instance, '_TESTS')
        assert isinstance(instance._TESTS, list)
        i = 0
        for entry in instance._TESTS:
            assert isinstance(entry, dict)
            for key, value in entry.items():
                if key == 'md5':
                    assert re.match(r'[0-9a-f]{32}', value)
                elif key == 'info_dict':
                    assert isinstance(value, dict)

# Generated at 2022-06-14 17:38:47.039539
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Test 1: an url presenting a ZDF channel
    url = 'https://www.zdf.de/service-und-hilfe/die-neue-zdf-mediathek/zdfmediathek-trailer-100.html'
    zdf_channel_ie = ZDFChannelIE()
    extractor = zdf_channel_ie.suitable(url)
    assert_true(extractor)
    # Test 2: an url presenting a ZDF channel
    url = 'https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html'
    zdf_channel_ie = ZDFChannelIE()
    extractor = zdf_channel_ie.suitable(url)

# Generated at 2022-06-14 17:38:59.037441
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf_base_ie = ZDFBaseIE()
    zdf_base_ie._call_api(
        'https://', 'id', 'item', api_token='api_token', referrer='referer')
    zdf_base_ie._extract_subtitles(None)
    zdf_base_ie._extract_format(
        'id', [], set(),
        {'url': 'http://', 'mimeType': 'application/x-mpegURL'})
    zdf_base_ie._extract_format(
        'id', [], set(),
        {'url': 'http://', 'mimeType': 'application/f4m+xml'})

# Generated at 2022-06-14 17:39:02.911699
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert type(ZDFBaseIE) == type



# Generated at 2022-06-14 17:39:03.742374
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ins = ZDFIE();
    assert(ins is not None)


# Generated at 2022-06-14 17:39:09.287000
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    base_ie = ZDFBaseIE(None)
    assert base_ie._GEO_COUNTRIES == ['DE']
    assert base_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

# The following def is for testing class method _extract_subtitles.

# Generated at 2022-06-14 17:39:58.800872
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    test = ZDFIE()
    assert(test.ie_key() == 'ZDF')
    assert(test.ie_key() != 'zdf')


# Generated at 2022-06-14 17:39:59.873403
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:40:13.452246
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()

    # Real world test for _VALID_URL of class ZDFIE
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'

    # Real world test for _TESTS of class ZDFIE

# Generated at 2022-06-14 17:40:20.823788
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from .test_zdf_playlist import ZDFPlaylistIE
    from .test_zdf import ZDFIE
    import unittest

    class ZDFChannelTest(unittest.TestCase):
        def setUp(self):
            self.ie = ZDFChannelIE({})

        def test_ZDFPlaylistIE(self):
            self.assertIsInstance(ZDFPlaylistIE.suitable(None), compat_str)
            self.assertTrue(ZDFPlaylistIE.suitable('https://www.zdf.de/dokumentation/planet-e'))

        def test_ZDFIE(self):
            self.assertIsInstance(ZDFIE.suitable(None), compat_str)

# Generated at 2022-06-14 17:40:28.649194
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    url = 'http://zdf.de/ZDFmediathek/beitrag/video/2343008/Aus-f%C3%BCr-den-Moloch'
    video_id = '10192676'
    headers = {
        'Api-Auth': 'Bearer access_token'
    }
    base_ie = ZDFBaseIE()
    ie = base_ie._call_api(url, video_id, 'Aus-f%C3%BCr-den-Moloch', api_token='access_token')
    assert ie is not None


# Generated at 2022-06-14 17:40:33.437732
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    z = ZDFBaseIE()
    z._call_api('http://a', 'b', 'c')
    z._extract_subtitles({'captions': '{}'})
    z._extract_format('b', '{}', '{}', '{}')
    z._extract_ptmd('http://a', 'b', 'c', 'd')
    z._extract_player('a', 'b')


# Generated at 2022-06-14 17:40:42.193114
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdchannel = ZDFChannelIE()
    expected_urls = [
        'https://www.zdf.de/filme/filme-sonstige/der-hauptmann-112.html',
        'https://www.zdf.de/wissen/nano/nano-21-mai-2019-102.html',
        'https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html',
    ]
    for i, url in enumerate(expected_urls):
        assert zdchannel.suitable(url)
        zdchannel._real_extract(url)
        assert zdchannel.urls_to_extract[i] in expected_

# Generated at 2022-06-14 17:40:44.671354
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_ie = ZDFChannelIE('https://www.zdf.de/service-und-hilfe/die-neue-zdf-mediathek'
                                '/zdfmediathek-trailer-100.html')
    print(zdf_channel_ie)

# Generated at 2022-06-14 17:40:53.944285
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.suitable('https://www.zdf.de/dokumentation/planet-e') == True
    assert ie.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html') == False
    assert ie.suitable('http://www.zdf.de/filme/interaktiv-fruehstuecksfernsehen-vom-12-maerz-2016-100.html') == False

# Generated at 2022-06-14 17:40:58.974637
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    extractor = ZDFIE()
    # ZDFBaseIE
    assert extractor._GEO_COUNTRIES == ['DE']
    assert extractor._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    # ZDFIE
    assert extractor._VALID_URL == ZDFIE._VALID_URL
    assert extractor._TESTS == ZDFIE._TESTS


# Generated at 2022-06-14 17:42:55.097288
# Unit test for constructor of class ZDFBaseIE

# Generated at 2022-06-14 17:42:57.766344
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.suitable('https://www.zdf.de/dokumentation/planet-e')



# Generated at 2022-06-14 17:43:01.099199
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.IE_NAME == 'ZDF'
    assert ie._VALID_URL == ZDFChannelIE._VALID_URL
    assert ie.__name__ == 'ZDFChannelIE'
    assert hasattr(ie, '_real_extract')


# Generated at 2022-06-14 17:43:04.899150
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    _constructor = ZDFBaseIE
    assert ZDFBaseIE._GEO_COUNTRIES == ['DE']
    assert ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:43:05.657678
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    pass

# Generated at 2022-06-14 17:43:10.005799
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.GEO_COUNTRIES == ['DE']
    assert ie.QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

# Generated at 2022-06-14 17:43:14.384624
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """Test constructor of class ZDFChannelIE."""
    def suitable(cls, url):
        return True
    ZDFChannelIE._suitable = classmethod(suitable)

    # ZDFIE overrides ZDFBaseIE -> ZDFChannelIE
    ZDFChannelIE.suitable = ZDFIE.suitable
    ZDFChannelIE.ie_key = ZDFIE.ie_key

    ie = ZDFChannelIE(None)
    assert ie.name == 'ZDF'
    assert ie.description == ie.ie_key() + ' (' + ZDFIE.ie_key() + ')'
    assert ie.age_limit == 18

    # ZDFBaseIE overrides CommonIE -> YoutubeIE
    assert ie.working == False
    assert ie.report_working == False

# Generated at 2022-06-14 17:43:21.696732
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFBaseIE()._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+\.html)'
    assert ZDFChannelIE()._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    with pytest.raises(AttributeError) as excinfo:
        ZDFChannelIE()._VALID_URL = r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert str(excinfo.value) == "'ZDFChannelIE' object attribute '_VALID_URL' is read-only"



# Generated at 2022-06-14 17:43:29.505750
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    p = ZDFChannelIE('https://www.zdf.de/dokumentation/planet-e')
    assert [
        x['url']
        for x in p._entries
        if x.get('url') == 'https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html'
    ]



# Generated at 2022-06-14 17:43:31.041797
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Test that the constructor of class ZDFBaseIE doesn't throw any exception
    ie = ZDFBaseIE()



# Generated at 2022-06-14 17:45:41.465954
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE()

# Generated at 2022-06-14 17:45:45.614427
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE('ask.fm')
    assert ie.GEO_BYPASS
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:45:48.184768
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE('https://www.zdf.de/filme/taunuskrimi/')


# Generated at 2022-06-14 17:45:51.003578
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # check whether the constructor is able to handle the case that a videoID is given as argument
    videoID = '1234'
    ZDFIE(None, videoID)


# Generated at 2022-06-14 17:45:52.978163
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # create ZDFChannelIE instance
    ie = ZDFChannelIE()
    # verify class type
    assert ie.is_class()

# Generated at 2022-06-14 17:45:53.505043
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE()

# Generated at 2022-06-14 17:45:57.674330
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    channel_ie = ZDFChannelIE()
    assert channel_ie.suitable('https://www.zdf.de/dokumentation/planet-e')
    # fail in case of suitable
    assert not ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html')

# Generated at 2022-06-14 17:45:58.611861
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE(InfoExtractor())


# Generated at 2022-06-14 17:45:59.353945
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:46:01.446142
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = "https://www.zdf.de/dokumentation/planet-e"
    assert ZDFChannelIE.suitable(url)
    zdfChannelIE = ZDFChannelIE()
    assert zdfChannelIE._real_extract(url)