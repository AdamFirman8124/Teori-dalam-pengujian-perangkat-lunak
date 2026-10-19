

# Generated at 2022-06-14 15:48:32.423685
# Unit test for constructor of class IsmFD
def test_IsmFD():
    info_dict = {
        'url': 'http://foo.bar/playlist.ism',
        'playlist_id': 'playlist.ism',
        'track_id': 1,
        'direct': True,
        'fragments': [
            {'url': 'http://foo.bar/segment-1.ism/QualityLevels(96000)/Fragments(audio=0)'},
            {'url': 'http://foo.bar/segment-2.ism/QualityLevels(96000)/Fragments(audio=96000)'},
            {'url': 'http://foo.bar/segment-3.ism/QualityLevels(96000)/Fragments(audio=192000)'},
        ],
    }

    FD = IsmFD(info_dict)

# Generated at 2022-06-14 15:48:39.550997
# Unit test for function extract_box_data
def test_extract_box_data():
    params = {
        'track_id': 1,  # ID of the track
        'fourcc': 'H264',  # four character code of the codec
        'duration': 1,  # duration of the track
        'timescale': 90000,  # timescale of the track
        'height': 480,  # height of the video track
        'width': 640,  # width of the video track
        'codec_private_data': '014280f5fc033a98c9a7f57bf2e801450011f8c0000016742c038010000e8d40b80',
    }
    stream = io.BytesIO()
    write_piff_header(stream, params)
    stream.seek(0)

# Generated at 2022-06-14 15:48:51.079181
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    if sys.version_info >= (3, 0):
        msg = 'Test of IsmFD.real_download method under Python 3.x is skipped'
        pytest.skip(msg)

        #
        # Some test cases need to be rewritten for Python 3.x
        #



# Generated at 2022-06-14 15:48:59.386411
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 1000,
        'timescale': 10,
        'width': 1920,
        'height': 1080,
        'codec_private_data': '0164001fffe100186764001facd9c0804d00322036e56ffc1002e05a00000fa800001fa40015e0e83c60d80',
        'nal_unit_length_field': 4
    }
    stream = io.BytesIO()
    write_piff_header(stream, params)
    print(io.BytesIO())


# Generated at 2022-06-14 15:49:11.620785
# Unit test for function extract_box_data
def test_extract_box_data():
    data = b'\x00\x00\x00\x20' + b'\x00\x00\x00' + b'\x00\x00\x00\x20' + b'\x00\x00\x00\x20' + b'\x00\x00\x00\x48'
    assert extract_box_data(data, (b'\x00\x00\x00',)) == data[4:]
    assert extract_box_data(data, (b'\x00\x00\x00\x20',)) == data[8:]
    assert extract_box_data(data, (b'\x00\x00\x00\x48',)) == data[20:]
test_extract_box_data()



# Generated at 2022-06-14 15:49:24.732527
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    url = 'https://manifest.prod.boltdns.net/manifest/v1/hls/v4/aes128/44444444444444444444444444444444/55555555555555555555555555555555/prog_index.m3u8?fast_chunk_count=10&fast_chunk_size=5000000&start_range=0'
    manifest_profile = manifest_download(url)
    manifest_profile_url = manifest_profile[1]
    profile_segment_count = len(manifest_profile[2])
    # Inserting _download_params
    params = {}
    params['track_id'] = 1
    params['fourcc'] = 'H264'
    params['duration'] = 529753
    params['timescale']

# Generated at 2022-06-14 15:49:31.542690
# Unit test for function write_piff_header
def test_write_piff_header():
    from .fragment import FragmentFD
    from ..utils import read_chunks
    from ..compat import (
        compat_urllib_request,
        compat_urllib_error,
    )

    fragment_url = 'https://amp.azure.net/libs/amp/2.2.4/azuremediaplayer.tech.min.js'
    fragment_filename = 'azuremediaplayer.tech.min.js'
    stream = io.BytesIO()
    params = {}
    params['track_id'] = 1
    params['duration'] = 0
    params['fourcc'] = 'AACL'
    params['channels'] = 2
    params['bits_per_sample'] = 16
    params['sampling_rate'] = 48000
    write_piff_header(stream, params)



# Generated at 2022-06-14 15:49:32.460935
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass



# Generated at 2022-06-14 15:49:45.289927
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Missing modules
    if sys.modules.get('Cryptodome', False):
        pycryptodome = sys.modules['Cryptodome']
    else:
        pycryptodome = sys.modules['Crypto']

    # Create fake data
    data = [b'ftyp',
            b'moov',
            b'moov',
            b'moov'
            ]

    # Create fake info dict
    info_dict = {'format_id': 'ism',
                 'fragments': data,
                 '_download_params': {'filename': 'filename',
                                      'total_frags': 20,
                                      'start_fragment': 5,
                                      'fragment_index': 5}
                 }

    # Create fake ctx

# Generated at 2022-06-14 15:49:57.008049
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    segments = [
        {'url': 'http://segment'},
        {'url': 'http://segment'},
        {'url': 'http://segment'},
        {'url': 'http://segment'},
        {'url': 'http://segment'},
        {'url': 'http://segment'},
        {'url': 'http://segment'},
    ]
    class T:
        def __init__(self):
            self.report_skip_fragment = lambda x: None
            self.report_retry_fragment = lambda x,y,z,q: None
            self.report_error = lambda x: None
    class F:
        def __init__(self):
            self.real_download = IsmFD.real_download

# Generated at 2022-06-14 15:50:55.160905
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        params = {
            'track_id': 1,
            'fourcc': 'H264',
            'duration': 0xffffffffffffffff,
            'nal_unit_length_field': 4,
            'timescale': 10000000,
            'language': 'eng',
            'height': 576,
            'width': 720,
        }

        write_piff_header(stream, params)

        stream.seek(0)
        assert stream.read(8) == b'moov\x80\x00\x00\x00'
        assert stream.read(8) == b'mvhd\x00\x00\x00\x18'

# Generated at 2022-06-14 15:51:04.764838
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # set up a file descriptor to write test video fragments to
    temp_video = tempfile.NamedTemporaryFile('wb', prefix='youtube-dl_test_video_', suffix='.ism', delete=False)
    temp_video_uri = path_to_uri(temp_video.name)
    temp_video.close()

    # perform a test download
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'test': True,
        'outtmpl': temp_video_uri,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # this is a sample video with two fragments:
        # https://storage.googleapis.com/shaka-demo-assets/angel-one/dash.mpd
        ydl

# Generated at 2022-06-14 15:51:11.508097
# Unit test for constructor of class IsmFD
def test_IsmFD():
  params = {
    'fragments': [{'url': 'test'}],
    '_download_params': {'track_id': 0, 'fourcc': 'test',
      'duration': 10, 'timescale': 10, 'language': 'und',
      'height': 100, 'width': 200,
      'video_stream': {'sampling_rate': 10}}
  }
  ismfd = IsmFD(params)
  ismfd.real_download('test.ism', params)


# Generated at 2022-06-14 15:51:24.270584
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:51:33.527842
# Unit test for function write_piff_header
def test_write_piff_header():
    from collections import OrderedDict

    def test_piff_header(stream, params):
        write_piff_header(stream, params)
        stream.seek(0)

# Generated at 2022-06-14 15:51:44.827037
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:51:47.896461
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .ism import IsmFD
    if IsmFD.available():
        IsmFD()


# Generated at 2022-06-14 15:51:55.088748
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .downloader import YoutubeDL
    from .extractor import YoutubeIE
    from .utils import sanitize_open
    from .compat import compat_http_server
    import tempfile
    import shutil
    import os
    import threading
    import time
    import json
    import atexit
    import http.server

    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)

    file_server = compat_http_serve

# Generated at 2022-06-14 15:52:00.284829
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'fourcc': 'H264',
        'track_id': 1,
        'sampling_rate': 8000,
        'duration': 20560010,
        'nal_unit_length_field': 4,
        'codec_private_data': '014328DE11FC0033FAE8D001164C689F00F0E0C0',
    }

    write_piff_header(stream, params)

# Generated at 2022-06-14 15:52:12.843092
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
  # Test initialization
  info_dict = {
    'fragments': [
      'http://localhost:8090/Fragments(4)',
      'http://localhost:8090/Fragments(8)',
      'http://localhost:8090/Fragments(12)',
      'http://localhost:8090/Fragments(16)',
      'http://localhost:8090/Fragments(20)',
      'http://localhost:8090/Fragments(24)'
    ],
    '_download_params': {
      'track_id': 1,
      'fourcc': 'AACL',
      'duration': 2600000,
      'timescale': 10000000,
      'sampling_rate': 44100,
      'channels': 2,
      'bits_per_sample': 16
    }
  }


# Generated at 2022-06-14 15:53:25.677515
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import webvtt
    
    webvtt_url = 'http://blablabla/webvtt.vtt'

    webvtt_content = 'WEBVTT\n\n X-TIMESTAMP-MAP=MPEGTS:900000,LOCAL:00:00:00.000\n \n NOTE This is a subtitle file\n \n 1\n 00:00:02.250 --> 00:00:03.850\n The most recent security vulnerability found\n \n 2\n 00:00:03.850 --> 00:00:07.830\n in Chrome was discovered by security engineer Fermin Serna'


    path = os.path.join(os.getcwd(), 'test.mp4')


# Generated at 2022-06-14 15:53:26.445718
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    return None


# Generated at 2022-06-14 15:53:37.027804
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:53:45.231069
# Unit test for function write_piff_header
def test_write_piff_header():
    class Dummy(io.BytesIO):
        def getvalue(self):
            return self._buffer.getvalue()

    def run_test(params, expected):
        stream = Dummy()
        write_piff_header(stream, params)
        assert expected == stream.getvalue()


# Generated at 2022-06-14 15:53:54.714004
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:53:56.991240
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD()
    assert fd.FD_NAME == 'ism'



# Generated at 2022-06-14 15:54:08.092334
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from ykdl.util.match import match1
    from ykdl.compact import urlopen, build_opener
    from ykdl.extractor import VideoExtractor
    from ykdl.videoinfo import VideoInfo
    from ykdl.util.html import get_content
    from ykdl.util.m3u8_wrap import load as load_m3u8, dump_m3u8

    # test extraction from .ism
    urls = [
        'http://download.microsoft.com/download/3/b/e/3bef8d9b-2c85-4e97-b7d8-ed4d054a4c4e/Exploring_F#!Transcript_EN.ism'
    ]

    for url in urls:
        m3u8_raw = urlopen

# Generated at 2022-06-14 15:54:18.410413
# Unit test for function write_piff_header
def test_write_piff_header():
    from .common import read_moov_atom
    from .hls import u32_to_str
    from .utils import ExtractorError, sanitize_open
    stream = io.BytesIO()
    write_piff_header(stream, {'track_id': 1, 'fourcc': 'AVC1', 'language': 'fra', 'height': 0, 'width': 0, 'duration': 5780050})
    stream.seek(0, io.SEEK_SET)
    moov_atom = read_moov_atom(stream)
    if len(moov_atom) != 1:
        raise ExtractorError('Expected 1 moov atom, got %d' % len(moov_atom))
    stream.seek(0, io.SEEK_SET)
    stream.truncate()

# Generated at 2022-06-14 15:54:26.702823
# Unit test for function write_piff_header
def test_write_piff_header():
    f = FragmentFD()
    params = { 'track_id': 0x01, 'fourcc': 'AACL', 'duration': 0, 'timescale': 90000, 'language': 'und', 'sampling_rate': 44100, 'bits_per_sample': 16, 'channels': 2 }
    write_piff_header(f, params)
    f.seek(0)

# Generated at 2022-06-14 15:54:37.722039
# Unit test for function write_piff_header
def test_write_piff_header():
    global_params = {
        'track_id': 1,
        'duration': 3672200000000,
        'timescale': 10000000,
        'width': 0,
        'height': 0,
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 44100,
    }
    piff_header = io.BytesIO()
    write_piff_header(piff_header, global_params)
    print(binascii.hexlify(piff_header.getvalue()))
    with open('piff_header.txt', 'wb') as f:
        f.write(piff_header.getvalue())



# Generated at 2022-06-14 15:57:09.878060
# Unit test for function write_piff_header
def test_write_piff_header():
    pass


# Generated at 2022-06-14 15:57:16.015133
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    url = 'https://manifest.prod.boltdns.net/movie/mp4/1/bipbop_adv_example_hevc/master.m3u8'
    ie = IsmFD(url)
    ret = ie.real_download('test_file_name', dict())
    assert ret == True



# Generated at 2022-06-14 15:57:23.716386
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    ctx = {}
    filename = 'test'
    info_dict = {}
    ctx['filename'] = filename
    ctx['total_frags'] = 'test'
    self._prepare_and_start_frag_download(ctx)
    fragment_retries = self.params.get('fragment_retries', 0)
    skip_unavailable_fragments = self.params.get('skip_unavailable_fragments', True)
    track_written = False
    frag_index = 0
    for i, segment in enumerate(segments):
        frag_index += 1
        if frag_index <= ctx['fragment_index']:
            continue
        count = 0

# Generated at 2022-06-14 15:57:29.903790
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        write_piff_header(
            stream,
            {
                'track_id': 0xebc0,
                'fourcc': 'AACL',
                'duration': 100000,
                'channels': 2,
                'bits_per_sample': 16,
                'sampling_rate': 48000,
            })

# Generated at 2022-06-14 15:57:37.468953
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:57:48.499290
# Unit test for function write_piff_header
def test_write_piff_header():
    audio_params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 1000,
        'timescale': 10000000,
        'language': 'und',
        'sampling_rate': 44100,
    }
    video_params = {
        'track_id': 2,
        'fourcc': 'H264',
        'duration': 1000,
        'timescale': 10000000,
        'language': 'und',
        'width': 1280,
        'height': 720,
        'codec_private_data': '01640040ac2b40',
        'nal_unit_length_field': 4,
    }

    s = io.BytesIO()
    write_piff_header(s, audio_params)

# Generated at 2022-06-14 15:57:54.303768
# Unit test for constructor of class IsmFD
def test_IsmFD():

    # Initialize test variables
    url = "test url"
    params = {}
    info_dict = {}
    info_dict['fragments'] = [{"url" : "http://test.com/test_file"}]
    info_dict['_download_params'] = {'track_id' : 1}

    # GIVEN an IsmFD object
    test_fd = IsmFD(url, params)

    # WHEN calling the real_download function with a fake filename
    success = test_fd.real_download('', info_dict)

    # THEN verify the output
    assert success
