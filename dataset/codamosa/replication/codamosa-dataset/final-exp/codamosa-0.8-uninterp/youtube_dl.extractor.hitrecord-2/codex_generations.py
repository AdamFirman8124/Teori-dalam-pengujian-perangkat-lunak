

# Generated at 2022-06-14 16:24:04.740883
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    HitRecordIE.__init__(url)
    """
    test_hitRecord = HitRecordIE()
    url = test_hitRecord._VALID_URL
    assert url == 'https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'

# Generated at 2022-06-14 16:24:10.338584
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    a = HitRecordIE("http://hitrecord.org/records/2954362")
    assert a._VALID_URL==r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Test for method _real_extract of class HitRecordIE  

# Generated at 2022-06-14 16:24:21.863225
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test empty response
    responseBody = {}
    assert HitRecordIE()._real_extract("", responseBody) is None
    # Test invalid response
    responseBody = { 'title' : "Universes" }
    assert HitRecordIE()._real_extract("", responseBody) is None
    # Test valid response

# Generated at 2022-06-14 16:24:31.054299
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("https://hitrecord.org/records/2954362")
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie.IE_NAME == 'hitrecord'
    assert ie.ie_key() == 'HitRecord'
    assert ie.url_result("https://hitrecord.org/records/2954362") == 'https://hitrecord.org/records/2954362'
    assert ie.video_id("https://hitrecord.org/records/2954362") == '2954362'

# Generated at 2022-06-14 16:24:42.628038
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    url = "https://hitrecord.org/records/2954362"
    video_id = info_extractor._match_id(url)
    assert video_id == '2954362'
    title = info_extractor._download_json(
        'https://hitrecord.org/api/web/records/%s' % video_id, video_id)
    assert title == 'A Very Different World (HITRECORD x ACLU)'
    video_url = info_extractor._download_json(
        'https://hitrecord.org/api/web/records/%s' % video_id, video_id)

# Generated at 2022-06-14 16:24:46.055499
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:47.678635
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecordIE = HitRecordIE()

    assert hitrecordIE.__class__.__name__ == 'HitRecordIE'

# Generated at 2022-06-14 16:24:48.267470
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:57.340394
# Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:25:00.108010
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(None)
    assert ie.SITE_NAME == "HitRecord"
    assert ie.AVAILABLE_TRANSFORM_FUNCTIONS == None

# Generated at 2022-06-14 16:25:09.570984
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:11.696906
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = 'https://hitrecord.org/records/2954362'
    ie = HitRecordIE()
    ie.extract(url)

# Generated at 2022-06-14 16:25:13.326575
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    print(hitrecord._VALID_URL)
    print(hitrecord._TEST)

# Generated at 2022-06-14 16:25:14.936958
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:25:16.473468
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:25:17.132679
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE

# Generated at 2022-06-14 16:25:17.893069
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:20.531962
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # test HitRecordIE constructor
    HitRecordIE()


# Generated at 2022-06-14 16:25:32.026642
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    info_extractor = HitRecordIE()

    # Test real url
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

    assert info_extractor._match_id('https://hitrecord.org/records/2954362') == '2954362'

    # Test test

# Generated at 2022-06-14 16:25:34.638747
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:25:54.256236
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	ie = HitRecordIE(None)
	assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:57.549804
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    i = HitRecordIE()
    url = 'https://hitrecord.org/records/6730313'
    id = i._match_id(url)
    assert id == '6730313', 'ID should be 6730313'

# Generated at 2022-06-14 16:26:05.577454
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    assert info_extractor._VALID_URL == '(?i)(?:https?://)?(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'
    assert info_extractor._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert info_extractor._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert info_extractor._TEST['info_dict']['id'] == '2954362'
    assert info_extractor._TEST['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 16:26:10.073716
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Testing different URLs
    HitRecordIE()._real_extract(
        'https://hitrecord.org/records/2954362')
    HitRecordIE()._real_extract(
        'http://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:11.218603
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(InfoExtractor)

# Generated at 2022-06-14 16:26:20.044850
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE()._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert HitRecordIE()._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert HitRecordIE()._TEST['info_dict']['id'] == '2954362'
    assert HitRecordIE()._TEST['info_dict']['ext'] == 'mp4'
    assert HitRecordIE()._TEST['info_dict']['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:26:20.624487
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:21.237406
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:31.020030
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    video = HitRecordIE()
    video._download_json = lambda *args, **kwargs: {'title': 'A Very Different World (HITRECORD x ACLU)'}

# Generated at 2022-06-14 16:26:32.158852
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    return HitRecordIE()

# Generated at 2022-06-14 16:26:51.653766
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(HitRecordIE._VALID_URL)
    assert ie is not None


# Generated at 2022-06-14 16:26:53.341161
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit test for constructor of class HitRecordIE
    """
    assert HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:26:54.295739
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE.ie_key())

# Generated at 2022-06-14 16:26:55.602475
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(HitRecordIE._TEST)

# Generated at 2022-06-14 16:26:56.158330
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:26:57.356435
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:59.077393
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('hitrecord', '2954362')
    assert(ie.suitable('https://hitrecord.org/records/2954362'))

# Generated at 2022-06-14 16:26:59.773723
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:02.261197
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()
    except TypeError:
        pass
    else:
        raise Exception('Unit test failed')

# Generated at 2022-06-14 16:27:14.058568
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hre = HitRecordIE()
    # Unit test for regular expression
    assert hre._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert hre._TEST['url'] == 'https://hitrecord.org/records/2954362'
    # Test the real_extract function

# Generated at 2022-06-14 16:28:05.733607
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')

    assert ie._match_id('https://hitrecord.org/records/2954362') == '2954362'

# Generated at 2022-06-14 16:28:14.144893
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)"

# Generated at 2022-06-14 16:28:24.769090
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hrIE = HitRecordIE('https://www.hitrecord.org/records/2954362')
    print("Successfully constructed the object")
    assert isinstance(hrIE,InfoExtractor)
    assert hrIE.IE_NAME == 'hitrecord'
    assert hrIE.IE_DESC == 'HitRecord'
    assert hrIE._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert hrIE._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert hrIE._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert hrIE._TEST['info_dict']['id'] == '2954362'


# Generated at 2022-06-14 16:28:27.871743
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE('https://hitrecord.org/records/2954362')
    assert HitRecordIE('https://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:28:30.210132
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


if __name__ == '__main__':
    test_HitRecordIE()

# Generated at 2022-06-14 16:28:31.445561
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert isinstance(ie, HitRecordIE)

# Generated at 2022-06-14 16:28:32.475482
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_class = HitRecordIE()

# Generated at 2022-06-14 16:28:33.731442
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    from .html5_extractor_test import test_class_constructor_expression
    return test_class_constructor_expression('HitRecordIE')

# Generated at 2022-06-14 16:28:34.157743
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:37.084884
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(HitRecordIE._VALID_URL)
    if ie._TEST:
        if ie.suitable(ie._TEST['url']):
            if ie._real_extract(ie._TEST['url']):
                return True
    return False

# Generated at 2022-06-14 16:30:20.667444
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie._downloader.cache.remove()

# Generated at 2022-06-14 16:30:24.546636
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE.__name__ == 'HitRecord'
    assert HitRecordIE.__doc__ == 'hitrecord.org video extractor'


# Generated at 2022-06-14 16:30:25.673508
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test constructor attributes
    HitRecordIE()

# Generated at 2022-06-14 16:30:30.072701
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    video_id = '2954362'
    assert(HitRecordIE._VALID_URL == HitRecordIE._TEST['url'])
    assert(video_id == HitRecordIE._TEST['info_dict']['id'])

# Generated at 2022-06-14 16:30:32.852069
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert isinstance(ie, HitRecordIE)

# Generated at 2022-06-14 16:30:34.042131
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(HitRecordIE._VALID_URL, HitRecordIE._TEST)

# Generated at 2022-06-14 16:30:34.882382
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_HitRecordIE = HitRecordIE()

# Generated at 2022-06-14 16:30:37.063698
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    h = HitRecordIE()
    print("hitrecord test constructor: ")
    print(h)
    assert(h is not None)


# Generated at 2022-06-14 16:30:37.622134
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:30:38.299574
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()