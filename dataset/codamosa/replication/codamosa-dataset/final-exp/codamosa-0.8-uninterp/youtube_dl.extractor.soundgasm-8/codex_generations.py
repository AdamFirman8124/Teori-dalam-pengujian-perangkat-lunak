

# Generated at 2022-06-14 16:55:31.741835
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE('Soundgasm:profile')

# Generated at 2022-06-14 16:55:33.630840
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	test_SoundgasmIE = SoundgasmIE()

# Generated at 2022-06-14 16:55:34.695043
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    pass

# Generated at 2022-06-14 16:55:36.643025
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie=SoundgasmIE()
    print("test for constructor for SoundgasmIE is passed")


# Generated at 2022-06-14 16:55:39.344165
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """Constructor test"""
    ie = SoundgasmProfileIE()
    ie.to_screen()
    ie.IE_NAME

# Generated at 2022-06-14 16:55:43.733512
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    user = 'ytdl'
    display_id = 'Piano-sample'
    mobj = re.match(SoundgasmIE._VALID_URL, url)
    assert user == mobj.group('user')
    assert display_id == mobj.group('display_id')

# Generated at 2022-06-14 16:55:53.814047
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    inst = SoundgasmProfileIE("http://soundgasm.net/u/ytdl", "test")

# Generated at 2022-06-14 16:55:55.169261
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert SoundgasmIE().playlist_mincount == 1


# Generated at 2022-06-14 16:55:57.950860
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE("http://soundgasm.net/u/ytdl/Piano-sample")
    SoundgasmIE("http://www.soundgasm.net/u/ytdl/Piano-sample")
    SoundgasmIE("http://www.soundgasm.net/u/ytdl/Piano-sample")


# Generated at 2022-06-14 16:56:08.016213
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    import pytest

    profile_url = 'http://soundgasm.net/u/ytdl/'
    profile_class = SoundgasmProfileIE()
    profile_instance = profile_class.suitable(profile_url)
    assert profile_instance, 'Profile URL is not available!'

    with pytest.raises(AttributeError):
        assert profile_class.ie_key()

    assert profile_class.IE_NAME == 'soundgasm:profile'

    assert 'ytdl' == profile_class.profile_id(profile_url)


# Generated at 2022-06-14 16:56:14.073949
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE("http://soundgasm.net/u/ytdl")

# Generated at 2022-06-14 16:56:16.482153
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:56:23.638154
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    user_id = "ytdl"
    audio_url = "http://soundgasm.net/u/{0}/Piano-sample".format(user_id)
    ie = SoundgasmProfileIE()._real_extract(audio_url)
    assert ie['id'] == user_id
    assert ie['entries'][0]['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
    assert ie['entries'][0]['title'] == 'Piano sample'

# Generated at 2022-06-14 16:56:24.510574
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    return SoundgasmProfileIE

# Generated at 2022-06-14 16:56:35.283043
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE_NAME = 'soundgasm'
    _VALID_URL = r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:56:44.154695
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    test = {
        'url': 'http://soundgasm.net/u/ytdl/Piano-sample',
        'md5': '010082a2c802c5275bb00030743e75ad',
        'info_dict': {
            'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9',
            'ext': 'm4a',
            'title': 'Piano sample',
            'description': 'Royalty Free Sample Music',
            'uploader': 'ytdl',
        }
    }
    return SoundgasmIE().extract(test['url'])

# Generated at 2022-06-14 16:56:46.844568
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE(None, None)

# Generated at 2022-06-14 16:56:54.939725
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    url = 'http://soundgasm.net/u/ytdl/Piano-sample'
    obj = SoundgasmIE()
    assert obj.IE_NAME == 'soundgasm'
    assert re.match(r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)', url)
    assert obj._downloader is not None
    assert obj._match_id('ytdl') == 'ytdl'

# Generated at 2022-06-14 16:56:57.933548
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    result = SoundgasmIE()
    assert result.ie_name() == 'soundgasm'
    assert result.info_extractors()[0].ie_name() == 'soundgasm'

# Generated at 2022-06-14 16:57:03.336571
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    """ test_SoundgasmProfileIE: 
    """
    url = 'http://soundgasm.net/u/ytdl'
    ie = SoundgasmProfileIE()
    assert(ie.IE_NAME == 'soundgasm:profile')
    assert(ie.IE_DESC == 'Soundgasm profiles')
    assert(ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$')
    profile_id = ie._match_id(url)
    assert(profile_id == 'ytdl')

# Generated at 2022-06-14 16:57:11.281144
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	pass

# Generated at 2022-06-14 16:57:13.221501
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    inst = SoundgasmIE()
    # Test for constructor of class SoundgasmIE
    assert isinstance(inst, SoundgasmIE)

# Generated at 2022-06-14 16:57:15.614161
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    i = SoundgasmProfileIE("http://soundgasm.net/u/ytdl")
    assert i.IE_NAME == 'SoundgasmProfileIE'

# Generated at 2022-06-14 16:57:22.005394
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert ie.IE_NAME == 'soundgasm:profile'
    assert ie._TEST['url'] == 'http://soundgasm.net/u/ytdl'
    assert ie._TEST['info_dict'] == {'id': 'ytdl'}

# Generated at 2022-06-14 16:57:24.768791
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
	ie = SoundgasmIE()
	assert ie.IE_NAME == "SoundgasmIE"

# Generated at 2022-06-14 16:57:28.392883
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie=SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample ')
    assert isinstance(ie,InfoExtractor)


# Generated at 2022-06-14 16:57:29.529270
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:57:30.851602
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()

# Generated at 2022-06-14 16:57:40.575346
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    import requests
    # https://soundgasm.net/u/ytdl/Piano-sample


# Generated at 2022-06-14 16:57:43.037306
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()

# Generated at 2022-06-14 16:58:00.246143
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    
    """Test for constructor
    
    Returns:
        class object
    
    """

    s = SoundgasmIE()
    assert(isinstance(s, SoundgasmIE))

# Generated at 2022-06-14 16:58:00.687928
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert True

# Generated at 2022-06-14 16:58:02.750843
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():

    url = 'http://soundgasm.net/u/ytdl'
    # try instantiating SoundgasmProfileIE
    SoundgasmProfileIE(url)

# Generated at 2022-06-14 16:58:07.521258
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE(None, 'http://soundgasm.net/u/ytdl/Piano-sample')
    except:
        pass
    return True

# Generated at 2022-06-14 16:58:08.784338
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	test = SoundgasmProfileIE()

# Generated at 2022-06-14 16:58:11.647421
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    import os
    x = SoundgasmProfileIE()
    assert 'Soundgasm' == x._VALID_URL


# Generated at 2022-06-14 16:58:23.000027
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('')
    assert ie._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[^/]+)/(?P<display_id>[^/]+)'
    assert ie._DOWNLOAD_WEBPAGE_ERRORS == (1, 2, )

# Generated at 2022-06-14 16:58:25.509388
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    # Test with valid url
    assert SoundgasmProfileIE._TEST['url'] == 'http://soundgasm.net/u/ytdl'


# Generated at 2022-06-14 16:58:27.498108
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    profile_obj = SoundgasmProfileIE()
    assert (profile_obj.IE_NAME == "soundgasm:profile")

# Generated at 2022-06-14 16:58:31.619517
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_url = 'http://soundgasm.net/u/ytdl'
    obj = SoundgasmProfileIE()
    obj.url = test_url
    normal_url = obj._normalize_url(test_url)
    mobj = obj._VALID_URL_RE.match(normal_url)
    assert mobj is not None
    assert obj._match_id(normal_url) == 'ytdl'

# Generated at 2022-06-14 16:59:08.838352
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    url = 'http://soundgasm.net/u/ytdl'
    ie = SoundgasmProfileIE()
    profile_id = ie._match_id(url)
    webpage = ie._download_webpage(url, profile_id)
    entries = [ie.url_result(audio_url, 'Soundgasm')
              for audio_url in re.findall(r'href="([^"]+/u/%s/[^"]+)' % profile_id, webpage)]
    playlist = ie.playlist_result(entries, profile_id)
    if playlist['entries']:
        print ("Unit test of SoundgasmProfileIE:")
        print ("OK.")
    else:
        print ("Unit test of SoundgasmProfileIE:")
        print ("ERROR.")

# Generated at 2022-06-14 16:59:19.226109
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE
    ie_obj = ie('Soundgasm')
    assert ie_obj.IE_NAME == 'soundgasm'
    assert ie_obj._VALID_URL == 'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'

# Generated at 2022-06-14 16:59:29.539782
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    from soundgasm import SoundgasmProfileIE
    profile_url = 'http://soundgasm.net/u/ytdl'
    assert SoundgasmProfileIE._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'
    assert SoundgasmProfileIE(profile_url)._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<id>[^/]+)/?(?:\#.*)?$'

# Generated at 2022-06-14 16:59:35.999769
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    player_page = "http://soundgasm.net/u/ytdl/Piano-sample"
    soundgasm = SoundgasmIE(player_page)
    assert(soundgasm.extractor_name == "SoundgasmIE")
    assert(soundgasm.extractor_key == "Soundgasm")


# Generated at 2022-06-14 16:59:36.688218
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 16:59:37.947094
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
	# Test the constructor for class SoundgasmProfileIE
	SoundgasmProfileIE()

# Generated at 2022-06-14 16:59:42.738309
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    a = ie.get_playlist('http://soundgasm.net/u/ytdl/Piano-sample')
    assert a[0]['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'


# Generated at 2022-06-14 16:59:45.905057
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert ie.IE_NAME == 'Soundgasm'
    assert ie.IE_DESC == 'Soundgasm.net: profile and audio'


# Generated at 2022-06-14 16:59:49.091731
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    """ test the constructor of SoundgasmIE """
    # pylint: disable=protected-access
    ie = SoundgasmIE('http://www.soundgasm.net/')
    # pylint: enable=protected-access
    assert ie is not None


# Generated at 2022-06-14 16:59:51.066575
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert not SoundgasmIE()._build_search_title_re('a')


# Generated at 2022-06-14 17:01:06.530918
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    sg = SoundgasmIE()
    assert hasattr(sg, '_VALID_URL'), "Missing mandatory member _VALID_URL"
    if sg._VALID_URL is not None:
        # Check if _VALID_URL is a regular expression
        assert re.match(sg._VALID_URL, sg._TEST['url']), "Invalid regular expression " + sg._VALID_URL
        # Check if _VALID_URL regex contains an appropriate group
        assert re.match(sg._VALID_URL, sg._TEST['url']).group(1) is not None, "Invalid regular expression " + sg._VALID_URL


# Generated at 2022-06-14 17:01:08.219946
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')

# Generated at 2022-06-14 17:01:09.428073
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    s = SoundgasmIE()
    print(str(s))

# Generated at 2022-06-14 17:01:12.256462
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    IE = SoundgasmIE()
    assert IE.IE_NAME == 'soundgasm'
    assert IE.VALID_URL == SoundgasmIE._VALID_URL


# Generated at 2022-06-14 17:01:15.589254
# Unit test for constructor of class SoundgasmProfileIE

# Generated at 2022-06-14 17:01:19.554512
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    test_class = SoundgasmProfileIE
    test_class.extract(test_class._TEST['url'])

# Generated at 2022-06-14 17:01:20.662917
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    SoundgasmProfileIE()

# Generated at 2022-06-14 17:01:27.053811
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE('http://soundgasm.net/u/ytdl/Piano-sample')
    assert '010082a2c802c5275bb00030743e75ad' == ie._download_webpage('http://soundgasm.net/u/ytdl/Piano-sample', None, '88abd86ea000cafe98f96321b23cc1206cbcbcc9')['md5']

if __name__ == "__main__":
    test_SoundgasmIE()

# Generated at 2022-06-14 17:01:28.779577
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE._TEST['url'] == 'http://soundgasm.net/u/ytdl'

# Generated at 2022-06-14 17:01:30.201567
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    try:
        SoundgasmIE()
    except ValueError:
        pass

# Generated at 2022-06-14 17:04:21.713935
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    s = SoundgasmIE()
    # test case for class initialize.
    assert s._VALID_URL == r'https?://(?:www\.)?soundgasm\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'


# Generated at 2022-06-14 17:04:24.753761
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ie = SoundgasmIE()
    assert (ie.IE_NAME == "soundgasm")


# Generated at 2022-06-14 17:04:26.087293
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    assert (SoundgasmIE().ie_key() == 'Soundgasm')

# Generated at 2022-06-14 17:04:27.047895
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    ae = SoundgasmIE()



# Generated at 2022-06-14 17:04:36.132438
# Unit test for constructor of class SoundgasmIE
def test_SoundgasmIE():
    # Create an instance of the class SoundgasmIE
    soundgasm = SoundgasmIE()
    # Function result of exercising
    test_result = soundgasm._real_extract('http://soundgasm.net/u/ytdl/Piano-sample')

    if test_result == {'id': '88abd86ea000cafe98f96321b23cc1206cbcbcc9',
                       'ext': 'm4a',
                       'title': 'Piano sample',
                       'description': 'Royalty Free Sample Music',
                       'uploader': 'ytdl',
                       'url': 'http://audio.soundgasm.net/u/ytdl/Piano-sample.m4a'}:
        print('Unit test for SoundgasmIE passed!')

# Generated at 2022-06-14 17:04:44.214748
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    ie = SoundgasmProfileIE('test')
    assert ie.ie_key() == 'Soundgasm:profile'
    assert ie.ie_name() == 'Soundgasm'
    assert ie.valid_url('http://soundgasm.net/u/ytdl')
    assert ie.valid_url('https://soundgasm.net/u/ytdl')
    assert ie.valid_url('https://soundgasm.net/u/ytdl#blah')
    assert ie.valid_url('https://soundgasm.net/u/ytdl/')

# Generated at 2022-06-14 17:04:50.006865
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    #Extracts the links to audios uploaded by a soundgasm profile (e.g. http://soundgasm.net/u/ytdl)
    s = SoundgasmProfileIE()
    #Testing with a profile that contains 1 audio
    links = s.extract('http://soundgasm.net/u/ytdl')
    assert len(links.get('entries', [])) == 1
    #Testing with a profile that contains 2 audios
    links = s.extract('http://soundgasm.net/u/mouser')
    assert len(links.get('entries', [])) == 2

# Generated at 2022-06-14 17:05:00.653567
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    class SoundgasmProfileIEUnitTest(SoundgasmProfileIE):
        def _real_extract(self, url):
            return super(SoundgasmProfileIEUnitTest, self)._real_extract(url)

    # Test normal use case
    ie = SoundgasmProfileIEUnitTest()
    test_url = 'http://soundgasm.net/u/ytdl'
    test_playlist = {
        'id': 'ytdl',
    }

    assert ie._real_extract(test_url)['entries'][0]['url'] == 'http://soundgasm.net/u/ytdl/Piano-sample'

# Generated at 2022-06-14 17:05:02.226235
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert isinstance(SoundgasmProfileIE(None), InfoExtractor)

# Generated at 2022-06-14 17:05:03.662224
# Unit test for constructor of class SoundgasmProfileIE
def test_SoundgasmProfileIE():
    assert SoundgasmProfileIE()._VALID_URL == SoundgasmProfileIE._VALID_URL