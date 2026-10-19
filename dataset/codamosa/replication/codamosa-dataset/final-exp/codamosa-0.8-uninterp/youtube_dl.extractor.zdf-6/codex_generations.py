

# Generated at 2022-06-14 17:38:02.558120
# Unit test for constructor of class ZDFChannelIE

# Generated at 2022-06-14 17:38:14.863296
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    #test extract formats
    ie = ZDFBaseIE()
    formats = []
    track_uris = set()
    # test extract format
    f_qualities = [{'qualities':[{'quality': 'low', 'audio': {'tracks':[{'uri': 'http://x.x/x'}]}}]}]
    for quality in f_qualities:
        tracks = try_get(quality, lambda x: x['audio']['tracks'], list)
        if not tracks:
            continue

# Generated at 2022-06-14 17:38:18.714171
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:38:19.889266
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE._GEO_COUNTRIES == ['DE']


# Generated at 2022-06-14 17:38:25.002563
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    with pytest.raises(TypeError, match=r'unexpected keyword argument \'e\''):
        ZDFIE(e=1)


# Generated at 2022-06-14 17:38:37.187042
# Unit test for constructor of class ZDFBaseIE

# Generated at 2022-06-14 17:38:42.168184
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    t_ZDFBaseIE = ZDFBaseIE()
    assert t_ZDFBaseIE._GEO_COUNTRIES == ['DE']
    assert t_ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:38:46.086879
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    from .zdf import ZDFIE
    from .zdf_mediathek import ZDFMediathekIE

    ZDFBaseIE(ZDFIE)
    ZDFBaseIE(ZDFMediathekIE)
    test_ZDFBaseIE()



# Generated at 2022-06-14 17:38:50.759915
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdfbase = ZDFBaseIE()
    assert zdfbase._GEO_COUNTRIES == ['DE']
    assert zdfbase._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:38:51.749193
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    pass



# Generated at 2022-06-14 17:39:21.211121
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert(ie.ie_key() == 'ZDF')
    assert(ie.extract_id('https://www.zdf.de/filme/filme-sonstige/der-hauptmann-112.html') == 'der-hauptmann-112')
    assert(ie.url_result('https://www.zdf.de/filme/filme-sonstige/der-hauptmann-112.html').ie_key() == 'ZDF')

# Generated at 2022-06-14 17:39:25.669351
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Arrange
    url = 'https://www.zdf.de/filme/taunuskrimi/'
    ZDFChannelIE_target = ZDFChannelIE()
    # Act
    ZDFChannelIE_actual = ZDFChannelIE()
    # Assert
    assert ZDFChannelIE_target.suitable(url) == ZDFChannelIE_actual.suitable(url)


# Generated at 2022-06-14 17:39:28.470517
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zie = ZDFChannelIE(ZDFChannelIE._VALID_URL)
    return zie.suitable(ZDFChannelIE._VALID_URL)

# Generated at 2022-06-14 17:39:32.446444
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    rr = ZDFChannelIE()
    url = 'https://www.zdf.de/politik/phoenix-sendungen'
    rr.suitable(url)
    rr.extract(url)


# Generated at 2022-06-14 17:39:43.994544
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    parser = ZDFIE()
    if not parser.check_ie():
        print("ZDFIE can not be tested")
        return

# Generated at 2022-06-14 17:39:49.143452
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # First check for expected assertion
    try:
        ie = ZDFIE(None, None)
        ie._real_extract(None)
        assert False
    except AssertionError:
        assert True
    # Simple call that doesn't fail
    ie = ZDFIE(None, ZDFIE._VALID_URL)
    # Again with the right arguments
    ie = ZDFIE(None, ZDFIE._VALID_URL.format(id='id'))


# Generated at 2022-06-14 17:39:51.196875
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert(isinstance(ZDFIE(InfoExtractor()), ZDFIE))



# Generated at 2022-06-14 17:40:03.061407
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdf_ie = ZDFBaseIE(ZDFIE)
    print('Testing initialization of ZDFBaseIE-object.')
    assert isinstance(zdf_ie, ZDFBaseIE)
    assert isinstance(zdf_ie, InfoExtractor)
    assert isinstance(zdf_ie.geo_countries, list)
    assert len(zdf_ie.geo_countries) == 1
    assert zdf_ie.geo_countries[0] == 'DE'
    assert isinstance(zdf_ie.qualities, tuple)
    assert len(zdf_ie.qualities) == 6
    assert isinstance(zdf_ie._call_api, object)
    assert isinstance(zdf_ie._extract_subtitles, object)

# Generated at 2022-06-14 17:40:14.895455
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """ Unit test for constructor of class ZDFChannelIE """
    import unittest
    from .test_utils import make_test_case

    # testcases

# Generated at 2022-06-14 17:40:16.653263
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_ie = ZDFChannelIE("http://www.zdf.de/filme/taunuskrimi/")

# Generated at 2022-06-14 17:41:06.803252
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE()



# Generated at 2022-06-14 17:41:16.861530
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    web_page_url1 = 'https://www.zdf.de/filme/taunuskrimi/'
    web_page_url2 = 'https://www.zdf.de/filme/taunuskrimi/taunuskrimi-uebersichtsseite-filme-die-es-gibt-100.html'

    # testing constructor of class ZDFChannelIE
    zdf_channel_ie = ZDFChannelIE(web_page_url1)
    assert zdf_channel_ie.suitable(web_page_url1) == True
    assert zdf_channel_ie.suitable(web_page_url2) == False

# Generated at 2022-06-14 17:41:29.586623
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    try:
        import yaml
        yaml.safe_load('')
    except ImportError:
        return

    test_cases = yaml.safe_load(
        compat_urllib_request.urlopen(
            'https://raw.githubusercontent.com/ytdl-org/youtube-dl/master/'
            'test/test_data/compatibility/zdf_channels.yml'
        ).read())

    for ie_code, ie_config in test_cases.items():
        ie = get_info_extractor(ie_code)
        for url, video_id, video_title in ie_config['ids']:
            if not ie_config.get('skip_ids'):
                assert video_id == ie._match_id(url)

# Generated at 2022-06-14 17:41:33.805885
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    t = ZDFIE()
    t.extract('https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html')



# Generated at 2022-06-14 17:41:40.804116
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_extractor = ZDFBaseIE()
    assert test_extractor._GEO_COUNTRIES == ["DE"]
    assert test_extractor._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

# Unit tests for functions of class ZDFBaseIE
# def test_ZDFBaseIE_call_api():
# def test_ZDFBaseIE_extract_subtitles():
# def test_ZDFBaseIE_extract_format():
# def test_ZDFBaseIE_extract_ptmd():
# def test_ZDFBaseIE_extract_player():



# Generated at 2022-06-14 17:41:45.598008
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    with pytest.raises(ZDFBaseIE._BuildError):
        c = ZDFChannelIE(url)
        pytest.fail('Should raise exception.')

# Generated at 2022-06-14 17:41:49.182183
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    instance = ZDFBaseIE()
    assert instance._GEO_COUNTRIES == ['DE']
    assert instance._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:41:50.074913
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE(None, None)


# Generated at 2022-06-14 17:41:50.703883
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE()

# Generated at 2022-06-14 17:41:56.508844
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE(
        'http://www.zdf.de/ZDFmediathek')._GEO_COUNTRIES == ['DE'] 
    assert ZDFBaseIE(
        'http://www.zdf.de/ZDFmediathek')._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:44:19.016386
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    try:
        import zdf_channel
    except ImportError:
        zdf_channel = sys.modules['__main__']
    ZDFChannelIE().suitable('https://www.zdf.de/dokumentation/planet-e')
    assert zdf_channel.ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert zdf_channel.ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi')
    assert not zdf_channel.ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html')
    assert not zdf_

# Generated at 2022-06-14 17:44:23.865756
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert_raises(TypeError, ZDFBaseIE, None, 'ZDFBaseIE', 'zdf')
    assert_raises(ValueError, ZDFBaseIE, 'ZDFBaseIE', None, 'zdf')
    assert_raises(ValueError, ZDFBaseIE, 'ZDFBaseIE', 'ZDFBaseIE', None)



# Generated at 2022-06-14 17:44:34.545013
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    from youtube_dl.downloader.http import HttpFD
    from youtube_dl.downloader.external.ffmpeg import FFmpegFD

    import sys

    class TestDownloader(object):
        def __init__(self, ydl, params):
            self.params = params
            self.ydl = ydl

        def to_screen(self, s):
            print(s, file=sys.stderr)

        def trouble(self, s):
            print('error: ' + s, file=sys.stderr)
            exit(1)

        def download(self, url_list):
            if len(url_list) > 1:
                raise NotImplementedError()
            url = url_list[0]
            ie = self.ydl.extract_info(url, download=False)
            video_

# Generated at 2022-06-14 17:44:43.182864
# Unit test for constructor of class ZDFChannelIE

# Generated at 2022-06-14 17:44:50.289552
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    z = ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e')
    z = ZDFChannelIE.suitable('https://www.zdf.de/_/dokumentation/planet-e')
    z = ZDFChannelIE.suitable('https://www.zdf.de/planet-e')
    assert isinstance(z, bool)


# Generated at 2022-06-14 17:44:53.002267
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES == ['DE']


# Generated at 2022-06-14 17:44:56.777288
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    constructor = ZDFBaseIE
    assert constructor.ie_key() == 'ZDF'
    assert constructor.ie_key()

    # new instance of class ZDFBaseIE
    instance = constructor(None, 'None')
    assert isinstance(instance, InfoExtractor)


# Generated at 2022-06-14 17:44:58.378323
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'ZDF'
    assert ie.ssl == False



# Generated at 2022-06-14 17:45:01.579018
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE("")
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:45:03.924862
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    a = ZDFBaseIE()
    assert a._QUALITIES is None
    assert a.ie_key() is None
    assert a.host() is None
