

# Generated at 2022-06-14 17:27:16.023583
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    _UDNEmbedIE = UDNEmbedIE(UDNEmbedIE.ie_key())
    assert _UDNEmbedIE.info_extractors[-1].IE_KEY == UDNEmbedIE.ie_key()
    assert _UDNEmbedIE.ie_key() == UDNEmbedIE.ie_key()
    assert _UDNEmbedIE.ie_key() is not None
    assert _UDNEmbedIE._VALID_URL is not None
    assert _UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL is not None
    assert _UDNEmbedIE._TESTS is not None
    # call _real_extract() method to ensure there is no exception raised
    for _test in _UDNEmbedIE._TESTS:
        _UDNEmbed

# Generated at 2022-06-14 17:27:25.634682
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    info_extractor = UDNEmbedIE()
    video_url = 'https://video.udn.com/embed/news/300040'

    info_extractor._real_extract(video_url)
    assert(info_extractor._match_id(video_url) == '300040')
    assert(info_extractor._VALID_URL ==
           'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)')
    assert(info_extractor._PROTOCOL_RELATIVE_VALID_URL ==
           '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:27:37.179877
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnEmbedIE = UDNEmbedIE()
    assert udnEmbedIE._REGEX_VIDEO_ID == r'(?P<id>\d{6})'
    assert udnEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udnEmbedIE._VALID_URL == r'https?:' + udnEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:27:42.195047
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    ret = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    m = re.match(ret, url)
    assert m, 'URL {} do not match pattern {}'.format(url, ret)
    print('')

# Generated at 2022-06-14 17:27:51.122048
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    constructor_input_output_list = [
        # (input, output)
        (UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL, [r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL]),
        ("https://www.bing.com/", [])
    ]
    for constructor_input, expected_output in constructor_input_output_list:
        ie = UDNEmbedIE(constructor_input)
        assert ie._VALID_URL == expected_output


# Generated at 2022-06-14 17:28:02.349334
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:28:08.621408
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    #test 1
    _URL = 'http://video.udn.com/embed/news/300040'
    url = _URL
    xie = UDNEmbedIE()
    test_str = xie.extract(url)
    assert xie._VALID_URL == 'https?:' + '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert xie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert xie.IE_DESC == '聯合影音'
    assert xie.IE_NAME == 'UDNEmbed'


# Generated at 2022-06-14 17:28:10.403244
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:28:11.905841
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie is not None

# Generated at 2022-06-14 17:28:18.328062
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie_instance = UDNEmbedIE()

    ret_str = ie_instance._PROTOCOL_RELATIVE_VALID_URL
    assert isinstance(ret_str, str) == True
    assert ret_str == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    ret_str = ie_instance._VALID_URL
    assert isinstance(ret_str, str) == True
    assert ret_str == r'https?:' + ie_instance._PROTOCOL_RELATIVE_VALID_URL

    ret_dict = ie_instance._TESTS[0]
    assert isinstance(ret_dict, dict) == True
    assert ret_dict['url'] == 'http://video.udn.com/embed/news/300040'

    ret_dict

# Generated at 2022-06-14 17:28:33.101915
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    i = UDNEmbedIE()

test_UDNEmbedIE()

# Generated at 2022-06-14 17:28:40.555981
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    # Test _PROTOCOL_RELATIVE_VALID_URL
    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # Test _VALID_URL
    assert udn_embed_ie._VALID_URL == 'https?:' + udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL
    # Test _TEST

# Generated at 2022-06-14 17:28:48.968142
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class_UDNEmbedIE = UDNEmbedIE()
    assert class_UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert class_UDNEmbedIE._VALID_URL == r'https?:' + class_UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert class_UDNEmbedIE.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:28:56.010432
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Constructor test
    """
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == ie._VALID_URL.replace('(', '(?:').replace(')', ')?')
    assert ie._VALID_URL == ie._VALID_URL.replace('^', '^(?:https?:)?//')

# Generated at 2022-06-14 17:28:58.681198
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(UDNEmbedIE._create_ie_instance())
    print(str(ie))
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:29:05.708211
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:29:17.885997
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # FIXME: since this test is not test of the class UDNEmbedIE,
    # it should be put in a separated unit test file.
    # However, it is not very easy to move this test out of this file
    # because the class UDNEmbedIE is dynamically initialized
    # to add an entry to _EXT_TO_IE, for backward compatibility.
    url = 'http://video.udn.com/embed/news/300040'
    udn_embed_ie = UDNEmbedIE._build_extractor({'url': url, 'ie': 'UDNEmbed'})
    assert udn_embed_ie.name == 'UDNEmbed'
    assert udn_embed_ie._VALID_URL == r'https?://video\.udn\.com/embed/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:29:20.514642
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """ test for constructor of class UDNEmbedIE """
    assert UDNEmbedIE != None
    print("test_UDNEmbedIE: test for constructor of class UDNEmbedIE passed!")



# Generated at 2022-06-14 17:29:29.549216
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:29:38.786099
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_case = [{
        'url': 'http://video.udn.com/embed/news/300040',
        'expected_video_id': '300040'
    }, {
        'url': 'https://video.udn.com/play/news/300040',
        'expected_video_id': '300040'
    }]
    for tc in test_case:
        ud_embed_ie = UDNEmbedIE()
        assert ud_embed_ie._match_id(tc['url']) == tc['expected_video_id']


# Generated at 2022-06-14 17:30:12.873246
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    def test_constructor(url, id, ie):
        ie = ie
        if ie is not None:
            assert isinstance(ie, InfoExtractor)
            assert id == ie._match_id(url)
        else:
            assert ie is None
    ie = UDNEmbedIE(None)

    test_constructor('http://video.udn.com/embed/news/300040', '300040', ie)
    test_constructor('http://video.udn.com/news/300040', None, ie)

# Generated at 2022-06-14 17:30:20.492450
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    assert ie._match_id(url) == '300040'
    assert ie._real_extract(url)['formats'][0]['url'] == 'https://cc.udn.com.tw/v1/static/news/300040/mp4_1280x720_1500k.mp4'

# Generated at 2022-06-14 17:30:25.094098
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:30:36.515273
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from youtube_dl.utils import regex_search
    # test for regex_search function in class InfoExtractor
    assert regex_search(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL, '//video.udn.com/embed/news/300040') == ('//video.udn.com/embed/news/300040', {'id': '300040'})
    # test for IE_DESC property in class InfoExtractor
    assert UDNEmbedIE.IE_DESC == '聯合影音'
    # test for _VALID_URL property in class InfoExtractor
    assert UDNEmbedIE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # test for _TES

# Generated at 2022-06-14 17:30:43.517879
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    url = ie._TESTS[0]['url']
    assert ie.suitable(url) == True
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:48.314386
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # most simple case
    UDNEmbedIE(None, 'https://video.udn.com/embed/news/300040')

    # with options
    UDNEmbedIE(None, {'url': 'https://video.udn.com/embed/news/300040'})

# Generated at 2022-06-14 17:30:50.029397
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL



# Generated at 2022-06-14 17:30:51.777959
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE


# Generated at 2022-06-14 17:30:53.013089
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:30:54.893488
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE(None)._VALID_URL == UDNEmbedIE._VALID_URL

# Generated at 2022-06-14 17:31:31.155108
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    IE = UDNEmbedIE()
    assert IE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert IE.IE_NAME == IE.__class__.__name__
    assert IE.IE_DESC == '聯合影音'
    assert IE._VALID_URL == 'https?:' + IE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:31:34.004606
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed = UDNEmbedIE('https://video.udn.com/embed/news/300040')
    udn_embed.to_screen('[udn_embed]')
    return udn_embed

# Generated at 2022-06-14 17:31:39.521080
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test creation of class UDNEmbedIE"""
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'

    url = 'http://video.udn.com/embed/news/300040'
    match = ie._VALID_URL.match(url)
    assert match
    assert match.lastgroup == 'id'
    assert ie._match_id(url) == '300040'
    assert ie._real_extract(url) is not None

# Generated at 2022-06-14 17:31:42.948442
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._match_id(ie._VALID_URL) == ie._match_id(ie._PROTOCOL_RELATIVE_VALID_URL)

# Generated at 2022-06-14 17:31:54.271938
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # _PROTOCOL_RELATIVE_VALID_URL is not valid yet, fix it with adding scheme
    ie.match_url = lambda _: ie._PROTOCOL_RELATIVE_VALID_URL
    ie.match_id = lambda _: '300040'

# Generated at 2022-06-14 17:31:55.884403
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    h = UDNEmbedIE()
    h.ie_key()
    h.suitable()
    h.add_ie()


# Generated at 2022-06-14 17:32:05.973916
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print("Testing UDNEmbedIE...")
    udn_embed_extractor = UDNEmbedIE()
    url_list = [
        "http://video.udn.com/embed/news/300040",
        "https://video.udn.com/embed/news/300040",
        "https://video.udn.com/play/news/303776",
    ]
    for url in url_list:
        print("Testing UDNEmbedIE with url {}".format(url))
        info_dict = udn_embed_extractor._real_extract(url)
        for key in info_dict.keys():
            print("Testing key {}".format(key))
            print("Value: {}".format(info_dict[key]))

if __name__ == '__main__':
    test_

# Generated at 2022-06-14 17:32:08.587301
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test = "http://video.udn.com/embed/news/300040"
    obj = UDNEmbedIE()
    assert obj._match_id(test)

# Generated at 2022-06-14 17:32:17.804934
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._VALID_URL == \
        'https?://video.udn.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert ie.IE_DESC == '聯合影音'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[1]['url'] == 'https://video.udn.com/embed/news/300040'
    assert 'Failed to parse JSON Expecting value' in ie._TESTS[0]['expected_warnings']

# Generated at 2022-06-14 17:32:24.371541
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print("testing UDNEmbedIE ...")
    video = UDNEmbedIE()
    video._match_id("http://video.udn.com/news/300040")
    video.IE_DESC
    video._PROTOCOL_RELATIVE_VALID_URL
    video._VALID_URL
    video._TESTS
    print("finished testing UDNEmbedIE")

if __name__ == "__main__":
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:33:39.815064
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    i = UDNEmbedIE()
    i.extractor.IE_DESC = 'Example'
    i.extractor._PROTOCOL_RELATIVE_VALID_URL = r'//example\.com/'
    i.extractor._VALID_URL = r'https?://example\.com/'

# Generated at 2022-06-14 17:33:49.585566
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:33:50.945258
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:33:57.548745
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	import unittest

	class UDNEmbedIETest(unittest.TestCase):
		def test_UDNEmbedIE(self):
			UDNEmbedIE()._match_id('//video.udn.com/embed/news/300040')

	unittest.main(argv=['first-arg-is-ignored'], exit=False)

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:34:07.555763
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/300040') == '300040'
    assert ie._match_id('//video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('//video.udn.com/play/news/300040') == '300040'

    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:34:12.277228
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE(UDNEmbedIE.create_ie()).url_result(url)
    # Test if it works with `&` in the url
    url = url + '&id=id'
    UDNEmbedIE(UDNEmbedIE.create_ie()).url_result(url)

# Generated at 2022-06-14 17:34:13.363749
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:34:20.124192
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import InfoExtractor
    from ..utils import (
        determine_ext,
        int_or_none,
        js_to_json,
    )
    from ..compat import compat_urlparse

    ie = UDNEmbedIE()
    # testing for invalid_url
    assert ie.suitable('http://video.udn.com/embed/news/300040') == False

    ie = InfoExtractor()
    # testing for suitable
    assert ie.suitable('http://video.udn.com/embed/news/300040') == True

# Generated at 2022-06-14 17:34:25.850781
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Regular cases
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:34:28.002846
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('input_url')

if __name__ == '__main__':
    print(test_UDNEmbedIE())