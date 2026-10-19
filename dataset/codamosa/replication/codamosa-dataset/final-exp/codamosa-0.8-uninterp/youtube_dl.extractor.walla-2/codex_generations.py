

# Generated at 2022-06-14 17:37:32.612493
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:37:37.261733
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_cases = ["http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"]
    inst = WallaIE()
    for test_url in test_cases:
        match = inst._VALID_URL_RE.match(test_url)
        assert match, "The URL did not match"
        assert inst._real_extract(test_url)

# Generated at 2022-06-14 17:37:42.107500
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("vod.walla.co.il")
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    #ie._real_extract(url="http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
#test_WallaIE()

# Generated at 2022-06-14 17:37:46.290042
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert WallaIE._VALID_URL == ie._VALID_URL
    assert WallaIE._TEST == ie._TEST
    assert WallaIE._SUBTITLE_LANGS == ie._SUBTITLE_LANGS

# Generated at 2022-06-14 17:37:48.347210
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.unit_test() is True

# Generated at 2022-06-14 17:37:49.342077
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:37:58.408385
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    obj = WallaIE()._real_extract(url)
    assert obj['title'] == 'וואן דיירקשן: ההיסטריה', obj['title']
    assert obj['id'] == '2642630', obj['id']
    assert obj['display_id'] == 'one-direction-all-for-one', obj['display_id']
    assert obj['duration'] == 3600, obj['duration']
    assert obj['subtitles'] == {}, obj['subtitles']
    assert obj['formats'][0]['format_id'] == '1080p', obj['formats'][0]['format_id']

# Generated at 2022-06-14 17:37:59.240502
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert 'Walla' in ie.IE_NAME

# Generated at 2022-06-14 17:38:02.593655
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.__class__ == WallaIE

# Generated at 2022-06-14 17:38:05.967188
# Unit test for constructor of class WallaIE
def test_WallaIE():
    e = WallaIE()

# Generated at 2022-06-14 17:38:17.557282
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE != None

# Generated at 2022-06-14 17:38:19.526954
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il')
    assert ie.__class__.__name__ == 'WallaIE'

# Generated at 2022-06-14 17:38:24.143576
# Unit test for constructor of class WallaIE
def test_WallaIE():
    infoExtractor = WallaIE()
    assert(infoExtractor.get_class_name() == 'WallaIE')
    assert(infoExtractor.ie_key() == 'walla')

# Generated at 2022-06-14 17:38:29.474280
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert obj.__class__.__name__ == 'WallaIE'
    assert obj.ie_key() == 'Walla'


# Generated at 2022-06-14 17:38:34.178975
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .common import InfoExtractor
    from .walla import WallaIE
    assert( isinstance( WallaIE(InfoExtractor()), WallaIE ) )

if __name__ == '__main__':
    test_WallaIE()

# Generated at 2022-06-14 17:38:45.339472
# Unit test for constructor of class WallaIE
def test_WallaIE():
    video_id = '2642630'
    class_ = WallaIE
    assert class_._VALID_URL.match(
        'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert class_._VALID_URL.match(
        'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert class_.__name__ == 'WallaIE'
    assert class_.__doc__ == 'Walla! video extractor'
    assert class_.ie_key() == 'walla'
    ie = class_(None)
    ie.set_downloader(None)

# Generated at 2022-06-14 17:38:46.346677
# Unit test for constructor of class WallaIE
def test_WallaIE():
    i = WallaIE()


# Generated at 2022-06-14 17:38:50.182106
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    assert ie.SUCCESS == ie._real_extract(url)

# Generated at 2022-06-14 17:39:00.685517
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:13.180214
# Unit test for constructor of class WallaIE
def test_WallaIE():
	title = 'וואן דיירקשן: ההיסטריה'
	sub_he = {'ext':'srt', 'url': 'http://vod.walla.co.il/subtitles/sb_srt.ashx?v=2642630&l=he&a=2642630_1'}
	sub_en = {'ext':'srt', 'url': 'http://vod.walla.co.il/subtitles/sb_srt.ashx?v=2642630&l=en&a=2642630_1'}

# Generated at 2022-06-14 17:39:26.054794
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert issubclass(WallaIE, InfoExtractor)

# Generated at 2022-06-14 17:39:29.796389
# Unit test for constructor of class WallaIE
def test_WallaIE():
    reqres = requests.get("https://vod.walla.co.il/movie/2639276/sapir-1-10")
    print(reqres.content)
    

# Generated at 2022-06-14 17:39:32.500352
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:40.343081
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.url == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie.host == 'vod.walla.co.il'

    mobj = re.match(ie._VALID_URL, ie.url)
    assert mobj.group('id') == '2642630'
    assert mobj.group('display_id') == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:39:46.800897
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert (type(WallaIE._SUBTITLE_LANGS) is dict)
    assert(WallaIE._SUBTITLE_LANGS.has_key('עברית'))
    assert(WallaIE._SUBTITLE_LANGS.get('עברית') == 'heb')
    test = WallaIE
    print(test.__doc__)

# Generated at 2022-06-14 17:39:47.380338
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:39:54.946598
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from bs4 import BeautifulSoup
    from xml.etree import ElementTree
    from xml.dom import minidom

    # Test case (1)
    # Test function: get_metadata_url
    # Define video as BeautifulSoup object
    video = BeautifulSoup(
        '<div class="player" data-video="" data-id="2716116" data-model="movie" data-autoplay="false" data-width="640" data-height="360"></div>',
        'html.parser')
    # Test the get_metadata_url functio
    url = WallaIE._get_metadata_url(video)
    assert url == 'http://video2.walla.co.il/?w=null/null/2716116/@@/video/flv_pl'
    
    # Test case (2

# Generated at 2022-06-14 17:39:57.397920
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:40:00.272301
# Unit test for constructor of class WallaIE
def test_WallaIE():
  ie = WallaIE()
  assert ie.name == 'walla'
  assert ie.description == 'Videos from walla.co.il'
  assert ie.valid_urls == ['http://vod.walla.co.il/']
  assert ie.display_id == display_id
  assert ie.url_to_display_id == url_to_display_id
  assert ie.extract_id == extract_id

# Generated at 2022-06-14 17:40:13.667512
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie != None
    assert ie.IE_NAME == "walla"
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._TEST['info_dict']['id'] == '2642630'
    assert ie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert ie._TEST['info_dict']['ext'] == 'flv'

# Generated at 2022-06-14 17:40:43.835212
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        WallaIE()
        return True
    except Exception:
        return False
assert test_WallaIE()

# Generated at 2022-06-14 17:40:49.697479
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from walla.WallaIE import WallaIE
    from walla.WallaIE import InfoExtractor
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one', InfoExtractor)
    ie._real_initialize()
    assert ie.display_id == 'one-direction-all-for-one'
    assert ie.id == '2642630'

# Generated at 2022-06-14 17:40:52.236229
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Check that WallaIE class is constructed correctly
    # (asserts are used for checking)
    ie = WallaIE('example.com/some_url')

# Generated at 2022-06-14 17:40:57.559553
# Unit test for constructor of class WallaIE
def test_WallaIE():
    #Test for instantiating WallaIE
    a = WallaIE("https://vod.walla.co.il/movie/2629602/the-birth-of-sake")
    #Test for instantiating WallaIE
    b = WallaIE("https://vod.walla.co.il/movie/2629602/the-birth-of-sake")
    #Test for object identity
    assert a is b

# Generated at 2022-06-14 17:41:04.440854
# Unit test for constructor of class WallaIE
def test_WallaIE():
    import sys
    if sys.version_info < (3, 0):
        return
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    ie.extract(url)
    assert(ie.display_id == 'one-direction-all-for-one')
    assert(ie.title == "וואן דיירקשן: ההיסטריה")
    assert(ie.duration == 3600)

# Generated at 2022-06-14 17:41:06.108887
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert (WallaIE(WallaIE.ie_key()) is not None)

# Generated at 2022-06-14 17:41:14.175359
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from walla import WallaIE
    from urlparse import urlparse
    from urlparse import urlunparse
    from urlparse import parse_qs
    desired_parser_list = ['//vod.walla.co.il/', '//video2.walla.co.il']
    desired_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()
    constructors_list = extractor.ie_key()
    is_current_url_supported = False
    for constructor in constructors_list:
        url_data = urlparse(desired_url)
        if constructor in desired_parser_list:
            is_current_url_supported = True

# Generated at 2022-06-14 17:41:19.724105
# Unit test for constructor of class WallaIE
def test_WallaIE():
    testCase = WallaIE()
    # Assert character name is equal to the expected character name
    assert testCase._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    # Assert character name is equal to the expected character name

# Generated at 2022-06-14 17:41:23.832687
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    ie.extract(url)

# Generated at 2022-06-14 17:41:33.056213
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert(ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)')

# Generated at 2022-06-14 17:42:43.425768
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print('Constructor: ' + WallaIE.__name__)
    '''
    def __init__(self, ie_name, ie_key, *args):
        self._ready = True
        # Set ie_key
        super(WallaIE, self).__init__(ie_name, ie_key, *args)
    # class constructor for WallaIE
    # assert constructor
    walla = WallaIE('WallaIE', 'walla')
    print('>>> ie_name: ' + walla._ie_name)
    print('>>> ie_key: ' + walla._ie_key)
    print('>>> args: ' + str(walla._args))
    print('>>> ready: ' + repr(walla._ready))
    '''

# Generated at 2022-06-14 17:42:46.683806
# Unit test for constructor of class WallaIE
def test_WallaIE():
    try:
        WallaIE(InfoExtractor._downloader, 'wala.co.il/vod/2642630/one-direction-all-for-one')
    except:
        assert(False)


# Generated at 2022-06-14 17:42:54.296266
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:43:02.431268
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:43:05.292492
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    WallaIE()._real_extract(url)

# Generated at 2022-06-14 17:43:05.956773
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:43:17.200702
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from json import loads

    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE()
    ie.extract(url)
    ie_dict = loads(ie.__str__())

    assert(ie_dict['id'] == '2642630')
    assert(ie_dict['display_id'] == 'one-direction-all-for-one')
    assert(ie_dict['ext'] == 'flv')
    assert(ie_dict['title'] == 'וואן דיירקשן: ההיסטריה')
    assert(ie_dict['description'] == 'md5:de9e2512a92442574cdb0913c49bc4d8')

# Generated at 2022-06-14 17:43:18.500800
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE

# Generated at 2022-06-14 17:43:19.068236
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:43:22.924045
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert re.match('^http://vod.walla.co.il/\d+/[^/]+$', ie._VALID_URL) == None


# Generated at 2022-06-14 17:45:21.983838
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.IE_NAME == 'walla'

# Generated at 2022-06-14 17:45:24.279036
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
# Unit test of extraction

# Generated at 2022-06-14 17:45:34.535196
# Unit test for constructor of class WallaIE
def test_WallaIE():
        assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:45:35.708857
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie,InfoExtractor)

# Generated at 2022-06-14 17:45:38.565446
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.name == 'walla'
    assert ie.VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(\d+)/(.+)'

# Generated at 2022-06-14 17:45:45.737466
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert (ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)')
    return True


# Generated at 2022-06-14 17:45:50.574854
# Unit test for constructor of class WallaIE
def test_WallaIE():
	object_WallaIE = WallaIE()
	current_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
	object_WallaIE._real_extract(current_url)

# Generated at 2022-06-14 17:45:53.847506
# Unit test for constructor of class WallaIE
def test_WallaIE():
    class_name = "WallaIE"
    mod = __import__("walla", fromlist=[class_name])
    klass = getattr(mod, class_name)
    ie = klass("Walla")
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:45:57.831577
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # testing constructor of class WallaIE
    try:
        WallaIE()
    except Exception as e:
        print(e)

# Generated at 2022-06-14 17:46:08.459607
# Unit test for constructor of class WallaIE
def test_WallaIE():
    walla=WallaIE()
    assert walla._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert walla._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert walla._TEST['info_dict']['id'] == '2642630'
    assert walla._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert walla._TEST['info_dict']['ext'] == 'flv'