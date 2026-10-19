

# Generated at 2022-06-14 17:37:37.935911
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('Walla')
    # Test properties
    assert ie.name == 'Walla'
    assert ie.ie_key == 'walla'
    assert ie.ie_key == ie.IE_NAME

# Generated at 2022-06-14 17:37:38.761552
# Unit test for constructor of class WallaIE
def test_WallaIE():
	# constructor of WallaIE
	assert WallaIE

# Generated at 2022-06-14 17:37:43.977292
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """Basic regression test.
    """
    ie = WallaIE()
    ie.initialize()
    assert ie.initialized == True
    assert ie.ie_key() == 'Walla'
    assert ie.url_re.match('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:37:44.934288
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE = WallaIE()

# Generated at 2022-06-14 17:37:49.417375
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._VALID_URL == WallaIE._VALID_URL
    assert 'walla' == ie._NETRC_MACHINE
    ie = WallaIE(None)
    assert ie._VALID_URL == WallaIE._VALID_URL
    assert 'walla' == ie._NETRC_MACHINE

# Generated at 2022-06-14 17:37:51.046917
# Unit test for constructor of class WallaIE
def test_WallaIE():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    ie = WallaIE({})
    assert IsWallaIE(ie)


# Generated at 2022-06-14 17:37:57.444423
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE(url)
    obj = ie.extract()
    assert(obj['id'] == '2642630')
    assert(obj['display_id'] == 'one-direction-all-for-one')
    assert(obj['ext'] == 'flv')
    assert(obj['title'] == 'וואן דיירקשן: ההיסטריה')

# Generated at 2022-06-14 17:37:59.988760
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._SUBTITLE_LANGS == {
        'עברית': 'heb',
    }

# Generated at 2022-06-14 17:38:11.269070
# Unit test for constructor of class WallaIE
def test_WallaIE():
    wallaIE = WallaIE()
    assert wallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert wallaIE._TEST.get('url') == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert wallaIE._TEST.get('info_dict').get('id') == '2642630'
    assert wallaIE._TEST.get('info_dict').get('display_id') == 'one-direction-all-for-one'
    assert wallaIE._TEST.get('info_dict').get('ext') == 'flv'

# Generated at 2022-06-14 17:38:14.398355
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'

# Generated at 2022-06-14 17:38:22.270707
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie._download_xml = lambda x,y: ''
    ie._download_webpage = lambda x,y: ''
    ie._real_extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:38:24.945955
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:38:25.638072
# Unit test for constructor of class WallaIE
def test_WallaIE():
    return WallaIE

# Generated at 2022-06-14 17:38:27.951986
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert(ie.TEST == WallaIE._TEST)

# Generated at 2022-06-14 17:38:30.989464
# Unit test for constructor of class WallaIE
def test_WallaIE():
    #constructor
    with open("WallaIE.json", "r") as f:
        assert(WallaIE(f))

# Generated at 2022-06-14 17:38:43.121154
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:45.841699
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE().get_url_list(list('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'.split()))

# Generated at 2022-06-14 17:38:50.440444
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # pylint: disable=undefined-variable
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    # pylint: enable=undefined-variable

# Generated at 2022-06-14 17:38:51.734809
# Unit test for constructor of class WallaIE
def test_WallaIE():
    unittest.main(module=__name__)

# Generated at 2022-06-14 17:38:54.768361
# Unit test for constructor of class WallaIE
def test_WallaIE():
    e = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert e != None

# Generated at 2022-06-14 17:39:06.083918
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL

# Generated at 2022-06-14 17:39:09.007278
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.VALID_URL == WallaIE._VALID_URL

# Generated at 2022-06-14 17:39:15.168630
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Constructor of class WallaIE should take the url of a video from Walla:
    # http://vod.walla.co.il
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    test_ie = WallaIE(url)
    assert test_ie.url == url

# Generated at 2022-06-14 17:39:16.449534
# Unit test for constructor of class WallaIE
def test_WallaIE():
    init = WallaIE()

# Generated at 2022-06-14 17:39:16.981319
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:39:18.223963
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla'

# Generated at 2022-06-14 17:39:25.551483
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:32.029156
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Example: WallaIE()
    # I would put an example here, but it's not that easy.
    # You need a URL like http://vod.walla.co.il/movie/2642630/one-direction-all-for-one
    # which is only valid for several days, then the site will respond with a 404.
    # So that's why it's commented out. See comment above.
    pass

# Generated at 2022-06-14 17:39:33.111530
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE


# Generated at 2022-06-14 17:39:35.043155
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.suitable('http://url/')
    ie.extract('http://url/')
    ie.add_ie(WallaIE)

# Generated at 2022-06-14 17:39:53.738536
# Unit test for constructor of class WallaIE
def test_WallaIE():
    return WallaIE().test()

# Generated at 2022-06-14 17:40:04.029167
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._TEST['info_dict']['id'] == '2642630'
    assert ie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert ie._TEST['info_dict']['ext'] == 'flv'

# Generated at 2022-06-14 17:40:08.311627
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print("testing WallaIE class constructor.")
    ie=WallaIE()
    assert ie.ie_key() == 'walla', "Should return the correct ie key"
    print("WallaIE class constructor test passed")

# Generated at 2022-06-14 17:40:17.724633
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:40:20.730812
# Unit test for constructor of class WallaIE
def test_WallaIE():
    oIE = WallaIE()
    assert oIE.extract(_TEST['url'])['info_dict'] == _TEST['info_dict']

# Generated at 2022-06-14 17:40:21.788241
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie != None

# Generated at 2022-06-14 17:40:32.667120
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla=WallaIE()
    assert(walla._VALID_URL == "https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)")

# Generated at 2022-06-14 17:40:34.969842
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert(ie != None)


# Generated at 2022-06-14 17:40:45.126027
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla_ie = WallaIE('Unittest', 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert (walla_ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)')
    assert (walla_ie._downloader.params['noprogress'] == True)
    assert (walla_ie.suitable('Unittest') == True)
    assert (walla_ie._download_xml('http://video2.walla.co.il/?w=null/null/2642630/@@/video/flv_pl', 'one-direction-all-for-one') != None)

# Generated at 2022-06-14 17:40:49.435586
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """This function can be used to test the constructor of WallaIE. """
    from walla import WallaIE
    instance = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    return instance

# Generated at 2022-06-14 17:41:26.684568
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:41:29.366165
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    return ie

# Generated at 2022-06-14 17:41:33.001568
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:41:34.624799
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        WallaIE()
    except Exception as e:
        assert False, e

# Generated at 2022-06-14 17:41:37.236317
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:41:41.800918
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:41:53.524625
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('1', '2')._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert WallaIE('1', '2')._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:42:02.575446
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test with a video that has no subtitles.
    video_id = '2642630'
    display_id = 'one-direction-all-for-one'
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    wallaIE = WallaIE()

# Generated at 2022-06-14 17:42:05.850298
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert(obj._VALID_URL == "^https?://vod\.walla\.co\.il/[^/]+/(?P<id>\\d+)/(?P<display_id>.+)")
    assert(obj._TEST.has_key('url') == True)

# Generated at 2022-06-14 17:42:08.253036
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie is not None
    assert ie.IE_NAME == 'Walla'

# Generated at 2022-06-14 17:44:02.944470
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla_ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert walla_ie.url == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert walla_ie.VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:44:08.986006
# Unit test for constructor of class WallaIE
def test_WallaIE():
	print("\n----------------------- test_WallaIE() ----------------------------")
	walla = WallaIE()
	assert(walla.url == None)
	walla = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
	assert(walla.url == "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:44:12.871174
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    w._test_unit(WallaIE._TEST)

""" 
w = WallaIE()
w._real_initialize()
w._real_extract(WallaIE._TEST['url'])
"""

# Generated at 2022-06-14 17:44:15.695680
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    ie.extract('http://vod.walla.co.il/series/2811986/dance+moms')

# Generated at 2022-06-14 17:44:26.987224
# Unit test for constructor of class WallaIE
def test_WallaIE():
    wallaie = WallaIE('http://vod.walla.co.il/movie/2618758/one-direction-all-for-one')
    assert wallaie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert wallaie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert wallaie._TEST['info_dict']['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:44:28.601295
# Unit test for constructor of class WallaIE
def test_WallaIE():
    _ = WallaIE(WallaIE._downloader, WallaIE._VALID_URL)

# Generated at 2022-06-14 17:44:32.550460
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:44:35.358608
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE

# Generated at 2022-06-14 17:44:43.421507
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_func = InfoExtractor.test_video_ie
    class A(WallaIE):
        pass

    test_func(A, "http://vod.walla.co.il/movie/2945279/", {}, u"וואן דיירקשן: ההיסטריה")
    test_func(A, "http://vod.walla.co.il/movie/3362471/", {}, u"וואן דיירקשן: ההיסטריה")

# Generated at 2022-06-14 17:44:56.183625
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'