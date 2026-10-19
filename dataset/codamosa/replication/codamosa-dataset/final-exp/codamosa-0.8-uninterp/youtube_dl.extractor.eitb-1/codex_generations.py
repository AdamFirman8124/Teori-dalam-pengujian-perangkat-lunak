

# Generated at 2022-06-14 16:03:08.523167
# Unit test for constructor of class EitbIE
def test_EitbIE():
    vie = EitbIE()
    assert vie.IE_NAME == "eitb.tv"
    assert vie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:18.572919
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Unit test method.
    """
    ie = EitbIE()
    assert ie._VALID_URL == "https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)"
    info = ie._real_extract(ie._TEST['url'])
    assert ie.IE_NAME == 'eitb.tv'
    assert info['id'] == '4090227752001'
    assert info['title'] == '60 minutos (Lasa y Zabala, 30 años)'
    assert info['formats'][0]['format_id'] == 'http-2048'

# Generated at 2022-06-14 16:03:19.678273
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE()._test_class

# Generated at 2022-06-14 16:03:29.651283
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .common import _TEST_HEADERS, QueryDict
    from .common import _TEST_MULTIWEBTV_VIDEO_ID_RESULTS as _TEST_RESULTS

    ie = EitbIE({'headers': _TEST_HEADERS,
                 'multimedia_url': 'http://multimedia.eitb.tv/multimedia/',
                 'token_auth_url': 'http://mam.eitb.eus/mam/REST/ServiceMultiweb/DomainRestrictedSecurity/TokenAuth/'})
    ie.extract(QueryDict(ie.multimedia_url + ie.token_auth_url + '?id=' + _TEST_RESULTS['id']))


# Generated at 2022-06-14 16:03:39.246457
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == "eitb.tv"
    assert ie._VALID_URL == "https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)"

# Generated at 2022-06-14 16:03:41.477791
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.get_info('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')['id'] == '4090227752001'

# Generated at 2022-06-14 16:03:44.295325
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from .test_json_urls import json_urls
    for url, id in json_urls:
        test_EitbIE.__name__ = 'test_%s' % id
        yield check_json_url, url, id

# Generated at 2022-06-14 16:03:54.609148
# Unit test for constructor of class EitbIE
def test_EitbIE():
    IE = EitbIE.IE_NAME
    obj = EitbIE()
    assert obj.ie_key() == IE, 'IE key does not match expected value'
    assert obj.IE_NAME == IE, 'IE name does not match expected value'
    assert obj.ie_key() in globals(), \
        'global variable "%s" is not present' % obj.ie_key()
    assert obj.test() is None, 'No test function found'
    assert obj._VALID_URL == 'https?://(?:www\\.)?eitb\\.tv/(?:eu/bideoa|es/video)/[^/]+/\\d+/(?P<id>\\d+)', \
        'URL format does not match expected value'

# Generated at 2022-06-14 16:03:56.246881
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = InfoExtractor(EitbIE.IE_NAME)

# Generated at 2022-06-14 16:03:58.534136
# Unit test for constructor of class EitbIE
def test_EitbIE():

    with pytest.raises(ValueError):
        EitbIE(None, None, None)

# Generated at 2022-06-14 16:04:10.085730
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:12.001722
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    ie.IE_NAME
    ie._VALID_URL
    ie._TEST

# Generated at 2022-06-14 16:04:17.969535
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Test class EitbIE.
    """
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:19.043540
# Unit test for constructor of class EitbIE
def test_EitbIE():
    return EitbIE();

# Generated at 2022-06-14 16:04:24.271780
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/eu/bideoa/6-minutuak/4104995132001/4090227752001/lasa-y-zabala-30-urte/'

    ie = EitbIE()
    assert ie.match(url) == True
    ie.parse(url)

# Generated at 2022-06-14 16:04:32.046752
# Unit test for constructor of class EitbIE
def test_EitbIE():
    f = EitbIE()
    assert f._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert f._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'

# Generated at 2022-06-14 16:04:33.926204
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbie = EitbIE()
    assert eitbie != None


# Generated at 2022-06-14 16:04:41.207828
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert(eitb.IE_NAME == 'eitb.tv')
    assert(eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')
    assert(eitb._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert(eitb._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998')

# Generated at 2022-06-14 16:04:45.752764
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_IE = EitbIE()
    assert eitb_IE.ie_key() == 'eitb.tv'
    assert eitb_IE.ie_name() == 'eitb.tv'
    assert eitb_IE.ie_version() == '1.0'

# Generated at 2022-06-14 16:04:47.445422
# Unit test for constructor of class EitbIE
def test_EitbIE():
    c = EitbIE()
    assert c is not None

# Generated at 2022-06-14 16:05:06.964148
# Unit test for constructor of class EitbIE
def test_EitbIE():
    testcase = dict(
    	url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/",
        md5 = "edf4436247185adee3ea18ce64c47998",
        info_dict = dict(
            id = "4090227752001",
            ext = "mp4",
            title = "60 minutos (Lasa y Zabala, 30 años)",
            description = "Programa de reportajes de actualidad.",
            duration = 3996.76,
            timestamp = 1381789200,
            upload_date = "20131014",
            tags = list,
        ),
    )
   

# Generated at 2022-06-14 16:05:16.057925
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    # Check for ie.IE_NAME
    assert ie.IE_NAME == 'eitb.tv'
    # Check for _VALID_URL
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    # Check for _TEST

# Generated at 2022-06-14 16:05:24.974867
# Unit test for constructor of class EitbIE
def test_EitbIE():
    import sys
    sys.path.append("/Users/bren/Documents/repo/YTDL/YTDL") #os.pardir = .. 
    sys.path.append("/Users/bren/Documents/repo/YTDL/YTDL/extractor") #os.pardir = .. 
    from ..compat import compat_parse_qs
    EitbIE(compat_parse_qs(['http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/']))

# Generated at 2022-06-14 16:05:26.863711
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test constructor of EitbIE
    result = EitbIE()
    assert result.IE_NAME in globals()

# Generated at 2022-06-14 16:05:27.948141
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE(InfoExtractor())

# Generated at 2022-06-14 16:05:34.613520
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    inputs = ["http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"]
    expected_id = "4090227752001"

    for url in inputs:
        a = ie._match_id(url)
        assert a == expected_id


# Generated at 2022-06-14 16:05:36.213856
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE('http://example.com').IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:05:37.415400
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == EitbIE._VALID_URL

# Generated at 2022-06-14 16:05:40.907823
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test class of EitbIE"""
    from inspect import isclass
    # check if the class is declared
    assert isclass(EitbIE)
    # create object to call methods.
    obj = EitbIE()
    # call method _real_extract() of class EitbIE
    obj._real_extract("url")

# Generated at 2022-06-14 16:05:46.294239
# Unit test for constructor of class EitbIE
def test_EitbIE():
	y = EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")
	assert y.IE_NAME == "eitb.tv"


# Generated at 2022-06-14 16:06:19.009957
# Unit test for constructor of class EitbIE
def test_EitbIE():

    args = (1, 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert args == EitbIE._TEST.items()

# Generated at 2022-06-14 16:06:29.195967
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, 'IE_DESC')
    assert hasattr(ie, 'IE_NAME')
    assert hasattr(ie, '_TEST')
    assert hasattr(ie, '_download_webpage_handle')
    assert hasattr(ie, '_download_webpage')
    assert hasattr(ie, '_download_json')
    assert hasattr(ie, '_download_xml')
    assert hasattr(ie, '_html_search_regex')
    assert hasattr(ie, '_html_search_meta')
    assert hasattr(ie, '_html_search_meta_regex')
    assert hasattr(ie, '_html_search_schema')

# Generated at 2022-06-14 16:06:32.696092
# Unit test for constructor of class EitbIE
def test_EitbIE():
    import unittest
    test = unittest.makeSuite(EitbIE)
    runner = unittest.TextTestRunner()
    runner.run(test) 

# Generated at 2022-06-14 16:06:38.789972
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    # _TEST is not a class member so there is no need to check it


# Generated at 2022-06-14 16:06:41.675017
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    expected_id = "4090227752001"
    ie = EitbIE()
    assert True == ie._match_id(url)
    assert expected_id == ie._match_id(url)

# Generated at 2022-06-14 16:06:43.301315
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test to make sure it doesn't crash when trying to use it
    EitbIE()

# Generated at 2022-06-14 16:06:44.519530
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    ie.IE_NAME

# Generated at 2022-06-14 16:06:54.327378
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/eu/bideoak/irratia/100-irratia-euskal-herrira/14/308640/')
    i = ie._real_extract('http://www.eitb.tv/eu/bideoak/irratia/100-irratia-euskal-herrira/14/308640/')
    assert i['title'] == '100 irratia euskal herrira (Euskal herriko erakundeen babesa)'
    assert i['description'] == 'Euskal herriko erakundeen babesa'
    assert i['id'] == '308640'

# Generated at 2022-06-14 16:07:03.080546
# Unit test for constructor of class EitbIE
def test_EitbIE():
  ie = EitbIE(None)
  assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
  assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
  assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2022-06-14 16:07:09.619585
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/','EitbIE','http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:08:34.948358
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:08:36.091746
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:08:36.748113
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE

# Generated at 2022-06-14 16:08:37.697341
# Unit test for constructor of class EitbIE
def test_EitbIE():
    constructor_test(EitbIE)

# Generated at 2022-06-14 16:08:39.744568
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    oe = EitbIE()
    assert ie is oe

test_EitbIE()

# Generated at 2022-06-14 16:08:50.132955
# Unit test for constructor of class EitbIE
def test_EitbIE():
    '''
    Unit test for constructor of class EitbIE.
    '''
    url = 'http://www.eitb.tv/eu/bideoa/gaztelaniaz-etorri/34734/'
    MyEitbIE = EitbIE()
    assert MyEitbIE._VALID_URL == '''https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'''

# Generated at 2022-06-14 16:08:51.560580
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:08:53.644837
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert 'EitbIE' == EitbIE().IE_NAME


# Generated at 2022-06-14 16:08:54.325148
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:09:04.606460
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # some valid test urls for eitb.tv
    testurls=[
        'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    ]
    res = EitbIE.suitable(testurls[0])
    if not res:
        print("URL %s is not suitable for class EitbIE"%(testurls[0]))
    else:
        print("URL %s is suitable for class EitbIE"%(testurls[0]))

if __name__ == "__main__":
    # run all unit tests
    test_EitbIE()

# Generated at 2022-06-14 16:10:43.378908
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:10:44.503027
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == EitbIE._VALID_URL

# Generated at 2022-06-14 16:10:47.551192
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Unit test for constructor of class EitbIE
    """
    eitb = EitbIE()
    assert eitb.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:10:49.040578
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE(True)


# Generated at 2022-06-14 16:10:57.966328
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie.IE_NAME == 'eitb.tv'
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert eitb_ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert eitb_ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2022-06-14 16:11:01.020774
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == 'eitb.tv'
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:11:03.905646
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == 'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:11:10.171786
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    ie_u = ie.url_result("http://www.eitb.tv/traductor/")
    result = ie._real_extract("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")

# Generated at 2022-06-14 16:11:11.771741
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:11:14.118376
# Unit test for constructor of class EitbIE
def test_EitbIE():
    a = EitbIE()
    assert a.IE_NAME == 'eitb.tv'
    return
