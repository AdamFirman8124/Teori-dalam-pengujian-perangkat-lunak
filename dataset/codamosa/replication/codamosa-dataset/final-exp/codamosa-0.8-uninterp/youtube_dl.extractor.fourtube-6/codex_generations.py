

# Generated at 2022-06-14 16:13:47.864989
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    video_data = {
        'mediaId': '53047',
        'title': 'Test video',
        'durationInSeconds': 60,
    }
    video_base64_encoded = compat_urllib_parse_unquote(
        compat_b64encode(compat_str(video_data).encode('utf-8')).decode('ascii'))
    video_base64_encoded_last_part = video_base64_encoded[len(video_base64_encoded) - 100:]
    video_json = '{"page":{"video":' + video_base64_encoded + '}}'
    PornTubeIE._parse_json(video_json, '53047')

# Generated at 2022-06-14 16:13:57.649041
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    class_ = FourTubeIE
    # Ensure that FourTubeIE constructor sets the correct _VALID_URL, _URL_TEMPLATE and _TKN_HOST variables
    assert class_._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?4tube\.com/(?:videos|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert class_._URL_TEMPLATE == 'https://www.4tube.com/videos/%s/video'
    assert class_._TKN_HOST == 'token.4tube.com'


# Generated at 2022-06-14 16:13:59.209069
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    # simply run for the purpose of code coverage
    FourTubeBaseIE()

# Generated at 2022-06-14 16:14:12.601419
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    from .test_f4m import test_f4m_common
    # test_f4m_common(FourTubeIE.ie_key(), (
    #     r'http://www.4tube.com/videos/60249/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black',
    #     {'kind': 'www', 'id': '60249'},
    #     {'kind': 'm', 'id': '60249'},
    #     'http://www.4tube.com/embed/60249',
    #     r'http://www.4tube.com/(?:videos|embed)/60249'))

# Generated at 2022-06-14 16:14:22.896074
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    url = 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'

# Generated at 2022-06-14 16:14:28.784916
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():

    # Itunes URL
    url = "https://www.4tube.com/videos/213484/curvy-babe-seduces-her-boss-and-gets-fucked-on-couch"
    obj = FourTubeIE()
    result = obj._real_extract(url)

    # Basic Tile
    assert result['title'] == 'Curvy babe seduces her boss and gets fucked on couch'

    # Number of formats
    assert len(result['formats']) == 4

    # Uploader
    assert result['uploader'] == 'Jules Jordan'


# Generated at 2022-06-14 16:14:30.932883
# Unit test for constructor of class FuxIE
def test_FuxIE():
    # The constructor of the FuxIE class should not throw an exception
    FuxIE()

# Generated at 2022-06-14 16:14:35.675185
# Unit test for constructor of class FuxIE
def test_FuxIE():
    url = 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    FuxIE(FuxIE._VALID_URL)
    FuxIE.suitable(url)
    info = FuxIE._real_extract(FuxIE(), url)
    print(info)


# Generated at 2022-06-14 16:14:42.206353
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE(None)
    assert ie.IE_NAME == 'pornerbros'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert ie._TKN_HOST == 'token.pornerbros.com'

# Generated at 2022-06-14 16:14:45.197187
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    obj = FourTubeBaseIE()
    assert obj.ie_key() in globals(), 'IE key is not in globals'
    ie = globals()[obj.ie_key()]
    assert ie.ie_key() == obj.ie_key()
    assert ie.ie_key() == 'FourTubeBaseIE'
    assert ie.IE_NAME == '4tube'

# Generated at 2022-06-14 16:15:07.485530
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE('http://www.4tube.com/videos/170296/squirting-in-public-part-two')
    assert ie.__class__.__name__ == 'FourTubeIE'
    assert ie._TKN_HOST == 'token.4tube.com'


# Generated at 2022-06-14 16:15:16.828629
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie._TKN_HOST == 'token.pornerbros.com'
    #assert ie._VALID_URL == 'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    #assert ie._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    #assert ie._TESTS[0]['md5'] == '6516c8ac63b03de06bc8eac14362db4f'

# Generated at 2022-06-14 16:15:18.108033
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    assert issubclass(FourTubeBaseIE, InfoExtractor)

# Generated at 2022-06-14 16:15:19.695947
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE('FourTube', 'FourTubeBaseIE')
    assert isinstance(ie, FourTubeBaseIE)

# Generated at 2022-06-14 16:15:21.251069
# Unit test for constructor of class FuxIE
def test_FuxIE():
    obj = FuxIE()
    assert obj._TKN_HOST == 'token.fux.com'

# Generated at 2022-06-14 16:15:23.284103
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    from ytdl.extractor.PornTubeIE import PornTubeIE
    # For now, we just test that no exception is raised by the constructor
    ptub = PornTubeIE()

# Generated at 2022-06-14 16:15:27.081699
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE()
    assert fux._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fux._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fux._TKN_HOST == 'token.fux.com'


# Generated at 2022-06-14 16:15:33.205915
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    ie = FourTubeIE()

    # Test _extract_formats
    # https://token.4tube.com/175965/desktop/1080+720+480+360

# Generated at 2022-06-14 16:15:34.747832
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    PornerBrosIE()

# Generated at 2022-06-14 16:15:41.584673
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fuxIE = FuxIE('https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert fuxIE._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fuxIE.get_url() == 'https://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow'
    assert fuxIE.get_info('id') == '195359'
    assert fuxIE.get_info('ext') == 'mp4'
    assert fuxIE.get_info('title')

# Generated at 2022-06-14 16:16:25.390040
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    """Test for constructor of class FourTubeBaseIE"""
    url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    assert FourTubeBaseIE._VALID_URL.findall(url)
    assert FourTubeBaseIE._URL_TEMPLATE == 'https://%(site)s.4tube.com/videos/%s/video'
    assert FourTubeBaseIE._TKN_HOST == 'token.%(site)s.com'
    url = 'https://www.fux.com/videos/195359/awesome-fucking-kitchen-ends-cum-swallow'
    assert FuxIE._VALID_URL.findall(url)
    assert FuxIE._URL_T

# Generated at 2022-06-14 16:16:25.829364
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE()

# Generated at 2022-06-14 16:16:26.481774
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()

# Generated at 2022-06-14 16:16:29.034518
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    """Basic test for PornerBrosIE."""
    # Test without video id
    obj = PornerBrosIE()
    assert obj._TEST.get('skip')

# Generated at 2022-06-14 16:16:32.549361
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    # assert that the constructor of class FourTubeIE has not been changed
    assert FourTubeIE._TESTS[0]['url'] == "http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black"



# Generated at 2022-06-14 16:16:37.455724
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fux = FuxIE()
    assert fux._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'
    assert fux._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert fux._TKN_HOST == 'token.fux.com'
    assert type(fux._TESTS) is list


# Generated at 2022-06-14 16:16:39.105265
# Unit test for constructor of class FuxIE
def test_FuxIE():
    fuxIE = FuxIE()
    assert(fuxIE._TESTS[1]['url'] == 'https://www.fux.com/embed/195359')

# Generated at 2022-06-14 16:16:48.555259
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    def dowload_json(url, video_id, data, headers, query):
        assert re.match(r'https?://token\.4tube\.com/\d+/desktop/[0-9]+p', url)
        assert video_id == 209733
        assert data == b''
        assert headers['Origin'] == 'http://www.4tube.com'
        assert headers['Referer'] == 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'

# Generated at 2022-06-14 16:16:58.783694
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    assert PornerBrosIE()._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?pornerbros\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'
    assert PornerBrosIE()._URL_TEMPLATE == 'https://www.pornerbros.com/videos/video_%s'
    assert PornerBrosIE()._TKN_HOST == 'token.pornerbros.com'
    assert PornerBrosIE()._TESTS[0]['url'] == 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    assert PornerBrosIE

# Generated at 2022-06-14 16:17:06.592169
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    expected_result = {
                        'id': '181369',
                        'ext': 'mp4',
                        'title': 'Skinny brunette takes big cock down her anal hole',
                        'uploader': 'PornerBros HD',
                        'uploader_id': 'pornerbros-hd',
                        'upload_date': '20130130',
                        'timestamp': 1359527401,
                        'duration': 1224,
                        'view_count': int,
                        'categories': list,
                        'age_limit': 18
                      }
    url = 'https://www.pornerbros.com/videos/skinny-brunette-takes-big-cock-down-her-anal-hole_181369'
    pornerBrosIE = PornerBrosIE()
    pornerBrosIE._

# Generated at 2022-06-14 16:18:30.986176
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    m = FourTubeIE()._VALID_URL
    assert 'www' in m.group('kind')
    assert int(m.group('id')) > 0
    assert m.group('display_id')

# Generated at 2022-06-14 16:18:31.973752
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    '''Test PornTubeIE constructor'''
    PornTubeIE()

# Generated at 2022-06-14 16:18:33.658198
# Unit test for constructor of class FourTubeBaseIE

# Generated at 2022-06-14 16:18:36.690637
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Arrange
    url = 'https://www.porntube.com/videos/squirting-teen-ballerina-ecg_1331406'
    expected_title = 'Squirting Teen Ballerina on ECG'

    # Act
    video = PornTubeIE._real_extract(PornTubeIE(), url)
    title = video['title']

    # Assert
    assert title == expected_title

# Generated at 2022-06-14 16:18:37.543474
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    ie = FourTubeBaseIE()
    assert ie is not None

# Generated at 2022-06-14 16:18:42.780053
# Unit test for constructor of class FuxIE
def test_FuxIE():
    from .test_imports import get_testcases
    testcases = get_testcases(FuxIE, 'FuxIE')
    for tc in testcases:
        url = tc['url']
        obj = FuxIE(url)
        mobj = re.match(obj._VALID_URL, url)
        title = tc['title']
        vault_id, display_id = mobj.group('id', 'display_id')
        assert obj._VALID_URL == obj._TESTS[0]['url']
        assert obj._TKN_HOST == obj._TESTS[0]['md5']
        assert obj._URL_TEMPLATE == obj._TESTS[0]['duration']
        assert obj._VALID_URL  == obj._TESTS[0]['are_age_restricted']


# Generated at 2022-06-14 16:18:50.651572
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
	print("")
	print("--------------------------------------")
	print("test_FourTubeBaseIE")
	print("--------------------------------------")
	test_module_name = "FourTubeBaseIE"
	expect_result = "dl-with-youtube-dl"
	test_obj = FourTubeBaseIE()
	result = test_obj.__class__.__name__
	print("type: {0}, actual: {1}, expect: {2}".format(test_module_name, result, expect_result))
	assert result == expect_result, "{0}.{1}".format(test_module_name, sys._getframe().f_code.co_name)
	print("")


# Generated at 2022-06-14 16:18:52.396986
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    pornerBrosIE = PornerBrosIE("www.pornerbros.com")

# Generated at 2022-06-14 16:18:57.369238
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    instance = PornTubeIE()
    assert instance._URL_TEMPLATE == 'https://www.porntube.com/videos/video_%s'
    assert instance._TKN_HOST == 'tkn.porntube.com'
    assert instance._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?porntube\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\d+)'


# Generated at 2022-06-14 16:18:58.730414
# Unit test for constructor of class PornerBrosIE
def test_PornerBrosIE():
    ie = PornerBrosIE()
    assert ie.IE_NAME == 'pornerbros'

# Generated at 2022-06-14 16:22:37.906789
# Unit test for constructor of class FuxIE
def test_FuxIE():
    """
    Test that FuxIE works as advertised (has no errors and fails when appropriate)
    :return:
    """
    info_extractor = FuxIE()
    video = info_extractor.extract('http://www.fux.com/video/195359/awesome-fucking-kitchen-ends-cum-swallow')
    assert video['id'] == '195359'
    assert video['timestamp'] == 1388361660
    assert video['ext'] == 'mp4'
    assert len(video['formats']) == 2

# Generated at 2022-06-14 16:22:45.110993
# Unit test for constructor of class FourTubeIE

# Generated at 2022-06-14 16:22:47.185711
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ce = FuxIE()
    assert ce.ie_key() == 'Fux'
    assert ce.ie_name() == 'Fux'

# Generated at 2022-06-14 16:22:51.895262
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    webObj = InfoExtractor()

    weburl = "http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black"
    # call real extract method
    webObj._downloader = "html5lib"
    webObj.real_extract(weburl)

# Generated at 2022-06-14 16:22:55.574901
# Unit test for constructor of class FourTubeBaseIE
def test_FourTubeBaseIE():
    IE = FourTubeBaseIE()
    IE.IE_NAME = 'Test'
    IE._VALID_URL = r'https?://www\.test\.com/\d+'
    IE._URL_TEMPLATE = 'https://www.test.com/%s/video'
    IE._TKN_HOST = 'token.test.com'

# Generated at 2022-06-14 16:22:57.036338
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    obj = FourTubeIE()

# Generated at 2022-06-14 16:23:03.552181
# Unit test for constructor of class FuxIE
def test_FuxIE():
    ie = FuxIE()
    assert ie._TKN_HOST == 'token.fux.com'
    assert ie._URL_TEMPLATE == 'https://www.fux.com/video/%s/video'
    assert ie.IE_NAME == 'fux'
    assert ie._VALID_URL == r'https?://(?:(?P<kind>www|m)\.)?fux\.com/(?:video|embed)/(?P<id>\d+)(?:/(?P<display_id>[^/?#&]+))?'


# Generated at 2022-06-14 16:23:05.577058
# Unit test for constructor of class FuxIE
def test_FuxIE():
    FuxIE('url')

# Generated at 2022-06-14 16:23:06.154840
# Unit test for constructor of class FourTubeIE
def test_FourTubeIE():
    FourTubeIE()

# Generated at 2022-06-14 16:23:07.841459
# Unit test for constructor of class PornTubeIE
def test_PornTubeIE():
    # Test to check the constructor of PornTubeIE
    PornTubeIE()