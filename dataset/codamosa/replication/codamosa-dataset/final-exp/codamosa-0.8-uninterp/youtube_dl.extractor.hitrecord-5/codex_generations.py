

# Generated at 2022-06-14 16:24:00.186715
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('hitrecord.org')

# Generated at 2022-06-14 16:24:04.660446
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test 1 - Normal test case
    page_url = "https://hitrecord.org/records/2954362"
    he = HitRecordIE(page_url)
    he_id = he._match_id(page_url)
    url = he._real_extract(page_url)
    assert he_id == '2954362'
    assert url['id'] == he_id

# Generated at 2022-06-14 16:24:17.348916
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert (HitRecordIE()._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

# Generated at 2022-06-14 16:24:22.520730
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("https://hitrecord.org/records/2954362")
    assert ie._match_id("https://hitrecord.org/records/2954362") == "2954362"
    assert ie._match_id("https://hitrecord.org/records/2954362/") == "2954362"

# Generated at 2022-06-14 16:24:32.995302
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    url = 'https://hitrecord.org/records/2954362'
    if ie._VALID_URL != ie._TEST['url']:
        raise Exception('ERROR: _VALID_URL and _TEST["url"] are not matching')
    if ie._download_json(ie._TEST['url'], 1) != ie._TEST['info_dict']:
        raise Exception(
            'ERROR: _download_json and _TEST["info_dict"] are not matching')
    if ie._real_extract(url) != ie._TEST['info_dict']:
        raise Exception(
            'ERROR: _real_extract and _TEST["info_dict"] are not matching')
    ie._real_extract(url)

# Generated at 2022-06-14 16:24:35.917559
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.info_extractors['hitrecord'] is ie

# Generated at 2022-06-14 16:24:38.356873
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie._real_extract('https://hitrecord.org/records/2954362')
assert(True)

# Generated at 2022-06-14 16:24:43.111769
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
  url = 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:24:54.062735
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:55.037538
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test constructor
    HitRecordIE()

# Generated at 2022-06-14 16:25:11.743273
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    x = HitRecordIE()
    assert x._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:18.056326
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord'
    assert ie.IE_DESC == 'hitrecord'
    assert ie.VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:18.940846
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:31.125502
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:32.119494
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(None)._VALID_URL

# Generated at 2022-06-14 16:25:34.097242
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE.__name__ == 'HitRecordIE'
    assert HitRecordIE.__doc__ == InfoExtractor.__doc__

# Generated at 2022-06-14 16:25:46.559948
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()._real_extract('https://hitrecord.org/records/2954362')
    assert ie['id'] == '2954362'
    assert ie['url'] == 'https://media.hitrecord.org/media/videos/000/025/439/original/watch.mp4'
    assert ie['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:25:57.294087
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE("http://hitrecord.org/records/2954362")
    assert obj._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:58.194941
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:25:58.812918
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:07.603229
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie_hitrecord = HitRecordIE()
    assert ie_hitrecord.ie_key() == 'HitRecord'
    assert ie_hitrecord.ie_name() == 'HitRecord'


# Generated at 2022-06-14 16:26:09.364353
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Create an instance of HitRecordIE.
    HitRecordIE()


# Generated at 2022-06-14 16:26:10.291492
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:26:12.396720
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()._real_extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:12.969267
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:20.992394
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    extractor = HitRecordIE(None)
    assert isinstance(extractor, InfoExtractor)
    exp_title = r'A Very Different World \(HITRECORD x ACLU\)'
    exp_url = r'https://hitrecord.org/records/2954362'
    exp_id = r'2954362'
    exp_md5 = r'fe1cdc2023bce0bbb95c39c57426aa71'
    exp_desc = r'md5:e62defaffab5075a5277736bead95a3d'
    exp_duration = r'139.327'
    exp_timestamp = r'1471557582'
    exp_upload_date = r'20160818'
    exp_uploader = r'Zuzi.C12'
    exp_uploader

# Generated at 2022-06-14 16:26:24.204217
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Test case for the constructor of class HitRecordIE.
    """

    def test_constructor():
        """
        Test the constructor.
        """
        HitRecordIE()

# Generated at 2022-06-14 16:26:32.596249
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:33.704378
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


# Generated at 2022-06-14 16:26:34.467894
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


# Generated at 2022-06-14 16:26:45.013119
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:46.498335
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:26:49.534553
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # test the constructor of HitRecordIE
    ie = HitRecordIE('http://hitrecord.org/records/2954362')
    assert isinstance(ie, HitRecordIE)

# Generated at 2022-06-14 16:26:50.301672
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:52.411071
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(None)
    assert ie._VALID_URL.__class__ == type(re.compile(''))

# Generated at 2022-06-14 16:26:55.832056
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract("https://hitrecord.org/records/2954362")
    assert(ie.TEST['id'] == '2954362')

# Generated at 2022-06-14 16:26:56.720701
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE.test()

# Generated at 2022-06-14 16:26:57.921848
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    global HitRecordIE
    HitRecordIE

# Generated at 2022-06-14 16:27:00.155841
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE(): # This test case will fail, because the url is not valid any more.
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:27:10.080491
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert ie.suitable('https://www.hitrecord.org/records/2954362')
    assert not ie.suitable('https://hitrecord.org/foobar')
    assert not ie.suitable('https://www.hitrecord.org/foobar')
    assert ie._match_id('https://hitrecord.org/records/2954362') == '2954362'
    assert ie._match_id('https://www.hitrecord.org/records/2954362') == '2954362'

# Generated at 2022-06-14 16:27:38.063582
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:48.252160
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:49.064157
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    pass

# Generated at 2022-06-14 16:27:50.239426
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	try:
		HitRecordIE()
	except:
		assert(False)

# Generated at 2022-06-14 16:27:57.438174
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE({'info_dict':{'id':'1','url':'http://www.hitrecord.org/records/1'}})

# Generated at 2022-06-14 16:27:58.284076
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:00.799122
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Create object
    try:
        HitRecordIE()
        assert True
    except:
        assert False


# Unit tests for functions of class HitRecordIE

# Generated at 2022-06-14 16:28:12.165719
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordIE = HitRecordIE()
    assert hitRecordIE._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:28:15.620369
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'hitrecord'
    assert ie.ie_name() == 'HitRecord'
    assert isinstance(ie.SUTTITL, tuple)

# Generated at 2022-06-14 16:28:19.704333
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    '''
    Constructor of HitRecordIE was successful.
    '''
    ie = HitRecordIE(None)
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:29:19.143348
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:29:21.312459
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:29:32.634102
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('http://www.hitrecord.org/records/2954362')
    info = ie._real_extract('http://www.hitrecord.org/records/2954362')
    assert(info['id'] == '2954362')
    assert(info['url'] == 'https://videos.hitrecord.org/videos/482386/2954362.mp4')
    assert(info['title'] == 'A Very Different World (HITRECORD x ACLU)')

# Generated at 2022-06-14 16:29:35.625157
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:29:37.625243
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    videoIE = HitRecordIE()
    assert videoIE

# Generated at 2022-06-14 16:29:45.032979
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	# Input for constructor of class HitRecordIE
	url = HitRecordIE._VALID_URL = r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
	# Outputs of constructor of class HitRecordIE
	video_id = HitRecordIE._match_id(url)
	video = HitRecordIE._download_json(
		'https://hitrecord.org/api/web/records/%s' % video_id, video_id)
	# Inputs for function _real_extract
	video_id = video_id
	video = video
	# Output of function _real_extract
	HitRecordIE._real_extract(video)

# Generated at 2022-06-14 16:29:45.619811
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:29:56.451287
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == 'https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'

# Generated at 2022-06-14 16:29:57.874066
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ins = HitRecordIE()
    assert isinstance(ins, HitRecordIE)

# Generated at 2022-06-14 16:29:58.888452
# Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:31:44.925937
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

###############
# Unit Tests
# To run unit test, in project directory, run command:
# pytest test_hitrecord.py

# Generated at 2022-06-14 16:31:55.055045
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    from ..utils import ExtractorError

    # Test with invalid URL
    with pytest.raises(ExtractorError) as excinfo:
        HitRecordIE("www.xhamster.com")
        assert excinfo.type == 'ERROR'

    # Test with invalid URL
    with pytest.raises(ExtractorError) as excinfo:
        HitRecordIE("wrong_url_pattern")
        assert excinfo.type == 'ERROR'

    # Test with valid URL
    c = HitRecordIE("https://hitrecord.org/records/2954362")
    assert c._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:31:56.481994
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:32:05.819030
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit test for constructor of class HitRecordIE

    """
    # Constructor Unit Test
    HitRecordIE.__module__ = 'test'
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert isinstance(ie, InfoExtractor)
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

    # Test _match_id method of class HitRecordIE
    match = ie._match_id('https://hitrecord.org/records/2954362')
    assert match == '2954362'

    # Test _real_extract method of class HitRecordIE
    dict = ie._real_extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:32:14.541125
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecordie = HitRecordIE()
    assert hitrecordie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:32:17.128587
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(None)
    HitRecordIE._VALID_URL = 'test'
    assert ie._match_id('test') is not None
    assert ie._real_extract('test') is not None

# Generated at 2022-06-14 16:32:22.734628
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print(test_HitRecordIE.__name__)
    ie = HitRecordIE()
    # Constructor should raise an exception for non-existing video
    try:
        ie.extract(url='https://hitrecord.org/records/999999')
        assert False, 'Constructor did not raise an exception'
    except Exception as e:
        assert str(e) == 'No video found at https://hitrecord.org/records/999999', \
            'Constructor raised a wrong exception'

# Generated at 2022-06-14 16:32:25.583430
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    importer_test(HitRecordIE, [
        {
            'url': 'https://hitrecord.org/records/2954362',
            'only_matching': True,
        },
    ])

# Generated at 2022-06-14 16:32:26.377079
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:32:33.521300
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('test')
    assert ie
    assert ie.name == 'HitRecord'
    assert ie.ie_key() == 'hitrecord'