

# Generated at 2026-10-25 05:16:16.345536
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag

    plain_manifest = """\
#EXTM3U
#EXTINF:10,
segment1.ts
"""

    try:
        # Ordinary VOD playlists are supported.
        can_decrypt_frag = False
        assert HlsFD.can_download(plain_manifest, {})
        assert HlsFD.can_download(
            plain_manifest + '#EXT-X-KEY:METHOD=NONE\n', {})

        # Live streams are not supported by the native downloader.
        assert not HlsFD.can_download(plain_manifest, {'is_live': True})

        # Initialization segments and unsupported encryption methods require
        # delegation to ffmpeg.
        assert not HlsFD.can_download(
            plain_manifest + '#EXT-X-MAP:URI="init.mp4"\n', {})
        assert not HlsFD.can_download(
            plain_manifest + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key"\n', {})

        aes_manifest = (
            plain_manifest
            + '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        )

        # AES-128 requires an available AES implementation.
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported even when AES
        # decryption is available.
        assert not HlsFD.can_download(
            aes_manifest + '#EXT-X-BYTERANGE:1024@0\n', {})

        # Unencrypted byte-range playlists are supported.
        assert HlsFD.can_download(
            plain_manifest + '#EXT-X-BYTERANGE:1024@0\n', {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 05:16:17.795112
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

# Generated at 2026-10-25 05:16:42.983039
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@2
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def read(self):
            return manifest

        def geturl(self):
            return 'https://example.com/video/playlist.m3u8'

    class FakeYDL(object):
        def __init__(self):
            self.requested_urls = []

        def urlopen(self, url):
            self.requested_urls.append(url)
            return FakeResponse()

    ydl = FakeYDL()
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
        lifecycle.append(('start', dict(ctx)))

    def download_fragment(ctx, url, info_dict, headers):
        downloaded.append((url, dict(headers)))
        return True, ('content:%s' % url).encode('utf-8')

    def append_fragment(ctx, content):
        appended.append(content)

    def finish(ctx):
        lifecycle.append(('finish', dict(ctx)))

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish

    info_dict = {
        'url': 'https://example.com/original.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
    }

    assert fd.real_download('output.ts', info_dict) is True

    assert ydl.requested_urls == [
        'https://example.com/original.m3u8',
    ]

    # The

# Generated at 2026-10-25 05:16:45.407395
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 05:16:47.832113
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 05:16:50.260628
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 05:16:52.688444
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 05:16:55.156791
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 05:16:58.000896
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 05:17:00.646736
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:03.171390
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:05.592234
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:08.024937
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:10.444073
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:12.863905
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:15.282728
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:17.701047
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:20.121032
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:22.539711
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:24.958208
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:27.374786
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:29.795464
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:32.216321
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:34.642334
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:37.060882
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:39.483084
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:41.901026
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:44.320669
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:46.739055
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:49.156766
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:17:51.576312
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:53.996173
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:56.415367
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:17:58.833576
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:01.277763
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:03.694658
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:06.114653
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:08.530769
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:10.950605
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:13.368916
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:15.789816
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:18.207916
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:20.626479
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:23.044381
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:25.463330
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:27.882338
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:30.302036
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:32.719480
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:35.136774
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:37.557118
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:39.975846
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:42.418194
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:44.824357
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:47.243340
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:18:49.660270
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:52.076812
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:54.494692
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:56.912990
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:18:59.331760
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:19:01.749496
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:19:04.166769
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:19:05.549391
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:19:06.936705
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:04.409197
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:05.843287
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:08.265947
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:10.685424
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:13.103968
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:15.522399
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:17.940566
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:20.358034
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:22.776518
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:25.196099
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:27.615466
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:30.033571
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:32.450286
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:34.871512
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:37.291111
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:39.707785
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:42.126779
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:44.545860
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:46.964902
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:20:49.382150
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:20:51.798609
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 05:20:54.216275
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:55.632853
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:20:57.034570
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:21:54.327404
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:21:56.746779
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:21:59.635597
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:22:17.632220
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    info_dict = {}

    # Basic supported manifests
    assert HlsFD.can_download('#EXTM3U\n', info_dict)
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\n', info_dict)
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-BYTERANGE:1024@0\nsegment.ts\n', info_dict)
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:1234\n', info_dict)
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-PLAYLIST-TYPE:EVENT\n', info_dict)

    # Unsupported encryption method
    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES\n', info_dict)

    # Initialization segments are unsupported
    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\n', info_dict)

    # Live streams are unsupported by the native downloader
    assert not HlsFD.can_download(
        '#EXTM3U\n', {'is_live': True})

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # AES-128 requires the Crypto AES implementation
        can_decrypt_frag = False
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n',
            info_dict)

        can_decrypt_frag = True
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n',
            info_dict)

        # AES-128 combined with byte ranges is unsupported even when
        # decryption support is available.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXT-X-BYTERANGE:1024@0\n'
            'segment.ts\n',
            info_dict)
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 05:23:14.585880
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:23:16.004820
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:23:17.332848
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:23:35.579585
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import MagicMock

    manifest = b"""\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
"""

    manifest_response = MagicMock()
    manifest_response.geturl.return_value = (
        'https://cdn.example.com/media/playlist.m3u8'
    )
    manifest_response.read.return_value = manifest

    ydl = MagicMock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    prepared_contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx)

    fd._prepare_url = MagicMock(side_effect=lambda info, url: url)
    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(
        side_effect=[
            (True, b'first-fragment'),
            (True, b'second-fragment'),
        ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'url': 'https://example.com/original/playlist.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }

    assert fd.real_download('output.ts', info_dict) is True

    ydl.urlopen.assert_called_once_with(
        'https://example.com/original/playlist.m3u8')

    assert len(prepared_contexts) == 1
    ctx = prepared_contexts[0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    assert fd._download_fragment.call_count == 2
    downloaded_urls = [
        call_args[0][1]
        for call_args in fd._download_fragment.call_args_list
    ]
    assert downloaded_urls == [
        'https://cdn.example.com/media/segment-1.ts',
        'https://cdn.example.com/media/segment-2.ts',
    ]

    appended_contents = [
        call_args[0][1]
        for call_args in fd._append_fragment.call_args_list
    ]
    assert appended_contents == [
        b'first-fragment',
        b'second-fragment',
    ]

    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 05:24:29.268547
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:24:30.971696
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:24:32.495880
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 05:24:53.669291
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import Mock, call

    manifest = b"""#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#UPLYNK-SEGMENT,ad
advertisement.ts
#UPLYNK-SEGMENT,segment
segment-1.ts
#EXT-X-BYTERANGE:4@8
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
"""

    manifest_response = Mock()
    manifest_response.geturl.return_value = (
        'https://cdn.example.com/hls/index.m3u8')
    manifest_response.read.return_value = manifest

    ydl = Mock()
    ydl.urlopen.return_value = manifest_response

    # Avoid invoking FragmentFD initialization and isolate real_download's
    # playlist-processing behavior.
    fd = HlsFD.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    }
    fd._progress_hooks = []

    fd.to_screen = Mock()
    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    prepared_contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx)

    fd._prepare_and_start_frag_download = Mock(
        side_effect=prepare_download)

    downloaded_fragments = []

    def download_fragment(ctx, url, info_dict, headers):
        # Copy headers because real_download may mutate the original dictionary
        # when processing EXT-X-BYTERANGE.
        downloaded_fragments.append((url, dict(headers)))
        content = {
            'https://cdn.example.com/hls/segment-1.ts': b'first',
            'https://media.example.com/segment-2.ts': b'secon',
        }[url]
        return True, content

    fd._download_fragment = Mock(side_effect=download_fragment)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'url': 'https://example.com/original/index.m3u8',
        'is_live': False,
        'http_headers': {'User-Agent': 'test-agent'},
    }

    assert fd.real_download('output.ts', info_dict) is True

    ydl.urlopen.assert_called_once_with(
        'https://example.com/original/index.m3u8')

    assert prepared_contexts[0]['filename'] == 'output.ts'
    assert prepared_contexts[0]['total_frags'] == 2
    assert prepared_contexts[0]['ad_frags'] == 1

    # The advertisement must not be downloaded. Relative media URLs should be
    # resolved against the redirected manifest URL.
    assert downloaded_fragments == [
        (
            'https://cdn.example.com/hls/segment-1.ts',
            {'User-Agent': 'test-agent'},
        ),
        (
            'https://media.example.com/segment-2.ts',
            {
                'User-Agent': 'test-agent',
                'Range': 'bytes=8-11',
            },
        ),
    ]

    assert fd._append_fragment.call_args_list == [
        call(prepared_contexts[0], b'first'),
        call(prepared_contexts[0], b'secon'),
    ]
    fd._finish_frag_download.assert_called_once_with(prepared_contexts[0])

# Generated at 2026-10-25 05:25:04.042888
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag
    try:
        basic_manifest = '#EXTM3U\n#EXTINF:10,\nsegment.ts\n'
        assert HlsFD.can_download(basic_manifest, {})
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})

        # Unencrypted streams do not require AES support.
        can_decrypt_frag = False
        none_manifest = '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts\n'
        assert HlsFD.can_download(none_manifest, {})

        # AES-128 requires an available crypto implementation.
        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXTINF:10,\n'
            'segment.ts\n'
        )
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # Encryption methods other than NONE and AES-128 are unsupported.
        unsupported_encryption_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
            'segment.ts\n'
        )
        assert not HlsFD.can_download(unsupported_encryption_manifest, {})

        # Initialization sections are unsupported.
        map_manifest = (
            '#EXTM3U\n'
            '#EXT-X-MAP:URI="init.mp4"\n'
            'segment.m4s\n'
        )
        assert not HlsFD.can_download(map_manifest, {})

        # Byte ranges are supported for unencrypted streams, but not together
        # with AES-128 encryption.
        byte_range_manifest = (
            '#EXTM3U\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n'
        )
        assert HlsFD.can_download(byte_range_manifest, {})
        assert not HlsFD.can_download(
            aes_manifest + '#EXT-X-BYTERANGE:1000@0\n', {})

    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 05:25:26.564733
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest_url = 'https://example.com/video/playlist.m3u8'
    manifest = b'''#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
ad-segment.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@2
segment-2.ts?existing=yes
#EXT-X-BYTERANGE:3
https://cdn.example.com/segment-3.ts
#EXT-X-ENDLIST
'''

    class MockResponse(object):
        def geturl(self):
            return manifest_url

        def read(self):
            return manifest

    class MockYDL(object):
        params = {}

        def __init__(self):
            self.urlopen_calls = []

        def urlopen(self, request):
            self.urlopen_calls.append(request)
            return MockResponse()

        def to_screen(self, *args, **kwargs):
            pass

        def report_warning(self, *args, **kwargs):
            raise AssertionError('Unexpected warning: %r' % (args,))

        def report_error(self, *args, **kwargs):
            raise AssertionError('Unexpected error: %r' % (args,))

    class TestHlsFD(HlsFD):
        def __init__(self, ydl):
            super(TestHlsFD, self).__init__(ydl, {})
            self.downloaded_fragments = []
            self.appended_fragments = []
            self.started_ctx = None
            self.finished = False

        def _prepare_url(self, info_dict, url):
            return url

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0
            self.started_ctx = dict(ctx)

        def _download_fragment(self, ctx, frag_url, info_dict, headers=None):
            # Copy headers because real_download may reuse and mutate the same
            # dictionary for subsequent byte ranges.
            self.downloaded_fragments.append((
                frag_url,
                dict(headers or {}),
            ))
            return True, ('fragment-%d' % len(self.downloaded_fragments)).encode('ascii')

        def _append_fragment(self, ctx, frag_content):
            self.appended_fragments.append(frag_content)
            ctx['fragment_index'] += 1

        def _finish_frag_download(self, ctx):
            self.finished = True

    ydl = MockYDL()
    fd = TestHlsFD(ydl)

    info_dict = {
        'url': manifest_url,
        'extra_param_to_segment_url': 'token=abc',
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }

    assert fd.real_download('output.ts', info_dict) is True

    # The manifest contains three media fragments and one