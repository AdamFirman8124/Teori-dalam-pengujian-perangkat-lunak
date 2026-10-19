

# Generated at 2022-06-14 17:16:33.605250
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:16:40.677006
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	url = TruTVIE._TEST[ 'url' ]
	info = TruTVIE._TEST[ 'info_dict' ]
	TruTVIE()._real_extract( url )
	assert TruTVIE._VALID_URL == url
	assert info[ 'id' ] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
	assert info[ 'ext' ] == 'mp4'
	assert info[ 'description' ] == "A customer is stunned when he sees Michael's sunlight-activated flower."

# Generated at 2022-06-14 17:16:42.844650
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.IE_NAME == "trutv"
    assert "trutv.com" in ie.VALID_URL

# Generated at 2022-06-14 17:16:43.460122
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:51.896647
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE('truTV.com')
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:16:57.116753
# Unit test for constructor of class TruTVIE

# Generated at 2022-06-14 17:16:57.630064
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:58.124219
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:00.284416
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:17:10.905006
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:16.569130
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:17.347970
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:27.198057
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:28.227704
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
    v = TurnerBaseIE()

# Generated at 2022-06-14 17:17:28.958471
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:37.540159
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test for TruTVIE for checking if url is valid or not
    url1 = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    # Test for TruTVIE retrieving the data from url
    url2 = "https://www.trutv.com/full-episodes/754189/jokes-on-you-s01-e04-july-09-2015.html"
    # Test for TruTVIE for invalid url
    url3 = "https://www.trutv.com/full-episodes/754189/jokes-on-you-s01-e04-july-09-2015.html"
    assert TruTVIE._TEST.get('url') == url1

# Generated at 2022-06-14 17:17:38.229536
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:41.223121
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
        assert False
    except TypeError:
        assert True
    except Exception as e:
        assert False, 'Exception "%s" raised unexpectedly' % e

# Generated at 2022-06-14 17:17:45.932789
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.IE_NAME == 'trutv'
    assert ie._VALID_URL == TruTVIE._VALID_URL
    assert ie._TEST == TruTVIE._TEST
    assert ie._download_json == TurnerBaseIE._download_json
    assert ie._extract_ngtv_info == TurnerBaseIE._extract_ngtv_info


# Generated at 2022-06-14 17:17:46.963418
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    x = TruTVIE()
    assert x is not None

# Generated at 2022-06-14 17:18:00.513718
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Test TruTVIE constructor"""
    trutv_ie = TruTVIE()
    assert(trutv_ie.IE_NAME == "truTV")
    assert(trutv_ie.IE_DESC == "truTV.com")

# Generated at 2022-06-14 17:18:08.603583
# Unit test for constructor of class TruTVIE

# Generated at 2022-06-14 17:18:19.852413
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttvie = TruTVIE("http://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    assert ttvie.getTitle() == u"Sunlight-Activated Flower"
    assert ttvie.getEpisodeNum() == None
    assert ttvie.getSeasonNum() == None
    assert ttvie.getDescription() == u"A customer is stunned when he sees Michael's sunlight-activated flower."
    assert ttvie.getSeries() == u"The Carbonaro Effect"
    assert ttvie.getDisplayID() == "sunlight-activated-flower"
    assert ttvie.getID() == "f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1"
    assert ttvie.getTim

# Generated at 2022-06-14 17:18:21.632481
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    pass

# Generated at 2022-06-14 17:18:22.348830
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:22.882526
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:24.132937
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    #test the TruTVIE class
    # TBD: write a test case
    assert True


# Generated at 2022-06-14 17:18:25.523031
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    raise NotImplementedError('Need to implement TruTVIE constructor')

# Generated at 2022-06-14 17:18:28.941571
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()._call_api('https://api.trutv.com/v2/web/series/clip/impractical-jokers/wedding-party')
    TruTVIE()._call_api('https://api.trutv.com/v2/web/episode/impractical-jokers/9954')

# Generated at 2022-06-14 17:18:30.888902
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    '''
    Check if an instance of TruTVIE is created correctly.
    '''
    TruTVIE()

# Generated at 2022-06-14 17:18:57.999066
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    class_ = TruTVIE
    valid_url = TruTVIE._VALID_URL
    data = {
        'url': 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
        'info_dict': {'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1', 'ext': 'mp4', 'title': 'Sunlight-Activated Flower', 'description': "A customer is stunned when he sees Michael's sunlight-activated flower."},
        'params': {'skip_download': True},
    }
    instance = class_(data)
    instance._real_extract(data['url'])


# Generated at 2022-06-14 17:19:05.288142
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test case 1.
    test = TruTVIE()
    assert test.IE_NAME == 'trutv'

    # Test case 2.
    data = {'url': 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
            'info_dict': {'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1', 'ext': 'mp4',
                          'title': 'Sunlight-Activated Flower',
                          'description': "A customer is stunned when he sees Michael's sunlight-activated flower.",
                          },
            'params': {'skip_download': True,
                       },
            }
    test = TruTVIE(data)


# Generated at 2022-06-14 17:19:06.528500
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    cls = TurnerBaseIE.get_ie('https://www.trutv.com/shows')
    assert cls == TruTVIE


# Generated at 2022-06-14 17:19:13.756114
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_obj = TruTVIE()
    assert test_obj._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert test_obj._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

# Generated at 2022-06-14 17:19:14.726240
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE = TruTVIE()

# Generated at 2022-06-14 17:19:18.937311
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    parsed_url = re.match(TruTVIE._VALID_URL, url).groups()
    TruTVIE._real_extract(None, url)

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:19:26.217039
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE()
    print('test_TruTVIE={}'.format(obj))
    assert obj is not None

test_all_class = [TruTVIE]

if __name__ == "__main__":
    for cls in test_all_class:
        test_TruTVIE()
        print('{} tested'.format(cls.__name__))

# Generated at 2022-06-14 17:19:27.932835
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    truTVIE = TruTVIE()
    assert truTVIE.name == 'trutv:video'

# Generated at 2022-06-14 17:19:30.438333
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    return
    ie = TruTVIE()
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')


# Generated at 2022-06-14 17:19:41.023965
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE(TruTVIE._downloader)
    assert(trutv_ie.ie_key() == 'trutv')
    assert(trutv_ie.ie_name() == 'TruTV')
    assert(trutv_ie._VALID_URL == TruTVIE._VALID_URL)
    assert(trutv_ie._TEST == TruTVIE._TEST)
    assert(trutv_ie.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'))
    assert(not trutv_ie.suitable('https://www.trutv.com'))

# Generated at 2022-06-14 17:20:29.431217
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.download_webpage('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:20:31.042215
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttvie = TruTVIE("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    svr = isinstance(ttvie, TruTVIE)
    assert(svr)


# Generated at 2022-06-14 17:20:42.315133
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    module = TruTVIE()
    assert module._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:20:46.862189
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    # Test case 1: Correct parameters
    ttvIE1 = TruTVIE(TruTVIE._downloader, "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html");
    assert ttvIE1 != None

    # Test case 2: Inorrect URL
    ttvIE2 = TruTVIE(TruTVIE._downloader, "Wrong URL")
    assert ttvIE2 == None

    return


# Generated at 2022-06-14 17:20:48.365766
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Make sure class TruTVIE exists and can be instantiated
    obj = TruTVIE()
    assert obj != None


# Generated at 2022-06-14 17:20:49.979588
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
  try:
    TruTVIE = TruTVIE()
  except:
    raise AssertionError("Unable to create TruTVIE")

# Generated at 2022-06-14 17:21:00.515615
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvie = TruTVIE()
    assert trutvie is not None
    assert type(trutvie) is TruTVIE
    print ("type TruTVIE is: %s" % type(trutvie))

    shorturl = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    trutvie._TEST['url'] = shorturl
    result = trutvie._real_extract(shorturl)
    assert result['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'

# Generated at 2022-06-14 17:21:02.416967
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	from .test_download import _TestDownload
	t = TruTVIE({})
	assert isinstance(t, _TestDownload)


# Generated at 2022-06-14 17:21:03.345599
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Create TruTVIE objects
    TruTVIE()

# Generated at 2022-06-14 17:21:09.213789
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # This should fail, as the URL isn't valid in this case
    TruTVIE('abc', 'abc')
    # This should pass, as the URL is valid in this case
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html', 'the-carbonaro-effect')

# Generated at 2022-06-14 17:23:02.576377
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE(None)
    trutv_url = TruTVIE._TEST.get('url')
    trutv_info = TruTVIE._TEST.get('info_dict')
    trutv_params = TruTVIE._TEST.get('params')
    trutv_real_extract = TruTVIE._real_extract(trutv, trutv_url)

    assert(trutv.suitable(trutv_url) == True)
    assert(trutv.IE_NAME == 'Turner')
    assert(trutv._VALID_URL == TruTVIE._VALID_URL)
    assert(trutv._TEST == TruTVIE._TEST)

# Generated at 2022-06-14 17:23:04.022984
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:13.797229
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Initialize TruTVIE with TruTVIE's clip
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

    # Initialize TruTVIE with TruTVIE's episode
    trutv_ie = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/episodes/episode-28-freak-your-florist-out.html')
    assert trutv_ie.video_id == '28'
    assert trutv_ie.display_id == 'episode-28-freak-your-florist-out'
    assert trutv_ie.show_title == 'Carbonaro Effect, The'
    assert trutv_ie.season_number == 0
    assert trut

# Generated at 2022-06-14 17:23:14.832241
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()._real_extract(TruTVIE._TEST['url'])

# Generated at 2022-06-14 17:23:15.469169
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE



# Generated at 2022-06-14 17:23:17.174194
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    test = ie._TEST
    test.__class__ = TruTVIE
    return test

# Generated at 2022-06-14 17:23:17.726549
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:19.264334
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:23:30.253594
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Without a try-except block
    test_class_TruTVIE = TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert test_class_TruTVIE.url == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert test_class_TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:31.148752
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()