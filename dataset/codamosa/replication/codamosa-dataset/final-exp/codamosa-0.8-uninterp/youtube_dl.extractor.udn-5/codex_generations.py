

# Generated at 2022-06-14 17:27:11.915942
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/embed/news/300040'
    udn_embed_extractor = UDNEmbedIE()

    assert udn_embed_extractor._match_id(url) == '300040'

# Generated at 2022-06-14 17:27:23.725225
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    example_input_1 = '//video.udn.com/embed/news/300040'
    example_input_2 = 'https://video.udn.com/embed/news/300040'

    # case 1: given an input url without protocol ("http://"), 
    # constructor should add "http://" in the front of url (which is the default page protocol)
    assert UDNEmbedIE._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    udn_ie = UDNEmbedIE(example_input_1)
    # class should add "http://" in the front of input url
    assert udn_ie._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:27:33.064831
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    assert udne._VALID_URL is not None
    assert udne._PROTOCOL_RELATIVE_VALID_URL is not None
    assert udne._TESTS is not None
    assert udne.IE_NAME is not None
    assert udne.IE_DESC is not None
    assert udne.ie_key() is not None
    assert udne.extract() is not None
    assert udne._download_webpage() is not None
    assert udne._html_search_regex() is not None
    assert udne._parse_json() is not None
    assert udne._real_extract() is not None
    assert udne._match_id() is not None
    assert udne._sort_form

# Generated at 2022-06-14 17:27:36.519374
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    print(ie)

if __name__ == "__main__":
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:27:47.653505
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """test construct class UDNEmbedIE"""
    udn_embed_ie = UDNEmbedIE()
    url = 'http://video.udn.com/embed/news/300040'
    video_id = udn_embed_ie._match_id(url)
    page = udn_embed_ie._download_webpage(url, video_id)
    options_str = udn_embed_ie._html_search_regex(
        r'var\s+options\s*=\s*([^;]+);', page, 'options')
    trans_options_str = js_to_json(options_str)
    options = udn_embed_ie._parse_json(trans_options_str, 'options', fatal=False) or {}
    if options:
        video_urls = options['video']

# Generated at 2022-06-14 17:27:49.522474
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:27:50.651148
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:27:54.500168
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    assert ie.suitable(url) == True
    assert re.match(ie._VALID_URL, url)
    assert ie.IE_NAME == 'udn'



# Generated at 2022-06-14 17:28:01.037286
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie._html_search_regex( 
            udn_embed_ie._VALID_URL, url, 'id') == '300040'
    assert udn_embed_ie._match_id(url) == '300040'
    assert udn_embed_ie._match_id('abc') is None

# Generated at 2022-06-14 17:28:05.943695
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert 'UDNEmbed' == ie.IE_NAME
    assert '聯合影音' == ie.IE_DESC
    assert ie._VALID_URL
    assert ie._TESTS
    assert ie.SUFFIX

# Generated at 2022-06-14 17:28:20.460264
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('test', 'test')

# Generated at 2022-06-14 17:28:24.939773
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Arrange
    url = 'http://video.udn.com/embed/news/300040'
    class_ = UDNEmbedIE(None)
    # Act
    result = class_._match_id(url)
    # Assert
    assert result == '300040'


# Generated at 2022-06-14 17:28:29.159326
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	from .common import InfoExtractor
	ie = InfoExtractor('UDNEmbedIE',True)
	assert ie.ie_key() == 'UDNEmbedIE'

# Generated at 2022-06-14 17:28:33.244408
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE._match_id(url) == '300040'
    assert UDNEmbedIE._match_id(UDNEmbedIE._VALID_URL) == '300040'

# Generated at 2022-06-14 17:28:35.009810
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('UDNEmbedIE', True)

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:28:47.861189
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?:(//video\.udn\.com/embed/news/|//video\.udn\.com/play/news/)(?P<id>\\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:28:57.462663
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test __init__.py with UDNEmbedIE
    info_dict = {
        'id': '300040',
        'ext': 'mp4',
        'title': '生物老師男變女 全校挺"做自己"',
        'thumbnail': r're:^https?://.*\.jpg$',
    }
    url = 'http://video.udn.com/embed/news/300040'
    url_complex = 'https://video.udn.com/embed/news/300040'
    url_complex_https = 'https://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:29:04.541000
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    """
        UDNEmbedIE.__init__ function test
        """
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == ie.ie_key() == 'UDNEmbedIE'
    assert ie.IE_DESC == ie.ie_key() == '聯合影音'
    assert ie._VALID_URL == ie.ie_key() == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == ie.ie_key() == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:29:07.550945
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnEmbedIE = UDNEmbedIE('test')
    return True

# Generated at 2022-06-14 17:29:10.404847
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    video_url = 'https://video.udn.com/embed/news/200001'
    ie = UDNEmbedIE()
    url_info = ie._real_extract('https://video.udn.com/embed/news/200001')
    assert url_info
    assert url_info['id']
    assert url_info['title']
    assert url_info['formats']
    assert url_info['thumbnail']
    # youtube
    assert ie.suitable('https://video.udn.com/embed/news/1234')

# Generated at 2022-06-14 17:29:41.323886
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    # Search pattern of main method
    pattern = ie._download_webpage.__func__.__code__.co_varnames[1]
    assert pattern == 'note'

# Generated at 2022-06-14 17:29:48.876837
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udnie = UDNEmbedIE()
    # test valid URLs
    valid_urls = [
        '//video.udn.com/embed/news/300040',
        '//video.udn.com/play/news/300040']
    for url in valid_urls:
        assert udnie._PROTOCOL_RELATIVE_VALID_URL == udnie._VALID_URL
        assert udnie._VALID_URL == udnie._TESTS[0]['url']
        assert udnie._TESTS[1]['url'] == udnie._TESTS[2]['url']

        match = udnie._match_id(url)
        assert match == '300040'
        assert isinstance(match, str)

# Generated at 2022-06-14 17:29:54.652561
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert (UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL ==
            r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    assert (UDNEmbedIE._VALID_URL ==
            r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')


# Generated at 2022-06-14 17:30:04.491570
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_ie = UDNEmbedIE()
    # test URL matching
    test_urls = [
        'http://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/news/300040',
        'http://video.udn.com/play/news/300040',
    ]
    for url in test_urls:
        # test URL matching
        mobj = re.match(udn_ie._VALID_URL, url)
        assert mobj is not None
        # test video id extractions
        assert mobj.group('id') == '300040'

# Generated at 2022-06-14 17:30:12.404568
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert udne._match_id == '300040'
    assert udne._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:14.412617
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # TODO:  add testcases
    ie = UDNEmbedIE("https://video.udn.com/embed/news/300040");
    assert ie != None;

# Generated at 2022-06-14 17:30:21.045869
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:30:22.258638
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert True

# Generated at 2022-06-14 17:30:23.917417
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(UDNEmbedIE.ie_key())


# Generated at 2022-06-14 17:30:32.434568
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    _UDNEmbedIE = UDNEmbedIE()
    # Check the constructor of class UDNEmbedIE
    assert _UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    # Check the _real_extract function of class UDNEmbedIE
    url = 'http://video.udn.com/embed/news/300040'
    webpage = _UDNEmbedIE._download_webpage(url, '300040')

# Generated at 2022-06-14 17:31:06.768998
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    match_res = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL.match('//video.udn.com/embed/news/300040')
    assert match_res != None
    assert match_res.group('id') == '300040'

    match_res = UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL.match('//video.udn.com/play/news/300040')
    assert match_res != None
    assert match_res.group('id') == '300040'

# Generated at 2022-06-14 17:31:08.017329
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:31:11.493165
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:31:14.588255
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE(dict())._VALID_URL == UDNEmbedIE._VALID_URL

# Generated at 2022-06-14 17:31:17.063795
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    obj = UDNEmbedIE()

# Generated at 2022-06-14 17:31:21.688106
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert udn._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:31:24.302702
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    url = ie._PROTOCOL_RELATIVE_VALID_URL
    mobj = re.match(ie._VALID_URL, url)
    assert mobj != None

# Generated at 2022-06-14 17:31:33.589793
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    m = ie._PROTOCOL_RELATIVE_VALID_URL.match('//video.udn.com/embed/news/300040')
    assert m and m.group('id') == '300040'

    m = ie._PROTOCOL_RELATIVE_VALID_URL.match('//video.udn.com/play/news/300040')
    assert m and m.group('id') == '300040'

    m = ie._VALID_URL.match('http://video.udn.com/embed/news/300040')
    assert m and m.group('id') == '300040'

# Generated at 2022-06-14 17:31:35.375975
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:31:38.788635
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE.IE_NAME == 'udn'
    assert UDNEmbedIE.IE_DESC == '聯合影音'
    assert UDNEmbedIE._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL


# Generated at 2022-06-14 17:32:56.794565
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    url = 'http://video.udn.com/embed/news/300040'
    udn_html = udn._download_webpage(url, '300040')

    options_str = udn._html_search_regex(
        r'var\s+options\s*=\s*([^;]+);', udn_html, 'options')
    trans_options_str = js_to_json(options_str)
    options = udn._parse_json(trans_options_str, 'options', fatal=False) or {}
    if options:
        video_urls = options['video']
        title = options['title']

# Generated at 2022-06-14 17:32:59.943980
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert(ie.IE_DESC == '聯合影音')
    assert(ie._VALID_URL == 'https?:(?://video\.udn\.com/embed/news/(?P<id>\d+)|(?://video\.udn\.com/play/news/(?P<id>\d+)))')

# Generated at 2022-06-14 17:33:02.683827
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert not UDNEmbedIE.IE_DESC.startswith('亞洲視界')
    assert not UDNEmbedIE.IE_DESC.startswith('東森新聞')
    assert UDNEmbedIE.IE_DESC.startswith('聯合影音')

# Generated at 2022-06-14 17:33:10.217784
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'


if __name__ == "__main__":
    import unittest
    unittest.main()

# Generated at 2022-06-14 17:33:11.937169
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ref = UDNEmbedIE()
    assert ref._VALID_URL == r'https?:' + ref._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:33:14.237117
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()


# Generated at 2022-06-14 17:33:15.505872
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert type(UDNEmbedIE()) == UDNEmbedIE


# Generated at 2022-06-14 17:33:19.719404
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed = UDNEmbedIE()
    assert udn_embed.ie_key() == 'udn'

# some test URLs
test_urls = [
    'http://video.udn.com/embed/news/300040',
    'https://video.udn.com/embed/news/300040',
]

# Generated at 2022-06-14 17:33:29.740846
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    import sys
    sys.path.append("..")
    from ytdl.downloader import Downloader
    from ytdl.YoutubeDL import YoutubeDL
    from ytdl.extractor import gen_extractors, youtube

    # get extractors
    list_extractor = [
        {'test': (r'^https?://video\.udn\.com/(?:embed|play)/news/.+$'),
         'class': 'UDNEmbedIE'}
    ]
    list_extractor.extend(gen_extractors())
    list_extractor.extend(youtube.gen_extractors())

    # call constructor
    mydl = Downloader()
    mydl.add_info_extractors(list_extractor)

    # set up options

# Generated at 2022-06-14 17:33:39.011665
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from . import UniTestCase
    import logging

    class TestUDNEmbedIE(UniTestCase):
        def test_init(self):
            m = UDNEmbedIE(UniTestCase.get_test_logger())
            self.assertEqual(m.IE_NAME, 'udn')
            self.assertEqual(m.IE_DESC, '聯合影音')

    # TODO: This will be called automatically when not run as a test
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    logger.debug("test_UDNEmbedIE")
    TestUDNEmbedIE().init()

# Generated at 2022-06-14 17:36:16.405342
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'https://video.udn.com/embed/news/300040'
    udn_ie = UDNEmbedIE()
    got_id = udn_ie._match_id(url)
    assert(got_id == '300040')


# Generated at 2022-06-14 17:36:19.245896
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udna_IE = UDNEmbedIE()
    assert len(udna_IE._TESTS) == 3

# Generated at 2022-06-14 17:36:23.073016
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from youtube_dl.YoutubeDL import YoutubeDL
    ytdl = YoutubeDL({'verbose': True})
    url = 'https://video.udn.com/embed/news/300040'
    ytdl.download([url])


# Generated at 2022-06-14 17:36:29.160549
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne_ie = UDNEmbedIE()
    assert udne_ie.IE_DESC == '聯合影音'
    assert udne_ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:36:36.706345
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udne = UDNEmbedIE()
    # testing url_result
    url = 'https://video.udn.com/play/news/303776'
    video_url = 'https://www.youtube.com/v/zDZFcDGpL4U?version=3&autohide=1'
    video_id = 'zDZFcDGpL4U'
    test_dict = {
        'id': video_id,
        'url': video_url,
        'ie_key': 'Youtube',
    }
    assert test_dict == udne.url_result(url, ie='Youtube', video_id=video_id).__dict__

# Generated at 2022-06-14 17:36:47.254530
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:36:48.570202
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    u = UDNEmbedIE()
    assert isinstance(u, UDNEmbedIE)

# Generated at 2022-06-14 17:36:52.303579
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    obj = UDNEmbedIE()
    obj2 = InfoExtractor(obj.suitable(url), url)

    assert obj is obj2
    assert obj.IE_DESC == obj2.IE_DESC
    assert obj.IE_NAME == obj2.IE_NAME

# Generated at 2022-06-14 17:36:56.178998
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    unit_test_UDNEmbedIE = UDNEmbedIE()
    assert unit_test_UDNEmbedIE.ie_key() == 'UDNEmbed'
    assert unit_test_UDNEmbedIE.ie_desc() == '聯合影音'