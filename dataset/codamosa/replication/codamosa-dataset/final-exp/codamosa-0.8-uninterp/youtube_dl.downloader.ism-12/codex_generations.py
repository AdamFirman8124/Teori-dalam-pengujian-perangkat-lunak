

# Generated at 2022-06-14 15:48:21.185219
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass

# Generated at 2022-06-14 15:48:32.383468
# Unit test for function write_piff_header
def test_write_piff_header():
    b = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 100000,
        'timescale': 10000000,
        'language': 'und',
        'height': 0,
        'width': 0,
        'bits_per_sample': 16,
        'channels': 2,
        'sampling_rate': 44100,
    }
    write_piff_header(b, params)

# Generated at 2022-06-14 15:48:44.500335
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        params = dict(
            track_id=1,
            fourcc='MP4V',
            duration=100,
            width=100,
            height=100,
            codec_private_data='0000000167428029af2c81384',
        )
        write_piff_header(stream, params)
        stream.seek(0)

        assert stream.read(4) == b'\x00\x00\x00\x1e'  # ftyp size
        assert stream.read(4) == b'ftyp'  # ftyp type
        assert stream.read(4) == b'isml'  # major brand
        assert u32.unpack(stream.read(4))[0] == 1  # minor version
        assert stream.read(8)

# Generated at 2022-06-14 15:48:50.135136
# Unit test for function extract_box_data
def test_extract_box_data():
    filename = '../videoio/tests/data/test.ismv'
    with FragmentFD(filename) as f:
        data = f.read()
        uuid = extract_box_data(data, (b'uuid', b'piff', b'pssh'))
        uuid = uuid[16:32]
        assert binascii.hexlify(uuid) == b'9a04f07998404286ab92d65b8e8cea8a'

test_extract_box_data()

# Generated at 2022-06-14 15:48:59.639126
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:49:12.189058
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:49:13.457129
# Unit test for constructor of class IsmFD
def test_IsmFD():
    pass



# Generated at 2022-06-14 15:49:26.058757
# Unit test for function extract_box_data
def test_extract_box_data():
    box_sequence = (b'moov', b'trak', b'mdia', b'minf', b'stbl', b'stsd', b'avc1')

# Generated at 2022-06-14 15:49:33.492252
# Unit test for constructor of class IsmFD
def test_IsmFD():
    segment_urls = ["https://mysharedlink.com/s/s1.ism/Seg1-Frag1",
                    "https://mysharedlink.com/s/s1.ism/Seg1-Frag2",
                    "https://mysharedlink.com/s/s1.ism/Seg1-Frag3",
                    "https://mysharedlink.com/s/s1.ism/Seg1-Frag4",
                    "https://mysharedlink.com/s/s1.ism/Seg1-Frag5",
                    "https://mysharedlink.com/s/s1.ism/Seg1-Frag6"]

# Generated at 2022-06-14 15:49:35.722248
# Unit test for constructor of class IsmFD
def test_IsmFD():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:49:58.609744
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    stream = io.BytesIO()
    result = IsmFD.real_download(stream, 'mytest.mp4',  
        {'info_dict': {'_download_params': {'fourcc': 'H264',
                                            'codec_private_data': '000000016764001f9a9f01078ae5829d',
                                            'sampling_rate': 44100, 'track_id': 1,
                                            'duration': 9.88},
         'fragments': [{'url': 'https://mytest.akamaized.net/seg-1-v1-a1.h264.ts?sd=10&rebase=on'}]},
            'params': {'fragment_retries': 0, 'skip_unavailable_fragments' : True}})


# Generated at 2022-06-14 15:50:00.776344
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass

# ----------
# FragmentFD end
# ----------

# ----------
# DASHFD start
# ----------

# Generated at 2022-06-14 15:50:11.964227
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()


    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 12261497,
        'timescale': 90000,
        'height': 720,
        'width': 1280,
        'codec_private_data': '01640033ffe1001facb082c583580d18b83ddce0c99fa2b7e'
    }

    write_piff_header(stream, params)

# Generated at 2022-06-14 15:50:13.588230
# Unit test for constructor of class IsmFD
def test_IsmFD():
    print(IsmFD.FD_NAME)
    return IsmFD.FD_NAME

# Generated at 2022-06-14 15:50:18.761651
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    fd = IsmFD()
    ism_test_url = 'https://vid-ams.plex.tv/video/564/1416644533/1/master.m3u8'

    fd.real_download(ism_test_url, {})


if __name__ == '__main__':
    test_IsmFD_real_download()

# Generated at 2022-06-14 15:50:29.177576
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .downloader import FileDownloader
    from .extractor import gen_extractors

    dl = FileDownloader({})
    for ie in gen_extractors():
        if ie.ie_key() == 'generic':
            continue
        dl.add_info_extractor(ie)

    manifest_url = 'http://download.tsi.telecom-paristech.fr/gpac/DASH_CONFORMANCE/TelecomParisTech/mp4-live-mkv-avc-aac/mp4-live-mkv-avc-aac_silence.mpd'
    dl.params['force_generic_extractor'] = True

    dl.add_default_info_extractors()
    dl.download([manifest_url])


# Generated at 2022-06-14 15:50:34.903802
# Unit test for function extract_box_data
def test_extract_box_data():
    data = box('foo', box('bar', '123')) + box('baz', '456')
    assert extract_box_data(data, ['foo', 'bar']) == '123'
    assert extract_box_data(data, ['baz']) == '456'



# Generated at 2022-06-14 15:50:42.733052
# Unit test for function extract_box_data
def test_extract_box_data():
    from .fragment import FragmentFD
    from .piff import extract_box_data
    from .compat import urlopen
    from .common import UUID_RE, UUID_TEMPLATE

    uuid = '00000000000000000000000000000000'
    test_uuid = UUID_TEMPLATE % uuid
    url_1 = UUID_RE.sub(test_uuid, 'https://m.video.msn.com/watch/video/coming-of-age/1z00fhgkc')
    test_data = urlopen(url_1).read()
    sample_content_box = extract_box_data(test_data, (b'sidx', b'pssh', b'content'))

# Generated at 2022-06-14 15:50:55.652677
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import expect_download, pafy_module, video
    from .common import download_parameters
    from .common import video_data
    from .common import video_data
    from .common import video_info
    from .common import download_parameters
    from .common import download_parameters

    # Test with audio only.
    pafy_module.Pafy(video['audio_only']).getbestaudio().download()
    expect_download(download_parameters(video['audio_only'],
        video_data['audio_only']['bitrates']['65'], '0.mp4',
        video_info['audio_only']['formats'][1]),
        audio_only=True)

    # Test with video.

# Generated at 2022-06-14 15:51:03.605816
# Unit test for function write_piff_header
def test_write_piff_header():
    from io import BytesIO

    stream = BytesIO()
    params = {}
    params['track_id'] = 1
    params['fourcc'] = 'AACL'
    params['duration'] = 9
    params['timescale'] = 10000000
    params['channels'] = 2
    params['bits_per_sample'] = 16
    params['language'] = 'und'
    params['sampling_rate'] = 48000
    write_piff_header(stream, params)
    print(stream.getvalue())
    print(len(stream.getvalue()))
    assert len(stream.getvalue()) == 597



# Generated at 2022-06-14 15:51:34.452567
# Unit test for function extract_box_data
def test_extract_box_data():
    box_data = b'\x00\x00\x00\x00'  # unspecified size
    box_data += b'\x00\x00\x00\x00'  # unspecified type
    box_data += b'\x00\x00\x00\x00'  # unspecified size
    box_data += b'\x00\x00\x00\x01'  # type 1
    box_data += b'\x00\x00\x00\x08'  # size 8
    box_data += b'\x00\x00\x00\x02'  # type 2
    box_data += b'\x00\x00\x00\x08'  # size 8
    box_data += b'\x00\x00\x00\x03'  # type 3

# Generated at 2022-06-14 15:51:45.514839
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:51:57.499955
# Unit test for function write_piff_header
def test_write_piff_header():
    sizes = [(0, 1, 46), (0, 2, 47), (1, 1, 177), (1, 2, 178)]

    for is_audio, count, size in sizes:
        params = {
            'track_id': 1,
            'fourcc': 'H264' if not is_audio else 'AACL',
            'duration': 14084,
            'timescale': 12800,
            'language': 'und',
            'height': 0,
            'width': 0,
            'nal_unit_length_field': 4,
        }
        if is_audio:
            params.update({
                'sampling_rate': 48000,
                'channels': 2,
                'bits_per_sample': 16,
            })

# Generated at 2022-06-14 15:52:02.703131
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Test for constructor of class IsmFD
    # Create a IsmFD object with required parameters
    IsmFD('https://test.url/test.ism/manifest', params={})


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:52:14.147340
# Unit test for function extract_box_data
def test_extract_box_data():
    box_data = extract_box_data(b'\x00\x00\x00\x00' * 10, [b'ABCD', b'EFGH'])
    assert box_data is None
    box_data = extract_box_data(b'\x00\x00\x00\x00' * 10, [b'ABCD'])
    assert box_data == b'\x00\x00\x00\x00' * 6
    box_data = extract_box_data(b'\x00\x00\x00\x00' * 10, [b'ABCD', b'EFGH', b'IJKL'])
    assert box_data == b'\x00\x00\x00\x00' * 2



# Generated at 2022-06-14 15:52:25.733274
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Instantiate object
    IsmFDim = IsmFD("http://storage.googleapis.com/exoplayer-test-media-0/play.mp3")

    # Get protion of segments[0] for testing
    seg_0_content = IsmFDim.download("https://storage.googleapis.com/exoplayer-test-media-0/play.mp3",
                                     {'fragments': [{'url': "segment0000.hevc"}]})[1]

    # Create empty file
    with open("test_IsmFD_real_download\\test.ismv", "wb") as dest_stream:
        pass

    # Run real_download
    IsmFDim.filename = "test_IsmFD_real_download\\test.ismv"
    IsmFDim.real

# Generated at 2022-06-14 15:52:27.517083
# Unit test for function write_piff_header
def test_write_piff_header():
    assert write_piff_header(None, None) is None


# Generated at 2022-06-14 15:52:30.321204
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Segments are not downloaded in test mode
    res = IsmFD.real_download(None, '', {'fragments': [{'url': '?'}]})
    assert res == True



# Generated at 2022-06-14 15:52:39.983158
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.open('tests/piff_header_test.piff', 'rb') as expected_stream, \
            io.BytesIO() as stream:
        params = {
            'track_id': 1,
            'fourcc': 'AVC1',
            'duration': 542260000,
            'width': 1280,
            'height': 720,
            'codec_private_data': '0164001fffe100186764001fa4034c0101fffe1001867640016d90f001467640016d6017c0048b4f6d4d8000001840000000168ea02e3',
        }
        write_piff_header(stream, params)
        assert stream.getvalue() == expected_stream.read()

TRAF_DATA_OFFSET = 0x1

# Generated at 2022-06-14 15:52:51.472864
# Unit test for constructor of class IsmFD
def test_IsmFD():
    print("Downloading the sub title file")