

# Generated at 2022-06-14 17:37:41.359324
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Make sure it accepts only a valid URL
    assert WallaIE.suitable('https://www.walla.co.il/item/2642630') is False
    assert WallaIE.suitable('https://vod.walla.co.il/item/2642630') is False
    assert WallaIE.suitable('https://vod.walla.co.il/movie/2642630/one-direction-all-for-one') is True


# Generated at 2022-06-14 17:37:50.361362
# Unit test for constructor of class WallaIE
def test_WallaIE():
    cls = globals()['WallaIE']
    assert cls.__name__ == 'WallaIE'
    assert cls._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:37:54.610180
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test unittest.
    # Test constructor.
    # Test the object instance.
    # Test for the basic structure of '__dict__'.
    ie = WallaIE()
    ie.download('2670048/twlight-new-moon')


# Generated at 2022-06-14 17:37:57.759185
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:37:58.948350
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:38:02.314873
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert(WallaIE('WallaIE', 'vod.walla.co.il')._VALID_URL ==
        '^https?://vod\.walla\.co\.il/.*$')

# Generated at 2022-06-14 17:38:06.782431
# Unit test for constructor of class WallaIE
def test_WallaIE():
	class_name = WallaIE.__name__
	test_obj = globals()["test_" + class_name]
	obj = globals()[class_name]
	instance = obj(test_obj['url'])
	assert(re.match(instance._VALID_URL, test_obj['url']))

# Generated at 2022-06-14 17:38:12.222685
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE
    obj = ie(None)
    assert ie == WallaIE
    assert obj.ie_key() == 'Walla'
    assert obj.ie_key_short() == 'walla'
    assert obj.extractor_key() == 'Walla'


# Generated at 2022-06-14 17:38:18.515725
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._SUBTITLE_LANGS['עברית'] == 'heb'
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    WallaIE._sort_formats(None)
    WallaIE._real_extract(None)

# Generated at 2022-06-14 17:38:19.962511
# Unit test for constructor of class WallaIE
def test_WallaIE():
	#test case: run the constructor of WallaIE class
	ie = WallaIE()


# Generated at 2022-06-14 17:38:28.120344
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Unit test for constructor of class WallaIE
    """
    # print "Constructor Test\n===================\n"
    test = WallaIE()

# Generated at 2022-06-14 17:38:29.805416
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert isinstance(WallaIE(None, {}), WallaIE)

# Generated at 2022-06-14 17:38:33.673078
# Unit test for constructor of class WallaIE
def test_WallaIE():
	from .common import InfoExtractor
	assert InfoExtractor.ie_key('vod.walla.co.il') == 'walla'


# Generated at 2022-06-14 17:38:35.667125
# Unit test for constructor of class WallaIE
def test_WallaIE():
    c = WallaIE()
    # No assert as the object is difficult to test
    return c

# Generated at 2022-06-14 17:38:43.776127
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.ie_key() == 'Walla'
    assert ie.ie_name() == 'walla'
    assert ie.suitable(None) == False
    assert ie.suitable(url="") == False
    assert ie.suitable(url="http://walla.co.il/tv") == False
    assert ie.suitable(url="http://vod.walla.co.il/movie/2642630/one-direction-all-for-one") == True


# Generated at 2022-06-14 17:38:44.751509
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()

# Generated at 2022-06-14 17:38:56.595117
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    ie = WallaIE({})
    assert ie.suitable(test_url)
    # Check this is a WallaIE by checking the regex
    assert re.search(ie._VALID_URL + '$', test_url)
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    # Check the structure of the dict
    assert len(ie._TEST.keys()) == 5
    assert ie._TEST['url'] == test_url
    assert len(ie._TEST['info_dict'].keys()) == 7
    assert ie

# Generated at 2022-06-14 17:39:05.622749
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:39:07.830959
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie

# Unit tests for get_subtitle_lang() method of class WallaIE

# Generated at 2022-06-14 17:39:11.579550
# Unit test for constructor of class WallaIE
def test_WallaIE():
	extractor = WallaIE("https://walla.co.il")
	return extractor

if __name__ == '__main__':
	print(test_WallaIE())

# Generated at 2022-06-14 17:39:17.622396
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE().IE_NAME == 'Walla'

# Generated at 2022-06-14 17:39:24.311478
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert ie.url == "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    assert ie.suitable("http://vod.walla.co.il/movie/2642630/one-direction-all-for-one")
    assert ie.valid()
    assert ie.display_id == "one-direction-all-for-one"
    assert ie.id == "2642630"

# Generated at 2022-06-14 17:39:26.205124
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.suite()

# Generated at 2022-06-14 17:39:29.954879
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE("test 1", "test 2", "test 3")
    assert (ie.ie_key() == 'Walla')
    assert (ie.video_id == "test 1")

# Generated at 2022-06-14 17:39:39.575963
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert 'WallaIE' == ie.IE_NAME
    assert 'walla.co.il' == ie.IE_DESC
    assert 'walla' == ie.ie_key()
    assert 'walla' in ie.downloader_options()
    assert re.match('https?://vod.walla.co.il/[^/]+/\d+/[^/]+', ie.working_url('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'))
    assert None == ie.working_url('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one-')

# Generated at 2022-06-14 17:39:46.933281
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    test_values = ['http://vod.walla.co.il/movie/2642630/one-direction-all-for-one']

    ie = WallaIE()
    ie.suite()

# Generated at 2022-06-14 17:39:53.872939
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None)
    assert ie._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:04.104046
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE(None, 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie.VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:40:08.373006
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    ie= WallaIE()
    ie._real_extract(url)

# Generated at 2022-06-14 17:40:10.169627
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie = WallaIE('WallaIE')

# Generated at 2022-06-14 17:40:30.237646
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.extractor._VALID_URL = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    ie.extractor._SUBTITLE_LANGS = {
        'עברית': 'heb',
    }
    
    ie.extractor._real_extract(ie.extractor._VALID_URL);

# Generated at 2022-06-14 17:40:41.825503
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'

    ie = WallaIE()
    ie_result = ie.extract(url)

    assert ie_result['id'] == '2642630'
    assert ie_result['display_id'] == 'one-direction-all-for-one'
    assert ie_result['ext'] == 'flv'
    assert ie_result['title'] == 'וואן דיירקשן: ההיסטריה'
    assert ie_result['description'] == 'md5:de9e2512a92442574cdb0913c49bc4d8'

# Generated at 2022-06-14 17:40:51.535327
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert ('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one',
            WallaIE().suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'))
    assert ('http://vod.walla.co.il/movie/2642630/one-direction',
            WallaIE().suitable('http://vod.walla.co.il/movie/2642630/one-direction'))
    assert ('http://vod.walla.co.il/movie/1390082/one-direction-worth-it',
            WallaIE().suitable('http://vod.walla.co.il/movie/1390082/one-direction-worth-it'))

# Generated at 2022-06-14 17:41:00.669397
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    urls = ['http://vod.walla.co.il/movie/2642630/one-direction-all-for-one']

# Generated at 2022-06-14 17:41:06.474105
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE(InfoExtractor())._VALID_URL == 'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert WallaIE(InfoExtractor())._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'


# Generated at 2022-06-14 17:41:07.066214
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE

# Generated at 2022-06-14 17:41:13.028763
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = "http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    w = WallaIE().suitable(url)

# Generated at 2022-06-14 17:41:15.671531
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Test for public constructor
    try:
        o = WallaIE()
    except:
        raise Exception('Failed to construct class WallaIE')
    else:
        return True


# Generated at 2022-06-14 17:41:16.841677
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE()
    assert obj



# Generated at 2022-06-14 17:41:19.638503
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_WallaIE = WallaIE()
    return test_WallaIE

# Generated at 2022-06-14 17:41:32.395791
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.url="http://vod.walla.co.il/movie/2642630/one-direction-all-for-one"
    assert(ie.url) == ('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:41:33.005696
# Unit test for constructor of class WallaIE
def test_WallaIE():
    return WallaIE()

# Generated at 2022-06-14 17:41:36.677040
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    #print obj.__class__
    #print dir(obj)
    #print obj.ext

# Generated at 2022-06-14 17:41:40.708759
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # Testing the extraction of a WallaIE video, with a random URL
    # from the site
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    WallaIE()._real_extract(url)

# Calling the unit-test
if __name__ == '__main__':
    test_WallaIE()

# Generated at 2022-06-14 17:41:44.169813
# Unit test for constructor of class WallaIE
def test_WallaIE():
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    WallaIE()(url)

# Generated at 2022-06-14 17:41:46.074313
# Unit test for constructor of class WallaIE
def test_WallaIE():
    inst = WallaIE()
    assert inst.SUCCESS_TICK == '0:10:12'

# Generated at 2022-06-14 17:41:51.765943
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE(None)

    assert 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one' ==  w._VALID_URL
    assert 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one' ==  w._TEST['url']
    assert 'md5:de9e2512a92442574cdb0913c49bc4d8' ==  w._TEST['info_dict']['description']



# Generated at 2022-06-14 17:42:00.977386
# Unit test for constructor of class WallaIE
def test_WallaIE():
    # The function name is 'test', which is necessary. The test case needs to be defined in the 'test_' folder.
    # This is an example of unit testing in Python. You can use any method to do the unit testing,
    # the unit testing here is only used as a demonstration. This function tests the function of this class.
    # It is highly recommended to write unit tests for IE or extractors.
    # You can get more information on the link below.
    # https://github.com/rg3/youtube-dl/blob/master/README.md#output-template
    # https://github.com/rg3/youtube-dl/tree/master/test
    tester = WallaIE()

# Generated at 2022-06-14 17:42:09.396277
# Unit test for constructor of class WallaIE
def test_WallaIE():
    test_cases = [
        {
            'desc': 'Check that url validation succeeds',
            'url': 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one',
            'passes': True,
        },
        {
            'desc': 'Check that url validation fails',
            'url': 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one/',
            'passes': False,
        },
    ]

    for test_case in test_cases:
        desc = test_case.get('desc')
        url = test_case.get('url')
        passes = test_case.get('passes')
        wallaIE = WallaIE(url)

# Generated at 2022-06-14 17:42:12.207220
# Unit test for constructor of class WallaIE
def test_WallaIE():
    cur_vars = globals().copy()
    for key,value in cur_vars.items():
        print("%s ==> %s" % (key,value))

if __name__ == '__main__':
    test_WallaIE()

# Generated at 2022-06-14 17:42:49.022152
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.IE_NAME == 'walla'
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'
    assert ie._TEST['url'] == 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    assert ie._TEST['info_dict']['id'] == '2642630'
    assert ie._TEST['info_dict']['display_id'] == 'one-direction-all-for-one'
    assert ie._TEST['info_dict']['ext'] == 'flv'

# Generated at 2022-06-14 17:42:57.501796
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.url_re == WallaIE._VALID_URL
    assert ie._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:43:01.349779
# Unit test for constructor of class WallaIE

# Generated at 2022-06-14 17:43:05.697241
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'walla:vod'
    assert ie.VALID_URL == ie._VALID_URL
    assert ie.TEST == ie._TEST

# Generated at 2022-06-14 17:43:06.320192
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()


# Generated at 2022-06-14 17:43:08.358498
# Unit test for constructor of class WallaIE
def test_WallaIE():

    # Check WallaIE constructor
    obj = WallaIE({})
    assert obj.ie_key() == 'Walla'

# Generated at 2022-06-14 17:43:10.202635
# Unit test for constructor of class WallaIE
def test_WallaIE():

    WallaIE('')


# Generated at 2022-06-14 17:43:19.490596
# Unit test for constructor of class WallaIE
def test_WallaIE():
    """
    Comparing the expected result to the real result
    """
    url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
    testWallaIE = WallaIE()
    info = testWallaIE._real_extract(url)

# Generated at 2022-06-14 17:43:20.892649
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.download(URL)

# Generated at 2022-06-14 17:43:25.312912
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert ie.get_info_extractor() is not None



# Generated at 2022-06-14 17:44:35.499354
# Unit test for constructor of class WallaIE
def test_WallaIE():
	url = 'http://vod.walla.co.il/movie/2642630/one-direction-all-for-one'
	ex = WallaIE()
	info = ex._real_extract(url)
	assert info['id'] == '2642630'
	assert info['display_id'] == 'one-direction-all-for-one'
	assert info['ext'] == 'flv'
	assert info['title'] == 'וואן דיירקשן: ההיסטריה'
	assert info['description'] == 'md5:de9e2512a92442574cdb0913c49bc4d8'
	assert info['thumbnail'] == r're:^https?://.*\.jpg'
	assert info['duration'] == 3600

# Generated at 2022-06-14 17:44:37.126952
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert ie.add_ie(ie.ie_key()) == ie



# Generated at 2022-06-14 17:44:46.751628
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    assert re.match(ie._VALID_URL, ie._TEST[ 'url' ])
    info_dict = ie._TEST[ 'info_dict' ]
    assert info_dict[ 'id' ] == '2642630'
    assert info_dict[ 'display_id' ] == 'one-direction-all-for-one'
    assert info_dict[ 'ext' ] == 'flv'
    assert info_dict[ 'title' ] == 'וואן דיירקשן: ההיסטריה'
    assert info_dict[ 'duration' ] == 3600
    assert info_dict[ 'thumbnail' ] == 're:^https?://.*\.jpg'
    assert 'description' in info_dict

# Generated at 2022-06-14 17:44:49.856670
# Unit test for constructor of class WallaIE
def test_WallaIE():
    obj = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one', {})
    assert obj is not None

# Generated at 2022-06-14 17:45:01.062832
# Unit test for constructor of class WallaIE
def test_WallaIE():
    ie = WallaIE()
    ie.suitable('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')

# Generated at 2022-06-14 17:45:01.661531
# Unit test for constructor of class WallaIE
def test_WallaIE():
    WallaIE()

# Generated at 2022-06-14 17:45:03.924814
# Unit test for constructor of class WallaIE
def test_WallaIE():
    w = WallaIE()
    w.add_default_values()
    assert w._SUBTITLE_LANGS['עברית'] == 'heb'

# Generated at 2022-06-14 17:45:11.613004
# Unit test for constructor of class WallaIE
def test_WallaIE():
    IE = WallaIE()
    html = IE.extract('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one')
    assert html['id'] == '2642630'
    assert html['display_id'] == 'one-direction-all-for-one'
    assert html['ext'] == 'flv'
    assert html['title'] == 'וואן דיירקשן: ההיסטריה'
    assert html['description'] == 'md5:de9e2512a92442574cdb0913c49bc4d8'
    assert html['thumbnail'] == r're:^https?://.*\.jpg'
    assert html['duration'] == 3600
# test_WallaIE()

# Generated at 2022-06-14 17:45:23.667115
# Unit test for constructor of class WallaIE
def test_WallaIE():
    assert WallaIE._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'

# Generated at 2022-06-14 17:45:34.422767
# Unit test for constructor of class WallaIE
def test_WallaIE():
    instance = WallaIE('http://vod.walla.co.il/movie/2642630/one-direction-all-for-one');
    assert isinstance(instance, WallaIE)
    assert instance._VALID_URL == r'https?://vod\.walla\.co\.il/[^/]+/(?P<id>\d+)/(?P<display_id>.+)'