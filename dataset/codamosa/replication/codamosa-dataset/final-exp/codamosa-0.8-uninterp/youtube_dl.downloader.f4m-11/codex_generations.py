

# Generated at 2022-06-14 15:23:29.929830
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:23:34.306596
# Unit test for function write_flv_header
def test_write_flv_header():
    stream = io.BytesIO()
    write_flv_header(stream)
    assert stream.getvalue() == b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'



# Generated at 2022-06-14 15:23:46.111748
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    box_data = (
        b'\x00\x00\x00\x00'
        b'\x00\x00\x00\x00'
        b'\x00\x00\x00\x00'
    )
    assert FlvReader(box_data).read_box_info() == (0, b'\x00' * 4, b'')
    box_data = (
        b'\x00\x00\x00\x00'
        b'\x00\x00\x00\x08'
        b'\x00\x00\x00\x00'
        b'\x00\x00\x00\x00'
    )

# Generated at 2022-06-14 15:23:55.390494
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    TEST_CASES = [
        ('<media />', '<media />'),
        ('<media><a/><b/><c/></media>', '<media><a/><b/><c/></media>'),
        ('<media><a/><b drmAdditionalHeaderId="12"/></media>', '<media><a/></media>'),
        ('<media><a drmAdditionalHeaderSetId="2"/></media>', '<media></media>'),
    ]
    for test_case, expected in TEST_CASES:
        assert remove_encrypted_media(compat_etree_fromstring(test_case)) == compat_etree_fromstring(expected)
        assert remove_encrypted_media(compat_etree_fromstring('<a>' + test_case + '</a>'))

# Generated at 2022-06-14 15:24:06.468558
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    import random
    def _test_FlvReader_read_afrt():
        class FakeReader(object):
            def __init__(self, data):
                self.data = data
                self.read_count = 0
            def read(self, n):
                if self.read_count >= len(self.data):
                    return b''
                res = self.data[self.read_count:self.read_count + n]
                self.read_count += n
                return res
            def read_unsigned_char(self):
                return self.read(1)[0]
            def read_unsigned_int(self):
                return compat_struct_unpack('I', self.read(4))[0]

# Generated at 2022-06-14 15:24:16.985967
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    stream = io.BytesIO()
    stream.write(compat_struct_pack('>I', 8))
    stream.write(b'asrt')
    stream.write(compat_struct_pack('>B', 1))
    # Flags
    stream.write(compat_struct_pack('>I', 0))
    # QualityEntryCount
    stream.write(compat_struct_pack('>I', 1))
    stream.write(compat_struct_pack('>B', 2))
    stream.write(compat_struct_pack('>B', 3))
    # SegmentRunTableCount
    stream.write(compat_struct_pack('>I', 2))
    # SegmentRunEntry
    stream.write(compat_struct_pack('>I', 4))

# Generated at 2022-06-14 15:24:27.929597
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:24:36.789851
# Unit test for function build_fragments_list
def test_build_fragments_list():
    from ..extractor.common import InfoExtractor
    from .. import downloader
    test_cmd = [
        sys.executable,
        '-m',
        'youtube_dl.extractor.common',
        '--print-fragments-list',
        'http://www.rai.tv/dl/RaiTV/programmi/media/ContentItem-e7ac3d78-9638-4b5a-a6a5-ca1ee0c7e0e1-tg1.html#p=0',
    ]

    # $ ../youtube_dl/__main__.py --print-fragments-list http://www.rai.tv/dl/RaiTV/programmi/media/ContentItem-e7ac3d78-9638-4b5a-a6a5-ca1

# Generated at 2022-06-14 15:24:44.227258
# Unit test for function get_base_url
def test_get_base_url():
    manifest = '''
<manifest xmlns="http://ns.adobe.com/f4m/1.0">
  <baseURL>http://example.com/path/123.456</baseURL>
</manifest>
'''
    assert get_base_url(manifest) == 'http://example.com/path/123.456'
    manifest = '''
<manifest xmlns="http://ns.adobe.com/f4m/2.0">
  <baseURL>http://example.com/path/123.456</baseURL>
</manifest>
'''
    assert get_base_url(manifest) == 'http://example.com/path/123.456'



# Generated at 2022-06-14 15:24:54.156984
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:26:14.581959
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import sys
    import logging

    logger = logging.getLogger(__name__)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.DEBUG)

    # The content of the test file is extracted from
    # http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8
    TEST_FILE='http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8'
    import urllib

    FLV_FILE_1 = 'http://devimages.apple.com/iphone/samples/bipbop/gear2/prog_index.m3u8'

# Generated at 2022-06-14 15:26:26.595805
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    reader = FlvReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bootstrapinfo.dat'), 'rb').read())
    bootstrap_info = reader.read_bootstrap_info()
    # expected values are taken from bootstrapinfo.xml
    assert bootstrap_info['live']
    assert len(bootstrap_info['segments']) == 1
    assert len(bootstrap_info['fragments']) == 2
    assert len(bootstrap_info['fragments'][0]['fragments']) == 11
    assert len(bootstrap_info['fragments'][1]['fragments']) == 5
    assert len(bootstrap_info['segments'][0]['segment_run']) == 1

# Generated at 2022-06-14 15:26:35.798448
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    fd = FlvReader(b'\x00\x00\x00\x0babcdabcdabcdabcd')
    total_size, box_type, box_data = fd.read_box_info()
    assert total_size == 11
    assert box_type == b'abcd'
    assert box_data == b'abcdabcdabcd'

    fd = FlvReader(b'\x00\x00\x00\x01\x00\x00\x00\x0babcdabcdabcdabcd')
    total_size, box_type, box_data = fd.read_box_info()
    assert total_size == 11
    assert box_type == b'abcd'
    assert box_data == b'abcdabcdabcd'



# Generated at 2022-06-14 15:26:45.514323
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    from xml.etree import ElementTree as ET
    media = ET.fromstring('''<media url="a" />''')
    assert remove_encrypted_media([media]) == [
        ET.fromstring('''<media url="a" />''')]
    media = ET.fromstring('''<media url="a" drmAdditionalHeaderId="b" />''')
    assert remove_encrypted_media([media]) == []
    media = ET.fromstring('''<media url="a" drmAdditionalHeaderSetId="b" />''')
    assert remove_encrypted_media([media]) == []
    media = ET.fromstring('''<media url="a" drmAdditionalHeaderId="b" drmAdditionalHeaderSetId="c" />''')
    assert remove_encrypted_media([media]) == []
    media

# Generated at 2022-06-14 15:26:50.674161
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    f = FlvReader(compat_struct_pack('!I4s7s10s', 13, b'Test', b'1234567', b'8901234567'))
    assert f.read_string() == b'Test'
    assert f.read_string() == b'1234567'
    assert f.read_string() == b'8901234567'



# Generated at 2022-06-14 15:27:02.157517
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:27:06.919368
# Unit test for constructor of class F4mFD
def test_F4mFD():
    from .extractor.common import InfoExtractor
    from .downloader.http import HttpFD
    from .compat import parse_qs

    ie = InfoExtractor('test')
    assert isinstance(ie.fd, HttpFD)
    ie = InfoExtractor('test', downloader=None)
    assert isinstance(ie.fd, F4mFD)


if __name__ == '__main__':
    test_F4mFD()

# Generated at 2022-06-14 15:27:09.190082
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    assert FlvReader(b'test\x00').read_string() == b'test'
    assert FlvReader(b'test').read_string() == b'test'



# Generated at 2022-06-14 15:27:14.490450
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    flv_reader = FlvReader(b'\x00\x00\x00\x1e\x61\x73\x72\x74\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00')
    asrt = flv_reader.read_asrt()
    assert(asrt['segment_run'] == [(0,2), (2,2)])
    print('test_FlvReader_read_asrt: ok')

test_FlvReader_read_asrt()

# Unit test

# Generated at 2022-06-14 15:27:23.403898
# Unit test for method read_box_info of class FlvReader

# Generated at 2022-06-14 15:28:06.568166
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:28:16.808421
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Initialize the class object to be tested
    fd = F4mFD({'url': 'http://example.com/a.f4m', 'fragment_index': 0, 'noprogress': True, 'test': True})
    # Call the method to be tested
    success = fd.real_download('/tmp/a.flv', {})
    # If downloading is successful, the test may continue
    if success:
        # Open the downloaded file and read its bytes
        with open('/tmp/a.f4m', 'rb') as f:
            content = f.read()
        # Remove the downloaded file
        os.remove('/tmp/a.f4m')
        # Check the contents of the file

# Generated at 2022-06-14 15:28:22.964663
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from .downloader import FileDownloader
    from .extractor import gen_extractors
    from .utils import (
        match_filter_func,
        setopt,
    )

    setopt('verbose', True)
    setopt('quiet', False)
    setopt('no_warnings', False)
    setopt('youtube_include_dash_manifest', 'manual')
    setopt('test', True)
    setopt('hls_use_mpegts', True)
    setopt('hls_prefer_native', False)

    ie = gen_extractors()['http://www.rtve.es/infantil/directo/']()
    # You can uncomment the below lines to run the unit test using your system's
    # ffmpeg and ffprobe.
    # ie.params['external_

# Generated at 2022-06-14 15:28:32.863527
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:28:39.602896
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:28:51.810879
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:01.882780
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:29:13.388704
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    media_ele1 = compat_etree_fromstring(
        '<media href="Seg1-Frag40" bitrate="1751" width="480" height="270" '
        'indexRange="590-3463" duration="2.90800" bootstrapInfoId="bootstrap0" '
        'drmAdditionalHeaderId="drmheader0"/>').getchildren()[0]
    media_ele2 = compat_etree_fromstring(
        '<media href="Seg1-Frag40" bitrate="1751" width="480" height="270" '
        'indexRange="590-3463" duration="2.90800" bootstrapInfoId="bootstrap0" '
        'drmAdditionalHeaderSetId="drmheader1"/>').getchildren()[0]

# Generated at 2022-06-14 15:29:20.016168
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = compat_struct_pack(
        '!BBBBIBBBBI',
        0, 1, 0, 0, 1, len(b'qualityLevels'), b'qualityLevels', 0, 0, 0, 1)
    data += compat_struct_pack('!I', 2)
    data += compat_struct_pack('!II', 0, 1)
    data += compat_struct_pack('!II', 1, 2)
    data += b'\x00'
    flv = FlvReader(data)
    assert flv.read_asrt() == {'segment_run': [(0, 1), (1, 2)]}

# Generated at 2022-06-14 15:29:31.265063
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:30:38.428861
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:30:48.779843
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    xml = '''
    <manifest xmlns="http://ns.adobe.com/f4m/1.0">
    <media id="1" url="http://first.com/file.mp4" bitrate="750000" />
        <media id="2" url="http://second.com/file.mp4" bitrate="3500000" />
        <media id="3" url="http://third.com/file.mp4" bitrate="600000" drmAdditionalHeaderId="12345" />
    </manifest>
    '''
    root = compat_etree_fromstring(xml)
    media = root.findall('./media')
    assert len(media) == 3
    media = remove_encrypted_media(media)
    assert len(media) == 2



# Generated at 2022-06-14 15:30:58.770138
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:31:09.706205
# Unit test for function get_base_url
def test_get_base_url():
    assert get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0"></manifest>')) is None

    assert get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
        '<baseURL>base</baseURL>'
        '</manifest>')) == 'base'

    assert get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/2.0">'
        '<baseURL>base</baseURL>'
        '</manifest>')) == 'base'



# Generated at 2022-06-14 15:31:13.965085
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    f4m_url = 'http://manifest.us.rtl.nl/rtlxl/net5/vod/2015/01/19/Zie_mij_niet_klagen.mp4/Zie_mij_niet_klagen.mp4.f4m'
    assert(F4mFD.can_download(f4m_url))

    f4m_file = F4mFD(params={'test': True})
    f4m_data = f4m_file.real_download('./test', {'url' : f4m_url})
    assert(f4m_data)

if __name__ == '__main__':
    import sys
    import os

    os.chdir('test')


# Generated at 2022-06-14 15:31:24.304758
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:31:36.068939
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    media = [
        '<media url="msg.mp4" bootstrapInfoId="bootstrap0" qualityLevelId="msg" bitrate="44000" width="720" height="576" type="video" codec="avc1.42c001" duration="1598.99" lang="und" drmAdditionalHeaderId="2" drmAdditionalHeaderSetId="1"/>',
        '<media url="msg.mp4" bootstrapInfoId="bootstrap0" qualityLevelId="msg" bitrate="44000" width="720" height="576" type="video" codec="avc1.42c001" duration="1598.99" lang="und" drmAdditionalHeaderId="2" drmAdditionalHeaderSetId="1"/>'
    ]
    result = remove_encrypted_media(media)
    assert result == []



# Generated at 2022-06-14 15:31:47.775206
# Unit test for function build_fragments_list
def test_build_fragments_list():
    boot_info = {
        'live': False,
        'fragments': [
            {
                'fragments': [
                    {
                        'duration': 100,
                        'discontinuity_indicator': None,
                        'first': 0,
                        'ts': 0,
                    },
                    {
                        'duration': 100,
                        'discontinuity_indicator': None,
                        'first': 1,
                        'ts': 100
                    },
                    {
                        'duration': 100,
                        'discontinuity_indicator': None,
                        'first': 2,
                        'ts': 200,
                    },
                ],
            },
        ],
        'segments': [
            {
                'segment_run': [
                    (0, 3),
                ],
            },
        ],
    }


# Generated at 2022-06-14 15:31:59.153838
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:32:11.064124
# Unit test for function build_fragments_list