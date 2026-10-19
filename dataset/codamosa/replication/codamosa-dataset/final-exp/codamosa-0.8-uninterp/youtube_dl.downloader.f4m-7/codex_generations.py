

# Generated at 2022-06-14 15:23:11.706209
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:23:20.156692
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    manifest_url = 'http://streaming.universite-lyon.fr/vod/mp4:cours1-2.mp4/master.m3u8'

# Generated at 2022-06-14 15:23:32.169498
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:23:43.915556
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:23:49.108219
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    with tempfile.TemporaryDirectory() as tmpdir:
        # unitest doesn't use the command line argument `--test`
        F4mFD().real_download(os.path.join(tmpdir, "file.flv"), {
            "url": "http://my-manifest.f4m",
            "info_dict": {"id": "some_id"},
        })

# Generated at 2022-06-14 15:23:57.376416
# Unit test for method real_download of class F4mFD

# Generated at 2022-06-14 15:24:08.693883
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    flv = FlvReader(b'\x00\x00\x01\x00' + b'\x00\x00\x00\x04' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x01')
    assert flv.read_box_info() == (16, b'\x00\x00\x00\x04', b'\x00\x00\x00\x00')
    assert flv.read_box_info() == (1, b'\x00\x00\x00\x01', b'')
    try:
        flv.read_box_info()
        assert False
    except DataTruncatedError:
        pass



# Generated at 2022-06-14 15:24:15.698922
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    flv_reader = FlvReader(b'\x04\x00\x00\x00test\x00\x00\x00\x06foobar\x00\x06foobar\x00\x00\x00\x09foobarfoo')
    assert flv_reader.read_string() == b'test'
    assert flv_reader.read_string() == b'foobar'
    assert flv_reader.read_string() == b'foobar'
    assert flv_reader.read_string() == b'foobarfoo'



# Generated at 2022-06-14 15:24:26.766461
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:24:30.677564
# Unit test for function write_flv_header
def test_write_flv_header():
    s = io.BytesIO()
    write_flv_header(s)
    assert s.getvalue() == b'FLV\x01\x05\x00\x00\x00\x09\x00\x00\x00\x00'



# Generated at 2022-06-14 15:25:20.354105
# Unit test for function get_base_url
def test_get_base_url():
    f = io.StringIO('<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
                    '<baseURL>http://example.com/</baseURL></manifest>')
    assert get_base_url(compat_etree_fromstring(f.read())) == 'http://example.com/'

    f = io.StringIO('<manifest xmlns="http://ns.adobe.com/f4m/1.0">'
                    '<baseURL>http://example.com/</baseURL>'
                    '<bootstrapInfo>bootstraptest</bootstrapInfo></manifest>')
    assert get_base_url(compat_etree_fromstring(f.read())) == 'http://example.com/'


# Generated at 2022-06-14 15:25:31.690673
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from common import clean_html, get_testdata_files_path
    filepath = get_testdata_files_path()
    filepath_html = os.path.join(filepath, 'rtmpdump.html')

# Generated at 2022-06-14 15:25:42.119549
# Unit test for function get_base_url
def test_get_base_url():
    manifest = '''<manifest xmlns="http://ns.adobe.com/f4m/2.0"><baseURL>https://cdn-6.pscp.tv/</baseURL></manifest>'''
    assert get_base_url(manifest) == "https://cdn-6.pscp.tv/"
    manifest = '''<manifest xmlns="http://ns.adobe.com/f4m/2.0"></manifest>'''
    assert get_base_url(manifest) is None
    manifest = '''<manifest xmlns="http://ns.adobe.com/f4m/2.0"><baseURL>https://cdn-6.pscp.tv/</baseURL><baseURL>https://cdn-7.pscp.tv/</baseURL></manifest>'''
    assert get_base_url

# Generated at 2022-06-14 15:25:45.290944
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from ydl_f4m_tests import F4mFD_real_download
    F4mFD_real_download()

__all__ = ['F4mFD', 'test_F4mFD_real_download']

# Generated at 2022-06-14 15:25:55.202271
# Unit test for function build_fragments_list
def test_build_fragments_list():
    from .common import decode_msgpack
    from .fragment import parse_fragment_url
    fragment_url = (
        'http://localhost:8080/hds-live/livepkgr/_definst_/'
        'liveevent/livestream.f4m?e=1439215703&h=3efec9d958d08f1bbfe25c3ae3b7dca2')

    frag_info = parse_fragment_url(fragment_url)
    if not frag_info.get('bootstrap_info'):
        raise ValueError('Bootstrap is missing')
    boot_info = read_bootstrap_info(frag_info['bootstrap_info'])
    fragments = list(build_fragments_list(boot_info))
    # List of [(0

# Generated at 2022-06-14 15:25:59.188984
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    abst = 'AAAAcA=='
    box_info = FlvReader(compat_b64decode(abst.encode('ascii'))).read_abst()
    assert box_info == {
        'segments': [],
        'fragments': [],
        'live': False,
    }

# Generated at 2022-06-14 15:26:09.335597
# Unit test for function get_base_url
def test_get_base_url():
    assert get_base_url(compat_etree_fromstring(
        '<manifest><baseURL>http://example.com/</baseURL></manifest>')) == 'http://example.com/'
    assert get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/1.0"><baseURL>http://example.com/</baseURL></manifest>')) == 'http://example.com/'
    assert get_base_url(compat_etree_fromstring(
        '<manifest xmlns="http://ns.adobe.com/f4m/2.0"><baseURL>http://example.com/</baseURL></manifest>')) == 'http://example.com/'
    assert get_base_url

# Generated at 2022-06-14 15:26:14.581209
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    flvreader = FlvReader(compat_b64decode(b'''CQAACvIDAAEXAQAAZp4EAAB72gAAAAMAAAA8AAAA4WyAjYyMzA1YTEzMjU0ZjUzZmU3ZDM='''))
    print(flvreader.read_asrt())



# Generated at 2022-06-14 15:26:26.596804
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    sample_data = (
        b'\x00\x00\x00\x00' + b'\x00\x00\x00\x09' + b'ftypisom' +
        b'\x00\x00\x00\x01' + b'\x00\x00\x00\x00' + b'\x00\x00\x00\x00'
    )
    fr = FlvReader(sample_data)
    total_size, box_type, box_data = fr.read_box_info()
    assert total_size == 9
    assert box_type == b'ftyp'
    assert box_data == b'isom'
    total_size, box_type, box_data = fr.read_box_info()
    assert total_size == 1

# Generated at 2022-06-14 15:26:37.075299
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    def make_bytes_io(data):
        return FlvReader(compat_struct_pack(
            '!QI', 1, len(data) + 8) + data)

    data = {'segments': [{'segment_run': [(0, 1)]}],
            'fragments': [{'fragments': [{'first': 0, 'ts': 0,
                                          'duration': 2, 'discontinuity_indicator': None}]}]}
    abst = data['segments'][0]['segment_run'][0]['first']

# Generated at 2022-06-14 15:27:03.602414
# Unit test for method read_asrt of class FlvReader

# Generated at 2022-06-14 15:27:05.674674
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    flv = FlvReader(open('tests/resources/bootstrap', 'rb').read())
    print(flv.read_bootstrap_info())


# Generated at 2022-06-14 15:27:12.285812
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:27:22.530192
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:27:27.940132
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    filename = 'tests/data/bootstrap_live.abst'
    with open(filename, 'rb') as f:
        abst = FlvReader(f.read()).read_bootstrap_info()

        asrt = abst['segments'][0]
        expected_asrt = {
            'segment_run': [(0, 4)],
        }
        assert asrt == expected_asrt


# Generated at 2022-06-14 15:27:38.848731
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    import xml.etree.ElementTree as ET
    xml_str = (
        '<smil><body><switch>'
        '<video src="http://example.com/1" drmAdditionalHeaderSetId="1" />'
        '<video src="http://example.com/2" drmAdditionalHeaderId="2" />'
        '<video src="http://example.com/3" />'
        '</switch></body></smil>')
    root = ET.fromstring(xml_str)
    media = root.findall('.//video')
    assert len(media) == 3
    media = remove_encrypted_media(media)
    assert len(media) == 1
    assert media[0].get('src') == 'http://example.com/3'



# Generated at 2022-06-14 15:27:50.236204
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    """ Test whether a f4m manifest is correctly downloaded """
    from .test_fragment import _prepare_handle, _prepare_test

    test_url = 'http://vodhss-i.akamaihd.net/hss/storage/exp=1399407300~acl=/*~hmac=51a1c0b2c7a8d91e1ad05329c5e2587c7554cda9d9590036caf084e3c3b547a2/vod/mp4:BigBuckBunny_115k.m4v/manifest.f4m'
    # mock a ytdl instance
    ytdl_obj = _prepare_test()
    # mock a downloader
    fake_down = Downloader(ytdl_obj)
    #

# Generated at 2022-06-14 15:28:00.476975
# Unit test for function build_fragments_list
def test_build_fragments_list():
    def test(case, res):
        assert build_fragments_list(case) == res

    test({
        'segments': [{
            'segment_run': [
                (0, 2),
                (1, 3)
            ]
        }],
        'fragments': [{
            'fragments': [
                {'first': 1},
                {'first': 4},
                {'first': 7},
                {'first': 10},
            ]
        }],
    }, [(0, 1), (0, 2), (1, 3), (1, 4), (1, 5), (1, 6)])



# Generated at 2022-06-14 15:28:11.511356
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:28:15.516477
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    data = b'\x00\x00\x00\x20' + b'abst' + (b'\x00' * 32)
    box_size, box_type, box_data = FlvReader(data).read_box_info()
    assert box_type == b'abst'
    assert box_size == 32
    assert len(box_data) == 28

# Generated at 2022-06-14 15:29:01.276573
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:29:13.219583
# Unit test for function build_fragments_list
def test_build_fragments_list():
    def _assert_fragments_list(boot_info, expected_fragments_list):
        assert build_fragments_list(boot_info) == expected_fragments_list

    # Test for non-live stream

# Generated at 2022-06-14 15:29:21.173967
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    flv_reader = FlvReader(open('test.bootstrap', 'rb').read())

# Generated at 2022-06-14 15:29:31.586678
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    import zlib

# Generated at 2022-06-14 15:29:36.385091
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    def read_abst(b64data):
        data = compat_b64decode(b64data)
        return FlvReader(data).read_abst()

# Generated at 2022-06-14 15:29:45.956467
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    xml_text = '''
    <manifest>
      <media id="1" bootstrapInfoId="bootstrap1" drmAdditionalHeaderSetId="additional-header-set-id" drmAdditionalHeaderId="additional-header-id" url="header.abst" bitrate="1">
      </media>
      <media id="2" bootstrapInfoId="bootstrap2" url="header.abst" bitrate="1">
      </media>
    </manifest>
    '''
    root = compat_etree_fromstring(xml_text)
    media = root.findall('media')
    remove_encrypted_media(media)
    assert len(media) == 1
    assert media[0].attrib['id'] == '2'

# Generated at 2022-06-14 15:29:56.340677
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from ..utils import encode_data_uri
    from ..extractor.common import InfoExtractor


# Generated at 2022-06-14 15:30:02.308591
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    url =  'https://s3.amazonaws.com/video-content.ec2.aws.xlib.ch/sample_a.f4m'
    ydl = YoutubeDL()
    ydl.params['writedescription'] = True
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(F4mFD() )
    ydl.prepare_filename( { 'url': url} )
    result = ydl.extract_info(url)
    return result

if __name__ == '__main__':
    print(test_F4mFD_real_download())

# Generated at 2022-06-14 15:30:12.857038
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:30:17.957111
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    from nose.tools import eq_
    data = b'\x00\x00\x00\x0C' + b'test' + b'\x00' * 14
    reader = FlvReader(data)
    eq_(reader.read_box_info(), (16, b'test', b'\x00' * 8))



# Generated at 2022-06-14 15:31:20.904849
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    import unittest
    import os
    test_file = os.path.join(os.path.dirname(__file__), 'test_data', 'asrt_test')
    _, box_type, box_data = FlvReader(open(test_file, 'rb').read()).read_box_info()
    assert box_type == b'asrt'
    segment_run = FlvReader(box_data).read_asrt()
    test_cases = [
        (0, 0, 1, 1),
        (1, 8, 9, 1),
        (9, 16, 17, 1),
        (17, 24, 25, 1),
        (25, 32, 33, 1),
        (33, 40, 41, 1),
        (41, 48, 49, 1),
    ]

# Generated at 2022-06-14 15:31:30.962012
# Unit test for function build_fragments_list
def test_build_fragments_list():
    test_boot_info = {
        'segments': [{
            'segment_run': [(0, 3)],
        }],
        'fragments': [{
            'fragments': [
                {'first': 0},
                {'first': 3},
                {'first': 6},
            ],
        }],
    }
    assert build_fragments_list(test_boot_info) == [
        (0, 0), (0, 1), (0, 2), (0, 3),
        (0, 4), (0, 5), (0, 6), (0, 7),
        (0, 8),
    ]


# Generated at 2022-06-14 15:31:42.673938
# Unit test for method read_abst of class FlvReader

# Generated at 2022-06-14 15:31:47.621020
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    flv_bin_file = open('test_cases/video_bootstrap.bin', 'rb')
    flv_reader = FlvReader(flv_bin_file.read())
    flv_reader.read_bootstrap_info()
    flv_bin_file.close()



# Generated at 2022-06-14 15:31:59.060726
# Unit test for method real_download of class F4mFD

# Generated at 2022-06-14 15:32:06.326340
# Unit test for function build_fragments_list
def test_build_fragments_list():
    # http://ondemand.nbcnews.com/video/nbcnews/newsy/120430/nbcnewsy-120430-traveling-with-nbc-news-ptsd-lisa-myers-16x9-1024x576.flv
    bitrates = [150, 750, 1000, 1500, 2500, 5000, 10000]
    abr_count = len(bitrates)
    abr_fragments_count = 180
    fragments = []
    segment_run_table = {
        'first_segment': 0,
        'fragments_per_segment': 1,
        'segment_run': [(0, abr_fragments_count * abr_count)]}

    fragment_run_entry_table = []

# Generated at 2022-06-14 15:32:16.748906
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    import base64
