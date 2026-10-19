

# Generated at 2022-06-14 16:34:50.806257
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    p = KonserthusetPlayIE()
    p.http.request = lambda self, _, __, ___: ("", {})
    p._download_json = lambda self, __, ___, ____: {
        "media": {
            "playerconfig": {
                "title": "myTitle"
            }
        }
    }
    p._real_extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A') # wont work because of p.http.request


# Generated at 2022-06-14 16:34:53.486888
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    inst = KonserthusetPlayIE()
    return inst.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')


# Generated at 2022-06-14 16:34:56.446618
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthusetplayIE = KonserthusetPlayIE()
    assert (str(konserthusetplayIE.__class__) == "<class 'youtube_dl.extractor.konserthusetplay.KonserthusetPlayIE'>")

# Generated at 2022-06-14 16:34:57.677906
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:02.977086
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Note: the test case is taken from
    # https://github.com/rg3/youtube-dl/blob/master/youtube_dl/extractor/konserthusetplay.py
    # For a working URL, there is no point for us to test it
    return KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:04.126632
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:11.780582
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    URLs = [
        ('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'),
        ('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'),
    ]
    for url in URLs:
        try:
            KonserthusetPlayIE() # pylint: disable=W0104
        except:
            assert(False)
    assert(True)

# Generated at 2022-06-14 16:35:21.938903
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie._download_webpage = lambda url, video_id: open(
        'test/data/konserthuset_play.html'
    ).read()

# Generated at 2022-06-14 16:35:23.647291
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()


# Generated at 2022-06-14 16:35:30.597545
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    regex = KonserthusetPlayIE._VALID_URL
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert re.search(regex, url) is not None
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    assert video_id == ie._match_id(url)

# Generated at 2022-06-14 16:35:59.716450
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:09.431669
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    inst = KonserthusetPlayIE()
    assert inst._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:13.104208
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert hasattr(ie, '_VALID_URL') == True
    assert hasattr(ie, '_download_webpage') == True

# Generated at 2022-06-14 16:36:14.595877
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj

# Generated at 2022-06-14 16:36:26.054649
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == 'https?://(?:www\\.)?(?:konserthusetplay|rspoplay)\\.se/\\?.*\\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:32.412878
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'KonserthusetPlay'
    #assert ie.supported_extensions() == ['flv','mp4','m3u8','mp3','webm','ogg','ogv','m4a']
    #assert ie.supported_domains() == ['rspoplay.se','konserthusetplay.se']

# Generated at 2022-06-14 16:36:34.684009
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Just verify that the code can be executed for testing purposes
    KonserthusetPlayIE(None)

if __name__ == '__main__':
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:35.504554
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:47.880643
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    q = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert q.url_result == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert q.url_title == 'Orkesterns instrument: Valthornen'
    assert q.url_description == 'Valthornen är inte bara en av orkesterns största instrument, de är också färgstarka och kraftfulla. Hur skapas valthornstonen? Och hur demoleras en valthorn?'

# Generated at 2022-06-14 16:36:52.034915
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    IE = KonserthusetPlayIE()
    assert IE._VALID_URL == IE._VALID_URL
    assert IE._TESTS == KonserthusetPlayIE._TESTS

# Generated at 2022-06-14 16:37:39.709881
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()




# Generated at 2022-06-14 16:37:49.042589
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:38:00.980180
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.get_id() == 'konserthusetplay'
    assert ie.get_name() == 'KonserthusetPlay'
    assert ie.get_description() == 'Världens musik tillgänglig dygnet runt'
    assert ie.get_pattern() == r'^https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/.+?\bm=.+?$'
    assert ie.get_regex() == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:38:07.018895
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
	params = {
		'url': url,
		'id': 'CKDDnlCY-dhWAAqiMERd-A',
		'video_id': 'CKDDnlCY-dhWAAqiMERd-A',
		'ext': 'mp4',
		'title': 'Orkesterns instrument: Valthornen',
		'description': 'md5:f10e1f0030202020396a4d712d2fa827',
		'thumbnail': 're:^https?://.*$',
		'duration': 398.76,
	}
	result = KonserthusetPlayIE()._real_

# Generated at 2022-06-14 16:38:12.380482
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE('http://www.konserthusetplay.se')
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    k.extract_info(url)
    assert k.extractor_key == 'KonserthusetPlay'

# Generated at 2022-06-14 16:38:18.787454
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    tester = KonserthusetPlayIE()
    assert tester.ie_key() == 'KonserthusetPlay'
    assert tester.ie_obj.ie_key() == 'KonserthusetPlay'
    assert tester._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert tester._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert tester._TESTS[0]['md5'] == 'e3fd47bf44e864bd23c08e487abe1967'
    assert tester._T

# Generated at 2022-06-14 16:38:19.771276
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie_object = KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:20.687201
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE

# Generated at 2022-06-14 16:38:30.332160
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    jstr = ie._download_webpage("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A", 'CKDDnlCY-dhWAAqiMERd-A')
    e = ie._search_regex(r'https?://csp\.picsearch\.com/rest\?.*\be=(.+?)[&"\']', jstr, 'e')

# Generated at 2022-06-14 16:38:33.061865
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # url: url for konserthusetplay
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    # creating instance of KonserthusetPlayIE using constructor
    instance = KonserthusetPlayIE()
    # extracting info from url and saving it in info_dict
    # info_dict contains information about video
    info_dict = instance._real_extract(url)
    assert info_dict is not None


# Generated at 2022-06-14 16:39:28.383511
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:39:32.860237
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert (ie.IE_NAME == 'konserthusetplay:play')
    assert (ie.IE_DESC == 'Rikskonserter Play')
    assert (ie._VALID_URL == KonserthusetPlayIE._VALID_URL)

# Generated at 2022-06-14 16:39:34.444358
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        ie = KonserthusetPlayIE()
    except Exception:
        assert False
    assert True

# Generated at 2022-06-14 16:39:42.344656
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Unit test for constructor of class KonserthusetPlayIE
    """
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay', ie.ie_key()
    assert ie.ie_key() == ie.IE_NAME, ie.ie_key()
    assert ie.IE_NAME == 'konserthusetplay', ie.IE_NAME
    assert ie.IE_DESC == 'Konserthuset play', ie.IE_DESC
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)', ie.VALID_URL


# Generated at 2022-06-14 16:39:43.816854
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie is not None


# Generated at 2022-06-14 16:39:47.601785
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE()
    ie.extract(url)
    assert(ie.is_valid())

# Generated at 2022-06-14 16:39:50.244656
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test case for valid url
    KonserthusetPlayIE(KonserthusetPlayIE._VALID_URL, KonserthusetPlayIE._TESTS)

# Generated at 2022-06-14 16:39:51.580585
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()


# Generated at 2022-06-14 16:39:53.960761
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.info_extractors
    assert ie.extractor_key == 'KonserthusetPlay'

# Generated at 2022-06-14 16:40:02.533370
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
	assert KonserthusetPlayIE()._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:42:22.264303
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:42:23.583304
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE()
    try:
        assert isinstance(instance, InfoExtractor)
    finally:
        pass


# Generated at 2022-06-14 16:42:25.537444
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
  info_extractor = KonserthusetPlayIE('https://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
  print(info_extractor)

# Generated at 2022-06-14 16:42:31.939874
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test initialization
    from ..constructor import ie_keywords
    ie_keywords.append('KonserthusetPlay')
    sample_url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    ie = KonserthusetPlayIE(dict(params=dict(url=sample_url)))
    # Assert that URL provided as argument is used
    assert ie._url == sample_url

# Generated at 2022-06-14 16:42:34.562601
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except:
        assert False, "Unit test for constructor of class KonserthusetPlayIE failed"
    else:
        assert True


# Generated at 2022-06-14 16:42:38.216654
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:42:39.793241
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE(None)
    # I don't know how to properly test this

# Generated at 2022-06-14 16:42:46.033333
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE._download_json = lambda self, url, video_id, transform_source: '{}'

    url = ('http://www.konserthusetplay.se/?'
           'm=CKDDnlCY-dhWAAqiMERd-A')

    ie = KonserthusetPlayIE(url)
    assert ie.url == url
    assert ie.video_id == 'CKDDnlCY-dhWAAqiMERd-A'
    assert ie.title == ''
    assert ie.description == ''
    assert ie.thumbnail == ''
    assert ie.duration == ''
    assert ie.subtitles == ''

# Generated at 2022-06-14 16:42:56.814513
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    # Arrange
    url = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    info_dict = {
        'id': 'elWuEH34SMKvaO4wO_cHBw',
        'ext': 'mp4',
        'title': 'Konsert med Gun-Britt Sundström 18 april 2015',
        'description': 'md5:3f8bd3ca68ae3d3d1f4b3c4647f4d4f4',
        'thumbnail': 're:^https?://.*$',
        'duration': 5313.36,
    }
    video_id = 'elWuEH34SMKvaO4wO_cHBw'

# Generated at 2022-06-14 16:43:05.353821
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    assert KonserthusetPlayIE.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert KonserthusetPlayIE.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')

    #TODO: make this test possible by extracting it to a separate static method
    #assert ie._match