

# Generated at 2022-06-14 17:27:15.660350
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_obj = UDNEmbedIE()
    url_pattern = test_obj._PROTOCOL_RELATIVE_VALID_URL
    url_base = 'https:'
    assert re.match(url_pattern, url_base + '/video.udn.com/embed/news/300040') is not None
    assert re.match(url_pattern, url_base + '/video.udn.com/play/news/300040') is not None
    assert re.match(url_pattern, url_base + '/video.udn.com/embed/news/300040') is not None
    url_base = 'http:'
    assert re.match(url_pattern, url_base + '/video.udn.com/embed/news/300040') is not None

# Generated at 2022-06-14 17:27:17.676053
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_id = UDNEmbedIE()
    print(udn_embed_id)

# Generated at 2022-06-14 17:27:25.291014
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import InfoExtractor
    from .udn import UDNEmbedIE

    # In case of windows
    # InfoExtractor._download_webpage(None, "http://video.udn.com/embed/news/300040", "300040")
    
    info_extractor = InfoExtractor()
    udn_ie = UDNEmbedIE(info_extractor)
    udn_ie._real_extract("http://video.udn.com/embed/news/300040")


if __name__ == "__main__":
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:27:27.490019
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()(url)

# Generated at 2022-06-14 17:27:36.015506
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    for url in ['http://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/news/300040']:
        assert UDNEmbedIE._match_id(url) == '300040'
    assert UDNEmbedIE._match_id('https://video.udn.com/play/news/303776') == '303776'
    assert UDNEmbedIE._match_id('https://video.udn.com/more_news/303776') is None

# Unit test of function _real_extract()

# Generated at 2022-06-14 17:27:42.659852
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    udn = UDNEmbedIE()
    assert udn.IE_NAME == 'udn'
    assert udn._VALID_URL == udn._VALID_URL
    assert udn._PROTOCOL_RELATIVE_VALID_URL == udn._PROTOCOL_RELATIVE_VALID_URL
    assert udn._TESTS == udn._TESTS

# Generated at 2022-06-14 17:27:47.566900
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('http://video.udn.com/embed/news/300040')

    UDNEmbedIE('https://video.udn.com/embed/news/300040')

    UDNEmbedIE('http://video.udn.com/play/news/300040')


# Generated at 2022-06-14 17:27:49.414740
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:27:54.590764
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Input/output string with/without protocol
    assert UDNEmbedIE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:58.064556
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('udn.com')
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:10.690341
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Check correct initialization of UDNEmbedIE by a valid URL.
    UDNEmbedIE('http://video.udn.com/embed/news/300040')

    # Check incorrect initialization of UDNEmbedIE by an invalid URL.
    try:
        UDNEmbedIE('http://video.udn.com/embed/news/300040ssss')
    except AssertionError:
        pass

# Generated at 2022-06-14 17:28:18.813416
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert UDNEmbedIE._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE.IE_DESC == '聯合影音'
    assert UDNEmbedIE.ie_key() == 'UDNEmbed'
    assert 'UDNEmbedIE' in ie_key_map

# Generated at 2022-06-14 17:28:19.910355
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:28:21.070660
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None)

# Generated at 2022-06-14 17:28:28.176106
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_cases = [
        (
            "http://video.udn.com/embed/news/300040",
            "300040",
        ),
        (
            "https://video.udn.com/embed/news/300040",
            "300040",
        ),
        (
            "http://video.udn.com/play/news/300040",
            "300040",
        ),
    ]
    for url, video_id in test_cases:
        udn = UDNEmbedIE(url)
        assert udn._match_id(url) == video_id

# Generated at 2022-06-14 17:28:38.972829
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert ie._TESTS[0]['info_dict']['title'] == '生物老師男變女 全校挺"做自己"'

# Generated at 2022-06-14 17:28:48.163007
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    e = UDNEmbedIE()
    e._match_id('http://video.udn.com/embed/news/300040')
    e._match_id('//video.udn.com/embed/news/300040')
    e._match_id('http://video.udn.com/play/news/300040')
    e._match_id('//video.udn.com/play/news/300040')
    e._match_id('http://video.udn.com/embed/news/300040')
    e._match_id('//video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:28:52.962026
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    temp = UDNEmbedIE()
    assert temp._PROTOCOL_RELATIVE_VALID_URL is not None
    assert temp._VALID_URL is not None
    assert temp._TESTS is not None
    assert temp.IE_DESC is not None
    assert temp._real_extract('') is not None

# Generated at 2022-06-14 17:28:57.217599
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TESTS == ie.TESTS
    assert ie.IE_DESC == ie.ie_key()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == ie._VALID_URL.replace('https?', '')


# Generated at 2022-06-14 17:28:59.074968
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE('IE')
    obj._real_extract("http://video.udn.com/embed/news/300040")

# Generated at 2022-06-14 17:29:14.011772
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._real_extract(url)

# Generated at 2022-06-14 17:29:15.030485
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(InfoExtractor())

# Generated at 2022-06-14 17:29:16.744601
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert issubclass(UDNEmbedIE, InfoExtractor)

# Generated at 2022-06-14 17:29:24.247009
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    udnVideo = UDNEmbedIE()._real_extract(url)
    print(udnVideo)
    assert isinstance(udnVideo, dict)
    assert '300040' == udnVideo['id']
    assert 'mp4' == udnVideo['formats'][0]['ext']
    assert '生物老師男變女 全校挺"做自己"' == udnVideo['title']


# Generated at 2022-06-14 17:29:27.088513
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # normal
    assert UDNEmbedIE._build_url(video_id="300040", video_type='embed') == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:29:39.316832
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == "//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)"
    assert UDNEmbedIE._VALID_URL == "https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)"
    assert UDNEmbedIE._TESTS[0]['url'] == "http://video.udn.com/embed/news/300040"
    assert UDNEmbedIE._TESTS[0]['info_dict']['id'] == "300040"
    assert UDNEmbedIE._TESTS[0]['info_dict']['ext'] == "mp4"

# Generated at 2022-06-14 17:29:42.227455
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnIE = UDNEmbedIE()
    # test match id
    assert udnIE._match_id('https://video.udn.com/embed/news/300040') == '300040'

# Generated at 2022-06-14 17:29:52.088281
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test the constructor of class UDNEmbedIE
    url = 'https://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    assert ie.IE_NAME == ie.ie_key()
    assert ie.IE_DESC == ie.ie_desc()
    assert ie.WORKING == ie.working()
    assert ie._VALID_URL == ie.valid_url()
    assert ie._TESTS == ie.tests()
    assert ie.PROTOCOL_RELATIVE_VALID_URL == ie.protocol_relative_valid_url()

    # Test the method _real_extract()
    page = ie._download_webpage(url, "300040")

# Generated at 2022-06-14 17:30:00.833281
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from ..test import get_testcases
    test_cases = get_testcases(UDNEmbedIE, [UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL])
    assert test_cases == [
        {
            'url': 'https://video.udn.com/embed/news/300040',
            'only_matching': True,
        },
        {
            'url': 'http://video.udn.com/play/news/300040',
            'only_matching': True,
        }
    ]

# Generated at 2022-06-14 17:30:02.577365
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie is not None

# Generated at 2022-06-14 17:30:36.427190
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    udneie = UDNEmbedIE()
    assert udneie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udneie._match_id(url) == '300040'
    assert '聯合影音' in udneie._real_extract(url)['title']

# Generated at 2022-06-14 17:30:44.579882
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:30:54.099682
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # Check if the protocol relative url can be processed
    test_url = '//video.udn.com/embed/news/300040'
    assert(ie._match_id(test_url) == '300040')
    assert(ie._match_id(test_url, strict=True) == None)
    # Check if the protocol relative url can be transformed to valid url
    url_transformed = ie._PROTOCOL_RELATIVE_URL_TEMPLATE % {'url': test_url}
    assert(ie._match_id(url_transformed) == '300040')
    assert(ie._match_id(url_transformed, strict=True) == None)
    # Check if the valid url can be processed

# Generated at 2022-06-14 17:30:56.848132
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_ie = UDNEmbedIE()
    # verify correct IE type
    assert udn_ie.ie_key() == 'udn'


# Generated at 2022-06-14 17:31:03.655570
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Check _PROTOCOL_RELATIVE_VALID_URL
    assert(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

    # Check _VALID_URL
    assert(UDNEmbedIE._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

# Generated at 2022-06-14 17:31:11.705264
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE.IE_DESC == '聯合影音'




# Generated at 2022-06-14 17:31:21.002404
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL # what is this for?
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:31:31.671624
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('https://video.udn.com/embed/news/300040')
    expected_app_name = 'UDNEmbedIE'
    assert ie.app_name == expected_app_name, 'Expected app_name "{}", but it is "{}"'.format(expected_app_name, ie.app_name)
    expected_ie_key = 'UDNEmbed'
    assert ie.ie_key == expected_ie_key, 'Expected ie_key "{}", but it is "{}"'.format(expected_ie_key, ie.ie_key)
    expected_re = 'https?:(//video\.udn\.com/(?:embed|play)/news/(\\d+))'
    expected_flags = 0
    actual_re = ie._VALID_URL

# Generated at 2022-06-14 17:31:39.710399
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://example.com/')
    assert ie.IE_NAME == 'udn:embed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:31:42.221113
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        udn_obj = UDNEmbedIE()
        assert(True)
    except:
        assert(False)

# Generated at 2022-06-14 17:33:00.594464
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'


# Generated at 2022-06-14 17:33:01.500726
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(InfoExtractor())

# Generated at 2022-06-14 17:33:12.660868
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Constructor test of class UDNEmbedIE"""
    from ..extractor import gen_extractors_by_ie
    ie_list = list(gen_extractors_by_ie(UDNEmbedIE.ie_key()))
    assert len(ie_list) is 1
    ie_instance = ie_list[0]
    assert ie_instance.ie_key() == 'UDNEmbed'
    assert ie_instance.IE_NAME == 'UDN'
    assert ie_instance.ie_desc() == '聯合影音'
    assert ie_instance._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:33:18.048563
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert len(ie._TESTS) == 3

# Generated at 2022-06-14 17:33:21.630139
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._VALID_URL = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    UDNEmbedIE()._TESTS = [{
        'url': url,
    }]
    UDNEmbedIE()._real_initialize()
    assert UDNEmbedIE()._VALID_URL == UDNEmbedIE._VALID_URL
    assert UDNEmbedIE()._TESTS == [{
        'url': 'https:' + url,
    }]

# Generated at 2022-06-14 17:33:24.233633
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # ANCHOR format test
    url = 'https://video.udn.com/embed/news/300040'
    UDNEmbedIE()._match_id(url)

# Generated at 2022-06-14 17:33:32.472973
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    '''
    Test the constructor of class UDNEmbedIE
    '''
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'


# Generated at 2022-06-14 17:33:41.566178
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import TestServer
    # start a test server running,
    # which serves the file test/testdata/test.mp4
    # and will be stopped automatically
    with TestServer() as test_server:
        # pass the local address of the test server
        # as the first parameter of constructor
        # of class UDNEmbedIE
        udn_embed_ie = UDNEmbedIE(test_server.get_url())
        assert udn_embed_ie._VALID_URL == r'https?:%s' % re.escape(test_server.get_url())
        assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == re.escape(test_server.get_url())
        # call the method to get information of test video
        # URL is the test video URL which is served by

# Generated at 2022-06-14 17:33:48.229110
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # protocol relative URL
    _PROTOCOL_RELATIVE_VALID_URL = r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    ie = UDNEmbedIE(None)
    ie._real_initialize()
    mobj = ie._extract_video_id_from_url(_PROTOCOL_RELATIVE_VALID_URL, url_protocol_relative=True)
    assert mobj is not None
    # normal URL
    _VALID_URL = r'https?:' + _PROTOCOL_RELATIVE_VALID_URL
    ie = UDNEmbedIE(None)
    ie._real_initialize()
    mobj = ie._extract_video_id_from_url(_VALID_URL)

# Generated at 2022-06-14 17:33:50.946031
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from ..utils import _test_recognize_IE
    _test_recognize_IE(UDNEmbedIE)

# Generated at 2022-06-14 17:36:30.773784
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_obj_UDNEmbed = UDNEmbedIE()
    assert(test_obj_UDNEmbed != None)

# Generated at 2022-06-14 17:36:38.415488
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # case 1
    url = 'http://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE().url_result(url)
    ie_desc = ie.IE_NAME
    expected_output = 'UDNEmbed'
    assert ie_desc == expected_output, 'Constructor of class UDNEmbedIE should be %s!' % expected_output

    # case 2
    url = 'https://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE().url_result(url)
    ie_desc = ie.IE_NAME
    expected_output = 'UDNEmbed'
    assert ie_desc == expected_output, 'Constructor of class UDNEmbedIE should be %s!' % expected_output

    # case 3

# Generated at 2022-06-14 17:36:47.884127
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:36:52.054357
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test the constructor of class UDNEmbedIE
    # It should accept the following URL
    UDNEmbedIE(None)._PROTOCOL_RELATIVE_VALID_URL
    UDNEmbedIE(None)._VALID_URL

# Generated at 2022-06-14 17:36:52.875171
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()