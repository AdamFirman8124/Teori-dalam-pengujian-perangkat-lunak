

# Generated at 2022-06-14 15:22:49.902238
# Unit test for method read_bootstrap_info of class FlvReader

# Generated at 2022-06-14 15:22:56.526067
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    # Test file created according to the spec described in
    # https://www.adobe.com/devnet/f4v.html#seg_table
    asrt_data = compat_b64decode(br'''
            AAAkAAAAQQAAAAgAAAAAACAAADAAAAAQAAAAAAAAAAAAAAABYAsrVFvcgMi2Q==
            ''')

    segments = FlvReader(asrt_data).read_asrt()
    assert segments['segment_run'] == [
        (0, 0), (1, 3), (4, 4), (8, 1), (9, 0), (9, 1), (10, 0)
    ]

# Generated at 2022-06-14 15:23:07.792295
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    xml_str = open("tests/test_data/f4m_read_asrt.xml", "rb").read()
    tree = compat_etree_fromstring(xml_str)
    box_data = fix_xml_ampersands(xml_str).encode('utf-8')

    reader = FlvReader(box_data)
    segments = reader.read_asrt()['segment_run']

    expected = [
        (0, xpath_text(tree, 'segment_run_table/segment_run_entry[1]/@first_segment')),
        (1, xpath_text(tree, 'segment_run_table/segment_run_entry[2]/@fragments_per_segment')),
    ]
    assert segments == expected

# Generated at 2022-06-14 15:23:17.281792
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    from xml.etree import ElementTree as ET
    media1 = ET.Element('media')
    media1.attrib['url'] = 'http://example.com/media1.ts'
    media2 = ET.Element('media')
    media2.attrib['url'] = 'http://example.com/media2.ts'
    media2.attrib['drmAdditionalHeaderId'] = '1'
    media3 = ET.Element('media')
    media3.attrib['url'] = 'http://example.com/media3.ts'
    media3.attrib['drmAdditionalHeaderSetId'] = '1'
    media4 = ET.Element('media')
    media4.attrib['url'] = 'http://example.com/media4.ts'

# Generated at 2022-06-14 15:23:20.891772
# Unit test for method read_string of class FlvReader
def test_FlvReader_read_string():
    # build a string to test
    string_data = b'abc\x00'
    reader = FlvReader(string_data)
    string = reader.read_string()
    assert string == b'abc'



# Generated at 2022-06-14 15:23:32.782592
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    data_str = (
        b'\x00\x00\x00\x00\x00\x00\x00\xFF'
        b'\x00\x00\x00\x00\x00\x00\x00\x4A'
        b'\x00\x00\x00\x00\x00\x00\x00\x1B'
    )
    data = FlvReader(data_str)

    segment_data = data.read_asrt()
    assert len(segment_data['segment_run']) == 2

    # First segment
    assert segment_data['segment_run'][0][0] == 255
    assert segment_data['segment_run'][0][1] == 74

    # Second segment

# Generated at 2022-06-14 15:23:44.599885
# Unit test for method read_asrt of class FlvReader
def test_FlvReader_read_asrt():
    assert FlvReader(
        b'\x00\x00\x00\x1b\x61\x73\x72\x74\x01\x00\x00\x00\x00\x01\x00\x00\x00\x0b\x65\x6e\x67\x69\x73\x68\x5f\x63\x64\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    ).read_asrt() == {
        'segment_run': [(0, 11)],
    }



# Generated at 2022-06-14 15:23:54.355674
# Unit test for function get_base_url
def test_get_base_url():
    manifest = compat_etree_fromstring(fix_xml_ampersands(
        """
        <manifest xmlns="http://ns.adobe.com/f4m/1.0">
        </manifest>
        """
    ))
    assert get_base_url(manifest) is None

    manifest = compat_etree_fromstring(fix_xml_ampersands(
        """
        <manifest xmlns="http://ns.adobe.com/f4m/1.0">
            <baseURL>http://example.com/</baseURL>
        </manifest>
        """
    ))
    assert get_base_url(manifest) == 'http://example.com/'


# Generated at 2022-06-14 15:24:04.178893
# Unit test for method read_afrt of class FlvReader

# Generated at 2022-06-14 15:24:14.933011
# Unit test for function get_base_url
def test_get_base_url():
    # Test for normal case
    manifest = fix_xml_ampersands(compat_etree_fromstring('''
        <manifest xmlns="http://ns.adobe.com/f4m/1.0">
          <baseURL>base/</baseURL>
        </manifest>
    '''))
    assert 'base/' == get_base_url(manifest)

    # Test for <baseURL>2.0</baseURL>
    manifest = fix_xml_ampersands(compat_etree_fromstring('''
        <manifest xmlns="http://ns.adobe.com/f4m/2.0">
          <baseURL>base/</baseURL>
        </manifest>
    '''))
    assert 'base/' == get_base_url(manifest)

    #

# Generated at 2022-06-14 15:25:32.341369
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:25:42.900028
# Unit test for method read_abst of class FlvReader
def test_FlvReader_read_abst():
    # This test assumes that the sample file was downloaded from the URL in
    # the extractor
    with open('c:/shuati/f4v/sample.abst', 'rb') as f:
        box_data=f.read()
        bootstrap_info = FlvReader(box_data).read_abst()

# Generated at 2022-06-14 15:25:44.906958
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    unit = F4mFD()
    unit.real_download(None, None)


# Generated at 2022-06-14 15:25:54.810376
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    # Setup
    _TO_SCREEN = ['to_screen']
    _INFO_DICT = [{'url': 'http://example.com/manifest.f4m'}]
    data = {'_PREPARE_FRAG_DOWNLOAD': _PREPARED_FRAG_DOWNLOAD_MOCK_DATA,
            'ydl': {'urlopen': urlopen,
                    'params': {'hls_use_mpegts': False}},
            '_download_fragment': lambda *args: (True, b'')}
    f4mfd = F4mFD(**data)
    f4mfd.to_screen = lambda *args: _TO_SCREEN.pop(0)

    # Execution

# Generated at 2022-06-14 15:26:04.072855
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import io, sys
    sys.stdout = io.StringIO()
    ydl = YoutubeDL()
    ydl.params['noplaylist'] = True
    f = F4mFD(ydl)
    f.real_download("test.mp4", {"url": 'http://127.0.0.1:8080/test.f4m'})
    assert sys.stdout.getvalue() == '[f4m] Downloading f4m manifest\n'
    


# Generated at 2022-06-14 15:26:12.018895
# Unit test for function build_fragments_list

# Generated at 2022-06-14 15:26:23.492898
# Unit test for function build_fragments_list
def test_build_fragments_list():
    assert build_fragments_list({
        'segments': [{
            'segment_run': [
                (0, 1),
            ],
        }],
        'fragments': [{
            'fragments': [
                {'first': 3, 'ts': 0, 'duration': 0, 'discontinuity_indicator': None},
            ],
        }],
        'live': False,
    }) == [(0, 3)]


# Generated at 2022-06-14 15:26:35.137001
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    input = """
    <media href="manifest-media0.abst" qualityLevels="1" bitrate="1298000">
        <metadata>
            <id>00000</id>
        </metadata>
        <drmAdditionalHeaderId>1000000000</drmAdditionalHeaderId>
        <drmAdditionalHeaderSetId>0</drmAdditionalHeaderSetId>
        <segmentUrl media="manifest-media0.f4f" />
    </media>
    """
    expected_output = """
    <media href="manifest-media0.abst" qualityLevels="1" bitrate="1298000">
        <metadata>
            <id>00000</id>
        </metadata>
        <segmentUrl media="manifest-media0.f4f" />
    </media>
    """

    xml = remove_

# Generated at 2022-06-14 15:26:44.097422
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    from .extractor.common import InfoExtractor
    from .utils import encode_data_uri
    from .compat import str_to_bytes
    ie = InfoExtractor(params={}, downloader=None)
    ie.add_info_extractor(F4mIE.ie_key())
    ie.add_info_extractor(M3u8IE.ie_key())
    ie.add_info_extractor(Aes128EcbDecrypter.ie_key())
    ie.add_info_extractor(AdobePassIE.ie_key())
    ie.add_info_extractor(TveIE.ie_key())
    ie.add_info_extractor(OoyalaIE.ie_key())
    ie.add_info_extractor(Md5Checker.ie_key())

    # Test

# Generated at 2022-06-14 15:26:50.962069
# Unit test for function build_fragments_list
def test_build_fragments_list():
    from ..compat import compat_str


# Generated at 2022-06-14 15:31:22.995568
# Unit test for method read_box_info of class FlvReader
def test_FlvReader_read_box_info():
    import six
    import zlib
    assert zlib  # get rid of pyflakes warning
    if six.PY2:
        from binascii import a2b_hex
    else:
        from binascii import unhexlify as a2b_hex
    data = a2b_hex(b'0000004381637673000000000000000000000000000000000000000101000000')
    reader = FlvReader(data)

# Generated at 2022-06-14 15:31:35.289719
# Unit test for function write_metadata_tag
def test_write_metadata_tag():
    from .fragment import FragmentFD
    from ..utils import sanitize_xml


# Generated at 2022-06-14 15:31:47.762464
# Unit test for function remove_encrypted_media
def test_remove_encrypted_media():
    ENCRYPTED_MEDIA = '''<media bootstrapInfoId="1234" bitrate="4608"
                                 drmAdditionalHeaderId="5678"
                                 drmAdditionalHeaderSetId="9101"
                                 height="360"
                                 id="17101"
                                 joint="JVTTE"
                                 lang="und"
                                 mimeType="video/mp4"
                                 url="http://c.brightcove.com/services/mobile/streaming/index/rendition.m3u8?assetId=1628927893001&amp;videoId=4029235957001&amp;pubId=2850251328001&amp;format=mpeg4"
                                 width="640"/>'''

# Generated at 2022-06-14 15:31:59.769725
# Unit test for method real_download of class F4mFD
def test_F4mFD_real_download():
    import os
    # Using the youtube britney spears womanizer video as input
    test_url = 'http://pdl.warnerbros.com/wbol/us/dd/med/moulin/MOULIN_ROUGE_EXTENDED_CUT/Moulin_Rouge_Extended_trailer_2_700.f4m'
    ydl = YoutubeDL()
    ydl.params['outtmpl'] = 'test/test_%(playlist_index)s/%(id)s-%(title)s.%(ext)s'
    ydl.params['format'] = 'best'
    # The following line is added by Ayushman
    ydl.params['forceduration'] = True
    ydl.params['forcetitle'] = True
    # ydl.params['verbose

# Generated at 2022-06-14 15:32:13.326450
# Unit test for function build_fragments_list
def test_build_fragments_list():
    # Test VOD
    boot_info = {
        'live': False,
        'fragments': [
            {
                'fragments': [
                    {
                        'discontinuity_indicator': None,
                        'duration': 4,
                        'first': 0,
                        'ts': 0
                    },
                    {
                        'discontinuity_indicator': None,
                        'duration': 4,
                        'first': 1,
                        'ts': 4
                    },
                    {
                        'discontinuity_indicator': None,
                        'duration': 4,
                        'first': 2,
                        'ts': 8
                    }
                ]
            }
        ],
        'segments': [
            {
                'segment_run': [(0, 3)]
            }
        ]
    }

# Generated at 2022-06-14 15:32:20.766641
# Unit test for method read_bootstrap_info of class FlvReader
def test_FlvReader_read_bootstrap_info():
    from ..utils import (
        encode_base_n,
    )
    import binascii
    testcases = ['tests/resources/bootstrap_info1.flv',
                 'tests/resources/bootstrap_info2.flv']
    for filename in testcases:
        f = open(filename, 'rb')
        data = f.read()
        start_offset = data.find(b'bootstrap_info')
        bootstrap_info_data = data[start_offset:]
        reader = FlvReader(bootstrap_info_data)
        info = reader.read_bootstrap_info()
        # print info
        # pprint.pprint(info)
        # print(encode_base_n(binascii.hexlify(reader.read()), 16, '0123456789abcdef'