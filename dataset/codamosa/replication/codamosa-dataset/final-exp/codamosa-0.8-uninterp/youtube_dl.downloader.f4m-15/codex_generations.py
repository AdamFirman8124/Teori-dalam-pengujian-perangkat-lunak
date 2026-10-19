

# Generated at 2022-06-14 15:23:11.019395
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:23:19.711790
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    import unittest
    import binascii


# Generated at 2022-06-14 15:23:31.763586
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:23:43.454273
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    """
    Unit test for method real_download of class F4mFD
    """
    from ydl.url import parse_url
    from ydl.filefd import FileDownloader
    from ydl.info import Info

    url = 'http://sample.com/manifest.f4m'
    url = parse_url(url)
    # test.py is run from the root directory so we need to go one level up
    path = os.getcwd()
    os.chdir('..')
    filename = 'test.flv'
    info_dict = Info({
        'id': 'f4m',
        'url': url,
        'title': 'test',
        'ext': 'flv'
    })
    ydl = FileDownloader({'outtmpl': filename})
    f4m_fd = F

# Generated at 2022-06-14 15:23:45.606956
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    s = b'stdout\x00\x00\x00\x00'
    assert FlvReader(s).read_string() == b'stdout'



# Generated at 2022-06-14 15:23:56.660813
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:24:08.745600
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:24:17.799793
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:24:28.495987
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:24:37.307723
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:25:23.096077
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    from .smil import read_smil_flavor_assets
    testcases = [
        ('abst', 'abst-1.dat', 20),
        ('smil', 'smil.dat', 17),
        ('smil', 'smil-2.dat', 20)
    ]
    for box_type, file_name, count in testcases:
        file_path = os.path.join(os.path.dirname(__file__), 'media', file_name)
        with open(file_path, 'rb') as fp:
            content = fp.read()
        reader = FlvReader(content)
        if box_type == 'abst':
            bootstrap_info = reader.read_bootstrap_info()
            assert len(bootstrap_info['segments']) == 1

# Generated at 2022-06-14 15:25:29.404400
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    xml = b'''<MediaSequence>
        <Media drmAdditionalHeaderId="xxxxx" drmAdditionalHeaderSetId="2" url="http://..."/>
        <Media url="http://..."/>
    </MediaSequence>'''
    xml_media = compat_etree_fromstring(xml).findall('Media')
    assert len(xml_media) == 2
    assert len(remove_encrypted_media(xml_media)) == 1



# Generated at 2022-06-14 15:25:37.344228
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    p = FlvReader(
        b'\x00\x00\x00\x01' + b'abcd'
        + b'\x00\x00\x00\x01' + b'efgh'
        + b'\x00\x00\x00\x09' + b'ijkl'
        + b'\x00\x00\x00\x00\x00\x00\x00\x11' + b'mnop'
    )
    assert p.read_box_info() == (1, b'abcd', b'')
    assert p.read_box_info() == (1, b'efgh', b'')
    assert p.read_box_info() == (9, b'ijkl', b'')

# Generated at 2022-06-14 15:25:47.782129
# Unit test for function get_base_url
def test_get_base_url():
    manifest = compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
        '  <baseURL>http://example.com/dir1/dir2/</baseURL>'
        '</manifest>')
    assert u'http://example.com/dir1/dir2/' == get_base_url(manifest)
    manifest = compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
        '  <baseURL>http://example.com/dir1/dir2</baseURL>'
        '</manifest>')
    assert u'http://example.com/dir1/dir2' == get_base_url(manifest)

# Generated at 2022-06-14 15:25:52.478682
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    test_input = b'\x00\x00\x00\x1C\x61\x73\x72\x74\x00\x00\x00\x00\x00\x00\x00\x01\x63\x75\x72\x72\x65\x6E\x74\x00\x00\x00\x01\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x0E'
    fr = FlvReader(test_input)
    res = fr.read_asrt()
    assert res ==  {
        'segment_run': [
            (0, 7),
            (1, 14),
        ]
    }


# Generated at 2022-06-14 15:26:01.708588
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:26:10.786921
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from .fragment import (
        get_f4m_fragment_base_urls,
        get_fragment_base_url,
    )
    # Test1: bootstrap info of http://multiplatform-f.akamaihd.net/z/multi/april11/hdworld/hdworld_,512x288_450_b,640x360_700_b,768x432_1000_b,1024x576_1400_b,1280x720_1900_b,.mp4.csmil/manifest.f4m

# Generated at 2022-06-14 15:26:20.304783
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:26:31.727939
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:26:40.992670
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from ..utils import encode_base_n
    from ..compat import compat_chr
    from hashlib import md5


# Generated at 2022-06-14 15:27:09.005504
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    raise NotImplementedError


# Generated at 2022-06-14 15:27:15.188995
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    
    #Initialisation of the variables
    first_attempt = True
    second_attempt = True
    success_first_attempt = False
    success_second_attempt = False
    F4mFD_instance = F4mFD()
    filename = 'my_filename'
    info_dict = { 'url': 'https://manifest_url'}
    
    #First attemp
    
    #Initialisation of the variables
    man_url = 'https://manifest_url'
    requested_bitrate = None
    F4mFD_instance.to_screen = lambda *args: None #Avoid printing
    F4mFD_instance.ydl = Mock_YDL()
    F4mFD_instance.ydl.urlopen = lambda *args: Mock_Urlopen() #Define the Mock_Urlopen method to

# Generated at 2022-06-14 15:27:25.126281
# Unit test for method read_box_info of class FlvReader

# Generated at 2022-06-14 15:27:31.449185
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Create instance of class F4mFD
    real_download = F4mFD()
    # Download a manifest
    assert real_download.real_download(filename="output/manifest.f4m",info_dict={'url':'http://host/manifest.f4m'})
    # Download a fragment
    assert real_download.real_download(filename="output/fragment.f4f",info_dict={'url':'http://host/fragment.f4f'})


# Generated at 2022-06-14 15:27:43.236886
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:27:52.170743
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data = b'\x00\x00\x00\x36\x61\x73\x72\x74\x00\x00\x00\x00\x00\x00\x00\x01\x66\x6c\x76\x36\x66\x6c\x76\x35\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x02'
    asrt = FlvReader(data).read_asrt()
    assert asrt == {
        'segment_run': [(0, 1), (1, 2)],
    }


# Generated at 2022-06-14 15:28:03.903681
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:28:14.338435
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    data = b'\x00\x00\x00\x38\x00\x00\x00\x01\x00\x00\x00\xfa\x00\x00\x00\xfa\x00\x00\x00\xfa\x00\x00\x00\xfa\x00\x00\x00\xfa\x00\x00\x00\xfa\x00\x00\x00\xfa\x00\x00\x00\xfa'
    fragments = FlvReader(data).read_afrt()['fragments']
    assert len(fragments) == 7
    assert fragments[0]['duration'] == 250
    assert fragments[1]['duration'] == 250
    assert fragments[2]['duration'] == 250

# Generated at 2022-06-14 15:28:21.364327
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    # Input data, as a hex string
    data = b'0000001c6175647374000003000008000100000000000000010468656c6c6f00'
    reader = FlvReader(data)
    ret = reader.read_abst()
    assert ret['live'] is False
    assert len(ret['segments']) == 1
    assert len(ret['fragments']) == 1
    assert len(ret['segments'][0]['segment_run']) == 1
    assert ret['segments'][0]['segment_run'][0] == (0, 1)
    assert len(ret['fragments'][0]['fragments']) == 1
    assert ret['fragments'][0]['fragments'][0]['duration'] == 1


# Generated at 2022-06-14 15:28:30.665543
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:02.699755
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:29:10.995204
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    class MockInfoDict():
        def __init__(self, url=None, extra_param_to_segment_url=None):
            self.url = url
            self.extra_param_to_segment_url = extra_param_to_segment_url
            self.tbr = None
    class MockYDL():
        def __init__(self, url=None, return_value=None):
            self.url = url
            self.return_value = return_value
        def urlopen(self, url):
            self.url = url
            class MockUrlh():
                def __init__(self, geturl=None, read=None):
                    self.read = read
                    self.geturl = geturl
                def read(self):
                    return self.read
                def geturl(self):
                    return

# Generated at 2022-06-14 15:29:19.451163
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:31.181387
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:32.278026
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    pass


# Generated at 2022-06-14 15:29:41.002203
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    # Test case 6.2.3.4 in the standard.
    binary = (
        b'\x00\x00\x00\x17'  # box size
        b'asrt'              # box type
        b'\x00'              # version
        b'\x00\x00\x00'      # flags
        b'\x00'              # QualityEntryCount
        b'\x00\x00\x00\x01'  # SegmentRunTableCount
        b'\x00\x00\x00\x00'  # first_segment
        b'\x00\x00\x00\x02'  # fragments_per_segment
    )
    reader = FlvReader(binary)
    info = reader.read_asrt()
    assert info['segment_run']

# Generated at 2022-06-14 15:29:49.159266
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:29:58.237351
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    # Test1: normal case
    f = io.BytesIO(
        b'\x00\x00\x00.ftypM4V \x00\x00\x00\x01M4V\x00\x00\x00\x00M4A \x00\x00\x00\x01M4A\x00\x00\x00\x00isomiso2avc1mp41')
    f.seek(0)
    actual_value = FlvReader(f).read_box_info()
    expected_value = (464,)
    assert len(actual_value) == len(expected_value)
    assert actual_value[0] == expected_value[0]
    # Test2: end of file, exception raised

# Generated at 2022-06-14 15:30:04.997636
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:30:14.475960
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    test_data = b'\x00\x00\x00\x1f\x61\x73\x72\x74\x01\x00\x00\x00\n\x61\x75\x64\x69\x6f\x61\x63\x63\x65\x73\x73\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x00\x10'
    asrt = FlvReader(test_data).read_asrt()
    assert len(asrt['segment_run']) == 2

# Generated at 2022-06-14 15:31:42.014715
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    """
    This test case is manually extracted from a .bootstrap file
    """

# Generated at 2022-06-14 15:31:51.676783
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from .compat import ByteStringIO
    from .utils import make_HTTPServer
    # Make sure that the test environment is set to the
    # expected state, which is freshly imported module
    assert F4mFD_real_download.__module__ == '__main__', 'TEST ENVIRONMENT ERROR. TEST FAILED. ABORT!'

    expected_test_url = 'http://localhost:8080/frag.f4m'
    expected_test_filename = 'test.flv'
    expected_test_info_dict = {'url': expected_test_url, 'fragment_index': 0}
    expected_test_fragment_index = 0
    expected_test_bytes_downloaded = 0
    expected_test_total_frags = 5
    expected_test_live = False
    expected_

# Generated at 2022-06-14 15:31:56.274306
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    flv_filename = './test_fragments/pya7s186i1svi.abst'
    with io.open(flv_filename, 'rb') as f:
        abst = FlvReader(f.read()).read_bootstrap_info()

# Generated at 2022-06-14 15:32:04.993460
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:32:16.231446
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Create a mock ydl object
    ydl_obj = mock.MagicMock()

    # Specify return value of the mocked method
    ydl_obj.report_error.return_value = True
    ydl_obj.report_warning.return_value = True

    # Create a mock urlopen object
    urlopen_obj = mock.MagicMock()
    urlopen_obj.geturl.return_value = True
    urlopen_obj.read.return_value = b"FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00"
    urlopen_obj.close.return_value = True

    # Specify return value of the mocked method
    ydl_obj.urlopen.return_value = urlopen_obj

    # Create a mock f