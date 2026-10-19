

# Generated at 2022-06-14 16:34:45.289472
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:34:56.354018
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE(url)
    assert isinstance(ie, KonserthusetPlayIE)
    assert ie.host is not None
    assert ie.host == 'www.konserthusetplay.se'
    assert ie.video_id == 'CKDDnlCY-dhWAAqiMERd-A'
    assert ie.title is None
    assert ie._VALID_URL == 'https?://(?:www\\.)?(?:konserthusetplay|rspoplay)\\.se/\\?.*\\bm=(?P<id>[^&]+)'


# Generated at 2022-06-14 16:34:58.021462
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	ie = KonserthusetPlayIE()


# Generated at 2022-06-14 16:35:05.324745
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert KonserthusetPlayIE._match_id(url).startswith(video_id)
    assert KonserthusetPlayIE._match_id(video_id).startswith(video_id)

# Generated at 2022-06-14 16:35:07.116305
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None

# Generated at 2022-06-14 16:35:15.132257
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.extractor == KonserthusetPlayIE
    assert ie.url == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert ie.id == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:35:18.308394
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test when using a different constructor
    KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:35:23.179123
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Unit test for constructor of class KonserthusetPlayIE
    """
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == KonserthusetPlayIE._VALID_URL
    assert ie._TESTS == KonserthusetPlayIE._TESTS

# Generated at 2022-06-14 16:35:34.034715
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert ie.URL == 'http://www.konserthusetplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    assert ie.name == 'KonserthusetPlay'
    assert ie.id == 'elWuEH34SMKvaO4wO_cHBw'
    assert ie.playlist_id == ''
    assert ie.playlist_title == ''
    assert ie.playlist_description == ''
    assert ie.playlist_url == ''
    assert ie.playlist_count == 0
    assert ie.playlist_size == 0
    assert ie.video_title == ''

# Generated at 2022-06-14 16:35:35.988343
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    extractor = KonserthusetPlayIE()
    assert isinstance(extractor, InfoExtractor)

# Generated at 2022-06-14 16:36:07.272107
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Constructor test
    """
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay', 'Incorrect ie_key'
    assert ie.extractor_key() == 'KonserthusetPlay', 'Incorrect extractor_key'

# Generated at 2022-06-14 16:36:09.905655
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test URL
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

    # Test instance
    KonserthusetPlayIE(url)

# Generated at 2022-06-14 16:36:14.740961
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Constructor test
    """
    ie = KonserthusetPlayIE()
    # Test no exception thrown
    # ie.download('http://www.play.konserthuset.se/?m=efQ2PZoTiPuXeRajRd1sHQ')

# Generated at 2022-06-14 16:36:17.369903
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test if type of unit_test is "class"
    assert type(KonserthusetPlayIE) == type(type)


# Generated at 2022-06-14 16:36:19.054710
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie != None


# Generated at 2022-06-14 16:36:22.435125
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = (
        'http://www.konserthusetplay.se/?'
        'm=CKDDnlCY-dhWAAqiMERd-A')
    KonserthusetPlayIE(url)

# Generated at 2022-06-14 16:36:23.994730
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    print(KonserthusetPlayIE)

# Generated at 2022-06-14 16:36:25.513271
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    my_test = KonserthusetPlayIE()
    assert my_test != None

# Generated at 2022-06-14 16:36:29.310460
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_key() in globals()
    assert ie.supported_extensions() == ['mp4']

# Generated at 2022-06-14 16:36:31.813300
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.IS_DEVELOPMENT
    assert ie._VALID_URL
    assert ie._TESTS

# Generated at 2022-06-14 16:37:18.586723
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:37:20.337975
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None


# Generated at 2022-06-14 16:37:22.007285
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.IE_NAME == 'KonserthusetPlay'

# Generated at 2022-06-14 16:37:24.472104
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	# KonserthusetPlayIE should return a value of type InfoExtractor
	assert isinstance(KonserthusetPlayIE, InfoExtractor)


# Generated at 2022-06-14 16:37:25.399851
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE(KonserthusetPlayIE._VALID_URL)

# Generated at 2022-06-14 16:37:33.511739
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Valid URL
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    # Download webpage
    webpage = get_webpage(url)
    # Download JSON from webpage
    rest_url = 'http://csp.picsearch.com/rest?e=I1_pKjJz4MwO2O4wM-mI_g&containerId=mediaplayer&i=object'
    rest = get_json(rest_url)
    # Extract video id
    video_id = re.search(r'm=([^&]+)', url).group(1)
    # Extract formats and other properties
    formats, title, description, thumbnail, duration = get_KonserthusetPlay_formats(webpage, rest)
   

# Generated at 2022-06-14 16:37:40.828804
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        # Checking the constructor
        assert(KonserthusetPlayIE is not None)
    except AssertionError:
        print("Author: Anshuman Suri, URL: https://github.com/MrSuri/ytdl-org")
        raise AssertionError


if __name__ == '__main__':
    # Test class
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:41.817868
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	obj = KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:50.073442
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    '''
    This unittest tests the constructor of the class KonserthusetPlayIE.
    '''

    konserthuset_play_ie = KonserthusetPlayIE()
    assert konserthuset_play_ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:55.799271
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie._downloader is not None

# Generated at 2022-06-14 16:38:53.705496
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE("http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw")

# Generated at 2022-06-14 16:38:57.754289
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except KeyError:
        assert False, 'Error when instantiating class'


# Generated at 2022-06-14 16:38:59.552678
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    r = KonserthusetPlayIE();


# Generated at 2022-06-14 16:39:09.970453
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    print("Testing KonserthusetPlayIE")
    url = "https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    kpIE = KonserthusetPlayIE()
    res = kpIE._real_extract(url)
    print(res)
    assert(res['id']=='CKDDnlCY-dhWAAqiMERd-A')
    assert(res['title']=="Orkesterns instrument: Valthornen")
    assert(res['ext']=='mp4')

# Generated at 2022-06-14 16:39:12.518283
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj_1 = KonserthusetPlayIE()
    obj_2 = KonserthusetPlayIE()

    assert obj_1 == obj_2

# Generated at 2022-06-14 16:39:22.240937
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie != None
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'KonserthusetPlay'
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert not ie.suitable('https://www.google.com/')


# Generated at 2022-06-14 16:39:24.236227
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    url = 'http://www.konserthusetplay.se/?m=%s' % video_id
    ie = KonserthusetPlayIE()
    ie._real_extract(url)

# Generated at 2022-06-14 16:39:29.102168
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'


# Generated at 2022-06-14 16:39:30.643115
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE()
    assert(instance)

# Generated at 2022-06-14 16:39:31.645487
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()


# Generated at 2022-06-14 16:41:47.309240
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay'
    assert ie.SUCCESS == 'SUCCESS'

# Generated at 2022-06-14 16:41:49.105585
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:41:52.100862
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # KonserthusetPlayIE constructor takes in a parameter and it does return a object
    KonserthusetPlayIE('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:41:57.924446
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test that the constructor of class KonserthusetPlayIE
    # is able to handle the url given in this unit test
    url = "http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw"
    konser_obj = KonserthusetPlayIE()
    res = konser_obj
    assert isinstance(res, KonserthusetPlayIE)
    assert url == res._VALID_URL

# Generated at 2022-06-14 16:42:01.665558
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.KT_URL_BASE == 'http://www.konserthusetplay.se/'
    assert ie.RSPOPLAY_URL_BASE == 'http://rspoplay.se/'

# Generated at 2022-06-14 16:42:02.641779
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:06.432724
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    decode_url = KonserthusetPlayIE._match_id(None).decode('unicode-escape')
    assert decode_url == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:42:07.385759
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:16.118858
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert KonserthusetPlayIE('http://www.konserthusetplay.se/')._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:42:17.702607
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    hasattr(ie, '_real_extract')