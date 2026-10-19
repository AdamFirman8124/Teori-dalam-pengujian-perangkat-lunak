

# Generated at 2022-06-14 15:23:10.371528
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    """
    Unit test for method real_download of class F4mFD
    """
    # Test simple manifest

# Generated at 2022-06-14 15:23:20.730555
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    def _test(test_name, test, expected_result, expected_exc=None):
        print("Running test '{0}'".format(test_name))
        try:
            assert test == expected_result
            print("Test '{0}' successful".format(test_name))
        except AssertionError:
            print("Test '{0}' failed".format(test_name))
            print("Expected result:")
            print(expected_result)
            print("Actual result:")
            print(test)
            raise AssertionError("Test '{0}' failed".format(test_name))

# Generated at 2022-06-14 15:23:32.594825
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    media = compat_etree_fromstring("""
    <media>
        <metadata>
            ...
        </metadata>
        <metadata>
            ...
        </metadata>
        <encryptedMedia drmAdditionalHeaderId="0" drmAdditionalHeaderSetId="1">
            ...
        </encryptedMedia>
        <encryptedMedia drmAdditionalHeaderId="2" drmAdditionalHeaderSetId="2">
            ...
        </encryptedMedia>
        <encryptedMedia drmAdditionalHeaderId="2" drmAdditionalHeaderSetId="3">
            ...
        </encryptedMedia>
    </media>
    """)

# Generated at 2022-06-14 15:23:44.336712
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:23:54.166978
# Unit test for function get_base_url
def test_get_base_url():
    ns = {
        _add_ns('baseURL', 1): '',
        _add_ns('baseURL', 2): '',
        '': 'http://ns.adobe.com/f4m/',
    }
    manifest = compat_etree_fromstring('<manifest></manifest>',
                                       parser=compat_etree_XMLParser(ns_clean=False))
    manifest.attrib['xmlns'] = ns[_add_ns('', 1)]
    manifest.attrib[ns[_add_ns('', 1)] + 'baseURL'] = ''
    manifest.attrib[ns[_add_ns('', 2)] + 'baseURL'] = ''

    assert get_base_url(manifest) == ''

    manifest.attrib[_add_ns('baseURL', 1)] = 'test_1'
    manifest

# Generated at 2022-06-14 15:24:04.046421
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:24:14.815451
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:24:26.523854
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:24:36.020773
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x00P\x73\x72\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x2a\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\xff\xff\xff\xff'
    data = compat_b64decode(data)
    res = FlvReader(data).read_asrt()
    assert res == {
        'segment_run': [(1, 1), (1, 1)],
    }

# Unit

# Generated at 2022-06-14 15:24:42.474153
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    data = b'\x00\x06p\x00\x04\xc3\xb6\xc3\xa4\x00'
    result = FlvReader(data).read_string()
    assert result == b'p\xc3\xb6\xc3\xa4'
    try:
        FlvReader(b'p\xc3\xb6\xc3\xa4').read_string()
    except DataTruncatedError as e:
        assert 'FlvReader error' in str(e)



# Generated at 2022-06-14 15:25:36.755199
# Unit test for function get_base_url
def test_get_base_url():
    base_url = 'http://example.com/test.f4m'
    manifest_url = 'http://example.com/'
    manifest = compat_etree_fromstring(
        b'''<manifest xmlns="http://ns.adobe.com/f4m/1.0">
        <baseURL>''' + base_url.encode('utf-8')
          + b'''</baseURL>
        </manifest>''')
    assert get_base_url(manifest) == base_url

    manifest = compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0"/>')
    assert get_base_url(manifest) is None


# Generated at 2022-06-14 15:25:40.241047
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    test_data = b'\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x01'
    fr = FlvReader(test_data)
    assert fr.read_asrt() == {
            'segment_run': [
                (1, 3),
                (2, 1),
            ],
        }


# Generated at 2022-06-14 15:25:49.842060
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:52.826495
# Unit test for function get_base_url
def test_get_base_url():
    xml_base_url = """<?xml version="1.0" encoding="UTF-8"?>
    <manifest
        xmlns="http://ns.adobe.com/f4m/1.0">
        <baseURL>http://example.com/</baseURL>
    </manifest>
    """
    root = compat_etree_fromstring(xml_base_url)
    base_url = get_base_url(root)
    assert base_url == "http://example.com/"


# Generated at 2022-06-14 15:26:01.839720
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    abst = compat_b64decode('''
AAAABYAAAAcAAADM1rXcX0AAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
    ''')
    info = FlvReader(abst).read_abst()

# Generated at 2022-06-14 15:26:10.615810
# Unit test for function get_base_url
def test_get_base_url():
    manifest = compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0"></manifest>')
    assert get_base_url(manifest) is None
    manifest = compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0"><baseURL>url</baseURL></manifest>')
    assert get_base_url(manifest) == 'url'
    manifest = compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/2.0"><baseURL>url</baseURL></manifest>')
    assert get_base_url(manifest) == 'url'



# Generated at 2022-06-14 15:26:20.192754
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():

    def check_mock_download(self, filename, info_dict):
        assert filename == 'my_filename.f4m'
        assert info_dict == {'url': 'http://manifest.com/man.f4m', 'http_chunk_size': 1048576, 'tbr': 600}

    def mock_download(self, filename, info_dict):
        check_mock_download(self, filename, info_dict)

    F4mFD.download = mock_download


# Generated at 2022-06-14 15:26:31.625454
# Unit test for function get_base_url
def test_get_base_url():
    manifest_xml = b'''
        <manifest xmlns="http://ns.adobe.com/f4m/1.0">
            <baseURL>base_url</baseURL>
        </manifest>
        '''
    manifest = compat_etree_fromstring(manifest_xml)
    base_url = get_base_url(manifest)
    assert base_url == 'base_url'

    manifest_xml = b'''
        <manifest xmlns="http://ns.adobe.com/f4m/2.0">
            <baseURL>base_url_v2</baseURL>
        </manifest>
        '''
    manifest = compat_etree_fromstring(manifest_xml)
    base_url = get_base_url(manifest)

# Generated at 2022-06-14 15:26:37.131408
# Unit test for function get_base_url
def test_get_base_url():
    manifest = compat_etree_fromstring(b"""
    <manifest xmlns="http://ns.adobe.com/f4m/2.0">
    <baseURL>
        URL-1
    </baseURL>
    <media baseURL="URL-2" />
    </manifest>
    """)
    assert get_base_url(manifest) == 'URL-1'



# Generated at 2022-06-14 15:26:46.499465
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:21.781729
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    f = open("3%5E_F%2C+PN~0_2_2%5E0_1~0_1_F~0_1.abst")
    abst = FlvReader(f.read()).read_bootstrap_info()
    f.close()

# Generated at 2022-06-14 15:27:31.635351
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'bootstrap_info.dat')

# Generated at 2022-06-14 15:27:38.271752
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    pass
    # F4mFD_real_download()



# def _download_fragment(self, uri, info_dict):
#     range_header = {}
#     if self._total_bytes > 0:
#         range_header = {
#             'Range': 'bytes=%d-' % (self._total_bytes)
#         }
#     retries = 10
#     success = False
#     while retries > 0:
#         try:
#             urlh = self._request_webpage(uri, info_dict, range_header=range_header)
#             content_length = urlh.headers.get('Content-Length')
#             if content_length:
#                 length = int_or_none(content_length)
#             else:
#                 length = -1
#             down_

# Generated at 2022-06-14 15:27:49.865177
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:28:02.207421
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:28:11.636862
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = (
        b'\x00\x00\x00#'  # size
        b'asrt'  # type
        b'\x00'  # version
        b'\x00\x00\x00'  # flags
        b'\x05'  # QualityEntryCount
        b'\x00\x00\x00\x00\x00\x00\x00\x00' # segment run
    )
    asrt_data = FlvReader(data).read_asrt()
    assert asrt_data == {
        'segment_run': [
            (0, 0),
        ],
    }


# Generated at 2022-06-14 15:28:19.913871
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    flv = io.BytesIO(b'\x00\x00\x00\x0Aabcd\x00\x00\x00\x00')
    reader = FlvReader(flv)
    box_size, box_type, box_data = reader.read_box_info()
    assert box_size == 10
    assert box_type == b'abcd'
    assert box_data == b''
    flv = io.BytesIO(b'\x00\x00\x00\x0E\x00\x00\x00\x01abcd\x00\x00\x00\x00')
    reader = FlvReader(flv)
    box_size, box_type, box_data = reader.read_box_info()
    assert box_size == 14
    assert box_

# Generated at 2022-06-14 15:28:29.861767
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    import base64

# Generated at 2022-06-14 15:28:39.812579
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:28:52.048518
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:29:20.019168
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    test_f4m_doc = compat_etree_fromstring("""
    <bootstrapInfo profile="named"
                   id="bootstrap1"
                   url="http://example.com/bootstrap.abc"
                   serverBaseURL="http://example.com/">
    </bootstrapInfo>
    """)
    f4m_url_components = compat_urllib_parse_urlparse(
        xpath_text(test_f4m_doc, './@url', 'bootstrap URL'))
    test_bootstrap_url = 'http://example.com/bootstrap.abc'
    test_base_url = 'http://example.com/'
    test_absolute_base_url = 'http://example.com/'

# Generated at 2022-06-14 15:29:31.345935
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():

    import sys
    from youtube_dl.downloader.f4m import F4mFD
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.youtube import YoutubeIE
    #from youtube_dl.extractor.rutube import RutubeIE
    from youtube_dl.compat import compat_urllib_parse_urlencode
    from youtube_dl.downloader import FragmentFD
    from youtube_dl.utils import sanitize_open

    # url = 'http://www.rutube.ru/api/play/options/33c2945dee1b417d8bd44df7e0cdf47d/?format=json&sig=a7bddf1ad8cc08e11d3b3e98ac50c34f'
    # url = 'http://rut

# Generated at 2022-06-14 15:29:40.333696
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:29:48.754336
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:29:50.598417
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    """
    Unit test for method real_download of class F4mFD
    """
    pass



# Generated at 2022-06-14 15:29:58.091434
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    from xml.etree import ElementTree as ET

# Generated at 2022-06-14 15:30:03.750800
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    url = "http://vod.c.nmdn.net/vod/mp4:mediapm/ovp/content/test/video/spacealonehd_sounas_640_700.mp4/manifest.f4m"
    s = F4mFD({'url': url, 'test': True}).real_download("http://vod.c.nmdn.net/vod/mp4:mediapm/ovp/content/test/video/spacealonehd_sounas_640_700.mp4/manifest.f4m")
    assert s


# Test of code needs to be run from directory testing/

# Generated at 2022-06-14 15:30:13.198013
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    flv_reader = FlvReader(b'\x00\x00\x00\x1Cftypiso5\x00\x00\x02\x00isomiso2avc1mp41\x00\x00\x00\x08free\x00\x00\x00\x00')
    assert flv_reader.read_box_info() == (28, b'ftyp', b'iso5\x00\x00\x02\x00isomiso2avc1mp41')
    assert flv_reader.read_box_info() == (8, b'free', b'')
    assert flv_reader.read_box_info() == (0, b'', b'')



# Generated at 2022-06-14 15:30:24.061534
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    raw_bytes = b'\x00\x00\x00\x24\x61\x73\x72\x74\x00\x00\x00\x00\x00\x00\x00\x01' + \
        b'\x00\x00\x00\x01\x00\x00\x00\x64\x00\x00\x03\x1a\x00\x00\x00\x00\x00' + \
        b'\x00\x00\x00'
    data = FlvReader(raw_bytes)
    res = data.read_asrt()
    assert res['segment_run'] == [(100, 58)]

# Generated at 2022-06-14 15:30:33.169029
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x00(\x61\x73\x72\x74\x01\x00\x00\x00\x33\x30\x31\x30'
    data += b'\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x00'
    data += b'\x00\x00\x00\x03\x00\x00\x00\x06'
    reader = FlvReader(data)
    assert reader.read_asrt() == {
        'segment_run': [(0, 3), (3, 3), (6, 3)]
    }


# Generated at 2022-06-14 15:31:37.995680
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    class TestFlvReader(FlvReader):
        def __init__(self):
            self.data = io.BytesIO()
            self.read_count = 0

        def read_bytes(self, n):
            self.read_count += 1
            assert n == 1
            return self.data.read(n)

    reader = TestFlvReader()
    # test for real_size=0
    reader.data.write(compat_struct_pack('!I', 0))
    reader.data.write(b'abcd')
    reader.data.seek(0)
    assert reader.read_box_info() == (0, b'abcd', b'')
    # test for real_size=1
    reader.data.seek(0)

# Generated at 2022-06-14 15:31:49.301310
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:32:00.235565
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    from xml.etree import ElementTree as ET

# Generated at 2022-06-14 15:32:10.859372
# Unit test for function build_fragments_list
def test_build_fragments_list():
    boot_info = {
        'segments': [
            {
                'segment_run': [
                    (11, 1),
                    (12, 2),
                ]
            },
        ],
        'fragments': [
            {
                'fragments': [
                    {'ts': 0, 'discontinuity_indicator': None, 'first': 0, 'duration': 0}
                ]
            },
        ],
        'live': False,
    }
    r = build_fragments_list(boot_info)
    assert r == [(11, 0), (12, 1), (12, 2)]



# Generated at 2022-06-14 15:32:13.652393
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    filename = 'filename'
    info_dict = {}
    # This call should not raise an exception
    F4mFD().real_download(filename, info_dict)