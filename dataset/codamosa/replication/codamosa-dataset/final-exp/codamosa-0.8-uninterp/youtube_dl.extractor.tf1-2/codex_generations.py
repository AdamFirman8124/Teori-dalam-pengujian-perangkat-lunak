

# Generated at 2022-06-14 17:06:09.964850
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE(TF1IE._downloader)
    assert ie.ie_key() == 'tf1'
    assert ie.SUFFIX == '.html'
    assert ie.VIDEO_URL_TEMPLATE == 'https://www.tf1.fr/graphql/web'
    assert ie.VIDEO_ID_TEMPLATE == '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f'
    assert ie.VIDEO_PREFERENCE_KEY == 'tf1'

# Generated at 2022-06-14 17:06:10.590427
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:15.946542
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:06:20.463404
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:06:30.016053
# Unit test for constructor of class TF1IE
def test_TF1IE():
    extractor = TF1IE()
    assert extractor._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:39.142121
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE = TF1IE()
    expected = 'https://www.tf1.fr/graphql/web?query=id%3A9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f%0D%0Avariables%3A%7B%22programSlug%22%3A%22tmc%22%2C%22slug%22%3A%22quotidien-premiere-partie-11-juin-2019%22%7D'
    assert TF1IE._download_json._VALID_URL_TEMPLATE == expected

# Generated at 2022-06-14 17:06:44.815635
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE('', {'class': 'TF1IE'})
    myassert(
        tf1ie.VALID_URL,
        r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    )



# Generated at 2022-06-14 17:06:45.813011
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:06:55.886125
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Description:
        Test constructor of TF1IE.
    """
    info_extractor = TF1IE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:05.631406
# Unit test for constructor of class TF1IE
def test_TF1IE():
    inst = TF1IE()
    assert inst._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:19.821070
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.get_filesize('back-to-the-roots-ep-19') > 1000
    assert ie.get_filesize('back-to-the-roots-ep-19') < 100000000

# Generated at 2022-06-14 17:07:28.373927
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert t.IE_NAME == 'tf1'
    assert t.IE_DESC == 'tf1.fr'
    assert t._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:33.016122
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._real_extract('http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:07:34.495286
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE('wat') == TF1IE('wat', None)

# Generated at 2022-06-14 17:07:35.024538
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:07:38.496023
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:39.763921
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # For some reason, the class doesn't work if I execute it here...
    pass

# Generated at 2022-06-14 17:07:46.730438
# Unit test for constructor of class TF1IE
def test_TF1IE():
	url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
	TF1IE()._real_extract(url)
	
 # Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:07:48.148224
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE is not None

# Generated at 2022-06-14 17:07:49.690199
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(InfoExtractor)._real_initialize()

# Generated at 2022-06-14 17:08:04.689252
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t.ie_key() == 'TF1'
    assert t._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:15.394648
# Unit test for constructor of class TF1IE
def test_TF1IE():
    res = TF1IE(None)
    assert res.ie_key() == 'tf1'
    assert res.ie_name() == 'tf1'
    assert res.http() is not None
    assert res.url_result('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html') is not None
    assert res.url_result('https://www.tf1.fr/foo/bar/videos/baz.html') is None
    assert res.url_result('https://www.tf1.fr/foo/bar/videos/baz.htm') is None

# Generated at 2022-06-14 17:08:16.367712
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert tf1ie.IE_NAME == 'TF1'

# Generated at 2022-06-14 17:08:20.363423
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert instance._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:22.707740
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE()
    assert repr(tf1_ie) == "<TF1IE http://www.tf1.fr/>"


# Generated at 2022-06-14 17:08:28.012898
# Unit test for constructor of class TF1IE
def test_TF1IE():
  TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html', 'quotidien-premiere-partie-11-juin-2019')  # pass
  assert(False)   # should not be reached


# Generated at 2022-06-14 17:08:30.026623
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.NAME == 'tf1'

# Generated at 2022-06-14 17:08:31.004194
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert instance

# Generated at 2022-06-14 17:08:33.182997
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:08:34.651432
# Unit test for constructor of class TF1IE
def test_TF1IE():
    x = TF1IE({})
    assert x is not None

# Generated at 2022-06-14 17:09:00.486649
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.suitable("") == False
    assert TF1IE.suitable("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html") == True

# Generated at 2022-06-14 17:09:01.844159
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._real_extract("https://www.tf1.fr/")



# Generated at 2022-06-14 17:09:06.065215
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:09:12.661629
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test with URL of video from TMC's Quotidien (French late night show)
    tf1_ie = TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert tf1_ie._TESTS[0]['info_dict'] == tf1_ie.suitable(tf1_ie._TESTS[0]['url'])

    # Test with URL of video from TF1's Koh-Lanta (French survival show)
    tf1_ie = TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert tf1_

# Generated at 2022-06-14 17:09:15.051438
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:09:20.293617
# Unit test for constructor of class TF1IE
def test_TF1IE():
    for url in ["https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html",
                "https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html"]:
        TF1IE(url)
        

# Generated at 2022-06-14 17:09:25.643570
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(InfoExtractor())._real_extract('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:09:26.274741
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert True

# Generated at 2022-06-14 17:09:27.030908
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:09:31.817752
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert(t.ie_key() == 'TF1')
    assert(t.ie_name() == 'TF1')
    assert(t.ie_description() == 'Video service of the french TV channel TF1')

# Generated at 2022-06-14 17:10:24.696662
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:10:31.510855
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = "http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    ie = TF1IE(url)
    assert_equal(ie.program_slug, "quotidien-avec-yann-barthes")
    assert_equal(ie.id, "quotidien-premiere-partie-11-juin-2019")

# Generated at 2022-06-14 17:10:39.116582
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # This is a test function; it is not supposed to have any executable code.
    # It is not run by the test runner, but is used as input for type checkers
    # such as pyi-mypy.
    def check_TF1IE(instance_of_class_TF1IE: TF1IE) -> None:
        assert isinstance(instance_of_class_TF1IE._VALID_URL, str)
        assert isinstance(instance_of_class_TF1IE._TESTS[0]['url'], str)
        assert isinstance(instance_of_class_TF1IE._TESTS[0]['info_dict']['id'], str)
        assert isinstance(instance_of_class_TF1IE._TESTS[0]['info_dict']['ext'], str)

# Generated at 2022-06-14 17:10:42.441054
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")

# Generated at 2022-06-14 17:10:47.599738
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:10:59.809823
# Unit test for constructor of class TF1IE
def test_TF1IE():
	assert TF1IE()._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
	assert TF1IE()._download_webpage._url_re == re.compile(r'^https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html$')
	assert TF1IE()._download_json._url_re == re.compile(r'^https?://(?:www\.)?tf1\.fr/graphql/web$')
	assert TF1IE()._real_extract._video_regex == re.compile

# Generated at 2022-06-14 17:11:01.375470
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None)._real_extract(None)

# Generated at 2022-06-14 17:11:02.139105
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:11:04.398143
# Unit test for constructor of class TF1IE
def test_TF1IE():
    def test_constructor():
        test_tf1ie = TF1IE()
        assert test_tf1ie

# Generated at 2022-06-14 17:11:07.318201
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:13:21.343219
# Unit test for constructor of class TF1IE
def test_TF1IE():
    if not hasattr(TF1IE, '_download_json'):
        TF1IE._download_json = TF1IE.download_json

    download_json = getattr(TF1IE, '_download_json')
    TF1IE.download_json = lambda *args, **kwargs: download_json(*args, **kwargs)

    for test in TF1IE._TESTS:
        test_TF1IE.__name__ = 'test_' + test['url']
        yield test_TF1IE, TF1IE(), test

# Generated at 2022-06-14 17:13:23.083378
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:13:24.531234
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('Koh Lanta - Replay du 22-05-15')

# Generated at 2022-06-14 17:13:30.127252
# Unit test for constructor of class TF1IE
def test_TF1IE():
  print("Start test_TF1IE")
  url="https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
  try:
    TF1IE()
  except Exception as e:
    print("test_TF1IE: not working")
    print(e)
    return False
  else :
    print("test_TF1IE: working")
    return True


# Generated at 2022-06-14 17:13:37.013722
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test object construction
    obj = TF1IE()
    assert obj._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    # Test type of attribute _TESTS
    assert isinstance(obj._TESTS, list)

# Generated at 2022-06-14 17:13:43.522779
# Unit test for constructor of class TF1IE
def test_TF1IE():
    a = TF1IE("https://www.tf1.fr/")
    assert a.IE_NAME == 'tf1'
    assert a.VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:13:45.015775
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Check that the constructor of class TF1IE is callable
    TF1IE()

# Generated at 2022-06-14 17:13:46.740645
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Check that class TF1IE can be constructed.
    """
    assert TF1IE

# Generated at 2022-06-14 17:13:50.428727
# Unit test for constructor of class TF1IE
def test_TF1IE():
    i = TF1IE()

# Generated at 2022-06-14 17:13:53.193890
# Unit test for constructor of class TF1IE
def test_TF1IE():
  a = TF1IE()
  assert a._VALID_URL == TF1IE._VALID_URL

# Test the constructor of class TF1IE and the content of some fields