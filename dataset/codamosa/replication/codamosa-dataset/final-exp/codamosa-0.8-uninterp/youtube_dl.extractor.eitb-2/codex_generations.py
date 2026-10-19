

# Generated at 2022-06-14 16:03:12.986093
# Unit test for constructor of class EitbIE
def test_EitbIE():
	u = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
	e = EitbIE()
	assert e._download_json(
		"http://mam.eitb.eus/mam/REST/ServiceMultiweb/Video/MULTIWEBTV/%s/" % e._match_id(u),
		e._match_id(u), 'Downloading video JSON') == {
			u'errorCode': u'1',
			u'errorDescription': u'Error',
			u'success': False
		}


# Generated at 2022-06-14 16:03:14.913390
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert isinstance(eitb, InfoExtractor)

# Generated at 2022-06-14 16:03:19.166669
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE()
    assert eitbIE.IE_NAME == 'eitb.tv'
    assert eitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:03:21.009037
# Unit test for constructor of class EitbIE
def test_EitbIE():
	try:
		EitbIE()
	except:
		assert False

# Generated at 2022-06-14 16:03:21.767889
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:03:26.839980
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert(eitb.IE_NAME == 'eitb.tv')
    assert(eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')


# Generated at 2022-06-14 16:03:28.742507
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE(None) is not None


# Generated at 2022-06-14 16:03:29.837914
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()

# Generated at 2022-06-14 16:03:33.657650
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        assert EitbIE
    except NameError:
        print('NameError raised, EitbIE still not implemented!')
    else:
        print('All clear!')



# Generated at 2022-06-14 16:03:38.317176
# Unit test for constructor of class EitbIE
def test_EitbIE():
    
    # Valid URL
    url= "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    ied = EitbIE()
    assert ied.ie_key() == 'Eitb'
    assert ied.suitable(url)

    # Invalid URL
    url= "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos.html"
    assert not ied.suitable(url)

# Generated at 2022-06-14 16:03:52.524428
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE(None).IE_NAME == 'EitbTV'

# Generated at 2022-06-14 16:03:54.198630
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        assert EitbIE
    except NameError:
        assert False
    return True

# Generated at 2022-06-14 16:04:01.757069
# Unit test for constructor of class EitbIE
def test_EitbIE():
	arguments = ['http://www.eitb.tv/eu/bideoa/60-minutos/4104995148001/60-minutos-2013-2014/lasa-y-zabala-30-anos/'];
	assert (EitbIE._VALID_URL in EitbIE._TEST.url), "EitbIE: Wrong URL format"
	assert (EitbIE._TEST.url == arguments[0]), "EitbIE: Wrong argument 'url'"

# Generated at 2022-06-14 16:04:06.939333
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    result = dict(eitb.extract(url))
    assert result["id"] == "4090227752001"


# Generated at 2022-06-14 16:04:09.815619
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert(eitb_ie.IE_NAME == 'eitb.tv')

# Generated at 2022-06-14 16:04:11.616050
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE()
    assert IE.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:04:23.631367
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    # test valid URL is correctly recognized
    assert ie.suitable('something') == False
    assert ie.suitable(
        'http://www.eitb.tv/eu/bideoa/eitb-laburpena/15774/fernando-torres-la-fuerza-de-vencer/') == True
    assert ie.suitable('http://www.eitb.tv/eu/bideoa/eitb-laburpena/15774/fernando-torres-la-fuerza-de-vencer/') == True

    # test valid URL is correctly extracted

# Generated at 2022-06-14 16:04:24.885829
# Unit test for constructor of class EitbIE
def test_EitbIE():
    t = EitbIE();
    assert t.IE_NAME == "eitb.tv"

# Generated at 2022-06-14 16:04:35.561572
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # pylint: disable=redefined-outer-name
    eitb = EitbIE()

# Generated at 2022-06-14 16:04:39.171017
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE()
    assert e.IE_NAME == 'eitb.tv'
    assert e._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:06.746128
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert (eitb.IE_NAME == 'eitb.tv')

# Generated at 2022-06-14 16:05:09.636187
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:11.206179
# Unit test for constructor of class EitbIE
def test_EitbIE():
    instance = EitbIE()
    assert instance is not None

# Generated at 2022-06-14 16:05:20.741264
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()

    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:25.023696
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Unit test for constructor of class EitbIE"""
    instEitb = EitbIE()
    instEitb.IE_NAME = 'eitb.tv'
    assert instEitb.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:05:28.510068
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE("http://www.eitb.tv/eu/bideoa/hitza-kalean/4065342063001/")
    assert IE.get_name() == 'EitbIE'

# Generated at 2022-06-14 16:05:38.479827
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:05:42.767789
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE("EitbIE")._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:05:54.042929
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE_eitb = EitbIE()

# Generated at 2022-06-14 16:06:03.143546
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    video_id = '4090227752001'
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    # Test constructor
    assert ie._VALID_URL is not None
    assert ie._TEST['url'] is not None
    assert ie._TEST['md5'] is not None
    # Test the extraction of url with the function _real_extract
    ie._real_extract(url)
    # Test the correct work of the _real_extract function, by comparing the md5 hash of the result, with the one saved in the _TEST value

# Generated at 2022-06-14 16:07:01.414314
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        contructor = EitbIE()
    except Exception as e:
        print(e)
        return 1
    return 0


# Generated at 2022-06-14 16:07:02.754650
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE(None, None)


# Generated at 2022-06-14 16:07:12.741317
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert eitb_ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert eitb_ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert eitb_ie._TEST['info_dict']['id']

# Generated at 2022-06-14 16:07:13.484443
# Unit test for constructor of class EitbIE
def test_EitbIE():
    test_dict=EitbIE()
    assert test_dict == "EitbIE"

# Generated at 2022-06-14 16:07:16.516915
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:07:16.992229
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:07:22.381767
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:07:32.160093
# Unit test for constructor of class EitbIE
def test_EitbIE():
    input_url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    expected_url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    expected_video_id = '4090227752001'

# Generated at 2022-06-14 16:07:34.320083
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == EitbIE._VALID_URL

# Generated at 2022-06-14 16:07:39.073917
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:10:16.529114
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE()
    assert IE.IE_NAME == "Eitb"

# Test for EitbIE._real_extract

# Generated at 2022-06-14 16:10:19.277796
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE();
    assert ie.IE_NAME == 'eitb.tv';
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)';

# Generated at 2022-06-14 16:10:27.001800
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Create object of class EitbIE
    _eitbie = EitbIE();

    # Get url object
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

    print(_eitbie._TEST)

    # Check if video is downloaded
    _eitbie._download_webpage(url, None, note='Downloading page', errnote='Failed to download page');

    # Get video id
    video_id = _eitbie._match_id(url);

    # Get video info

# Generated at 2022-06-14 16:10:28.484480
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()


# Generated at 2022-06-14 16:10:29.673702
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert isinstance(EitbIE(), EitbIE)

# Generated at 2022-06-14 16:10:38.147495
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Constructor test
    ie = EitbIE(EitbIE.IE_NAME, EitbIE._VALID_URL)
    assert ie.ie_key() == EitbIE.IE_NAME, 'Ie key should be %s' % EitbIE.IE_NAME
    assert ie.ie_key() != 'Eitb', 'Ie key should not be "Eitb"'
    assert ie.ie_key() != 'Eitb.tv', 'Ie key should not be "Eitb.tv"'
    assert ie.ie_key() != 'Eitb.tv/eu/bideoa', 'Ie key should not be "Eitb.tv/eu/bideoa"'

# Generated at 2022-06-14 16:10:44.061152
# Unit test for constructor of class EitbIE
def test_EitbIE():
    '''
    Test EitbIE class object initialization.

    This test is not really doing anything, but it invokes the __init__ method
    as this is the required format for unit tests.

    This is also a tutorial for how to test your custom extractors:
    https://github.com/rg3/youtube-dl/blob/master/README.md#testing-your-extractor
    '''
    _EitbIE = EitbIE()


if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:10:46.056819
# Unit test for constructor of class EitbIE
def test_EitbIE():
    raise Exception("Unit test for constructor of class EitbIE not implemented yet")



# Generated at 2022-06-14 16:10:47.006074
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Should not throw exception
    EitbIE()

# Generated at 2022-06-14 16:10:52.108609
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert ie.IE_NAME == 'EitbIE'
