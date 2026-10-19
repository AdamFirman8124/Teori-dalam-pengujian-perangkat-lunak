

# Generated at 2022-06-14 17:27:08.385650
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()(url)

# Generated at 2022-06-14 17:27:09.536794
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()


# Generated at 2022-06-14 17:27:10.945945
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    #test that the IE object has been initialized
    assert ie is not None


# Generated at 2022-06-14 17:27:19.978110
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test constructor of class UDNEmbedIE"""
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:21.023296
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 17:27:23.724833
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    UDNEmbedIE(url, "unit test for constructor of class UDNEmbedIE").download()

# Generated at 2022-06-14 17:27:28.022541
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Unit test for constructor of class UDNEmbedIE
    """
    the_class = UDNEmbedIE()

    assert(the_class._PROTOCOL_RELATIVE_VALID_URL == "//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)")

# Generated at 2022-06-14 17:27:35.526607
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_ie._VALID_URL == r'https?:' + udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL
    assert udn_embed_ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:27:43.878171
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    pattern = re.compile(r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    match = pattern.match('//video.udn.com/embed/news/300040')
    assert match.group('id') == '300040'
    assert match.group('id') != '300041'

    match = pattern.match('//video.udn.com/play/news/300040')
    assert match.group('id') == '300040'
    assert match.group('id') != '300041'

# Generated at 2022-06-14 17:27:53.468013
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, UDNEmbedIE)
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'


# Generated at 2022-06-14 17:28:17.085700
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:28:24.939003
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    i = UDNEmbedIE()
    assert i.IE_DESC == '聯合影音'
    assert i._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert i._VALID_URL == r'https?:' + i._PROTOCOL_RELATIVE_VALID_URL
    assert i.suitable(url) == True

# Generated at 2022-06-14 17:28:28.739405
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    a = UDNEmbedIE()
    print(a)

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:28:33.207965
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    

# Generated at 2022-06-14 17:28:36.674855
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_url = "http://video.udn.com/embed/news/300040"
    test_video_id = "300040"
    video_result = UDNEmbedIE()._real_extract(test_url)
    assert video_result['id'] == test_video_id
    assert video_result['formats'] != []

# Generated at 2022-06-14 17:28:38.240999
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None)

# Generated at 2022-06-14 17:28:49.782939
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    e = UDNEmbedIE()
    e._download_webpage = lambda *args, **kwargs: b''
    e._parse_json = lambda *args, **kwargs: {
        'video': {
            'm3u8': 'foo.m3u8',
            'mp4': 'foo.mp4',
            'f4m': 'foo.f4m',
            'youtube': 'https://www.youtube.com/watch?v=bar',
        },
        'title': 'title',
        'poster': 'poster.jpg',
    }

    # Test protocol-relative URLs
    UDN_RELATIVE_INPUT_URLS = ['//video.udn.com/embed/news/123', '//video.udn.com/play/news/123']


# Generated at 2022-06-14 17:28:55.326023
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(None)
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL


# Generated at 2022-06-14 17:28:57.013947
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert True

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:29:02.357505
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Go through the following steps:
    # 1. constructor of class InfoExtractor
    # 2. constructor of class UDNEmbedIE
    c = UDNEmbedIE()
    # test the following attributes are initialized
    print(c.IE_DESC)
    print(c._VALID_URL)
    print(c._PROTOCOL_RELATIVE_VALID_URL)
    print(c._TESTS)

if __name__ == "__main__":
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:29:17.385331
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	ud = UDNEmbedIE('http://video.udn.com/embed/news/300040')
	print(ud)

# Generated at 2022-06-14 17:29:27.420164
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    IE_DESC = '聯合影音'
    _PROTOCOL_RELATIVE_VALID_URL = r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    _VALID_URL = r'https?:' + _PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:29:34.475255
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE("https://video.udn.com/embed/news/300040")
    assert ie != None
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == "https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)"

# Generated at 2022-06-14 17:29:39.431431
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnei = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert udnei._match_id(udnei._VALID_URL) == '300040'
    assert udnei._match_id(udnei._PROTOCOL_RELATIVE_VALID_URL) == '300040'

# Generated at 2022-06-14 17:29:43.123986
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE = _make_IE('UDNEmbedIE')
    assert UDNEmbedIE is not None



# Generated at 2022-06-14 17:29:44.090403
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test constructor"""
    UDNEmbedIE()

# Generated at 2022-06-14 17:29:46.646748
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE(None)._real_extract(test_url)

# Generated at 2022-06-14 17:29:57.727316
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_data = UDNEmbedIE()._TESTS
    test_data_instance = test_data[0]

    assert test_data_instance['url'] == "http://video.udn.com/embed/news/300040"
    assert test_data_instance['info_dict']['id'] == "300040"
    assert test_data_instance['info_dict']['ext'] == "mp4"
    assert test_data_instance['info_dict']['title'] == "生物老師男變女 全校挺\"做自己\""
    assert test_data_instance['expected_warnings'][0] == "Failed to parse JSON Expecting value"

# Generated at 2022-06-14 17:29:58.667943
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()

# Generated at 2022-06-14 17:30:02.864076
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_extractor = UDNEmbedIE()
    assert udn_extractor.ie_key() == 'udn'
    assert udn_extractor._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:34.037110
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_ie = UDNEmbedIE()
    assert udn_ie.IE_NAME == 'udn'
    assert udn_ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:30:35.176677
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:30:40.285818
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('https://video.udn.com/embed/news/300040')
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:30:51.547238
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:30:55.634439
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    # must return _VALID_URL
    assert ie._VALID_URL == ie.IE_DESC



# Generated at 2022-06-14 17:31:06.087605
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:31:09.481316
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(None)
    obj = ie.suitable('https://video.udn.com/embed/news/300040')
    assert obj is not None, "constructor test fail"
    obj = UDNEmbedIE(None).suitable('https://video.udn.com/news/300040')
    assert obj is None, "url validation fail"

# Generated at 2022-06-14 17:31:13.535190
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = UDNEmbedIE._VALID_URL
    ie = UDNEmbedIE(url)
    assert ie.IE_NAME == 'udn'
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == UDNEmbedIE.IE_DESC

# Generated at 2022-06-14 17:31:16.110194
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url_test_main(UDNEmbedIE, 'taiwan', ['http://video.udn.com/embed/news/300040'])

# Generated at 2022-06-14 17:31:27.200062
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    def create_url(video_id):
        return 'http://video.udn.com/embed/news/%s' % (video_id)

    ie = UDNEmbedIE()
    for video_id in ['300040', '303776']:
        url = create_url(video_id)
        result = ie.suitable(url)
        assert result

    video_id = '300040'
    url = create_url(video_id)
    result = ie.extract(url)
    assert(result['id'] == video_id)
    assert(result['title'] == '生物老師男變女 全校挺"做自己"')
    assert(result['thumbnail'])

# Generated at 2022-06-14 17:32:34.922769
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert udne.IE_DESC == '聯合影音'
    assert udne._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udne._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udne._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert udne._TESTS[0]['info_dict']['id'] == '300040'

# Generated at 2022-06-14 17:32:36.888806
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(None)
    assert ie._PROTOCOL_RELATIVE_VALID_URL == ie._VALID_URL[5:]

# Generated at 2022-06-14 17:32:47.981253
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    # Test embed URL
    embed_url = 'http://video.udn.com/embed/news/300040'
    embed_id = udn_embed_ie._match_id(embed_url)
    assert embed_id == '300040'
    # Test non-embed URL
    non_embed_url = 'https://video.udn.com/play/news/300040'
    assert udn_embed_ie._match_id(non_embed_url) == None
    # Test get protocol-relative URL
    protocol_relative_url = '//video.udn.com/play/news/300040'
    assert udn_embed_ie._match_id(protocol_relative_url) == '300040'
    # Test prefix URL
    prefix_

# Generated at 2022-06-14 17:32:51.883669
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    result = UDNEmbedIE()._real_extract(url)
    assert(result['id'] == '300040')
    assert(result['title'] != None)

# Generated at 2022-06-14 17:32:54.025927
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie._TESTS[1]['only_matching'] == True

# Generated at 2022-06-14 17:33:01.382745
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udneie = UDNEmbedIE()
    assert udneie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udneie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:33:10.572480
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.IE_NAME == 'udn'  # initialization of instance variable IE_NAME
    assert udn_embed_ie.IE_DESC == '聯合影音'  # initialization of instance variable IE_DESC
    assert udn_embed_ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'  # initialization of instance variable _VALID_URL

# Generated at 2022-06-14 17:33:21.050981
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from youtube_dl.YoutubeDL import YoutubeDL
    # Constructor of class InfoExtractor is private, it will be called in class YoutubeDL
    ydl = YoutubeDL({'forcejson': True})
    info_extractor = ydl._ies['udn']
    assert isinstance(info_extractor, UDNEmbedIE)
    # Test whether the regex in '_VALID_URL' of this InfoExtractor works.
    assert info_extractor._match_id('https://video.udn.com/embed/news/123456') == '123456'
    assert info_extractor._match_id('http://video.udn.com/embed/news/123456') == '123456'
    assert info_extractor._match_id('//video.udn.com/embed/news/123456') == '123456'

# Generated at 2022-06-14 17:33:25.109542
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    for test in UDNEmbedIE._TESTS:
        test_url = test.get('url')
        assert udn_embed_ie.suitable(test_url), 'Incorrectly reports as unsuitable'

# Generated at 2022-06-14 17:33:37.042202
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    instance = UDNEmbedIE()
    # Constructor of UDNEmbedIE class
    assert instance.ASSOCIATED_IE == []
    assert instance.IE_DESC == '聯合影音'
    assert instance._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert instance._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:36:09.284390
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:36:10.406973
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:36:16.116071
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
  # Initialize UDNEmbedIE
  udn = UDNEmbedIE()
  # Test a cache file, get name of cache file
  cache_name = udn.extract('test-url')['id']
  # Test cache file, if exist
  assert os.path.exists(udn.ydl.cache.cache_fn(cache_name)) == True

if __name__ == '__main__':
  test_UDNEmbedIE()

# Generated at 2022-06-14 17:36:23.205349
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    info_extractor = UDNEmbedIE()
    assert_equals(info_extractor.IE_NAME, 'UDNEmbed')
    assert_equals(info_extractor.IE_DESC, '聯合影音')
    assert_equals(info_extractor._VALID_URL, 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

# Generated at 2022-06-14 17:36:28.900107
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    dummy_url = "https://video.udn.com/embed/news/300040"
    ie = UDNEmbedIE()
    assert ie._match_id(dummy_url) == '300040'
    assert ie._extract_urls(dummy_url) == [dummy_url]

# Generated at 2022-06-14 17:36:31.533863
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert(udne._PROTOCOL_RELATIVE_VALID_URL ==
           r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

# Generated at 2022-06-14 17:36:37.760405
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test URL '//video.udn.com/embed/news/300040'
    ie = UDNEmbedIE('//video.udn.com/embed/news/300040')
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'

    # Test URL '//video.udn.com/play/news/300040'
    ie = UDNEmbedIE('//video.udn.com/play/news/300040')
    assert ie._match_id('https://video.udn.com/play/news/300040') == '300040'

# Generated at 2022-06-14 17:36:44.796549
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == 'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert len(ie._TESTS) == 3


# Generated at 2022-06-14 17:36:46.613830
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:36:49.918496
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    video_id = '300040'
    url = 'http://video.udn.com/embed/news/' + video_id
    ie = UDNEmbedIE().working_youtube_ie
    # Returns the YoutubeIE object
    assert isinstance(ie, InfoExtractor)
    # Returns the video_id.
    assert ie._match_id(url) == video_id