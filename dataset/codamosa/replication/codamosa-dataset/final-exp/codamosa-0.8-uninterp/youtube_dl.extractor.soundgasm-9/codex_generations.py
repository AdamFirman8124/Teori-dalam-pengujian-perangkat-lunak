

# Generated at 2022-06-14 16:55:32.186814
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    ie.extract("http://soundgasm.net/u/ytdl/Piano-sample")


# Generated at 2022-06-14 16:55:36.488007
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sg = SoundgasmIE()
    assert sg._VALID_URL == re.compile(r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')

# Generated at 2022-06-14 16:55:40.694142
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = "http://soundgasm.net/u/ytdl/"

    ie = SoundgasmProfileIE()
    extractor = ie.suitable(url)

    assert extractor is not None
    assert ie._VALID_URL == extractor._VALID_URL

# Generated at 2022-06-14 16:55:42.654619
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    return SoundgasmIE()._real_extract("http://soundgasm.net/u/ytdl/Piano-sample")

# Generated at 2022-06-14 16:55:45.729477
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('https://soundgasm.net/u/ytdl/')
    assert ie.IE_NAME == 'SoundgasmProfile'
    assert ie.validate('https://soundgasm.net/u/ytdl/') == True


# Generated at 2022-06-14 16:55:46.469756
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    pass

# Generated at 2022-06-14 16:55:49.651137
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    assert ie._TEST['url'] == ie.url

# Generated at 2022-06-14 16:55:51.909972
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie=SoundgasmProfileIE()
    assert str(ie) == 'Soundgasm.net profile url downloader'


# Generated at 2022-06-14 16:55:58.002161
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Test cases for class SoundgasmIE
    """
    print("Testing SoundgasmIE Class")

    # Test case with broken URL
    soundgasm_ie = SoundgasmIE()
    broken_url = "http://soundgasm.net/u/ytdl/Piano-sample"
    expected_output = re.compile(r'Piano-sample$')
    assert(soundgasm_ie._match_id(broken_url) == expected_output)
    print("Broken URL Test passed")

    # Test case with valid URL
    valid_url = "http://soundgasm.net/u/ytdl/Piano-sample"
    expected_output = "Piano-sample"
    assert(soundgasm_ie._match_id(valid_url) == expected_output)

# Generated at 2022-06-14 16:56:05.633015
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url='http://soundgasm.net/u/ytdl'
    m = SoundgasmProfileIE._VALID_URL
    mobj = re.match(m, url)
    pg = SoundgasmProfileIE._real_extract(SoundgasmProfileIE(),url)
    assert pg['id'] == mobj.group('id')
    assert pg['_type'] == 'playlist'
    assert len(pg["entries"]) == pg['playlist_count']

# Generated at 2022-06-14 16:56:09.783442
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:56:11.732802
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    # Test that SoundgasmIE can be instantiated
    assert(ie is not None)

# Generated at 2022-06-14 16:56:17.982516
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST == {
            'url': 'http://soundgasm.net/u/ytdl',
            'info_dict': {
                'id': 'ytdl',
            },
            'playlist_count': 1,
        }
    return


# Generated at 2022-06-14 16:56:20.798168
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    try:
        SoundgasmProfileIE('http://soundgasm.net/u/ytdl')
    except:
        print ("Error in SoundgasmProfileIE constructor")

# Generated at 2022-06-14 16:56:22.353202
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Create a SoundgasmProfileIE object
    SoundgasmProfileIE()
    # Create a SoundgasmProfileIE object, with a specified IE name
    SoundgasmProfileIE("SoundgasmProfileIE")

# Generated at 2022-06-14 16:56:33.339411
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    audio_id = '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    ie = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    assert ie.get_id() == audio_id
    assert ie.get_name() == 'Soundgasm'
    assert ie.get_url() == url
    assert ie.is_audiobook() == False
    assert ie.is_shorted_url() == False
    assert ie.get_hash() == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'


# Generated at 2022-06-14 16:56:37.842566
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Simple unit test for class Soundgasm IE
    """
    class_ = SoundgasmIE
    info_extractor = class_(class_.ie_key())
    assert info_extractor.ie_name == 'Soundgasm'

# Generated at 2022-06-14 16:56:44.637935
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert SoundgasmProfileIE._TEST == {
       'url': 'http://soundgasm.net/u/ytdl',
       'info_dict': {
           'id': 'ytdl',
       },
       'playlist_count': 1,
    }


# Generated at 2022-06-14 16:56:48.257856
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert(ie.IE_NAME == "Soundgasm")


# Generated at 2022-06-14 16:56:58.807057
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.ie_key() == 'Soundgasm'
    assert ie.extractor_key() == 'Soundgasm'
    assert ie.IE_NAME == 'Soundgasm'
    assert ie.suitable(None) == False
    assert ie.suitable(3) == False
    assert ie.suitable('test') == False
    assert ie.suitable('http://soundgasm.net/u/ytdl/') == False
    assert ie.suitable('http://soundgasm.net/u/ytdl/foo') == True
    assert ie.suitable('http://soundgasm.net/u/ytdl/FOO') == True
    assert ie.suitable('http://soundgasm.net/u/ytdl/foo/bar') == False
    assert ie

# Generated at 2022-06-14 16:57:08.832366
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    class_name = "SoundgasmIE"
    instance = SoundgasmIE()
    assert (instance.ie_key() == class_name)


# Generated at 2022-06-14 16:57:10.912992
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    ie.download("http://soundgasm.net/u/ytdl/Piano-sample")


# Generated at 2022-06-14 16:57:14.173582
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE(None)
    # Test that _VALID_URL constant is valid
    ie._match_id(ie._VALID_URL)
    # Test that _TEST constant is valid
    ie._match_id(ie._TEST['url'])

# Generated at 2022-06-14 16:57:15.177398
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert True

# Generated at 2022-06-14 16:57:20.591455
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Test case with valid URL
    ie = SoundgasmIE()
    assert ie.suitable('http://soundgasm.net/u/ytdl')
    # Test case with invalid URL
    ie = SoundgasmIE()
    assert not ie.suitable('http://soundgasm.net/u/ytdl/Invalid*URL')


# Generated at 2022-06-14 16:57:22.216933
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:57:35.420324
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE = SoundgasmIE()._real_initialize()

    # pass
    IE.xml
    IE.verbose
    IE.quiet
    IE.no_warnings
    IE.forceurl
    IE.forcetitle
    IE.forceid
    IE.simulate
    IE.geturl
    IE.gettitle
    IE.getid
    IE.getthumbnail
    IE.getdescription
    IE.getfilename
    IE.getformat

    # pass
    IE._match_id('s3://elasticbeanstalk-us-west-2-139401696309/ytdl-video/test.m4a')
    # should pass but does not:
    # IE._match_id(None)
    # IE._match_id('')
    # IE._match_id('http://www

# Generated at 2022-06-14 16:57:39.489574
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    m = SoundgasmIE()
    assert m.IE_NAME == 'soundgasm'
    assert m._VALID_URL == SoundgasmIE._VALID_URL
    assert m._TEST == SoundgasmIE._TEST
    assert m.IE_DESC == 'SoundGASM'


# Generated at 2022-06-14 16:57:41.225927
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('soundgasm:profile', 'http://soundgasm.net/u/ytdl', {})

# Generated at 2022-06-14 16:57:49.451944
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    testcase = (r'https://soundgasm.net/user/User9/recordings/title-1',
                'http://soundgasm.net/u/User9/title-1')
    user_id, display_id = re.match(r'^https?://soundgasm\.net/user/(?P<user>[^/]+)/recordings/(?P<display>[^/]+)$', testcase[0]).groups()
    assert(user_id == 'User9')
    assert(display_id == 'title-1')
    assert(re.match(SoundgasmIE._VALID_URL, testcase[1]))

# Generated at 2022-06-14 16:58:16.349550
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm = SoundgasmProfileIE()
    soundgasm.IE_NAME = 'ytdl.extractor.soundgasm.SoundgasmProfileIE'
    soundgasm.IE_DESC = 'Soundgasm user\'s profile'
    soundgasm.VALID_URL = 'https://soundgasm.net/u/ytdl'
    soundgasm.TEST = {
        'url': 'https://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }
    soundgasm.NAME = 'Soundgasm user\'s profile'
    assert soundgasm.NAME == 'Soundgasm user\'s profile'

# Generated at 2022-06-14 16:58:27.052912
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    import os
    import json
    import unittest
    
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    test_file_path = os.path.join(cur_dir, "test.json")    
    
    with open(test_file_path, "r") as f:
        js = json.load(f)
     
    for test_item in js:
        url = test_item["url"]
        result = SoundgasmIE().extract(url)
        assert(result["id"] == test_item["id"])
        assert(result["ext"] == test_item["ext"])
        assert(result["title"] == test_item["title"])
        assert(result["description"] == test_item["description"])

# Generated at 2022-06-14 16:58:30.779307
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
        This function is called to test the constructor of class SoundgasmIE.
    """
    soundgasmIE = SoundgasmIE()
    assert soundgasmIE._downloader is None
    assert soundgasmIE._connection is None

# Generated at 2022-06-14 16:58:34.656423
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE(SoundgasmIE(None), None)._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'



# Generated at 2022-06-14 16:58:47.206561
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    ie = SoundgasmIE()
    info_dict = ie._real_extract(test_url)

    assert len(info_dict) == 8
    assert info_dict['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert info_dict['ext'] == 'm4a'
    assert info_dict['title'] == 'Piano sample'
    assert info_dict['description'] == 'Royalty Free Sample Music'
    assert info_dict['uploader'] == 'ytdl'
    assert info_dict['display_id'] == 'Piano-sample'

# Generated at 2022-06-14 16:58:52.485523
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE({})
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST == {'url': 'http://soundgasm.net/u/ytdl',
     'info_dict': {'id': 'ytdl'},
     'playlist_count': 1}

# Generated at 2022-06-14 16:58:57.911987
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert (SoundgasmProfileIE()._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')
    assert (SoundgasmProfileIE()._TEST == {'url': 'http://soundgasm.net/u/ytdl', 'info_dict': {'id': 'ytdl'}, 'playlist_count': 1})


# Generated at 2022-06-14 16:59:02.046759
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	#test whether the constructor of class SoundgasmProfileIE can run normally
	ie = SoundgasmProfileIE("")
	ie.extract("http://soundgasm.net/u/ytdl")

# Generated at 2022-06-14 16:59:04.031582
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    soundgasm = SoundgasmIE()
    assert soundgasm.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:59:04.651963
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:59:36.330823
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE(None, None)._real_extract("http://soundgasm.net/u/ytdl")

# Generated at 2022-06-14 16:59:46.877815
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    audio_url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    audio_info = SoundgasmIE()._real_extract(audio_url)
    assert audio_info['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert audio_info['display_id'] == 'Piano-sample'
    assert audio_info['url'] == 'http://soundgasm.net/stream/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a'
    assert audio_info['vcodec'] == 'none'
    assert audio_info['title'] == 'Piano sample'
    assert audio_info['description'] == 'Royalty Free Sample Music'
    assert audio_info

# Generated at 2022-06-14 16:59:50.410671
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    i = SoundgasmProfileIE()
    assert i.IE_NAME == 'soundgasm:profile'
    assert i._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 17:00:00.764484
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Create instance of class SoundgasmIE
    ie = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    # Make sure it is valid IE
    assert ie.IE_NAME == "Soundgasm"
    # Make sure its URL is correct
    assert ie.IE_URL == "http://soundgasm.net/u/ytdl/Piano-sample"
    # Make sure it is created with the correct URL
    assert ie.url == "http://soundgasm.net/u/ytdl/Piano-sample"
    # Make sure it is created with the correct display_id
    assert ie.display_id == "Piano-sample"
    # Make sure its _VALID_URL is correct

# Generated at 2022-06-14 17:00:06.888097
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.extract('http://soundgasm.net/u/ytdl/Piano-sample')
    ie._download_webpage('http://soundgasm.net/u/ytdl/Piano-sample', 'Piano-sample')


# Generated at 2022-06-14 17:00:09.064937
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    SoundgasmProfileIE().suitable(url)

# Generated at 2022-06-14 17:00:12.645934
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    a = SoundgasmProfileIE()
    import inspect
    print(inspect.getmembers(a))
    return

# Generated at 2022-06-14 17:00:15.494159
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """Unit test for constructor of class SoundgasmProfileIE.
    """
    instance = SoundgasmProfileIE()
    printinstance.soundgasm_profile_ie

# Generated at 2022-06-14 17:00:22.144257
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	sound = SoundgasmProfileIE()
	test = sound._download_webpage("http://soundgasm.net/u/ytdl", "ytdl")
	test = sound._download_webpage("http://soundgasm.net/u/ytdl", "ytdl")
	test = sound._download_webpage("http://soundgasm.net/u/ytdl", "ytdl")


# Generated at 2022-06-14 17:00:28.301089
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Test for soundgasm:profile when there is no audio for the user
    sg_ie = SoundgasmProfileIE()
    result = sg_ie._real_extract('http://soundgasm.net/u/ytdl_none')
    expected = []
    assert (result['entries'] == expected)

# Generated at 2022-06-14 17:01:55.209003
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        import youtube_dl
        obj = youtube_dl.YoutubeDL(youtube_dl.utils.dict_to_kwargs({}))
        SoundgasmIE()(obj)
        assert False, 'unit test for SoundgasmIE class has errors.'
    except TypeError:
        pass


# Generated at 2022-06-14 17:01:58.685151
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    m = SoundgasmIE()
    assert m._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:03.329212
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = "http://soundgasm.net/u/ytdl/Piano-sample"
    SoundgasmIE()._real_extract(url)

test = test_SoundgasmIE()
test

# Generated at 2022-06-14 17:02:07.383589
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm_profile_ie = SoundgasmProfileIE()
    mobj = re.match(soundgasm_profile_ie._VALID_URL, 'http://soundgasm.net/u/ytdl')
    assert mobj.group('id') == 'ytdl'


# Generated at 2022-06-14 17:02:11.389732
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile = SoundgasmProfileIE()
    assert profile.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 17:02:20.663784
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """Unit test for constructor of class SoundgasmIE."""

    test_url = 'http://blah.com/Xyz_123'


# Generated at 2022-06-14 17:02:21.779186
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    s2 = SoundgasmProfileIE('SoundgasmProfileIE')
    assert s2 != None


# Generated at 2022-06-14 17:02:22.840469
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 17:02:32.705987
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sample_url = "http://soundgasm.net/u/ytdl/Piano-sample"
    ie = SoundgasmIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert ie._TEST['url'] == sample_url
    assert ie._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'
    assert ie._TEST['info_dict']['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'

# Generated at 2022-06-14 17:02:34.647133
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    u = SoundgasmProfileIE()