

# Generated at 2022-06-14 16:24:10.603217
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    assert hitrecord
    assert hitrecord._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:11.993089
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    i = HitRecordIE()
    assert i is not None

# Generated at 2022-06-14 16:24:15.902842
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(2545763)
    ext = ie.extract()
    assert ext['id'] == '2545763'
    assert ext['timestamp'] == 1478914060
    assert ext['duration'] == 60.899

# Generated at 2022-06-14 16:24:17.077918
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:26.255634
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	
	# downloaded_json_files = []

	# def download_json(self, *args, **kwargs):
	# 	downloaded_json_files.append(args[0])
	# 	return super(HitRecordIE, self)._download_json(*args, **kwargs)

	# HitRecordIE._download_json = download_json

	ie = HitRecordIE()
	ie._download_json('https://hitrecord.org/api/web/records/2954362')
	assert (downloaded_json_files == 'https://hitrecord.org/api/web/records/2954362')

# Generated at 2022-06-14 16:24:36.567468
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:46.921252
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("HitRecordIE", "https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:24:56.368673
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    This tests that constructor of HitRecordIE Class
    creates a HitRecordIE class with appropriate attributes
    """
    test_url = 'https://hitrecord.org/records/2954362'
    test_video_id = '2954362'
    test_ie = HitRecordIE(unit_test=True)._real_extract(test_url)
    assert(test_ie['id'] == test_video_id)

# Generated at 2022-06-14 16:25:08.457865
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

    assert(ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

# Generated at 2022-06-14 16:25:09.201784
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()
    return

# Generated at 2022-06-14 16:25:19.547358
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    recorded = HitRecordIE()
    print(recorded)

# Generated at 2022-06-14 16:25:24.190041
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert hasattr(ie, "_TEST")


# Generated at 2022-06-14 16:25:24.874506
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    t = HitRecordIE()
#     t.
    

# Generated at 2022-06-14 16:25:26.023614
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert ie.ie_key() == 'HitRecord'

# Generated at 2022-06-14 16:25:27.099973
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:36.570646
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:37.309066
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:38.390759
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:25:41.645254
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecord = HitRecordIE()

# Generated at 2022-06-14 16:25:42.300350
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:08.785084
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('A Very Different World (HITRECORD x ACLU)')
    assert ie._NAME == 'HitRecord'
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:09.722624
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE is not None

# Generated at 2022-06-14 16:26:10.800993
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


# Generated at 2022-06-14 16:26:12.759100
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    extractor = HitRecordIE()

    assert extractor.get_id() == 'HitRecord'

# Generated at 2022-06-14 16:26:15.226453
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	"""
	Constructor of class HitRecordIE
	"""
	assert HitRecordIE()._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:26:16.641208
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	hit_record_ie = HitRecordIE()


# Generated at 2022-06-14 16:26:19.352546
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = "https://hitrecord.org/records/2954362"
    hitrecord_ie = HitRecordIE()
    assert hitrecord_ie._match_id('https://hitrecord.org/records/2954362') == '2954362'

# Generated at 2022-06-14 16:26:24.372480
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test HitRecordIE initialized with url_or_request
    url_or_request = 'https://hitrecord.org/records/2954362'
    ie = HitRecordIE(url_or_request)
    assert ie.url == 'https://hitrecord.org/records/2954362'


# Generated at 2022-06-14 16:26:26.046408
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:27.650991
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    __import__('sys').modules['HitRecordIE'] = HitRecordIE
    import unittest
    from .test_HitRecordIE import TestHitRecordIE
    TestHitRecordIE('test_constructor').test()

# Generated at 2022-06-14 16:26:47.159807
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    assert isinstance(info_extractor, InfoExtractor) == True


# Generated at 2022-06-14 16:26:57.167358
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	assert HitRecordIE()._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
	assert HitRecordIE()._TEST['url'] == 'https://hitrecord.org/records/2954362'
	assert HitRecordIE()._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'

# Generated at 2022-06-14 16:26:58.940535
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie is not None


# Generated at 2022-06-14 16:26:59.653004
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:00.422991
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:09.387612
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Create a fake test class instance of InfoExtractor
    class FakeInfoExtractor(InfoExtractor):
        def __init__(self):
            InfoExtractor.__init__(self)

    # Run constructor of HitRecordIE class with fake test instance as argument
    try:
        HitRecordIE(FakeInfoExtractor())
    except Exception as e:
        # Print error message if an exception is thrown
        print('Error: ' + str(e.message))
    else:
        # Success
        print('HitRecordIE constructor successfully completed!')

# Define main function

# Generated at 2022-06-14 16:27:12.535615
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:27:14.183763
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(HitRecordIE._VALID_URL, HitRecordIE._TEST)
    print(ie)

# Generated at 2022-06-14 16:27:15.369798
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE._VALID_URL)

# Generated at 2022-06-14 16:27:16.036631
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:06.998004
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert not ie.suitable('https://hitrecord.org/records/2954362/chapters')

# Generated at 2022-06-14 16:28:08.117945
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE is not None

# Generated at 2022-06-14 16:28:11.059104
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # since HitRecordIE.successor is None, it shouldn't work
    ie = HitRecordIE('http://www.hitrecord.org/records/2954362')
    assert ie.extractor_key == 'HitRecord'

# Generated at 2022-06-14 16:28:13.768578
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert not ie.suitable('https://hitrecord.org/')

# Generated at 2022-06-14 16:28:14.378390
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:15.279458
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:16.545132
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    m = HitRecordIE()
    assert (m.name != None)


# Generated at 2022-06-14 16:28:27.605999
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie.VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:28:29.394411
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('HitRecordIE', 'user/channel', 'https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:28:34.023711
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print("\n Testing HitRecordIE.__init__()")
    h = HitRecordIE()
    print("\n Testing HitRecordIE.valid_url()")
    print(h.valid_url())
    print("\n Testing HitRecordIE.real_extract()")
    print(h.real_extract())



# Generated at 2022-06-14 16:30:17.184607
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == HitRecordIE._TEST['url']
    assert HitRecordIE._md5 == HitRecordIE._TEST['md5']
    assert HitRecordIE._info_dict == HitRecordIE._TEST['info_dict']

# Generated at 2022-06-14 16:30:18.052548
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:30:19.673790
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hit = HitRecordIE()
    assert(hit.password == None)


# Generated at 2022-06-14 16:30:27.225811
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()
    assert isinstance(obj, InfoExtractor)
    assert obj._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:38.257651
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_dict = {
        'id': '2954362',
        'ext': 'mp4',
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
    ie = HitRecordIE()

# Generated at 2022-06-14 16:30:38.806655
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:30:40.655338
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    return
#    ie = HitRecordIE()
#    assert ie.__class__ == HitRecordIE

# Generated at 2022-06-14 16:30:41.550512
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE('id') != None

# Generated at 2022-06-14 16:30:44.147333
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    from .constructors import Constructor
    ie = Constructor.from_supported_ie_key("HitRecordIE")
    assert ie != None


# Generated at 2022-06-14 16:30:45.379773
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    init_HitRecordIE = HitRecordIE()
    assert init_HitRecordIE is not None