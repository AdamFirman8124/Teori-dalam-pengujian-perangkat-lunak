

# Generated at 2022-06-14 15:23:18.400805
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:23:23.601113
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    f = FlvReader(b'\x00\x00\x00\x04test\x00\x00\x00\x04\x00\x00\x00\x00')
    assert f.read_string() == b'test'
    assert f.read_string() == b''



# Generated at 2022-06-14 15:23:34.953167
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:23:46.686999
# Unit test for function get_base_url
def test_get_base_url():
    manifest = '''<?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns="http://ns.adobe.com/f4m/1.0">
        <baseURL>http://example.com/</baseURL>
    </manifest>'''
    assert get_base_url(manifest) == 'http://example.com/'
    manifest = '''<?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns="http://ns.adobe.com/f4m/1.0">
        <baseURL>
            http://example.com/
        </baseURL>
    </manifest>'''
    assert get_base_url(manifest) == 'http://example.com/'

# Generated at 2022-06-14 15:23:55.819874
# Unit test for function get_base_url

# Generated at 2022-06-14 15:23:58.589247
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    test_str = b'test string\x00123'
    f = FlvReader(test_str)
    assert f.read_string() == b'test string'



# Generated at 2022-06-14 15:24:10.151433
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:24:21.236794
# Unit test for function get_base_url
def test_get_base_url():
    assert get_base_url(compat_etree_fromstring('<manifest/>')) is None
    assert get_base_url(compat_etree_fromstring('<manifest><baseURL>url</baseURL></manifest>')) == 'url'
    assert get_base_url(compat_etree_fromstring('<manifest><foo>bar</foo></manifest>')) is None
    assert get_base_url(compat_etree_fromstring('<manifest><baseURL/></manifest>')) == ''
    assert get_base_url(compat_etree_fromstring('<manifest><baseURL>url</baseURL><baseURL>bar</baseURL></manifest>')) == 'url'



# Generated at 2022-06-14 15:24:30.771120
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    test_input_list = [
        {
            'media': [
                {
                    'attrib': {'drmAdditionalHeaderId': 'test'}
                }
            ],
            'expected': []
        },
        {
            'media': [
                {
                    'attrib': {}
                }
            ],
            'expected': [{'attrib': {}}]
        }
    ]

# Generated at 2022-06-14 15:24:34.179718
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    data = b'ab\x00de\x00'
    s = FlvReader(data)
    assert s.read_string() == b'ab'
    assert s.read_string() == b'de'
    assert s.read_string() == b''



# Generated at 2022-06-14 15:25:05.086717
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    import xml.etree.ElementTree as ET

# Generated at 2022-06-14 15:25:16.569633
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    """
    The test case is provided by the pyamf project:
    https://github.com/hydralabs/pyamf/tree/master/tests/util/f4f
    """

# Generated at 2022-06-14 15:25:27.885276
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    from .common import test_data_file
    with open(test_data_file('bootstrap_info.flv'), 'rb') as f:
        bootstrap_info = FlvReader(f.read()).read_bootstrap_info()
        assert len(bootstrap_info['segments']) == 2
        assert len(bootstrap_info['fragments']) == 2
        assert bootstrap_info['live'] == False
        assert bootstrap_info['segments'][0]['segment_run'] == [(0, 2)]
        assert bootstrap_info['segments'][1]['segment_run'] == [(2, 1)]
        assert bootstrap_info['fragments'][0]['fragments'][0]['first'] == 0

# Generated at 2022-06-14 15:25:37.196958
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:25:41.949915
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    # add fixed duration
    test_xml = '''<manifest>
        <media duration="12000" bootstrapInfoId="bootstrap1" />
        <media duration="12000" bootstrapInfoId="bootstrap2" />
        <media duration="12000" bootstrapInfoId="bootstrap1">
            <attribute name="drmAdditionalHeaderId" value="header1" />
        </media>
        <media duration="12000" bootstrapInfoId="bootstrap1" />
        <media duration="12000" bootstrapInfoId="bootstrap2">
            <attribute name="drmAdditionalHeaderId" value="header1" />
        </media>
        <media duration="12000" bootstrapInfoId="bootstrap1" />
    </manifest>'''
    root = compat_etree_fromstring(test_xml)
   

# Generated at 2022-06-14 15:25:51.305118
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:58.450982
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    data = b'\x00\x06\x6c\x6f\x6e\x67\x00\x02\x69\x64\x00\x00\x00\x00'
    f = FlvReader(data)
    s = f.read_string()
    assert s == b'long', 'Test case 1 failed'
    s = f.read_string()
    assert s == b'id', 'Test case 2 failed'
    return 'Test read_string() passed.'


# Generated at 2022-06-14 15:26:07.820956
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import unittest
    class F4mFD_real_download(unittest.TestCase):
        def setUp(self):
            self.fd = F4mFD({'url': 'http://link.com/video.f4m', 'params': {'test': True}, 'noprogress': True})
            self.fd.real_download = lambda x, y: True
        def test_ok(self):
            self.assertEqual(self.fd.real_download('file.flv', {'url': 'http://link.com/video.f4m', 'params': {'test': True}, 'noprogress': True}), True)
    unittest.main()



# Generated at 2022-06-14 15:26:17.824031
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:26:25.209015
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    from xml.etree import ElementTree as ET

# Generated at 2022-06-14 15:27:01.084517
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import sys
    from . import FileDownloader
    ydl = FileDownloader({'outtmpl': '%(id)s.%(ext)s'})
    ydl.add_info_extractor({'ie_key':'Sites', 'ie':'F4mFD'})
    res = ydl.download([sys.argv[1]])
    print (res)


# Generated at 2022-06-14 15:27:09.249942
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:18.466406
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    test_metadata = b'test'
    stream = io.BytesIO()
    write_metadata_tag(stream, test_metadata)
    expected_stream_content = (
        b'\x12\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00' +
        test_metadata + b'\x00\x00\x00\x1a')
    assert stream.getvalue() == expected_stream_content



# Generated at 2022-06-14 15:27:28.344429
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    # Test for a sample response of method read_afrt of class FlvReader
    data = b'\x00\x00\x00\x30\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x02'
    res = FlvReader(data).read_afrt()

# Generated at 2022-06-14 15:27:36.311510
# Unit test for function get_base_url
def test_get_base_url():
    assert get_base_url(
        compat_etree_fromstring(
            '<manifest xmlns="http://ns.adobe.com/f4m/1.0"></manifest>')) == \
        None
    assert get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
        '<baseURL>http://example.com/</baseURL>'
        '</manifest>')) == 'http://example.com/'

# Generated at 2022-06-14 15:27:42.507668
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    data = compat_struct_pack('!II', 17, 0x61727473) + b'test\x00'
    f = FlvReader(data)
    assert f.read_unsigned_int() == 17
    assert f.read_unsigned_int() == 0x61727473
    assert f.read_string() == b'test'



# Generated at 2022-06-14 15:27:46.833488
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from .common import file_bytes
    # It's a valid bootstrap info
    flv_reader = FlvReader(file_bytes('bootstrap_sample.abst'))
    bootstrap_info = flv_reader.read_bootstrap_info()


# Generated at 2022-06-14 15:27:54.985968
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:28:00.136079
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    # An empty string
    box_data = b'\x00'
    assert FlvReader(box_data).read_string() == b''

    # A string
    box_data = b'abc\x00'
    assert FlvReader(box_data).read_string() == b'abc'


# Generated at 2022-06-14 15:28:08.147097
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    with open('tests/test.bootstrap', 'rb') as f:
        bootstrap = FlvReader(f.read()).read_bootstrap_info()

# Generated at 2022-06-14 15:28:33.565369
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    fr = FlvReader(b'abc\x00abc\x00\x00')
    assert fr.read_string() == b'abc'
    assert fr.read_string() == b'abc'
    assert fr.read_string() == b''


# Generated at 2022-06-14 15:28:42.053261
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    # Data should be terminated with \x00
    reader = FlvReader(b'\x0b\x00\x00\x00abcd\x00')
    assert reader.read_string() == b'abcd'

    # \x00 not at the end of the data
    reader = FlvReader(b'\x0a\x00\x00\x00abc\x00d')
    assert reader.read_string() == b'abc'

    # Long string
    reader = FlvReader(b'\x0f\x00\x00\x00a' * 100 + b'\x00')
    assert reader.read_string() == b'a' * 100

    # Invalid string
    reader = FlvReader(b'\x0f\x00\x00\x00a' * 100)


# Generated at 2022-06-14 15:28:51.663658
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    read_string_test_data_a = ['\x00', '\x00\x00\x00',
                               '\x00\x00\x00\x00', '\x00\x00\x00\x00\x00', ]
    read_string_test_data_b = ['', '', '', '', ]
    for i in range(len(read_string_test_data_a)):
        obj = FlvReader(read_string_test_data_a[i])
        assert obj.read_string() == read_string_test_data_b[i]



# Generated at 2022-06-14 15:29:01.790714
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    def _test(data):
        reader = FlvReader(data)
        return reader.read_box_info()
    # Realistic test case

# Generated at 2022-06-14 15:29:13.387671
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:29:20.919001
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:31.508769
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:29:40.522064
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from io import BytesIO
    from io import StringIO
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl.utils import sanitize_open

    ydl = YoutubeDL({
        'outtmpl': '%(id)s.%(ext)s',
        'skip_download': True,
        'quiet': True,
        'simulate': True,
    })
    ydl.add_default_info_extractors()
    (info_dict, _) = ydl.extract_info(
        'http://example.com', download=False)
    # We can't use use test_DASH_real_download because of issue
    # https://github.com/ytdl-org/youtube-dl/issues/9214

# Generated at 2022-06-14 15:29:45.571407
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    data = 'ABC\x00haha\x00hoho\x00\x00\x00\x00\x00\x00\x00'
    stream = FlvReader(data)
    assert stream.read_string() == b'ABC'
    assert stream.read_string() == b'haha'
    assert stream.read_string() == b'hoho'
    assert stream.read_string() == b''



# Generated at 2022-06-14 15:29:52.135102
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    # The following bytes are extracted from the header of an FLV file
    # downloaded from an Akamai server.
    bootstrap_info_bytes = compat_b64decode(b'AAAAIAAAABYAAAAkc29tZV9rZXkAAQDZ2QAAAAZkZXNjAAAAf8AAAAAEAAEAAABpAAAAAZm9vYmFyAAABn5/5A/w==')
    assert len(bootstrap_info_bytes) == 97
    bootstrap_info = FlvReader(bootstrap_info_bytes).read_bootstrap_info()