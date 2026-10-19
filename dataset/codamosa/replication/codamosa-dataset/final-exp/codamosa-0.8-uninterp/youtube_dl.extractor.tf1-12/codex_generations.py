

# Generated at 2022-06-14 17:06:11.725812
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Illegal URL
    with pytest.raises(ExtractorError) as e:
        tf1ie = TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015")
    # legal URL
    tf1ie = TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert tf1ie._VALID_URL == "https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html"

# Generated at 2022-06-14 17:06:16.641086
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert isinstance(ie, TF1IE)
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:17.157756
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:20.222499
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    print(ie.IE_NAME)
    print(ie.ie_key())

# Generated at 2022-06-14 17:06:23.271213
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')


# Generated at 2022-06-14 17:06:29.985764
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Unit test of constructor of class TF1IE
    input_url = "http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
    input_webpage = ""
    input_video_id = "replay-koh-lanta-22-mai-2015"

    instance_TF1IE = TF1IE()
    instance_TF1IE._real_extract(input_url)
    assert instance_TF1IE.video_id is input_video_id

# Generated at 2022-06-14 17:06:36.150012
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    expected_output = {
        '_type': 'url_transparent',
        'ie_key': 'TF1',
        'url': url
    }
    ie = TF1IE(url)
    assert ie.__dict__ == expected_output

# Generated at 2022-06-14 17:06:42.025534
# Unit test for constructor of class TF1IE
def test_TF1IE():
    class_ = TF1IE
    assert class_.get_vid_from_url("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html") == "replay-koh-lanta-22-mai-2015"
    assert class_.get_program_from_url("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html") == "koh-lanta"

# Generated at 2022-06-14 17:06:43.405186
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test to make sure the constructor runs correctly
    TF1IE()

# Generated at 2022-06-14 17:06:45.178572
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert IE != None

# Generated at 2022-06-14 17:06:53.354862
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE_test1 = TF1IE()
    assert isinstance(TF1IE_test1, TF1IE)

# Generated at 2022-06-14 17:06:54.862469
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == TF1IE._VALID_URL

# Generated at 2022-06-14 17:07:02.447329
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.IE_NAME == 'tf1'
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert ie.BR_DESC == 'Replay et direct 🗲 de la chaîne france 2 : Les JT, les séries, les films, tous les programme en replay et toutes les émissions à voir et à revoir'

# Generated at 2022-06-14 17:07:04.069561
# Unit test for constructor of class TF1IE
def test_TF1IE():
    test_TF1IE = TF1IE(None, None)
    assert test_TF1IE is not None

# Generated at 2022-06-14 17:07:06.583422
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:07:09.035238
# Unit test for constructor of class TF1IE
def test_TF1IE():
    global TF1IE
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:07:10.733655
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE(None)
    assert isinstance(obj, TF1IE)

# Generated at 2022-06-14 17:07:14.762829
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:07:16.137781
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE(None)
    assert tf1ie.name == 'tf1.fr'

# Generated at 2022-06-14 17:07:18.055151
# Unit test for constructor of class TF1IE
def test_TF1IE():
   tp_tf1 = TF1IE()
   print(tp_tf1)
#

# Generated at 2022-06-14 17:07:32.023162
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # TF1IE defined in __init__.py
    assert WatIE.ie_key() == 'wat'

# Generated at 2022-06-14 17:07:36.341023
# Unit test for constructor of class TF1IE
def test_TF1IE():
    with open('tf1.json') as f:
        json_data = json.load(f)
    print(json_data)
    res = TF1IE._real_extract(json_data)
    print(res)


if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:07:37.081500
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE().extract('')

# Generated at 2022-06-14 17:07:39.261008
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    tf1ie._VALID_URL = re.compile(TF1IE._VALID_URL)

# Generated at 2022-06-14 17:07:46.518174
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert t._VALID_URL == "https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html"

# Generated at 2022-06-14 17:07:56.879890
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    tf1.get_url() == 'wat:VDB0'
    tf1.get_title() == 'Mylène Farmer, d\'une icône'
    tf1.get_description() == 'Catherine Rambert retrace sur HD1 dans Documenteurs le parcours hors norme de la chanteuse étiquetée "icône de la musique française".'
    tf1.get_thumbnail() == 'http://r-image-prod.com/CDN/image/origin/HD1/2016/09/28/HD1_Documenteurs_S_Icard_S__161003_0000_A.jpg'

# Generated at 2022-06-14 17:07:59.101908
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract(test_TF1IE.__doc__)

# Generated at 2022-06-14 17:08:03.280273
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from .test_download_common import _test_download_ie
    tf1 = TF1IE({})
    _test_download_ie(tf1, 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:08:07.431074
# Unit test for constructor of class TF1IE
def test_TF1IE():
	url = "https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html"
	TF1IE_unit_test = TF1IE()
	TF1IE_unit_test.suitable(url)
	TF1IE_unit_test._real_extract(url)

# Generated at 2022-06-14 17:08:08.862932
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Just test if the constructor works
    """
    TF1IE()

# Generated at 2022-06-14 17:08:35.145193
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Check if TF1IE is initialized
    assert TF1IE()._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:45.379770
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info_extractor = TF1IE()
    for test in info_extractor._TESTS:
        url = test.get('url')
        program_slug, slug = re.match(info_extractor._VALID_URL, url).groups()
        video = info_extractor._download_json(
            'https://www.tf1.fr/graphql/web', slug, query={
                'id': '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f',
                'variables': json.dumps({
                    'programSlug': program_slug,
                    'slug': slug,
                })
            })['data']['videoBySlug']
        wat_id = video['streamId']

       

# Generated at 2022-06-14 17:08:51.269374
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Should work with a URL as input
    assert TF1IE().suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    # Should work with a ID as input
    assert TF1IE().suitable('13641379') == True

# Generated at 2022-06-14 17:08:52.289979
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Smoke test
    TF1IE({})

# Generated at 2022-06-14 17:08:55.339072
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract('https://www.tf1.fr/tf1-series-films/the-voice/videos/the-voice-6-mai-2015-replay.html')

# Generated at 2022-06-14 17:08:57.247325
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:08:59.415493
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t.__class__.__name__ == "TF1IE"

# Generated at 2022-06-14 17:09:08.804379
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test that TF1IE can be instantiated properly.
    """
    # Test the URL of a video on the TF1 website.
    TF1IE = TF1IE(
        'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    )
    # Test the URL of a video on the TMC website (which redirects to TF1).
    TF1IE = TF1IE(
        'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    )

# Generated at 2022-06-14 17:09:17.459005
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t.suitable("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert t.suitable("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert t.suitable("https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")
    assert not t.suitable("https://wat.tv/get/android5/401621c5df_bg_16600000k-500000000k.mp4")

# Generated at 2022-06-14 17:09:18.431433
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None, None)

# Generated at 2022-06-14 17:09:53.582474
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.IE_NAME == 'tf1'
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert ie._API_BASE == 'https://www.tf1.fr/graphql/web'

# Generated at 2022-06-14 17:09:56.026104
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:09:58.026552
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert isinstance(t, TF1IE)

# Generated at 2022-06-14 17:09:59.747259
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 17:10:05.925745
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    obj = InfoExtractor.getInfoExtractor(url).IE_NAME
    assert obj == TF1IE.IE_NAME

# Generated at 2022-06-14 17:10:09.533494
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tester = TF1IE()
    print(tester.playlist_result('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'))

# Generated at 2022-06-14 17:10:10.832605
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE('TF1IE')
    obj.set_player_url

# Generated at 2022-06-14 17:10:15.768188
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert IE.IE_NAME == 'tf1'
    assert IE.IE_DESC == 'TF1'
    assert IE.valid_url('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert IE.valid_url('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    assert not IE.valid_url('https://www.gamersyde.com/')

# Generated at 2022-06-14 17:10:23.075763
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')


# Generated at 2022-06-14 17:10:26.609409
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._real_extract('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:11:27.026358
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert IE.__name__ == 'TF1'
    assert IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert IE.IE_NAME == 'tf1'

# Generated at 2022-06-14 17:11:27.872460
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE("")

# Generated at 2022-06-14 17:11:34.949885
# Unit test for constructor of class TF1IE
def test_TF1IE():
    example_url = ['https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html',
                   'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html',
                   'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html']
    tester = TF1IE()
    assert [tester.suitable(x) for x in example_url] == [True, True, True]

# Generated at 2022-06-14 17:11:36.476109
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Check if TF1IE can be instantiated
    """
    TF1IE("")

# Generated at 2022-06-14 17:11:37.766972
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.suitable()
    ie.download()


# Generated at 2022-06-14 17:11:38.421559
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:11:40.503844
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")

# Generated at 2022-06-14 17:11:40.953008
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:11:41.374489
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:11:44.080685
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test an example match."""
    match = TF1IE._VALID_URL
    assert match('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert TF1IE._match_id('wat:1234') == '1234'

# Generated at 2022-06-14 17:13:54.956282
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html");

# Generated at 2022-06-14 17:13:56.788131
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    assert tf1.tf1_class_instantiates()


# Generated at 2022-06-14 17:14:07.218817
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert re.match(TF1IE._VALID_URL, 'https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')
    assert re.match(TF1IE._VALID_URL, 'https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert re.match(TF1IE._VALID_URL, 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:14:08.850089
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._real_extract(TF1IE._TESTS[0])

# Generated at 2022-06-14 17:14:10.314690
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1 is not None

# Generated at 2022-06-14 17:14:10.908288
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE({})

# Generated at 2022-06-14 17:14:13.271978
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:14:16.181461
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    tf1._real_extract("http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")

# Generated at 2022-06-14 17:14:20.200025
# Unit test for constructor of class TF1IE
def test_TF1IE():
    from wptransparent import WATIE
    wat_ie = WATIE()
    tf1_ie = TF1IE(wat_ie)
    assert tf1_ie.ie_key() == 'tf1'

# Generated at 2022-06-14 17:14:30.417730
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Unit test for constructor of class TF1IE
    """