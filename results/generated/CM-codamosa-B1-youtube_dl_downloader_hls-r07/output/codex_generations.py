

# Generated at 2026-10-25 01:03:53.478129
# Unit test for constructor of class HlsFD
def test_HlsFD():ydl = object()

# Generated at 2026-10-25 01:04:13.547355
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

# Generated at 2026-10-25 01:04:14.980510
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

# Generated at 2026-10-25 01:04:43.228302
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:04:44.680223
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:04:46.007305
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:05:39.204866
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:05:41.623137
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:05:44.036950
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:05:46.452498
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:05:48.865218
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:05:51.279883
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:05:53.698980
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:05:56.114160
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:05:58.529553
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:06:00.944027
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:06:03.359762
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:06:05.773169
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:06:08.188607
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:06:10.604999
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:06:13.019855
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:06:15.435259
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:06:17.992372
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:06:19.326410
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:07:15.513359
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:07:17.932216
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:07:20.346750
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:07:46.951381
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock, call
    except ImportError:
        from mock import Mock, call

    manifest_url = 'https://example.com/master/playlist.m3u8'
    redirected_manifest_url = 'https://cdn.example.com/media/playlist.m3u8'
    filename = 'output.ts'

    manifest = b'''\
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:5.0,
segment-1.ts
#UPLYNK-SEGMENT,ad
#EXTINF:5.0,
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXTINF:5.0,
segment-2.ts
#EXT-X-ENDLIST
'''

    response = Mock()
    response.geturl.return_value = redirected_manifest_url
    response.read.return_value = manifest

    ydl = Mock

# Generated at 2026-10-25 01:08:10.607888
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class FakeResponse(object):
        def __init__(self, url, data):
            self._url = url
            self._data = data

        def geturl(self):
            return self._url

        def read(self):
            return self._data

    manifest = (
        '#EXTM3U\n'
        '#EXT-X-MEDIA-SEQUENCE:7\n'
        '#EXTINF:10,\n'
        'segment-1.ts\n'
        '#ANVATO-SEGMENT-INFO:type=ad\n'
        '#EXTINF:5,\n'
        'advertisement.ts\n'
        '#ANVATO-SEGMENT-INFO:type=master\n'
        '#EXT-X-BYTERANGE:4@2\n'
        '#EXTINF:10,\n'
        'segment-2.ts\n'
        '#EXT-X-ENDLIST\n'
    ).encode('utf-8')

    class FakeYDL(object):
        def __init__(self):
            self.requested_urls = []

        def urlopen(self, url):
            self.requested_urls.append(url)
            return FakeResponse(
                'https://cdn.example.test/media/index.m3u8',
                manifest)

    ydl = FakeYDL()
    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    messages = []
    prepared_contexts = []
    download_calls = []
    appended_fragments = []
    finished_contexts = []

    fd.to_screen = lambda message: messages.append(message)
    fd._prepare_url = lambda info_dict, url: url

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx.copy())

    def download_fragment(ctx, url, info_dict, headers):
        download_calls.append((url, dict(headers)))
        contents = {
            'https://cdn.example.test/media/segment-1.ts?token=abc':
                b'first-fragment',
            'https://cdn.example.test/media/segment-2.ts?token=abc':
                b'second-fragment',
        }
        return True, contents[url]

    def append_fragment(ctx, content):
        appended_fragments.append(content)

# Generated at 2026-10-25 01:08:13.026823
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:08:15.593146
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:08:18.009614
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:08:20.423992
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:08:22.842556
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:08:27.614670
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():manifest = '#EXTM3U\n#EXTINF:10.0,\nsegment.ts\n#EXT-X-ENDLIST\n'

# Generated at 2026-10-25 01:08:47.458509
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import MagicMock, call
    except ImportError:
        from mock import MagicMock, call

    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#UPLYNK-SEGMENT,ad
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXTINF:10,
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
'''

    manifest_response = MagicMock()
    manifest_response.geturl.return_value = (
        'https://cdn.example.com/hls/playlist.m3u8')
    manifest_response.read.return_value = manifest.encode('utf-8')

    ydl = MagicMock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    })

    fd.to_screen = MagicMock()
    fd._prepare_url = MagicMock(
        side_effect=lambda info_dict, url: url)

    def prepare_download(ctx):
        # FragmentFD normally initializes this value.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(
        side_effect=[
            (True, b'first fragment'),
            (True, b'second fragment'),
        ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'url': 'https://example.com/original/playlist.m3u8',
        'is_live': False,
        'http_headers': {'User-Agent': 'test-agent'},
    }

    assert fd.real_download('output.ts', info_dict) is True

    ydl.urlopen.assert_called_once_with(
        'https://example.com/original/playlist.m3u8')

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    headers = info_dict['http_headers']
    fd._download_fragment.assert_has_calls([
        call(
            ctx,
            'https://cdn.example.com/hls/segment-1.ts',
            info_dict,
            headers),
        call(
            ctx,
            'https://media.example.com/segment-2.ts',
            info_dict,
            headers),
    ])

    appended_fragments = [
        fragment_call[0][1]
        for fragment_call in fd._append_fragment.call_args_list
    ]
    assert appended_fragments == [
        b'first fragment',
        b'second fragment',
    ]

    # The advertisement URL must not be downloaded.
    downloaded_urls = [
        fragment_call[0][1]
        for fragment_call in fd._download_fragment.call_args_list
    ]
    assert all('advertisement.ts' not in url for url in downloaded_urls)

    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:09:13.934683
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:09:16.460625
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:09:18.876050
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:09:21.294547
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:09:23.705718
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:09:26.121602
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:09:38.670249
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():global can_decrypt_frag


# Generated at 2026-10-25 01:09:53.405556
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    vod_info = {'is_live': False}

    basic_manifest = (
        '#EXTM3U\n'
        '#EXTINF:10,\n'
        'segment.ts\n'
    )

    # Ordinary VOD playlists are supported.
    assert HlsFD.can_download(basic_manifest, vod_info)

    # Live streams are not supported by the native downloader.
    assert not HlsFD.can_download(basic_manifest, {'is_live': True})

    # Explicitly unencrypted streams are supported.
    none_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=NONE\n'
        '#EXTINF:10,\n'
        'segment.ts\n'
    )
    assert HlsFD.can_download(none_manifest, vod_info)

    # Encryption methods other than AES-128 are unsupported.
    unsupported_encryption_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
        '#EXTINF:10,\n'
        'segment.ts\n'
    )
    assert not HlsFD.can_download(
        unsupported_encryption_manifest, vod_info)

    # Initialization segments require ffmpeg.
    map_manifest = (
        '#EXTM3U\n'
        '#EXT-X-MAP:URI="init.mp4"\n'
        '#EXTINF:10,\n'
        'segment.m4s\n'
    )
    assert not HlsFD.can_download(map_manifest, vod_info)

    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXTINF:10,\n'
        'segment.ts\n'
    )
    aes_byterange_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXT-X-BYTERANGE:1000@0\n'
        'segment.ts\n'
    )

    # Make AES tests deterministic regardless of whether Crypto is installed.
    function_globals = HlsFD.can_download.__globals__
    original_can_decrypt_frag = function_globals['can_decrypt_frag']

    try:
        function_globals['can_decrypt_frag'] = False
        assert not HlsFD.can_download(aes_manifest, vod_info)

        function_globals['can_decrypt_frag'] = True
        assert HlsFD.can_download(aes_manifest, vod_info)

        # AES-128 combined with byte ranges remains unsupported.
        assert not HlsFD.can_download(aes_byterange_manifest, vod_info)
    finally:
        function_globals['can_decrypt_frag'] = original_can_decrypt_frag

# Generated at 2026-10-25 01:10:19.731533
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest_url = 'https://cdn.example/video/playlist.m3u8'
    redirected_manifest_url = (
        'https://cdn.example/video/final-playlist.m3u8?source=test'
    )


# Generated at 2026-10-25 01:10:22.264066
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:10:24.681731
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:10:27.098010
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:10:29.514449
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:10:31.929221
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:10:34.344319
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:10:57.958622
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import MagicMock, call

    manifest = b"""#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@2
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
"""

    response = MagicMock()
    response.geturl.return_value = 'https://cdn.example.com/media/playlist.m3u8'
    response.read.return_value = manifest

    ydl = MagicMock()
    ydl.urlopen.return_value = response

    # Construct the downloader without invoking unrelated initialization logic.
    fd = object.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    }
    fd._progress_hooks = []

    fd.to_screen = MagicMock()
    fd.report_error = MagicMock()
    fd.report_warning = MagicMock()
    fd.report_skip_fragment = MagicMock()
    fd.report_retry_fragment = MagicMock()
    fd._prepare_url = MagicMock(
        return_value='https://example.com/original/playlist.m3u8')

    prepared_contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx)

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    downloaded_fragments = []

    def download_fragment(ctx, url, info_dict, headers):
        # Copy headers because real_download mutates the original dictionary
        # when processing byte ranges.
        downloaded_fragments.append((url, dict(headers)))
        content = (
            b'first-fragment'
            if len(downloaded_fragments) == 1
            else b'second-fragment'
        )
        return True, content

    fd._download_fragment = MagicMock(side_effect=download_fragment)


# Generated at 2026-10-25 01:11:24.843038
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:27.257534
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:29.672976
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:32.244349
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:34.659260
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:37.073341
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:39.487992
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:40.867187
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:42.249935
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:11:57.115820
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:12:03.273259
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():manifest = '#EXTM3U\n#EXTINF:10.0,\nsegment.ts\n#EXT-X-ENDLIST\n'

# Generated at 2026-10-25 01:12:28.143563
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:10
segment-1.ts
#UPLYNK-SEGMENT,ad
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXT-X-BYTERANGE:4@2
segment-2.ts
#EXT-X-BYTERANGE:3
segment-2.ts
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def read(self):
            return manifest

        def geturl(self):
            # Simulate a redirect and ensure relative fragments use the final URL.
            return 'https://cdn.example/video/playlist.m3u8'

    class FakeYDL(object):
        def __init__(self):
            self.requested_urls = []

        def urlopen(self, url):
            self.requested_urls.append(url)
            return FakeResponse()


# Generated at 2026-10-25 01:12:30.559660
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:32.977686
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:35.389818
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:38.008716
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:40.420365
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:42.837567
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:45.251615
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:47.667279
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:50.081813
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:52.496932
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:54.910997
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:57.326125
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:12:59.740862
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:13:02.155588
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:13:04.583543
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:13:06.997570
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:13:09.596928
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:13:10.992632
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:13:36.896007
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest import mock
    except ImportError:
        import mock

    manifest = b'''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
segment-1.ts
#UPLYNK-SEGMENT,ad
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXT-X-BYTERANGE:4@2
segment-2.ts
#EXT-X-ENDLIST
'''

    response = mock.Mock()
    response.geturl.return_value = 'https://cdn.example.com/video/playlist.m3u8'
    response.read.return_value = manifest

    ydl = mock.Mock()
    ydl.urlopen.return_value = response

    info_dict = {
        'url': 'https://example.com/original.m3u8',
    }

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd._prepare_url = mock.Mock(
        side_effect=lambda unused_info_dict, url: url)

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = mock.Mock(
        side_effect=prepare_download)
    fd._download_fragment = mock.Mock(side_effect=[
        (True, b'first fragment'),
        (True, b'second fragment'),
    ])
    fd._append_fragment = mock.Mock()
    fd._finish_frag_download = mock.Mock()

    result = fd.real_download('output.ts', info_dict)

    assert result is True
    assert fd._prepare_and_start_frag_download.call_count == 1

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_count == 2

    first_download = fd._download_fragment.call_args_list[0][0]
    assert first_download[0] is ctx

# Generated at 2026-10-25 01:14:05.095818
# Unit test for method real_download of class HlsFD