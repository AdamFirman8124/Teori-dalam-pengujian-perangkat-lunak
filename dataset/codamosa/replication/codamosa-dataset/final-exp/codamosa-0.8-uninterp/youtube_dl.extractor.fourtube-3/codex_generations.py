

# Generated at 2022-06-14 16:13:44.163953
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # Set up mocking.
    class MockPafy(object):
        def __init__(self, url):
            pass
    class MockYoutubeDL(object):
        def extract_info(self, url):
            return {
                'title': 'Video title',
                'upload_date': '2018-03-03 00:00:00',
                'uploader_id': 'uploader-id',
                'uploader': 'uploader',
                'categories': ['cat1', 'cat2'],
                'duration': 100,
                'thumbnail': 'thumbnail-url',
                'view_count': 1000,
                'like_count': 1000,
                'tags': ['tag1', 'tag2']
            }
        def set_progress_hook(self, progress_hook):
            pass

# Generated at 2022-06-14 16:13:46.689475
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()

# Generated at 2022-06-14 16:13:50.086465
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie.ie_key() == 'Fux'
    assert ie.ie_name() == 'Fux'
    assert ie.ie_description() == None


# Generated at 2022-06-14 16:13:51.351343
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        f = FourTubeBaseIE("")
    except Exception as e:
        pass
    else:
        assert False



# Generated at 2022-06-14 16:13:58.258536
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    from .test_common import make_test_result
    from youtube_dl.downloader.f4m import F4MDownloader

    assert PornerBrosIE._F4M_DOWNLOADER_CLS == F4MDownloader

    output = make_test_result({})
    ie = PornerBrosIE()
    result = ie.extract(
        'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369',
        output, download=False)
    assert result.get('formats') is not None
    assert result.get('formats', [{}])[0].get('url') is not None

# Generated at 2022-06-14 16:14:09.452820
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert issubclass(PornerBrosIE, InfoExtractor)
    assert issubclass(PornerBrosIE, FourTubeBaseIE)
    unit_test_instance = PornerBrosIE()
    assert unit_test_instance._VALID_URL == PornerBrosIE._VALID_URL
    assert unit_test_instance._URL_TEMPLATE == PornerBrosIE._URL_TEMPLATE
    assert unit_test_instance._TKN_HOST == PornerBrosIE._TKN_HOST
    assert unit_test_instance.IE_NAME == 'PornerBros'


# Generated at 2022-06-14 16:14:11.396909
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros = PornerBrosIE()
    assert pornerbros.IE_NAME == 'pornerbros'

# Generated at 2022-06-14 16:14:16.617692
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    test_PornTubeIE = PornTubeIE()
    print(test_PornTubeIE)


# Generated at 2022-06-14 16:14:24.003057
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    url = 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    # constructor should use class instance variables (_VALID_URL,  _URL_TEMPLATE, _TKN_HOST)
    pt = PornTubeIE()
    pt._download_webpage(url, '7089759')
    pt._download_json(
        'https://www.porntube.com/videos/video_7089759', '7089759',
        data=b'', headers={'Referer': url})

# Generated at 2022-06-14 16:14:25.805223
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    test_obj = FourTubeIE()
    print(test_obj.IE_NAME)

# Generated at 2022-06-14 16:14:41.363384
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    pn = PornTubeIE();

# Generated at 2022-06-14 16:14:43.204807
# Unit test for constructor of class FuxIE
def test_FuxIE():
    result = FuxIE()
    assert result._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:14:47.745016
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert ie.IE_NAME == '4tube'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert ie._TKN_HOST == 'tkn.porntube.com'
    assert len(ie._TESTS) == 3

# Generated at 2022-06-14 16:14:48.389941
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    FourTubeBaseIE() == PornerBrosIE()

# Generated at 2022-06-14 16:14:49.452579
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # FuxIE without argument
    assert FuxIE()



# Generated at 2022-06-14 16:14:50.712679
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    constr = FourTubeBaseIE
    print(constr)

if __name__ == '__main__':
    test_FourTubeBaseIE()

# Generated at 2022-06-14 16:14:55.630832
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    for cls in [FourTubeIE, FuxIE, PornTubeIE, PornerBrosIE]:
        obj = cls()
        obj.suitable('https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black')
        obj.suitable('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
        obj.suitable('https://www.porntube.com/videos/teen-couple-doing-anal_7089759')
        obj.suitable('https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369')
        obj

# Generated at 2022-06-14 16:15:02.352248
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    p = PornTubeIE(None)
    assert p.__class__ == PornTubeIE
    assert p._VALID_URL == PornTubeIE._VALID_URL
    assert p._URL_TEMPLATE == PornTubeIE._URL_TEMPLATE
    assert p._TKN_HOST == PornTubeIE._TKN_HOST

# Generated at 2022-06-14 16:15:10.997809
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    ie.extract("https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")
    ie.extract("http://www.4tube.com/embed/209733")
    ie.extract("http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")

# Generated at 2022-06-14 16:15:12.061242
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE("test", {}, {})

# Generated at 2022-06-14 16:15:45.459876
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros_ie = PornerBrosIE()
    assert pornerbros_ie.IE_NAME == 'Pornerbros'
    assert pornerbros_ie.URL_TEMPLATE == "https://www.pornerbros.com/videos/video_%s"
    assert pornerbros_ie.VALID_URL == "https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)"
    assert pornerbros_ie.TKN_HOST == "token.pornerbros.com"


# Generated at 2022-06-14 16:15:46.195056
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
	fourTubeIE = PornerBrosIE(None)

# Generated at 2022-06-14 16:15:47.645238
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    ie2 = FourTubeBaseIE()
    assert ie._TKN_HOST == ie2._TKN_HOST

# Generated at 2022-06-14 16:15:50.311897
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # test for creating instance of FourTubeBaseIE
    obj = FourTubeBaseIE()
    assert obj is not None

# Generated at 2022-06-14 16:15:51.814766
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    try:
        PornTubeIE()
    except Exception:
        assert False

# Generated at 2022-06-14 16:16:01.785079
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Test with a valid url
    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    fourtube_base_ie = FourTubeBaseIE()
    mobj = re.match(fourtube_base_ie._VALID_URL, url)
    assert mobj is not None
    # Test with an invalid url
    url = 'http://www.4tube.com/videos/'
    mobj = re.match(fourtube_base_ie._VALID_URL, url)
    assert mobj is None

# Generated at 2022-06-14 16:16:02.861869
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE(None)



# Generated at 2022-06-14 16:16:03.871174
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    raise NotImplementedError('This test must be implemented')

# Generated at 2022-06-14 16:16:05.874670
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE('0123456789', 'abcd', 'display_id')

# Generated at 2022-06-14 16:16:07.159184
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    obj = FourTubeBaseIE()
    assert obj.IE_NAME == '4tube'

# Generated at 2022-06-14 16:17:06.456776
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
        ie = FourTubeBaseIE("url")
        assert ie._VALID_URL is None
        assert ie._URL_TEMPLATE is None
        assert ie._TKN_HOST is None

# Generated at 2022-06-14 16:17:07.476142
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE().suitable('181369')

# Generated at 2022-06-14 16:17:10.444218
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    obj = FourTubeBaseIE(
        'generic',
        'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
        'mp4',
        'best')
    print(obj)
    print(obj.getUrls())

# Generated at 2022-06-14 16:17:11.551034
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

# Generated at 2022-06-14 16:17:21.570031
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from ..jsinterp import JSInterpreter
    import base64

    # Load the Javascript code
    js_code = open('test/testdata/player-embed.js', 'rb').read().decode('utf-8')
    # Run the code to obtain the initial parameters
    jsi = JSInterpreter(js_code)
    jsi.execute('encodeURIComponent(decodeURIComponent(url))')
    params = jsi.get_user_var('params')
    # Recreate the list
    params = PornTubeIE._parse_json(
        '[%s]' % params, 'https://www.porntube.com/embed/7089759',
        transform_source=lambda x: base64.b64decode(x.encode('ascii')).decode('utf-8'))


# Generated at 2022-06-14 16:17:29.925486
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    videos = [
        '//www.porntube.com/videos/blonde-babe-seduces-her-sisters-bf_1204164',
        '//www.porntube.com/embed/1204164',
        '//m.porntube.com/videos/blonde-babe-seduces-her-sisters-bf_1204164'
    ]
    for video in videos:
        pornTubeIE = PornTubeIE()
        pornTubeIE._VALID_URL = PornTubeIE._VALID_URL
        pornTubeIE.working = True
        pornTubeIE._real_extract(video)



# Generated at 2022-06-14 16:17:38.132901
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    fourtube = FourTubeIE()
    assert fourtube.IE_NAME == "4tube"
    assert fourtube.valid_url("http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")
    assert fourtube.valid_url("http://m.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black")
    assert fourtube.valid_url("http://www.4tube.com/embed/209733")
    assert not fourtube.valid_url("https://www.4tube.com")
    assert not fourtube.valid_url("http://www.4tube.com/")


# Generated at 2022-06-14 16:17:40.526684
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE() is not None
    # assert test_PornerBrosIE is not None

# Generated at 2022-06-14 16:17:43.572793
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE._URL_TEMPLATE is not None
    assert FuxIE._VALID_URL is not None
    assert FuxIE._TKN_HOST is not None
    assert FuxIE._TESTS is not None


# Generated at 2022-06-14 16:17:44.196538
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    test_FourTubeIE = FourTubeIE()

# Generated at 2022-06-14 16:20:20.473392
# Unit test for constructor of class FuxIE
def test_FuxIE():
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    info_dict = {
        'id': '195359',
        'ext': 'mp4',
        'title': 'Awesome fucking in the kitchen ends with cum swallow',
        'uploader': 'alenci2342',
        'uploader_id': 'alenci2342',
        'upload_date': '20131230',
        'timestamp': 1388361660,
        'duration': 289,
        'view_count': int,
        'like_count': int,
        'categories': list,
        'age_limit': 18,
    }
    params = {
        'skip_download': True,
    }

    IE = FuxIE()
   

# Generated at 2022-06-14 16:20:22.572366
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    ie = PornTubeIE()
    assert (ie.__class__.__name__ == 'PornTubeIE')

# Generated at 2022-06-14 16:20:24.145667
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        FourTubeBaseIE()
    except Exception as e:
        assert False, e
        return
    assert True

# Generated at 2022-06-14 16:20:34.010399
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from .test_common import FakeWebPage
    page = FakeWebPage()
    page.set_url('https://www.porntube.com/embed/7089759')

# Generated at 2022-06-14 16:20:36.924124
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    test = FourTubeBaseIE()
    for i in ['FourTubeIE', 'FuxIE', 'PornTubeIE', 'PornerBrosIE']:
        assert i == test.__class__.__name__



# Generated at 2022-06-14 16:20:38.059430
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:20:39.716756
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE('https://www.fux.com/embed/195359')

# Generated at 2022-06-14 16:20:41.476345
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    o = PornerBrosIE()
    assert o._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:20:43.241931
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()


# Generated at 2022-06-14 16:20:54.462355
# Unit test for constructor of class PornTubeIE