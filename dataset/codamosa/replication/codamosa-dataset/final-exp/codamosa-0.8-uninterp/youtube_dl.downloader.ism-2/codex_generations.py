

# Generated at 2022-06-14 15:48:16.870088
# Unit test for constructor of class IsmFD
def test_IsmFD():
    IsmFD(None, None, None, None)



# Generated at 2022-06-14 15:48:28.957654
# Unit test for function write_piff_header
def test_write_piff_header():
    import test_utils
    import os

    def _download(url):
        tmp_file = test_utils.get_temp_file(suffix='.ismv')
        request = compat_urllib_request.Request(url)
        request.add_header('User-Agent', test_utils.USER_AGENT)
        try:
            data = compat_urllib_request.urlopen(request).read()
        except (compat_urllib_error.URLError, compat_http_client.HTTPException, socket.error) as err:
            os.remove(tmp_file)
            raise ExtractorError('Unable to download ' + url + ': ' + compat_str(err))

# Generated at 2022-06-14 15:48:32.752670
# Unit test for function write_piff_header
def test_write_piff_header():
    from .testcases import testcases

    for case in testcases:
        # Just try
        stream = io.BytesIO()
        with FragmentFD(stream) as fd:
            write_piff_header(fd, case['param'])


# Generated at 2022-06-14 15:48:39.785130
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:48:40.479442
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    return None

# Generated at 2022-06-14 15:48:41.680405
# Unit test for constructor of class IsmFD
def test_IsmFD():
    print(IsmFD)
    return True

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:48:52.502735
# Unit test for function write_piff_header
def test_write_piff_header():
    import pytest
    from .test import stream_test, get_test_data_file
    stream = io.BytesIO()
    with pytest.warns(UserWarning) as warning:
        write_piff_header(stream, {
            'track_id': 1,
            'fourcc': 'H264',
            'codec_private_data': '0000000167428029DE7A22D10000000168CE0388DE7A22D1',
            'language': 'eng',
            'width': 640,
            'height': 480,
            'duration': 12300000})
    assert warning[0].message.args == ('Unknown codec for video',)

    assert stream_test(stream, get_test_data_file('video.mov'))

    stream = io.BytesIO()
    write_piff

# Generated at 2022-06-14 15:49:01.137745
# Unit test for function extract_box_data
def test_extract_box_data():
    # Test for the case in which there is no box of the given box_sequence
    mp4_sample = binascii.unhexlify(b'6d70347600000000')  # mp4v00000000
    assert extract_box_data(mp4_sample, (b'piff', b'mdat')) is None

    # Test for the case in which there is a box of the given box_sequence
    mp4_sample = binascii.unhexlify(b'6d70347600000000' + b'6d61740000000000' + b'00000001')  # mp4v00000000 + mdat00000000 + 00000001
    assert extract_box_data(mp4_sample, (b'piff', b'mdat')) == b'\x00' * 8
test_extract_box_data()



# Generated at 2022-06-14 15:49:13.293850
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()

# Generated at 2022-06-14 15:49:25.849669
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor.common import InfoExtractor
    from .downloader.common import FileDownloader
    from .utils import encode_data_uri


# Generated at 2022-06-14 15:49:44.067879
# Unit test for constructor of class IsmFD
def test_IsmFD():
    test_IsmFD = IsmFD(None, {'test': True})
    # test for name
    assert test_IsmFD.FD_NAME == 'ism'
    # test for params 
    assert test_IsmFD.params == {'test': True}
    # test for real_download function
    assert test_IsmFD.real_download == IsmFD.real_download

# Generated at 2022-06-14 15:49:55.843804
# Unit test for function write_piff_header
def test_write_piff_header():
    """
    Test the public functions write_piff_header
    """

# Generated at 2022-06-14 15:50:05.676695
# Unit test for constructor of class IsmFD
def test_IsmFD():
    url_info_dict = {
        'url': 'http://localhost/',
        'player_url': 'http://localhost/',
        'http_headers': {},
        'fragments': [
            {
                'url': 'http://localhost/?test=test'
            }
        ],
        '_download_params': {
            'track_id': 0,
            'fourcc': 'H264',
            'duration': 0,
            'timescale': 10000000,
            'language': 'und',
            'height': 0,
            'width': 0
        }
    }

    output_path = os.path.join(os.path.dirname(__file__), 'test_IsmFD.ism')

# Generated at 2022-06-14 15:50:15.632024
# Unit test for function extract_box_data
def test_extract_box_data():
    box_data = b'\x00\x00\x00\x00'
    try:
        extract_box_data(box_data, (b'\x00\x00\x00\x00'))
    except:
        print('extract_box_data err1')
    box_data = b'\x00\x00\x00\x01\x00\x00\x00\x01'
    try:
        extract_box_data(box_data, (b'\x00\x00\x00\x00'))
    except:
        print('extract_box_data err2')
    box_data = b'\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00'


# Generated at 2022-06-14 15:50:25.835694
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    print('Testing real_download')

    test_url = 'http://test.com/test.ismv'
    test_filename = 'test_filename.ismv'

# Generated at 2022-06-14 15:50:32.212164
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Test with real manifest file
    manifest_url = 'http://pdl.warnerbros.com/wbol/us/dd/med/harry_potter_and_the_deathly_hallows_part_2/harry_potter_and_the_deathly_hallows_part_2_franchise_trailer_480p_dl.ism/Manifest'
    ism_fd = IsmFD(manifest_url, {})

    # Check if it's an IsmFD
    assert ism_fd.fd_name() == 'ism'


# Generated at 2022-06-14 15:50:41.367616
# Unit test for function extract_box_data
def test_extract_box_data():
    box1_data = u32.pack(0x10) + b'box1' + u32.pack(0x20) + b'box_data1'
    box2_data = u32.pack(0x10) + b'box2' + u32.pack(0x20) + b'box_data2'
    data = u32.pack(0x10) + b'box' + u32.pack(len(box1_data) + len(box2_data) + 0x10) + box2_data + box1_data
    assert(extract_box_data(data, (b'box', b'box1',)) == b'box_data1')
    assert(extract_box_data(data, (b'box', b'box2',)) == b'box_data2')




# Generated at 2022-06-14 15:50:51.032305
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """
    Unit test for constructor of class IsmFD
    """

    manifest_url = 'http://mdstrm.com/live-stream/56c25d6fe4b0a2c64a0a91b9/manifest_high.m3u8'
    _, ext = os.path.splitext(manifest_url)
    ismfd = IsmFD(manifest_url, {'name': '', 'ext': ext}, params={'skip_unavailable_fragments': False})
    assert(ismfd.manifest_url == manifest_url)



# Generated at 2022-06-14 15:51:02.181780
# Unit test for method real_download of class IsmFD

# Generated at 2022-06-14 15:51:12.450086
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    stream = io.StringIO()
    write_piff_header(stream, {'track_id': 0, 'fourcc': 'AACL', 'duration': 0, 'timescale': 0, 'language': 'und', 'sampling_rate': 0})

# Generated at 2022-06-14 15:55:42.756193
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import pycurl
    import io

    class MockPyCurl:
        """Mock pycurl.Curl class"""

        def __init__(self):
            self.url = ''
            self.buffer = io.BytesIO()
            self.headers = {}

        def setopt(self, option, param):
            if option == pycurl.URL:
                self.url = param
            elif option == pycurl.WRITEDATA:
                self.buffer = param
            elif option == pycurl.HTTPHEADER:
                for header in param:
                    name, value = header.split(b':', 1)
                    self.headers[name.strip()] = value.strip()

# Generated at 2022-06-14 15:55:51.332259
# Unit test for function write_piff_header
def test_write_piff_header():
    from ..third_party.piff_info import piff_info
    stream = io.BytesIO()
    write_piff_header(stream, {'track_id': 1, 'fourcc': 'AVC1', 'codec_private_data': '000000016742802995FA0', 'duration': 9999900, 'width': 640, 'height': 360})
    assert piff_info(stream.getvalue()) is not None



# Generated at 2022-06-14 15:56:00.433212
# Unit test for function write_piff_header
def test_write_piff_header():
    header_size = 4 + 8 + 156 + 4 + 8 + 92 + 4 + 8 + 20 + 4 + 8 + 8 + 4 + 8 + 24 + 4 + 8 + 24
    #file_size = 0
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'timescale': 10000000,
        'duration': 872000,
        'sampling_rate': 44100,
        'channels': 2,
        'bits_per_sample': 16,
        'fourcc': 'AACL'
    }
    write_piff_header(stream, params)
    assert stream.tell() == header_size



# Generated at 2022-06-14 15:56:07.991233
# Unit test for constructor of class IsmFD
def test_IsmFD():
    filename = 'sintel-trimmed-fragmented.ism'
    params = {'frag_index': 0,
              'test': True,
              'skip_unavailable_fragments': True,
              'fragment_retries': 0,
              'format': 'bestvideo+bestaudio',
              'playlist_items': '-1',
              'outtmpl': filename,
              'nooverwrites': True,
              'playliststart': -1,
              'playlistend': -1,
              'playlist_items': -1,
              'merge_output_format': 'mp4',
              'noplaylist': True,
              'cachedir': False}


# Generated at 2022-06-14 15:56:18.766781
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import os
    import shutil
    import tempfile
    import m3u8
    from .test_download import (
        FakeYDL,
    )

    # First test case
    # Create temp directory
    tempdir = tempfile.mkdtemp(prefix='youtubedl')
    # Create a new FakeYDL object
    ydl_opts = {'outtmpl': os.path.join(tempdir, '%(id)s'),
                'noplaylist': True,
                'quiet': True}
    ydl = FakeYDL(ydl_opts)
    # Create a new IsmFD object
    ism_fd = IsmFD(ydl, ydl_opts)
    # Create a new VideoInfoExtractor using the FakeYDL object

# Generated at 2022-06-14 15:56:28.645120
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        write_piff_header(stream, {
            'track_id': 1,
            'fourcc': 'AVC1',
            'duration': 10000000,
            'timescale': 10000000,
            'language': 'und',
            'width': 1920,
            'height': 1080,
            'codec_private_data': '01640028ffe1000867640028ac2c802921c008ef6d960633e4af5983a00e3a53c01c2f00'
        })

# Generated at 2022-06-14 15:56:32.374318
# Unit test for constructor of class IsmFD
def test_IsmFD():
    ism = IsmFD({'username': 'test_user', 'password': 'test_password', 'url': 'http://test.url.com/test.ismv', 'test': False, 'fragment_retries': 0, 'skip_unavailable_fragments': True, 'format_id': 'test_format_id'}, None, None)
    assert ism

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:56:41.878072
# Unit test for method real_download of class IsmFD

# Generated at 2022-06-14 15:56:51.384564
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Constructor of class IsmFD

    # Test Input Parameters
    ismfd = IsmFD('http://example.com/test.ism/manifest(format=m3u8-aapl-v3).m3u8', params={'skip_unavailable_fragments': True, 'fragment_retries': 0, 'test': True}, output_dir='.', merge_output_format='mp4', verbose=True, forceurl=True, forceduration=None, forcetitle=None, forcetotal=False, sim_formats_only=False, simulate=False, quiet=False, skip_download=False, format=None, skip_unavailable_fragments=None, fragment_retries=None, test=False)
    print(ismfd.FD_NAME)
    print(ismfd.params)
    print

# Generated at 2022-06-14 15:57:01.491505
# Unit test for method real_download of class IsmFD