

# Generated at 2022-06-14 17:27:03.766401
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:27:07.467414
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Basic unit test case to test the constructor of class UDNEmbedIE."""
    udn = UDNEmbedIE()

    # Check if it is a subclass of InfoExtractor
    assert udn.__class__.__bases__[0].__name__ == 'InfoExtractor'

    # Check if it implements _real_extract()
    assert udn._real_extract.__func__ is not InfoExtractor._real_extract.__func__

# Generated at 2022-06-14 17:27:08.479704
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:27:10.305696
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    assert obj._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:14.256612
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Unit test for constructor of class UDNEmbedIE
    """
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:25.420310
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/embed/news/300040'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:34.116653
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_cases = [
        ('//video.udn.com/embed/news/300040', '300040'), 
        ('//video.udn.com/play/news/300041', '300041'),
        ('https://video.udn.com/play/news/300042', '300042'),
    ]
    ie = UDNEmbedIE()
    for test_case in test_cases:
        url = test_case[0]
        video_id = test_case[1]
        assert ie._match_id(url) == video_id

# Generated at 2022-06-14 17:27:40.014651
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    IE = UDNEmbedIE()
    assert IE.IE_DESC == '聯合影音'
    assert IE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert IE._TESTS[1]['only_matching'] == True

# Generated at 2022-06-14 17:27:41.977139
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie1 = UDNEmbedIE()
    ie2 = UDNEmbedIE()
    assert ie1 != ie2

# Generated at 2022-06-14 17:27:44.592823
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/embed/news/300040'
    UDNEmbedIE()._real_extract(url)

# Generated at 2022-06-14 17:27:54.213448
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Unit test for constructor of class UDNEmbedIE
    """
    UDNEmbedIE()



# Generated at 2022-06-14 17:28:04.267237
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie.IE_DESC, str)
    assert len(ie.IE_DESC) > 0
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'

# Generated at 2022-06-14 17:28:10.133075
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """test the construction of class UDNEmbedIE"""
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:28:12.010391
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert type(UDNEmbedIE({}).decryptor) is not None
    assert UDNEmbedIE({}).IE_DESC

# Generated at 2022-06-14 17:28:15.342041
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE(None).get_ie_key('https://video.udn.com/embed/news/300040') == 'UDNEmbed'
    assert UDNEmbedIE(None).get_ie_key('https://video.udn.com/play/news/300040') == 'UDNEmbed'

# Generated at 2022-06-14 17:28:26.644275
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:29.799226
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('https://video.udn.com/embed/news/300040')
    assert(ie._VALID_URL == ie.VALID_URL)

# Generated at 2022-06-14 17:28:32.144406
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    assert obj.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:28:39.888901
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test class UDNEmbedIE"""
    print('[Start udn test]')
    vid = '300040'

    # YouTube test
    youtube_url = 'http://video.udn.com/embed/news/140065?autoplay=1&vid=YOUTUBE_266833025'
    from .youtube import YoutubeIE
    assert YoutubeIE().suitable(youtube_url) == True

    # Full test (including m3u8/f4m/mp4)
    test_url = 'https://video.udn.com/embed/news/' + vid
    u = UDNEmbedIE()
    info = u.extract(test_url)
    assert u.suitable(test_url) == True
    assert info['id'] == vid
    assert info['title'] != ''

# Generated at 2022-06-14 17:28:48.501002
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    infoExtractor = UDNEmbedIE()
    infoExtractor.suitable('http://video.udn.com/embed/news/300040')
    infoExtractor.suitable('https://video.udn.com/embed/news/300040')
    infoExtractor.suitable('https://video.udn.com/play/news/303776')
    try:
        infoExtractor.suitable('https://video.udn.com/news/300040')
        assert False
    except Exception as e:
        assert str(e) == 'Not suitable for this IE'

# Generated at 2022-06-14 17:29:04.066787
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert(ie.IE_NAME == 'udn')
    assert(ie.IE_DESC == '聯合影音')


# Generated at 2022-06-14 17:29:09.473596
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnei = UDNEmbedIE()
    assert udnei.IE_NAME == 'udn:embed' and udnei.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:29:10.594660
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print(UDNEmbedIE)

# Generated at 2022-06-14 17:29:14.383079
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    a = UDNEmbedIE()
    assert a._VALID_URL == a.VALID_URL
    assert a._TESTS[0]["url"] == a.workingUrl("http://video.udn.com/embed/news/300040")

# Generated at 2022-06-14 17:29:20.385132
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import InfoExtractor

    ie = InfoExtractor(UDNEmbedIE.ie_key())
    assert ie.IE_NAME == UDNEmbedIE.ie_name()
    assert ie.IE_DESC == UDNEmbedIE.ie_desc()
    assert ie.IE_VERSION == UDNEmbedIE.ie_version()



# Generated at 2022-06-14 17:29:22.137146
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    u = UDNEmbedIE()
    assert isinstance(u, UDNEmbedIE)

# Generated at 2022-06-14 17:29:25.832937
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIEInstance = UDNEmbedIE()
    assert UDNEmbedIEInstance._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'



# Generated at 2022-06-14 17:29:33.089409
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'

# Generated at 2022-06-14 17:29:36.719059
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    info_extractor = UDNEmbedIE()
    assert info_extractor._VALID_URL == r'https?:\/\/video\.udn\.com\/(?:embed|play)\/news\/(?P<id>\d+)'



# Generated at 2022-06-14 17:29:42.181823
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    obj.IE_NAME = 'videoudn'
    obj.IE_DESC = 'UDN Video'
    assert obj.IE_NAME == 'videoudn'
    assert obj.IE_DESC == 'UDN Video'

# Generated at 2022-06-14 17:30:14.148102
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # It should raise a ValueError when its protocol of the video is
    # neither 'http://' nor 'https://'.
    try:
        UDNEmbedIE('//video.udn.com/embed/news/300040')
    except Exception as err:
        assert isinstance(err, ValueError)
        assert str(err) == 'The value of url must be an url starts with http:// or https://, but actually it is not.'

# Generated at 2022-06-14 17:30:24.387579
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # Note that the following URL is not a valid URL, but just a string
    # to be fed to constructor of the class
    assert ie.IE_NAME == 'udn'
    url = 'http://video.udn.com/play/news/300040'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert ie.SUFFIX == '(?:embed|play)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id']

# Generated at 2022-06-14 17:30:26.396266
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._real_initialize(url)

# Generated at 2022-06-14 17:30:31.408651
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_ie._VALID_URL == r'https?:' + udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:30:32.570490
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    t = UDNEmbedIE()
    print(t)

# Generated at 2022-06-14 17:30:37.521551
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    t = UDNEmbedIE()
    assert t.IE_DESC == '聯合影音'
    assert t._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert t._VALID_URL == 'https?:' + t._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:30:38.750295
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Test UDNEmbedIE constructor
    """
    UDNEmbedIE()

# Generated at 2022-06-14 17:30:50.590311
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .test_download import fake_http_server
    import requests

    def http_handler(s, h, r):
        h.putheader('content-type', 'text/html')
        h.endheaders()
        s.wfile.write(b'<video></video>')
        return True

    with fake_http_server(http_handler) as httpd:
        udn_extractor = UDNEmbedIE.ie_key()('http://localhost:80/foo')
        assert isinstance(udn_extractor, UDNEmbedIE)
        assert udn_extractor.url == 'http://localhost:80/foo'
        assert udn_extractor._downloader is None
        assert len(udn_extractor._ies) == 0

# Generated at 2022-06-14 17:30:52.112565
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        UDNEmbedIE(u'UDNEmbedIE')
    except ValueError:
        assert False

# Generated at 2022-06-14 17:30:53.356416
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None)

# Generated at 2022-06-14 17:31:20.473640
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('', {})
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:31:22.215360
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:31:27.849506
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Tests relative URL
    url = '//video.udn.com/embed/news/300040'
    UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL = re.escape(url)
    ie = UDNEmbedIE(url)
    assert ie._match_id(url) == '300040'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == re.escape(url)

# Generated at 2022-06-14 17:31:31.274893
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # Since URL is not needed in this constructor,
    # we could create an instance without a URL
    assert ie.test()



# Generated at 2022-06-14 17:31:33.773792
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    i = UDNEmbedIE()
    assert(i.IE_NAME == 'UDN')
    assert(i.IE_DESC == '聯合影音')

# Generated at 2022-06-14 17:31:38.059108
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE = UDNEmbedIE()
    _, _ = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    _, _ = UDNEmbedIE('https://video.udn.com/embed/news/300040')
    _, _ = UDNEmbedIE('https://video.udn.com/play/news/300040')

# Generated at 2022-06-14 17:31:40.398436
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert udn.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:31:46.517554
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test https url
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()(url)
    # test protocol-relative url
    url = '//video.udn.com/embed/news/300040'
    UDNEmbedIE()(url)

# Generated at 2022-06-14 17:31:48.291696
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'UDNEmbed'

# Generated at 2022-06-14 17:31:57.024431
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:33:10.786080
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test with a valid url
    url = 'https://video.udn.com/embed/news/300040'
    try:
        ie = UDNEmbedIE()
        assert ie._match_id(url) == '300040'
    except:
        assert False

# Generated at 2022-06-14 17:33:13.977060
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL = re.compile(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL)
    except Exception as e:
        print("Error: " + str(e))
    testIE = UDNEmbedIE("http://video.udn.com/embed/news/300040")
    print("Test completed.")

# Generated at 2022-06-14 17:33:19.601903
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from ..compat import compat_str
    # Test class construction
    udn_embed_ie = UDNEmbedIE()
    assert isinstance(udn_embed_ie._VALID_URL, compat_str)
    assert udn_embed_ie._TESTS
    assert isinstance(udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL, compat_str)
    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:33:22.954898
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie_obj = UDNEmbedIE(None)
    assert ie_obj != None

# Generated at 2022-06-14 17:33:24.863491
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE({}, {}, {}, {})
    assert ie.IE_NAME == ie.ie_key()

# Generated at 2022-06-14 17:33:30.491481
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from ..infoextractors import InfoExtractor

    ie = InfoExtractor()
    ie.add_info_extractor(UDNEmbedIE)
    for t in ie._TESTS:
        ie.extract(t['url'])
        ie.download(t['url'])

# Generated at 2022-06-14 17:33:32.097253
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    return UDNEmbedIE(InfoExtractor())


# Generated at 2022-06-14 17:33:35.314150
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    valid_url = 'https://video.udn.com/embed/news/300040'
    invalid_url = 'https://www.udn.com/news/breaknews/1/1200797'

    # This is valid URL
    assert UDNEmbedIE._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE.suitable(valid_url)

    # This is invalid URL
    assert not UDNEmbedIE.suitable(invalid_url)


# Generated at 2022-06-14 17:33:39.778757
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test normal cases
    UDNEmbedIE()

    # Test exception cases
    try:
        UDNEmbedIE(test=True)
        assert False
    except:
        assert True

    assert True

# Generated at 2022-06-14 17:33:40.864449
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(True)

# Generated at 2022-06-14 17:36:20.635208
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test for extracting the udn video id.
    udn_ie = UDNEmbedIE('http://video.udn.com/play/news/300040')
    assert udn_ie._match_id('http://video.udn.com/embed/news/300040') == '300040'

    # Test for _real_extract method in UDNEmbedIE object.
    extract_result = udn_ie._real_extract('http://video.udn.com/embed/news/300040')
    assert extract_result.get('id') == '300040'
    assert extract_result.get('title') == '生物老師男變女 全校挺"做自己"'
    assert extract_result.get('thumbnail') is not None

# Generated at 2022-06-14 17:36:32.534370
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    #pylint: disable=protected-access
    url = 'http://video.udn.com/embed/news/300040'
    obj = UDNEmbedIE._udn_embed_ie(url)
    assert obj._VALID_URL == UDNEmbedIE._VALID_URL
    assert obj._TESTS == UDNEmbedIE._TESTS
    assert obj._downloader.params['force_generic_extractor'] == False

    urls = ['http://video.udn.com/embed/news/300040', 'https://video.udn.com/embed/news/300040']
    for url in urls:
        IE_DESC = '聯合影音'

# Generated at 2022-06-14 17:36:41.048051
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # given
    video_url = 'https://video.udn.com/embed/news/303776'

    # when
    ie = UDNEmbedIE(None)
    ie.extract(video_url)

    # then
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:36:43.498452
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Unit test for constructor of class UDNEmbedIE"""
    UDNEmbedIE()



# Generated at 2022-06-14 17:36:45.869011
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    embed_ie = UDNEmbedIE()
    embed_ie.download('http://video.udn.com/embed/news/300040')
    embed_ie.download('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:36:46.626253
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Todo: implment
    pass

# Generated at 2022-06-14 17:36:52.521302
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    url = 'http://video.udn.com/embed/news/300040'
    expected_re = r'^http://video\.udn\.com/embed/news/(?P<id>\d+)$'
    expected_ie_key = 'UDNEmbed'
    expected_ie_desc = '聯合影音'