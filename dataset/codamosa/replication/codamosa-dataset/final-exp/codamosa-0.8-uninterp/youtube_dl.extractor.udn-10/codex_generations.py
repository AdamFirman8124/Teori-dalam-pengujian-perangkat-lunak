

# Generated at 2022-06-14 17:27:09.673032
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(IE_DESC)
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:27:11.628212
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    id = '300040'
    url = 'http://video.udn.com/embed/news/' + id
    print(url)
    #url="https://video.udn.com/embed/news/300040/"
    udn._real_extract(url)

# Generated at 2022-06-14 17:27:19.515015
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.IE_NAME == 'udn'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[1]['url'] == 'https://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:27:27.569157
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # pylint: disable=no-member
    # -*- coding: utf-8 -*-
    import os
    import unittest
    class TestUDNEmbedIE(unittest.TestCase):
        def setUp(self):
            self.ie = UDNEmbedIE()
            self.ie.ydl.params['forcejson'] = True
            self.ie.ydl.params['skip_download'] = True
        def test_search_regex(self):
            # pattern: r'var\s+options\s*=\s*([^;]+);',
            text = 'var options = app.config;'
            result = self.ie._html_search_regex(r'var\s+options\s*=\s*([^;]+);', text, 'options')
            self

# Generated at 2022-06-14 17:27:31.047272
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test UDNEmbedIE class constructor."""
    youtube_ie = UDNEmbedIE()
    assert youtube_ie.ie_key() == 'UDNEmbed'
    assert youtube_ie.ie_desc() == '聯合影音'

# Generated at 2022-06-14 17:27:32.917772
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None)

# Generated at 2022-06-14 17:27:43.834870
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    expected_description = '聯合影音'
    expected_ie_key = 'UDNEmbed'
    # Instantiate the unit test object
    udn_embed_test_obj = UDNEmbedIE(url)
    # Print out the object's description
    print('Description: ', udn_embed_test_obj.IE_DESC)
    # Print out the object's IE_KEY
    print('IE_key: ', udn_embed_test_obj.IE_KEY)
    # Check if the description matches the expected description
    assert udn_embed_test_obj.IE_DESC == expected_description
    # Check if the ie_key matches the expected ie_key
    assert udn_embed_test_

# Generated at 2022-06-14 17:27:50.067898
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    embed_ie = UDNEmbedIE()
    embed_ie._match_id(url)
    embed_ie._real_extract(url)
    embed_ie._match_id('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:27:59.292378
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    __URL__ = 'https://video.udn.com/embed/news/300040'
    __VIDEO_ID__ = '300040'
    __EXPECTED_TITLE__ = '生物老師男變女 全校挺"做自己"'
    
    instance = UDNEmbedIE(__URL__)
    video = instance._real_extract(__URL__)

    assert video['id'] == __VIDEO_ID__
    assert video['title'] == __EXPECTED_TITLE__

# Generated at 2022-06-14 17:28:06.578606
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:28:28.568125
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Init
    udn_embed_ie = UDNEmbedIE()
    # Successful cases
    assert(udn_embed_ie.suitable('https://video.udn.com/embed/news/300040'))
    assert(udn_embed_ie.suitable('http://video.udn.com/embed/news/300040'))
    assert(udn_embed_ie.suitable('https://video.udn.com/play/news/303776'))
    assert(udn_embed_ie.suitable('http://video.udn.com/play/news/303776'))
    # Unsuccessful cases
    assert(not udn_embed_ie.suitable('https://video.udn.com/embed'))

# Generated at 2022-06-14 17:28:39.031733
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import unittest
    import pycountry
    u = UDNEmbedIE()
    assert(u.IE_NAME == 'udn')
    assert('udn.com' in u._VALID_URL)

    test_str_1 = '//video.udn.com/embed/news/300040'
    test_str_2 = 'http://video.udn.com/embed/news/300040'
    test_str_3 = 'http://www.udn.com/'
    test_str_4 = 'http://vod.udn.com/embed/news/300040'
    test_str_5 = 'http://video.udn.com/play/news/300040'
    test_str_6 = 'http://video.udn.com/play/news/300040/123'
   

# Generated at 2022-06-14 17:28:46.057599
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    expected_url_match = r'http://video\.udn\.com/(?:embed|play)/news/(\d+)'
    assert obj._VALID_URL == 'https?:' + expected_url_match
    assert obj._PROTOCOL_RELATIVE_VALID_URL == expected_url_match

assert UDNEmbedIE.__name__ == 'UDNEmbedIE'

# Generated at 2022-06-14 17:28:47.919907
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)



# Generated at 2022-06-14 17:28:50.756368
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test whether we can get the udnei object
    udnei = UDNEmbedIE()
    assert(udnei != None)

# Generated at 2022-06-14 17:28:54.314518
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():

    url = 'https://video.udn.com/embed/news/300040'
    urlsplit = compat_urlparse.urlsplit(url)

    assert urlsplit.scheme == 'https'
    assert urlsplit.netloc == 'video.udn.com'



# Generated at 2022-06-14 17:28:55.874540
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == '聯合影音'

# Generated at 2022-06-14 17:29:03.572406
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert UDNEmbedIE._TESTS[0]['info_dict']['id'] == '300040'
    assert UDNEmbedIE._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:29:06.025398
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    assert obj.IE_NAME == 'udn'

# Generated at 2022-06-14 17:29:07.489444
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    pass

# Generated at 2022-06-14 17:29:24.526639
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE().IE_NAME == 'udn'
    assert UDNEmbedIE().IE_DESC == '聯合影音'
    assert UDNEmbedIE()._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:29:32.744916
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_dict = {
        'url': 'http://video.udn.com/embed/news/300040',
        'info_dict': {
            'id': '300040',
            'ext': 'mp4',
            'title': '生物老師男變女 全校挺"做自己"',
            'thumbnail': r're:^https?://.*\.jpg$',
        },
        'params': {
            # m3u8 download
            'skip_download': True,
        },
        'expected_warnings': ['Failed to parse JSON Expecting value'],
    }
    test_extractor = UDNEmbedIE()
    test_url = test_dict['url']
    # Check whether the URL matches the test's one


# Generated at 2022-06-14 17:29:33.761201
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

# Generated at 2022-06-14 17:29:41.147607
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    inst = UDNEmbedIE()
    print('Testing constructor of class UDNEmbedIE')
    # Testing _PROTOCOL_RELATIVE_VALID_URL
    assert inst._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # Testing _VALID_URL
    assert inst._VALID_URL == r'https?:' + inst._PROTOCOL_RELATIVE_VALID_URL
    # Testing IE_DESC
    assert inst.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:29:51.812667
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_cases = [{
        'assert_in': {
            'url': 'http://video.udn.com/embed/news/300040',
            'expected_IE_NAME': 'UDNEmbed'
        },
        'assert_raises': {
            'url': 'https://vimeo.com/172769459'
        }
    }, {
        'assert_in': {
            'url': 'https://video.udn.com/embed/news/300040'
        }
    }, {
        'assert_in': {
            'url': 'https://video.udn.com/play/news/303776'
        }
    }]

    for test_dict in test_cases:
        if 'assert_in' in test_dict:
            assert_in_dict = test_dict

# Generated at 2022-06-14 17:29:59.780471
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    print(dir(ie))
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:01.160726
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Unit test for constructor of class UDNEmbedIE"""
    UDNEmbedIE()

# Generated at 2022-06-14 17:30:02.863618
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert isinstance(UDNEmbedIE(InfoExtractor()), InfoExtractor)

# Generated at 2022-06-14 17:30:04.788084
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE("https://video.udn.com/embed/news/300040")

# Generated at 2022-06-14 17:30:14.304512
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test with valid url
    UDNEmbedIE('http://video.udn.com/embed/news/300040')
    UDNEmbedIE('https://video.udn.com/embed/news/300040')
    # test with invalid url
    UDNEmbedIE('http://photo.udn.com/embed/news/300040')
    UDNEmbedIE('http://face.udn.com/embed/news/300040')
    # check for exception
    assert UDNEmbedIE('http://photo.udn.com/embed/news/300040') is None

# Generated at 2022-06-14 17:30:50.492158
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    assert obj.IE_NAME == 'udn'
    assert obj.IE_DESC == '聯合影音'
    assert obj._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert obj._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:52.033280
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE.suitable('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:30:56.676513
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """ Test constructor of class UDNEmbedIE """
    ctor = UDNEmbedIE.__init__
    assert_equal(UDNEmbedIE._VALID_URL, r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

# Generated at 2022-06-14 17:30:57.880713
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('test_UDNEmbedIE')

# Generated at 2022-06-14 17:30:59.317237
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test initialization
    udn_ie = UDNEmbedIE()


# Generated at 2022-06-14 17:31:10.274905
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
  url = 'http://video.udn.com/embed/news/300040'
  result = UDNEmbedIE()._real_extract(url)
  assert result['id'] == '300040'
  assert result['formats'][0]['tbr'] == 300
  assert result['title'] == '生物老師男變女 全校挺"做自己"'
  assert result['thumbnail'] == 'http://img.youtube.com/vi/lR1QYVwUBDQ/hqdefault.jpg'

if __name__ == '__main__':
  test_UDNEmbedIE()

# Generated at 2022-06-14 17:31:12.248276
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = '//video.udn.com/embed/news/300040'
    UDNEmbedIE._build_url_result(url)

# Generated at 2022-06-14 17:31:18.534624
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Quick test for constructor of class UDNEmbedIE
    url = 'https://video.udn.com/play/news/303776'
    udne = UDNEmbedIE.ie_key(url)
    assert udne == 'udn'
    udne_o = UDNEmbedIE()
    assert url == udne_o.working_as_of

# Generated at 2022-06-14 17:31:21.630046
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    

# Generated at 2022-06-14 17:31:23.952133
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from unittest.mock import Mock
    from ..extractor.common import InfoExtractor

    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:32:30.746281
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Exercise constructor
    test_cases = [('https://video.udn.com/embed/news/300040')]
    for test_case in test_cases:
        UDNEmbedIE()._real_extract(test_case)


# Generated at 2022-06-14 17:32:37.244515
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:32:38.563530
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()


# Generated at 2022-06-14 17:32:39.455060
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:32:40.280419
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:32:47.435659
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:32:50.814817
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    url = "//video.udn.com/embed/news/300040"
    match = ie._PROTOCOL_RELATIVE_VALID_URL
    # 'match' is a compiled regular expression object
    # expect the resulting 'm' to be the match for the video id
    m = re.match(match, url)
    video_id = m.group('id')
    # Test that the video_id is '300040'
    assert video_id == '300040'

# Generated at 2022-06-14 17:32:53.357039
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    input_url = "http://video.udn.com/embed/news/300040"
    ie = UDNEmbedIE()
    oc = ie.extract(input_url)
    print(oc)

# Generated at 2022-06-14 17:33:02.502834
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    extractor = UDNEmbedIE()
    result = extractor._real_extract('https://video.udn.com/embed/news/300040')
    assert result['id'] == '300040'
    assert result['title'] == '生物老師男變女 全校挺"做自己"'
    assert '//video.udn.com/v/r18/5e/9a/3_160422_hls_f0.m3u8' in [f['url'] for f in result['formats']]

# Generated at 2022-06-14 17:33:08.903397
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import unittest

    class _TestCase(unittest.TestCase):
        def test_make_smoke_test(self):
            url = "http://video.udn.com/embed/news/300040"
            video_id = "300040"

# Generated at 2022-06-14 17:35:32.506205
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    assert(UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL)


# Generated at 2022-06-14 17:35:39.362868
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['title'] == '生物老師男變女 全校挺"做自己"'
    assert ie._TESTS[0]['params']['skip_download'] == True

# Generated at 2022-06-14 17:35:47.985794
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert type(UDNEmbedIE.IE_DESC) is str
    assert isinstance(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL, str)
    assert isinstance(UDNEmbedIE._VALID_URL, str)
    assert type(UDNEmbedIE._TESTS) is list
    assert isinstance(UDNEmbedIE._TESTS[0]['url'], str)
    assert isinstance(UDNEmbedIE._TESTS[0]['info_dict'], dict)
    assert isinstance(UDNEmbedIE._TESTS[0]['info_dict']['ext'], str)
    assert isinstance(UDNEmbedIE._TESTS[0]['info_dict']['id'], str)

# Generated at 2022-06-14 17:35:58.617957
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Basic test case.
    """
    IE = UDNEmbedIE("http://video.udn.com/embed/news/300040")
    assert(IE._VALID_URL == "(?P<protocol>https?)://video\.udn\.com/(?P<type>embed|play)/news/(?P<id>[0-9]+)")
    assert(IE._TESTS[0]['url'] == "http://video.udn.com/embed/news/300040")
    assert(IE._TESTS[0]['info_dict']['id'] == "300040")

# Generated at 2022-06-14 17:36:04.484017
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import IncompleteVideoError
    from .dailymotion import DailymotionIE
    from .youtube import YoutubeIE

    inst = UDNEmbedIE()
    assert inst._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert inst._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert inst._TESTS[0]['only_matching'] == False
    assert inst._TESTS[0]['expected_warnings'] == ['Failed to parse JSON Expecting value']
    assert inst._TESTS[1]['url'] == 'https://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:36:06.630138
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie_UDNEmbed = UDNEmbedIE()
    # extract 'http://video.udn.com/embed/news/300040'
    ie_UDNEmbed._real_extract('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:36:09.400806
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'


# Generated at 2022-06-14 17:36:18.358506
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test the constructor
    ie = UDNEmbedIE()
    # test the video urls

# Generated at 2022-06-14 17:36:26.596385
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print('test_UDNEmbedIE()')
    ie = UDNEmbedIE(None)
    ie2 = UDNEmbedIE(None)
    for url in [
          'http://video.udn.com/embed/news/300040',
          'https://video.udn.com/embed/news/300040',
          'https://video.udn.com/play/news/303776',
          ]:
        #print(ie.suitable(url))
        #print(ie.IE_NAME)
        #print(ie.IE_DESC)
        m = ie.suitable(url)
        print(m is not None)
        assert(m is not None)
        assert(ie is ie2)
    return


# Generated at 2022-06-14 17:36:34.298468
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test UDNEmbedIE constructor with given URL"""
    try:
        UDNEmbedIE("http://video.udn.com/embed/news/300040")
        UDNEmbedIE("http://video.udn.com/play/news/300040")
        UDNEmbedIE("https://video.udn.com/embed/news/300040")
        UDNEmbedIE("https://video.udn.com/play/news/300040")
    except Exception as e:
        print("Test failed: {}".format(e))

if __name__ == "__main__":
    test_UDNEmbedIE()