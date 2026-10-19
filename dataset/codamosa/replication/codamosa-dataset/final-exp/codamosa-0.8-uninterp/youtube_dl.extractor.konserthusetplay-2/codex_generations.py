

# Generated at 2022-06-14 16:34:55.272492
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    webpage = 'http://www.rspoplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    e = '0dSxk-1yCAdQQAPTZHXNQQ'
    rest = 'http://csp.picsearch.com/rest?e=0dSxk-1yCAdQQAPTZHXNQQ&containerId=mediaplayer&i=object'
    playerconfig = 'http://csp.picsearch.com/rest?e=0dSxk-1yCAdQQAPTZHXNQQ&containerId=mediaplayer&i=object'
    title = 'Orkesterns instrument: Valthornen'

# Generated at 2022-06-14 16:34:57.776423
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:34:59.938367
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert (ie.IE_NAME == 'KonserthusetPlay')

# Generated at 2022-06-14 16:35:07.337900
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert ie.IE_NAME == 'konserthusetplay'

# Generated at 2022-06-14 16:35:12.470529
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """This unit test tests if KonserthusetPlayIE is used to download
    the requested information.
    """
    test_url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    KonserthusetPlayIE().download(test_url)

# Generated at 2022-06-14 16:35:20.955821
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:35:32.240571
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    entry = KonserthusetPlayIE()._real_extract(url)
    assert entry.get('title') == 'Orkesterns instrument: Valthornen'
    assert entry.get('id') == 'CKDDnlCY-dhWAAqiMERd-A'
    assert entry.get('thumbnail') == 'http://content.srv.csp.picsearch.com/rest/media/2.81/10266892.jpg'
    assert entry.get('subtitles').get('sv').get('url') == 'http://content.srv.csp.picsearch.com/rest/tx/1.33/10266892.vtt'

# Generated at 2022-06-14 16:35:35.343801
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    x = KonserthusetPlayIE()
    assert(x.get_url_re() == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')

# Generated at 2022-06-14 16:35:38.695256
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Unit test for class KonserthusetPlayIE
    """
    url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    KonserthusetPlayIE.extract(url)

# Generated at 2022-06-14 16:35:46.194035
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from unittest import mock

    # Test constructor of class KonserthusetPlayIE
    def _test_KonserthusetPlayIE(url, expected_url, expected_ext, expected_title, expected_duration, expected_webpage):
        ie = KonserthusetPlayIE({})
        info = ie.extract({'url': url})

        assert info['url'] == expected_url
        assert info['ext'] == expected_ext
        assert info['title'] == expected_title
        assert info['duration'] == expected_duration
        assert ie._download_webpage.call_count == 1
        assert ie._download_webpage.call_args_list[0][0][0] == expected_webpage
        assert ie._download_json.call_count == 1

    # Mock methods
    ie = Konserthuset

# Generated at 2022-06-14 16:36:17.200207
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'https://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    ie = KonserthusetPlayIE()
    ie.extract(url)
    assert ie.url == url
    assert ie.video_id == 'elWuEH34SMKvaO4wO_cHBw'

# Generated at 2022-06-14 16:36:18.446262
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:20.023754
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE in InfoExtractor.__dict__.values()

# Generated at 2022-06-14 16:36:30.876560
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:36:38.187095
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:40.211378
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE(InfoExtractor())

# Generated at 2022-06-14 16:36:41.674337
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:43.815815
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    assert ie.ie_key() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:36:53.323326
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL==r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:56.749065
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthusetplay_ie = KonserthusetPlayIE()
    assert konserthusetplay_ie is not None


# Generated at 2022-06-14 16:37:45.214105
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE()
    assert instance

# Generated at 2022-06-14 16:37:51.972234
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	testData = {'duration': 398.76, 'title': 'Orkesterns instrument: Valthornen', 'id': 'CKDDnlCY-dhWAAqiMERd-A', 'description': 'Johan Nordenankar lär oss mer om valthornen, som är ett av de allra äldsta verktygen för att framföra ljud. \nHur gör man för att lära sig blåsa i ett valthorn och varför är det så viktigt att det är synkroniserat med andra instrument? \n\nLängd: 6:38', 'ext': 'mp4'}
	#Test for constructor of KonserthusetPlayIE
	test = KonserthusetPlayIE()
	

# Generated at 2022-06-14 16:37:53.812081
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE(None)
    except:
        assert False
    assert True

# Generated at 2022-06-14 16:38:03.710099
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:38:06.875832
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:15.741094
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    import sys
    from os.path import dirname
    sys.path.append(dirname(dirname(dirname(__file__))))
    from youtube_dl.options import _parse_args
    from youtube_dl.YoutubeDL import YoutubeDL
    konserthuset_play = KonserthusetPlayIE()
    argv = '-u http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'.split()
    args = _parse_args(argv, process_ie_cfg()).__dict__
    args['extractors'] = [konserthuset_play]
    ydl = YoutubeDL(args)

# Generated at 2022-06-14 16:38:22.987827
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    if ie.__class__.__name__ == 'KonserthusetPlayIE':
        print("Unit test for KonserthusetPlayIE is successful")
    else:
        print("Unit test for KonserthusetPlayIE has failed")    

if __name__ == '__main__':
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:33.210544
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Constructor test
    """
    obj = KonserthusetPlayIE()

    assert obj._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:33.853098
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    my_ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:40.331508
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:40:40.297262
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        # The test video belongs to the video id: CKDDnlCY-dhWAAqiMERd-A
        test = KonserthusetPlayIE()._real_extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
        assert test, "should return a dictionary"
    except AssertionError:
        raise AssertionError("test failed: should return a dictionary")

    try:
        assert isinstance(test['id'], unicode), "key id should be a string"
    except AssertionError:
        raise AssertionError("test failed: key id should be a string")


# Generated at 2022-06-14 16:40:41.539070
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE()
    assert k is not None

# Generated at 2022-06-14 16:40:49.379822
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Test constructor of KonserthusetPlayIE
    """
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay'
    assert ie.video_id == 'video_id'
    assert ie.thumbnails == []
    assert ie.title == 'title'
    assert ie.url == 'url'
    assert ie.source_url == 'source_url'
    assert ie.embed_url == 'embed_url'
    assert ie.filesize == 0
    assert ie.uploader == 'uploader'
    assert ie.uploader_id == 'uploader_id'
    assert ie.uploader_url == 'uploader_url'
    assert ie.upload_date == 'upload_date'
    assert ie.license == 'license'

# Generated at 2022-06-14 16:40:50.922397
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Tests whether the class can be instantiated
    ie = KonserthusetPlayIE()
    assert ie is not None

# Generated at 2022-06-14 16:40:54.525693
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()._VALID_URL == KonserthusetPlayIE._VALID_URL
    assert KonserthusetPlayIE()._TESTS == KonserthusetPlayIE._TESTS

# Generated at 2022-06-14 16:40:58.297207
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    if not KonserthusetPlayIE:
        return
    assert KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
                              )._match_id('CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:41:00.084470
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Create instance of class KonserthusetPlayIE
    ie = KonserthusetPlayIE()
    # Call method
    ie.extract()

# Generated at 2022-06-14 16:41:01.198922
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()
    assert True

# Generated at 2022-06-14 16:41:01.978452
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:41:04.384715
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'