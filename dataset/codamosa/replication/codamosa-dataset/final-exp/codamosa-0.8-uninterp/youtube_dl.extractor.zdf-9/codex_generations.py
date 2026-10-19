

# Generated at 2022-06-14 17:37:54.224506
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannel = ZDFChannelIE()
    assert zdfChannel._VALID_URL is not None

# Generated at 2022-06-14 17:37:56.892876
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 17:38:08.537415
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from .test_downloader import FakeYDL
    with FakeYDL({'logger': my_fake_logger}) as ydl:
        ydl.add_info_extractor(ZDFChannelIE.ie_key())
        ydl.add_info_extractor(ZDFIE.ie_key())
        ydl.download(['https://www.zdf.de/politik/frontal-21/frontal-21-100.html'])
        extracted_info = ydl.extracted_info.copy()
        extracted_info['entries'] = []
        extracted_info['playlist'] = extracted_info['id']

# Generated at 2022-06-14 17:38:20.323933
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE(None)

# Generated at 2022-06-14 17:38:23.512568
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    zdfie.ie_key()



# Generated at 2022-06-14 17:38:27.436841
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Since ZDFIE is a class, we are testing
    # if ZDF_ie = ZDFIE() works
    ZDF_ie = ZDFIE()
    assert(ZDF_ie)


# Generated at 2022-06-14 17:38:32.591565
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdfBaseIE = ZDFBaseIE()
    assert zdfBaseIE._GEO_COUNTRIES == ['DE']
    assert zdfBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:38:34.231104
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE.__name__ == 'ZDFBaseIE'


# Generated at 2022-06-14 17:38:35.321824
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_zdf = ZDFBaseIE()

# Generated at 2022-06-14 17:38:36.600274
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:39:13.258378
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():

    class ZDFBaseIETestIE(ZDFBaseIE):
        _VALID_URL = r'https?://(?:www\.)?'
        IE_NAME = 'unit test for ZDFBaseIE: ' + _VALID_URL

        _TEST = {
            'url': 'http://unit.test/url',
            'info_dict': {
                'id': 'url',
            }
        }

    ie = ZDFBaseIETestIE()
    yield (ie.suitable, 'http://unit.test/url')
    yield (ie.suitable, 'http://unit.test/url/')
    yield (ie.suitable, 'http://www.unit.test/url')
    yield (ie.suitable, 'http://www.unit.test/url/')

# Generated at 2022-06-14 17:39:14.881316
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert isinstance(ZDFBaseIE("ZDFBaseIE"), InfoExtractor)



# Generated at 2022-06-14 17:39:15.882015
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE._check_call_api()

# Generated at 2022-06-14 17:39:18.224248
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # make sure that ZDFIE instantiation doesn't fail
    ZDFIE('https://www.zdf.de/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html')

# Generated at 2022-06-14 17:39:26.174553
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():

    # Test for when content-type is 'application/x-mpegURL' or ext is 'm3u8'
    info = ZDFBaseIE._extract_format(
            '150918_dokukanal_zeit',
            [],
            set(),
            {
                'url': 'https://zdf0616-a.akamaihd.net/n/deDE/edge/video/161014/739029_mediathek_lq_m3u8-aac_1546k-aac_0_vh.m3u8',
                'mimeType': 'application/x-mpegURL',
                'quality': 'veryhigh'
            })

# Generated at 2022-06-14 17:39:33.565564
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE()._GEO_COUNTRIES == ['DE']
    assert ZDFBaseIE()._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert callable(ZDFBaseIE()._extract_subtitles)
    assert callable(ZDFBaseIE()._extract_format)
    assert callable(ZDFBaseIE()._extract_ptmd)
    assert callable(ZDFBaseIE()._extract_player)



# Generated at 2022-06-14 17:39:38.640780
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # try to extract from a URL that is not related to zdf.de
    zdfie = ZDFIE()
    with pytest.raises(RegexNotFoundError):
        zdfie._real_extract(r'https://www.phoenix.de/sendungen/ereignisse/corona-nachgehakt.html')



# Generated at 2022-06-14 17:39:39.807936
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE()
    return True


# Generated at 2022-06-14 17:39:45.513146
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # This is a test for instance creation of class ZDFIE
    ie = ZDFIE()
    assert ZDFIE.ie_key() == 'ZDF'
    #assert er instanceof InfoExtractor
    assert type(ie) == type(InfoExtractor())
    assert ie.ie_key() == 'ZDF'




# Generated at 2022-06-14 17:39:53.836201
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Test case 1
    meta = {
        'format': 'mp4',
        'quality': 'hd',
        'quality_type': 'high',
        'autoselect': True,
        'filename': 'test1',
        'codecs': 'avc1.4d401e',
        'url': 'http://test1'
    }
    fmtd_meta = ZDFBaseIE._extract_format('test', [], set(), meta)
    assert len(fmtd_meta) == len(meta) and meta['url'] == fmtd_meta[0]['url']

    # Test case 2

# Generated at 2022-06-14 17:40:53.339751
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannelIE = ZDFChannelIE('zdf.de', 'https://www.zdf.de/dokumentation/planet-e')
    assert zdfChannelIE.ie_key() == 'ZDFChannel'

# Generated at 2022-06-14 17:40:57.716656
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert ie.suitable('https://www.zdf.de/dokumentation/planet-e/')
    assert ie.suitable('https://www.zdf.de/dokumentation/planet-e/Planet-e-übersichtsseite-weitere-Dokumentationen-von-Planet-e-100.html')
    assert not ie.suitable('https://www.zdf.de/dokumentation/planet-e/Die-Magie-der-Farben-2-2-100.html')

# Generated at 2022-06-14 17:41:02.495578
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    try:
        test = ZDFIE()
        test._download_webpage(test._VALID_URL, 'test_id')
    except Exception as e:
        print(e)
        return False
    return True

if __name__ == '__main__':
    print('Unit test results of class ZDFIE:')
    print(test_ZDFIE())

# Generated at 2022-06-14 17:41:04.500229
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_ie = ZDFChannelIE()
    assert zdf_channel_ie is not None


# Generated at 2022-06-14 17:41:16.772110
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    cases = [
        # Valid
        ('https://www.zdf.de/dokumentation/planet-e', True),
        ('https://www.zdf.de', False),

        # Invalid - a channel URL redirects to another URL
        ('https://www.zdf.de/politik/phoenix-sendungen', False),

        # Invalid - a channel URL redirects to a video URL
        ('https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html', False),
    ]

    ie = ZDFChannelIE()
    for url, result in cases:
        assert(ie.suitable(url) == result)

# Generated at 2022-06-14 17:41:21.524403
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE(): #
    ie = ZDFBaseIE()
    countries = ie._GEO_COUNTRIES
    assert countries == ['DE'], "Wrong ZDFBaseIE._GEO_COUNTRIES"
    qualities = ie._QUALITIES
    assert qualities == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'), "Wrong ZDFBaseIE._QUALITIES"
# end unit test



# Generated at 2022-06-14 17:41:24.480563
# Unit test for constructor of class ZDFIE
def test_ZDFIE():

    print(ZDFIE._TESTS[0])
    zdfie = ZDFIE.ie_key()
    print(zdfie)


# Generated at 2022-06-14 17:41:33.564533
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.__class__.__name__ == 'ZDFIE'
    assert ie.ie_key() == 'ZDF'
    assert ie.server_site() == 'zdf.de'
    assert ie._VALID_URL == 'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'

# Generated at 2022-06-14 17:41:35.716525
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE(ZDFIE.ie_key())
    assert ie.SUITABLE(ZDFChannelIE._VALID_URL)
    assert not ie.SUITABLE(ZDFIE._VALID_URL)



# Generated at 2022-06-14 17:41:48.011159
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e')
    ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e/')
    ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e#')
    ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e?')
    ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e/?')
    ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e/#')

# Generated at 2022-06-14 17:44:24.825521
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    class MockZDFChannelIE(ZDFChannelIE):
        def _download_json(self, url_or_request, video_id, note=''):
            class MockResult:
                def __init__(self, data):
                    self.data = data

# Generated at 2022-06-14 17:44:32.172750
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = "https://www.zdf.de/dokumentation/planet-e"
    # should return ZDFChannelIE itself
    assert ZDFChannelIE.suitable(url)
    ie = ZDFChannelIE()
    # should return ZDFChannelIE.ie_key()
    assert ie.suitable(url)
    assert ie.ie_key() == 'ZDFChannel'
    # should return False
    assert not ZDFIE.suitable(url)

# Generated at 2022-06-14 17:44:34.467657
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannelIE = ZDFChannelIE()
    assert zdfChannelIE.suitable(ZDFChannelIE._VALID_URL) == True


# Generated at 2022-06-14 17:44:43.109138
# Unit test for constructor of class ZDFChannelIE

# Generated at 2022-06-14 17:44:44.380181
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE("ZDFIE")



# Generated at 2022-06-14 17:44:47.921994
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE.ie_key() == 'zdf'
    # assert ZDFBaseIE.ie_key() == 'ZDFBaseIE'


# Generated at 2022-06-14 17:44:59.729177
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    player = {'config': {
        'playerConfig': {
            'config': {'content': {
                'videoId': 'S00123456',
                'apiUrl': 'https://vod-api-nocdn.zdf.de/api/v1/video/S00123456',
                'httpStreamingUrl': 'https://daserste-vod.zdf.de/S00123456',
            }}
        }
    }}
    video_id = 'S00123456'
    ext = ZDFBaseIE()
    assert ext.is_logged() == True
    assert ext.is_geo_restricted() == True
    assert ext._GEO_COUNTRIES == ['DE']

# Generated at 2022-06-14 17:45:06.761964
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Unit test for ZDFChannelIE.suitable
    assert not ZDFChannelIE.suitable('https://zdf.de/dokumentation/planet-e')
    assert ZDFChannelIE.suitable('https://zdf.de/dokumentation')

    # Unit test for ZDFChannelIE._real_extract
    zdfChannelIE = ZDFChannelIE('https://zdf.de/dokumentation/planet-e')
    assert zdfChannelIE._real_extract('https://zdf.de/dokumentation/planet-e')

# Generated at 2022-06-14 17:45:10.376604
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    z = ZDFIE()
    assert z
    assert z._GEO_COUNTRIES == ['DE']
    assert z._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:45:20.055051
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf = ZDFIE()
    zdf_valid_url = zdf._VALID_URL
    zdf_valid_url_match = zdf._VALID_URL_MATCH = re.compile(zdf_valid_url).match
    zdf_match_id = zdf._match_id('https://www.zdf.de/service-und-hilfe/die-neue-zdf-mediathek/zdfmediathek-trailer-100.html')
    assert zdf_match_id == 'zdfmediathek-trailer'
