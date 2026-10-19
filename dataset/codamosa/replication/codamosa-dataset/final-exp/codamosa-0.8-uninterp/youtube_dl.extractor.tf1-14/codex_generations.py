

# Generated at 2022-06-14 17:06:01.356881
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:03.821817
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    ie.extract("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")

# Generated at 2022-06-14 17:06:04.606073
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:06:06.483708
# Unit test for constructor of class TF1IE
def test_TF1IE():
    constructor_test(TF1IE, {
        'tf1_video_id': '13641379',
    })

# Generated at 2022-06-14 17:06:18.289874
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # This test should cover all attributes of TF1IE class which are used in
    # TF1IE constructor.
    TF1IE(None)._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:28.654595
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:06:29.605016
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tfie=TF1IE()

# Generated at 2022-06-14 17:06:33.287155
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Arrange
    url = 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html'
    tF1IE = TF1IE(url)
    # Act
    result = tF1IE.extract(url)
    # Assert
    assert result == 'echo $url;'

# Generated at 2022-06-14 17:06:34.320939
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert isinstance(TF1IE(), InfoExtractor)

# Generated at 2022-06-14 17:06:40.178814
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Without argument
    check_class(TF1IE)

    # With argument
    check_class(TF1IE, 'http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')

# Generated at 2022-06-14 17:06:55.516593
# Unit test for constructor of class TF1IE

# Generated at 2022-06-14 17:07:01.219960
# Unit test for constructor of class TF1IE
def test_TF1IE():
    entry = TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")
    assert entry._VALID_URL == r'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:07:02.182916
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1ie = TF1IE()

# Generated at 2022-06-14 17:07:06.471013
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert ie.program_slug == 'koh-lanta'
    assert ie.slug == 'replay-koh-lanta-22-mai-2015'

# Generated at 2022-06-14 17:07:15.205284
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()

    url = 'http://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'

    for item in tf1._VALID_URL, tf1._TESTS[0]['url']:
        assert tf1._match_id(item)

    print(tf1._real_extract(url))

    return tf1

if __name__ == '__main__':
    test_TF1IE()

# Generated at 2022-06-14 17:07:17.403935
# Unit test for constructor of class TF1IE
def test_TF1IE():
    _TF1IE = TF1IE()
    assert isinstance(_TF1IE, TF1IE)


# Generated at 2022-06-14 17:07:23.798234
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Constructor of the class TF1IE
    # Access the protected (private) _real_initialize() method
    #   with no parameters
    tf1IE = TF1IE._real_initialize()
    # Access the method defined in InfoExtractor
    tf1IE.suitable('https://www.tf1.fr/...')
    # Access the method defined in InfoExtractor
    tf1IE.is_allowed_url('https://www.tf1.fr/...')

# Generated at 2022-06-14 17:07:25.720256
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Test if the the constructor of TF1IE is correct
    _ = TF1IE(None)

# Generated at 2022-06-14 17:07:37.539986
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    url_msn = 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html'
    tf1_obj = t._real_extract(url_msn)

    assert tf1_obj['id'] == '497077'
    assert tf1_obj['url'] == 'wat:497077'
    assert tf1_obj['title'] == 'Mylène Farmer, d\'une icône'
    assert tf1_obj['description'] == None
    assert tf1_obj['timestamp'] == 1556699600
    assert tf1_obj['duration'] == None
    assert tf1_obj['tags'] == []
    assert tf1_obj['series'] == 'HD1 - Le documentaire'
    assert tf

# Generated at 2022-06-14 17:07:39.309100
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE()

# Generated at 2022-06-14 17:07:58.251193
# Unit test for constructor of class TF1IE
def test_TF1IE():
    base_url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    tf1 = TF1IE(base_url)
    assert(tf1._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html')

# Generated at 2022-06-14 17:08:05.271761
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE('TF1IE', 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html')
    assert ie.params['series'] is None
    assert ie.params['season_number'] is None
    assert ie.params['episode_number'] is None
    assert ie.params['timestamp'] is None
    assert ie.params['duration'] is None

# Generated at 2022-06-14 17:08:06.059996
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()

# Generated at 2022-06-14 17:08:12.430548
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    assert t.suitable('https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html') == False
    assert t.suitable('https://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html') == False



# Generated at 2022-06-14 17:08:16.146705
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Constructor test of TF1IE class object."""
    TF1IE()


# Generated at 2022-06-14 17:08:22.423852
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert instance._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'


test_TF1IE()

# Generated at 2022-06-14 17:08:27.341787
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    assert ie._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:34.946744
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html")
    assert TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    assert TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")

# Generated at 2022-06-14 17:08:41.722848
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """
    Test for class TF1IE constructor
    """
    args = (object, 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    tf1IE = TF1IE()
    assert tf1IE._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:08:42.609668
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    print(t)

# Generated at 2022-06-14 17:09:06.161061
# Unit test for constructor of class TF1IE
def test_TF1IE():
    # Call function constructor with given parameters
    TF1IE("url")
    # We want '_VALID_URL' to be defined and to be of type string
    assert hasattr(TF1IE, "_VALID_URL") and isinstance(TF1IE._VALID_URL, str)

# Generated at 2022-06-14 17:09:08.884246
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    # AssertionError: 'wat_api' is undefined # pylint: disable=E1101
    assert hasattr(tf1, '_download_webpage')

# Generated at 2022-06-14 17:09:17.538293
# Unit test for constructor of class TF1IE
def test_TF1IE():
    exp0 = TF1IE
    s0 = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    exp1 = "https://www.tf1.fr/graphql/web"
    s1 = 'quotidien-premiere-partie-11-juin-2019'
    exp2 = '9b80783950b85247541dd1d851f9cc7fa36574af015621f853ab111a679ce26f'

# Generated at 2022-06-14 17:09:19.076009
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test for class TF1IE"""
    instance = TF1IE()
    assert isinstance(instance, TF1IE)



# Generated at 2022-06-14 17:09:19.671229
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:09:20.223059
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:09:22.345851
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert IE.ie_key() == 'TF1'
    assert IE.ie_url() == 'https://www.tf1.fr/'

# Generated at 2022-06-14 17:09:22.806912
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:09:24.730385
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1_ie = TF1IE()

    assert(tf1_ie.test_test_test() == 2)

# Generated at 2022-06-14 17:09:36.022481
# Unit test for constructor of class TF1IE
def test_TF1IE():
    assert TF1IE.ie_key() == "TF1"
    assert TF1IE.is_valid_url("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html") == True
    assert TF1IE.is_valid_url("https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html") == True
    # The following url gives a 403 error
    # assert TF1IE.is_valid_url("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html") == True

# Generated at 2022-06-14 17:10:27.619921
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("https://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")
    TF1IE("http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html")

# Generated at 2022-06-14 17:10:28.567613
# Unit test for constructor of class TF1IE
def test_TF1IE():
    t = TF1IE()
    t.suite()

# Generated at 2022-06-14 17:10:29.166484
# Unit test for constructor of class TF1IE
def test_TF1IE():
    pass

# Generated at 2022-06-14 17:10:37.128764
# Unit test for constructor of class TF1IE
def test_TF1IE():
    obj = TF1IE('http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html')
    assert obj.IE_NAME == 'tf1'
    assert obj.IE_DESC == 'TF1'
    assert obj._VALID_URL == 'https?://(?:www\.)?tf1\.fr/[^/]+/(?P<program_slug>[^/]+)/videos/(?P<id>[^/?&#]+)\.html'

# Generated at 2022-06-14 17:10:40.427537
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("url")

# Generated at 2022-06-14 17:10:46.190346
# Unit test for constructor of class TF1IE
def test_TF1IE():
    class_ = TF1IE
    tf1ie = class_('TF1IE', True, class_.ie_key())
    assert tf1ie.suitable(tf1ie.ie_key()) == "tf1"
    assert tf1ie.IE_NAME == 'tf1.fr'
    assert tf1ie.thumbnail == 're:^https?://.*\.jpg$'

# Generated at 2022-06-14 17:10:47.241927
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE(None, None)

# Generated at 2022-06-14 17:10:57.244364
# Unit test for constructor of class TF1IE
def test_TF1IE():
    program_slug = 'tmc/quotidien-avec-yann-barthes'
    slug = 'quotidien-premiere-partie-11-juin-2019'
    url = "https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html"
    ie = TF1IE(url)

    assert ie.program_slug == program_slug
    assert ie.slug == slug

# Generated at 2022-06-14 17:11:00.212151
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    assert tf1 is not None

# Generated at 2022-06-14 17:11:03.113084
# Unit test for constructor of class TF1IE
def test_TF1IE():
    IE = TF1IE()
    assert IE.IE_NAME == 'tf1'
    assert IE.IE_DESC == 'TF1 videos'

# Generated at 2022-06-14 17:13:16.491838
# Unit test for constructor of class TF1IE
def test_TF1IE():
    tf1 = TF1IE()
    tmc_quotidien_slug = 'quotidien-avec-yann-barthes'
    tmc_quotidien_url = 'https://www.tf1.fr/tmc/{}/videos/quotidien-premiere-partie-11-juin-2019.html'.format(tmc_quotidien_slug)
    assert tf1.suitable(tmc_quotidien_url)
    assert tf1.VALID_URL == TF1IE._VALID_URL
    assert tf1.IE_NAME == 'tf1'
    assert tf1.TESTS == TF1IE._TESTS
    assert tf1.BR_DESC == 'Video'
    assert tf1._VALID_URL == TF1IE._VALID

# Generated at 2022-06-14 17:13:17.850815
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test: class TF1IE
    """
    tf1 = TF1IE()
    assert tf1 != None

# Generated at 2022-06-14 17:13:26.714246
# Unit test for constructor of class TF1IE
def test_TF1IE():
    ie = TF1IE()
    # Check that the regex matches an example link
    assert ie._VALID_URL == re.match(ie._VALID_URL, 'http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html').string

    # Check that the regex does not match another example link
    assert not ie._VALID_URL == re.match(ie._VALID_URL, 'http://www.tf1.fr/hd1/documentaire/videos/mylene-farmer-d-une-icone.html').string

# Generated at 2022-06-14 17:13:27.831901
# Unit test for constructor of class TF1IE
def test_TF1IE():
    instance = TF1IE()
    if not instance:
        return False
    return True

# Generated at 2022-06-14 17:13:29.237935
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()._real_extract(TF1IE._TESTS[0]['url'])

# Generated at 2022-06-14 17:13:33.558939
# Unit test for constructor of class TF1IE
def test_TF1IE():
    try:
        TF1IE(None)
    except TypeError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 17:13:34.176383
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE()

# Generated at 2022-06-14 17:13:38.247705
# Unit test for constructor of class TF1IE
def test_TF1IE():
    url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
    TF1IE().suitable(url)
    TF1IE().extract(url)

# Generated at 2022-06-14 17:13:42.736556
# Unit test for constructor of class TF1IE
def test_TF1IE():
    TF1IE("http://www.tf1.fr/tf1/koh-lanta/videos/replay-koh-lanta-22-mai-2015.html")


# Generated at 2022-06-14 17:13:44.623187
# Unit test for constructor of class TF1IE
def test_TF1IE():
    """Test for class TF1IE"""
    assert TF1IE is not None

