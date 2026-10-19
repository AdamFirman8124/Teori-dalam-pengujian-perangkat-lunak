

# Generated at 2022-06-14 16:24:00.362480
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_HitRecordIE = HitRecordIE()
    assert test_HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:01.263423
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie=HitRecordIE()
    return

# Generated at 2022-06-14 16:24:12.824616
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	from .common import InfoExtractor
	from ..compat import compat_str
	from ..utils import (
	    clean_html,
	    float_or_none,
	    int_or_none,
	    try_get,
	)


	class HitRecordIE(InfoExtractor):
	    _VALID_URL = r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:16.277958
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    This test is used to check that the constructor of HitRecordIE
    can be executed without throwing exceptions.
    """
    ied = HitRecordIE([])
    return type(ied) == HitRecordIE

# Generated at 2022-06-14 16:24:28.133786
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit tests for constructor of HitRecordIE class
    """
    instance = HitRecordIE()
    assert instance._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:29.122964
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert "HitRecordIE" in globals()

# Generated at 2022-06-14 16:24:33.032176
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    assert hitrecord._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)' \
                              r'|https?://(?:www\.)?hitrecord\.org/videos/(?P<id>\d+)'



# Generated at 2022-06-14 16:24:36.290971
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("https://hitrecord.org/records/2954362")
    assert type(ie) == HitRecordIE

# Generated at 2022-06-14 16:24:38.531466
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # test for valid url
    assert HitRecordIE._match_id('https://hitrecord.org/records/2954362')
    # test for invalid url
    assert HitRecordIE._match_id('http://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:48.132702
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:54.417037
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = ('https://hitrecord.org/records/2954362')
    HitRecordIE()

# Generated at 2022-06-14 16:25:06.628022
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Constructor test
    ie = HitRecordIE()
    # Test type of instance
    assert isinstance(ie, HitRecordIE)
    # Test type of attribute
    assert isinstance(ie._VALID_URL, str)
    # Test attribute
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:08.966272
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie._real_extract('https://hitrecord.org/records/2954362')


# Generated at 2022-06-14 16:25:11.609628
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    extractor = HitRecordIE()
    assert extractor.ie_key() == 'HitRecord'
    assert HitRecordIE._VALID_URL == extractor.valid_url

# Generated at 2022-06-14 16:25:15.237332
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    _HitRecordIE = HitRecordIE()
    assert _HitRecordIE.url_re.match('https://hitrecord.org/records/2954362')
    assert _HitRecordIE._match_id('https://hitrecord.org/records/2954362') == '2954362'
# End of Unit test



# Generated at 2022-06-14 16:25:16.196446
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:25:28.850356
# Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:25:30.456474
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:25:32.836477
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(InfoExtractor('https://hitrecord.org/records/2954362'))

# Generated at 2022-06-14 16:25:45.029773
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE('https://hitrecord.org/records/2954362')._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE('https://www.hitrecord.org/records/2954362')._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE('https://www.hitrecord.org/records/2954362')._TEST['url'] == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:26:02.715976
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    param = {
        'url': 'https://hitrecord.org/records/2954362'
    }
    obj = HitRecordIE()
    assert obj._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert obj._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert obj._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert obj._TEST['info_dict']['id'] == '2954362'
    assert obj._TEST['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 16:26:14.225585
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    class_instance = HitRecordIE()
    
    assert class_instance._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:17.049841
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.suitable('https://hitrecord.org/records/2954362')
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:18.821836
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == HitRecordIE._VALID_URL
    assert HitRecordIE()._TEST == HitRecordIE._TEST

# Generated at 2022-06-14 16:26:22.399248
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    downloaded_video = HitRecordIE().extract(HitRecordIE._TEST['url'])
    expected_video = HitRecordIE._TEST['info_dict']

    assert downloaded_video['id'] == expected_video['id']

# Generated at 2022-06-14 16:26:25.685116
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    url = 'https://hitrecord.org/records/2954362'
    # get the info without fail
    ie._real_extract(url)

# Generated at 2022-06-14 16:26:28.099601
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:26:33.809574
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('hitrecord', 'https://hitrecord.org/records/2954362')
    test_url = 'https://hitrecord.org/records/2954362'
    assert ie._match_id(test_url) == '2954362'
    assert ie._real_extract(test_url)

# Generated at 2022-06-14 16:26:36.444830
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Trivial test case to ensure that the HitRecordIE
    constructor works.
    """
    ie = InfoExtractor('hitrecord', True)
    assert ie.IE_NAME == 'hitrecord'

# Generated at 2022-06-14 16:26:37.352975
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	assert(HitRecordIE)


# Generated at 2022-06-14 16:26:50.671050
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    testHitRecordIE = HitRecordIE("https://hitrecord.org/records/2954362")
    assert testHitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:57.013329
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecordIE = HitRecordIE()
    unit_test_url = "https://hitrecord.org/records/2954362"
    assert hitrecordIE._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)"
    assert hitrecordIE._TEST["url"] == "https://hitrecord.org/records/2954362"
    assert hitrecordIE._TEST["md5"] == "fe1cdc2023bce0bbb95c39c57426aa71"

# Generated at 2022-06-14 16:26:57.872413
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:59.081095
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('HitRecord')  # noqa pylint: disable=W0613
    assert ie

# Generated at 2022-06-14 16:27:10.509861
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_url = HitRecordIE._TEST['url']
    video_id = HitRecordIE._TEST['info_dict']['id']

    search_class = 'hitrecord-search'
    search_id = 'hitrecord-search-form'

    test_object = HitRecordIE(test_url)
    print(vars(test_object))

    assert test_object._downloader == None
    assert test_object._match_id(test_url) == video_id
    assert test_object._search_regex(search_class, 20, search_class, search_id) == search_id

    assert test_object._real_extract(test_url) == HitRecordIE._TEST['info_dict']

# Generated at 2022-06-14 16:27:12.573882
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    
    assert ie == ie
    assert ie != 23
    assert ie != None

# Generated at 2022-06-14 16:27:14.225652
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:27:16.218214
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordIE = HitRecordIE();
    assert hitRecordIE is not None, "Failed to construct HitRecordIE."


# Generated at 2022-06-14 16:27:18.252997
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    match = ie.IE_NAME + ':' + ie._VALID_URL
    assert match == 'HitRecord:https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:27:20.037232
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()

# Generated at 2022-06-14 16:27:48.295801
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = 'https://hitrecord.org/records/2954362'
    exp_result = True
    result = HitRecordIE._is_valid_url(url)
    assert exp_result == result

# Generated at 2022-06-14 16:27:49.436334
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:50.280690
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE('www')

# Generated at 2022-06-14 16:27:53.380694
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test 1:
    # Tries to download a data file and extract the format of the video
    # file (not a video-file)
    i = HitRecordIE('https://hitrecord.org/records/2954362')
    i.extract()
    print(i.url)

# Generated at 2022-06-14 16:27:53.860709
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:55.958942
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert not ie.suitable('https://hitrecord.org/records/2954362/123')

# Generated at 2022-06-14 16:27:58.949528
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """Test HitRecordIE constructor"""
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie.url == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:27:59.562189
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:11.430041
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print('Testing HitRecordIE constructor')

    ie = HitRecordIE(None)
    assert ie.VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:28:20.706916
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord'
    assert ie.IE_VERSION == '0.0.1'
    assert ie.IE_DESC == 'Hitrecord is a collaborative production company founded by actor and director Joseph Gordon-Levitt.'
    assert ie.VALID_URL
    assert ie.DB == 'HitRecordDB'
    assert ie.LANG == 'en'

    assert ie.VALID_URL == HitRecordIE._VALID_URL
    assert ie.TEST == HitRecordIE._TEST
    assert ie.ABSTRACT == HitRecordIE._ABSTRACT
    assert ie.URL_PATTERN == HitRecordIE._URL_PATTERN



# Generated at 2022-06-14 16:29:11.197615
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE(): 
    print("\nTesting HitRecordIE()...")
    ie = HitRecordIE()
    print(ie)


'''
start = time.time()
test_HitRecordIE()
print('HitRecordIE().__init__() test completed in {:.2f} seconds\n'.format(time.time() - start))
'''

# Generated at 2022-06-14 16:29:12.035384
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE({})

# Generated at 2022-06-14 16:29:13.222426
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert isinstance(HitRecordIE, InfoExtractor)


# Generated at 2022-06-14 16:29:14.981569
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Constructor test
    """
    hit_record = HitRecordIE()
    assert hit_record

# Generated at 2022-06-14 16:29:17.645734
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    #assert HitRecordIE.ie_key() == 'HitRecord'

test_HitRecordIE()

# Generated at 2022-06-14 16:29:21.895921
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    vid_url = 'https://hitrecord.org/records/2954362'
    ie = HitRecordIE().ie_key()
    assert ie.suitable(vid_url) == True

# Generated at 2022-06-14 16:29:33.050187
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_url = 'https://hitrecord.org/records/2954362'
    downloader = HitRecordIE()
    videoInfo = downloader._real_extract(test_url)
    assert videoInfo.get('id') == '2954362'
    assert videoInfo.get('url') == 'https://hitrecord-res.cloudinary.com/video/upload/v1470890501/production/uploads/437083/source_file/source_file_mp4_2954362.mp4'
    assert videoInfo.get('title') == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:29:39.872213
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:29:43.368581
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE('HitRecordIE', 'http://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:29:44.695416
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:31:17.637334
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:31:19.233561
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test the constructor of class HitRecordIE
    HitRecordIE()

# Generated at 2022-06-14 16:31:19.946206
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_inst = HitRecordIE()

# Generated at 2022-06-14 16:31:24.774668
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test with a data that is not a URL
    # Should raise an exception
    with pytest.raises(ExtractorError):
        HitRecordIE(data=None)

    # Test with an empty URL
    # Should raise an exception
    with pytest.raises(ExtractorError):
        HitRecordIE(url='')

    # Test with an invalid URL
    # Should raise an exception
    with pytest.raises(ExtractorError):
        HitRecordIE(url='https://google.com')

# Generated at 2022-06-14 16:31:27.087143
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE("https://hitrecord.org/records/2954362").information("https://hitrecord.org/records/2954362")['title'] == "A Very Different World (HITRECORD x ACLU)", "HitRecordIE test failed"

# Generated at 2022-06-14 16:31:29.163582
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:31:30.503722
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(None)

# Generated at 2022-06-14 16:31:34.570103
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert ie.suitable('https://www.hitrecord.org/records/2954362')
    assert not ie.suitable('http://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:31:35.670001
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:31:38.817223
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('hitrecord', {})
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'