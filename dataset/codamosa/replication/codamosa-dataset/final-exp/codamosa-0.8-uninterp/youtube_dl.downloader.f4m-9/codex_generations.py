

# Generated at 2022-06-14 15:23:28.376188
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .test_fragments import _TEST_FRAGMENTS_DUMP

    with open(_TEST_FRAGMENTS_DUMP, 'rb') as f:
        data = FlvReader(f.read()).read_bootstrap_info()

# Generated at 2022-06-14 15:23:33.950764
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    from xml.etree import ElementTree
    et = ElementTree
    media1 = et.Element('media')
    media2 = et.Element('media', {'drmAdditionalHeader': '1'})
    media3 = et.Element('media', {'drmAdditionalHeaderId': '2'})
    media4 = et.Element('media', {'drmAdditionalHeaderSetId': '3'})
    test_media = [media1, media2, media3, media4]
    assert remove_encrypted_media(test_media) == [media1]



# Generated at 2022-06-14 15:23:43.017230
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from .extractor import get_suitable_downloader
    from .common import str_to_bytes

    suitable_downloader = get_suitable_downloader(str_to_bytes('https://example.com/'))
    assert suitable_downloader and isinstance(suitable_downloader, F4mFD)

    fd = suitable_downloader('example.com', {'url': 'https://example.com/example.f4m'})
    fd.real_download('output.flv', {'url': 'https://example.com/example.f4m'})

# Generated at 2022-06-14 15:23:53.145661
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    with io.open('tests/testdata/test_abst.txt', 'rb')as f:
        abst = FlvReader(f.read()).read_abst()
        assert abst['segments'][0] == {
            'segment_run': [(0, 1), (1, 1)],
        }
        assert abst['fragments'][0]['fragments'][0] == {
            'first': 1,
            'ts': 60,
            'duration': 60,
            'discontinuity_indicator': None
        }
        assert abst['fragments'][1]['fragments'][0] == {
            'first': 1,
            'ts': 0,
            'duration': 480,
            'discontinuity_indicator': 1,
        }



# Generated at 2022-06-14 15:24:03.663150
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Testing the method real_download of class F4mFD.
    F4mFD.real_download = real_download
    test_url = 'http://backend.dev.snapito.com/web/f4m?url=http://test.dev/test/test.f4m&format=mp4'
    ydl = YoutubeDL(params={'format': 'mp4'})

# Generated at 2022-06-14 15:24:06.745753
# Unit test for function write_flv_header
def test_write_flv_header():
    from io import BytesIO
    stream = BytesIO()
    write_flv_header(stream)
    assert stream.getvalue() == b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
test_write_flv_header()



# Generated at 2022-06-14 15:24:16.628246
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:24:23.986792
# Unit test for function build_fragments_list
def test_build_fragments_list():
    bootstrap_info = read_bootstrap_info(open(
        'tests/data/hds/bootstrap_info.abst', 'rb').read())
    assert build_fragments_list(bootstrap_info) == [
        (0, 0), (0, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8),
        (4, 9), (5, 10)]



# Generated at 2022-06-14 15:24:35.179702
# Unit test for function get_base_url
def test_get_base_url():
    assert get_base_url(compat_etree_fromstring('''
        <manifest xmlns="http://ns.adobe.com/f4m/1.0">
            <baseURL>abc</baseURL>
            <media />
        </manifest>
    ''')) == 'abc'
    assert get_base_url(compat_etree_fromstring('''
        <manifest xmlns="http://ns.adobe.com/f4m/1.0">
            <baseURL />
            <media />
        </manifest>
    ''')) is None

# Generated at 2022-06-14 15:24:41.871419
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:09.955973
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import os
    import tempfile
    filename = os.path.join(tempfile.gettempdir(), 'test_bootstrap')

# Generated at 2022-06-14 15:25:20.206714
# Unit test for function build_fragments_list
def test_build_fragments_list():
    def _test(boot_info, fragments):
        fragments_from_boot_info = build_fragments_list(boot_info)
        assert fragments_from_boot_info == fragments


# Generated at 2022-06-14 15:25:31.594354
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from .Downloader import FakeYDL
    from .Downloader import FakeYDLFile
    from .utils import FakeTempDir

    def _range_matcher(range):
        def range_matcher(request):
            actual_range = request.headers.get('Range')
            expected_range = 'bytes=%d-' % range
            if actual_range != expected_range:
                raise AssertionError(
                    'Expected range "%s" but got "%s"' % (expected_range, actual_range))
            return True
        return range_matcher


# Generated at 2022-06-14 15:25:42.017247
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    """
    Test FlvReader.read_abst
    """

# Generated at 2022-06-14 15:25:51.358637
# Unit test for function build_fragments_list
def test_build_fragments_list():
    boot_info = {
        'segments': [
            {
                'segment_run': [
                    (0, 2),
                    (1, 3),
                ],
            },
        ],
        'fragments': [
            {
                'fragments': [
                    # first, ts, duration, discontinuity_indicator
                    (0, 0, 0, None),
                    (2, 15000, 5000, False),
                    (3, 20000, 5000, False),
                    (4, 25000, 5000, False),
                    (5, 30000, 5000, False),
                ],
            },
        ],
        'live': False,
    }

# Generated at 2022-06-14 15:26:00.964454
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import unittest


# Generated at 2022-06-14 15:26:10.442323
# Unit test for function build_fragments_list
def test_build_fragments_list():
    bootstrap_info = {
        'segments': [{
            'segment_run': [
                (1, 3),
                (2, 1),
            ]
        }],
        'fragments': [{
            'fragments': [{
                'first': 1,
                'ts': 1234,
                'duration': 5,
                'discontinuity_indicator': None,
            }, {
                'first': 2,
                'ts': 2234,
                'duration': 5,
                'discontinuity_indicator': None,
            }, {
                'first': 3,
                'ts': 3234,
                'duration': 0,
                'discontinuity_indicator': 3,
            }]
        }],
        'live': False,
    }
    fragments = build

# Generated at 2022-06-14 15:26:15.020570
# Unit test for function write_flv_header
def test_write_flv_header():
    from cStringIO import StringIO
    s = StringIO()
    write_flv_header(s)
    assert s.getvalue() == b'FLV\x01\x05\x00\x00\x00\t\x00\x00\x00\x00'
test_write_flv_header()



# Generated at 2022-06-14 15:26:26.993168
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:26:37.360103
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    def test_afrt(s, expect):
        afrt = FlvReader(s).read_afrt()
        assert afrt == expect, (afrt, expect)

    # Test case from https://github.com/rg3/youtube-dl/blob/test/test_downloader_hls.py

# Generated at 2022-06-14 15:26:59.561561
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download(): #Test passed
    from youtube_dl.downloader.f4mfd import F4mFD
    url = 'my_url'
    info_dict = {'id':'Bish0u', 'ext':'f4m', 'url':url}
    filename = 'Bish0u.f4m'
    youtube_dl = type('obj', (object,), {'params': {'test': True}, 'to_screen': print, 'report_error': print, 'report_warning': print})()
    ffd = F4mFD(youtube_dl)
    ffd.real_download(filename, info_dict)


# Generated at 2022-06-14 15:27:07.230157
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    flv_reader = FlvReader(b'\x00\x00\x00\x00' + b'asrt' + b'\x00\x00\x00\x00' +
                           b'\x00\x00\x00\x01' +
                           b'\x00\x00\x00\x03' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x01' + b'\x00\x00\x00\x00')
    result = flv_reader.read_asrt()
    assert result == {
        'segment_run': [(0, 3)],
    }


# Generated at 2022-06-14 15:27:11.775248
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import io
    import tempfile
    fd = F4mFD(None, None)
    stream = io.open(os.path.join(os.path.dirname(__file__), 'test.f4m.xml'), 'r', encoding='utf-8')
    temp = tempfile.TemporaryFile()
    assert(fd.real_download(temp, {"url": "", "tbr": None, "player_url": "", "protocol": 'm3u8', "fragment_base_url": 'http://resources.download.tsi.telecom-paristech.fr/gpac/DASH_CONFORMANCE/TelecomParisTech/mp4-dash/mp4-dash-fragments.mp4'}))



# Generated at 2022-06-14 15:27:22.239228
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:27:32.195266
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from ..compat import compat_urllib_request
    from ..utils import (
        sanitized_Request,
    )
    from ..downloader.http import HttpFD
    bootstrap_url = 'https://manifest.us.rtl.com/v1/a1/5221bae5fb8d5a5f5c1a5a5a32a812eb/5221bae5fb8d5a5f5c1a5a5a32a812eb/abc.abc.abc.abc_rtl_de_hls_1500_0_vod_10.abst'
    box_data = HttpFD(sanitized_Request(
        bootstrap_url), progress_hooks=[lambda *_: None]).readall()

# Generated at 2022-06-14 15:27:44.191868
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:53.358331
# Unit test for function build_fragments_list
def test_build_fragments_list():
    def b(s):
        return s.encode('ascii')

    def b64(s):
        return b(compat_b64decode(s))

    def build_test_bootstrap_info(segment_run_table, fragment_run_entry_table, live=False):
        return {
            'live': live,
            'segments': [
                {'segment_run': segment_run_table}
            ],
            'fragments': [
                {'fragments': fragment_run_entry_table}
            ],
        }


# Generated at 2022-06-14 15:28:04.875132
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:28:15.247560
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:28:26.210897
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:29:22.287803
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:32.322699
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    import struct
    abst = struct.pack('!IBBB',
                       0,  # box size (filled later)
                       ord('a'), ord('b'), ord('s'), ord('t'))
    abst += struct.pack('!BBBBI',
                        0,  # version
                        0, 0, 0,  # flags
                        0,  # BootstrapinfoVersion
                        0x20)  # Profile,Live,Update,Reserved
    abst += struct.pack('!II',
                        0,  # time scale
                        0)  # CurrentMediaTime
    abst += struct.pack('!QQ',
                        0,  # SmpteTimeCodeOffset
                        0)  # SmpteTimeCodeOffset
    abst += struct.pack('!Bc',
                        1, b'\x00')  # MovieIdentifier
    abst += struct

# Generated at 2022-06-14 15:29:41.046854
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .common import fake_http_response

    # Test data from https://github.com/rg3/youtube-dl/blob/master/youtube_dl/extractor/limelight.py
    test_url = 'https://example.com/'

# Generated at 2022-06-14 15:29:53.885208
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:30:01.697017
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from io import BytesIO
    fd = F4mFD()
    # Assert real_download with filename, info_dict input
    filename = 'test'
    info_dict = {'url': 'http://someurl.com/manifest.f4m'}
    fd.ydl = mock.MagicMock()
    fd.ydl.urlopen = mock.MagicMock()
    fd.ydl.urlopen.return_value = BytesIO(b'<manifest></manifest>')

    fd._get_bootstrap_from_url = mock.MagicMock()
    fd._get_bootstrap_from_url.return_value = read_bootstrap_info(b'\x00\x00\x00\x00\x00')

# Generated at 2022-06-14 15:30:08.382948
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    """
    Test case for method real_download of class F4mFD.
    """
    # Test default case
    # Expected result: True
    form = F4mFD("", None)
    assert True == form.real_download("filename.txt", "info_dict.txt")
    
    # Test case with real filename and info_dict
    url = "http://acs.org/acsmicrosite/live/hds/acsmtv-sd.f4m"
    with youtube_dl.YoutubeDL(params={}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
    for fmt in info_dict['formats']:
        form = F4mFD("", None)
        assert True == form.real_download(fmt['url'], info_dict)


# Generated at 2022-06-14 15:30:16.129001
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:30:27.417909
# Unit test for function build_fragments_list
def test_build_fragments_list():
    from xml.dom import minidom
    from ..downloader.http import SELECT_FORMAT

    _, boot_url, _ = SELECT_FORMAT(
        'http://player.ooyala.com/static/cacheable/7c83faf1d6f12caf1b35eee96c6d4477/player_v2.swf?embedCode=h0NWZvczrZTq6-Lq3rqACwGEFTzJ2aD0')  # noqa

    boot_content = compat_urllib_request.urlopen(boot_url).read()

    boot_info = read_bootstrap_info(boot_content)

    list_fragments = build_fragments_list(boot_info)

# Each fragment is a tuple with the format (segment_number,

# Generated at 2022-06-14 15:30:36.199238
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # [youtube] tN37YbSkcW8: Downloading f4m manifest
    # [youtube] tN37YbSkcW8: Downloading f4m manifest
    # [info] Reading annotations for video tN37YbSkcW8
    # [info] Writing video description metadata as JSON to: video1.info.json
    # [info] Downloading video #1
    # [download] Destination: video1.f247.mp4
    # [download] 100% of 2.35MiB in 00:00
    # [ffmpeg] Destination: video1.mp4
    # Deleted original file video1.f247.mp4 (pass -k to keep)

    # TODO: Add tests

    return True

# Generated at 2022-06-14 15:30:46.880619
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    f = io.BytesIO(
        b'\x00\x00\x00)\x61\x66\x72\x74\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00')

# Generated at 2022-06-14 15:32:17.888757
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = (
        b'\x00\x00\x00&'  # box_size
        b'asrt'  # box_type
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x00'  # QualityEntryCount
        b'\x00\x00\x00\x01'  # SegmentRunEntryCount
        b'\x00\x00\x00\x00'  # FirstSegment
        b'\x00\x00\x00\x0f'  # FragmentsPerSegment
    )
    assert FlvReader(data).read_asrt() == {
        'segment_run': [(0, 15)],
    }

