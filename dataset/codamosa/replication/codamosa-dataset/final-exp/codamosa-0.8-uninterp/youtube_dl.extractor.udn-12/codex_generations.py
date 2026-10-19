

# Generated at 2022-06-14 17:27:15.169510
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn_embed'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['title'] == '生物老師男變女 全校挺"做自己"'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:27:19.709420
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie_UDNEmbed = UDNEmbedIE()
    assert ie_UDNEmbed.IE_NAME == 'udn'
    assert ie_UDNEmbed.IE_DESC == '聯合影音'
    assert ie_UDNEmbed._VALID_URL == 'https?://video.udn.com/(?:embed|play)/news/(?P<id>\\d+)'

# Generated at 2022-06-14 17:27:22.860459
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE(None)
    assert ie.IE_NAME == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:27:35.267146
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    IE = UDNEmbedIE()
    assert(IE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    assert(IE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)')
    assert(IE._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040')
    assert(IE._TESTS[0]['info_dict']['id'] == '300040')
    assert(IE._TESTS[1]['url'] == 'https://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:27:46.626024
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    u = UDNEmbedIE()
    assert (u.IE_NAME == 'udn_embed')
    assert (u.IE_DESC == '聯合影音')
    assert (u._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)')
    assert (u._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)')

# Generated at 2022-06-14 17:27:56.820158
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:28:05.772189
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    # assert part
    # test video_id extraction
    assert udn_embed_ie._match_id(
        '//video.udn.com/embed/news/300040') == '300040'
    assert udn_embed_ie._match_id(
        'https://video.udn.com/play/news/300040') == '300040'
    assert udn_embed_ie._match_id(
        'http://video.udn.com/embed/news/300040') == '300040'
    assert udn_embed_ie._match_id(
        'http://video.udn.com/play/news/300040') == '300040'

# Generated at 2022-06-14 17:28:09.922067
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Test normal usage
    UDNEmbedIE()._real_extract(
        'http://video.udn.com/embed/news/300040')
    # Test no constructor args
    UDNEmbedIE()

# Generated at 2022-06-14 17:28:11.129259
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:21.424342
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE.IE_DESC == '聯合影音'
    assert UDNEmbedIE._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:37.037791
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()

    assert ie._VALID_URL == r'https?:(//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+))'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'

# Generated at 2022-06-14 17:28:39.644702
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    print(ie)

# Generated at 2022-06-14 17:28:51.421060
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:28:52.404296
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(downloader=None)

# Generated at 2022-06-14 17:29:00.637889
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    This test case tests __init__ function of class UDNEmbedIE.
    It calls __init__ function and checks if it can save value introduced by user
    and the value is passed to InfoExtractor.
    """
    site_dict = {}
    site_dict['CHANNEL_NAME'] = 'udn'
    site_dict['CHANNEL_URL'] = 'https://video.udn.com'
    site_dict['CHANNEL_LINK'] = 'https://video.udn.com/'
    site_dict['CHANNEL_DESC'] = '聯合影音'
    site_dict['CHANNEL_ID'] = 'udn'

    udn_embed = UDNEmbedIE(site_dict)

    assert udn_embed._site == 'udn'

# Generated at 2022-06-14 17:29:03.684698
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    url = ie._url_reverse('300040')

    assert ie._real_initialize(url)


if __name__ == '__main__':
    pass

# Generated at 2022-06-14 17:29:11.947942
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test constructor of class UDNEmbedIE and test protected methods."""
    url_list = [
        'http://video.udn.com/embed/news/300040',
        'https://video.udn.com/embed/news/300040',
        'https://video.udn.com/play/news/303776',
    ]

# Generated at 2022-06-14 17:29:14.413479
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    if obj.IE_DESC.find('聯合影音') == -1:
        print('error in IE_DESC of UDNEmbedIE')

# Generated at 2022-06-14 17:29:16.445112
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None)

# Generated at 2022-06-14 17:29:24.294221
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbed_instance = UDNEmbedIE()
    assert UDNEmbed_instance._PROTOCOL_RELATIVE_VALID_URL == \
        r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbed_instance._VALID_URL == r'https?:' + \
        r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbed_instance.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:29:41.230734
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """ test code for class UDNEmbedIE """

    UDNEmbedIE("https://video.udn.com/embed/news/300040")

# test for function _real_extract()

# Generated at 2022-06-14 17:29:46.232032
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:29:53.070859
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # input: url
    # output: none
    # test: parameter URL is valid or not
    if __name__ == "__main__":
        try:
            UDNEmbedIE('http://video.udn.com/embed/news/300040')
        except:
            print("constructor of UDNEmbedIE class is not working")

    return None


# Generated at 2022-06-14 17:29:57.045628
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    i = UDNEmbedIE()
    assert i.IE_NAME == "udn.com:embed"
    assert i.IE_DESC == "聯合影音"
    assert i._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:30:01.116018
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE("http://video.udn.com/embed/news/300040")
    assert(ie.ie_key() == "UDNEmbed")
    assert(ie.ie_desc() == "聯合影音")


# Generated at 2022-06-14 17:30:08.552801
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.IE_NAME == 'udn'
    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_ie._VALID_URL == 'https?:' + UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:30:21.045779
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    i = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert i._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert i._VALID_URL == r'https?:' + i._PROTOCOL_RELATIVE_VALID_URL
    assert i._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert i._TESTS[0]['info_dict']['id'] == '300040'
    assert 'http://video.udn.com/embed/news/300040' == i._TESTS[0]['info_dict']['ext']
    assert i._

# Generated at 2022-06-14 17:30:24.687612
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "https://video.udn.com/embed/news/300040"
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:30:28.222433
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	test_UDNEmbed = 'https://video.udn.com/embed/news/300040'
	x = UDNEmbedIE()
	assert(x.suitable(test_UDNEmbed) == True)
	assert(x.IE_DESC == '聯合影音')

# Generated at 2022-06-14 17:30:38.294863
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.Udn import Udne

    ydl = YoutubeDL({})

    # Check for expected errors on invalid URLs
    for url in [
            # No match for this url
            'https://video.udn.com/',
            # Invalid video id
            'http://video.udn.com/embed/news/xxx',
    ]:
        assert not ydl.extract_info(url, download=False)

    # Check that YoutubeDL's extractors list is uptodate
    youtube_ie = ydl.get_info_extractor('Youtube')
    udn_ie = ydl.get_info_extractor('Udn')
    assert udn_ie.IE_DESC in youtube_ie._WORKING_IE_DESC

# Generated at 2022-06-14 17:31:03.835877
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE == type(UDNEmbedIE({}))

# Generated at 2022-06-14 17:31:11.873783
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    _test_UDNEmbedIE = UDNEmbedIE().match(
        'https://video.udn.com/embed/news/300040')
    assert _test_UDNEmbedIE(
        'https://video.udn.com/embed/news/300040')
    # Test if _PROTOCOL_RELATIVE_VALID_URL doesn't work
    # without 'https?'
    assert not UDNEmbedIE().match('//video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:31:16.530012
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert UDNEmbedIE._TESTS[0]['info_dict'] == udn._real_extract(UDNEmbedIE._TESTS[0]['url'])

# Generated at 2022-06-14 17:31:18.709815
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('http://video.udn.com/embed/news/300040')

# Generated at 2022-06-14 17:31:23.072110
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()
    UDNEmbedIE('http://video.udn.com/embed/news/300040')
    UDNEmbedIE('http://video.udn.com/play/news/300040')

# Generated at 2022-06-14 17:31:33.953112
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert udn_embed_ie.is_match('http://video.udn.com/embed/news/300040')
    assert udn_embed_ie.is_match('http://video.udn.com/play/news/300040')
    assert udn_embed_ie.is_match('//video.udn.com/embed/news/300040')
    assert not udn_embed_ie.is_match('http://video.udn.com/embed/news/300040?no')
    assert not udn_embed_ie.is_match('http://video.udn.com/embed/news/300040#')

# Generated at 2022-06-14 17:31:35.304146
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # This should not raise any exception
    UDNEmbedIE()

# Generated at 2022-06-14 17:31:40.828472
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    urls = {
        'video.udn.com/embed/news/300040': '300040',
        'video.udn.com/play/news/300040': '300040',
        'www.youtube.com/watch?v=mEihiNIW8eU': 'mEihiNIW8eU',
    }
    for url, expect_id in urls.items():
        ie = UDNEmbedIE(url)
        try:
            assert ie.video_id == expect_id
        except AssertionError:
            print('video id of %s is not %s' % (url, expect_id))

# Generated at 2022-06-14 17:31:43.858142
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('http://video.udn.com/embed/news/300040')
    assert ie == globals()['UDNEmbedIE']

# Generated at 2022-06-14 17:31:53.053301
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE("http://video.udn.com/embed/news/300040")
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[0]['info_dict']['id'] == '300040'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:33:06.920958
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Test for instantiation of class UDNEmbedIE"""
    ie = UDNEmbedIE()
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:33:11.242585
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # url = 'http://video.udn.com/embed/news/59965'
    # url = 'https://video.udn.com/embed/news/59965'
    url = 'http://video.udn.com/embed/news/59965'
    UDNEmbedIE(url).extract()

# Generated at 2022-06-14 17:33:12.189044
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    assert obj.IE_NAME == 'udn'

# Generated at 2022-06-14 17:33:23.311871
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert udn._VALID_URL == "https?://video\.udn\.com/(?:embed|play)/(?P<id>[0-9]{4,})"
    assert udn._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert udn._TESTS[0]['info_dict']['id'] == '300040'
    assert udn._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert udn._TESTS[0]['info_dict']['title'] == '生物老師男變女 全校挺"做自己"'
    assert udn._TES

# Generated at 2022-06-14 17:33:25.762340
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:33:33.667571
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import InfoExtractor as IE
    from .common import ExtractorError

    # Assert that the specified regular expression is used.
    try:
        IE('UDNEmbedIE', 'http://video.udn.com/embed/news/xxx')
    except ExtractorError:
        pass
    else:
        assert False, 'AssertionError: ExtractorError is not raised by UDNEmbedIE.'


# Generated at 2022-06-14 17:33:44.840115
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from .common import InfoExtractor
    from chardet import detect
    import os.path
    import os

    def read_text_file(filename):
        dirname = os.path.dirname(__file__)
        file_path = os.path.join(dirname, filename)
        with open(file_path, 'r') as f:
            encoding = detect(f.read())['encoding']
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()

    class MockYoutubeDL(object):
        def __init__(self, ie):
            self.ie = ie
        def extract_info(self, url, download=True):
            return self.ie._real_extract(url)
        def prepare_filename(self, info_dict):
            return

# Generated at 2022-06-14 17:33:51.159138
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_url = 'https://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    assert ie._match_id(test_url) == '300040'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:33:52.448448
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:34:00.933447
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_IE = UDNEmbedIE()
    assert udn_embed_IE.ie_key() == 'udn'
    for regex in udn_embed_IE._VALID_URL:
        assert isinstance(regex, compat_str)
    assert udn_embed_IE.IE_DESC == '聯合影音'
    assert udn_embed_IE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_IE._VALID_URL == r'https?:' + udn_embed_IE._PROTOCOL_RELATIVE_VALID_URL
    assert len(udn_embed_IE._TESTS) > 0

# Generated at 2022-06-14 17:36:37.116838
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    obj = UDNEmbedIE()
    assert obj.ie_key() == 'UDNEmbed'
    # Test the public functions
    fns = ['_real_extract', '_PROTOCOL_RELATIVE_VALID_URL', '_VALID_URL', '_TESTS']
    for fn in fns:
        assert hasattr(obj, fn)



# Generated at 2022-06-14 17:36:40.683287
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE.IE_NAME
    assert UDNEmbedIE.IE_DESC
    assert UDNEmbedIE._VALID_URL
    assert UDNEmbedIE._TESTS

# Generated at 2022-06-14 17:36:41.630256
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:36:51.785374
# Unit test for constructor of class UDNEmbedIE

# Generated at 2022-06-14 17:36:54.845743
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()

    assert udn_embed_ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'