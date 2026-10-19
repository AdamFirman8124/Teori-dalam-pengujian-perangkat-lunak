

# Generated at 2022-06-14 17:16:40.284753
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # test_dumps_dissectors
    trutv_ie = TruTVIE()
    assert trutv_ie._VALID_URL == 'https?://(?:www\\.)?trutv\\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\\d+))'
    assert trutv_ie.IE_NAME == 'trutv.com'
    assert trutv_ie.IE_DESC == 'Turner Entertainment Network'


# Generated at 2022-06-14 17:16:41.881587
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:16:42.900895
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()

# Generated at 2022-06-14 17:16:46.369771
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE();
    assert(t.name == 'TruTV');
    assert(t._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))');

# Generated at 2022-06-14 17:16:56.243012
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    x = TruTVIE()
    y = x._extract_ngtv_info("https://videoapi.ngtv.truex.com/api/v1/auth/web/v2/f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1.json?context=%7B%22site%22%3A%22truTV%22%7D", "abcd", "abcd")
    assert (y is None)


# Generated at 2022-06-14 17:16:58.691404
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


# Generated at 2022-06-14 17:17:08.939149
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    T = TruTVIE()
    t = T.ie_key()
    assert t == 'trutv'
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    match = re.match(T._VALID_URL, url)
    series_slug, clip_slug, video_id = match.groups()
    assert series_slug == 'the-carbonaro-effect'
    assert clip_slug == 'sunlight-activated-flower'
    assert video_id == None
    T._download_ngtv_formats()
    T._extract_ngtv_info()
    T._real_extract(url)

# Generated at 2022-06-14 17:17:09.242439
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:09.827148
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:18.744939
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test url parameter
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    # Test url error
    url2 = 'https://www.trutv.com/shows/'
    # Test url parsing
    url3 = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/'
    # Test url parsing error
    url4 = 'https://www.trutv.com/shows/the-carbonaro-effect/'    
    # Test TruTVIE constructor
    TruTVIE()

# Generated at 2022-06-14 17:17:37.034005
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv = TruTVIE()
    assert ttv._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert len(ttv._TEST['url']) > 0
    assert len(ttv._TEST['info_dict']['id']) > 0
    assert len(ttv._TEST['info_dict']['ext']) > 0
    assert len(ttv._TEST['info_dict']['title']) > 0

# Generated at 2022-06-14 17:17:43.343741
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    obj = t._match_id(url)
    assert obj.group('series_slug') == 'the-carbonaro-effect'
    assert obj.group('clip_slug') == 'sunlight-activated-flower'
    assert obj.group('id') is None

# Generated at 2022-06-14 17:17:47.310323
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE = TruTVIE()
    except ValueError:
        print("Constructor of TruTVIE is correct")

test_TruTVIE()

# Generated at 2022-06-14 17:17:57.354755
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE(False)
    assert obj._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:17:58.460080
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:59.114212
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:00.024715
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t != None

# Generated at 2022-06-14 17:18:00.744374
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    pass

# Generated at 2022-06-14 17:18:11.755595
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url1 = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    url2 = 'https://www.trutv.com/shows/the-carbonaro-effect/full-episodes/400-lbs-of-mushrooms.html'
    url3 = 'https://www.trutv.com/shows/the-carbonaro-effect/full-episodes/rattlesnake-bites.html'
    url4 = 'https://www.trutv.com/shows/impractical-jokers/videos/its-a-tug-of-war.html'

    # Testing constructor of class with valid URL
    ie = TruTVIE()
    assert isinstance(ie, TruTVIE)

    # Testing constructor of class with invalid URL
   

# Generated at 2022-06-14 17:18:12.862701
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:24.069016
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Happy path
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html', {}, {}, {})

# Generated at 2022-06-14 17:18:26.527012
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie._real_extract("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")

# Generated at 2022-06-14 17:18:30.312717
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'


# Generated at 2022-06-14 17:18:32.167602
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE = TruTVIE(None)
    print(TruTVIE)


# Generated at 2022-06-14 17:18:34.562503
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # TruTVIE(IE_NAME, ie, ie_key=None, ie_fetch_info=None, ver=()):
    trutv_ie = TruTVIE('TruTV', TurnerBaseIE(), ie_key="TruTV", ie_fetch_info="Some IE", ver="4.5")
    assert trutv_ie.name == 'TruTV'

# Generated at 2022-06-14 17:18:37.881305
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .test_trutv import test_TruTVIE as test
    test(TruTVIE)

# Generated at 2022-06-14 17:18:38.550771
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE

# Generated at 2022-06-14 17:18:41.333005
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    truTV_youtube = TruTVIE()

# Generated at 2022-06-14 17:18:47.040995
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    for url in 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html', 'https://www.trutv.com/shows/the-carbonaro-effect/565933.html'.strip().split():
        assert TruTVIE(url)._match_id(url) is not None
    # assert TruTVIE(url)._match_id(url) is not None


# Generated at 2022-06-14 17:18:48.485799
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE().constructor()

# Generated at 2022-06-14 17:19:08.960421
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


# Generated at 2022-06-14 17:19:09.773771
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:13.364835
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Test TruTVIE constructor
    """
    tr = TruTVIE()
    assert isinstance(tr, TruTVIE)


# Generated at 2022-06-14 17:19:22.812403
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    # Arrange
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    import youtube_dl
    ydl = youtube_dl.YoutubeDL(
        {
            'outtmpl': '%(id)s%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'noplaylist': True,
            'quiet': True,
            'simulate': True
        })

    # Act
    TruTVIE(ydl)._real_extract(url)

# Generated at 2022-06-14 17:19:30.627608
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    video = TruTVIE()._real_extract(url)
    assert video["id"] == "f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1"
    assert video["timestamp"] == "2016-06-19T06:00:00Z"
    assert len(video["formats"]) == 4
    assert video["display_id"] == "sunlight-activated-flower"
    assert video["title"] == "Sunlight-Activated Flower"

# Generated at 2022-06-14 17:19:31.192410
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:36.009482
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .test_embed import construct_test_embed
    t = construct_test_embed('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html', TruTVIE)
    assert t.test_TruTVIE()

# Generated at 2022-06-14 17:19:43.040558
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    import unittest
    assert TruTVIE.__name__ == 'TruTVIE'
    assert TruTVIE._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'



# Generated at 2022-06-14 17:19:44.381407
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:53.426587
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.IE_NAME == 'TruTV'
    assert ie.LOGO_URL == 'http://trutv.mtvnimages.com/images/trutv/3.0/global/og-image.png'
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'


# Generated at 2022-06-14 17:20:39.879927
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE().extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:20:47.478827
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == "https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))"
    assert TruTVIE()._TEST['url'] == "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    assert TruTVIE()._TEST['info_dict']['id'] == "f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1"

# Generated at 2022-06-14 17:20:52.639376
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTV_ie = TruTVIE()
    TruTV_ie._real_initialize()
    TruTV_ie._downloader.http.headers.update({'User-Agent': TruTV_ie._downloader.user_agent()})

    assert TruTV_ie._VALID_URL == TruTVIE._VALID_URL

    # These should all be matched by the regular expression
    assert TruTV_ie._WORKING_URL_RE.match(TruTV_ie._VALID_URL)

    # These should not be matched by the regular expression
    assert TruTV_ie._WORKING_URL_RE.match('https://www.trutv.com/') == None
    assert TruTV_ie._WORKING_URL_RE.match('https://www.trutv.com/shows') == None
    assert TruTV_ie._WORK

# Generated at 2022-06-14 17:20:54.738277
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:20:57.676825
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._TEST.get('url') == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

# Generated at 2022-06-14 17:20:59.223135
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """ Test TruTVIE.__init__() """


# Generated at 2022-06-14 17:21:01.554188
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    truTV = TruTVIE()
    assert truTV.ie_key() == 'truTV'
    assert truTV.ie_name() == 'truTV'

# Generated at 2022-06-14 17:21:02.093133
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:03.218171
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    return t

# Generated at 2022-06-14 17:21:06.497777
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('truTV', 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html', 'id')

# Generated at 2022-06-14 17:22:48.345351
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:22:59.142995
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie._download_json = lambda i, _, __: {'episode': {'mediaId': '123'}, 'info': {'mediaId': '456'}}
    ie._extract_ngtv_info = lambda id, __, ___: {'id': id}

# Generated at 2022-06-14 17:23:00.442614
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:01.049976
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:23:04.927468
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Success
    TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    # Failure
    try:
        TruTVIE('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower')
    except:
        return True
    return False

# Generated at 2022-06-14 17:23:05.960657
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('trutv.com')

# Generated at 2022-06-14 17:23:07.739214
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE(TurnerBaseIE())
    except:
        print("Could not create TruTVIE")
        assert False
    assert True


# Generated at 2022-06-14 17:23:15.566746
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._VALID_URL == 'https?://(?:www\\.)?trutv\\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\\d+))'

# Generated at 2022-06-14 17:23:16.818580
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_IE = TruTVIE({})
    assert trutv_IE is not None

# Generated at 2022-06-14 17:23:20.138032
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Constructor for class TruTVIE
    """
    ie = TruTVIE()
    assert ie._VALID_URL == TruTVIE._VALID_URL
    assert ie._TEST == TruTVIE._TEST
    return ie
