

# Generated at 2022-06-14 16:24:10.443612
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    extractor = HitRecordIE()
    # test for following inputs
    valid_inputs = [
        'https://hitrecord.org/records/2954362',
        'http://hitrecord.org/records/2954362',
        'https://www.hitrecord.org/records/2954362',
    ]

    for url in valid_inputs:
        print('Testing for url:', url)
        assert extractor._VALID_URL.match(url)

    invalid_inputs = [
        'http://hitrecord.org/records/',
        'https://www.hitrecord.org/records/',
        'https://www.hitrecord.org/'
    ]

    for url in invalid_inputs:
        print('Testing for url:', url)
        assert extractor._VALID_

# Generated at 2022-06-14 16:24:11.733541
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Constructor
    obj = HitRecordIE()

# Generated at 2022-06-14 16:24:12.085292
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    return HitRecordIE()

# Generated at 2022-06-14 16:24:15.578554
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test for constructor
    # test for function _real_extract
    # test for function _real_initialize
    print("testing")


if __name__ == '__main__':
    test_HitRecordIE()

# Generated at 2022-06-14 16:24:17.617780
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    assert info_extractor.ie_key() == 'hitrecord'

# Generated at 2022-06-14 16:24:21.178831
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    HitRecordIE._TEST
    HitRecordIE._TEST['md5']
    HitRecordIE._TEST['info_dict']
    HitRecordIE._TEST['info_dict']['tags']

# Generated at 2022-06-14 16:24:21.798357
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:27.709804
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    from .common import InfoExtractor
    from .youtube import YoutubeIE
    print("Testing constructor of class HitRecordIE")
    assert InfoExtractor.ie_key() == 'HitRecord'
    assert HitRecordIE.ie_key() == 'HitRecord'
    assert YoutubeIE.ie_key() != 'HitRecord'


# Generated at 2022-06-14 16:24:29.750949
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:31.008636
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert (ie.ie_key() == 'hitrecord')

# Generated at 2022-06-14 16:24:40.799024
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:49.489733
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    i = HitRecordIE()
    assert i.IE_NAME == 'HitRecord'
    assert i._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:51.405924
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE._VALID_URL)


# Generated at 2022-06-14 16:24:52.338672
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()

# Generated at 2022-06-14 16:24:53.213004
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	assert HitRecordIE._TEST

# Generated at 2022-06-14 16:24:59.325205
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'


# Generated at 2022-06-14 16:25:00.608450
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(HitRecordIE._VALID_URL, str)
    assert isinstance(HitRecordIE._TEST, dict)

# Generated at 2022-06-14 16:25:06.362377
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    video_url = 'https://hitrecord.org/records/2954362'
    try:
        HitRecordIE(HitRecordIE._VALID_URL, video_url)
    except:
        success = False
    else:
        success = True
    assert(success == True)



# Generated at 2022-06-14 16:25:06.990369
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:12.468968
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie.url == 'https://hitrecord.org/records/2954362'
    assert ie.video_id == '2954362'
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:25:23.568182
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Constructor test of class HitRecordIE.
    """
    ie = HitRecordIE()

# Generated at 2022-06-14 16:25:26.582436
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    expected = HitRecordIE
    if expected is not HitRecordIE:
        raise AssertionError(
            'Expected %s but received %s' % (expected, HitRecordIE))



# Generated at 2022-06-14 16:25:28.096145
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	# Test that class HitRecordIE implements __init__ correctly
	assert True

# Generated at 2022-06-14 16:25:29.472414
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	import hitrecord

	# Instantiate a class
	assert isinstance( hitrecord.HitRecordIE, object )

# Generated at 2022-06-14 16:25:41.935901
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'

# Generated at 2022-06-14 16:25:45.853779
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.suitable('https://hitrecord.org/records/2954362')
    ie.download('https://hitrecord.org/records/2954362')

# test_HitRecordIE()

# Generated at 2022-06-14 16:25:54.594478
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Set up
    url = 'https://hitrecord.org/records/2954362'
    ret = HitRecordIE(url)

    # Edge case
    if ret.url != url:
        print("url is not the same")
    if ret.user_id != '362811':
        print("wrong user id")
    if ret.host != 'hitrecord':
        print("host is not what we want")
    if ret.video_id != '2954362':
        print("video_id is not what we want")


if __name__ == '__main__':
    test_HitRecordIE()

# Generated at 2022-06-14 16:25:59.269355
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    # tests for private members of class HitRecordIE
    assert HitRecordIE._VALID_URL is not None
    assert HitRecordIE._TEST is not None

    # tests for public members of class HitRecordIE
    ie = HitRecordIE()
    assert ie._real_extract is not None
    assert ie._match_id is not None
    assert ie._download_json is not None

# Generated at 2022-06-14 16:25:59.830057
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:01.347749
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362', 'test_HitRecordIE')

# Generated at 2022-06-14 16:26:21.981215
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE
    assert HitRecordIE

# Generated at 2022-06-14 16:26:25.232694
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_HitRecordIE = HitRecordIE()
    test_HitRecordIE()
#=====================================================

# Constructor for class ScrappablePlaylistBaseIE

# Generated at 2022-06-14 16:26:26.166596
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE.suite()

# Generated at 2022-06-14 16:26:28.009135
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    assert hitrecord.IE_NAME == 'hitrecord:record'
    assert hitrecord.valid_url('https://hitrecord.org/records/2954362')
    assert not hitrecord.valid_url('https://hitrecord.org')
    assert hitrecord.find_video_id('https://hitrecord.org/records/2954362') == '2954362'

# Generated at 2022-06-14 16:26:31.909327
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('test')
    assert ie.valid_url('https://hitrecord.org/records/2954362')
    assert ie.valid_url('https://www.hitrecord.org/records/2954362')
    assert not ie.valid_url('https://hitrecord.org/foo')
    assert not ie.valid_url('https://hitrecord.org/')

# Generated at 2022-06-14 16:26:33.341620
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.download(url = "https://hitrecord.org/records/2954945")

# Generated at 2022-06-14 16:26:35.658198
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    e = HitRecordIE()
    assert e


if __name__ == '__main__':
    # TODO: add unit tests
    test_HitRecordIE()
    test_HitRecordIE().test()

# Generated at 2022-06-14 16:26:36.182477
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:36.793528
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:37.357352
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:28.298118
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert ie._TEST['info_dict']['id'] == '2954362'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
    assert ie._TEST['info_dict']['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:27:30.529110
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:27:31.672565
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:35.934500
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.name == 'hitrecord'
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:39.385530
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    assert (info_extractor._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')



# Generated at 2022-06-14 16:27:46.628046
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print("\nRunning test for HitRecordIE")
    URL = 'https://hitrecord.org/records/2954362'
    instance = HitRecordIE()
    assert instance._VALID_URL == instance._VALID_URL
    assert instance._TEST['url'] == instance._TEST['url']
    assert instance._TEST['md5'] == instance._TEST['md5']
    assert instance._TEST['info_dict'] == instance._TEST['info_dict']
    print("\tTest Passed")


# Generated at 2022-06-14 16:27:47.884284
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord'

# Generated at 2022-06-14 16:27:50.040528
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    i = HitRecordIE(None)
    assert i.VALID_URL == i._VALID_URL
    assert i.TEST == i._TEST

# Generated at 2022-06-14 16:27:57.304943
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    e = HitRecordIE("http://hitrecord.org/records/2954362")
    assert e.url == "https://hitrecord.org/records/2954362"
    assert e.name == "HitRecord"
    assert e._VALID_URL == "https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)"
    assert e.id == "HitRecord"
    assert e.IE_NAME == "hitrecord:record"
    assert e.app_name == "hitrecord"
    assert e.app_version == "1"
    assert e.app_url == "https://www.hitrecord.org"

# Generated at 2022-06-14 16:27:58.781814
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # check that HitRecordIE object is created
    assert(HitRecordIE)

    return

# Generated at 2022-06-14 16:29:43.968625
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()
        assert(True)
    except:
        assert(False)


# Generated at 2022-06-14 16:29:48.485284
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	ie = HitRecordIE()
	# test for the methods in class InfoExtractor
	assert ie.suitable('https://hitrecord.org/records/2954362')
	assert not ie.suitable('https://www.yahoo.com')
	# test for the method in class YoutubeIE
	assert ie._real_extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:29:53.436578
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.NAME == 'HitRecord'
    assert ie.IE_NAME == 'hitrecord'
    assert ie.HEADERS['User-Agent'] == 'Mozilla/5.0'
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:03.758083
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:09.514262
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    object_hitRecord = HitRecordIE()
    assert object_hitRecord._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:20.552834
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Check if the class constructor works properly
    """
    # r'https?://(www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:24.723231
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL.match(HitRecordIE._TEST['url'])
    assert ie._VALID_URL.match('https://hitrecord.org/records/2954362')
    assert ie._VALID_URL.match('https://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:30:35.815288
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE();
    assert isinstance(ie, InfoExtractor);
    assert isinstance(ie._VALID_URL, (str, unicode));
    assert isinstance(ie._TEST, dict);
    assert isinstance(ie._TEST['url'], (str, unicode));
    assert isinstance(ie._TEST['md5'], (str, unicode));
    assert isinstance(ie._TEST['info_dict'], dict);
    assert isinstance(ie._TEST['info_dict']['id'], (str, unicode));
    assert isinstance(ie._TEST['info_dict']['ext'], (str, unicode));
    assert isinstance(ie._TEST['info_dict']['title'], (str, unicode));

# Generated at 2022-06-14 16:30:36.859429
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()(None)

# Generated at 2022-06-14 16:30:38.562381
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    print("Unit test for constructor of class HitRecordIE")
    return True
