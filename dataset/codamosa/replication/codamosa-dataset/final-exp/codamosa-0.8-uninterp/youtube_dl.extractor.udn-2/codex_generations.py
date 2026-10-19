

# Generated at 2022-06-14 17:27:15.327034
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test the constructor of class UDNEmbedIE
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == ie._VALID_URL
    assert ie._TESTS == ie._TESTS
    assert ie._extract_m3u8_formats(ie, '') == ie._extract_m3u8_formats(ie, '')
    assert ie._real_extract(ie, '') == ie._real_extract(ie, '')

# Generated at 2022-06-14 17:27:18.154949
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None)

# Generated at 2022-06-14 17:27:19.721112
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    print(udn)


# Generated at 2022-06-14 17:27:25.048729
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import sys
    orig_test_UDNEmbedIE = UDNEmbedIE.test
    UDNEmbedIE.test = lambda *args, **kwargs: None
    try:
        UDNEmbedIE(sys.argv[1:])
    finally:
        UDNEmbedIE.test = orig_test_UDNEmbedIE

# Generated at 2022-06-14 17:27:29.184797
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('test', True)
    UDNEmbedIE('test', False)
    UDNEmbedIE('test', 0)
    UDNEmbedIE('test', '0')
    UDNEmbedIE('test', [])
    UDNEmbedIE('test', None)


# Generated at 2022-06-14 17:27:33.054895
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:36.517505
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert isinstance(udn_embed_ie, InfoExtractor)


# Generated at 2022-06-14 17:27:47.641725
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test when query of 'url' is '/embed/news/*', the I.E. UDNEmbedIE
    # should be constructed.
    query = '/embed/news/Udn_20171114_MOV00239'
    match = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    m = re.match(match, query)
    assert m
    ie = UDNEmbedIE({})
    assert ie._match_id(query) == 'udn_20171114_mov00239'

    # Test when query of 'url' is '/play/news/*', the I.E. UDNEmbedIE
    # should be constructed.
    query = '/play/news/Udn_20171114_MOV00239'
    m = re.match(match, query)
    assert m

# Generated at 2022-06-14 17:27:54.807306
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'


# Generated at 2022-06-14 17:28:04.664422
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from ..compat import str

    UDNEmbedIE_url= 'http://video.udn.com/embed/news/300040'
    expected_udn_embed_ie = UDNEmbedIE(
        compat_urlparse.urlparse(UDNEmbedIE_url),str(UDNEmbedIE_url))

    assert expected_udn_embed_ie.ie_key() == 'UDNEmbed'
    assert expected_udn_embed_ie.ie_desc() == '聯合影音'
    assert expected_udn_embed_ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert expected_udn_embed_ie._PROTOCOL_RELATIVE_VALID_

# Generated at 2022-06-14 17:28:20.115925
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE("")
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:28:27.815574
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TESTS[0]['url'] == ie.TESTS[0]['url']
    assert ie._TESTS[0]['info_dict']['id'] == ie.TESTS[0]['info_dict']['id']
    assert ie.is_suitable('https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:28:30.006159
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Construct an object (for testing purposes).
    """
    UDNEmbedIE()

# Generated at 2022-06-14 17:28:38.236141
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        import bs4
        import requests
    except ImportError:
        print("Please install the `bs4` or `requests` package.")
    assert bs4 is not None, "`bs4` is required for this test."
    assert requests is not None, "`requests` is required for this test."

    url = "http://video.udn.com/embed/news/300040"
    webpage = requests.get(url).text
    soup = bs4.BeautifulSoup(webpage, "html.parser")
    iframe = soup.find("iframe")
    assert iframe is not None, "Can't find `iframe` in url=%s." % url


# Generated at 2022-06-14 17:28:49.785596
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class TestUDNEmbedIE(UDNEmbedIE):
        def _real_extract(self, url):
            return super(TestUDNEmbedIE, self)._real_extract(url)

    # test for _PROTOCOL_RELATIVE_VALID_URL
    assert (TestUDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
        == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

    # test for _VALID_URL
    assert (TestUDNEmbedIE._VALID_URL 
        == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')

    # test for IE_DESC

# Generated at 2022-06-14 17:28:55.682330
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert ie.IE_DESC == '聯合影音'

    ie = UDNEmbedIE('http://video.udn.com/play/news/300040')
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:28:57.014734
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test for constructor
    ie = UDNEmbedIE()

# Generated at 2022-06-14 17:28:57.833760
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_instance = UDNEmbedIE()

# Generated at 2022-06-14 17:29:03.942187
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        assert UDNEmbedIE._VALID_URL == "https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)"
        assert UDNEmbedIE.IE_DESC == "聯合影音"
        # self.assertRegexpMatches(UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL,
        # r'^//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    except: pass
    print("Unit test for constructor of class UDNEmbedIE PASS!")


# Generated at 2022-06-14 17:29:09.364656
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:29:31.235246
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    class_UDNEmbedIE = UDNEmbedIE
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE = class_UDNEmbedIE(url, {})
    # Test for _match_id(url)
    assert (UDNEmbedIE._match_id(url) == '300040')
    # Test for _real_extract(url)
    assert (UDNEmbedIE._real_extract(url)['id'] == '300040')
    assert (UDNEmbedIE._real_extract(url)['url'] == 'http://vod.udn.com.edgesuite.net/udnvideo/300040_0p_400.mp4')

# Generated at 2022-06-14 17:29:36.912838
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    pattern = re.compile(r'^https?://video\.udn\.com/(?:embed|play)/news/\d+$')
    ie = UDNEmbedIE()
    assert pattern.match(ie._VALID_URL) is not None
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:29:44.122409
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn.com:embed'
    assert ie._VALID_URL == 'https?://video\\.udn\\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\\.udn\\.com/(?:embed|play)/news/(?P<id>\\d+)'

# Generated at 2022-06-14 17:29:49.908413
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    url = ie.extract('http://video.udn.com/embed/news/300040')
    assert url.get('url') == 'https://www.youtube.com/watch?v=r_T0TpV9Dik'
    url = ie.extract('https://video.udn.com/embed/news/300040')
    assert url.get('url') == 'https://www.youtube.com/watch?v=r_T0TpV9Dik'

# Generated at 2022-06-14 17:29:52.568508
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    IE = UDNEmbedIE()
    ie = IE.from_id('')


# Generated at 2022-06-14 17:29:55.774314
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDN'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:30:00.882423
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/play/news/303776'
    ie = UDNEmbedIE()
    obj1 = ie._match_id(url)
    obj2 = ie._real_extract(url)

    assert obj1 == obj2['id']

# Generated at 2022-06-14 17:30:03.246581
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url ='https://video.udn.com/embed/news/300040'
    UDNEmbedIE()._real_extract(url)

# Generated at 2022-06-14 17:30:11.501370
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import InfoExtractor
    from ..compat import compat_urllib_parse

    url = 'http://video.udn.com/embed/news/300040'
    video_id = UDNEmbedIE._match_id(url);
    page = InfoExtractor()._download_webpage(url, video_id)

    options_str = UDNEmbedIE._html_search_regex(
        r'var\s+options\s*=\s*([^;]+);', page, 'options')
    trans_options_str = js_to_json(options_str)

    options = UDNEmbedIE._parse_json(trans_options_str, 'options', fatal=False)

    if options:
        title = options['title']
        poster = options.get('poster')

# Generated at 2022-06-14 17:30:13.419632
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Constructor test case"""

    udne_test = UDNEmbedIE()

test_UDNEmbedIE()

# Generated at 2022-06-14 17:30:43.372450
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('http://example.com')

# Generated at 2022-06-14 17:30:47.788251
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    _udn = UDNEmbedIE()
    assert _udn._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:57.732334
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:31:00.201859
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == "聯合影音"

# Generated at 2022-06-14 17:31:11.230024
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    parser = UDNEmbedIE()
    assert parser.suitable('http://video.udn.com/embed/news/300040') == True
    assert parser.suitable('https://video.udn.com/embed/news/300040') == True
    assert parser.suitable('https://video.udn.com/play/news/300040') == True
    assert parser.suitable('https://video.udn.com/embed/news/300000') == False
    assert parser.suitable('https://video.udn.com/google/news/300040') == False
    assert parser.suitable('http://video.udn.com/google/news/300040') == False


# Generated at 2022-06-14 17:31:15.076529
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:31:23.181798
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    instance = UDNEmbedIE()
    assert(isinstance(instance, InfoExtractor))
    res = instance._real_extract(url)
    assert(bool(res))
    #for key, value in res.items():
    #    print("key: {0}, value: {1}".format(key, value))


if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:31:30.314585
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE({})
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.IE_DESC == '聯合影音'


# Generated at 2022-06-14 17:31:35.750090
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    i = UDNEmbedIE()
    url = 'http://video.udn.com/embed/news/300040'
    assert i._VALID_URL == UDNEmbedIE._VALID_URL
    assert i._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert i._match_url(url) == ('300040','')

# Generated at 2022-06-14 17:31:40.171402
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300044'
    UDNEmbedIE(UDNEmbedIE.ie_key())._real_extract(url)

# Generated at 2022-06-14 17:32:58.626284
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie == UDNEmbedIE

# Generated at 2022-06-14 17:33:11.124904
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .. import UDNEmbedIE
    udn_IE = UDNEmbedIE()
    assert(udn_IE.IE_DESC == '聯合影音')
    assert(udn_IE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    assert(udn_IE._VALID_URL == 'https?:' + udn_IE._PROTOCOL_RELATIVE_VALID_URL)
    # Unit test for _real_extract
    udn_IE._real_extract(
        'http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:33:22.997011
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn.com:embed'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'

# Generated at 2022-06-14 17:33:23.944962
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('test').test()

# Generated at 2022-06-14 17:33:28.456281
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    q1 = ie._PROTOCOL_RELATIVE_VALID_URL
    q2 = ie._VALID_URL
    assert q1 == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)', q1
    assert q2 == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)', q2

# Generated at 2022-06-14 17:33:29.684284
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:33:30.737573
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:33:40.503721
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('udn')
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:33:46.001038
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    #assert ie._VALID_URL == r'https?:(//video\.udn\.com/(?:embed|play)/news/)(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'(//video\.udn\.com/(?:embed|play)/news/)(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:33:48.872680
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:36:37.341972
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
  instance = UDNEmbedIE()
  assert instance._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
  assert instance._VALID_URL == r'https?:' + instance._PROTOCOL_RELATIVE_VALID_URL
  assert instance._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
  assert instance._TESTS[0]['info_dict']['id'] == '300040'
  assert instance._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:36:41.408331
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import warnings
    warnings.simplefilter("ignore", DeprecationWarning)
    parsers.UDNEmbedIE()
    warnings.simplefilter("default", DeprecationWarning)

# Unit Test for _real_extract() of class UDNEmbedIE

# Generated at 2022-06-14 17:36:48.720073
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:36:58.120064
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "http://video.udn.com/embed/news/300040"
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'UDN'
    assert ie.IE_DESC == '聯合影音'
    pattern = ie._PROTOCOL_RELATIVE_VALID_URL
    assert pattern == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    _VALID_URL = r'https?:' + pattern
    assert _VALID_URL == url
