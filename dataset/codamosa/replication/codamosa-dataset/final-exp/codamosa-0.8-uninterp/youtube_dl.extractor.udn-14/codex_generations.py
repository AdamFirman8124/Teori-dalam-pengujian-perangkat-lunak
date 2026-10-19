

# Generated at 2022-06-14 17:27:13.857776
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Test pattern match: Extract video ID

# Generated at 2022-06-14 17:27:15.839880
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    video_url = 'http://video.udn.com/embed/news/300040'
    udne = UDNEmbedIE()
    assert udne._match_id(video_url) == '300040'

# Generated at 2022-06-14 17:27:23.488937
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    '''Test the constructor of the class UDNEmbedIE'''
    udnembed_IE = UDNEmbedIE()

    assert udnembed_IE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udnembed_IE._VALID_URL == r'https?:' + r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'


# Generated at 2022-06-14 17:27:25.820935
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    from inspect import isfunction
    from youtube_dl.extractor import UDNEmbedIE
    assert isfunction(UDNEmbedIE._real_extract)

# Generated at 2022-06-14 17:27:34.619608
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    test_url = 'http://video.udn.com/embed/news/300040'
    res = ie._real_extract(test_url)
    assert res['id'] == '300040'
    assert res['title'] == '生物老師男變女 全校挺"做自己"'
    assert re.match(r'https?://.*\.jpg$', res['thumbnail']) is not None
    assert len(res['formats']) == 5

# Generated at 2022-06-14 17:27:38.602939
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    result = UDNEmbedIE().result()
    assert len(result)
    assert len(result[0])
    assert len(result[0][1])

if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:27:41.933346
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

# Generated at 2022-06-14 17:27:53.422761
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = "https://video.udn.com/embed/news/300040"

    # Option a: Using custom created instance
    udn_ie = UDNEmbedIE()
    info_dict = udn_ie._real_extract(url)
    assert info_dict['id'] == '300040'
    assert info_dict['title'] == '生物老師男變女 全校挺"做自己"'

    # Option b: Using YoutubeDL's internal instance
    from youtube_dl import YoutubeDL
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    info_dict = ydl.extract_info(url, download=False)
    assert info_dict['id'] == '300040'
    assert info

# Generated at 2022-06-14 17:27:54.528628
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:28:04.485525
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Arrange
    url = "https://video.udn.com/embed/news/300040"
    # Act
    result = UDNEmbedIE()
    # Assert
    assert isinstance(result, InfoExtractor)
    assert result._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert result._VALID_URL == r'https?:' + result._PROTOCOL_RELATIVE_VALID_URL
    assert result._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert result._TESTS[0]['info_dict']['id'] == '300040'

# Generated at 2022-06-14 17:28:19.893651
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """
    Refer to https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py
    """
    import youtube_dl
    ydl = youtube_dl.YoutubeDL({'verbose': False,
                                'forceurl': True,
                                'forcetitle': True,
                                'forcejson': True,
                                })
    ie = ydl.extract_info(
        'http://video.udn.com/embed/news/300040',
        download=False
    )
    # test if url has been normalized
    assert ie['url'] == 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:28:24.818083
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.suitable('http://video.udn.com/embed/news/300040')
    assert ie.suitable('https://video.udn.com/embed/news/300040')
    assert not ie.suitable('https://video.udn.com/news/300040')

# Generated at 2022-06-14 17:28:28.060939
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert(isinstance(UDNEmbedIE(None)._PROTOCOL_RELATIVE_VALID_URL, str))

# Generated at 2022-06-14 17:28:32.565586
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print ("test_UDNEmbedIE")
    if __name__ == '__main__':
        exit(test_UDNEmbedIE())

# Generated at 2022-06-14 17:28:37.842993
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE()._VALID_URL == UDNEmbedIE._VALID_URL
    assert UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL == UDNEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert UDNEmbedIE().IE_DESC == UDNEmbedIE.IE_DESC
    assert UDNEmbedIE()._TESTS == UDNEmbedIE._TESTS

# Generated at 2022-06-14 17:28:49.422641
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.IE_NAME == 'udn'
    assert udn_embed_ie.IE_DESC == '聯合影音'
    assert udn_embed_ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert udn_embed_ie._TESTS[-1]['url'] == 'https://video.udn.com/play/news/303776'
    assert udn_embed_ie._T

# Generated at 2022-06-14 17:29:01.240151
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    result = UDNEmbedIE()._PROTOCOL_RELATIVE_VALID_URL
    verifier = re.compile(r'^//video\.udn\.com/embed/news/(?P<id>\d+)$')
    assert verifier.match(result) is not None
    assert verifier.match('//video.udn.com/embed/news/300040') is not None
    assert verifier.match('//video.udn.com/embed/news/300040aaa') is None
    assert verifier.match('http://video.udn.com/embed/news/300040') is None
    assert verifier.match('https://video.udn.com/embed/news/300040') is None

# Generated at 2022-06-14 17:29:14.230789
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
	from ..utils import ExtractorError

	ie = UDNEmbedIE()
	try:
		ie.get_info(url=None, ie_key=None, downloader=None, fatal=True)
	except ExtractorError as e:
		assert e.msg == 'URL must be specified'
	try:
		ie.get_info(url='', ie_key=None, downloader=None, fatal=True)
	except ExtractorError as e:
		assert e.msg == 'URL must be specified'
	try:
		ie.get_info(url='foo', ie_key=None, downloader=None, fatal=True)
	except ExtractorError as e:
		assert e.msg == 'Invalid URL foo'

# Generated at 2022-06-14 17:29:20.237443
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    test_cases = ['http://video.udn.com/embed/news/300040',
                  'https://video.udn.com/embed/news/300040',
                  '//video.udn.com/embed/news/300040']
    for case in test_cases:
        ie._real_extract(case)



# Generated at 2022-06-14 17:29:28.046706
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_cases=[
        ({'url': 'http://video.udn.com/embed/news/300040'},'UDNEmbedIE'),
        ({'url': 'https://video.udn.com/embed/news/300040'},'UDNEmbedIE'),
        ({'url': 'https://video.udn.com/play/news/303776'},'UDNEmbedIE'),
        ]
    for test_data in test_cases:
        udl=UDNEmbedIE()
        [id,expected]=list(test_data.values())
        assert(udl._match_id(id)==expected)

# Generated at 2022-06-14 17:29:50.866027
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test class of UDNEmbedIE
    # test for constructor
    udn_ie = UDNEmbedIE()
    if udn_ie.IE_DESC != '聯合影音' :
        print('IE_DESC mismatch: expected: ' + '聯合影音' + ' , but get ' + udn_ie.IE_DESC)

# Generated at 2022-06-14 17:29:53.122534
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    try:
        UDNEmbedIE()
    except Exception as e:
        assert False, "UDNEmbedIE constructor failed."

# Generated at 2022-06-14 17:29:54.463048
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie



# Generated at 2022-06-14 17:29:58.510944
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    embed_ie = UDNEmbedIE()
    embed_ie._match_id('//video.udn.com/embed/news/300040') == '300040'

# Generated at 2022-06-14 17:30:05.174912
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('www')
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.ie_key() == 'UDNEmbed'
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:30:16.874290
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    constructor_test(
        UDNEmbedIE,
        [
            # Valid URL
            "http://video.udn.com/embed/news/300040",
            "https://video.udn.com/embed/news/300040"
        ],
        # Invalid URL
        [
            "http://video.udn.com/blah/news/300040",
            "https://video.udn.com/embed/news/300040",
            "https://video.udn.com/embed/news/300040/blah"
        ],
        {
            # Constructor should not accept the URL
            "https://video.udn.com/embed/news/300040/blah" : False
        }
    )


# Generated at 2022-06-14 17:30:18.509105
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE(None).get_urls_from_webpage(None)

# Generated at 2022-06-14 17:30:24.097715
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    """Run unit test for UDNEmbedIE"""
    url = 'https://video.udn.com/embed/news/300040'
    ie = UDNEmbedIE()
    json = ie.extract(url)
    assert json['id'] == '300040'
    assert json['title'] == '生物老師男變女 全校挺"做自己"'
    assert json['thumbnail'] is not None

# Generated at 2022-06-14 17:30:30.968131
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert UDNEmbedIE.suitable("http://video.udn.com/embed/news/300040") == True
    assert UDNEmbedIE.suitable("https://video.udn.com/play/news/303776") == True
    assert UDNEmbedIE.suitable("https://video.udn.com/embed/news/300040") == True
    assert UDNEmbedIE.suitable("https://video.udn.com/embed/news/") == False
    assert UDNEmbedIE.suitable("https://video.udn.com/play/news/") == False

# Generated at 2022-06-14 17:30:33.219441
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'
    UDNEmbedIE()._real_extract(url)

# Generated at 2022-06-14 17:31:06.493851
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test constructing of class UDNEmbedIE
    udnEmbedIE = UDNEmbedIE()

    # test _PROTOCOL_RELATIVE_VALID_URL
    assert udnEmbedIE._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'

    # test _VALID_URL, should be r'https?:' + udnEmbedIE._PROTOCOL_RELATIVE_VALID_URL
    assert udnEmbedIE._VALID_URL == r'https?:' + udnEmbedIE._PROTOCOL_RELATIVE_VALID_URL

# Generated at 2022-06-14 17:31:16.138085
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn = UDNEmbedIE()
    assert udn.IE_DESC == '聯合影音'
    url = 'http://video.udn.com/embed/news/300040'
    assert udn._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\\d+)'
    assert udn._VALID_URL == 'https?:' + udn._PROTOCOL_RELATIVE_VALID_URL
    assert udn._match_id(url) == '300040'
    #assert udn._real_extract(url)
    #assert udn._download_webpage(url, '300040')


# Generated at 2022-06-14 17:31:17.286368
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    print("Hello World!")

# Generated at 2022-06-14 17:31:19.485417
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE("https://video.udn.com/play/news/303776")

# Generated at 2022-06-14 17:31:26.508185
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():

    # Normal case : there is a valid url.
    url = 'https://video.udn.com/embed/news/300040'
    UDNEmbedIE(url)

    # Exception case : there is NOT a valid url.
    url = 'https://video.udn.com/embed/news/bad_id'
    try :
        UDNEmbedIE(url)
    except KeyError:
        raise Exception('Bad url :(')


# Generated at 2022-06-14 17:31:33.363281
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()

    # Test of _PROTOCOL_RELATIVE_VALID_URL
    url = '//video.udn.com/embed/news/300040'
    match = udn_embed_ie._PROTOCOL_RELATIVE_VALID_URL
    result = re.match(match, url)

    assert result is not None
    assert result.group('id') == '300040'


# Generated at 2022-06-14 17:31:38.921338
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn.com:embed'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert not ie._WORKING

# Generated at 2022-06-14 17:31:41.745368
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.ie_key() == 'udn'
    assert ie.ie_desc() == '聯合影音'

# Generated at 2022-06-14 17:31:47.760636
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
  ie = UDNEmbedIE(None)
  url = 'http://video.udn.com/embed/news/300040'
  mobj = re.match(ie._VALID_URL, url)
  assert ie._real_extract(url) == ie.url_result(url, ie.ie_key())

# Generated at 2022-06-14 17:31:51.541772
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    IE = UDNEmbedIE()

    # Valid URL
    assert IE.suitable('https://video.udn.com/embed/news/300040')

    # Invalid URL
    assert not IE.suitable('https://video.udn.com/abc')

# Generated at 2022-06-14 17:33:14.615455
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # test for _real_extract function
    _real_extract = UDNEmbedIE._real_extract
    print('Unit test for _real_extract function')
    extractor = UDNEmbedIE('http://www.dummy.com', {})
    # test for youtube video
    youtube_url = 'https://www.youtube.com/watch?v=Xy1KowLTxQs'
    video_id = '300040'
    def _download_webpage_for_youtube(url, video_id, note=None, errnote=None):
        assert url == options['video']['youtube']
        return youtube_url
    extractor._download_webpage = _download_webpage_for_youtube

# Generated at 2022-06-14 17:33:17.193085
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'



# Generated at 2022-06-14 17:33:19.397725
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # Valid URL
    assert UDNEmbedIE().working == True
    # Invalid URL
    assert UDNEmbedIE().working == False


# Generated at 2022-06-14 17:33:24.480868
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    udn_embed_ie = UDNEmbedIE()
    assert udn_embed_ie.IE_NAME == 'udn.com:embed'
    assert udn_embed_ie.IE_DESC == '聯合影音'


if __name__ == '__main__':
    test_UDNEmbedIE()

# Generated at 2022-06-14 17:33:33.623555
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie.IE_NAME == 'udn'
    assert ie.IE_DESC == '聯合影音'
    assert ie._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._PROTOCOL_RELATIVE_VALID_URL == '//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'


# Generated at 2022-06-14 17:33:41.494886
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE()
    assert ie._VALID_URL == r'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'http://video.udn.com/embed/news/300040'
    assert ie._TESTS[2]['url'] == 'https://video.udn.com/play/news/303776'

# Generated at 2022-06-14 17:33:44.221865
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE('UDNEmbed',True,True,True)
    UDNEmbedIE('UDNEmbed')
    UDNEmbedIE('UDNEmbed',False,False,False)



# Generated at 2022-06-14 17:33:52.503459
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    ie = UDNEmbedIE('https://video.udn.com/embed/news/300040')
    assert ie._PROTOCOL_RELATIVE_VALID_URL == r'//video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ie._VALID_URL == r'https?:' + ie._PROTOCOL_RELATIVE_VALID_URL
    assert ie.IE_DESC == '聯合影音'

# Generated at 2022-06-14 17:34:04.800150
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    url = 'http://video.udn.com/embed/news/300040'

# Generated at 2022-06-14 17:34:13.659093
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    # instantiate UDNEmbedIE
    ie = UDNEmbedIE()

    # concat url prefix with _PROTOCOL_RELATIVE_VALID_URL
    url = ie._VALID_URL

    # extract video id
    video_id = ie._match_id(url)

    # download webpage
    page = ie._download_webpage(url, video_id)

    # search options
    options_str = ie._html_search_regex(
        # regular expression: var options = xxx;
        r'var\s+options\s*=\s*([^;]+);', page, 'options')

    # json string to json object
    trans_options_str = js_to_json(options_str)

    # parse json string

# Generated at 2022-06-14 17:36:44.753947
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()



# Generated at 2022-06-14 17:36:48.131449
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    assert isinstance(UDNEmbedIE("http://video.udn.com/embed/news/300040"), InfoExtractor)
    assert isinstance(UDNEmbedIE("https://video.udn.com/embed/news/300040"), InfoExtractor)
    assert isinstance(UDNEmbedIE("//video.udn.com/embed/news/300040"), InfoExtractor)

# Generated at 2022-06-14 17:36:48.786918
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    UDNEmbedIE()

# Generated at 2022-06-14 17:37:00.210910
# Unit test for constructor of class UDNEmbedIE
def test_UDNEmbedIE():
    test_UDNEmbedIE_instance = UDNEmbedIE()
    assert test_UDNEmbedIE_instance.IE_DESC == '聯合影音'
    assert test_UDNEmbedIE_instance._VALID_URL == 'https?://video\.udn\.com/(?:embed|play)/news/(?P<id>\d+)'
    assert ('https://video.udn.com/embed/news/300040' ==
            test_UDNEmbedIE_instance._match_id('https://video.udn.com/embed/news/300040'))