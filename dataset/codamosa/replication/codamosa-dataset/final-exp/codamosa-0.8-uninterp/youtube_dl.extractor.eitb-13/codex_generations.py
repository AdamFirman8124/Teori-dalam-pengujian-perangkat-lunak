

# Generated at 2022-06-14 16:03:05.502885
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:03:07.346694
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    assert eitb_ie is not None


# Generated at 2022-06-14 16:03:17.267866
# Unit test for constructor of class EitbIE
def test_EitbIE():
    '''
    Test for constructor of class EitbIE
    '''
    eitb_ie = EitbIE()
    assert eitb_ie.IE_NAME == "eitb.tv"
    assert eitb_ie.IE_DESC == 'EITB'
    assert eitb_ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:18.288670
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE() is not None

# Generated at 2022-06-14 16:03:23.578260
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    i = EitbIE(url)
    print(i._real_extract(url))

# Generated at 2022-06-14 16:03:27.270743
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE()._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:03:28.833772
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()


# Generated at 2022-06-14 16:03:29.955919
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie

# Generated at 2022-06-14 16:03:32.964690
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        e = EitbIE()
    except:
        assert False, "constructor must not return an exception"


# Generated at 2022-06-14 16:03:37.221357
# Unit test for constructor of class EitbIE
def test_EitbIE():
    video = EitbIE()
    assert video.IE_NAME == "eitb.tv"
    assert video._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:03:53.280709
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test one of the basic fields of class EitbIE
    # It has to return 'eitb.tv'
    assert EitbIE.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:03:55.258827
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test class EitbIE."""
    eitb_ie = EitbIE()
    pass

# Generated at 2022-06-14 16:04:02.563446
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitbIE = EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/");
    assert eitbIE.VALID_URL == 'http://www.eitb.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/%s' % EitbIE._VALID_URL;

# Generated at 2022-06-14 16:04:10.574269
# Unit test for constructor of class EitbIE
def test_EitbIE():
    'Test constructor of class EitbIE'
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    eitbie = EitbIE()
    assert eitbie.IE_NAME == 'eitb.tv'
    assert eitbie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:04:15.879521
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    EitbIE().suitable(url)

# Generated at 2022-06-14 16:04:21.242076
# Unit test for constructor of class EitbIE
def test_EitbIE():
    e = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert e.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:04:25.562206
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

# Generated at 2022-06-14 16:04:32.047757
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """Test EitbIE constructor"""
    IE_TEST = EitbIE()

    assert IE_TEST.IE_NAME == 'eitb.tv'
    assert IE_TEST._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'



# Generated at 2022-06-14 16:04:35.641475
# Unit test for constructor of class EitbIE
def test_EitbIE():
   ie = EitbIE()
   assert ie._VALID_URL == "http://www.eitb.tv/(?:eu/bideoa|es/video)/[^/]+/\\d+/(?P<id>\\d+)"


# Generated at 2022-06-14 16:04:45.882479
# Unit test for constructor of class EitbIE
def test_EitbIE():
    print('Testing constructor for class EitbIE')
    print('Testing EitbIE._VALID_URL')
    assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    print('Testing EitbIE._TEST')

# Generated at 2022-06-14 16:05:04.031025
# Unit test for constructor of class EitbIE
def test_EitbIE():

    # Testing the constructor with a valid URL
    EitbIE_v = EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert EitbIE_v.ie_key() == 'eitb.tv'
    assert EitbIE_v.ie_name() == 'Eitb'



# Generated at 2022-06-14 16:05:07.816993
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE("http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")

# Generated at 2022-06-14 16:05:09.051979
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert EitbIE()._VALID_URL == EitbIE._VALID_URL

# Generated at 2022-06-14 16:05:16.615234
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # test valid url
    valid_url = 'http://www.eitb.tv/eu/bideoa/bideoak/60-minutos-60-minutos/253806/'
    result = EitbIE()._real_initialize()
    assert result == True
    result = EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert result == True

# Generated at 2022-06-14 16:05:22.218993
# Unit test for constructor of class EitbIE
def test_EitbIE():
    base_link='https://www.eitb.tv/eu/noticias/deportes/detalle/2707284'
    ie = EitbIE()
    ie._match_id(base_link)
    ie._download_json(base_link, video_id='test_video')
    ie._download_webpage(base_link, video_id='test_video')
    ie._real_extract(base_link)

# Generated at 2022-06-14 16:05:30.857844
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

    # In the constructor we must initialize one or more attributes
    # first:
    assert ie._VALID_URL is not None
    assert ie._TEST is not None

    # Also, test_* should not be called by constructor
    assert ie._test_suite is None
    assert ie._downloader is None

    # If we are here, test has passed

# Generated at 2022-06-14 16:05:39.839038
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    ie = EitbIE(EitbIE.IE_NAME)
    info_dict = ie.extract(url)
    assert info_dict['id'] == '4090227752001'
    assert info_dict['ext'] == 'mp4'
    assert info_dict['title'] == '60 minutos (Lasa y Zabala, 30 años)'
    assert info_dict['description'] == 'Programa de reportajes de actualidad.'
    assert info_dict['duration'] == 3996.76
    assert info_dict['timestamp'] == 1381789

# Generated at 2022-06-14 16:05:43.144921
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert eitb.extract(EitbIE._TEST['url']) == EitbIE._TEST['info_dict']

# Generated at 2022-06-14 16:05:44.724154
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE().IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:05:46.466277
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # Test instantiation
    ie = EitbIE()
    assert(ie is not None)



# Generated at 2022-06-14 16:06:18.237750
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
# Test for method _real_extract of class EitbIE

# Generated at 2022-06-14 16:06:28.376286
# Unit test for constructor of class EitbIE
def test_EitbIE():
    global IE_NAME, _VALID_URL
    IE_NAME = 'eitb.tv'
    _VALID_URL = r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

    ie = EitbIE()
    video = ie._real_extract(_TEST['url'])

    assert video['id'] == _TEST['info_dict']['id']
    assert video['title'] == _TEST['info_dict']['title']
    assert video['description'] == _TEST['info_dict']['description']
    assert video['duration'] == _TEST['info_dict']['duration']

# Generated at 2022-06-14 16:06:32.965572
# Unit test for constructor of class EitbIE
def test_EitbIE():
    from ytdl.extractor.common import InfoExtractor
    from ytdl.utils import sanitized_Request
    eitb_ie = EitbIE('www.eitb.tv', InfoExtractor, {}, sanitized_Request)
    assert eitb_ie != None


# Generated at 2022-06-14 16:06:33.541885
# Unit test for constructor of class EitbIE
def test_EitbIE():
	assert True

# Generated at 2022-06-14 16:06:43.363632
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE('http://www.eitb.tv/eu/bideoa/gazteak-gastronomia/14890/bideoak/gorri-gazpacho-danok-erantzun/')
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:06:45.959453
# Unit test for constructor of class EitbIE
def test_EitbIE():
    try:
        EitbIE()
    except Exception as e:
        assert False, 'Test for creating constructor for class EitbIE fails with exception: ' + repr(e)

# Generated at 2022-06-14 16:06:56.549041
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb_ie = EitbIE()
    # Assert member variables have been correctly initialized
    assert eitb_ie.ie_key() == "EitbIE"
    assert eitb_ie.ie_name() == "eitb.tv"
    assert eitb_ie.valid_url("http://www.eitb.tv/eu/video/gaur/4090227713001/") == True
    assert eitb_ie.valid_url("http://www.eitb.tv/eu/video/gaur/4090227713001/4090227610001/") == False
    assert eitb_ie.valid_url("http://www.eitb.tv/eu/video/gaur/4090227713001") == False

# Generated at 2022-06-14 16:06:59.931152
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/',{})

# Generated at 2022-06-14 16:07:01.448210
# Unit test for constructor of class EitbIE
def test_EitbIE():
    obj = EitbIE()

# Generated at 2022-06-14 16:07:02.077097
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE

# Generated at 2022-06-14 16:08:24.561178
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:30.710473
# Unit test for constructor of class EitbIE
def test_EitbIE():
    video_url = 'http://www.eitb.tv/eu/bideoa/egunkaria/6986/4568/'
    video_id = '4568'
    importer = EitbIE(EitbIE.IE_NAME, video_url)
    regexp = r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert importer._VALID_URL == regexp
    assert importer._match_id(video_url) == video_id


# Generated at 2022-06-14 16:08:32.618430
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie


# Generated at 2022-06-14 16:08:37.066959
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'


# Generated at 2022-06-14 16:08:47.341634
# Unit test for constructor of class EitbIE
def test_EitbIE():
    eitb = EitbIE()
    assert(eitb.IE_NAME == 'eitb.tv')
    assert(eitb._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)')

# Generated at 2022-06-14 16:08:49.124235
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'

# Generated at 2022-06-14 16:08:52.642991
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'

# Generated at 2022-06-14 16:08:53.872372
# Unit test for constructor of class EitbIE
def test_EitbIE(): 
    EitbIE()

# Generated at 2022-06-14 16:08:55.492838
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie
    return ie


# Generated at 2022-06-14 16:09:01.971129
# Unit test for constructor of class EitbIE
def test_EitbIE():
    url = "http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/"
    eitb_video = EitbIE()._real_extract(url)

    assert eitb_video['title'] == '60 minutos (Lasa y Zabala, 30 años)'

# Generated at 2022-06-14 16:12:08.970437
# Unit test for constructor of class EitbIE

# Generated at 2022-06-14 16:12:10.025867
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE()

# Generated at 2022-06-14 16:12:17.372899
# Unit test for constructor of class EitbIE
def test_EitbIE():
    # test EitbIE
    video_url = 'http://www.eitb.tv/eu/bideoa/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    eitb_IE = EitbIE()
    # test _real_extract()
    eitb_IE._real_extract(video_url)
    # test EitbIE._real_extract(url)
    eitb_IE.extract(video_url)

# Generated at 2022-06-14 16:12:22.636883
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')

if __name__ == '__main__':
    test_EitbIE()

# Generated at 2022-06-14 16:12:23.984093
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie != None


# Generated at 2022-06-14 16:12:28.103308
# Unit test for constructor of class EitbIE
def test_EitbIE():
    EitbIE("http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/")


# Generated at 2022-06-14 16:12:29.536804
# Unit test for constructor of class EitbIE
def test_EitbIE():
    assert EitbIE.IE_NAME == 'eitb.tv'


# Generated at 2022-06-14 16:12:31.089754
# Unit test for constructor of class EitbIE
def test_EitbIE():
    """
    Constructor of test cases for EitbIE class
    """
    return EitbIE()

# Generated at 2022-06-14 16:12:37.292492
# Unit test for constructor of class EitbIE
def test_EitbIE():
  assert EitbIE._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
  assert EitbIE.IE_NAME == 'eitb.tv'

  ie = EitbIE()
  assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
  assert ie.IE_NAME == 'eitb.tv'



# Generated at 2022-06-14 16:12:38.291899
# Unit test for constructor of class EitbIE
def test_EitbIE():
    ie = EitbIE()
    assert ie.IE_NAME == 'EITB'