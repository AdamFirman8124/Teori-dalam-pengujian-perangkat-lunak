

# Generated at 2022-06-14 16:24:02.099140
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:24:08.912600
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_class = HitRecordIE()
    assert test_class._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:09.546874
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:13.781193
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    # Unit test for constructor of class HitRecordIE
    def test_init_HitRecordIE():
        IE_name = "HitRecordIE"
        hitRecord_info_extractor = HitRecordIE()
        assert hitRecord_info_extractor._VALID_URL == HitRecordIE._VALID_URL
        assert hitRecord_info_extractor._TEST == HitRecordIE._TEST
        assert hitRecord_info_extractor._is_valid_url("_VALID_URL") == HitRecordIE._is_valid_url("_VALID_URL")
        assert hitRecord_info_extractor.IE_NAME == IE_name
        assert hitRecord_info_extractor.js_to_json("_download_json") == HitRecordIE.js_to_json("_download_json")

    # Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:24:15.416121
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_HitRecordIE = HitRecordIE()
    print (test_HitRecordIE)

# Generated at 2022-06-14 16:24:17.022991
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord_ie = HitRecordIE()
    assert hitrecord_ie != null

# Generated at 2022-06-14 16:24:24.588183
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie_inst = HitRecordIE()

    # Test with: #1
    x = ie_inst.extract('https://hitrecord.org/records/2954362')
    assert x['id'] == '2954362'
    assert x['url'] == 'http://s3.amazonaws.com/node-thumbnails/3/6/2/8/1/1/362811/a-very-different-world--hitrecord-x-aclu--.mp4'
    assert x['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:24:29.399229
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    if __name__ == "__main__":
        test = HitRecordIE()
        test._downloader.params.update({'noplaylist': True})
        url = 'https://hitrecord.org/records/2823824'
        info_dict = test._real_extract(url)
        print(info_dict)

# Generated at 2022-06-14 16:24:30.702804
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ietester = HitRecordIE()
    assert ietester

# Generated at 2022-06-14 16:24:42.584910
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie.IE_NAME == 'hitrecord'

# Generated at 2022-06-14 16:24:53.508059
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """Test HitRecordIE constructor."""
    ie = HitRecordIE('hitrecord.org')  # pylint: disable=unused-variable

# Generated at 2022-06-14 16:24:55.037910
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord_ie = HitRecordIE()
    print(hitrecord_ie)

# Generated at 2022-06-14 16:24:56.091050
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    youtube_ie = HitRecordIE()

# Generated at 2022-06-14 16:24:57.465367
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Constructor for class HitRecordIE.
    """
    HitRecordIE()

# Generated at 2022-06-14 16:25:00.974716
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:25:03.895996
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE('http://www.hitrecord.org/records/2954362')
    assert hitrecord

# Generated at 2022-06-14 16:25:07.565739
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('')
    # This test is trivial
    expected = 'https://hitrecord.org/api/web/records/{0}'
    assert ie._make_api_url('1234') == expected.format('1234')

# Generated at 2022-06-14 16:25:10.837827
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Instantiate the Unit Test Class
    hitrecord_ie = HitRecordIE()
    url = 'https://hitrecord.org/records/2954362'
    hitrecord_ie.extract(url)

# Generated at 2022-06-14 16:25:21.734376
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert ie._TEST['info_dict']['id'] == '2954362'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
    assert ie._TEST['info_dict']['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:25:23.088506
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:45.183191
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	infoExtractor = HitRecordIE("https://hitrecord.org/records/2954362", "some_downloader")
	infoExtractor.check_options("some_options")
	infoExtractor.report_download_webpage("some_webpage")

# Generated at 2022-06-14 16:25:46.561195
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()
        assert True
    except Exception:
        assert False

# Generated at 2022-06-14 16:25:47.670701
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


# Generated at 2022-06-14 16:25:58.154461
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)"
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'

# Generated at 2022-06-14 16:25:59.104587
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:00.985132
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test that HitRecordIE constructor 
    # HitRecordIE()
    assert (HitRecordIE.__name__ == 'HitRecordIE')


# Generated at 2022-06-14 16:26:07.634346
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'HitRecord'
    assert ie.ie_name() == 'HitRecord'
    assert ie.valid_url("https://hitrecord.org/records/2954362", ie) == True
    assert ie.valid_url("https://hitrecord.org/records/2954362", ie) == True
    assert ie._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)"
    assert ie.valid_url("https://hitrecord.org/records/2954362/", ie) == True
    assert ie.valid_url("https://hitrecord.org/records/2954362/", ie) == True

# Generated at 2022-06-14 16:26:12.353157
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE()
    url = "https://hitrecord.org/records/2954362"
    result = instance._real_extract(url)
    assert result["id"] == "2954362"
    assert result["title"] == "A Very Different World (HITRECORD x ACLU)"

# Generated at 2022-06-14 16:26:20.605418
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test for proper URL for HitRecordIE class
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    # test for _TEST object
    test = HitRecordIE._TEST
    # test for url
    assert test['url'] == 'https://hitrecord.org/records/2954362'
    # test for md5
    assert test['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    # test for info dict
    info_dict = test['info_dict']
    assert info_dict['id'] == '2954362'
    assert info_dict['ext'] == 'mp4'

# Generated at 2022-06-14 16:26:26.469913
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    unit_test_url = 'https://hitrecord.org/records/2954362'

    ie = HitRecordIE(unit_test_url)

    assert ie._VALID_URL == HitRecordIE._VALID_URL
    assert ie.suitable(unit_test_url) is True
    assert ie.IE_DESC == 'hitrecord'
    assert ie.ie_key() == 'HitRecord'

# Generated at 2022-06-14 16:26:54.961123
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    extractor = HitRecordIE()
    assert extractor.IE_NAME == 'HitRecord'
    assert extractor._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert extractor._TEST.keys() == {'url', 'md5', 'info_dict'}
    assert extractor._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert extractor._TEST['info_dict'].keys() == {'id', 'ext', 'title', 'description', 'duration', 'timestamp', 'upload_date', 'uploader', 'uploader_id', 'view_count', 'like_count', 'comment_count', 'tags'}

# Generated at 2022-06-14 16:26:57.829186
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Arrangements
    url = "http://hitrecord.org/records/2954362"

    # Act
    hitrecord = HitRecordIE(url)

    # Assert
    assert hitrecord.url == url

# Generated at 2022-06-14 16:27:00.146916
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE().extract("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:27:03.986050
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)', 'HitRecordIE._VALID_URL is not valid'

# Generated at 2022-06-14 16:27:14.953764
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hit_record = HitRecordIE()
    assert hit_record._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:16.876562
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https://hitrecord.org/records/\d+'

# Generated at 2022-06-14 16:27:18.879620
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    return HitRecordIE()._real_extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:27:21.042684
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE()
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:27:24.790370
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:26.182756
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord_ie = HitRecordIE()
    assert(hitrecord_ie)

# Generated at 2022-06-14 16:28:12.910810
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(None)

# Generated at 2022-06-14 16:28:23.677675
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert ie._TEST['info_dict']['id'] == '2954362'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
    assert ie._TEST['info_dict']['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:28:24.264166
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:27.353336
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.url = 'https://hitrecord.org/records/2954362'
    ie.extract(ie.url)

# Generated at 2022-06-14 16:28:28.471317
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.name == 'HitRecord'
    assert ie.valid_url == HitRecordIE._VALID_URL
    assert ie.url_re == HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:28:29.224355
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:28:30.346125
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:31.565475
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:28:35.450214
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test with hitrecord video
    hitrecord = HitRecordIE()
    info = hitrecord._real_extract(
        'https://hitrecord.org/records/2954362')
    assert info['id'] == '2954362'
    assert info['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:28:36.588425
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:30:20.763167
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = 'https://hitrecord.org/records/2954362'

    obj = HitRecordIE()
    obj.match(url)

    assert (True)

# Generated at 2022-06-14 16:30:21.723004
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE();
    assert (ie.get_netrc_machine() == "hitrecord")
    assert (ie.get_netrc_password() == "hitrecord_password")

# Generated at 2022-06-14 16:30:26.449438
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.SUFFIX == 'm4a'
    assert not ie._LOGIN_REQUIRED
    # testing a video URL
    assert ie.IE_NAME == 'HitRecord'
    # testing a video URL
    assert ie.match_url('https://hitrecord.org/records/2954362')
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:37.579379
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	ie = HitRecordIE()
	assert ie._VALID_URL == "https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)"

# Generated at 2022-06-14 16:30:39.437785
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    constructor_test(HitRecordIE, [HitRecordIE._VALID_URL], [HitRecordIE._TEST])

# Generated at 2022-06-14 16:30:42.191164
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    a = HitRecordIE()
    assert_raises(AttributeError, getattr, a,'_VALID_URL')
    assert_raises(AttributeError, getattr, a,'_TEST')

# Generated at 2022-06-14 16:30:51.222644
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    cls = HitRecordIE
    assert cls._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:53.893510
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("http://hitrecord.org/records/2954362")
    assert ie is not None

# Generated at 2022-06-14 16:30:57.140116
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try: # if you don't have a valid url , it will fail
        HitRecordIE()._real_extract("https://hitrecord.org/records/2954362")
    except:
        assert False
    assert True



# Generated at 2022-06-14 16:30:59.256429
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == HitRecordIE._VALID_URL
    assert HitRecordIE()._TEST == HitRecordIE._TEST