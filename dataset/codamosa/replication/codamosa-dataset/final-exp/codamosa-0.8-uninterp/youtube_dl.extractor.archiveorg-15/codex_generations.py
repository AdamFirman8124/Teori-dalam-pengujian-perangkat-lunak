

# Generated at 2022-06-14 16:03:08.809519
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    r = ArchiveOrgIE(ArchiveOrgIE.IE_NAME, ArchiveOrgIE.IE_DESC)
    if r.IE_NAME != ArchiveOrgIE.IE_NAME:
        print('ERROR: ArchiveOrgIE.name() returns ' + r.IE_NAME)
    if r.IE_DESC != ArchiveOrgIE.IE_DESC:
        print('ERROR: ArchiveOrgIE.description() returns ' + r.IE_DESC)

# Generated at 2022-06-14 16:03:17.304580
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ArchiveOrgIE.suitable('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert not ArchiveOrgIE.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect/')
    assert ArchiveOrgIE.suitable('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert ArchiveOrgIE.suitable('https://archive.org/details/Cops1922')

# Generated at 2022-06-14 16:03:20.550155
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from . import archiveorg
    # Constructor should return a ArchiveOrgIE object
    obj = archiveorg.ArchiveOrgIE()
    # Check that the IE object is an instance of ArchiveOrgIE
    assert isinstance(obj, archiveorg.ArchiveOrgIE)
    # Check that the IE object is an instance of InfoExtractor
    assert isinstance(obj, InfoExtractor)

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:03:22.237129
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert(ie != None)

# Generated at 2022-06-14 16:03:25.764623
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    info_extractor = ArchiveOrgIE()
    info_extractor._match_id(url)

# Generated at 2022-06-14 16:03:37.300574
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	from youtube_dl.YoutubeDL import YoutubeDL
	from youtube_dl.options import Options
	from youtube_dl.YoutubeDLProcessor import YoutubeDLProcessor
	from youtube_dl.FileDownloader import FileDownloader
	from youtube_dl.utils import YoutubeDLHandler
	from youtube_dl.postprocessor import FFmpegMergeFilesPP
	from youtube_dl.FFmpegPostProcessor import FFmpegPostProcessor
	from youtube_dl.postprocessor import FFmpegMetadataPP
	from youtube_dl.downloader.rtmp import RTMPFD
	from youtube_dl.downloader.external.ExternalFD import ExternalFD
	from youtube_dl import YoutubeDL
	from youtube_dl.compat import (
		compat_urlopen,
		compat_urllib_error
	)


# Generated at 2022-06-14 16:03:42.521741
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:45.912528
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    result = ArchiveOrgIE()
    assert result.IE_NAME == 'archive.org'
    assert result.IE_DESC == 'archive.org videos'
    assert result._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:52.689896
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()

    instance_internetarchive = instance.InternetArchiveIE()
    assert(isinstance(instance_internetarchive, instance.InternetArchiveIE))

    instance_jwplayer = instance.JWPlayerIE()
    assert(isinstance(instance_jwplayer, instance.JWPlayerIE))

    instance_html5media = instance.Html5MediaIE()
    assert(isinstance(instance_html5media, instance.Html5MediaIE))

# Generated at 2022-06-14 16:04:03.588784
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.ie_key() == 'archive.org'
    assert ie.video_id == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie.webpage_url == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie.playlist_id is None
    assert ie.playlist_title == 'Videos matching query: XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie.playlist_description is None
    assert ie.playlist_url is None
    assert ie._search_regex is not None
    assert ie

# Generated at 2022-06-14 16:04:14.661172
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:18.078266
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    print('Completed unit testing for archive.org')

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:04:29.270179
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    modules = ['archive']
    returns = [None]
    module_paths = [None]
    args = [None]
    temp_modules = [None]
    try:
        import importlib
        from importlib import reload
        from importlib import find_loader
        from sys import modules
        for module_key in modules:
            if module_key in modules:
                temp_modules.append(modules[module_key])
                del modules[module_key]
                if find_loader(module_key) is None:
                    module = importlib.import_module(module_key)
                    modules[module_key] = module
                    returns.append(module)
                else:
                    reload(modules[module_key])
                    returns.append(modules[module_key])
    except Exception as e:
        module_paths.append

# Generated at 2022-06-14 16:04:38.801351
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert len(ie._TESTS) == 4
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'
    info_dict = ie._TESTS[0]['info_dict']

# Generated at 2022-06-14 16:04:40.708038
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archive = ArchiveOrgIE()
    assert archive



# Generated at 2022-06-14 16:04:50.713425
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie._match_id('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect') == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    metadata = ie._download_json('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'XD300-23_68HighlightsAResearchCntAugHumanIntellect', query={
                'output': 'json',
            })['metadata']
    assert metadata['title'] == ['1968 Demo - FJCC Conference Presentation Reel #1']

# Generated at 2022-06-14 16:04:54.748091
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:04:58.164351
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	from .common import InfoExtractor
	ie = InfoExtractor(None, {})
	# Exercise the constructor


if __name__ == '__main__':
	test_ArchiveOrgIE()

# Generated at 2022-06-14 16:05:04.097020
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test the constructor with valid input
    assert ArchiveOrgIE.suitable('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

    # Test the constructor with invalid input
    assert not ArchiveOrgIE.suitable('https://www.youtube.com/watch?v=TEST')

# Generated at 2022-06-14 16:05:13.218276
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == "archive.org"
    assert ie.IE_DESC == "archive.org videos"
    assert ie._VALID_URL == "https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)"
    assert ie._TESTS[0]["url"] == "http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    assert ie._TESTS[0]["md5"] == "8af1d4cf447933ed3c7f4871162602db"
    assert ie._TESTS[0]["info_dict"]["id"] == "XD300-23_68HighlightsAResearchCntAugHumanIntellect"

# Generated at 2022-06-14 16:05:34.920001
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:35.337392
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    infoExtractor = ArchiveOrgIE()

# Generated at 2022-06-14 16:05:36.362066
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    _info = 'http://www.youtube.com/watch?v=wjxOFk-lt_Q'



# Generated at 2022-06-14 16:05:39.471009
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archiveOrgIE = ArchiveOrgIE()
    print(archiveOrgIE._VALID_URL)
    print(archiveOrgIE._TESTS )
    # print(archiveOrgIE._download_webpage())
    # print(archiveOrgIE._extract_info())


# Generated at 2022-06-14 16:05:40.335454
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE(None)

# Generated at 2022-06-14 16:05:41.468252
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie

# Generated at 2022-06-14 16:05:42.772464
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:47.806239
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    x = ArchiveOrgIE()
    print(x.IE_DESC)
    assert x.IE_NAME == 'archive.org'
    assert x.IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:50.055697
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ie._TESTS[0]['url']

# Generated at 2022-06-14 16:05:51.108754
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie

# Generated at 2022-06-14 16:06:19.802827
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:21.820616
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:06:25.343403
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info_extractor = InfoExtractor.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert isinstance(info_extractor, ArchiveOrgIE)

# Generated at 2022-06-14 16:06:35.972111
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # test archive.org url
    url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect?start=100&end=110'
    result = ArchiveOrgIE()._extract_urls(url, test=True)
    assert result == ['https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect']

    # test archive.org embed url
    url = 'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    result = ArchiveOrgIE()._extract_urls(url, test=True)
    assert result == ['http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect']

# Generated at 2022-06-14 16:06:45.013620
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Unit test for constructor of class ArchiveOrgIE.
    """

    # Success test case 1
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    ie = ArchiveOrgIE(url)
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:06:56.083770
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ArchiveOrgIE().IE_NAME == 'archive.org'
    assert ArchiveOrgIE().IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE()._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ArchiveOrgIE()._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'

# Generated at 2022-06-14 16:07:04.300344
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_desc() == 'archive.org videos'
    assert ie.valid_url('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.valid_url('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.valid_url('https://archive.org/details/Cops1922')
    assert ie.valid_url('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert ie.valid_url('http://archive.org/Inval1d_URL') is False

# Generated at 2022-06-14 16:07:14.359697
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    params = dict()
    params["url"] = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    params["md5"] = '8af1d4cf447933ed3c7f4871162602db'
    params["info_dict"] = dict()
    params["info_dict"]["id"] = 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    params["info_dict"]["ext"] = 'ogg'
    params["info_dict"]["title"] = '1968 Demo - FJCC Conference Presentation Reel #1'
    params["info_dict"]["description"] = 'md5:da45c349df039f1cc8075268eb1b5c25'

# Generated at 2022-06-14 16:07:14.871528
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:16.066181
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert(issubclass(ArchiveOrgIE, InfoExtractor))

# Generated at 2022-06-14 16:08:21.131304
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archiveOrg = ArchiveOrgIE()
    assert archiveOrg._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:08:22.077177
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archive_ie = ArchiveOrgIE()


# Generated at 2022-06-14 16:08:26.837643
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    try:
        ie.suitable('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
        ie.suitable('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    except TypeError as e:
        assert "unexpected keyword argument" in str(e)



# Generated at 2022-06-14 16:08:28.211751
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'


# Generated at 2022-06-14 16:08:29.846383
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:08:38.766085
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.name == 'archive.org'
    assert ie.description == 'archive.org videos'
    assert ie.valid_urls == ['http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'https://archive.org/details/Cops1922', 'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/']
    assert ie.ie_key() == 'archive.org'

# Generated at 2022-06-14 16:08:39.790861
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test if constructor works
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:08:41.382268
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    o = ArchiveOrgIE()
    assert o.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:08:43.190738
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:08:43.775981
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:10:58.597130
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info_extractor = ArchiveOrgIE()
    info_extractor._extract()

# Generated at 2022-06-14 16:11:01.528723
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == '(?i)https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:11:02.852874
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # This test would fail if this class threw any exception
    instance = ArchiveOrgIE()
    instance.IE_NAME

# Generated at 2022-06-14 16:11:03.692692
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    pass

# Generated at 2022-06-14 16:11:04.404217
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:11:11.108159
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    instance = ie.IE_CLASS(ie.ie_key())

    assert ie.ie_key() == ArchiveOrgIE.ie_key()
    assert ie.IE_CLASS.__name__ == ArchiveOrgIE.IE_NAME
    assert instance.ie_key() == ArchiveOrgIE.ie_key()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert str(ie)[8:] == 'archive.org'

# Generated at 2022-06-14 16:11:15.275909
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:11:16.078154
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()


# Generated at 2022-06-14 16:11:19.641009
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Creating the ArchiveOrgIE object with url as None should raise
    ValueError if url is None
    """

    info_extractor = ArchiveOrgIE(None)
    try:
        info_extractor.extract(None)
    except ValueError:
        pass
    else:
        raise Exception("Creating the ArchiveOrgIE object with url as None should raise ValueError if url is None")

# Generated at 2022-06-14 16:11:20.525671
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Check constructor doesn't throw exception
    ArchiveOrgIE()