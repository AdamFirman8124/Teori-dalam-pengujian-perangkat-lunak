

# Generated at 2022-06-14 15:22:52.068083
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    # case 1
    reader = FlvReader(b'asdf\x00qwer\x00')
    assert reader.read_string() == b'asdf'
    assert reader.read_string() == b'qwer'

    # case 2
    reader = FlvReader(b'asdfqwer\x00')
    assert reader.read_string() == b'asdfqwer'

    # case 3
    reader = FlvReader(b'asdf\x00')
    assert reader.read_string() == b'asdf'

    # case 4
    reader = FlvReader(b'asdf')
    try:
        reader.read_string()
        assert False
    except DataTruncatedError:
        assert True



# Generated at 2022-06-14 15:22:59.157853
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    data = compat_struct_pack(
        b'!I4sII',
        18,
        b'test',
        1,
        2)
    reader = FlvReader(data)
    assert reader.read_box_info() == (18, b'test', compat_struct_pack(b'!II', 1, 2))

    data = compat_struct_pack(
        b'!Q4sQQQQ',
        26,
        b'test',
        1,
        2,
        3,
        4,
        5)
    reader = FlvReader(data)
    assert reader.read_box_info() == (26, b'test', compat_struct_pack(b'!QQQQ', 1, 2, 3, 4))



# Generated at 2022-06-14 15:23:00.195912
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    pass


# Generated at 2022-06-14 15:23:06.617880
# Unit test for constructor of class F4mFD
def test_F4mFD():
    url = ('http://sldrm.download.akamai.com/11996/sldrm/'
           'mediapm/ondemand/cbc/cbc_nbcolympics_live/'
           'cbc_nbcolympics_live_20080510_3200k.f4m')
    fd = F4mFD(None, {'url': url})
    assert fd.manifest_url == url
    assert fd.params['url'] == url



# Generated at 2022-06-14 15:23:10.313532
# Unit test for function write_flv_header
def test_write_flv_header():
    from ..utils import encode_data_uri
    from io import BytesIO
    stream = BytesIO()
    write_flv_header(stream)
    assert stream.getvalue() == b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'



# Generated at 2022-06-14 15:23:19.278760
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:23:26.724071
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    import io
    metadata = b"a=b"
    stream = io.BytesIO()
    write_metadata_tag(stream, metadata)
    s = stream.getvalue()
    assert s == b'\x12\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x61\x3d\x62\x00\x00\x00\x15'



# Generated at 2022-06-14 15:23:32.067061
# Unit test for constructor of class F4mFD
def test_F4mFD():
    from .testcases import gettestcases
    for manifest in gettestcases(F4mFD):
        print('Testing %s' % (manifest))
        fd = F4mFD({'url': manifest, 'username': 'whatever', 'password': 'whatever'})
        fd.real_download('test.flv', {'url': manifest})


# Utility functions

# Generated at 2022-06-14 15:23:43.811011
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import base64

# Generated at 2022-06-14 15:23:53.822353
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    f4m_fd = F4mFD()
    # Set up mock urllib2
    # ToDo: set up mock file
    #f4m_fd.ydl.urlopen(self._prepare_url(info_dict, man_url))
    # Get real download URL
    #urlh.geturl()

# Generated at 2022-06-14 15:24:20.049665
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:24:22.412007
# Unit test for constructor of class F4mFD
def test_F4mFD():
    f4mfd = F4mFD({'params': {}}, None)
    assert 'F4mFD' == f4mfd.FD_NAME

# Generated at 2022-06-14 15:24:29.720123
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    test_data = b'\x00\x00\x00\x25\x61\x73\x72\x74\x01\x6a\x6f\x6f\x6d\x00\x61\x76\x69\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x0c\x00\x00\x00\x01'
    res = FlvReader(test_data).read_asrt()
    assert res['segment_run'] == [(12, 1)]


# Generated at 2022-06-14 15:24:38.211430
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:24:45.869763
# Unit test for constructor of class F4mFD
def test_F4mFD():
    class FakeInfoDict(object):
        def __init__(self, url):
            self.url = url
            self.tbr = None
            self.extra_param_to_segment_url = None

    # Fake info dict to simulate download
    fake_info = FakeInfoDict('http://fake_info/')
    f4m_fd = F4mFD(None, fake_info, None)

    # Fake info dict to simulate download with bitrate
    fake_info = FakeInfoDict('http://fake_info/?bitrate=500')
    fake_info.tbr = 500
    f4m_fd = F4mFD(None, fake_info, None)

    # Fake info dict to simulate download with extra_param_to_segment_url

# Generated at 2022-06-14 15:24:54.804902
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    # Test case 1: a box with length equals 1
    box_root = b'\x00\x00\x01\x43\x6f\x6e\x74\x65\x6e\x74\x73\x42\x6f\x78\x00'
    box = FlvReader(box_root)
    assert box.read_box_info() == (
        0x43, b'cont', b'entsBox')
    # Test case 2: a box with length not equal 1
    box_root = b'\x00\x00\x01\x63'
    box = FlvReader(box_root)
    assert box.read_box_info() == (
        99, b'c', b'\x00' * 95)



# Generated at 2022-06-14 15:25:03.280016
# Unit test for constructor of class F4mFD
def test_F4mFD():
    from .extractor.common import InfoExtractor
    from .compat import compat_cookiejar
    from .utils import parse_duration

    class TestIE(InfoExtractor):
        IE_NAME = 'test'
        IE_DESC = 'test'
        _VALID_URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'


# Generated at 2022-06-14 15:25:14.745976
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from collections import defaultdict
    from .extractor.common import InfoExtractor
    from .utils import ExtractorError
    from .utils import HEADRequest
    from io import BytesIO

    url = 'http://some.url/someid.f4m'


# Generated at 2022-06-14 15:25:23.911041
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:25:31.165090
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    start_time = time.time()
    for test_file in ['test_bootstrap_info_vod', 'test_bootstrap_info_live']:
        with io.open('test/' + test_file + '.flv', 'rb') as f:
            assert FlvReader(f.read()).read_bootstrap_info() == eval(open('test/' + test_file + '.bootstrap_info.py').read())
    print('%s: OK.' % (sys._getframe().f_code.co_name))



# Generated at 2022-06-14 15:28:15.206291
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    assert FlvReader(b'\x00\x00\x00\x1C\x61\x62\x73\x74\x00\x00\x00\x00\x00\x00\x00\x00test').read_abst() == {
        'segments': [],
        'fragments': [],
        'live': False,
    }

# Generated at 2022-06-14 15:28:24.643906
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:28:26.713200
# Unit test for function get_base_url
def test_get_base_url():
    manifest = {'baseURL': 'a'}
    assert get_base_url(manifest) == 'a'



# Generated at 2022-06-14 15:28:37.201790
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:28:37.907399
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    pass



# Generated at 2022-06-14 15:28:42.749544
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import urlopen
    from youtube_dl.postprocessor import FFmpegMetadataPP
    from youtube_dl.utils import sanitize_open
    from io import BytesIO

    class TestFD(F4mFD):
        def _prepare_url(self, info_dict, url):
            return url

        def _find_executable(self, exe):
            return exe

        def _prepare_frag_download(self, ctx):
            ctx['frag_filename'] = 'test.f4m.tmp'
            ctx['dest_stream'] = BytesIO()
            ctx['frag_tmp'] = BytesIO()


# Generated at 2022-06-14 15:28:48.922367
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    F4mFD_res = F4mFD().real_download('asdasd', {'url': 'https://fooooooooooooo.bar', 'extra_param_to_segment_url': 'bar'})
    assert F4mFD_res == True, 'F4mFD().real_download() should be true'


# Generated at 2022-06-14 15:28:59.962298
# Unit test for function build_fragments_list
def test_build_fragments_list():
    assert build_fragments_list({
        'segments': [{
            'segment_run': [
                (0, 1),
            ]
        }],
        'fragments': [{
            'fragments': [
                {'first': 0},
            ]
        }],
    }) == [
        (0, 0),
    ]

# Generated at 2022-06-14 15:29:12.298078
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    fake_file = b'\x00\x00\x00\x00' + b'moov' + b'\x00\x00\x00\x00'
    flv_reader = FlvReader(fake_file)
    size, box_type, data = flv_reader.read_box_info()
    assert size == 8
    assert box_type == b'moov'
    assert data == b''

    fake_file = (b'\x00\x00\x00\x01' + b'moov' +
                 b'\x00\x00\x00\x00\x00\x00\x00\x08')
    flv_reader = FlvReader(fake_file)
    size, box_type, data = flv_reader.read_box_info()
   

# Generated at 2022-06-14 15:29:14.762765
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    video_url = 'http://example.com/manifest.f4m'
    video_params = {'url': video_url}
    async_test(urls=[video_url], res=[video_params],
               prep=[lambda: F4mFD('test.flv', video_params).real_download('', video_params)])

if __name__ == '__main__':
    test_F4mFD_real_download()

# Generated at 2022-06-14 15:29:52.602172
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import sys
    import unittest
    class TestRealDownload(unittest.TestCase):
        def setUp(self):
            self.fd_f4m = F4mFD()
            self.fd_f4m._downloader = Downloader(None, None)
        def test_F4mFD_real_download(self):
            self.fd_f4m.real_download(str(''),{'url': str('url'),'tbr': int(),'extra_param_to_segment_url': str('')})
    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-14 15:30:00.262667
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:30:11.001375
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:30:17.817227
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    data = (
        b'\x00\x00\x00\'\x66\x74\x72\x61'
        b'\x00\x00\x00\x01\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    )
    info = FlvReader(data).read_afrt()
    assert info['fragments'] == [{
        'first': 0,
        'ts': 0,
        'duration': 0,
        'discontinuity_indicator': 0,
    }]



# Generated at 2022-06-14 15:30:28.649942
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:30:37.844044
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:30:47.835310
# Unit test for function build_fragments_list
def test_build_fragments_list():
    boot_info = read_bootstrap_info(bootstrap_live)
    expected = [(5, 8), (5, 9)]
    res = build_fragments_list(boot_info)
    assert res == expected

    boot_info = read_bootstrap_info(bootstrap_vod)
    expected = [
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
        (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15)
    ]
    res = build_fragments_list(boot_info)
    assert res == expected



# Generated at 2022-06-14 15:30:58.068791
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:31:03.686924
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    class TestFlvReader(FlvReader):
        def __init__(self, *args, **kwargs):
            self.pos = 0
            super(TestFlvReader, self).__init__(*args, **kwargs)

        def read(self, n):
            data = super(TestFlvReader, self).read(n)
            self.pos += n
            return data

        def tell(self):
            return self.pos


# Generated at 2022-06-14 15:31:15.544998
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:32:16.303485
# Unit test for function build_fragments_list