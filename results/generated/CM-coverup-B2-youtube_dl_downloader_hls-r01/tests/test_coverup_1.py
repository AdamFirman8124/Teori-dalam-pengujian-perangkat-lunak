# file: project/youtube_dl/downloader/hls.py:60-216
# asked: {"lines": [61, 62, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 107, 108, 109, 112, 114, 115, 116, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 178, 179, 180, 181, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 209, 210, 211, 212, 214, 216], "branches": [[68, 69], [68, 80], [69, 70], [69, 72], [76, 77], [76, 78], [91, 92], [91, 106], [93, 94], [93, 95], [95, 96], [95, 101], [96, 97], [96, 98], [98, 99], [98, 100], [101, 102], [101, 104], [120, 121], [120, 122], [128, 129], [128, 214], [130, 128], [130, 131], [131, 132], [131, 187], [132, 133], [132, 134], [135, 136], [135, 137], [141, 142], [141, 143], [145, 146], [145, 147], [147, 148], [147, 162], [151, 152], [151, 153], [160, 147], [160, 161], [162, 163], [162, 171], [163, 164], [163, 168], [171, 172], [171, 181], [178, 179], [178, 181], [183, 184], [183, 185], [187, 188], [187, 200], [190, 128], [190, 191], [191, 192], [191, 193], [193, 194], [193, 196], [196, 197], [196, 198], [198, 128], [198, 199], [200, 201], [200, 202], [202, 203], [202, 209], [209, 210], [209, 211], [211, 128], [211, 212]]}
# gained: {"lines": [61, 62, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 107, 108, 109, 112, 114, 115, 116, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 178, 179, 180, 181, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 209, 210, 211, 212, 214, 216], "branches": [[68, 69], [68, 80], [69, 70], [69, 72], [76, 77], [76, 78], [91, 92], [91, 106], [93, 94], [93, 95], [95, 96], [95, 101], [96, 97], [96, 98], [98, 99], [98, 100], [101, 102], [101, 104], [120, 121], [120, 122], [128, 129], [128, 214], [130, 128], [130, 131], [131, 132], [131, 187], [132, 133], [132, 134], [135, 136], [135, 137], [141, 142], [141, 143], [145, 146], [145, 147], [147, 148], [147, 162], [151, 152], [151, 153], [160, 147], [160, 161], [162, 163], [162, 171], [163, 164], [163, 168], [171, 172], [171, 181], [178, 179], [178, 181], [183, 184], [183, 185], [187, 188], [187, 200], [190, 191], [191, 192], [191, 193], [193, 194], [193, 196], [196, 197], [196, 198], [198, 199], [200, 201], [200, 202], [202, 203], [202, 209], [209, 210], [209, 211], [211, 128], [211, 212]]}

import binascii

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.hls import HlsFD


MANIFEST = """#EXTM3U
#EXT-X-MEDIA-SEQUENCE:5
#EXT-X-TARGETDURATION:10
#EXTINF:10,
http://example.com/seg1.ts
#EXTINF:10,
seg2.ts
#EXTINF:10,
http://example.com/seg3.ts
#EXT-X-ENDLIST
"""


class FakeResponse(object):
    def __init__(self, data, url):
        if isinstance(data, str):
            data = data.encode('utf-8')
        self.data = data
        self.url = url

    def read(self):
        return self.data

    def geturl(self):
        return self.url


class FakeYDL(object):
    def __init__(self, manifest, key=b'0123456789abcdef'):
        self.manifest = manifest
        self.key = key
        self.opened = []
        self.params = {}

    def urlopen(self, url):
        self.opened.append(url)
        if 'm3u8' in url:
            return FakeResponse(self.manifest, url)
        return FakeResponse(self.key, url)

    def to_screen(self, *args, **kwargs):
        pass

    def to_stderr(self, *args, **kwargs):
        pass

    def trouble(self, *args, **kwargs):
        pass

    def report_warning(self, *args, **kwargs):
        pass

    def report_error(self, *args, **kwargs):
        pass


class FakeFD(HlsFD):
    def __init__(self, ydl, params=None):
        super(FakeFD, self).__init__(ydl, params or {})
        self.appended = []
        self.finished = []
        self.errors = []
        self.warnings = []
        self.retries = []
        self.skipped = []
        self.frag_downloads = []
        self.frag_download_result = (True, b'FRAGDATA')
        self.frag_download_errors = []
        self.resume_index = 0
        self.ctx = None

    def to_screen(self, *args, **kwargs):
        pass

    def to_stderr(self, *args, **kwargs):
        pass

    def report_error(self, msg, *args, **kwargs):
        self.errors.append(msg)
        return msg

    def report_warning(self, msg, *args, **kwargs):
        self.warnings.append(msg)

    def report_retry_fragment(self, err, frag_index, count, retries):
        self.retries.append((frag_index, count, retries))

    def report_skip_fragment(self, frag_index):
        self.skipped.append(frag_index)

    def _prepare_url(self, info_dict, url, *args, **kwargs):
        return url

    def _prepare_and_start_frag_download(self, ctx):
        self.ctx = ctx
        ctx['fragment_index'] = self.resume_index

    def _download_fragment(self, ctx, frag_url, info_dict, headers=None):
        self.frag_downloads.append((frag_url, dict(headers or {})))
        if self.frag_download_errors:
            err = self.frag_download_errors.pop(0)
            if err is not None:
                raise err
        return self.frag_download_result

    def _append_fragment(self, ctx, frag_content):
        self.appended.append(frag_content)

    def _finish_frag_download(self, ctx):
        self.finished.append(ctx)


def make_fd(manifest, params=None, key=b'0123456789abcdef'):
    return FakeFD(FakeYDL(manifest, key), params)


def enable_aes(monkeypatch, aes_obj):
    import youtube_dl.downloader.hls as hls_mod
    monkeypatch.setattr(hls_mod, 'AES', aes_obj, raising=False)
    monkeypatch.setattr(hls_mod, 'can_decrypt_frag', True, raising=False)
    return hls_mod


def test_real_download_basic():
    fd = make_fd(MANIFEST)
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert fd.ctx['total_frags'] == 3
    assert fd.ctx['ad_frags'] == 0
    assert fd.ctx['filename'] == 'out.mp4'
    assert len(fd.appended) == 3
    assert fd.appended == [b'FRAGDATA', b'FRAGDATA', b'FRAGDATA']
    assert fd.finished == [fd.ctx]
    assert fd.errors == []
    assert fd.frag_downloads[1][0] == 'http://example.com/seg2.ts'
    assert fd.frag_downloads[0][0] == 'http://example.com/seg1.ts'


def test_real_download_delegates_to_ffmpeg(monkeypatch):
    import youtube_dl.downloader.hls as hls_mod

    calls = {}

    class FakeFFmpegFD(object):
        def __init__(self, ydl, params):
            calls['init'] = (ydl, params)
            self.hooks = []

        def add_progress_hook(self, ph):
            self.hooks.append(ph)
            calls.setdefault('hooks', []).append(ph)

        def real_download(self, filename, info_dict):
            calls['download'] = (filename, info_dict)
            return 'FFMPEG-RESULT'

    monkeypatch.setattr(hls_mod, 'FFmpegFD', FakeFFmpegFD)
    fd = make_fd('#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\n')
    hook = lambda d: None
    fd._progress_hooks = [hook]
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) == 'FFMPEG-RESULT'
    assert calls['download'] == ('out.mp4', info)
    assert calls['init'][1] is fd.params
    assert calls['hooks'] == [hook]
    assert len(fd.warnings) == 1
    assert 'delegated to ffmpeg' in fd.warnings[0]


def test_real_download_unsupported_with_extra_params(monkeypatch):
    import youtube_dl.downloader.hls as hls_mod

    def boom(*args, **kwargs):
        raise AssertionError('FFmpegFD must not be used')

    monkeypatch.setattr(hls_mod, 'FFmpegFD', boom)
    fd = make_fd('#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\n')
    info = {
        'url': 'http://example.com/manifest.m3u8',
        'extra_param_to_segment_url': 'token=abc',
    }
    assert fd.real_download('out.mp4', info) is False
    assert fd.errors == ['pycrypto not found. Please install it.']


def test_real_download_unsupported_with_decryption_key_url(monkeypatch):
    import youtube_dl.downloader.hls as hls_mod

    def boom(*args, **kwargs):
        raise AssertionError('FFmpegFD must not be used')

    monkeypatch.setattr(hls_mod, 'FFmpegFD', boom)
    fd = make_fd('#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\n')
    info = {
        'url': 'http://example.com/manifest.m3u8',
        '_decryption_key_url': 'http://example.com/key',
    }
    assert fd.real_download('out.mp4', info) is False
    assert fd.errors == ['pycrypto not found. Please install it.']


def test_real_download_ad_fragments_skipped():
    manifest = """#EXTM3U
#EXTINF:10,
http://example.com/seg1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:10,
http://example.com/ad1.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10,
http://example.com/seg2.ts
#UPLYNK-SEGMENT:abc,ad
#EXTINF:10,
http://example.com/ad2.ts
#UPLYNK-SEGMENT:abc,segment
#EXTINF:10,
http://example.com/seg3.ts
"""
    fd = make_fd(manifest)
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert fd.ctx['total_frags'] == 3
    assert fd.ctx['ad_frags'] == 2
    urls = [u for u, _ in fd.frag_downloads]
    assert urls == [
        'http://example.com/seg1.ts',
        'http://example.com/seg2.ts',
        'http://example.com/seg3.ts',
    ]
    assert len(fd.appended) == 3


def test_real_download_extra_query_and_headers():
    fd = make_fd(MANIFEST)
    info = {
        'url': 'http://example.com/manifest.m3u8',
        'extra_param_to_segment_url': 'token=abc&x=1',
        'http_headers': {'User-Agent': 'test'},
    }
    assert fd.real_download('out.mp4', info) is True
    assert len(fd.frag_downloads) == 3
    for url, headers in fd.frag_downloads:
        assert 'token=abc' in url
        assert headers['User-Agent'] == 'test'


def test_real_download_byte_range():
    manifest = """#EXTM3U
#EXT-X-BYTERANGE:100@0
#EXTINF:10,
http://example.com/seg1.ts
#EXT-X-BYTERANGE:50
#EXTINF:10,
http://example.com/seg2.ts
"""
    fd = make_fd(manifest)
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    headers = [h for _, h in fd.frag_downloads]
    assert headers[0]['Range'] == 'bytes=0-99'
    assert headers[1]['Range'] == 'bytes=100-149'


def test_real_download_fragment_index_resume():
    fd = make_fd(MANIFEST)
    fd.resume_index = 2
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert len(fd.appended) == 1
    assert [u for u, _ in fd.frag_downloads] == ['http://example.com/seg3.ts']


def test_real_download_download_fragment_failure():
    fd = make_fd(MANIFEST)
    fd.frag_download_result = (False, None)
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is False
    assert fd.appended == []
    assert fd.finished == []


def test_real_download_retry_then_success():
    fd = make_fd(MANIFEST, params={'fragment_retries': 2})
    err = compat_urllib_error.HTTPError('http://x', 503, 'unavailable', None, None)
    fd.frag_download_errors = [err, None]
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert fd.retries == [(1, 1, 2)]
    assert len(fd.appended) == 3


def test_real_download_skip_unavailable_fragment():
    fd = make_fd(MANIFEST, params={'fragment_retries': 1})
    err = compat_urllib_error.HTTPError('http://x', 404, 'gone', None, None)
    fd.frag_download_errors = [err, err]
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert fd.skipped == [1]
    assert len(fd.appended) == 2
    assert fd.finished == [fd.ctx]


def test_real_download_give_up_after_retries():
    fd = make_fd(MANIFEST, params={
        'fragment_retries': 1,
        'skip_unavailable_fragments': False,
    })
    err = compat_urllib_error.HTTPError('http://x', 404, 'gone', None, None)
    fd.frag_download_errors = [err, err]
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is False
    assert fd.errors == ['giving up after 1 fragment retries']
    assert fd.appended == []


def test_real_download_aes128_with_iv_and_relative_key(monkeypatch):
    created = {}

    class FakeAES(object):
        MODE_CBC = 2

        @staticmethod
        def new(key, mode, iv):
            created['key'] = key
            created['mode'] = mode
            created['iv'] = iv

            class Cipher(object):
                def decrypt(self, data):
                    return b'DECRYPTED'
            return Cipher()

    enable_aes(monkeypatch, FakeAES)
    manifest = """#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin",IV=0x000102030405060708090a0b0c0d0e0f
#EXTINF:10,
http://example.com/seg1.ts
"""
    fd = make_fd(manifest, key=b'0123456789abcdef')
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert created['key'] == b'0123456789abcdef'
    assert created['iv'] == binascii.unhexlify('000102030405060708090a0b0c0d0e0f')
    assert fd.appended == [b'DECRYPTED']
    assert 'http://example.com/key.bin' in fd.ydl.opened


def test_real_download_aes128_test_mode_skips_decryption(monkeypatch):
    class FakeAES(object):
        MODE_CBC = 2

        @staticmethod
        def new(*args, **kwargs):
            raise AssertionError('AES must not be used in test mode')

    enable_aes(monkeypatch, FakeAES)
    manifest = """#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="http://example.com/key.bin"
#EXTINF:10,
http://example.com/seg1.ts
#EXTINF:10,
http://example.com/seg2.ts
"""
    fd = make_fd(manifest, params={'test': True})
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert fd.appended == [b'FRAGDATA']
    assert len(fd.frag_downloads) == 1


def test_real_download_aes128_key_url_changed_resets_key(monkeypatch):
    keys = []

    class FakeAES(object):
        MODE_CBC = 2

        @staticmethod
        def new(key, mode, iv):
            keys.append(key)

            class Cipher(object):
                def decrypt(self, data):
                    return data
            return Cipher()

    enable_aes(monkeypatch, FakeAES)
    manifest = """#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="http://example.com/key1.bin"
#EXTINF:10,
http://example.com/seg1.ts
#EXT-X-KEY:METHOD=AES-128,URI="http://example.com/key2.bin"
#EXTINF:10,
http://example.com/seg2.ts
"""
    fd = make_fd(manifest, key=b'KEYDATA')
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert len(keys) == 2
    assert fd.ydl.opened.count('http://example.com/key1.bin') == 1
    assert fd.ydl.opened.count('http://example.com/key2.bin') == 1
    assert len(fd.appended) == 2


def test_real_download_aes128_extra_query_on_key(monkeypatch):
    class FakeAES(object):
        MODE_CBC = 2

        @staticmethod
        def new(key, mode, iv):
            class Cipher(object):
                def decrypt(self, data):
                    return data
            return Cipher()

    enable_aes(monkeypatch, FakeAES)
    manifest = """#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="http://example.com/key.bin"
#EXTINF:10,
http://example.com/seg1.ts
"""
    fd = make_fd(manifest)
    info = {
        'url': 'http://example.com/manifest.m3u8',
        'extra_param_to_segment_url': 'token=abc',
    }
    assert fd.real_download('out.mp4', info) is True
    key_urls = [u for u in fd.ydl.opened if 'key.bin' in u]
    assert len(key_urls) == 1
    assert 'token=abc' in key_urls[0]


def test_real_download_media_sequence_used_for_iv(monkeypatch):
    ivs = []

    class FakeAES(object):
        MODE_CBC = 2

        @staticmethod
        def new(key, mode, iv):
            ivs.append(iv)

            class Cipher(object):
                def decrypt(self, data):
                    return data
            return Cipher()

    enable_aes(monkeypatch, FakeAES)
    manifest = """#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXT-X-KEY:METHOD=AES-128,URI="http://example.com/key.bin"
#EXTINF:10,
http://example.com/seg1.ts
#EXTINF:10,
http://example.com/seg2.ts
"""
    fd = make_fd(manifest)
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert len(ivs) == 2
    assert ivs[0] != ivs[1]
    assert len(ivs[0]) == 16
    assert len(fd.appended) == 2


def test_real_download_blank_lines_and_unknown_tags():
    manifest = """#EXTM3U

#EXT-X-VERSION:3
#EXTINF:10,
http://example.com/seg1.ts

#EXT-X-ENDLIST
"""
    fd = make_fd(manifest)
    info = {'url': 'http://example.com/manifest.m3u8'}
    assert fd.real_download('out.mp4', info) is True
    assert fd.ctx['total_frags'] == 1
    assert len(fd.appended) == 1
