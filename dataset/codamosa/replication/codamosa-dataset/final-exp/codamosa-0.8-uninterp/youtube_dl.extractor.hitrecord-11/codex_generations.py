

# Generated at 2022-06-14 16:24:11.018721
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    # Unit test for _real_extract(url)

# Generated at 2022-06-14 16:24:11.678209
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:18.717323
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Dummy url
    url="https://hitrecord.org/records/2954362"

    # In case the url is not valid, an error should be raised
    try:
        infoExtractor=HitRecordIE()
        infoExtractor.url_result(url)
        assert False
    except:
        assert True

    # In case the url is valid, all should go fine
    infoExtractor=HitRecordIE()
    assert infoExtractor.url_result(url)

# Generated at 2022-06-14 16:24:21.025000
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = 'https://hitrecord.org/records/2954362'
    HitRecordIE(HitRecordIE()).suitable(url)

# Generated at 2022-06-14 16:24:32.064216
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordIE = HitRecordIE()
    assert(hitRecordIE._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)")

# Generated at 2022-06-14 16:24:32.649397
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:36.152212
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    info_extractor.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:36.749260
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:37.349835
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	pass

# Generated at 2022-06-14 16:24:42.804400
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    if ie._VALID_URL != HitRecordIE._VALID_URL:
        print ('FAIL: _VALID_URL must be %s' % HitRecordIE._VALID_URL)
    if ie._TEST != HitRecordIE._TEST:
        print ('FAIL: _TEST must be %s' % HitRecordIE._TEST)

# Generated at 2022-06-14 16:24:47.849152
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:49.178600
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:51.032505
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert isinstance(HitRecordIE, InfoExtractor)


# Generated at 2022-06-14 16:24:52.421588
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert(ie != None)

# Generated at 2022-06-14 16:24:54.573541
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL=='https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'

# Generated at 2022-06-14 16:24:59.084271
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord'
    assert ie.IE_DESC == 'hitrecord.org'
    assert ie.IE_VERSION == '0.1.1'
    assert ie.VALID_URL == 'https://hitrecord.org/records/*'

# Generated at 2022-06-14 16:25:03.401119
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    inst = HitRecordIE()
    assert inst._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:25:05.557683
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.suitable("""https://hitrecord.org/records/2954362""")

# Generated at 2022-06-14 16:25:08.213264
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_input = "https://hitrecord.org/records/2954362"
    #Testing class constructor
    HitRecordIE(test_input)


# Generated at 2022-06-14 16:25:08.577105
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:21.081410
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()
    assert obj.ie_key() == 'HitRecord'
    assert obj.ie_name() == 'HitRecord.org'

# Generated at 2022-06-14 16:25:23.759441
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE("not a real url")
    assert (instance.IE_NAME == "hitrecord")

# Generated at 2022-06-14 16:25:24.394244
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:24.741224
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:34.889589
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Constructor without arguments
    instance = HitRecordIE()
    assert instance.name == 'hitrecord'
    assert instance._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:38.201034
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	# Test constructors of the HitRecordIE class
	# Intentionally empty
	assert (HitRecordIE is not None), "Failed to instantiate HitRecordIE class"

# Generated at 2022-06-14 16:25:38.926594
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:41.000898
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()
    print("Unit test for constructor of class HitRecordIE")

# Generated at 2022-06-14 16:25:41.541336
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:42.124602
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:02.243665
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    assert hitrecord._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:08.700260
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == (
        r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')
    assert ie._TEST['url'] == ('https://hitrecord.org/records/2954362')
    assert ie._TEST['md5'] == ('fe1cdc2023bce0bbb95c39c57426aa71')
    assert ie._TEST['info_dict']['id'] == ('2954362')
    assert ie._TEST['info_dict']['ext'] == ('mp4')
    assert ie._TEST['info_dict']['title'] == (
        'A Very Different World (HITRECORD x ACLU)')

# Generated at 2022-06-14 16:26:09.265282
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:12.486909
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._TEST['url'] == ie._VALID_URL
    assert ie._TEST['id'] == ie._VALID_URL.split('/')[-1]

# Generated at 2022-06-14 16:26:21.410642
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:31.167264
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    m = HitRecordIE()
    m.to_screen(m.IE_NAME)
    _VALID_URL = r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    valid_url = m.extract(url="https://hitrecord.org/records/2954362")
    m.to_screen(valid_url["id"])
    m.to_screen(valid_url["url"])
    m.to_screen(valid_url["title"])
    m.to_screen(valid_url["description"])
    m.to_screen(valid_url["duration"])
    m.to_screen(valid_url["timestamp"])
    m.to_screen(valid_url["uploader"])

# Generated at 2022-06-14 16:26:32.777665
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    video_id = "2954362"
    HitRecordIE(video_id)

# Generated at 2022-06-14 16:26:33.790529
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('HitRecordIE');

# Generated at 2022-06-14 16:26:35.294910
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'hitrecord'


# Generated at 2022-06-14 16:26:37.269066
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    global HitRecordIE
    assert HitRecordIE._valid_url(HitRecordIE._TEST['url']) == True

# Generated at 2022-06-14 16:27:26.440707
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    testUrl = 'http://hitrecord.org/records/2954362'
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE._TEST['url'] == testUrl
    assert HitRecordIE._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert HitRecordIE._TEST['info_dict']['id'] == '2954362'
    assert HitRecordIE._TEST['info_dict']['ext'] == 'mp4'
    assert HitRecordIE._TEST['info_dict']['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:27:27.432672
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


# Generated at 2022-06-14 16:27:28.765847
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE([]) is not None


# Generated at 2022-06-14 16:27:30.160532
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    import unittest
    HitRecordIE('HitRecordIE', unittest.TestCase())

# Generated at 2022-06-14 16:27:34.167636
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Constructor
    TestHitRecordIE = HitRecordIE()
    # Check if TestHitRecordIE is indeed a instance of the HitRecordIE class
    assert isinstance(TestHitRecordIE, HitRecordIE)

# Generated at 2022-06-14 16:27:36.320813
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    # Constructor of class HitRecordIE is not tested because
    # it has no '_real_initialize' method
    pass



# Generated at 2022-06-14 16:27:39.908455
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()
    assert obj.suitable('https://hitrecord.org/records/2954362') == True
    assert obj.suitable('https://hitrecord.org/records/29543622') == False

# Generated at 2022-06-14 16:27:43.813172
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.suitable('https://hitrecord.org/records/2954362')
    assert ie.match('https://hitrecord.org/records/2954362') is not None
    assert ie.suitable('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:27:44.344379
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:53.932999
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    assert hitrecord._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:29:30.701502
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()._real_extract("")

# Generated at 2022-06-14 16:29:33.936192
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.extractor.get_id() == 'hitrecord'
    assert ie.extractor.get_url_regex() == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:29:34.434350
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:29:38.081368
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test constructor of HitRecordIE with valid url
    HitRecordIE(None)


# Generated at 2022-06-14 16:29:38.774480
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:29:40.243699
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie == HitRecordIE

# Generated at 2022-06-14 16:29:51.518136
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:29:53.117181
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:29:55.653496
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE().extract_urls('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:29:57.960572
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord:record'
    assert ie.IE_DESC == 'HitRecord'

# Generated at 2022-06-14 16:33:33.480020
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:33:36.195684
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == HitRecordIE._VALID_URL
    assert ie._TEST == HitRecordIE._TEST



# Generated at 2022-06-14 16:33:40.704280
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # A test method
    # In order to prove that class HitRecordIE can be successfully initiated with different
    # parameters, two test cases are successfully tested.
    test_case_1 = HitRecordIE()
    test_case_2 = HitRecordIE('test_method', 'test_param')

# Generated at 2022-06-14 16:33:45.394567
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print("*** Running HitRecordIE tests ***")
    br = HitRecordIE()
    assert br._match_id('https://hitrecord.org/records/2954362') == "2954362"
    assert br._download_json('https://hitrecord.org/api/web/records/2954362', "2954362")
    print("*** HitRecordIE tests completed ***")

# Generated at 2022-06-14 16:33:47.668131
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	hitrecordIE = HitRecordIE()
	assert isinstance(hitrecordIE, InfoExtractor)

# Generated at 2022-06-14 16:33:54.718867
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'