

# Generated at 2022-06-14 15:48:34.430403
# Unit test for function write_piff_header
def test_write_piff_header():
    from ..fragments import SegmentedFD

    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'sampling_rate': 8000,
        'channels': 1,
    }
    out = SegmentedFD(FragmentFD(), b'', b'.ismv')
    out.write(b'\0\0\0\0')
    write_piff_header(out, params)
    assert out.seek(0, 2) == 0x29c
    assert out.seek(0) == 0
    assert out.read(4) == b'\0\0\0\0'
    assert out.read(4) == b'moov'
    assert out.read(4) == b'\0\0\0\x27c'

# Generated at 2022-06-14 15:48:41.875111
# Unit test for constructor of class IsmFD
def test_IsmFD():
    class IsmFD_test(IsmFD):
        def __init__(self, ydl, params):
            IsmFD.__init__(self, ydl, params)
            self.params.update(params)

    param_dict = {'url': 'http://test_url.com', 'keep_fragments': True, 'fragment_retries': 0}
    fd = IsmFD_test(None, param_dict)
    assert fd.params == param_dict



# Generated at 2022-06-14 15:48:45.865181
# Unit test for constructor of class IsmFD
def test_IsmFD():
    assert IsmFD.FD_NAME == 'ism'
    assert IsmFD.__name__ == 'IsmFD'
    assert IsmFD.constructor_hook() == FragmentFD

test_IsmFD()

# Generated at 2022-06-14 15:48:54.523014
# Unit test for function write_piff_header
def test_write_piff_header():
    import sys
    import tempfile
    import hashlib
    from decimal import Decimal
    if sys.version_info >= (3, 3):
        from unittest.mock import Mock
    else:
        from mock import Mock
    VideoFragmentFD = Mock()
    VideoFragmentFD.duration = 10000
    VideoFragmentFD.timescale = 10000000
    VideoFragmentFD.width = 960
    VideoFragmentFD.height = 540
    AudioFragmentFD = Mock()
    AudioFragmentFD.duration = 20000
    AudioFragmentFD.timescale = 48000
    AudioFragmentFD.sampling_rate = 48000
    AudioFragmentFD.channels = 1
    AudioFragmentFD.bits_per_sample = 16
    stream = io.BytesIO()

# Generated at 2022-06-14 15:49:08.002191
# Unit test for function write_piff_header
def test_write_piff_header():
    from .test import (
        get_file_descriptor,
        _DummyFile,
        _create_file,
        _create_file_descriptor,
        assert_content_equals,
        assert_equals,
    )
    from .piff import (
        write_piff_header,
    )
    from ..compat import (
        compat_struct_pack,
        compat_struct_unpack,
    )

    fd = _DummyFile()


# Generated at 2022-06-14 15:49:10.454575
# Unit test for constructor of class IsmFD
def test_IsmFD():
    ismfd = IsmFD()

    assert ismfd.FD_NAME == 'ism', 'IsmFD test error (FD_NAME)'
    assert ismfd.FD_NAME in _AVAILABLE_FD_NAMES, 'IsmFD test error (_AVAILABLE_FD_NAMES)'


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:49:24.339338
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {}
    params['track_id'] = 1
    params['fourcc'] = 'AACL'
    params['duration'] = 10000000
    params['timescale'] = 10000000
    params['language'] = 'und'
    params['height'] = 0
    params['width'] = 0
    params['channels'] = 0
    params['bits_per_sample'] = 0
    params['sampling_rate'] = 0
    write_piff_header(stream, params)

    actual = stream.getvalue()

# Generated at 2022-06-14 15:49:29.283877
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        'height': 720,
        'width': 1280,
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 1000000000,
        'codec_private_data': '0000000167640028AC2C80',
    }
    stream = io.BytesIO()
    write_piff_header(stream, params)
    stream.seek(0)
    assert stream.read(4) == b'\x00\x00\x00\x2C'  # ftyp box
    assert stream.read(4) == b'ftyp'
    assert stream.read(4) == b'isml'  # major brand
    assert u32.unpack(stream.read(4))[0] == 1  # minor version

# Generated at 2022-06-14 15:49:32.460776
# Unit test for function extract_box_data
def test_extract_box_data():
    with open('fragment.ismv', 'rb') as fp:
        with open('moov.dat', 'wb') as fp2:
            fp2.write(extract_box_data(fp.read(), (b'moov',)))



# Generated at 2022-06-14 15:49:45.291069
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import os
    import time

    from .downloader import FileDownloader
    from .downloader import get_suitable_downloader
    from .extractor import get_info_extractor

    test_filename = 'test.mp4'
    if os.path.exists(test_filename):
        os.remove(test_filename)

    def download(url):
        ydl = FileDownloader({'format': 'bestvideo+bestaudio/worst', 'outtmpl': test_filename})
        ie = get_info_extractor(ydl, url)
        ie.download(url)

    def get_ctime(filename):
        return os.stat(filename).st_ctime


# Generated at 2022-06-14 15:49:54.703931
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass


# Generated at 2022-06-14 15:50:05.034661
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from ytdl.downloader.common import FileDownloader
    from ytdl.extractor.ism import Ism
    from ytdl.utils import urlopen
    url = 'http://amssamples.streaming.mediaservices.windows.net/91492735-c523-432b-ba01-faba6c2206a2/AzurePromo.ism/manifest'
    video_id = 'AzurePromo'
    ism = Ism(url, video_id)
    info_dict = ism._real_extract(urlopen(url))

# Generated at 2022-06-14 15:50:15.151094
# Unit test for constructor of class IsmFD
def test_IsmFD():
    import json
    import os
    from .ism import parse_ism_playlist

    downloader = FileDownloader({'url': 'http://foo.com/manifest.ism'})
    # test through IsmFD.real_download
    info_dict = parse_ism_playlist('http://foo.com/manifest.ism', downloader.ydl, None)
    test_filename = 'ism_test_' + info_dict['fragments'][0]['url'].split('/')[-1] + '_' + info_dict['fragments'][-1]['url'].split('/')[-1]
    test_filename = test_filename[:test_filename.rindex('.')]
    test_filename += '.piff'

# Generated at 2022-06-14 15:50:25.379447
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 10000,
        'timescale': 10000,
        'language': 'und',
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 44100,
    }
    stream = io.BytesIO()
    write_piff_header(stream, params)
    result = stream.getvalue()

# Generated at 2022-06-14 15:50:33.614085
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD("http://foo.com/bar")
    assert fd.url == "http://foo.com/bar"
    assert fd.frag_index == 0
    assert fd.params == {}
    assert fd.retries == 10
    assert fd.continuedl == False
    assert fd.noprogress == False
    assert fd.filenums == []
    assert fd.cookiejar is None
    assert fd.nopart == False
    assert fd.restrictedfilenames == False
    assert fd.test is False
    assert fd.fragment_retries == 0
    assert fd.skip_unavailable_fragments == True
    assert fd.keepvideo is False
    assert fd.age_limit is None
    assert fd.min_

# Generated at 2022-06-14 15:50:36.471058
# Unit test for constructor of class IsmFD
def test_IsmFD():
    downloader = IsmFD(params={'file_id': '39Lh8W0YuqD', 'format': 'mpd'})
    assert isinstance(downloader, IsmFD)



# Generated at 2022-06-14 15:50:40.022415
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """
    Test IsmFD constructor
    """
    url = 'http://example.com'
    params = {'isfragmented': True}
    ismFD = IsmFD(url, params)
    assert ismFD is not None



# Generated at 2022-06-14 15:50:52.730407
# Unit test for constructor of class IsmFD
def test_IsmFD():
  from .extractor.common import InfoExtractor
  from .downloader.ism import IsmFD
  if __name__ == "__main__":
    ism_fd = IsmFD

    # Test case where no manifest_url is provided
    # it should throw an exception
    ie = InfoExtractor()
    ie.set_downloader(ism_fd)

# Generated at 2022-06-14 15:51:03.402293
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    mock_urlopen = mock.MagicMock()

# Generated at 2022-06-14 15:51:09.292688
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Create an IsmFD
    ismfd = IsmFD()
    # Test download()
    test_file = 'test_file.ism'
    assert ismfd.download(test_file, 'http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest') == True

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:51:29.952291
# Unit test for function extract_box_data
def test_extract_box_data():
    data = binascii.unhexlify(b'00000014667479707000000000000000100000014667479707100000014667479707200000014667479707300000014667479707400000014667479707500000014667479707600000014667479707700000014667479707800000014667479707900000014667479707a00000014667479707b00000014667479707c00000014667479707d00000014667479707e00000014667479707f00000014667479708000000001466747970810000001466747970820000001466747970830000001466747970840000001466747970850012000000000000002000000000000000000000000000000000000000000000000030000003200000000000000000000')

# Generated at 2022-06-14 15:51:32.778080
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    return IsmFD(None).real_download("test-filename", {})


# Generated at 2022-06-14 15:51:44.120546
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
  """ IsmFD.real_download() should return True if all the download request are successful. """
  url = "http://www.youtube.com/watch?v=9bZkp7q19f0"
  expected_result = True
  params = {
    'fragment_retries': 3,
    'skip_unavailable_fragments': True
  }
  downloader = YoutubeDL(params)
  info_dict = downloader.extract_info(url, download=False)
  params = info_dict['_download_params']
  data = {"url": params['fragments'][0]['url'], "content": "fragment"}
  response = json.dumps(data)

# Generated at 2022-06-14 15:51:55.406208
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    ydl = Ydl()
    ydl.params['fragment_retries'] = 0
    ydl.params['skip_unavailable_fragments'] = False
    ydl.params['test'] = True
    ydl.params['noprogress'] = True
    ydl.params['noplaylist'] = True
    ydl.params['quiet'] = True
    ydl.add_default_info_extractors()
    ydl.download(['https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd'])
    assert len(ydl.download_retcode.errors) == 0
    assert ydl.download_retcode.result


# Generated at 2022-06-14 15:52:00.676706
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    """
    Unit test for method real_download of class IsmFD
    """
    ctx = {'dest_stream': object(), 'fragment_index': 1, 'total_frags': 1, 'filename': 'test'}
    real_download(ctx, 'http://test/')



# Generated at 2022-06-14 15:52:13.136781
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        # Prepare input parameters
        params = {
            'sampling_rate': 44100,
            'bits_per_sample': 16,
            'channels': 2,
            'fourcc': 'AACL',
            'track_id': 1,
            'duration': 1000,
        }
        # Call function to test
        write_piff_header(stream, params)
        # Check result

# Generated at 2022-06-14 15:52:21.367533
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    write_piff_header(
        stream,
        {
            'track_id': 1,
            'fourcc': 'H264',
            'codec_private_data': '0000000167640032ACD9411F832C1F00000168CE03880',
            # https://tools.ietf.org/html/draft-ietf-payload-rtp-h264-15#section-5.1
            'width': 1920,
            'height': 1080,
            'duration': 736000,  # seconds to microseconds
            'sampling_rate': 44100,
            'channels': 2,
        }
    )
    stream.seek(0)
    data = stream.read()
    assert len(data) == 523

# Generated at 2022-06-14 15:52:31.730856
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:52:38.557383
# Unit test for constructor of class IsmFD
def test_IsmFD():
    return {
        'url': 'http://keycdn.theoplayer.com/demos/assets/ism/0096/manifest.ism/Manifest',
        'info_dict': {
            'id': '0096',
            'ext': 'mp4',
            'title': 'Albatross (H264)',
        },
        'params': {
            'outtmpl': '%(id)s.%(ext)s',
        },
        'skip': 'Requires rtmpdump'
    }

# Generated at 2022-06-14 15:52:39.246477
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass


# Generated at 2022-06-14 15:53:16.951935
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    tmp_name = get_temp_filename(u'.ism')
    ctx = {'filename': tmp_name, 'total_frags': 10}

# Generated at 2022-06-14 15:53:24.668862
# Unit test for function write_piff_header
def test_write_piff_header():
    import re
    import hashlib
    from .test_fragment import test_write_moof_fragment, test_read_piff_header

    params = {
        'track_id': 0x0FFA,
        'fourcc': 'AACL',
        'duration': 731000000,
        'sampling_rate': 44100,
    }
    stream = io.BytesIO()
    write_piff_header(stream, params)
    stream = io.BytesIO(stream.getvalue())
    test_read_piff_header(stream, params)
    stream.close()
    stream = io.BytesIO()


# Generated at 2022-06-14 15:53:30.225733
# Unit test for constructor of class IsmFD
def test_IsmFD():
    test_Case = IsmFD(params= {'url': 'https://test-ismc.akamaized.net/hls/live/578440/ngp/master.m3u8'},
                      downloader_params= {'test': True})
    print(test_Case)


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:53:40.881300
# Unit test for function write_piff_header
def test_write_piff_header():
    #params = {'track_id': 1, 'language': 'eng', 'codec_private_data': '01640029ffe100188e27c0', 'width': 1280, 'bits_per_sample': 16, 'channels': 2, 'fourcc': 'AVC1', 'height': 720, 'sampling_rate': 48000}
    params = {'track_id': 1, 'duration': 23961016735, 'language': 'eng', 'sampling_rate': 44100, 'bits_per_sample': 16, 'fourcc': 'AACL', 'channels': 2}
    stream = io.BytesIO()
    write_piff_header(stream, params)
    with open('moov.bin','wb') as f:
        f.write(stream.getvalue())

# Generated at 2022-06-14 15:53:48.314877
# Unit test for function extract_box_data
def test_extract_box_data():
    assert(extract_box_data(b'moovtest', [b'moov']) == b'test')
    assert(extract_box_data(b'\x00\x00\x00\x0cmoovteststbl', [b'moov', b'stbl']) == b'test')
    assert(extract_box_data(b'\x00\x00\x00\x18moov\x00\x00\x00\x08testteststbl', [b'moov', b'stbl']) == b'testtest')
    assert(extract_box_data(b'moovtestteststbl', [b'stbl']) == b'')

# Generated at 2022-06-14 15:53:59.808915
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import FakeYDL
    from .extractor.common import InfoExtractor

    import io
    import random
    import re

    def make_random_string(min_length, max_length):
        length = random.randint(min_length, max_length)
        return b''.join((b'%c' % random.randint(0, 255) for _ in range(length)))

    def generate_ism_manifest(track_id, duration, timescale, single_segment):
        manifest = {}
        manifest['track_id'] = track_id
        manifest['segment_timeline'] = [{'duration': duration}]
        manifest['is_live'] = False
        manifest['adaptive_type'] = 'ISM'
        manifest['playlist_type'] = 'VOD'

# Generated at 2022-06-14 15:54:09.390257
# Unit test for function write_piff_header
def test_write_piff_header():
    import base64
    import binascii
    from .hls_m3u8 import HLS_M3U8_SEGMENT_URL
    from .hls_m3u8 import HLS_M3U8_TARGET_DURATION
    from .hls_m3u8 import HLS_M3U8_DISCONTINUITY
    from .hls_m3u8 import HLS_M3U8_EXT_X_ALLOW_CACHE
    from .hls_m3u8 import HLS_M3U8_CODECS
    from .hls_m3u8 import HLS_M3U8_EXT_X_BYTERANGE
    from .hls_m3u8 import HLS_M3U8_EXT_X_MAP

# Generated at 2022-06-14 15:54:12.690213
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD('test')
    assert fd.FD_NAME == "ism"
    assert fd.params == {}
    assert fd.dest_stream == 'test'


# Generated at 2022-06-14 15:54:16.319446
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    input_filename = 'data1.ism/Manifest'
    output_filename = 'testoutput.ismv'
    # Example of class initialization
    ismfd = IsmFD()
    # Example of real_download method
    ismfd.real_download(output_filename, input_filename)

# Unit test module initialization

# Generated at 2022-06-14 15:54:25.376835
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'fourcc': 'mp4a',
        'track_id': 1,
        'duration': 1,
        'timescale': 1,
        'bits_per_sample': 16,
        'channels': 1,
        'sampling_rate': 8000,
    }
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:54:53.399042
# Unit test for constructor of class IsmFD
def test_IsmFD():
    assert IsmFD.can_download('https://example.com/file.ism/manifest')
    assert IsmFD.can_download('https://example.com/file.ism/manifest(format=mpd-time-csf)')
    assert IsmFD.can_download('https://example.com/file.ism/QualityLevels(100000)/Manifest')

    assert not IsmFD.can_download('https://example.com/file.m3u8')
    assert not IsmFD.can_download('https://example.com/file.mpd')
    assert not IsmFD.can_download('https://example.com/file.ism')


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:55:04.602719
# Unit test for function write_piff_header
def test_write_piff_header():
    fd = io.BytesIO()

# Generated at 2022-06-14 15:55:15.977755
# Unit test for function write_piff_header
def test_write_piff_header():
    fd = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 1574400000,
        'width': 640,
        'height': 360,
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 44100,
        'codec_private_data': '67640028ffe1000b676f48042801b8529d004800011f80000300800000105d00101e4023090307020500fffe100f4d4d453e4d4c0f4d453d43430f43430d43410d43410b43400b4340094340094340084340',
    }
    write_piff_header(fd, params)


# Generated at 2022-06-14 15:55:21.438023
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .dash import add_ns, NS_MAP
    from .extractor import get_info_extractor
    from .downloader import determined
    from .utils import encode_data_uri

    def _test_IsmFD(url, data, params, result_info_dict=None, **fetch_params):
        # Extract info dict
        info_extractor = get_info_extractor(url)
        context = determined(dummy_opener)
        info_dict = info_extractor._real_extract(context, url, downloader=None, **fetch_params)
        # Fetch ISM manifest
        manifest = compat_urllib_request.urlopen(info_dict['url']).read()
        # Create manifest for test
        manifest_parts = manifest.split(b'<!--')

# Generated at 2022-06-14 15:55:29.786890
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Fake params for testing
    params = {
         'test': True,
    }
    fake_info_dict = {
        'fragments':['url1', 'url2'],
        '_download_params':[{}],
    }
    # Try calling function with fake params
    result = IsmFD.real_download('filename', fake_info_dict, params)
    return result

ism_fd = IsmFD()


# Generated at 2022-06-14 15:55:38.816000
# Unit test for function write_piff_header
def test_write_piff_header():
    from cStringIO import StringIO
    from ..extractor import gen_extractors
    from ...utils import ExtractorError

    fd = StringIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 2,
        'timescale': 2,
        'width': 1920,
        'height': 1080,
        'codec_private_data': '01640028ffe1000867640028ac72c8022c0a8a8a8c0'
    }

    write_piff_header(fd, params)

    fd.seek(0)
    extractor = gen_extractors(fd, params)
    assert len(extractor) == 1

# Generated at 2022-06-14 15:55:49.890483
# Unit test for function write_piff_header
def test_write_piff_header():
    # Audio track
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 34425,
        'sampling_rate': 44100,
        'channels': 2,
        'bits_per_sample': 16
    }
    stream = io.BytesIO()
    write_piff_header(stream, params)
    # Video track
    params = {
        'track_id': 2,
        'fourcc': 'H264',
        'duration': 5012,
        'width': 1280,
        'height': 720,
        'nal_unit_length_field': 1,
        'codec_private_data': '0000000167640028ac2b4028683ef0a10000000168ebe3c80',
    }
    write_

# Generated at 2022-06-14 15:55:54.910859
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL(params={'quiet': True, 'simulate': True, 'format': 'ism'})
    try:
        ydl.download(['http://www.example.com/'])
        assert False
    except DownloadError as e:
        assert str(e) == 'No IsmFD info extractor available'

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:55:56.665857
# Unit test for constructor of class IsmFD
def test_IsmFD():
    return IsmFD

# Since this is null it's not really required

# Generated at 2022-06-14 15:56:04.822465
# Unit test for function extract_box_data
def test_extract_box_data():
    from .common import make_tempfile

    with make_tempfile(u8.pack(8) * 2 + box(b'abcd', b'efgh')) as f:
        assert extract_box_data(b'', [b'abcd']) is None
        assert extract_box_data(u32.pack(22) + box(b'abcd', b'efgh'), [b'abcd']) == b'efgh'
        assert extract_box_data(u32.pack(22) + box(b'abcd', b'efgh'), [b'abcd', b'efgh']) == b'efgh'
        assert extract_box_data(u32.pack(22) + box(b'abcd', b'efgh'), [b'efgh']) is None
        assert extract_box_data

# Generated at 2022-06-14 15:57:21.381139
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:57:27.868961
# Unit test for function write_piff_header
def test_write_piff_header():
    fd = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 1000,
        'timescale': 10000000,
        'width': 640,
        'height': 360,
        'codec_private_data': '01640028ffe1000568c80',
        'nal_unit_length_field': 4,
    }
    write_piff_header(fd, params)

# Generated at 2022-06-14 15:57:28.648994
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass


# Generated at 2022-06-14 15:57:36.682811
# Unit test for function extract_box_data
def test_extract_box_data():
    assert extract_box_data(b'\x00\x00\x00\x10ftyp' + b'\x00\x00\x00\x20moov' + b'\x00\x00\x00\x10ftyp'
                            + b'\x00\x00\x00\x10moov' + b'\x00\x00\x00\x10moov', (b'moov', b'moov')) == (b'\x00\x00\x00\x10ftyp' + b'\x00\x00\x00\x10moov')

# Generated at 2022-06-14 15:57:47.710596
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from ..compat import parse_qs
    test_uri = 'ism://someserver.com/somepath/Manifest'