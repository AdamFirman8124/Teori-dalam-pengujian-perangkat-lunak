

# Generated at 2022-06-14 17:16:32.087291
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE = TruTVIE()
	assert TruTVIE


# Generated at 2022-06-14 17:16:33.653797
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Unit test for constructor of TruTVIE
    """
    return TruTVIE

# Generated at 2022-06-14 17:16:34.305868
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:16:35.789762
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.__name__ == "TruTVIE"

# Generated at 2022-06-14 17:16:40.716134
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.suitable("https://www.trutv.com/full-episodes/123456789/the_carbonaro_effect_s2_ep16_the_jigsaw_job_video.html")
    assert ie.suitable("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")

# Generated at 2022-06-14 17:16:46.223319
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    o = TruTVIE()
    assert o._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'


# Generated at 2022-06-14 17:16:46.984843
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


# Generated at 2022-06-14 17:16:52.500386
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test for the constructor of class TruTVIE
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    TruTVIE(url)


# Generated at 2022-06-14 17:16:54.544223
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()._VALID_URL == TruTVIE._VALID_URL
    assert TruTVIE()._TEST == TruTVIE._TEST

# Generated at 2022-06-14 17:16:55.009132
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:01.787607
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    TrueTVIE 
    """

    TrueTVIE = TruTVIE()

# Generated at 2022-06-14 17:17:11.843789
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    inst = TruTVIE()
    assert len(inst._TEST) == 3
    assert inst._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert inst._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert 'id' in inst._TEST['info_dict']
    assert 'ext' in inst._TEST['info_dict']

# Generated at 2022-06-14 17:17:18.405716
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE.get_url_re() == TruTVIE._VALID_URL
    assert re.match(TruTVIE._VALID_URL, url)

    t = TruTVIE
    type(t).get_url_re = TruTVIE.get_url_re
    instance = t(url)
    assert isinstance(instance, TruTVIE)

test_TruTVIE()


# Unit tests for fetching data from a TruTVIE link

# Generated at 2022-06-14 17:17:19.223225
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

import io

# Generated at 2022-06-14 17:17:20.266414
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	truTVIE = TruTVIE()
	assert(truTVIE != None)

# Generated at 2022-06-14 17:17:21.079324
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:28.991067
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()

    # Checking attribute initialization
    assert t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

    # Checking successful extraction
    assert "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html" == t._TEST['url']
    assert "Sunlight-Activated Flower" == t._TEST['info_dict']['title']
    assert "A customer is stunned when he sees Michael's sunlight-activated flower." == t._T

# Generated at 2022-06-14 17:17:32.595362
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE(None)
        TruTVIE.initialize()
        TruTVIE.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
        TruTVIE.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    except Exception as e:
        print(str(e))

# Generated at 2022-06-14 17:17:39.520101
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    clip_url_with_slug = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    clip_url_with_id = 'https://www.trutv.com/shows/the-carbonaro-effect/31876/sunlight-activated-flower/index.html'
    episode_url = 'https://www.trutv.com/full-episodes/31876/the-carbonaro-effect/index.html'
    clip_info = TruTVIE()._real_extract(clip_url_with_slug)
    clip_info2 = TruTVIE()._real_extract(clip_url_with_id)
    episode_info = TruTVIE()._real_extract(episode_url)

# Generated at 2022-06-14 17:17:48.300243
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Create a TruTVIE object
    trutv = TruTVIE()

    # Check if the url is in the correct format
    url = 'https://www.trutv.com/full-episodes/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert trutv._match_id(url) == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'

    # Check if the video displays the correct information
    info = trutv._extract_info_dict(url, {}, {'url': url})

# Generated at 2022-06-14 17:17:58.792194
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:05.492227
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert(t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))')

# Generated at 2022-06-14 17:18:14.913751
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    '''
    Unit test for class TruTVIE
    '''
    obj = TruTVIE()
    assert obj.name == 'trutv'
    assert TruTVIE.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
    assert TruTVIE()._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:17.907897
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    my_TruTVIE = TruTVIE()
    print(my_TruTVIE)
###############################################################################

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:18:21.614425
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
	tv = TruTVIE(url)
	assert tv.url == url

# Generated at 2022-06-14 17:18:26.993988
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
	re_result = re.match(TruTVIE._VALID_URL,url)
	print(re_result.groupdict())
	trutvIE = TruTVIE()
	info = trutvIE._real_extract(url)
	print(info)


# Generated at 2022-06-14 17:18:38.047123
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:39.133939
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()
# Test TruTVIE

# Generated at 2022-06-14 17:18:47.002341
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
        TruTVIE.ie_key()
        TruTVIE.suitable('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')
        TruTVIE.ie()
        TruTVIE._VALID_URL
        TruTVIE._TEST
        TruTVIE._download_json
        TruTVIE._extract_ngtv_info
    except NameError as e:
        print('NameError: {0}'.format(e))

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:18:48.486094
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:10.267409
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    for x in range(0, 3):
        tru_tv_ie = TruTVIE()
        assert(tru_tv_ie is not None)

# Generated at 2022-06-14 17:19:14.498933
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    ie = TruTVIE()
    ie.extract(url)

# Generated at 2022-06-14 17:19:19.151466
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE(None)._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:19:21.306121
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()._TEST

# Generated at 2022-06-14 17:19:31.151237
# Unit test for constructor of class TruTVIE
def test_TruTVIE():

    # Using the constructor of TruTVIE to create an instance
    instance_TruTVIE = TruTVIE()

    # Testing the type of the first argument of the constructor
    assert(isinstance(instance_TruTVIE._TEST, dict))

    # Testing the type of the second argument of the constructor
    assert(isinstance(instance_TruTVIE._VALID_URL, str))

    # Testing the type of the third argument of the constructor
    assert(isinstance(instance_TruTVIE._download_webpage, types.FunctionType))

    # Testing the type of the forth argument of the constructor
    assert(isinstance(instance_TruTVIE._download_json, types.FunctionType))

    # Testing the type of the fifth argument of the constructor

# Generated at 2022-06-14 17:19:31.785588
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:32.406937
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:19:34.872212
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE._TEST['url'] == TruTVIE(None)._TEST['url']

# Generated at 2022-06-14 17:19:36.118406
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(None)

# Generated at 2022-06-14 17:19:40.322494
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    if ie._VALID_URL is None or ie._TEST is None:
        raise Exception('TruTVIE not properly initialized!')
    print('TruTVIE initialization test passed!')



# Generated at 2022-06-14 17:20:30.303011
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    _test_class_name = 'TruTVIE'
    _test_class_instance = TruTVIE()
    assert _test_class_instance.name == "truTV"

# Generated at 2022-06-14 17:20:31.848233
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttvie = TruTVIE()


# Generated at 2022-06-14 17:20:42.918038
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert ie.suitable("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html")
    assert not ie.suitable("https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower/html")
    assert ie.suitable("https://www.trutv.com/full-episodes/1113682/videos/sunlight-activated-flower.html")
    assert ie.suitable("https://www.trutv.com/full-episodes/1113682")
    assert not ie.suitable("https://www.trutv.com/full-episodes/1113682/")
    assert not ie.suitable("https://www.trutv.com/")


# Generated at 2022-06-14 17:20:44.325732
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Check if the object created has been created properly
    assert TruTVIE()

# Generated at 2022-06-14 17:20:45.964956
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    for url in TruTVIE._TEST['url'].split(" "):
        TruTVIE(url)

# Generated at 2022-06-14 17:20:52.286711
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from utils import TestCase
    from ..utils import url_basename
    test = TestCase(TruTVIE)
    # clip
    test.run(
        'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
        'TruTVIE',
        url_basename('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'),
        'truTV - Sunlight-Activated Flower',
        'mp4', 'A customer is stunned when he sees Michael\'s sunlight-activated flower.')
    # episode

# Generated at 2022-06-14 17:20:52.949621
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:21:03.146355
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE.ie_key() == 'trutv:video'
    assert TruTVIE.ie_key() != 'trutv:playlist'
    assert TruTVIE._TEST['url'] == 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE._TEST['info_dict']['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
    assert TruTVIE._TEST['info_dict']['ext'] == 'mp4'
    info_dict = TruTVIE._TEST['info_dict']
    assert info_dict['title'] == 'Sunlight-Activated Flower'

# Generated at 2022-06-14 17:21:14.056231
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_url_1 = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    test_url_2 = 'https://www.trutv.com/shows/at-home-with-amy-sedaris/videos/s1/e1/chili-mariachi-chef.html'
    # Test TruTVIE class
    TruTVIE_test = TruTVIE()
    try:
        assert TruTVIE_test.suitable(test_url_1) == True
        assert TruTVIE_test.suitable(test_url_2) == True
    except AssertionError as e:
        print('Failed to assert TruTVIE class', e)


# Generated at 2022-06-14 17:21:22.913283
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test case for TruTVIE
    trutvIE = TruTVIE()
    # check if _VALID_URL is set properly
    assert trutvIE._VALID_URL == (
        r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/'
        '(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    )
    # check if _TEST is set properly

# Generated at 2022-06-14 17:23:09.687482
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    print(ie.IE_NAME)
    print(ie.IE_SHORT_NAME)
    print(ie._VALID_URL)
    print(len(ie._TESTS))
    print(ie._TEST)
    print(ie.extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'))

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:23:16.541353
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutvIE = TruTVIE()
    trutvIE._TEST = {'url': 'http://www.trutv.com/full-episodes/2118/kris/videos/impossible-darts.html',
                     'info_dict':
                         {
                             'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1',
                             'ext': 'mp4',
                             'title': 'Impossible Darts',
                             'description': "A customer is stunned when he sees Michael's sunlight-activated flower."
                         },
                     'params': {'skip_download': True}}

# Generated at 2022-06-14 17:23:17.898476
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    tru = TruTVIE()
    assert tru._VALID_URL is not None

# Generated at 2022-06-14 17:23:29.123142
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    instance = TruTVIE()
    assert instance._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:31.568368
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(None)

# Generated at 2022-06-14 17:23:36.422763
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    u = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    test = TruTVIE()._extract(u)
    assert 'id' in test
    assert 'url' in test
    assert 'site_name' in test
    assert 'auth_required' in test



# Generated at 2022-06-14 17:23:45.330851
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    obj = TruTVIE('truTV')
    assert obj._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:23:56.033025
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    #truTV test
    trutv = TruTVIE()
    #trutv URL test
    #https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html
    #series slug: the-carbonaro-effect
    #clip slug: sunlight-activated-flower
    input = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    assert TruTVIE._VALID_URL==trutv._VALID_URL
    assert TruTVIE._TEST==trutv._TEST
    assert TruTVIE._real_extract(trutv,input)

# Generated at 2022-06-14 17:24:00.458216
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .test import TestIE
    test = TestIE(TruTVIE)
    # Test the youtube test video
    test.test('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html',
              'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1')

# Generated at 2022-06-14 17:24:01.044922
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()