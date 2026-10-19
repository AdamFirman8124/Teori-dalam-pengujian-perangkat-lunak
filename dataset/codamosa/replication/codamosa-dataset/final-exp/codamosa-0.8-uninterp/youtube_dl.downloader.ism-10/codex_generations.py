

# Generated at 2022-06-14 15:48:25.230434
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .testconst import ISM_EXAMPLE_URL
    youtube_dl_instance = YoutubeDL({'quiet':True})
    downloader = IsmFD(youtube_dl_instance, {'outtmpl':'-'})
    info_dict = {}

# Generated at 2022-06-14 15:48:28.633003
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    arg = sys.argv[0]
    filename = ''
    info_dict = {}
    real_download(filename, info_dict)


# Generated at 2022-06-14 15:48:40.306687
# Unit test for function extract_box_data
def test_extract_box_data():
    from .util import (
        video_sample,
        audio_sample,
    )

    with FragmentFD(u'moov.m4s') as inf:
        moov_data = inf.read()
        video_data = extract_box_data(moov_data, (b'mdia', b'minf', b'stbl', b'stsd', b'avc1', b'avcC'))
        audio_data = extract_box_data(moov_data, (b'mdia', b'minf', b'stbl', b'stsd', b'mp4a', b'esds'))
        if video_data != video_sample():
            raise AssertionError('Unexpected video data')
        if audio_data != audio_sample():
            raise AssertionError('Unexpected audio data')



# Generated at 2022-06-14 15:48:47.569717
# Unit test for function extract_box_data
def test_extract_box_data():
    raw_data = b'\x00\x00\x00\x40moov\x00\x00\x00\x20trak\x00\x00\x00\x10mdia\x00\x00\x00\x08minf'
    assert b'mdia' == extract_box_data(raw_data, [b'moov', b'trak', b'mdia'])
    assert b'minf' == extract_box_data(raw_data, [b'moov', b'trak', b'mdia', b'minf'])
    assert None == extract_box_data(raw_data, [b'moov', b'trak', b'mdia', b'minf', b'sttb'])



# Generated at 2022-06-14 15:48:49.979896
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """Test IsmFD class constructor."""
    IsmFD(
        params={
            'url': 'http://example.com',
            'format': 'ism',
            'fragment_base_url': 'http://example.com/fragment',
            'downloader': None,
        },
    )

# Generated at 2022-06-14 15:48:53.877411
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    stream = io.FileIO('test.piff', 'wb')
    write_piff_header(stream, {'track_id': 1, 'fourcc': 'AACL', 'duration': 10000, 'sampling_rate': 44100, 'channels': 2})
    stream.close()
# End test unit for method real_download of class IsmFD



# Generated at 2022-06-14 15:49:07.726613
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import os
    import tempfile
    import threading
    import time
    import socket
    import subprocess
    import random
    import json
    import re
    import shutil

    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    from urllib.request import urlopen
    from urllib.error import URLError

    from .utils import prepend_extension, get_filesystem_encoding

    def run_server():
        class TestHTTPRequestHandler(BaseHTTPRequestHandler):
            def do_HEAD(self):
                self.never_download = False
                self.send_response(200)
                self.send_header('Content-type', 'video/mp4')

# Generated at 2022-06-14 15:49:10.686593
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:49:14.707248
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD()
    assert fd.FD_NAME == 'ism'

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:49:27.111823
# Unit test for function write_piff_header
def test_write_piff_header():
    import pytest
    from .http import FakeHTTPAdapter
    from requests import Session

    class FakeFragmentFD(FragmentFD):

        def __init__(self, params, headers, url_handle, filename, expected_info):
            pass

        def get_headers(self):
            return None

        def read_fragment(self, fragment_index):
            return None

        def get_size(self):
            return 0

    class FakeSmoothStreamsIE(SmoothStreamsIE):

        _smooth_streams_url = 'https://player.cloud.wowza.com/hosted/Ie4J3qld/manifest.f4m'

# Generated at 2022-06-14 15:49:49.715833
# Unit test for function write_piff_header
def test_write_piff_header():
    # Generate a few example PIFF headers
    with io.BytesIO() as buffer:
        # audio header
        params = {
            'track_id': 1,
            'fourcc': 'AACL',
            'duration': 0,
            'timescale': 48000,
            'sampling_rate': 48000,
        }
        write_piff_header(buffer, params)
        audio_header = buffer.getvalue()

        # video header
        buffer.seek(0)
        buffer.truncate()

# Generated at 2022-06-14 15:50:00.730281
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD()
    test_video_id = 'D041E9B9A285'
    info_dict = {}

# Generated at 2022-06-14 15:50:08.872297
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:50:14.404257
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    if not os.path.isfile('test.ism'):
        print("Download a sample (e.g. Media Services - Smooth Streaming - santabanta - 720p - Turbo.ism) from http://archive.org/details/MediaServicesSmoothStreaming and save it under 'test.ism'")
        return
    return IsmFD().real_download('test.ism', {'fragments': ['test.ism']})



# Generated at 2022-06-14 15:50:24.364877
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import gen_extractors
    from .utils import match_filter_func

    # Download an ISM video and check if video is downloaded successfully
    video_id = 'ism:i:0:c:32:0:0'
    info_dict = False
    for ie in gen_extractors():
        if match_filter_func(ie.IE_NAME):
            _, info_dict = ie._real_extract(video_id)
            break
    params = {
        'filename': 'test.ismv',
        'info_dict': info_dict,
        'fragment_index': 0,
        'fragments_num': None,
        'tmpfilename': 'tmp',
        'continuedl': False,
    }
    fd = IsmFD(params)
    res = f

# Generated at 2022-06-14 15:50:27.476992
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    filename = 'test.mp4'
    info_dict = {'fragments': [{'url': 'test_url',}], '_download_params': {'track_id': 0,}}
    self = IsmFD(params={})
    self.real_download(filename, info_dict)


# Generated at 2022-06-14 15:50:40.259602
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'fourcc': b'AVC1',
        'sampling_rate': 44100,
        'bits_per_sample': 16,
        'channels': 2,
        'nal_unit_length_field': 4,
        'track_id': 1,
        'duration': 10000,
        'timescale': 10000000,
        'codec_private_data': '0164001fffe100192744001388bf4cf4000001010200050001000003001c083c55cc02f2b581c3228c1',
        'width': 640,
        'height': 360
    }
    write_piff_header(stream, params)
    assert(len(stream.getvalue()) == 266)



# Generated at 2022-06-14 15:50:52.846311
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .downloader import Downloader
    from .extractor import gen_extractors
    def _print(s):
        pass
    params = {
        'outtmpl': None,
    }
    downloader = Downloader(_print, params)
    gen_extractors(downloader)
    #url = "http://www.example.com/test.ism/manifest"
    url = "http://smil.lvl3.cdn.video.sky.com/sports/cricket_eng/tv1/cricket/t20blast/2017/08/05/170805-1830-ENG_T20_BLAST_SUS_v_GLO_REP-400k.ism/manifest"
    ext = downloader._guess_ext(url, None)
    assert ext == 'ism'
    info_dict

# Generated at 2022-06-14 15:51:03.484077
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'codec_private_data': '0164001facd9082b2058a4e4d4e880518f43a97700000000000000000000000168e30c8',
        'sampling_rate': 44100,
        'channels': 2,
        'bits_per_sample': 16,
        'duration': 566400000,
        'width': 1280,
        'height': 720,
        'nal_unit_length_field': 4,
    }
    bio = io.BytesIO()
    write_piff_header(bio, params)

# Generated at 2022-06-14 15:51:13.119635
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as f:
        params = dict(track_id=1, fourcc='H264', duration=1, timescale=400000, width=1280, height=720,
            codec_private_data='00000001483fac5948c1e626f48c98c94110000b8e6028c8100000101414025c3f18ffdcdc')
        write_piff_header(f, params)
        assert f.tell() == 815

# Generated at 2022-06-14 15:51:42.909609
# Unit test for function write_piff_header
def test_write_piff_header():
    import struct
    import sys
    import os

    width = 1280
    height = 720
    fourcc = 'H264'
    duration = 10.0
    timescale = 10000000
    track_id = 3
    language = 'fra'
    nal_unit_length_field = 4
    codec_private_data = '01640028ffc1001e6742c0028ffc1e2742c0028ffc1012f964000820000001e23800000fc1030053964002800ffc8008274001a9a00980'

    class FakeStream(io.BytesIO):
        def close(self):
            pass

    stream = FakeStream()


# Generated at 2022-06-14 15:51:55.145968
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD({'ext': 'ism'})
    assert fd._get_filename('http://example.com/video.ismv') == 'video.ism'
    assert fd._get_filename('http://example.com/video.ism/QualityLevels(500000)/Fragments?start=10') == 'video.ism'
    assert fd._get_filename('http://example.com/Manifest') == 'Manifest.ism'
    assert fd._get_filename('http://example.com/Manifest?') == 'Manifest.ism'
    assert fd._get_filename('http://example.com/test.ism/Manifest') == 'test.ism.ism'

# Generated at 2022-06-14 15:52:07.608913
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor.generic import get_info_extractor
    from .common import Options
    from .utils import download_json, DEFAULT_OUTTMPL, match_filter_func
    class TestInfoExtractor(GetInfoExtractor):
        IE_NAME = 'test'
        _FEED_NAME = 'test'
    opts = Options()
    opts.__dict__['youtube_include_dash_manifest'] = True
    opts.__dict__['merge_output_format'] = 'ism'
    opts.__dict__['skip_download'] = True
    opts.__dict__['dump_single_json'] = True
    opts.__dict__['outtmpl'] = DEFAULT_OUTTMPL
    opts.__dict__['write_annotations'] = True
    opts.__dict__

# Generated at 2022-06-14 15:52:18.229452
# Unit test for function write_piff_header
def test_write_piff_header():
    import os
    import tempfile
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AVC1',
        'width': 1280,
        'height': 720,
        'duration': 2394*10000000,
        'timescale': 10000000,
        'language': 'eng',
        'codec_private_data': '01640029ffe1001b67640029acd941c16d941c0000000168ee3c80',
        'nal_unit_length_field': 4
    }
    write_piff_header(stream, params)
    stream.flush()
    data = stream.getvalue()
    fd, name = tempfile.mkstemp()
    os.write(fd, data)

# Generated at 2022-06-14 15:52:29.337364
# Unit test for function write_piff_header
def test_write_piff_header():
    self = FragmentFD('test_write_piff_header.ismv')
    with self:
        write_piff_header(self.stream, {'track_id': 1, 'fourcc': 'AACL', 'sampling_rate': 48000, 'duration': 60 * 1000 * 10000})
        self.stream.write(binascii.unhexlify(b'00000010667479707174'))
        self.stream.write(u32.pack(4))
        self.stream.write(u16.pack(4))
        self.stream.write(u8.pack(0))
        self.stream.write(u8.pack(0))


# Generated at 2022-06-14 15:52:31.228147
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    fd = IsmFD()
    assert fd.real_download('Hello World', {'fragments': []}) == True

# Generated at 2022-06-14 15:52:40.494000
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    file_name = 'IsmTestFile.ism'
    manifest_url = 'http://playready.directtaps.net/smoothstreaming/SSWSS720H264PR/SuperSpeedway_720.ism/Manifest'
    params = {
        'usenetrc': True,
        'retries': 10,
        'ratelimit': 100000,
        'fragment_retries': 10,
        'skip_unavailable_fragments': True
    }
    ismfd = IsmFD(manifest_url, params)
    info_dict = ismfd.get_real_info_dict(manifest_url)

    ismfd.real_download(file_name, info_dict)


# Generated at 2022-06-14 15:52:44.516868
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Create an IsmFD object
    fd = IsmFD()
    assert fd
    assert fd.FD_NAME == 'ism'

# Test case for IsmFD.real_download

# Generated at 2022-06-14 15:52:46.152515
# Unit test for constructor of class IsmFD
def test_IsmFD():
    ismFD = IsmFD()


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:52:58.262533
# Unit test for function write_piff_header
def test_write_piff_header():

    stream = io.BytesIO()

# Generated at 2022-06-14 15:54:02.751387
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {'track_id': 1,
              'fourcc': 'AACL',
              'duration': 1,
              'timescale': 10,
              'language': 'eng',
              'height': 0,
              'width': 0}
    stream = io.BytesIO()
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:54:15.122390
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import prepare_fake_extractors_module, prepare_fake_downloader, FakeYDL
    
    manifest_url = 'http://manifest_url'
    manifest_base_url = 'http://manifest_url'
    params = {'fragment_retries': 10, 'skip_unavailable_fragments': True}

# Generated at 2022-06-14 15:54:24.303798
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:54:28.758616
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from __main__ import params
    fd = IsmFD(params, params)
    fd.real_download("output.ism", "info")


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:54:40.369396
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    stream.seek(0)
    params = {'fourcc': 'AACL', 'duration': 123456789,
              'track_id': 1, 'height': 0, 'width': 0,
              'sampling_rate': 48000,
              'codec_private_data': '000004505343323034000000539DE0A2', 'channels': 2}
    write_piff_header(stream, params)
    # print(repr(stream.getvalue()))

# Generated at 2022-06-14 15:54:45.404868
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.open('test/test_write_piff_header.ismv', 'wb') as f:
        write_piff_header(f, {'track_id': 1, 'fourcc': 'H264', 'codec_private_data': '000000016742c01e9a030015f8411280', 'height': 720, 'width': 1280, 'duration': 10000000})



# Generated at 2022-06-14 15:54:54.863959
# Unit test for function write_piff_header
def test_write_piff_header():
    from ..compat import (
        compat_HTTPError,
        compat_chr,
        compat_urllib_error,
    )

    from ..utils import (
        ExtractorError,
        check_executable,
    )

    from io import BytesIO

    from subprocess import Popen, PIPE

    import pytest


    def _run_ffprobe(params):
        """
        Run ffprobe for params and return stdout as a byte string
        """
        cmd = ['ffprobe']
        cmd.extend(params)
        proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = proc.communicate()


# Generated at 2022-06-14 15:55:02.122646
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 1000,
        'timescale': 10000,
        'language': 'und',
        'height': 720,
        'width': 1280,
        'codec_private_data': '01640029ffe1000567640029ac32a98fac626988d5a53'
    }
    write_piff_header(stream, params)


# Generated at 2022-06-14 15:55:14.109560
# Unit test for constructor of class IsmFD
def test_IsmFD():

    # set parameters
    tests = 0
    test_passed = 0
    test_failed = 0
    test_crashed = 0

    # define error codes
    ERR_CODE_NONE                                 = 0
    ERR_CODE_CRASHED                              = 1

    # initialize err_code
    err_code = ERR_CODE_NONE


# Generated at 2022-06-14 15:55:19.982720
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Test with a single empty fragment
    ext = IsmFD()
    ext.params = dict(noplaylist=True)

# Generated at 2022-06-14 15:57:27.639982
# Unit test for constructor of class IsmFD
def test_IsmFD():
    pass

# endregion

# region SMOOTHFD



# Generated at 2022-06-14 15:57:34.146820
# Unit test for function write_piff_header
def test_write_piff_header():
    from ..utils import read_files_fragments
    from ..downloader.http import FragmentFD

# Generated at 2022-06-14 15:57:44.353591
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.open('piff_header.txt', 'w', encoding='utf-8') as f:
        f.write(u8.pack(0) * 32 + u16.pack(0) * 16 + u32.pack(0) * 4 + u16.pack(0) * 2 + u8.pack(0) + u16.pack(0) * 2 + u32.pack(0))
        with FragmentFD(f) as self_contained_stream:
            write_piff_header(self_contained_stream, {'track_id': 1, 'duration': 10, 'sampling_rate': 44100, 'fourcc': 'AACL'})
        f.close()

# Generated at 2022-06-14 15:57:51.027478
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Load the test url
    url = "http://manifest.us.rtl.nl/net/rtl-nu/bb/live/chunklist_b800000_sleng.m3u8"
    test_IsmFD.fd.add_info_dict({'url': url})

    # Download the file from the test url
    def _hook(status):
        print(status)

    test_IsmFD.fd.download(filename='test_IsmFD.ism', extra_info={}, progress_hooks=[_hook])


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:57:51.820012
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass
# Test runner

# Generated at 2022-06-14 15:57:59.917785
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    rundir = os.path.abspath(os.path.dirname(__file__))
    shutil.rmtree(os.path.join(rundir,'sample'))