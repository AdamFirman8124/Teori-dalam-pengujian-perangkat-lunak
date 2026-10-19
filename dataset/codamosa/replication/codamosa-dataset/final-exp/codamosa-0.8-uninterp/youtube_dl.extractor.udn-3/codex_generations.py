

# Generated at 2022-06-14 17:27:15.868229
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert ("https://video.udn.com/embed/news/300878", False) == UDNEmbedIE._match_url("https://video.udn.com/embed/news/300878")
    assert ("https://video.udn.com/embed/news/300878", False) == UDNEmbedIE._match_url("http://video.udn.com/embed/news/300878")
    assert ("https://video.udn.com/embed/news/300878", False) == UDNEmbedIE._match_url("https://video.udn.com/embed/news/300878")

# Generated at 2022-06-14 17:27:25.782014
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnEmbedIE = UDNEmbedIE()
    ie = udnEmbedIE
    # test PRIVATE static property _PROTOCOL_RELATIVE_VALID_URL
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    # test PRIVATE static property _VALID_URL
    assert ie._VALID_URL == 'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

    # test function _real_extract
    url = 'http://video.udn.com/embed/news/300040'
    video_id = udnEmbedIE._match_id(url)
    assert video_id == '300040'
    page = udnEmbedIE

# Generated at 2022-06-14 17:27:27.972677
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:27:39.005223
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert len(ie._TESTS) == 3
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:27:42.533450
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Instantiate the class and run its internal function `_real_extract`
    # by passing a url to the video page
    UDNEmbedIE()._real_extract('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:27:43.409097
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	obj = UDNEmbedIE()


# Generated at 2022-06-14 17:27:46.223992
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Instantiate an object of class UDNEmbedIE
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    return

# Generated at 2022-06-14 17:27:48.233442
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:27:55.372627
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # test to set format
    formats = [
        {'a': 'b'},
        {'c': 'd'},
        {'e': 'f'},
    ]
    ie.set_formats(formats)
    assert len(ie.formats) == len(formats)


# Generated at 2022-06-14 17:27:56.948791
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie is not None

# Generated at 2022-06-14 17:28:12.052079
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:15.538139
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:18.986475
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # Test function _real_extract()
    ie._real_extract('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:28:22.586157
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    regex_result = UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL
    assert regex_result == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:25.886201
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    pattern = re.compile(r'//video\.udn\.com/embed/news/\d+')
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == pattern.pattern

# Generated at 2022-06-14 17:28:27.146932
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()



# Generated at 2022-06-14 17:28:34.896721
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.IE_DESC == '聯合影音'
    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_ie._VALID_URL == r'https?:' + udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL


# Generated at 2022-06-14 17:28:37.909794
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_test_case = UDNEmbedIE(InfoExtractor)
    print(udn_test_case)

# Generated at 2022-06-14 17:28:43.916373
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    temp_UDNEmbedIE = UDNEmbedIE()
    assert temp_UDNEmbedIE.ie_key() == 'UDNEmbed'
    assert temp_UDNEmbedIE.IE_NAME == '聯合影音'
    assert temp_UDNEmbedIE.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:28:45.956195
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test the definition of class UDNEmbedIE."""
    UDNEmbedIE()

# Generated at 2022-06-14 17:29:19.570947
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    test_cases = [{
        'url': 'http://video.udn.com/embed/news/300040',
        'id': '300040',
        'title': '生物老師男變女 全校挺"做自己"',
    }]
    for test_case in test_cases:
        url = test_case['url']
        video_id = test_case['id']
        title = test_case['title']
        info_dict = ie.extract(url)
        assert video_id == info_dict['id']
        assert title == info_dict['title']
        assert isinstance(info_dict['thumbnail'], str)

# Generated at 2022-06-14 17:29:23.981940
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_PROTOCOL_RELATIVE_VALID_URL')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, 'IE_DESC')

# Generated at 2022-06-14 17:29:26.676618
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Run some basic tests on the constructor of class UDNEmbedIE."""
    ie = UDNEmbedIE()
    # Test: simple initialization
    ie.__init__()



# Generated at 2022-06-14 17:29:29.161457
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Unit test for constructor of class UDNEmbedIE
    """
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'udn'

# Generated at 2022-06-14 17:29:32.104840
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:29:41.377846
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.suitable('http://video.udn.com/embed/news/300040')
    assert not udn_embed_ie.suitable('http://video.udn.com/news/300040')
    assert udn_embed_ie.suitable('https://video.udn.com/embed/news/300040')
    assert not udn_embed_ie.suitable('https://video.udn.com/news/300040')
    assert udn_embed_ie.suitable('//video.udn.com/embed/news/300040')
    assert udn_embed_ie.suitable('//video.udn.com/play/news/300040')

# Generated at 2022-06-14 17:29:45.668236
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL


# Generated at 2022-06-14 17:29:49.891993
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url='http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._real_extract(url)


# Generated at 2022-06-14 17:29:53.406693
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    the_url = 'http://video.udn.com/embed/news/300040'
    the_result = UDNEmbedIE()._real_extract(the_url)
    assert the_result['id'] == '300040'

# Generated at 2022-06-14 17:30:00.565049
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert udne.IE_NAME == 'UDNEmbed'
    assert udne.IE_DESC == '聯合影音'
    assert udne._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udne._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:30:27.211524
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
  assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:31.444775
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from . import _get_testcases
    return _get_testcases(__name__, UDNEmbedIE, [])

# Generated at 2022-06-14 17:30:36.641863
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from unittest import TestCase

    class TestUDNEmbedIE(TestCase):
      def test_parse_headline_id(self):
        
        class testInput:
            def __init__(self, headline_id):
                self.headline_id = headline_id
        

# Generated at 2022-06-14 17:30:46.595963
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    for test in ie._TESTS:
        ie_result = ie.suitable(test['url'])
        assert ie_result

        if 'info_dict' in test:
            # Extract
            result = ie.extract(test['url'])

            # Compare result
            for key, value in test['info_dict'].items():
                assert_result = result.get(key)
                assert assert_result == value, ('%s field: %s != %s' % (key, assert_result, value))

# Generated at 2022-06-14 17:30:49.896339
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_obj = UDNEmbedIE()
    assert udn_embed_obj._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:58.745232
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnEmbedIE = UDNEmbedIE()
    assert udnEmbedIE.IE_NAME == 'udn_embed'
    assert udnEmbedIE.IE_DESC == '聯合影音'
    assert udnEmbedIE._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udnEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:31:11.185486
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    info_dict = {
        'id': '300040',
        'ext': 'mp4',
        'title': '生物老師男變女 全校挺"做自己"',
        'thumbnail': r're:^https?://.*\.jpg$',
    }
    params = {
        # m3u8 download
        'skip_download': True,
    }
    expected_warnings = ['Failed to parse JSON Expecting value']
    # Unit test for _real_extract() of class UDNEmbedIE

# Generated at 2022-06-14 17:31:24.651478
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_IE = UDNEmbedIE()
    assert udn_embed_IE.IE_DESC == '聯合影音'
    assert udn_embed_IE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'

# Generated at 2022-06-14 17:31:25.704485
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert True

# Generated at 2022-06-14 17:31:36.126906
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE()._VALID_URL == r'https?:' + UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE().IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:32:45.882869
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('https://video.udn.com/play/news/303776')

# Generated at 2022-06-14 17:32:53.780704
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    udneie = UDNEmbedIE()
    assert udneie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udneie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udneie._match_id(url) == '300040'

# Generated at 2022-06-14 17:32:54.527346
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None, None)

# Generated at 2022-06-14 17:33:02.029055
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    instance = UDNEmbedIE(url)

    assert instance.protocol_relative_valid_url == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert instance.valid_url == r'https?:' + instance.protocol_relative_valid_url

# Generated at 2022-06-14 17:33:05.541822
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    Obj = UDNEmbedIE(None)
    assert Obj._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert Obj._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:33:08.050765
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor of UDNEmbedIE should able to initialize with a valid url
    UDNEmbedIE('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:33:14.292447
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL = r'//video\.udn\.com/embed/news/(?P<id>\d+)'
    UDNEmbedIE._VALID_URL = r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    ie = UDNEmbedIE()
    #print(ie._VALID_URL)
    #print(type(ie._VALID_URL))

    #print(ie._PROTOCOL_RELATIVE_VALID_URL)
    #print(type(ie._PROTOCOL_RELATIVE_VALID_URL))

    #match_obj = re.search(ie._VALID_URL, url)

# Generated at 2022-06-14 17:33:15.183612
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == "UDNEmbed"

# Generated at 2022-06-14 17:33:17.079096
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:33:18.146629
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('')
    ie.IE_NAME
    ie.IE_DESC
    ie._VALID_URL

# Generated at 2022-06-14 17:35:33.617916
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:35:40.957266
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert ie._TESTS[0]['info_dict']['title'] == '生物老師男變女 全校挺"做自己"'
   

# Generated at 2022-06-14 17:35:42.011548
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie

# Generated at 2022-06-14 17:35:46.993142
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:35:57.387939
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/embed/news/300040'

    info_dict = {
        'id': '300040',
        'ext': 'mp4',
        'title': '生物老師男變女 全校挺"做自己"',
        'thumbnail': r're:^https?://.*\.jpg$',
    }
    params = {
        # m3u8 download
        'skip_download': True,
    }
    expected_warnings = ['Failed to parse JSON Expecting value']

    test_dict = {
        'url': url,
        'info_dict': info_dict,
        'params': params,
        'expected_warnings': expected_warnings,
    }
    assert UDNE

# Generated at 2022-06-14 17:36:02.198353
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    base_url = 'https://video.udn.com/embed/news/300040'
    instance = UDNEmbedIE(base_url)
    assert (instance._VALID_URL, base_url)
    assert instance._PROTOCOL_RELATIVE_VALID_URL == r'//video.udn.com/embed/news/(?P<id>\d+)'
    assert instance._match_id(base_url) == "300040"
    assert instance.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:36:11.375611
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Create a class
    udne = UDNEmbedIE()
    # Test the first use case of _match_id
    test_match_url = 'http://video.udn.com/embed/news/300040'
    test_match_id = udne._match_id(test_match_url)
    assert test_match_id == '300040' , "Test for extracting video id from url failed."
    # Test the second use case of _match_id
    test_match_id = udne._match_id(None, '300040')
    assert test_match_id == '300040' , "Test for extracting video id from argument failed."
    # Test the _real_extract function
    # Sidenote:
    #   Some test cases cannot be tested here because they use
    #   _html_

# Generated at 2022-06-14 17:36:14.025296
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/890"
    UDNEmbedIE()._real_extract(url)


# Generated at 2022-06-14 17:36:17.952377
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == IE_NAME
    assert ie.IE_DESC == IE_DESC
    pattern = re.compile(
        r'(https?:)?//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    )
    assert pattern == ie._VALID_URL

# Generated at 2022-06-14 17:36:22.851167
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert udne.IE_NAME == 'UDNEmbed'
    assert udne._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udne.IE_DESC == '聯合影音'