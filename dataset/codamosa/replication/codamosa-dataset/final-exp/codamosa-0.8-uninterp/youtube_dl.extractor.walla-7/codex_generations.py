

# Generated at 2022-06-14 17:37:33.466632
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Add test function to WallaIE class
    """
    # Given
    url = "http://w.walla.co.il"
    # When
    walla = WallaIE(url)

    # Then
    assert walla != None

# Generated at 2022-06-14 17:37:41.853107
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    assert ie._VALID_URL == "https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)"
    assert ie._TEST['url'] == "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"

# Generated at 2022-06-14 17:37:45.968053
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Constructor test

    """
    IE = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert IE.NAME == 'Walla!', 'Walla was not initilized properly'

# Generated at 2022-06-14 17:37:52.231025
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test if a WallaIE object can be constructed.
    try:
        WallaIE()
    except:
        assert False, "A WallaIE object can not be constructed."


# Generated at 2022-06-14 17:37:53.643488
# Unit test for constructor of class WallaIE
def test_WallaIE():
    v = WallaIE()
    assert isinstance(v, WallaIE)

# Generated at 2022-06-14 17:38:00.249521
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:01.816266
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE is not None
    


# Generated at 2022-06-14 17:38:07.614747
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    video = ie._real_extract(url)
    assert video == WallaIE._TEST['info_dict']

# Generated at 2022-06-14 17:38:08.209193
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:38:09.246059
# Unit test for constructor of class WallaIE
def test_WallaIE():
    global WallaIE
    WallaIE()

# Generated at 2022-06-14 17:38:15.285567
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE(InfoExtractor())

# Generated at 2022-06-14 17:38:22.553108
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test = WallaIE(info_dict={'id': '2642630', 'display_id': 'one-direction-all-for-one', 'ext': 'flv', 'title': 'וואן דיירקשן: ההיסטריה', 'url': 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one', 'duration': 3600, 'thumbnail': 're:^https?://.*\\.jpg', 'description': 'md5:de9e2512a92442574cdb0913c49bc4d8', 'duration': 3600 })
    print(test)

# Generated at 2022-06-14 17:38:30.174020
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.display_id == 'one-direction-all-for-one'
    assert ie.video_id == '2642630'
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:33.673161
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE(WallaIE._TEST)
    assert obj.__class__.__name__ == 'WallaIE'


# Generated at 2022-06-14 17:38:42.518439
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:38:44.177518
# Unit test for constructor of class WallaIE
def test_WallaIE():
    cases = [WallaIE]
    for case in cases:
        assert case

# Generated at 2022-06-14 17:38:45.474026
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print('test_WallaIE')
    ie = WallaIE()

# Generated at 2022-06-14 17:38:47.604994
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .. import test_classes_extractors
    test_classes_extractors(WallaIE, ['WallaIE'])

# Generated at 2022-06-14 17:38:59.353987
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test Case 1
    ie = WallaIE()
    ie.download('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.get_downloader()._filename == '2642630.flv'
    assert ie.get_downloader()._download_params['url'] == 'vod.walla.co.il/vod'
    assert ie.get_downloader()._download_params['play_path'] == 'WallaXMLServer/_definst_/mp4:' + ie.get_downloader()._filename

    # Test Case 2
    ie = WallaIE()
    ie.download('http://vod.walla.co.il/movie/2642603/one-direction-all-for-one-english-subtitles')


# Generated at 2022-06-14 17:39:13.136350
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:27.331947
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('vod.walla.co.il', 'one-direction-all-for-one')
    assert(ie.url == 'http://vod.walla.co.il/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:29.489706
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj.__class__.__name__ == 'WallaIE'

# Generated at 2022-06-14 17:39:39.883523
# Unit test for constructor of class WallaIE
def test_WallaIE():

    ie = WallaIE(_VALID_URL)
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:41.608203
# Unit test for constructor of class WallaIE
def test_WallaIE():
    wallaIE = WallaIE()
    assert wallaIE

# Generated at 2022-06-14 17:39:43.007750
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(_VALID_URL)

# Generated at 2022-06-14 17:39:47.448877
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert ie.info_dict["id"] == "2642630"
    assert ie.info_dict["display_id"] == "one-direction-all-for-one"

# Generated at 2022-06-14 17:39:50.496382
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    display_id = 'one-direction-all-for-one'
    extractor = WallaIE(url)
    assert extractor.display_id == display_id


# Generated at 2022-06-14 17:39:51.437566
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == WallaIE._VALID_URL

# Generated at 2022-06-14 17:39:57.377752
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(InfoExtractor())._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:58.449295
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE() is not None

# Generated at 2022-06-14 17:40:30.270179
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .rtmp import RTMPIE
    w = WallaIE()
    assert isinstance(w, RTMPIE)
    a = w._real_extract(WallaIE._TEST['url'])
    assert type(a['id']) == unicode
    assert type(a['display_id']) == unicode
    assert type(a['title']) == unicode
    assert type(a['description']) == unicode
    assert type(a['thumbnail']) == unicode
    assert type(a['duration']) == int
    assert type(a['formats']) == list
    assert type(a['subtitles']) == dict
    for k in a['subtitles']:
        assert type(k) == unicode
        assert type(a['subtitles'][k]) == list
        assert type

# Generated at 2022-06-14 17:40:31.933889
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()
test_WallaIE.test = 'true'

# Generated at 2022-06-14 17:40:43.485606
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._TEST['info_dict']['id'] == '2642630'
    assert ie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert ie._TEST['info_dict']['ext'] == 'flv'

# Generated at 2022-06-14 17:40:43.996448
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:40:45.820265
# Unit test for constructor of class WallaIE
def test_WallaIE():
    wallaIE = WallaIE()

# Generated at 2022-06-14 17:40:48.702813
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(None, None)._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:59.220685
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_url = WallaIE._TEST['url']
    url = WallaIE._VALID_URL

    id_from_url = re.match(url, test_url)
    assert id_from_url is not None, 'Unable to extract "id" from url.'
    assert id_from_url.group('id') == WallaIE._TEST['info_dict']['id'], \
        'Extracted value of "id" from url is different than expected value.'

    display_id_from_url = re.match(url, test_url)
    assert display_id_from_url is not None, 'Unable to extract "id" from url.'

# Generated at 2022-06-14 17:41:08.994797
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    # Valid URL:
    # unit test for absolute URL (http://...)
    WallaIE.test_url(ie, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    # unit test for relative URL (/...)
    WallaIE.test_url(ie, '/movie/2642630/one-direction-all-for-one')
    # unit test for URL with query string (?...)
    WallaIE.test_url(ie, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one/?a=b')
    # unit test for URL with anchor (#...)

# Generated at 2022-06-14 17:41:18.738518
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\\d+)/(?P<display_id>.+)'
    assert w._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:41:22.572137
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL.match('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one') is not None

# Generated at 2022-06-14 17:42:12.341471
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST.get('subtitles') == {'heb': [{'ext': 'srt', 'url': 'http://video2.walla.co.il/?w=null/null/2642630/@@/video/subtitles/subtitles.2642630.heb.srt'}]}

# Generated at 2022-06-14 17:42:20.191704
# Unit test for constructor of class WallaIE
def test_WallaIE():
    m = re.match(WallaIE._VALID_URL, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert m.group('id') == '2642630'
    assert m.group('display_id') == 'one-direction-all-for-one'
    assert WallaIE._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:42:23.912430
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    ie.extract("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")

# Generated at 2022-06-14 17:42:25.930358
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE is not None, 'Failed to init WallaIE'

# Generated at 2022-06-14 17:42:29.437941
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:42:30.207278
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:42:39.910090
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

    # And now with a URL that is invalid
    obj = WallaIE('http://vod.walla.co.il/movie/2662630/one-direction-all-for-one')
    # The class WallaIE should be initialized with an URL, otherwise
    # it will throw an exception

# Generated at 2022-06-14 17:42:44.090367
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE().ie_key() == 'Walla'
    assert WallaIE().suitable('http://www.walla.co.il/')
    assert not WallaIE().suitable('http://www.some-website.com/')
    assert WallaIE()._VALID_URL == 'https?://.*'

# Generated at 2022-06-14 17:42:50.627490
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Create instance
    ie = WallaIE()

    # Test supported URL
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert re.match(ie._VALID_URL, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

    # Test unsupported URL
    assert ie._VALID_URL != r'https?://vod\.walla\.co\.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:42:55.870372
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

test_WallaIE()

# Generated at 2022-06-14 17:44:47.707054
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:44:50.840118
# Unit test for constructor of class WallaIE
def test_WallaIE():
    video = WallaIE()
    video.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    return

# Generated at 2022-06-14 17:44:52.942306
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('www.walla.co.il', 'http://vod.walla.co.il', 'Not empty')

# Generated at 2022-06-14 17:44:55.314341
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Test for constructor of class WallaIE
    """
    c = WallaIE()
    c.suite().run(c.test_result())

# Generated at 2022-06-14 17:44:55.865800
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:44:57.602167
# Unit test for constructor of class WallaIE
def test_WallaIE():
    '''
    Test constructor of class WallaIE.
    '''
    ie = WallaIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:44:58.947680
# Unit test for constructor of class WallaIE
def test_WallaIE():
	w = WallaIE()
	assert isinstance(w, WallaIE)


# Generated at 2022-06-14 17:45:08.087236
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert WallaIE._VALID_URL(url)
    assert WallaIE._TEST['url'] == url
    assert WallaIE._TEST['info_dict']['id'] == '2642630'
    assert WallaIE._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert WallaIE._TEST['info_dict']['ext'] == 'flv'
    assert WallaIE._TEST['info_dict']['title'] == 'וואן דיירקשן: ההיסטריה'

# Generated at 2022-06-14 17:45:10.658851
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    ie.download('2642630')

# Generated at 2022-06-14 17:45:15.689812
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        a = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    except Exception as e:
        print(e)