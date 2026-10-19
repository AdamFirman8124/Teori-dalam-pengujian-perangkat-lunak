

# Generated at 2022-06-14 17:38:01.423339
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Test same URL for ZDFChannelIE and ZDFIE
    url = 'https://www.zdf.de/filme/taunuskrimi/'
    assert ZDFIE.suitable(url) and not ZDFChannelIE.suitable(url)
    assert ZDFChannelIE.suitable(url.replace('https', 'http').replace('/filme/taunuskrimi/', '/sport/das-aktuelle-sportstudio/')) and not ZDFChannelIE.suitable(url)
    assert ZDFChannelIE.suitable(url.replace('https', 'http').replace('/filme/taunuskrimi/', '/dokumentation/planet-e/')) and not ZDFChannelIE.suitable(url)

# Generated at 2022-06-14 17:38:03.456582
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    f = ZDFBaseIE._call_api
    assert f(1, 2, 3) == None



# Generated at 2022-06-14 17:38:07.635986
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    result = ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/')
    assert result is False, ('invalid result in constructor of class ZDFChannelIE. Result was: {}'.format(result))

# Generated at 2022-06-14 17:38:12.187975
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE(None)
    assert ie._GEO_COUNTRIES, "ZDFBaseIE._GEO_COUNTRIES is empty"
    assert ie._QUALITIES, "ZDFBaseIE._QUALITIES is empty"
    assert ie._call_api(None, None, None, None)



# Generated at 2022-06-14 17:38:14.002058
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()


# Generated at 2022-06-14 17:38:17.930320
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Test constructor
    result = ZDFChannelIE()._real_extract('https://www.zdf.de/dokumentation/planet-e')
    assert result['id'] == 'planet-e'
    assert 'title' in result

# Generated at 2022-06-14 17:38:26.293925
# Unit test for constructor of class ZDFIE

# Generated at 2022-06-14 17:38:29.858436
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    global ZDFBaseIE

    # Check for constructor "ZDFBaseIE"
    obj = ZDFBaseIE(ZDFBaseIE._downloader, {})
    assert isinstance(obj, ZDFBaseIE)



# Generated at 2022-06-14 17:38:31.541330
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE()

# Generated at 2022-06-14 17:38:32.699559
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 17:39:00.758092
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # https://www.zdf.de/kultur/3sat-festival
    mobj = re.search(r'https?://(?P<url>www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+))', "https://www.zdf.de/kultur/3sat-festival")
    assert mobj
    # print(mobj.group('id'))
    # assert(0)


# Generated at 2022-06-14 17:39:04.951357
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    ie_key = ie.ie_key()
    assert ie_key == 'ZDF'

# Generated at 2022-06-14 17:39:13.889064
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Create instance of class you want to test
    ie = ZDFChannelIE()
    # Create dummy url
    url = 'http://www.zdf.de/dokumentation/planet-e'
    # Get the actual result of the function or method ie.suitable()
    actual_result = ie.suitable(url)
    # Get the expected result
    expected_result = True
    # Compare if the actual result corresponds to the expected result
    assert actual_result == expected_result, "actual result: %s instead of expected result: %s" % (actual_result, expected_result)
    # Print what the unit test has achieved
    print('%s.suitable() successful' % ie.__class__)

# Generated at 2022-06-14 17:39:15.310278
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    s = ZDFChannelIE()
    assert(s is not None)


# Generated at 2022-06-14 17:39:20.698418
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Test with correct url
    url = 'https://www.zdf.de/politik/frontal21/forderung-nach-abrechnung-100.html'
    assert ZDFIE._VALID_URL == ZDFIE._extract_url(ZDFIE._VALID_URL), 'Valid url should not be changed'
    assert not ZDFIE._working, 'Valid url should set _working to True'
    assert ZDFIE._real_extract(url)


# Generated at 2022-06-14 17:39:21.733109
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_ZDFBaseIE = ZDFBaseIE()

# Generated at 2022-06-14 17:39:22.663214
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE(None, {})


# Generated at 2022-06-14 17:39:23.885956
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE('ZDFBaseIE', 'www.zdf.de')


# Generated at 2022-06-14 17:39:32.126144
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    assert(ZDFChannelIE.ie_key() == 'ZDF:channel')
    assert(ZDFChannelIE.suitable(url))
    assert(ZDFChannelIE(ZDFChannelIE.ie_key())._VALID_URL == ZDFChannelIE._VALID_URL)
    obj = ZDFChannelIE(ZDFChannelIE.ie_key())
    obj._real_extract(url)

# Generated at 2022-06-14 17:39:38.179768
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Create the class of the channel
    info = ZDFChannelIE().extract(
        'https://www.zdf.de/politik/phoenix-sendungen')
    # Check if the if the length of the playlist is equal or greater than 23
    assert len(info['entries']) >= 23
    assert info['id'] == 'phoenix-sendungen'
    assert info['title'] == 'Phoenix Sendungen'

# Generated at 2022-06-14 17:40:10.170272
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.suitable(ZDFChannelIE._VALID_URL)
    assert ie.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert not ie.suitable('https://www.zdf.de/politik/wahl-2019/')
    assert not ie.suitable('https://www.zdf.de/kinder/logo/wissensquiz-100.html')

# Generated at 2022-06-14 17:40:13.817627
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    assert zdfie._GEO_COUNTRIES == ['DE']
    assert zdfie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:40:15.834920
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE('ZDFIE')
    assert ie.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:40:21.980834
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    obj = ZDFChannelIE()
    url = 'https://www.zdf.de/dokumentation/planet-e'
    channel_id = ZDFChannelIE._match_id(url)
    webpage = obj._download_webpage(url, channel_id)
    player = obj._extract_player(webpage, channel_id)
    channel_id = obj._search_regex(r'docId\s*:\s*(["\'])(?P<id>(?!\1).+?)\1', webpage, 'channel id', group='id')
    channel = obj._call_api('https://api.zdf.de/content/documents/%s.json' % channel_id, player, url, channel_id)


# Generated at 2022-06-14 17:40:32.790356
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    import sys

    # Define the ZDFIE test class as a subclass of ZDFBaseIE
    class TmpZDFIE(ZDFBaseIE):
        def __init__(self, *args, **kwargs):
            super(ZDFIE, self).__init__(*args, **kwargs)

        def _real_extract(self, url):
            return 'test'
    # End of definition

    test_instance = TmpZDFIE()

    # Check that the test instances have the attributes of the
    # parent classes

# Generated at 2022-06-14 17:40:33.538261
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()



# Generated at 2022-06-14 17:40:38.010651
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    l = ZDFIE()
    l
    assert l._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert l._GEO_COUNTRIES == ('DE')



# Generated at 2022-06-14 17:40:39.408834
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    print(ZDFIE())



# Generated at 2022-06-14 17:40:40.455633
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    test = ZDFIE()
    test.suite()

# Generated at 2022-06-14 17:40:42.399276
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    youtube_ie = ZDFIE()
    assert youtube_ie.suitable ("https://www.zdf.de/") == False


# Generated at 2022-06-14 17:41:30.604567
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    video_id = 'abc'
    webpage = 'abc'
    player_json = 'abc'
    assert isinstance(ZDFBaseIE(video_id, webpage, player_json), ZDFBaseIE)



# Generated at 2022-06-14 17:41:34.433230
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channel_ie = ZDFChannelIE()
    assert zdf_channel_ie.suitable('https://www.zdf.de/filme/taunuskrimi/')
    assert not zdf_channel_ie.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio')


# Generated at 2022-06-14 17:41:35.569780
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
  zdfie = ZDFIE()

# Generated at 2022-06-14 17:41:37.795293
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    """Test if extracting with ZDFIE works"""
    ZDFIE().extract(test_ZDFIE.__doc__)


# Generated at 2022-06-14 17:41:50.701150
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/dokumentation/planet-e'
    import re
    import string
    import time

    # Wait for a random time of 0-1 seconds before proceeding. Useful for
    # when you want to test with multiple instances, but don't want to DDOS
    # the ZDF servers.
    time.sleep(random.randint(0, 1))
    webpage = request.urlopen(url).read()
    # For some reason, ZDF is sometimes sending back a bytes object and sometimes a string,
    # therefore, we use re.sub to convert everything to a string.
    webpage = re.sub('[%s]' % string.ascii_letters, '', webpage.decode('utf-8'))

# Generated at 2022-06-14 17:41:55.877610
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from .test_html5_media_extractor import test_extractor
    ZDFBaseIE.test_video_id()
    ZDFBaseIE.test_extract()

    test_extractor(ZDFChannelIE, ['https://www.zdf.de/filme/taunuskrimi/'])



# Generated at 2022-06-14 17:42:03.719902
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    e = ZDFBaseIE()
    assert e._GEO_COUNTRIES == ['DE']
    assert e._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert e._call_api(object(), 'foobar', 'baz', api_token=None, referrer=None)
    assert e._extract_subtitles(object()) == {}
    assert e._extract_format(object(), object(), object(), object()) is None
    assert e._extract_ptmd(object(), 'foobar', object(), object()) == {}
    assert e._extract_player(object(), 'foobar', fatal=True) == {}
    assert e._extract_player(object(), 'foobar', fatal=False) == {}


# Generated at 2022-06-14 17:42:06.456619
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.extractor_key == ZDFChannelIE.ie_key()
    assert ie.suitable(ZDFChannelIE._VALID_URL)



# Generated at 2022-06-14 17:42:09.327117
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    obj = ZDFBaseIE(InfoExtractor())
    assert obj._GEO_COUNTRIES == ['DE']
    assert obj._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:42:11.959789
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    instance = ZDFChannelIE('https://www.zdf.de/dokumentation/planet-e')
    instance.params = {
        'skip_download': True,
    }
    instance.extract()

# Generated at 2022-06-14 17:44:21.202972
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE(None)
    assert ie.suitable(ZDFChannelIE._VALID_URL) == True
    assert ie.suitable(ZDFIE._VALID_URL) == False

# Generated at 2022-06-14 17:44:22.660423
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfIE = ZDFIE()
    

# Generated at 2022-06-14 17:44:29.449635
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE(ZDFIE._VALID_URL, ZDFIE._TESTS, True)
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'

# Generated at 2022-06-14 17:44:31.795502
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """ Unit test for ZDFChannelIE """
    ZDFChannelIE()._real_extract('https://www.zdf.de/dokumentation/planet-e')


# Generated at 2022-06-14 17:44:33.326176
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    try:
        ie = ZDFBaseIE()
    except:
        assert False



# Generated at 2022-06-14 17:44:41.154004
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfchannel = ZDFChannelIE()
    assert zdfchannel.suitable(None) is False
    assert zdfchannel.suitable('') is False
    assert zdfchannel.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert zdfchannel.suitable('https://www.zdf.de/dokumentation/planet-e/')
    assert zdfchannel.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio')
    assert zdfchannel.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio/')
    assert zdfchannel.suitable('https://www.zdf.de/dokumentation/planet-e')
    assert zdf

# Generated at 2022-06-14 17:44:51.883459
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdf_channelIE_namespace = {}
    exec(compat_urllib_request.urlopen(ZDFChannelIE.__module__.replace(".", "/") + ".py").read(), zdf_channelIE_namespace)
    for sname, sc in zdf_channelIE_namespace.items():
        if isinstance(sc, type) and issubclass(sc, ZDFChannelIE):
            cl = sc("https://www.zdf.de/dokumentation/planet-e")
            assert cl == ZDFChannelIE("https://www.zdf.de/dokumentation/planet-e")

# Generated at 2022-06-14 17:45:02.042413
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    zdfbase = ZDFBaseIE()
    assert zdfbase._GEO_COUNTRIES == ['DE']
    assert zdfbase._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert zdfbase._call_api('https://zdf.de', 'test', 'metadata') is None
    assert zdfbase._extract_subtitles({'captions': [{'uri': 'https://zdf.de', 'language': 'deu'}]}) == {'deu': [{'url': 'https://zdf.de'}]}

# Generated at 2022-06-14 17:45:03.670672
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    """
    Shouldn't raise AssertionError
    """
    ZDFIE()


# Generated at 2022-06-14 17:45:06.220397
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    obj = ZDFBaseIE()
    # ZDFBaseIE is an abstract class and shouldn't be instantiated
    assert False
