

# Generated at 2022-06-14 16:24:04.175727
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecordIE = HitRecordIE()
    # Test result
    assert (hitrecordIE.IE_NAME == "hitrecord")
    assert (hitrecordIE.IE_DESC == "HitRecord")
    assert (hitrecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

# Generated at 2022-06-14 16:24:04.702767
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:17.400777
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("http://hitrecord.org/records/2827517")
    assert ie._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)"

# Generated at 2022-06-14 16:24:18.584334
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie is not None

from .youtube import YoutubeIE

# Generated at 2022-06-14 16:24:30.079092
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:34.204069
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    i = HitRecordIE()
    assert i._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:24:36.486925
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('http://hitrecord.org/records/')
    assert ie is not None
    ie = HitRecordIE('https://hitrecord.org/records/')
    assert ie is not None
    ie = HitRecordIE('https://hitrecord.org/records/123')
    assert ie is not None
    assert type(ie) == HitRecordIE


# Generated at 2022-06-14 16:24:37.070782
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:42.178608
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert not ie.suitable('https://hitrecord.org/records')
    assert not ie.suitable('https://hitrecord.org/')
    assert ie.IE_NAME == 'HitRecord'



# Generated at 2022-06-14 16:24:47.966983
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_url = "https://hitrecord.org/records/2954362"
    test_object = HitRecordIE()
    assert test_object._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)"
    assert test_object._TEST["url"] == "https://hitrecord.org/records/2954362"

# Generated at 2022-06-14 16:24:58.620970
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print(HitRecordIE._TEST)

# Generated at 2022-06-14 16:24:59.657198
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


# Generated at 2022-06-14 16:25:04.155915
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE.suitable('https://hitrecord.org/records/2954362')
    assert HitRecordIE.suitable('https://hitrecord.org') == False


# Generated at 2022-06-14 16:25:10.880751
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362') == True
    assert ie.suitable('https://hitrecord.org/records/2954362') == True
    assert ie.suitable('https://hitrecord.org') == False
    assert ie.suitable('https://hitrecord.org/') == False
    assert ie.suitable('https://hitrecord.org/records/') == False

# Generated at 2022-06-14 16:25:21.831723
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:27.298822
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.suitable('http://hitrecord.org/records/2954362')
    assert ie.IE_NAME == 'hitrecord'
    assert ie.VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'



# Generated at 2022-06-14 16:25:36.697755
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    sample_url = 'https://hitrecord.org/records/2954362'
    sample_id = '2954362'

    assert HitRecordIE._VALID_URL == sample_url

    info_extractor = HitRecordIE()
    assert info_extractor._match_id(sample_url) == sample_id

    # Unit test for method _real_extract:
    # Check if metadata is properly extracted from the web page
    info = info_extractor._real_extract(sample_url)
    assert info['id'] == sample_id
    assert info['url'] == 'https://live.hitrecord.org/videos/5lkmq3jkjfhg.mp4'
    assert info['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:25:39.907620
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecordClass = HitRecordIE('https://hitrecord.org/records/2954362');
    hitrecordClass._real_extract('https://hitrecord.org/records/2954362');

# Generated at 2022-06-14 16:25:41.095896
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:47.770059
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    item_hitrecord = HitRecordIE()
    test_url_hitrecord = 'https://hitrecord.org/records/2954362'
    test_url_hitrecord_wrong = 'https://hitrecord.org/records/2222222'

    assert item_hitrecord._TEST['url'] == test_url_hitrecord
    assert item_hitrecord._TEST['url'] != test_url_hitrecord_wrong


# Generated at 2022-06-14 16:26:17.700841
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    struct = HitRecordIE()
    assert struct.__class__ == HitRecordIE
    assert struct._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:18.203255
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:26:28.695446
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	video_id = 2954362
	title = "A Very Different World (HITRECORD x ACLU)"
	video_url = "https://s3.amazonaws.com/hitrecordstatic/recordings/mp4/57b9f5e95f264e33b66a5c55.mp4"

# Generated at 2022-06-14 16:26:32.398908
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:26:34.686799
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """Test that constructor of HitRecordIE works properly"""
    HitRecordIE._test_developer_mode_result(HitRecordIE._TEST)


# Generated at 2022-06-14 16:26:35.252574
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:37.935761
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    h = HitRecordIE()
    assert h.name == 'hitrecord'
    assert h._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:26:39.351972
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit test for class HitRecordIE
    """
    pass

# Generated at 2022-06-14 16:26:41.452335
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('')
    assert isinstance(ie, HitRecordIE)
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:26:42.623469
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()



# Generated at 2022-06-14 16:27:26.393953
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info = HitRecordIE().extract('https://hitrecord.org/records/2954362')
    assert info['id'] == '2954362'

# Generated at 2022-06-14 16:27:32.966715
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE()
    assert instance._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:43.281909
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordIE = HitRecordIE()
    print("Test constructor of class HitRecordIE")
    assert hitRecordIE._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert hitRecordIE._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert hitRecordIE._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert hitRecordIE._TEST['info_dict']['id'] == '2954362'
    assert hitRecordIE._TEST['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 16:27:48.457569
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    class HIT_RECORD_IE(InfoExtractor):
        IE_NAME = 'hitrecord'
        _VALID_URL = HitRecordIE._VALID_URL
        _TEST = HitRecordIE._TEST

    HIT_RECORD_IE = HIT_RECORD_IE()
    HIT_RECORD_IE._real_extract(HitRecordIE._TEST['url'])

# Generated at 2022-06-14 16:27:49.919537
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hit_record_ie = HitRecordIE()


# Generated at 2022-06-14 16:27:53.639182
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._TEST.get("url") == 'https://hitrecord.org/records/2954362'
    assert HitRecordIE._TEST.get("md5") == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert HitRecordIE._TEST.get("info_dict")

# Generated at 2022-06-14 16:27:54.418796
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord_ie = HitRecordIE(None)
    assert hitrecord_ie

# Generated at 2022-06-14 16:27:55.774885
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert isinstance(HitRecordIE, InfoExtractor)
#

# Generated at 2022-06-14 16:27:56.762528
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:02.694355
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(HitRecordIE._VALID_URL)
    assert ie.url == HitRecordIE._VALID_URL
    assert ie.video_id == HitRecordIE._TEST['info_dict']['id']
    assert ie.video_url == HitRecordIE._TEST['url']
    assert ie.title == HitRecordIE._TEST['info_dict']['title']

# Generated at 2022-06-14 16:29:47.935374
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(HitRecordIE._VALID_URL, HitRecordIE._TEST)

    assert ie.name == 'HitRecord.org'

# Generated at 2022-06-14 16:29:54.835308
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.name == 'HitRecord'
    assert ie.description == 'md5:bbac34f3ca81a3e3b2c10a36e13578e7'
    assert ie.valid_url('https://hitrecord.org/records/2954362')
    assert ie.valid_url('https://www.hitrecord.org/records/2954362')
    assert not ie.valid_url('https://www.hitrecord.org/')

# Generated at 2022-06-14 16:29:56.865558
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # test instance of class HitRecordIE
    HitRecordIE()


# Generated at 2022-06-14 16:29:58.457851
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    print("Method - test_HitRecordIE")

    # Create HitRecordIE object
    HitRecordIE()


# Generated at 2022-06-14 16:30:06.725950
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('http://hitrecord.org/records/2954362', {})
    assert ie._VALID_URL ==  r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:07.824827
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    # TODO: implement

# Generated at 2022-06-14 16:30:09.378638
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = 'https://hitrecord.org/records/2954362'
    HitRecordIE(url)

# Generated at 2022-06-14 16:30:10.743538
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE()
    assert instance._downloader

# Generated at 2022-06-14 16:30:11.881109
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(InfoExtractor)

# Generated at 2022-06-14 16:30:16.461332
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.url_result('https://hitrecord.org/records/2954362').result == '2954362'
    assert ie._match_id(ie.valid_url('https://hitrecord.org/records/2954362')) == '2954362'