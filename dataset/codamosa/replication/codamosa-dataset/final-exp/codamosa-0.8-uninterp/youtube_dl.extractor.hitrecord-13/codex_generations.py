

# Generated at 2022-06-14 16:24:00.502986
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE() is not None

# Generated at 2022-06-14 16:24:06.388640
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Test for the HitRecordIE class
    """
    assert HitRecordIE._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    test = HitRecordIE._TEST
    url = test['url']
    url_id = HitRecordIE._match_id(url)
    assert url_id == '2954362'
    assert HitRecordIE._download_json(
        'https://hitrecord.org/api/web/records/%s' % url_id, url_id)

# Generated at 2022-06-14 16:24:10.134721
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE() # Launch the constuctor of class HitRecordIE
    assert type(ie) == HitRecordIE # Make sure that the constructor returns a HitRecordIE object

# Generated at 2022-06-14 16:24:11.941053
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:24:13.567006
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    video = HitRecordIE()
    assert video.ie_key() == 'HitRecord'

# Generated at 2022-06-14 16:24:25.568781
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    instance = HitRecordIE()

# Generated at 2022-06-14 16:24:26.363060
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    _ = HitRecordIE()

# Generated at 2022-06-14 16:24:36.748222
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert(ie._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')

# Generated at 2022-06-14 16:24:39.000465
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test to create an instance of HitRecordIE
    print("Testing constructor of class HitRecordIE")
    HitRecordIE()

# Generated at 2022-06-14 16:24:40.838146
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test1 = HitRecordIE()
    test2 = HitRecordIE()

    assert test1 is test2

# Generated at 2022-06-14 16:24:54.825662
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert isinstance(ie, HitRecordIE)
    # Assert that url matches regex
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert ie._TEST['url'] == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:25:07.039771
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_HitRecordIE = HitRecordIE()
    assert test_HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:15.943342
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:25:18.745783
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE(HitRecordIE._downloader)._VALID_URL == HitRecordIE._VALID_URL


# Generated at 2022-06-14 16:25:21.940196
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # test the constructor of HitRecordIE
    url = 'https://hitrecord.org/records/2954362'
    HitRecordIE(url)

# Generated at 2022-06-14 16:25:23.568563
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Test constructor to create HitRecordIE.
    """
    HitRecordIE(None)

# Generated at 2022-06-14 16:25:23.950698
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:25:25.386378
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()
    assert obj


# Generated at 2022-06-14 16:25:26.794538
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie


# Generated at 2022-06-14 16:25:28.247965
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE({}) is not None


# Generated at 2022-06-14 16:25:42.527883
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    success = True

    # test YoutubeIE
    hit_record = HitRecordIE(object())

    success = success and hit_record.suitable('https://hitrecord.org/records/2954362')

    return success

# Generated at 2022-06-14 16:25:45.131265
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE("https://www.hitrecord.org/records/2954362")
    assert ie.__class__ == HitRecordIE

# Generated at 2022-06-14 16:25:48.126392
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE(HitRecordIE._VALID_URL)
    assert ie.name == 'HitRecord'
    assert ie.urls == ['https://hitrecord.org/records/2954362']

# Generated at 2022-06-14 16:25:49.017193
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE

# Generated at 2022-06-14 16:25:49.813271
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(HitRecordIE._downloader)

# Generated at 2022-06-14 16:25:50.694296
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE is not None

# Generated at 2022-06-14 16:25:54.395342
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Simple test to ensure that none of the attributes of class HitRecordIE
    are null.
    """
    HitRecordIE(HitRecordIE._TEST)

# Generated at 2022-06-14 16:25:54.958427
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:26:03.505112
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362/') == True
    assert ie.suitable('https://hitrecord.org/records/2954362/') == True
    assert ie.suitable('https://hitrecord.org/records/2954362/') == True
    assert ie.suitable('https://hitrecord.org/records/2954362/') == True
    assert ie.suitable('https://hitrecord.org/records/2954362/') == True
    assert ie.suitable('https://hitrecord.org/records/2954362/') == True
    assert ie.suitable('https://hitrecord.org/records/2954362/') == True


# Generated at 2022-06-14 16:26:06.095935
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    x = HitRecordIE()
    y = x._real_extract("https://hitrecord.org/records/2954362")
    print(y)

# Generated at 2022-06-14 16:26:26.356823
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:26:26.948895
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE()
    assert obj._VALID_URL is not None

# Generated at 2022-06-14 16:26:34.326482
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    e = HitRecordIE()
    assert e._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'
    assert isinstance (e._TEST, dict)
    assert isinstance (e._TEST['url'], str)
    assert isinstance (e._TEST['md5'], str)
    assert isinstance (e._TEST['info_dict'], dict)


# Generated at 2022-06-14 16:26:37.530104
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    c = HitRecordIE('url')
    a = c.extract_info('http://www.hitrecord.org/records/2954362')
    assert a.get('id') == '2954362'
    assert a.get('uploader') == 'Zuzi.C12'

# Generated at 2022-06-14 16:26:49.175117
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
    # test url
    url = 'https://hitrecord.org/records/2954362'
    # create test object
    HitRecordIE_object = HitRecordIE(InfoExtractor())
    # test
    assert HitRecordIE_object._match_id(url) == '2954362'
    assert HitRecordIE_object._TEST['id'] == '2954362'
    assert HitRecordIE_object._TEST['url'] == 'https://hitrecord.org/records/2954362'

# Generated at 2022-06-14 16:26:58.353135
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    obj = HitRecordIE('http://www.hitrecord.org/records/2954362')
    assert obj._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:27:05.752950
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie._VALID_URL.search('https://hitrecord.org/records/2954362')
    assert not ie._VALID_URL.search('https://hitrecord.org/records/')
    assert ie._VALID_URL.search('https://hitrecord.org/records/748989')
    assert not ie._VALID_URL.search('https://hitrecord.org/records/000000')

# Generated at 2022-06-14 16:27:06.912507
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    h = HitRecordIE()
    assert h is not None

# Generated at 2022-06-14 16:27:08.136090
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    _test = HitRecordIE()

# Generated at 2022-06-14 16:27:13.305683
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    """
    Tests the HitRecordIE class.
    """
    ie = HitRecordIE()
    ie.match("https://hitrecord.org/records/2954362")
    ie.download("https://hitrecord.org/records/2954362")
    ie.extract("https://hitrecord.org/records/2954362")

# Generated at 2022-06-14 16:28:14.099988
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert_equal(ie._VALID_URL, r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)')
    assert_equal(ie._TEST['url'], 'https://hitrecord.org/records/2954362')
    assert_equal(ie._TEST['md5'], 'fe1cdc2023bce0bbb95c39c57426aa71')
    assert_equal(ie._TEST['info_dict']['id'], '2954362')
    assert_equal(ie._TEST['info_dict']['ext'], 'mp4')
    assert_equal(ie._TEST['info_dict']['title'], 'A Very Different World (HITRECORD x ACLU)')

# Generated at 2022-06-14 16:28:15.406956
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    assert HitRecordIE()


# Generated at 2022-06-14 16:28:15.997564
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:16.547817
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE()

# Generated at 2022-06-14 16:28:17.588429
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    x = HitRecordIE()
    print(x)

# Generated at 2022-06-14 16:28:19.799487
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Test the constructor of class HitRecordIE
    ie = HitRecordIE()
    print(ie)


test_HitRecordIE()

# Generated at 2022-06-14 16:28:31.126211
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():

    h = HitRecordIE()
    assert h._TEST['url'] == 'https://hitrecord.org/records/2954362'
    assert h._TEST['md5'] == 'fe1cdc2023bce0bbb95c39c57426aa71'
    assert h._TEST['info_dict']['id'] == '2954362'
    assert h._TEST['info_dict']['ext'] == 'mp4'
    assert h._TEST['info_dict']['title'] == 'A Very Different World (HITRECORD x ACLU)'
    assert h._TEST['info_dict']['description'] == 'md5:e62defaffab5075a5277736bead95a3d'
    assert h._TEST['info_dict']['duration'] == 139.327

# Generated at 2022-06-14 16:28:33.821956
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test_object = HitRecordIE()
    # Test for constructor of class HitRecordIE
    assert isinstance(test_object, HitRecordIE)
    
# Test to look for id in url

# Generated at 2022-06-14 16:28:42.502073
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # Init
    info_extractor = InfoExtractor()
    info_extractor._downloader = None
    # Execute
    hitRecordIE = HitRecordIE(info_extractor)
    # Judgment
    assert hitRecordIE._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:28:44.457762
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # HitRecordIE constructor is expected to fail when given URL is None.
    assert HitRecordIE() is None

# Generated at 2022-06-14 16:30:31.511718
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    ie.IE_NAME == 'hitrecord'

# Generated at 2022-06-14 16:30:34.443543
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    test = HitRecordIE()
    test.suite()
    if test.constructor == HitRecordIE:
        print('HitRecordIE: constructor: Correct')
    else:
        print('HitRecordIE: constructor: Incorrect')


# Generated at 2022-06-14 16:30:44.480245
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    # NOTE: The following test will check whether class can be instanciated.
    #       No data is being tested at the moment.
    #       The code is being placed at the very bottom of this script because
    #       formating of the code may look kinda complex.
    from . import Options
    from .common import InfoExtractor
    from .common import FileDownloader
    from .common import common
    from .common import compat_str
    from .common import compat_urllib_request
    from .common import compat_urllib_error
    from .common import compat_urllib_parse
    from .common import compat_urlparse
    from .common import compat_shlex_quote
    from .common import compat_kwargs
    from .common import compat_os_path
    from .common import compat_setenv

# Generated at 2022-06-14 16:30:52.430338
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hit = HitRecordIE()
    assert hit._VALID_URL == 'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:30:59.013160
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
     #initiating the class HitRecordIE
    obj = HitRecordIE()
    #initiating the url to each request
    url = 'https://hitrecord.org/records/2954362'
    #calling the method _real_extract for testing the class
    obj._real_extract(url)
    #testing the class with the template
    obj._TEST['url'] = url
    obj._TEST['info_dict']
 

# Generated at 2022-06-14 16:31:00.131524
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(None)


# Generated at 2022-06-14 16:31:02.921803
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE()
    assert ie.suitable('https://hitrecord.org/records/2954362')


# Generated at 2022-06-14 16:31:07.269330
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    ie = HitRecordIE('http://www.hitrecord.org/records/2954362')
    assert ie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:31:17.758847
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    hie = HitRecordIE()
    assert hie._VALID_URL == r'https?://(?:www\.)?hitrecord\.org/records/(?P<id>\d+)'

# Generated at 2022-06-14 16:31:19.036231
# Unit test for constructor of class HitRecordIE
def test_HitRecordIE():
    HitRecordIE(None)
