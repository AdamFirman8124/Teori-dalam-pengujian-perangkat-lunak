

# Generated at 2022-06-14 15:23:31.763655
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:23:43.456277
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:23:53.230198
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:23:59.163486
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    """
    Test removing from the list media elements with attribute
    "drmAdditionalHeaderId" or "drmAdditionalHeaderSetId".
    """

# Generated at 2022-06-14 15:24:11.021466
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:24:18.280388
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from .test_fragments import bootstrap_info
    bootstrap_info_reader = FlvReader(compat_b64decode(bootstrap_info))
    # This test is not exhaustive yet
    assert (
        bootstrap_info_reader.read_bootstrap_info() == {
            'fragments': [{
                'fragments': [{
                    'duration': 4096,
                    'first': 1,
                    'ts': 0,
                    'discontinuity_indicator': None,
                }],
            }],
            'segments': [{
                'segment_run': [(1, 1)],
            }],
            'live': False,
        }
    )



# Generated at 2022-06-14 15:24:28.725992
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:24:37.454263
# Unit test for function get_base_url
def test_get_base_url():
    base_url = 'http://example.com/streams/'
    manifest = compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
        '<baseURL>{0}</baseURL></manifest>'.format(base_url))
    assert get_base_url(manifest) == base_url
    manifest = compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0"/>')
    assert get_base_url(manifest) is None

# Generated at 2022-06-14 15:24:42.183215
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from .common import load_bootstrap_info

    url = 'https://vod.llnw.cdn.llnwd.net/e1/uds/pd/20200323/20200323_13970/20200323_13970.bootstrap'
    bootstrap_info = load_bootstrap_info(url)
    # FlvReader(bootstrap_info).read_bootstrap_info()



# Generated at 2022-06-14 15:24:53.013577
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    abs_info = FlvReader(open('test/test.bootstrap', 'rb').read()).read_bootstrap_info()

# Generated at 2022-06-14 15:25:20.517325
# Unit test for function build_fragments_list
def test_build_fragments_list():
    assert build_fragments_list({
        'segments': [{
            'segment_run': [
                (0, 4),
            ],
        }],
        'fragments': [{
            'fragments': [
                {'first': 1},
            ],
        }],
        'live': False,
    }) == [(0, 1), (0, 2), (0, 3), (0, 4)]

# Generated at 2022-06-14 15:25:31.837301
# Unit test for function build_fragments_list
def test_build_fragments_list():
    # Tests for VOD
    assert build_fragments_list({
        'segments': [{
            'segment_run': [
                (1, 10)
            ]
        }],
        'fragments': [{
            'fragments': [
                {'first': 1, 'ts': 100, 'duration': 1, 'discontinuity_indicator': None},
            ]
        }],
        'live': False,
    }) == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)]


# Generated at 2022-06-14 15:25:41.913236
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    media = [
        {
            'url': 'video.mp4',
            'drmAdditionalHeaderId': '',
        },
        {
            'url': 'video2.mp4',
            'another_element': '',
        },
        {
            'url': 'video3.mp4',
            'drmAdditionalHeaderId': '',
            'drmAdditionalHeaderSetId': '',
        },
        {
            'url': 'video4.mp4',
        },
    ]
    expected = [
        {
            'url': 'video2.mp4',
            'another_element': '',
        },
        {
            'url': 'video4.mp4',
        },
    ]
    assert remove_encrypted_media(media) == expected



# Generated at 2022-06-14 15:25:51.173196
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from .fragment import parse_manifest
    from ..utils import determine_ext
    from .common import FileDownloader
    from ..extractor import gen_extractors, get_info_extractor

    url = 'https://hls.goodgame.ru/hls/475426.m3u8'
    print('URL: %s' % url)
    ie = get_info_extractor(url)
    downloader = FileDownloader({})
    ie.downloader = downloader
    ext = determine_ext(ie.url)

    def test_item(url, ie, ext, downloader):
        manifest = parse_manifest(downloader.cache.load(ie._download_webpage_handle(url, 'initial')))

# Generated at 2022-06-14 15:26:00.863918
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:26:08.208866
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    # If a bootstrap info has no protected media, it returns the same info
    protected_media = [
        {'url': 'protected_url', 'drmAdditionalHeaderId': 'headerId'},
        {'url': 'notProtected_url', 'drmAdditionalHeaderId': 'headerId'}
    ]
    not_protected_media = [
        {'url': 'notProtected_url2', 'drmAdditionalHeaderId': 'headerId'},
    ]
    assert (remove_encrypted_media(protected_media) ==
            remove_encrypted_media(not_protected_media))



# Generated at 2022-06-14 15:26:18.062033
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:26:28.394023
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    media_encrypted = ['<media url="media_encrypted_0.f4f" bitrate="84819" streamId="video" bootstrapInfoId="bootstrap84819" width="720" height="404" drmAdditionalHeaderId="id_ec_header" drmAdditionalHeaderSetId="id_ec_header_set" />']
    media_not_encrypted = ['<media url="media_not_encrypted_0.f4f" bitrate="84819" streamId="video" bootstrapInfoId="bootstrap84819" width="720" height="404" />']
    expected_output = media_not_encrypted

    output = remove_encrypted_media(media_encrypted)
    assert output == expected_output


# Generated at 2022-06-14 15:26:30.224882
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    with open('tests/f4m/example.f4m', 'rb') as f:
        res = F4mFD()._real_download(
            "example.flv", {"url": "http://example.com/example.f4m"}, f.read()
        )
    assert res

# Generated at 2022-06-14 15:26:35.164659
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():

    # First test run
    def test_real_download_first(self):
        self.real_download("/tmp/test.flv", {'url': "http://test/test.f4m", 'tbr': None})

    F4mFD.real_download = test_real_download_first

    # Second test run
    def test_real_download_second(self):
        self.real_download("/tmp/test.flv", {'url': "http://test/test.f4m", 'tbr': None})

    F4mFD.real_download = test_real_download_second

    # Initialize YoutubeDL object
    ydl_opts = {}
    ydl = YoutubeDL(ydl_opts)

    # Initialize F4mFD object
    f4m_fd = F4m

# Generated at 2022-06-14 15:26:59.922235
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    # The test data is generated by running the following command:
    #   ffmpeg -r 1 -i http://devimages.apple.com/iphone/samples/bipbop/gear1/prog_index.m3u8 -map 0 -codec copy -f flv -
    # and then extracting the data from the two boxes (asrt and afrt), located at the offset starting with 0x29C
    # The data is encoded as hex string and base64 encoded in order to save space, and then decoded here for testing.
    asrt_base64 = b'AAAAAAMAAAAAAAAAAQ16AAQAAfAAAgAAAAEA'
    asrt_hex = compat_b64decode(asrt_base64)
    asrt_data = FlvReader(asrt_hex).read_asrt()
    assert asrt_data

# Generated at 2022-06-14 15:27:08.392418
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    f = compat_urllib_request.urlopen(
        'https://github.com/rg3/youtube-dl/issues/5684/files/34657467344')
    bootstrap_info = FlvReader(f.read()).read_bootstrap_info()
    assert bootstrap_info['segments'][0]['segment_run'][0] == (0, 9)
    assert bootstrap_info['fragments'][0]['fragments'][0]['first'] == 0
    assert bootstrap_info['fragments'][0]['fragments'][0]['duration'] == 2
    assert bootstrap_info['fragments'][0]['fragments'][0]['ts'] == 4476

# Generated at 2022-06-14 15:27:13.635239
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    # Test with a bootstrap info file, downloaded from
    # http://devimages.apple.com/iphone/samples/bipbop/gear1/prog_index.m3u8
    bootstrap_info_content = open('test/bootstrap_info.dat', 'rb').read()
    bootstrap_info = FlvReader(bootstrap_info_content).read_bootstrap_info()
    assert bootstrap_info[1] == b'abst'
    assert bootstrap_info[2]['live'] is True
    assert len(bootstrap_info[2]['segments']) == 3
    assert len(bootstrap_info[2]['fragments']) == 3
    assert len(bootstrap_info[2]['fragments'][0]['fragments']) == 2
    assert len

# Generated at 2022-06-14 15:27:23.143578
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:27:30.798698
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .test_fragments import _TEST_FILE
    abst = FlvReader(_TEST_FILE).read_bootstrap_info()
    assert abst == {
        'segments': [{'segment_run': []}],
        'fragments': [
            {
                'fragments': [
                    {
                        'first': 0,
                        'ts': 0,
                        'duration': 10000,
                        'discontinuity_indicator': None,
                    }
                ]
            }
        ],
        'live': False,
    }
# End of unit test



# Generated at 2022-06-14 15:27:42.719066
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x00H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x72\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2e\x6d\x70\x34\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x27'
    fr = FlvReader(data)
    segments = fr.read_asrt()['segment_run']

# Generated at 2022-06-14 15:27:52.494916
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    manifest_url = 'https://pubads.g.doubleclick.net/gampad/ads?sz=640x480&iu=/124319096/external/ad_rule_samples&ciu_szs=300x250&ad_rule=1&impl=s&gdfp_req=1&env=vp&output=vmap&unviewed_position_start=1&cust_params=deployment%3Ddevsite%26sample_ar%3Dpremidpost&cmsid=496&vid=short_onecue&correlator='
    ydl = YoutubeDL({'outtmpl': 'test%(ext)s', 'test': True})
    f4mfd = F4mFD(ydl, manifest_url)

# Generated at 2022-06-14 15:28:04.208328
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    # Create a test string with 4 boxes, whose sizes are 2, 4, 8, 10
    # A box size of 1 indicates that the box size will be read in the next 8
    # bytes.
    raw = compat_struct_pack(
        '!IIIIIIIIII',
        2, 0, 0, 0, 1, 0, 0, 0, 0, 0,
        4, 0, 0, 0, 2, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 8, 0, 0, 0, 0, 0,
        10, 0, 0, 0, 3, 0, 0, 0, 0, 0)
    reader = FlvReader(raw)
    assert reader.read_box_info() == (2, b'\x00\x00\x00\x00', b'')

# Generated at 2022-06-14 15:28:14.659556
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:28:25.667221
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:28:41.309574
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:28:53.286218
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:29:02.823143
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    flv_reader = FlvReader(open('fixtures/a.f4f.sample.abst', 'rb').read())
    abst = flv_reader.read_bootstrap_info()
    assert abst['fragments'][0]['fragments'][0]['first'] == 1
    assert abst['fragments'][0]['fragments'][1]['first'] == 2
    assert abst['fragments'][0]['fragments'][2]['first'] == 3
    assert abst['fragments'][0]['fragments'][3]['first'] == 4
    assert abst['fragments'][0]['fragments'][4]['first'] == 5
    assert abst['fragments'][0]['fragments'][5]['first'] == 6
   

# Generated at 2022-06-14 15:29:14.014847
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:29:21.756384
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:29:31.879439
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:38.168490
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:29:45.740793
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    from .testcases import read_bin_file
    raw_string = read_bin_file('f4m_afrt')
    afrt_dict = FlvReader(raw_string).read_afrt()
    assert afrt_dict == {
        'fragments': [
            {
                'first': 0,
                'ts': 0,
                'duration': 25000,
                'discontinuity_indicator': None,
            },
            {
                'first': 1,
                'ts': 25000000,
                'duration': 25000,
                'discontinuity_indicator': None,
            }]
    }
    pass

# Generated at 2022-06-14 15:29:56.195238
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    class CheckAFRT:
        def __init__(self):
            self.check_results = True
            self.trace = False

    def assertTrue(value):
        assert value is True

    def assertFalse(value):
        assert value is False

    def assertEqual(a, b):
        if isinstance(a, list) and isinstance(b, list):
            for i in range(len(a)):
                assertEqual(a[i], b[i])
        else:
            assert a == b

    def assertNotEqual(a, b):
        assert a != b

    def assertIs(a, b):
        assert a == b


# Generated at 2022-06-14 15:30:08.432778
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:30:28.899885
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import sys
    import ytdl_module_test_module
    test = ytdl_module_test_module.init_common_testing()
    test.options.dump_single_json = True
    test.options.outtmpl='%(id)s'
    test.options.verbose = True
    test.options.format='best'
    test.options.quiet = False
    test.options.skip_download = False
    test.options.nooverwrites = False
    test.options.noprogress = False
    test.options.forceurl = False
    test.options.forcetitle = False
    test.options.forceid = False
    test.options.forcedescription = False
    test.options.forcefilename = False
    test.options.forceformat = False
    test.options.forcerating

# Generated at 2022-06-14 15:30:37.843731
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from ..utils import (
        encode_base_n,
    )


# Generated at 2022-06-14 15:30:47.098459
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    def check_box_info(box_data, exp_size, exp_type):
        fd = FlvReader(box_data)
        size, box_type, box_content = fd.read_box_info()
        assert size == exp_size
        assert box_type == exp_type

    check_box_info(
        compat_struct_pack('!IB3s', 12, b'styp', b'\x00\x00\x00'), 12, b'styp')
    check_box_info(
        compat_struct_pack('!I', 1) + compat_struct_pack('!Q', 13) + b'schm', 13, b'schm')



# Generated at 2022-06-14 15:30:55.396119
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    assert FlvReader(b'\x00\x00\x00\x1f\x61\x73\x72\x74\x01\x66\x6f\x6f\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05').read_asrt() == {
        'segment_run': [
            (0, 3),
            (4, 5),
        ],
    }



# Generated at 2022-06-14 15:31:05.233324
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import youtube_dl.YoutubeDL
    ydl = youtube_dl.YoutubeDL({
        'debug_printtraffic': True,
        'forcejson': True,
        'nooverwrites': True,
        'quiet': True,
        'simulate': True,
        'skip_download': True,
        'format': 'bestvideo',
    })
    downloads = ydl.download(['http://demo.unified-streaming.com/video/smurfs/smurfs.ism/smurfs.f4m'])
    assert len(downloads) == 1
    download = downloads[0]
    assert download['status'] == 'finished'
    assert download['filename'] is not None
    assert download['fragment_index'] is not None
    assert download['total_frags'] is not None



# Generated at 2022-06-14 15:31:16.817313
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:31:26.195669
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:31:37.996770
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import unittest
    import tempfile
    import os
    from youtube_dl.utils import *
    from youtube_dl.extractor.common import InfoExtractor

    class F4mManifestTest(unittest.TestCase):
        def setUp(self):
            self._tmpfiles = []

        def tearDown(self):
            for tmp in self._tmpfiles:
                os.remove(tmp)

        def _create_tmp(self):
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.f4m')
            tmp.close()
            self._tmpfiles.append(tmp.name)
            return tmp.name


# Generated at 2022-06-14 15:31:48.030589
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    xml = u"""
    <media url="http://www.example.com/video.mp4" quality="high">
        <media url="http://www.example.com/video.mp4" quality="low"
               drmAdditionalHeaderId="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
               drmAdditionalHeaderSetId="01234">
        </media>
    </media>
    """
    elem = compat_etree_fromstring(fix_xml_ampersands(xml))
    media = elem.findall("media")
    assert len(media) == 2
    assert len(remove_encrypted_media(media)) == 1



# Generated at 2022-06-14 15:31:59.344885
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from io import BytesIO
    from youtube_dl.downloader import F4mFD
    from urllib.parse import urlparse
    from .testutils import FakeYoutubeDL

    ydl = FakeYoutubeDL()