

# Generated at 2022-06-14 16:24:01.173035
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()._real_extract("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:24:02.992666
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    print(ie.extract())
    assert ie.extract()

# Generated at 2022-06-14 16:24:04.183367
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    inst = HitRecordIE()
    assert inst._VALID_URL == _VALID_URL

# Generated at 2022-06-14 16:24:11.098472
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE
    data = ie._TEST
    expect_id = data['info_dict']['id']
    expect_url = data['url']
    expect_result = data['info_dict']

    result = ie._real_extract(expect_url)
    assert result['id'] == expect_id
    for key in expect_result:
        assert result[key] == expect_result[key]

# Generated at 2022-06-14 16:24:22.745639
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'hitrecord'
    assert ie.IE_NAME == 'hitrecord'
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:25.304807
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:25.688176
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:26.349960
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:27.904938
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == HitRecordIE._TEST.get("url")

# Generated at 2022-06-14 16:24:30.658265
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = HitRecordIE()._VALID_URL
    print(url)
    match = HitRecordIE._VALID_URL_RE.match(url)
    id = match.group("id")

# Generated at 2022-06-14 16:24:40.585668
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:41.263769
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:42.193198
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_HitRecordIE = HitRecordIE()

# Generated at 2022-06-14 16:24:45.248789
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(None, None)
    ie._real_initialize(None)
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:24:46.591714
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://www.hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:24:56.126220
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # tests for HitRecordIE
    IE_list={HitRecordIE}
    for IE in IE_list:
        print(IE)
        ie=IE()
        print(ie.suitable('https://hitrecord.org/records/2954362'))
        print(ie.suitable('https://hitrecord.org/records/2954362'))
    # tests for YoutubeIE
    from .youtube import YoutubeIE
    IE_list = {YoutubeIE}
    for IE in IE_list:
        print (IE)
        ie = IE()
        print(ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc'))
        print(ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc'))
    # tests for Daily

# Generated at 2022-06-14 16:24:59.283353
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:25:00.229941
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE()
    assert instance

# Generated at 2022-06-14 16:25:01.898973
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    record = HitRecordIE()

# Generated at 2022-06-14 16:25:06.088969
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


# Generated at 2022-06-14 16:25:25.876672
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert isinstance(HitRecordIE('https://hitrecord.org/records/2954362'), InfoExtractor)

# Generated at 2022-06-14 16:25:30.866882
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """Simple unit test for class HitRecordIE"""
    class_instance = HitRecordIE()
    assert class_instance._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'


if __name__ == '__main__':
    test_HitRecordIE()

# Generated at 2022-06-14 16:25:37.467034
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test = HitRecordIE()
    assert test._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert test._TEST['id'] == '2954362'
    assert test._TEST['title'] == 'A Very Different World (HITRECORD x ACLU)'
    assert test._TEST['description'] == 'md5:e62defaffab5075a5277736bead95a3d'

# Generated at 2022-06-14 16:25:38.155341
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:25:40.270114
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("HitRecordIE","https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:25:43.866456
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ### Main case which will be used in whole program
    assert(HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

    ### Testing extract_id function
    # Case with number
    assert(HitRecordIE._match_id("https://hitrecord.org/records/2954362") == "2954362")
    # Case with string
    assert(HitRecordIE._match_id("https://hitrecord.org/records/dsfsdgdsf") == "dsfsdgdsf")

# Generated at 2022-06-14 16:25:46.239865
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(None)
    url = 'https://hitrecord.org/records/2954362'
    assert ie.suitable(url)

# Generated at 2022-06-14 16:25:48.082801
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


if __name__ == '__main__':
    test_HitRecordIE()

# Generated at 2022-06-14 16:25:49.290665
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hit_record = HitRecordIE()
    print(hit_record)


# Generated at 2022-06-14 16:25:52.357214
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE(None, 'https://hitrecord.org/records/2954362')
    except Exception as e:
        print('test_HitRecordIE FAILED: ', e)
        return -1
    else:
        return 0

if __name__ == "__main__":
    test_HitRecordIE()

# Generated at 2022-06-14 16:26:33.912070
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE({})
    assert ie.NAME == 'hitrecord'
    assert ie.IE_NAME == 'hitrecord'
    assert ie.VALID_URL is not None
    assert ie.TEST is not None

# Generated at 2022-06-14 16:26:35.680583
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:44.644384
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hit_record_url = HitRecordIE._VALID_URL

    # test invalid urls
    HitRecordIE._VALID_URL = 'http://hitrecord.org/records/tacos'
    assert HitRecordIE().suitable('http://hitrecord.org/records/tacos') == False
    HitRecordIE._VALID_URL = 'http://hitrecord.org/records/'
    assert HitRecordIE().suitable('http://hitrecord.org/records/tacos') == False
    HitRecordIE._VALID_URL = hit_record_url
    assert HitRecordIE().suitable('http://hitrecord.org/records/tacos') == False

# Generated at 2022-06-14 16:26:45.901332
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE() is not None

# Generated at 2022-06-14 16:26:48.248738
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'HitRecord', ie.ie_key()

# Generated at 2022-06-14 16:26:51.151256
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.url = "https://hitrecord.org/records/2954362"
    ie.id = "2954362"

# Generated at 2022-06-14 16:26:54.698106
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test for constructing of instance HitRecordIE
    ie = HitRecordIE()

    # Test for returning url from _VALID_URL
    url = 'https://hitrecord.org/records/2954362'
    assert ie._match_id(url) == '2954362'

# Generated at 2022-06-14 16:26:56.333785
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    print(ie._VALID_URL)
    print(ie._TEST)

# Generated at 2022-06-14 16:27:03.988764
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert ie._TEST['info_dict']['id'] == '2954362'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
    assert ie._TEST['info_dict']['title'] == 'A Very Different World (HITRECORD x ACLU)'

# Generated at 2022-06-14 16:27:09.904518
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    unit = HitRecordIE()
    expected_url = 'https://hitrecord.org/records/2954362'
    expected_video_id = '2954362'
    url, video_id = unit._real_extract('https://hitrecord.org/records/2954362')
    assert url == expected_url
    assert video_id == expected_video_id

# Generated at 2022-06-14 16:28:44.980833
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    InfoExtractor("HitRecordIE")

# Generated at 2022-06-14 16:28:49.839201
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord'
    assert ie.IE_DESC == 'HITRECORD'
    assert ie.VALID_URL == HitRecordIE._VALID_URL
    assert ie.__name__ == 'HitRecordIE'
    assert ie.test() == HitRecordIE._TEST

# Generated at 2022-06-14 16:28:57.907999
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:28:58.408887
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:29:01.676433
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE.__name__ == 'HitRecord'
    assert HitRecordIE.ie_key() == 'HitRecord'

# Generated at 2022-06-14 16:29:12.036190
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test = HitRecordIE('HitRecordIE', 'hitrecord.org', 0, 0)
    assert test.name == 'HitRecordIE'
    assert test.ie_key == 'hitrecord.org'
    assert test.max_downloads == 0
    assert test.age_limit == 0
    test_hitrecord_url = 'https://hitrecord.org/records/2954362'
    # This is a test for the constructor of HitRecordIE
    test_HitRecordIE_constructor = HitRecordIE(test_hitrecord_url,
        'HitRecordIE', 'hitrecord.org', 0, 0)
    assert test_HitRecordIE_constructor.url == test_hitrecord_url
    assert test_HitRecordIE_constructor.name == 'HitRecordIE'
    assert test_HitRecordIE_constructor.ie_

# Generated at 2022-06-14 16:29:16.101044
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("foo", True)
    assert (ie.__name__ == 'hitrecord')
    assert (ie.ie_key() == 'hitrecord')
    assert (ie.SUCCESS == True)
    assert (ie.json_urls == ['https://hitrecord.org/api/web/records/%s'])

# Generated at 2022-06-14 16:29:19.284023
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(None)

# Generated at 2022-06-14 16:29:21.089874
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(test) 
test_HitRecordIE()

# Generated at 2022-06-14 16:29:23.520007
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    e = HitRecordIE("")
    assert type(e) == HitRecordIE
    assert e._VALID_URL == HitRecordIE._VALID_URL



# Generated at 2022-06-14 16:33:15.603270
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:33:17.111517
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:33:18.730873
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	info_extractor = HitRecordIE()
	info_extractor.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:33:21.986086
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    obj = ie._match_id('https://hitrecord.org/records/123456789')
    assert obj == '123456789'

# Generated at 2022-06-14 16:33:24.898041
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie == HitRecordIE('HitRecord')

# Generated at 2022-06-14 16:33:26.265336
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:33:26.964376
# Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:33:27.423428
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    pass

# Generated at 2022-06-14 16:33:28.466375
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE()
    
test_HitRecordIE()

# Generated at 2022-06-14 16:33:28.944623
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()