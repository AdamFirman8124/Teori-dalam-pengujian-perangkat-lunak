

# Generated at 2022-06-14 17:06:06.484080
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE();
    assert ie.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:06:10.831203
# Unit test for constructor of class TF1IE
def test_TF1IE():
   """Check if constructor works."""
   try:
      TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
   except AssertionError:
      pass

# Generated at 2022-06-14 17:06:11.367534
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:12.725492
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('wat', 'wat_id')

# Generated at 2022-06-14 17:06:24.808241
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE()
    assert obj.IE_NAME == 'tf1'
    assert obj.IE_DESC == 'TF1'
    assert obj._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:28.400548
# Unit test for constructor of class TF1IE
def test_TF1IE():
	tf1_ie = TF1IE()
	url = "https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
	tf1_ie.extract(url)

# Generated at 2022-06-14 17:06:38.271361
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:06:39.833429
# Unit test for constructor of class TF1IE
def test_TF1IE():
    result = TF1IE()
    assert type(result) == TF1IE

# Generated at 2022-06-14 17:06:43.485520
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("url", "downloader")._real_extract("url")
    TF1IE("url", "downloader")._download_webpage("url")
    TF1IE("url", "downloader")._download_json("url", "record_id")

# Generated at 2022-06-14 17:06:45.714734
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.tf1_constructor()

# Generated at 2022-06-14 17:07:06.394031
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie._real_initialize()
    assert ie._VALID_URL == 'https?://(?:www\\.)?tf1\\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\\.html'

# Generated at 2022-06-14 17:07:08.179015
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:08.795578
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:10.478704
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE("")
    assert instance.ie_key() == "TF1"

# Generated at 2022-06-14 17:07:12.417763
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # create instance of class TF1IE
    # test it's type
    assert(isinstance(TF1IE(), TF1IE))

# Generated at 2022-06-14 17:07:13.861404
# Unit test for constructor of class TF1IE
def test_TF1IE():
    class_to_test = "TF1IE"
    assert class_to_test

# Generated at 2022-06-14 17:07:16.205704
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:07:18.838787
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    instance.http._downloader.params.update({'proxy': '127.0.0.1:8118'})
    instance._match_id(instance._VALID_URL)

# Generated at 2022-06-14 17:07:19.867938
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1

# Generated at 2022-06-14 17:07:23.798399
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._real_extract('http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')



# Generated at 2022-06-14 17:07:35.499628
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:38.538944
# Unit test for constructor of class TF1IE
def test_TF1IE():
	ie = TF1IE()
	assert ie._VALID_URL == ie._VALID_URL
	assert ie._TESTS == ie._TESTS
	assert ie._real_extract == ie._real_extract

# Generated at 2022-06-14 17:07:41.983951
# Unit test for constructor of class TF1IE
def test_TF1IE():
  assert TF1IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:48.366347
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:49.013209
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:54.464287
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # These playlists don't exist anymore
    tf1 = TF1IE()
    tf1._real_extract('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    tf1._real_extract('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:07:59.667822
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")


# Generated at 2022-06-14 17:08:00.720739
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert(TF1IE().tf1VideoUrl('test') == 'test.html')

# Generated at 2022-06-14 17:08:01.400595
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:03.345765
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .wat import WatIE
    instance = TF1IE()
    assert isinstance(instance, WatIE)

# Generated at 2022-06-14 17:08:30.727116
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert obj.program_slug == 'koh-lanta'
    assert obj.slug == 'replay-koh-lanta-22-mai-2015'

# Generated at 2022-06-14 17:08:32.079678
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:08:39.818175
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert re.match(TF1IE._VALID_URL, 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html') is not None
    assert re.match(TF1IE._VALID_URL, 'https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html') is not None
    assert re.match(TF1IE._VALID_URL, 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html') is not None

# Generated at 2022-06-14 17:08:45.174988
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Extract URL
    ext = TF1IE()._extract_url(
        "http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    )
    # Check that all variables are defined (and not empty)
    assert ext.get('id')
    assert ext.get('url')
    assert ext.get('title')
    assert ext.get('thumbnails')
    assert ext.get('description')
    assert ext.get('timestamp')
    assert ext.get('duration')
    assert ext.get('series')
    assert ext.get('tags')
    assert ext.get('season_number')
    assert ext.get('episode_number')

# Generated at 2022-06-14 17:08:45.751485
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:47.845787
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()

# Generated at 2022-06-14 17:08:57.505472
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # _VALID_URL refers to a valid video from TF1 website
    _VALID_URL = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'

    # url_data stores the url that is passed to constructor of class TF1IE
    url_data = {'url': _VALID_URL}

    # in order to test constructor of class TF1IE
    # we can pass url_data dict to the constructor
    test_tf1 = TF1IE('test', url_data)
    # we can check if the url_data is valid by the function _real_extract
    test_tf1._real_extract(url_data['url'])

# Generated at 2022-06-14 17:08:59.631212
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == tf1IE._VALID_URL

tf1IE = TF1IE()

# Generated at 2022-06-14 17:09:02.511549
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # These may or may not be real video IDs in the future.
    assert(TF1IE.ie_key() == 'tf1')
    assert(TF1IE.working == True)

# Generated at 2022-06-14 17:09:03.521157
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('A', 'B')

# Generated at 2022-06-14 17:09:50.351668
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert tf1ie.name == 'tf1'

# Generated at 2022-06-14 17:09:51.293717
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE is not None

# Generated at 2022-06-14 17:09:52.281316
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('www.tf1.fr');

# Generated at 2022-06-14 17:09:54.518978
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:09:56.125558
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('TF1IE', 'tf1')

# Generated at 2022-06-14 17:09:57.672598
# Unit test for constructor of class TF1IE
def test_TF1IE():
    constructor_test(TF1IE)

# Generated at 2022-06-14 17:09:58.373366
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:09:59.645423
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:10:08.421931
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL == 'https?://(?:www\\.)?tf1\\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\\.html'
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html', {'skip_download': True, 'format': 'bestvideo'})

# Generated at 2022-06-14 17:10:15.771579
# Unit test for constructor of class TF1IE
def test_TF1IE():
    print ('test_TF1IE:------------')
    url_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    url_program_slug = 'quotidien-avec-yann-barthes'
    url_slug = 'quotidien-premiere-partie-11-juin-2019'
    id_id = '13641379'
    info_dict_id = '13641379'
    info_dict_ext = 'mp4'
    info_dict_title = 'md5:f392bc52245dc5ad43771650c96fb620'

# Generated at 2022-06-14 17:12:09.450527
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test that TF1IE is initialized properly"""
    assert isinstance(TF1IE(), TF1IE)

# Generated at 2022-06-14 17:12:11.770931
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """test_TF1IE class constructor"""
    IE = TF1IE()
    assert IE.ie_key() == 'TF1'
    assert IE.ie_name() == 'tf1.fr'

# Generated at 2022-06-14 17:12:18.867831
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()
    assert tf1IE.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert tf1IE.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert not tf1IE.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:12:29.457659
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.extractor is None
    assert tf1.ie_key is None
    assert tf1.host is None
    assert tf1.suitable is None
    assert tf1.IE_DESC is None
    assert tf1.webpage_read_content is None
    assert tf1.BR_DESC is None
    assert tf1.working is None
    assert tf1.age_limit is None
    assert tf1.http is None
    assert tf1.TOKEN_HOST is None
    assert tf1.TOKEN_API_URL is None
    assert tf1.TOKEN_QUERY_TEMPLATE is None
    assert tf1.TOKEN_SUCCESS is None
    assert tf1.TOKEN_FAILURE is None
    assert tf1.uuid is None


# Generated at 2022-06-14 17:12:31.435721
# Unit test for constructor of class TF1IE
def test_TF1IE():
    total = 0
    for a in range(1000000):
        b = TF1IE()
        total += a
    assert total == 499999500000

# Generated at 2022-06-14 17:12:36.703156
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE()
    assert tf1_ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:12:37.262078
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:12:43.212539
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Constructor with values
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

    # Constructor with values
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:12:51.462882
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL == "https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html"

# Generated at 2022-06-14 17:12:56.195238
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Given
    url = 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html'
    self = TF1IE()

    # When
    tf1ie = self.tf1ie(url)

    # Then
    assert isinstance(tf1ie, TF1IE)