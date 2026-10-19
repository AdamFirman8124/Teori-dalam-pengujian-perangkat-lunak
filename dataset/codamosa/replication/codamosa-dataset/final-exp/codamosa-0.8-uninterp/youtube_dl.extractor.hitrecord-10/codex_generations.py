

# Generated at 2022-06-14 16:24:01.255618
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:01.820886
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:24:06.120354
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	# Constructor 1
	if HitRecordIE.suitable('https://hitrecord.org/records/2954362') != True:
		print("[test_HitRecordIE] constructor 1 failed")
	# Constructor 2
	if HitRecordIE.suitable('https://hitrecord.org') == True:
		print("[test_HitRecordIE] constructor 2 failed")


# Generated at 2022-06-14 16:24:11.881460
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    valid_url = 'https://hitrecord.org/records/2954362'
    regex_factory = r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE._VALID_URL == regex_factory

# Generated at 2022-06-14 16:24:23.949656
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecordIE = HitRecordIE()


# Generated at 2022-06-14 16:24:24.658556
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print(HitRecordIE())

# Generated at 2022-06-14 16:24:26.363229
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_video = HitRecordIE(HitRecordIE._TEST)
    assert(test_video.get_id() == '2954362')

# Generated at 2022-06-14 16:24:36.748342
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:37.355750
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:38.820958
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	test_HitRecordIE()

# Generated at 2022-06-14 16:24:50.807182
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    he = HitRecordIE()
    assert he._TEST['url'] == 'https://hitrecord.org/records/2954362'


# Generated at 2022-06-14 16:24:52.254049
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """ Just a test to create HitRecordIE class """
    HitRecordIE()

# Generated at 2022-06-14 16:24:53.138349
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:53.697360
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:06.050915
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

    url = 'https://hitrecord.org/records/2954362'
    video_id = '2954362'

    # Validate URL
    assert ie._VALID_URL == ie._VALID_URL_TEMPLATE

    # Check invalid URLs
    assert ie.suitable('https://hitrecord.org/records') is False
    assert ie.suitable('https://hitrecord.org/') is False
    assert ie.suitable('http://hitrecord.org/records/2954362') is False
    assert ie.suitable('https://hitrecord.org/records/2954362/reviews') is False
    assert ie.suitable('https://hitrecord.org/records/2954362/submissions') is False

# Generated at 2022-06-14 16:25:06.735090
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:09.078868
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('http://www.hitrecord.org/records/2954362')
    ie.test_result()

# Generated at 2022-06-14 16:25:15.870115
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    # Positive tests
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert ie.suitable('http://hitrecord.org/records/2954362')
    assert ie.suitable('https://www.hitrecord.org/records/2954362')
    assert ie.suitable('http://www.hitrecord.org/records/2954362')
    # Negative tests
    assert not ie.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('http://www.hitrecord.org')

# Generated at 2022-06-14 16:25:16.978816
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()


# Generated at 2022-06-14 16:25:18.933119
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE.__name__ == 'HitRecordIE'

# Generated at 2022-06-14 16:25:33.145492
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE();
    url = 'https://hitrecord.org/records/2954362'
    assert ie._match_id(url) == '2954362'
    assert ie._VALID_URL == ie._TEST['url']
    assert ie._TEST == ie._download_json(ie._VALID_URL, ie._TEST['url'])

# Generated at 2022-06-14 16:25:34.389002
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    init = HitRecordIE(0)
    print(init)


# Generated at 2022-06-14 16:25:35.010931
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:37.024678
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:25:37.664315
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:39.598094
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == HitRecordIE._VALID_URL


# Generated at 2022-06-14 16:25:40.836280
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:42.711362
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    print(hitrecord)

# Generated at 2022-06-14 16:25:43.461517
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:44.172892
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:26:04.776578
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_ie = HitRecordIE("")
    assert test_ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:07.938245
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._TEST['url'] == HitRecordIE._VALID_URL % HitRecordIE._TEST['info_dict']['id']

# Generated at 2022-06-14 16:26:09.526549
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    y = HitRecordIE()
    y._match_id
    y._real_extract

# Generated at 2022-06-14 16:26:12.397622
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == 'https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'

# Generated at 2022-06-14 16:26:13.805130
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    lst=HitRecordIE("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:26:16.003376
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.download('https://hitrecord.org/records/2954362')
    ie.extract()

# Generated at 2022-06-14 16:26:26.300490
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	print("[=== Start testing HitRecordIE ===]")
	extractor = HitRecordIE()
	# Test url
	url = "https://hitrecord.org/records/2954362"
	result = extractor._real_extract(url)
	print("The extracted id is %s" % result['id'])
	print("The extracted url is %s" % result['url'])
	print("The extracted title is %s" % result['title'])
	print("The extracted description is %s" % result['description'])
	print("The extracted duration is %s" % result['duration'])
	print("The extracted uploader is %s" % result['uploader'])
	print("The extracted timestamp is %s" % result['timestamp'])

# Generated at 2022-06-14 16:26:26.918403
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    # Test not working
    assert False


# Generated at 2022-06-14 16:26:28.466826
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:33.631947
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print('Testing class HitRecordIE')
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    print(ie)
    if ie:
        print('yes')
    else:
        print('no')


# Generated at 2022-06-14 16:27:12.629831
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'HitRecord'

# Generated at 2022-06-14 16:27:14.267281
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    assert info_extractor.IE_NAME == 'hitrecord'

# Generated at 2022-06-14 16:27:15.453323
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:27:16.627543
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")


# Generated at 2022-06-14 16:27:21.142864
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit test for constructor of class HitRecordIE
    """
    ie = HitRecordIE()
    assert isinstance(ie, HitRecordIE)
    assert isinstance(ie.get_info, object)
    assert ie.name == 'hitrecord'



# Generated at 2022-06-14 16:27:23.146329
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL[:10] == 'https://hitrecord.org/records/'

# Generated at 2022-06-14 16:27:24.339816
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:28.110508
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    test HitRecordIE's constructor
    """
    extractor = HitRecordIE(
        HitRecordIE._create_get_url_opener(HitRecordIE._TEST))
    assert extractor.url_result.video_id == '2954362'

# Generated at 2022-06-14 16:27:29.885784
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	ns = HitRecordIE(HitRecordIE._VALID_URL)

if __name__ == "__main__":
	test_HitRecordIE

# Generated at 2022-06-14 16:27:30.794838
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:29:07.195947
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test constructor of HitRecordIE class
    hitrecordie = HitRecordIE()




# Generated at 2022-06-14 16:29:16.300553
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    expect = {
        'id': '2954362',
        'url': 'https://www.hitrecord.org/records/2954362',
        'title': 'A Very Different World (HITRECORD x ACLU)',
        'description': 'md5:e62defaffab5075a5277736bead95a3d',
        'duration': 139.327,
        'timestamp': 1471557582,
        'upload_date': '20160818',
        'uploader': 'Zuzi.C12',
        'uploader_id': '362811',
        'view_count': int,
        'like_count': int,
        'comment_count': int,
        'tags': list,
    }
    actual = HitRecordIE()._real_extract(expect['url'])

# Generated at 2022-06-14 16:29:19.322513
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    i = HitRecordIE()

# Generated at 2022-06-14 16:29:20.128339
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:29:31.801222
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    rIE = HitRecordIE()
    assert(rIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

# Generated at 2022-06-14 16:29:34.012894
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE('https://www.youtube.com/watch?v=ZjUbf4w4M4k')
    assert hitrecord is not None

# Generated at 2022-06-14 16:29:37.093931
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://www.HitRecord.org/records/2954362')

# Generated at 2022-06-14 16:29:37.946975
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:29:38.673409
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:29:42.101315
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert hasattr(ie, '_VALID_URL'), '_VALID_URL not found'
    assert hasattr(ie, '_TEST'), '_TEST not found'
    assert hasattr(ie, '_real_extract'), '_real_extract not found'

# Generated at 2022-06-14 16:33:37.256644
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('http://hitrecord.org/records/2954362')
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:33:38.123101
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:33:40.786466
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    #Test Constructor
    HitRecordIE(HitRecordIE._VALID_URL)


# Generated at 2022-06-14 16:33:41.299916
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:33:42.650658
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
  HitRecordIE('SOME_URL')

# Generated at 2022-06-14 16:33:45.171662
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# To test the above function, uncomment the below line and run the command below
# python -m unittest -v test_HitRecordIE.py

# End of Code

# Generated at 2022-06-14 16:33:47.862356
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert(ie._VALID_URL == HitRecordIE._VALID_URL)


# Generated at 2022-06-14 16:33:48.364070
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    pass

# Generated at 2022-06-14 16:33:50.098944
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == HitRecordIE._VALID_URL
    assert HitRecordIE()._TEST == HitRecordIE._TEST