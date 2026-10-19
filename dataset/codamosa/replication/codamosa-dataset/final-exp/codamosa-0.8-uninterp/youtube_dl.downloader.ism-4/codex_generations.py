

# Generated at 2022-06-14 15:48:25.890141
# Unit test for constructor of class IsmFD
def test_IsmFD():
    url = u'http://foo.com/file.ism'
    ismfd = IsmFD(url)
    assert ismfd.url == url
    assert ismfd.params == {'noprogress': True, 'nooverwrites': False}
    assert ismfd.ie_key() == 'ism'
    assert ismfd.IE_NAME == 'ism'
    assert ismfd.FD_NAME == 'ism'

    url = u'http://foo.com/file.ism?foo.bar=2'
    ismfd = IsmFD(url)
    assert ismfd.params == {'foo.bar': 2, 'noprogress': True, 'nooverwrites': False}


# Generated at 2022-06-14 15:48:36.103350
# Unit test for function write_piff_header
def test_write_piff_header():
    test_params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 1241059240,
        'timescale': 10000000,
        'language': 'eng',
        'height': 0,
        'width': 0,
        'codec_private_data': '1210'
    }

    piff_header = write_piff_header(io.BytesIO(), test_params)

# Generated at 2022-06-14 15:48:44.206465
# Unit test for constructor of class IsmFD
def test_IsmFD():
    stream_url = 'http://manifest.wvstreams.com/perf/VIDEO_NAME/VIDEO_NAME_manifest.ism'
    ydl = YoutubeDL({
        'format': 'ism',
        'outtmpl': 'VIDEO_NAME_%(format_id)s.mp4',
    })
    fd = IsmFD(ydl, {
        'url': stream_url,
        'ext': 'mp4',
    })
    assert isinstance(fd, IsmFD)

# Generated at 2022-06-14 15:48:54.508741
# Unit test for function write_piff_header
def test_write_piff_header():
    stream = io.BytesIO()
    params = {'track_id': 1, 'fourcc': 'H264', 'duration': 400, 'timescale': 10000000, 'codec_private_data': '01640028ffe1001467640028acd9b400d91432e1200089f27140400f400000168ebe901f00040001c0', 'width': 1920, 'height': 1080}
    write_piff_header(stream, params)
    stream.seek(0)
    assert stream.read(4) == b'\x00\x00\x00\x7c'
    assert stream.read(4) == b'ftyp'
    assert stream.read(4) == b'isml'

# Generated at 2022-06-14 15:49:08.000931
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    from .common import FileDownloader
    from .extractor import gen_extractors
    from .downloader import gen_extractor_classes
    from .youtube_dl.utils import (
        get_suitable_downloader,
        DownloadContext,
        FileDownloader
    )
    from .youtube_dl.utils import (
        encodeFilename,
    )

# Generated at 2022-06-14 15:49:16.227404
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    url = "http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/Manifest"
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    info_dict = ydl._parse_ism_manifest(url, u'http://playready.directtaps.net/smoothstreaming/SSWSS720H264/SuperSpeedway_720.ism/QualityLevels(1700000)/Fragments(video=0)', False)
    fd = IsmFD(url, ydl)
    fd.real_download(None, info_dict)


# Generated at 2022-06-14 15:49:16.936260
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    pass


# Generated at 2022-06-14 15:49:28.909194
# Unit test for function write_piff_header
def test_write_piff_header():
    def assert_list_similar(list1, list2, msg=None):
        try:
            assert len(list1) == len(list2)
        except:
            raise AssertionError(msg)

        try:
            assert all([x == y for x, y in zip(list1, list2)])
        except:
            raise AssertionError(msg)



# Generated at 2022-06-14 15:49:39.442784
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():

    ## IsmFD_TestCase is a subClass of YoutubeDL class
    ## self.to_screen => Used to print
    ## self.url => Used to generate a download request
    ## self.params => Used to set the download parameters
    ## TODO
    class IsmFD_TestCase(YoutubeDL):
        def __init__(self):
            YoutubeDL.__init__(self)
            self.result = None

        def to_screen(self, message, skip_eol=False):
            print(message)

        def urlopen(self, request):
            return compat_urllib_request.urlopen(request)

        def report_destination(self, filename):
            self.result = filename

    ## TODO
    ## create an instance of class IsmFD and give an url as parameter
    ## TODO

# Generated at 2022-06-14 15:49:52.012015
# Unit test for function write_piff_header
def test_write_piff_header():
    for track_id in (1, 65535):
        for fourcc in ('AACL', 'AVC1', 'H264'):
            for bits_per_sample in (8, 16, 24, 32):
                for sampling_rate in (8, 16, 32, 44100, 48000, 96000):
                    sample_rates = {
                        'AACL': (8, 16, 32, 44100, 48000, 96000),
                        'AVC1': (44100, 48000, 96000),
                        'H264': (44100, 48000, 96000),
                    }
                    if fourcc not in sample_rates or sampling_rate not in sample_rates[fourcc]:
                        continue
                    if fourcc == 'AACL' and bits_per_sample not in (8, 16):
                        continue

# Generated at 2022-06-14 15:50:12.762864
# Unit test for constructor of class IsmFD
def test_IsmFD():
    ydl = YoutubeDL(params={'forceurl':True})
    ydl.add_info_extractor(IsmFD() )
    ydl.prepare_filename( {'fragments': [ { 'url': 'http://example.com/test.ism/Fragments(video=2)'} ] } )
    ydl.download([ 'http://example.com/test.ism' ])


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:50:23.883924
# Unit test for function extract_box_data
def test_extract_box_data():
    box_sequence = ('moov', 'mvhd')

# Generated at 2022-06-14 15:50:32.687705
# Unit test for function write_piff_header
def test_write_piff_header():
    res = io.BytesIO()
    write_piff_header(res, {'fourcc': 'AVC1', 'codec_private_data': '000000016764001f9d9d8a401e9a000001b074410000', 'track_id': 1, 'duration': 416666666, 'sampling_rate': 44100, 'channels': 2, 'bits_per_sample': 16, 'height': 720, 'width': 1280})

# Generated at 2022-06-14 15:50:35.801606
# Unit test for constructor of class IsmFD
def test_IsmFD():
    t = IsmFD("http://playready.directtaps.net/smoothstreaming/SSWSS720H264PR/SuperSpeedway_720.ism/Manifest","test.ism")


# Generated at 2022-06-14 15:50:36.732001
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    assert False, "Not yet implemented"



# Generated at 2022-06-14 15:50:48.364170
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:50:59.077217
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .ism import IsmFD
    from .http import HttpFD

    def test_download(self, filename, info_dict):
        return True

    info_dict = {
        'url': 'http://example.com',
        'fragments': [{
            'url': 'http://example.com/seg1.ismc',
            'byterange': '300@0',
        }, {
            'url': 'http://example.com/seg2.ismc',
            'byterange': '400@0',
        }]
    }

    HttpFD.real_download = test_download

    IsmFD().download(info_dict['url'], info_dict)

# Generated at 2022-06-14 15:51:05.079749
# Unit test for constructor of class IsmFD
def test_IsmFD():
    from .http import HTTPFD
    http_fd = HTTPFD(params={})
    url = 'http://a.b.c/manifest(filter=test).ism'
    ism_fd = IsmFD(url, params={}, http_fd=http_fd)
    assert ism_fd.url == url
    assert ism_fd.params == {}
    assert ism_fd.http_fd == http_fd

# Generated at 2022-06-14 15:51:14.203331
# Unit test for constructor of class IsmFD
def test_IsmFD():
    # Create a new instance of class IsmFD
    ismFD = IsmFD()
    # Unit test for function _download_fragment
    ismFD._download_fragment(None, None, None)
    # Unit test for function _append_fragment
    ismFD._append_fragment(None, None)
    # Unit test for function _finish_frag_download
    ismFD._finish_frag_download(None)
    # Unit test for function _prepare_and_start_frag_download
    ismFD._prepare_and_start_frag_download(None)
    # Unit test for function download
    ismFD.download(None, None)

if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:51:24.738085
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    try:
        from ytdl.YoutubeDL import YoutubeDL
        ydl = YoutubeDL({})
        fd = IsmFD(ydl, {
            'url': 'urL',
            'manifest_url': 'manifest_url',
            'fragments': [{'url': 'url'}],
            'skip_unavailable_fragments': True,
            'fragment_retries': 0,
        })
        fd.real_download('filename', {'_download_params': {}, 'fragments': []})
    except Exception as ex:
        raise AssertionError(ex.message)



# Generated at 2022-06-14 15:51:56.092959
# Unit test for function write_piff_header
def test_write_piff_header():
    from ..utils import encode_data_uri
    from .smoothstreams import fakes_smoothstreams_m3u8
    from .dash import get_dash_manifest_headers, parse_dash_manifest

    contents = fakes_smoothstreams_m3u8.str().encode('utf-8')
    headers = get_dash_manifest_headers(FakeFileDownloader(contents))
    params = parse_dash_manifest(FakeFileDownloader(contents, headers))

    assert params is not None
    assert params['codecs'] == 'avc1.640028,mp4a.40.2'

    # Generate PIFF file fragment and test its contents
    with io.BytesIO() as file_stream:
        write_piff_header(file_stream, params)

# Generated at 2022-06-14 15:52:02.764111
# Unit test for function write_piff_header

# Generated at 2022-06-14 15:52:09.091429
# Unit test for constructor of class IsmFD
def test_IsmFD():
    fd = IsmFD(params={'f': 'mp4', 'test': True,
                       'fragment_base_url': 'http://test.test/test/test.ism/QualityLevels(3333)/Fragments(sstf=0)'},
               ydl=YoutubeDL(),
               format='mp4')


if __name__ == '__main__':
    test_IsmFD()

# Generated at 2022-06-14 15:52:19.266753
# Unit test for function write_piff_header
def test_write_piff_header():
    import unittest
    import io
    stream = io.BytesIO()

# Generated at 2022-06-14 15:52:30.365501
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:52:32.187527
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    fd = IsmFD()
    fd = fd(None, None)
    return fd.real_download(None, info_dict)


# Generated at 2022-06-14 15:52:43.654140
# Unit test for constructor of class IsmFD

# Generated at 2022-06-14 15:52:55.232719
# Unit test for function extract_box_data
def test_extract_box_data():
    box_data1 = extract_box_data(b'\x00\x00\x00\x01\x00\x00\x00\x01', [b'\x00\x00\x00\x01'])
    assert u32.unpack(box_data1)[0] == 1
    box_data2 = extract_box_data(b'\x00\x00\x00\x01\x00\x00\x00\x01', [b'\x00\x00\x00\x02', b'\x00\x00\x00\x01'])
    assert box_data2 is None

# Generated at 2022-06-14 15:53:04.491847
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import requests
    from .downloader import YoutubeDL
    from .extractor import get_info_extractor
    from .compat import compat_urllib_request
    from .utils import HEADRequest, urlopen
    from .extractor.http import HttpFD
    from .extractor.ism import (
        IsmFD,
        _append_fragment,
        _download_fragment,
        _finish_frag_download,
        _prepare_and_start_frag_download,
        extract_box_data,
        write_piff_header,
    )

    class FakeDict(object):
        pass
    info = FakeDict()
    info.report_warning = lambda msg: None
    info.report_error = lambda msg: None

# Generated at 2022-06-14 15:53:15.723031
# Unit test for method real_download of class IsmFD
def test_IsmFD_real_download():
    import io
    import pytest
    from ytdl.target import out

    class IsmFDStub(IsmFD):
        def _prepare_and_start_frag_download(self, ctx): pass
        def _download_fragment(self, ctx, fragment_url, info_dict): pass
        def _append_fragment(self, ctx, frag_content): pass
        def _finish_frag_download(self, ctx): pass

    def extract_box_data(data, box_sequence):
        return b''

    def write_piff_header(stream, params): pass

    out_stream = io.BytesIO()