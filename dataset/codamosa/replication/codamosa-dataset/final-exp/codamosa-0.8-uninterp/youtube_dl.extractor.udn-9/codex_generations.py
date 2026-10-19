

# Generated at 2022-06-14 17:27:10.055220
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # pylint: disable=protected-access
    # pylint: disable=no-member
    udn_embed = UDNEmbedIE()._downloader.udn_embed

    # Test valid scenario
    url = 'http://video.udn.com/embed/news/300040'
    url_match = udn_embed._VALID_URL.match(url)
    assert url_match is not None
    video_id = udn_embed._match_id(url)
    assert video_id == '300040'
    info_dict = udn_embed._real_extract(url)
    assert info_dict is not None
    assert info_dict.get('id') == video_id
    # Test invalid scenario
    url = 'http://video.udn.com/play/news/300041'
   

# Generated at 2022-06-14 17:27:14.358611
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_input = 'https://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    assert ie._match_id(test_input) == '300040'
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TESTS == ie.TESTS

# Generated at 2022-06-14 17:27:16.248645
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    u = UDNEmbedIE()
    assert u.ie_key() == 'UDNEmbed'
    assert u.ie_desc() == '聯合影音'

# Generated at 2022-06-14 17:27:23.802071
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    # _VALID_URL
    match = re.match(udn_embed_ie._VALID_URL, '//video.udn.com/embed/news/300040')
    assert match
    assert match.group('id') == '300040'
    match = re.match(udn_embed_ie._VALID_URL, '//video.udn.com/play/news/300040')
    assert match
    assert match.group('id') == '300040'

# Generated at 2022-06-14 17:27:29.247325
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040','300040','mp4','生物老師男變女 全校挺"做自己"','https://video.udn.com/vod/3000/281/3000/300040.mp4/300040_1000k.mp4')
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/300040') == '300040'
    assert ie._download_webpage('http://video.udn.com/embed/news/300040', '300040')

# Generated at 2022-06-14 17:27:33.149365
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    data = UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL
    assert data == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:38.312634
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(UDNEmbedIE.IE_NAME, UDNEmbedIE.IE_DESC)
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.ie_desc() == '聯合影音'

# Generated at 2022-06-14 17:27:40.332286
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert(isinstance(ie, UDNEmbedIE))


# Generated at 2022-06-14 17:27:44.999714
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    video_embed_ie = UDNEmbedIE()
    video_embed_ie._real_extract('http://video.udn.com/embed/news/300040')
    video_embed_ie._real_extract('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:27:47.840143
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'udn'
    assert ie.ie_desc() == '聯合影音'

# Generated at 2022-06-14 17:28:12.368647
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	assert UDNEmbedIE(None, None)._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
	assert UDNEmbedIE(None, None)._VALID_URL == r'https?:' + UDNEmbedIE(None, None)._PROTOCOL_RELATIVE_VALID_URL
	assert UDNEmbedIE(None, None).IE_DESC == '聯合影音'
	assert UDNEmbedIE(None, None)._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:28:22.242623
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import sys
    import os
    import unittest
    module_name = os.path.basename(os.path.splitext(sys.argv[0])[0])
    output_dir = os.getenv('YOUTUBE_DL_JS_TEST_OUTPUT_DIR')

    if not output_dir:
        print('Must set YOUTUBE_DL_JS_TEST_OUTPUT_DIR environment variable')
        sys.exit(1)

    class TestYoutubeDl(unittest.TestCase):
        def test_ie(self):
            ie = UDNEmbedIE()
            for test in ie._TESTS:
                print('Testing URL: ' + test['url'])
                res = ie.extract(test['url'])

# Generated at 2022-06-14 17:28:26.707044
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    obj.extract('http://video.udn.com/embed/news/300040')
    obj.extract('https://video.udn.com/embed/news/300040')
    obj.extract('https://video.udn.com/play/news/303776')

# Generated at 2022-06-14 17:28:27.953623
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:28:37.256694
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test a valid url.
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE(url)

    # Test a url with an invalid scheme.
    url = 'ftp://video.udn.com/embed/news/300040'
    try:
        UDNEmbedIE(url)
    except:
        pass
    else:
        raise Exception('Expect to raise an exception for a url with an invalid scheme!')

    # Test a url with an invalid netloc.
    url = 'http://vide0.udn.com/embed/news/300040'
    try:
        UDNEmbedIE(url)
    except:
        pass
    else:
        raise Exception('Expect to raise an exception for a url with an invalid netloc!')

# Generated at 2022-06-14 17:28:44.992230
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert udn.IE_NAME == 'UDNEmbed'
    assert udn.IE_DESC == '聯合影音'
    assert udn._VALID_URL == udn.VALID_URL
    assert udn.IE_DESC == '聯合影音'
    assert udn._TESTS == udn.TESTS

# Generated at 2022-06-14 17:28:52.291300
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url_valid = 'http://video.udn.com/embed/news/300040'
    url_invalid = 'http://video.udn.com/news/300040'

    extractor_valid = UDNEmbedIE()
    extractor_invalid = UDNEmbedIE()

    extractor_valid.suitable(url_valid)
    extractor_invalid.suitable(url_invalid)

    extractor_valid.extract(url_valid)
    extractor_invalid.extract(url_invalid)

# Generated at 2022-06-14 17:28:58.143582
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    assert obj.ie_key() == 'UDNEmbed'
    assert obj.IE_NAME == 'UDNEmbed'
    assert obj.IE_DESC == '聯合影音'
    assert obj._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert obj._VALID_URL == 'https?:' + obj._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:29:09.380818
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS
    assert ie._real_extract('http://video.udn.com/embed/news/300040')
    assert ie._real_extract('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:29:10.487052
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:29:36.252599
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print(UDNEmbedIE()._download_webpage)



# Generated at 2022-06-14 17:29:43.226374
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    v = UDNEmbedIE()
    assert v.IE_NAME == 'udn'
    assert v.IE_DESC == '聯合影音'
    assert v._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert v._TESTS

# Generated at 2022-06-14 17:29:48.076425
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie_UDN = UDNEmbedIE()
    url = 'http://video.udn.com/embed/news/300040'
    assert ie_UDN.ie_key() == 'UDNEmbed'
    assert ie_UDN.suitable(url)
    assert ie_UDN.working()
    assert ie_UDN._VALID_URL == ie_UDN._TESTS[0]['url']

# Generated at 2022-06-14 17:29:50.123733
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:29:51.259980
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:29:55.050569
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('https://video.udn.com/embed/news/300040')
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.ie_desc() == '聯合影音'

# Generated at 2022-06-14 17:30:00.207602
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    obj = UDNEmbedIE()
    a = obj._real_extract(url)
    assert a['id'] == '300040'
    assert len(a['formats']) == 4

# Generated at 2022-06-14 17:30:03.403062
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import sys
    url = 'https://video.udn.com/play/news/303776'
    ie = sys.modules['youtube_dl.extractor.udn'].UDNEmbedIE(url)
    assert ie

# Generated at 2022-06-14 17:30:04.570790
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:30:12.478548
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    obj = ie._real_extract('http://video.udn.com/embed/news/300040')
    assert obj['id'] == '300040'
    assert obj['title'] == '生物老師男變女 全校挺"做自己"'
    assert len(obj['formats']) == 2
    assert obj['formats'][0]['url'] == 'http://videocdn.q3.udn.com.tw/vod/_definst_/mp4:news/300040/300040_500k_14.mp4/playlist.m3u8'
    assert obj['formats'][1]['height'] == 720
    assert obj['formats'][1]['tbr']

# Generated at 2022-06-14 17:31:10.595450
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.IE_DESC == '聯合影音'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:31:14.544556
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed = UDNEmbedIE()
    # Returns metadata of given url
    url = 'https://video.udn.com/embed/news/300040'
    info = udn_embed.extract(url)
    print(info)
    
# Unit test (need the url to be modified)
# test_UDNEmbedIE()

# Generated at 2022-06-14 17:31:17.063337
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._match_id(url)

# Generated at 2022-06-14 17:31:26.554498
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import ExtractorError
    from ..utils import clean_html

    invalid_tests = [
        # None is passed as the first argument
        (None, None),
        # invalid URL
        ('//video.udn.com/embed/news/abc', None),
        # invalid video ID
        ('//video.udn.com/embed/news/', None),
    ]

    for url, video_id in invalid_tests:
        ie = UDNEmbedIE(url)
        try:
            ie.extract()
        except ExtractorError:
            pass
        else:
            assert False, 'Invalid URL should raise ExtractorError'

# Generated at 2022-06-14 17:31:36.828727
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    '''
    Constructor of class UDNEmbedIE
    '''
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._real_initialize()
    i = UDNEmbedIE()
    ret = i._real_extract(url)

# Generated at 2022-06-14 17:31:48.589044
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print("Test the class UDNEmbedIE")
    # Test class constructor
    print("Test class constructor")
    print("Object UDNEmbedIE initialize")
    udn_embed_ie = UDNEmbedIE()
    print("Finish testing class constructor")
    # Test class real_extract
    print("Test class real_extract")
    print("Object UDNEmbedIE initialize")
    udn_embed_ie = UDNEmbedIE()
    print("Test url")
    url = "http://video.udn.com/embed/news/300040"
    udn_embed_ie.url_result(url, 'UDNEmbedIE')
    print("Finish testing class real_extract")


# Generated at 2022-06-14 17:31:50.438040
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('https://video.udn.com/play/news/303776')

# Generated at 2022-06-14 17:32:02.891089
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    testClass = UDNEmbedIE()
    print(testClass._match_id(url))
    print(testClass._real_extract("https://video.udn.com/embed/news/300040"))
    print(testClass._PROTOCOL_RELATIVE_VALID_URL)
    print(testClass._VALID_URL)
    print(testClass.IE_DESC)
    print(testClass._extract_f4m_formats.__doc__)
    print(testClass._extract_m3u8_formats.__doc__)
    print(testClass._download_webpage(url, "udn.com"))
    print(testClass._search_regex("", ""))

# Generated at 2022-06-14 17:32:07.401372
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE("http://video.udn.com/embed/news/300040")
    assert ie.ie_key() == 'UDNEmbed'

# Generated at 2022-06-14 17:32:16.656717
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:34:32.653814
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    instance = UDNEmbedIE()
    assert 'UDNEmbedIE' == instance.IE_NAME
    assert '聯合影音' == instance.IE_DESC
    assert instance._VALID_URL == 'http[s]?:(//video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+))'
    assert instance._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:34:40.955943
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_cases = (
        {
            # From https://video.udn.com/news/303776
            'url': 'https://video.udn.com/play/news/303776',
            'only_matching': True,
        },
    )
    for test_case in test_cases:
        ie = UDNEmbedIE()
        assert ie.suitable(test_case['url'])
        # Test url_result
        url_result = ie.url_result(test_case['url'])
        assert url_result['ie_key'] == 'UDNEmbed'
        assert url_result['url'] == test_case['url']
        # Test _real_extract
        res = ie._real_extract(test_case['url'])
        assert res == test_case

# Generated at 2022-06-14 17:34:53.596654
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnIE = UDNEmbedIE({})
    import os
    os.getcwd()

# Generated at 2022-06-14 17:35:04.880726
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE()._VALID_URL == r'https?:' + UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE().IE_DESC == '聯合影音'
    assert UDNEmbedIE()._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:35:17.515722
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	# Test for class constructor
	ie = UDNEmbedIE()
	assert ie.ie_key() == 'UDNEmbed', 'ie_key() should return UDNEmbed here'
	assert ie.ie_desc() == '聯合影音', 'ie_desc() should return 聯合影音 here'
	assert re.match(ie._VALID_URL, 'http://video.udn.com/embed/news/300040'), 'URL regexp validation should pass here'
	assert not re.match(ie._VALID_URL, 'http://video.udn.com/embed/news/300040/'), 'URL regexp validation should pass here'

# Generated at 2022-06-14 17:35:22.635086
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert udn._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:35:24.520174
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    ie = UDNEmbedIE(url)
    # assert here

# Generated at 2022-06-14 17:35:29.088974
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert udn.IE_NAME == 'UDNEmbed'
    assert udn.IE_DESC == '聯合影音'
    assert udn._VALID_URL.startswith('http')
    # 'https:video.udn.com/play/news/303776' is a valid url for UDNEmbedIE
    assert udn._PROTOCOL_RELATIVE_VALID_URL.startswith('//')

# Generated at 2022-06-14 17:35:31.937964
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'

    UDNEmbedIE(UDNEmbedIE.ie_key())._real_extract(url)

# Generated at 2022-06-14 17:35:34.676638
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    myclass = UDNEmbedIE()
    myclass.add_ie(UDNEmbedIE.ie_key())
    assert list(myclass._ies) == [UDNEmbedIE]