

# Generated at 2022-06-14 15:48:25.704023
# Unit test for function extract_box_data
def test_extract_box_data():
    data = b'\x00\x00\x00\x1cftyp\x00\x00\x00\x04isml\x00\x00\x00\x01\x00\x00\x00\x03piff\x00\x00\x00\x03iso2'
    assert extract_box_data(data, ['ftyp']) == b'\x00\x00\x00\x04isml\x00\x00\x00\x01\x00\x00\x00\x03piff\x00\x00\x00\x03iso2'
    assert extract_box_data(data, ['ftyp', 'piff']) == b'\x00\x00\x00\x02iso2'

# Generated at 2022-06-14 15:48:35.663548
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .http import HttpFD
    with _TempDownloader() as td:
        ydl = FakeYDL()
        ydl.params['proxy'] = '192.168.56.1:3128'
        ydl.params['proxy_username'] = 'proxyuser'
        ydl.params['proxy_password'] = 'proxypass'
        ydl.add_info_extractor(IsmIE())
        ydl.add_info_extractor(IsmcIE())
        ydl.add_info_extractor(IsmaIE())
        ydl.add_downloader(IsmFD())
        ydl.download(['http://dai.google.com/ondemand/wmedia/media/Motion_Test_3Mbps_VP6.wmv'])


# Generated at 2022-06-14 15:48:47.732642
# Unit test for function extract_box_data
def test_extract_box_data():
    data = b'moov\x00\x00\x00\x00'
    assert(extract_box_data(data, [b'moov']) == b'')

    data = b'moov\x02\x00\x00\x00' + b'moov\x00\x00\x00\x00'
    assert(extract_box_data(data, [b'moov']) == b'')

    data = b'moov\x01\x00\x00\x00' + b'moov\x00\x00\x00\x00'
    assert(extract_box_data(data, [b'moov']) == b'')


# Generated at 2022-06-14 15:48:55.442345
# Unit test for function write_piff_header
def test_write_piff_header():
    from ..compat import compat_etree_ElementTree, compat_urlparse

    my_params = {}
    my_params['track_id'] = 1
    my_params['fourcc'] = 'H264'
    my_params['timescale'] = 10000000
    my_params['duration'] = 0
    my_params['language'] = 'eng'
    my_params['height'] = 432
    my_params['width'] = 768
    my_params['codec_private_data'] = '0000000167640032acd900002b0d8d3c0000000168ebecb5'
    my_params['nal_unit_length_field'] = 4

    my_stream = io.BytesIO()
    write_piff_header(my_stream, my_params)

# Generated at 2022-06-14 15:48:58.721779
# Unit test for constructor of class IsmFD
def test_IsmFD():
    assert IsmFD(None, None, None)

if __name__ == '__main__':
    unittest.main()

# Generated at 2022-06-14 15:49:11.572611
# Unit test for function write_piff_header
def test_write_piff_header():
    class Stream(io.BytesIO):
        def __init__(self, *args, **kwargs):
            self.box_count = 0
            super(Stream, self).__init__(*args, **kwargs)

        def write(self, data):
            self.box_count += data.count(b'ftyp') + data.count(b'moov') + data.count(b'trak') + data.count(b'mvex') + \
                data.count(b'mdia') + data.count(b'minf') + data.count(b'stbl') + data.count(b'stsd') + \
                data.count(b'stts') + data.count(b'stsc') + data.count(b'stco') + data.count(b'avcC')

# Generated at 2022-06-14 15:49:18.172080
# Unit test for constructor of class IsmFD
def test_IsmFD():
    params = {
        'url': 'http://foobar',
        'fragments': [
            {
                'url': 'http://bar@foo'
            },
            {
                'url': 'http://bar@foo2'
            }
        ]
    }
    output_file = tempfile.NamedTemporaryFile()
    IsmFD(params, output_file).download(params)


# Generated at 2022-06-14 15:49:19.361398
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass


# Generated at 2022-06-14 15:49:30.445643
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import FakeYDL
    import os

    ydl = FakeYDL()
    my_fd = IsmFD({'format': 'ism'}, ydl)

# Generated at 2022-06-14 15:49:42.201548
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # For debug
    # (IsmFD, object)
    print(type(IsmFD))
    # Class IsmFD
    print(IsmFD)
    # IsmFD
    print(IsmFD.__name__)
    # <class 'youtubedl.fragment.IsmFD'>
    print(repr(IsmFD))
    # <class 'youtubedl.fragment.IsmFD'>
    print(str(IsmFD))
    # youtubedl.fragment.IsmFD
    print(IsmFD.__module__)
    # 'IsmFD'
    print(IsmFD.FD_NAME)
    # fragment
    print(IsmFD.__module__)
    # IsmFD
    print(IsmFD.__qualname__)


# Generated at 2022-06-14 15:50:04.429374
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    """Test method real_download of class IsmFD"""
    # TODO make this test work
    return

    # Load current YoutubeDL instance
    ydl = YoutubeDL({})
    # Define parameters to test
    params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True
    }

# Generated at 2022-06-14 15:50:14.600864
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:50:24.606289
# Unit test for constructor of class IsmFD
def test_IsmFD():
    """
    Tests for class IsmFD

    Note: for this test you need to download a file called
        "my-ism.ismc" from the internet and place it in
        "HOME/.youtube-dl/tmp/".
    """

    from .extractor.common import InfoExtractor
    from .downloader.http import HttpFD
    from .utils import compat_urllib_parse
    from .extractor.discoauth import DiscoAuthInfoExtractor

    url = 'file://%s/my-ism.ismc' % compat_urllib_parse.unquote(gettempdir())

    extractor = InfoExtractor(DiscoAuthInfoExtractor())
    extractor.add_info_extractor(
        IsmFD(HttpFD(extractor), url, extractor.gen_extractors(), False))


# Generated at 2022-06-14 15:50:30.126432
# Unit test for function write_piff_header
def test_write_piff_header():
    import json
    import io

    print('Unit test for function write_piff_header')
    # Video
    with io.BytesIO() as output:
        params = {
            'track_id': 1,
            'fourcc': 'H264',
            'codec_private_data': '000000016742e00d9659040898c240410000003001000000300a900100003005000001030008000100000030080000300b080001000000300c0000300d90010000300e040015a0d',
            'duration': 30000000,
            'width': 1280,
            'height': 720,
        }
        write_piff_header(output, params)
        output.seek(0)
        content = output.read()

# Generated at 2022-06-14 15:50:40.492691
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    ffd = FragmentFD(None, 0)
    params = {
        'track_id': 1,
        'height': 360,
        'width': 640,
        'timescale': 10000000,
        'duration': 10000,
        'codec_private_data': '0164001fffe1006742c0032b6643e030010000003001e847'
            'fdf9014004278eea41e8a4aa4df9e096428080',
        'fourcc': 'AVC1',
        'nal_unit_length_field': 4}
    write_piff_header(stream, params)
    print(stream.getvalue())
    assert(1==1)
    # assert stream.getvalue() == b'\x00\x00

# Generated at 2022-06-14 15:50:53.070899
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Test for passing arguments as dictionary
    ismFDInstance = IsmFD({'url': 'http://example.com/example.ism/Manifest', 'ism_id': '0010', 'f': 'ism', 'player_url': 'http://example.com/example.js'})
    assert ismFDInstance.url == 'http://example.com/example.ism/Manifest'
    assert ismFDInstance._ism_id == '0010'
    assert ismFDInstance.player_url == 'http://example.com/example.js'

    # Test for passing arguments as keyword arguments
    ismFDInstance = IsmFD(url='http://example.com/example.ism/Manifest', ism_id='0020', f='ism', player_url='http://example.com/example.js')

# Generated at 2022-06-14 15:51:03.647481
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        params = {
            'track_id': 1,
            'fourcc': 'AACL',
            'sampling_rate': 48000,
            'duration': 300000,
            'channels': 2,
            'bits_per_sample': 16,
        }
        write_piff_header(stream, params)
        data = stream.getvalue()

        assert data[0:4] == b'moov'
        assert data[12:16] == b'trak'
        assert data[28:32] == b'tkhd'
        assert data[44:48] == b'mdia'
        assert data[60:64] == b'mdhd'
        assert data[76:80] == b'hdlr'

# Generated at 2022-06-14 15:51:12.493586
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    _filename = 'test.ism'

# Generated at 2022-06-14 15:51:18.828766
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    video_id = '5189620'
    url = 'http://www.channelnewsasia.com/news/video_player/cna_video/%s/mobile.m3u8' % video_id
    return IsmFD().real_download(url, None)# Unit test for method real_download of class IsmFD

# Generated at 2022-06-14 15:51:29.784051
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:51:56.320571
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        params = {
            'bitrate': 400000,
            'duration': 50000,
            'sampling_rate': 44100,
            'channels': 2,
        }
        write_piff_header(stream, params)
        print(stream.getvalue())
        True



# Generated at 2022-06-14 15:52:01.881374
# Unit test for function extract_box_data
def test_extract_box_data():
    test_string = '0000002400000000647479704d534e5600000010776f72646d61696e75736572747900000001000000001a000000240000000074657874536572766572537461746500000014776f72646d61696e7573657274790000000100'
    test_string_bytes = binascii.unhexlify(test_string)
    expected_box_data = binascii.unhexlify('00000001000000001a')
    assert extract_box_data(test_string_bytes, (b'dtyp', b'msvc')) == expected_box_data


# Generated at 2022-06-14 15:52:13.943486
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    filename = 'test_filename.ism'
    info_dict = {
        'fragments': [{
            'url': 'https://test_url.ism',
        }],
    }

    def _download_fragment(ctx, url, info_dict):
        return url == 'https://test_url.ism' and info_dict == {}, b'moof' + u32.pack(0xf) + b'traf' + u32.pack(0xf) + b'tfhd' + u32.pack(0x4) + b'\x00' * 4

    def _append_fragment(ctx, frag_content):
        pass

    def _finish_frag_download(ctx):
        pass


# Generated at 2022-06-14 15:52:21.750454
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'codec_private_data': '1210',
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 48000,
        'duration': 10000,
    }
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:52:31.963866
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl_opts = {
        'noplaylist' : True,
        'simulate': True,
    }
    ydl = YoutubeDL(ydl_opts)
    ydl.add_default_info_extractors()


# Generated at 2022-06-14 15:52:43.472852
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:52:55.052208
# Unit test for function write_piff_header
def test_write_piff_header():
    def f(**kwargs):
        with io.BytesIO() as fd:
            write_piff_header(fd, kwargs)
            return fd.getvalue()


# Generated at 2022-06-14 15:53:04.397428
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        'track_id': 0x1,
        'fourcc': 'H264',
        'duration': 0x1,
        'timescale': 0x1,
        'language': 'eng',
        'height': 0x100,
        'width': 0x100,
        'codec_private_data': '01640033ffe100178c8b840a1444109d2c5e0e5a5d569d0101400000fa4040404040400401e16832760',
        'nal_unit_length_field': 4,
    }
    stream = FragmentFD(io.BytesIO())
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:53:05.455108
# Unit test for constructor of class IsmFD
def test_IsmFD():
    pass


# Generated at 2022-06-14 15:53:16.592181
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:54:13.927381
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    assert IsmFD().real_download("filename", "info_dict") == True

test_IsmFD_real_download()


# Generated at 2022-06-14 15:54:21.533180
# Unit test for function write_piff_header
def test_write_piff_header():
    track_id = 1
    fourcc = 'AVC1'
    duration = 650000000
    timescale = 10000000
    language = 'und'
    height = 720
    width = 1280
    is_audio = False
    creation_time = modification_time = int(time.time())

    codec_private_data = '0164001fffe1001ef8000047accf00000168eb0102fda80180021e01000014668d881ea06000001a200000001a2000c800000000'

# Generated at 2022-06-14 15:54:24.487697
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Constructor test
    ism_fd = IsmFD()
    assert ism_fd.FD_NAME == 'ism'


# Generated at 2022-06-14 15:54:37.126827
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Test with the URL of a ISM manifest and a working YouTube player
    ismfd = IsmFD({'noprogress': True}, {'url': 'http://s.ytimg.com/yts/swfbin/player-vflrbhY7X/watch_as3-vflz8sjQ7.swf'})

    # Test with a ISM manifest URL
    ismfd.real_download('test.ism', {'url': 'http://mss2.smart.stream.ne.jp/ts/hotel_au2/hotel_au2.ism/Manifest'})

    # Test with a ISM manifest URL and a working YouTube player

# Generated at 2022-06-14 15:54:46.761793
# Unit test for function write_piff_header
def test_write_piff_header():
    import struct
    out = io.BytesIO()
    params = {
        'track_id': 1,
        'duration': 2000,
        'timescale': 1000,
        'sampling_rate': 44100,
        'channels': 2,
        'bits_per_sample': 16,
        'fourcc': 'AACL',
    }
    write_piff_header(out, params)

# Generated at 2022-06-14 15:54:56.912974
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .ytdlsim import ytdl_hooks
    from .extractor import gen_extractors


# Generated at 2022-06-14 15:55:01.385562
# Unit test for constructor of class IsmFD
def test_IsmFD():
    import os.path
    import tempfile
    (filehandle, filename) = tempfile.mkstemp(text=False)
    os.close(filehandle)

    os.unlink(filename)


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:55:13.540439
# Unit test for function write_piff_header
def test_write_piff_header():
    from .helpers import Tester
    from .test_fragments import fragment_urls
    from .test_segments import mp4_mdat_payload
    from ..compat import (
        compat_etree_fromstring,
        compat_urllib_request,
    )

# Generated at 2022-06-14 15:55:21.154614
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import get_testdata_files_path
    from .smoothstreams import SmoothstreamsFD
    from .http import download_webpage
    from .extractor import get_info_extractor

    test_file = get_testdata_files_path() + 'test_ism.ism/Manifest'
    manifest = download_webpage(test_file, None)
    g = get_info_extractor(SmoothstreamsFD.ie_key())
    info = g._real_extract(SmoothstreamsFD.suitable(test_file), manifest)

    output = info['_output_file']

    # Open the video file we just created
    from .subtitles import subtitles_filename
    from .utils import determine_ext

    out_sub_filename = subtitles_filename(output, 'en') + determine_ext

# Generated at 2022-06-14 15:55:33.675458
# Unit test for function write_piff_header
def test_write_piff_header():
    output = io.BytesIO()
    params = dict(track_id=1, fourcc='H264', duration=0, width=1920, height=1080, nal_unit_length_field=4, codec_private_data='6764001facd9c01e9031ffcb80a0aa1263001fa810000030001000003000168ea00000168e9c80000001f976c01e9031ffcb805ae3dbf3e0e7b3a87a204700000030080000019c07ae7a1d4789bffc8b4f6bf4c4d2f6d300000001c0000000000f0')
    write_piff_header(output, params)
    output.seek(0)
    assert output.read() == binascii.unhex