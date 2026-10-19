

# Generated at 2022-06-14 16:34:48.940630
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.suitable('http://rspoplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    ie.extract('http://rspoplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:34:50.910264
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None


# Generated at 2022-06-14 16:34:55.996673
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE("")
    KonserthusetPlayIE("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    KonserthusetPlayIE("http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw")


# Generated at 2022-06-14 16:35:08.531985
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    assert ie.IE_NAME == 'konserthusetplay'
    assert ie.IE_DESC == 'Konserthuset Play'
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:11.974943
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    assert ie.NAME == "Konserthuset Play"
    assert ie.IE_NAME == "konserthusetplay"
    assert hasattr(ie, "ie_key")
    assert ie.ie_key() == "KonserthusetPlay"
    assert hasattr(ie, "info_extractors")
    assert ie.info_extractors() == [{'ie_key': 'KonserthusetPlay', 'ie': 'KonserthusetPlayIE', 'test': True}]

# Generated at 2022-06-14 16:35:17.050528
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Check if constructor of class KonserthusetPlayIE is well-behaved
    assert KonserthusetPlayIE.__name__ == 'KonserthusetPlayIE'
    assert KonserthusetPlayIE.__doc__ == "KonserthusetPlay and RSO Play"

# Generated at 2022-06-14 16:35:18.345602
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Create object for testing
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:30.124236
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert (KonserthusetPlayIE({})._VALID_URL ==
            r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')
    # Test input is not changed
    test_input = {'_formats': '8624'}
    assert (KonserthusetPlayIE(test_input)._formats == '8624')

# Generated at 2022-06-14 16:35:31.954478
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, KonserthusetPlayIE)

# Generated at 2022-06-14 16:35:33.872981
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # TODO(adw): Add asserts
    ie = KonserthusetPlayIE()
    ie.extract(ie._VALID_URL)

# Generated at 2022-06-14 16:35:59.716144
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    url = 'https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    test_info_dict = {
        'id': 'CKDDnlCY-dhWAAqiMERd-A',
        'ext': 'mp4',
        'title': 'Orkesterns instrument: Valthornen',
        'description': 'md5:f10e1f0030202020396a4d712d2fa827',
        'thumbnail': 're:^https?://.*$',
        'duration': 398.76
    }
    info_dict = ie._real_extract(url)
    assert info_dict == test_info_dict

# Generated at 2022-06-14 16:36:09.431541
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Unit test for KonserthusetPlayIE constructor.

    It is done by calling the constructor with a test url,
    and verifying that the created object matches expected data.

    Returns:
        None.

    Raises:
        AssertionError: If the test fails.
    """

# Generated at 2022-06-14 16:36:10.572545
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:22.436861
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie._VALID_URL == "https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)"

# Generated at 2022-06-14 16:36:23.551218
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:25.446812
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE()
    # TODO: Fix this test
    assert(k != None)

# Generated at 2022-06-14 16:36:31.450849
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # given
    url = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'

    # when
    the_correct_KonserthusetPlayIE_is_created = KonserthusetPlayIE(url)

    # then
    assert isinstance(the_correct_KonserthusetPlayIE_is_created, KonserthusetPlayIE)


# Generated at 2022-06-14 16:36:38.496204
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    # Test for _real_extract()
    info = ie._real_extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert info['id'] == 'CKDDnlCY-dhWAAqiMERd-A'
    assert info['ext'] == 'mp4'
    assert info['title'] == 'Orkesterns instrument: Valthornen'
    assert info['duration'] == 398.76

# Generated at 2022-06-14 16:36:41.266172
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()




# Generated at 2022-06-14 16:36:42.326355
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:13.549070
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A");
    assert obj.url == "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    assert obj.video_id == "CKDDnlCY-dhWAAqiMERd-A"
    return True

# Generated at 2022-06-14 16:37:15.652101
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:37:24.037245
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # If function is not None it means that test succeeded
    assert KonserthusetPlayIE.__name__ == 'KonserthusetPlayIE' and \
        KonserthusetPlayIE.__doc__ == InfoExtractor.__doc__ and \
        KonserthusetPlayIE.SUFFIX == ':konserthusetplay' and \
        getattr(KonserthusetPlayIE.__init__, '__doc__', None) == \
        InfoExtractor.__init__.__doc__ and \
        not hasattr(KonserthusetPlayIE.__init__, '__doc__')


# Unit tests for class KonserthusetPlayIE (KonserthusetPlay)

# Generated at 2022-06-14 16:37:31.790080
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    regex = KonserthusetPlayIE._VALID_URL
    # pass
    regex.match('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    # not pass
    regex.match('http://www.konserthusetplay.se/b/CKDDnlCY-dhWAAqiMERd-A')
    regex.match('http://www.konserthusetplay.se/a/CKDDnlCY-dhWAAqiMERd-A')
    regex.match('http://www.konserthusetplay.se/v/CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:37:32.680381
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:36.143748
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE()
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'


# Generated at 2022-06-14 16:37:38.032674
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE

# Generated at 2022-06-14 16:37:39.851208
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:37:46.243816
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert(KonserthusetPlayIE.suitable(
        "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"))
    assert(KonserthusetPlayIE.suitable(
        "http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw"))
    assert(not KonserthusetPlayIE.suitable(
        "http://rspoplay.se/"))

# Generated at 2022-06-14 16:37:51.446630
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    if not KonserthusetPlayIE.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'):
        raise AssertionError('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A not suitable')

# Generated at 2022-06-14 16:38:58.945295
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    info = KonserthusetPlayIE._build_url_result('CKDDnlCY-dhWAAqiMERd-A')
    assert info['id'] == 'CKDDnlCY-dhWAAqiMERd-A'
    assert info['title'] == 'Orkesterns instrument: Valthornen'
    assert info['description'] == 'md5:f10e1f0030202020396a4d712d2fa827'
    assert info['thumbnail'] == 're:^https?://.*$'
    assert info['duration'] == 398.76
    assert info['formats'][0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:39:03.636700
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Check with valid URL
    konserthusetplay = KonserthusetPlayIE()
    assert konserthusetplay != None

    # Check with a non valid URL
    konserthusetplay = KonserthusetPlayIE()
    assert konserthusetplay != None

# Generated at 2022-06-14 16:39:09.079989
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie.IE_NAME == 'konserthusetplay:play'
    assert ie.IE_DESC == 'Konserthuset Play'

# Generated at 2022-06-14 16:39:20.771303
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    kp_ie = KonserthusetPlayIE(url)
    assert kp_ie._match_id("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A") == "CKDDnlCY-dhWAAqiMERd-A"
    assert kp_ie._match_id("http://rspoplay.se/?m=CKDDnlCY-dhWAAqiMERd-A") == "CKDDnlCY-dhWAAqiMERd-A"

# Generated at 2022-06-14 16:39:23.040208
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie.__class__.__name__ == 'KonserthusetPlayIE'

# Generated at 2022-06-14 16:39:28.946815
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthuset_play_ie = KonserthusetPlayIE()

    assert konserthuset_play_ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:30.379127
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None

# Generated at 2022-06-14 16:39:31.808173
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()



# Generated at 2022-06-14 16:39:33.831509
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test for constructor with invalid url
    try:
        assert KonserthusetPlayIE('test_url') != None
    except:
        return

# Generated at 2022-06-14 16:39:37.733283
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    # Test regex
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:41:54.760068
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay'
    assert ie.ie_key() == 'rspoplay'

# Generated at 2022-06-14 16:41:55.566553
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:41:58.885984
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    KonserthusetPlayIE()._real_extract(url, video_id)

# Generated at 2022-06-14 16:41:59.846885
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:42:01.199713
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert(isinstance(KonserthusetPlayIE, type) )

# Generated at 2022-06-14 16:42:09.320041
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:42:12.032319
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE(KonserthusetPlayIE.IE_NAME, KonserthusetPlayIE._VALID_URL)
    assert obj.ie_key() == KonserthusetPlayIE.IE_NAME

# Generated at 2022-06-14 16:42:18.441189
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('url', 'pagename', 'title', 'ext', 'thumbnail', 'duration', 'formats', 'subtitles')
    assert ie.url == 'url'
    assert ie.pagename == 'pagename'
    assert ie.title == 'title'
    assert ie.ext == 'ext'
    assert ie.thumbnail == 'thumbnail'
    assert ie.duration == 'duration'
    assert ie.formats == 'formats'
    assert ie.subtitles == 'subtitles'


# Generated at 2022-06-14 16:42:19.294951
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE(InfoExtractor())

# Generated at 2022-06-14 16:42:20.374571
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    constructor = KonserthusetPlayIE()
    assert constructor