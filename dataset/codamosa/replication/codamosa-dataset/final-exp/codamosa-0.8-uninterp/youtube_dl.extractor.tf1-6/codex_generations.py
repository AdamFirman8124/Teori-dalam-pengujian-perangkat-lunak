

# Generated at 2022-06-14 17:06:02.169256
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:02.759446
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:12.116469
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .test_common import TESTS

    with TESTS.get_test_data_path('tf1.html') as test_file:
        test_file = open(test_file, 'r')
        test_content = test_file.read()
        test_content = test_content.encode('utf-8')
        test_file.close()
        TF1IE('wat', '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f', test_content)


if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:06:16.316990
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:18.753715
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test constructor of class TF1IE
    :return:
    """
    extractor = TF1IE()
    assert isinstance(extractor, TF1IE)


# Generated at 2022-06-14 17:06:25.346352
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Unit test for constructor of class TF1IE"""
    url = 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    assert TF1IE._valid_url(url, 'TF1IE') is True
    assert TF1IE._valid_url("https://tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html", 'TF1IE') is True
    assert TF1IE._valid_url("http://tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html", 'TF1IE') is True

# Generated at 2022-06-14 17:06:29.744946
# Unit test for constructor of class TF1IE
def test_TF1IE():
    name = 'TF1IE'
    test_class = TF1IE
    # The instance of TF1IE should have attribute '_VALID_URL'
    assert hasattr(test_class, '_VALID_URL')
    # The attribute '_VALID_URL' of TF1IE should be a string
    assert type(test_class._VALID_URL) is str
    # The instance of TF1IE should have attribute '_TESTS'
    assert hasattr(test_class, '_TESTS')
    # The attribute '_TESTS' of TF1IE should be a list
    assert type(test_class._TESTS) is list
    # The instance of TF1IE should have attribute '_download'
    assert hasattr(test_class, '_download')
    # The attribute '_download' of TF1

# Generated at 2022-06-14 17:06:30.387169
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:06:32.428122
# Unit test for constructor of class TF1IE
def test_TF1IE():
    f1 = TF1IE()
    assert f1 is not None
    assert f1.IE_NAME

# Generated at 2022-06-14 17:06:33.908327
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert isinstance(IE, TF1IE)

# Generated at 2022-06-14 17:06:49.546416
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test constructor for class TF1IE
    # Test case 1: url: https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html
    # Test case 2: url: http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html
    downloader = InfoExtractor()
    assert downloader.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert downloader.suitable('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:06:54.248040
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')



# Generated at 2022-06-14 17:06:58.854981
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.IE_NAME == 'TF1'
    assert tf1.IE_DESC == 'tf1.fr videos'
    assert tf1.VALID_URL == TF1IE._VALID_URL
    assert tf1.TEST == TF1IE._TESTS

# Generated at 2022-06-14 17:07:04.241644
# Unit test for constructor of class TF1IE
def test_TF1IE():
	tf1 = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
	assert tf1._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:07.042275
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    return

# Generated at 2022-06-14 17:07:11.700927
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test the constructor of class TF1IE
    """
    ie = TF1IE()
    assert ie._VALID_URL

    # Test the regex
    assert re.match(ie._VALID_URL, ie._TESTS[0]['url'])

# Generated at 2022-06-14 17:07:18.461883
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    res = ie.extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert res['id'] == '13641379'

# Generated at 2022-06-14 17:07:26.819680
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # "1" is used as the identifier for this test
    t = TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")
    assert t.SUFFIX == ""
    assert t.THUMB_SUFFIX == ""
    assert t.ie_key() == 'TF1'
    assert t.video_id == "1"
    assert t.url == "http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html"
    assert t._type == "url"
    assert t.query["url"] == t.url



# Generated at 2022-06-14 17:07:27.635521
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()



# Generated at 2022-06-14 17:07:29.623944
# Unit test for constructor of class TF1IE
def test_TF1IE():
    v = TF1IE()
    assert v and v.name

# Generated at 2022-06-14 17:07:42.878585
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf = TF1IE()
    assert tf

# Generated at 2022-06-14 17:07:44.293603
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE()

# Generated at 2022-06-14 17:07:45.705967
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()

# Generated at 2022-06-14 17:07:48.466242
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test constructor of class TF1IE
    x = TF1IE()

# Generated at 2022-06-14 17:07:57.617944
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert tf1ie.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert not tf1ie.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert not tf1ie.suitable('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:07:58.435518
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()

# Generated at 2022-06-14 17:07:59.659044
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('TF1IE')

# Generated at 2022-06-14 17:08:01.239496
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.ie_key() == "TF1"

# Generated at 2022-06-14 17:08:03.203710
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE()
    if obj:
        raise Exception("Unit test failed. Object should be None")

# Generated at 2022-06-14 17:08:04.114040
# Unit test for constructor of class TF1IE
def test_TF1IE():
    _ = TF1IE(None, {}, {})

# Generated at 2022-06-14 17:08:25.648294
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE("TF1IE")

# Generated at 2022-06-14 17:08:35.728244
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:42.801262
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Wrong url format to test the __init__ method
    with pytest.raises(ValueError, match=r'Invalid URL.*'):
        TF1IE('http://tf1.com')
    # Good url format to test the __init__ method
    assert TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:08:45.605099
# Unit test for constructor of class TF1IE
def test_TF1IE():
    global TEST_URL, TF1IE
    info = TF1IE.suitable(TEST_URL)
    assert info == 'TF1IE'

# Generated at 2022-06-14 17:08:47.990646
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t1v = TF1IE()
    assert t1v.ie_key() == 'tf1'
    assert t1v.ie_desc() == 'TF1'

# Generated at 2022-06-14 17:08:57.757201
# Unit test for constructor of class TF1IE
def test_TF1IE():
    _TRANSFORM = {
        'name': 'tf1',
        'params': {
            'id': '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f',
            'variables': {
                'programSlug': 'quotidien-avec-yann-barthes',
                'slug': 'quotidien-premiere-partie-11-juin-2019',
            },
        },
    }


# Generated at 2022-06-14 17:09:08.682943
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    # Regular expression used to match URL in this extractor
    assert tf1._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    # Predefined lists for this extractor

# Generated at 2022-06-14 17:09:14.057089
# Unit test for constructor of class TF1IE
def test_TF1IE():
    inst = TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert inst.url == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'

# Generated at 2022-06-14 17:09:15.839660
# Unit test for constructor of class TF1IE
def test_TF1IE():
    wat_id = '13641377'
    TF1IE(1).get_info(wat_id)

# Generated at 2022-06-14 17:09:17.115299
# Unit test for constructor of class TF1IE
def test_TF1IE():
    o = TF1IE()

# Generated at 2022-06-14 17:10:05.926037
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.suitable("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
test_TF1IE()

# Generated at 2022-06-14 17:10:07.983935
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:10:10.489020
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE()
        assert False, "An exception should have been thrown"
    except TypeError as e:
        assert str(e) == 'This class must be sub-classed by an IE', "The error message is incorrect"

# Generated at 2022-06-14 17:10:11.273531
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('re', 'play')

# Generated at 2022-06-14 17:10:23.500194
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test with the url of a video
    url = 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html'
    tf1IE = TF1IE(url)
    # Assert the media is a video
    assert tf1IE.MEDIA_TYPES == [ 'video' ]
    # Assert the media is not a playlist
    assert tf1IE.IS_PLAYLIST == False
    # Assert the ie key is wat
    assert tf1IE._ie_key() == 'wat'
    # Assert the class name is TF1IE
    assert tf1IE.__class__.__name__ == 'TF1IE'
    # Assert the _VALID_URL is defined
    assert tf1IE._VALID_URL is not None

# Unit test

# Generated at 2022-06-14 17:10:30.510064
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert tf1.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert not tf1.suitable('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:10:33.905738
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE()
    assert tf1_ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'


# Generated at 2022-06-14 17:10:34.755249
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()

# Generated at 2022-06-14 17:10:37.517321
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert tf1ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:10:41.701014
# Unit test for constructor of class TF1IE
def test_TF1IE():
  instance = TF1IE()
  assert(instance._VALID_URL.find("https") != -1)

# Generated at 2022-06-14 17:12:42.877161
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()


# Generated at 2022-06-14 17:12:51.235258
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    # Check that TF1IE is initialized with the correct video id: 13641379
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')._real_extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')['_type'] == 'url_transparent'

# Generated at 2022-06-14 17:12:52.616572
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE(None)
    assert obj != None

# Generated at 2022-06-14 17:12:55.860386
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test class TF1IE"""
    print("\nTesting test_TF1IE")
    test_tf1 = TF1IE()
    print("Succesfully iniated test_TF1IE")



# Generated at 2022-06-14 17:13:02.591766
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info_extractor = TF1IE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:13:04.483225
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()

# Generated at 2022-06-14 17:13:05.742764
# Unit test for constructor of class TF1IE
def test_TF1IE():
    _ = TF1IE(InfoExtractor)

# Generated at 2022-06-14 17:13:06.303839
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:13:06.925149
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t != None

# Generated at 2022-06-14 17:13:15.822558
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    unit test to test the constructor and attributes of class TF1IE
    """
    inst = TF1IE()
    assert inst._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert inst._downloader == None
    assert inst._match_id == {'program_slug': '1', 'id': '2'}
    assert inst._download_webpage_handle == None
    assert inst._download_webpage == None
    assert inst._download_json == None
    assert inst._download_xml == None
    assert inst._html_search_meta == None
    assert inst._html_search_regex == None
    assert inst._search_re

# Generated at 2022-06-14 17:14:40.200035
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test if all expected infomation is found, also test if the constructor of InfoExtractor class can
    # instantiate an object of TF1IE class
    return TF1IE().extract(r'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:14:41.346963
# Unit test for constructor of class TF1IE
def test_TF1IE():
    #TODO: implement it
    assert False

# Generated at 2022-06-14 17:14:49.076674
# Unit test for constructor of class TF1IE
def test_TF1IE():
    str = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    obj = TF1IE(str)

# Generated at 2022-06-14 17:14:51.032387
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE()
    except:
        assert False
    else:
        assert True

# Generated at 2022-06-14 17:14:51.568426
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:14:54.562794
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    TF1IE()(url)

# Generated at 2022-06-14 17:15:05.562828
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE()
    assert tf1_ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:15:07.341809
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1 is not None

# Generated at 2022-06-14 17:15:08.152217
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert(True)

# Generated at 2022-06-14 17:15:11.768968
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(InfoExtractor())("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")