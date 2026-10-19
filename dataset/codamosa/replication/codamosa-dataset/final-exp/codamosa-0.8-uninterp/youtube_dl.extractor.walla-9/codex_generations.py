

# Generated at 2022-06-14 17:37:42.044143
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test download
    # WallaIE().download_test('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

    # Test _real_extract
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()

# Generated at 2022-06-14 17:37:48.141551
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.get_id() == '2642630'
    assert ie.get_display_id() == 'one-direction-all-for-one'
    assert ie.get_url() == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:37:52.865680
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'



# Generated at 2022-06-14 17:37:56.758815
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, WallaIE)

# Generated at 2022-06-14 17:38:08.398259
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from youtube_dl.utils import DownloadError

    e1 = WallaIE()
    assert e1._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:08.967577
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:38:09.961808
# Unit test for constructor of class WallaIE
def test_WallaIE():
        ie = WallaIE('0')

# Generated at 2022-06-14 17:38:10.921843
# Unit test for constructor of class WallaIE
def test_WallaIE():
	wallaIE = WallaIE()


# Generated at 2022-06-14 17:38:13.411674
# Unit test for constructor of class WallaIE
def test_WallaIE():
	obj = WallaIE(None)

# Generated at 2022-06-14 17:38:14.499383
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE(None, {})

# Generated at 2022-06-14 17:38:27.027228
# Unit test for constructor of class WallaIE
def test_WallaIE():
	print("Unit test for constructor of class WallaIE")
	print("Test passed")

test_WallaIE()

# Generated at 2022-06-14 17:38:27.723613
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:38:31.174927
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.SUCCESS == (1, 2, 3)
    assert ie.FAILURE == (4, 5, 6)

# Generated at 2022-06-14 17:38:31.784625
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:38:36.946885
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    ie = WallaIE()
    obj = ie.url_result(url)
    assert obj.display_id == 'one-direction-all-for-one'
    assert obj.id == '2642630'

# Generated at 2022-06-14 17:38:38.646914
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_object = WallaIE()
    assert test_object

# Generated at 2022-06-14 17:38:42.764916
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(None)._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'


# Generated at 2022-06-14 17:38:53.220822
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('https://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:57.314127
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie.format_id('XviD') == 'xvid'
    assert ie.format_id('SD') == 'sd'
    assert ie.format_id('720p') == '720p'

# Generated at 2022-06-14 17:38:58.690221
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:39:22.004410
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Check __init__
    obj = WallaIE()
    assert isinstance(obj, InfoExtractor)

# Generated at 2022-06-14 17:39:28.193082
# Unit test for constructor of class WallaIE
def test_WallaIE():
    class_name = 'walla'
    instance = WallaIE()
    # Check for expected attributes
    assert hasattr(instance, '_VALID_URL')
    assert hasattr(instance, '_download_webpage')
    assert hasattr(instance, '_download_xml')
    assert hasattr(instance, '_sort_formats')
    assert hasattr(instance, '_real_extract')
    assert hasattr(instance, '_SUBTITLE_LANGS')

    # Make sure that _VALID_URL is a compiled regular expression
    assert hasattr(instance._VALID_URL, 'match')


# Generated at 2022-06-14 17:39:33.856453
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one/')


# Generated at 2022-06-14 17:39:45.937847
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert isinstance(ie, WallaIE)
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:47.407760
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("WallaIE URL")
    assert ie is not None

# Generated at 2022-06-14 17:39:49.020928
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla'

# Generated at 2022-06-14 17:40:01.730188
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # pylint: disable=protected-access
    assert(WallaIE._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)')
    assert(WallaIE._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert(WallaIE._TEST['info_dict']['id'] == '2642630')
    assert(WallaIE._TEST['info_dict']['display_id'] == 'one-direction-all-for-one')
    assert(WallaIE._TEST['info_dict']['ext'] == 'flv')

# Generated at 2022-06-14 17:40:11.716144
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('WallaIE', 'WallaIE', 'WallaIE')
    assert ie.get_url() == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie.get_id() == '2642630'
    assert ie.get_display_id() == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:40:12.264462
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:40:13.119978
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE(None)


# Generated at 2022-06-14 17:40:40.738255
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:40:43.993758
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:50.781893
# Unit test for constructor of class WallaIE
def test_WallaIE():
    video_url_string = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    video_url = WallaIE._VALID_URL
    mobj = re.match(video_url, video_url_string)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert video_id == '2642630'
    assert display_id == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:40:55.996937
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    # Test functions of class WallaIE
    assert ie._real_extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:40:57.482274
# Unit test for constructor of class WallaIE
def test_WallaIE():
    '''
    Check if constructor of class WallaIE raises error
    '''
    assert WallaIE()

# Generated at 2022-06-14 17:40:59.734142
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:41:01.447079
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Check instantiation of WallaIE
    ie_Walla = WallaIE()
    assert ie_Walla

# Generated at 2022-06-14 17:41:05.313845
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.test(test_params={'skip_download': True},
                   downloader=None,
                   url='http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:41:08.044213
# Unit test for constructor of class WallaIE
def test_WallaIE():
	# prepare for the test: create a instance for WallaIE class
	ie = WallaIE()
	# the value returned must be an instance of InfoExtractor class
	assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:41:15.070486
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.description == 'walla.co.il'
    assert ie.thumbnail == 're:^https?://.*\\.jpg'
    assert ie.url_re == ie._VALID_URL
    assert ie._TEST.keys() == {
        'url', 'params', 'info_dict'
        }


# Generated at 2022-06-14 17:42:04.140907
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    instance = WallaIE()
    assert instance._VALID_URL == instance.VALID_URL
    assert instance._TEST == instance.TEST

# Generated at 2022-06-14 17:42:14.528758
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie = WallaIE(url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    ie = WallaIE(url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one', ie = None)
    ie = WallaIE(url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one', ie = InfoExtractor())
    ie = WallaIE(url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one', ie = InfoExtractor(), extra_args = None)

# Generated at 2022-06-14 17:42:18.470002
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie.url == ie._VALID_URL

# Generated at 2022-06-14 17:42:22.466596
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.url == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie.video_id == 2642630

# Generated at 2022-06-14 17:42:24.925096
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.ie_name() == 'Walla'

# Generated at 2022-06-14 17:42:26.626155
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Constructor tests
    WallaIE(WallaIE._downloader)

# Generated at 2022-06-14 17:42:30.351153
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert w._TEST == None

# Generated at 2022-06-14 17:42:33.502190
# Unit test for constructor of class WallaIE
def test_WallaIE():
    inst = WallaIE()

# Generated at 2022-06-14 17:42:40.574478
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:42:43.967979
# Unit test for constructor of class WallaIE
def test_WallaIE():
    unit_test = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    # Check the kind of the returned value
    assert type(unit_test) == WallaIE._TEST

# Generated at 2022-06-14 17:44:38.554578
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:44:47.603019
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._TEST['info_dict']['id'] == '2642630'
    assert ie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert ie._TEST['info_dict']['ext'] == 'flv'
   

# Generated at 2022-06-14 17:44:52.756440
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE({})
    assert ie.IE_NAME == 'walla'
    assert ie.VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:44:58.884942
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test extracting video info, using http://vod.walla.co.il/movie/2642630/one-direction-all-for-one as an example
    video_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    ie.extract(video_url)

    # Test constructor of class WallaIE
    ie = WallaIE()

# Generated at 2022-06-14 17:45:01.649239
# Unit test for constructor of class WallaIE
def test_WallaIE():
    return WallaIE(_test_downloader, 'http://ofek-shtainer.walla.co.il/item/2829015').test_download()

# Generated at 2022-06-14 17:45:04.093645
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'


# Generated at 2022-06-14 17:45:05.301107
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(None)._VALID_URL

# Generated at 2022-06-14 17:45:09.353195
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:45:16.249754
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE = WallaIE()
    # URL of the test case
    url = IE._TEST['url']
    assert IE.suitable(url)
    # extract info of test case
    info = IE.extract(url)
    # test that the assert_video_info function returns True
    assert_video_info(info, IE._TEST['info_dict'])


# Generated at 2022-06-14 17:45:20.206139
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test = WallaIE()
    assert isinstance(test, WallaIE)
    assert isinstance(test._VALID_URL, str)
    assert isinstance(test._TEST, dict)
    assert isinstance(test._SUBTITLE_LANGS, dict)
