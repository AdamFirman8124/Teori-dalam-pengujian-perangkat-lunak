

# Generated at 2022-06-14 16:55:37.844194
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from .common import SoundgasmProfileIE


# Generated at 2022-06-14 16:55:40.408172
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert isinstance(ie, InfoExtractor) and ie.IE_NAME == 'soundgasm:profile'

    ie = SoundgasmIE()
    assert isinstance(ie, InfoExtractor) and ie.IE_NAME == 'soundgasm'

# Generated at 2022-06-14 16:55:42.696160
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	import unit
	from soundgasm import SoundgasmProfileIE
	assert unit.constructor_test(SoundgasmProfileIE, 'http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:55:45.173184
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 16:55:56.259345
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'soundgasm'
    assert ie.IE_DESC == 'Soundgasm'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:56:00.329237
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    instance = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert instance._VALID_URL == instance.VALID_URL
    assert instance._TEST == instance.TEST

# Generated at 2022-06-14 16:56:12.396922
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_SoundgasmProfileIE_constructor = SoundgasmProfileIE(None, None, None, None, None)
    assert test_SoundgasmProfileIE_constructor.IE_NAME == 'soundgasm:profile'
    assert test_SoundgasmProfileIE_constructor._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert test_SoundgasmProfileIE_constructor._TEST == {'url': 'http://soundgasm.net/u/ytdl',
                                                                  'info_dict': {'id': 'ytdl'},
                                                                  'playlist_count': 1}



# Generated at 2022-06-14 16:56:17.987133
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    audio_id = 'Piano-sample'

    # Test for constructor
    test_obj = SoundgasmIE(url, audio_id)

# Generated at 2022-06-14 16:56:22.289978
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    #Test for the "__init__" method of the class SoundgasmProfileIE.
    SoundgasmProfileIE_instance = SoundgasmProfileIE()
    assert isinstance(SoundgasmProfileIE_instance, SoundgasmProfileIE), 'Check if the created instance is a SoundgasmProfileIE'


# Generated at 2022-06-14 16:56:33.661921
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'

    print("Testing url:\t{}".format(url))

    ie = SoundgasmIE()
    info = ie.extract(url)

    print("Testing title:\t\t{}".format(info["title"]))
    assert "Piano sample" == info["title"]

    print("Testing description:\t{}".format(info["description"]))
    assert "Royalty Free Sample Music" == info["description"]

    print("Testing id:\t\t{}".format(info["id"]))
    assert "88abd86ea000cafe98f96321b23cc1206cbcbcc9" == info["id"]

    print("Testing display_id:\t{}".format(info["display_id"]))


# Generated at 2022-06-14 16:56:40.816335
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	assert SoundgasmProfileIE()._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:56:42.693844
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm = SoundgasmProfileIE()
    assert soundgasm.IE_NAME == "soundgasm:profile"

# Generated at 2022-06-14 16:56:45.403884
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    my_Soundgasm_object = SoundgasmIE()
    my_Soundgasm_object.IE_NAME
    my_Soundgasm_object._VALID_URL
test_SoundgasmIE()


# Generated at 2022-06-14 16:56:51.620327
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE()
    assert (obj._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)')


# Generated at 2022-06-14 16:57:01.179669
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    res = re.match(SoundgasmIE._VALID_URL, url)
    assert res

    url = 'http://soundgasm.net/u/ytdl'
    res = re.match(SoundgasmIE._VALID_URL, url)
    assert res is None

    from .common import *
    from .Mock_httpd import MockHttpServer
    from .downloader.http import HttpRequest

    url = 'http://soundgasm.net/u/ytdl'
    test = MockHttpServer()

# Generated at 2022-06-14 16:57:03.537104
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 16:57:14.138135
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    he = SoundgasmIE()
    # he.extractor._VALID_URL = re.compile(r'https?://(?:www\.)?soundgasm\.net/u/')
    he.extractor._VALID_URL = re.compile(r'https?://(?:www\.)?soundgasm\.net/u/([0-9a-zA-Z_-]+)/([0-9a-zA-Z_-]+)')

# Generated at 2022-06-14 16:57:14.957259
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    s = SoundgasmIE()

# Generated at 2022-06-14 16:57:17.737455
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE(None)
    ie._real_extract('http://soundgasm.net/u/ytdl/Piano-sample')



# Generated at 2022-06-14 16:57:21.106912
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    sgprofile = SoundgasmProfileIE()
    

# Generated at 2022-06-14 16:57:39.775105
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    metadata = {
        'url' : 'http://soundgasm.net/u/ytdl/Piano-sample',
        'md5' : '010082a2c802c5275bb00030743e75ad',
        'info_dict' : {
            'id' : '88abd86ea000cafe98f96321b23cc1206cbcbcc9',
            'ext' : 'm4a',
            'title' : 'Piano sample',
            'description' : 'Royalty Free Sample Music',
            'uploader' : 'ytdl'
        }
    }
    sg_ie = SoundgasmIE()
    info = sg_ie._real_extract(metadata['url'])

    assert info['id'] == metadata['info_dict']['id']

# Generated at 2022-06-14 16:57:47.765921
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    object = SoundgasmIE()
    assert object._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:57:53.320202
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
  sample_input_url='http://soundgasm.net/u/ytdl/Piano-sample'
  sg_ie = SoundgasmIE(sample_input_url);
  assert sg_ie.url==sample_input_url;
  assert sg_ie.info_dict=={'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9', 'ext': 'm4a', 'title': 'Piano sample', 'description': 'Royalty Free Sample Music', 'uploader': 'ytdl'};
  assert sg_ie.download_webpage==None;

# Generated at 2022-06-14 16:57:55.005573
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE(InfoExtractor()).IE_NAME == "soundgasm"


# Generated at 2022-06-14 16:57:56.869505
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Test for constructor of class SoundgasmIE
    assert SoundgasmIE()._VALID_URL == SoundgasmIE._VALID_URL

# Generated at 2022-06-14 16:58:01.975702
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    soundgasm = SoundgasmProfileIE(SoundgasmProfileIE.IE_NAME)
    a = soundgasm._extract_urls('http://soundgasm.net/u/ytdl')
    assert(a == ['http://soundgasm.net/u/ytdl'])

# Generated at 2022-06-14 16:58:05.946604
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:58:09.286644
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # constructor
    ie = SoundgasmProfileIE()

    # sample url
    test_url = 'http://soundgasm.net/u/ytdl'

    # sample url for profile
    res = ie._download_webpage(test_url, 'ytdl')
    if res is not None:
        print ('Test successful!')



# Generated at 2022-06-14 16:58:12.250755
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Url to be used for testing
    url = "http://soundgasm.net/u/ytdl/"
    # Passing the url to the constructor of the class
    ie = SoundgasmProfileIE(url)
    # Writing the unit test for the constructor
    ie.url == url


# Generated at 2022-06-14 16:58:23.664788
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	# Create instance of class SoundgasmIE
	ie = SoundgasmIE.SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
	# Check that the URL is set
	assert ie.url == 'http://soundgasm.net/u/ytdl/Piano-sample'
	# Check that the IE_NAME is set
	assert ie.IE_NAME == 'soundgasm'
	# Check that the _VALID_URL is set
	assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
	# Check that the _TEST is set
	assert ie

# Generated at 2022-06-14 16:58:46.861511
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	print("Testing SoundgasmIE")
	print("-------------------")

	result = SoundgasmIE._build_url_result("Youtube-dl", "Youtube-dl", "youtube-dl")
	assert result["url"] == "Youtube-dl"
	assert result["ie_key"] == "Soundgasm"
	assert result["id"] == "youtube-dl"
	assert result["_type"] == "url"


# Generated at 2022-06-14 16:58:47.413118
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()

# Generated at 2022-06-14 16:58:54.195982
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('SoundgasmProfile', 'http://soundgasm.net/u/ytdl')
    assert(ie.IE_NAME == 'SoundgasmProfile')
    # Test that the constructor does not fail when called without parameters
    ie = SoundgasmProfileIE()
    assert(ie.IE_NAME == 'SoundgasmProfile')

# Generated at 2022-06-14 16:58:55.773496
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE().test()

# Generated at 2022-06-14 16:59:04.388068
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._TEST == {
        'url': 'http://soundgasm.net/u/ytdl',
        'info_dict': {
            'id': 'ytdl',
        },
        'playlist_count': 1,
    }


# Generated at 2022-06-14 16:59:05.701048
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test_SoundgasmIE = SoundgasmIE()


# Generated at 2022-06-14 16:59:09.943750
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Test without video
    soundgasm_IE = SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    assert soundgasm_IE.NAME == "Soundgasm"
    # Test with video
    soundgasm_IE.extract("http://soundgasm.net/u/ytdl/Piano-sample")
    assert soundgasm_IE.NAME == "Soundgasm"

# Generated at 2022-06-14 16:59:12.103528
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert (ie.IE_NAME == 'soundgasm:profile')

# Generated at 2022-06-14 16:59:18.243373
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # test url filelists
    url_filelists = open("data/url_filelists.txt", "r").read()
    RE_FIND_URL = r'href="([^"]+)"'
    urls = re.findall(RE_FIND_URL, url_filelists)
    for url in urls:
        ie = SoundgasmIE()
        print(url)
        ie.suitable(url)


# Generated at 2022-06-14 16:59:28.929684
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():

	# Read the URL from console
	url = raw_input('Please enter the URL to test: ')

	# Check if the URL is valid

# Generated at 2022-06-14 17:00:07.187852
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE("SoundgasmProfileIE", "http://soundgasm.net/u/ytdl")
    assert_equal(ie.ie_key(), 'Soundgasm')

# Generated at 2022-06-14 17:00:09.309623
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Check type of object SoundgasmProfileIE
    assert SoundgasmProfileIE().__class__ == SoundgasmProfileIE


# Generated at 2022-06-14 17:00:20.693656
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE()
    assert obj.IE_NAME == 'soundgasm'
    assert obj._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:00:23.931667
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('https://soundgasm.net/u/ytdl/Piano-sample')
    ie.download('88abd86ea000cafe98f96321b23cc1206cbcbcc9')

# Generated at 2022-06-14 17:00:30.129223
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    constructor = SoundgasmProfileIE()
    assert constructor.IE_NAME == 'soundgasm:profile'
    assert constructor._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'


# Generated at 2022-06-14 17:00:33.411461
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie.extract('http://soundgasm.net/u/ytdl/Piano-sample')
    assert ie.extract('http://soundgasm.net/u/ytdl')

# Generated at 2022-06-14 17:00:40.448196
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    u = 'http://soundgasm.net/u/ytdl'
    obj = SoundgasmProfileIE()
    assert obj is not None
    assert obj.IE_NAME == 'soundgasm:profile'
    assert obj.VALID_URL == 'http://(?:www\\.)?soundgasm\\.net/u/(?P<id>[^/]+)/?(?:#.*)?$'
    assert obj.url == u
    assert obj.id == 'ytdl'
    assert obj.playlist_count == 1


# Generated at 2022-06-14 17:00:48.871961
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    class_ = SoundgasmIE
    input_string = 'http://soundgasm.net/u/ytdl/Piano-sample'
    expected_string = 'http://soundgasm.net/u/ytdl/Piano-sample'
    assert class_.suitable(input_string) is True
    assert class_.url_result(input_string) == expected_string


# Generated at 2022-06-14 17:00:52.927216
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('soundgasm.net')
    assert isinstance(ie, SoundgasmIE)
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 17:00:54.934623
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE()._real_extract('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 17:02:23.184718
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    SoundgasmIE()._real_extract(url)


# Generated at 2022-06-14 17:02:26.036279
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE({'title': 'Test Constructor'})
    title = ie._TEST['info_dict']['title']
    assert title == 'Test Constructor'

# Generated at 2022-06-14 17:02:28.616818
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    teststr = SoundgasmIE
    assert teststr == SoundgasmIE, "test failed"

# Generated at 2022-06-14 17:02:29.493369
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE(None, None)

# Generated at 2022-06-14 17:02:31.495863
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test = SoundgasmProfileIE()

# Generated at 2022-06-14 17:02:35.215444
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # The SoundgasmIE constructor is expected to throw an exception as a result
    # of the regular expression failing to match the URL
    SoundgasmIE('http://soundgasm.net/u/Josh')

# Generated at 2022-06-14 17:02:42.481043
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    playlist_content = [
        'Piano sample',
        'http://soundgasm.net/u/ytdl/Piano-sample',
        'http://soundgasm.net/u/ytdl/Piano-sample.m4a',
        '010082a2c802c5275bb00030743e75ad'
    ]
    url = playlist_content[1]
    ie = SoundgasmProfileIE()
    playlist = ie.extract(url)
    for index in range(len(playlist_content)):
        assert playlist_content[index] == playlist['entries'][0][playlist.keys()[index]]

# Generated at 2022-06-14 17:02:44.706096
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    obj = SoundgasmIE(None)
    assert obj.IE_NAME == 'soundgasm'


# Generated at 2022-06-14 17:02:54.349727
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    i = SoundgasmIE("https://soundgasm.net/u/ytdl/Piano-sample")
    obj = i._real_extract("https://soundgasm.net/u/ytdl/Piano-sample")
    assert obj["id"] == "88abd86ea000cafe98f96321b23cc1206cbcbcc9"
    assert obj["display_id"] == "Piano-sample"
    assert obj["vcodec"] == "none"
    assert obj["title"] == "Piano sample"
    assert obj["description"] == "Royalty Free Sample Music"
    assert obj["uploader"] == "ytdl"


# Generated at 2022-06-14 17:02:56.038033
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    print("Unit test for constructor of class SoundgasmIE")
    a = SoundgasmIE()
