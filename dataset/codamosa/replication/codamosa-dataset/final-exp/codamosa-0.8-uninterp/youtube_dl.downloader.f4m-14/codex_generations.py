

# Generated at 2022-06-14 15:22:54.659341
# Unit test for function get_base_url
def test_get_base_url():
    manifest = compat_etree_fromstring(
        b'<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
        b'<baseURL>/base/path</baseURL>'
        b'<media url="/foo.mp4">'
        b'<bootstrapInfo>'
        b'<bootstrapVersion>0</bootstrapVersion>'
        b'<state>0</state>'
        b'</bootstrapInfo>'
        b'</media>'
        b'</manifest>')
    assert get_base_url(manifest) == '/base/path'

# Generated at 2022-06-14 15:23:07.004263
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from ytdl.downloader.f4m import F4mFD
    from ytdl.structures import *
    from ytdl.extractor import YoutubeDL
    from ytdl.compat import parse_qs,urlparse
    import unittest
    ############################################
    #                                          #
    #  Constructor for class F4mFD             #
    #                                          #
    ############################################
    f4mfd = F4mFD(
             ydl=YoutubeDL(params=dict()),
             params=dict(),
             ie=None,
             filename=None,
             info_dict=dict(url="http://someurl"))
    result = isinstance(f4mfd, F4mFD)
    assert result == True, 'Constructor of class F4mFD failed.'

    #

# Generated at 2022-06-14 15:23:16.618198
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # test_F4mFD_real_download() is not a PyUnit test.
    # TODO It is a pytest unit test
    from .youtube_dl.YoutubeDL import YoutubeDL
    import sys
    import os

    # Workaround to make this script work as a "individual test"
    # and as a part of the whole test suite
    try:
        # When this module is executed as a part of the whole test
        # suite, the parent directory is youtube_dl
        sys.path.append(sys.path[0] + '/..')
    except IndexError:
        pass


# Generated at 2022-06-14 15:23:28.850542
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    # Test case with box_size = 0
    fd = io.BytesIO(compat_struct_pack('!I4s', 0, b'abst'))
    assert FlvReader(fd).read_box_info() == (0, b'abst', b'')
    fd = io.BytesIO(compat_struct_pack('!I4s', 1, b'abst'))
    assert FlvReader(fd).read_box_info() == (1, b'abst', b'')
    fd = io.BytesIO(compat_struct_pack('!Q4s', 1, b'abst'))
    assert FlvReader(fd).read_box_info() == (1, b'abst', b'')
    # Real case, box_size = 53

# Generated at 2022-06-14 15:23:29.701771
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    pass



# Generated at 2022-06-14 15:23:38.610795
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    from io import BytesIO
    metadata = b"<?xml version='1.0'?><root/>"
    stream = BytesIO()
    write_metadata_tag(stream, metadata)
    assert stream.getvalue() == (
        b'\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' +
        metadata + b'\x00\x00\x00\x2C')
    stream = BytesIO()
    write_metadata_tag(stream, None)
    assert stream.getvalue() == b''



# Generated at 2022-06-14 15:23:47.758918
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():

    from .test_fragment import _load_bin
    from .files import check_files

    box_data = _load_bin('flv-reader/asrt.bin', 240)

    segment = FlvReader(box_data).read_asrt()
    assert segment == {
        'segment_run': [
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
        ],
    }

    check_files('FlvReader.read_asrt', segment)


# Generated at 2022-06-14 15:23:56.559028
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:24:04.406289
# Unit test for function get_base_url
def test_get_base_url():
    test_cases = [
        ('assets/player/myVideo.f4m', 'assets/'
         if not is_py2 else 'assets/'),
        ('/assets/player/myVideo.f4m', '/assets/'),
        ('assets/video/myVideo.f4m', ''),
        ('/assets/video/myVideo.f4m', '/'),
    ]
    for input, expected in test_cases:
        assert get_base_url(input) == expected


# Generated at 2022-06-14 15:24:12.614868
# Unit test for constructor of class F4mFD
def test_F4mFD():
    # Test: media attributes
    fd = F4mFD({'url': "http://dummy", 'http_headers': {}})
    info_dict = {}
    ret = fd._get_unencrypted_media(compat_etree_fromstring(
        '<media url="url"></media>'))
    assert len(ret) == 1
    ret = fd._get_unencrypted_media(compat_etree_fromstring(
        '<media url="url" bootstrapInfoId="id"></media>'))
    assert len(ret) == 1
    ret = fd._get_unencrypted_media(compat_etree_fromstring(
        '<media url="url" bootstrapInfoId="id"></media>'))
    assert len(ret) == 1
    # Test: Additional DRM
    ret

# Generated at 2022-06-14 15:25:14.459472
# Unit test for method real_download of class F4mFD

# Generated at 2022-06-14 15:25:23.697883
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from .extractor.common import InfoExtractor
    from .downloader.common import FileDownloader
    from .downloader.f4m import F4mFD
    from .compat import compat_urllib_parse_urlparse, compat_urllib_parse_unquote_plus

    # F4mFD constructor
    f4mFD = F4mFD(FileDownloader({'format': '720p', 'verbose': 'True'}))


# Generated at 2022-06-14 15:25:33.785768
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:25:44.581812
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:25:53.749791
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:26:02.237067
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .common import fake_urlretrieve

    path = u'http://example.com/manifest.f4m'
    path += u'#'
    path += compat_b64decode('AAAAAAABAAAAAa1kJAAAAAAAAAANhc3RwbGF5ZXJ0eXBlPW1'
                             'tbXV0eXBlPWVtYmVkZGVkcGxheWVyAAAAAA==')
    url = path.split('#')[0]
    base = compat_urllib_parse_urlparse(path)

    class FakeFile(io.BytesIO):
        def __init__(self, *args, **kwargs):
            io.BytesIO.__init__(self, *args, **kwargs)
            self.path = path

# Generated at 2022-06-14 15:26:14.227864
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:26:26.277346
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    s = b'''
    00 00 00 1C
    61 73 72 74
    00 01 00 00
    00 00 00 01
    61 00 00 00
    00 00 00 01
    00 00 00 00
    00 00 00 00
    '''
    assert FlvReader(s).read_asrt() == {
        'segment_run': [
            (
                0,
                0,
            )
        ]
    }
    s = b'''
    00 00 00 2D
    61 73 72 74
    00 01 00 00
    00 00 00 02
    61 00 00 00
    00 00 00 01
    00 00 00 00
    00 00 00 00
    61 00 00 00
    00 00 00 01
    00 00 00 01
    00 00 00 01
    '''
    assert FlvReader(s).read_

# Generated at 2022-06-14 15:26:36.927781
# Unit test for function write_metadata_tag

# Generated at 2022-06-14 15:26:45.965450
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import youtube_dl
    import youtube_dl.extractor
    import urllib.request
    import urllib.parse
    import urllib.error
    import json
    import shutil
    import os
    from os import path

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Store the old working directory
    old_cwd = os.getcwd()

    # Change the working directory to the temporary directory
    os.chdir(temp_dir)

    # Create an instance of class youtube_dl.YoutubeDL
    ydl_opts = {
        'verbose': False,
        'quiet': True,
        'no_warnings': True,
        'simulate': True,
        'skip_download': True,
    }
    ydl = youtube_dl.Y

# Generated at 2022-06-14 15:27:53.293044
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    test_url = 'http://live-1-1.rutube.ru/stream/1024/HDS/SD/C2NKsS85HQNckgn5HdEmOQ/1454167650/S-s604419906/move/four/dirs/upper/1024-576p.f4m'
    ydl_opts = {'format': 'f4m_test'}
    fd = F4mFD(1, ydl_opts, 'test', 'test')
    fd.real_download(None, {'url': test_url})
    ydl_opts = {'format': 'f4m_test', 'test': True}
    fd = F4mFD(1, ydl_opts, 'test', 'test')

# Generated at 2022-06-14 15:28:04.841246
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    test_file = open('test/sample.bootstrap', 'rb')
    abst = FlvReader(test_file.read()).read_bootstrap_info()
    test_file.close()

    # The test is performed comparing the content of the sample.bootstrap file
    # with the output of the method read_bootstrap_info
    # (see http://www.adobe.com/devnet/f4v.html for the description of the file format)

    # The file contains two boxes, one of type "abst" (BootstrapInfo) and another one of type "asrt" (SegmentRunTableBox)
    # The "abst" box starts with the header (8 bytes) followed by a string "abst" (4 bytes) and by the box size (4 bytes).
    # The box size is the size of the box in bytes, not

# Generated at 2022-06-14 15:28:09.228994
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    with open("tests/bootstrap.abst", "rb") as bootstrap_fd:
        bootstrap_info = FlvReader(bootstrap_fd.read()).read_bootstrap_info()
    assert len(bootstrap_info["segments"]) == 1
    assert len(bootstrap_info["fragments"]) == 1


# Generated at 2022-06-14 15:28:18.574230
# Unit test for function build_fragments_list
def test_build_fragments_list():
    assert list(build_fragments_list({
        'live': False,
        'segments': [{
            'segment_run': [
                (0, 2),
                (1, 3),
            ],
        }],
        'fragments': [{
            'fragments': [
                {'first': 1},
                {'first': 5},
                {'first': 11},
            ],
        }],
    })) == [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (1, 5),
    ]


# Generated at 2022-06-14 15:28:28.635137
# Unit test for function build_fragments_list
def test_build_fragments_list():
    segments_dict = {
        'segment_run': [
            (1, 1),
            (4, 1)
        ]
    }

    fragment_dict = {
        'fragments': [{
            'first': 0,
            'ts': 0,
            'duration': 0,
            'discontinuity_indicator': None
        }, {
            'first': 1,
            'ts': 100,
            'duration': 100,
            'discontinuity_indicator': None
        }],
    }

    res = build_fragments_list(dict(
        segments=[segments_dict],
        fragments=[fragment_dict],
        live=False
    ))
    assert res == [(1, 0), (4, 1)]


# Generated at 2022-06-14 15:28:38.925345
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    with open('tests/data/bootstrap_info.bin', 'rb') as f:
        bootstrap_info = FlvReader(f.read()).read_bootstrap_info()
    # segment_run
    expected_segment_run = [
        (0, 1)
    ]
    assert bootstrap_info['segments'][0]['segment_run'] == expected_segment_run, 'segment_run'
    # fragments_ts
    expected_fragments_ts = [
        0,
        15,
        30,
        45,
        60,
        75,
        90,
        105,
        120,
        135,
    ]

# Generated at 2022-06-14 15:28:41.840613
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    url = ''
    info_dict = {}
    filename = ''

    obj = F4mFD()
    obj.real_download(filename, info_dict)
    pass

# Generated at 2022-06-14 15:28:53.845397
# Unit test for function build_fragments_list
def test_build_fragments_list():
    boot_info = {
        'live': True,
        'segments': [{
            'fragment_run_entry_table': [
                (0, 1),
                (1, 1),
                (1, 4294967295),
                (2, 1),
            ]
        }],
        'fragments': [{
            'fragment_run_entry_table': [
                {
                    'first': 0,
                    'ts': 0,
                    'duration': 0,
                },
                {
                    'first': 1,
                    'ts': 90000,
                    'duration': 90000,
                },
            ],
        }],
    }

# Generated at 2022-06-14 15:29:03.218498
# Unit test for function build_fragments_list
def test_build_fragments_list():
    bootstrap_info = {u"segments": [{u"segment_run": [(0, 1)]}], u"fragments": [{u"fragments": [{u"ts": 0, u"discontinuity_indicator": 0, u"first": 0, u"duration": 4}]}], u"live": False}
    expected = [(0, 0)]
    assert build_fragments_list(bootstrap_info) == expected


# Generated at 2022-06-14 15:29:14.343177
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from ..compat import compat_urlopen
    from ..utils import (
        determine_ext,
        get_element_by_attribute,
        HEADRequest,
        video_extensions,
    )
    from ..extractor import (
        get_info_extractor,
        list_extractors,
        YoutubeIE,
    )
    youtube_ie = YoutubeIE()
    url = 'https://www.youtube.com/watch?v=8WGuTxJcEqA'
    info = youtube_ie._real_extract(url)

# Generated at 2022-06-14 15:30:14.956578
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:30:26.829220
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
	from unittest.mock import patch
	from ytdl import YoutubeDL
	with patch.object(YoutubeDL, 'urlopen') as urlopen_mock:
		from ytdl.extractor import F4mFD
		from ytdl.utils import URL_RE

		url = 'https://video-weaver.ams3.cdn.digitaloceanspaces.com/6f4e633d4a3/6f4e633d4a3bc7bc6c4cdeb88ff6ad46.f4m'
		filename = '6f4e633d4a3bc7bc6c4cdeb88ff6ad46.f4m'

# Generated at 2022-06-14 15:30:35.589421
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    f = open('tests/files/f4m_bootstrap_info.dat', 'rb')
    data = f.read()
    f.close()
    bootstrap_info = FlvReader(data).read_bootstrap_info()
    assert bootstrap_info['segments'][0]['segment_run'][0] == (0, 1)
    assert bootstrap_info['segments'][0]['segment_run'][1] == (1, 2)
    assert len(bootstrap_info['fragments'][0]['fragments']) == 3
    assert bootstrap_info['fragments'][1]['fragments'][0]['first'] == 4
    assert not bootstrap_info['live']



# Generated at 2022-06-14 15:30:46.482794
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:30:56.873747
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    f = open('test.abst', 'rb')
    data = f.read()
    f.close()
    info = FlvReader(data).read_afrt()
    assert info['fragments'][0]['first'] == 0
    assert info['fragments'][0]['ts'] == 0
    assert info['fragments'][0]['duration'] == 400000

    assert info['fragments'][1]['first'] == 1
    assert info['fragments'][1]['ts'] == 400000
    assert info['fragments'][1]['duration'] == 400000

    assert info['fragments'][2]['first'] == 2
    assert info['fragments'][2]['ts'] == 800000
    assert info['fragments'][2]['duration'] == 400

# Generated at 2022-06-14 15:31:03.054519
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    data_a = compat_b64decode(
        b'AAAAHgAAAA8AAAAIAAAABUAAQAAACYAAAAAAAAAAdUbiT8AAAAAAAAAAAAAAAAAAA'
        b'AAAFAAAAAAAAAAEAAQAAAAAAAAARKgQFAAMAAAAAAAAAZwAAIwAAACEAAAB8AAAA'
        b'XgAAAAAAAAAAAAAAAAAAAAEAAQAXAIQAAAAAAAAAAA==')
    data_b = compat_b64decode(
        b'AAAAGAAAABgAAAArAAAABUAAQAAACYAAAAAAAAAAdUbiT8AAAAAAAAAAAAAAAAAAA'
        b'AAAFAAAAAAAAAAEAAQAAAAAAAAARKgQFAAMAAAAAAAAAZwAAIwAAACEAAAB8AAAA'
        b'XgAAAAAAAAAAAAAAAAAAAAEAAQAXAIMAAAC5AAC8')

# Generated at 2022-06-14 15:31:14.679011
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from ..compat import compat_chr
    from ..utils import bytes_to_intlist


# Generated at 2022-06-14 15:31:24.749661
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:31:36.653878
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:31:48.302544
# Unit test for method read_bootstrap_info of class FlvReader