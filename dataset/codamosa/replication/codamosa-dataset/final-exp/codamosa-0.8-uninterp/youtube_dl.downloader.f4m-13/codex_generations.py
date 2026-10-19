

# Generated at 2022-06-14 15:22:56.248556
# Unit test for function get_base_url
def test_get_base_url():
    assert '' == get_base_url(compat_etree_fromstring('''
        <manifest xmlns="http://ns.adobe.com/f4m/1.0"/>
    '''))
    assert 'http://media.example.com/base/url' == get_base_url(compat_etree_fromstring('''
        <manifest xmlns="http://ns.adobe.com/f4m/1.0">
            <baseURL>http://media.example.com/base/url</baseURL>
        </manifest>
    '''))

# Generated at 2022-06-14 15:23:07.752167
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    box1_type = b'a'
    box1_data = b'b'
    box1_size = len(box1_type) + len(box1_data) + 8
    # Case 1: length is less than 0xFFFFFFFF
    assert FlvReader(
        compat_struct_pack(
            '!I', box1_size) + box1_type + box1_data).read_box_info() == (
                box1_size, box1_type, box1_data)
    # Case 2: length is greater than 0xFFFFFFFF
    assert FlvReader(
        compat_struct_pack(
            '!I', 1) + b'\x00' * 8 + compat_struct_pack(
            '!Q', box1_size) + box1_type + box1_data).read_box

# Generated at 2022-06-14 15:23:13.091061
# Unit test for function get_base_url
def test_get_base_url():
    xml_test_string = '''\
<manifest xmlns="http://ns.adobe.com/f4m/1.0">
  <baseURL>test base URL</baseURL>
</manifest>
'''
    manifest = compat_etree_fromstring(xml_test_string)
    assert get_base_url(manifest) == 'test base URL'
    xml_test_string = '''\
<manifest xmlns="http://ns.adobe.com/f4m/2.0">
  <baseURL>test base URL</baseURL>
</manifest>
'''
    manifest = compat_etree_fromstring(xml_test_string)
    assert get_base_url(manifest) == 'test base URL'

# Generated at 2022-06-14 15:23:20.895601
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:23:32.829267
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    """Unit test for method real_download of class F4mFD"""
    from .extractor import YoutubeDL
    from .utils import format_bytes
    from .compat import parse_qsl

    def _print_working_bitrate(ydl):
        """ Print bitrate of active F4mFD """
        if ydl.downloader.get_fd_func() == 'f4m':
            bitrate = ydl.downloader.activeFD.tbr
            infostr = '%s of %s at %s/s' % (
                format_bytes(ydl.downloaded_bytes),
                format_bytes(ydl.total_bytes),
                format_bytes(bitrate)
                )

# Generated at 2022-06-14 15:23:44.599787
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    # Simplest case, one quality level and one segment
    flv_reader = FlvReader(b'\x00\x00\x00\x19\x61\x73\x72\x74\x01\x00\x00\x00one\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01')
    assert flv_reader.read_asrt() == {
        'segment_run': [(1, 1)]}

    # Two segment runs in two quality levels

# Generated at 2022-06-14 15:23:54.942379
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    # Example of the "asrt" box
    # Box type: 'asrt'
    # Size: 0x00000012
    # --
    # Version: 0x01
    # Flags: 0x00 00 00
    # QualityEntryCount: 0x01
    # QualitySegmentUrlModifiers: 'mp4a'
    # SegmentRunEntryCount: 0x01
    # FirstSegment: 0x00000001
    # FragmentsPerSegment: 0x00000001
    asrt_data = compat_struct_pack(
        '!I4sB3sB5sI2I', 0x12, b'asrt', 1, b'\x00' * 3, 1,
        b'mp4a', 1, 1, 1)
    asrt = FlvReader(asrt_data).read_asrt()
   

# Generated at 2022-06-14 15:24:02.114809
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x01<\x06asrt\x00\x00\x00'\
           b'\x00\x00\x00\x01\x00\x04\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01'
    assert FlvReader(data).read_asrt() == {
        'segment_run': [(1, 1)],
    }


# Generated at 2022-06-14 15:24:13.353815
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:24:25.517427
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:02.519203
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:25:13.490638
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    from ..utils import encode_base_n

# Generated at 2022-06-14 15:25:21.792621
# Unit test for function build_fragments_list
def test_build_fragments_list():

    test_boot_info = {
      u'live': False,
      u'segments': [
          {u'segment_run': [(1, 2)]}],
      u'fragments': [
          {u'fragments': [
              {u'ts': 0, u'discontinuity_indicator': None, u'first': 1, u'duration': 0},
              {u'ts': 0, u'discontinuity_indicator': None, u'first': 2, u'duration': 0}]}]}

    test_result = [(1, 1), (1, 2)]

    assert test_result == build_fragments_list(test_boot_info)



# Generated at 2022-06-14 15:25:32.673239
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:43.406862
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:53.224913
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import unittest
    from base64 import b64decode

# Generated at 2022-06-14 15:26:01.905001
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:26:10.957046
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:26:20.453026
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:26:31.875078
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    import unittest
    import struct

    class FlvReaderTests(unittest.TestCase):
        def test_read_abst(self):
            data = """<D:propertyupdate xmlns:D="DAV:" xmlns:Z="http://ns.example.com/standards/z39.50/"><D:set><D:prop><Z:Authors><Z:Author>Jim Whitehead</Z:Author><Z:Author>Roy Fielding</Z:Author></Z:Authors></D:prop></D:set></D:propertyupdate>"""


# Generated at 2022-06-14 15:26:42.579522
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    return

# Generated at 2022-06-14 15:26:46.380342
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    ydl = YoutubeDL(YoutubeDL.params)
    f4mFD = F4mFD(ydl)
    assert f4mFD.real_download(filename, info_dict) == False

if __name__ == "__main__":
    test_F4mFD_real_download()

# Generated at 2022-06-14 15:26:55.477849
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .common import FakeFile
    from .common import read_f4f_manifest

    assert_info = lambda info: (len(info['segments']) == 1, len(info['fragments']))
    video_info = assert_info(read_f4f_manifest(FakeFile('test-abst.bin')))
    assert all(video_info), 'test_FlvReader_read_abst failed'
    print('test_FlvReader_read_abst success')

test_FlvReader_read_abst()


# Generated at 2022-06-14 15:27:05.194207
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:11.963846
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:22.352122
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    import os
    import sys
    import unittest
    
    class TestFlvReader(unittest.TestCase):
        def setUp(self):
            test_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'asf_bootstrap_info.bin')
            self.reader = FlvReader(open(test_file, 'rb').read())
            
        def test_FlvReader_read_abst(self):
            abst = self.reader.read_abst()
            self.assertIsInstance(abst, dict)
            self.assertEqual(abst['live'], False)
            self.assertEqual(len(abst['segments']), 4)

# Generated at 2022-06-14 15:27:32.305006
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import sys
    import re
    def myurlopener(self, req): 
        print('in myurlopener')
        class MyResponse:
            def read(self):
                print('in read')
                return b'data'
            def info(self): 
                print('in info')
                class MyHeaders:
                    def __init__(self, headers):
                        self.hdrs = headers
                    def getheaders(self, name):
                        print('in getheaders')
                        return self.hdrs.get(name)
                return MyHeaders({'Content-Type': 'video/f4m'})

        return MyResponse()
    # create the MockYdl object, which will pretend to be the YoutubeDL class.
    # Any method called on this object will simply print its name and arguments.

# Generated at 2022-06-14 15:27:38.534243
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:27:49.990776
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .test import _TEST_DATA_DIR
    from .common import determine_ext
    with open(_TEST_DATA_DIR + 'bootstrapinfo', 'rb') as f1:
        abst = FlvReader(f1.read()).read_bootstrap_info()
        assert abst['segments'][0]['segment_run'][0] == (1, 2)
        assert abst['segments'][0]['segment_run'][1] == (3, 4)
        assert abst['segments'][1]['segment_run'][0] == (5, 6)
        assert abst['fragments'][0]['fragments'][0]['first'] == 1
        assert abst['fragments'][0]['fragments'][0]['ts'] == 3

# Generated at 2022-06-14 15:28:02.346348
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:28:27.956418
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    if __name__ == '__main__':
        pass

# Generated at 2022-06-14 15:28:38.391083
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    # The following box data is copied from an actual bootstrap box
    # of a real video.
    abst_data = b'\x00\x00\x00\x19\x61\x62\x73\x74\x01\x00\x00\x00\x01' + \
                b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00' + \
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x61' + \
                b'\x73\x31\x00\x00\x00\x00\x00\x00' + \
                compat_

# Generated at 2022-06-14 15:28:50.249166
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:28:57.098315
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:29:04.536675
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from ..compat import compat_struct_pack
    from .common import file_bytes

    bootstrap_info = file_bytes('test/test_bootstrap_info.bin')
    reader = FlvReader(bootstrap_info)
    abst = reader.read_bootstrap_info()
    for i, segment in enumerate(abst['segments']):
        # segment_run_table, 1 segment with 3 sub segments
        if i == 0:
            assert segment['segment_run'] == [(0, 3)], segment
        elif i == 1:
            assert segment['segment_run'] == [(0, 1)], segment
        else:
            assert False, ("unexpected segment run table", abst)
    assert len(abst['fragments']) == 2, abst

# Generated at 2022-06-14 15:29:11.990214
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from .test_interop import get_test_cases
    for test_case in get_test_cases():
        if test_case.args.test_case_name == 'FlvReader.read_bootstrap_info':
            with open(test_case.input, 'rb') as in_f:
                data = in_f.read()
            bootstrap_info = FlvReader(data).read_bootstrap_info()
            assert bootstrap_info == test_case.expected_value



# Generated at 2022-06-14 15:29:20.132239
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    flv = b'\x00\x00\x00\x1A'\
          b'f4v \x00\x00\x00\x00'\
          b'\x00\x00\x00\x00\x00\x00\x00\x00'  # box size: 1, type: f4v
    fr = FlvReader(flv)
    fr.read_box_info()
    flv = b'\x00\x00\x00\x0D'\
          b'ftyp'\
          b'PIFF'  # box size: 13, type: ftyp
    fr = FlvReader(flv)
    fr.read_box_info()

# Generated at 2022-06-14 15:29:24.699105
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    reader = FlvReader(b'\x00' + b'abc\x00def')
    assert reader.read_string() == b'abc'
    reader.seek(0)
    assert reader.read_string() == b'def'



# Generated at 2022-06-14 15:29:33.893897
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    import unittest
    from xml.etree import cElementTree as ElementTree
    from .utils import remove_media_protocol


# Generated at 2022-06-14 15:29:39.417519
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    f = io.BytesIO(b'\x10\x0f\x00\x00moov.abstl\x00\x00\x00\x00' + b'\x00' * 10)
    assert len(f.read(5)) == 5
    assert FlvReader(f).read_box_info() == (15, b'moov', b'.abstl\x00\x00\x00\x00' + b'\x00' * 10)



# Generated at 2022-06-14 15:30:57.989675
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    test_media = """<media>
    <metadata />
    <metadata attribute="value" />
    <metadata drmAdditionalHeaderId="value" />
    <metadata drmAdditionalHeaderSetId="value" />
    </media>"""
    assert len(remove_encrypted_media(compat_etree_fromstring(test_media))) == 2



# Generated at 2022-06-14 15:31:03.636597
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:31:15.497113
# Unit test for method read_box_info of class FlvReader

# Generated at 2022-06-14 15:31:25.276891
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    # The test data is an ASRT box generated by Adobe HDS Dumper.
    # The test data is in ASCII-HEX encoding, by converting it to binary.
    asrt_hex = """
00 00 00 5B
61 73 72 74
00 00 00 00
01
75
00 00 00 0A
00 00 00 05
00 00 02 02
01
00 00 00 0A
00 00 00 02
00 00 00 02
00 00 00 01
00 00 00 0A
00 00 00 05
00 00 00 01
00 00 00 01
"""
    asrt_binary = asrt_hex.strip().replace(' ', '').decode('hex')
    asrt_reader = FlvReader(asrt_binary)
    info = asrt_reader.read_asrt()

# Generated at 2022-06-14 15:31:37.319321
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    # In this test we assume the 'afrt' box is correctly read
    # by the method read_box_info
    box_data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    flv_reader = FlvReader(box_data)
    assert flv_reader.read_afrt() == {'fragments': []}


# Generated at 2022-06-14 15:31:48.815057
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:31:59.870110
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = (
        b'\x00\x00\x00\x19'
        b'\x61\x73\x72\x74'
        b'\x00\x00\x00\x01'
        b'\x00'
        b'\x00\x00\x00\x01'
        b'\x00\x00\x00\x00'
        b'\x00\x00\x00\x00'
        b'\x00\x00\x00\x00'
        b'\x00\x00\x00\x00'
    )
    expect = {
        'segment_run': [(0, 0)],
    }
    res = FlvReader(data).read_asrt()
    assert res == expect


# Generated at 2022-06-14 15:32:12.788738
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    example_asrt = (
        b'\x00\x00\x01+\x06\x06asrt\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'
        b'\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00'
        b'\x02\x00\x00\x00\x03\x00\x00\x00\x04'
    )
    parsed_example = FlvReader(example_asrt).read_asrt()