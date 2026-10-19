

# Generated at 2022-06-14 17:06:10.407950
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert t.program_slug == 'koh-lanta'
    assert t.slug == 'replay-koh-lanta-22-mai-2015'
    assert t.api_query() == {
        'id': '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f',
        'variables': json.dumps({
            'programSlug': 'koh-lanta',
            'slug': 'replay-koh-lanta-22-mai-2015'
        })
    }

# Generated at 2022-06-14 17:06:22.153595
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert TF1IE._TESTS[0]['url'] == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert TF1IE._TESTS[0]['info_dict']['id'] == '13641379'
    assert TF1IE._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:06:22.784251
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:26.698839
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test for case where we get a search result for the query
    TF1IE(None, 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html').go()

# Generated at 2022-06-14 17:06:36.229926
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    tf1.url = "https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
    tf1.program_slug = "koh-lanta"
    tf1.id = "replay-koh-lanta-22-mai-2015"
    assert tf1.program_slug == "koh-lanta"
    assert tf1.id == "replay-koh-lanta-22-mai-2015"


# Generated at 2022-06-14 17:06:42.057947
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test instantiation
    IE = TF1IE()
    # Test type
    assert IE.IE_NAME == 'tf1'
    # Test get info
    info = IE.extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert info['id'] == '13641379'
    assert info['ext'] == 'mp4'
    assert info['title'] == 'Quotidien – Première partie - 11 juin 2019'
    assert info['description'] == 'Retrouvez la première partie du "Quotidien" de cette semaine avec Yann Barthès.'
    assert info['upload_date'] == '20190611'


# Generated at 2022-06-14 17:06:44.408584
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE._download_json = lambda *args, **kwargs: {}
    TF1IE('wat:123')

# Generated at 2022-06-14 17:06:46.657505
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:48.210700
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None)._real_extract(None)

# Generated at 2022-06-14 17:07:00.356928
# Unit test for constructor of class TF1IE
def test_TF1IE():
    def instantiate_exception_raised(args, kwargs):
         try:
             TF1IE(*args, **kwargs)
             raise
         except Exception:
             pass

    # Invalid URL
    instantiate_exception_raised([], {"url": ''})
    instantiate_exception_raised([], {"url": 'http://www.tf1.fr'})
    assert (not instantiate_exception_raised([], {"url": 'http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'}))

    # Call constructor of class InfoExtractor

# Generated at 2022-06-14 17:07:16.711246
# Unit test for constructor of class TF1IE
def test_TF1IE():
    video_url = 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    assert TF1IE._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:17.809613
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()

# Generated at 2022-06-14 17:07:19.344708
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE()
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-14 17:07:20.786549
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == TF1IE._VALID_URL

# Generated at 2022-06-14 17:07:22.225418
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("TF1IE", 1)



# Generated at 2022-06-14 17:07:25.699902
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    TF1IE(url)

# Generated at 2022-06-14 17:07:35.209423
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Add a test method to the TF1IE class to grab the video
    "Quotidien : Première partie - 11 juin 2019".
    """
    TestTF1IE = TF1IE({'extractor': 'TF1IE', 'url': 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'})
    expected_title = "md5:f392bc52245dc5ad43771650c96fb620"
    expected_description = "md5:a02cdb217141fb2d469d6216339b052f"
    expected_date = "20190611"
    expected_duration = "1738"

# Generated at 2022-06-14 17:07:43.230605
# Unit test for constructor of class TF1IE
def test_TF1IE():
    print('test TF1IE')
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    # url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    tf1 = TF1IE()
    res = tf1._real_extract(url)
    print(json.dumps(res, indent=4, sort_keys=True))

if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:07:50.126954
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    test_program_slug = "tmc/quotidien-avec-yann-barthes"
    test_slug = "quotidien-premiere-partie-11-juin-2019"

    test_tf1 = TF1IE(test_url)

    assert test_tf1.program_slug == test_program_slug
    assert test_tf1.slug == test_slug

# Generated at 2022-06-14 17:07:51.302890
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None, None)

# Generated at 2022-06-14 17:08:02.432840
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:03.094256
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:08:09.349406
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = "https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
    og = TF1IE()
    og.suitable(url)
    og.extract(url)
    assert True

# Generated at 2022-06-14 17:08:12.381908
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert instance.ie_key() == 'TF1'
    assert instance.server_info().get('id') == 'tf1'

# Generated at 2022-06-14 17:08:13.432315
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.__name__ == 'TF1IE'

# Generated at 2022-06-14 17:08:17.484750
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from wat import WatExtractor
    assert isinstance(
        TF1IE._build_extractor({'wat_id': 'foobar'}),
        WatExtractor
    )

# Generated at 2022-06-14 17:08:19.122786
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.__name__ == 'TF1IE'

# Generated at 2022-06-14 17:08:20.163481
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1IE = TF1IE()

# Generated at 2022-06-14 17:08:21.131699
# Unit test for constructor of class TF1IE
def test_TF1IE():
	assert TF1IE()


# Generated at 2022-06-14 17:08:22.041171
# Unit test for constructor of class TF1IE
def test_TF1IE():
    a = TF1IE()
    assert a is not None

# Generated at 2022-06-14 17:08:49.915279
# Unit test for constructor of class TF1IE
def test_TF1IE():
    input_url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    output_url = 'wat:13641379'
    test_result = TF1IE()
    assert test_result.extract(input_url)["url"] == output_url

# Generated at 2022-06-14 17:08:50.966546
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE(TF1IE.IE_NAME)

# Generated at 2022-06-14 17:08:52.790756
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE('88888888')
    assert tf1ie.ie_key() == 'TF1'

# Generated at 2022-06-14 17:08:54.354542
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    print(tf1)

# Generated at 2022-06-14 17:08:55.296505
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE("TF1")

# Generated at 2022-06-14 17:08:57.695720
# Unit test for constructor of class TF1IE
def test_TF1IE():
    item = TF1IE()

# Generated at 2022-06-14 17:08:58.999335
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:09:09.400097
# Unit test for constructor of class TF1IE
def test_TF1IE():
    result1 = TF1IE()._real_extract( # pylint: disable=no-value-for-parameter
        'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert result1['id'] == '13641379'
    assert result1['ext'] == 'mp4'
    assert result1['description'] == 'md5:a02cdb217141fb2d469d6216339b052f'
    assert result1['tags'] == ['intégrale', 'quotidien', 'Replay']


# Generated at 2022-06-14 17:09:17.747860
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    tf1.extract('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    tf1.extract('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:09:18.336858
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:10:02.369546
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:10:13.229189
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()

# Generated at 2022-06-14 17:10:14.595994
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert True

# Generated at 2022-06-14 17:10:20.655069
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert hasattr(TF1IE, "_download_webpage")
    assert hasattr(TF1IE, "_search_regex")
    assert hasattr(TF1IE, "_download_json")
    assert hasattr(TF1IE, "_real_extract")
    assert hasattr(TF1IE, "suitable")
    assert TF1IE.__name__ == "TF1IE"
    assert TF1IE.__doc__ is not None


# Generated at 2022-06-14 17:10:23.945470
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE()

# Generated at 2022-06-14 17:10:27.366152
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test class TF1IE
    """
    tf1 = TF1IE()
    assert tf1.name == 'TF1'
    assert tf1.ie_key() == 'TF1'
    assert tf1.thumbnail() is None

# Generated at 2022-06-14 17:10:35.789454
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE(googletest.FakeYoutubeIE(), 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert ie.url_suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert ie.url_suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:10:38.837119
# Unit test for constructor of class TF1IE
def test_TF1IE():
    extractor = TF1IE()
    assert extractor._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:10:44.294929
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    TF1IE(url)


# Generated at 2022-06-14 17:10:48.269277
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE()
    assert obj._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'


# Generated at 2022-06-14 17:12:51.756975
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert ie.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert ie.suitable('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    assert not ie.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/11-juin-2019.html')
    assert not ie

# Generated at 2022-06-14 17:12:52.362234
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:12:55.946778
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Testing TF1IE constructor"""
    ie = TF1IE()
    assert ie._VALID_URL.startswith('https?://(?:www\.)?tf1\.fr/[^/]+/[^/]+/videos/')

# Generated at 2022-06-14 17:13:02.787338
# Unit test for constructor of class TF1IE
def test_TF1IE():
    w = TF1IE()
    assert w._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:13:11.984311
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL.match('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html') is not None
    assert TF1IE._VALID_URL.match('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html') is not None

#Unit test for _real_extract of class TF1IE

# Generated at 2022-06-14 17:13:17.395870
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE()
    except Exception as e:
        return e
    else:
        return None

print(test_TF1IE())

# Generated at 2022-06-14 17:13:28.142322
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert instance._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert instance._TESTS[0]['url'] == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert instance._TESTS[0]['info_dict']['id'] == '13641379'
    assert instance

# Generated at 2022-06-14 17:13:32.152601
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('')
    assert isinstance(ie, TF1IE)

# Generated at 2022-06-14 17:13:33.316599
# Unit test for constructor of class TF1IE
def test_TF1IE():
    m = TF1IE()


# Generated at 2022-06-14 17:13:40.924491
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test for _VALID_URL
    tf1 = TF1IE(url='https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    # Test returns program_slug
    assert tf1.program_slug == 'quotidien-avec-yann-barthes'
    # Test returns slug for use in GraphQL API
    assert tf1.slug == 'quotidien-premiere-partie-11-juin-2019'