

# Generated at 2022-06-14 16:24:00.814600
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:08.258503
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    # Test that _VALID_URL is a valid URL.
    m = re.match(info_extractor._VALID_URL, info_extractor._VALID_URL)
    assert m, repr(info_extractor._VALID_URL) + " is not a valid URL"
    #
    # Test that _VALID_URL contains a group named 'id'.
    groups = m.groups()
    assert len(groups) > 0, repr(info_extractor._VALID_URL) + " does not contain any groups"
    assert "id" in groups, repr(info_extractor._VALID_URL) + " does not contain a group named 'id'"
    #
    # Test that _TEST is not None.
    test = info_extractor._TEST

# Generated at 2022-06-14 16:24:09.994480
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert isinstance(HitRecordIE, type)


# Generated at 2022-06-14 16:24:11.737678
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:12.431919
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('http://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:24:13.091183
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:24:25.107915
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # When: constructing HitRecordIE
    ie = HitRecordIE()
    # Then: You can check some attributes are constructed
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'

# Generated at 2022-06-14 16:24:26.283009
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")


# Generated at 2022-06-14 16:24:27.856986
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE._VALID_URL)

# Generated at 2022-06-14 16:24:32.394433
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    try:
        HitRecordIE()
    except TypeError as e:
        assert "expected 1 argument, got 0" in str(e), "Constructor of class HitRecordIE is correct"
    assert "Constructor of class HitRecordIE is correct", "Constructor of class HitRecordIE is correct"


# Generated at 2022-06-14 16:24:44.149958
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Unit test for constructor of class HitRecordIE
    """
    HitRecordIE("http://hitrecord.org/records/2954362")



# Generated at 2022-06-14 16:24:44.949416
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:24:49.339434
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert ie.suitable('https://hitrecord.org/records/2954362') == True
    assert ie.suitable('https://hitrecord.org/records/29543622') == False


# Generated at 2022-06-14 16:24:52.337510
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # create instance of HitRecordIE
    ie_obj = HitRecordIE()
    print(ie_obj._VALID_URL)
    print(ie_obj.name)

# Generated at 2022-06-14 16:24:53.916775
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie != None

# Generated at 2022-06-14 16:24:56.336836
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
	# Create instance of class HitRecordIE
	href = HitRecordIE()
	print(href)

test_HitRecordIE()

# Generated at 2022-06-14 16:24:57.308785
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:25:09.619563
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    info_extractor = HitRecordIE()
    assert(info_extractor._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

# Generated at 2022-06-14 16:25:11.383180
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie._real_extract('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:25:16.224619
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')
    assert not ie.suitable('https://hitrecord.org/records/')
    assert ie.IE_NAME == 'hitrecord'
    assert ie.VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie.VIDEO_URL == 'https://hitrecord.org/api/web/records/%s'

# Generated at 2022-06-14 16:25:38.181862
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.suitable('https://hitrecord.org/records/2954362')
    print("URL Suitable : Passed")
    ie.suitable('https://hitrecord.org/records/29543623')
    print("URL Not Suitable : Passed")
    ie.suitable('https://hitrecord.org/records/295436')
    print("URL Not Suitable : Passed")


# Generated at 2022-06-14 16:25:49.644092
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("https://hitrecord.org/records/2954362")
    assert ie.ie_key() == 'HitRecord'
    assert ie.ie_name() == 'HitRecord'
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert ie._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'

# Generated at 2022-06-14 16:25:50.366020
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('HitRecord', True)

# Generated at 2022-06-14 16:25:56.323842
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.IE_NAME == 'hitrecord'
    assert ie.IE_DESC == 'HitRecord'
    assert ie.VALID_URL.__doc__ == 'Regex for HitRecord videos'
    assert ie.VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:58.064911
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(1, 2, 3)
    assert ie.ie_key() == 'HitRecord'

# Generated at 2022-06-14 16:26:00.698728
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    extractor = HitRecordIE
    sample_url = "https://hitrecord.org/records/2954362"
    extractor._download_json(extractor._build_url(sample_url))

# Generated at 2022-06-14 16:26:02.869434
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.test('https://hitrecord.org/records/2954362')
    assert not ie.test('https://hitrecord.org')

# Generated at 2022-06-14 16:26:05.814598
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()
    i = obj.suitable('https://hitrecord.org/records/2954362')
    assert i == True

# Generated at 2022-06-14 16:26:08.339905
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.extract("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:26:10.285779
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._matches_url('https://hitrecord.org/records/2954362')
    assert not HitRecordIE._matches_url('https://hitrecord.org/')
    assert HitRecordIE._matches_url('https://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:26:39.190402
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:26:45.066012
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    test_urls = ['https://hitrecord.org/records/2954362',
                 'https://hitrecord.org/records/2954362?page=0&sort=3']

    for url in test_urls:
        print(ie._match_id(url))

if __name__ == '__main__':
    test_HitRecordIE()

# Generated at 2022-06-14 16:26:47.982069
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_HitRecordIE.HitRecordIE = HitRecordIE
    a = HitRecordIE()

# Test HitRecordIE by calling _extract_url

# Generated at 2022-06-14 16:26:52.805654
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.ie_key() == 'hitrecord'
    assert ie.ie_name() == 'HitRecord'
    assert ie.supported_extractors == [
        'DailymotionCloudIE',
        'YoutubeIE',
        'GenericIE',
        'VimeoIE',
        'HitRecordIE'
    ]

# Generated at 2022-06-14 16:26:58.352913
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    expected = HitRecordIE(HitRecordIE._create_context(HitRecordIE._TESTS[0]))
    assert expected._VALID_URL == HitRecordIE._VALID_URL
    assert expected._TEST == HitRecordIE._TEST
    assert expected.SUFFIX == 'LdJl7ARuQaA'
    assert expected.IE_DESC == 'HitRecord'
    assert expected.ie_key() == 'HitRecord'
    assert expected.video_id == '2954362'

# Generated at 2022-06-14 16:26:59.822664
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    'Test constructor'
    assert HitRecordIE()

# Generated at 2022-06-14 16:27:03.027708
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:03.937219
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:27:04.859854
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie

# Generated at 2022-06-14 16:27:06.258508
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    print(ie)

# Generated at 2022-06-14 16:28:02.471129
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Call private initializer method of HitRecordIE class
    HitRecordIE._real_initialize()
    # This class should only have one extractor field
    assert len(HitRecordIE._IE_DESC) == 1
    # Check that the name of the only extractor field is HitRecordIE
    assert list(HitRecordIE._IE_DESC.keys())[0] == HitRecordIE.ie_key()

# Generated at 2022-06-14 16:28:12.808026
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    url = "https://hitrecord.org/records/2954362"
    assert HitRecordIE().suitable(url) == True
    assert HitRecordIE()._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE()._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert HitRecordIE()._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert HitRecordIE()._TEST['description'] == 'md5:e62defaffab5075a5277736bead95a3d'
    assert HitRecordIE()._TEST['duration'] == 139.327

# Generated at 2022-06-14 16:28:15.994748
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.report_download_page('https://hitrecord.org')
    ie.report_extraction('https://hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:28:16.546893
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:23.597387
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie_class = HitRecordIE
    if ie_class is None:
        assert False, 'Please comment out these lines before running the test'

    ie = ie_class()
    assert ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    match = ie._VALID_URL_RE.match(ie._TEST['url'])
    assert match
    assert match.groupdict()['id'] == '2954362'

# Generated at 2022-06-14 16:28:24.896311
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie
    assert ie.IE_NAME

# Generated at 2022-06-14 16:28:27.968741
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('https://hitrecord.org/records/2954362')
    assert ie.url == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:28:28.500879
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()

# Generated at 2022-06-14 16:28:30.880224
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://hitrecord.org/records/2954362')


# Generated at 2022-06-14 16:28:31.408449
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:30:22.061292
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:30:23.388425
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hitrecord = HitRecordIE()
    assert hitrecord is not None

# Generated at 2022-06-14 16:30:25.010389
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    record = HitRecordIE()
    print(record)

if __name__ == '__main__':
    test_HitRecordIE()

# Generated at 2022-06-14 16:30:36.278939
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:39.901271
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    h = HitRecordIE()
    assert h._match_id('https://hitrecord.org/records/2954362') == '2954362'
    assert h._match_id('https://hitrecord.org/records/2954362') == '2954362'

# Generated at 2022-06-14 16:30:47.329878
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Get instance of HitRecordIE class
    obj = HitRecordIE()
    # Run extract method of HitRecordIE class
    # with sample link
    obj.extract("https://hitrecord.org/records/2954362")
    # Get dictionary of values
    info = obj._downloader.info

    # Validate video ID
    assert info['id'] == '2954362'
    # Validate video Title
    assert info['title'] == 'A Very Different World (HITRECORD x ACLU)'
    # Validate video uploader
    assert info['uploader'] == 'Zuzi.C12'

# Generated at 2022-06-14 16:30:51.193151
# Unit test for constructor of class HitRecordIE

# Generated at 2022-06-14 16:30:53.849667
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('HitRecord', 'https://hitrecord.org/records/2954362')



# Generated at 2022-06-14 16:30:55.281748
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE('https://www.hitrecord.org/records/2954362')

# Generated at 2022-06-14 16:31:06.139411
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert HitRecordIE().IE_NAME == 'hitrecord'