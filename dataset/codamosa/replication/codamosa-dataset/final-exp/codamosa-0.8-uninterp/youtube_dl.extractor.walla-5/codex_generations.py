

# Generated at 2022-06-14 17:37:35.504484
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()


# Generated at 2022-06-14 17:37:40.694417
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Unit test for class 'WallaIE'
    walla = WallaIE()
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    # test if the url is valid
    assert walla._match_id(url) is not None
    # testing the extraction of the names of the sub-titles
    assert walla._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:37:43.394581
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:37:46.376220
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert IE == 'WallaIE'

# Generated at 2022-06-14 17:37:51.542630
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'walla'

# Generated at 2022-06-14 17:37:59.213977
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:00.804628
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        WallaIE()
        assert False
    except:
        pass

# Generated at 2022-06-14 17:38:01.926409
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:38:03.038503
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:38:07.406045
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:38:24.804363
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:26.677297
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE();
    assert(ie != None)

# Generated at 2022-06-14 17:38:28.301375
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('test')

# Generated at 2022-06-14 17:38:39.724385
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:41.838527
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:38:44.739770
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'walla'
    assert ie.ie_name() == 'walla'
    assert callable(ie.suitable)

# Generated at 2022-06-14 17:38:55.020290
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test = WallaIE()
    test._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:01.604121
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w._SUBTITLE_LANGS['עברית'] == 'heb'
    assert w.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')['duration'] == 3600
    assert 'all-for-one' in w.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')['display_id']

# Generated at 2022-06-14 17:39:06.066481
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:39:07.501973
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('WallaIE').IE_NAME == "WallaIE"

# Generated at 2022-06-14 17:39:36.044331
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    info = w._real_extract(url)
    assert type(info) is dict
    assert info['id'] == '2642630'
    assert info['ext'] == 'flv'
    assert info['title'] == 'וואן דיירקשן: ההיסטריה'
    assert info['duration'] == 3600
    assert type(info['thumbnail']) is str

# Generated at 2022-06-14 17:39:43.928596
# Unit test for constructor of class WallaIE
def test_WallaIE():
    theParsedUrl = re.match(WallaIE._VALID_URL, WallaIE._TEST['url'])
    assert(theParsedUrl)  # URL is valid
    assert(theParsedUrl.group('id') == '2642630')  # Video id exists
    assert(theParsedUrl.group('display_id') == 'one-direction-all-for-one')  # Display id exists

# Generated at 2022-06-14 17:39:44.556999
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:39:53.233231
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    video_id = '2642630'
    display_id = 'one-direction-all-for-one'
    test = WallaIE()
    test._match_id(url)
    assert test._VALID_URL == r'^https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)$'
    assert test._TEST is not None
    assert test._SUBTITLE_LANGS['עברית'] == 'heb'
    assert test._real_extract(url) is not None
    assert test._real_extract(url)['id'] == video_id


# Generated at 2022-06-14 17:39:55.499214
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:39:57.025023
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .common import test_IE
    test_IE([WallaIE])

# Generated at 2022-06-14 17:40:01.695732
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/one-direction-all-for-one/2642630'
    ie = WallaIE(url)
    assert ie.url == url
    assert ie.video_id == '2642630'
    assert ie.display_id == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:40:03.454303
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE().extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')['title'] == 'וואן דיירקשן: ההיסטריה'

# Generated at 2022-06-14 17:40:07.617370
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    # Just check if it is defined and not empty
    try:
      assert ie
      assert ie._SUBTITLE_LANGS
    except Exception:
      assert False

# Generated at 2022-06-14 17:40:10.455992
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('','', -1, -1, -1, -1, -1, -1, -1, '', '')

# Generated at 2022-06-14 17:41:00.179964
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:41:04.759748
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_url = 'https://www.youtube.com/watch?v=W8SVxjnUd-k'
    test_result = WallaIE(test_url)

    # Tests object type
    assert isinstance(test_result, InfoExtractor)

# Generated at 2022-06-14 17:41:07.185307
# Unit test for constructor of class WallaIE
def test_WallaIE():
	assert 0 == WallaIE()._VALID_URL


# Generated at 2022-06-14 17:41:13.615359
# Unit test for constructor of class WallaIE
def test_WallaIE():
	"""
	This function checks if all the fields needed before and after the extraction are created.
	"""
	assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
	assert WallaIE._SUBTITLE_LANGS == {'עברית': 'heb'}

# Generated at 2022-06-14 17:41:19.337579
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # It would be nice to be able to mock the class instead of creating a new one every time but I did not figure out a way to do it
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

    assert("http://video2.walla.co.il/?w=null/null/2642630/@@/video/flv_pl" == ie.url)
    assert("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one" == ie.url_)
    assert("/2642630/one-direction-all-for-one" == ie.report_download_webpage_read_failure.__defaults__[1][0])


# Generated at 2022-06-14 17:41:22.364480
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:41:27.578157
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:41:38.319596
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.get_id() == '2642630'
    assert ie.get_title() == 'וואן דיירקשן: ההיסטריה'
    assert ie.get_duration() == 3600
    assert ie.get_thumbnail() == r'^https?://.*\.jpg'
    assert ie.get_description() == 'md5:de9e2512a92442574cdb0913c49bc4d8'

# Generated at 2022-06-14 17:41:44.117647
# Unit test for constructor of class WallaIE
def test_WallaIE():
    info = WallaIE().extract('http://vod.walla.co.il/?w=null/null/2655893/@@/video/flv_pl')
    assert info['id'] == '2655893'
    assert info['subtitles'] == {}

# Generated at 2022-06-14 17:41:52.092505
# Unit test for constructor of class WallaIE
def test_WallaIE():
    iframe, url = WallaIE()._extract_m3u8_formats(
        "hds",
        "http://vod.walla.co.il/movie/2644576/jingle-all-the-way",
        "2644576")
    assert iframe is None
    assert url == "http://vod.walla.co.il/movie/2644576/jingle-all-the-way?w=960/null/null/@@/video/flv_pl.m3u8"

# Generated at 2022-06-14 17:42:49.271846
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    pass

# Generated at 2022-06-14 17:42:57.280563
# Unit test for constructor of class WallaIE
def test_WallaIE():

    ie = WallaIE()

    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:42:57.806888
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE();

# Generated at 2022-06-14 17:42:59.677794
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE("vod.walla.co.il")._VALID_URL == "http://vod.walla.co.il/*"

# Generated at 2022-06-14 17:43:02.894315
# Unit test for constructor of class WallaIE
def test_WallaIE():
    for test in WallaIE._TEST:
        _ = WallaIE.suitable(test)
        assert True

# Generated at 2022-06-14 17:43:05.343877
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    className = ie.__class__.__name__
    assert ie.__class__.__name__ == className

# Generated at 2022-06-14 17:43:07.366526
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert(w._VALID_URL == re.compile(r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'))

# Generated at 2022-06-14 17:43:08.033421
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:43:18.586647
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert walla._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:43:19.838975
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE

# Generated at 2022-06-14 17:44:27.458259
# Unit test for constructor of class WallaIE
def test_WallaIE():
    video_id = '2642630'
    info_dict = {
        'id': '2642630',
        'display_id': 'one-direction-all-for-one',
        'ext': 'flv',
        'title': 'וואן דיירקשן: ההיסטריה',
        'description': 'md5:de9e2512a92442574cdb0913c49bc4d8',
        'thumbnail': r're:^https?://.*\.jpg',
        'duration': 3600,
    }
    assert WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')._TEST == info_dict

# Generated at 2022-06-14 17:44:29.057159
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    result = w.ie_key()
    assert result == 'WallaIE'

# Generated at 2022-06-14 17:44:30.574965
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == WallaIE._VALID_URL

# Generated at 2022-06-14 17:44:33.485271
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:44:38.150703
# Unit test for constructor of class WallaIE
def test_WallaIE():
    e = WallaIE()
    assert e.__class__.__name__ == 'WallaIE'
# test WallaIE for url "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"

# Generated at 2022-06-14 17:44:38.625580
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:44:47.627415
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:44:48.811258
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w != None

# Generated at 2022-06-14 17:44:49.430773
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:44:51.944947
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj is not None


# Generated at 2022-06-14 17:47:01.623305
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:47:03.431741
# Unit test for constructor of class WallaIE
def test_WallaIE():
    i = WallaIE(None)
    assert isinstance(i, InfoExtractor)

# Generated at 2022-06-14 17:47:10.188574
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test the constructor of class WallaIE
    # Input: 
    #    url: http://vod.walla.co.il/movie/2642630/one-direction-all-for-one
    # Expected:
    #    videoID: 2642630
    #    videoDisplayID: one-direction-all-for-one
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    youtube_ie = WallaIE(url)

# Generated at 2022-06-14 17:47:14.124911
# Unit test for constructor of class WallaIE
def test_WallaIE():
    video_id = '2642630'
    display_id = 'one-direction-all-for-one'
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    t = WallaIE()
    t.extract(url)

# Generated at 2022-06-14 17:47:15.480786
# Unit test for constructor of class WallaIE
def test_WallaIE():
	f = WallaIE()


# Generated at 2022-06-14 17:47:16.345598
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie is not None

# Generated at 2022-06-14 17:47:26.330480
# Unit test for constructor of class WallaIE
def test_WallaIE():
    _VALID_URL = r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'