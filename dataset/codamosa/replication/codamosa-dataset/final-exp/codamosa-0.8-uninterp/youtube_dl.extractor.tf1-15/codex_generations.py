

# Generated at 2022-06-14 17:06:06.140546
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE()
    assert obj._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'


# Generated at 2022-06-14 17:06:08.395067
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Description of test_TF1IE"""
    test_TF1IE = TF1IE(None)
    assert test_TF1IE

# Generated at 2022-06-14 17:06:10.292713
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()

# Generated at 2022-06-14 17:06:11.287863
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE(None)

# Generated at 2022-06-14 17:06:18.835199
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Arrange
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    TF1IE_instance = TF1IE(url)

    # Act
    TF1IE_instance.extract()

    # Assert
    assert TF1IE_instance.url == url

# Generated at 2022-06-14 17:06:19.842138
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(InfoExtractor())

# Generated at 2022-06-14 17:06:22.172141
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")

# Generated at 2022-06-14 17:06:26.569402
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

    assert(ie.ie_key() == 'TF1')
    assert(ie.short_name() == 'TF1')
    assert(ie.url_result('foo') == 'TF1:foo')
    assert(ie.url_result('foo', 'bar') == 'TF1:foo')

# Generated at 2022-06-14 17:06:29.376118
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    tf1.extract('TF1IE')

# Generated at 2022-06-14 17:06:31.334924
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test case for class TF1IE
    """
    tester = TF1IE()
    assert tester != None

# Generated at 2022-06-14 17:06:47.380363
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # V1 : Test Youtube-like URL
    test = TF1IE()
    test.assertTrue(all(getattr(test, x) for x in ('_VALID_URL', '_TESTS', '_download_json', '_real_extract')))

    # V2 : Test Youtube-like URL
    test = TF1IE()
    test.assertTrue(all(getattr(test, x) for x in ('_VALID_URL', '_TESTS', '_download_json', '_real_extract')))

# Generated at 2022-06-14 17:06:52.398762
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE('wat:123')
    assert tf1ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/[^/]+/videos/[^/?&#]+\.html'
# end of unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:07:03.113557
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:07:08.122502
# Unit test for constructor of class TF1IE
def test_TF1IE():
    i = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    # Test the initialisation of _VALID_URL
    print(i._VALID_URL)
    # Test the initialisation of _TESTS
    print(i._TESTS)
    # Test the initialisation of _TEST
    print(i._TEST)

# Generated at 2022-06-14 17:07:08.717535
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE({})

# Generated at 2022-06-14 17:07:10.427310
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()._VALID_URL == TF1IE._VALID_URL

# Generated at 2022-06-14 17:07:18.256720
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:07:18.873242
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE

# Generated at 2022-06-14 17:07:29.547616
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()
    assert tf1ie.IE_NAME == 'tf1'
    assert tf1ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert tf1ie._TESTS[0]["url"] == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert tf1ie._TESTS[0]['info_dict']['id'] == '13641379'

# Generated at 2022-06-14 17:07:37.497679
# Unit test for constructor of class TF1IE
def test_TF1IE():
    my_TF1IE = TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    print('Programme slug :', my_TF1IE._program_slug)
    print('Video slug :', my_TF1IE._video_slug)
    print('JSON :', my_TF1IE._JSON)
    print('Youtube ID :', my_TF1IE._youtube_id)

# Generated at 2022-06-14 17:08:00.742258
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL

# Generated at 2022-06-14 17:08:06.843026
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.IE_NAME == 'tf1'
    assert ie.VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == None
    assert ie.IE_DESC == 'Tf1'


# Generated at 2022-06-14 17:08:11.626946
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie.ie_key() == 'tf1'
    assert ie.ie_key() in ie.supported_ie_keys()
    assert isinstance(ie.supported_ie_keys(), list)
    assert isinstance(ie._VALID_URL, basestring)

# Generated at 2022-06-14 17:08:18.842232
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    url = 'http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/replay-koh-lanta-22-mai-2015.html'
    actual = ie._real_extract(url)
    assert actual['id'] == '13641379'
    assert actual['ext'] == 'mp4'
    assert actual['title'] == 'md5:f392bc52245dc5ad43771650c96fb620'
    assert actual['description'] == 'md5:a02cdb217141fb2d469d6216339b052f'
    assert actual['upload_date'] == '20190611'
    assert actual['timestamp'] == 1560273989
    assert actual['duration'] == 1738
    assert actual

# Generated at 2022-06-14 17:08:27.678991
# Unit test for constructor of class TF1IE
def test_TF1IE():
    testObject = TF1IE()
    assert testObject._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:37.229324
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:42.078790
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert isinstance(IE, InfoExtractor)

# Generated at 2022-06-14 17:08:51.994463
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None).get_info('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    TF1IE(None).get_info('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    TF1IE(None).get_info('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')

# Generated at 2022-06-14 17:08:55.474760
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:09:00.485710
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html', None)

# Generated at 2022-06-14 17:09:24.226045
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE("id")
    try:
        assert instance.id != None
        assert instance.re != None
    except Exception:
        pass

# Generated at 2022-06-14 17:09:26.243147
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')

# Generated at 2022-06-14 17:09:37.682920
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:09:43.634471
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Pass
    """
    url = "https://www.tf1.fr/divertissement/the-voice/videos/the-voice-joe-soul_BU08053987"
    TF1IE()._real_extract(url)

# Generated at 2022-06-14 17:09:54.716395
# Unit test for constructor of class TF1IE
def test_TF1IE():
    wat_id = "13641379"
    test_url_TF1_video = "https://www.tf1.fr/graphql/web"
    test_TF1_video_data = {'id': wat_id, 'variables': json.dumps({'programSlug': 'quotidien-avec-yann-barthes', 'slug': 'quotidien-premiere-partie-11-juin-2019'})}

# Generated at 2022-06-14 17:09:56.124823
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("TF1IE", "tf1")

# Generated at 2022-06-14 17:09:57.672896
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None, None, None)

# Generated at 2022-06-14 17:09:59.006132
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test for constructor
    TF1IE(None)

# Generated at 2022-06-14 17:10:07.593522
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL == 'https?://(?:www\\.)?tf1\\.fr/[^/]+/([^/]+)/videos/([^/?&#]+).html'
    # Asserting True is the same as doing nothing
    assert TF1IE._TESTS[0]['params']['skip_download'] == True
    assert TF1IE._TESTS[1]['only_matching'] == True
    assert TF1IE._TESTS[2]['only_matching'] == True
    # Since we want to be sure everything is OK
    assert TF1IE._TESTS[0]['info_dict']['id'] == '13641379'
    assert TF1IE._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert TF

# Generated at 2022-06-14 17:10:08.236703
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:10:58.741291
# Unit test for constructor of class TF1IE
def test_TF1IE():
    '''Constructor method for TF1IE'''
    tf1 = TF1IE()
    assert tf1
    assert tf1._VALID_URL is not None
    assert tf1._TESTS is not None

# Generated at 2022-06-14 17:10:59.411999
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:11:08.330381
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.suitable('https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    ie.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    ie.suitable('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html')


# Generated at 2022-06-14 17:11:09.600752
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:11:11.403932
# Unit test for constructor of class TF1IE
def test_TF1IE():
    info_extractor = TF1IE()

    assert(info_extractor.params is None)

# Generated at 2022-06-14 17:11:12.766942
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE = InfoExtractor()
    TF1IE.tf1_ie()

# Generated at 2022-06-14 17:11:15.425233
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert TF1IE._VALID_URL == tf1._VALID_URL

# Generated at 2022-06-14 17:11:18.019451
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert ctor_test('TF1IE')


# Generated at 2022-06-14 17:11:25.533167
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t.suitable('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html') == True
    assert t.suitable('http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html') == True
    assert t.suitable('http://www.tf1.fr/tf1/les-12-coups-de-midi/videos/emission-du-14-juin-2019-partie-1.html') == True

# Generated at 2022-06-14 17:11:27.067691
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE('TF1IE', 'tf1.fr')

# Generated at 2022-06-14 17:13:37.158397
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_video = TF1IE()

if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:13:38.343578
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert(True is True)

# Generated at 2022-06-14 17:13:47.695089
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert tf1.url == 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    assert tf1.id == '13641379'
    assert tf1.slug == 'quotidien-premiere-partie-11-juin-2019'

# Generated at 2022-06-14 17:13:58.475015
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test _VALID_URL
    assert TF1IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

    # Test _TESTS

# Generated at 2022-06-14 17:14:07.295972
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html
    """
    program_slug, slug = 'koh-lanta', 'replay-koh-lanta-22-mai-2015'
    id = '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f'
    variables = {'programSlug': program_slug, 'slug': slug}
    query = {'id': '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f', 'variables': json.dumps(variables)}

# Generated at 2022-06-14 17:14:07.676427
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:14:10.008272
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # When testing constructor of class TF1IE,
    # we need to start a instance of class InfoExtractor first.
    InfoExtractor()


# Generated at 2022-06-14 17:14:10.619392
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:14:11.734164
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()

# Generated at 2022-06-14 17:14:12.470878
# Unit test for constructor of class TF1IE
def test_TF1IE():
    x = TF1IE()
    assert isinstance(x, TF1IE)