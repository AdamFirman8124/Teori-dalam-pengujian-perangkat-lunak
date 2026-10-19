

# Generated at 2022-06-14 16:24:08.091894
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordIE = HitRecordIE()
    assert hitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:19.872585
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()

# Generated at 2022-06-14 16:24:22.423096
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    cls = HitRecordIE
    assert cls._VALID_URL is not None
    assert cls._TEST is not None
    assert cls.__name__ is not None

# Generated at 2022-06-14 16:24:30.211684
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit test for constructor of class HitRecordIE
    """
    # Arrange
    # Create instance of HitRecordIE
    hit_record_ie = HitRecordIE()

    # Act
    # Call _real_extract on extracted video
    info_dict = hit_record_ie._real_extract(
        "https://hitrecord.org/records/2954362")

    # Assert
    # Assert that the title is correct
    assert info_dict["title"] == "A Very Different World (HITRECORD x ACLU)"

# Generated at 2022-06-14 16:24:42.273689
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie_result = ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:42.746275
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:43.636762
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(_TEST['url'])

# Generated at 2022-06-14 16:24:48.536916
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()
    except Exception as e:
        print("Unit test of HitRecordIE constructor failed: %s" % (
            e.message), file=sys.stderr)
    else:
        print("Unit test of HitRecordIE constructor successful",
              file=sys.stderr)


# Generated at 2022-06-14 16:24:50.808020
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:24:58.412955
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = 'https://hitrecord.org/records/2954362'
    hr = HitRecordIE()
    hitrecord = hr._real_extract(url)
    assert hitrecord['id'] == '2954362'
    assert hitrecord['url'] == 'https://hitrecord.cloudfront.net/uploads.stage3/a/a/a/2954362/2954362-3d9b7e70e540bf19d746f59a10c28e57.mp4?AWSAccessKeyId=AKIAJP4I4JF4WE4N7JAA&Expires=1472193784&Signature=p4A%2F9y4k0Yk4%2BwJ1FzQZ0v55P8o%3D'

# Generated at 2022-06-14 16:25:13.659376
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hrie = HitRecordIE()
    assert hrie.ie_key() == 'hitrecord:record'
    assert hrie.ie_name() == 'hitrecord:record'
    assert hrie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:17.031401
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:25:18.461653
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:20.753328
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordIE = HitRecordIE()
    assert hitRecordIE is not None

# Generated at 2022-06-14 16:25:32.213843
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE();
    assert ie._VALID_URL, 'Unit Test: Valid URL not defined'
    ie._TEST = {};
    ie._TEST['url'] = ie._VALID_URL;
    ie._real_initialize();
    # unit test known video
    assert ie._TEST['id'] is None, 'Unit Test: ID not defined'
    ie._TEST['info_dict'] = {
        'id': ie._TEST['id'],
        'url': 'https://hitrecord.org/records/2954362'
        };
    info_dict = ie._real_extract(ie._TEST['url']);
    assert info_dict == ie._TEST['info_dict'], 'Unit Test: extraction failed'
    #unit test unknown video
    ie._TEST['url']

# Generated at 2022-06-14 16:25:33.483164
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    tester = HitRecordIE()
    assert tester != None


# Generated at 2022-06-14 16:25:34.051199
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:34.929114
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:25:37.798662
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """Unit test for constructor of class HitRecordIE"""
    HitRecordIE(None)
    # No exceptions should be raised in the constructor

# Generated at 2022-06-14 16:25:38.439462
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:50.395027
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable("http://hitrecord.org/records/2954362")
    assert not ie.suitable("http://hitrecord.org/records/295436")


# Generated at 2022-06-14 16:26:00.944441
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("http://hitrecord.org/records/2954362")
    assert isinstance(ie, InfoExtractor)
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:03.395375
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable("https://hitrecord.org/records/2954362")
    assert not ie.suitable("http://www.example.com")
            

# Generated at 2022-06-14 16:26:09.441301
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:18.893374
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord'
    assert ie.IE_DESC == 'HitRecord'
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:20.977944
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
  HitRecordIE('https://hitrecord.org/records/2954362', 'HitRecordIE')



# Generated at 2022-06-14 16:26:24.999480
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362') == True
    assert ie.suitable('https://hitrecord.org/records/29543623') == False

# Generated at 2022-06-14 16:26:26.655345
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:32.741201
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord.org'
    # Check that the regex has the right name
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:26:33.746579
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
  a = HitRecordIE()

# Generated at 2022-06-14 16:26:53.697951
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE("unit test")
        assert True
    except:
        assert False


# Generated at 2022-06-14 16:26:54.302210
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	pass

# Generated at 2022-06-14 16:26:56.781337
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:27:00.655721
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # First check that HitRecordIE inherits the class InfoExtractor
    assert issubclass(HitRecordIE, InfoExtractor)
    # Now check that HitRecordIE has the correct name
    assert HitRecordIE.IE_NAME == 'hitrecord:record'


# Generated at 2022-06-14 16:27:01.976728
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    res = HitRecordIE()
    assert(res)

# Generated at 2022-06-14 16:27:04.771310
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("http://hitrecord.org/records/2954362")
    assert isinstance(ie, HitRecordIE)

# Generated at 2022-06-14 16:27:06.557610
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE._VALID_URL, HitRecordIE._TEST)

# Generated at 2022-06-14 16:27:08.182634
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL

# Generated at 2022-06-14 16:27:09.333062
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:27:12.415184
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    result = HitRecordIE()._real_extract("https://hitrecord.org/records/2954362")
    assert result['id'] == '2954362'

# Generated at 2022-06-14 16:27:50.748028
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordIE = HitRecordIE()
    assert hitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:57.755895
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:59.091098
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:28:04.184475
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    #Test multiple constructors for correct bindings
    assert HitRecordIE._VALID_URL is not None
    assert HitRecordIE._TEST is not None
    assert HitRecordIE.__module__ is not None
    assert HitRecordIE.name is not None
    assert HitRecordIE.description is not None

# Generated at 2022-06-14 16:28:05.782179
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit test for constructor of class HitRecordIE
    """
    HitRecordIE()

# Generated at 2022-06-14 16:28:06.550114
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	pass

# Generated at 2022-06-14 16:28:07.895376
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:28:09.831830
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE.suitable('https://hitrecord.org/records/2954362') == True

# Generated at 2022-06-14 16:28:10.765454
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


# Generated at 2022-06-14 16:28:18.181418
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    v = HitRecordIE('',{})
    assert v._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert v._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert v._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert v._real_extract('https://hitrecord.org/records/2954362')['id'] == '2954362'

# Generated at 2022-06-14 16:29:18.600094
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    test = ie._TEST
    test_url = test['url']
    video_id = ie._match_id(test_url)
    video = ie._download_json(
        'https://hitrecord.org/api/web/records/%s' % video_id, video_id)
    title = video['title']
    video_url = video['source_url']['mp4_url']

    tags = None
    tags_list = try_get(video, lambda x: x['tags'], list)

# Generated at 2022-06-14 16:29:21.194470
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(2954362) == "https://hitrecord.org/records/2954362"


# Generated at 2022-06-14 16:29:23.052956
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:29:24.122473
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:29:25.195099
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecord = HitRecordIE()
    assert hitRecord is not None

# Generated at 2022-06-14 16:29:26.219148
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	# Initialize
	HitRecordIE()
	pass

# Generated at 2022-06-14 16:29:36.781714
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'

# Generated at 2022-06-14 16:29:38.671461
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert (isinstance(ie, HitRecordIE))

# Generated at 2022-06-14 16:29:45.359567
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_url = 'https://hitrecord.org/records/2954362'
    test_video_id = '2954362'
    test_url2 = 'https://hitrecord.org/records/4877199'
    test_video_id2 = '4877199'
    hitrecord_ie = HitRecordIE()
    assert hitrecord_ie.suitable(test_url) == True
    assert hitrecord_ie.suitable(test_url2) == True
    assert hitrecord_ie._match_id(test_url) == test_video_id
    assert hitrecord_ie._match_id(test_url2) == test_video_id2

# Generated at 2022-06-14 16:29:48.142001
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:31:31.848603
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    vid = "https://hitrecord.org/records/2954362"
    HitRecordIE()._real_initialize(vid)

# Generated at 2022-06-14 16:31:34.884955
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord_ie = HitRecordIE()
    assert hitrecord_ie._VALID_URL == HitRecordIE._VALID_URL
    assert hitrecord_ie._TEST == HitRecordIE._TEST

# Generated at 2022-06-14 16:31:41.569602
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecord_test = HitRecordIE(HitRecordIE._downloader, HitRecordIE._VALID_URL)
    assert hitRecord_test._VALID_URL == HitRecordIE._VALID_URL
    assert hitRecord_test._TEST == HitRecordIE._TEST
    assert hitRecord_test._downloader == HitRecordIE._downloader
    assert hitRecord_test._match_id(HitRecordIE._VALID_URL) == '2954362'
    assert hitRecord_test._real_extract(HitRecordIE._TEST['url']) == HitRecordIE._TEST['info_dict']

# Generated at 2022-06-14 16:31:43.745100
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:31:45.427229
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL.match('https://hitrecord.org/records/2954362') is not None

# Generated at 2022-06-14 16:31:45.941752
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:31:46.453318
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:31:47.172677
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:31:57.991772
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Creation of an instance of class HitRecordIE
    hitrecord = HitRecordIE()
    # Testing the 'url' and 'id' properties of class HitRecordIE
    assert hitrecord._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert hitrecord._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert hitrecord._TEST['info_dict']['id'] == '2954362'
    # testing the '_real_extract' method of class HitRecordIE
    video = hitrecord._real_extract(hitrecord._TEST['url'])
    assert video['id'] == hitrecord._TEST['info_dict']['id']

# Generated at 2022-06-14 16:31:59.437403
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')
