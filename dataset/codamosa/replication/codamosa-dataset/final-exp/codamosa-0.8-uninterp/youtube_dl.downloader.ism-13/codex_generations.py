

# Generated at 2022-06-14 15:48:14.885595
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD(params={}, params_url='test_params_url')
    assert fd.params_url == 'test_params_url'



# Generated at 2022-06-14 15:48:15.604821
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    assert True

# Generated at 2022-06-14 15:48:21.646417
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Case 1: normal
    print('Normal case -- ')
    _url = 'http://test.ism'
    _params = {}
    _fd = IsmFD(_url, _params)
    assert isinstance(_fd, IsmFD)
    assert _fd.url == _url
    assert _fd.params == _params


# Generated at 2022-06-14 15:48:31.659941
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .manifest import DASHManifest
    ismFD = IsmFD()

    manifest = DASHManifest.parse("https://dash-mse-test.commondatastorage.googleapis.com/media/motion-ts/manifest_dash.mpd")
    ismFD._download_params = manifest.get_video_info()
    ismFD._download_params['outtmpl'] = './test-%(playlist_title)s.mp4'
    ismFD._download_params['fragment_retries'] = 10
    ismFD._download_params['skip_unavailable_fragments'] = False
    ismFD.download([],manifest.get_video_info())
    return True

# Generated at 2022-06-14 15:48:43.528033
# Unit test for function write_piff_header
def test_write_piff_header():
    import random

# Generated at 2022-06-14 15:48:53.325706
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    """
    Test method real_download of class IsmFD
    """
    import os
    import tempfile

    from .compat import compat_urllib_request
    
    from .common import load_json, FileDownloader
    from .extractor import get_info_extractor

    # Get the unit test path
    test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test'))
    if len(test_path) == 0:
        test_path = os.path.abspath('test')

    # Test manifest file name
    manifest_filename = 'manifest_short.ism'

    # Set the test manifest file path
    manifest_filepath = os.path.join(test_path, manifest_filename)

    # Create a temporary file
   

# Generated at 2022-06-14 15:48:57.663224
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    print("Testing method real_download of class IsmFD")
    t = IsmFD()
    t.real_download("filename", "info_dict")



# Generated at 2022-06-14 15:49:10.745013
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor.ism import IsmFD
    from .utils import get_cachedir
    from .downloader.external import ExternalFD

    # Constructor of class IsmFD
    sess = compat_urllib_request.build_opener(
        compat_urllib_request.HTTPCookieProcessor()).open
    cache = get_cachedir()
    youtube_dl = YoutubeDL()
    params = {
        'noprogress': True,
        'quiet': True
    }
    external_fd = ExternalFD(sess, cache, youtube_dl, params)
    ism_fd = IsmFD(sess, cache, youtube_dl, params)

    # Attributes of class IsmFD
    assert ism_fd.FD_NAME == 'ism'
    assert ism_fd.continued

# Generated at 2022-06-14 15:49:13.592995
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """
    Test for IsmFD.
    """
    test_exe = IsmFD()
    assert test_exe is not None, 'IsmFD constructor is not working!'



# Generated at 2022-06-14 15:49:20.998769
# Unit test for constructor of class IsmFD
def test_IsmFD():
        params = {
            'format': 'ism',
            'file': 'test.ismv',
            'playpath': 'mp4:test.mp4',
            'app': 'test',
            'rtmp': 'rtmp://example.com:1935/orbs/app/'
        }
        ydl = YoutubeDL(params)
        # ism_fd = IsmFD(ydl)
        # assert ism_fd

_FD_CLASSES = [IsmFD]

# Generated at 2022-06-14 15:49:44.471417
# Unit test for function write_piff_header
def test_write_piff_header():
    from .testutils import TmpDirTestCase


# Generated at 2022-06-14 15:49:51.158782
# Unit test for function extract_box_data
def test_extract_box_data():
    data_reader = io.BytesIO(b'\0\0\0\x11moov\x00\x00\x00\x1fbox1\0\0\0\x0fbox2\0\0\0\x0fbox3')
    assert extract_box_data(data_reader.read(), ['moov', 'box1', 'box2']) == b'box2' + b'\0' * 7



# Generated at 2022-06-14 15:49:57.255828
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    successful_download = IsmFD().real_download('C:/Users/jkczc/Downloads/video.ism', {'url': 'http://jkczc.com/playlist.m3u8?publisher_id=0e0d7d2e-3e3c-4a38-88d0-e1ce3c3086ed'})
    assert successful_download is not None

# Generated at 2022-06-14 15:50:06.647595
# Unit test for function extract_box_data
def test_extract_box_data():
    assert extract_box_data(b'moov\x00\x00\x00\x00', [b'moov']) == b''
    assert extract_box_data(b'moov\x00\x00\x00\x00mvhd\x00\x00\x00\x00', [b'moov', b'mvhd']) == b''
    assert extract_box_data(b'moov\x00\x00\x00\x00mvhd\x00\x00\x00\x00test', [b'moov', b'mvhd']) == b'test'

# Generated at 2022-06-14 15:50:07.774728
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Tested
    pass


# Generated at 2022-06-14 15:50:13.714467
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    url = 'http://amssamples.streaming.mediaservices.windows.net/91492735-c523-432b-ba01-faba6c2206a2/AzureMediaServicesPromo.ism/manifest'
    params = {'url': url}
    fd = IsmFD(params)

    # Test the expected return value of method real_download
    assert fd.real_download(None, None) is False

# Generated at 2022-06-14 15:50:21.436142
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # test basic attributes
    fd = IsmFD({ 'url': 'http://url.com/manifest.ism' })
    assert fd.url == 'http://url.com/manifest.ism'
    assert fd.params == {}
    # test constructor with parameters
    fd = IsmFD({ 'url': 'http://url.com/manifest.ism?params' }, { 'param': 'value' })
    assert fd.url == 'http://url.com/manifest.ism?params'
    assert fd.params == { 'param': 'value' }

# Generated at 2022-06-14 15:50:31.130991
# Unit test for constructor of class IsmFD
def test_IsmFD():
    ret = IsmFD.can_download({"protocol": "ism", "url": "http://www.example.com/some.ism/some.mp4"})
    assert(ret == True)


# Generated at 2022-06-14 15:50:40.827058
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = FragmentFD()
    params = {
        'track_id': 1,
        'fourcc': 'AVC1',
        'duration': 10000,
        'height': 480,
        'width': 640,
        'codec_private_data': '01640022ffe10017674d0012ac01fc1d6081000003000168ee3c8040000030028ee3c8'
    }
    write_piff_header(stream, params)


# Generated at 2022-06-14 15:50:53.391695
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from ydl_test_utils import FakeYDL
    from ydl_test_utils import FakeDownloader
    from ydl_test_utils import change_process_title
    from ydl_test_util_params import test_params_smooth
    import mock

    params = test_params_smooth
    ydl = FakeYDL()
    ydl.params.update(params)

    def noop_hook(d):
        pass

    ydl.add_post_process(noop_hook)
    ydl.add_download_listener(noop_hook)
    ydl.add_info_extractor(IsmIE(ydl))
    ydl.add_progress_hook(noop_hook)


# Generated at 2022-06-14 15:51:10.567865
# Unit test for function write_piff_header
def test_write_piff_header():
    # setup
    params = {'track_id':1, 'fourcc':'AACL', 'duration':10000, 'language':'und', 'sampling_rate':44100}
    iostream = io.BytesIO()
    write_piff_header(iostream, params)
    iostream.seek(0)

    # test
    # TODO



# Generated at 2022-06-14 15:51:16.328435
# Unit test for constructor of class IsmFD
def test_IsmFD():
    manifest_url = 'http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest'
    params = {
        'url': manifest_url,
        'test': True,
    }
    IsmFD(params).download(os.devnull)

# Generated at 2022-06-14 15:51:28.111501
# Unit test for function write_piff_header
def test_write_piff_header():
    f = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AVC1',
        'duration': 8000000000,
        'timescale': 10000000,
        'language': 'eng',
        'height': 320,
        'width': 240,
        'codec_private_data': '01640028ffe1000867640028ac320001000468ee3c80',
        'nal_unit_length_field': 4,
    }
    write_piff_header(f, params)

# Generated at 2022-06-14 15:51:40.512884
# Unit test for function write_piff_header
def test_write_piff_header():
    import ctypes
    import struct

    struct_ptr = ctypes.c_int.from_address(id(struct.Struct) + 3 * ctypes.sizeof(ctypes.c_void_p))
    original_structure_size = struct_ptr.value

    stream = io.BytesIO()

# Generated at 2022-06-14 15:51:45.100479
# Unit test for function extract_box_data
def test_extract_box_data():
    data = b'\x00\x00\x00\x0cftypiso2\x00\x00\x00\x1cmoov\x00\x00\x00\x0ctrak\x00\x00\x00\x08mdia'
    assert extract_box_data(data, (b'moov', b'mdia')) == b'\x00\x00\x00\x08mdia'



# Generated at 2022-06-14 15:51:47.635336
# Unit test for constructor of class IsmFD
def test_IsmFD():
    IsmFD('http://example.com/video.ismv')

# Generated at 2022-06-14 15:51:58.243505
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():

    import sys
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.youtube import YoutubeIE
    from youtube_dl import utils

    downloader = YoutubeDL(dict(forceurl=True,
                                hls_prefer_native=False,
                                hls_prefer_ffmpeg=False,
                                hls_use_mpegts=False,
                                fragment_retries=1,
                                skip_unavailable_fragments=False,
                                format='ismv/1000'))
    test_url = "http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest"
    if hasattr(sys, 'version_info') and sys.version_info >= (3, 0):
        test_

# Generated at 2022-06-14 15:52:03.718752
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Create youtube-dl instance
    ydl = YoutubeDL()
    # Create IsmFD
    fd = IsmFD(ydl, {})

    # Assert
    assert fd.FD_NAME == 'ism'

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:52:15.278953
# Unit test for function write_piff_header
def test_write_piff_header():
    fd = io.BytesIO()
    params = {
        'fourcc': 'AACL',
        'sampling_rate': 44100,
        'track_id': 1,
        'duration': 0,
    }
    write_piff_header(fd, params)
    fd.seek(0)

# Generated at 2022-06-14 15:52:17.166442
# Unit test for constructor of class IsmFD
def test_IsmFD():
    IsmFD('', {})



# Generated at 2022-06-14 15:52:34.773642
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass



# Generated at 2022-06-14 15:52:45.855191
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    parameters = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'track_id': 23,
        'fourcc': 'avc1',
        'duration': 1000000,
        'timescale': 10000000,
        'language': 'und',
        'height': 0,
        'width': 0,
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 48000,
        'codec_private_data': '0164001fffacd9a1b51af97b906500a0dae809be00000000000000000000000168ebe3c80f'
    }
    with open("output.mp4", 'wb') as ctx['dest_stream']:
        write

# Generated at 2022-06-14 15:52:57.930252
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # test1
    try:
        IsmFD('http://link.theplatform.com/s/HNK2IC/hls?mbr=true', {'test': True}, None)
        print(True)
    except Exception as e:
        print(False)
    # test2
    try:
        IsmFD('http://link.theplatform.com/s/HNK2IC/hls?mbr=true', {'test': True}, None)
        print(True)
    except Exception as e:
        print(False)
    # test3
    try:
        IsmFD('http://link.theplatform.com/s/HNK2IC/hls?mbr=true', {'test': True}, None)
        print(True)
    except Exception as e:
        print(False)
   

# Generated at 2022-06-14 15:53:00.307502
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """IsmFD: constructor test"""
    return IsmFD(params={'noprogress':False, 'fragment_retries':0})



# Generated at 2022-06-14 15:53:07.232744
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import os
    import shutil
    import tempfile
    import yaml

    class IsmFD_real_download_FakeParams(object):
        pass

    class IsmFD_real_download_FakeInfoDict(object):
        pass

    class IsmFD_real_download_FakeSegment(object):
        pass

    class IsmFD_real_download_FakeYDL(object):
        def to_screen(self, msg):
            print(msg)
        def to_stderr(self, msg):
            print(msg)

    class IsmFD_real_download_FakeFragmentFD(FragmentFD):
        def set_downloader(self, ydl):
            self.ydl = ydl
        def _prepare_and_start_frag_download(self, ctx):
            ctx

# Generated at 2022-06-14 15:53:14.839520
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Create an IsmFD object
    IsmFD(ydl=None, params=None)
    # Create an IsmFD object
    IsmFD(ydl=None, params={'skip_unavailable_fragments': True})
    # Create an IsmFD object
    IsmFD(ydl=None, params={'test': False})
    # Create an IsmFD object
    IsmFD(ydl=None, params={'fragment_retries': 0})



# Generated at 2022-06-14 15:53:15.763912
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    return True

# Generated at 2022-06-14 15:53:21.840199
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """
    Test opening FD for an ISM manifest.
    """
    from .extractor.common import InfoExtractor
    from .downloader.ism import IsmFD
    from .downloader.http import HttpFD
    import os.path

    # Use the same test file
    filename = 'test'
    url = 'test'
    ie = InfoExtractor()
    ie.params.update({
        'noplaylist': True,
        'usenetrc': False,
    })
    ie.add_info_extractor('https?://(?:www\.)?(?:sample|foobar).com',
                          'test_suite/extractor/test_smoothstreaming')
    info_dict = ie._real_extract(url)

    # Test test_suite/extractor/test_ism.py

# Generated at 2022-06-14 15:53:27.965684
# Unit test for function write_piff_header
def test_write_piff_header():
    import random
    import time
    import re

    def generate_random_bytes(b):
        return ''.join([chr(random.randint(0, 255)) for _ in range(b)])

    def write_piff_header_test_case(is_audio, sampling_rate=44100, channels=2, bits_per_sample=16,
                                    width=0, height=0,
                                    codec_private_data='', timescale=10000000, track_id=1,
                                    duration=10000000, language='und'):
        stream = io.BytesIO()

# Generated at 2022-06-14 15:53:38.533003
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import youtube_dl
    from .extractor.common import InfoExtractor
    from .extractor import gen_extractors_classes
    gen_extractors_classes(InfoExtractor)

    return IsmFD(youtube_dl, {'extractor': youtube_dl})

if __name__ == '__main__':
    ism = test_IsmFD()
    ism.real_download('/tmp/test.mp4', {'id': 104, 'fragments': [{'url': 'https://s3.amazonaws.com/id-media-us-east-1/I04/s4s_beacon_web/bm11.ism/bm11-frag2'}], '_download_params': {'fourcc': 'H264'}})

# Generated at 2022-06-14 15:54:17.027783
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    audio_params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 1234,
        'timescale': 44100,
        'language': 'eng',
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 44100,
    }

# Generated at 2022-06-14 15:54:25.029303
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 30000,
        'timescale': 90000,
        'height': 720,
        'width': 1280,
        'language': 'und',
        'codec_private_data': '0164001fffe100176764001facd940800100000030080000003008000003341241b408dfb02e24a878d5322f0a04f30a0',
        'nal_unit_length_field': 4,
    }
    write_piff_header(stream, params)
    return stream.getvalue()


# Generated at 2022-06-14 15:54:27.448507
# Unit test for constructor of class IsmFD
def test_IsmFD():
    testIsmFD=IsmFD()
    print('Create a IsmFD successfully.\n')


# Generated at 2022-06-14 15:54:39.350518
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    '''
        Tests IsmFD.real_download()
        Note: IsmFD requires SSL certificate that is not included in the test 
    '''
    test_utils = TestUtils()
    test_utils.add_mapping('http://testserver.com/', 'https://dummy_test_url.com/')

    download_params = {'format_id': '1'}
    download_params['sampling_rate'] = 22050
    download_params['channels'] = 2
    download_params['bits_per_sample'] = 16
    download_params['fourcc'] = 'AACL'
    download_params['track_id'] = 1
    download_params['duration'] = 10
    download_params['timescale'] = 10000000

# Generated at 2022-06-14 15:54:40.737010
# Unit test for constructor of class IsmFD
def test_IsmFD():
    '''
    Constructor of IsmFD
    '''
    IsmFD({})

# Generated at 2022-06-14 15:54:49.420094
# Unit test for constructor of class IsmFD
def test_IsmFD():
    manifest_url = 'http://playready.directtaps.net/pr/svc/rightsmanager.asmx'

# Generated at 2022-06-14 15:55:00.116395
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()

# Generated at 2022-06-14 15:55:12.303096
# Unit test for constructor of class IsmFD
def test_IsmFD():
    if '2' in sys.version:
        return

    progress = progress_streams.DummyProgress()

    params = {
        'username': 'abc',
        'password': 'abc',
        'hds_live_edge': 12,
        'hds_fragment_retries': 3,
        'hds_flags': 'live',
        'test': True
    }

    def _test_frag_downloader(fd):
        fd.report_destination(sys.stdout)
        fd.download(progress.update)


# Generated at 2022-06-14 15:55:20.569323
# Unit test for method real_download of class IsmFD

# Generated at 2022-06-14 15:55:33.333525
# Unit test for constructor of class IsmFD
def test_IsmFD():
    pass



# Generated at 2022-06-14 15:57:22.467462
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import configargparse
    args = ['-u', 'plugin://plugin.video.microsoft.iss/play/video/{3A5D5C07-28C6-4D6F-8D8C-F1C9EAFFD58C}?path=/api/Manifest/hls/GB/Production/1/v4',
            '--skip-download']
    parser = configargparse.ArgumentParser(args)
    params = parser.add_argument_group('ism options')
    params.add('--fragment-retries', default=0, type=int, help='number of retries for each fragment')
    params.add('--skip-unavailable-fragments', default=True, action='store_true', help='skip unavailable fragments')

# Generated at 2022-06-14 15:57:27.039968
# Unit test for method real_download of class IsmFD

# Generated at 2022-06-14 15:57:33.538745
# Unit test for function write_piff_header
def test_write_piff_header():
    from .test.media import get_test_data_file

    audio_params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'codec_private_data': '1200',
        'sampling_rate': 1,
        'channels': 2,
        'duration': 10,
    }

    video_params = {
        'track_id': 2,
        'fourcc': 'AVC1',
        'codec_private_data': '674280d15d9001e17e4280d15d9001e1007b901000468ee2c80',
        'width': 1,
        'height': 2,
        'duration': 20,
    }

    fd = io.open(get_test_data_file('audio'), 'rb')
    write_

# Generated at 2022-06-14 15:57:39.783055
# Unit test for function write_piff_header
def test_write_piff_header():
    fh = io.BytesIO()
    write_piff_header(fh, {'track_id': 1, 'fourcc': 'H264', 'duration': 1000, 'timescale': 10000000, 'width': 0, 'height': 0})

# Generated at 2022-06-14 15:57:45.504721
# Unit test for constructor of class IsmFD
def test_IsmFD():
    vd = IsmFD({
        'url': 'http://www-itec.uni-klu.ac.at/ftp/datasets/mmsys12/RedBullPlayStreets/redbull_4s/Manifest.ism/Manifest',
        'skip_unavailable_fragments': True
    })
    vd.download('test_video')

if __name__ == '__main__':
    test_IsmFD()