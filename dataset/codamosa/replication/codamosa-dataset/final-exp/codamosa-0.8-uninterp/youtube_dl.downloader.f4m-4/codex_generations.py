

# Generated at 2022-06-14 15:22:47.803153
# Unit test for function build_fragments_list
def test_build_fragments_list():
    # Testing non-live
    boot_info = {
        'live': False,
        'segments': [{
            'segment_run': [
                (0, 2),
                (1, 1),
            ]
        }],
        'fragments': [{
            'fragments': [
                {'first': 0, 'ts': 0, 'duration': 4, 'discontinuity_indicator': None},
                {'first': 3, 'ts': 8, 'duration': 4, 'discontinuity_indicator': None},
                {'first': 2, 'ts': 4, 'duration': 4, 'discontinuity_indicator': None},
            ]
        }]
    }

# Generated at 2022-06-14 15:22:56.406520
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    filename = get_testdata_file(u'hds1.bootstrap')
    with open(filename, 'rb') as f:
        info = FlvReader(f.read()).read_bootstrap_info()
    assert info['segments'] == [{'segment_run': [(0, 11)]}]

# Generated at 2022-06-14 15:23:02.039628
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:23:07.448561
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    f4m_fd = F4mFD()
    f4m_fd.real_download(None,
        {
            'url': 'http://example.com/manifest.f4m',
            'fragment_index': 1,
            'complete_frags_downloaded_bytes': 1,
            'filename': '/tmp/output.flv',
        }
    )

# Generated at 2022-06-14 15:23:12.509412
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    flv = FlvReader(b'\x00\x01\x00\x00\x00\x08abcd\x00\x04abcd\x00')
    flv.seek(6)
    assert flv.read_string() == b'abcd'
    assert flv.read_string() == b'abcd'
    assert flv.tell() == 23

# Generated at 2022-06-14 15:23:23.962150
# Unit test for function build_fragments_list
def test_build_fragments_list():
    boot_info = {
        'segments': [
            {'segment_run': [(1, 1), (2, 2)]}
        ],
        'fragments': [
            {'fragments': [
                {'first': 0, 'ts': 0, 'duration': 0, 'discontinuity_indicator': None},
                {'first': 1, 'ts': 1000, 'duration': 2000, 'discontinuity_indicator': None},
                {'first': 2, 'ts': 3000, 'duration': 4000, 'discontinuity_indicator': None},
                {'first': 4, 'ts': 7000, 'duration': 8000, 'discontinuity_indicator': None},
            ]}
        ],
        'live': False,
    }

# Generated at 2022-06-14 15:23:33.632812
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from io import BytesIO
    fd = F4mFD()
    with open('./test-data/f4m/test_404.txt', 'r') as f:
        manifest = f.read()
    dest_stream = BytesIO()
    # We must replace the download method with a mock method
    old_download = fd.download
    fd.download = lambda *args: args[0].write(manifest)
    res = fd.real_download('./test.flv', {'url': 'http://test.com/test.f4m'}, 0)
    fd.download = old_download
    assert res

# Generated at 2022-06-14 15:23:45.469424
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:23:52.859245
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x00\x19\x61\x73\x72\x74\x01\x00\x00\x00\x62\x30\x30\x30\x39\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x02'
    reader = FlvReader(data)
    assert reader.read_asrt() == {
        'segment_run': [
            (1, 1),
            (2, 1),
        ],
    }

# Generated at 2022-06-14 15:24:03.486618
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:24:35.139799
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:24:44.038941
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:24:48.775015
# Unit test for function write_flv_header
def test_write_flv_header():
    stream = io.BytesIO()
    write_flv_header(stream)
    assert stream.getvalue() == (
        b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')


# Generated at 2022-06-14 15:24:57.153790
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:05.139317
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .fragment_mp4 import (
        _read_samples_as_moof_fragment,
    )

# Generated at 2022-06-14 15:25:10.158429
# Unit test for function write_flv_header
def test_write_flv_header():
    from io import BytesIO as StringIO
    stream = StringIO()
    write_flv_header(stream)
    assert stream.getvalue() == b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'



# Generated at 2022-06-14 15:25:15.474020
# Unit test for function write_metadata_tag

# Generated at 2022-06-14 15:25:24.460661
# Unit test for method real_download of class F4mFD

# Generated at 2022-06-14 15:25:33.414261
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:25:37.482653
# Unit test for function write_flv_header
def test_write_flv_header():
    import io
    stream = io.BytesIO()
    write_flv_header(stream)
    assert stream.getvalue() == (b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00')



# Generated at 2022-06-14 15:26:06.323700
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    data = io.BytesIO(b'abcd\x00')
    v = FlvReader(data).read_string()
    assert v == b'abcd'
    data = b'\x06abcd\x00efg'
    v = FlvReader(io.BytesIO(data)).read_string()
    assert v == b'abcd', v
    data = b'\x07abcdefg\x00'
    v = FlvReader(io.BytesIO(data)).read_string()
    assert v == b'abcdefg', v
    data = b'\x06abcdefg'
    try:
        v = FlvReader(io.BytesIO(data)).read_string()
        raise ValueError('Should not pass')
    except DataTruncatedError:
        pass



# Generated at 2022-06-14 15:26:14.182877
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    metadata = 'metadata'
    stream = io.BytesIO()
    write_metadata_tag(stream, metadata)
    stream.seek(0)
    data = stream.read()
    # Check that tag header is written
    assert data[0:11] == b'\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    # Check that metadata is written after tag header
    assert data[11:] == bytearray(metadata, 'ascii')



# Generated at 2022-06-14 15:26:26.278077
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:26:36.892778
# Unit test for function build_fragments_list
def test_build_fragments_list():
    #
    # Test for non-live HDS streams
    #
    # live == False
    assert build_fragments_list({
        'live': False,
        'segments': [
            {'segment_run': [(0, 1), (1, 4)]}
        ],
        'fragments': [
            {'fragments': [
                {'first': 1, 'ts': 1000},
                {'first': 5, 'ts': 2000},
                {'first': 9, 'ts': 3000}
            ]}
        ]
    }) == [(0, 1), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9)]
    #
    # Test for live HDS streams
    #
    # live == True
    # the number of fragments is less than expected

# Generated at 2022-06-14 15:26:46.259888
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:26:58.067781
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    fragment_count = 2
    box_length = 22 + 6*fragment_count
    box_data = compat_struct_pack('!BBBBIBHH',
        0, 0, 0, 0,  # version and flags
        1,  # time scale
        0,  # QualitySegmentUrlModifiers
        fragment_count,
        3, 6,  # fragments
        10, 15,  # fragments
    )
    assert box_length == len(box_data)

# Generated at 2022-06-14 15:27:07.152316
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:13.801188
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    data = compat_b64decode(b'''
    AAUAAb4BoKZwa4n2240WG9pIXvSj1eJnCd+z2wgQMvEJ2QhZ64l5g5I5X5gyBqG7AdyEjAr8V7f
    2h5QQMjOi8B7xXrwgyIqUA7mOgjG8fOtIoBPt4/4BD4o/0/0DgX9v/AcSvv/4BdCg+/wH/vf+D/
    3//AfoDgP9/v8D/f+AAT/AwL/wB6Fv/3/gHpIHcAAA==
    ''')
    result = Flv

# Generated at 2022-06-14 15:27:22.089912
# Unit test for function build_fragments_list
def test_build_fragments_list():
    bootstrap_info = read_bootstrap_info(COMMON_BOOTSTRAP_BYTES)
    assert build_fragments_list(bootstrap_info) == COMMON_FRAGMENTS_LIST

    bootstrap_info = read_bootstrap_info(LIVE_BOOTSTRAP_BYTES)
    assert build_fragments_list(bootstrap_info) == LIVE_FRAGMENTS_LIST

    bootstrap_info = read_bootstrap_info(LIVE_BOOTSTRAP_1_BYTES)
    assert build_fragments_list(bootstrap_info) == LIVE_FRAGMENTS_1_LIST



# Generated at 2022-06-14 15:27:30.922858
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    def test_helper(flv_reader, expected_result):
        assert flv_reader.read_box_info() == expected_result
    test_helper(FlvReader(b'\x00\x00\x00\x11' + b'abst' + b'a' * 21), (
        17, b'abst', b'a' * 17))
    test_helper(FlvReader(b'\x00\x00\x00\x01' + b'abst' + b'\x00' * 8 + b'a' * 9), (
        18, b'abst', b'\x00' * 8 + b'a' * 9))



# Generated at 2022-06-14 15:27:55.585954
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    """Unit test for method real_download of class F4mFD"""
    import sys
    import tempfile
    from nose.tools import assert_true
    from youtube_dl.utils import urlopen
    from youtube_dl.downloader.f4m import (
        get_base_url, read_bootstrap_info, build_fragments_list,
        remove_encrypted_media)
    from youtube_dl.downloader.http import HttpFD
    from youtube_dl.extractor.common import InfoExtractor

    ie = InfoExtractor('http://foo.com')
    ie.fd = HttpFD()
    ie.fd.add_info_extractor(ie)

    def get_f4m_doc(f4m_url):
        f4m_webpage = urlopen(f4m_url).read()


# Generated at 2022-06-14 15:28:03.641554
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    flv = FlvReader(compat_b64decode('''
AAAA
wAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
AAAA
'''))
    asrt = flv.read_asrt()
    assert asrt == {
        'segment_run': [
            (0, 0),
        ],
    }

# Generated at 2022-06-14 15:28:14.102791
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from .test_fragment import f4m_bootstrap_info
    data = compat_b64decode(f4m_bootstrap_info)

# Generated at 2022-06-14 15:28:18.668719
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import youtube_dl.YoutubeDL
    ydl = youtube_dl.YoutubeDL({
        'writesubtitles': False, 'skip_download': False, 'quiet': True,
        'simulate': True, 'outtmpl': '/dev/null', 'format': 'best',
        'format_limit': None, 'nooverwrites': False})
    f4mfd = F4mFD(ydl)
    try:
        f4mfd.real_download('test.f4m', {
            'url': 'http://playertest.longtailvideo.com/adaptive/bipbop/gear4/prog_index.m3u8'})
    except youtube_dl.utils.DownloadError:
        pass

# Generated at 2022-06-14 15:28:23.988595
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:28:33.878762
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:28:43.261841
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:28:55.151965
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import json
    import tempfile

    # Load unittest configuration file
    f = open('unittest_config.json')
    unittest_config = json.load(f)
    f.close()

    # Create temporary files and folders to store the test output and the expected results
    temp_folder = tempfile.mkdtemp()
    temp_filename = os.path.join(temp_folder, 'download_test.flv')

    # Download the manifest file
    manifest_url = unittest_config['f4m_manifest_akamai']['url']['template']
    manifest_url = manifest_url.replace('{mediaPrefix}', unittest_config['f4m_manifest_akamai']['url']['mediaPrefix'])

# Generated at 2022-06-14 15:29:03.910841
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    from io import BytesIO
    stream = BytesIO()


# Generated at 2022-06-14 15:29:14.764132
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:29:34.442668
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:29:42.250622
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import sys
    import os

    test_case_number = 0

    def _test_F4mFD_real_download(test_cases, real_download_test_case_number, 
        expected_download_url, expected_mp4_file_name):
        global test_case_number

        test_case_number += 1

        if real_download_test_case_number == 0 or  \
           real_download_test_case_number == test_case_number:
            print("\n\n")
            print("test case %d..." % test_case_number)

            fd = F4mFD()
            if hasattr(sys, "pypy_version_info"):
                test_case_config = test_cases.test_case_1_PyPy

# Generated at 2022-06-14 15:29:49.874894
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    flv_reader = FlvReader(b'F\x00\x00\x00@\x00\x02\x00<as\x00\x00\x00\x06\x01)\x99\x99\x99\x99\x99\x9a\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01')

# Generated at 2022-06-14 15:29:53.556318
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import sys
    test_data = open(sys.argv[1], 'rb').read()
    bootstrap_info = FlvReader(test_data).read_bootstrap_info()
    print(bootstrap_info)



# Generated at 2022-06-14 15:30:01.455466
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Testing for real_download of class F4mFD
    from youtube_dl.extractor import YoutubeIE
    from youtube_dl.utils import ExtractorError
    from .test_utils import FakeYDL
    ydl = FakeYDL()
    ydl.params['debug_printtraffic'] = True
    ydl.params['noprogress'] = True
    ydl.params['quiet'] = True
    ydl.params['skip_download'] = True
    ie = YoutubeIE(ydl)
    ie.url = 'https://www.youtube.com/watch?v=PAeX8jKPnTQ'
    ie._real_initialize()
    info_dict = ie.extract(ie.url)
    fd = F4mFD(ydl, ie, info_dict)

# Generated at 2022-06-14 15:30:12.094044
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    flv = open(os.path.join('test', 'fixtures', 'bootstrap_info.data'), 'rb').read()
    reader = FlvReader(flv)
    res = reader.read_bootstrap_info()

# Generated at 2022-06-14 15:30:23.617888
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:30:33.601825
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    assert FlvReader(b'\x04\x66\x6f\x6f\x00\x03\x62\x61\x72\x00').read_string() == b'foo'
    assert FlvReader(b'\x03\x66\x6f\x6f\x00\x03\x62\x61\x72\x00').read_string() == b'foo'
    assert FlvReader(b'\x02\x66\x6f\x00\x03\x62\x61\x72\x00').read_string() == b'fo'
    assert FlvReader(b'\x01\x66\x00\x03\x62\x61\x72\x00').read_string() == b'f'

# Generated at 2022-06-14 15:30:44.352424
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    def get_abst(string):
        return FlvReader(string).read_bootstrap_info()

# Generated at 2022-06-14 15:30:51.453082
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    flv_file = open("test.flv",'r+b')
    f_data = flv_file.read()
    flv_reader = FlvReader(f_data)
    bootstrap_info = flv_reader.read_bootstrap_info()
    print("bootstrap_info:",bootstrap_info)
    f_data = flv_file.read()
    print("f_data:",f_data)

test_FlvReader_read_bootstrap_info()


# Generated at 2022-06-14 15:31:26.825307
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    url = 'http://example.com/test.f4m'
    ydl = YoutubeDL('/tmp')
    ydl.params['test'] = True
    fd = F4mFD(ydl, url, {'noplaylist': True, 'url': url})

    def urlopen(url):
        if url == 'http://example.com/test.f4m':
            return io.BytesIO('<manifest><media url="http://example.com/test.f4m" /></manifest>'.encode('utf-8'))
        elif url == 'http://example.com/test.f4m/Seg0-Frag0':
            return io.BytesIO(b'mdatfragment')
        else:
            raise ValueError('unexpected url: ' + repr(url))


# Generated at 2022-06-14 15:31:38.573070
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:31:46.355756
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    metadata = b'\x01\x02\x03\x04'
    stream = io.BytesIO()
    write_metadata_tag(stream, metadata)
    assert stream.getvalue() == (
        to_bytes(b'\x12\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00') + metadata +
        to_bytes(b'\x00\x00\x00\x10'))



# Generated at 2022-06-14 15:31:58.181936
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:32:05.827902
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    url = 'http://download.tsi.telecom-paristech.fr/gpac/DASH_CONFORMANCE/TelecomParisTech/mp4-main-multi-mpd-AV-NBS.mpd'
    ydl = YoutubeDL({})

# Generated at 2022-06-14 15:32:16.473028
# Unit test for method read_abst of class FlvReader