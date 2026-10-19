

# Generated at 2022-06-14 15:48:31.796673
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 10000,
        'language': 'und',
        'timescale': 10000000,
        'height': 720,
        'width': 1280,
        'codec_private_data': '01640033ac56f3064f302c8018000000ffff00002c80000fa400000568ce943a0000000168ee3c80'
    }
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:48:37.563434
# Unit test for constructor of class IsmFD
def test_IsmFD():
    params = {'url': 'http://manifest.us.llnwd.net/media/fa/manifest/hls-world-live-000.ism/manifest(format=m3u8-aapl).m3u8'}
    fd = IsmFD(params, None)
    assert fd is not None

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:48:49.484663
# Unit test for function write_piff_header
def test_write_piff_header():
    res = io.BytesIO()
    test_params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 3000000,
        'timescale': 10000000,
        'language': 'und',
        'channels': 1,
        'bits_per_sample': 16,
        'sampling_rate': 44100,
        'nal_unit_length_field': 4,
        'codec_private_data': '0000000167428029BFC09D746C0032F89907FFF91000568CBA'
    }
    write_piff_header(res, test_params)

# Generated at 2022-06-14 15:48:59.161628
# Unit test for function write_piff_header
def test_write_piff_header():
    piff_header = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 30,
        'timescale': 10000000,
        'sampling_rate': 44100,
        'nal_unit_length_field': 4,
        'codec_private_data': '0164001fffe1001767640029acd93e808800000030080000003008da0044a000f8884000fa0fac1a69402f002d2daafe2a003b9c1be01057c50f2f0101000568ebecb22c',
    }
    write_piff_header(piff_header, params)

# Generated at 2022-06-14 15:49:11.826125
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        write_piff_header(stream, {
            'track_id': 1,
            'fourcc': 'AVC1',
            'duration': 20000000,
            'timescale': 10000000,
            'language': 'und',
            'height': 1080,
            'width': 1920,
            'codec_private_data': '0000000167640028acd92811801f1fa401000468efbc40028th1511c0',
        })
        stream = stream.getvalue()

# Generated at 2022-06-14 15:49:17.767616
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import pytest
    with pytest.raises(AttributeError):
        ctx = {}
        segments = ctx['fragments']
        test_IsmFD = IsmFD({'test': False, 'skip_unavailable_fragments': True,'fragment_retries': 0}, {'continue': False, 'quiet': True, 'no_warnings': False})



# Generated at 2022-06-14 15:49:18.479188
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass

# Generated at 2022-06-14 15:49:29.870526
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .YoutubeDL import YoutubeDL
    from .extractor.common import InfoExtractor
    from .compat import urlparse, compat_urllib_error
    from .Downloader import FakeDownloader
    from .utils import encodeFilename
    from .utils import parse_codecs
    from .extractor.common import ExtractorError
    from .utils import sanitize_filename
    from .utils import read_batch_urls
    from .extractor.smoothstreams import (
        SmoothStreamsIE,
        SmoothStreamsPidIE,
        SmoothStreamsM3U8IE,
    )
    from .utils import find_xpath_attr
    from .utils import remove_end
    from .compat import compat_str
    from .utils import remove_end
    from .utils import compat_urllib_request


# Generated at 2022-06-14 15:49:41.090863
# Unit test for function extract_box_data
def test_extract_box_data():
    #   ftyp
    #   moov
    #     mvhd
    #     trak
    #       tkhd
    #       mdia
    #         mdhd
    #         hdlr
    #         minf
    #           vmhd
    #           dinf
    #             dref
    #           stbl
    #             stsd
    #               avc1
    #                 avcC
    #             stts
    #             stsc
    #             stco
    ftyp_payload = b'isml'  # major brand
    ftyp_payload += u32.pack(1)  # minor version
    ftyp_payload += b'piff' + b'iso2'  # compatible brands
    ftyp_box = box(b'ftyp', ftyp_payload)
   

# Generated at 2022-06-14 15:49:44.224898
# Unit test for function write_piff_header
def test_write_piff_header():
    import json
    import os
    import tempfile
    from .piff_test import piff_open_for_writing

    with tempfile.NamedTemporaryFile('w+b', suffix='.ismv') as stream:
        params = json.load(open(os.path.join(os.path.dirname(__file__), 'piff_test', 'params.json')))
        write_piff_header(stream, params)
        stream.seek(0)
        with piff_open_for_writing(stream, params) as stream_writer:
            stream_writer.write(b'foo')



# Generated at 2022-06-14 15:49:56.577938
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # constructor test
    IsmFD('http://example.com/ism/.ismc', {})



# Generated at 2022-06-14 15:50:02.784797
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    """Test for method real_download of class IsmFD"""

    # assert statements
    # all arguments of method 'real_download' of class IsmFD
    filename = None
    info_dict = None
    # make sure to use attributes for all other arguments
    # of method 'real_download' of class IsmFD
    # call method from class IsmFD
    obj = IsmFD()
    obj.real_download(filename, info_dict)

# Generated at 2022-06-14 15:50:09.975922
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .YoutubeDL import YoutubeDL
    from .downloader import RtmpFD
    from .extractor import (
        YoutubeIE,
        SoundcloudIE,
        MetacafeIE,
    )

    def _get_filename(id):
        return '%s.ismv' % id

    def _download_file(id):
        ie = YoutubeIE(YoutubeDL({'noplaylist': True}))
        ie.extract('https://youtu.be/%s' % id)

    def _get_file(id):
        return open(os.path.join(os.path.dirname(__file__), _get_filename(id)), 'rb').read()

    def _test_id(id):
        ie = YoutubeIE(YoutubeDL({'noplaylist': True}))

# Generated at 2022-06-14 15:50:18.058884
# Unit test for function extract_box_data
def test_extract_box_data():
    data_reader = io.BytesIO(
        b'\x00\x00\x00\x20ftyp'
        b'\x00\x00\x01\x00'
        b'\x00\x00\x00\x1Cmoov'
        b'\x00\x00\x00\x14mvhd'
        b'\x00\x00\x00\x28trak'
        b'\x00\x00\x00\x10tkhd'
        b'\x00\x00\x00\x08mdia'
        b'\x00\x00\x00\x14mdhd'
        b'\x00\x00\x00\x10minf')

# Generated at 2022-06-14 15:50:28.575569
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:50:40.416028
# Unit test for function write_piff_header
def test_write_piff_header():
    from collections import OrderedDict
    from ..utils import (
        KeyValueObject,
        int_or_none,
    )
    from ..compat import (
        compat_etree_fromstring,
    )

    codec_private_data = ('0000000167428029883a98c0b0040015fac002800f2c90448b440e8880080000'
                          '01000468ced608000001b0e8c4740001000001b56900a0a00010000000168e9'
                          'e89e01800480048d8452ae803000001b2740014eeb6080')

    def assert_piff_header(stream, moov_element):
        from .ism import ism_as_m3u8_playlist, ism_as_dash

# Generated at 2022-06-14 15:50:53.082239
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Setup input stream
    input_stream = io.BytesIO(b'\x00\x00\x00\x24ftypisml\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00piffiso2')
    # Setup context
    ctx = {
        'filename': 'filename',
        'total_frags': len(('fragments')),
    }
    # Setup params

# Generated at 2022-06-14 15:51:03.647998
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import gen_extractors
    extractors = gen_extractors()

# Generated at 2022-06-14 15:51:05.304339
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import gen_extractors
    _, ie = gen_extractors(u'http://www.example.com/test/video.ism')[0]
    assert isinstance(ie, IsmFD)

# Generated at 2022-06-14 15:51:14.083485
# Unit test for function write_piff_header
def test_write_piff_header():
    it = io.BytesIO()
    hd = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 300000000,
        'sampling_rate': 48000,
        'channels': 2,
        'codec_private_data': '000000016764001facd942c01fc5a03e00000030010000003001c4d401e3c039f95c0'
    }
    write_piff_header(it, hd)
    assert len(it.getvalue()) == 969
    assert u32.unpack(it.getvalue()[:4])[0] == 965
    assert it.getvalue()[4:8] == b'moov'



# Generated at 2022-06-14 15:51:35.172009
# Unit test for constructor of class IsmFD
def test_IsmFD():
    downloader = IsmFD(params={}, ydl=None)

# Generated at 2022-06-14 15:51:45.983851
# Unit test for function write_piff_header
def test_write_piff_header():
    from .ptypes import read_piff_fragment_header
    import base64
    import zlib
    params = {'track_id': 1, 'fourcc': 'AVC1',
        'duration': 120000000, 'timescale': 10000000,
        'language': 'eng', 'height': 720, 'width': 1280,
        'codec_private_data': '0164001fffe100176764001fddf800010401e00302c80000fa40018301800603014002079f1400a8fff81001000100000030080000fa400183018006030000001c8afc0610a040120008081001000102803f001000100000083f8610002040000802080'}

# Generated at 2022-06-14 15:51:54.351307
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:51:55.797500
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # test IsmFD constructor
    fd = IsmFD()



# Generated at 2022-06-14 15:52:02.591562
# Unit test for function write_piff_header
def test_write_piff_header():
    from io import BytesIO
    bs = BytesIO()
    params = dict(track_id=1, fourcc='H264', duration=10, width = 1920, height = 1080, sampling_rate = 44100, channels=2, bits_per_sample=16, codec_private_data='0000000167640028AC2280058CE601E0')
    write_piff_header(bs, params)

# Generated at 2022-06-14 15:52:14.458516
# Unit test for method real_download of class IsmFD

# Generated at 2022-06-14 15:52:26.328937
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:52:27.878041
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .ism import IsmFD
    ismfd = IsmFD()
    assert (ismfd.FD_NAME == 'ism')


# Generated at 2022-06-14 15:52:35.119380
# Unit test for constructor of class IsmFD
def test_IsmFD():
    class MyIsmFD(IsmFD):
        def _download_fragment(self, ctx, url, info_dict):
            return True, b'TEST'

    myfd = MyIsmFD('http://example.com/test.ismv')

# Generated at 2022-06-14 15:52:46.152957
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .extractor.common import InfoExtractor
    from .compat import parse_qsl, compat_urllib_request, compat_urlparse, compat_urllib_error
    from .utils import (
        encode_dict,
        decode_packed_codes,
        ExtractorError,
    )
    from .downloader import (
        _parse_m3u8_attributes,
    )

    # TODO Remove this entire method in Python 3

    import sys
    if sys.version_info >= (3, 0):
        return

    # Generate an instance of IsmFD to test
    IsmFDobj = IsmFD()

    # Generate an instance of InfoExtractor to test
    InfoExtractorobj = InfoExtractor()

    # Constructor test

# Generated at 2022-06-14 15:53:59.069126
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        write_piff_header(stream, {
            'track_id': 1,
            'fourcc': 'AACL',
            'duration': 1000000,
            'sampling_rate': 44100,
            'channels': 2,
        })

# Generated at 2022-06-14 15:54:08.022009
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = dict()
    params['track_id'] = 1
    params['fourcc'] = 'H264'
    params['duration'] = 10000000
    params['timescale'] = 10000000
    params['language'] = 'und'
    params['height'] = 480
    params['width'] = 854
    params['codec_private_data'] = '6764001f2a9ee02e000c0d93e6912a25f687600000000168e0c2c60'

    write_piff_header(stream, params)
    data = stream.getvalue()
    print(data)
    assert len(data) > 0


# Generated at 2022-06-14 15:54:18.314636
# Unit test for function extract_box_data
def test_extract_box_data():
    data = b"\x00\x00\x00\x30mdia\x00\x00\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

# Generated at 2022-06-14 15:54:23.884079
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fragment_filename = 'test_ism.ism'

# Generated at 2022-06-14 15:54:36.749422
# Unit test for function write_piff_header
def test_write_piff_header():
    data = io.BytesIO()
    write_piff_header(data, {
        'track_id': 1,
        'duration': 20000000,
        'sampling_rate': 96000,
        'bits_per_sample': 16,
        'channels': 2,
        'fourcc': 'AACL',
        'language': 'en',
    })

# Generated at 2022-06-14 15:54:39.797266
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Test with a sample URL
    IsmFD('http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest')


# Generated at 2022-06-14 15:54:41.537189
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # test_method.py::test_IsmFD_real_download
    pass


# Generated at 2022-06-14 15:54:43.263136
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    fd = IsmFD()
    fd.real_download('filename', 'info_dict')

# Generated at 2022-06-14 15:54:51.017250
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .downloader import FileDownloader
    from .common import FileDownloaderParams
    from .extractor import gen_extractors
    from .dashmanifest import get_video_info
    import io
    class Mock_gen_extractors(object):
        """
        Mock object to gen_extractors method
        """
        def __init__(self):
            self.youtube_dl = None

        def __call__(self, ie_key, url):
            class Mock_gen_extractors(object):
                """
                Mock object to youtube_dl.extractor.gen_extractors method
                """
                def __init__(self):
                    self.youtube_dl = None


# Generated at 2022-06-14 15:55:01.889828
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    def _real_extract(_, url):
        match = re.search(
            r'<Protection>\s*<ProtectionHeader(?: [^>]*)?>(?P<pssh>[0-9a-fA-F]*)',
            compat_urllib_request.urlopen(url).read().decode('utf-8'))
        pssh_base64 = match.group('pssh')

# Generated at 2022-06-14 15:57:44.659217
# Unit test for function write_piff_header
def test_write_piff_header():
    import gzip
    from io import BytesIO
    stream = BytesIO()

# Generated at 2022-06-14 15:57:52.882941
# Unit test for function write_piff_header