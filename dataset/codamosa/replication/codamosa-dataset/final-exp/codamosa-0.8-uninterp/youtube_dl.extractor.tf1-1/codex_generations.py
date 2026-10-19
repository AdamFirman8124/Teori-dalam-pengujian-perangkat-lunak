

# Generated at 2022-06-14 17:06:03.634788
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:15.800192
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    ie.extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    ie.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:06:16.384851
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:06:17.916532
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._get_test()

# Generated at 2022-06-14 17:06:28.622429
# Unit test for constructor of class TF1IE
def test_TF1IE():
    infoExtractor = TF1IE()
    assert infoExtractor._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:34.522785
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('TF1', 'quotidien-avec-yann-barthes', 'quotidien-premiere-partie-11-juin-2019')
    assert(ie.program_slug == 'quotidien-avec-yann-barthes')
    assert(ie.slug == 'quotidien-premiere-partie-11-juin-2019')

# Generated at 2022-06-14 17:06:37.487301
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/', 'test')

# Generated at 2022-06-14 17:06:48.370565
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert tf1.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert not tf1.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html2')
    assert tf1.suitable('https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    assert tf1._VALID

# Generated at 2022-06-14 17:06:51.397365
# Unit test for constructor of class TF1IE
def test_TF1IE():
    '''
    Unit test for TF1IE
    '''
    inst_TF1IE = TF1IE()
    assert inst_TF1IE

# Generated at 2022-06-14 17:06:53.443084
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1 is not None

# Generated at 2022-06-14 17:07:08.314785
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t._VALID_URL == 'https?://(?:www\\.)?tf1\\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\\.html'

# Generated at 2022-06-14 17:07:09.353509
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(InfoExtractor)

# Generated at 2022-06-14 17:07:14.817878
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()
    # test for url of class
    assert tf1IE._VALID_URL == re.compile(r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html')
    # test for name of class
    assert tf1IE._NAME == 'TF1'
    # test for class fields

# Generated at 2022-06-14 17:07:25.968731
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:34.495637
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE_instance = TF1IE()
    assert(TF1IE_instance.suitable('https://www.video.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'))
    assert(TF1IE_instance.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'))

# Generated at 2022-06-14 17:07:40.051153
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._valid_url(TF1IE._TESTS[0]['url'], TF1IE._VALID_URL)
    assert TF1IE._valid_url(TF1IE._TESTS[1]['url'], TF1IE._VALID_URL)
    assert TF1IE._valid_url(TF1IE._TESTS[2]['url'], TF1IE._VALID_URL)

# Generated at 2022-06-14 17:07:44.606007
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE().ie_key() == 'TF1'
    assert TF1IE().info_url_key() == 'url'


# Generated at 2022-06-14 17:07:53.495337
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    program_slug, id_video = re.match(ie._VALID_URL, 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html').groups()
    # Get real values also for the unit test

# Generated at 2022-06-14 17:07:58.310234
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('wat:L0KZKjX0cT')
    assert ie.ie_key() == 'wat'
    assert ie.SUITABLE_VIDEO_EXTENSIONS == ['mp4']

# Generated at 2022-06-14 17:07:59.105910
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:12.669336
# Unit test for constructor of class TF1IE
def test_TF1IE():
	ie = TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:08:15.191084
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE

# Generated at 2022-06-14 17:08:19.980240
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """ TF1IE test method: basic unit test for TF1IE constructor """
    from .test import make_test_info_extractor_object
    info_extractor = make_test_info_extractor_object(TF1IE)
    assert info_extractor.get_downloader(TF1IE.IE_NAME) is not None


# Generated at 2022-06-14 17:08:27.918215
# Unit test for constructor of class TF1IE
def test_TF1IE():
    video = TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert(video._VALID_URL == re.compile(r'(?x)\Ahttps?://(?:www\.)?tf1\.fr/(?P[^/]+)/[^/]+/videos/(?P[^/?&#]+)\.html\Z'))
    assert(video.program_slug == "koh-lanta")
    assert(video.slug == "replay-koh-lanta-22-mai-2015")
    assert(video.videoBySlug["streamId"] == "8444414")

# Generated at 2022-06-14 17:08:31.103398
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:08:36.850770
# Unit test for constructor of class TF1IE
def test_TF1IE():
    i = TF1IE()
    assert i._VALID_URL.find('www.tf1.fr/') > -1
    print(json.dumps(i._TESTS))
    assert json.dumps(i._TESTS).find('intégrale') > -1
    print(i._real_extract)
    assert i._real_extract
    assert i._download_json

# Generated at 2022-06-14 17:08:37.877058
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE()

# Generated at 2022-06-14 17:08:39.564934
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:47.791499
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE('http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert obj.url == 'http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert obj._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:57.473237
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:09:25.350715
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:09:36.984004
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')._real_extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')._real_extract('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    TF1

# Generated at 2022-06-14 17:09:40.475893
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    t._real_extract("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    t._download_json("https://www.tf1.fr/graphql/web", "quotidien-premiere-partie-11-juin-2019")
# End of unit testing

# Generated at 2022-06-14 17:09:41.762925
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()



# Generated at 2022-06-14 17:09:43.031674
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_TF1IE = TF1IE()
    assert test_TF1IE

# Generated at 2022-06-14 17:09:48.647908
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .common import InfoExtractor
    from .playlist import PlaylistIE
    from .wat import WatIE

    assert issubclass(TF1IE, InfoExtractor)
    assert issubclass(TF1IE, PlaylistIE)
    assert issubclass(TF1IE, WatIE)


# Generated at 2022-06-14 17:09:49.809337
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._TESTS

# Generated at 2022-06-14 17:09:51.849703
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test = TF1IE()
    test_str = str(test)
    assert test_str == '<TF1IE>'

# Generated at 2022-06-14 17:09:55.863147
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE(None)
    assert (re.match(IE._VALID_URL,
                     'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html') != None)
    assert (re.match(IE._VALID_URL,
                     'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html') != None)
    assert (re.match(IE._VALID_URL,
                     'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html') != None)

# Generated at 2022-06-14 17:09:57.885946
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.suitable(TF1IE._VALID_URL)

# Generated at 2022-06-14 17:10:52.740933
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE(InfoExtractor())._VALID_URL == TF1IE._VALID_URL
    assert TF1IE(InfoExtractor())._TESTS == TF1IE._TESTS

# Generated at 2022-06-14 17:10:53.811424
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:10:54.882536
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL

# Generated at 2022-06-14 17:11:02.456743
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE(None)

    # Test '_VALID_URL' of class TF1IE
    assert(ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html')

    # Test '_TESTS' of class TF1IE

# Generated at 2022-06-14 17:11:06.064170
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    tf1.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')


# Generated at 2022-06-14 17:11:07.768113
# Unit test for constructor of class TF1IE
def test_TF1IE():
    iet = TF1IE()
    assert iet.name == "TF1"

# Generated at 2022-06-14 17:11:11.311379
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:11:22.964269
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE('http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert tf1.url == 'http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert tf1.VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:11:34.390762
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_string = ['https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html',
                   'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html',
                   'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html',
                   "https://www.tf1.fr/tf1/all-inclusive/videos/all-inclusive-la-finale-pensez-a-bip-bip-et-coyote.html"]
    return_string = ['1234567']
    ie = InfoExtractor(TF1IE, test_string)


# Generated at 2022-06-14 17:11:41.125872
# Unit test for constructor of class TF1IE
def test_TF1IE():
    value_1 = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    obj_1 = TF1IE('test', value_1)
    assert obj_1._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:13:54.444580
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.IE_NAME == TF1IE.ie_key()
    assert ie._VALID_URL == TF1IE.VALID_URL
    assert ie._TESTS == TF1IE.TESTS

# Generated at 2022-06-14 17:13:59.389611
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test a valid url
    url = TF1IE._TESTS[0]['url']
    assert TF1IE._VALID_URL.match(url)

    info_dict = TF1IE._TESTS[0]['info_dict']
    assert info_dict['id'] == '13641379'
    assert info_dict['ext'] == 'mp4'
    assert info_dict['title'] == 'md5:f392bc52245dc5ad43771650c96fb620'
    assert info_dict['description'] == 'md5:a02cdb217141fb2d469d6216339b052f'
    assert info_dict['upload_date'] == '20190611'
    assert info_dict['timestamp'] == 1560273989
    assert info_dict['duration'] == 1738


# Generated at 2022-06-14 17:14:00.030692
# Unit test for constructor of class TF1IE
def test_TF1IE():
    return TF1IE()

# Generated at 2022-06-14 17:14:02.788774
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:14:04.367562
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert type(t) == TF1IE

# Generated at 2022-06-14 17:14:07.544304
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('', {})

# Generated at 2022-06-14 17:14:11.583032
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test1 = TF1IE()
    assert test1._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:14:13.470578
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.ie_key() == 'tf1'

# Generated at 2022-06-14 17:14:19.516849
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'

    #test_obj = unit_test_class(url)
    test_obj = TF1IE()
    assert test_obj._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:14:20.565633
# Unit test for constructor of class TF1IE
def test_TF1IE():
    i = TF1IE()