

# Generated at 2022-06-14 17:16:31.612106
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    m = TruTVIE()
    assert m is not None

# Generated at 2022-06-14 17:16:34.893802
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert(t)


# Generated at 2022-06-14 17:16:35.530993
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE();

# Generated at 2022-06-14 17:16:36.164144
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:36.806158
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert True

# Generated at 2022-06-14 17:16:37.434496
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:40.727899
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    video_url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    trutv_object = TruTVIE()
    trutv_object.extract(video_url)

# Generated at 2022-06-14 17:16:42.152562
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE(TruTVIE._downloader) is not None

# Generated at 2022-06-14 17:16:51.064465
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()
    first_match = re.match(trutv_ie._VALID_URL, 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert first_match is not None
    assert first_match.group('series_slug') == 'the-carbonaro-effect'
    assert first_match.group('clip_slug') == 'sunlight-activated-flower'
    assert first_match.group('id') is None

    second_match = re.match(trutv_ie._VALID_URL, 'https://www.trutv.com/full-episodes/1536/the-carbonaro-effect-1x18/episode-18.html')
    assert second_match is not None
   

# Generated at 2022-06-14 17:16:52.129696
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TrutvIE = TruTVIE()

# Generated at 2022-06-14 17:16:59.396312
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_instance = TruTVIE()
    return test_instance

# Generated at 2022-06-14 17:17:00.064548
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:03.857978
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    video_ie = TruTVIE()
    assert video_ie.suitable("https://www.trutv.com/shows/the-carbonaro-effect/videos/mannequin-in-the-crapper.html") == True

# Generated at 2022-06-14 17:17:09.394415
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvIE = TruTVIE()
    assert trutvIE.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert trutvIE.IE_NAME == 'trutv:video'
    assert trutvIE.PLAYLIST_TITLE == 'truTV Gallery'



# Generated at 2022-06-14 17:17:10.833056
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    param_TruTVIE = TruTVIE()
    assert isinstance(param_TruTVIE, TruTVIE)

# Generated at 2022-06-14 17:17:11.904744
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.__name__ == 'TruTVIE'

# Generated at 2022-06-14 17:17:13.249675
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:17:15.166640
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    object_TruTVIE = TruTVIE()

# Generated at 2022-06-14 17:17:24.507451
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert "TruTVIE" == instance.IE_NAME

    # Unit test for class field _VALID_URL
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    valid_url_match = instance._VALID_URL.match(url)
    assert valid_url_match is not None
    assert '16c03beec1e84cd7d1a51f11d8fcc29124cc7f1' == instance._extract_display_id(url)

# Generated at 2022-06-14 17:17:35.798833
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:56.216423
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    # test for VALID_URL
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    # tests for _real_extract
    series_slug, clip_slug, video_id = re.match(ie._VALID_URL, ie._TEST['url']).groups()
    if video_id: path = 'episode'
    else: path = 'series/clip'
    assert ie._real_extract(ie._TEST['url']) == ie._T

# Generated at 2022-06-14 17:17:57.525990
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Initialize TruTVIE class
    TruTVIE()

# Generated at 2022-06-14 17:18:09.595604
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvIE = TruTVIE()
    assert trutvIE._VALID_URL == 'https?://(?:www\\.)?trutv\\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\\d+))'

# Generated at 2022-06-14 17:18:17.432795
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    
    # no error
    try:
        TruTVIE()
    except:
        assert False, "Cannot initialize TruTVIE class"
    
    # error upon invalid id
    try:
        TruTVIE("invalid_id")
        assert False, "Should not accept invalid id"
    except:
        pass

    # no error upon valid id
    try:
        TruTVIE("trutv")
    except:
        assert False, "Cannot initialize TruTVIE class with valid ID"

# Generated at 2022-06-14 17:18:24.633759
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    import requests

    # positive test case
    test = TruTVIE()
    assert test._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

    # negative test case
    # test = TruTVIE()
    # assert test.authenticated_hd_url != 'htthps://api.trutv.com/v3/videos/auth/hd/'



# Generated at 2022-06-14 17:18:28.973602
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    '''
    unit test for constructor of class TruTVIE
    '''
    trutv = TruTVIE()
    return

# Generated at 2022-06-14 17:18:30.725803
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    a = TruTVIE()
    try:
        b = TruTVIE(a)
    except Exception:
        b = None
    assert b is None


# Generated at 2022-06-14 17:18:36.951880
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert obj._TEST['url'] == r'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert obj._TEST['info_dict']['id'] == r'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'

# Generated at 2022-06-14 17:18:40.854227
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert isinstance(instance, TurnerBaseIE)
    assert TruTVIE._VALID_URL == instance._VALID_URL
    assert TruTVIE._TEST == instance._TEST

# Generated at 2022-06-14 17:18:45.109164
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()
    assert trutv_ie.ie_key() == 'trutv'
    assert trutv_ie.ie_name() == 'TruTV'
    assert trutv_ie.ie_url() == 'trutv.com'

# Generated at 2022-06-14 17:19:07.645013
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:19:11.649625
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:19:17.462967
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Note: This test is used for comparing the output of the constructor with the expected value
    # Note: This test is used for debugging purposes only
    test_url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    test_class = TruTVIE()
    expected_value = True
    actual_value = test_class.suitable(test_url)
    assert actual_value == expected_value


# Generated at 2022-06-14 17:19:24.107050
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert(TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')
    assert(TruTVIE._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')    

# Generated at 2022-06-14 17:19:28.056257
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj=TruTVIE()
    if not isinstance(obj, TruTVIE):
        print("Failure:object was not created")
        return
    if not isinstance(obj, TurnerBaseIE):
        print("Failure:object not created for TurnerBaseIE")
        return

# Generated at 2022-06-14 17:19:30.899096
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    assert obj.ie_key() == 'trutv'
    assert obj.ie_name() == 'TruTV'


# Unit tests for main function

# Generated at 2022-06-14 17:19:32.728432
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv_test = TruTVIE('test')
    print(ttv_test)



# Generated at 2022-06-14 17:19:34.212840
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:41.407469
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert(TruTVIE.__name__ == 'TruTVIE')
    assert(TruTVIE._VALID_URL == r'^https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))$')

# Generated at 2022-06-14 17:19:41.981948
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    pass

# Generated at 2022-06-14 17:20:33.680595
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    '''Constructor of class TruTVIE'''
    from .yandex import YandexIE
    from .common import InfoExtractor
    from .anvato import AnvatoIE
    from .pladform import PladformIE
    from .tvasahi import TvasahiIE
    from .tbs import TBSIE
    from .ooyala import OoyalaIE
    from .kaltura import KalturaIE
    from .pornhub import PornHubIE
    from .jwplatform import JWPlatformIE
    from .aenetworks import AENetworksIE
    from .brightcove import BrightcoveLegacyIE
    from .brightcove4 import Brightcove4IE
    from .tvplay import TVPlayIE
    from .rtve import RTVEALaCartaIE

# Generated at 2022-06-14 17:20:35.912463
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	x = TruTVIE()
	assert x is not None



# Generated at 2022-06-14 17:20:43.408872
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_fun = TruTVIE()
    print(test_fun.__class__.__name__)
    print(test_fun._VALID_URL)
    print(test_fun._TEST)
    print(test_fun._extract_ngtv_info)
    test_fun = TruTVIE._extract_ngtv_info
    print(test_fun.__name__)
    print(test_fun.__code__.co_varnames)
    print(test_fun.__code__.co_argcount)
    print(test_fun.__code__.co_code)


if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:20:48.388511
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    import TruTV

    try:
        s_slug = 'TheCarbonaroEffect'
        c_slug = 'SunlightActivatedFlower'
        v_id = '1066'

        obj = TruTV.TruTVIE(s_slug, c_slug, v_id)
        assert (obj.series_slug == s_slug)
        assert (obj.clip_slug == c_slug)
        assert (obj.video_id == v_id)
    except Exception as e:
        raise e



# Generated at 2022-06-14 17:20:48.864313
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:20:49.546908
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	ie = TruTVIE()

# Generated at 2022-06-14 17:20:52.283363
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tu = TruTVIE()
    return

# Generated at 2022-06-14 17:20:55.792297
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    c = TruTVIE()
    c.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    return True

# Generated at 2022-06-14 17:20:57.310464
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    with TruTVIE(None) as xt:
        assert xt


# Generated at 2022-06-14 17:20:58.377931
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_TruTVIE = TruTVIE()

# Generated at 2022-06-14 17:22:45.410818
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	truTV = TruTVIE()

# Generated at 2022-06-14 17:22:47.607458
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        assert(TruTVIE)
    except NameError:
        assert(False)


# Unittest for extract method of class TruTVIE

# Generated at 2022-06-14 17:22:49.402818
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()
    trutv_ie.ie_key()

# Generated at 2022-06-14 17:22:52.495343
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    IE = TruTVIE()
    assert isinstance(IE, TurnerBaseIE)
    assert hasattr(IE, '_VALID_URL')
    assert hasattr(IE, '_TEST')
    return


# Generated at 2022-06-14 17:23:03.733655
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	trutv = TruTVIE()
	assert isinstance(trutv._downloader, YoutubeDL)
	assert trutv._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
	assert trutv._downloader.params['noplaylist'] is True
	assert trutv._downloader.params['outtmpl'] == '%(id)s-%(playlist_index)s-%(title)s.%(ext)s'

# Generated at 2022-06-14 17:23:05.146163
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    x = TruTVIE()
    assert isinstance(x, TurnerBaseIE)

# Generated at 2022-06-14 17:23:14.461578
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:19.345263
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.turner_key = 'fake_key'
    ie.turner_secret = 'fake_secret'
    ie.turner_test_device_id = 'fake_id'
    assert ie.turner_key == 'fake_key'
    assert ie.turner_secret == 'fake_secret'
    assert ie.turner_test_device_id == 'fake_id'

# Generated at 2022-06-14 17:23:19.841402
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:22.076761
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()