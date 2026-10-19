

# Generated at 2022-06-14 17:27:14.853399
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    youtube_url = 'https://video.udn.com/embed/news/300040'
    udn_embed = UDNEmbedIE(youtube_url, {}, {}, {})
    assert udn_embed.match()
    ff = udn_embed.get_formats()
    assert ff
    assert ff[0].get('protocol') == 'm3u8_native'
    info = udn_embed.extract({}, youtube_url)
    vid = info.get('id')
    assert vid

# Generated at 2022-06-14 17:27:16.852733
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test constructor of class UDNEmbedIE"""
    UDNEmbedIE()

# Generated at 2022-06-14 17:27:22.450370
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert udn._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn._VALID_URL == r'https?:' + udn._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:27:24.998881
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:27:28.397191
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/embed/news/300040'
    inst = UDNEmbedIE()
    if (not inst):
        return False
    return inst._match_id(url) == '300040'

# Generated at 2022-06-14 17:27:34.840379
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    a = UDNEmbedIE()
    assert a._VALID_URL == UDNEmbedIE._VALID_URL
    assert a._TESTS == UDNEmbedIE._TESTS
    assert a._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert a.IE_DESC == UDNEmbedIE.IE_DESC

# Generated at 2022-06-14 17:27:37.521316
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """ Unit test for UDNEmbedIE"""
    UDNEmbedIE('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:27:40.800089
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:43.098829
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert udne.IE_NAME == 'udn.com:embed'

# Generated at 2022-06-14 17:27:45.858350
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        UDNEmbedIE()
    except TypeError:
        assert False, 'UDNEmbedIE constructor does not accept any arguments'

# Generated at 2022-06-14 17:27:57.529890
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    from .. import YoutubeDL
    ydl = YoutubeDL()
    udn = UDNEmbedIE()
    result = udn._real_extract(url)
    ydl.download([result['formats'][0]['url']])

# Generated at 2022-06-14 17:28:00.348686
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:28:07.350015
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE(None)

    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_ie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:13.226396
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:15.445825
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert re.search(udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL, "//video.udn.com/embed/news/300040")

# Generated at 2022-06-14 17:28:18.550999
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # A constructor of class InfoExtractor cannot have default value for parameter url
    UDNEmbedIE(url='http://test.test')

# Generated at 2022-06-14 17:28:20.908311
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    info_extractor = UDNEmbedIE

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:28:27.815291
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/300040?foo=bar') == '300040'


# Generated at 2022-06-14 17:28:30.429181
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    ie._real_extract('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:28:38.530905
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(None)

    test_url = 'http://video.udn.com/embed/news/300040'
    assert ie._match_id(test_url)
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

    test_url = 'https://video.udn.com/embed/news/300040'
    assert ie._match_id(test_url)

# Generated at 2022-06-14 17:28:54.426753
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie._PROTOCOL_RELATIVE_VALID_URL, compat_str)
    assert isinstance(ie._VALID_URL, compat_str)
    assert isinstance(ie._TESTS, list)



# Generated at 2022-06-14 17:29:02.549647
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    udnie = UDNEmbedIE()
    # test for _PROTOCOL_RELATIVE_VALID_URL
    assert udnie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # test for _VALID_URL
    assert udnie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # test for _TESTS

# Generated at 2022-06-14 17:29:09.138757
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:29:19.862981
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('test1_url')
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:29:24.527198
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    testclass = UDNEmbedIE()
    testclass.extract('http://video.udn.com/embed/news/300040')
    testclass.extract('https://video.udn.com/embed/news/300040')
    testclass.extract('https://video.udn.com/play/news/303776')

# Generated at 2022-06-14 17:29:29.642055
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:29:34.273033
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        UDNEmbedIE("", "", "")
    except Exception as e:
        print("UDNEmbedIE initial error: %s" % e)
        assert(False)


# Generated at 2022-06-14 17:29:42.534800
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Unit test for constructor of class UDNEmbedIE"""
    expected_IE = (
        UDNEmbedIE
        .udn_embed
        .ie
        .UDNEmbedIE
    )

    udn_embed_ie = expected_IE()

    # Check the type and value of the object
    assert isinstance(udn_embed_ie, expected_IE)
    assert udn_embed_ie.IE_NAME == 'UDNEmbed'
    assert udn_embed_ie.IE_DESC == '聯合影音'
    assert udn_embed_ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_ie._PROTOCOL_RELATIVE_

# Generated at 2022-06-14 17:29:44.483282
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Unit test case for udn_embed.UDNEmbedIE.__init__
    """
    pass


# Generated at 2022-06-14 17:29:53.070118
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE._real_extract('https://video.udn.com/embed/news/300040')
    UDNEmbedIE._real_extract('https://video.udn.com/play/news/300040')
    UDNEmbedIE._real_extract('https://video.udn.com/play/news/300040')
    UDNEmbedIE._real_extract('//video.udn.com/play/news/300040')

# Generated at 2022-06-14 17:30:26.543673
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_obj = UDNEmbedIE()
    expected_result = re.compile(r'^https?://.*\.jpg$')

    # Check if return value is as expected
    assert test_obj._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert test_obj._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert expected_result.match(test_obj._TESTS[0].get('thumbnail'))
    assert test_obj._TESTS[0].get('info_dict').get('id') == '300040'

# Generated at 2022-06-14 17:30:31.264490
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnIE = UDNEmbedIE()
    valid_url1 = "http://video.udn.com/embed/news/300040"
    valid_url2 = "https://video.udn.com/embed/news/300040"

    udnIE.suitable(valid_url1)
    udnIE.suitable(valid_url2)


test_UDNEmbedIE()

# Generated at 2022-06-14 17:30:33.064563
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE().to_screen("https://video.udn.com/embed/news/300040")

# Generated at 2022-06-14 17:30:37.455869
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert udne._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udne._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:38.667731
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_instantiation_of_class(UDNEmbedIE)


# Generated at 2022-06-14 17:30:40.481210
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    a = UDNEmbedIE()
    print("UDNEmbedIE-class initialized")

# Generated at 2022-06-14 17:30:51.670741
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # URL: http://video.udn.com/embed/news/300040
    url = 'http://video.udn.com/embed/news/300040'
    IE = UDNEmbedIE()
    assert IE.ie_key() == 'UDNEmbed'
    assert IE._VALID_URL == IE.VALID_URL
    assert 'url' in IE.get_info(url) # get_info

    # Test regex match
    # Test valid_url
    assert IE.valid_url(url)
    # Test _PROTOCOL_RELATIVE_VALID_URL
    url = url.replace('http://', '//')
    assert IE._PROTOCOL_RELATIVE_VALID_URL == IE.PROTOCOL_RELATIVE_VALID_URL
    assert IE.valid_url(url)

# Generated at 2022-06-14 17:30:58.087511
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:31:10.682845
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert ie._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('//video.udn.com/embed/news/300040') == '300040'
    assert ie._match_id('http://video.udn.com/play/news/300040') == '300040'
    assert ie._match_id('https://video.udn.com/play/news/300040') == '300040'

# Generated at 2022-06-14 17:31:13.535186
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE

# Generated at 2022-06-14 17:32:17.721703
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    instance = UDNEmbedIE()
    assert instance.IE_DESC == '聯合影音'
    assert instance._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert instance._VALID_URL == r'https?:' + instance._PROTOCOL_RELATIVE_VALID_URL
    assert instance._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert instance._TESTS[0]['info_dict']['id'] == '300040'

# Generated at 2022-06-14 17:32:19.906203
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    instance = UDNEmbedIE()
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 17:32:24.577048
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE(test_UDNEmbedIE.__name__)._VALID_URL == UDNEmbedIE._VALID_URL
    assert UDNEmbedIE(test_UDNEmbedIE.__name__)._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:32:29.194907
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert hasattr(ie, '_VALID_URL') and ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert hasattr(ie, '_TESTS') and len(ie._TESTS)
    assert hasattr(ie, '_PROTOCOL_RELATIVE_VALID_URL') and ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:32:36.442315
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():  
    url1 = 'https://video.udn.com/embed/news/300040'
    url2 = 'http://video.udn.com/embed/news/300040'
    assert UDNEmbedIE._VALID_URL == r'https?://video\.udn\.com/embed/news/(?P<id>\d+)'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/embed/news/(?P<id>\d+)'
    match1 = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    match2 = UDNEmbedIE._VALID_URL
    assert re.match(match1, url1) != None
    assert re.match(match1, url2) != None

# Generated at 2022-06-14 17:32:47.393321
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_obj = UDNEmbedIE()
    assert re.match(udn_obj._PROTOCOL_RELATIVE_VALID_URL, '//video.udn.com/embed/news/300040')
    assert re.match(udn_obj._PROTOCOL_RELATIVE_VALID_URL, '//video.udn.com/play/news/300040')
    assert re.match(udn_obj._VALID_URL, 'http://video.udn.com/embed/news/300040')
    assert re.match(udn_obj._VALID_URL, 'https://video.udn.com/embed/news/300040')
    assert re.match(udn_obj._VALID_URL, 'https://video.udn.com/play/news/300040')

# Generated at 2022-06-14 17:32:55.904453
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:33:00.550052
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE('test', 'test')
    assert udn_embed_ie.IE_DESC == '聯合影音'



# Generated at 2022-06-14 17:33:04.779152
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    for url in [
        "http://video.udn.com/embed/news/300040",
        "https://video.udn.com/embed/news/300040",
    ]:
        ie = UDNEmbedIE(url)
        assert ie.url == url
        assert ie.video_id == '300040'
        assert ie.ie_key() == 'UDNEmbed'


# Generated at 2022-06-14 17:33:07.713737
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    video = UDNEmbedIE(UDNEmbedIE.ie_key())
    video.extract(url)

# Generated at 2022-06-14 17:35:29.201488
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Constructor should not raise exception, so it's a successful test
    UDNEmbedIE(None)

# Generated at 2022-06-14 17:35:30.963722
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert 'UDNEmbed' in udne.ie_key()

# Generated at 2022-06-14 17:35:32.374150
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert (udne != None)

# Generated at 2022-06-14 17:35:36.319692
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert(UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    assert(UDNEmbedIE()._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

# Generated at 2022-06-14 17:35:39.319967
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:35:42.064453
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL.replace('/', '')
    assert UDNEmbedIE._VALID_URL == url

# Generated at 2022-06-14 17:35:49.511139
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/embed/news/300040'

    udn_embed_ie = UDNEmbedIE()
    udn_embed_ie._match_id(url)
    udn_embed_ie._real_extract(url)

    assert udn_embed_ie.IE_NAME == 'udn'
    assert udn_embed_ie.IE_DESC == '聯合影音'
    assert re.match(udn_embed_ie._VALID_URL, url)
    assert udn_embed_ie._TESTS[0]['url'] == url
    assert udn_embed_ie._TESTS[0]['info_dict']['id'] == '300040'

# Generated at 2022-06-14 17:35:53.597542
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE("http://video.udn.com/embed/news/300040")
    assert udne.IE_DESC == "聯合影音"

# Generated at 2022-06-14 17:35:54.514293
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None)

# Generated at 2022-06-14 17:35:59.799047
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    assert 'UDNEmbed' in obj.IE_NAME
    assert '聯合影音' in obj.IE_DESC
    assert obj._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert obj._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'