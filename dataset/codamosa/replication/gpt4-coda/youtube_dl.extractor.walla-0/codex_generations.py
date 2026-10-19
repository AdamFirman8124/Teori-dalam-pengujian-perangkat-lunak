

# Generated at 2024-03-18 09:28:35.625313
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()
    assert extractor.suitable(test_url), "WallaIE should recognize the URL"
    assert extractor._match_id(test_url) == '2642630', "WallaIE should extract the correct video ID"


# Generated at 2024-03-18 09:28:45.702264
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly by asserting the _VALID_URL attribute
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

    # Check if the _TEST dictionary is properly set
    test_url = ie._TEST['url']
    test_info_dict = ie._TEST['info_dict']
    assert test_url == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert test_info_dict['id'] == '2642630'
    assert test_info_dict['display_id'] == 'one-direction-all-for-one'
    assert test_info_dict['ext'] == 'flv'

# Generated at 2024-03-18 09:28:48.379254
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:28:51.749332
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:29:01.759322
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor and _VALID_URL
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)

    # Test case for WallaIE._real_extract method with a mock URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    info_dict = ie.extract(test_url)
    assert info_dict.get('id') == '2642630'
    assert info_dict.get('display_id') == 'one-direction-all-for-one'
    assert info_dict.get('ext') == 'flv'

# Generated at 2024-03-18 09:29:04.843212
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:29:08.177950
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:29:12.788620
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()
    assert extractor.suitable(test_url), "WallaIE should recognize the URL"
    assert extractor._match_id(test_url) == '2642630', "WallaIE should extract the correct video ID"


# Generated at 2024-03-18 09:29:19.872305
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    extractor = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(extractor, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(extractor._VALID_URL, test_url), "The URL should match the _VALID_URL pattern"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    match = re.match(extractor._VALID_URL, test_url)
    assert match.group('id') == '2642630', "The video ID should be extracted correctly"

# Generated at 2024-03-18 09:29:22.508626
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:29:42.432421
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(ie._VALID_URL, test_url), "The URL should match the _VALID_URL pattern"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    mobj = re.match(ie._VALID_URL, test_url)
    assert mobj.group('id') == '2642630', "The video ID should be extracted correctly"

# Generated at 2024-03-18 09:29:51.563864
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(ie._VALID_URL, test_url), "The URL should match the _VALID_URL pattern"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    mobj = re.match(ie._VALID_URL, test_url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert video_id == '2642630', "The extracted video ID should be '2642630'"

# Generated at 2024-03-18 09:29:57.399222
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor and _real_extract method
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()
    
    # Check if the instance is created
    assert isinstance(extractor, WallaIE), "WallaIE instance not created"
    
    # Check if the _VALID_URL pattern matches the test URL
    assert re.match(extractor._VALID_URL, test_url), "Test URL does not match _VALID_URL pattern"
    
    # Extract information
    info = extractor._real_extract(test_url)
    
    # Check if the extracted information matches the expected results

# Generated at 2024-03-18 09:30:01.381830
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:30:09.300836
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(ie._VALID_URL, test_url), "The URL should match the _VALID_URL pattern"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    mobj = re.match(ie._VALID_URL, test_url)
    assert mobj.group('id') == '2642630', "The video ID should be extracted correctly"

# Generated at 2024-03-18 09:30:18.590427
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor and _real_extract method
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()

    # Check if the instance is created
    assert isinstance(extractor, WallaIE), "WallaIE instance not created"

    # Check if the _VALID_URL pattern matches the test URL
    assert re.match(extractor._VALID_URL, test_url), "Test URL does not match _VALID_URL pattern"

    # Extract information from the test URL
    info = extractor._real_extract(test_url)

    # Check if the extracted information matches the expected results
    assert info['id'] == '2642630', "Extracted video ID does not match expected"
    assert info['display_id'] == 'one-direction-all-for-one', "Extracted display ID does not match expected"

# Generated at 2024-03-18 09:30:24.865057
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor and _real_extract method
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()
    
    # Check if the instance is created
    assert isinstance(extractor, WallaIE), "WallaIE instance not created"
    
    # Check if the _VALID_URL pattern matches the test URL
    assert re.match(extractor._VALID_URL, test_url), "Test URL does not match the _VALID_URL pattern"
    
    # Extract information
    info_dict = extractor._real_extract(test_url)
    
    # Check if the extracted information matches the expected results

# Generated at 2024-03-18 09:30:27.838102
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:30:31.978158
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:30:35.123743
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for the constructor of WallaIE
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:31:03.202480
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:31:10.057985
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(ie._VALID_URL, test_url), "The URL should match the _VALID_URL pattern"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    mobj = re.match(ie._VALID_URL, test_url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert video_id == '2642630', "The extracted video ID should be '2642630'"

# Generated at 2024-03-18 09:31:13.404186
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:31:16.690634
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:31:25.888653
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor and _real_extract method
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()

    # Check if the instance is created
    assert isinstance(extractor, WallaIE), "WallaIE instance not created"

    # Check if the _VALID_URL pattern matches the test URL
    assert re.match(extractor._VALID_URL, test_url), "Test URL does not match _VALID_URL pattern"

    # Extract information
    info = extractor._real_extract(test_url)

    # Check if the extracted information matches the expected results
    test_info_dict = WallaIE._TEST['info_dict']
    for key in test_info_dict:
        if key == 'description':
            assert re.match(test_info_dict[key], info[key]), f"Extracted {key} does not match expected value"

# Generated at 2024-03-18 09:31:29.398150
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:31:33.997962
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()
    assert extractor.suitable(test_url), "WallaIE should recognize the URL"
    assert extractor._match_id(test_url) == '2642630', "WallaIE should extract the correct video ID"


# Generated at 2024-03-18 09:31:37.022959
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:31:41.050885
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:31:43.390594
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for the constructor of WallaIE
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:32:41.424724
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()

    # Check if the extractor correctly identifies the valid URL
    assert extractor.suitable(test_url), "WallaIE should recognize the URL"

    # Check if the extractor extracts the correct video ID and display ID
    extracted_ids = extractor._match_id(test_url)
    assert extracted_ids == ('2642630', 'one-direction-all-for-one'), "WallaIE should extract the correct video ID and display ID"

    # Check if the test dictionary is correctly defined
    test_dict = extractor._TEST
    assert 'url' in test_dict, "The test dictionary should contain the 'url' key"
    assert 'info_dict' in test_dict, "The test dictionary should contain the 'info_dict' key"
    assert test_dict['url']

# Generated at 2024-03-18 09:32:48.333248
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(ie._VALID_URL, test_url), "The URL should match the _VALID_URL pattern"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    mobj = re.match(ie._VALID_URL, test_url)
    assert mobj.group('id') == '2642630', "The video ID should be extracted correctly"

# Generated at 2024-03-18 09:32:51.213553
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:32:54.262378
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for the constructor of WallaIE
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:33:01.421209
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly by asserting the _VALID_URL attribute
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

    # Check if the _TEST dictionary is properly set
    test_dict = ie._TEST
    assert test_dict['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert test_dict['info_dict']['id'] == '2642630'
    assert test_dict['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert test_dict['info_dict']['ext'] == 'flv'

# Generated at 2024-03-18 09:33:13.026251
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(ie._VALID_URL, test_url), "The URL should match the _VALID_URL pattern"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    mobj = re.match(ie._VALID_URL, test_url)
    assert mobj.group('id') == '2642630', "The video ID should be extracted correctly"

# Generated at 2024-03-18 09:33:18.202568
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()
    assert extractor.suitable(test_url), "WallaIE should recognize the URL"
    assert extractor._match_id(test_url) == '2642630', "WallaIE should extract the correct video ID"


# Generated at 2024-03-18 09:33:20.526576
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for the constructor of WallaIE
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:33:23.943669
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:33:26.166225
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for the constructor of WallaIE
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:35:13.025986
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor and _real_extract method
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    extractor = WallaIE()
    
    # Check if the extractor correctly identifies the valid URL
    assert extractor.suitable(test_url), "WallaIE should recognize the URL"

    # Extract information
    info = extractor._real_extract(test_url)

    # Check the extracted information
    assert info['id'] == '2642630', "Extracted video ID should match"
    assert info['display_id'] == 'one-direction-all-for-one', "Extracted display ID should match"
    assert info['title'] == 'וואן דיירקשן: ההיסטריה', "Extracted title should match"

# Generated at 2024-03-18 09:35:20.221177
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(ie._VALID_URL, test_url), "The URL should match the _VALID_URL pattern"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    mobj = re.match(ie._VALID_URL, test_url)
    assert mobj.group('id') == '2642630', "The video ID should be extracted correctly"

# Generated at 2024-03-18 09:35:29.140957
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Create an instance of the WallaIE class
    ie = WallaIE()

    # Check if the instance is created properly and is an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor), "WallaIE should be an instance of InfoExtractor"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(ie._VALID_URL, test_url), "_VALID_URL does not match the expected URL"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    mobj = re.match(ie._VALID_URL, test_url)
    video_id = mobj.group('id')
    display_id = mobj.group('display_id')
    assert video_id == '2642630', "Extracted video ID does not match the expected video ID"

# Generated at 2024-03-18 09:35:32.754365
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:35:35.765231
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:35:38.525699
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for the constructor of WallaIE
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:35:41.344166
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for the constructor of WallaIE
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:35:44.432497
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for the constructor of WallaIE
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:35:47.593038
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Test case for WallaIE constructor
    ie = WallaIE()
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:35:54.398829
# Unit test for constructor of class WallaIE
def test_WallaIE():    # Instance creation
    extractor = WallaIE()

    # Check if the instance is of the correct type
    assert isinstance(extractor, WallaIE), "WallaIE instance is not created properly"

    # Check if the _VALID_URL pattern matches the expected URL
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert re.match(extractor._VALID_URL, test_url), "_VALID_URL does not match the expected URL"

    # Check if the _VALID_URL pattern extracts the correct video ID and display ID
    match = re.match(extractor._VALID_URL, test_url)
    assert match.group('id') == '2642630', "Extracted video ID does not match the expected ID"
    assert match.group('display_id') == 'one-direction-all-for-one', "Extracted display ID does not match the expected display ID"
