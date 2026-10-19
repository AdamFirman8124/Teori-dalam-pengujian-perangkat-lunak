

# Generated at 2022-06-14 15:48:27.371863
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:48:40.311243
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Using a simple playlist with just one fragment
    test_playlist = "https://priv.example.com/master.m3u8"
    ismfd = IsmFD(test_playlist, params={})

# Generated at 2022-06-14 15:48:45.142074
# Unit test for function extract_box_data
def test_extract_box_data():
    sample_data = b'moovtrakmdia'
    box_type = b'trak'
    box_data = extract_box_data(sample_data, (box_type,))
    assert box_data == b'mdia'
    box_type = b'mdia'
    box_data = extract_box_data(sample_data, (b'trak', box_type))
    assert box_data == b''

# Generated at 2022-06-14 15:48:54.731941
# Unit test for function write_piff_header
def test_write_piff_header():
    import hashlib
    f = io.BytesIO()
    params = {
        'fourcc': 'H264',
        'nal_unit_length_field': 4,
        'codec_private_data': '0164001fffe100176764001facd94080b0401f88e0143314190140016e7a2c01000468ee3c80',
        'width': 640,
        'height': 480,
        'track_id': 1,
        'duration': 1,
    }
    write_piff_header(f, params)
    assert hashlib.md5(f.getvalue()).hexdigest() == 'a028fcb4ae4f4be66eadbd4b4da08a7d'  # noqa



# Generated at 2022-06-14 15:49:08.120670
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    self = IsmFD()
    import os
    for filename in os.listdir('download'):
        os.remove('download/' + filename)
    from collections import OrderedDict
    from .extractor import YoutubeIE
    from .bytestringpattern import ByteStringPattern
    filename = 'download/00001'
    info_dict = OrderedDict()
    info_dict['url'] = 'http://manifest.us.llnwd.net/hls/vod/clear/157000/157000/157000.ism/157000.m3u8'
    info_dict['fragments'] = [OrderedDict()]

# Generated at 2022-06-14 15:49:17.318177
# Unit test for function write_piff_header
def test_write_piff_header():
    memfile = io.BytesIO()

# Generated at 2022-06-14 15:49:22.695434
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        write_piff_header(stream, {'track_id': 1, 'fourcc': 'AACL', 'language': 'und', 'width': 0, 'height': 0, 'sampling_rate': 48000, 'duration': 4200000000})

# Generated at 2022-06-14 15:49:32.062375
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import gen_extractors
    generic_downloads = gen_extractors('generic')
    for ie in generic_downloads:
        if hasattr(ie, '_WORKING'):
            raise RuntimeError('Test can not run because of the previous "--test" execution')

# Generated at 2022-06-14 15:49:42.135052
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import gen_extractors
    extractors = gen_extractors()
    for ie_name in sorted(extractors.keys()):
        if ie_name in ('generic', 'googledrive', 'googlesearch', 'http', 'rtmp'):
            continue
        ie = extractors[ie_name]()
        if ie_name == 'ism':
            assert isinstance(ie.fd.__class__(), IsmFD)
        else:
            assert isinstance(ie.fd.__class__(), FragmentFD)


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:49:54.053691
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    manifest_url = 'http://media.example.com/ism/manifest.ism'

# Generated at 2022-06-14 15:50:15.733712
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # test_IsmFD_object_creation()
    from .smoothstreams import SmoothStreamsFD
    #
    # Test video stream
    #
    # Test a video stream containing a video and an audio track
    test_url_video_stream = 'http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest'

# Generated at 2022-06-14 15:50:25.831025
# Unit test for function write_piff_header
def test_write_piff_header():
    params = dict()
    params['track_id'] = 1
    params['fourcc'] = 'H264'
    params['duration'] = 10000000000
    params['timescale'] = 10000000
    params['language'] = 'und'
    params['height'] = 720
    params['width'] = 1280
    params['nal_unit_length_field'] = 4
    params['codec_private_data'] = '000000016742c0ffd868ee9e3050f008ae14a2050000030017742e001fdf900000b852a500000568ca500000568ca500000568ca500000568ca500000168efb0'
    stream = io.BytesIO()
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:50:28.181392
# Unit test for constructor of class IsmFD
def test_IsmFD():
    print("[downloader/ism] test_IsmFD()")
    ydl = YoutubeDL({})
    dl = IsmFD("http://example.com", {})
    assert dl.params == ydl.params

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:50:35.110790
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """
    Test constructor of class IsmFD
    """
    ydl = YoutubeDL({'forceurl': True})
    frag_downloader = IsmFD(ydl, {
        'format': 'ismv',
        'key': 'base_url/segment_key',
        'fragments': [
            {'url': 'base_url/segment_1',},
            {'url': 'base_url/segment_2',},
        ],
    })
    assert frag_downloader.base_url == 'base_url/'
    assert frag_downloader.frag_count == 2
    assert frag_downloader.dctx.params['key'] == 'base_url/segment_key'

# Generated at 2022-06-14 15:50:42.840855
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as f:
        write_piff_header(f, {
            'track_id': 1,
            'fourcc': 'AACL',
            'duration': 92651000,
            'timescale': 10000000,
            'language': 'eng',
            'channels': 2,
            'bits_per_sample': 16,
            'sampling_rate': 48000,
        })
        with open('write_piff_header.dat', 'wb') as write_file:
            write_file.write(f.getvalue())

        f.seek(0)
        with open('write_piff_header.txt', 'w') as write_file:
            write_file.write(binascii.hexlify(f.getvalue()).decode('utf-8'))


# Generated at 2022-06-14 15:50:55.763744
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import FakeYDL
    from .extractor.common import InfoExtractor
    from .compat import compat_urllib_request
    from .compat import compat_urlparse
    from .compat import compat_socket
    from .downloader import HttpFD
    from .downloader.fragment import FragmentFD
    from .downloader.http import MediaFD
    from .downloader.external_downloader import ExternalFD
    from .utils import struct_unpack
    from .utils import extract_attributes
    from .utils import int_or_none
    from .utils import xpath_text
    from .utils import xpath_attr
    from .utils import int_or_none
    from .utils import float_or_none
    from .utils import update_url_query
    from .utils import unescapeHTML
   

# Generated at 2022-06-14 15:51:05.022446
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import USER_AGENT
    from .downloader import extractor
    from .downloader import FileDownloader
    from .extractor import gen_extractors
    from .compat import compat_urllib_request
    from .YoutubeDL import YoutubeDL
    from os.path import join as os_join

    # _download_fragment

# Generated at 2022-06-14 15:51:07.836775
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    real_download(IsmFD)

if __name__ == '__main__':
    os.chdir('../')
    test_IsmFD_real_download()

# Generated at 2022-06-14 15:51:15.512307
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:51:27.561074
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .test_fragment_downloader import TestFD
    from .test_common import download_content
    from .test_common import mock_http_server
    from .test_login import test_login
    import collections


# Generated at 2022-06-14 15:51:47.826959
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 12345,
    }
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:51:48.450078
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass



# Generated at 2022-06-14 15:51:58.836167
# Unit test for function write_piff_header
def test_write_piff_header():
    def _test_audio(**kwargs):
        with io.BytesIO() as stream:
            params = {
                'track_id': 1,
                'fourcc': 'AACL',
                'duration': 1000000000,
                'timescale': 10000000,
                'language': 'und',
                'height': 0,
                'width': 0,
                'sampling_rate': 44100,
                'channels': 2,
                'bits_per_sample': 16,
            }
            params.update(kwargs)
            write_piff_header(stream, params)
            return stream.getvalue()

# Generated at 2022-06-14 15:52:10.801159
# Unit test for constructor of class IsmFD
def test_IsmFD():
    info = {u'name': u'Mad Men', u'protocol': u'm'}
    fd = IsmFD(info)

    return fd.__class__.__name__ == 'IsmFD'
    
# 'https://media.example.com/title.ism/QualityLevels({bitrate})/Fragments(video=0,format={format})'
# 'Url': '{protocol}://{manifest_hostname}/{filename}.{ext}/Manifest'
# 'Url': '{protocol}://{manifest_hostname}/{filename}.{ext}/manifest({format})'
# 'Url': '{protocol}://{manifest_hostname}/{filename}.{ext}/manifest({format})/{bitrate}'

# Generated at 2022-06-14 15:52:14.598919
# Unit test for constructor of class IsmFD
def test_IsmFD():
    #print("Test class IsmFD")
    #print("Finish test class IsmFD")
    print("Testing IsmFD class")
    print("Finish")

if __name__ == "__main__":
    test_IsmFD()

# Generated at 2022-06-14 15:52:26.327138
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor.ism import IsmFD
    from .common import parse_ism_formats
    url = 'http://amssamples.streaming.mediaservices.windows.net/69fbaeb4-b5f6-4b1a-b5ef-bd74db6a2e4a/BigBuckBunny.ism/manifest(format=mpd-time-csf)'

# Generated at 2022-06-14 15:52:34.373260
# Unit test for constructor of class IsmFD
def test_IsmFD():
    tempdir = os.getenv('TEMPDIR')
    if not tempdir:
        tempdir = tempfile.gettempdir()
    outfile = os.path.join(tempdir, 'test.ism')
    ydl = YoutubeDL({'outtmpl': outfile, 'fragment_retries': 0, 'quiet': True, 'skip_unavailable_fragments': False, 'retries': 0})

# Generated at 2022-06-14 15:52:45.378481
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
  # Context
  # Gets the directory name where the script is located
  dirname = os.path.dirname(__file__)
  # Gets the file name 
  filename = inspect.getframeinfo(inspect.currentframe()).filename
  # Gets the full path of the file
  filepath = os.path.abspath(os.path.join(dirname, filename)) 
  # Reads the url of the video
  url = input("Enter the url of the video: ")
  # Create an IsmFD instance with the url and the file name
  ismFD = IsmFD({'url': url}, 'ism_fragment_downloader.py')
  # Calls the real_download method with the full path of the file and the info_dict of the video

# Generated at 2022-06-14 15:52:57.547834
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:53:00.648484
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    res = IsmFD_real_download()
    if res == True:
        print("test_IsmFD_real_download() successful")
    else:
        print("test_IsmFD_real_download() not successful")


# Generated at 2022-06-14 15:53:39.903759
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """ test_IsmFD """
    ydl = YoutubeDL()
    ydl.add_info_extractor(IsmIE(ydl))
    fd = IsmFD(ydl)

# Generated at 2022-06-14 15:53:47.332973
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    """
    Unit test for method real_download of class IsmFD
    
    test cases:
    1. Fragment size is larger than one chunk
    2. Fragment size is smaller than one chunk
    """
    default_params = {
        'skip_unavailable_fragments': True,
        'fragment_retries': 0,
        'test': False,
    }
    dl = IsmFD(None, default_params)
    filename = "test.ism"
    fragments = [{'url': 'url'}]

# Generated at 2022-06-14 15:53:58.545310
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 72000000000,
        'timescale': 40000000,
        'language': 'eng',
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 44100,
    }
    stream = io.BytesIO()
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:54:08.554784
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Create temporary test folder
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test file name
        test_fname = os.path.join(temp_dir, "test.ism")

        # Generate test parameters
        params = {
            'filepath': test_fname,
            'recode_video': 'mp2',
            'keep_fragments': True,
        }

        # Create DummyIsmFD instance
        ism_fd = DummyIsmFD(params)

        # Call method real_download
        assert ism_fd.real_download(test_fname, {'fragments': [
            {'url': 'https://example.com/file1.ism/QualityLevels(12000)/Fragments(video=0)'},
        ]}) == True



# Generated at 2022-06-14 15:54:18.577279
# Unit test for function write_piff_header
def test_write_piff_header():
    from .hls_downloader import HLSDownloader
    test_params = {
    'track_id': 1,
    'fourcc': 'H264',
    'duration': 30000,
    'timescale': 90000,
    'language': 'und',
    'height': 480,
    'width': 640,
    'sampling_rate': 48000,
    'bits_per_sample': 16,
    'nal_unit_length_field': 4,
    'codec_private_data': '000000016764001facd9c40a981f601000428ee008a0a11a5820e0022efff21001f95b'
}

# Generated at 2022-06-14 15:54:24.089997
# Unit test for constructor of class IsmFD
def test_IsmFD():
    url_fmt = 'http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest'
    info_dict = {'fragments': [{'url': url_fmt, 'duration': 10}, {'url': url_fmt, 'duration': 20}]}
    video_id = 'SuperSpeedway_720'

# Generated at 2022-06-14 15:54:25.015321
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass

# Generated at 2022-06-14 15:54:36.319076
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        "track_id": 0x01,
        "fourcc": "H264",
        "duration": 0x22222222,
        "timescale": 0x10000,
        "language": "und",
        "height": 1200,
        "width": 1800,
        "codec_private_data": '0000000167640033AC9D40DEC2914B0C824F8080000030001E67640033AC9D40DEC2914B0C824F8',
    }
    f = io.BytesIO()
    write_piff_header(f, params)
    print(f.getvalue())

#test_write_piff_header()



# Generated at 2022-06-14 15:54:36.949999
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():

    return



# Generated at 2022-06-14 15:54:46.590821
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Passing test
    filename = 'filename'
    info_dict = {
        'fragments': [
            {'url': 'http://hostname/segment1/Frag1'},
            {'url': 'http://hostname/segment2/Frag2'}
        ],
        '_download_params' : {
            'fourcc': 'AACL',
            'sampling_rate': 48000,
            'duration': 10000,
            'track_id': 1,
            'timescale': 10000000
        }
    }
    params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True
    }

    # mock object for class IsmFD

# Generated at 2022-06-14 15:55:52.901006
# Unit test for constructor of class IsmFD
def test_IsmFD():
    info_dict = {
        'fragments': [
            {'url': "http://www.video.com/segment1.ts"},
            {'url': "http://www.video.com/segment2.ts"},
            {'url': "http://www.video.com/segment3.ts"},
            {'url': "http://www.video.com/segment4.ts"},
            {'url': "http://www.video.com/segment5.ts"},
        ]
    }
    test_fd = IsmFD(info_dict)
    assert type(test_fd) == IsmFD

# Generated at 2022-06-14 15:56:01.846184
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 13491609,
        'timescale': 10000000,
        'language': 'und',
        'height': 720,
        'width': 1280,
        'nal_unit_length_field': 4,
        'codec_private_data': '01640028ffebf079e5b5f5c39d8735d20f507433002b7d036ecb09df2ac3d3b3f1b05f000c8000d47401f67a3da3b3d3c3f01a4079fd8b0'
    }
    write_piff_header(stream, params)
    stream.seek(0)
   

# Generated at 2022-06-14 15:56:03.432070
# Unit test for constructor of class IsmFD
def test_IsmFD():
    stream = get_test_stream('ism')
    fd = IsmFD(stream['url'])
    return fd.test()



# Generated at 2022-06-14 15:56:06.203128
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Test for method real_download (2)
    # This function is defined in youtube_dl/downloader/ism.py
    pass



# Generated at 2022-06-14 15:56:16.641058
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import gen_extractors
    ie = gen_extractors(u'http://example.com/manifest.ism', None)[0]
    fd = ie.get_FD(False)
    assert_true(isinstance(fd, IsmFD))
    assert_false(fd._initialize_frag_download())
    assert_true(fd._finish_frag_download({'total_frags': -1, 'fd': None, 'dont_close': False, 'frag_index': -1}))

# Generated at 2022-06-14 15:56:20.007566
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():

    if cProfile:
        cProfile.run('test_IsmFD_real_download2()')
    else:
        test_IsmFD_real_download2()


# Generated at 2022-06-14 15:56:28.467211
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from youtube_dl.extractor.ism import IsmFD
    from youtube_dl.FileDownloader import FileDownloader
    ydl = FileDownloader()

# Generated at 2022-06-14 15:56:33.396626
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.open('temp.ismv', 'wb') as f:
        params = dict(fourcc='H264', track_id=1, duration=1000,
                      codec_private_data='000000016764001f976c14d40001fac2c0032ac2c0032ac2c008000fa0033000100000168ebecb22c')
        write_piff_header(f, params)

# Generated at 2022-06-14 15:56:42.163353
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    write_piff_header(stream, {'track_id': 1, 'fourcc': b'H264', 'duration': 10, 'timescale': 10,
        'samples_per_second': 5, 'bits_per_sample': 16, 'channels': 2, 'width': 1280, 'height': 720,
        'language': 'eng', 'codec_private_data': '0164001ffe1001867640028acd9d80102032f48c03880801f0000030001b8cb68e0afebb9000400003d38080'})
    assert stream.tell() == 1444

# Generated at 2022-06-14 15:56:50.698999
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    """
    Create an IsmFD object, download a playlist and then download the first two fragments.
    """
    from .ytdl_HLSFD import HlsFD
    from .downloader import FileDownloader
    from .common import SameFileError
    from ..player import F4mFD
    from .common import (
        FileDownloader,
        SameFileError,
    )
    from .ytdl_HLSFD import HlsFD
    from .downloader import (
        FileDownloader,
    )
    from .player import F4mFD
    from .extractor import (
        gen_extractors,
    )

    # For testing purposes
    # fd = F4mFD(params=None)
    # fd = HlsFD(params=None)