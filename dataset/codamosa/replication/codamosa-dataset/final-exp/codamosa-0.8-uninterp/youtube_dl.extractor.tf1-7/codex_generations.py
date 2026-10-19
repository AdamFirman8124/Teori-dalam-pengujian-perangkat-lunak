

# Generated at 2022-06-14 17:06:14.477286
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .constructor_test import ConstructorTest
    from .constructor_test import check_ie
    from .constructor_test import make_expected


# Generated at 2022-06-14 17:06:15.813555
# Unit test for constructor of class TF1IE
def test_TF1IE():
    x = TF1IE()
    assert x != None

# Generated at 2022-06-14 17:06:16.790627
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from tf1 import TF1IE
    assert True

# Generated at 2022-06-14 17:06:27.996432
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_url = [
        'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html',
        'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html',
        'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html'
    ]
    for url in test_url:
        test_TF1IE = TF1IE()
        assert test_TF1IE._match_id(url) is not None, "_match_id() returns incorrect ID for URL: " + url

# Generated at 2022-06-14 17:06:29.418414
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE
    except:
        assert False, "Class could not be constructed."


# Generated at 2022-06-14 17:06:30.069740
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:30.731829
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:06:34.818786
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    TF1IE(url)


# Generated at 2022-06-14 17:06:40.224411
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie_constructor = 'wat:' + '13641379'
    assert ie.ie_key() == 'TF1'
    assert ie.constructor == 'TF1IE'
    assert ie_constructor in repr(ie)

# Generated at 2022-06-14 17:06:41.966376
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Check it fails for empty URL
    t = TF1IE()
    assert t.suitable(None) == False

# Generated at 2022-06-14 17:06:49.823506
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert instance._VALID_URL is not None

# Generated at 2022-06-14 17:06:55.217322
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test of instantiation of an object of class TF1IE
    tf1 = TF1IE()
    # Test the test() method
    tf1.test()
    with open('TF1_test_output.txt', 'a') as f:
        f.write('test_TF1IE OK')
test_TF1IE()

# Generated at 2022-06-14 17:07:00.539720
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    object = ie.tf1_ie("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")
    assert object.url == "http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html"

# Generated at 2022-06-14 17:07:08.646436
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    ie.get_url('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    ie.get_urldata('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    ie.download('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:07:13.944340
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_url = 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    expected_extract = 'replay-koh-lanta-22-mai-2015'
    assert TF1IE._match_id(test_url) == expected_extract

# Generated at 2022-06-14 17:07:18.302797
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info_extractor = TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:07:19.321754
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None, None)

# Generated at 2022-06-14 17:07:27.890620
# Unit test for constructor of class TF1IE
def test_TF1IE():
    sample_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    # This should work fine
    TF1IE()

    # It should raise an error when an unsupported URL is used
    unsupported_url = 'https://www.youtube.com/watch?v=y6h5M6hl5wI'
    with pytest.raises(ExtractorError) as excinfo:
        TF1IE(unsupported_url)
    assert unsupported_url in str(excinfo)

    # This should work fine
    info_dict = TF1IE(sample_url)
    assert info_dict.get('id') == '13641379'

# Generated at 2022-06-14 17:07:31.472739
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert isinstance(instance, InfoExtractor)
    assert isinstance(instance, TF1IE)


# Generated at 2022-06-14 17:07:41.382078
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert instance.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html') == True
    assert instance.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html') == True
    assert instance.suitable('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html') == True
    assert instance.suitable('http://www.tf1.fr/documentaire/videos/mylene-farmer-d-une-icone.html') == False
    assert instance.suitable

# Generated at 2022-06-14 17:07:53.245373
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:56.619672
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE("test_TF1IE")
    print("test_TF1IE")

# Generated at 2022-06-14 17:08:03.609852
# Unit test for constructor of class TF1IE
def test_TF1IE():
    s = TF1IE()
    assert s.tf1 is not None
    assert s.tf1.baseURL == 'https://www.tf1.fr/graphql/web'
    assert s.tf1.headers == {'Content-Type': 'application/json',
                             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}


# Generated at 2022-06-14 17:08:04.792845
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert isinstance(tf1, InfoExtractor)

# Generated at 2022-06-14 17:08:06.098341
# Unit test for constructor of class TF1IE
def test_TF1IE():
    global tf1
    tf1 = TF1IE()
    tf1.suite()

# Generated at 2022-06-14 17:08:07.527164
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE().test()

# Generated at 2022-06-14 17:08:16.714496
# Unit test for constructor of class TF1IE
def test_TF1IE():

    # test with invalid starting URL
    t = TF1IE(None)
    assert t.is_valid() is False
    t = TF1IE('url')
    assert t.is_valid() is False

    # test with valid starting URL
    t = TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert t.is_valid() is True
    t = TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    assert t.is_valid() is True

    # test that it works with the PLATFORM_ID, and that the PLATFORM_ID is extracted correctly
    # (the PLATFORM_

# Generated at 2022-06-14 17:08:18.672298
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE_inst = TF1IE()
    assert isinstance(TF1IE_inst, TF1IE)

# Generated at 2022-06-14 17:08:22.992432
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.download('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert ie._VALID_URL
    assert ie._TESTS


# Generated at 2022-06-14 17:08:27.011821
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._extract_info_from_url('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:08:51.220457
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("test", "test")

# Generated at 2022-06-14 17:08:54.790280
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:09:03.521157
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert obj._VALID_URL == "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"

# Generated at 2022-06-14 17:09:06.492583
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:09:07.110497
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:09:09.329085
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    print("\nTest constructor of TF1IE")
    assert tf1
    print("OK\n")


# Generated at 2022-06-14 17:09:15.927181
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:09:24.713355
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:09:26.449020
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test construction of TF1IE class"""
    assert isinstance(TF1IE, InfoExtractor)

# Generated at 2022-06-14 17:09:35.445306
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert ie.url == 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    assert ie.id == 'replay-koh-lanta-22-mai-2015'
    assert ie.program_slug == 'tf1/koh_lanta'

# Generated at 2022-06-14 17:10:23.589829
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert IE != None

# Generated at 2022-06-14 17:10:24.361148
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie

# Generated at 2022-06-14 17:10:26.814047
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert(tf1ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html')

# Generated at 2022-06-14 17:10:35.412353
# Unit test for constructor of class TF1IE
def test_TF1IE():
    no_args_ie = TF1IE()
    assert TF1IE._VALID_URL == "https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html"
    assert TF1IE._TESTS[0]['url'] == "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    assert TF1IE._TESTS[0]['info_dict']['id'] == "13641379"
    assert TF1IE._TESTS[0]['info_dict']['ext'] == "mp4"
    assert TF1IE

# Generated at 2022-06-14 17:10:41.992988
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = ("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    result = TF1IE()._real_extract(url)
    assert result['id'] == '13641379'
    assert result['ext'] == 'mp4'
    assert result['title'] == '#QT1 du 11 juin 2019 - Partie 1/2'
    assert result['description'] == 'Pour découvrir la suite de votre programme, rendez-vous sur MYTF1 et suivez le direct de la deuxième partie ! '
    assert result['upload_date'] == '20190611'
    assert result['timestamp'] == 1560273989

# Generated at 2022-06-14 17:10:44.150485
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_instance = TF1IE()
    assert isinstance(test_instance, TF1IE)

# Generated at 2022-06-14 17:10:45.124398
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(InfoExtractor())

# Generated at 2022-06-14 17:10:52.967316
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:10:53.612506
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:10:55.034100
# Unit test for constructor of class TF1IE
def test_TF1IE():
    _ = TF1IE(IE_NAME, {'api_key': API_KEY})

# Generated at 2022-06-14 17:13:10.770237
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:13:13.279770
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Description:
        Test constructor of class TF1IE
    """
    # The basic test
    assert isinstance(TF1IE(),InfoExtractor)
    # Need to develop to test more cases
    # ...

# Generated at 2022-06-14 17:13:15.634943
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:13:20.341334
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html', 0)
    assert ie.url == 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'

# Generated at 2022-06-14 17:13:30.127846
# Unit test for constructor of class TF1IE
def test_TF1IE():

    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    originalIE = TF1IE().url_result(url)

    assert originalIE.__class__.__name__ == 'WatIE', "URL is not well-formed"

    # Download both URLs to ensure they are the same
    originalIE = originalIE.extract()
    newIE = TF1IE().url_result(url).extract()

    assert originalIE['id'] == newIE['id'], "IDs must be the same"
    assert originalIE['url'] == newIE['url'], "URLs must be the same"

# Generated at 2022-06-14 17:13:41.273153
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    assert TF1IE._VALID_URL == TF1IE.VALID_URL
    assert TF1IE._TESTS == TF1IE.TESTS
    assert TF1IE._real_extract("") == InfoExtractor._real_extract("")
    assert TF1IE.suitable("") == InfoExtractor.suitable("")
    assert TF1IE.suitable(url) == InfoExtractor.suitable(url)
    assert TF1IE.IE_NAME == InfoExtractor.IE_NAME
    assert TF1IE.IE_DESC == InfoExtractor.IE_DESC

# Generated at 2022-06-14 17:13:50.479393
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from ..helpers import generate_extractor_test

# Generated at 2022-06-14 17:13:51.092045
# Unit test for constructor of class TF1IE
def test_TF1IE():
    return TF1IE()

# Generated at 2022-06-14 17:13:54.396608
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert ie is not None

# Generated at 2022-06-14 17:14:00.928027
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()
    assert tf1IE is not None
    assert tf1IE.IE_NAME == "tf1"
    assert tf1IE.IE_DESC == "tf1.fr"
    assert tf1IE.VALID_URL == "https?://(?:www\.)?tf1\.fr/(?:[^/]+/){2}videos/(?P<id>[^/?&#]+)\.html"
    assert tf1IE.HOST == "www.tf1.fr"
    assert tf1IE.API_URL == "https://www.tf1.fr/graphql/web"
    assert tf1IE.BRAND_SLUG == "tf1"
