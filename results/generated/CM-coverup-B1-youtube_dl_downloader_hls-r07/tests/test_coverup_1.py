# file: project/youtube_dl/downloader/hls.py:60-216
# asked: {"lines": [61, 62, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 107, 108, 109, 112, 114, 115, 116, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 178, 179, 180, 181, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 209, 210, 211, 212, 214, 216], "branches": [[68, 69], [68, 80], [69, 70], [69, 72], [76, 77], [76, 78], [91, 92], [91, 106], [93, 94], [93, 95], [95, 96], [95, 101], [96, 97], [96, 98], [98, 99], [98, 100], [101, 102], [101, 104], [120, 121], [120, 122], [128, 129], [128, 214], [130, 128], [130, 131], [131, 132], [131, 187], [132, 133], [132, 134], [135, 136], [135, 137], [141, 142], [141, 143], [145, 146], [145, 147], [147, 148], [147, 162], [151, 152], [151, 153], [160, 147], [160, 161], [162, 163], [162, 171], [163, 164], [163, 168], [171, 172], [171, 181], [178, 179], [178, 181], [183, 184], [183, 185], [187, 188], [187, 200], [190, 128], [190, 191], [191, 192], [191, 193], [193, 194], [193, 196], [196, 197], [196, 198], [198, 128], [198, 199], [200, 201], [200, 202], [202, 203], [202, 209], [209, 210], [209, 211], [211, 128], [211, 212]]}
# gained: {"lines": [61, 62, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 107, 108, 109, 112, 114, 115, 116, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 178, 179, 180, 181, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 209, 210, 211, 212, 214, 216], "branches": [[68, 69], [68, 80], [69, 70], [69, 72], [76, 77], [76, 78], [91, 92], [91, 106], [93, 94], [93, 95], [95, 96], [95, 101], [96, 97], [96, 98], [98, 99], [98, 100], [101, 102], [101, 104], [120, 121], [120, 122], [128, 129], [128, 214], [130, 128], [130, 131], [131, 132], [131, 187], [132, 133], [132, 134], [135, 136], [135, 137], [141, 142], [141, 143], [145, 146], [145, 147], [147, 148], [147, 162], [151, 152], [151, 153], [160, 147], [160, 161], [162, 163], [162, 171], [163, 164], [163, 168], [171, 172], [171, 181], [178, 179], [178, 181], [183, 184], [183, 185], [187, 188], [187, 200], [190, 128], [190, 191], [191, 192], [191, 193], [193, 194], [193, 196], [196, 197], [196, 198], [198, 128], [198, 199], [200, 201], [200, 202], [202, 203], [202, 209], [209, 210], [209, 211], [211, 128], [211, 212]]}

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.hls import HlsFD


class _FakeCipher(object):
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def decrypt(self, data):
        return bytes(
            ((b ^ self.iv[i % len(self.iv)]) ^ self.key[i % len(self.key)])
            for i, b in enumerate(data))


class _FakeAES(object):
    MODE_CBC = 'CBC'

    @staticmethod
    def new(key, mode=None, iv=None):
        assert mode == _FakeAES.MODE_CBC
        assert len(key) == 16
        assert iv is not None and len(iv) == 16
        return _FakeCipher(key, iv)


class _FakeResponse(object):
    def __init__(self, data, url=None):
        self._data = data
        self._url = url

    def geturl(self):
        return self._url

    def read(self):
        return self._data


class _FakeYDL(object):
    def __init__(self, manifest, key=b'0123456789abcdef'):
        self.manifest = manifest
        self.key = key
        self.urlopen_calls = []
        self.key_calls = []

    def to_screen(self, *args, **kwargs):
        pass

    def report_warning(self, *args, **kwargs):
        pass

    def report_error(self, *args, **kwargs):
        pass

    def urlopen(self, url):
        self.urlopen_calls.append(url)
        if 'key' in str(url):
            self.key_calls.append(url)
            return _FakeResponse(self.key)
        return _FakeResponse(
            self.manifest.encode('utf-8'),
            url='https://cdn.example.com/hls/manifest.m3u8')


def _http_error(url):
    return compat_urllib_error.HTTPError(url, 404, 'Not Found', {}, None)


def _make_fd(monkeypatch, manifest, params=None, fragment_index=0,
             download_impl=None, can_download=True, key=b'0123456789abcdef'):
    monkeypatch.setattr(
        'youtube_dl.downloader.hls.AES', _FakeAES, raising=False)
    if can_download is not None:
        monkeypatch.setattr(
            HlsFD, 'can_download',
            staticmethod(lambda manifest_, info_dict: can_download))
    ydl = _FakeYDL(manifest, key=key)
    fd = HlsFD(ydl, dict(params or {}))
    state = {
        'ctx_start': None,
        'ctx': None,
        'frag_urls': [],
        'headers': [],
        'appended': [],
        'finished': [],
        'warnings': [],
        'errors': [],
        'retries': [],
        'skipped': [],
        'download_calls': 0,
    }
    fd._prepare_url = lambda info_dict, url: url
    fd.to_screen = lambda *args, **kwargs: None
    fd.report_warning = lambda *args, **kwargs: state['warnings'].append(args)
    fd.report_error = lambda *args, **kwargs: state['errors'].append(args)
    fd.report_retry_fragment = (
        lambda err, frag_index, count, retries:
        state['retries'].append((frag_index, count, retries)))
    fd.report_skip_fragment = lambda frag_index: state['skipped'].append(frag_index)

    def _prepare(ctx):
        state['ctx_start'] = dict(ctx)
        ctx['fragment_index'] = fragment_index
        state['ctx'] = ctx

    def _download(ctx, frag_url, info_dict, headers=None):
        state['download_calls'] += 1
        state['frag_urls'].append(frag_url)
        state['headers'].append(dict(headers) if headers is not None else None)
        if download_impl is not None:
            return download_impl(
                ctx, frag_url, info_dict, headers, state['download_calls'])
        return True, b'frag-%d' % state['download_calls']

    fd._prepare_and_start_frag_download = _prepare
    fd._download_fragment = _download
    fd._append_fragment = lambda ctx, content: state['appended'].append(content)
    fd._finish_frag_download = lambda ctx: state['finished'].append(dict(ctx))
    return fd, ydl, state


def test_delegates_to_ffmpeg_when_unsupported(monkeypatch):
    created = []

    class FakeFFmpegFD(object):
        def __init__(self, ydl, params):
            self.ydl = ydl
            self.params = params
            self.hooks = []
            self.downloaded = None
            created.append(self)

        def add_progress_hook(self, hook):
            self.hooks.append(hook)

        def real_download(self, filename, info_dict):
            self.downloaded = (filename, info_dict)
            return True

    monkeypatch.setattr('youtube_dl.downloader.hls.FFmpegFD', FakeFFmpegFD)
    fd, ydl, state = _make_fd(
        monkeypatch, '#EXTM3U\nseg.ts\n', can_download=False)
    hook1 = lambda status: None
    hook2 = lambda status: None
    fd._progress_hooks = [hook1, hook2]
    info = {'url': 'https://example.com/manifest.m3u8'}

    assert fd.real_download('out.mp4', info) is True
    assert len(created) == 1
    assert created[0].hooks == [hook1, hook2]
    assert created[0].downloaded == ('out.mp4', info)
    assert state['warnings'] and 'ffmpeg' in state['warnings'][0][0]
    assert state['finished'] == []


@pytest.mark.parametrize('extra', [
    {'extra_param_to_segment_url': 'token=abc'},
    {'_decryption_key_url': 'https://example.com/key.bin'},
])
def test_unsupported_with_key_params_reports_error(monkeypatch, extra):
    fd, ydl, state = _make_fd(
        monkeypatch, '#EXTM3U\nseg.ts\n', can_download=False)
    info = {'url': 'https://example.com/manifest.m3u8'}
    info.update(extra)

    assert fd.real_download('out.mp4', info) is False
    assert state['errors'] == [('pycrypto not found. Please install it.',)]
    assert state['finished'] == []


def test_normal_download_ads_byterange_media_sequence(monkeypatch):
    manifest = '\n'.join([
        '#EXTM3U',
        '',
        '#EXT-X-MEDIA-SEQUENCE:42',
        '#EXT-X-KEY:METHOD=NONE',
        '#ANVATO-SEGMENT-INFO:type=ad',
        'ad-anvato.ts',
        '#ANVATO-SEGMENT-INFO:type=master',
        '#EXT-X-BYTERANGE:100@0',
        'seg1.ts',
        '#UPLYNK-SEGMENT:1,ad',
        'ad-uplynk.ts',
        '#UPLYNK-SEGMENT:2,segment',
        '#EXT-X-BYTERANGE:50',
        'https://media.example.com/seg2.ts',
        '',
    ])
    fd, ydl, state = _make_fd(monkeypatch, manifest)
    info = {
        'url': 'https://example.com/original.m3u8',
        'http_headers': {'X-Test': 'yes'},
    }

    assert fd.real_download('out.mp4', info) is True
    assert state['ctx_start']['total_frags'] == 2
    assert state['ctx_start']['ad_frags'] == 2
    assert state['frag_urls'] == [
        'https://cdn.example.com/hls/seg1.ts',
        'https://media.example.com/seg2.ts',
    ]
    assert state['headers'][0]['Range'] == 'bytes=0-99'
    assert state['headers'][0]['X-Test'] == 'yes'
    assert state['headers'][1]['Range'] == 'bytes=100-149'
    assert state['appended'] == [b'frag-1', b'frag-2']
    assert len(state['finished']) == 1
    assert ydl.urlopen_calls[0] == 'https://example.com/original.m3u8'


def test_extra_param_applied_to_relative_and_absolute_fragments(monkeypatch):
    manifest = '#EXTM3U\nseg1.ts\nhttps://media.example.com/seg2.ts\n'
    fd, ydl, state = _make_fd(monkeypatch, manifest)
    info = {
        'url': 'https://example.com/manifest.m3u8',
        'extra_param_to_segment_url': 'token=abc&x=1',
    }

    assert fd.real_download('out.mp4', info) is True
    assert 'token=abc' in state['frag_urls'][0]
    assert 'x=1' in state['frag_urls'][0]
    assert state['frag_urls'][0].startswith('https://cdn.example.com/hls/seg1.ts?')
    assert 'token=abc' in state['frag_urls'][1]
    assert state['appended'] == [b'frag-1', b'frag-2']


def test_resume_skips_already_downloaded_fragment(monkeypatch):
    manifest = '#EXTM3U\nseg1.ts\nseg2.ts\n'
    fd, ydl, state = _make_fd(monkeypatch, manifest, fragment_index=1)

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is True
    assert state['frag_urls'] == ['https://cdn.example.com/hls/seg2.ts']
    assert state['appended'] == [b'frag-1']
    assert len(state['finished']) == 1


def test_test_mode_downloads_only_first_fragment(monkeypatch):
    manifest = '#EXTM3U\nseg1.ts\nseg2.ts\nseg3.ts\n'
    fd, ydl, state = _make_fd(monkeypatch, manifest, params={'test': True})

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is True
    assert state['frag_urls'] == ['https://cdn.example.com/hls/seg1.ts']
    assert state['appended'] == [b'frag-1']
    assert len(state['finished']) == 1


def test_download_fragment_failure_aborts(monkeypatch):
    def impl(ctx, url, info, headers, call_no):
        return False, None

    fd, ydl, state = _make_fd(
        monkeypatch, '#EXTM3U\nseg1.ts\nseg2.ts\n', download_impl=impl)

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is False
    assert state['download_calls'] == 1
    assert state['appended'] == []
    assert state['finished'] == []


def test_http_error_retry_then_success(monkeypatch):
    def impl(ctx, url, info, headers, call_no):
        if call_no == 1:
            raise _http_error(url)
        return True, b'recovered'

    fd, ydl, state = _make_fd(
        monkeypatch, '#EXTM3U\nseg1.ts\n',
        params={'fragment_retries': 2}, download_impl=impl)

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is True
    assert state['download_calls'] == 2
    assert state['retries'] == [(1, 1, 2)]
    assert state['appended'] == [b'recovered']
    assert len(state['finished']) == 1


def test_http_error_skip_unavailable_fragment(monkeypatch):
    def impl(ctx, url, info, headers, call_no):
        if 'seg1' in url:
            raise _http_error(url)
        return True, b'good'

    fd, ydl, state = _make_fd(
        monkeypatch, '#EXTM3U\nseg1.ts\nseg2.ts\n',
        params={'fragment_retries': 0, 'skip_unavailable_fragments': True},
        download_impl=impl)

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is True
    assert state['skipped'] == [1]
    assert state['appended'] == [b'good']
    assert len(state['finished']) == 1


def test_http_error_giving_up_after_retries(monkeypatch):
    def impl(ctx, url, info, headers, call_no):
        raise _http_error(url)

    fd, ydl, state = _make_fd(
        monkeypatch, '#EXTM3U\nseg1.ts\nseg2.ts\n',
        params={'fragment_retries': 1, 'skip_unavailable_fragments': False},
        download_impl=impl)

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is False
    assert state['download_calls'] == 2
    assert state['retries'] == [(1, 1, 1)]
    assert state['errors'] == [('giving up after 1 fragment retries',)]
    assert state['finished'] == []


def test_aes128_with_iv_relative_key_extra_query_and_cached_key(monkeypatch):
    key_line = (
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin",'
        'IV=0x00000000000000000000000000000001')
    # Key is cached only while the same decrypt_info dict is reused:
    # seg1 fetches, seg2 (no new EXT-X-KEY line) reuses KEY.
    # Repeating the identical EXT-X-KEY line replaces decrypt_info,
    # so seg3 fetches again despite decrypt_url == URI (KEY is absent
    # in the newly parsed dict).
    manifest = '\n'.join([
        '#EXTM3U',
        key_line,
        'seg1.ts',
        'seg2.ts',
        key_line,
        'seg3.ts',
    ])

    def impl(ctx, url, info, headers, call_no):
        return True, b'A' * 32

    fd, ydl, state = _make_fd(
        monkeypatch, manifest, download_impl=impl)
    info = {
        'url': 'https://example.com/m.m3u8',
        'extra_param_to_segment_url': 'token=abc',
    }

    assert fd.real_download('out.mp4', info) is True
    assert len(ydl.key_calls) == 2
    assert ydl.key_calls[0].startswith('https://cdn.example.com/hls/key.bin?')
    assert 'token=abc' in ydl.key_calls[0]
    assert ydl.key_calls[1] == ydl.key_calls[0]
    assert len(state['appended']) == 3
    assert all(len(content) == 32 for content in state['appended'])
    assert all(content != b'A' * 32 for content in state['appended'])
    assert len(state['finished']) == 1


def test_aes128_without_iv_uses_media_sequence_and_decryption_key_url(monkeypatch):
    manifest = '\n'.join([
        '#EXTM3U',
        '#EXT-X-MEDIA-SEQUENCE:7',
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"',
        'seg1.ts',
    ])

    def impl(ctx, url, info, headers, call_no):
        return True, b'B' * 32

    fd, ydl, state = _make_fd(
        monkeypatch, manifest, download_impl=impl)
    info = {
        'url': 'https://example.com/m.m3u8',
        '_decryption_key_url': 'https://keys.example.com/mykey',
    }

    assert fd.real_download('out.mp4', info) is True
    assert ydl.key_calls == ['https://keys.example.com/mykey']
    assert len(state['appended']) == 1
    assert len(state['appended'][0]) == 32
    assert state['appended'][0] != b'B' * 32


def test_aes128_absolute_key_uri_and_key_change_refetches(monkeypatch):
    manifest = '\n'.join([
        '#EXTM3U',
        '#EXT-X-KEY:METHOD=AES-128,URI="https://keys.example.com/key1.bin",'
        'IV=0x00000000000000000000000000000002',
        'seg1.ts',
        '#EXT-X-KEY:METHOD=AES-128,URI="https://keys.example.com/key2.bin",'
        'IV=0x00000000000000000000000000000003',
        'seg2.ts',
    ])

    def impl(ctx, url, info, headers, call_no):
        return True, b'C' * 32

    fd, ydl, state = _make_fd(
        monkeypatch, manifest, download_impl=impl)

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is True
    assert ydl.key_calls == [
        'https://keys.example.com/key1.bin',
        'https://keys.example.com/key2.bin',
    ]
    assert len(state['appended']) == 2
    assert all(len(content) == 32 for content in state['appended'])
    assert all(content != b'C' * 32 for content in state['appended'])
    assert len(state['finished']) == 1


def test_aes128_test_mode_fetches_key_but_does_not_decrypt(monkeypatch):
    manifest = '\n'.join([
        '#EXTM3U',
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin",'
        'IV=0x00000000000000000000000000000001',
        'seg1.ts',
        'seg2.ts',
    ])

    def impl(ctx, url, info, headers, call_no):
        return True, b'not-block-aligned'

    fd, ydl, state = _make_fd(
        monkeypatch, manifest, params={'test': True}, download_impl=impl)

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is True
    assert ydl.key_calls == ['https://cdn.example.com/hls/key.bin']
    assert state['appended'] == [b'not-block-aligned']
    assert state['download_calls'] == 1
    assert len(state['finished']) == 1


def test_empty_manifest_finishes_successfully(monkeypatch):
    fd, ydl, state = _make_fd(monkeypatch, '#EXTM3U\n\n#EXT-X-ENDLIST\n')

    assert fd.real_download('out.mp4', {'url': 'https://example.com/m.m3u8'}) is True
    assert state['ctx_start']['total_frags'] == 0
    assert state['ctx_start']['ad_frags'] == 0
    assert state['appended'] == []
    assert len(state['finished']) == 1
