

# Generated at 2022-06-14 16:34:44.224281
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie

# Generated at 2022-06-14 16:34:46.936889
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
        return True
    except:
        return False

# Generated at 2022-06-14 16:34:49.034854
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Instantiate the KonserthusetPlayIE class"""
    class_inst = KonserthusetPlayIE()

# Generated at 2022-06-14 16:34:52.822547
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    i = KonserthusetPlayIE()
    assert i
    assert callable(i.suitable)
    assert callable(i.extract)
    assert callable(i._real_extract)
    assert callable(i._match_id)

# Generated at 2022-06-14 16:34:56.354179
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Check that the constructor of class KonserthusetPlayIE works
    """

    ie = KonserthusetPlayIE()

    # Check that it is an instance of the correct class
    assert(isinstance(ie, KonserthusetPlayIE))


# Generated at 2022-06-14 16:35:08.963701
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    i = 0
    inp = 'Metallica: Nothing else matters'
    exp = 'Metallica: Nothing else matters'
    print('Test: ',str(i),'input: ',inp,'expected: ',exp)
    assert exp == inp
    i += 1
    inp = 'Metallica: Nothing else matters(Live in Paris,France,1992)'
    exp = 'Metallica: Nothing else matters'
    print('Test: ',str(i),'input: ',inp,'expected: ',exp)
    assert exp == inp
    i += 1
    inp = 'Metallica - Seek & destroy (Live In Paris,France,1992)'
    exp = 'Metallica: Seek & destroy'
    print('Test: ',str(i),'input: ',inp,'expected: ',exp)

# Generated at 2022-06-14 16:35:13.454695
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    o = KonserthusetPlayIE()
    o.extract(url)
    # assert o.extract(url) == True

# Generated at 2022-06-14 16:35:20.881029
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A') is True, \
        'KonserthusetPlayIE should be suitable for this URL'
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw') is True, \
        'KonserthusetPlayIE should be suitable for this URL'

# Generated at 2022-06-14 16:35:23.840252
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert str(ie) == type(ie).__name__
    assert ie.IE_NAME == 'KonserthusetPlay'

# Generated at 2022-06-14 16:35:26.109389
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE(None)
    assert obj != None


# Generated at 2022-06-14 16:35:56.204719
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except:
        assert False, "Unit test for constructor of class KonserthusetPlayIE failed"
    assert True, "Unit test for constructor of class KonserthusetPlayIE passed"


# Generated at 2022-06-14 16:36:01.027071
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE(url)
    assert ie.extractor.__class__.__name__ == 'KonserthusetPlayIE'


# Generated at 2022-06-14 16:36:02.815609
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('KonserthusetPlayIE', 'konserthusetplay.se')

# Generated at 2022-06-14 16:36:05.546610
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # given
    url = 'http://someurl/'
    # when
    kp = KonserthusetPlayIE()
    # then
    assert kp is not None

# Generated at 2022-06-14 16:36:09.935549
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("https://www.konserthusetplay.se/?p=video&id=3125")
    if ie.__class__.__name__ == 'KonserthusetPlayIE':
        print("Unit test for KonserthusetPlayIE passed.")
    else:
        print("Unit test for KonserthusetPlayIE failed.")


# Generated at 2022-06-14 16:36:13.543559
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:36:15.033625
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert hasattr(KonserthusetPlayIE, '_VALID_URL') == True

# Generated at 2022-06-14 16:36:21.380957
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE()
    result = k._download_webpage('https://www.konserthusetplay.se/?m=akx1CeHwY_jOAkfRVuTVhXHZiV3sDt2a', '')
    assert result == "<!DOCTYPE html>\n<html><head><title>Videoplayer</title></head></html>"

# Generated at 2022-06-14 16:36:24.174360
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthuset_play_ie = KonserthusetPlayIE()
    assert konserthuset_play_ie is not None


# Generated at 2022-06-14 16:36:34.195536
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None, None)
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:01.690311
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, KonserthusetPlayIE)

# Generated at 2022-06-14 16:37:06.015697
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Check the instance is created
    inst = KonserthusetPlayIE(None)

    # Check for URL regular expression
    assert (inst._VALID_URL ==
            r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')


# Generated at 2022-06-14 16:37:07.755190
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    instance = KonserthusetPlayIE(InfoExtractor())
    assert isinstance(instance, InfoExtractor)

# Generated at 2022-06-14 16:37:19.092486
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kp_ie = KonserthusetPlayIE()
    match_id = kp_ie._match_id
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    video_id = match_id(url)
    assert video_id == 'CKDDnlCY-dhWAAqiMERd-A'
    video_id = match_id('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert video_id == 'elWuEH34SMKvaO4wO_cHBw'
    url_or_none = kp_ie._url_or_none

# Generated at 2022-06-14 16:37:27.610105
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test case : http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    obj = KonserthusetPlayIE()
    obj._VALID_URL = obj.VALID_URL
    obj._download_webpage = lambda url: '<html>'
    obj._extract_m3u8_formats = lambda a, b, c, d, e, f: 'hls'

# Generated at 2022-06-14 16:37:32.006409
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, '_download_webpage')
    assert hasattr(ie, '_search_regex')
    assert hasattr(ie, '_match_id')
    assert hasattr(ie, '_real_extract')

# Generated at 2022-06-14 16:37:41.640164
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # TODO: specify a test case for this class
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    info_dict = {
            'id': 'CKDDnlCY-dhWAAqiMERd-A',
            'ext': 'mp4',
            'title': 'Orkesterns instrument: Valthornen',
            'description': 'md5:f10e1f0030202020396a4d712d2fa827',
            'thumbnail': 're:^https?://.*$',
            'duration': 398.76,
        }

# Generated at 2022-06-14 16:37:44.846791
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    if __name__ == "__main__":
        konserthusetPlayIE_obj = KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:49.118913
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = InfoExtractor("KonserthusetPlay", "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert ie.ie_key() == "KonserthusetPlay"
    assert ie.suitable("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")



# Generated at 2022-06-14 16:37:56.834979
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj._TESTS[0]['url'] == "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    assert obj._TESTS[1]['url'] == 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'

test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:59.395998
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # You can add your own URL of a Konserthuset video
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:39:05.071658
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthusetplay_ie = KonserthusetPlayIE()
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    id = konserthusetplay_ie._match_id(url)
    assert id == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:39:13.987933
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:17.144782
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE(): 
    ie = KonserthusetPlayIE()
    assert ie is not None
    assert ie._VALID_URL is not None
    assert ie._TESTS is not None

# Generated at 2022-06-14 16:39:21.736381
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
  match = KonserthusetPlayIE._VALID_URL.match('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
  assert match
  assert match.group('id') == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:39:28.646968
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE._VALID_URL.pattern == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:39:30.690197
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthusetplay = KonserthusetPlayIE()
    return konserthusetplay

# Generated at 2022-06-14 16:39:32.105835
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None

# Generated at 2022-06-14 16:39:36.361493
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
        info_extractor = KonserthusetPlayIE()
        assert info_extractor._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
        

# Generated at 2022-06-14 16:39:40.525918
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    if ((ie.EXT_REGEX == r'https?://csp\.picsearch\.com/rest\?.*\be=(.+?)[&"\']')
        and (ie.FORMAT_ID_REGEX == r'_([^_]+)_h264m\.mp4')):
        return 1
    else:
        return 0

# Generated at 2022-06-14 16:40:59.112468
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    a = KonserthusetPlayIE({})
    assert(isinstance(a,InfoExtractor))

# Generated at 2022-06-14 16:41:06.723286
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:41:10.755164
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE(KonserthusetPlayIE._VALID_URL)

    assert obj.url == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:41:16.121757
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:41:20.205013
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    # Test invalid URLs
    assert ie.suitable('https://www.google.com/') == False, 'Suitable for invalid URLs'
    assert ie.suitable('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A') == True, 'Suitable for valid URLs'

# Generated at 2022-06-14 16:41:27.472655
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kpi = KonserthusetPlayIE()
    assert kpi._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:41:29.082955
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
  assert KonserthusetPlayIE() is not None



# Generated at 2022-06-14 16:41:30.613304
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()


# Generated at 2022-06-14 16:41:32.482402
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    # Check if IE constructs without error
    KonserthusetPlayIE()



# Generated at 2022-06-14 16:41:40.124734
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE()
    ie._download_webpage = lambda url: '<a href="http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"></a>'
    ie._search_regex = lambda pattern, string, name, default=None, fatal=True:\
        'test'
    ie._download_json = lambda url, video_id: {'e': 'test'}
    ie._real_extract(url)

# Generated at 2022-06-14 16:43:58.842932
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from .common import FakeYDL   # Only for unit test

    FakeYDL()._test_extract({
        'url': 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A',
        'only_matching': True
    })

# Generated at 2022-06-14 16:44:03.050055
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    info_extractor = KonserthusetPlayIE()
    assert (info_extractor.IE_NAME == 'konserthusetplay')
    assert (info_extractor.IE_DESC == 'Konserthuset Play')
    assert (info_extractor._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)')
    assert (info_extractor._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:44:04.245951
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie

# Generated at 2022-06-14 16:44:06.010627
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    kp = KonserthusetPlayIE()
    assert kp is not None

# Generated at 2022-06-14 16:44:13.139503
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    konserthuset_play_ie = KonserthusetPlayIE()
    assert konserthuset_play_ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert konserthuset_play_ie.IE_NAME == 'konserthusetplay:play'

# Generated at 2022-06-14 16:44:13.927747
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:44:16.117428
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    extractor_object = KonserthusetPlayIE()
    assert extractor_object.ie_key() == "KonserthusetPlay"

# Generated at 2022-06-14 16:44:17.169008
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test empty constructor
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:44:19.724629
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Simple unit test
    """
    kpIE = KonserthusetPlayIE()
    kpIE._match_id("http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw")

# Generated at 2022-06-14 16:44:20.555004
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE("jflks")