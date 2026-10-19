

# Generated at 2022-06-14 16:34:43.267986
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    
# Invokes download method of class InfoExtractor with the url of a video from KonserthusetPlay

# Generated at 2022-06-14 16:34:45.238535
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay'

# Generated at 2022-06-14 16:34:56.625524
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(None)
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.suitable('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert not ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A&t=12345')
    assert not ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A&c=12345')

# Generated at 2022-06-14 16:35:05.769547
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE().download_webpage('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    KonserthusetPlayIE()._match_id('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    KonserthusetPlayIE()._real_extract('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:35:08.531280
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == "KonserthusetPlay"



# Generated at 2022-06-14 16:35:11.300289
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Unit test is used to check the constructor
    # of class KonserthusetPlayIE is not empty
    assert hasattr(KonserthusetPlayIE(), '_real_extract')

# Generated at 2022-06-14 16:35:21.660899
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # This line is needed because tests will be run in a different folder.
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

    from ytdl.extractor.konserthusetplay import KonserthusetPlayIE
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:35:22.902307
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:26.514401
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.extract("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")

# Generated at 2022-06-14 16:35:35.983745
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Unit test for the constructor of class KonserthusetPlayIE.
    """
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    i = KonserthusetPlayIE()

    assert i._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:04.800280
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    # testing add_ie
    ie = KonserthusetPlayIE()
    ie.add_ie(KonserthusetPlayIE)


# Generated at 2022-06-14 16:36:08.838188
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    IE = KonserthusetPlayIE(url, True)

# Generated at 2022-06-14 16:36:11.338876
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    try:
        KonserthusetPlayIE()
    except:
        print('Error: class KonserthusetPlayIE() not initialised')

# Generated at 2022-06-14 16:36:13.971588
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE(None, None)
    except Exception as e:
        assert False, e
    else:
        assert True

# Generated at 2022-06-14 16:36:25.325344
# Unit test for constructor of class KonserthusetPlayIE

# Generated at 2022-06-14 16:36:26.709947
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Assert 1
    KonserthusetPlayIE(None)


# Generated at 2022-06-14 16:36:28.636178
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.name

# Generated at 2022-06-14 16:36:32.865774
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    This is a contructor test. It will check if the class is properly constructed.
    If a constructor test fails, it is likely that the rest of the codes will not work.
    """
    obj=KonserthusetPlayIE()
    print("Constructor test for class KonserthusetPlayIE ----> Passed\n")


# Generated at 2022-06-14 16:36:33.608529
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:45.252929
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert ie._TESTS[0]['md5'] == 'e3fd47bf44e864bd23c08e487abe1967'
    assert ie._TESTS[0]['info_dict']['id'] == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:37:42.277911
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:43.235393
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:45.254931
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE(InfoExtractor)
    assert isinstance(ie, KonserthusetPlayIE)


# Generated at 2022-06-14 16:37:47.816132
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE("CKDDnlCY-dhWAAqiMERd-A")

if __name__ == '__main__':
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:48.839288
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    temp_obj=KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:51.328424
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:37:52.361621
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()


# Generated at 2022-06-14 16:37:53.509388
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE() is not None

# Generated at 2022-06-14 16:38:03.582536
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from zope.interface import implementer, verify
    from zope.interface.verify import BrokenMethodImplementation
    from zope.interface.exceptions import DoesNotImplement
    from zope.interface.exceptions import BrokenImplementation
    from zope.interface.exceptions import BrokenMethodImplementation
    from zope.interface.exceptions import BrokenClassImplementation
    from zope.interface.exceptions import DoesNotImplement
    from zope.interface.exceptions import DoesNotImplement
    from youtube_dl.info import InfoExtractor
    from zope.interface import Interface


    @implementer(Interface)
    class TestableKonserthusetPlayIE(InfoExtractor):
        IE_NAME = 'konserthusetplay'
        _VALID_URL = ''
        _TEST = {}


# Generated at 2022-06-14 16:38:08.181365
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, KonserthusetPlayIE)


# Generated at 2022-06-14 16:39:43.297383
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    inst = KonserthusetPlayIE()
    inst.download('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    inst.download('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    inst.download('https://www.konserthusetplay.se/?m=elWuEH34SMKvaO4wO_cHBw')


# Generated at 2022-06-14 16:39:45.256292
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:39:47.830539
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:39:53.797225
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    m = KonserthusetPlayIE._VALID_URL
    url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    result = m.match(url).group('id')
    assert result is not None
    assert result == 'CKDDnlCY-dhWAAqiMERd-A'

test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:39:55.398854
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert 'KonserthusetPlayIE' == ie.IE_NAME

# Generated at 2022-06-14 16:39:57.575781
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE("null")
    except Exception as e:
        assert False
    else:
        assert True


# Generated at 2022-06-14 16:40:00.563387
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE("KonserthusetPlayIE", "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    pass # No errors

# Generated at 2022-06-14 16:40:08.199938
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    print ("Unit test for class KonserthusetPlayIE")
    test_url1 = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    kp_video1 = KonserthusetPlayIE()
    print (kp_video1._extract_urls(test_url1))
    print (kp_video1._real_extract(test_url1))
    test_url2 = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    kp_video2 = KonserthusetPlayIE()
    print (kp_video2._extract_urls(test_url2))

# Generated at 2022-06-14 16:40:12.211439
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.matches('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    assert ie.matches('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:40:16.055258
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Tests KonserthusetPlayIE.__init__
    ie = KonserthusetPlayIE()
    assert ie.id 
    assert ie.title 
    assert ie.description 
    assert ie.thumbnail 
    assert ie.duration 
    assert ie.formats
    assert ie.subtitles