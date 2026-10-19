

# Generated at 2022-06-14 17:16:33.333777
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert(t._TEST is not None)
    return True

# runs plural tests on class TruTVIE
test_TruTVIE()

# Generated at 2022-06-14 17:16:39.164779
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    # Use regex for the url
    assert t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'



# Generated at 2022-06-14 17:16:49.318256
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    v = TruTVIE()
    assert v._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:16:53.363371
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()

    # Assert presence of valid URL regex
    assert ie._VALID_URL

    # Assert presence of _TEST dict
    assert ie._TEST

    # Assert result of _real_extract() call
    assert ie._real_extract(ie._TEST['url'])

# Declare TruTVIE to be tested
__all__ = ['TruTVIE']

# Generated at 2022-06-14 17:16:56.961070
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.download('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:17:01.369617
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    try:
        TruTVIE()
    except:
        raise AssertionError("Could not create class TruTVIE")

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:17:02.397566
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:03.037061
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:04.461543
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
  ie = TruTVIE()
  ie._download_json()


# Generated at 2022-06-14 17:17:05.477990
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:16.848240
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert trutv is not None
    assert trutv._VALID_URL is not None
    assert trutv._TEST is not None


# Generated at 2022-06-14 17:17:25.544652
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    test_instance = TruTVIE()
    expected_instantiation = {
        '_VALID_URL': re.compile(r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'),
        'ie_key': 'TruTV', 'ie': 'TruTv'
    }
    assert test_instance.__dict__ == expected_instantiation

# Generated at 2022-06-14 17:17:26.278709
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:17:28.547425
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()

# Generated at 2022-06-14 17:17:31.504344
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """
    Unit test for constructor of class TruTVIE
    """
    tru_tv_ie = TruTVIE()
    assert tru_tv_ie.IE_NAME == u'truTV'

# Generated at 2022-06-14 17:17:32.533350
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()

# Generated at 2022-06-14 17:17:33.770698
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE().ie_key() == 'trutv'

# Generated at 2022-06-14 17:17:36.165307
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()


# Generated at 2022-06-14 17:17:42.291999
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    assert TruTVIE._VALID_URL == 'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'
    assert TruTVIE.suitable(url) is True
    assert TruTVIE.__name__ == 'TruTVIE'
    # Test for TruTVIE.ie_key()
    # Check the ie_key for TruTVIE's constructor

# Generated at 2022-06-14 17:17:45.246530
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t != None


# Generated at 2022-06-14 17:18:08.349923
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttv = TruTVIE()

    assert ttv.source == 'trutv'
    assert ttv.short_code == 'trutv'
    assert ttv.player == 'trutv'
    assert ttv.show_id == 'trutv'
    assert ttv.channel_code == 'trutv'

# Generated at 2022-06-14 17:18:14.224551
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	assert hasattr(TruTVIE, '_VALID_URL')
	assert hasattr(TruTVIE, '_TEST')
	assert hasattr(TruTVIE, '_download_webpage')
	assert hasattr(TruTVIE, '_extract_ngtv_info')
	assert hasattr(TruTVIE, '_real_extract')

# Generated at 2022-06-14 17:18:16.980445
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    truTVIE = TruTVIE()
    print(truTVIE)
    assert truTVIE is not None

if __name__ == '__main__':
    test_TruTVIE()

# Generated at 2022-06-14 17:18:17.988386
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE(3)

# Generated at 2022-06-14 17:18:18.558395
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:19.065139
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    pass

# Generated at 2022-06-14 17:18:29.530258
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVInstance = TruTVIE()
    assert TruTVInstance._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:18:30.130000
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:18:32.356850
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()._real_extract("http://www.trutv.com/full-episodes/82275/jokers-wild-videos/odin-holds-it-down.html")
    TruTVIE()._real_extract("http://www.trutv.com/full-episodes/82275/jokers-wild-videos/odin-holds-it-down")

# Generated at 2022-06-14 17:18:39.556420
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    object_TruTVIE = TruTVIE()

# Generated at 2022-06-14 17:18:58.315239
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    """Unit test for constructor of class TruTVIE"""
    TruTVIE()

# Generated at 2022-06-14 17:19:05.017778
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t._VALID_URL == r'https?://(?:www\.)?trutv\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\d+))'

# Generated at 2022-06-14 17:19:05.879560
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    print(trutv)


# Generated at 2022-06-14 17:19:12.230087
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    regex = TruTVIE._VALID_URL

    match = re.match(regex, url)
    assert match

    series_slug = match.group('series_slug')
    clip_slug = match.group('clip_slug')
    video_id = match.group('id')

    assert series_slug == 'the-carbonaro-effect'
    assert clip_slug == 'sunlight-activated-flower'
    assert video_id is None

# Generated at 2022-06-14 17:19:14.726630
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.extract(url='https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:19:17.217766
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # make sure TruTVIE is instance of TurnerBaseIE
    TruTVIE = TruTVIE()
    assert isinstance(TruTVIE, TurnerBaseIE)

# Generated at 2022-06-14 17:19:23.817282
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    url = "https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html"
    data = ie._real_extract(url)
    assert 'id' in data and 'display_id' in data and 'title' in data and 'thumbnails' in data and 'timestamp' in data and 'series' in data and 'season_number' in data and 'episode_number' in data

# Generated at 2022-06-14 17:19:32.374660
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ttvie = TruTVIE()

    # make sure the constructor sets some things up
    assert ttvie._VALID_URL is not None # pylint: disable=W0212
    assert ttvie._TEST is not None # pylint: disable=W0212
    other_test_url = ttvie._TEST['url'] # pylint: disable=W0212
    other_test_info = ttvie._TEST['info_dict'] # pylint: disable=W0212
    assert other_test_url is not None
    assert other_test_info is not None

    # make sure the _real_extract method gets some data
    other_test_info = ttvie._real_extract(other_test_url) # pylint: disable=W0212
    assert other_test_

# Generated at 2022-06-14 17:19:33.518672
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    pass

# Generated at 2022-06-14 17:19:34.587760
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    return (TruTVIE()._TEST)

# Generated at 2022-06-14 17:20:22.363895
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    # Test initialization of class TruTVIE
    assert TruTVIE, 'Could not instantiate class TruTVIE'
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

#
# Unit tests for TruTVIE
#
# The code below is unit test code for TruTVIE. It does not need to be included in the
# actual IE or in any documentation.
#
import os
import sys
import unittest
import json

try:
    from urllib.parse import urlparse, parse_qs
except ImportError:
    from urlparse import urlparse, parse_qs

# TODO: Add '../' to avoid this hard coding for test files

# Generated at 2022-06-14 17:20:33.503527
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    expected = {
        'id': 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1',
        'ext': 'mp4',
        'title': 'Sunlight-Activated Flower',
        'description': "A customer is stunned when he sees Michael's sunlight-activated flower.",
    }
    # get info
    info = TruTVIE._real_extract(TruTVIE(), url)
    # check title
    assert info['title'] == expected['title']
    # check description
    assert info['description'] == expected['description']
    # check id
    assert info['id'] == expected['id']
    # check ext

# Generated at 2022-06-14 17:20:37.175433
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_ie = TruTVIE()
    assert trutv_ie.name == 'trutv'
    assert trutv_ie.description == TruTVIE.__doc__


# Generated at 2022-06-14 17:20:38.806475
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv_instance = TruTVIE()
    assert trutv_instance is not None

# Generated at 2022-06-14 17:20:40.521691
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    assert isinstance(ie, TruTVIE)


# Generated at 2022-06-14 17:20:42.304434
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    from .test_turner import TurnerBaseIETest
    TurnerBaseIETest(TruTVIE, 'TruTV').test()


# Generated at 2022-06-14 17:20:43.853922
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE('test', None)

# Generated at 2022-06-14 17:20:44.647829
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('test')

# Generated at 2022-06-14 17:20:45.932535
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

test_TruTVIE()



# Generated at 2022-06-14 17:20:48.262250
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	TruTVIE()._real_extract('https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html')

# Generated at 2022-06-14 17:22:23.823301
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE('trutv', 'http://www.trutv.com/')
    TruTVIE('trutv', 'http://www.trutv.com')
    TruTVIE('trutv', 'http://www.trutv.com/')
    TruTVIE('trutv', 'https://www.trutv.com')
    TruTVIE('trutv', 'https://www.trutv.com/')

# Generated at 2022-06-14 17:22:24.170471
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:22:30.450913
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    ie = TruTVIE()
    ie.download(TruTVIE._TEST['url'])
    # This outputs
    # http://mf.svc.nflxvideo.net/u/pc6/tt71313/v/6/e/c/4/6c4a3eb1d6a4bddc7fa9e9e2c7b0d1218a6e4f4a.m3u8?ndn.nginx=1&ndn.ttl=60&ndn.fwu=android&ndn.fws=androidtv&ndn.ip=64.196.36.13&ndn.tos=2&ndn.cid=23&ndn.crid=23&ndn.cidr=0&ndn.secid=2&ndn.btid

# Generated at 2022-06-14 17:22:31.959171
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    video = TruTVIE(None)

# Generated at 2022-06-14 17:22:33.020261
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    assert TruTVIE()


# Generated at 2022-06-14 17:22:39.189019
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
	url='https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
	turnerIE = TruTVIE()
	result=turnerIE._real_extract(url)
	assert result['id'] == 'f16c03beec1e84cd7d1a51f11d8fcc29124cc7f1'
	assert result['ext'] == 'mp4'
	assert result['title'] == 'Sunlight-Activated Flower'
	assert result['description'].strip() == "A customer is stunned when he sees Michael's sunlight-activated flower."

# Generated at 2022-06-14 17:22:42.850111
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    global TruTVIE
    TruTVIE_test = TruTVIE()
    if not TruTVIE_test:
        raise AssertionError('Failed to initialize TruTVIE.')
        

# Generated at 2022-06-14 17:22:50.991971
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    t = TruTVIE()
    assert t.name == 'trutv'
    assert t.IE_NAME == 'trutv'
    assert t.IE_DESC == 'TruTV'

# Generated at 2022-06-14 17:22:52.318099
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    trutv = TruTVIE()
    assert True


# Generated at 2022-06-14 17:22:53.633744
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    TruTVIE()

# Generated at 2022-06-14 17:26:22.299864
# Unit test for constructor of class TruTVIE
def test_TruTVIE():
    url = 'https://www.trutv.com/shows/the-carbonaro-effect/videos/sunlight-activated-flower.html'
    trutv_ie = TruTVIE(url)
    assert trutv_ie._VALID_URL == url
    assert trutv_ie._TEST
    assert trutv_ie._extract_ngtv_info
    assert trutv_ie._download_json
    assert trutv_ie._get_mvpd_resource
    assert trutv_ie._real_extract