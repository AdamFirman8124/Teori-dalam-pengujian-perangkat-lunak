

# Generated at 2022-06-14 15:22:48.098076
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:22:56.173926
# Unit test for function build_fragments_list
def test_build_fragments_list():
    assert build_fragments_list(
        {
            'segments': [{
                'segment_run': [
                    (0, 5),
                    (10, 5),
                ]
            }],
            'fragments': [{
                'fragments': [
                    {'first': 1, 'ts': 1000, 'duration': 2000},
                    {'first': 2, 'ts': 3000, 'duration': 2000},
                ]
            }],
            'live': False,
        }
    ) == [
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        (10, 6), (10, 7), (10, 8), (10, 9), (10, 10),
    ]



# Generated at 2022-06-14 15:23:07.709664
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:23:17.243434
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    # case 1:
    test_input1 = (bytes(b'\x00\x00\x00\x00') +
                   bytes(b'\x04\x4f\x4c\x44'))
    assert FlvReader(test_input1).read_box_info() == (0, 'OLD', b'')

    # case 2:
    test_input2 = (bytes(b'\x00\x00\x00\x00') +
                   bytes(b'\x04\x4f\x4c\x44') +
                   bytes(b'\x01'))
    assert FlvReader(test_input2).read_box_info() == (0, 'OLD', bytes(b'\x01'))

    # case 3:

# Generated at 2022-06-14 15:23:25.219458
# Unit test for function get_base_url
def test_get_base_url():
    assert get_base_url(
        compat_etree_fromstring('<manifest><baseUrl>a</baseUrl></manifest>')) == 'a'
    assert get_base_url(
        compat_etree_fromstring('<manifest><baseURL>a</baseURL></manifest>')) == 'a'
    assert get_base_url(
        compat_etree_fromstring('<manifest><baseURL2>a</baseURL2></manifest>')) is None



# Generated at 2022-06-14 15:23:32.735848
# Unit test for function write_flv_header
def test_write_flv_header():
    for buf_size in (1024, 4096, 8192):
        stream = io.BytesIO()
        write_flv_header(stream)
        assert stream.getvalue() == (
            b'FLV\x01'
            b'\x05'
            b'\x00\x00\x00\x09'
            b'\x00\x00\x00\x00'
        )
        stream.close()

test_write_flv_header()



# Generated at 2022-06-14 15:23:41.330686
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    f4mFD = F4mFD()
    f4mFD.params = {u'test': True}
    f4mFD.ydl = object()
    filename = u'filename.ts'
    info_dict = {}
    info_dict[u'url'] = u'https://c.brightcove.com/services/mobile/streaming/index/master.m3u8?videoId=5373736541001'
    info_dict[u'tbr'] = None
    f4mFD.real_download(filename, info_dict)


# Generated at 2022-06-14 15:23:51.860458
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    with open('tests/data/bootstrap_test.txt') as f:
        flvdata = f.readline().strip().encode('ascii')
    fragmented_flv_reader = FlvReader(compat_b64decode(flvdata))
    abst = fragmented_flv_reader.read_bootstrap_info()
    # Make sure we have read all the data
    assert len(fragmented_flv_reader.read()) == 0

# Generated at 2022-06-14 15:24:03.068420
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:24:10.937360
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    """
    This method is used to test the real_download method of class F4mFD
    :return:
    """

# Generated at 2022-06-14 15:24:52.621206
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from ytdl.downloader.common import FileDownloader
    from ytdl.utils import FileDownloaderYtdl, BetterFileCache
    from ytdl.extractor import get_info_extractor, gen_extractors
    gen_extractors()
    ie = get_info_extractor('generic')
    ydl = FileDownloader({'outtmpl': '%(id)s.%(ext)s'}, ie)
    # Set up FileDownloaderYtdl
    fd = F4mFD(ydl, {'url': 'http://example.com/manifest.f4m', 'fragment_index': 0})
    ydl = FileDownloaderYtdl(ydl, fd)
    # Set up BetterFileCache

# Generated at 2022-06-14 15:24:56.453405
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    url = "https://c.brightcove.com/services/mobile/streaming/index/master.m3u8?videoId=5477645804001"
    ydl_opts = {}
    ie = F4mFD()
    ie.download(url, ydl_opts)

# Generated at 2022-06-14 15:25:03.316808
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    with io.open('abst_0.dat', 'rb') as abst_file:
        abst_data = abst_file.read()
    abst_reader = FlvReader(abst_data)
    abst = abst_reader.read_abst()
    assert abst[
        'segments'][0]['segment_run'] == [(0, 36), (1, 1), (2, 1), (3, 23)]
    assert len(abst['fragments']) == 1
    assert abst['fragments'][0]['fragments'][0]['discontinuity_indicator'] == None



# Generated at 2022-06-14 15:25:14.757225
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    media_tree = compat_etree_fromstring(fix_xml_ampersands(
        """
        <media url="http://test.com/test.mp4"
               bootstrapInfoId="bootstrap0"
               bitrate="1055"
               width="0"
               height="0"
               streamId="video"
               drmAdditionalHeaderId="{additional_header_id}"
               drmAdditionalHeaderSetId="{additional_header_set_id}"/>
        <media url="http://test.com/test_nodrm.mp4"
               bootstrapInfoId="bootstrap1"
               bitrate="1055"
               width="0"
               height="0"
               streamId="video"/>
        """))
    media = remove_encrypted_media(media_tree)
    assert len(media)

# Generated at 2022-06-14 15:25:19.890826
# Unit test for function write_flv_header
def test_write_flv_header():
    io_stream = io.BytesIO()
    write_flv_header(io_stream)
    return io_stream.getvalue()
# if __name__ == '__main__':
#     assert test_write_flv_header() == b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'


# Generated at 2022-06-14 15:25:30.985208
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:25:37.291677
# Unit test for function write_flv_header
def test_write_flv_header():
    """Tests that write_flv_header writes correct FLV header"""
    import tempfile
    temp_file = tempfile.TemporaryFile()
    write_flv_header(temp_file)
    temp_file.seek(0)
    header = temp_file.read()
    assert header == b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'
    temp_file.close()



# Generated at 2022-06-14 15:25:47.739616
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:25:58.341520
# Unit test for function get_base_url
def test_get_base_url():
    f = io.BytesIO('<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<manifest xmlns="http://ns.adobe.com/f4m/1.0"></manifest>')
    assert get_base_url(compat_etree_fromstring(f.read())) is None
    f = io.BytesIO('<?xml version="1.0" encoding="UTF-8"?>\n'
                   '<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
                   '<baseURL>abcd</baseURL></manifest>')
    assert get_base_url(compat_etree_fromstring(f.read())) == 'abcd'

# Generated at 2022-06-14 15:26:08.735836
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    test_asrt_data = compat_b64decode(b"""
AAAAHgAAAAEAAQAAQAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAADAwAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAgAAAAAAAQAAAAUAAQAAAgAAAAg
A/w==
""")
    asrt_data = FlvReader(test_asrt_data).read_

# Generated at 2022-06-14 15:26:42.059480
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    sample_f4m_url1 = 'http://multiplatform-f.akamaihd.net/z/multi/april11/hdworld/hdworld_,512x288_450_b,640x360_700_b,768x432_1000_b,1024x576_1400_m,1280x720_1900_m,1280x720_2500_m,1280x720_3500_m,.mp4.csmil/manifest.f4m'

# Generated at 2022-06-14 15:26:49.889363
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:27:01.441121
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    scraper = F4mFD()


# Generated at 2022-06-14 15:27:09.511676
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:27:20.718048
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    flv = FlvReader(b'\x00\x04ftypftypftyp')
    assert flv.read_box_info() == (4, b'ftyp', b'ftyp')
    flv = FlvReader(b'\x00\x00\x00\x0cftypftypftyp')
    assert flv.read_box_info() == (12, b'ftyp', b'ftypftyp')
    flv = FlvReader(b'\x00\x00\x00\x01\x00\x00\x00\x0cftypftypftyp')
    assert flv.read_box_info() == (12, b'ftyp', b'ftypftyp')

# Generated at 2022-06-14 15:27:30.922139
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:27:42.765376
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:27:52.544642
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:27:57.191733
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    with open('media/test.abst','rb') as f:
        abst_data = f.read()
        abst_info = FlvReader(abst_data).read_abst()
        print(abst_info)

# Generated at 2022-06-14 15:28:01.546445
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    import xml.etree.ElementTree as ET
    test_str = '''
    <media url="http://myurl/myfile.f4f"
           bootstrapInfoId="bootstrap1"
           bitrate="700"
           qualityLevels="2" width="1280" height="720" codec="AACL"
           drmAdditionalHeaderId="drm1"
           drmAdditionalHeaderSetId="drm2">
    </media>
    '''
    test_tree = ET.fromstring(test_str)
    test_media = test_tree.findall('media')
    test_media = remove_encrypted_media(test_media)
    assert len(test_media) == 1
    test_media = test_media[0]
    assert 'drmAdditionalHeaderId' not in test_media.attrib

# Generated at 2022-06-14 15:28:20.940024
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:28:26.504797
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    from .common import make_temp_directory

    with make_temp_directory() as t:
        path = os.path.join(t, 'p.flv')
        with open(path, 'wb') as out:
            write_flv_header(out)
            write_metadata_tag(out, b'')
        assert os.path.getsize(path) == 15



# Generated at 2022-06-14 15:28:36.221653
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:28:41.954109
# Unit test for function get_base_url
def test_get_base_url():
    txt = b"""<?xml version="1.0" encoding="UTF-8"?>
<manifest xmlns="http://ns.adobe.com/f4m/1.0">
  <baseURL>http://host.com/publishpoint/</baseURL>
</manifest>"""
    assert get_base_url(compat_etree_fromstring(txt)) == 'http://host.com/publishpoint/'



# Generated at 2022-06-14 15:28:53.970759
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    from .fragment import FragmentFD
    # The data is from file bootstrap.abst

# Generated at 2022-06-14 15:29:02.352317
# Unit test for function remove_encrypted_media

# Generated at 2022-06-14 15:29:12.252440
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    from .testcases import fake_data
    reader = FlvReader(fake_data())
    size, box_type, data = reader.read_box_info()
    assert size == 9
    assert box_type == b'abst'
    assert len(data) == 1
    size, box_type, data = reader.read_box_info()
    assert size == 21
    assert box_type == b'afrt'
    assert len(data) == 17
    size, box_type, data = reader.read_box_info()
    assert size == 25
    assert box_type == b'asrt'
    assert len(data) == 21


# Generated at 2022-06-14 15:29:16.549525
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    flv_reader = io.BytesIO(compat_struct_pack('!I', 2) + b'afrt' + compat_struct_pack('!II', 12, 1))
    assert FlvReader(flv_reader).read_afrt() == {'fragments': [{'first': 12, 'duration': 1, 'discontinuity_indicator': None, 'ts': 0}]}


# Generated at 2022-06-14 15:29:21.501325
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    xml = b'<Media><SegmentURL media="s1m1" quality="high" ' + \
          b'drmAdditionalHeaderId="16" drmAdditionalHeaderSetId="1"/>' + \
          b'<SegmentURL media="s1m1" quality="low" ' + \
          b'drmAdditionalHeaderId="16" drmAdditionalHeaderSetId="2"/></Media>'
    media = remove_encrypted_media(compat_etree_fromstring(xml))
    assert media == []



# Generated at 2022-06-14 15:29:31.739396
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:29:51.417776
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    test_data = (b'\x03abc\x00\x0512345\x00', b'abc', b'12345')
    flv_reader = FlvReader(test_data[0])
    strings = []
    for i in range(2):
        strings.append(flv_reader.read_string())
    assert strings == list(test_data[1:])

# Generated at 2022-06-14 15:29:59.825859
# Unit test for method read_afrt of class FlvReader
def test_FlvReader_read_afrt():
    # Data generated by Adobe's flvtool2
    data = compat_b64decode('''
    AQAAAMQCAAAAAAA5gUxMAEBAA0AAICzAMCAwMDBQC1AwMAAACc01X/nN/
    f5x5o5i5MzDpAUAAAAADwgDAAUAAAAEAAAAFY6X///8AAAEAABQAAAAQA
    AAABmO1+////AAABAAAgAQAAGQEAAA9Xf////8AAAEAAEAAAABAAAAFZ
    8f///wAAAQAAAAAAAAAAAEBEAQA=
    ''')
    fr = FlvReader(data)

# Generated at 2022-06-14 15:30:10.731048
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import base64
    from .test_download import testdata
    bootstrap_b64 = testdata('test/test.bootstrap')
    bootstrap = base64.b64decode(bootstrap_b64)

    bootstrap_info = FlvReader(bootstrap).read_bootstrap_info()
    assert len(bootstrap_info['segments']) == 1
    assert len(bootstrap_info['segments'][0]['segment_run']) == 1
    assert bootstrap_info['segments'][0]['segment_run'][0][0] == 0
    assert bootstrap_info['segments'][0]['segment_run'][0][1] == 5

    assert len(bootstrap_info['fragments']) == 1

# Generated at 2022-06-14 15:30:14.156694
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    data = b'\x04\x00\x00\x00' + b'type' + b'\x06\x00\x00\x00' + 'string'
    flv = FlvReader(data)
    assert flv.read_string() == b'type'

# Generated at 2022-06-14 15:30:25.922143
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:30:35.448321
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Test with a list of URLs that we can download without errors
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 15:30:46.342282
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    """
    Unit test for method read_bootstrap_info of class FlvReader
    """
    from .test import _download_test_file
    f = FlvReader(_download_test_file('bootstrapinfo'))

# Generated at 2022-06-14 15:30:56.759049
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:31:03.012957
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:31:14.679085
# Unit test for method read_afrt of class FlvReader