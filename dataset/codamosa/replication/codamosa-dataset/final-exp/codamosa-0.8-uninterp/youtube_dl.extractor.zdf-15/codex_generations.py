

# Generated at 2022-06-14 17:37:55.100914
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    a = ZDFChannelIE('https://www.zdf.de/dokumentation/planet-e')
    assert a.ZDFBaseIE.api_host == 'https://api.zdf.de'
    assert a.SUFFIX == 'https://www.zdf.de/dokumentation/planet-e'


# Generated at 2022-06-14 17:37:58.295456
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # For coverage
    ZDFBaseIE(ZDFBaseIE.ie_key(), ZDFBaseIE.ie_key())


# Generated at 2022-06-14 17:37:59.482435
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # No tests
    assert True

# Generated at 2022-06-14 17:38:08.071102
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfIE = ZDFIE()
    assert zdfIE._GEO_COUNTRIES == ['DE']
    assert zdfIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')
    assert zdfIE._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'
    assert zdfIE.ie_key() == 'ZDF'
    assert zdfIE.working == True
    return 0



# Generated at 2022-06-14 17:38:15.285885
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE.ie_key() == 'ZDF'
    test_instance = ZDFIE()
    assert test_instance._VALID_URL == ZDFIE._VALID_URL
    assert test_instance._TESTS == ZDFIE._TESTS
    assert test_instance.IE_NAME == 'ZDF'
    assert test_instance.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:38:19.477612
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
	zdfBase = ZDFBaseIE()
	zdfBase._call_api('http://www.zdf.de/ZDFmediathek/xmlservice/web/beitragsDetails?ak=web&id=1565470', 'video_id', 'api item')



# Generated at 2022-06-14 17:38:22.247915
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()


# Generated at 2022-06-14 17:38:28.459434
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    '''
    Test the constructor of ZDFBaseIE
    '''
    zdfbase_ie = ZDFBaseIE('youtube_dl')
    assert zdfbase_ie._GEO_COUNTRIES == ['DE']
    assert zdfbase_ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:38:34.014439
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    instance = ZDFBaseIE()
    attributes = ['_GEO_COUNTRIES', '_QUALITIES']
    for attr in attributes:
        assert hasattr(instance, attr), \
            'ZDFBaseIE is missing the attribute {}'.format(attr)



# Generated at 2022-06-14 17:38:38.426947
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    constructor_test(ZDFChannelIE, [
        'https://www.zdf.de/dokumentation/planet-e',
        'https://www.zdf.de/sport/das-aktuelle-sportstudio'])

# Generated at 2022-06-14 17:39:05.712465
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfIE = ZDFIE()


#####################################
# HELPER FUNCTION FOR ANALYSING JSON #
#####################################



# Generated at 2022-06-14 17:39:15.223505
# Unit test for constructor of class ZDFChannelIE

# Generated at 2022-06-14 17:39:19.343017
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """ test ZDFChannelIE constructor """
    demo_url = 'https://www.zdf.de/dokumentation/planet-e'
    zdf_channel_ie = ZDFChannelIE()
    zdf_channel_ie.suitable(demo_url)
    zdf_channel_ie.extract(demo_url)

# Generated at 2022-06-14 17:39:22.008382
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE('ZDFBaseIE')
    assert ie.ie_key() == 'zdf'


# Generated at 2022-06-14 17:39:27.332055
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    assert(zdfie._GEO_COUNTRIES == ['DE'])
    assert(zdfie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html')
    assert(zdfie.ie_key() == 'ZDF')
    assert(zdfie.SUCCESS == 0)
    assert(zdfie.FAILURE == -1)


# Generated at 2022-06-14 17:39:31.370654
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    a = ZDFIE(None)
    assert isinstance(a, ZDFBaseIE)


# Generated at 2022-06-14 17:39:33.519946
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    try:
        _ZDFBaseIE = ZDFBaseIE()
    except:
        assert False
    assert True



# Generated at 2022-06-14 17:39:34.769404
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()


# Generated at 2022-06-14 17:39:36.535096
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
  ie = ZDFBaseIE()
  assert ie


# Generated at 2022-06-14 17:39:38.565471
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFBaseIE is not ZDFIE


# Generated at 2022-06-14 17:40:31.313320
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:40:36.559874
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/filme/taunuskrimi/'
    zdf = ZDFChannelIE()
    assert zdf.suitable(url) is True
    assert zdf._VALID_URL in url
    assert zdf.__name__ in ZDFIE.ie_key()
    assert zdf.__name__ in ZDFChannelIE.ie_key()

# Generated at 2022-06-14 17:40:39.608178
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    """
    Create a ZDFIE instance.
    """
    ZDFIE()

# Generated at 2022-06-14 17:40:42.865616
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannelIE = ZDFChannelIE()
    assert zdfChannelIE.suitable("https://www.zdf.de/dokumentation/planet-e") is True
    assert zdfChannelIE.suitable("https://www.zdf.de/filme/taunuskrimi/") is True


# Generated at 2022-06-14 17:40:44.072360
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE(None)



# Generated at 2022-06-14 17:40:45.681000
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    e = ZDFIE()
    assert isinstance(e, ZDFBaseIE)


# Generated at 2022-06-14 17:40:52.707131
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannelIE = ZDFChannelIE()
    assert zdfChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e') == True
    assert zdfChannelIE.suitable('https://www.zdf.de/politik/frontal-21/frontal-21-21-29-100.html') == False


# Generated at 2022-06-14 17:40:56.370325
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:40:58.410219
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()

# Generated at 2022-06-14 17:41:03.558248
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    t_ZDFBaseIE = ZDFBaseIE()
    assert t_ZDFBaseIE._GEO_COUNTRIES == ['DE']
    assert t_ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')

test_ZDFBaseIE()



# Generated at 2022-06-14 17:43:00.772343
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    url = "http://www.zdf.de/ZDFmediathek"
    webpage = '<div data-zdfplayer-jsb=\'{"foo":"bar"}\'></div>'
    # Test call method _extract_player
    zdfbase_test = ZDFBaseIE()
    zdfbase_test.extract(url)
    zdfbase_test._search_regex(r'(?s)(["\'])(?P<json>{.+?})\1', webpage, 'player JSON', default='{}' if not True else NO_DEFAULT, group='json')


# Generated at 2022-06-14 17:43:04.788909
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfe = ZDFIE()
    assert zdfe._VALID_URL == "https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html"
    return



# Generated at 2022-06-14 17:43:06.686767
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Invoke constructor of class ZDFBaseIE
    ZDFBaseIE('test')


# Generated at 2022-06-14 17:43:13.228851
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    channel_url = 'https://www.zdf.de/dokumentation/planet-e/'
    sess = requests.Session()
    zdf_channel_ie = ZDFChannelIE(channel_url, sess)
    assert zdf_channel_ie.url == channel_url
    assert zdf_channel_ie.sess == sess
    assert zdf_channel_ie.request_webpage(channel_url)



# Generated at 2022-06-14 17:43:19.178153
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'
    assert ie._TESTS[0]['url'] == 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'


# Generated at 2022-06-14 17:43:30.880850
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    assert zdfie._VALID_URL == r'https?://www\.zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)\.html'

# Generated at 2022-06-14 17:43:35.989635
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    zdf_channel_ie = ZDFChannelIE(url)
    assert zdf_channel_ie.suitable(url) is True
    zdf_channel_ie._TESTS = None


# Generated at 2022-06-14 17:43:41.950289
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    zdfchannel = ZDFChannelIE()
    zdfchannel.suitable(url)
    zdfchannel._real_extract(url)
    zdfchannel._download_webpage(url, 'test')
    zdfchannel.url_result('https://www.zdf.de/dokumentation/planet-e/planet-e-die-erde-wird-fremd-100.html', 'youtube')


# Generated at 2022-06-14 17:43:47.244219
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE(None)
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:43:51.673530
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    og_video = '''
<meta property="og:video" content="https://zdfplayer.de/embed/36237986" />
<meta property="og:video:type" content="application/x-mpegURL" />
<meta property="og:video:width" content="1024" />
<meta property="og:video:height" content="576" />
'''
    webpage = '''
<meta name="tt:videoID" content="36237986" />
%s
''' % og_video