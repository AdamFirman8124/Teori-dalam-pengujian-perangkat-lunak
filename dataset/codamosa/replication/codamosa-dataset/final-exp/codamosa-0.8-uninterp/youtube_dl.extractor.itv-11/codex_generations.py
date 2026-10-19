

# Generated at 2022-06-14 16:34:49.602731
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    constructor = ITVBTCCIE.__init__
    test_instance = ITVBTCCIE()
    assert test_instance.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert callable(constructor)

# Generated at 2022-06-14 16:34:58.644411
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    def test_real_extract(self):
        pass

    class MyITVBTCCIE(ITVBTCCIE):
        _real_extract = test_real_extract
    assert MyITVBTCCIE.ie_key() == 'ITVBTCC'
    assert MyITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE is not None

# Generated at 2022-06-14 16:35:10.916504
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from itertools import chain
    from io import BytesIO
    from unittest.mock import patch, MagicMock
    from yarl import URL

    from ..common import InfoExtractor

    VIDEO_ID = '5788972427001'
    TITLE = 'BTCC 2018: All the action from Brands Hatch'
    URL_PREFIX = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId='


# Generated at 2022-06-14 16:35:13.309699
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    try:
        instance = ITVBTCCIE()
        assert isinstance(instance, ITVBTCCIE)
    except:
        pass

# Generated at 2022-06-14 16:35:17.910800
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    assert re.match( ITVBTCCIE._VALID_URL, url )


# Generated at 2022-06-14 16:35:24.326327
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ITVBTCCIE(IE=InfoExtractor)._real_initialize()
    ITVBTCCIE(IE=InfoExtractor).suitable(url)
    ITVBTCCIE(IE=InfoExtractor)._real_extract(url)

# Generated at 2022-06-14 16:35:28.069866
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = ITVIE()._build_url('2a4547a0012')
    assert url == ("https://www.itv.com/hub/{"
                   "id}/2a4547a0012")

# Generated at 2022-06-14 16:35:30.235264
# Unit test for constructor of class ITVIE
def test_ITVIE():
    yt = ITVIE()
    yt.extract("https://www.itv.com/hub/liar/2a4547a0012")

# Generated at 2022-06-14 16:35:36.149553
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvBTCCIE = ITVBTCCIE()
    assert itvBTCCIE._PLAYLIST_URL_TEMPLATE == 'https://www.itv.com/hub/%s'
    assert itvBTCCIE._PLAYLIST_TITLE_RE == r'(?s)<h1>(?P<title>.+?)</h1>'
    assert itvBTCCIE._PLAYLIST_DESCRIPTION_RE == r'(?s)<div class="synopsis">(?P<description>.+?)</div>'

# Generated at 2022-06-14 16:35:43.195589
# Unit test for constructor of class ITVIE
def test_ITVIE():
    resp = {}

# Generated at 2022-06-14 16:36:04.979412
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Test for constructor of class ITVBTCCIE
    :return: None
    """
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ITVBTCCIE()._real_extract(url)

# Generated at 2022-06-14 16:36:06.997675
# Unit test for constructor of class ITVIE
def test_ITVIE():
    try:
        from ..utils import TestDataJsonld
        TestDataJsonld.test_ITVIE()
    except Exception as e:
        print(e)

# Generated at 2022-06-14 16:36:11.083329
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE()
    assert itvbtccie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:36:15.471710
# Unit test for constructor of class ITVIE
def test_ITVIE():
    print("test_itv_video_id")
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    itv_ie = ITVIE()
    assert itv_ie.suitable(url) == True


# Generated at 2022-06-14 16:36:19.109984
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE(ITVBTCCIE._downloader, 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:36:20.674707
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE().extract().__class__ == ITVIE


# Generated at 2022-06-14 16:36:25.638528
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    result = ITVBTCCIE._extract_urls(url, ITVBTCCIE.ie_key())
    assert len(result) == 1
    assert result[0] == url

# Generated at 2022-06-14 16:36:28.243326
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    try:
        ITVBTCCIE()
    except Exception as e:
        assert False, "Unexpected exception: " + str(e)

# Generated at 2022-06-14 16:36:30.747713
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE.__name__ == 'ITVIE'
    i = ITVIE(None)
    assert i.__class__.__name__ == 'ITVIE'

# Generated at 2022-06-14 16:36:36.320520
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    processing = ITVBTCCIE()._real_extract(url)
    assert processing['entries'][0]['id'] == '5868753526001'
    assert processing['entries'][4]['id'] == '5867878992001'
    assert processing['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert len(processing['entries']) >= 9

# Generated at 2022-06-14 16:37:17.960221
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # pylint: disable=redefined-outer-name
    from ..test import TestCase

    # No test for ITVIE._VALID_URL
    TestCase.test_ITVIE = TestCase.test_class_API
    # No test for ITVIE._GEO_COUNTRIES
    # No test for ITVIE._TESTS
    TestCase.test_ITVIE = TestCase.test_class_API
    # No test for ITVIE.BRIGHTCOVE_URL_TEMPLATE
    TestCase.test_ITVIE = TestCase.test_class_API
    # No test for ITVIE.BRIGHTCOVE_URL_TEMPLATE
    TestCase.test_ITVIE = TestCase.test_class_API
    # No test for ITVIE.BRIGHTCOVE_URL_T

# Generated at 2022-06-14 16:37:21.564797
# Unit test for constructor of class ITVIE
def test_ITVIE():
    class_name = 'ITVIE'
    obj = ITVIE(
        # need to set _downloader to prevent failing of _real_initialize
        object()
    )
    assert class_name
    assert obj.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:37:23.185724
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE is None
    assert ie.BRIGHTCOVE_ACCOUNT_ID is None
    assert ie.BRIGHTCOVE_POLICY_KEY is None
    assert ie._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:37:25.516300
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    c = ITVBTCCIE()
    title = 'BTCC 2018: All the action from Brands Hatch'
    assert c._og_search_title(c._download_webpage('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch', 'btcc-2018-all-the-action-from-brands-hatch'), fatal=False) == title

# Generated at 2022-06-14 16:37:27.419509
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034'
    expected_result = False
    result = ITVIE()._is_valid_url(url)
    assert result == expected_result

# Generated at 2022-06-14 16:37:33.846568
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._match_id(url) == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ITVBTCCIE._match_id('http://www.itv.com/gt/races/dtm-2018-2019-season-review') == 'dtm-2018-2019-season-review'

# Generated at 2022-06-14 16:37:45.339753
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    a = ITVBTCCIE()
    assert a._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert a._TEST['url'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert a._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert a._TEST['info_dict']['title'] == 'BTCC 2018: All the action from Brands Hatch'
    assert a._TEST['playlist_mincount'] == 9
    assert a.BRIGHTCOVE_URL_T

# Generated at 2022-06-14 16:37:49.750605
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    sp = ITVBTCCIE()
    assert ITVBTCCIE._VALID_URL == sp._VALID_URL
    assert ITVBTCCIE._TEST['url'] == sp._TEST['url']
    assert ITVBTCCIE._TEST['info_dict'] == sp._TEST['info_dict']
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == sp.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:38:01.678167
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:38:13.978034
# Unit test for constructor of class ITVIE

# Generated at 2022-06-14 16:39:16.180494
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()

# Generated at 2022-06-14 16:39:18.594685
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    import sys
    import os

    sys.path.append(os.path.join("test", "youtube-dl", "youtube_dl"))

    from test.youtube_dl_test import YoutubeDLTest

    test = YoutubeDLTest(ITVBTCCIE)
    test.test()

# Generated at 2022-06-14 16:39:22.477683
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE()
    assert itv.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:33.711069
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Tests for examples of valid urls
    ITVIE("http://www.itv.com/hub/liar/2a4547a0012")
    ITVIE("http://www.itv.com/hub/through-the-keyhole/2a2271a0033")
    ITVIE("http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034")
    ITVIE("http://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024")
    ITVIE("http://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024")

    # Tests for examples of invalid urls

# Generated at 2022-06-14 16:39:35.858030
# Unit test for constructor of class ITVIE
def test_ITVIE():
    t = ITVIE()
    assert t._VALID_URL == ITVIE._VALID_URL

# Generated at 2022-06-14 16:39:38.195513
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    _ITVBTCCIE = ITVBTCCIE()
    _ITVBTCCIE._real_extract(ITVBTCCIE._TEST['url'])

# Generated at 2022-06-14 16:39:39.923516
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:39:42.237575
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._TESTS[0]['info_dict']['id'] == ITVIE(ITVIE())._match_id(ITVIE._TESTS[0]['url'])


# Generated at 2022-06-14 16:39:52.355365
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    btcc_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    btcc_id = 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:39:54.329719
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE();
    assert(type(itvbtccie)==ITVBTCCIE)

# Generated at 2022-06-14 16:42:37.328729
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Create an instance of ITVBTCCIE as its constructor takes no arguments.
    A broken instance would raise a type error.
    """
    ITVBTCCIE()

# Generated at 2022-06-14 16:42:39.884347
# Unit test for constructor of class ITVIE
def test_ITVIE():
    f = ITVIE('http://www.itv.com/hub/liar/2a4547a0012')
    # assert that f is an instance of ITVIE
    assert isinstance(f, ITVIE)

# Generated at 2022-06-14 16:42:41.036843
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.ie_key() == 'ITV'

# Generated at 2022-06-14 16:42:42.465588
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE(open('tests/ITVBTCCIE.html', 'r').read())

# Generated at 2022-06-14 16:42:50.685436
# Unit test for constructor of class ITVIE
def test_ITVIE():
    constructor = ITVIE()
    assert constructor._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert constructor._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:42:58.296535
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE().suitable(test_url)
    assert ITVBTCCIE()._match_id(test_url) == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE()._real_extract(test_url)



# Generated at 2022-06-14 16:43:01.726323
# Unit test for constructor of class ITVIE
def test_ITVIE():
    t = ITVIE()
    t._download_webpage = lambda *args, **kwargs: ''
    assert t.construct_url(t._VALID_URL, {'itv': True}) == ITVIE._VALID_URL

# Generated at 2022-06-14 16:43:05.739154
# Unit test for constructor of class ITVIE
def test_ITVIE():
    cls = ITVIE
    assert cls.BRIGHTCOVE_URL_TEMPLATE is None
    assert cls.geo_verification_headers
    assert cls.PLAYLIST_TITLE_RE is None
    assert cls.BRIGHTCOVE_SIG is None
    assert cls.BRIGHTCOVE_INFO_URL is None
    assert cls.BRIGHTCOVE_PUBLIC_KEY is None

# Generated at 2022-06-14 16:43:15.739247
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .common import InfoExtractor

    itv_new = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert itv_new.request_headers['referer'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert itv_new.request_headers['User-Agent'].find('Mozilla') != -1
    assert itv_new.request_headers['X-Forwarded-For'] == '193.113.0.0, 54.36.162.0, 159.65.16.0'

# Generated at 2022-06-14 16:43:23.177125
# Unit test for constructor of class ITVIE
def test_ITVIE():
    
    #I used ITVIE class because it has only one field which is the URL
    #I have tested the constructor of the class in the following lines
    ITVIE.test()
    #I have used the test data from the _TESTS list
    assert ITVIE._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'
    #I have used the test data from the _TESTS list
    assert ITVIE._TESTS[0]['info_dict']['id'] == '2a4547a0012'
    #I have used the test data from the _TESTS list
    assert ITVIE._TESTS[0]['info_dict']['ext'] == 'mp4'
    
    
    
