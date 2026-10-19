

# Generated at 2022-06-14 16:24:01.254695
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert hasattr(ie, 'HitRecordIE')

# Generated at 2022-06-14 16:24:03.468470
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'HitRecord'
    assert ie.ie_name() == 'HitRecord'

# Generated at 2022-06-14 16:24:07.877857
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'

# Generated at 2022-06-14 16:24:13.036086
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie.get_class() == 'HitRecordIE'
    assert ie.get_url() == 'https://hitrecord.org/records/2954362'

# Test the get_url function

# Generated at 2022-06-14 16:24:13.771556
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:15.848473
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    line = 'https://hitrecord.org/records/2954362'
    HitRecordIE(line)

# Generated at 2022-06-14 16:24:27.762612
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:35.900648
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie.VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:37.811850
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.suitable('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:47.705223
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.url_result("https://hitrecord.org/records/2954362")
    assert ie.url_result("https://www.hitrecord.org/records/2954362")
    assert ie.url_result("http://www.hitrecord.org/records/2954362")
    assert ie.url_result("http://hitrecord.org/records/2954362")
    assert not ie.url_result("https://hitrecord.org/records/2954362/")
    assert not ie.url_result("https://hitrecord.org/records/2954362?")
    assert not ie.url_result("https://hitrecord.org/records/2954362/test")

# Generated at 2022-06-14 16:24:58.395697
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord'

# Generated at 2022-06-14 16:25:00.185655
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE.ie_key())._VALID_URL == HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:25:04.790556
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(2954362)
    assert ie.video_id == '2954362'
    assert ie.url == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:25:09.918954
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_url = 'https://hitrecord.org/records/2954362'

    # Instantiating an object of class HitRecordIE
    test_object = HitRecordIE()

    # Call the method to test the constructor of class HitRecordIE
    video_id = test_object._match_id(test_url)

    return video_id

# Generated at 2022-06-14 16:25:20.267159
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'

# Generated at 2022-06-14 16:25:24.281660
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    extraction_test = HitRecordIE().suitable('https://hitrecord.org/records/2954362')
    assert extraction_test and "This is a test unit for video_id"


# Generated at 2022-06-14 16:25:25.699456
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("http://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:25:34.349863
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('http://hitrecord.org/records/2954362')
    assert not ie.suitable('http://hitrecord.org/records/')
    assert not ie.suitable('http://hitrecord.org/records')
    assert not ie.suitable('http://hitrecord.org/')
    assert not ie.suitable('http://hitrecord.org')
    assert not ie.suitable('http://hitrecord.org/users/362811')
    assert not ie.suitable('http://hitrecord.org/users/')
    assert not ie.suitable('http://hitrecord.org/users')

# Generated at 2022-06-14 16:25:35.388152
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:25:37.023032
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	he = HitRecordIE()

# Generated at 2022-06-14 16:25:55.729180
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Unit test of url classifier

# Generated at 2022-06-14 16:25:57.204834
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:25:59.530570
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    extractor = HitRecordIE()
    assert extractor._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:01.065395
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:02.282608
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:04.775738
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    inst = HitRecordIE()
    assert inst.name == 'hitrecord'
    assert inst._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:05.468911
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:08.337329
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = 'https://hitrecord.org/records/2954362'
    ie = HitRecordIE()
    ie._real_extract(url)

# Generated at 2022-06-14 16:26:18.060746
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>[0-9]+)'

# Generated at 2022-06-14 16:26:20.605689
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    '''
    Test for constructor of class HitRecordIE
    '''
    # Test for get id with valid url
    assert HitRecordIE._match_id('https://hitrecord.org/records/2954362') == '2954362'


# Generated at 2022-06-14 16:26:57.281463
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()._extract_urls_from_webpage('', None, r'hitrecord.org/records/\d+')

# Generated at 2022-06-14 16:26:59.771930
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()
        print('HitRecordIE Test Passed')
    except:
        print('HitRecordIE Test Failed')

# Generated at 2022-06-14 16:27:00.814664
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	test = HitRecordIE()


# Generated at 2022-06-14 16:27:05.081294
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Only run this test if you are using PythonTestCase class.
    try:
        from .test_common import PythonTestCase
    except ImportError:
        return
    # Constructor successfully creates a HitRecordIE object
    assert HitRecordIE is not None

# Generated at 2022-06-14 16:27:06.451618
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie

# Generated at 2022-06-14 16:27:10.079381
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	ie = HitRecordIE()
	assert hasattr(ie, '_VALID_URL')
	assert hasattr(ie, '_TEST')
	assert hasattr(ie, '_real_extract')

# Generated at 2022-06-14 16:27:11.111583
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:27:14.510664
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    # URL for record with id 1
    url = 'http://hitrecord.org/records/1'
    record_id = ie._match_id(url)
    assert record_id == "1"

# Generated at 2022-06-14 16:27:15.369108
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('some_url')

# Generated at 2022-06-14 16:27:16.217105
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:28:06.898622
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	data = HitRecordIE('hitrecord','','','','','','','','','','','','','','','','','','','','','','','','','','','','')
	data.suitable('test')

# Generated at 2022-06-14 16:28:08.041092
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE is not None

# Generated at 2022-06-14 16:28:10.687579
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    i = HitRecordIE()
    assert i._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:28:11.608824
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE


# Generated at 2022-06-14 16:28:22.447938
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """

    Unit test case for this module
    """

# Generated at 2022-06-14 16:28:28.126251
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_dict = {
        'id': '2954362',
        'url': 'https://hitrecord.org/records/2954362',
        'test_name': 'YoutubeIE.test_HitRecordIE',
        'test_class': HitRecordIE,
        'test_module': 'youtube_dl.extractor.hitrecord',
        'object_type': 'URL'
    }
    return test_dict

# Generated at 2022-06-14 16:28:28.667089
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    pass

# Generated at 2022-06-14 16:28:29.440861
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:29.979473
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    h = HitRecordIE();
    print("Test HitRecordIE.py")

# Generated at 2022-06-14 16:28:38.059479
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:20.474010
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    from . import HitRecordIE
    assert HitRecordIE._VALID_URL == 'http://hitrecord.org/records/2954362'
    assert HitRecordIE._TEST['url'] == HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:30:21.043290
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	pass

# Generated at 2022-06-14 16:30:23.959486
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    unit_test = HitRecordIE()
    unit_test._VALID_URL = HitRecordIE._VALID_URL
    unit_test._TEST = HitRecordIE._TEST
    assert unit_test

# Generated at 2022-06-14 16:30:24.444200
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE

# Generated at 2022-06-14 16:30:25.940339
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    inst = HitRecordIE()
    assert isinstance(inst, HitRecordIE)

# Generated at 2022-06-14 16:30:30.289054
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.name == 'HitRecord'
    assert ie.url_re == 'https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'

# Generated at 2022-06-14 16:30:33.720275
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    video_id = '3326217'
    url = 'https://hitrecord.org/records/%s' % video_id
    HitRecordIE()._real_extract(url)


# Generated at 2022-06-14 16:30:34.881929
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()._real_extract(HitRecordIE._TEST['url'])

# Generated at 2022-06-14 16:30:36.735004
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_obj1 = HitRecordIE()
    assert isinstance(test_obj1, HitRecordIE)


# Generated at 2022-06-14 16:30:37.954238
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == HitRecordIE._VALID_URL