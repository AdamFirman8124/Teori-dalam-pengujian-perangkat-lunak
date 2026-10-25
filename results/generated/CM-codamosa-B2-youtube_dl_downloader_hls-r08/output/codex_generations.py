

# Generated at 2026-10-25 03:19:56.408321
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:58.821602
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:01.237345
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:03.652166
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:06.070111
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:08.487112
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:10.905198
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:13.318912
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:15.732773
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:18.147642
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:20.562784
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:22.978027
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:20:24.459073
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from unittest.mock import MagicMock

    mock_ydl = MagicMock()
    params = {}

    fd = HlsFD(mock_ydl, params)

    assert isinstance(fd, FragmentFD)
    assert isinstance(fd, HlsFD)
    assert fd.ydl is mock_ydl
    assert fd.params is params
    assert fd.FD_NAME == 'hlsnative'

# Generated at 2026-10-25 03:20:53.455983
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:55.883426
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:58.420105
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:00.839231
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:03.250139
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:05.665430
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:08.079538
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:10.493877
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:12.908499
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:15.322804
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:17.736782
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:20.151500
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:22.565794
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:24.980302
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:27.394574
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:29.808522
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:32.442318
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:33.777708
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:52.556892
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class FakeResponse(object):
        def __init__(self, url, content):
            self._url = url
            self._content = content

        def geturl(self):
            return self._url

        def read(self):
            return self._content

    class FakeYDL(object):
        def __init__(self, manifest_url, manifest):
            self.manifest_url = manifest_url
            self.manifest = manifest
            self.requested_urls = []

        def urlopen(self, url):
            self.requested_urls.append(url)
            assert url == self.manifest_url
            return FakeResponse(url, self.manifest.encode('utf-8'))

    manifest_url = 'https://example.com/hls/index.m3u8'
    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#UPLYNK-SEGMENT,ad
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXT-X-BYTERANGE:4@10
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
'''

    ydl = FakeYDL(manifest_url, manifest)
    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    messages = []
    downloaded = []
    appended = []
    finished = []

    fd.to_screen = lambda message: messages.append(message)
    fd._prepare_url = lambda info_dict, url: url

    def prepare_download(ctx):
        assert ctx['filename'] == 'output.ts'
        assert ctx['total_frags'] == 2
        assert ctx['ad_frags'] == 1
        ctx['fragment_index'] = 0

    def download_fragment(ctx, url, info_dict, headers):
        downloaded.append((url, dict(headers)))
        return True, {
            'https://example.com/hls/segment-1.ts': b'first',
            'https://example.com/hls/segment-2.ts': b'next',
        }[url]

    fd._prepare_and_start_frag_download = prepare_download
    fd._download_fragment = download_fragment
    fd._append_fragment = lambda ctx, content: appended.append(content)
    fd._finish_frag_download = lambda ctx: finished.append(ctx)

    result = fd.real_download('output.ts', {
        'url': manifest_url,
        'http_headers': {'User-Agent': 'test-agent'},
    })

    assert result is True
    assert ydl.requested_urls == [manifest_url]

    # The advertisement must not be downloaded.
    assert downloaded == [
        (
            'https://example.com/hls/segment-1.ts',
            {'User-Agent': 'test-agent'},
        ),
        (
            'https://example.com/hls/segment-2.ts',
            {
                'User-Agent': 'test-agent',
                'Range': 'bytes=10-13',
            },
        ),
    ]

    assert appended == [b'first', b'next']
    assert len(finished) == 1
    assert finished[0]['total_frags'] == 2
    assert finished[0]['ad_frags'] == 1
    assert messages == ['[hlsnative] Downloading m3u8 manifest']

# Generated at 2026-10-25 03:22:03.513674
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    vod_manifest = '''\
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
segment-1.ts
#EXT-X-ENDLIST
'''

    assert HlsFD.can_download(vod_manifest, {})
    assert not HlsFD.can_download(vod_manifest, {'is_live': True})

    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts\n',
        {})

    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
        'segment.ts\n',
        {})

    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-MAP:URI="init.mp4"\n'
        'segment.m4s\n',
        {})

    original_can_decrypt_frag = can_decrypt_frag
    try:
        aes_manifest = '''\
#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXTINF:10,
segment.ts
'''

        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        aes_byterange_manifest = '''\
#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXT-X-BYTERANGE:1024@0
segment.ts
'''
        assert not HlsFD.can_download(aes_byterange_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 03:22:19.080420
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # Basic unencrypted VOD playlist is supported.
        can_decrypt_frag = False
        assert HlsFD.can_download(
            '#EXTM3U\n#EXTINF:10,\nsegment.ts',
            {'is_live': False})

        # Unencrypted byte-range playlists are supported.
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-BYTERANGE:1000@0\nsegment.ts',
            {'is_live': False})

        # METHOD=NONE is supported without Crypto.
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts',
            {'is_live': False})

        # Unsupported encryption methods must be rejected.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES\nsegment.ts',
            {'is_live': False})

        # AES-128 requires Crypto support.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            'segment.ts',
            {'is_live': False})

        can_decrypt_frag = True

        # AES-128 is supported when decryption is available.
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            'segment.ts',
            {'is_live': False})

        # AES-128 combined with byte ranges is unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts',
            {'is_live': False})

        # Initialization maps are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s',
            {'is_live': False})

        # Native HLS downloading is disabled for live streams.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXTINF:10,\nsegment.ts',
            {'is_live': True})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 03:22:21.497131
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:23.912877
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:26.327624
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:28.741714
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:31.157876
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:32.537464
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:51.129307
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:52.767719
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:54.204087
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:06.529577
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    info_dict = {'is_live': False}
    method_globals = HlsFD.can_download.__globals__
    original_can_decrypt = method_globals['can_decrypt_frag']

    try:
        # Basic VOD playlist is supported.
        assert HlsFD.can_download('#EXTM3U\nsegment.ts', info_dict)

        # Unencrypted byte-range playlists are supported.
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-BYTERANGE:100@0\n'
            'segment.ts',
            info_dict)

        # Initialization segments are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-MAP:URI="init.mp4"\n'
            'segment.m4s',
            info_dict)

        # Encryption methods other than NONE and AES-128 are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key"\n'
            'segment.ts',
            info_dict)

        # AES-128 requires the crypto dependency.
        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key"\n'
            'segment.ts'
        )

        method_globals['can_decrypt_frag'] = False
        assert not HlsFD.can_download(aes_manifest, info_dict)

        method_globals['can_decrypt_frag'] = True
        assert HlsFD.can_download(aes_manifest, info_dict)

        # AES-128 combined with byte ranges is unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key"\n'
            '#EXT-X-BYTERANGE:100@0\n'
            'segment.ts',
            info_dict)

        # Native HLS downloading does not support live streams.
        assert not HlsFD.can_download(
            '#EXTM3U\nsegment.ts',
            {'is_live': True})

    finally:
        method_globals['can_decrypt_frag'] = original_can_decrypt

# Generated at 2026-10-25 03:23:56.625514
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:58.100171
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:59.533717
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:24:10.175406
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    plain_manifest = """#EXTM3U
#EXTINF:10,
segment-1.ts
"""

    assert HlsFD.can_download(plain_manifest, {})
    assert HlsFD.can_download(
        plain_manifest + '#EXT-X-BYTERANGE:100@0\n', {})
    assert HlsFD.can_download(
        plain_manifest + '#EXT-X-MEDIA-SEQUENCE:1\n', {})
    assert HlsFD.can_download(
        plain_manifest + '#EXT-X-PLAYLIST-TYPE:EVENT\n', {})

    assert not HlsFD.can_download(
        plain_manifest + '#EXT-X-MAP:URI="init.mp4"\n', {})
    assert not HlsFD.can_download(
        plain_manifest + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key"\n', {})
    assert not HlsFD.can_download(plain_manifest, {'is_live': True})

    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key"\n'
        '#EXTINF:10,\n'
        'segment-1.ts\n'
    )

    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 streams using byte ranges are unsupported even when
        # AES decryption is available.
        assert not HlsFD.can_download(
            aes_manifest + '#EXT-X-BYTERANGE:100@0\n', {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 03:24:21.451808
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag
    basic_manifest = '#EXTM3U\n#EXTINF:10,\nsegment.ts\n'

    try:
        # Ordinary VOD playlists are supported.
        assert HlsFD.can_download(basic_manifest, {})
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts\n', {})

        # Live streams are not supported by the native downloader.
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})

        # Initialization sections require ffmpeg.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s\n', {})

        # Unsupported encryption methods require ffmpeg.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key"\nsegment.ts\n',
            {})

        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXTINF:10,\n'
            'segment.ts\n'
        )

        # AES-128 requires the Crypto AES implementation.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # Unencrypted byte ranges are supported.
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-BYTERANGE:100@0\n'
            'segment.ts\n',
            {})

        # AES-128 together with byte ranges is not supported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXT-X-BYTERANGE:100@0\n'
            'segment.ts\n',
            {})

    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 03:24:45.104813
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import Mock

    manifest = b"""\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
segment-2.ts
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def geturl(self):
            # Simulate a redirected manifest URL. Relative fragment URLs should
            # be resolved against this URL rather than the original one.
            return 'https://cdn.example.com/video/index.m3u8'

        def read(self):
            return manifest

    ydl = Mock()
    ydl.urlopen.return_value = FakeResponse()

    # Avoid invoking the real downloader constructor and filesystem handling.
    fd = object.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    }
    fd._progress_hooks = []

    fd.to_screen = Mock()
    fd._prepare_url = Mock(side_effect=lambda info, url: url)

    def prepare_download(ctx):
        # FragmentFD normally initializes this value.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'first fragment'),
        (True, b'second fragment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'url': 'https://example.com/original.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True

    fd.to_screen.assert_called_once_with(
        '[hlsnative] Downloading m3u8 manifest')
    fd._prepare_url.assert_called_once_with(
        info_dict, 'https://example.com/original.m3u8')

# Generated at 2026-10-25 03:25:08.149288
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b"""\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10,
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
"""

    manifest_response = MagicMock()
    manifest_response.geturl.return_value = (
        'https://media.example.com/path/playlist.m3u8'
    )
    manifest_response.read.return_value = manifest

    ydl = MagicMock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })
    fd._prepare_url = MagicMock(return_value='prepared-manifest-url')

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download
    )
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'first-fragment'),
        (True, b'second-fragment'),
    ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'url': 'https://origin.example.com/playlist.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
    }

    assert fd.real_download('output.ts', info_dict) is True

    fd._prepare_url.assert_called_once_with(
        info_dict, info_dict['url']
    )
    ydl.urlopen.assert_called_once_with('prepared-manifest-url')

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1


# Generated at 2026-10-25 03:25:27.303522
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import Mock

    manifest = b"""\
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:5.0,
segment-1.ts
#UPLYNK-SEGMENT,ad
#EXTINF:5.0,
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXT-X-BYTERANGE:4@10
#EXTINF:5.0,
segment-2.ts
#EXT-X-ENDLIST
"""

    manifest_response = Mock()
    manifest_response.geturl.return_value = (
        'https://cdn.example.com/media/index.m3u8')
    manifest_response.read.return_value = manifest

    fd = HlsFD.__new__(HlsFD)
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    }
    fd._progress_hooks = []

    fd.ydl = Mock()
    fd.ydl.urlopen.return_value = manifest_response

    fd.to_screen = Mock()
    fd.report_error = Mock()
    fd.report_warning = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_retry_fragment = Mock()
    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    initial_context = {}

    def prepare_download(ctx):
        initial_context.update(ctx)
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)

    downloaded_fragments = []

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_fragments.append((url, dict(headers)))
        if 'segment-1.ts' in url:
            return True, b'first-fragment'
        if 'segment-2.ts' in url:
            return True, b'second-fragment'
        raise AssertionError('Unexpected fragment URL: %s' % url)

    fd._download_fragment = Mock(side_effect=download_fragment)

    appended_content = []
    fd._append_fragment = Mock(
        side_effect=lambda ctx, content: appended_content.append(content))
    fd._finish_frag_download = Mock()

    info_dict = {
        'url': 'https://origin.example.com/playlist.m3u8',
        'extra_param_to_segment_url': 'token=secret',
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True
    assert initial_context == {
        'filename': 'output.ts',
        'total_frags': 2,
        'ad_frags': 1,
    }

    # Relative URLs are resolved against the redirected manifest URL, and the
    # extra query parameter is applied to each media segment.
    assert downloaded_fragments == [
        (
            'https://cdn.example.com/media/segment-1.ts?token=secret',
            {},
        ),
        (
            'https://cdn.example.com/media/segment-2.ts?token=secret',
            {'Range': 'bytes=10-13'},
        ),
    ]

    # The advertisement fragment must not be downloaded or appended.
    assert appended_content == [
        b'first-fragment',
        b'second-fragment',
    ]

    fd._prepare_and_start_frag_download.assert_called_once()
    assert fd._download_fragment.call_count == 2
    assert fd._append_fragment.call_count == 2
    fd._finish_frag_download.assert_called_once()
    fd.report_error.assert_not_called()
    fd.report_warning.assert_not_called()

# Generated at 2026-10-25 03:25:38.350624
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    vod_info = {'is_live': False}
    live_info = {'is_live': True}

    plain_manifest = '#EXTM3U\n#EXTINF:10,\nsegment.ts'
    byterange_manifest = (
        '#EXTM3U\n'
        '#EXT-X-BYTERANGE:1000@0\n'
        'segment.ts'
    )
    aes128_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXTINF:10,\n'
        'segment.ts'
    )

    assert HlsFD.can_download(plain_manifest, vod_info)
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts', vod_info)
    assert HlsFD.can_download(byterange_manifest, vod_info)

    assert not HlsFD.can_download(plain_manifest, live_info)
    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s', vod_info)
    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
        'segment.ts',
        vod_info)

    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes128_manifest, vod_info)

        can_decrypt_frag = True
        assert HlsFD.can_download(aes128_manifest, vod_info)

        # AES-128 combined with byte ranges is unsupported even when
        # AES decryption is available.
        assert not HlsFD.can_download(
            aes128_manifest + '\n#EXT-X-BYTERANGE:1000@0',
            vod_info)
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 03:26:02.127571
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest import mock
    except ImportError:
        import mock

    manifest_url = 'https://example.test/master.m3u8'
    redirected_manifest_url = 'https://cdn.example.test/hls/playlist.m3u8'

    manifest = b'''\
#EXTM3U
#EXT-X-TARGETDURATION:10
#ANVATO-SEGMENT-INFO:type=ad
advertisement-1.ts
#ANVATO-SEGMENT-INFO:type=master
segment-1.ts
#UPLYNK-SEGMENT,ad
advertisement-2.ts
#UPLYNK-SEGMENT,segment
https://media.example.test/segment-2.ts
#EXT-X-ENDLIST
'''

    class FakeResponse(object):
        def geturl(self):
            return redirected_manifest_url

        def read(self):
            return manifest

    ydl = mock.Mock()
    ydl.urlopen.return_value = FakeResponse()

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })
    fd.to_screen = mock.Mock()
    fd._prepare_url = mock.Mock(side_effect=lambda info_dict, url: url)

    prepared_contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(dict(ctx))

    fd._prepare_and_start_frag_download = mock.Mock(
        side_effect=prepare_download)

    fragment_contents = {
        'https://cdn.example.test/hls/segment-1.ts': b'segment-one',
        'https://media.example.test/segment-2.ts': b'segment-two',
    }
    downloaded_urls = []

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_urls.append(url)
        return True, fragment_contents[url]

    fd._download_fragment = mock.Mock(side_effect=download_fragment)

    appended_fragments = []

    def append_fragment(ctx, content):
        appended_fragments.append(content)

    fd._append_fragment = mock.Mock(side_effect=append_fragment)
    fd._finish_frag_download = mock.Mock()


# Generated at 2026-10-25 03:26:22.941043
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:26:24.287022
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:26:25.642468
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:26:46.139025
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class MockResponse(object):
        def __init__(self, url, content):
            self._url = url
            self._content = content

        def geturl(self):
            return self._url

        def read(self):
            return self._content

    manifest_url = 'https://example.com/master.m3u8'
    redirected_manifest_url = 'https://cdn.example.com/hls/index.m3u8'
    manifest = b'''#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:5.0,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5.0,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:5.0,
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
'''

    class MockYDL(object):
        def __init__(self):
            self.requested_urls = []

        def urlopen(self, request):
            self.requested_urls.append(request)
            assert request == manifest_url
            return MockResponse(redirected_manifest_url, manifest)

    ydl = MockYDL()
    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    downloaded = []
    appended = []
    lifecycle = []

    fd.to_screen = lambda message: None
    fd._prepare_url = lambda info_dict, url: url

    def prepare(ctx):
        ctx['fragment_index'] = 0
        lifecycle.append(('start', ctx.copy()))

    def download_fragment(ctx, frag_url, info_dict, headers):
        downloaded.append((frag_url, dict(headers)))
        return True, ('content:%s' % frag_url).encode('utf-8')

    def append_fragment(ctx, content):
        appended.append(content)

    def finish(ctx):
        lifecycle.append(('finish', ctx.copy()))

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish

    result = fd.real_download('output.ts', {
        'url': manifest_url,
        'http_headers': {'User-Agent': 'test-agent'},
        'extra_param_to_segment_url': 'token=abc',
        'is_live': False,
    })

    expected_urls = [
        'https://cdn.example.com/hls/segment-1.ts?token=abc',
        'https://media.example.com/segment-2.ts?token=abc',
    ]

    assert result is True
    assert ydl.requested_urls == [manifest_url]
    assert [url for url, _ in downloaded] == expected_urls
    assert all(headers == {'User-Agent': 'test-agent'}
               for _, headers in downloaded)
    assert appended == [
        ('content:%s' % url).encode('utf-8') for url in expected_urls
    ]

    assert lifecycle[0][0] == 'start'
    assert lifecycle[0][1]['filename'] == 'output.ts'
    assert lifecycle[0][1]['total_frags'] == 2
    assert lifecycle[0][1]['ad_frags'] == 1
    assert lifecycle[-1][0] == 'finish'

# Generated at 2026-10-25 03:27:09.283266
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b"""\
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:5.0,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5.0,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:5.0,
segment-2.ts
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def read(self):
            return manifest

        def geturl(self):
            # Simulate the manifest URL being redirected.
            return 'https://cdn.example.com/video/playlist.m3u8'

    class FakeYDL(object):
        def __init__(self):
            self.opened_urls = []
            self.messages = []

        def urlopen(self, url):
            self.opened_urls.append(url)
            return FakeResponse()

        def to_screen(self, message, *args, **kwargs):
            self.messages.append(message)

        def report_warning(self, message, *args, **kwargs):
            raise AssertionError('Unexpected warning: %s' % message)

        def report_error(self, message, *args, **kwargs):
            raise AssertionError('Unexpected error: %s' % message)

    ydl = FakeYDL()
    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    prepared_contexts = []
    downloaded_urls = []
    appended_fragments = []
    finished_contexts = []

    # Avoid depending on FileDownloader's request-building implementation.
    fd._prepare_url = lambda info_dict, url: url

    def prepare_and_start(ctx):
        prepared_contexts.append(ctx)
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_urls.append(url)
        fragment_data = {
            'https://cdn.example.com/video/segment-1.ts': b'fragment-one',
            'https://cdn.example.com/video/segment-2.ts': b'fragment-two',
        }
        return True, fragment_data[url]


# Generated at 2026-10-25 03:27:20.978319
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    basic_manifest = '''#EXTM3U
#EXT-X-VERSION:3
#EXTINF:10,
segment-1.ts
#EXT-X-ENDLIST
'''

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # Basic VOD playlists are supported.
        assert HlsFD.can_download(basic_manifest, {})
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts', {})

        # Live streams are not supported by the native downloader.
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})

        # Initialization segments require ffmpeg.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s', {})

        # Encryption methods other than AES-128 are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
            'segment.ts',
            {})

        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            'segment.ts'
        )

        # AES-128 requires the Crypto dependency.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported.
        assert not HlsFD.can_download(
            aes_manifest + '\n#EXT-X-BYTERANGE:1000@0', {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 03:28:09.288369
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:10.646909
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:13.191464
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:15.606910
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:18.020715
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:20.436077
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:22.851269
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:25.270650
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:27.687038
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:30.104536
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:32.518815
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:34.933716
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:28:37.349208
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:28:39.765217
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:28:42.179587
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:28:53.934433
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE\n', {})

# Generated at 2026-10-25 03:29:18.547012
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from urllib.parse import parse_qs, urlparse
    except ImportError:
        from urlparse import parse_qs, urlparse


# Generated at 2026-10-25 03:29:21.674660
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:29:24.091031
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:29:26.510138
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:29:28.927637
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:29:31.341398
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:29:33.766222
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:29:36.183356
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:29:38.598089
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:29:41.017561
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:29:43.428546
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:29:45.842555
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:29:48.257460
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:29:50.671683
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:29:53.087392
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:29:55.502352
# Unit test for method real_download of class HlsFD