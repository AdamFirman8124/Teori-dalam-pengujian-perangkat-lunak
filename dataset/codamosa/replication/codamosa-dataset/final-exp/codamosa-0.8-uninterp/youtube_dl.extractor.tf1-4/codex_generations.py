

# Generated at 2022-06-14 17:06:10.390188
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE('test:test', 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    assert IE.NAME == 'tf1'
    assert bool(IE.IE_NAME) is True
    assert IE.VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert IE._TESTS is not None
    assert IE.br.close() is None


# Generated at 2022-06-14 17:06:11.666625
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert isinstance(ie, TF1IE)

# Generated at 2022-06-14 17:06:19.746862
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE()
    if not isinstance(obj, TF1IE):
        print('ERROR: type of object is NOT TF1IE')
        return False
    assert obj.IE_NAME == 'tf1:player'
    if not re.match(obj._VALID_URL, 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'):
        print('ERROR: format of URL is WRONG')
        return False
    return True


# Generated at 2022-06-14 17:06:25.822459
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:30.225371
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test constructor of TF1IE
    # Create a instance of TF1IE
    tf1 = TF1IE()

# Generated at 2022-06-14 17:06:32.270078
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert isinstance(TF1IE(None)._build_url_result('wat:foo'), dict)

# Generated at 2022-06-14 17:06:32.922769
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:37.816455
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = "http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
    tf1 = TF1IE(url)
    assert tf1.video_id == "replay-koh-lanta-22-mai-2015"
    assert tf1.program_slug == "koh-lanta"

# Generated at 2022-06-14 17:06:41.722029
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html", {})
    except ValueError:
        pass

# Generated at 2022-06-14 17:06:45.765999
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        # Testing TF1IE object creation
        obj_TF1IE = TF1IE()
    except Exception as e:
        assert False, "TF1IE object creation error. Err: %s" % e
    return



# Generated at 2022-06-14 17:07:05.718064
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    This tests whether TF1IE works as expected.
    """

# Generated at 2022-06-14 17:07:07.593792
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE

# Generated at 2022-06-14 17:07:14.980577
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()
    assert tf1IE is not None
    assert isinstance(tf1IE, InfoExtractor)
    assert hasattr(tf1IE, '_VALID_URL')
    assert hasattr(tf1IE, '_DOWNLOAD_WEBPAGE_FORMAT')
    assert hasattr(tf1IE, 'report_download_webpage')
    assert hasattr(tf1IE, '_download_json')
    assert hasattr(tf1IE, '_real_extract')


# Generated at 2022-06-14 17:07:16.007974
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # test for the constructor working well
    TF1IE(None)._VALID_URL

# Generated at 2022-06-14 17:07:18.768483
# Unit test for constructor of class TF1IE
def test_TF1IE():
    a = TF1IE()
    assert a.IE_NAME == "tf1"
    assert a.VALID_URL == TF1IE._VALID_URL


# Generated at 2022-06-14 17:07:19.377020
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:22.019093
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1._VALID_URL.__class__ is type(re.compile('hello'))

# Generated at 2022-06-14 17:07:23.232914
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE();
    t.test();

# Generated at 2022-06-14 17:07:23.807405
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:24.428531
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()

# Generated at 2022-06-14 17:07:36.691541
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie._VALID_URL

# Generated at 2022-06-14 17:07:44.942960
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()

    assert t.name == "TF1"
    assert "TF1" in t.IE_NAME
    assert t.ie_key() == "TF1"
    assert t.tested is None

    # test extraction
    t_extract_url = t.extract_url("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")

    assert t_extract_url.id == "13721082"
    assert t_extract_url.url == "wat:13721082"
    assert t_extract_url.title == "Mylène Farmer : d'une icône"
    assert t_extract_url.series == "D'une icône à l'autre"
    assert t_

# Generated at 2022-06-14 17:07:53.813769
# Unit test for constructor of class TF1IE
def test_TF1IE():
    example_id_1 = 'https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html'
    example_id_2 = 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html'
    example_id_3 = 'https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone'
    example_id_4 = 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone'
    TF1IE._download_xml = lambda self, url, video_id: 'The Title'

# Generated at 2022-06-14 17:08:00.686532
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info_extractor = TF1IE()
    assert isinstance(info_extractor, InfoExtractor)
    assert info_extractor._VALID_URL == '(?i)https?://(?:www\.)?tf1\.fr/(?P<path>[^/]+)/videos/(?P<id>[^/?&#]+).html'


# Generated at 2022-06-14 17:08:05.909954
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")
    assert obj._VALID_URL == "https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html"


# Generated at 2022-06-14 17:08:07.738600
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()
    assert tf1IE._NAME == 'tf1'

# Generated at 2022-06-14 17:08:10.786298
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:08:18.433666
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # This test ensures that TF1IE constructor actually works
    # Let's instantiate an object
    t = TF1IE(None)
    # Check if TF1IE constructor returns an object of the right class
    assert isinstance(t, TF1IE)
    # Check if type of the instance is set properly
    assert t._type == 'url_transparent'
    # Check if URL pattern is actually set
    assert t._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    # Check if _TESTS attribute is actually set
    assert t._TESTS
    # Check if _download_json method is working

# Generated at 2022-06-14 17:08:19.567293
# Unit test for constructor of class TF1IE
def test_TF1IE():
    x = TF1IE()
    print(x)

# Generated at 2022-06-14 17:08:20.940875
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1

# Generated at 2022-06-14 17:08:45.242358
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Create a TF1IE instance
    tf1 = TF1IE()
    # Check that it is an InfoExtractor instance
    assert isinstance(tf1, InfoExtractor)

# Generated at 2022-06-14 17:08:50.266201
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE(None)._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'


# Generated at 2022-06-14 17:08:59.259433
# Unit test for constructor of class TF1IE
def test_TF1IE():
    class_name = TF1IE.__name__
    test_url = "https://www.tf1.fr/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"

# Generated at 2022-06-14 17:09:02.972258
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # TF1 does not provide publicly accessible videos.
    # This test is only here to make sure TF1IE works.

    ie = TF1IE()
    ie.extract('wat:123')
    ie.extract('wat:456')

# Generated at 2022-06-14 17:09:03.982491
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()

# Generated at 2022-06-14 17:09:05.489269
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None)

# Generated at 2022-06-14 17:09:08.315428
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:09:17.257776
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:09:23.093209
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert t._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert isinstance(t, TF1IE)



# Generated at 2022-06-14 17:09:23.751034
# Unit test for constructor of class TF1IE
def test_TF1IE():
	TF1IE()

# Generated at 2022-06-14 17:10:09.963234
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # TF1IE is the main class for youtube extractor.
    # This class takes URL of a website from command
    # line and extracts all the information from that
    # website.
    # TF1IE
    assert TF1IE is not None


# Generated at 2022-06-14 17:10:10.727270
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()

# Generated at 2022-06-14 17:10:17.268903
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:10:20.102598
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.suitable("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html") == True

# Generated at 2022-06-14 17:10:25.707413
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL is not None
    assert ie._TESTS is not None
    assert ie._real_extract is not None

# Test run of class TF1IE on _TESTS

# Generated at 2022-06-14 17:10:30.386194
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.ie_key() == 'tf1'
    assert ie.ie_name() == 'TF1'
    assert ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:10:36.761841
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test non-existent video
    wat_id = "13641379"
    test_url = "https://wat.tv/video/quotidien-premiere-partie-11-juin-2019-13641379.html"
    # Error message sent by wat.tv when video is not present
    error_message = "No video found"
    # Should not crash
    TF1IE()._extract_url(test_url, wat_id)

# Generated at 2022-06-14 17:10:37.748361
# Unit test for constructor of class TF1IE
def test_TF1IE():
    a = TF1IE()
    assert isinstance(a, TF1IE)

# Generated at 2022-06-14 17:10:43.391577
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:10:49.010945
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    class_ = TF1IE
    attr = "wat"
    exp = "13641379"

    obj = class_(url)
    assert obj.__dict__["url"] == url
    assert obj.__dict__[attr] == exp


# Generated at 2022-06-14 17:11:48.295244
# Unit test for constructor of class TF1IE
def test_TF1IE():
    fail_test_urls = [
        "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html",
        "http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html",
        "http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html",
    ]
    success_test_urls = [
        "https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html",
    ]

# Generated at 2022-06-14 17:11:56.653509
# Unit test for constructor of class TF1IE
def test_TF1IE():
    import re
    import json
    from ..utils import parse_iso8601
    from yatube.extractor import TF1IE

# Generated at 2022-06-14 17:11:59.011608
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info = TF1IE.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert info is not None

# Generated at 2022-06-14 17:12:03.092341
# Unit test for constructor of class TF1IE
def test_TF1IE():
    match = TF1IE._VALID_URL.match('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert match
    assert match.span() == (0, 98)
    assert match.group(1) == "tmc/quotidien-avec-yann-barthes"
    assert match.group(2) == "quotidien-premiere-partie-11-juin-2019"

# Generated at 2022-06-14 17:12:04.562386
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()
    tf1IE.extract()

# Generated at 2022-06-14 17:12:06.206511
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE(object, 'any_url')

# Generated at 2022-06-14 17:12:06.722744
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:12:09.870426
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:12:12.777915
# Unit test for constructor of class TF1IE
def test_TF1IE():
    parser = TF1IE("https://www.tf1.fr/");
    assert parser.ie_key() == 'tf1', "TF1IE tests - Validate ie key"
    assert parser.IE_NAME == 'tf1', "TF1IE tests - Validate ie name"

# Generated at 2022-06-14 17:12:13.540478
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:14:13.025925
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:14:13.667176
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:14:14.247312
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:14:14.856430
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:14:16.409749
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:14:20.611439
# Unit test for constructor of class TF1IE
def test_TF1IE():
    print(TF1IE)
    print(InfoExtractor)
    tf1 = TF1IE()
    print(tf1)
    print(tf1.__class__.__name__)
    assert tf1.__class__.__name__ == "TF1IE"

# Generated at 2022-06-14 17:14:30.826013
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Valid URL
    tf1 = TF1IE("http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert tf1.suitable("http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html") == True
    assert tf1.suitable("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html") == True

# Generated at 2022-06-14 17:14:31.677304
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Testing the constructor of class TF1IE"""
    tf1IE = TF1IE()
    assert tf1IE is not None

# Generated at 2022-06-14 17:14:41.263570
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_cases = [
        ['https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html'],
        ['http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'],
        ['https://www.tf1.fr/c8/touche-pas-a-mon-poste/videos/tpmptest-3-mai-2016.html'],
    ]

    for input in test_cases:
        tf1ie_instance = TF1IE(input)
        assert 'TF1IE' == tf1ie_instance.IE_NAME
        assert True == tf1ie_instance._VALID_URL(input)


# Generated at 2022-06-14 17:14:49.048137
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test with a TF1 URL
    url = 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    tf1IE = TF1IE(url)
    assert tf1IE.program_slug == 'koh-lanta'
    assert tf1IE.slug == 'replay-koh-lanta-22-mai-2015'

    # Test with a non TF1 URL
    url = 'https://www.6play.fr/public-senat/videos/planete-senat-saison-1-du-mardi-23-avril-2019-ep-6-5-c1573236/'
    tf1IE = TF1IE(url)