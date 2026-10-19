

# Generated at 2022-06-14 17:06:01.984770
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:02.997046
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()

# Generated at 2022-06-14 17:06:15.111548
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:26.613012
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Try to construct a TF1IE instance with url containing
    # program name and its video id
    url = "https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"

    # Construct TF1IE instance and call handle method
    # with a constructed instance and the passing url
    TF1IE.suitable(TF1IE(), url)

    # Try to construct a TF1IE instance with url not
    # containing program name and its video id
    url = "https://www.tf1.fr/tf1/koh-lanta/videos/" \
            "replay-koh-lanta-22-mai-2015-screw-you-tf1.html"

    # Construct TF1IE instance and call handle method
    # with a

# Generated at 2022-06-14 17:06:37.961883
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:06:48.760414
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE({})
    assert tf1_ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:52.453076
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE('TF1IE','http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    return

# Generated at 2022-06-14 17:06:53.358798
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:02.275352
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    ie = TF1IE(url)
    assert(ie.program_slug == 'quotidien-avec-yann-barthes')
    assert(ie.slug == 'quotidien-premiere-partie-11-juin-2019')
    ie.program_slug = 'test'
    ie.slug = 'test'
    assert(ie.program_slug == 'test')
    assert(ie.slug == 'test')

# Generated at 2022-06-14 17:07:03.202614
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test initialization
    TF1IE()

# Generated at 2022-06-14 17:07:25.434919
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE()
    _VALID_URL = r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert list(re.match(tf1_ie._VALID_URL, 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html').groups()) == ['tmc/quotidien-avec-yann-barthes', 'quotidien-premiere-partie-11-juin-2019']

# Generated at 2022-06-14 17:07:27.568822
# Unit test for constructor of class TF1IE
def test_TF1IE():
    URL = "https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
    TF1IE(URL)

# Generated at 2022-06-14 17:07:28.698710
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:07:32.273306
# Unit test for constructor of class TF1IE
def test_TF1IE():
    import sys
    # Constructor of class
    my_IE = TF1IE()
    # Testing IPs
    my_IE.test(sys.argv[1:])

# Generated at 2022-06-14 17:07:34.196486
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    expected = 'tf1'
    assert instance._NETRC_MACHINE == expected

# Generated at 2022-06-14 17:07:43.333307
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert(TF1IE()._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html')

# Generated at 2022-06-14 17:07:47.655230
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Constructor test"""
    t = TF1IE
    assert t(None)._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:57.146440
# Unit test for constructor of class TF1IE
def test_TF1IE():
    s = TF1IE()
    assert s._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:02.563595
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE(TF1IE.needs_subprocessing(None))
    assert ie.tf1_program_slug == "tmc/quotidien-avec-yann-barthes"
    assert ie.tf1_slug == "quotidien-premiere-partie-11-juin-2019"

# Generated at 2022-06-14 17:08:06.908912
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # test the constructor from the class
    ie = TF1IE("Try to create an instance of TF1IE")
    # test the extraction for a normal video
    ie.extract("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")

# Generated at 2022-06-14 17:08:20.363849
# Unit test for constructor of class TF1IE
def test_TF1IE():
    import pytest
    assert pytest.raises(AssertionError, TF1IE, 'http://www.tf1.fr')

# Generated at 2022-06-14 17:08:24.663634
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.download("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:08:26.583447
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test constructor of class TF1IE
    """
    TF1IE('hello', 'world')


# Generated at 2022-06-14 17:08:27.198139
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:28.250653
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()

# Generated at 2022-06-14 17:08:31.672990
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("TF1IE", "http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:08:32.778760
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()

# Generated at 2022-06-14 17:08:34.266613
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE('TF1IE')



# Generated at 2022-06-14 17:08:36.698315
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = InfoExtractor('TF1IE')
    assert IE.ie_key() == 'TF1'

# Generated at 2022-06-14 17:08:39.690705
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE(youtube_dl=None)
    assert obj.ie_key() == 'TF1'

# Generated at 2022-06-14 17:09:10.522940
# Unit test for constructor of class TF1IE
def test_TF1IE():
    input_url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    tf1_ie = TF1IE()
    assert tf1_ie.suitable(input_url)
    assert (tf1_ie.compat_str(tf1_ie.IE_NAME) == tf1_ie.IE_NAME)
    assert (tf1_ie.compat_str(tf1_ie.IE_NAME) == tf1_ie.IE_NAME)
    assert (tf1_ie.compat_str(tf1_ie.name) == tf1_ie.name)
    assert (tf1_ie.compat_str(tf1_ie.name) == tf1_ie.name)

# Generated at 2022-06-14 17:09:13.631919
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(return_type=True)

# Generated at 2022-06-14 17:09:21.013480
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:09:24.470797
# Unit test for constructor of class TF1IE
def test_TF1IE():
    vimeo_ie = TF1IE()
    assert vimeo_ie is not None


# Generated at 2022-06-14 17:09:26.230658
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE()
        #assert False
    except TypeError:
        #assert True
        pass

# Generated at 2022-06-14 17:09:33.052325
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Create TF1IE instance
    tf1 = TF1IE()
    # Check if instance has the expected attribute
    assert tf1._VALID_URL  == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:09:34.367816
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:09:35.240709
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Check tf1ie is a subclass of InfoExtractor
    assert issubclass(TF1IE, InfoExtractor)

# Generated at 2022-06-14 17:09:46.135318
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert instance._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert instance._TESTS[0]['url'] == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert instance._TESTS[1]['url'] == 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'

# Generated at 2022-06-14 17:09:52.038567
# Unit test for constructor of class TF1IE
def test_TF1IE():
    args = ['https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html']
    tf1 = TF1IE()
    assert TF1IE._VALID_URL == tf1._VALID_URL, 'Regex of TF1IE is not correct'
    assert tf1._real_extract == tf1.real_extract, 'Not implemented real_extract method'

# Generated at 2022-06-14 17:10:39.970950
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:10:41.357218
# Unit test for constructor of class TF1IE
def test_TF1IE():
    global tf1
    tf1 = TF1IE()

# Generated at 2022-06-14 17:10:46.099399
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert ie._TESTS

# Generated at 2022-06-14 17:10:53.557860
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()  # uses default video_id, wat_id and program_slug from global variables
    # Tests that TF1IE constructor has used default values
    assert tf1ie._video_id == '13641379'
    assert tf1ie._wat_id == '10a8e19b-f9cb-4d43-a0f2-b24f8daf702d'
    assert tf1ie._program_slug == 'quotidien-avec-yann-barthes'
    # Tests that the rest of the instance variables have been initialized to default values

# Generated at 2022-06-14 17:11:01.933109
# Unit test for constructor of class TF1IE
def test_TF1IE():
    class_ = TF1IE

# Generated at 2022-06-14 17:11:04.597596
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE(None)._extract_mgid.__name__ == TF1IE._extract_mgid.__name__

# Generated at 2022-06-14 17:11:09.352595
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert t.program_slug == 'koh-lanta'
    assert t.slug == 'replay-koh-lanta-22-mai-2015'

# Generated at 2022-06-14 17:11:09.978175
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:11:21.604967
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:11:23.847904
# Unit test for constructor of class TF1IE
def test_TF1IE():
	TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:13:34.725727
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract(ie)

# Generated at 2022-06-14 17:13:35.932775
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None, None)

# Generated at 2022-06-14 17:13:37.315752
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert instance.ie_key() == 'tf1'

# Generated at 2022-06-14 17:13:40.222166
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test TF1IE with actual video
    TF1IE()

# Generated at 2022-06-14 17:13:41.340913
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE();


# Generated at 2022-06-14 17:13:45.208745
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url_test = 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    obj_test = TF1IE(url_test)
    print(obj_test)

# Generated at 2022-06-14 17:13:46.499223
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:13:51.721086
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == TF1IE._VALID_URL
    assert TF1IE()._TESTS == TF1IE._TESTS

# Generated at 2022-06-14 17:13:53.641961
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert tf1ie.IE_NAME == 'tf1'

# Generated at 2022-06-14 17:13:55.834704
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert tf1ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'