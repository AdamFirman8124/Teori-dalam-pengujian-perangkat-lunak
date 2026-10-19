

# Generated at 2022-06-14 16:24:08.236123
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE()
    assert(instance._VALID_URL ==  r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

# Generated at 2022-06-14 16:24:09.946550
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordTest = HitRecordIE()
    assert hitRecordTest.SUCCEEDED == 1

# Generated at 2022-06-14 16:24:13.616253
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert not ie.suitable('https://hitrecord.org/records')

# Generated at 2022-06-14 16:24:15.686013
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit test for HitRecordIE constructor
    """
    HitRecordIE("HitRecord", 'hitrecord.org')

# Generated at 2022-06-14 16:24:27.069642
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    params = {
        'info_dict':
        {
            'id': '3456',
            'ext': 'mp4',
            'title': 'My HitRecord Video',
            'description': 'This is my HITRECORD video',
            'duration': '120',
            'timestamp': '123456',
            'upload_date': '20160802',
            'uploader': 'SomeGuy',
            'uploader_id': '234567',
            'view_count': '1000',
            'like_count': '100',
            'comment_count': '10',
            'tags':
            [
                'cat',
                'dog'
            ]
        }
    }
    ie.extract(params)

# Generated at 2022-06-14 16:24:27.826312
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:30.258144
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")


if __name__ == "__main__":
    test_HitRecordIE()

# Generated at 2022-06-14 16:24:33.414259
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE.ie_key())._VALID_URL == HitRecordIE._VALID_URL
    HitRecordIE(HitRecordIE.ie_key())

# Generated at 2022-06-14 16:24:38.822018
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE.IE_NAME, HitRecordIE._VALID_URL)._VALID_URL == HitRecordIE._VALID_URL
    assert HitRecordIE(HitRecordIE.IE_NAME, HitRecordIE._VALID_URL).IE_NAME == HitRecordIE.IE_NAME

# Generated at 2022-06-14 16:24:40.165663
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == HitRecordIE._VALID_URL

# Generated at 2022-06-14 16:24:50.137668
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	_test_HitRecordIE = HitRecordIE(None,)

# Generated at 2022-06-14 16:24:54.099242
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == HitRecordIE._VALID_URL
    assert ie._TEST == HitRecordIE._TEST 
    assert ie._download_json == HitRecordIE._download_json
    assert ie._match_id == HitRecordIE._match_id

# Generated at 2022-06-14 16:24:55.554949
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.SUFFIX == 'org'

# Generated at 2022-06-14 16:24:56.523774
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:58.492306
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Execute constructor of the class
    HitRecordIE()
    # No errors raised



# Generated at 2022-06-14 16:25:10.789884
# Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:25:11.339739
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:12.983453
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_obj = HitRecordIE('HitRecordIE', 'hitrecord.org')
    assert test_obj

# Generated at 2022-06-14 16:25:14.157315
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert str(ie) == '<HitRecordIE>'

# Generated at 2022-06-14 16:25:16.107675
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(InfoExtractor, HitRecordIE.suitable, HitRecordIE.__name__)

# Generated at 2022-06-14 16:25:34.220047
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    global HitRecordIE
    hit_recordie = HitRecordIE()

    assert(True)

# Generated at 2022-06-14 16:25:39.239118
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	hit = HitRecordIE(HitRecordIE.ie_key())
	assert isinstance(hit, HitRecordIE)
	assert hit.IE_NAME == HitRecordIE.ie_key()
	assert hit._VALID_URL == HitRecordIE._VALID_URL
	assert hit._TEST == HitRecordIE._TEST

# Generated at 2022-06-14 16:25:43.128597
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE('https://hitrecord.org/records/2954362')
    assert instance.url_result == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:25:44.823216
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	'''Test case for HitRecordIE constructor'''

	HitRecordIE(None)

# Generated at 2022-06-14 16:25:46.604152
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()


# Create an instance of the HitRecordIE class
HitRecordIE()

# Generated at 2022-06-14 16:25:47.723509
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


# Generated at 2022-06-14 16:25:52.368980
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Create object of class HitRecordIE
    ie = HitRecordIE("https://hitrecord.org/records/2954362")
    # Check that the function _real_extract is called
    ie._real_extract("https://hitrecord.org/records/2954362")

if __name__ == '__main__':
    test_HitRecordIE()

# Generated at 2022-06-14 16:25:55.729343
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecord = HitRecordIE()
    assert hitRecord.ie_key() == 'hitrecord:record'
    assert hitRecord.ie_name() == 'HitRecord'


# Generated at 2022-06-14 16:25:56.381998
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE

# Generated at 2022-06-14 16:25:58.109734
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert(ie.__class__.__name__ == "HitRecordIE")

# Generated at 2022-06-14 16:26:35.656230
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    #Constructor test
    HitRecordIE(None)

# Generated at 2022-06-14 16:26:37.872051
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    my_info = HitRecordIE()
    instance = HitRecordIE()
    assert(my_info.ie_key() == 'hitrecord')

# Generated at 2022-06-14 16:26:48.580685
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    global HitRecordIE
    import requests
    import re
    url = "https://hitrecord.org/records/2954362"
    info = HitRecordIE._real_extract(HitRecordIE(), url)
    print("Title: " + info["title"])
    print("URL: " + info["url"])
    print("Id: " + info["id"])
    print("Description: " + info["description"])
    print("Uploader: " + info["uploader"])
    print("View count: " + compat_str(info["view_count"]))
    print("Like count: " + compat_str(info["like_count"]))
    print("Comment count: " + compat_str(info["comment_count"]))

# Generated at 2022-06-14 16:26:50.206558
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    assert type(hitrecord) == HitRecordIE

# Generated at 2022-06-14 16:26:51.999285
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()


if __name__ == '__main__':
    unittest.main()

# Generated at 2022-06-14 16:26:52.635052
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:55.393911
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hre = HitRecordIE(HitRecordIE._VALID_URL)
    assert hre._match_id(HitRecordIE._VALID_URL) == HitRecordIE._TEST['info_dict']['id']

# Generated at 2022-06-14 16:26:57.880089
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL is not None 
    assert HitRecordIE._TEST is not None
    test_HitRecordIE._real_extract is not None


# Generated at 2022-06-14 16:26:58.457019
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:00.495926
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(HitRecordIE._VALID_URL, HitRecordIE._TEST)
    ie.download(HitRecordIE._TEST)

# Generated at 2022-06-14 16:28:42.038621
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:28:43.617254
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test case of HitRecordIE
    HitRecordIE('http://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:28:47.574118
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'HitRecord'
    assert ie.IE_NAME == 'HitRecord'
    assert ie.SUCCEEDED == 0
    assert ie.FAILED == 1

# Generated at 2022-06-14 16:28:56.380727
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:28:57.482764
# Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:28:58.861172
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:28:59.884402
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    _HitRecordIE = HitRecordIE()

# Generated at 2022-06-14 16:29:04.925829
# Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:29:07.153526
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('HitRecordIE', 'http://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:29:08.794753
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert(HitRecordIE._VALID_URL == HitRecordIE(None)._VALID_URL)


# Generated at 2022-06-14 16:32:37.223004
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    
    ie = HitRecordIE()
    ie.extract('some url')

# Generated at 2022-06-14 16:32:47.951155
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitRecordIE = HitRecordIE()
    assert hitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:32:51.452484
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ''' Unit Test to check if the constructor of HitRecordIE class works fine '''
    instance = HitRecordIE('https://hitrecord.org/records/2954362')
    assert instance.name == 'hitrecord'
    assert instance.ie_key() == 'hitrecord:record'
    assert instance.valid_url.match('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:32:53.613208
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE(HitRecordIE._VALID_URL, HitRecordIE._TEST)
    except:
        return False
    return True

# Generated at 2022-06-14 16:32:54.668567
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:33:05.398689
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:33:05.893634
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:33:09.983038
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert HitRecordIE._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'


# Generated at 2022-06-14 16:33:10.836362
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('HitRecordIE', 'HitRecord', True)

# Generated at 2022-06-14 16:33:13.093660
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    t1 = HitRecordIE('','')
