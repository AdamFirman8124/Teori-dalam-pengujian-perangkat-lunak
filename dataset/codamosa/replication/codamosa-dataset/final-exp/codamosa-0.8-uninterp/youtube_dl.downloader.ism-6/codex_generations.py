

# Generated at 2022-06-14 15:48:15.031174
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    """
    IsmFD.real_download unit test.
    """
    pass



# Generated at 2022-06-14 15:48:27.371331
# Unit test for constructor of class IsmFD
def test_IsmFD():
    filename = 'test_file.ism'
    duration = 360
    bitrate = {'in_kbps': 1500}

# Generated at 2022-06-14 15:48:32.574673
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .ism import IsmFD

    # Test constructor of class IsmFD
    assert(IsmFD)

    # Test setting of FD_NAME to 'ism'
    assert('ism' == IsmFD.FD_NAME)


# Generated at 2022-06-14 15:48:39.656563
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        params = {
            'track_id': 1,
            'fourcc': 'H264',
            'duration': 30000,
            'timescale': 1,
            'language': 'und',
            'height': 2160,
            'width': 4096,
            'nal_unit_length_field': 4,
            'codec_private_data': '000000016764001FACD9001F0183F1FFC0000000168EBE3CB80'
        }
        write_piff_header(stream, params)

# Generated at 2022-06-14 15:48:51.159438
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:49:02.601128
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .downloader import FileDownloader
    from .extractor import YoutubeIE
    ydl = FileDownloader(params={
        u'youtube_include_dash_manifest': True,
        u'noplaylist': True,
        u'format': u'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'})
    ydl.add_info_extractor(YoutubeIE())
    url = 'https://www.youtube.com/watch?v=pk-SkZgvB5o'
    info = ydl.extract_info(url, download=False)

# Generated at 2022-06-14 15:49:03.873433
# Unit test for constructor of class IsmFD
def test_IsmFD():
    IsmFD({})


# Generated at 2022-06-14 15:49:15.070992
# Unit test for function extract_box_data
def test_extract_box_data():
    ftyp_payload = b'isml'  # major brand
    ftyp_payload += u32.pack(1)  # minor version
    ftyp_payload += b'piff' + b'iso2'  # compatible brands
    ftyp_box = box(b'ftyp', ftyp_payload)

    mvhd_payload = u64.pack(int(time.time()))
    mvhd_payload += u64.pack(int(time.time()))
    mvhd_payload += u32.pack(10000000)
    mvhd_payload += u64.pack(1000000)
    mvhd_payload += s1616.pack(1)  # rate
    mvhd_payload += s88.pack(1)  # volume
    mvhd_

# Generated at 2022-06-14 15:49:25.486396
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:49:32.716763
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import get_info_extractor
    from .common import InfoExtractor

    ie = get_info_extractor(IsmFD.ie_key())


# Generated at 2022-06-14 15:49:53.918809
# Unit test for constructor of class IsmFD
def test_IsmFD():
    info = {
        'fragments': [{'url': 'test'}, {'url': 'test'}],
        '_download_params': {
            'track_id': 'test',
            'fourcc': 'test',
            'duration': 'test',
            'timescale': 'test',
            'language': 'test',
            'height': 0,
            'width': 'test',
            'sampling_rate': 'test',
            'bits_per_sample': 'test',
            'channels': 'test',
            'codec_private_data': 'test',
            'nal_unit_length_field': 'test', 
            'test': True
        },
    }
    params = {}
    test = IsmFD(params)
    ret = test.real_download('test', info)

# Generated at 2022-06-14 15:50:02.476519
# Unit test for constructor of class IsmFD
def test_IsmFD():
    class test_IsmFD(IsmFD):
        is_test = True

    test_IsmFD.http_scheme = ['http', 'https', 'ftp']
    test_IsmFD.https_scheme = ['https', 'http']
    test_IsmFD.params = {
        'test': True
    }
    test_IsmFD.ydl = YoutubeDL()
    test_IsmFD.ydl.params = {
        'test': True,
        'verbose': True,
        'quiet': True
    }
    test_IsmFD.to_screen = lambda s, **k: sys.stdout.write(s)
    test_IsmFD.to_stderr = lambda s, **k: sys.stderr.write(s)
    test_IsmFD.report

# Generated at 2022-06-14 15:50:13.961521
# Unit test for method real_download of class IsmFD

# Generated at 2022-06-14 15:50:24.270433
# Unit test for function extract_box_data
def test_extract_box_data():
    box_sequence = (b'moov', b'trak', b'mdia', b'minf', b'stbl', b'stsd')

# Generated at 2022-06-14 15:50:31.399696
# Unit test for function extract_box_data
def test_extract_box_data():
    extract_box_data(b'\x00\x00\x00\x14ftyp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14moov\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14moov', (b'moov',))



# Generated at 2022-06-14 15:50:40.968699
# Unit test for constructor of class IsmFD
def test_IsmFD():
    pass

# Generated at 2022-06-14 15:50:53.527510
# Unit test for function write_piff_header
def test_write_piff_header():
    import tempfile
    with tempfile.NamedTemporaryFile() as tf:
        write_piff_header(tf, {
            'track_id': 1,
            'fourcc': 'AACL',
            'duration': 20000000,
            'sampling_rate': 44100,
            'channels': 2,
            'bits_per_sample': 16,
        })
        assert tf.tell() == 200
        tf.seek(0)
        # fmt: off

# Generated at 2022-06-14 15:51:01.482156
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    downloader = FakeYDL()
    ie_result = type(
        'FakeIE',
        (object, ),
        {'_type': 'dash', 'fragments': [{'url': 'http://example.com/data'}], '_download_params': {}})
    fd = IsmFD(downloader)
    success = fd.real_download('filename', ie_result)
    assert success is True
    assert len(ie_result._download_params) == 1
    assert ie_result._download_params['track_id'] is not None



# Generated at 2022-06-14 15:51:05.824766
# Unit test for function extract_box_data
def test_extract_box_data():
    box_sequence = (b'moov', b'trak', b'mdia', b'minf', b'stbl', b'stsd', b'mp4a')
    box_data = extract_box_data(open(__file__[:__file__.rindex('.')] + '.m4a', 'rb').read(), box_sequence)
    assert box_data[-1:] == b'\x20'



# Generated at 2022-06-14 15:51:14.584186
# Unit test for function write_piff_header
def test_write_piff_header():
    import struct
    piff_header = io.BytesIO()
    params = {'duration': None, 'sampling_rate': None, 'channels': None,
              'bits_per_sample': None, 'language': None, 'track_id': None,
              'width': None, 'height': None, 'fourcc': None}

    with assert_raises(AssertionError):
        write_piff_header(piff_header, params)
    params['duration'] = 0
    params['sampling_rate'] = 48000
    params['channels'] = 2
    params['bits_per_sample'] = 16
    params['language'] = 'und'
    params['track_id'] = 1
    params['width'] = 0
    params['height'] = 0
    params['fourcc'] = 'AACL'

# Generated at 2022-06-14 15:54:11.066728
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:54:20.390441
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import sys, os
    import zipfile

    # Variables for test
    test_real_download_url = "http://amssamples.streaming.mediaservices.windows.net/683f7e47-bd83-4427-b0a3-26a6c4547782/BigBuckBunny.ism/manifest"
    test_real_download_src_file_path = "BigBuckBunny.zip"

    with youtube_dl.YoutubeDL() as ydl:
        # download test_file if not already downloaded
        if not os.path.isfile(test_real_download_src_file_path):
            print("Downloading file " + test_real_download_src_file_path + " as it does not exist.")
            # TODO: find a better test file - this one does not work

# Generated at 2022-06-14 15:54:34.244644
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'sampling_rate': 44100,
        'duration': 1337 * 44100,
    }
    write_piff_header(stream, params)
    stream.close()

# Generated at 2022-06-14 15:54:35.991084
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass

# Generated at 2022-06-14 15:54:46.567985
# Unit test for function write_piff_header
def test_write_piff_header():
    from ..utils import _str_to_bytes
    _str_to_bytes_orig = _str_to_bytes

    def _str_to_bytes_mock(s):
        return s
    
    _str_to_bytes.__code__ = _str_to_bytes_mock.__code__
    
    sio = io.BytesIO()

# Generated at 2022-06-14 15:54:57.887852
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'mp4v',
        'duration': 5000,
        'timescale': 25000,
        'width': 640,
        'height': 360,
    }
    write_piff_header(stream, params)
    data = stream.getvalue()
    assert data[0:8] == b'\x00\x00\x01\x00ftyp'
    assert data[16:20] == b'moov'
    assert data[24:28] == b'mvhd'
    assert data[48:52] == b'trak'
    assert data[52:56] == b'tkhd'
    assert data[76:80] == b'mdia'

# Generated at 2022-06-14 15:55:11.150780
# Unit test for function write_piff_header
def test_write_piff_header():
    import StringIO
    params = dict(
        track_id=1,
        fourcc='H264',
        duration=1500000000,
        height=360,
        width=640,
        codec_private_data='0000000167640033ACD90D88901FFFF00013F91E3C803000003000168EBECB22C',
        timescale=10000000,
    )
    stream = StringIO.StringIO()
    write_piff_header(stream, params)

# Generated at 2022-06-14 15:55:20.329720
# Unit test for function extract_box_data
def test_extract_box_data():
    data = b'ftypisomisomiso2mp41freefreefreefree'
    box_sequence = (b'ftyp',)
    assert extract_box_data(data, box_sequence) == data[8:]
    box_sequence = (b'mp41',)
    assert extract_box_data(data, box_sequence) is None
    data = full_box(b'moov', 1, 0, box(b'mvhd', b'\x00' * 104))
    box_sequence = (b'moov', b'mvhd')
    assert extract_box_data(data, box_sequence) == b'\x00' * 104
    data = full_box(b'moov', 1, 0, full_box(b'mvhd', 1, 0, b'\x00' * 100))
    box

# Generated at 2022-06-14 15:55:33.753174
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .ism import IsmFD
    from .common import FragmentFD
    from ytdl.YoutubeDL import YoutubeDL
    from ytdl.extractor import gen_extractors

    ydl = YoutubeDL({'fragment_retries':100})
    gen_extractors(ydl)
    info_dict = dict(
        fragments=[
            dict(url='http://127.0.0.1/segment_1.ism/Seg0-Frag0'),
            dict(url='http://127.0.0.1/segment_1.ism/Seg0-Frag1'),
            dict(url='http://127.0.0.1/segment_1.ism/Seg0-Frag2'),
        ]
    )

# Generated at 2022-06-14 15:55:41.712320
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .fragment import FragmentFD
    from .http import HttpFD
    from .http import HttpFD


    opt_dict = {
        'url': 'http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism',
        'skip_unavailable_fragments': False,
        'test': False,
        'fragment_retries': 10,
        'is_live': False,
        'ignoreerrors': False,
        'format': 'mp4',
        'outtmpl': u'%(title)s.mp4',
        'nopart': False,
        'updatetime': False,
    }

    # Case 1: Test constructor of class IsmFD