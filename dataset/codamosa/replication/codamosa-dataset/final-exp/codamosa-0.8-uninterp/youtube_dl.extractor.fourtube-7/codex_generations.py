

# Generated at 2022-06-14 16:13:40.605292
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie.__class__ ==  FourTubeIE


# Generated at 2022-06-14 16:13:44.286071
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    try:
        test_FourTubeBaseIE.FourTubeBaseIE_object
    except AttributeError:
        test_FourTubeBaseIE.FourTubeBaseIE_object = FourTubeBaseIE()

    assert isinstance(test_FourTubeBaseIE.FourTubeBaseIE_object, InfoExtractor)

# Generated at 2022-06-14 16:13:46.373291
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE()

# Generated at 2022-06-14 16:13:47.972673
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie is not None

# Generated at 2022-06-14 16:13:58.947861
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    video_id = '209733'
    display_id = 'hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    mobj = re.match(FourTubeBaseIE._VALID_URL, url)
    token_url = 'https://%s/%s/desktop/720p+480p' % (FourTubeBaseIE._TKN_HOST, video_id)

    assert((mobj.group('kind'), mobj.group('id'), mobj.group('display_id')) == ('www', video_id, display_id))

# Generated at 2022-06-14 16:14:11.398860
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Constructor should fail if hostnames mismatch
    F = classmethod(FourTubeBaseIE)
    assert issubclass(
        F('porntube.com', 'token.4tube.com', '4tube.com'),
        FourTubeBaseIE)
    assert not issubclass(
        F('porntube.com', 'token.4tube.com', '4tube.co'),
        FourTubeBaseIE)
    assert not issubclass(
        F('porntube.com', 'token.4tube.com', 'porntube.com'),
        FourTubeBaseIE)
    assert not issubclass(
        F('porntube.com', 'token.4tube.com', 'token.4tube.com'),
        FourTubeBaseIE)

# Generated at 2022-06-14 16:14:12.100730
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE(PornTubeIE._create_ie_instance())

# Generated at 2022-06-14 16:14:12.898664
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()



# Generated at 2022-06-14 16:14:20.156513
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    i = FourTubeIE()
    assert i._TKN_HOST == 'token.4tube.com'
    assert i._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert i._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'

# Generated at 2022-06-14 16:14:20.807552
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    FourTubeBaseIE()

# Generated at 2022-06-14 16:14:50.918631
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    suite = unittest.TestSuite()
    suite.addTest(TestFourTubeIE('test_constructor'))
    return suite


# Generated at 2022-06-14 16:14:52.362137
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    fourtube_ie = FourTubeIE()
    assert str(fourtube_ie) == '<FourTubeIE>'

# Generated at 2022-06-14 16:14:54.353000
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    fourTubeBaseIE = FourTubeBaseIE()
    fourTubeBaseIE._download_webpage('https://www.pornerbros.com/embed/181369', None)



# Generated at 2022-06-14 16:14:55.705213
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE(PornerBrosIE._VALID_URL, PornerBrosIE.IE_NAME)

# Generated at 2022-06-14 16:15:07.113112
# Unit test for constructor of class FuxIE
def test_FuxIE():
    import datetime
    from .common import InfoExtractor
    youtube_ie = InfoExtractor(FuxIE._VALID_URL)
    FuxIE.__init__(youtube_ie)

    assert youtube_ie._VALID_URL == FuxIE._VALID_URL
    assert youtube_ie._URL_TEMPLATE == FuxIE._URL_TEMPLATE
    assert youtube_ie._TKN_HOST == FuxIE._TKN_HOST
    assert youtube_ie._TESTS == FuxIE._TESTS

    assert youtube_ie.IE_NAME == FuxIE.IE_NAME



# Generated at 2022-06-14 16:15:11.456425
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    v = "The Fux company name"
    assert ie._SITE_NAME == v, "FuxIE name does not equal" + v
    v = "Fux"
    assert ie.ie_key() == v, "FuxIE ie_key() does not equal " + v
    v = "https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?"
    assert ie._VALID_URL == v, "FuxIE _VALID_URL does not equal " + v
    v = "https://www.fux.com/video/%s/video"

# Generated at 2022-06-14 16:15:12.120107
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    pass

# Generated at 2022-06-14 16:15:13.188379
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    o = FourTubeIE();



# Generated at 2022-06-14 16:15:19.224655
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE()
    assert fux._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fux._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fux._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:15:26.520797
# Unit test for constructor of class FuxIE
def test_FuxIE():
    url_1 = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    obj_1 = FuxIE('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert obj_1._VALID_URL == 'https?://(?:(?P<kind>www|m)\\.)?fux\\.com/(?:video|embed)/(?P<id>\\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert obj_1._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert obj_1._TKN_HOST == 'token.fux.com'
   

# Generated at 2022-06-14 16:16:08.365022
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    b = PornerBrosIE()
    assert b._TKN_HOST == 'token.pornerbros.com'
    assert b._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert b._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'

# Generated at 2022-06-14 16:16:09.506733
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE()

# Generated at 2022-06-14 16:16:10.733326
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # The constructor of class FourTubeBaseIE is un-tested
    assert True

# Generated at 2022-06-14 16:16:12.717285
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE = FuxIE()


# Generated at 2022-06-14 16:16:13.902443
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:16:15.756028
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros = PornerBrosIE()
    assert pornerbros._VALID_URL

# Generated at 2022-06-14 16:16:17.416359
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # Assert that does not raise
    b = FourTubeBaseIE()

# Generated at 2022-06-14 16:16:19.269167
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    assert PornTubeIE(PornTubeIE.suitable).__class__ == PornTubeIE


# Generated at 2022-06-14 16:16:20.583745
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

# Generated at 2022-06-14 16:16:24.101515
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    url = 'https://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    FourTubeIE(url)

# Generated at 2022-06-14 16:17:37.770141
# Unit test for constructor of class PornTubeIE

# Generated at 2022-06-14 16:17:41.173789
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # test for https://github.com/rg3/youtube-dl/issues/8303
    PornTubeIE()._download_webpage('http://www.porntube.com', '7089759')

# Generated at 2022-06-14 16:17:42.980392
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    prog = PornerBrosIE(None, None)
    assert prog.name == 'PornerBrosIE'

# Generated at 2022-06-14 16:17:44.084881
# Unit test for constructor of class FuxIE
def test_FuxIE():
    assert FuxIE()._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:17:50.582857
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    fourtube_ie = FourTubeIE()
    assert fourtube_ie.IE_NAME == "4tube"
    assert fourtube_ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fourtube_ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert fourtube_ie._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:17:51.004525
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    PornTubeIE()

# Generated at 2022-06-14 16:17:52.321968
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeBaseIE()
    assert ie._VALID_URL
    assert ie._URL_TEMPLATE
    assert ie._TKN_HOST
    assert ie._TESTS

# Generated at 2022-06-14 16:17:53.463952
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    test = FourTubeBaseIE('FourTubeBaseIE')
    assert('FourTubeBaseIE' == test.IE_NAME)

# Generated at 2022-06-14 16:17:57.831477
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    '''
    Just test if it runs at all.
    '''

    # Test direct constructor call
    ie = FourTubeBaseIE()
    ie = FuxIE()
    ie = PornTubeIE()
    ie = PornerBrosIE()

    # Test constructor call via generelized method
    ie = get_info_extractor('4tube')
    ie = get_info_extractor('fux')
    ie = get_info_extractor('porntube')
    ie = get_info_extractor('pornerbros')

# Generated at 2022-06-14 16:17:58.886038
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
        instance = FourTubeIE()

# Generated at 2022-06-14 16:21:10.329951
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    for url in [
        'https://www.porntube.com/videos/tiny4k-teen-blair-williams-huge-cock-creampie_1727681',
        'https://www.porntube.com/embed/1727681',
        'https://www.porntube.com/videos/video_1727681',
        'https://m.porntube.com/videos/video_1727681',
        'https://m.porntube.com/videos/tiny4k-teen-blair-williams-huge-cock-creampie_1727681',
    ]:
        assert PornTubeIE().suitable(url), url

# Generated at 2022-06-14 16:21:11.801030
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert isinstance(ie, FuxIE)

# Generated at 2022-06-14 16:21:21.096643
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    pt = PornTubeIE()
    pt_ie = pt._real_extract(url=pt._TESTS[1]['url'])
    assert pt_ie['id'] == '1331406'
    assert pt_ie['ext'] == 'mp4'
    assert pt_ie['title'] == 'Squirting Teen Ballerina on ECG'
    assert pt_ie['uploader'] == 'Exploited College Girls'
    assert pt_ie['uploader_id'] == '665'
    assert pt_ie['channel'] == 'Exploited College Girls'
    assert pt_ie['channel_id'] == '665'
    assert pt_ie['upload_date'] == '20130920'
    assert pt_ie['timestamp'] == 1379685485
    assert pt_ie['duration'] == 851
    assert pt_

# Generated at 2022-06-14 16:21:23.557485
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerbros_ie = PornerBrosIE()
    assert isinstance(pornerbros_ie, FourTubeBaseIE)

# Generated at 2022-06-14 16:21:24.511772
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()

# Generated at 2022-06-14 16:21:32.016307
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    constructor = FourTubeBaseIE._extract_formats
    media_id = "186932"
    sources = [
        "180",
        "240",
        "360",
        "480",
        "720",
        "1080",
    ]
    assert len(constructor("http://www.4tube.com/video/186932/amazing-asian-teen-gets-tamed-like-never-before",
                           "186932", media_id, sources)) == 6

# Generated at 2022-06-14 16:21:32.856256
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    pass

# Generated at 2022-06-14 16:21:41.982920
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    url = 'https://www.porntube.com/embed/7089759'

    obj = PornTubeIE()
    obj.initialize()

    settings = obj.extractor_settings
    assert settings['downloader']['prefer_insecure']
    assert settings['geo_bypass']
    assert settings['geo_bypass_country'] == 'US'
    assert settings['referer'] == url

    embed_page = obj.extract(url)
    assert embed_page['id'] == '7089759'

# Generated at 2022-06-14 16:21:48.068612
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert ie._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert ie._TKN_HOST == 'token.4tube.com'

# Generated at 2022-06-14 16:21:53.224736
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    class_PornerBrosIE=PornerBrosIE()
    expected_value=False
    actual_value=class_PornerBrosIE.PORNER_BROS_DOMAIN_RE == re.compile(
    '^(?:(?:www|m)\\.)?pornerbros\\.com$')
    assert(expected_value==actual_value)
