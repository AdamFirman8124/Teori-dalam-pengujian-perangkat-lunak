

# Generated at 2022-06-14 17:06:01.926341
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass


# Generated at 2022-06-14 17:06:14.114076
# Unit test for constructor of class TF1IE
def test_TF1IE():
    objects_urls = [('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html', 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')]
    for test_url in objects_urls:
        assert TF1IE.suitable(test_url[0]) == True
        assert TF1IE.link_re.match(test_url[0]) is not None
        assert TF1IE._VALID_URL in test_url[0], '%r invalid'%test_url
        assert TF1IE._TESTS[0]['url'] in test_url[0], '%r invalid'%test_url
       

# Generated at 2022-06-14 17:06:16.789376
# Unit test for constructor of class TF1IE
def test_TF1IE():

    # Test constructor should not raise an error
    try:
        TF1IE()
    except Exception as exception:
        assert False, exception



# Generated at 2022-06-14 17:06:19.082625
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:06:19.899143
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None)

# Generated at 2022-06-14 17:06:24.388183
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .common import InfoExtractor
    from .test_youtube import TestYouTubeIE
    from .helper import _extract_test, TestInfoExtractor

    # Test inheritance
    assert issubclass(TF1IE, InfoExtractor), 'TF1IE class should inherit from InfoExtractor'
    assert issubclass(TF1IE, TestInfoExtractor), 'TF1IE class should inherit from TestInfoExtractor'
    assert issubclass(TF1IE, TestYouTubeIE), 'TF1IE class should inherit from TestYouTubeIE'

# Generated at 2022-06-14 17:06:29.586471
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert re.match(TF1IE._VALID_URL, "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html").groups() == ('tmc/quotidien-avec-yann-barthes', 'quotidien-premiere-partie-11-juin-2019')

# Generated at 2022-06-14 17:06:30.677870
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()


# Generated at 2022-06-14 17:06:31.338700
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:06:36.003522
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE('test')
    assert tf1ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:45.045582
# Unit test for constructor of class TF1IE
def test_TF1IE():

    actual = TF1IE('TF1IE', 'TF1IE')
    assert actual.name == 'TF1IE'
    assert actual.ie_key == 'TF1IE'

# Generated at 2022-06-14 17:06:47.765781
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == TF1IE._VALID_URL
    assert TF1IE()._TESTS == TF1IE._TESTS

# Generated at 2022-06-14 17:06:49.155450
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE(None)
    assert isinstance(t, TF1IE)

# Generated at 2022-06-14 17:06:58.089864
# Unit test for constructor of class TF1IE
def test_TF1IE():
    global TF1IE
    t = TF1IE("http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert t.program_slug == "tmc/quotidien-avec-yann-barthes"
    assert t.slug == "quotidien-premiere-partie-11-juin-2019"
    assert t.id == "13641379"

# Generated at 2022-06-14 17:07:07.180612
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    with pytest.raises(RegexNotFoundError):
        TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
        # this url is not a "tf1" url, so exception must be raised
    TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:07:09.468611
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Unit test for constructor of class TF1IE"""
    assert isinstance(TF1IE(), InfoExtractor)

# Generated at 2022-06-14 17:07:13.943715
# Unit test for constructor of class TF1IE
def test_TF1IE():

    url = "http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
    ie = TF1IE(url)

    assert "https://www.tf1.fr/graphql/web" == ie.url

# Generated at 2022-06-14 17:07:15.785036
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:18.516730
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:07:24.014164
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE('TF1IE', 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert tf1ie.program_slug == 'koh-lanta'
    assert tf1ie.slug == 'replay-koh-lanta-22-mai-2015'

# Generated at 2022-06-14 17:07:36.976345
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:07:38.455900
# Unit test for constructor of class TF1IE
def test_TF1IE():
    print('test_TF1IE')
    video_test = TF1IE()

# Generated at 2022-06-14 17:07:42.033383
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert_equal(
        ie._VALID_URL,
        r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    )

# Generated at 2022-06-14 17:07:43.093998
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:44.483501
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:07:49.709538
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert instance._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert instance._downloader is not None
    assert isinstance(instance._downloader, InfoExtractor)
    assert instance._downloader._downloader is not None
    assert isinstance(instance._downloader._downloader, YoutubeDL)

# Generated at 2022-06-14 17:07:50.886909
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1Instance = TF1IE()

# Generated at 2022-06-14 17:07:51.882625
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:04.316819
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE().ie_key() == 'TF1'
    assert TF1IE()._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:06.800213
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_object = TF1IE()
    assert test_object is not None

# Generated at 2022-06-14 17:08:29.589180
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:08:32.169028
# Unit test for constructor of class TF1IE
def test_TF1IE():
    return TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:08:32.664252
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE

# Generated at 2022-06-14 17:08:36.270753
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._real_extract("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")


# Generated at 2022-06-14 17:08:40.955110
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .test_common import devnull
    with devnull():
        assert(TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'))

# Generated at 2022-06-14 17:08:44.244657
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:08:45.332652
# Unit test for constructor of class TF1IE
def test_TF1IE():
    print(TF1IE)

# Generated at 2022-06-14 17:08:56.255087
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info = TF1IE()._download_json(
        'https://www.tf1.fr/graphql/web',
        'redemption-island-episode-3-du-05-fevrier-2015',
        query={
            'id': '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f',
            'variables': json.dumps({
                'programSlug': 'koh-lanta',
                'slug': 'redemption-island-episode-3-du-05-fevrier-2015',
            })
        })['data']['videoBySlug']

    assert info['streamId'] == '13530127'

# Generated at 2022-06-14 17:08:57.339219
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:09:05.822857
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Unit test for constructor of class TF1IE
    # Test the initialization of TF1IE class
    data = TF1IE(None)

    # Test the setting of attributes by constructor of TF1 class
    assert data.ie_key() == 'TF1'
    assert data.ie_url() == 'http://www.tf1.fr/'
    assert data.http_header() == {
        'User-Agent': 'Wget/1.19.1 (linux-gnu)',
        'Accept-Encoding': '*',
        'Accept': '*/*'
    }

# Generated at 2022-06-14 17:09:51.808590
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ens = InfoExtractor(TF1IE)

# Generated at 2022-06-14 17:09:53.072418
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert(TF1IE.__name__ == "TF1IE")

# Generated at 2022-06-14 17:09:58.660245
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    match = t._VALID_URL.match(url)
    input_data = (match.groups())
    print(input_data[0])
    print(input_data[1])
    video_data = json.loads(input_data[1])
    print(video_data['data'])
    tags = []
    for tag in (try_get(video_data['tags'], list) or []):
        label = tag.get('label')
        if not label:
            continue
        tags.append(label)
    print(tags[0])

# Generated at 2022-06-14 17:10:07.427169
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Unit test for TF1IE"""
    # Unit test for constructor of class TF1IE
    tf1_ie = TF1IE()
    assert tf1_ie is not None

    # Unit test for class TF1IE.url_result()
    url_result = tf1_ie.url_result
    assert url_result is not None

    # Unit test for class TF1IE._html_search_regex()
    html_search_regex = tf1_ie._html_search_regex
    assert html_search_regex is not None

    # Unit test for class TF1IE._real_extract()
    real_extract = tf1_ie._real_extract
    assert real_extract is not None

    # Unit test for class TF1IE._download_json()
    download_json = tf1_ie._download

# Generated at 2022-06-14 17:10:08.422145
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:10:09.179327
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()



# Generated at 2022-06-14 17:10:16.368319
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .common import InfoExtractor, SkipTest
    from .tf1 import TF1IE
    from ..compat import compat_urllib_parse
    from ..utils import compat_str
    import urllib.parse

    assert issubclass(TF1IE, InfoExtractor)


# Generated at 2022-06-14 17:10:17.831740
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()

# Generated at 2022-06-14 17:10:18.993328
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.ie_key() == 'tf1'

# Generated at 2022-06-14 17:10:30.348435
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    # This test was written based on the results of this query:
    # https://www.tf1.fr/graphql/web?id=9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f&variables={"programSlug":"quotidien-avec-yann-barthes","slug":"quotidien-premiere-partie-11-juin-2019"}
    instance = TF1IE(url)
    assert instance.tld == 'fr'

# Generated at 2022-06-14 17:12:27.411340
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:12:31.091471
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.ie_key() == 'tf1'
    assert tf1.IE_NAME == 'TF1'
    assert tf1.ie_key() in globals()
    assert tf1.SUCCESS.items() == [('status', 'ok'), ('message', 'Object created')]

# Generated at 2022-06-14 17:12:34.617174
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:12:36.937918
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # If the unit test fails, remove the following line
    pass

# Generated at 2022-06-14 17:12:40.835360
# Unit test for constructor of class TF1IE
def test_TF1IE():
	video = TF1IE()
	assert video.url == 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'

# Generated at 2022-06-14 17:12:42.758812
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test case for constructor of TF1IE class.
    """
    instance = TF1IE()
    assert isinstance(instance, TF1IE)

# Generated at 2022-06-14 17:12:47.377247
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ietest = TF1IE()
    assert ietest._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:12:57.722258
# Unit test for constructor of class TF1IE
def test_TF1IE():
    constructor_test(TF1IE, [
        'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html',
        'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html',
        'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html',
    ])

# Generated at 2022-06-14 17:13:00.687181
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info_extractor = TF1IE()
    assert info_extractor.ie_key() == 'TF1'
    assert info_extractor.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:13:01.631294
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()