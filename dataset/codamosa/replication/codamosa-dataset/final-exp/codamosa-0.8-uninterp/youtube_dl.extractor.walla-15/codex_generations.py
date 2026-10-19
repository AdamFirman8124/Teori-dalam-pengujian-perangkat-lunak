

# Generated at 2022-06-14 17:37:35.652797
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE()

# Generated at 2022-06-14 17:37:47.296673
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = ''
    ie = WallaIE(url)



# Generated at 2022-06-14 17:37:49.518915
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj.ie_key() == 'Walla'
    assert obj.ie_key() in InfoExtractor._instances
    assert isinstance(obj, InfoExtractor)

# Generated at 2022-06-14 17:37:50.310935
# Unit test for constructor of class WallaIE
def test_WallaIE():
    return WallaIE()

# Generated at 2022-06-14 17:37:56.928509
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.url_result('http://vod.walla.co.il/movie/2643154/the-lego-movie') == 'http://vod.walla.co.il/movie/2643154/the-lego-movie'
    assert ie.suitable('http://vod.walla.co.il/movie/2643154/the-lego-movie') == 'http://vod.walla.co.il/movie/2643154/the-lego-movie'

# Generated at 2022-06-14 17:38:08.490541
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Download test video from http://vod.walla.co.il/movie/2642630/one-direction-all-for-one
    video_id = 2642630
    url = "http://vod.walla.co.il/movie/" + str(video_id) + "/one-direction-all-for-one"
    walla_ie = WallaIE()
    output = walla_ie._real_extract(url)
    
    assert output["id"] == str(video_id)
    assert output["title"] == "וואן דיירקשן: ההיסטריה"

# Generated at 2022-06-14 17:38:10.964456
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:38:13.895104
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(None)._VALID_URL == WallaIE._VALID_URL

# Generated at 2022-06-14 17:38:14.558167
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:38:16.142609
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie


# Generated at 2022-06-14 17:38:27.210886
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:38:28.346852
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test = WallaIE()
    test.suite()

# Generated at 2022-06-14 17:38:40.906444
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    WallaIE()._html_search_regex(url, 'One Direction', 'title')
    WallaIE()._html_search_regex(url, 'md5:de9e2512a92442574cdb0913c49bc4d8', 'description')
    WallaIE()._html_search_regex(url, r're:^https?://.*\.jpg', 'thumbnail')
    WallaIE()._html_search_regex(url, '3600', 'duration')


if __name__ == '__main__':
    test_WallaIE()

# Generated at 2022-06-14 17:38:42.142488
# Unit test for constructor of class WallaIE
def test_WallaIE():
	InfoExtractor()

# Generated at 2022-06-14 17:38:45.656488
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie.url = url
    ie._real_extract(url)

# Generated at 2022-06-14 17:38:48.050224
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie = type(ie)(ie.ie_key())
    assert ie.ie_key() == 'Walla'



# Generated at 2022-06-14 17:38:59.629879
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    result = ie.extract(url)

    walla_video_id = 2642630
    assert result['id'] == unicode(walla_video_id)
    assert result['display_id'] == 'one-direction-all-for-one'
    assert result['title'] == u'וואן דיירקשן: ההיסטריה'

# Generated at 2022-06-14 17:39:00.536772
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE([], None)

# Generated at 2022-06-14 17:39:08.727631
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # First, try to create object with wrong url
    wrong_url = 'wrong url'
    ie = WallaIE()
    assert ie.suitable(wrong_url) == False

    # Second, create object with good url
    good_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    assert ie.suitable(good_url)

# Generated at 2022-06-14 17:39:19.420502
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:33.829125
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    ie.download("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:39:39.534688
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('WallaIE', 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.name == 'WallaIE'
    assert ie.display_id == 'one-direction-all-for-one'
    assert ie.video_id == '2642630'

    assert ie.IE_NAME == 'walla'

# Generated at 2022-06-14 17:39:42.339109
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:45.055661
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Check if unit test is able to init class
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:47.736182
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    ie.download()

# Generated at 2022-06-14 17:39:48.280465
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:39:52.043637
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('Walla', [], {}, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    WallaIE('Walla', [], {}, 'https://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:56.705338
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print(__name__)
    obj = WallaIE()
    assert isinstance(obj, InfoExtractor)

if __name__ == '__main__':
    test_WallaIE()

# Generated at 2022-06-14 17:39:58.223012
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert isinstance(w, InfoExtractor)

# Generated at 2022-06-14 17:39:59.668678
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """Test constructor of WallaIE.WallaIE"""
    WallaIE()

# Generated at 2022-06-14 17:40:27.879721
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == WallaIE._VALID_URL

# Generated at 2022-06-14 17:40:37.128314
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .common import InfoExtractor  # do not change this line
    from .common import Firefox  # do not change this line
    # do not change this line
    test_WallaIE.__module__ = InfoExtractor.__module__
    # do not change this line
    test_WallaIE.__module__ = Firefox.__module__
    # do not change this line
    InfoExtractor.__name__ = 'InfoExtractor'  # do not change this line
    # do not change this line
    Firefox.__name__ = 'Firefox'  # do not change this line
    # do not change this line
    ie = WallaIE(InfoExtractor(Firefox()))
    # do not change this line

# Generated at 2022-06-14 17:40:42.706317
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert isinstance(ie, WallaIE)
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'


# Generated at 2022-06-14 17:40:49.975321
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        # http://vod.walla.co.il/movie/2642630/one-direction-all-for-one
        w = WallaIE(
            url='http://vod.walla.co.il/movie/2642630/one-direction-all-for-one',
            params={
                # rtmp download
                'skip_download': True,
            })
    except Exception as exception:
        print('Error in WallaIE constructor: %s' % exception)
        raise exception

test_WallaIE()

# Generated at 2022-06-14 17:40:55.697986
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print('Testing WallaIE...')
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    info = ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    print(info)

# Generated at 2022-06-14 17:41:01.533167
# Unit test for constructor of class WallaIE
def test_WallaIE():
    '''
    Unit test for WallaIE constructor
    '''
    ie = WallaIE()
    if not ie.suitable("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"):
        raise AssertionError("suitable + url did not return true")
    if ie.suitable("http://vod.walla.co.il/movie/264263/one-direction-all-for-one"):
        raise AssertionError("suitable + url did not return false")
    if not ie.working():
        raise AssertionError("working did not return true")

# Generated at 2022-06-14 17:41:14.727207
# Unit test for constructor of class WallaIE
def test_WallaIE():
    x = WallaIE()
    assert x.ie_key() == 'Walla'
    assert x.ie_name() == 'vod.walla.co.il'
    assert x._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:41:20.101466
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla = WallaIE()
    mobj = re.match(walla._VALID_URL, walla._TEST['url'])
    assert mobj is not None
    walla.suitable(walla._TEST['url'])
    walla._real_extract(walla._TEST['url'])
    return True

if __name__ == '__main__':
    print(test_WallaIE())

# Generated at 2022-06-14 17:41:26.556528
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    obj = WallaIE()
    obj.suite()
    obj.test_WallaIE()
    obj._download_xml(url, 2642630)
    obj._real_extract(url)
    obj._real_extract(url)



# Generated at 2022-06-14 17:41:33.347306
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE()
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    assert instance._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    mobj = re.match(instance._VALID_URL, url)
    assert mobj.group('id') == '2642630'
    assert mobj.group('display_id') == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:42:29.492166
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:42:30.573394
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj is not None

# Generated at 2022-06-14 17:42:36.262821
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    ie = WallaIE()
    ie.extract(url)

# Generated at 2022-06-14 17:42:39.519983
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test: WallaIE has the proper constructor
    try:
        WallaIE()
    except:
        assert(False)

# Generated at 2022-06-14 17:42:47.007213
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test = WallaIE()
    test._download_xml(
        'http://video2.walla.co.il/?w=null/null/2642630/@@/video/flv_pl',
        '2642630')
    test.report_warning('Just a test warning')
    test.report_error('Just a test error')
    test.to_screen(
        'Just a test screen',
        'http://video2.walla.co.il/?w=null/null/2642630/@@/video/flv_pl')

if __name__ == "__main__":
    # The unit test of the WallaIE constructor
    test_WallaIE()
    pass

# Generated at 2022-06-14 17:42:47.902166
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('', '')

# Generated at 2022-06-14 17:42:55.195269
# Unit test for constructor of class WallaIE
def test_WallaIE():
    inst = WallaIE()
    assert inst._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:43:00.018068
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.ie_key_friendly() == 'Walla'
    assert ie.get_hostname('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one') == 'vod.walla.co.il'


# Generated at 2022-06-14 17:43:01.554327
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == WallaIE._VALID_URL
    assert WallaIE()._TEST == WallaIE._TEST

# Generated at 2022-06-14 17:43:04.164155
# Unit test for constructor of class WallaIE
def test_WallaIE():
    a = WallaIE()
    print(a.__module__)
    print(a.IE_NAME)

test_WallaIE()

# Generated at 2022-06-14 17:45:02.619842
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    ie.extract()

# Generated at 2022-06-14 17:45:05.898501
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE(url)
    assert(ie is not None)

# Generated at 2022-06-14 17:45:06.725872
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    pass

# Generated at 2022-06-14 17:45:09.022972
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.__class__.__name__ == "WallaIE"

# Generated at 2022-06-14 17:45:11.788834
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.SUCCESS == ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:45:17.348730
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._TEST['url'] == ie._VALID_URL
    obj = ie._real_extract(ie._TEST['url'])
    assert ie._TEST['info_dict'] == obj


# Generated at 2022-06-14 17:45:25.448749
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from unittest import TestCase
    from nose.tools import assert_equals, raises, assert_is_instance

    class WallaIETest(TestCase):

        def setUp(self):
            self.ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

        def test_provider(self):
            assert_equals(self.ie.provider, 'walla')

        def test_subtitles(self):
            assert_is_instance(self.ie._SUBTITLE_LANGS, dict)

    test = WallaIETest()
    test.setUp()
    test.test_provider()
    test.test_subtitles()

# Generated at 2022-06-14 17:45:35.099963
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:45:37.914518
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """ Unit test for constructor of class WallaIE. """
    url = 'http://video2.walla.co.il/?w=null/null/2642630/@@/video/flv_pl'
    video = WallaIE(url)

# Generated at 2022-06-14 17:45:43.130214
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w.get_class_regex() == [re.compile(r'^http://vod\.walla\.co\.il/movie/\d+/.+'), re.compile(r'^http://vod\.walla\.co\.il/\w+/\d+/.+'), re.compile(r'^http://vod\.walla\.co\.il/\w+/\d+/.+'), re.compile(r'^http://vod\.walla\.co\.il/\w+/\d+/.+'), re.compile(r'^http://vod\.walla\.co\.il/\w+/\d+/.+')]