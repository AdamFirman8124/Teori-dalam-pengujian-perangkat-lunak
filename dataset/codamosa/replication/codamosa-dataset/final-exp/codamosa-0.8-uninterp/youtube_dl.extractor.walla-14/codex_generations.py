

# Generated at 2022-06-14 17:37:38.722361
# Unit test for constructor of class WallaIE
def test_WallaIE():
    #WallaIE()._download_webpage(url, video_id, 'Downloading webpage: %s' % url)
    input_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    pattern = 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    pattern = re.compile(pattern)
    assert pattern.match(input_url)


# Generated at 2022-06-14 17:37:41.926804
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'walla'
    assert hasattr(ie, '_SUBTITLE_LANGS')

# Generated at 2022-06-14 17:37:44.846742
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

test_WallaIE()

# Generated at 2022-06-14 17:37:47.635455
# Unit test for constructor of class WallaIE
def test_WallaIE():
    info_extractor = WallaIE([WallaIE._VALID_URL])
    assert(info_extractor._VALID_URL == WallaIE._VALID_URL)

# Generated at 2022-06-14 17:37:55.931803
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.suitable(WallaIE._TEST['url']) == True
    assert ie.IE_NAME == 'walla:vod'
    assert ie._VALID_URL == WallaIE._TEST['url']
    assert ie._TEST == WallaIE._TEST
    assert ie._SUBTITLE_LANGS['עברית'] == 'heb'
    assert ie._real_extract(WallaIE._TEST['url']) == WallaIE._TEST['info_dict']

# Generated at 2022-06-14 17:38:07.783427
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    # Constructor of class WallaIE requires url as argument
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:14.792675
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE(WallaIE._VALID_URL)
    mobj = re.match(ie._VALID_URL, url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert(video_id == "2642630")
    assert(display_id == "one-direction-all-for-one")

# Generated at 2022-06-14 17:38:18.942076
# Unit test for constructor of class WallaIE
def test_WallaIE():

    # Testing that WallaIE is a subclass of InfoExtractor:
    assert issubclass(WallaIE, InfoExtractor)

    # Testing that object of class WallaIE is an object of class InfoExtractor:
    assert isinstance(WallaIE(), InfoExtractor)

# Generated at 2022-06-14 17:38:25.370829
# Unit test for constructor of class WallaIE
def test_WallaIE():
  _VALID_URL = r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:37.427293
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'Walla'
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:38:50.031886
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.expand_rules(ie.IE_NAME) == ie.IE_DESC

# Generated at 2022-06-14 17:39:00.574462
# Unit test for constructor of class WallaIE
def test_WallaIE():
    print('testing WallaIE')
    #url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    #url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one?w=null/null/2642630/@@/video/flv_pl'

    class spy_logger:
        def debug(self, msg):
            print(msg)

    spy_logger = spy_logger()

    ie = WallaIE(spy_logger)
    ie._download_xml(url, None)
    exit(0)

# Unit

# Generated at 2022-06-14 17:39:02.961818
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    return obj

# Generated at 2022-06-14 17:39:05.658803
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:39:09.378794
# Unit test for constructor of class WallaIE
def test_WallaIE():
	print("Test WallaIE")
	WallaIE()
	return True

if __name__ == "__main__":
	if test_WallaIE():
		print("WallaIE class constructor works.")
	else:
		print("WallaIE class constructor does not work.")

# Generated at 2022-06-14 17:39:20.099071
# Unit test for constructor of class WallaIE
def test_WallaIE():
	import os
	videos = [
		"http://vod.walla.co.il/movie/2642630/one-direction-all-for-one",
		"http://vod.walla.co.il/movie/2644065/chile-israel",
		"http://vod.walla.co.il/movie/2622986/07-12-2014",
		"http://vod.walla.co.il/movie/2621635/toto-cutugno",
		"http://vod.walla.co.il/movie/2621635/toto-cutugno",
	]

	for video in videos:
		ie = WallaIE(video)
		info = ie._real_extract(video)
		assert info['id']

# Generated at 2022-06-14 17:39:21.342570
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    assert w

# Generated at 2022-06-14 17:39:29.251155
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    expected = {
        'id': '2642630',
        'display_id': 'one-direction-all-for-one',
        'ext': 'flv',
        'title': 'וואן דיירקשן: ההיסטריה',
        'description': 'md5:de9e2512a92442574cdb0913c49bc4d8',
        'thumbnail': r're:^https?://.*\.jpg',
        'duration': 3600,
    }
    fields = ie._real_extract(url)
    assert fields == expected

# Generated at 2022-06-14 17:39:30.012051
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:39:31.062959
# Unit test for constructor of class WallaIE
def test_WallaIE():
  call = WallaIE()

# Generated at 2022-06-14 17:39:54.195669
# Unit test for constructor of class WallaIE
def test_WallaIE():
	# try to initialize the class by calling constructor
	my_class = WallaIE()
	assert True

# Generated at 2022-06-14 17:40:04.282100
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    video = WallaIE()
    video_dict = video._real_extract(url)
    assert video_dict['id'] == '2642630'
    assert video_dict['display_id'] == 'one-direction-all-for-one'
    assert video_dict['title'] == 'וואן דיירקשן: ההיסטריה'
    assert video_dict['description'] == 'md5:de9e2512a92442574cdb0913c49bc4d8'
    assert video_dict['thumbnail'] == r're:^https?://.*\.jpg'
    assert video_dict['duration'] == 36

# Generated at 2022-06-14 17:40:13.299328
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie = WallaIE(test=True)
    assert ie.host == 'vod.walla.co.il'
    assert ie.host == 'vod.walla.co.il'
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie.match(url) is not None
    assert ie.match(url) is not None
    mobj = re.match(ie._VALID_URL, url)


# Generated at 2022-06-14 17:40:13.821180
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:40:17.361885
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE = WallaIE()

# Generated at 2022-06-14 17:40:21.602158
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:40:22.199876
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:40:23.164306
# Unit test for constructor of class WallaIE
def test_WallaIE():
	return WallaIE()

# Generated at 2022-06-14 17:40:29.674544
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/move/2642630/one-direction-all-for-one')
    assert ie._downloader._opener.addheaders[0] == ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.7.1')

# Generated at 2022-06-14 17:40:35.490469
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    w._extract_m3u8_formats
    assert WallaIE._VALID_URL == "^https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>[^/]+)$"



# Generated at 2022-06-14 17:41:23.865744
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE('http://vod.walla.co.il/2532272/one-direction-all-for-one')
    assert obj._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert obj._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:41:33.092433
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/.*/\\d+/.*'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

# Generated at 2022-06-14 17:41:37.122195
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == WallaIE._VALID_URL
    assert ie._TEST == WallaIE._TEST
    assert ie._SUBTITLE_LANGS == WallaIE._SUBTITLE_LANGS

# Generated at 2022-06-14 17:41:38.238233
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.ie_name() == 'Walla'

# Generated at 2022-06-14 17:41:42.976931
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Call constructor of class WallaIE with valid URL
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')



# Generated at 2022-06-14 17:41:43.478844
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()
    return

# Generated at 2022-06-14 17:41:44.224346
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:41:55.617775
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._TEST['info_dict']['id'] == '2642630'
    assert ie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:42:04.233253
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert hasattr(obj, 'ie_key')
    assert hasattr(obj, '_VALID_URL')
    assert hasattr(obj, '_TEST')
    assert obj._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:42:04.947702
# Unit test for constructor of class WallaIE
def test_WallaIE():
	e = WallaIE()

# Generated at 2022-06-14 17:44:03.372495
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()

# Generated at 2022-06-14 17:44:10.010252
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.suitable('http://vod.walla.co.il/movie/2655335/frozen-let-it-go-from-disneys-frozen-idina-menzel')
    assert not ie.suitable('http://vod.walla.co.il/?w=null/null/2642630/@@/video/flv_pl')


# Generated at 2022-06-14 17:44:12.382667
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:44:15.067066
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie = WallaIE('WallaIE', 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:44:19.264046
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # constructor of class WallaIE doesn't get any argument
    ie = WallaIE()
    # test whether ie is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:44:20.785155
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE()._VALID_URL == WallaIE._VALID_URL

# Generated at 2022-06-14 17:44:28.627471
# Unit test for constructor of class WallaIE
def test_WallaIE():
    from .common import InfoExtractor
    from .walla import WallaIE
    from .common import BaseInfoExtractor
    from .common import InfoExtractor
    from .common import JPodcastIE
    from .common import YoutubeIE
    from .common import YoutubePlaylistIE
    from .common import YoutubeUserIE
    from .common import YoutubeChannelIE
    from .common import YoutubeSearchIE
    from .common import YoutubeSearchDateIE
    from .common import YoutubeSearchURLIE
    from .common import YoutubeFavouritesIE
    from .common import YoutubeHistoryIE
    from .common import YoutubeRecommendedIE
    from .common import YoutubeShowIE
    from .common import YoutubeSubscriptionsIE
    from .common import YoutubeTruncatedURLIE
    from .common import YoutubeWatchLaterIE
    from .common import YoutubeIE
    from .common import YoutubePlaylist

# Generated at 2022-06-14 17:44:30.909256
# Unit test for constructor of class WallaIE
def test_WallaIE():
    constructor_success = False
    try:
        WallaIE()
        constructor_success = True
    except:
        pass
    assert constructor_success == True

# Generated at 2022-06-14 17:44:32.132733
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # check that class WallaIE can be constructed
    # without exceptions
    WallaIE()

# Generated at 2022-06-14 17:44:33.003610
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract()

# Generated at 2022-06-14 17:46:28.986067
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert ie.url == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie.video_id == '2642630'
    assert ie.display_id == 'one-direction-all-for-one'

# Generated at 2022-06-14 17:46:32.876337
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """Test WallaIE constructor."""
    assert WallaIE

# Generated at 2022-06-14 17:46:34.855832
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:46:35.458641
# Unit test for constructor of class WallaIE
def test_WallaIE():
    return WallaIE()

# Generated at 2022-06-14 17:46:40.464043
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Tests for constructor of WallaIE.
    """
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    video_id = '2642630'
    display_id = 'one-direction-all-for-one'
    _VALID_URL = r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    mobj = re.match(_VALID_URL, url)
    assert mobj.group('id') == video_id
    assert mobj.group('display_id') == display_id

# Generated at 2022-06-14 17:46:45.835201
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    ie.extract('http://vod.walla.co.il/movie/18/one-direction-all-for-one')

if __name__ == '__main__':
    test_WallaIE()

# Generated at 2022-06-14 17:46:46.677129
# Unit test for constructor of class WallaIE
def test_WallaIE():
	pass


# Generated at 2022-06-14 17:46:58.842656
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE({})
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:47:03.149177
# Unit test for constructor of class WallaIE
def test_WallaIE():
    res = WallaIE()._real_extract(WallaIE._TEST['url'])

# Generated at 2022-06-14 17:47:04.636819
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'