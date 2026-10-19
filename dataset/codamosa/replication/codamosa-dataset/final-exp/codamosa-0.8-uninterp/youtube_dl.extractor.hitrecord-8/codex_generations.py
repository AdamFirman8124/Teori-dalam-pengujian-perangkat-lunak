

# Generated at 2022-06-14 16:24:07.841178
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_class = HitRecordIE()
    assert test_class._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert test_class._TEST['url'] == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:24:09.122763
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("url")

# Generated at 2022-06-14 16:24:16.497125
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Testing constructor of HitRecordIE
    HitRecordIE_object = HitRecordIE()

    assert HitRecordIE_object._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE_object.IE_NAME == 'hitrecord'
    assert HitRecordIE_object.IE_DESC == 'HitRecord'
    assert HitRecordIE_object.EXTRACTOR_KEY == 'hitrecord'

# Generated at 2022-06-14 16:24:17.666722
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE


# Generated at 2022-06-14 16:24:29.261116
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    infoExtractor = HitRecordIE()
    assert infoExtractor.IE_NAME == 'hitrecord'
    assert infoExtractor.IE_DESC == 'HitRecord.org'
    assert isinstance(infoExtractor._VALID_URL, type(''))
    assert infoExtractor._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert infoExtractor._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert infoExtractor._TEST['info_dict']['id'] == '2954362'
    assert infoExtractor._TEST['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 16:24:29.864989
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:24:31.814181
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	try:
		HitRecordIE()
	except Exception as e:
		print(e)
		raise Exception("Construction of class HitRecordIE failed.")

# Generated at 2022-06-14 16:24:33.512196
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    infoExtractor = HitRecordIE.HitRecordIE()
    assert infoExtractor is not None

# Generated at 2022-06-14 16:24:36.373941
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable(ie.ie_key())
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert not ie.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')

# Generated at 2022-06-14 16:24:39.331173
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:49.052460
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:24:57.813461
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print("test_HitRecordIE")
    obj = HitRecordIE()
    assert(obj._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

# Generated at 2022-06-14 16:24:59.323695
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:25:00.367707
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()
    except Exception as e:
        print("test_HitRecordIE failed: " + str(e))


# Generated at 2022-06-14 16:25:12.425788
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()
    assert HitRecordIE()._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE()._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert HitRecordIE()._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert HitRecordIE()._TEST['info_dict']['id'] == '2954362'
    assert HitRecordIE()._TEST['info_dict']['ext'] == 'mp4'
    assert HitRecordIE()._TEST['info_dict']['title'] == 'A Very Different World (HITRECORD x ACLU)'
    assert HitRecordIE

# Generated at 2022-06-14 16:25:13.975434
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:25:17.890587
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:18.936677
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    return HitRecordIE()

# Generated at 2022-06-14 16:25:23.558731
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('hitrecord')
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:25.784911
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert type(ie) == HitRecordIE
#Test case for test_HitRecordIE
#test_HitRecordIE()

# Generated at 2022-06-14 16:25:44.772591
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE != None

# Generated at 2022-06-14 16:25:46.194095
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE.__name__ == "HitRecordIE"


# Generated at 2022-06-14 16:25:46.798996
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	pass

# Generated at 2022-06-14 16:25:54.444411
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE('','')
    except:
        import sys
        import traceback
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # On success, report no errors
        print(exc_type, fname, exc_tb.tb_lineno)
        print(traceback.format_exc())
    else:
        print('No exceptions!')

# Generated at 2022-06-14 16:26:03.396735
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie._match_id(
        'https://hitrecord.org/records/2954362') == '2954362'
    assert ie._match_id(
        'https://hitrecord.org/records/2954362/video') == '2954362'
    assert ie._match_id(
        'https://hitrecord.org/records/2954362/video/') == '2954362'
    assert ie._match_id(
        'https://hitrecord.org/records/2954362/video/some-other-text') == '2954362'

# Generated at 2022-06-14 16:26:08.972762
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(None)._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE(None)._TEST['url'] == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:26:09.900370
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(None, None)

# Generated at 2022-06-14 16:26:11.740153
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert (HitRecordIE()._VALID_URL ==
            HitRecordIE._VALID_URL)

# Generated at 2022-06-14 16:26:12.461944
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    inst = HitRecordIE()
    inst.info()

# Generated at 2022-06-14 16:26:13.719825
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    HitRecordIE.__init__()
    """
    HitRecordIE()

# Generated at 2022-06-14 16:26:39.337096
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)"

# Generated at 2022-06-14 16:26:39.916701
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:42.623805
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:45.408399
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hri = HitRecordIE()
    print(hri.extract('https://hitrecord.org/records/2954362'))

# Generated at 2022-06-14 16:26:46.703638
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()


# Generated at 2022-06-14 16:26:47.476948
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE

# Generated at 2022-06-14 16:26:49.122855
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # create an instance of HitRecordIE
    HitRecordIE()

# Generated at 2022-06-14 16:26:50.298593
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    _ = HitRecordIE()

# Generated at 2022-06-14 16:26:55.683785
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'

# Generated at 2022-06-14 16:26:56.591328
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	assert HitRecordIE("")

# Generated at 2022-06-14 16:27:43.469975
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_instance = HitRecordIE()

# Generated at 2022-06-14 16:27:46.525306
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == HitRecordIE._VALID_URL
    assert ie._TEST == HitRecordIE._TEST

# Generated at 2022-06-14 16:27:48.046409
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:27:49.557485
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()
        assert True
    except:
        assert False

# Generated at 2022-06-14 16:27:51.965184
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'HitRecord'
    assert ie.extractor == HitRecordIE
    assert ie._VALID_URL == ie._VALID_URL

# Generated at 2022-06-14 16:27:53.785344
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.download_webpage('https://hitrecord.org/records/2954362')



# Generated at 2022-06-14 16:27:54.264593
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE

# Generated at 2022-06-14 16:27:59.740089
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hit_record_ie = HitRecordIE()

    assert(hit_record_ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)' )

# Generated at 2022-06-14 16:28:05.443884
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.url = 'https://hitrecord.org/records/2954362'
    ie.video_id = '2954362'
    assert ie.url == 'https://hitrecord.org/records/2954362'
    assert ie.video_id == '2954362'

# Generated at 2022-06-14 16:28:07.759217
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'hitrecord'


# Generated at 2022-06-14 16:29:51.684820
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    constructor = HitRecordIE([], {}, {})
    # Method _real_extract() inherited from the parent class
    assert constructor._real_extract is not None

# Generated at 2022-06-14 16:29:54.361045
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()(
            'https://hitrecord.org/records/2954362')
    except Exception as e:
        print(e)
        raise AssertionError('HitRecordIE: Failed to create instance')


# Generated at 2022-06-14 16:29:57.827617
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test HitRecordIE for Youtube.
    hitRecord = HitRecordIE();

    # Test HitRecordIE for Instagram.
    hitRecord = HitRecordIE();

# Generated at 2022-06-14 16:29:58.845211
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(InfoExtractor)

# Generated at 2022-06-14 16:30:04.438795
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie.get_url().startswith('http:') == True
    assert ie.get_url().endswith('/2954362') == True
    assert ie.get_url() == 'http://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:30:05.718442
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(_VALID_URL)
    


# Generated at 2022-06-14 16:30:06.402827
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("Url")

# Generated at 2022-06-14 16:30:08.368471
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert isinstance(ie, InfoExtractor)
    

# Generated at 2022-06-14 16:30:10.413217
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:30:13.204971
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TEST')
