

# Generated at 2022-06-14 16:13:38.314222
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    obj = FourTubeBaseIE()
    print(FourTubeBaseIE.__name__)
    print(obj.__class__)

# Generated at 2022-06-14 16:13:39.104220
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE(None)

# Generated at 2022-06-14 16:13:40.094900
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE(FourTubeBaseIE()) is not None

# Generated at 2022-06-14 16:13:41.717999
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    fourTubeIE = FourTubeIE()
    print(fourTubeIE.__class__.__name__)

# Generated at 2022-06-14 16:13:43.011328
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    try:
        FourTubeIE()
    except Exception as e:
        pass



# Generated at 2022-06-14 16:13:48.080999
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    test_instance = FourTubeIE()
    assert test_instance.IE_NAME == '4tube'
    assert test_instance.IE_DESC == '4tube.com'



# Generated at 2022-06-14 16:13:50.141890
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    t = FourTubeIE()
    assert t.IE_NAME == '4tube'



# Generated at 2022-06-14 16:13:50.601663
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE()

# Generated at 2022-06-14 16:13:57.748872
# Unit test for constructor of class FuxIE
def test_FuxIE():
    test_obj = FuxIE('http://www.fux.com/videos/195359/awesome-fucking-kitchen-ends-cum-swallow')
    attributes = ['_VALID_URL', 'IE_NAME', '_TKN_HOST', '_URL_TEMPLATE', '_TESTS']
    for attribute in attributes:
        assert test_obj.__getattribute__(attribute) == FuxIE.__getattribute__(attribute)

# Generated at 2022-06-14 16:13:58.448442
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE()

# Generated at 2022-06-14 16:14:16.145711
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE('http://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')

# Generated at 2022-06-14 16:14:17.850899
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    a = FourTubeIE()

# Generated at 2022-06-14 16:14:18.445400
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:14:19.489138
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()


# Generated at 2022-06-14 16:14:21.783626
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros_ie = PornerBrosIE()
    pornerbros_ie.get_url_1()



# Generated at 2022-06-14 16:14:22.453263
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:14:30.289764
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    from .test_download import assertRaisesRegexp
    assertRaisesRegexp(
        AssertionError, 'PornerBrosIE is only for PornerBros websites and not for PornerBros.com',
        PornerBrosIE, 'http://pornerbros.com/')
    assertRaisesRegexp(
        AssertionError, 'PornerBrosIE is only for PornerBros websites and not for PornerBros.com',
        PornerBrosIE, 'http://www.pornerbros.com/')
    assertRaisesRegexp(
        AssertionError, 'PornerBrosIE is only for PornerBros websites and not for Pornerbros.com',
        PornerBrosIE, 'http://www.pornerbros.com/')
   

# Generated at 2022-06-14 16:14:38.584367
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Cover case without self._URL_TEMPLATE
    class TestFourTubeIE(FourTubeIE):
        IE_NAME = 'Test'
        _VALID_URL = r''
    ie = TestFourTubeIE()
    assert ie._build_url == ie._default_build_url
    # Cover case with self._URL_TEMPLATE
    class TestFourTubeIE(FourTubeIE):
        IE_NAME = 'Test'
        _VALID_URL = r''
        _URL_TEMPLATE = 'Test'
    ie = TestFourTubeIE()
    assert ie._build_url != ie._default_build_url
    assert ie._build_url(1010101) == "Test"

# Generated at 2022-06-14 16:14:48.320104
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .common import InfoExtractor
    from .. import compat_str
    from ..compat import compat_b64decode
    from ..utils import parse_duration
    from ..compat import compat_urllib_parse_unquote
    from ..compat import compat_urllib_parse_urlparse
    import re
    import json

    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    mobj = re.match(FourTubeIE._VALID_URL, url)
    video_id = mobj.group('id')

    _url = 'http://www.4tube.com/videos/%s/video' % video_id

# Generated at 2022-06-14 16:14:48.928570
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:15:17.392023
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE(None, None)

# Generated at 2022-06-14 16:15:21.601537
# Unit test for constructor of class FuxIE
def test_FuxIE():
    video_id = '195359'
    url = 'https://www.fux.com/videos/squirting-teen-ballerina-ecg_1331406'
    ie = FuxIE()
    data = ie._real_extract(url)
    # test that the id of the video is the same as the one from the url
    assert data['id'] == video_id

# Generated at 2022-06-14 16:15:23.027319
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE()
    assert fux._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:15:27.189522
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE()._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert FourTubeIE()._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert FourTubeIE()._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:15:28.790483
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fuxIE = FuxIE()
    fuxIE.IE_NAME = "FuxIE"
    assert fuxIE.IE_NAME == "FuxIE"


# Generated at 2022-06-14 16:15:30.410372
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert isinstance(ie, PornTubeIE)
    assert isinstance(ie, FourTubeBaseIE)
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:15:31.144969
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux_ie = FuxIE()

# Generated at 2022-06-14 16:15:32.800128
# Unit test for constructor of class FuxIE
def test_FuxIE():
    data = 'www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    assert FuxIE(data)._VALID_URL

# Generated at 2022-06-14 16:15:38.044408
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert ie._TKN_HOST == 'token.pornerbros.com'



# Generated at 2022-06-14 16:15:45.338904
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assertie.IE_NAME == '4tube'
    assertie._TKN_HOST == 'token.4tube.com'
    assertie._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assertie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'

# Generated at 2022-06-14 16:16:48.106638
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux_url = "https://www.fux.com/video/152702/black-girl-axa-jays-first-anal-scene"
    ie = FuxIE(fux_url)
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:16:57.004432
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux_ie = FuxIE()
    assert fux_ie.IE_NAME == 'Fux'
    assert fux_ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fux_ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fux_ie._TKN_HOST == 'token.fux.com'

if __name__ == '__main__':
    test_FuxIE()

# Generated at 2022-06-14 16:17:01.789028
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    f = FourTubeIE("https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")
    assert f._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert f._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert f._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:17:02.336861
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
	FourTubeIE.suite()


# Generated at 2022-06-14 16:17:02.948864
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()


# Generated at 2022-06-14 16:17:05.769330
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    url = 'http://www.pornerbros.com/videos/hottie-loves-to-suck-cock-and-get-fucked-hard_224566'
    pornerbros_ie = PornerBrosIE(url)


# Generated at 2022-06-14 16:17:15.424105
# Unit test for constructor of class FuxIE
def test_FuxIE():
    video_id = 'x'
    tkn_host = 'a'
    url_template = 'y'
    valid_url = 'z'

    fux = FuxIE()

    assert fux.IE_NAME == '4tube'
    assert fux._VALID_URL == valid_url
    assert fux._URL_TEMPLATE == url_template
    assert fux._TKN_HOST == tkn_host

# Generated at 2022-06-14 16:17:18.108584
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    o = FourTubeIE()
    if o is not None:
        print('Successfully instantiated')
    else:
        print('Failed to instantiate')

# Generated at 2022-06-14 16:17:21.009532
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from .test_PornTubeIE import PornTubeIE
    obj = PornTubeIE('PornTube')
    obj._download_webpage()

# Generated at 2022-06-14 16:17:28.535710
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE.__name__ is 'FuxIE'
    assert FuxIE._VALID_URL is 'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert FuxIE._URL_TEMPLATE is 'https://www.fux.com/video/%s/video'
    assert FuxIE._TKN_HOST is 'token.fux.com'

# Generated at 2022-06-14 16:18:57.853504
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    from .common import InfoExtractor
    from .common import FakeIE
    from .common import FakeInfoExtractor
    from .common import FakeService
    from .common import FakeServiceIE

    assert issubclass(FourTubeBaseIE, ServiceIE)

    # Create empty class
    # Test that constructor of ServiceIE is called
    class FakeIE(FourTubeBaseIE):
        pass

    assert isinstance(FakeIE, InfoExtractor)
    assert isinstance(FakeIE, FakeInfoExtractor)
    assert isinstance(FakeIE, FakeServiceIE)
    assert isinstance(FakeIE, ServiceIE)

    # Create class with _VALID_URL
    # Test that constructor of ServiceIE is called
    class FakeIE(FourTubeBaseIE):
        _VALID_URL = 'http://example.com'


# Generated at 2022-06-14 16:19:04.665213
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    assert FourTubeIE.suitable('http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert FourTubeIE.suitable('http://www.4tube.com/embed/209733')
    assert FourTubeIE.suitable('http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
    assert not FourTubeIE.suitable('http://www.baidu.com/')


# Generated at 2022-06-14 16:19:13.539914
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie.__class__.__name__ == 'FourTubeIE'
    expected_urls = [
        'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'http://www.4tube.com/embed/209733',
    ]
    for url in expected_urls:
        assert ie._VALID_URL == url
        assert ie._real_extract(url)

# Generated at 2022-06-14 16:19:19.753963
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert ie._TESTS == ie.ie._TESTS
    assert ie._VALID_URL == ie.ie._VALID_URL
    assert ie._URL_TEMPLATE == ie.ie._URL_TEMPLATE
    assert ie._TKN_HOST == ie.ie._TKN_HOST


# Generated at 2022-06-14 16:19:22.523201
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    r = FourTubeIE('4Tube')._VALID_URL
    assert r == FourTubeIE._VALID_URL
    

# Generated at 2022-06-14 16:19:23.282857
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE(None, None)



# Generated at 2022-06-14 16:19:24.333619
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    class_ = PornerBrosIE
    assert class_ is not None

# Generated at 2022-06-14 16:19:25.363212
# Unit test for constructor of class FuxIE
def test_FuxIE():
    if __name__ == '__main__':
        test_FuxIE()

# Generated at 2022-06-14 16:19:31.812847
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie.IE_NAME == '4tube'

# Generated at 2022-06-14 16:19:34.731037
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    f = FourTubeIE()
    if f.IE_NAME != '4tube':
        print(f.IE_NAME)
        
if __name__ == '__main__':
    test_FourTubeIE()
    print("test")

# Generated at 2022-06-14 16:22:44.972736
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    obj = FourTubeIE()
    print(obj.IE_NAME)

# Generated at 2022-06-14 16:22:49.291179
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    IE = FourTubeIE()
    assert IE._VALID_URL == "https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?"

# Generated at 2022-06-14 16:22:51.246859
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    f = FourTubeBaseIE()
    assert f._TKN_HOST == 'token.4tube.com'



# Generated at 2022-06-14 16:22:52.365059
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE(FuxIE._downloader, FuxIE._VALID_URL)

# Generated at 2022-06-14 16:22:55.189150
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        FourTubeBaseIE()
    except AssertionError as e:
        print(e)
        assert False
    else:
        assert True


# Generated at 2022-06-14 16:22:56.236920
# Unit test for constructor of class FuxIE
def test_FuxIE():
    f = FuxIE()

# Generated at 2022-06-14 16:22:57.241760
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert issubclass(PornerBrosIE, PornTubeIE)

# Generated at 2022-06-14 16:23:05.767057
# Unit test for constructor of class FuxIE
def test_FuxIE():
    import sys
    import os
    import tempfile
    from six.moves import urllib

    from ytdl.const import *
    from ytdl.cipher import cipheruri_re

    # Preparation for test
    saved_argv = sys.argv[:]
    saved_environ = os.environ[:]


# Generated at 2022-06-14 16:23:07.397846
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    i = FourTubeBaseIE()
    assert isinstance(i, FourTubeBaseIE)

# Generated at 2022-06-14 16:23:08.013581
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    assert PornTubeIE()