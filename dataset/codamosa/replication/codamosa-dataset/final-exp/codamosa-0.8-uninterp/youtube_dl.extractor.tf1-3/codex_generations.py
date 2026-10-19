

# Generated at 2022-06-14 17:06:01.143834
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:06:12.072803
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Video must be implemented first
    if 'TF1IE' not in globals():
        return

    ie = TF1IE('https://www.tf1.fr/tf1/koh-lanta/vidos/replay-koh-lanta-22-mai-2015.html')
    assert ie.url == 'http://www.tf1.fr/tf1/koh-lanta/vidos/replay-koh-lanta-22-mai-2015.html'
    assert ie.extract_info('wat:15856438') == {
        '_type': 'url_transparent',
        'url': 'wat:15856438',
        'id': '15856438'
    }

# Generated at 2022-06-14 17:06:15.399978
# Unit test for constructor of class TF1IE
def test_TF1IE():
	# Unit tests test the function of a function or a class in a program, not the correctness of its output.
	# Extraction phase is not required to be test here
	TF1IE()

# Generated at 2022-06-14 17:06:16.291108
# Unit test for constructor of class TF1IE
def test_TF1IE():
	TF1IE(InfoExtractor())

# Generated at 2022-06-14 17:06:16.840311
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:18.749468
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:06:28.839099
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE(requests=True)
    # Verify that JSON of class TF1IE has there fields 'tags' and 'decoration'
    assert(IE.json['data']['videoBySlug'].get('tags') is not None)
    assert(IE.json['data']['videoBySlug'].get('decoration') is not None)
    # Verify that JSON of class TF1IE has not these fields
    assert(IE.json['data']['videoBySlug'].get('url') is None)
    assert(IE.json['data']['videoBySlug'].get('image') is None)
    # Verify that tags is not empty
    assert(len(IE.json['data']['videoBySlug'].get('tags')) != 0)
    # Verify that decoration is not empty


# Generated at 2022-06-14 17:06:33.075290
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    TF1IE(url, {})


test_TF1IE()

# Generated at 2022-06-14 17:06:33.709419
# Unit test for constructor of class TF1IE
def test_TF1IE():
	TF1IE()

# Generated at 2022-06-14 17:06:42.515952
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:06:50.120190
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1

# Generated at 2022-06-14 17:06:51.540670
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:06:57.158917
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.ie_key() == 'TF1'
    assert ie.ie_name() == 'TF1'
    assert ie.extract_id('replay-koh-lanta-22-mai-2015.html') == 'replay-koh-lanta-22-mai-2015'

# Generated at 2022-06-14 17:06:58.205225
# Unit test for constructor of class TF1IE
def test_TF1IE():
	ie = TF1IE()
	assert ie is not None


# Generated at 2022-06-14 17:06:59.645661
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert not tf1 is None


# Generated at 2022-06-14 17:07:02.353547
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # If a constructor raises an exception, we do not need an assert
    TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")

# Generated at 2022-06-14 17:07:06.882304
# Unit test for constructor of class TF1IE
def test_TF1IE():
	# Test for parameters passing with correct value
	test_function = TF1IE(TF1IE._VALID_URL, {})
	assert test_function._VALID_URL == TF1IE._VALID_URL
	# Test for parameters passing with incorrect value
	test_function = TF1IE("", {})
	assert test_function._VALID_URL != TF1IE._VALID_URL


# Generated at 2022-06-14 17:07:08.570445
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE({'headers': {}})

# Generated at 2022-06-14 17:07:17.489704
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert tf1ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:24.157400
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Arrange
    url = ['https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html']

    # Act
    tf1_ie = TF1IE()._real_extract(url)

    # Assert
    assert len(tf1_ie) > 0

# Generated at 2022-06-14 17:07:44.689687
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE()
    assert obj._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:46.046961
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:07:56.008565
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test video
    # http://www.wat.tv/video/koh-lanta-intégrale-du-22-mai-5h5w5_5f7ue_.html
    video_id = "5h5w5"
    # Test URLs
    video_urls = [
        "http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html",
        "http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html",
    ]
    ie = TF1IE()
    for url in video_urls:
        video = ie._real_extract(url)

# Generated at 2022-06-14 17:07:56.669419
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:07:57.760721
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:08:01.346319
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:08:04.960506
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE(None, None)._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:09.095218
# Unit test for constructor of class TF1IE
def test_TF1IE():
    video = TF1IE(
        'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:08:15.286703
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # without url
    url = ""
    t = TF1IE(url)

    # invalid url
    url = "htpps://www.tf1.fr/tf1/the-voice/videos/the-voice-7-mai-2019-1.html"
    t = TF1IE(url)

    # valid url
    url = "http://www.tf1.fr/tf1/the-voice/videos/the-voice-7-mai-2019-1.html"
    t = TF1IE(url)

# Generated at 2022-06-14 17:08:17.330325
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:08:48.358750
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    TF1IE('https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:08:52.291202
# Unit test for constructor of class TF1IE
def test_TF1IE():
    temp = TF1IE()
    assert temp._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:53.534510
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test construction of the TF1IE."""
    TF1IE({})

# Generated at 2022-06-14 17:08:54.998563
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1Instance = TF1IE()
    assert tf1Instance

# Generated at 2022-06-14 17:09:07.809475
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info_extractor = TF1IE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:09:16.899091
# Unit test for constructor of class TF1IE
def test_TF1IE():

    # Test with a video
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    ie = TF1IE(url)
    assert ie.url == url
    assert ie.program_slug == "quotidien-avec-yann-barthes"
    assert ie.slug == "quotidien-premiere-partie-11-juin-2019"
    
    # Test with a non-video url
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/"
    ie = TF1IE(url)
    
    # Test with a valid url

# Generated at 2022-06-14 17:09:27.051320
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.name == 'tf1.fr'
    assert ie.url_re == re.compile(TF1IE._VALID_URL)
    assert ie.test()
    assert ie.test_url('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert ie.test_url('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    assert ie.test_url('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:09:28.557021
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.__class__ == TF1IE

# Generated at 2022-06-14 17:09:38.890587
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test without real URL
    assert TF1IE._VALID_URL
    # Test with real URL
    ie = InfoExtractor()
    ie.add_info_extractor(
        TF1IE.ie_key(),
        TF1IE(ie, {})
    )
    extract_info = ie.extract(ie._make_url_result('', '', 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthés/videos/quotidien-première-partie-11-juin-2019.html'))
    t_obj = extract_info['_type']
    t_url = extract_info['url']
    assert 'wat' in t_url
    assert t_obj == 'url_transparent'
    assert extract_info['id']

# Generated at 2022-06-14 17:09:44.336733
# Unit test for constructor of class TF1IE
def test_TF1IE():
    import unittest
    class TF1IEInitTestCase(unittest.TestCase):
        def setUp(self):
            self.tf1IE = TF1IE()

        def test_TF1IE(self):
            self.assertTrue(type(self.tf1IE) == TF1IE)

    suite = unittest.TestLoader().loadTestsFromTestCase(TF1IEInitTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-14 17:10:33.789602
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE(None)._VALID_URL == TF1IE._VALID_URL
    assert TF1IE(None)._TESTS == TF1IE._TESTS

# Generated at 2022-06-14 17:10:34.629669
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None)


# Generated at 2022-06-14 17:10:36.377205
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('https://www.tf1.fr/')
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:10:37.355066
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(InfoExtractor._downloader)._request_webpage(None, None)

# Generated at 2022-06-14 17:10:40.391901
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    assert IE._VALID_URL == url
    assert IE._TESTS != url

# Generated at 2022-06-14 17:10:41.760742
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(InfoExtractor)

# Generated at 2022-06-14 17:10:51.089877
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Creating instance of TF1IE
    tf1 = TF1IE()

    assert tf1._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:10:53.708977
# Unit test for constructor of class TF1IE
def test_TF1IE():
    infoExtractor = TF1IE()
    assert infoExtractor.name == 'TF1'
    assert infoExtractor.suport() == True

# Generated at 2022-06-14 17:10:59.741131
# Unit test for constructor of class TF1IE
def test_TF1IE():
	print("Test_TF1IE")
	tf1 = TF1IE()
	assert tf1.duration == 0
	assert tf1.season_num == 0
	assert tf1.episode_num == 0


# To run a unit test, use 'py -3.7 -m unittest discover'
# If 'py' is not recognized, use 'python3 -m unittest discover'
if __name__ == "__main__":
	test_TF1IE()

# Generated at 2022-06-14 17:11:00.949739
# Unit test for constructor of class TF1IE
def test_TF1IE():
	TF1IE(0,0)


# Generated at 2022-06-14 17:13:18.744813
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_TF1IE = TF1IE()
    print(test_TF1IE)


# Generated at 2022-06-14 17:13:23.419382
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:13:26.586526
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.IE_NAME == TF1IE._IE_NAME
    assert tf1._VALID_URL == TF1IE._VALID_URL
    assert tf1._TESTS == TF1IE._TESTS

# Generated at 2022-06-14 17:13:31.087259
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test that TF1IE constructor is working."""
    tf1IE = TF1IE()
    response = tf1IE.extract('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    info = response.get('info_dict')
    assert info['title'] == 'md5:f392bc52245dc5ad43771650c96fb620'

# Generated at 2022-06-14 17:13:32.297684
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None)

# Generated at 2022-06-14 17:13:42.023596
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:13:44.721602
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/quotidien/videos/quotidien-premiere-partie-19-juin-2019.html')

# Generated at 2022-06-14 17:13:50.607956
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url_list = ['http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html', 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html']
    tf1_extractor = TF1IE()
    # Check if the extractor is initialized correctly
    tester = lambda each: tf1_extractor.suitable(each)
    assert(all(map(tester, url_list)))

# Generated at 2022-06-14 17:13:52.973420
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:13:55.670187
# Unit test for constructor of class TF1IE
def test_TF1IE():
    s = TF1IE()
    s._download_json('https://www.tf1.fr/graphql/web', 'replay-koh-lanta-22-mai-2015')