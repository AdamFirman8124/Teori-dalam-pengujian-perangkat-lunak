

# Generated at 2022-06-14 17:27:04.666702
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE(InfoExtractor())
    assert udn_embed_ie



# Generated at 2022-06-14 17:27:11.138767
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    m = UDNEmbedIE('')
    print(m.IE_NAME)
    print(m.IE_DESC)
    print(m.IE_VERSION)
    print(m.valid_urls)
    print(m.video_id_re)


# Generated at 2022-06-14 17:27:12.187978
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:27:12.938067
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie

# Generated at 2022-06-14 17:27:24.210602
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    res = udne.suitable('http://video.udn.com/embed/news/300040')
    assert(res)
    res = udne.suitable('http://video.udn.com/play/news/300040')
    assert(res)
    res = udne.suitable('http://video.udn.com/embed/news/300040')
    assert(res)
    res = udne.suitable('https://video.udn.com/play/news/300040')
    assert(res)
    res = udne.suitable('http://video.udn.com/news/303776')
    assert(not res)

# Generated at 2022-06-14 17:27:33.395091
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .test_common import make_test_url_result

    url = 'http://video.udn.com/embed/news/300040'
    # test protocol relative url
    assert UDNEmbedIE._match_id('//video.udn.com/embed/news/300040') == '300040'
    assert UDNEmbedIE._match_id('http://video.udn.com/embed/news/300040') == '300040'
    assert UDNEmbedIE._match_id('https://video.udn.com/embed/news/300040') == '300040'
    # test constructor
    ie = UDNEmbedIE(make_test_url_result(url, ie=UDNEmbedIE.ie_key()))
    # test _real_extract

# Generated at 2022-06-14 17:27:44.255678
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert bool(UDNEmbedIE._VALID_URL.match('http://video.udn.com/embed/news/300040'))
    assert bool(UDNEmbedIE._VALID_URL.match('https://video.udn.com/embed/news/300040'))
    assert UDNEmbedIE._VALID_URL.match('http://video.udn.com/play/news/300040')
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL.match('//video.udn.com/embed/news/300040')
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL.match('//video.udn.com/play/news/300040')

# Generated at 2022-06-14 17:27:56.460200
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
  print("Test UDNEmbedIE")
  # Save video in test.mp4 (UDNEmbedIE is the name of the class)
  # -f stands for format (mp4), -vn means no video, --no-playlist means don't download a playlist, -o stands for output
  # --write-sub means write vtt subtitles, --write-auto-sub means write srt subtitles
  # %(ext)s stands for extension, %(height)s stands for video height, %(id)s for video ID, %(uploader)s for uploader, %(uploader_id)s for uploader ID
  # %(upload_date)s for upload date (YYYYMMDD)

# Generated at 2022-06-14 17:27:59.550280
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Unit test for constructor of class UDNEmbedIE"""
    x = UDNEmbedIE()
    assert x


if __name__ == "__main__":
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:28:10.865027
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # https://video.udn.com/embed/news/333812
    url = 'https://video.udn.com/embed/news/333812'
    udn = UDNEmbedIE(False)
    assert udn._match_id(url) == '333812'
    udn._match_id('abcd') # No match, should return None
    # https://video.udn.com/play/news/333812
    url = 'https://video.udn.com/play/news/333812'
    udn = UDNEmbedIE(False)
    assert udn._match_id(url) == '333812'
    udn._match_id('abcd') # No match, should return None



# Generated at 2022-06-14 17:28:28.016840
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_IE = UDNEmbedIE()
    assert udn_embed_IE._PROTOCOL_RELATIVE_VALID_URL == "//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)"
    assert udn_embed_IE._VALID_URL == "(?i)https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)"

# Generated at 2022-06-14 17:28:29.317353
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:28:37.876108
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # If this fails due to changes, test_download_webpage_from_url also needs to
    # be updated
    IE_DESC = '聯合影音'

    assert 'UDNEmbedIE' == UDNEmbedIE.ie_key()

    # Check if video.udn.com/embed/news/300040 url is valid
    assert not UDNEmbedIE._match_id(
        'i_dont_match_any_pattern_in_UDNEmbedIE')

    assert '300040' == UDNEmbedIE._match_id('http://video.udn.com/embed/news/300040')
    assert '300040' == UDNEmbedIE._match_id('https://video.udn.com/embed/news/300040')

    # Check if json_

# Generated at 2022-06-14 17:28:45.409029
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE("UDNEmbedIE", "udn", UDNEmbedIE._VALID_URL, {}, {}, 'http://video.udn.com/embed/news/300040')
    UDNEmbedIE("UDNEmbedIE", "udn", UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL, {}, {}, '//video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:28:55.765336
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed = UDNEmbedIE()
    assert udn_embed._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed._VALID_URL == r'https?:' + udn_embed._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:29:03.482563
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Unit test for UDNEmbedIE class
    """
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.IE_DESC == '聯合影音', \
        "test_udn_embed_ie.py: UdneIE.IE_DESC should be '聯合影音'"
    assert udn_embed_ie._VALID_URL == \
        r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)', \
        "test_udn_embed_ie.py: UdneIE._VALID_URL is not consistent"

# Generated at 2022-06-14 17:29:09.138753
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_video_ie = UDNEmbedIE()
    assert(udn_video_ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)')

# Generated at 2022-06-14 17:29:09.965068
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    temp = UDNEmbedIE()
    test = temp._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:29:12.930884
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None)._valid_url('http://video.udn.com/embed/news/300040', '')
test_UDNEmbedIE.unit_test = True

# Generated at 2022-06-14 17:29:15.986632
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert ie.ie_key() == 'UDNEmbed'


# Generated at 2022-06-14 17:29:48.508813
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # youtube video
    youtube_url = 'http://video.udn.com/embed/news/300041'
    ie1 = UDNEmbedIE()
    assert ie1._PROTOCOL_RELATIVE_VALID_URL == ie1._VALID_URL[4:]
    ie1._download_webpage = lambda u, v, n: '\n'.join([
        'var options = {',
        '    "video" : {',
        '        "youtube" : "http://www.youtube.com/watch?v=xJXFrtKb-QQ"',
        '    }',
        '};',
        ])
    info_dicts = ie1._real_extract(youtube_url)

# Generated at 2022-06-14 17:29:50.174477
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE("test")



# Generated at 2022-06-14 17:29:59.245814
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    _test = udne._test
    assert _test('http://video.udn.com/embed/news/300040')
    assert _test('https://video.udn.com/embed/news/300040')
    assert _test('http://video.udn.com/play/news/303776')
    assert _test('https://video.udn.com/play/news/303776')

# Generated at 2022-06-14 17:30:00.308763
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:30:02.426401
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        # Check whether there is an exception
        UDNEmbedIE()
    except:
        assert False
    else:
        assert True

# Generated at 2022-06-14 17:30:08.130403
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """test UDNEmbedIE"""
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._VALID_URL == r'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE.IE_DESC == '聯合影音'

test_UDNEmbedIE()

# Generated at 2022-06-14 17:30:10.044272
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('http://video.udn.com', 'test_UDNEmbedIE')


# Generated at 2022-06-14 17:30:22.319893
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:30:31.550982
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('https://video.udn.com/embed/news/300040')
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:35.197692
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == ie._VALID_URL
    assert ie._PROTOCOL_RELATIVE_VALID_URL == ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie._TESTS == ie._TESTS

# Generated at 2022-06-14 17:31:01.745093
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

# Generated at 2022-06-14 17:31:03.990763
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .test_utils import parse_files_dict
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE.UDNEmbedIE(url, parse_files_dict())

# Generated at 2022-06-14 17:31:12.330318
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    _url = 'http://video.udn.com/embed/news/300040'
    _url_https = 'https://video.udn.com/embed/news/300040'
    _url_play = 'https://video.udn.com/play/news/300040'
    ie = UDNEmbedIE()
    assert ie._match_id(_url) == ie._match_id(_url_https) == '300040'
    assert ie._match_id(_url) == ie._match_id(_url_play)

# Generated at 2022-06-14 17:31:24.738582
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class_init = UDNEmbedIE
    instance = class_init
    # test '_VALID_URL'
    assert instance._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    # test '_PROTOCOL_RELATIVE_VALID_URL'
    assert instance._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    # test 'IE_DESC'
    assert instance.IE_DESC == '聯合影音'
    # test '_TEST'
    assert len(instance._TESTS) == 3
    # test '_TEST[0]'

# Generated at 2022-06-14 17:31:28.050615
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/play/news/303776'
    UDNEmbedIE()._match_id(url)

# Only to use in Unit test

# Generated at 2022-06-14 17:31:37.893020
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnEmbedIE = UDNEmbedIE()
    print(udnEmbedIE.ie_key())
    print(udnEmbedIE.ie_desc())
    print(udnEmbedIE.working)
    print(udnEmbedIE.webpage_url_re)
    print(udnEmbedIE.embed_webpage_url_re)
    print(udnEmbedIE.report_warnings)
    print(udnEmbedIE.has_age_limit)
    print(udnEmbedIE.age_limit)
    print(udnEmbedIE.update_dict)
    print(udnEmbedIE.available)
    print(udnEmbedIE.available_options)
    print(udnEmbedIE.extract_flat)

# Generated at 2022-06-14 17:31:50.137464
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/embed/news/300040'
    udne = UDNEmbedIE()
    # Make a fake webpage for testing
    webpage = '<html><head>'
    webpage += '<title>Fake UDNEmbedIE testing webpage</title>'
    webpage += '<meta name="description" content="Fake UDNEmbedIE testing webpage">'
    webpage += '<script language="javascript">var options={"x":"x","y":"y","z":"z"};</script>'
    webpage += '</head><body><div>Fake UDNEmbedIE testing webpage</div></body></html>'
    # Test if the fake webpage can be downloaded and parsed
    test1 = udne._download_webpage(url, udne._match_id(url))
    assert test1

# Generated at 2022-06-14 17:31:52.340023
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('UDNEmbedIE', 'http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:32:01.540058
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE({})
    with ie:
        assert ie._VALID_URL == ie.VALID_URL
        assert ie._PROTOCOL_RELATIVE_VALID_URL == ie.PROTOCOL_RELATIVE_VALID_URL
        assert ie._TESTS == ie.TESTS
        assert ie._PROTOCOL_RELATIVE_VALID_URL.match("//video.udn.com/embed/news/300040")
        assert ie._VALID_URL.match("http://video.udn.com/embed/news/300040")

# Generated at 2022-06-14 17:32:08.765415
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    c = UDNEmbedIE()
    assert c.IE_NAME == 'udn'
    assert c.IE_DESC == '聯合影音'
    assert c._VALID_URL == r'https?:' + c._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:33:18.389946
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()



# Generated at 2022-06-14 17:33:23.447912
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    expected = r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == expected, \
        "Unexpected _PROTOCOL_RELATIVE_VALID_URL"

# Generated at 2022-06-14 17:33:25.284452
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE('http://video.udn.com/embed/news/300040').IE_NAME == 'udn'

# Generated at 2022-06-14 17:33:26.899415
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test whether the constructor can work
    ie = UDNEmbedIE()
    assert ie

# Generated at 2022-06-14 17:33:36.196099
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Unit test for constructor of class UDNEmbedIE"""
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    for valid_url in ('http://video.udn.com/embed/news/300040', 'http://video.udn.com/play/news/300040'):
        assert ie.suitable(valid_url) == True
    assert ie.suitable('https://udn.com/news/story/7259/4515606') == False



# Generated at 2022-06-14 17:33:42.027748
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    if __name__ == '__main__':
        URL = 'http://video.udn.com/embed/news/300040'
        ie = UDNEmbedIE()
        info = ie.extract(URL)
        print(info)
    else:
        assert False

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:33:45.570959
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    r = UDNEmbedIE()
    assert r.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:33:47.835771
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    for test in UDNEmbedIE._TESTS:
        UDNEmbedIE(test)

# Generated at 2022-06-14 17:33:56.944289
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class_ = globals()['UDNEmbedIE']
    ie = class_()
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:34:06.951830
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:36:48.593576
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:36:51.295825
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == UDNEmbedIE._VALID_URL
    assert ie._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert ie._TESTS == UDNEmbedIE._TESTS