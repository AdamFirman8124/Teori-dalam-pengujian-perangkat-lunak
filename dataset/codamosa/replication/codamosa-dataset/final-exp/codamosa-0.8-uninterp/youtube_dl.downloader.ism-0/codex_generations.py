

# Generated at 2022-06-14 15:48:24.620870
# Unit test for function write_piff_header
def test_write_piff_header():
    # Create the output stream
    fout = io.BytesIO()
    # Write the PIFF header into the stream
    write_piff_header(fout, {
        'track_id': 1,
        'fourcc': 'AVC1',
        'duration': 1291708,
        'timescale': 10000000,
        'language': 'eng',
        'height': 1080,
        'width': 1920,
        'nal_unit_length_field': 4,
        'codec_private_data': '01640029ffe100166764001ffe1001c97000001fca000001fda000001ff00ecef9d0e0b0',
    })
    # Return the result
    return fout.getvalue()

# Assert that the unit test passed

# Generated at 2022-06-14 15:48:35.135742
# Unit test for function write_piff_header
def test_write_piff_header():
    test_video_params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 10000,
        'timescale': 10000,
        'height': 576,
        'width': 720,
        'codec_private_data': '000000016742802995E030033AC9D404014C4F40',
    }
    test_audio_params = {
        'track_id': 2,
        'fourcc': 'AACL',
        'duration': 100000,
        'timescale': 1000,
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 100000,
    }
    buf = io.BytesIO()
    write_piff_header(buf, test_video_params)
   

# Generated at 2022-06-14 15:48:36.208503
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Constructor test
    IsmFD()

# Generated at 2022-06-14 15:48:48.265866
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Test parameters
    params = {
        'test': True,
        'fragment_retries': 1,
        'skip_unavailable_fragments': False,
    }

    # Test input and expected output
    params['_download_params'] = {
        'fourcc': 'avc1',
        'track_id': 1,
        'duration': 400,
        'height': 0,
        'width': 0,
        'sampling_rate': 44100,
        'channels': 2,
        'bits_per_sample': 16,
    }


# Generated at 2022-06-14 15:48:57.955525
# Unit test for function extract_box_data
def test_extract_box_data():
    data = b'\x00\x00\x00\x2c' + b'moov' + \
           b'\x00\x00\x00\x28' + b'mvhd' + \
           b'\x00\x00\x00\x2c' + b'moov' + \
           b'\x00\x00\x00\x2c' + b'mvhd'  # mvhd is a box of type moov
    assert extract_box_data(data, (b'mvhd',)) == data[20:28]
    assert extract_box_data(data, (b'moov', b'mvhd')) == data[32:40]
test_extract_box_data()



# Generated at 2022-06-14 15:49:11.022266
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:49:24.625699
# Unit test for function extract_box_data

# Generated at 2022-06-14 15:49:31.378605
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    #test_IsmFD_real_download
    """test class IsmFD"""
    from . import FileDownloader
    from .extractor import common

    class FakeSanitizedFileDownloader(object):
        pass


# Generated at 2022-06-14 15:49:43.782909
# Unit test for function extract_box_data
def test_extract_box_data():
    from .test import fake_http_get
    moov_data = fake_http_get('test_data/test_dash_init.mp4')
    assert len(moov_data) == 64

# Generated at 2022-06-14 15:49:49.140558
# Unit test for constructor of class IsmFD
def test_IsmFD():
    qq_IsmFD = IsmFD('http://xxx.mp4', 'test_out.mp4', {'protocol': 'm3u8_native', 'ext': 'mp4'})
    print(qq_IsmFD.FD_NAME)
    print(qq_IsmFD.params)
#test_IsmFD()

# Generated at 2022-06-14 15:50:07.865274
# Unit test for constructor of class IsmFD
def test_IsmFD():
    info_dict = {
        '_type': 'IsmFD',
        'fragments': [
            {
                'url': 'http://i.cdn.turner.com/nba/big/video/dev/hls_minimal/nba_2013_01_31_bos_lac_hls_minimal_1800.ism/nba_2013_01_31_bos_lac_hls_minimal_1800-frag1000'
            }
        ]
    }
    ismFD = IsmFD(info_dict)
    filename = 'test'
    returned_info_dict = ismFD.real_download(filename, info_dict)
    print('returned_info_dict: ', returned_info_dict)
    assert returned_info_dict



# Generated at 2022-06-14 15:50:16.913694
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()

# Generated at 2022-06-14 15:50:27.251200
# Unit test for function write_piff_header
def test_write_piff_header():
    data = io.BytesIO()
    params = {}
    params['track_id'] = 1
    params['fourcc'] = 'H264'
    params['duration'] = 12345678900000
    params['timescale'] = 10000000
    params['channels'] = 2
    params['bits_per_sample'] = 16
    params['sampling_rate'] = 44100
    params['language'] = 'eng'
    params['height'] = 720
    params['width'] = 1280
    params['codec_private_data'] = '0164001fffe1002a27428080aacf8080808080808080'
    write_piff_header(data, params)

# Generated at 2022-06-14 15:50:31.609889
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    assert (True)



# Generated at 2022-06-14 15:50:41.040668
# Unit test for function write_piff_header
def test_write_piff_header():
    import binascii
    i = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 10000000,
        'timescale': 10000000,
        'language': 'und',
        'height': 576,
        'width': 1024,
        'codec_private_data': '0142C018FFE100188A9A9B9C0B4C4E4E4F526F665BEDE3C0BA2B2B3B4C4D4E4F678D2E2',
    }
    write_piff_header(i, params)

# Generated at 2022-06-14 15:50:42.093582
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
	assert True



# Generated at 2022-06-14 15:50:46.561052
# Unit test for constructor of class IsmFD
def test_IsmFD():
    print('TEST 1: Testing IsmFD [only constructor].\n')
    ismfd = IsmFD('', {})

# Commented out due to downloading of video files and failing on subsequent tests (network slow)
# test_IsmFD()

# Generated at 2022-06-14 15:50:58.837018
# Unit test for function write_piff_header
def test_write_piff_header():
    # audio-only PIFF header
    fd = io.BytesIO()
    write_piff_header(fd, {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 20000000,
        'timescale': 10000000,
        'sampling_rate': 48000,
        'channels': 2,
        'bits_per_sample': 16,
    })
    fd.seek(0)

# Generated at 2022-06-14 15:50:59.373921
# Unit test for constructor of class IsmFD
def test_IsmFD():
    pass



# Generated at 2022-06-14 15:51:10.300444
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():

    class IsmFD_case(IsmFD):
        def __init__(self, params):
            IsmFD.__init__(self, params)

        def _download_fragment(self, ctx, fragment_url, info_dict):
            if fragment_url == 'http://localhost:5000/segment1.dat':
                frag_content = b"\x01\x02\x03"
            elif fragment_url == 'http://localhost:5000/segment2.dat':
                frag_content = b"\x04\x05\x06"
            elif fragment_url == 'http://localhost:5000/segment3.dat':
                frag_content = b"\x07\x08\x09"
            else:
                self.report_error('Unexpected fragment url')
                return False, None

# Generated at 2022-06-14 15:51:31.189611
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    def _download_fragment(self, ctx, frag_url, filename, info_dict):
        ctx['fragment_id'] = frag_url[-12:-4]
        stream = compat_urllib_request.urlopen(frag_url)
        frag_content = stream.read()
        stream.close()
        return True, frag_content

    FilenameFD.real_download = IsmFD.real_download
    filename_fd = FilenameFD()
    filename_fd._download_fragment = lambda ctx, url, info_dict: _download_fragment(
        filename_fd, ctx, url, 'test.mp4', info_dict)
    filename_fd.params['batch_file'] = 'test.mp4'
    filename_fd.params['test'] = True
   

# Generated at 2022-06-14 15:51:42.908297
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .extractor import (
        get_info_extractor,
        list_extractors,
    )

    ie = get_info_extractor(
        list_extractors()[0],
    )

    def fake_download(
        _filename,
        _info_dict,
        segment_url,
        ie_params,
    ):
        """
        Fake _download_segment method of ie.
        """
        fs = io.BytesIO()
        # Write an empty tfhd box
        fs.write(u32.pack(16))
        fs.write(b'tfhd')
        fs.write(u8.pack(0))
        fs.write(u32.pack(0))
        fs.write(u32.pack(4))
        fs.write(u32.pack(0))


# Generated at 2022-06-14 15:51:55.146654
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:52:00.197444
# Unit test for function write_piff_header
def test_write_piff_header():
    f = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'VC-1',
        'duration': 10000000,
        'sampling_rate': 44100,
        'bits_per_sample': 16,
        'channels': 2,
        'height': 1080,
        'width': 1920,
        'codec_private_data': '01640028ffe10028676400286764002868e9c035130c0e58a0092c11010f138322c1',
        'nal_unit_length_field': 4,
    }
    write_piff_header(f, params)

# Generated at 2022-06-14 15:52:09.258877
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from ytdl.extractor import get_info_extractor
    from ytdl.YoutubeDL import YoutubeDL

    ydl = YoutubeDL({'format': 'ism/fragments'})
    ydl.add_info_extractor(get_info_extractor('ism'))
    info_dict = ydl.extract_info('https://account.wmcloud.com/content/status-codes', download=False)
    ism_fd = IsmFD(ydl, {})
    ism_fd.real_download('', info_dict)
    pass


# Generated at 2022-06-14 15:52:19.368464
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import os

    import youtube_dl.YoutubeDL
    import youtube_dl.extractor.fragment
    import downloader
    import extractor
    import fragment
    import postprocessor
    import InfoExtractor

    class YoutubeDL(youtube_dl.YoutubeDL):
        def __init__(self, *args, **kargs):
            super(YoutubeDL, self).__init__(*args, **kargs)
            self.to_stderr = lambda *args, **kargs: None

    class _Downloader(downloader.Downloader):
        def __init__(self, *args, **kargs):
            super(_Downloader, self).__init__(*args, **kargs)
            self.to_screen = lambda *args, **kargs: None

# Generated at 2022-06-14 15:52:30.457111
# Unit test for function write_piff_header
def test_write_piff_header():
    timescale = 10000000

# Generated at 2022-06-14 15:52:34.314058
# Unit test for constructor of class IsmFD
def test_IsmFD():
    url = 'http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest'
    ret = IsmFD(url)
    print(ret)


if __name__ == "__main__":
    test_IsmFD()
    pass

# Generated at 2022-06-14 15:52:45.299438
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    self = IsmFD()
    filename = 'D:\\Test\\filename.ism'
    info_dict = {'fragments': [{'url': 'fragment1.ismv'}, {'url': 'fragment2.ismv'}]}

    # unit test here
    #self._download_fragment = Mock(return_value=(True, 'tfhd'))
    #self._append_fragment = Mock(return_value=None)
    #self._finish_frag_download = Mock(return_value=False)
    #self._prepare_and_start_frag_download = Mock(return_value=None)
    #result = self.real_download(filename, info_dict)
    #if result is not False:
    #    raise AssertionError("IsmFD.real

# Generated at 2022-06-14 15:52:57.415590
# Unit test for method real_download of class IsmFD

# Generated at 2022-06-14 15:53:29.364220
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass  # TODO: write unit test



# Generated at 2022-06-14 15:53:40.103293
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from youtube_dl.extractor import YoutubeIE, FragmentFD
    from youtube_dl import YoutubeDL
    from urlparse import urlparse, parse_qs
    from .testutil import FakeYDL, FakeYDL
    ydl = FakeYDL()
    ie = YoutubeIE(ydl)
    ydl.add_info_extractor(ie)

# Generated at 2022-06-14 15:53:47.512338
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()

# Generated at 2022-06-14 15:53:58.814340
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # This is used to verify the expected outcome of the test
    # with arguments defined below.
    class FakeArgs(object):
        pass
    args = FakeArgs()
    args.fragment_retries = 1
    args.skip_unavailable_fragments = True

    # This is used to simulate the behavior of --test.
    args.test = True

    # This is used to simulate the behavior of --daterange.
    args.daterange = None

    # This is used to simulate the behavior of --match_filter.
    args.match_filter = None

    # This is used to simulate the behavior of --yes_playlist.
    args.yes_playlist = None

    # This is used to simulate the behavior of --recode_video.
    args.recode_video = None

    # This is used to simulate the

# Generated at 2022-06-14 15:54:08.722159
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import re

    enc_name = 'ism_enc'
    dec_name = 'test.mp4'
    enc_file_path = os.path.join(os.getcwd(), enc_name)
    dec_file_path = os.path.join(os.getcwd(), dec_name)
    # TODO
    # url = 'http://d3l4st8pog0zua.cloudfront.net/sintel-1024-surround.ism/Manifest'
    url = 'http://download.tsi.telecom-paristech.fr/gpac/DASH_CONFORMANCE/TelecomParisTech/mp4-live/mp4-live-mpd-AV-BS.mpd'

# Generated at 2022-06-14 15:54:09.408392
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass

# Generated at 2022-06-14 15:54:19.124516
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Generate mock object
    params = {"_cmd_downloader_handle": None, "_cmd_socket": "127.0.0.1", "_cmd_version": int('0x0403', 16),
              "_cmd_uuid": "ab028f9e-b4c4-44d4-8e8c-5b0d0ed5f736", "_cmd_tmp_filename": "tmp.ism",
              "_cmd_save_filename": "media.ism", "_cmd_keep_tmp_files": "False",
              "_cmd_target_stream": ["http://1.2.3.4:8080/data/ism/"], "_cmd_live": "False", "_cmd_live_buffer": 30}


# Generated at 2022-06-14 15:54:19.748458
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass

# Generated at 2022-06-14 15:54:33.013825
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    # Test with ISM manifest
    url = 'https://amssamples.streaming.mediaservices.windows.net/91492735-c523-432b-ba01-faba6c2206a2/AzureMediaServicesPromo.ism/manifest(format=m3u8-aapl)'
    # Run video.py and download the video
    filename = 'AzureMediaServicesPromo.ism'
    ydl = YoutubeDL({'outtmpl': filename})
    result = ydl.extract_info(url)
    ctx = {
        'filename': filename,
        'total_frags': 1,
        'frag_index': -1
    }

# Generated at 2022-06-14 15:54:41.819262
# Unit test for constructor of class IsmFD
def test_IsmFD():
    module = IsmFD()

    # Test empty dictionary
    parsed = module.parse_ism_url({})
    assert parsed is None

    # Test missing manifest URL
    parsed = module.parse_ism_url({'format_id': '1'})
    assert parsed is None

    # Test working manifest URL
    manifest_url = 'http://www.dailymotion.com/cdn/manifest/video/x2m0yjm.ism'
    parsed = module.parse_ism_url({'url': manifest_url, 'ext': 'mp4'})
    assert 'protocol' in parsed
    assert parsed['protocol'] == 'mss'



# Generated at 2022-06-14 15:55:28.153856
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass


# Generated at 2022-06-14 15:55:35.705713
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        write_piff_header(stream, {
            'track_id': 0x1,
            'fourcc': 'H264',
            'duration': 1000,
            'height': 1080,
            'width': 1920,
            'nal_unit_length_field': 4,
            'codec_private_data': '01640033ACD4011F7D8032046F00',
        })
        stream.seek(0)
        print(binascii.hexlify(stream.read()))



# Generated at 2022-06-14 15:55:38.459040
# Unit test for constructor of class IsmFD
def test_IsmFD():
    ismFD = IsmFD(None, None, None)
    # FD_NAME has not been set to invalid value
    assert ismFD.FD_NAME == 'ism'

# unit test for real_download() of class IsmFD

# Generated at 2022-06-14 15:55:40.988427
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})

if __name__ == '__main__':
    test_IsmFD_real_download()

# Generated at 2022-06-14 15:55:52.149544
# Unit test for function write_piff_header
def test_write_piff_header():
    def piff_header_test(params):
        stream = io.BytesIO()
        write_piff_header(stream, params)
        return stream.getvalue()
    mdat = piff_header_test(
        {'track_id': 1, 'fourcc': 'mp4a', 'sampling_rate': 44100, 'channels': 2, 'duration': 10})

# Generated at 2022-06-14 15:56:01.129598
# Unit test for constructor of class IsmFD
def test_IsmFD():

    # Test segment
    url = "https://pilgrim-videos-output-staging.s3.amazonaws.com/2b2c33df-f824-4a68-a2e2-d1833dc0522a/400k.ism/QualityLevels(400000)/Fragments(video=0)"

    # Test info_dict

# Generated at 2022-06-14 15:56:11.382227
# Unit test for function write_piff_header
def test_write_piff_header():
    with io.BytesIO() as stream:
        write_piff_header(stream, {
            'track_id': 1,
            'fourcc': 'H264',
            'duration': 3600,
            'timescale': 10000000,
            'codec_private_data': '0164001fffe100176764001facd9c800100000030080000003008000001f40000b00000001000000012000c48d8800000160e7a0a00f000c7f2e0e00f00',
            'width': 1280,
            'height': 720,
        })
        data = stream.getvalue()

# Generated at 2022-06-14 15:56:16.071316
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    selfMock = IsmFD()
    result = selfMock.real_download("filename", "info_dict")
    return result

if __name__ == "__main__":
    # Usage : python test_IsmFD.py
    # python -m unittest test_IsmFD
    test_IsmFD_real_download()

# Generated at 2022-06-14 15:56:17.572708
# Unit test for constructor of class IsmFD
def test_IsmFD():
    ismFD = IsmFD()
    assert(ismFD.__class__.__name__ == IsmFD.__name__)

# Generated at 2022-06-14 15:56:27.609982
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    class TestIsmFD(IsmFD):
        def _download_fragment(self, ctx, segment_url, info_dict):
            if count == fragment_retries:
                raise compat_urllib_error.HTTPError(segment_url, 403, 'Forbidden', None, None)
            else:
                return True, b''

        def _append_fragment(self, ctx, fragment_data):
            pass
