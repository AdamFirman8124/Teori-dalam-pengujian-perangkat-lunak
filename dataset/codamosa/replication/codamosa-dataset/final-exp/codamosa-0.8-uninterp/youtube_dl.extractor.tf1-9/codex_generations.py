

# Generated at 2022-06-14 17:06:13.592319
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.test(UrlTest('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html', 'tf1')) == True
    assert ie.test(UrlTest('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html', 'tf1')) == True
    assert ie.test(UrlTest('https://www.tf1.fr/foobarbaz/videos/mylene-farmer-d-une-icone.html', 'tf1')) == False

# Generated at 2022-06-14 17:06:19.505222
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie_instance = ie('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert isinstance(ie_instance, TF1IE)

# Generated at 2022-06-14 17:06:25.538917
# Unit test for constructor of class TF1IE
def test_TF1IE():
    check_extract_info(TF1IE(), 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html', {
        'id': '01456963',
        'series': 'Mylène Farmer, d\'une icône',
        'title': 'Mylène Farmer, d\'une icône',
        '_type': 'url_transparent',
    })

# Generated at 2022-06-14 17:06:37.338651
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE("https://www.wat.tv/video/quotidien-premiere-partie-11-juin-13641379.html")
    assert TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")

# Generated at 2022-06-14 17:06:39.691296
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # "This test is an initialization test of TF1IE class"
    test_object = TF1IE(None)
    assert test_object



# Generated at 2022-06-14 17:06:49.950042
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert ie._TESTS[0]['url'] == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert ie._TESTS[1]['url'] == 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'

# Generated at 2022-06-14 17:06:56.780569
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert(TF1IE().extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')['title'] == 'Quotidien 1ère partie - 11 juin 2019')

if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:07:06.239491
# Unit test for constructor of class TF1IE
def test_TF1IE():
	assert TF1IE._API_URL == 'https://www.tf1.fr/graphql/web'
	assert TF1IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:10.478821
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.url = ie._VALID_URL
    ie.program_slug, ie.slug = ie.url.split('/')[-3:]

# Generated at 2022-06-14 17:07:14.270707
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html", "koh-lanta", "replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:07:21.437463
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('md5:')

# Generated at 2022-06-14 17:07:27.939469
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    ie = TF1IE(url)
    assert ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert ie.suitable(url) == True
    assert ie.extract(url) is not None



# Generated at 2022-06-14 17:07:38.241427
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    ie = TF1IE()
    assert ie.matches(url)
    assert ie.suitable(url)
    assert ie.IE_NAME == ie.__class__.__name__
    assert ie.IE_DESC == ie.__class__.__doc__
    assert re.search(r"i.ytimg\.com\/vi\/[a-zA-Z0-9_-]{11}\/(mqdefault|hqdefault|maxresdefault)\.jpg", ie.ie_key())

# Generated at 2022-06-14 17:07:45.865588
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert tf1.name == 'TF1'
    assert tf1.ie_key() == 'TF1'
    assert tf1._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:54.275812
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    tf1_ie = TF1IE.ie_key()(url)
    assert tf1_ie._VALID_URL == TF1IE._VALID_URL
    for test in TF1IE._TESTS:
        tf1_ie = TF1IE.ie_key()(test['url'])
        assert tf1_ie._TESTS == TF1IE._TESTS


# Generated at 2022-06-14 17:07:59.149671
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE("http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert tf1.get_program() == "TMC"
    assert tf1.get_program_slug() == "quotidien-avec-yann-barthes"
    assert tf1.get_slug() == "quotidien-premiere-partie-11-juin-2019"

# Generated at 2022-06-14 17:08:00.301123
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()

# Generated at 2022-06-14 17:08:02.719604
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # This is an example of constructor
    TF1IE("url","param1","param2")

# Generated at 2022-06-14 17:08:05.199084
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test the constructor
    # instantiate the object
    assert TF1IE.__name__ == 'TF1IE'

    # test it
    TF1IE();


# Generated at 2022-06-14 17:08:12.015602
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t._VALID_URL == 'https?://(?:www\\.)?tf1\\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\\.html'
    assert t._TESTS[0]['url'] == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert t._TESTS[0]['only_matching'] is False
    assert t._TESTS[0]['params']['skip_download'] is True

# Generated at 2022-06-14 17:08:27.433624
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:31.715313
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE({})._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:32.478357
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # one-pass check
    TF1IE()

# Generated at 2022-06-14 17:08:37.577150
# Unit test for constructor of class TF1IE
def test_TF1IE():
    asserEqual(TF1IE.ie_key(), 'TF1')
    t = TF1IE()
    assertEqual(TF1IE.ie_key(), 'TF1')
    assertEqual(t.ie_key(), 'TF1')

    asserEqual(TF1IE.ie_key(), 'TF1')
    t = TF1IE()
    assertEqual(TF1IE.ie_key(), 'TF1')
    assertEqual(t.ie_key(), 'TF1')

# Generated at 2022-06-14 17:08:44.224662
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    ie.extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:08:44.803458
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:50.319068
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .test_downloader import run_on_default_downloads_dir
    run_on_default_downloads_dir(lambda: TF1IE().download("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"))

# Generated at 2022-06-14 17:08:51.368419
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tester=TF1IE()

# Generated at 2022-06-14 17:08:52.719830
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert(TF1IE)


# Generated at 2022-06-14 17:08:56.623489
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html') is True

if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:09:21.271056
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract('')
    assert ie is not None

# Generated at 2022-06-14 17:09:24.109622
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # The following line is not supposed to raise an exception
    TF1IE()

# Generated at 2022-06-14 17:09:30.617559
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert type(TF1IE('wat:123').WATCH_URL) is str
    assert TF1IE('wat:123').WATCH_URL == 'https://wat.tf1.fr/videos/123?format=json&authKey=wat-drupal-tf1'
    assert type(TF1IE('wat:123', headers={'User-Agent': 'Mozilla/5.0'})._USER_AGENT) is str
    assert TF1IE('wat:123', headers={'User-Agent': 'Mozilla/5.0'})._USER_AGENT == 'Mozilla/5.0'

# Generated at 2022-06-14 17:09:31.193216
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()

# Generated at 2022-06-14 17:09:35.102940
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert instance.__class__.__name__ == 'TF1IE'

# Generated at 2022-06-14 17:09:36.113060
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:09:36.761619
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("TF1IE", "tf1")

# Generated at 2022-06-14 17:09:37.487822
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('REPLAY')

# Generated at 2022-06-14 17:09:37.797511
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:09:38.258841
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:10:33.555248
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t.match({'url': 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'})
    assert not t.match({'url': 'https://www.youtube.com/watch?v=G6UoY6fXW6U'})
    assert t.extract({'url': 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'})

# Generated at 2022-06-14 17:10:40.649739
# Unit test for constructor of class TF1IE
def test_TF1IE():
    class_ = TF1IE
    tf1_video = 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    assert class_._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert class_._match_id(tf1_video) == (None, 'koh-lanta', 'replay-koh-lanta-22-mai-2015')

# Generated at 2022-06-14 17:10:50.203036
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t.suitable("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert not t.suitable("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Example of unit test for the extractor
#def test_TF1IE_1():
#    TF1IE_instance = TF1IE()
#    assert TF1IE_instance.suitable("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:10:52.690270
# Unit test for constructor of class TF1IE
def test_TF1IE():
    res = TF1IE.suite().run(TF1IE)
    print(res.errors)
    print(res.failures)

# Generated at 2022-06-14 17:11:01.541230
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert ie is not None
    assert ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:11:07.144606
# Unit test for constructor of class TF1IE
def test_TF1IE():
    exp = TF1IE()
    assert exp.url_re == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert exp.ie_key() == 'TF1'

# Generated at 2022-06-14 17:11:10.709649
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test class TF1IE constructor."""
    ie = TF1IE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TF1IE)

# Generated at 2022-06-14 17:11:11.763169
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()

# Generated at 2022-06-14 17:11:12.764764
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert(isinstance(TF1IE(), InfoExtractor))

# Generated at 2022-06-14 17:11:23.192736
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Tests for the TF1IE constructor
    wat_id = "FEJ60W"
    tf1_ie = TF1IE('id', wat_id)
    
    # The TF1IE constructor should assign the correct wat_id to the 'id' field
    assert tf1_ie.id == wat_id
    
    # The TF1IE constructor should assign the correct parsed_url to the 'url' field
    assert tf1_ie.url == 'wat:' + wat_id
    
    # The TF1IE constructor should assign the correct title to the 'title' field
    assert tf1_ie.title == "Fatal Bazooka - Fous ta cagoule"

test_TF1IE()

# Generated at 2022-06-14 17:13:39.545307
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None)._download_webpage(None, None, None, None, None)

# Generated at 2022-06-14 17:13:49.206197
# Unit test for constructor of class TF1IE
def test_TF1IE():
    inst = TF1IE()
    assert inst._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:13:51.042178
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Tests class constructor."""
    assert TF1IE()

# Generated at 2022-06-14 17:13:51.668860
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:14:00.289678
# Unit test for constructor of class TF1IE
def test_TF1IE():
    import re
    import unittest
    from yledl import YoutubeDL

    from .test_utils import (
        list_testcases,
        get_testcases_info,
        read_test_json,
        write_test_json,
        get_testcase_url,
    )

    testcases = list_testcases(TF1IE._TESTS)

    # testcases = [
    #     'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html',
    # ]

    class TF1IEUnitTest(unittest.TestCase):
        def setUp(self):
            self.ie = TF1IE()

        def tearDown(self):
            pass



# Generated at 2022-06-14 17:14:01.291352
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()


# Generated at 2022-06-14 17:14:06.339684
# Unit test for constructor of class TF1IE
def test_TF1IE():

    # Constructor of class TF1IE is called only if the URL matches a valid format.
    # Hence, we must test only one valid format here.
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    tf1 = TF1IE()

    # No exception means the constructor has been called successfully
    assert tf1 is not None

# Generated at 2022-06-14 17:14:11.682191
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test for constructor of TF1IE class.
    """
    TF1IE = TF1IE([]).__class__.__name__
    assert TF1IE == 'TF1IE', "Test for constructor of TF1IE class failed."
    print("Test for constructor of TF1IE class succeed.")



# Generated at 2022-06-14 17:14:14.734864
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    instance.extract()

# Generated at 2022-06-14 17:14:19.352955
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')