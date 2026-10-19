

# Generated at 2022-06-14 15:22:57.493593
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x00\x10\x61\x73\x72\x74\x00\x00\x00\x00\x00\x00\x00\x02' \
        b'\x47\x65\x6e\x65\x72\x61\x6c\x00\x41\x64\x73\x00\x00\x00\x00\x02' \
        b'\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
        b'\x00\x00\x00\x01\x00\x00\x00\x0b'
    assert Fl

# Generated at 2022-06-14 15:23:03.279783
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:23:12.626841
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    """
    Unit test for method read_bootstrap_info of class FlvReader
    """
    flv_data = open("tests/data/bootstrap_live_test/bootstrap_live.abst", "rb").read()
    res = FlvReader(flv_data).read_bootstrap_info()
    assert res['segments'][0]['segment_run'][0][0] == 1
    assert res['segments'][0]['segment_run'][0][1] == 5

    quality_entry_count = 1
    segments_count = 1
    fragments_run_count = 1
    assert len(res['segments']) == segments_count
    assert len(res['segments'][0]['segment_run']) == quality_entry_count

# Generated at 2022-06-14 15:23:24.131092
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():

    filepath = 'test_files/test_f4m_video_playlist.abst'
    with io.open(filepath, 'rb') as f:
        data = f.read()
    assert len(data) > 100

    bootstrap_info = FlvReader(data).read_bootstrap_info()
    assert len(bootstrap_info['fragments']) == 1
    assert len(bootstrap_info['segments']) == 1
    assert bootstrap_info['segments'][0]['segment_run'] == [(1, 1)]
    assert len(bootstrap_info['fragments'][0]['fragments']) == 1
    assert bootstrap_info['fragments'][0]['fragments'][0]['first'] == 1

# Generated at 2022-06-14 15:23:35.385581
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    data = b'\x00\x00\x00\x4A'  # box_size
    data += b'\x61\x62\x73\x74'  # box_type
    data += b'\x01'  # version
    data += b'\x00\x00\x00'  # flags
    data += b'\x00\x00\x00\x02'  # BootstrapinfoVersion
    data += b'\x00'  # Profile,Live,Update,Reserved
    data += b'\x00\x00\x00\x01'  # time_scale
    data += b'\x00\x00\x00\x00\x00\x00\x00\x01'  # CurrentMediaTime

# Generated at 2022-06-14 15:23:41.884540
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    assert b'\x00' == FlvReader(b'\x00').read_string()
    assert b'abc' == FlvReader(b'abc\x00').read_string()
    assert len(b'abc') == len(FlvReader(b'abc\x00').read_string())
    assert b'' == FlvReader(b'\x00').read_string()


# Generated at 2022-06-14 15:23:52.288458
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:24:03.298973
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    # testcase 1
    # output size = 637
    # box type = asrt
    # box data = version flags QualityEntryCount SegmentRunTable
    flv_reader = FlvReader(open(
        r'C:\Projects\testdata\f4v\bootstrap_info_testcase1.bin', 'rb').read())
    size, box_type, box_data = flv_reader.read_box_info()
    assert size == 637
    assert box_type == b'asrt'
    assert len(box_data) == 624

    # testcase 2
    # output size = 7
    # box type = abst
    # box data = version flags BootstrapinfoVersion ProfileLiveUpdate Reserved
    # TimeScale CurrentMediaTime SmpteTimeCodeOffset MovieIdentifier
    # ServerEntryCount ServerEntryTable QualityEntry

# Generated at 2022-06-14 15:24:07.813265
# Unit test for function write_flv_header
def test_write_flv_header():
    """
    FLV header should be 12 bytes.
    Asserts that it is 12 bytes long.
    """
    stream = io.BytesIO()
    write_flv_header(stream)
    assert len(stream.getvalue()) == 12
# End unit test


# Generated at 2022-06-14 15:24:17.216153
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01'
    assert FlvReader(data).read_asrt() == {
        'segment_run': [(1, 1)],
    }
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x10\x00\x00\x00\x10'
    assert FlvReader(data).read_asrt() == {
        'segment_run': [(2, 2), (16, 16)],
    }


# Generated at 2022-06-14 15:25:28.451431
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .common import fake_http_server
    from ..compat import compat_HTTPError
    from ..downloader.http import HEADRequest
    from ..downloader.http.headers import HeadRequest, UrlRequest
    # Helper functions for building bootstrap info
    BOOTSTRAP_BOX_TYPE = b'abst'
    ASRT_BOX_TYPE = b'asrt'
    AFRT_BOX_TYPE = b'afrt'
    def _write_unsigned_int(s, x):
        s.write(compat_struct_pack('!I', x))
    def _write_unsigned_long_long(s, x):
        s.write(compat_struct_pack('!Q', x))
    def _write_string(s, x):
        s.write(x)

# Generated at 2022-06-14 15:25:36.894385
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    xml = '''
        <media href="manifest-mpd-Q61285625-VOD.f4m">
        <id>1</id>
        <mimeType>video/mp4</mimeType>
        <bitrate>588</bitrate>
        <width>640</width>
        <height>360</height>
        <meanBitrate>588000</meanBitrate>
        <url>http://example.com</url>
        <drmAdditionalHeaderId>0</drmAdditionalHeaderId>
        <drmAdditionalHeaderSetId>0</drmAdditionalHeaderSetId>
        <drmAdditionalHeader>ABCDEF</drmAdditionalHeader>
        </media>'''
    root = compat_etree_fromstring(xml)
    assert len(root) == 1
    assert root[0].tag == 'media'

# Generated at 2022-06-14 15:25:39.460762
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    from .f4f_test import TESTS

    for input_, expected_output in TESTS:

        reader = FlvReader(b'')
        reader.write(input_)
        reader.seek(0)

        assert reader.read_string() == expected_output

    print('Success')

if __name__ == '__main__':
    test_FlvReader_read_string()



# Generated at 2022-06-14 15:25:52.034389
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Try to download a single fragment of this f4m stream.
    # The resulting fragment is expected to be an flv file only containing an mdat box.
    # The size of the box is 7 bytes.
    # The f4m stream is a video of length 0.5 seconds.
    # The video should provide omxplayer with this error:
    # [mpeg4_mediacodec @ 0x6ac0760] Unsupported visual object type
    # [mpeg4_mediacodec @ 0x6ac0760] Could not find codec parameters
    # [mpeg4 @ 0x6a76240] All info found
    url = 'http://liverail-d.cdn.turner.com/tbs/bigbrother/segment/0/0/au_au_1.f4m'
    info_dict = {}
    fileutils

# Generated at 2022-06-14 15:25:55.414771
# Unit test for function get_base_url
def test_get_base_url():
    manifest = {'baseURL': 'a/b/c'}
    actual = get_base_url(manifest)
    expected = 'a/b/c'
    assert actual == expected


# Generated at 2022-06-14 15:25:59.391304
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    reader = FlvReader(b'\x01\x00\x00\x00hello\x00world\x00\x00\x00\x01')
    assert reader.read_string() == b'hello'
    assert reader.read_string() == b'world'
    assert reader.read_unsigned_char() == 1



# Generated at 2022-06-14 15:26:09.465788
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:26:19.393951
# Unit test for function build_fragments_list
def test_build_fragments_list():
    from json import loads
    from os.path import join

    _TEST_DIR = 'tests/f4m/'
    for f4m_file in ['live.f4m', 'live2.f4m', 'playlist.f4m', 'playlist2.f4m']:
        with open(join(_TEST_DIR, f4m_file), 'rb') as f:
            data = f.read()
        # Get the bootstrap info
        bootstrap_info = read_bootstrap_info(data[data.find(b'abst'):data.find(b'asrt')])
        try:
            expected_result = loads(data[data.find(b'SegmentList'):data.rfind(b'</SegmentList>') + 15])
        except ValueError:
            expected_result

# Generated at 2022-06-14 15:26:30.868163
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:26:41.431251
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    """
    Test the extractor of fragments info from an afrt box.
    """
    # afrt box data

# Generated at 2022-06-14 15:27:11.889935
# Unit test for function get_base_url
def test_get_base_url():
    xml_text = '''
<?xml version="1.0"?>
<manifest xmlns="http://ns.adobe.com/f4m/1.0">
    <baseURL>http://test.com</baseURL>
    <media href="a" />
</manifest>
'''
    assert get_base_url(compat_etree_fromstring(xml_text)) == 'http://test.com'
    xml_text = '''
<?xml version="1.0"?>
<manifest xmlns="http://ns.adobe.com/f4m/2.0">
    <baseURL>http://test.com/</baseURL>
    <media href="a" />
</manifest>
'''

# Generated at 2022-06-14 15:27:22.306837
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:32.231282
# Unit test for function get_base_url
def test_get_base_url():
    test_manifest = """<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns="http://ns.adobe.com/f4m/1.0">
    <baseURL>http://test.org/</baseURL>
</manifest>
"""
    manifest = compat_etree_fromstring(test_manifest)
    assert get_base_url(manifest) == 'http://test.org/'
    # when baseURL is empty string or blank characters
    test_manifest = """<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns="http://ns.adobe.com/f4m/1.0">
    <baseURL></baseURL>
</manifest>
"""
    manifest = compat_etree_fromstring(test_manifest)
   

# Generated at 2022-06-14 15:27:44.280038
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    abst_box_data = b"\x00\x00\x00\x3c\x61\x62\x73\x74\x01\x00\x00" \
    b"\x00\x14\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01" \
    b"\x00\x00\x00\x2b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00" \
   

# Generated at 2022-06-14 15:27:53.398609
# Unit test for function get_base_url
def test_get_base_url():
    manifest_url = 'http://some/path'
    manifest = compat_etree_fromstring('''<?xml version="1.0"?>
    <manifest xmlns="http://ns.adobe.com/f4m/1.0">
      <baseURL>http://example.com/</baseURL>
    </manifest>
    ''')
    assert get_base_url(manifest) == 'http://example.com/'
    manifest = compat_etree_fromstring('''<?xml version="1.0"?>
    <manifest xmlns="http://ns.adobe.com/f4m/1.0">
      <baseURL>http://example.com</baseURL>
    </manifest>
    ''')

# Generated at 2022-06-14 15:28:04.875245
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    """Test funciton write_metadata_tag""" 
    metadata = b'\x02\x00\x0a\x6f\x6e\x4d\x65\x74\x61\x44\x61\x74\x61\x08\x00\x00\x00\x00\x00\x00\x00\x02\x00\x0b\x64\x72\x61\x77\x4f\x6e\x4d\x65\x74\x61\x44\x61\x74\x61\x00\x40\x34\x00\x00\x00\x00\x00\x00\x00'
    file = open('test.flv','wb')
    write_flv_header(file)
    write_

# Generated at 2022-06-14 15:28:15.290458
# Unit test for method real_download of class F4mFD

# Generated at 2022-06-14 15:28:26.262580
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:28:36.027821
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:28:44.852249
# Unit test for function build_fragments_list
def test_build_fragments_list():
    # A case where segment_run_table['segment_run'] is not empty
    boot_info = {
        'fragments': [
            {
                'fragments': [
                    {
                        'first': 1,
                        'ts': 0,
                        'duration': 0,
                        'discontinuity_indicator': 1,
                    },
                ]
            }
        ],
        'segments': [
            {
                'segment_run': [
                    (1, 1234),
                ],
            },
        ],
    }
    assert build_fragments_list(boot_info) == [(1, i) for i in range(1, 1235)]

    # A case where segment_run_table['segment_run'] is empty

# Generated at 2022-06-14 15:29:04.260360
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:06.581812
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    f4mFD = F4mFD()
    f4mFD.real_download("filename", "info_dict")

# Generated at 2022-06-14 15:29:15.676680
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    input = b'\x00\x00\x00\x4c\x61\x73\x72\x74\x00\x00\x00\x00\x00\x00\x00\x01' + \
            b'\x63\x68\x75\x6e\x6b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01' + \
            b'\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02'
    f = FlvReader(input)


# Generated at 2022-06-14 15:29:22.309369
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x00\x20\x61\x73\x72\x74\x00\x00\x00\x00\x00\x00\x00\x01' \
        b'\x2e\x33\x35\x30\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00' \
        b'\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x04'
    fp = FlvReader(data)

# Generated at 2022-06-14 15:29:32.321647
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:29:38.458830
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import test_utils
    import subprocess
    import time
    import tempfile
    import os
    import sys

    def run_real_download_test(test_path, file_to_upload):
        temp_dir = tempfile.mkdtemp()
        temp_path = os.path.join(temp_dir, 'test.mp4')

# Generated at 2022-06-14 15:29:47.084749
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .common import read_fixture_data
    example = read_fixture_data('flv_read_abst.txt')
    example = io.BytesIO(example)
    res = FlvReader(example).read_abst()
    assert res['live'] == False
    assert len(res['segments']) == 2
    assert len(res['segments'][0]['segment_run']) == 1
    assert res['segments'][0]['segment_run'][0] == (0, 1)
    assert len(res['segments'][1]['segment_run']) == 1
    assert res['segments'][1]['segment_run'][0] == (1, 1)
    assert len(res['fragments']) == 2

# Generated at 2022-06-14 15:29:54.560383
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    segments = FlvReader(compat_b64decode('''
        AQAAAPgAAAAAAAAAAOoAEVGVzdCBUZXN0AAAAAAAAAAAIAAgAAQAAABAAAAAAbAAEAAAAAAA
        AAAAAAABAAEAAAAAAACAAAEAAAAAAAAAAAAAAAIAAgAAAAAAAAACAAAEA/wAAABAAAAAAAA
        AAA=
        ''')).read_asrt()
    assert segments == {
        'segment_run': [
            (0, 6),
        ],
    }



# Generated at 2022-06-14 15:30:02.106315
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:30:12.655929
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:30:51.225735
# Unit test for function build_fragments_list
def test_build_fragments_list():
    """Verify that build_fragments_list() works as expected"""

# Generated at 2022-06-14 15:31:00.271604
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:31:11.275794
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:31:21.967048
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    f = io.BytesIO(
        b'\x00\x00\x00\x1d\x61\x73\x72\x74\x00\x00'
        b'\x00\x00\x02\x61\x34\x00\x61\x61\x00\x00'
        b'\x00\x01\x00\x00\x00\x00\x00\x00\x20\x00'
        b'\x00\x00\x2a\x00\x00\x00\x00\x00\x00\x00'
    )
    assert FlvReader(f).read_asrt() == {
        'segment_run': [
            (0, 42),
        ],
    }



# Generated at 2022-06-14 15:31:29.034710
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.utils import DownloadError
    dl = FileDownloader({'quiet': True})
    dl.add_info_extractor(F4mIE())
    dl.add_info_extractor(M3u8IE())
    dl.params['noprogress'] = True
    dl.to_screen = lambda *a, **k: None


# Generated at 2022-06-14 15:31:40.900080
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    # Test against a typical flv file
    real_size, box_type, box_data = FlvReader(b'\x00\x00\x00\x00').read_box_info()
    assert(real_size == 0)
    assert(box_type == b'\x00\x00\x00\x00')
    assert(box_data == b'')
    real_size, box_type, box_data = FlvReader(b'\x01\x00\x00\x00\x01\x02\x03\x04').read_box_info()
    assert(real_size == 1)
    assert(box_type == b'\x01\x02\x03\x04')
    assert(box_data == b'')
    real_size, box_type, box_

# Generated at 2022-06-14 15:31:51.052338
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:32:00.591119
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    tests = [
        ('\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
         '\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00',
         [{'segment_run': [(1, 1)]}]),
    ]
    for test, expected in tests:
        res = FlvReader(test).read_asrt()
        assert res == expected, 'Test failed: %r != %r' % (res, expected)


# Generated at 2022-06-14 15:32:07.315469
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:32:17.290774
# Unit test for method read_box_info of class FlvReader