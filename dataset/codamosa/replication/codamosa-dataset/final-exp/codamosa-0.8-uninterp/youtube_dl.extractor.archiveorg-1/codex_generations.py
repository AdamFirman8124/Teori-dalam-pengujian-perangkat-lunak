

# Generated at 2022-06-14 16:03:06.218255
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    ArchiveOrgIE(url, 'archive.org')
    return 0

# Generated at 2022-06-14 16:03:08.799541
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assertBeInstanceOf(ie, InfoExtractor)
    assertBeInstanceOf(ie, ie.__class__)
    assertBeInstanceOf(ie, ie.__class__.__base__)

# Generated at 2022-06-14 16:03:10.209667
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Test ArchiveOrgIE."""
    pass

# Generated at 2022-06-14 16:03:20.251016
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:25.271198
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:36.831162
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

    # Check capabilities
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:37.340273
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:40.153432
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_ArchiveOrgIE = ArchiveOrgIE()
    assert isinstance(test_ArchiveOrgIE, ArchiveOrgIE)

# Generated at 2022-06-14 16:03:47.692448
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    #TODO:get_valid_urls
    ##assert ie.get_valid_urls() == ['https://archive.org/details/Cops1922', 'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/', 'https://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'http://archive.org/embed/XD300-23_68HighlightsAR

# Generated at 2022-06-14 16:03:51.281296
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for constructor of class ArchiveOrgIE"""
    # pylint: disable=protected-access
    archive_org_ie = ArchiveOrgIE()
    assert(archive_org_ie._download_json == InfoExtractor._download_json)

# Generated at 2022-06-14 16:04:04.988820
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'


# Generated at 2022-06-14 16:04:10.620737
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:16.366695
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME=='archive.org'
    assert ArchiveOrgIE().IE_DESC=='archive.org videos'
    assert ArchiveOrgIE()._VALID_URL==r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:04:18.594168
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    inst = ArchiveOrgIE()
    inst.initialize()
    assert inst.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:04:20.081209
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_ArchiveOrgIE.test_instance = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:23.316386
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE.suitable('https://archive.org/details/Isekai-Wa-Smartphone-To-Tominaga-Iru-OP-Dance-Tenshi-no-Clover-')

# Generated at 2022-06-14 16:04:25.661532
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE._VALID_URL == ArchiveOrgIE.__dict__['_VALID_URL']

# Generated at 2022-06-14 16:04:26.602675
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()


# Generated at 2022-06-14 16:04:29.484524
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert(ie.IE_NAME == "archive.org")
    assert(ie.IE_DESC == "archive.org videos")

# Generated at 2022-06-14 16:04:30.438864
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:46.203168
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'
    assert ArchiveOrgIE().IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE()._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ArchiveOrgIE().IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:04:47.938384
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for constructor of class ArchiveOrgIE
    """
    ie = ArchiveOrgIE()
    print (ie)

# Generated at 2022-06-14 16:04:51.380695
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:52.578079
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:04:57.517804
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj.IE_NAME == 'archive.org'
    assert obj.IE_DESC == 'archive.org videos'
    assert obj._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert obj._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'


# Generated at 2022-06-14 16:04:58.832362
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:05:03.317602
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    print(ie.ie_key())
    print(ie.extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'))

# Generated at 2022-06-14 16:05:07.503833
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    inst = ArchiveOrgIE()
    assert inst.IE_NAME == ArchiveOrgIE.IE_NAME
    assert inst.IE_DESC == ArchiveOrgIE.IE_DESC
    assert inst._VALID_URL == ArchiveOrgIE._VALID_URL
    assert inst._TESTS == ArchiveOrgIE._TESTS

# Generated at 2022-06-14 16:05:08.759137
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:05:16.411085
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('http://archive.org', 'video.com/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:42.741420
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .test_imports import unittest
    class TestArchiveOrgIE(unittest.TestCase):
        def test_constructor(self):
            from .extractors.common import InfoExtractor
            # Test exception when there's no video_id
            self.assertRaises(TypeError, ArchiveOrgIE)
            # Test exception when video_id is not basestring
            self.assertRaises(TypeError, ArchiveOrgIE, [])
            # Test right InfoExtractor is returned
            obj = ArchiveOrgIE('video_id')
            self.assertIsInstance(obj, InfoExtractor)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestArchiveOrgIE)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-14 16:05:44.379134
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:05:52.096038
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # This test checks the constructor for class ArchiveOrgIE
    # (this test was written based on _VALID_URL)
    import re
    input_url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    result_match = re.match(ArchiveOrgIE._VALID_URL, input_url)
    assert result_match
    assert result_match.group('id') == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:05:56.973797
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

    assert ie._valid_url('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect') == True
    assert ie._valid_url('http://archive.org/bogus/') == False


# Generated at 2022-06-14 16:06:01.171255
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:01.517845
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:06:02.588331
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Test whether object is initialized properly"""
    ArchiveOrgIE()

# Generated at 2022-06-14 16:06:04.642618
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except:
        assert False
    else:
        assert True


# Generated at 2022-06-14 16:06:05.173792
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:06:06.652459
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE('archive.org', 'archive.org videos')

# Generated at 2022-06-14 16:06:51.225828
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:07:00.555596
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import fnmatch

    test_list = [
        ('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect',
         '8af1d4cf447933ed3c7f4871162602db'),
        ('http://archive.org/details/Cops1922',
         '0869000b4ce265e8ca62738b336b268a')
    ]
    for test_t in test_list:
        extractor = ArchiveOrgIE()
        app_info = extractor._real_extract(test_t[0])
        assert 'url' in app_info
        assert app_info['md5'] == test_t[1]


# Generated at 2022-06-14 16:07:01.078441
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:04.168012
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Test ArchiveOrgIE constructor."""
    assert ArchiveOrgIE._VALID_URL is not None
    assert ArchiveOrgIE.IE_NAME is not None
    assert ArchiveOrgIE.IE_DESC is not None
    assert ArchiveOrgIE.ie is not None

# Generated at 2022-06-14 16:07:07.016034
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_DESC
    ie.IE_NAME
    ie.RELEASE_DATE_FORMATS
    ie.__call__()

# Generated at 2022-06-14 16:07:16.249220
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:16.984944
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()._VALID_URL == ArchiveOrgIE._VALID_URL

# Generated at 2022-06-14 16:07:22.837389
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:32.494451
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE(None)
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_desc() == 'archive.org videos'
    assert ie.has_metadata('XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.has_metadata('https://archive.org/details/Cops1922')
    assert ie.has_metadata('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.has_metadata('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')

# Generated at 2022-06-14 16:07:34.726519
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except:
        assert False


# Generated at 2022-06-14 16:09:29.865257
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	pass

# Generated at 2022-06-14 16:09:33.704092
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Testing the with no URL
    try:
        ArchiveOrgIE()
        assert False
    except TypeError:
        assert True
    # Testing the with invalid value for URL
    try:
        ArchiveOrgIE('abc')
        assert False
    except TypeError:
        assert True
    # Testing the with valid value for URL
    assert ArchiveOrgIE('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:09:38.341977
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie._VALID_URL == 'https?://(?:www\\.)?archive\\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:09:43.827058
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:09:45.662579
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    arch = ArchiveOrgIE()
    assert arch.IE_NAME == 'archive.org' and arch.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:09:46.160025
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:09:46.767799
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:09:49.138206
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'


# Generated at 2022-06-14 16:09:52.165873
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_DESC = 'test desc'
    ie.IE_NAME = 'test name'
    ie._VALID_URL = 'test'
    ie._TESTS = []
    assert ie._real_extract('test') == {}

# Generated at 2022-06-14 16:09:55.631353
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
