

# Generated at 2022-06-14 15:22:53.143254
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    pass

    # my_F4mFD = F4mFD()
    # real_download = my_F4mFD.real_download

if __name__ == '__main__':
    # test_F4mFD_real_download()
    pass

# Generated at 2022-06-14 15:22:59.987760
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = compat_b64decode(b'''
        AAAAAAAAAAAAAAAAAAAAAO9YBYAAAfDACxhc3N0L1RWL0Jvb3QuMjAxMy4zLjI0LjEzLjMxLjIxNjkuODku
        Vjg5LzAxNjAwMDYwNDAwNDAwMDAwLkZMVi9BU1JULzBFMDQ0MjIzRDA0NgBQQUNLQUdFAA==
    ''')
    result = FlvReader(data).read_asrt()

# Generated at 2022-06-14 15:23:09.870431
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:23:14.986858
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    from .test_fragments import _load_test_data
    _data = _load_test_data('bootstrap.abst')
    reader = FlvReader(_data)
    assert reader.read_box_info() == (len(_data), b'abst', _data[8:])
    assert reader.read_box_info() == (0, b'', b'')



# Generated at 2022-06-14 15:23:27.284346
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .common import read_fixture
    data = read_fixture('fragment_f4m', 'bootstrapInfo.abst')

# Generated at 2022-06-14 15:23:37.147345
# Unit test for function build_fragments_list
def test_build_fragments_list():
    res = build_fragments_list({
        'segments': [{
            'segment_run': [
                (0, 1),
                (1, 1),
            ],
        }],
        'fragments': [{
            'fragments': [
                {'first': 0, 'ts': 0, 'duration': 5, 'discontinuity_indicator': None},
                {'first': 1, 'ts': 6, 'duration': 5, 'discontinuity_indicator': None},
                {'first': 2, 'ts': 12, 'duration': 5, 'discontinuity_indicator': None},
            ],
        }],
    })
    assert res == [(0, 0), (1, 1)]



# Generated at 2022-06-14 15:23:48.814758
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:23:57.169383
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:24:05.976666
# Unit test for constructor of class F4mFD
def test_F4mFD():
    f4m_fd = F4mFD({
        'params': {
            'url': 'http://example.org',
            'force_generic_extractor': True,
        }
    })
    assert isinstance(f4m_fd, F4mFD)


if __name__ == '__main__':
    _TEST_F4M = os.environ.get('TEST_F4M')
    _TEST_HDS = os.environ.get('TEST_HDS')
    _TEST_BOOTSTRAP = os.environ.get('TEST_BOOTSTRAP')
    if _TEST_BOOTSTRAP:
        from binascii import a2b_hex
        bootstrap = FlvReader(a2b_hex(_TEST_BOOTSTRAP)).read_

# Generated at 2022-06-14 15:24:14.574345
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    # Test case 1:
    # Input: 0x00
    # Output: ''
    assert FlvReader(b'\x00').read_string() == b''
    # Test case 2:
    # Input: 0x61 0x00
    # Output: 'a'
    assert FlvReader(b'\x61\x00').read_string() == b'a'
    # Test case 3:
    # Input: 0x61 0x62 0x63 0x00
    # Output: 'abc'
    assert FlvReader(b'\x61\x62\x63\x00').read_string() == b'abc'



# Generated at 2022-06-14 15:24:40.669782
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:24:47.056219
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    src_bytes = compat_struct_pack('!BBBB', 0x01, 0x02, 0x03, 0x00)
    dst_str = '\x01\x02\x03'
    bytes_io = io.BytesIO(src_bytes)
    reader = FlvReader(bytes_io)
    res_str = reader.read_string()
    assert res_str == dst_str



# Generated at 2022-06-14 15:24:51.952497
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    media = [
        {'url': 'http://example.com/file.mp4', 'drmAdditionalHeaderId': '1'},
        {'url': 'http://example.com/file.mp4'},
    ]
    assert remove_encrypted_media(media) == [{'url': 'http://example.com/file.mp4'}]


# Generated at 2022-06-14 15:25:01.052570
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:11.205630
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:25:15.475559
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:25:24.428259
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:25:33.415612
# Unit test for constructor of class F4mFD
def test_F4mFD():
    from youtube_dl.utils import DateRange

# Generated at 2022-06-14 15:25:38.253625
# Unit test for function get_base_url
def test_get_base_url():
    assert 'https://one.example.com/' == get_base_url(
        compat_etree_fromstring(
            u'<manifest><baseURL>https://one.example.com/</baseURL></manifest>'))
    assert None is get_base_url(
        compat_etree_fromstring(
            u'<manifest></manifest>'))



# Generated at 2022-06-14 15:25:45.863363
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = compat_b64decode(b'''
        AQAAAAEAAAABAAAABXNncnR0AAABAAAABAAAABgAAADEAAAAeAAAAAwAAAAAAAAAAAAAA
        AAAAAAABAAABAAAAKgAAAAMAAAAAAAAAAAAAAA4AAAAZAAAAGQAAABkAAAARAAAAAAAA
        AAAAAAAAAAAAAA==
    ''')
    reader = FlvReader(data)
    assert reader.read_asrt() == {
        'segment_run': [
            (1, 1),
        ],
    }



# Generated at 2022-06-14 15:26:09.724402
# Unit test for method read_box_info of class FlvReader

# Generated at 2022-06-14 15:26:19.587495
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    actual_value = {
        'segment_run': [
            (2, 3),
        ],
    }
    flv_reader = FlvReader(
        # Header
        b'\x00\x00\x00\x3e' + b'asrt' +
        # Version
        b'\x00' +
        # Flags
        b'\x00\x00\x00' +
        # QualityEntryCount
        b'\x00' +
        # SegmentRunEntryCount
        b'\x01\x00\x00\x00' +
        # FirstSegment
        b'\x02\x00\x00\x00' +
        # FragmentsPerSegment
        b'\x03\x00\x00\x00'
    )
    assert actual_value

# Generated at 2022-06-14 15:26:23.822096
# Unit test for constructor of class F4mFD
def test_F4mFD():
    # Initialize a downloader class
    fd = F4mFD({'noprogress': True, 'quiet': True})
    # Get the list of supported extractors
    info = fd._real_extract('http://s3.amazonaws.com/ akamai.netstorage/Big_Buck_Bunny.f4m')
    print(info)

if __name__ == '__main__':
    test_F4mFD()

# Generated at 2022-06-14 15:26:35.378866
# Unit test for method read_box_info of class FlvReader

# Generated at 2022-06-14 15:26:45.056910
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    raw_data = b'\x00\x00\x00(\x04frt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    afrt = FlvReader(raw_data).read_afrt()

# Generated at 2022-06-14 15:26:51.029024
# Unit test for function build_fragments_list
def test_build_fragments_list():
    def helper(boot_info, expected):
        actual = build_fragments_list(boot_info)
        assert actual == expected, (
            'build_fragments_list error: expected %r but got %r' % (
                expected, actual))


# Generated at 2022-06-14 15:27:02.642478
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    from .fragment import testutils
    class BytesIO(testutils.BytesIO):
        def read(self, n):
            if n > len(self.buf):
                raise DataTruncatedError
            res = self.buf[:n]
            self.buf = self.buf[n:]
            return res

# Generated at 2022-06-14 15:27:10.232532
# Unit test for function build_fragments_list
def test_build_fragments_list():
    def _build_bootstrap_info(segments, fragments, live=False):
        return {
            'segments': [{'segment_run': segments}],
            'fragments': [{'fragments': [{'first': x[1]} for x in fragments]}],
            'live': live,
        }

    # Check that we can handle all values of `fragments_count`

# Generated at 2022-06-14 15:27:21.230101
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:31.342170
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    """
    Test read_bootstrap_info method of FlvReader
    """

# Generated at 2022-06-14 15:28:32.037954
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:28:38.794464
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:28:50.770397
# Unit test for method read_box_info of class FlvReader

# Generated at 2022-06-14 15:29:01.203961
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:29:13.177351
# Unit test for method read_box_info of class FlvReader

# Generated at 2022-06-14 15:29:21.141144
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from ..utils import shellsafe

    def asrt_str(obj):
        return (
            ' '.join(shellsafe(s) for s in obj['segment_run'])
            if 'segment_run' in obj else None
        )

    def afrt_str(obj):
        return (
            ' '.join(
                '%d:%d' % (frag['first'], frag['duration'])
                for frag in obj['fragments']
            )
            if 'fragments' in obj else None
        )


# Generated at 2022-06-14 15:29:31.600362
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:29:37.986926
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:29:44.263265
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    class data:
        def __init__(self, url, manifest, urlh, requested_bitrate, test, params, ydl):
            self.url = url
            self.manifest = manifest
            self.urlh = urlh
            self._requested_bitrate = requested_bitrate
            self._test = test
            self._params = params
            self._ydl = ydl
    class context:
        def __init__(self, filename, total_frags, live):
            self.data = data
            self.filename = filename
            self.total_frags = total_frags
            self.live = live
    class dest_stream:
        def __init__(self, frag_data):
            self.frag_data = frag_data
        def write(self, frag_info):
            self.frag

# Generated at 2022-06-14 15:29:51.284027
# Unit test for function get_base_url
def test_get_base_url():
    manifest = compat_etree_fromstring('<manifest xmlns="http://ns.adobe.com/f4m/2.0" baseURL="http://example.com/f4m/base/url"/>')
    assert get_base_url(manifest) == 'http://example.com/f4m/base/url', 'get_base_url should give http://example.com/f4m/base/url'


# Generated at 2022-06-14 15:30:39.558636
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:30:50.291035
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:30:58.727056
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # tests the real_download method of F4mFD class
    # expected : return True
    # Assumtions : Internet connection is available
    #              GD module is installed
    manifest_url = "https://mnmedias.api.telequebec.tv/m3u8/29880.m3u8"

    from ydl.downloader.http_fd import HttpFD
    from ydl.downloader.f4mfd import F4mFD
    from ydl.postprocessor.ffmpeg import FFmpegPostProcessor
    from ydl.extractor.common import InfoExtractor
    from ydl.compat import compat_urllib_parse_urlparse
    from ydl.compat import compat_urllib_request
    from ydl.compat import compat_urlparse

# Generated at 2022-06-14 15:31:09.665899
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from ..compat import compat_b64decode

# Generated at 2022-06-14 15:31:20.629183
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from ..compat import detect_encoding
    from ..downloader.f4m import _compat_struct_pack

    def _gen_str(str_encoding, str_len):
        return _compat_struct_pack('!%ds' % str_len, str_encoding)
    def _gen_num(num):
        return _compat_struct_pack('!I', num)
    def _gen_num_long(num):
        return _compat_struct_pack('!Q', num)

    file_path = 'test.f4m'
    file_data = b''
    abst_data = b''

    # version
    abst_data += _compat_struct_pack('!B', 0)
    # flags
    abst_data += _compat_struct_pack('!B', 0)

# Generated at 2022-06-14 15:31:30.442528
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from ...compat import parse_qs
    from ...utils import ClosedFileObject
    from .test_download import MockYDL

# Generated at 2022-06-14 15:31:38.870811
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    doc = """
    <media>
      <metadata>...</metadata>
      <bootstrapInfoId>0</bootstrapInfoId>
      <drmAdditionalHeaderId>3</drmAdditionalHeaderId>
      <drmAdditionalHeaderSetId>4</drmAdditionalHeaderSetId>
      <segmentRunTableId>1</segmentRunTableId>
      <fragmentRunTableId>2</fragmentRunTableId>
    </media>
    """
    assert len(remove_encrypted_media(compat_etree_fromstring(doc))) == 1



# Generated at 2022-06-14 15:31:44.935165
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:31:57.596729
# Unit test for method real_download of class F4mFD

# Generated at 2022-06-14 15:32:05.507598
# Unit test for method read_asrt of class FlvReader