

# Generated at 2022-06-14 17:37:39.497549
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'walla'
    assert ie.ie_name() == 'walla.co.il'
    assert ie.ie_description() == 'walla.co.il'
    assert ie.is_initialized() == False

# Generated at 2022-06-14 17:37:40.701997
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:37:41.730090
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()


# Generated at 2022-06-14 17:37:43.972326
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:37:53.717913
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie.IE_NAME == 'walla'
    # WallaIE.TEST = {
    #     'url': 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one',
    #     'info_dict': {
    #         'id': '2642630',
    #         'display_id': 'one-direction-all-for-one',
    #         'ext': 'flv',
   

# Generated at 2022-06-14 17:37:55.874892
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

test_WallaIE()

# Generated at 2022-06-14 17:38:01.341061
# Unit test for constructor of class WallaIE
def test_WallaIE():
    description = "test description"
    duration = "test duration"
    title = "test title"
    thumbnail = "test thumbnail"
    video_id = "test video_id"
    display_id = "test display_id"


    class test_video_xml(object):
        def __init__(item):
            item.title = title
            item.duration = duration
            item.synopsis = description
            item.preview_pic = thumbnail

    class test_quality_xml(object):
        def __init__(quality):
            quality.title = "test format"
            quality.src = "test src"

        def xpath(quality, xpath):
            if xpath == './/src':
                return [quality.src]
            elif xpath == './/title':
                return [quality.title]
            


# Generated at 2022-06-14 17:38:03.401140
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        WallaIE()
    except:
        assert False
    assert True



# Generated at 2022-06-14 17:38:12.430578
# Unit test for constructor of class WallaIE
def test_WallaIE():
    import unittest
    class TestWallaIE(unittest.TestCase):
        def setUp(self):
            self.ie = WallaIE()

        def test_name(self):
            self.assertEqual(self.ie.IE_NAME, 'Walla!')

        def test_url_regex(self):
            self.assertEqual(WallaIE._VALID_URL, ('https?://vod\.walla\.co\.il/'
                                                  '[^/]+/(?P<id>\d+)/(?P<display_id>.+)'))
    unittest.main()

# Generated at 2022-06-14 17:38:14.274406
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

test_WallaIE()

# Generated at 2022-06-14 17:38:31.619226
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.url == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie.display_id == 'one-direction-all-for-one'
    assert ie.video_id == '2642630'

# Generated at 2022-06-14 17:38:43.420574
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:38:55.072428
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:04.126706
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    assert(ie.suitable(url))
    mobj = re.match(ie._VALID_URL, url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert(ie._TEST['url'] == url)
    assert(ie._TEST['info_dict']['id'] == video_id)
    assert(ie._TEST['info_dict']['display_id'] == display_id)
    assert(ie._TEST['info_dict']['title'] == ie.extract(url)['title'])

# Generated at 2022-06-14 17:39:10.235441
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert(ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)')
    assert(ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:11.768662
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # TODO
    pass

# Generated at 2022-06-14 17:39:23.438334
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("")
    assert hasattr(ie, '_VALID_URL'), "WallaIE class is missing the VALID_URL definition"
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)', "WallaIE class VALID_URL definition is missing the vod.walla.co.il part"
    assert hasattr(ie, '_SUBTITLE_LANGS'), "WallaIE class is missing the SUBTITLE_LANGS definition"
    assert hasattr(ie, '_TEST'), "WallaIE class is missing the TEST definition"
    assert hasattr(ie, '_real_extract'), "WallaIE class is missing the extract method"
    assert hasattr

# Generated at 2022-06-14 17:39:33.915657
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie_new = ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie_new, 'It is a suitable url'
    ie_new = ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie_new, 'It is a suitable url'
    ie_new = ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie_new, 'It is a suitable url'


# Generated at 2022-06-14 17:39:35.202508
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:39:40.795157
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    wie = WallaIE()
    assert wie.suitable(url)
    mo = wie._VALID_URL.match(url)
    assert mo
    assert mo.group('id') == '2642630'
    assert mo.group('display_id') == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:39:54.195775
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie = WallaIE("WallaIE")


# Generated at 2022-06-14 17:40:04.282706
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.ie_key() == 'walla'
    assert ie.SUITABLE_VIDEO_URL == WallaIE._VALID_URL
    assert ie.SUBTITLE_LANGS == WallaIE._SUBTITLE_LANGS
    assert ie.BASE_URL == 'http://vod.walla.co.il/'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/index.php/%s/videoPlayer/%s/%s/%s/?%s'
    assert ie.BRIGHTCOVE_EMBED_CODE == '4179188223001'
    assert ie

# Generated at 2022-06-14 17:40:09.643490
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._SUBTITLE_LANGS['עברית'] == 'heb'
    ie = WallaIE(None)
    assert ie._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:40:19.557689
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:20.280904
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:40:21.508732
# Unit test for constructor of class WallaIE
def test_WallaIE():
    r = WallaIE()
    assert r is not None

# Generated at 2022-06-14 17:40:25.816830
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # URL to be tested
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    # Object creation and initialization
    walla_ie = WallaIE()
    walla_ie._download_xml = lambda a, b: None
    walla_ie._real_extract(test_url)

# Generated at 2022-06-14 17:40:35.647824
# Unit test for constructor of class WallaIE
def test_WallaIE():
    unit = WallaIE(InfoExtractor())
    assert unit._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:40.262731
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:40:41.417546
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie != None


# Generated at 2022-06-14 17:41:04.483519
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Unit test for constructor of WallaIE
    """
    w = WallaIE()
    assert w == WallaIE
    


# Generated at 2022-06-14 17:41:13.233691
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla:video'  # Since the features are identical, we use the same class
    ie._downloader.params.update( { 'noplaylist': True } )
    # Should behave just like walla:video
    ie._VALID_URL = r'http://vod\.walla\.co\.il/[^/]+/[^/]*/[^/]+'

# Generated at 2022-06-14 17:41:18.115038
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print("\nStart Unit test for WallaIE")
    obj = WallaIE()
    assert 'walla' in obj._downloader.IE_NAME
    assert 'Walla' in obj._downloader.IE_NAME

    assert 'walla' in obj._WORKING_IE_NAME
    assert 'Walla' in obj._WORKING_IE_NAME
    print("Unit test for WallaIE is complete")


# Generated at 2022-06-14 17:41:22.363444
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:41:26.452719
# Unit test for constructor of class WallaIE
def test_WallaIE():
	w = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
	assert "WallaIE" in str(w)

if __name__ == '__main__':
	test_WallaIE()

# Generated at 2022-06-14 17:41:27.861195
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w.expected_results == 1

# Generated at 2022-06-14 17:41:30.686419
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE(url)
    assert ie.url == url

# Generated at 2022-06-14 17:41:31.389810
# Unit test for constructor of class WallaIE
def test_WallaIE():
    global WallaIE
    w = WallaIE("")

# Generated at 2022-06-14 17:41:38.682787
# Unit test for constructor of class WallaIE
def test_WallaIE():
    '''
    Unit test for constructor of class WallaIE.
    '''
    # URL of video: http://vod.walla.co.il/movie/2642630/one-direction-all-for-one
    url_video = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"

    # Create the object WallaIE
    obj = WallaIE({})

    # Check the url
    obj._match_id(url_video)
    assert obj._match_id(url_video)

# Generated at 2022-06-14 17:41:40.538939
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL

# Generated at 2022-06-14 17:42:34.661057
# Unit test for constructor of class WallaIE
def test_WallaIE():
    wie = WallaIE()
    assert wie.SUCCESS == True

# Generated at 2022-06-14 17:42:39.293596
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .common import url_for_test
    url = url_for_test(WallaIE, {'display_id': 'one-direction-all-for-one'})
    WallaIE()._download_xml(url, '2642630')

# Generated at 2022-06-14 17:42:40.401711
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:42:51.119341
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:42:54.284195
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Unit test for constructor of class WallaIE
    """
    ie = WallaIE()
    ie.suite()

# Generated at 2022-06-14 17:42:56.083696
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract(WallaIE._TEST['url'])

# Generated at 2022-06-14 17:42:58.453363
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    var = ie._real_extract(ie._TEST['url'])
    assert var == ie._TEST['info_dict']

# Generated at 2022-06-14 17:43:01.316701
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')._VALID_URL == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:43:03.907791
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE()
    # logger.debug("Unit test for WallaIE: %s" % instance)
    instance.suite()

# Generated at 2022-06-14 17:43:06.637589
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """ Constructor test for WallaIE """
    ie = WallaIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, WallaIE)

# Generated at 2022-06-14 17:45:01.068087
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:45:01.960016
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()


# Generated at 2022-06-14 17:45:06.834786
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:45:09.146221
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla_ie = WallaIE(InfoExtractor())
    assert walla_ie.extractor == 'walla'

# Generated at 2022-06-14 17:45:10.658247
# Unit test for constructor of class WallaIE
def test_WallaIE():
    return WallaIE(WallaIE._downloader)._real_initialize(WallaIE._TEST['url'])

# Generated at 2022-06-14 17:45:18.255636
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE(test_url)
    assert ie.url == test_url

    # Test seting of download parameters
    params = {
        'skip_download': True,
    }
    ie.set_params(params)
    assert ie.params == params

# Generated at 2022-06-14 17:45:22.141367
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one') == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:45:33.727328
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_input = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()

    ie_url = ie._VALID_URL
    ie_id = ie._TEST['info_dict']['id']
    ie_display_id = ie._TEST['info_dict']['display_id']

    mobj_url = re.match(ie_url, test_input)

    mobj_id = mobj_url.group('id')
    mobj_display_id = mobj_url.group('display_id')

    assert(ie_id == mobj_id and ie_display_id == mobj_display_id)

# Generated at 2022-06-14 17:45:41.328663
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._TEST['info_dict']['id'] == '2642630'
    assert ie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert ie._TEST['info_dict']['ext'] == 'flv'

# Generated at 2022-06-14 17:45:47.338077
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Note: we are not actually testing the object is a WallaIE object.
    #  The constructor for the InfoExtractor is actually being tested,
    #  but since we are explicitly passing the WallaIE class to the constructor
    #  we are actually testing WallaIE specific stuff.
    test_item = WallaIE('WALLA', WallaIE._TEST)
    assert test_item.url == WallaIE._TEST['url']
    return test_item