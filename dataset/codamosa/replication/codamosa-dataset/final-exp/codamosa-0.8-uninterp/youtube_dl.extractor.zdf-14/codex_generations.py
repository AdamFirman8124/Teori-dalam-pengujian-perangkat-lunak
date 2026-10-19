

# Generated at 2022-06-14 17:37:58.584397
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # test constructor with video id
    videoID = '35218002'
    ZDFBaseIE(videoID)
    ZDFBaseIE(compat_str(videoID))

    # test constructor with url
    url = "https://www.zdf.de/politik/frontal-21/frontal21-vom-4-dezember-2018-100.html"
    ZDFBaseIE(url)
    ZDFBaseIE(compat_str(url))


# Generated at 2022-06-14 17:38:01.987146
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE._GEO_COUNTRIES == ['DE']
    assert ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

# Generated at 2022-06-14 17:38:14.654795
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._call_api('url', 'v_id', 'item', 'api_token', 'referrer')

    assert ie._extract_subtitles({}) == {}

    src = {
        'captions': [
            {
                'uri': 'subtitle_url',
                'language': 'deu',
            }
        ]
    }
    assert ie._extract_subtitles(src) == {
        'deu': [{'url': 'subtitle_url'}]
    }

    formats = []
    format_urls = set()
    meta = {
        'url': 'format_url',
        'mimeType': 'application/f4m+xml',
    }

# Generated at 2022-06-14 17:38:16.656910
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE is not None, "Something went wrong with constructor of class ZDFBaseIE"


# Generated at 2022-06-14 17:38:22.703172
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert hasattr(ZDFBaseIE, '_GEO_COUNTRIES')
    assert hasattr(ZDFBaseIE, '_QUALITIES')
    assert hasattr(ZDFBaseIE, '_call_api')
    assert hasattr(ZDFBaseIE, '_extract_subtitles')
    assert hasattr(ZDFBaseIE, '_extract_format')
    assert hasattr(ZDFBaseIE, '_extract_ptmd')
    assert hasattr(ZDFBaseIE, '_extract_player')


# Generated at 2022-06-14 17:38:35.301718
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    from .test_utils import run_test_cases
    test_cases = [{
        'url': 'https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html',
        'info_dict': {
            'id': '151025_magie_farben2_tex',
            'ext': 'mp4',
            'title': 'Die Magie der Farben (2/2)',
            'description': 'md5:a89da10c928c6235401066b60a6d5c1a',
            'duration': 2615,
            'timestamp': 1465021200,
            'upload_date': '20160604',
        },
    }]


# Generated at 2022-06-14 17:38:46.479864
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf_base = ZDFBaseIE()

    video_id = '58d04441'
    geo_countries = zdf_base._GEO_COUNTRIES
    qualities = zdf_base._QUALITIES
    ptmd_url = 'https://api.zdf.de/content/documents/zdf/2.184/25gqh6k4/v9pjv4kx/58d04441/?profile=player-v1-hbbtv-hls-h264-aac&apiToken=bearer.2.2184.25gqh6k4.v9pjv4kx.58d04441.ZmYzNjE1MmU5ODJhMDVkNjRkNGE2MGU0MTRiYWZlYmE='
   

# Generated at 2022-06-14 17:38:50.034537
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'ZDF'
    assert ie.info()['title'] == 'ZDF'


# Generated at 2022-06-14 17:38:54.213364
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    base = ZDFBaseIE()
    assert base._GEO_COUNTRIES == ['DE']
    assert base._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:38:55.458467
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert 'ZDFBaseIE' == ZDFBaseIE.__name__


# Generated at 2022-06-14 17:39:22.542685
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    instance = ZDFIE()
    assert instance._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'


# Generated at 2022-06-14 17:39:30.424050
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    test_values = [
        "https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html",
        "https://www.zdf.de/dokumentation/planet-e/planet-e-uebersichtsseite-weitere-dokumentationen-von-planet-e-100.html",
    ]

    for test_value in test_values:
        ie = ZDFIE.ie_key()
        assert(ie in ZDFIE._ies)
        print(ie)
        instance = ZDFIE._ies[ie](test_value)
        assert(instance._VALID_URL == ZDFIE._VALID_URL)


# Generated at 2022-06-14 17:39:33.117678
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdf_ie = ZDFIE()
    assert zdf_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:39:38.622689
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    try:
        for extractor in (ZDFIE, ZDFChannelIE):
            ZDFBaseIE(extractor.ie_key(), extractor.ie_key())
            test_ZDFBaseIE.test_passed = True
    except:
        test_ZDFBaseIE.test_passed = False
test_ZDFBaseIE.test_passed = False



# Generated at 2022-06-14 17:39:42.939761
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    zdf_channel_ie = ZDFChannelIE()
    assert zdf_channel_ie.suitable(url) == True


# Generated at 2022-06-14 17:39:43.359473
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    pass


# Generated at 2022-06-14 17:39:46.998106
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    t = ZDFIE()
    assert t._GEO_COUNTRIES == ['DE']
    assert len(t._QUALITIES) == 6
    assert t._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'



# Generated at 2022-06-14 17:39:51.033433
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Smoke test for the constructor of class ZDFBaseIE
    i = ZDFBaseIE()
    assert hasattr(i, '_call_api')
    assert hasattr(i, '_extract_subtitles')
    assert hasattr(i, '_extract_format')
    assert hasattr(i, '_extract_ptmd')
    assert hasattr(i, '_extract_player')


# Generated at 2022-06-14 17:39:53.154455
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert(ZDFBaseIE._GEO_COUNTRIES == ['DE'])
    assert(ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'))


# Generated at 2022-06-14 17:39:56.709684
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    ie = ZDFChannelIE(url)
    assert ie.suitable(url)
    assert ie.extractor.suitable(url)
    assert not ie.suitable(ZDFBaseIE(url)._VALID_URL)
    assert not ie.extractor.suitable(ZDFBaseIE(url)._VALID_URL)

# Generated at 2022-06-14 17:40:48.784836
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    return ZDFIE(InfoExtractor()).ie_key()



# Generated at 2022-06-14 17:40:54.914191
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE('ZDF', 'DE')
    assert ie.ie_key() == 'ZDF'
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Base class for ZDF and ZDFMediathek

# Generated at 2022-06-14 17:41:02.374877
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """
    Unit test for constructor of class ZDFChannelIE
    """

    extractor = ZDFChannelIE()
    assert 'zdf.de' in extractor._VALID_URL
    assert 'zdf.de' in extractor._TESTS

    # TODO: use support.requires_internet() decorator in unit-test
    if True:
        return

    ZDFChannelIE()._extract_channel(
        'https://www.zdf.de/sport/das-aktuelle-sportstudio')
    ZDFChannelIE()._extract_channel(
        'https://www.zdf.de/dokumentation/planet-e')
    ZDFChannelIE()._extract_channel(
        'https://www.zdf.de/filme/taunuskrimi/')

# Generated at 2022-06-14 17:41:03.262026
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    pass


# Generated at 2022-06-14 17:41:06.793702
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    global ZDFBaseIE
    global ZDFIE
    assert(ZDFBaseIE != None)
    assert(ZDFIE != None)
    assert(ZDFIE.ie_key() == 'ZDF')


# Generated at 2022-06-14 17:41:07.739491
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE()



# Generated at 2022-06-14 17:41:12.402191
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Test with valid input
    try:
        ZDFBaseIE()
    except:
        # raise error if test has failed
        raise AssertionError("Failed to construct ZDFBaseIE")

# Generated at 2022-06-14 17:41:13.401273
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    inst = ZDFIE()

# Generated at 2022-06-14 17:41:14.786675
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    pass

# Generated at 2022-06-14 17:41:15.918394
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    zdfie

# Generated at 2022-06-14 17:43:06.489800
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ifile = ZDFIE()
    assert ifile.name == 'zdf'

##################################################################################################


# Generated at 2022-06-14 17:43:14.110623
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    obj = ZDFChannelIE()
    assert obj.ie_key() == 'ZDFChannel'
    assert obj.ie_key() in globals().keys()
    assert obj.SUITABLE_URL == 're:https?://www\.zdf\.de/.*'
    assert obj.VALID_URL == 'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert obj.VALID_URL == re.compile(obj.SUITABLE_URL).pattern


# Generated at 2022-06-14 17:43:18.066011
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_IE = ZDFBaseIE()
    assert test_IE._GEO_COUNTRIES == ['DE']
    assert test_IE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:43:30.060889
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # input
    title = "Wohin führt der Protest in der Pandemie?"
    description = "Die Corona-Pandemie verändert unser Leben fundamental. Daran zu zweifeln ist verständlich. Doch es gibt auch unverschämte Verschwörungstheorien, die das Vertrauen in die Politik untergraben. Wie weit gehen Demonstranten, die sich auf der Straße gegen die Regierung manifestieren? Welche Rolle spielen bei den Protesten auch militantere Gruppierungen und wie können die Strafverfolgungsbehörden damit umgehen?"
    duration = 1691
    timestamp = 1613948400

# Generated at 2022-06-14 17:43:32.650472
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = "https://www.zdf.de/dokumentation/planet-e"
    ie = ZDFChannelIE.suitable(url)
    assert ie is not None



# Generated at 2022-06-14 17:43:39.928670
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.SUBTITLE_LANGS == [{
        'ext': 'ttml',
        'key': 'deu',
        're': r'<p[^>]+begin="(?P<start>\d{2}:\d{2}:\d{2})\.[0-9]+"\s+end="(?P<end>\d{2}:\d{2}:\d{2}\.[0-9]+)"[^>]*>(?P<text>.+?)</p>',
    }]


# Generated at 2022-06-14 17:43:44.897608
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE()



# Generated at 2022-06-14 17:43:46.000225
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert callable(ZDFBaseIE)


# Generated at 2022-06-14 17:43:52.688855
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """Test for constructor of class ZDFChannelIE"""
    from .zdf_downloader import ZDFDownloader

    # Test for constructor of class ZDFDownloader
    test_ZDFDownloader()

    zdf_downloader = ZDFDownloader()

    zdf_channel_ie = zdf_downloader.get_IE('zdf:audio')
    assert zdf_channel_ie.ie_key() == 'ZDFChannel:audio'
    assert zdf_channel_ie == zdf_downloader.get_IE(zdf_channel_ie.ie_key())
    assert zdf_channel_ie != zdf_downloader.get_IE('zdf:video')

# Test for class ZDFChannelIE

# Generated at 2022-06-14 17:43:54.286886
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()
