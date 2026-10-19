

# Generated at 2022-06-14 17:27:10.109036
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():  
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    UDNEmbedIE.suitable(ydl, 'https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:27:14.121325
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert(ie._VALID_URL == UDNEmbedIE._VALID_URL)
    assert(ie._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL)


# Generated at 2022-06-14 17:27:16.315167
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()


# Generated at 2022-06-14 17:27:22.703073
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    obj = UDNEmbedIE()
    assert obj.IE_NAME == 'udn'
    assert obj.IE_DESC == '聯合影音'
    assert re.match(obj._PROTOCOL_RELATIVE_VALID_URL, url)
    assert not re.match(obj._VALID_URL, url)

# Generated at 2022-06-14 17:27:26.575506
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test for URL without "http" or "https"
    UDNEmbedIE()._real_initialize(
        compat_urlparse.urlparse('//video.udn.com/embed/news/300040'))

# Generated at 2022-06-14 17:27:29.881558
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    i = UDNEmbedIE()
    assert i._TESTS[0]['url'] == i._TESTS[0]['info_dict']['id']

# Generated at 2022-06-14 17:27:41.834741
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    _url = "https://video.udn.com/embed/news/300040"
    _url_protocol_relative = "//video.udn.com/embed/news/300040"
    _video_id = "300040"
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie._match_id(_url) == _video_id
    assert ie._match_id(_url_protocol_relative) == _video_id

# Generated at 2022-06-14 17:27:50.011336
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    valid_url = "https://video.udn.com/embed/news/300040"
    invalid_url = "https://video.udn.com/embed/news/"
    url = "https://video.udn.com/embed/news/"
    url = url + str(3 + 4)
    print(url)
    udnei = UDNEmbedIE()
    assert udnei.suitable(url)
    assert not udnei.suitable(invalid_url)
    assert udnei.suitable(valid_url)


if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:27:55.613931
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(downloader=None)
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:28:05.054964
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:28:13.739322
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test the constructor"""
    # Test with a single parameter
    IE = UDNEmbedIE(None)
    assert(IE.IE_DESC == '聯合影音')


# Generated at 2022-06-14 17:28:18.038609
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # using url from https://video.udn.com/news/302489
    url = 'https://video.udn.com/embed/news/302489'
    client = UDNEmbedIE()
    assert client._match_id(url) == '302489'

# Generated at 2022-06-14 17:28:23.531081
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'


# Generated at 2022-06-14 17:28:26.892994
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	try:
		temp = UDNEmbedIE()
	except:
		print("Unit test for constructor of class UDNEmbedIE failed")
		return
	print("Unit test for constructor of class UDNEmbedIE passed")

test_UDNEmbedIE()

# Generated at 2022-06-14 17:28:34.102833
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    inst = UDNEmbedIE()
    assert inst.IE_DESC == '聯合影音'
    assert inst._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert inst._VALID_URL == 'https?:' + inst._PROTOCOL_RELATIVE_VALID_URL
    assert len(inst._TESTS) == 3


# Generated at 2022-06-14 17:28:39.539425
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print('test_UDNEmbedIE')
    test_class = UDNEmbedIE()
    print('test_UDNEmbedIE: test_class = ', test_class)
    assert test_class


# Generated at 2022-06-14 17:28:43.008691
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:45.512419
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE().IE_NAME == 'video.udn'

# Generated at 2022-06-14 17:28:55.888765
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UdnEmbedIE()

# Generated at 2022-06-14 17:28:59.806758
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    ie.constructor(UDNEmbedIE.get_info_extractor(UDNEmbedIE._VALID_URL))
    ie.constructor(UDNEmbedIE.get_info_extractor(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL))
    return True

# Generated at 2022-06-14 17:29:21.302305
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    m = r'^https?:\/\/video\.udn\.com\/play\/news\/\d+$'
    assert udn_embed_ie._VALID_URL == m, '_VALID_URL should be %s' % m
    m = r'^https?:\/\/video\.udn\.com\/embed\/news\/\d+$'
    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == m, '_PROTOCOL_RELATIVE_VALID_URL should be %s' % m
    assert udn_embed_ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040', '_TESTS should have the right element.'
    assert udn

# Generated at 2022-06-14 17:29:27.252486
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # When the url is None, an exception should be raised
    try:
        info_extractor = UDNEmbedIE(None)
        assert False
    except TypeError:
        assert True

    # When the url is not a valid one, an exception should be raised
    try:
        info_extractor = UDNEmbedIE('not-a-valid-url')
        info_extractor._real_extract(None)
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-14 17:29:33.888244
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:29:42.376491
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:29:49.586341
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    m = ie._PROTOCOL_RELATIVE_VALID_URL
    assert m.match(r'//video\.udn\.com/embed/news/300040')
    assert m.match(r'//video\.udn\.com/play/news/300040')
    ie = UDNEmbedIE(UDNEmbedIE.ie_key())
    ie.extract('http://video.udn.com/embed/news/300040')
    ie.extract('https://video.udn.com/embed/news/300040')
    ie.extract('https://video.udn.com/play/news/300040')
    ie.extract('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:29:50.276824
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    pass

# Generated at 2022-06-14 17:29:53.017686
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    print(ie._PROTOCOL_RELATIVE_VALID_URL)
    print(ie._VALID_URL)


# Generated at 2022-06-14 17:29:55.143626
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._real_extract(url)

# Generated at 2022-06-14 17:30:06.069662
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Unit test for constructor of class UDNEmbedIE"""
    ie = UDNEmbedIE()
    # The middle one should be correct, the later two are all examples of wrong input
    input_urls = [
        'http://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/news/300040',
        'https://video.udn.com/play/news/303776',
        'http://video.udn.com/embed/news/300040/3',
        'http://video.udn.com/embed/news/300040/',
        'http://video.udn.com/embed/news/300040/asdf'
    ]
    expect_url = 'https://video.udn.com/embed/news/300040'


# Generated at 2022-06-14 17:30:18.612589
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Constructor test
    """
    video_id = '300040'
    webpage_url = 'http://video.udn.com/embed/news/%s' % video_id

    # test 1:
    # the webpage_url is a valid URL
    ie = UDNEmbedIE()
    if not ie.suitable(webpage_url):
        # should not be here
        raise AssertionError('UDN Embed IE: video.udn.com is not suitable.')
    # there should be no error raised
    ie.extract(webpage_url)

    # test 2:
    # the webpage_url is an invalid URL
    invalid_webpage_url = 'http://video.udn.com/embed/news/'
    ie = UDNEmbedIE()

# Generated at 2022-06-14 17:30:47.313190
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Testing constructor without parameter
    ie = UDNEmbedIE()
    # Testing constructor with parameter
    ie = UDNEmbedIE(params=dict())

# Generated at 2022-06-14 17:30:49.852394
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Smoke test for UDNEmbedIE
    """
    udn_embed_ie = UDNEmbedIE()
    # Constructor test
    assert udn_embed_ie

# Generated at 2022-06-14 17:30:53.061586
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udneie = UDNEmbedIE()

# Generated at 2022-06-14 17:30:56.677171
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    '''
    Constructor test
    '''
    assert(UDNEmbedIE.ie_key() == 'udn')
    assert(UDNEmbedIE.ie_name() == '聯合影音')

# Generated at 2022-06-14 17:30:57.938997
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE().IE_NAME == 'udn'

# Generated at 2022-06-14 17:31:01.601901
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/news/303776'
    actual = UDNEmbedIE()._real_extract(url)
    expected = '303776'
    assert actual['id'] == expected

# Generated at 2022-06-14 17:31:03.199620
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:31:06.403004
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    for url in UDNEmbedIE._TESTS:
        u = UDNEmbedIE(url)
        assert u._VALID_URL == url['url']
        assert u._TESTS == url

test_UDNEmbedIE()

# Generated at 2022-06-14 17:31:10.729986
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    assert ie._match_id(url) == '300040'

# Generated at 2022-06-14 17:31:15.549944
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    _ = InfoExtractor._make_result(UDNEmbedIE()._real_extract, url)

# Generated at 2022-06-14 17:32:16.346510
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:32:19.058002
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    inst = UDNEmbedIE()
    assert(inst != None)
    assert(isinstance(inst, InfoExtractor))

# Generated at 2022-06-14 17:32:20.742228
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie

# Generated at 2022-06-14 17:32:21.659712
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:32:23.584969
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    test for constructor of class UDNEmbedIE
    """
    u = UDNEmbedIE()
    assert u is not None

# Generated at 2022-06-14 17:32:26.552252
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    test_obj = UDNEmbedIE()
    result = test_obj.suitable(url)
    assert result is True
    assert test_obj._match_id(url) == '300040'

# Generated at 2022-06-14 17:32:32.642048
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL.encode('utf-8')
    try:
        UDNEmbedIE._VALID_URL = re.compile(url)
    except Exception:
        UDNEmbedIE._VALID_URL = re.compile(url.decode())

    UDNEmbedIE._TESTS[0]['url'] = url

    udn = UDNEmbedIE()
    assert udn._match_id(url) == '300040'

# Generated at 2022-06-14 17:32:34.833756
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDNEmbedIE'
    assert ie.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:32:38.908840
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE().IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:32:49.683868
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import FakeYDL
    from .youtube import YoutubeIE
    from . import YoutubeDL
    # Url for embed format
    embed_video_url = 'https://video.udn.com/embed/news/300040'
    # Url for play format
    play_video_url = 'https://video.udn.com/play/news/303776'
    # Url for youtube format
    youtube_video_url = 'https://video.udn.com/embed/news/300050'

    # Unit test to extract video original url

# Generated at 2022-06-14 17:34:47.815740
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE().IE_NAME == 'UDNEmbed'

# Generated at 2022-06-14 17:34:49.969007
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_obj = UDNEmbedIE()

    assert test_obj.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:34:53.719615
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('www.udn.com')
    UDNEmbedIE('http://www.udn.com')
    UDNEmbedIE('http://video.udn.com/embed/news/300040')
    UDNEmbedIE('https://video.udn.com/play/news/303776')

# Generated at 2022-06-14 17:35:04.920562
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    # Test matching of protocol-relative URL
    protocol_relative_valid_url = udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL
    assert protocol_relative_valid_url == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # Test matching of valid URL
    valid_url = udn_embed_ie._VALID_URL
    assert valid_url == r'https?:' + protocol_relative_valid_url
    # Test matching of URL by using valid URL
    url = 'https://video.udn.com/embed/news/300040'
    url_result = udn_embed_ie._match_id(url)
    assert url_result == '300040'
   

# Generated at 2022-06-14 17:35:17.549196
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .mock import MockIE

    # First create a mock IE to download the page
    class MockUDNEmbedIE(MockIE):
        IE_DESC = 'Mock video.udn.com'

        def _real_extract(self, url):
            return {
                'id': '300040',
                'html': '<script>var options = {video:{"mp4":""} };</script>'
            }
    mock_ie = MockUDNEmbedIE(test_UDNEmbedIE.__name__)

    # Then create a new IE instance, which will call the _real_extract() of
    # UDNEmbedIE class
    new_ie = UDNEmbedIE(test_UDNEmbedIE.__name__, mock_ie.test_result)

    new_ie.ext

# Generated at 2022-06-14 17:35:23.847820
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:35:30.613032
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE({})
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040' 
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:35:31.625018
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:35:35.525465
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # 1. Test return of the call to class constructor
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'

# Generated at 2022-06-14 17:35:46.009444
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Basic test cases."""
    url1 = 'http://video.udn.com/embed/news/300040'
    url2 = 'https://video.udn.com/embed/news/300040'
    url3 = 'https://video.udn.com/play/news/303776'

    # Check if the regex works in extracting video id from basic video urls
    assert UDNEmbedIE._match_id(url1) == '300040', \
        '"_match_id" failed in parsing video id from "%s"' % url1
    assert UDNEmbedIE._match_id(url2) == '300040', \
        '"_match_id" failed in parsing video id from "%s"' % url2