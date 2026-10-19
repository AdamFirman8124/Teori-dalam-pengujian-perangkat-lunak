

# Generated at 2022-06-14 17:37:36.065361
# Unit test for constructor of class WallaIE
def test_WallaIE():
    tmp = WallaIE()
    assert tmp._SUBTITLE_LANGS == {'עברית': 'heb'}

# Generated at 2022-06-14 17:37:42.918258
# Unit test for constructor of class WallaIE
def test_WallaIE():

	# Test URL with Hebrew title
	wallaIE = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
	assert wallaIE.lang == "heb"
	assert wallaIE.display_id == "one-direction-all-for-one"
	assert wallaIE.video_id == "2642630"
	assert wallaIE._SUBTITLE_LANGS["עברית"] == "heb"
	assert wallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:37:45.028412
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.get_info(WallaIE._TEST['url']) == WallaIE._TEST['info_dict']

# Generated at 2022-06-14 17:37:46.738465
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie == WallaIE()

# Generated at 2022-06-14 17:37:51.596742
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert (WallaIE  # pylint:disable=singleton-comparison
        .ie_key() == 'walla')

# Generated at 2022-06-14 17:37:54.199127
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert(ie.ie_key() == 'Walla')
    ie.PARHS_RE = re.compile(ie.VALID_URL)

# Generated at 2022-06-14 17:37:56.539227
# Unit test for constructor of class WallaIE
def test_WallaIE(): 
    obj = WallaIE()
    return

# Generated at 2022-06-14 17:38:08.167019
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:38:18.764609
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:21.025556
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    ie.extract(url)

# Generated at 2022-06-14 17:38:36.521657
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_class = WallaIE()
    assert test_class._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:41.977347
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Unit test for class WallaIE
    """
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    instance = WallaIE()
    assert re.match(instance._VALID_URL, url)



# Generated at 2022-06-14 17:38:42.537994
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:38:46.859835
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('WallaIE', 'mp4')
    assert ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.IE_NAME == 'Walla'
    assert ie.format_id == 'mp4'

# Generated at 2022-06-14 17:38:53.728565
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print('Unit test for constructor of class WallaIE')
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    obj = WallaIE()
    ret = obj.suitable(url)
    print(ret)
    assert ret == True
    mobj = re.match(obj._VALID_URL, url)
    print(mobj.group('id'))
    print(mobj.group('display_id'))


# Generated at 2022-06-14 17:39:02.572355
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    mobj = re.match(WallaIE._VALID_URL, url)
    assert mobj is not None
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert WallaIE._download_xml(
        'http://video2.walla.co.il/?w=null/null/' + video_id + '/@@/video/flv_pl',
        display_id) is not None
    info = WallaIE._real_extract(url)
    assert '2642630' == info['id']
    assert 'one-direction-all-for-one' == info['display_id']

# Generated at 2022-06-14 17:39:03.577286
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE();
    assert(instance)


# Generated at 2022-06-14 17:39:14.373293
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:17.121473
# Unit test for constructor of class WallaIE
def test_WallaIE():
	with open("test_WallaIE.txt", "w") as f:
		f.write(WallaIE)

	print("ok")


# Generated at 2022-06-14 17:39:19.674617
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(None)._VALID_URL == WallaIE._VALID_URL
    assert WallaIE(None)._TEST == WallaIE._TEST


# Generated at 2022-06-14 17:39:42.402079
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # TODO: move unit tests to 'ytsearch' plugin
    r = WallaIE()
    assert 'WallaIE' == r.IE_NAME
    assert r._VALID_URL == r.VALID_URL or r._TEST == r.TEST

# Generated at 2022-06-14 17:39:44.089528
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')



# Generated at 2022-06-14 17:39:52.957133
# Unit test for constructor of class WallaIE
def test_WallaIE():
    
    # No WallaIE object instantiation
    
    assert WallaIE()._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:55.308740
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # A list of the constructor arguments
    wargs = ['url', 'ie_key']
    WallaIE(*wargs)
    # A list of the constructor keyword arguments
    wkwargs = ['url', 'ie_key']
    WallaIE(**wkwargs)


# Generated at 2022-06-14 17:39:55.978177
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:39:57.959074
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(_GOOD_MARKER, {}) is not None


# Generated at 2022-06-14 17:39:58.619633
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, WallaIE)
    return

# Generated at 2022-06-14 17:40:01.615464
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    print(ie._real_extract(url))

# Generated at 2022-06-14 17:40:07.617856
# Unit test for constructor of class WallaIE
def test_WallaIE():
    a = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert a.get_info('id') == '2642630'
    assert a.get_info('display_id') == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:40:08.517819
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:40:38.101333
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    
test_WallaIE()

# Generated at 2022-06-14 17:40:43.297817
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE('',{'url': 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'})
    assert w.VALID_URL == WallaIE._VALID_URL
    assert w.TEST == WallaIE._TEST
    assert WallaIE.IE_NAME == 'Walla'

# Generated at 2022-06-14 17:40:50.452446
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Creation of WallaIE instance
    """
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    mobj = re.match(WallaIE._VALID_URL, url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')

    assert(video_id == '2642630')
    assert(display_id == 'one-direction-all-for-one')

    WallaIE(WallaIE)

# Generated at 2022-06-14 17:41:00.076997
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:41:03.379493
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'



# Generated at 2022-06-14 17:41:06.884493
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert not ie.suitable('http://google.com')

# Generated at 2022-06-14 17:41:17.372755
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    res = ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert res['id'] == '2642630'
    assert res['display_id'] == 'one-direction-all-for-one'
    assert res['ext'] == 'flv'
    assert res['title'] == 'וואן דיירקשן: ההיסטריה'
    assert res['description'] == 'md5:de9e2512a92442574cdb0913c49bc4d8'

# Generated at 2022-06-14 17:41:21.900240
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download = lambda *args, **kwargs: ie.extract(*args, **kwargs)
    ie.download(ie._TEST['url'])

# Generated at 2022-06-14 17:41:23.032332
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE(InfoExtractor('1'))

# Generated at 2022-06-14 17:41:23.784834
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:42:16.035634
# Unit test for constructor of class WallaIE
def test_WallaIE():
    import sys
    import os
    import shutil
    import tempfile
    import requests
    import re

    try:
        shutil.rmtree(tempfile.gettempdir() + '/tmp')
    except OSError as e:
        if e.errno != 2:
            # Directory did not exist
            raise e

    test_file = requests.get(
        'http://video2.walla.co.il/?w=null/null/2642630/@@/video/flv_pl')

    home_dir = tempfile.gettempdir() + '/tmp'
    os.mkdir(home_dir)

    open(home_dir + '/2642630.xml', 'w+').write(test_file.text.encode('utf8'))

# Generated at 2022-06-14 17:42:17.943285
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one");

# Generated at 2022-06-14 17:42:20.410568
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:42:21.257792
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE(InformationExtractor())

# Generated at 2022-06-14 17:42:23.582809
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:42:27.308837
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Constructor of class WallaIE
    ie = WallaIE("https://www.walla.co.il")
    # The class is an instance of InfoExtractor

# Generated at 2022-06-14 17:42:30.003777
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.VALID_URL is not None
    assert ie._TEST is not None

# Generated at 2022-06-14 17:42:37.063790
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'


# Generated at 2022-06-14 17:42:43.023824
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .common import get_testdata_file
    from .default import DefaultIE
    from ..utils import (
        urlencode_postdata,
        compat_urllib_request,
        compat_urlparse,
        compat_urllib_parse,
    )
    from ..compat import (
        compat_str,
        compat_HTTPError,
    )
    from ..extractor import gen_extractors, list_extractors

    _WallaIE = WallaIE
    class WallaIEDouble(WallaIE):
        """Doubles the behavior of WallaIE"""
        def _real_extract(self, url):
            """Doubles the behavior of WallaIE._real_extract"""
            return WallaIE._real_extract(self, url)


# Generated at 2022-06-14 17:42:46.812292
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('test_WallaIE')('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')['title'] == 'וואן דיירקשן: ההיסטריה'

# Generated at 2022-06-14 17:44:36.728195
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:44:40.152645
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla'
    assert ie._VALID_URL == ie.VALID_URL
    ie = WallaIE(ie)
    assert ie.IE_NAME == 'walla'
    assert ie.ie_key() == 'Walla'

# Generated at 2022-06-14 17:44:42.935604
# Unit test for constructor of class WallaIE
def test_WallaIE():
    b = WallaIE()
    b._download_xml('http://video2.walla.co.il/?w=null/null/2642630/@@/video/flv_pl', 'one-direction-all-for-one')
    b.extract(b._TEST['url'])

# Generated at 2022-06-14 17:44:48.482274
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Assume that the constructor of InfoExtractor class has been verified
    test_video_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    test_video_id = '2642630'
    test_display_id = 'one-direction-all-for-one'
    res = WallaIE().suitable(test_video_url)
    assert res

    # Assume _real_extract method has been verified
    walla_ie = WallaIE()
    res = walla_ie._real_extract(walla_ie._VALID_URL % (test_video_id, test_display_id))
    assert res['id'] == test_video_id
    assert res['display_id'] == test_display_id

    # If

# Generated at 2022-06-14 17:44:49.672737
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:44:52.027249
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE('http://vod.walla.co.il/') is not None

# Generated at 2022-06-14 17:44:58.272578
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """Check if all the member variables were initialized correctly"""
    # Test the private member of class WallaIE
    assert WallaIE._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    # Test the instance of class WallaIE
    walla_ie = WallaIE("Input url")
    assert type(walla_ie) == WallaIE

# Generated at 2022-06-14 17:45:00.528107
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    # At the moment, don't test anything else.
    # This just checks that the constructor doesn't raise an exception

# Generated at 2022-06-14 17:45:01.419406
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE({})

# Generated at 2022-06-14 17:45:02.580707
# Unit test for constructor of class WallaIE
def test_WallaIE():
	assert WallaIE(None, None)
