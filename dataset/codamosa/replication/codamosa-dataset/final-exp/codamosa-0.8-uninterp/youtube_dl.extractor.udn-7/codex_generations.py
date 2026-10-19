

# Generated at 2022-06-14 17:27:11.619543
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # verify that the test case works well
    UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL.match('//video.udn.com/embed/news/300040')
    UDNEmbedIE._VALID_URL.match('https://video.udn.com/embed/news/300040')



# Generated at 2022-06-14 17:27:18.182785
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    IE_DESC = '聯合影音'
    _VALID_URL = 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:27:20.663718
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None, None).extract('https://video.udn.com/play/news/303776')

# Generated at 2022-06-14 17:27:22.621591
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    print(udn_embed_ie.IE_NAME)

# Generated at 2022-06-14 17:27:24.523526
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE() is not None


# Generated at 2022-06-14 17:27:25.621296
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None, None)

# Generated at 2022-06-14 17:27:27.780212
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    _UDNEmbedIE = UDNEmbedIE()
    assert isinstance(_UDNEmbedIE, InfoExtractor)


# Generated at 2022-06-14 17:27:30.880325
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnEmbedIE = UDNEmbedIE()

    assert udnEmbedIE._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'




# Generated at 2022-06-14 17:27:36.991363
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_class = UDNEmbedIE()
    assert hasattr(test_class, '_PROTOCOL_RELATIVE_VALID_URL')
    assert hasattr(test_class, '_VALID_URL')
    assert hasattr(test_class, '_TESTS')
    assert hasattr(test_class, 'IE_DESC')
    assert hasattr(test_class, '_real_extract')

# Generated at 2022-06-14 17:27:39.854037
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    obj._match_id('')
    obj._match_id('')
    obj._real_extract('')


# Generated at 2022-06-14 17:28:03.089210
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    e = UDNEmbedIE()
    assert e.IE_DESC == '聯合影音'
    assert e._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert e._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert e._TESTS[0]['info_dict']['id'] == '300040'
    assert e._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:28:05.597266
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Just create a instance of UDNEmbedIE class,
    then it will be tested automatically
    """
    ie = UDNEmbedIE()

# Generated at 2022-06-14 17:28:12.228846
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:28:22.141263
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    print('Url: ' + url)
    print('Downloading webpage')
    webpage = (ie._download_webpage(url, '300040')).decode('utf-8')
    print('Parsing webpage')
    options_str_1 = ie._html_search_regex(r'var\s+options\s*=\s*(.+);', webpage, 'options')
    options_str_2 = options_str_1.strip()
    options_json = ie._parse_json(ie._replace(options_str_2), 'options')
    print('options_json:')
    print(options_json)

# Generated at 2022-06-14 17:28:24.612731
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    ie.extract('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:28:26.087429
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:28:31.908584
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import json
    IE = UDNEmbedIE(None, {})

# Generated at 2022-06-14 17:28:36.938978
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == "//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)"
    assert UDNEmbedIE._VALID_URL == "https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)"
    assert UDNEmbedIE.IE_DESC == "聯合影音"

# Generated at 2022-06-14 17:28:48.800219
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == 'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:28:51.738918
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    pattern = re.compile(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL)

    # test no raise
    UDNEmbedIE(None, pattern, None)


# Generated at 2022-06-14 17:29:12.657619
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert hasattr(ie, '_WORKING')
    assert ie._WORKING == True
    assert hasattr(ie, '_downloader')
    assert hasattr(ie, '_download_webpage')
    assert hasattr(ie, '_html_search_regex')
    assert hasattr(ie, 'IE_NAME')
    assert ie.IE_NAME == 'udn'


# Generated at 2022-06-14 17:29:17.429413
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == UDNEmbedIE._VALID_URL
    assert ie._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:29:18.326999
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:29:27.497644
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test for valid url
    ie = UDNEmbedIE()
    url = 'http://video.udn.com/embed/news/300040'
    assert ie._match_id(url) == '300040'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert ie.IE_NAME == 'udn'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'


# Test for method _real_extract of class UDNEmbedIE

# Generated at 2022-06-14 17:29:29.241110
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    # print(udn)


# Generated at 2022-06-14 17:29:40.766687
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(UDNEmbedIE._create_get_info())
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:29:47.028488
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    x = UDNEmbedIE()
    assert x._VALID_URL == x.ie_key() # test that ie_key() matches the IE_KEY
    x._PROTOCOL_RELATIVE_VALID_URL = x._VALID_URL
    y = UDNEmbedIE()
    assert y._VALID_URL == y._PROTOCOL_RELATIVE_VALID_URL
    assert x is not y

# Generated at 2022-06-14 17:29:53.019865
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    o = UDNEmbedIE()
    assert o._PROTOCOL_RELATIVE_VALID_URL.find('PROTOCOL_RELATIVE_VALID_URL') > 0
    assert o._VALID_URL.find('PROTOCOL_RELATIVE_VALID_URL') > 0

# Generated at 2022-06-14 17:30:04.986551
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert(ie._VALID_URL == UDNEmbedIE._VALID_URL)

# class UDNEmbedIE(InfoExtractor):
#     _VALID_URL = r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
#     _TEST = {
#         'url': 'http://video.udn.com/embed/news/300040',
#         'md5': '9bba9b2f4d4c4b8f8b794e0f21d72e54',
#         'info_dict': {
#             'id': '300040',
#             'ext': 'mp4',
#             'title': '生物老師男變女

# Generated at 2022-06-14 17:30:06.355582
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Unit test for constructor of class UDNEmbedIE
    """
    UDNEmbedIE('',{})

# Generated at 2022-06-14 17:30:37.958339
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    result = UDNEmbedIE()._real_extract('http://video.udn.com/embed/news/300040')
    assert(result['id'] == '300040')

# Generated at 2022-06-14 17:30:43.529686
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Arrange
    url = 'https://video.udn.com/embed/news/300040'
    # Act
    UDNEmbedIE.__name__ = 'UnrealPlayer86'
    ie = UDNEmbedIE(url)
    # Assert
    assert ie.url == url
    assert ie.video_id == '300040'

# Generated at 2022-06-14 17:30:50.915530
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbed = UDNEmbedIE(None)
    input_string = r'http://video.udn.com/embed/news/300040'
    assert UDNEmbed._match_id(input_string) == '300040'
    assert UDNEmbed._match_id(input_string, _VALID_URL) == '300040'
    assert UDNEmbed._match_id(input_string, _PROTOCOL_RELATIVE_VALID_URL) == '300040'

# Generated at 2022-06-14 17:30:52.874156
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """test class constructor"""
    UDNEmbedIE(None, None)

# Generated at 2022-06-14 17:31:03.882905
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:31:07.905928
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test URL with the protocol of http
	url = 'http://video.udn.com/embed/news/300040'
	ie = UDNEmbedIE()
	# Test URL with the protocol of https [FAIL]
	url = 'https://video.udn.com/embed/news/300040'
	ie = UDNEmbedIE()

# Generated at 2022-06-14 17:31:16.880078
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert(ie.IE_NAME == 'udn.com')
    assert(ie.IE_DESC == '聯合影音')
    assert(ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)')

# Generated at 2022-06-14 17:31:28.008838
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne_ie = UDNEmbedIE()
    assert udne_ie.IE_DESC == '聯合影音'
    assert udne_ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udne_ie._VALID_URL == r'https?:' + udne_ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:31:29.927040
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:31:35.710239
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE(
        '__main__'
    )._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE(
        '__main__'
    )._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'



# Generated at 2022-06-14 17:32:50.766294
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    x = UDNEmbedIE()
    assert x.IE_NAME == 'udn'
    assert x.IE_DESC == '聯合影音'
    assert x._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert x._VALID_URL == r'https?:' + x._PROTOCOL_RELATIVE_VALID_URL


# Generated at 2022-06-14 17:32:57.761791
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:33:00.802306
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE("http://video.udn.com/embed/news/300040")
    assert obj.IE_NAME == 'udn'
    assert obj._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert obj._TESTS


# Generated at 2022-06-14 17:33:02.374032
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(None)
    assert ie.get_info_extractors()

# Generated at 2022-06-14 17:33:04.599979
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:33:06.780092
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        UDNEmbedIE('UDNEmbedIE')
    except AttributeError:
        return(False)
    return(True)

# Generated at 2022-06-14 17:33:08.514878
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE(url)

# Generated at 2022-06-14 17:33:14.608955
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    info_extractor = UDNEmbedIE('youtube')

    assert info_extractor.IE_DESC == '聯合影音'
    assert info_extractor._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert info_extractor._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:33:25.422923
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print('test_UDNEmbedIE(): begin')
    # Test case 1
    info_extractor = UDNEmbedIE()
    video_id = '300040'
    url_prefix = 'http://video.udn.com/embed/news/'
    url = url_prefix + video_id
    assert info_extractor._real_extract(url)

    # Test case 2
    info_extractor = UDNEmbedIE()
    video_id = '300040'
    url_prefix = 'http://video.udn.com/play/news/'
    url = url_prefix + video_id
    assert info_extractor._real_extract(url)

    print('test_UDNEmbedIE(): end')
    return

# test_UDNEmbedIE()

# Generated at 2022-06-14 17:33:33.426282
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # case: valid URL
    valid_url = 'http://video.udn.com/embed/news/300040'
    assert ie._check_valid_url(valid_url)
    assert ie._match_id(valid_url) == '300040'
    invalid_url = 'https://www.udn.com'
    assert not ie._check_valid_url(invalid_url)

# Generated at 2022-06-14 17:36:02.699032
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()


# Generated at 2022-06-14 17:36:06.151037
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:36:11.352360
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_class = UDNEmbedIE()
    assert test_class.ie_key() == 'udn_embed'
    assert test_class.ie_desc() == '聯合影音'
    assert re.match(test_class._VALID_URL, 'https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:36:14.830819
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Test the constructor of class UDNEmbedIE
    """
    i=UDNEmbedIE()
    assert(i.IE_DESC == '聯合影音')


# Generated at 2022-06-14 17:36:18.768208
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # instantiate a YoutubeIE
    UDNEmbedIE()



# Generated at 2022-06-14 17:36:29.313510
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test from https://video.udn.com/news/300040
    udn_embed_ie = UDNEmbedIE(url='http://video.udn.com/embed/news/300040')
    udn_embed_ie.IE_DESC = '聯合影音'
    udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL = r'//video\.udn\.com/embed/news/(?P<id>\d+)'
    udn_embed_ie._VALID_URL = r'https?:' + udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:36:37.638897
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:36:47.143697
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Good URL
    url = 'https://video.udn.com/embed/news/300040'
    UDNEmbedInstance = UDNEmbedIE(url)
    # Good URL but to a video
    url = 'https://video.udn.com/play/news/303776'
    UDNEmbedInstance = UDNEmbedIE(url)
    # Good partial URL
    url = '//video.udn.com/play/news/303776'
    UDNEmbedInstance = UDNEmbedIE(url)
    # Bad URL
    url = 'https://www.udn.com/news/story/6656/3513958'
    try:
        UDNEmbedInstance = UDNEmbedIE(url)
    except ValueError:
        pass

# Generated at 2022-06-14 17:36:48.654628
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(UDNEmbedIE.IE_NAME, UDNEmbedIE.IE_DESC)

# Generated at 2022-06-14 17:36:55.514982
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    urls = [
        'http://video.udn.com/embed/news/300040',
        'https://video.udn.com/play/news/303776',
    ]
    for url in urls:
        udne._match_id(url)
        udne._real_extract(url)

if __name__ == '__main__':
    test_UDNEmbedIE()