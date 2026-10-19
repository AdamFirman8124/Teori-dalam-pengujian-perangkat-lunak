

# Generated at 2024-03-18 09:08:18.843834
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:08:24.555223
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
   

# Generated at 2024-03-18 09:08:31.429402
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Create an instance of the EitbIE class
    ie = EitbIE()

    # Check if the instance is indeed an instance of EitbIE and its superclass
    assert isinstance(ie, EitbIE), "Should be an instance of EitbIE"
    assert isinstance(ie, InfoExtractor), "Should be an instance of InfoExtractor"

    # Check if the IE_NAME is correctly set
    assert ie.IE_NAME == 'eitb.tv', "IE_NAME should be 'eitb.tv'"

    # Check if the _VALID_URL is correctly set
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)', "_VALID_URL pattern does not match"

    # Check if the _TEST dictionary is correctly set
    assert ie._

# Generated at 2024-03-18 09:08:38.944953
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:08:46.622662
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()

    # Check if the instance is created properly

# Generated at 2024-03-18 09:08:53.837669
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:09:01.184642
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:09:07.657112
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
   

# Generated at 2024-03-18 09:09:19.641490
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie.suitable('http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/')
    assert not ie.suitable('http://www.youtube.com/watch?v=7u8mheM2Hrg')

# Generated at 2024-03-18 09:09:27.805133
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:09:49.932387
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:09:57.950994
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:10:09.476088
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:10:19.343650
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert 'url' in ie._TEST
    assert 'md5' in ie._TEST
    assert 'info_dict' in ie._TEST
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2024-03-18 09:10:25.575192
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:10:36.110035
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()

    # Check if the instance is created properly

# Generated at 2024-03-18 09:10:42.853926
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:10:50.009253
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:10:56.491475
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:11:04.697905
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
   

# Generated at 2024-03-18 09:11:44.005244
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:11:53.503504
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:12:02.079860
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
   

# Generated at 2024-03-18 09:12:08.979435
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:12:18.072777
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:12:33.053056
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()

    # Check if the IE_NAME is correctly set

# Generated at 2024-03-18 09:12:45.126770
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()

    # Check if the instance is created properly

# Generated at 2024-03-18 09:12:49.768588
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert isinstance(ie, InfoExtractor)


# Generated at 2024-03-18 09:12:56.779942
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
   

# Generated at 2024-03-18 09:13:04.118005
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()

    # Check if the instance is created properly

# Generated at 2024-03-18 09:14:18.548653
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert 'url' in ie._TEST
    assert 'md5' in ie._TEST
    assert 'info_dict' in ie._TEST
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2024-03-18 09:14:28.937509
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert 'url' in ie._TEST
    assert 'md5' in ie._TEST
    assert 'info_dict' in ie._TEST
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2024-03-18 09:14:42.329306
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
   

# Generated at 2024-03-18 09:14:49.552912
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:14:55.868895
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert 'url' in ie._TEST
    assert 'md5' in ie._TEST
    assert 'info_dict' in ie._TEST
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'

# Generated at 2024-03-18 09:15:03.278943
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:15:12.822824
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()

    # Check if the instance is created properly

# Generated at 2024-03-18 09:15:20.454291
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()

    # Check if the instance is created properly

# Generated at 2024-03-18 09:15:33.451328
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for EitbIE constructor
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'
    assert ie._TEST['info_dict']['ext'] == 'mp4'
   

# Generated at 2024-03-18 09:15:41.903669
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()


# Generated at 2024-03-18 09:17:50.815107
# Unit test for constructor of class EitbIE
def test_EitbIE():    ie = EitbIE()

    # Check if the instance is created properly

# Generated at 2024-03-18 09:17:58.476531
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'
    assert ie._TEST['info_dict']['id'] == '4090227752001'

# Generated at 2024-03-18 09:18:04.948592
# Unit test for constructor of class EitbIE
def test_EitbIE():    # Test case for the constructor of EitbIE
    ie = EitbIE()
    assert ie.IE_NAME == 'eitb.tv'
    assert ie._VALID_URL == r'https?://(?:www\.)?eitb\.tv/(?:eu/bideoa|es/video)/[^/]+/\d+/(?P<id>\d+)'
    assert 'url' in ie._TEST
    assert 'md5' in ie._TEST
    assert 'info_dict' in ie._TEST
    assert ie._TEST['url'] == 'http://www.eitb.tv/es/video/60-minutos-60-minutos-2013-2014/4104995148001/4090227752001/lasa-y-zabala-30-anos/'
    assert ie._TEST['md5'] == 'edf4436247185adee3ea18ce64c47998'