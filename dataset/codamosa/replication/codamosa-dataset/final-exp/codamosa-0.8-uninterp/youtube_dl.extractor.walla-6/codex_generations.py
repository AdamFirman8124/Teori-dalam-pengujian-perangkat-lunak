

# Generated at 2022-06-14 17:37:35.944845
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'


# Generated at 2022-06-14 17:37:38.994174
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert_equals(ie._VALID_URL, r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)')

# Generated at 2022-06-14 17:37:43.636457
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Construct and return an instance of WallaIE with test url.
    """
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    obj = WallaIE()
    return obj._real_extract(url)

# Generated at 2022-06-14 17:37:44.982505
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE.__module__ == "__main__"

# Generated at 2022-06-14 17:37:49.416808
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:37:58.437897
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("https://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:01.358200
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == WallaIE.ie_key()
    assert ie.IA_NAME == WallaIE.ie_key()

# Generated at 2022-06-14 17:38:06.349280
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """unit test for WallaIE"""

    test_ie = WallaIE(WallaIE._downloader)
    # unit test for the constructor
    assert WallaIE(test_ie._downloader) is not None
    assert WallaIE._VALID_URL is not None
    assert WallaIE._SUBTITLE_LANGS is not None

# Generated at 2022-06-14 17:38:15.974090
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:18.607846
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(_download_json = lambda url: {'entries': []}) != None



# Generated at 2022-06-14 17:38:34.995815
# Unit test for constructor of class WallaIE
def test_WallaIE():
    e = WallaIE()
    assert e._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert e._TEST['info_dict']['id'] == '2642630'
    assert e._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert e._TEST['info_dict']['ext'] == 'flv'
    assert e._TEST['info_dict']['title'] == 'וואן דיירקשן: ההיסטריה'

# Generated at 2022-06-14 17:38:39.950591
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    mobj = WallaIE._VALID_URL.match(url)
    assert mobj.group('id') == '2642630'
    assert mobj.group('display_id') == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:38:43.334444
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert(ie.url_re.match('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one').group('id') == '2642630')

# Generated at 2022-06-14 17:38:49.462894
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Set some arguments for the WallaIE constructor
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    ie.urls = [url]
    # Get a webpage
    webpage = ie._download_webpage(url, None, False)
    # Process it
    ie._real_extract(webpage)

# Generated at 2022-06-14 17:38:58.912272
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Unit test for constructor of class WallaIE - test for no inputs to constructor (default values)
    # INPUT:  constructor has no inputs
    # OUTPUT: info about class (name, id and url regex groups) and _SUBTITLE_LANGS dict are saved to an object with default values
    wallaIE = WallaIE()
    assert wallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert wallaIE._SUBTITLE_LANGS == {
        'עברית': 'heb',
    }

# Generated at 2022-06-14 17:39:13.054389
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:14.921849
# Unit test for constructor of class WallaIE
def test_WallaIE():
    pass

# Generated at 2022-06-14 17:39:16.207882
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:39:17.043302
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.test()

# Generated at 2022-06-14 17:39:17.925046
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla = WallaIE()

# Generated at 2022-06-14 17:39:30.269331
# Unit test for constructor of class WallaIE
def test_WallaIE():
    o = WallaIE()
    assert o.SUCCESS_ONLY_VIDEO == False

# Generated at 2022-06-14 17:39:35.567059
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    mobj = re.match(ie._VALID_URL, url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert '2642630' == video_id
    assert 'one-direction-all-for-one' == display_id

# Generated at 2022-06-14 17:39:44.749157
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # this test is also used in extractor/common.py
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert ie.url == "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    assert ie.valid_url("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:39:47.125746
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:48.185532
# Unit test for constructor of class WallaIE
def test_WallaIE():
    global WallaIE
    WallaIE()

# Generated at 2022-06-14 17:39:49.426010
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE() 

# Test "test_method" of class WallaIE

# Generated at 2022-06-14 17:39:51.854665
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == "^https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)"

# Generated at 2022-06-14 17:39:56.237615
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        extractor = WallaIE({})
    except NameError as e:
        assert e.message == "global name 'InfoExtractor' is not defined"

# Generated at 2022-06-14 17:40:01.460115
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    ie._real_extract("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    # assert ie._VALID_URL:
    # assert ie._TEST:

# Generated at 2022-06-14 17:40:05.474243
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:40:41.262795
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:40:51.115853
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:56.523227
# Unit test for constructor of class WallaIE
def test_WallaIE():
	print("Unit test for constructor of class WallaIE")

if __name__ == '__main__':
	t1 = time.time()
	test_WallaIE()
	t2 = time.time()
	print("---------------------------------------------")
	print("Total time: {0:.2f} seconds".format(t2-t1))
	print("---------------------------------------------")

# Generated at 2022-06-14 17:40:58.821379
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(InfoExtractor())._VALID_URL

# Generated at 2022-06-14 17:41:02.023226
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Constructor test
    """

    # Constructor test
    ie = WallaIE()

    # run test
    assert ie.IE_NAME == 'walla'
    assert ie.IE_DESC == 'Walla! Video'

# Generated at 2022-06-14 17:41:05.164650
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    print("\n" + ie.__str__())

# Generated at 2022-06-14 17:41:06.208124
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE

# Generated at 2022-06-14 17:41:07.153653
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert 'WallaIE' in globals()

# Generated at 2022-06-14 17:41:14.923537
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # testing the content of the constructor
    # (not the functionality of the module)
    # no need to check __doc__ and _VERSION

    # check field regex
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

    # check field _SUBTITLE_LANGS
    assert WallaIE._SUBTITLE_LANGS == {'עברית': 'heb'}

    # check field _TEST

# Generated at 2022-06-14 17:41:17.373386
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie._SUBTITLE_LANGS
    assert ie._SUBTITLE_LANGS == {'עברית': 'heb'}


# Generated at 2022-06-14 17:42:08.839950
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:42:11.269755
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla_ie = WallaIE()
    walla_ie._download_xml = lambda url: None
    assert(walla_ie is not None)


# Generated at 2022-06-14 17:42:12.122152
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:42:14.687077
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test = WallaIE()

# Generated at 2022-06-14 17:42:16.236606
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie is not None

# Generated at 2022-06-14 17:42:24.467874
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:42:27.897391
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    wallaie = WallaIE()
    wallaie.extract(url)

# Generated at 2022-06-14 17:42:33.331278
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    WallaIE().suitable(url)
    WallaIE._VALID_URL.match(url)
    WallaIE._download_xml(url, WallaIE._VALID_URL.match(url).group('display_id'))

# Generated at 2022-06-14 17:42:40.431469
# Unit test for constructor of class WallaIE
def test_WallaIE():
    a = WallaIE()
    assert a._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:42:51.150787
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:44:52.027861
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # These two lines are commented out until we can pass the test
    # (further details in https://github.com/rg3/youtube-dl/issues/5664)
    # wie = WallaIE()
    # wie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    pass

# Generated at 2022-06-14 17:44:53.869716
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download(WallaIE._TEST['url'])

# Generated at 2022-06-14 17:44:58.698865
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\\d+)/(?P<display_id>.+)'
    assert ie._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:45:01.396545
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE("Walla")
    assert obj.ie_key() == 'Walla'

# Generated at 2022-06-14 17:45:05.008759
# Unit test for constructor of class WallaIE
def test_WallaIE():
    '''
    Test WallaIE constructor
    '''
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.ie_name() == 'Walla'
    assert ie.determine_ext() == 'flv'

# Generated at 2022-06-14 17:45:06.559285
# Unit test for constructor of class WallaIE
def test_WallaIE():
    testEntry = WallaIE()._TEST
    url = testEntry['url']
    video = WallaIE()._real_extract(url)
    assert video == testEntry

# Generated at 2022-06-14 17:45:08.897773
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._VALID_URL
    assert ie._SUBTITLE_LANGS

# Generated at 2022-06-14 17:45:21.006312
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # First test: downloading link to an Israeli movie named 'King Lear'
    # ---------------------------------------------------------------
    url = 'http://vod.walla.co.il/movie/2779540/king-lear'
    ie = WallaIE(url)

    info_dict = ie.extract(url)

    assert info_dict['id'] == '2779540'
    assert info_dict['display_id'] == 'king-lear'
    assert info_dict['ext'] == 'flv'

    # Second test: downloading link to an Israeli TV show named 'The Golden Girls'
    # ---------------------------------------------------------------
    url = 'http://vod.walla.co.il/show/2667792/the-golden-girls'
    ie = WallaIE(url)

    info_dict = ie.extract(url)


# Generated at 2022-06-14 17:45:23.600335
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_WallaIE = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    return test_WallaIE

# Generated at 2022-06-14 17:45:34.435604
# Unit test for constructor of class WallaIE
def test_WallaIE():
    display_id = "one-direction-all-for-one"
    video_id = 2642630
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    # Create a video
    video = WallaIE(url)
    # Create expected video dictionary