

# Generated at 2022-06-14 15:48:22.525651
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 50000000,
        'timescale': 10000000,
        'language': 'eng',
        'height': 720,
        'width': 1280,
        'nal_unit_length_field': 4,
        'codec_private_data': '0164001fffe1001867640029ac400000168ee3880',
    }
    write_piff_header(stream, params)
    # FIXME: Add proper unit testing
if __name__ == '__main__':
    test_write_piff_header()

# Generated at 2022-06-14 15:48:33.151328
# Unit test for function extract_box_data
def test_extract_box_data():
    test_data = b'\x00\x00\x00\x3c' + b'stsd' + b'\x00\x00\x00\x00\x00\x01' + b'\x02\x02'
    assert extract_box_data(test_data, (b'stsd',)) == b'\x00\x00\x00\x00\x00\x01' + b'\x02\x02'
    assert extract_box_data(test_data, (b'stsd', b'\x02\x02')) == b'\x00\x00\x00\x00'
    assert extract_box_data(test_data, (b'stts',)) is None



# Generated at 2022-06-14 15:48:45.469124
# Unit test for function write_piff_header
def test_write_piff_header():
    test_params_1 = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 10,
        'timescale': 10000,
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 44100
    }
    test_params_2 = {
        'track_id': 2,
        'fourcc': 'AVC1',
        'duration': 10,
        'timescale': 10000,
        'height': 720,
        'width': 1280,
        'codec_private_data': '01640033ACFFE300D2B6C34297F3D2C8BF47001F6740003289660F12C80'
    }
    with io.BytesIO() as stream:
        write_piff

# Generated at 2022-06-14 15:48:50.667505
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    ''' test_IsmFD.test_real_download '''
    # test real_download method of class IsmFD
    # TODO: unit test fails
    import os
    import tempfile
    import random
    import string
    import json
    import shutil
    import subprocess

    import youtube_dl.YoutubeDL
    import youtube_dl.InfoExtractors.ism

    CWD = os.getcwd()


# Generated at 2022-06-14 15:49:00.039992
# Unit test for function write_piff_header
def test_write_piff_header():
    from contextlib import closing
    from os import fstat
    from os.path import getsize
    from tempfile import NamedTemporaryFile

    with closing(NamedTemporaryFile()) as f:
        stream = fd_or_path_open(f, 'wb')

# Generated at 2022-06-14 15:49:02.210377
# Unit test for constructor of class IsmFD
def test_IsmFD():
    ismfd = IsmFD('foo.ism', {})
    assert ismfd.FD_NAME == 'ism'

# Generated at 2022-06-14 15:49:14.108393
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    url = ('http://smf.blob.core.windows.net/samples/videos/bigbuckbunny.ism/bigbuckbunny.ism')
    destination_path = "bigbuckbunny.mp4"
    params = {
        'track_id': 1,
        'fourcc': 'AVC1',
        'duration': 334595,
        'timescale': 10000000,
        'nal_unit_length_field': 4,
        'codec_private_data': '01640029ff4c0a20',
        'width': 640,
        'height': 360,
    }
    ism_fd = IsmFD(url, params)
    info_dict = {
        '_download_params': params,
        'fragments': [{'url': url}],
    }


# Generated at 2022-06-14 15:49:26.601401
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:49:34.356556
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():

    ctx = {
        'filename': 'dummy.mp4',
        'total_frags': 1,
    }

    _download_fragment = lambda _ctx, _dummy: (True, b'\x00' * 8 + b'moof' + b'\x00' * 4 + b'traf' + b'\x00' * 4 + b'tfhd' + b'\x00' * 4 + u32.pack(1))

    _append_fragment = lambda _ctx, _frag_content: None
    _finish_frag_download = lambda *_: None

    def _prepare_and_start_frag_download(_ctx):
        _ctx['dest_stream'] = io.BytesIO()
        _ctx['fragment_index'] = 0

# Generated at 2022-06-14 15:49:38.604458
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Test case where no url is given
    IsmFD({}, None)

    # Test case where a url is given
    IsmFD({'url': 'http://url.com'}, None)



# Generated at 2022-06-14 15:55:05.649883
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        "track_id": 1,
        "fourcc": 'avc1',
        "duration": 1000,
        "timescale": 10000000,
        "language": 'und',
        "height": 480,
        "width": 640,
        "codec_private_data": "01640028ffe1000c27640028acd9405f08011204811a33c1350cc400f85a8b68d0"
    }
    buf = io.BytesIO()
    write_piff_header(buf, params)
    # print(buf.getvalue().hex())
    # Open file for writing
    with open('test_write_piff_header.ismv', mode='wb') as file:
        file.write(buf.getvalue())

# Generated at 2022-06-14 15:55:17.419955
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
  ctx = {
    'filename': 'C:/temp/test_sample.ism',
    'total_frags': 2
  }
  info_dict = {
    'fragments': [{'url': 'QQQ'}, {'url': 'WWW'}],
    '_download_params': {
      'track_id': 1,
      'width': 0,
      'height': 0,
      'bits_per_sample': 16,
      'channels': 2,
      'duration': 0,
      'fourcc': 'AACL',
      'sampling_rate': 48000,
      'timescale': 10000000
    }
  }

# Generated at 2022-06-14 15:55:31.716721
# Unit test for constructor of class IsmFD
def test_IsmFD():
    class TestIsmFD(IsmFD):
        def real_download(self, filename, info_dict):
            raise NotImplementedError()

    info_dict = {'fragments': []}

    TestIsmFD('http://host.tld/ism/manifest', info_dict)
    TestIsmFD('http://host.tld/ism/manifest.ism/Manifest', info_dict)
    TestIsmFD('http://host.tld/m3u8/manifest.ism/Manifest', info_dict)
    TestIsmFD('http://host.tld/ism/manifest.ism/QualityLevels(1280)/Manifest', info_dict)

# Generated at 2022-06-14 15:55:40.476836
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        params = {
            'track_id': 1,
            'fourcc': 'H264',
            'duration': 10000000,
            'timescale': 10000000,
            'sampling_rate': 44100,
            'bits_per_sample': 16,
            'language': 'und',
            'width': 0,
            'height': 0,
            'codec_private_data': '0000000167428029c8140000a082011869f8020002d8'
                                  '50204000422f23a0bbd8eba83012c4456c4000001bb80'
                                  '00a0023f08c2ecbd7e69',
        }
        write_piff_header(stream, params)

# Generated at 2022-06-14 15:55:52.976293
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        params = {
            'track_id': 1,
            'fourcc': 'AACL',
            'channels': 2,
            'bits_per_sample': 16,
            'sampling_rate': 44100,
            'duration': 20000000,
        }
        write_piff_header(stream, params)

# Generated at 2022-06-14 15:56:03.166059
# Unit test for function write_piff_header
def test_write_piff_header():
    output = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AVC1',
        'duration': 0,
        'width': 640,
        'height': 480,
        'codec_private_data': '000000016764001EACD940800D83A30A018001002A0000018E22C48D90000019CE8DE0',
        'nal_unit_length_field': 4
    }
    write_piff_header(output, params)
    expected = b'\x00\x00\x00\x58ftypisml\x00\x00\x00\x00\x00\x00\x00\x00piffiso2'

# Generated at 2022-06-14 15:56:14.100553
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .test_download import extract_id, get_testcases
    from .downloader import FileDownloader

    testcases = get_testcases()
    for testcase in testcases:
        url = testcase[0]
        info_dict = testcase[1]
        expected_streams = testcase[2]

        ydl = FileDownloader({})
        extract_id(ydl)
        if ydl.params.get('print_id', False):
            continue

        ie = IsmFD(ydl=ydl)
        # Saves the manifest and the segments to the disk.
        success = ie.real_download("IsmFD-test.ismv", info_dict)
        assert success



# Generated at 2022-06-14 15:56:22.388794
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """Test constructor of class IsmFD"""
    ydl = YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

# Generated at 2022-06-14 15:56:25.019974
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD()

__all__ = [IsmFD]

# Generated at 2022-06-14 15:56:32.051401
# Unit test for constructor of class IsmFD
def test_IsmFD():
    def construct_IsmFD(params):
        params = params.copy()
        # The real functionality of construct_IsmFD is to copy the
        # first fragment of the manifest to our file-like object 'dest_stream'
        # and we need to pass some information in 'params', so let's pretend we do it

        # Extract 'url' parameter and find out if we are dealing with an ISMV file or an ISMC file
        url = params['url']
        if 'ismv' in url:
            filename = params['filename']
            # Write a header to the output file
            with open(filename, 'wb') as f:
                write_piff_header(f, params)
            # Fake the rest of the file from now on
            params['url'] = url.replace('ismv', 'ismc')
        # Call the real constructor