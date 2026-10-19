

# Generated at 2022-06-14 16:55:37.355274
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	IE = SoundgasmIE()
	assert(IE.IE_NAME == 'soundgasm')
	assert(IE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')


# Generated at 2022-06-14 16:55:40.399430
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()._download_webpage(url="http://soundgasm.net/u/ytdl", display_id="ytdl")


# Generated at 2022-06-14 16:55:45.286683
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    info_extractor = SoundgasmProfileIE()
    print (info_extractor.IE_NAME)
    print (info_extractor.IE_DESC)
    print (info_extractor.IE_VERSION)
    print (info_extractor._VALID_URL)
    print (info_extractor.__name__)
    print (info_extractor._NETRC_MACHINE)
    print (info_extractor._TESTS)

# Generated at 2022-06-14 16:55:47.322542
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl", 'Soundgasm:profile')

# Generated at 2022-06-14 16:55:52.405558
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    import soundgasm
    assert isinstance(soundgasm, InfoExtractor)
    assert hasattr(soundgasm, '_download_webpage')
    assert hasattr(soundgasm, 'url_result')
    assert hasattr(soundgasm, 'playlist_result')


# Generated at 2022-06-14 16:55:54.147433
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 16:55:56.545344
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    ie = SoundgasmIE()
    download_url = ie.download_webpage(url)
    assert download_url['url'] == url


# Generated at 2022-06-14 16:56:04.449153
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie._TEST == { 'url': 'http://soundgasm.net/u/ytdl', 'info_dict': { 'id': 'ytdl' }, 'playlist_count': 1 }

# Generated at 2022-06-14 16:56:09.457215
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_instance = SoundgasmProfileIE()
    assert test_instance._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:56:18.161838
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    s = SoundgasmIE()
    assert 'Soundgasm' in s.IE_NAME
    assert s._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:56:26.748420
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()


# Generated at 2022-06-14 16:56:31.816994
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    except:
        print("Failed test for SoundgasmIE")
        print("Please report this to https://github.com/rg3/youtube-dl/issues/new")

test_SoundgasmIE()

# Generated at 2022-06-14 16:56:39.698085
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    unit_test = SoundgasmIE()
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    display_id = 'Piano-sample'
    audio_id = '88abd86ea000cafe98f96321b23cc1206cbcbcc9'

# Generated at 2022-06-14 16:56:42.549639
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    print("Testing SoundgasmIE constructor")
    i = SoundgasmIE()
    print("Succesfully instantiated SoundgasmIE.")



# Generated at 2022-06-14 16:56:43.890278
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE()
        assert False
    except:
        assert True

# Generated at 2022-06-14 16:56:46.083324
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('http://soundgasm.net/u/ytdl/Piano-sample', 'ytdl/Piano-sample')

# Generated at 2022-06-14 16:56:52.237494
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Case 1
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    mobj = re.match(SoundgasmIE._VALID_URL, url)
    assert mobj is not None
    assert mobj.group('user') == 'ytdl'
    assert mobj.group('display_id') == 'Piano-sample'

# Generated at 2022-06-14 16:56:53.743495
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    print(ie)



# Generated at 2022-06-14 16:56:55.955488
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()._real_extract('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:56:57.631712
# Unit test for constructor of class SoundgasmIE

# Generated at 2022-06-14 16:57:14.824863
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:57:16.606170
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from .common import test_constructor
    test_constructor('soundgasm:profile')

# Generated at 2022-06-14 16:57:17.113026
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    pass

# Generated at 2022-06-14 16:57:18.456192
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    instance = SoundgasmIE()
    assert isinstance(instance, SoundgasmIE)

# Generated at 2022-06-14 16:57:22.390905
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    class_names = IE_NAME.split('.')

    exec('from %s import %s' % (class_names[0], class_names[1]))

    globals()[class_names[1]]('soundgasm', 'ytdl', '88abd86ea000cafe98f96321b23cc1206cbcbcc9')

# Generated at 2022-06-14 16:57:26.054779
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.author_url_template == "https://soundgasm.net/u/%s"

# Generated at 2022-06-14 16:57:37.830819
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl")
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl/")
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#")
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#/")
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#/soundgasm/")
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#/soundgasm/1")
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl/#/soundgasm/111")

# Generated at 2022-06-14 16:57:41.642847
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    soundgasmIE = SoundgasmIE()
    updates = soundgasmIE._real_extract(url)
    assert updates['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert updates['ext'] == 'm4a'
    assert updates['title'] == 'Piano sample'
    assert updates['description'] == 'Royalty Free Sample Music'
    assert updates['uploader'] == 'ytdl'



# Generated at 2022-06-14 16:57:49.071023
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Provide the arguments from the main function
    #--- sys.argv[1:] is the list of arguments for the program
    #--- the first argument is the url
    #--- the second argument is the output file
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    #url = sys.argv[1]
    filename = 'output.m4a'
    #filename = sys.argv[2]

    # Create instance of InfoExtractor
    info_extractor = SoundgasmIE()
    # Extract video
    extract_info = info_extractor.extract(url)
    # Write the video to the file
    #--- the 'url' property of the extract_info is the video file URL

# Generated at 2022-06-14 16:57:50.555699
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    return SoundgasmProfileIE('SoundgasmProfileIE', 'http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:58:14.878763
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    SoundgasmProfileIE._TEST = {}
    SoundgasmProfileIE._TEST = {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }
    test_SoundgasmProfileIE._TEST = SoundgasmProfileIE._TEST
    ie = SoundgasmProfileIE(url=url)
    print(ie)

# Generated at 2022-06-14 16:58:17.785340
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE('Soundgasm')

# Generated at 2022-06-14 16:58:18.766237
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert True


# Generated at 2022-06-14 16:58:22.927164
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    class_ = SoundgasmIE
    inst = class_()
    assert inst._VALID_URL == class_._VALID_URL
    assert inst._TEST == class_._TEST
    assert inst.IE_NAME == class_._TEST['url']

if __name__ == '__main__':
    test_SoundgasmIE()

# Generated at 2022-06-14 16:58:25.010739
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert isinstance(SoundgasmIE, type) and issubclass(SoundgasmIE, InfoExtractor)


# Generated at 2022-06-14 16:58:36.589124
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE()
    # Verify that the instance has been constructed correctly
    assert re.match(SoundgasmIE._VALID_URL, 'http://soundgasm.net/u/ytdl/Piano-sample')
    assert re.match(SoundgasmIE._VALID_URL, 'https://soundgasm.net/u/ytdl/Piano-sample')
    assert not re.match(SoundgasmIE._VALID_URL, 'https://soundgasm.net/u/ytdl/')
    assert not re.match(SoundgasmIE._VALID_URL, 'https://soundgasm.net/u/ytdl')
    # Verify that the expected instance variables have been set

# Generated at 2022-06-14 16:58:39.838984
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    unit_test = SoundgasmProfileIE('http://soundgasm.net/u/ytdl', {'soundgasm:profile'})
    assert unit_test.IE_NAME == 'soundgasm:profile'

# Generated at 2022-06-14 16:58:41.833309
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE()._VALID_URL == SoundgasmProfileIE._VALID_URL

# Generated at 2022-06-14 16:58:45.234848
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_obj=SoundgasmProfileIE()
    assert test_obj.IE_NAME=='soundgasm:profile'

# Generated at 2022-06-14 16:58:52.525376
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Arrange
    from .common import SoundgasmIE
    ie = SoundgasmIE()
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    # Act
    ie._real_extract(url)
    name =  ie.IE_NAME
    # Assert
    assert(name == 'soundgasm')


# Generated at 2022-06-14 16:59:25.247133
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    instance = SoundgasmProfileIE()
    print(instance.IE_NAME)




# Generated at 2022-06-14 16:59:29.211689
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    result = SoundgasmIE()._real_extract(
        "http://soundgasm.net/u/ytdl/Piano-sample")
    assert result['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'

# Generated at 2022-06-14 16:59:29.781477
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:59:33.366332
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    strURL = 'http://soundgasm.net/u/ytdl'
    objIE = SoundgasmProfileIE()
    objIE._real_extract(strURL)


# Generated at 2022-06-14 16:59:38.075893
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    t = SoundgasmIE()
    assert t.__name__ == 'Soundgasm'
    assert t.info_extractors[0].__name__ == 'Soundgasm'
    assert t.info_extractors[1].__name__ == 'Soundgasm Profile'

# Generated at 2022-06-14 16:59:48.517109
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_dict_1 = {
    'url': 'http://soundgasm.net/u/ytdl',
    'info_dict': {
        'id': 'ytdl',
    },
    'playlist_count': 1,
    }

    test_dict_2 = {
    'url': 'http://soundgasm.net/u/ytdl',
    'info_dict': {
        'id': 'ytdl',
    },
    'playlist_count': 1,
    }

    test_dict_3 = {
    'url': 'http://soundgasm.net/u/ytdl',
    'info_dict': {
        'id': 'ytdl',
    },
    'playlist_count': 1,
    }

    assert test_dict_1 == test_

# Generated at 2022-06-14 16:59:49.382550
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:59:54.651211
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from unittest import TestSuite, makeSuite
    from soundgasm_test import SoundgasmTest

    class ConstructorTest(SoundgasmTest):

        def runTest(self):
            self.assertTrue(isinstance(self.ie, SoundgasmProfileIE))

    suite = TestSuite([ConstructorTest('test_SoundgasmProfileIE')])
    return suite

# Generated at 2022-06-14 17:00:00.987452
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    info = SoundgasmIE()._call_api(
        'http://soundgasm.net/u/ytdl/Piano-sample')
    assert info == {
        'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9',
        'ext': 'm4a',
        'title': 'Piano sample',
        'description': 'Royalty Free Sample Music',
        'uploader': 'ytdl',
    }

# Generated at 2022-06-14 17:00:12.038972
# Unit test for constructor of class SoundgasmIE

# Generated at 2022-06-14 17:01:45.746228
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    assert ie._TEST['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert ie._TEST['md5'] == '010082a2c802c5275bb00030743e75ad'

# Generated at 2022-06-14 17:01:50.787871
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Given
    constructor_arguments = ['']
    # When
    instance = SoundgasmProfileIE(*constructor_arguments)
    # Then
    assert isinstance(instance, SoundgasmProfileIE)
    assert hasattr(instance, '_VALID_URL')
    assert hasattr(instance, '_TEST')
    assert hasattr(instance, '_real_extract')

# Generated at 2022-06-14 17:01:59.820566
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """
    Unit tests for the class SoundgasmIE
    """
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    mobj = re.search(SoundgasmIE._VALID_URL, url)
    audio_url = 'http://www.soundgasm.net/u/ytdl/Piano-sample/88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    audio_id = '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    title = 'Piano sample'
    uploader = 'ytdl'
    description = 'Royalty Free Sample Music'

    assert mobj
    assert mobj.group('user') == uploader

# Generated at 2022-06-14 17:02:04.913514
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert (SoundgasmIE()._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')


# Generated at 2022-06-14 17:02:11.588851
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    IE = SoundgasmProfileIE()
    # test get_username
    assert IE.get_username('http://soundgasm.net/u/ytdl') == 'ytdl'
    assert IE.get_username('http://soundgasm.net/u/ytdl/') == 'ytdl'
    assert IE.get_username('http://soundgasm.net/u/ytdl/any') == 'ytdl'
    assert IE.get_username('http://soundgasm.net/u/ytdl/#something') == 'ytdl'
    assert IE.get_username('http://soundgasm.net/u/ytdl/#') == 'ytdl'
    assert IE.get_username('http://soundgasm.net/u/ytdl##') == 'ytdl'

# Generated at 2022-06-14 17:02:17.698829
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    stem = 'test_videos/test_'
    target = stem + 'SoundgasmProfileIE.txt'
    myIE = SoundgasmProfileIE('Soundgasm', 'http://soundgasm.net/u/ytdl')
    result = myIE.extract()
    f = open(target, 'w')
    f.write(result)
    f.close()

# Tests for class SoundgasmIE

# Generated at 2022-06-14 17:02:23.039324
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        s = SoundgasmIE()
        s.extract("http://soundgasm.net/u/ytdl/Piano-sample")
        test = True
    except:
        test = False
    assert test


# Generated at 2022-06-14 17:02:24.669619
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    print('Unit test for class SoundgasmIE:')
    print(SoundgasmIE())

# Generated at 2022-06-14 17:02:34.006082
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    tc = SoundgasmIE()
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert tc._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:02:35.127053
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test = SoundgasmIE()