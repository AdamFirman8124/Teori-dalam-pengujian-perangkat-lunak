

# Generated at 2022-06-14 17:37:33.789726
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE = WallaIE()
    assert IE.ie_key() == 'Walla'
    assert IE.ie_name() == 'Walla'
    assert IE.supported_extensions() == ['flv']

# Generated at 2022-06-14 17:37:38.065276
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http.....')
    assert ie._VALID_URL == "http?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)"
    assert ie._SUBTITLE_LANGS == {"עברית": "heb"}

# Generated at 2022-06-14 17:37:44.610617
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Create WallaIE object and check it has properties
    """
    walla_ie = WallaIE()
    assert walla_ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:37:54.300451
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Create subclass of InfoExtractor
    class WallaIE(InfoExtractor):
        pass

    # Create object of class WallaIE
    wallaIE_obj = WallaIE(downloader=None)

    # Check properties of object WallaIE
    assert wallaIE_obj._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:37:55.193089
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:38:06.683254
# Unit test for constructor of class WallaIE
def test_WallaIE():
  assert(hasattr(WallaIE, '_VALID_URL') and WallaIE._VALID_URL is not None), \
    "WallaIE._VALID_URL should be defined."
  assert(hasattr(WallaIE, '_TEST') and WallaIE._TEST is not None), \
    "WallaIE._TEST should be defined."
  assert(hasattr(WallaIE, '_SUBTITLE_LANGS') and WallaIE._SUBTITLE_LANGS is not None), \
    "WallaIE._SUBTITLE_LANGS should be defined."
  assert(hasattr(WallaIE, '_real_extract') and WallaIE._real_extract is not None), \
    "WallaIE._real_extract should be defined."

# Generated at 2022-06-14 17:38:16.316860
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # This page does not exist anymore, using a page that does
    webpage = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

    assert WallaIE._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:25.312595
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    data = 'https://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert 'walla.co.il' in data

# Generated at 2022-06-14 17:38:37.388150
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    # test for class name
    assert ie.IE_NAME == 'walla'
    # test for URL regex
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    # test for video extraction code
    assert ie._real_extract.__code__.co_argcount == 2
    # test for video subtitiles not None
    assert ie._SUBTITLE_LANGS != None
    # test for video subtitles
    assert 'עברית' in ie._SUBTITLE_LANGS
    # test for video subtitles Hebrew
    assert ie._SUBTITLE_LANGS['עברית'] == 'heb'
   

# Generated at 2022-06-14 17:38:39.835822
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    # TODO: check if constructs properly

# Generated at 2022-06-14 17:39:00.945297
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert obj._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:02.939155
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie != None

# Generated at 2022-06-14 17:39:03.616146
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE

# Generated at 2022-06-14 17:39:05.609946
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('')

# Generated at 2022-06-14 17:39:08.208605
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")


# Generated at 2022-06-14 17:39:09.013438
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE()

# Generated at 2022-06-14 17:39:12.393403
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """Test WallaIE constructor"""
    ie = WallaIE(None)
    assert ie.IE_NAME == 'walla'

# Generated at 2022-06-14 17:39:17.113990
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:25.507837
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:39:37.252378
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:50.824698
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2692713/one-direction-all-for-one')
    assert ie.VALID_URL == WallaIE._VALID_URL
    assert ie.subtitles() == WallaIE._SUBTITLE_LANGS

# Generated at 2022-06-14 17:40:02.805633
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Constructor of class
    ie = WallaIE('https://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)', 'Error in class WallaIE()'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one', 'Error in class WallaIE()'

# Generated at 2022-06-14 17:40:13.667094
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    info = ie._real_extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._SUBTITLE_LANGS['עברית'] == 'heb'
    assert info['id'] == '2642630'
    assert info['display_id'] == 'one-direction-all-for-one'
    assert info['title'] == 'וואן דיירקשן: ההיסטריה'

# Generated at 2022-06-14 17:40:17.253737
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE = WallaIE()
    assert IE._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:22.806737
# Unit test for constructor of class WallaIE
def test_WallaIE():
    new_test = WallaIE._TEST.copy()
    new_test['url'] = (
        'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    )
    new_test['info_dict'][
        'url'
    ] = (
        'rtmp://wafla.walla.co.il/vod?h=c0b5d0c2e7e70f9544a8d1f63e9fdf7b&w=2634505&v=2642630&o=27&s=1'
    )

# Generated at 2022-06-14 17:40:29.563315
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_cases = [('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')]
    for test_case in test_cases:
        info_extractor_obj = WallaIE()
        result = info_extractor_obj.suitable(test_case)
        assert result, 'Error: {} should be suitable'.format(test_case)
    print('test_WallaIE finished')

# Generated at 2022-06-14 17:40:32.047080
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:40:35.986399
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert isinstance(ie, WallaIE)


# Generated at 2022-06-14 17:40:39.923515
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract(_TEST['url'])
    #print(str(ie))

# Generated at 2022-06-14 17:40:48.593452
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    obj = ie._real_extract(ie._TEST['url'])
    url = obj['formats'][0]['url']
    assert obj['id'] == ie._TEST['info_dict']['id']
    assert obj['duration'] == ie._TEST['info_dict']['duration']
    assert re.match(r'rtmp://wafla\.walla\.co\.il/vod', url)
    assert obj['subtitles']['heb'][0]['url'] == 'http://walla.co.il/HLS/2642630/walla-video-2642630-subs.srt'

# Generated at 2022-06-14 17:41:12.088803
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, WallaIE)


# Generated at 2022-06-14 17:41:18.227256
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    ie.url = url
    mobj = re.match(ie._VALID_URL, url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert(video_id == '2642630')
    assert(display_id == 'one-direction-all-for-one')

# Generated at 2022-06-14 17:41:19.540274
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:41:22.572785
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:41:32.297772
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:41:41.078256
# Unit test for constructor of class WallaIE
def test_WallaIE():
	assert WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
	assert WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")._real_extract("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")['id'] == u'2642630'

# Generated at 2022-06-14 17:41:53.050187
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert WallaIE._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:41:53.986477
# Unit test for constructor of class WallaIE
def test_WallaIE():
    constructor_test(WallaIE)

# Generated at 2022-06-14 17:41:56.007102
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # test for instance of class WallaIE
    assert isinstance(WallaIE(), WallaIE)

# Generated at 2022-06-14 17:41:59.742222
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('https://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert isinstance(ie, WallaIE)


# Generated at 2022-06-14 17:42:22.413749
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Unit test to check the result from _real_extract method of class WallaIE

# Generated at 2022-06-14 17:42:26.451509
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE()
    assert instance._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    

# Generated at 2022-06-14 17:42:30.857618
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    w.url = url
    w._real_extract(url)

# Generated at 2022-06-14 17:42:39.203447
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    try:
        WallaIE()._real_extract(url)
    except Exception as e:
        assert False, 'WallaIE._real_extract raised %r for url %r' % (e, url)

# Generated at 2022-06-14 17:42:40.294937
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie is not None

# Generated at 2022-06-14 17:42:41.029813
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:42:43.683390
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert 'Walla' in ie.IE_NAME

# Generated at 2022-06-14 17:42:47.122799
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.__class__ == WallaIE
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:42:51.594513
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE();
    assert(ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'))

    # Test not suitable for this class
    assert(not ie.suitable('http://dummy.com'))
    assert(not ie.suitable('http://dummy.com/vod/search/news/'))



# Generated at 2022-06-14 17:42:55.535011
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .common import InfoExtractor
    ie = InfoExtractor('WallaIE', 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert isinstance(ie, WallaIE)

# Generated at 2022-06-14 17:43:45.188458
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('WallaIE').__name__ == 'WallaIE'

# Generated at 2022-06-14 17:43:46.249867
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE is not None

# Generated at 2022-06-14 17:43:47.243638
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:43:54.633851
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print("test_WallaIE: Loading WallaIE class...")

    import httplib
    import json
    import time
    import xml.etree.ElementTree
    import sys

    # Add path of walla_ie.py to Python's path
    sys.path.append("../..")
    sys.path.append("..")
    sys.path.append(".")

    from walla_ie import WallaIE
    ie = WallaIE()

    conn = httplib.HTTPConnection(ie.http_conn.host)
    conn.request("GET", "/")
    response = conn.getresponse()
    print("")
    print("Response status: " + str(response.status))
    print("Response reason: " + str(response.reason))
    print("")
    print("Response headers:")

# Generated at 2022-06-14 17:43:55.610302
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('url')

# Generated at 2022-06-14 17:43:57.197190
# Unit test for constructor of class WallaIE
def test_WallaIE():
	obj = WallaIE()
	assert isinstance(obj, InfoExtractor)

# Generated at 2022-06-14 17:44:09.349340
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    expected_display_id = 'one-direction-all-for-one'
    expected_id = '2642630'
    expected_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    expected_title = 'וואן דיירקשן: ההיסטריה'
    expected_description = 'md5:de9e2512a92442574cdb0913c49bc4d8'
    expected_thumbnail = 're:^https?://.*\.jpg'
    expected_duration = 3600
    expected_ext = 'flv'



# Generated at 2022-06-14 17:44:10.751047
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj

# Generated at 2022-06-14 17:44:14.639952
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.ie_name() == 'Walla'
    assert re.search(ie.VALID_URL, "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:44:18.962947
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # test for WallaIE constructor
    ret = WallaIE()
    assert ret.ie_key() == 'Walla'
    assert ret.ie_url() == 'http://video2.walla.co.il/'
    assert ret.SUFFIX == '.walla.co.il'
    assert ret._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'


# Generated at 2022-06-14 17:45:42.334763
# Unit test for constructor of class WallaIE
def test_WallaIE():
    #the_WallaIE = WallaIE()

    assert(True)

# Generated at 2022-06-14 17:45:45.697056
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    # ie.download(url)
    ie.download(url)

# Generated at 2022-06-14 17:45:47.293882
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == WallaIE._VALID_URL

# Generated at 2022-06-14 17:45:51.902095
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert not ie.suitable('http://vod.walla.co.il/')

# Generated at 2022-06-14 17:45:52.421082
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE

# Generated at 2022-06-14 17:45:55.467192
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    ie.extract("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:45:56.721806
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract(WallaIE._TEST['url'])

# Generated at 2022-06-14 17:45:58.838483
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """ Unit test for constructor WallaIE """
    from . import WallaIE
    WallaIE()

# Generated at 2022-06-14 17:46:02.477137
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:46:10.564945
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from urlparse import urlparse
    from walla.walla import WallaIE
    walla = WallaIE()
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    parsed_url = urlparse(url)
    if '.co.il' not in parsed_url.netloc:
        raise AssertionError("The url '{0}' does not end with '.co.il'".format(url))