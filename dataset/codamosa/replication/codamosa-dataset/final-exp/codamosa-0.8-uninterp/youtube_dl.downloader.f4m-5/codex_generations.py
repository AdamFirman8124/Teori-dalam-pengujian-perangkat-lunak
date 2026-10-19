

# Generated at 2022-06-14 15:22:54.558291
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    string = b'\x00\x00\x00\xD8\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    for result in [FlvReader(string).read_afrt()]:
        print(result)



# Generated at 2022-06-14 15:23:06.962169
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # test case 1 (error: no media found)
    manifest = ''
    ydl_conf = {}
    ydl_conf['noprogress'] = True
    # manifest = manifest.decode('utf-8')
    ydl = YoutubeDL(ydl_conf)
    with pytest.raises(ExtractorError) as excinfo:
        f4mfd = F4mFD(ydl)
        f4mfd.real_download('', {'url': '', 'id': ''}, manifest)
    assert '[f4m] No media found' in str(excinfo.value)

    # test case 2 (error: missing id)

# Generated at 2022-06-14 15:23:16.064561
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    encrypted_media = '<Media fileId="1" isLive="true" initialization="1/init.f4v" keyUrl="1/key.bin" ' \
                      'mediaUrl="1/1.f4v" ' \
                      'drmAdditionalHeaderId="24" ' \
                      'drmAdditionalHeaderSetId="26"/>'
    unencrypted_media = '<Media fileId="1" isLive="true" initialization="1/init.f4v" keyUrl="1/key.bin" ' \
                        'mediaUrl="1/1.f4v"/>'
    test_media = remove_encrypted_media(
        compat_etree_fromstring(encrypted_media + unencrypted_media))
    assert len(test_media) == 1, 'Function remove_encrypted_media failed'



# Generated at 2022-06-14 15:23:27.134065
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    """
    Sample data from https://code.google.com/p/wami-recorder/source/browse/trunk/flash/test.flv?r=26
    """
    data = (b'\x00\x00\x00\x33\x61\x73\x72\x74\x01\x00\x00\x00'
            b'\x01\x61\x20\x00\x01\x02\x00\x00\x00\x01')
    flv_reader = FlvReader(data)
    res = flv_reader.read_asrt()
    assert res == {'segment_run': [(1, 2)]}



# Generated at 2022-06-14 15:23:37.813082
# Unit test for function get_base_url
def test_get_base_url():
    base_url = get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0"></manifest>'
    ))
    assert base_url is None

    base_url = get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/2.0"></manifest>'
    ))
    assert base_url is None

    base_url = get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
        '    <baseURL>http://example.com/</baseURL>'
        '</manifest>'
    ))


# Generated at 2022-06-14 15:23:49.463684
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    stream = io.BytesIO()
    metadata = b'"duration":0.0,"width":0,"height":0,"videodatarate":0.0,"framerate":0.0,"videocodecid":4,' \
               b'"audiodatarate":0.0,"audiosamplerate":44100.0,"audiosamplesize":16.0,' \
               b'"stereo":true,"audiocodecid":10,"filesize":0'
    write_metadata_tag(stream, metadata)
    stream.flush()

# Generated at 2022-06-14 15:23:57.558789
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = (
        b'\x00\x00\x00\x18'  # size
        b'asrt'  # box type
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x01'  # quality_entry_count
        b'\x00\x00\x00\x01'  # segment_run_count
        b'\x00\x00\x00\x00'  # first_segment
        b'\x00\x00\x00\x02'  # fragments_per_segment
    )
    res = FlvReader(data).read_asrt()

# Generated at 2022-06-14 15:24:07.058931
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    FlvReader('\x00\x00\x00\x10\x66\x74\x79\x70\x61\x73\x73\x74').read_box_info()
    FlvReader('\x00\x00\x00\x00\x66\x74\x79\x70\x61\x73\x73\x74').read_box_info()
    FlvReader('\x00\x00\x00\x01\x00\x66\x74\x79\x70\x61\x73\x73\x74').read_box_info()



# Generated at 2022-06-14 15:24:15.851791
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    test_data = b'\x00\x00\x04\xFA\x66\x74\x79\x70\x00\x00\x02\x00\x00\x00\x00'
    test_bytes = FlvReader(test_data)
    assert test_bytes.read_box_info() == (4, b'ftyp', b'\x00\x00\x02\x00')
    assert test_bytes.read_box_info() == (1024, b'\x00\x00\x00\x00', b'\x00' * 1020)
    return True
assert test_FlvReader_read_box_info()



# Generated at 2022-06-14 15:24:18.779074
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    with io.open('test.abst', 'rb') as f:
        data = f.read()
    print(FlvReader(data).read_bootstrap_info())



# Generated at 2022-06-14 15:24:56.610240
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:25:04.763476
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:25:16.030377
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    data = (
        b'\x00\x00\x00\x20'
        b'abst'
        b'\x00\x00\x00\x00'
    )
    info = FlvReader(data).read_box_info()
    assert info[0] == 0x20
    assert info[1] == b'abst'
    assert info[2] == b'\x00\x00\x00\x00'

    data = (
        b'\x00\x00\x00\x28'
        b'abst'
        b'\x00\x00\x00\x01'
        b'\x00\x00\x00\x01\x00\x00\x00\x01'
    )

# Generated at 2022-06-14 15:25:24.774776
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:34.384590
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:25:45.165100
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:54.075742
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:26:02.811073
# Unit test for function build_fragments_list
def test_build_fragments_list():
    # Simple test for non-live video
    test_data = b'AQAAAAAAAgAAAAAAAAAQAAAAAAAAAEAQAABQAAAADAAQAAAAAAAAA='
    boot_info = read_bootstrap_info(compat_b64decode(test_data))
    assert build_fragments_list(boot_info) == [
        (0, 1),
        (0, 2),
    ]

    # Simple test for live video
    test_data = b'AQAAAAAAAgAAAAAAAAAQAAAAAAAAAEAQAABQAAAADAAQAAABAAAAAAAAAAQAABQAAAADAAQAAAAEAAAAAAAAAQAABQAAAADAAQAAAAAAAAACAAAAAAAAAQAAAAAAAAAAAAAAAADAAQAAAAAAAAAAAAAAAwABABAAAABoAAABsAAAAAAAAAAAA='

# Generated at 2022-06-14 15:26:14.666351
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:26:23.157320
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:27:07.269625
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:27:10.417191
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    with io.open('tests/testdata/f4m/tears-of-steel-test-manifest.abst', 'rb') as f:
        bootstrap_info = FlvReader(f.read()).read_bootstrap_info()
        assert bootstrap_info['segments']
        assert bootstrap_info['fragments']



# Generated at 2022-06-14 15:27:16.008191
# Unit test for function build_fragments_list
def test_build_fragments_list():
    bootstrap_info = {
        'live': False,
        'segments': [
            {
                'segment_run': [
                    (0, 2),
                    (2, 3)
                ]
            }
        ],
        'fragments': [
            {
                'fragments': [
                    {
                        'first': 1,
                        'ts': 5000,
                        'duration': 5,
                        'discontinuity_indicator': None,
                    }, {
                        'first': 2,
                        'ts': 10000,
                        'duration': 6,
                        'discontinuity_indicator': None,
                    }
                ]
            }
        ]
    }

# Generated at 2022-06-14 15:27:25.911614
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    # box_type: free
    data = io.BytesIO(b''.join([compat_struct_pack('!I', 8), b'free', b'\x01\x02\x03\x04']))
    box_info = FlvReader(data).read_box_info()
    assert box_info == (8, b'free', b'\x01\x02\x03\x04')
    # box_type: mdat
    data = io.BytesIO(b''.join([compat_struct_pack('!I', 9), b'mdat', b'\x01\x02\x03\x04\x05']))
    box_info = FlvReader(data).read_box_info()

# Generated at 2022-06-14 15:27:34.674692
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:46.882113
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:27:52.272668
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    ydl = FakeYdl()
    info_dict = {'url': 'f4m_manifest_url',
                 'downloader_options': {'test': False},
                 'http_headers': {},
                 'protocol': 'f4m'}
    f4mFD = F4mFD(ydl, info_dict)
    filename = 'filename'
    f4mFD.real_download(filename, info_dict)


# Generated at 2022-06-14 15:27:57.878622
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    from .common import read_fixture_data
    data = read_fixture_data('ASRT.bin')
    assert FlvReader(data).read_asrt() == {
        'segment_run': [
            (1, 2),
            (3, 1),
        ],
    }

# Generated at 2022-06-14 15:28:06.446156
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    sample = open('tests/samples/bootstrap_info.txt', 'rb').read()
    sample_dict = FlvReader(sample).read_bootstrap_info()
    assert sample_dict['segments'] == [{
        'segment_run': [(0, 2)],
    }]
    assert sample_dict['fragments'] == [{
        'fragments': [
            {
                'duration': 5,
                'first': 0,
                'ts': 0,
            },
            {
                'duration': 5,
                'first': 1,
                'ts': 0,
            }
        ]
    }]
    assert sample_dict['live'] is False

test_FlvReader_read_abst()



# Generated at 2022-06-14 15:28:09.964614
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    from .test_asrt import test_asrt_raw, expect_asrt
    test_asrt = FlvReader(test_asrt_raw)
    assert test_asrt.read_asrt() == expect_asrt


# Generated at 2022-06-14 15:28:42.973042
# Unit test for function build_fragments_list
def test_build_fragments_list():

    import json
    import os

    _TEST_DIR = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(_TEST_DIR, 'test_data', 'bootstrap_info.json')) as b_info_fh:
        boot_info = json.load(b_info_fh)


# Generated at 2022-06-14 15:28:49.098434
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    import binascii
    flv_reader = FlvReader(binascii.unhexlify(b'404142434445000000000000000000000000000000'))
    assert flv_reader.read_box_info() == (
        8, b'ABCD', b'\x00\x00\x00\x00\x00\x00\x00\x00')
    flv_reader = FlvReader(binascii.unhexlify(b'20123456000000001234000000'))
    assert flv_reader.read_box_info() == (
        0x1234, b'1234', b'\x00\x00\x00\x00')
    flv_reader = FlvReader(binascii.unhexlify(
        b'0000000000000000000000000000000000000000'))

# Generated at 2022-06-14 15:29:00.122554
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    def test_case(data, box_size, box_type, box_data):
        stream = FlvReader(data)
        res = stream.read_box_info()
        assert res == (box_size, box_type, box_data)
    # Normal case
    test_case(
        compat_struct_pack('!I4s4s', 16, b'type', b'data'),
        16, b'type', b'data')
    # Size is in 8 bytes
    test_case(
        compat_struct_pack('!I4sQ16s', 1, b'type', 16, b'data'),
        16, b'type', b'data')
    # Size is 0

# Generated at 2022-06-14 15:29:08.074413
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    reader_segment = FlvReader(open(
        'test/files/reader_segment.mp4', 'rb').read())
    box_info = reader_segment.read_box_info()
    assert box_info == (
        4, b'ftyp',
        b'isom'
        + b'iso2'
        + b'avc1'
        + b'free'
    )


# Generated at 2022-06-14 15:29:17.438957
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import unittest

# Generated at 2022-06-14 15:29:30.189377
# Unit test for function write_metadata_tag

# Generated at 2022-06-14 15:29:39.992824
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:29:48.461641
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    test_box_data = (
        b'\x01\x00\x00\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x01'  # QualityEntryCount
        b'\x07QualityLevels(1000\x00'
        b'\x00\x00\x00\x02'  # SegmentRunEntryCount
        b'\x00\x00\x00\x11'  # first segmenet
        b'\x00\x00\x00\x02'  # FragmentsPerSegment
        b'\x00\x00\x00\x12'  # first segmenet
        b'\x00\x00\x00\x01'  # FragmentsPerSegment
    )
   

# Generated at 2022-06-14 15:29:56.340509
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    test_data = (
        (b'\x00\x00\x00\x2E\x61\x73\x72\x74\x01\x00\x00\x00\x31'
         b'\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x3C\x00'),
        {'segment_run': [(0, 60)]},
    )
    reader = FlvReader(test_data[0])
    assert reader.read_asrt() == test_data[1]



# Generated at 2022-06-14 15:30:08.596759
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:30:56.577866
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:31:07.019241
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Initializing class
    downloader = F4mFD()
    class ydl:
        def report_warning(self,msg):
            # Dummy report warning
            pass
    downloader.ydl = ydl()
    
    # Creating a dummy actual FD and dummy result
    class res:
        def __init__(self):
            self.result = None
    result = res()
    actualFD = F4mFD()
    class actual:
        def __init__(self):
            self.res = None
        def real_download(self,filename,info_dict):
            self.res = filename,info_dict
            return result.result
    actualFD.real_download = actual().real_download
    downloader.real_download = actualFD.real_download
    
    # Creating a dummy available FD and dummy result


# Generated at 2022-06-14 15:31:18.322907
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:31:27.158519
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import os
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    os.chdir(temp_dir.name)

    # Get video link
    video_url = 'https://www.youtube.com/watch?v=Vm-LX-XmA5I'
    ydl_opts = {}
    ydl = YoutubeDL(ydl_opts)
    video_info = ydl.extract_info(video_url, download=False)
    video_f4m_url = None
    for f in video_info['formats']:
        if f['format_id'] == '144+251':
            video_f4m_url = f['url']
    assert(video_f4m_url is not None)


# Generated at 2022-06-14 15:31:30.803618
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    with io.open('test/test.abst', 'rb') as f:
        abst_reader = FlvReader(f.read())
        print(abst_reader.read_abst())


# Generated at 2022-06-14 15:31:42.628992
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:31:52.096884
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from .common import (
        read_bootstrap_info
    )
    from .dash import (
        FLV_HEADER,
        FLV_EXTRA_DATA,
    )
    f = io.BytesIO(FLV_HEADER + FLV_EXTRA_DATA)
    info = read_bootstrap_info(f)
    assert info['live'] == False
    assert len(info['fragments']) == 1
    assert len(info['segments']) == 0
    assert info['segments'] == []
    assert info['fragments'][0]['ts'] == 0
    assert len(info['fragments'][0]['fragments']) == 17
    assert info['fragments'][0]['fragments'][0]['first'] == 0


# Generated at 2022-06-14 15:32:02.332869
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    """Ensure that FlvReader can read abst boxes correctly."""

# Generated at 2022-06-14 15:32:14.111493
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:32:18.554646
# Unit test for function build_fragments_list