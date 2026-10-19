

# Generated at 2022-06-14 15:48:24.471180
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:48:35.020622
# Unit test for function write_piff_header
def test_write_piff_header():
    #print(write_piff_header(sys.stdout, { 'track_id': 1, 'fourcc': 'AVC1', 'duration': 0,
    #                                      'codec_private_data': '67640029ffe100145e7e8cb15fbe5497c1e561020000003008000001074d0029ac400000101709f80ea8000002985dde
    #                                                              , 'sampling_rate': 44100, 'bits_per_sample': 16 }))
    #print(write_piff_header(sys.stdout, { 'track_id': 2, 'fourcc': 'AACL', 'duration': 0,
    #                                      'sampling_rate': 44100, 'channels': 2 }))
    pass


# Generated at 2022-06-14 15:48:47.089373
# Unit test for constructor of class IsmFD
def test_IsmFD():
    if not IsmFD.is_usable():
        raise unittest.SkipTest('ISMFD class is not usable')

    playlist_url = 'http://pubads.g.doubleclick.net/gampad/ads?sz=640x480&iu=/6062/iab_vast_samples/skippable&ciu_szs=300x250,728x90&impl=s&gdfp_req=1&env=vp&output=xml_vast2&unviewed_position_start=1&url=[referrer_url]&correlator=[timestamp]'

# Generated at 2022-06-14 15:48:57.310507
# Unit test for function extract_box_data
def test_extract_box_data():
    moov_box_data = binascii.unhexlify(
        '00000018' + '6d6f6f76' + '00000000' +
        '00000014' + '6d766864' + '00000000' +
        '00000005' + '66747970' + '69736D6C' + '00000001' + '69736F32'
    )
    extracted_box_data = extract_box_data(moov_box_data, (b'mvhd', ))

# Generated at 2022-06-14 15:49:05.131064
# Unit test for function extract_box_data
def test_extract_box_data():
    file_name = './playready/playready.ismc'
    with open(file_name, 'rb') as fin:
        data = fin.read()

    with open(file_name, 'rb') as fin:
        stream = io.BytesIO(fin.read())
        stream.seek(48)
        d = extract_box_data(stream.read(), (b'pssh', b'drm_system'))
        print(d)



# Generated at 2022-06-14 15:49:15.097855
# Unit test for function extract_box_data
def test_extract_box_data():
    fd = io.BytesIO(b'\x00\x00\x00\x1cfree\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x0cwide\x00\x00\x00\x08\x00\x00\x00\x01\x00\x00\x00\x0c')
    box1_data = extract_box_data(fd.read(), (b'wide',))
    assert box1_data == b'\x00\x00\x00\x01', 'box1_data failed'
    fd.seek(0)
    box2_data = extract_box_data(fd.read(), (b'free',))

# Generated at 2022-06-14 15:49:27.480175
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .downloader import YoutubeDL
    from .downloader import FakeYDL
    from .extractor.common import InfoExtractor
    import sys
    import os
    import tempfile
    import json
    url = 'http://www.example.com/testvideo.ism'

# Generated at 2022-06-14 15:49:34.201411
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    write_piff_header(stream, {
        'track_id': 1,
        'timescale': 90000,
        'duration': 90000,
        'height': 480,
        'width': 854,
        'language': 'eng',
        'fourcc': 'H264',
        'codec_private_data': '01640028ffe100186764002aacd9c01f8440202000003008000001b8f0a00050000000168ee3c80',
        'sampling_rate': 48000,
        'bits_per_sample': 16,
        'channels': 2,
    })

# Generated at 2022-06-14 15:49:47.655081
# Unit test for function extract_box_data
def test_extract_box_data():
    assert extract_box_data(binascii.unhexlify(b'000000006d6f6f76000000006d7668640000000000000018646973636f7665726500'), [b'moov', b'mvhd', b'dirc']) == binascii.unhexlify(b'646973636f76657265')
    from unittest import TestCase
    TestCase().assertEqual(extract_box_data(binascii.unhexlify(b'000000006d6f6f76000000006d7668640000000000000018646973636f7665726500'), [b'moov', b'mvhd', b'dirc']), binascii.unhexlify(b'646973636f76657265'))
test_extract_box_

# Generated at 2022-06-14 15:49:59.007501
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .dash import DASHIE, resolve_dash_template, parse_dash_manifest, _parse_mpd_formats
    from .utils import sanitize_open, determine_ext
    from .compat import compat_HTTPError
    from .downloader import Downloader
    from .extractor import gen_extractors
    best_audio_fmt = None
    class _FakeInfo:
        pass

    downloader = Downloader(params={'nocheckcertificate': True}, user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0')

    def _real_extract(self, url, *args, **kargs):
        print(url)

# Generated at 2022-06-14 15:50:13.038650
# Unit test for function extract_box_data
def test_extract_box_data():
    ftyp_box = u32.pack(36) + b'ftyp' + b'isml'  # major brand
    ftyp_box += u32.pack(1)  # minor version
    ftyp_box += b'piff' + b'iso2'  # compatible brands

    data = ftyp_box + b'A' * (100 - 36)

    assert extract_box_data(data, (b'ftyp', b'isml')) == None
    assert extract_box_data(data, (b'ftyp',)) == b'isml' + u32.pack(1) + b'piff' + b'iso2'
test_extract_box_data()



# Generated at 2022-06-14 15:50:14.181651
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Specific test case
    # IsmFD.real_download(filename, info_dict)
    pass


# Test:
# noinspection PyUnresolvedReferences

# Generated at 2022-06-14 15:50:24.318582
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 200000000,
        'timescale': 10000000,
        'language': 'und',
        'height': 0,
        'width': 0,
        'sampling_rate': 44100,
        'codec_private_data': '1210',
        'channels': 2,
        'bits_per_sample': 16
    }
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:50:32.962629
# Unit test for function extract_box_data
def test_extract_box_data():
    sample_box_data = u32.pack(0x10) + b'ABCD' + u32.pack(0x10) + b'EFGHI' + u32.pack(0x08) + b'JKLMNOP'
    assert(extract_box_data(sample_box_data, [b'ABCD']) == b'EFGHI')
    assert(extract_box_data(sample_box_data, [b'ABCD', b'EFGH']) == b'I')
    assert(extract_box_data(sample_box_data, [b'ABCD', b'EFGH', b'IJKL']) == b'')
    assert(extract_box_data(sample_box_data, [b'AAAAAAAA']) == None)

# Generated at 2022-06-14 15:50:41.494862
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AVC1',
        'duration': 20000000,
        'timescale': 10000000,
        'height': 1080,
        'width': 1920,
        'codec_private_data': '01640029ffe1001f674d401ef9402a0013a2006000003000100000300012003200056ee200056f02000560140013a820040068efbc8f15c12c000000300c9001000060001ee5880000030001003c00000030001ee8e800',
    }
    write_piff_header(stream, params)
    print(binascii.hexlify(stream.getvalue()))



# Generated at 2022-06-14 15:50:45.818085
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    input_data = os.path.join('..', 'tests', 'data', 'ism.ism')
    output_data = 'ism_test'
    run_IsmFD_test(input_data, output_data)



# Generated at 2022-06-14 15:50:58.247173
# Unit test for function extract_box_data
def test_extract_box_data():
    from .fragment import FragmentFD
    from .smoothstreams import SmoothStreamsFD
    from .fragment import update_url_query
    from ..downloader.common import FileDownloader
    from ..compat import compat_urlopen

    fe = FileDownloader({'username': 'sport365live', 'password': 'zw0VRS72', 'format': 'mp4_fragmented'})
    ie = fe._real_download(SmoothStreamsFD)
    stream = ie.get_audio_streams()[0].url
    stream = update_url_query(stream, {'format': 'fmp4'})
    stream = compat_urlopen(stream, data=b'\0' * 2).read()

# Generated at 2022-06-14 15:51:09.524359
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:51:11.199461
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD({})
    assert fd._fd_name == 'ism'


# Generated at 2022-06-14 15:51:23.947032
# Unit test for function write_piff_header
def test_write_piff_header():
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 10000000,
        'timescale': 44100,
        'sampling_rate': 44100,
        'channels': 2,
        'bits_per_sample': 16,
    }
    output = io.BytesIO()
    write_piff_header(output, params)

# Generated at 2022-06-14 15:51:55.595258
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .gen_extractors import get_info_extractor
    from .common import EXT_INFO_DICT
    from .extractor import get_info_extractor_list
    from .downloader import InfoExtractor

    # Test for constructor of IsmFD for adaptative streaming (2014-11-28)
    url = 'http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest'
    ie = get_info_extractor(url, InfoExtractor)
    info_dict = ie.get_info(url, {'ext': 'ism'})
    EXT_INFO_DICT.update(info_dict)
    get_info_extractor_list()

    # Test for constructor of IsmFD for IIS Smooth Streaming (2014-11-28)

# Generated at 2022-06-14 15:52:08.280182
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import make_tempdir
    from .extractor import gen_extractors
    from .downloader import gen_fd_names

    video_id = 'h4WS4FGPBx4'
    tempdir = make_tempdir()
    extractor_list = gen_extractors()
    fd_names = gen_fd_names(extractor_list)

# Generated at 2022-06-14 15:52:09.428128
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    raise Exception('TODO')

# Generated at 2022-06-14 15:52:11.566937
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD(None, None)
    assert fd.FD_NAME == 'ism'

# Generated at 2022-06-14 15:52:12.345093
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass



# Generated at 2022-06-14 15:52:17.888054
# Unit test for function extract_box_data
def test_extract_box_data():
    test_data = binascii.unhexlify(b'0000000200000000000060E6D6F6F7600000000000000186674797032')
    test_result = extract_box_data(test_data, [b'ftyp', b'moov'])
    assert binascii.hexlify(test_result) == b'000000186674797032'
test_extract_box_data()



# Generated at 2022-06-14 15:52:24.310314
# Unit test for constructor of class IsmFD
def test_IsmFD():
    import sys
    errno = IsmFD._real_initialize()
    if errno < 0:
        sys.stderr.write(u'ERROR: %s\n' % compat_str(IsmCl.get_error_message(errno)))
    else:
        sys.stdout.write(u'SUCCESS\n')

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:52:33.246945
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import re
    from urllib.parse import urlparse
    from ytdl.downloader.http import HttpFD
    from ytdl.downloader.dash import DashFD
    from ytdl.downloader.ism import IsmFD
    from ytdl.utils import FileDownloader

# Generated at 2022-06-14 15:52:44.355800
# Unit test for function write_piff_header
def test_write_piff_header():
    from .f4m import write_pssh_box, write_mss_protection_header
    params = {
        'track_id': 1,
        'channels': 2,
        'sampling_rate': 44100,
        'bits_per_sample': 16,
        'track_type': 'soun',
        'duration': 15000000,
        'fourcc': 'AACL',
        'timescale': 10000000,
        'language': 'und',
    }

# Generated at 2022-06-14 15:52:48.868646
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 100000000,
        'sampling_rate': 48000,
        'channels': 2,
        'bits_per_sample': 16,
        'nal_unit_length_field': 4,
        'codec_private_data': '0000000167640033ACD90A1E8B3C827C110A001000468EE3C80',
    }
    write_piff_header(stream, params)
    # Compare the dump of the stream with the expected output

# Generated at 2022-06-14 15:54:05.848793
# Unit test for function write_piff_header
def test_write_piff_header():
    def test(params_dict):
        f = io.BytesIO()
        write_piff_header(f, params_dict)

        f.seek(0)
        box_type = f.read(4)
        box_size = u32.unpack(f.read(4))[0]
        assert box_size == f.getbuffer().nbytes - 8
        moov = f.read(box_size)
        moov_b = io.BytesIO(moov)

        def traverse_box(b):
            b_type = b.read(4)
            b_size = u32.unpack(b.read(4))[0]
            if b_size == 1:
                b_size = u64.unpack(b.read(8))[0]


# Generated at 2022-06-14 15:54:14.024023
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        write_piff_header(
            stream,
            {
                'track_id': 1,
                'duration': 1000,
                'timescale': 10000000,
                'language': 'und',
                'fourcc': 'H264',
                'sampling_rate': 44100,
                'bits_per_sample': 16,
                'channels': 2,
                'codec_private_data': '01640029ffe1001427640029ac',
                'nal_unit_length_field': 4,
            }
        )

# Generated at 2022-06-14 15:54:21.581757
# Unit test for constructor of class IsmFD
def test_IsmFD():
    manifest_url = 'http://htdlive-i.akamaihd.net/i/nba_vod_hd@146988/index_700_av.m3u8?sd=10&rebase=on'
    video_id = 'live'

# Generated at 2022-06-14 15:54:33.510773
# Unit test for function write_piff_header
def test_write_piff_header():
    # Testing video track
    video_params = {
        'track_id': 1,
        'fourcc': 'AVC1',
        'width': 1920,
        'height': 1080,
        'sampling_rate': 0,
        'duration': 0,
        'codec_private_data': '0164001f0280018001e97ffefb080103c80001384d00013c401010017000000300800000000c80000001408d840',
        'nal_unit_length_field': 4
    }
    video_f = io.BytesIO()
    write_piff_header(video_f, video_params)
    print(video_f.getvalue())

# Generated at 2022-06-14 15:54:38.390571
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    global u8, u16, u1616, u32, u64, s16, s88, s1616, unity_matrix
    u8 = struct.Struct('>B')
    u16 = struct.Struct('>H')
    u32 = struct.Struct('>I')
    u64 = struct.Struct('>Q')
    s16 = struct.Struct('>h')
    s88 = struct.Struct('>bb')
    s1616 = struct.Struct('>hh')
    unity_matrix = b'\x00' * 36
    dummy_stream = io.BytesIO()

# Generated at 2022-06-14 15:54:47.783033
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:54:58.403340
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    print('TEST_ISMFD_REAL_DOWNLOAD')
    obj = IsmFD()
    obj._download_fragment = lambda ctx, url, info_dict: (True, b'Data')
    obj._prepare_and_start_frag_download = msw.noop
    obj._finish_frag_download = msw.noop
    obj.report_error = msw.noop
    obj.report_skip_fragment = msw.noop
    obj.report_retry_fragment = msw.noop
    obj._append_fragment = msw.noop

# Generated at 2022-06-14 15:55:11.192013
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:55:19.992203
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from ..extractor import gen_extractors
    from ..downloader import gen_extractor_classes

    # Test for RTMP
    _, info_dict = next(gen_extractors(['rtmp://cp379973.edgefcs.net/ondemand/media/mp4:c8/c8/c8c88ad6-2b01-44ee-9c42-7f59208e860c/c8c88ad6-2b01-44ee-9c42-7f59208e860c_300.mp4'], downloader=False))
    assert info_dict['protocol'] == 'rtmp'

    # Test for ISM

# Generated at 2022-06-14 15:55:21.201199
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass
