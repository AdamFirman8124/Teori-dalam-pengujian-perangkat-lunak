

# Generated at 2026-10-25 01:22:11.621214
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    basic_manifest = '''\
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
segment.ts
#EXT-X-ENDLIST
'''

    assert HlsFD.can_download(basic_manifest, {'is_live': False})
    assert not HlsFD.can_download(basic_manifest, {'is_live': True})

    assert HlsFD.can_download(
        basic_manifest + '#EXT-X-KEY:METHOD=NONE\n',
        {'is_live': False})

    assert not HlsFD.can_download(
        basic_manifest + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n',
        {'is_live': False})

    assert not HlsFD.can_download(
        basic_manifest + '#EXT-X-MAP:URI="init.mp4"\n',
        {'is_live': False})

    # Unencrypted byte-range playlists are supported.
    assert HlsFD.can_download(
        basic_manifest + '#EXT-X-BYTERANGE:1000@0\n',
        {'is_live': False})

    aes_manifest = (
        basic_manifest
        + '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
    )
    aes_byte_range_manifest = (
        aes_manifest
        + '#EXT-X-BYTERANGE:1000@0\n'
    )

    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {'is_live': False})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {'is_live': False})

        # AES-128 combined with byte ranges is unsupported even when
        # the AES implementation is available.
        assert not HlsFD.can_download(
            aes_byte_range_manifest, {'is_live': False})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:22:35.584173
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:5
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
segment-2.ts
#EXT-X-ENDLIST
'''

    manifest_response = Mock()
    manifest_response.geturl.return_value = (
        'https://cdn.example.com/video/master.m3u8')
    manifest_response.read.return_value = manifest.encode('utf-8')

    ydl = Mock()
    ydl.urlopen.return_value = manifest_response

    # Avoid depending on FragmentFD/FileDownloader initialization so this
    # remains a focused unit test for HlsFD.real_download.
    fd = object.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {}
    fd._progress_hooks = []

    fd.to_screen = Mock()
    fd._prepare_url = Mock(side_effect=lambda info, url: url)

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(
        side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'first-fragment'),
        (True, b'second-fragment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'url': 'https://origin.example.com/video/master.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True

    ydl.urlopen.assert_called_once_with(
        'https://origin.example.com/video/master.m3u8')

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1
    assert ctx['fragment_index'] == 0

    # Segment URLs must be resolved against the final manifest URL. The ad
    # fragment must not be downloaded.
    download_calls = fd._download_fragment.call_args_list
    assert len(download_calls) == 2

# Generated at 2026-10-25 01:22:59.526298
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock, call
    except ImportError:
        from mock import Mock, call

    manifest_url = 'https://example.com/master.m3u8'
    redirected_manifest_url = 'https://cdn.example.com/hls/index.m3u8'

    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:42
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
'''

    manifest_response = Mock()
    manifest_response.geturl.return_value = redirected_manifest_url
    manifest_response.read.return_value = manifest.encode('utf-8')

    ydl = Mock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }
    fd._

# Generated at 2026-10-25 01:23:24.529115
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:23:26.947046
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:23:29.592847
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:23:32.007440
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 01:23:34.424181
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 01:23:36.839402
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 01:23:48.289022
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    plain_manifest = '#EXTM3U\n#EXTINF:10,\nsegment.ts\n'
    assert HlsFD.can_download(plain_manifest, {})
    assert not HlsFD.can_download(plain_manifest, {'is_live': True})

    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\n#EXTINF:10,\nsegment.ts\n', {})

    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
        '#EXTINF:10,\nsegment.ts\n',
        {})

    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-MAP:URI="init.mp4"\n'
        '#EXTINF:10,\nsegment.m4s\n',
        {})

    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXTINF:10,\nsegment.ts\n'
    )
    aes_byterange_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXT-X-BYTERANGE:1000@0\n'
        'segment.ts\n'
    )

    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})
        assert not HlsFD.can_download(aes_byterange_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:24:05.333620
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    base_manifest = '''\
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10,
segment0.ts
#EXT-X-ENDLIST
'''

    info_dict = {'is_live': False}
    method_globals = HlsFD.can_download.__globals__
    original_can_decrypt_frag = method_globals['can_decrypt_frag']

    try:
        # Ordinary VOD playlists are supported.
        assert HlsFD.can_download(base_manifest, info_dict)

        # Unencrypted byte-range playlists are supported.
        assert HlsFD.can_download(
            base_manifest.replace(
                '#EXTINF:10,',
                '#EXTINF:10,\n#EXT-X-BYTERANGE:1000@0'),
            info_dict)

        # Explicitly unencrypted playlists are supported.
        assert HlsFD.can_download(
            base_manifest.replace(
                '#EXTM3U',
                '#EXTM3U\n#EXT-X-KEY:METHOD=NONE'),
            info_dict)

        # Unsupported encryption methods must be rejected.
        assert not HlsFD.can_download(
            base_manifest.replace(
                '#EXTM3U',
                '#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"'),
            info_dict)

        # Initialization sections are unsupported.
        assert not HlsFD.can_download(
            base_manifest.replace(
                '#EXTM3U',
                '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"'),
            info_dict)

        # Live streams are unsupported.
        assert not HlsFD.can_download(base_manifest, {'is_live': True})

        aes_manifest = base_manifest.replace(
            '#EXTM3U',
            '#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI="key.bin"')

        # AES-128 requires the crypto dependency.
        method_globals['can_decrypt_frag'] = False
        assert not HlsFD.can_download(aes_manifest, info_dict)

        method_globals['can_decrypt_frag'] = True
        assert HlsFD.can_download(aes_manifest, info_dict)

        # AES-128 combined with byte ranges is unsupported even when
        # decryption is available.
        aes_byte_range_manifest = aes_manifest.replace(
            '#EXTINF:10,',
            '#EXTINF:10,\n#EXT-X-BYTERANGE:1000@0')
        assert not HlsFD.can_download(aes_byte_range_manifest, info_dict)
    finally:
        method_globals['can_decrypt_frag'] = original_can_decrypt_frag

# Generated at 2026-10-25 01:24:31.806282
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

# Generated at 2026-10-25 01:24:34.386418
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:36.800355
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:39.214318
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:41.635817
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:44.051810
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:46.470405
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:48.884101
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:51.302654
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:53.716046
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:56.131497
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:24:58.545659
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:25:00.961172
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:25:03.377043
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:25:05.794698
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:25:07.192472
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:25:18.296099
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    plain_manifest = '''\
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
segment.ts
#EXT-X-ENDLIST
'''

    assert HlsFD.can_download(plain_manifest, {})
    assert not HlsFD.can_download(plain_manifest, {'is_live': True})

    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts\n',
        {'is_live': False})

    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key"\nsegment.ts\n',
        {'is_live': False})

    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s\n',
        {'is_live': False})

    aes_manifest = '''\
#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key"
#EXTINF:10,
segment.ts
'''

    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {'is_live': False})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {'is_live': False})

        aes_byterange_manifest = aes_manifest + (
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n'
        )
        assert not HlsFD.can_download(
            aes_byterange_manifest, {'is_live': False})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:25:40.927500
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    class FakeResponse(object):
        def geturl(self):
            # Simulate a redirected manifest URL. Relative fragment URLs must
            # be resolved against this URL rather than the original one.
            return 'https://cdn.example.com/video/index.m3u8'

        def read(self):
            return b'''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#UPLYNK-SEGMENT,ad
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXTINF:10,
segment-1.ts
#EXT-X-BYTERANGE:4@2
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
'''

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

    # Isolate real_download from FragmentFD's file and progress handling.
    fd.to_screen = lambda message: None
    fd._prepare_url = lambda info_dict, url: url

    prepared_contexts = []
    downloaded_fragments = []
    appended_fragments = []
    finished_contexts = []

    def prepare_and_start(ctx):
        # FragmentFD normally initializes this value.
        ctx['fragment_index'] = 0
        prepared_contexts.append(dict(ctx))

    fragment_contents = {
        'https://cdn.example.com/video/segment-1.ts': b'first',
        'https://cdn.example.com/video/segment-2.ts': b'second',
    }

    def download_fragment(ctx, frag_url, info_dict, headers):
        downloaded_fragments.append((frag_url, dict(headers)))
        return True, fragment_contents[frag_url]

    def append_fragment(ctx, content):
        appended_fragments.append(content)

    def finish_fragment_download(ctx):
        finished_contexts.append(dict(ctx))

    fd._prepare_and_start_frag_download = prepare_and_start
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd

# Generated at 2026-10-25 01:26:03.251019
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import MagicMock, call

    manifest_url = 'https://example.com/original/playlist.m3u8'
    redirected_url = 'https://cdn.example.com/hls/playlist.m3u8'
    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#UPLYNK-SEGMENT,ad
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXTINF:10,
/segment-2.ts
#EXT-X-ENDLIST
'''

    response = MagicMock()
    response.geturl.return_value = redirected_url
    response.read.return_value = manifest.encode('utf-8')

    ydl = MagicMock()
    ydl.urlopen.return_value = response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    })

    fd.to_screen = MagicMock()
    fd._prepare_url = MagicMock(return_value=manifest_url)

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'first-fragment'),
        (True, b'second-fragment'),
    ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'url': manifest_url,
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }

    assert fd.real_download('output.ts', info_dict) is True

    fd._prepare_url.assert_called_once_with(info_dict, manifest_url)
    ydl.urlopen.assert_called_once_with(manifest_url)

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1
    assert ctx['fragment_index'] == 0

    headers = info_dict['http_headers']

# Generated at 2026-10-25 01:26:05.784638
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:26:08.199465
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:26:22.880633
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:26:48.104378
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#UPLYNK-SEGMENT,ad
#EXTINF:5,
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXTINF:10,
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def read(self):
            return manifest

        def geturl(self):
            # Simulate a manifest redirect. Relative fragments should be
            # resolved against this URL rather than the original URL.
            return 'https://cdn.example.com/hls/media.m3u8'

    class FakeYDL(object):
        def __init__(self):
            self.requested_urls = []

        def urlopen(self, url):
            self.requested_urls.append(url)
            return FakeResponse()

    class TestHlsFD(HlsFD):
        def __init__(self, ydl):
            HlsFD.__init__(self, ydl, {})
            self.downloaded_fragments = []
            self.appended_fragments = []
            self.started_ctx = None
            self.finished_ctx = None

        def to_screen(self, message):
            pass

        def _prepare_url(self, info_dict, url):
            return url

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0
            self.started_ctx = ctx

        def _download_fragment(self, ctx, frag_url, info_dict, headers=None):
            self.downloaded_fragments.append((
                frag_url,
                dict(headers or {}),
            ))
            fragment_number = len(self.downloaded_fragments)
            return True, ('fragment-%d' % fragment_number).encode('ascii')

        def _append_fragment(self, ctx, frag_content):
            self.appended_fragments.append(frag_content)
            ctx['fragment_index'] += 1

        def _finish_frag_download(self, ctx):
            self.finished_ctx = ctx

    ydl = FakeYDL()
    downloader = TestHlsFD(ydl)


# Generated at 2026-10-25 01:26:50.749693
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:26:53.279878
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:26:55.817589
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:26:58.234316
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:00.652675
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:03.068889
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:05.485342
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:07.901995
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:10.316194
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:12.730650
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:15.144416
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:16.607549
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:27:27.741658
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag
    try:
        basic_manifest = '''#EXTM3U
#EXTINF:10,
segment-1.ts
'''

        assert HlsFD.can_download(basic_manifest, {})
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment-1.ts', {})
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-BYTERANGE:100@0\nsegment-1.ts', {})

        # Live streams are unsupported.
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})

        # Initialization segments are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment-1.m4s', {})

        # Encryption methods other than NONE and AES-128 are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
            'segment-1.ts',
            {})

        aes_manifest = '''#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXTINF:10,
segment-1.ts
'''

        # AES-128 requires the crypto dependency.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is always unsupported.
        aes_byterange_manifest = '''#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXT-X-BYTERANGE:100@0
segment-1.ts
'''
        assert not HlsFD.can_download(aes_byterange_manifest, {})

    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:27:52.547439
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    class FakeResponse(object):
        def __init__(self, url, content):
            self._url = url
            self._content = content

        def geturl(self):
            return self._url

        def read(self):
            return self._content

    manifest = b'''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10,
https://cdn.example/video/segment-2.ts?existing=yes
#EXT-X-ENDLIST
'''

    manifest_url = 'https://media.example/video/index.m3u8'
    ydl = MagicMock()
    ydl.urlopen.return_value = FakeResponse(manifest_url, manifest)

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    # Keep the test isolated from filesystem and networking behavior inherited
    # from FragmentFD.
    fd._prepare_url = MagicMock(side_effect=lambda info, url: url)

    prepared_contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx.copy())

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)

    fragment_contents = {
        '/video/segment-1.ts': b'first fragment',
        '/video/segment-2.ts': b'second fragment',
    }

    def download_fragment(ctx, url, info_dict, headers):
        path = compat_urlparse.urlparse(url).path
        return True, fragment_contents[path]

    fd._download_fragment = MagicMock(side_effect=download_fragment)
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()


# Generated at 2026-10-25 01:28:03.803411
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    vod_info = {'is_live': False}
    live_info = {'is_live': True}

    basic_manifest = """#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
segment.ts
#EXT-X-ENDLIST
"""

    # Ordinary VOD playlists are supported.
    assert HlsFD.can_download(basic_manifest, vod_info)

    # Live playlists are delegated to ffmpeg.
    assert not HlsFD.can_download(basic_manifest, live_info)

    # Unsupported encryption methods are rejected.
    unsupported_encryption = """#EXTM3U
#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"
#EXTINF:10,
segment.ts
"""
    assert not HlsFD.can_download(unsupported_encryption, vod_info)

    # Initialization segments are unsupported.
    initialization_segment = """#EXTM3U
#EXT-X-MAP:URI="init.mp4"
#EXTINF:10,
segment.m4s
"""
    assert not HlsFD.can_download(initialization_segment, vod_info)

    # Unencrypted byte-range playlists are supported.
    byte_range_manifest = """#EXTM3U
#EXT-X-BYTERANGE:1000@0
segment.ts
"""
    assert HlsFD.can_download(byte_range_manifest, vod_info)

    aes_manifest = """#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXTINF:10,
segment.ts
"""

    aes_byte_range_manifest = """#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXT-X-BYTERANGE:1000@0
segment.ts
"""

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # AES-128 requires crypto support.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, vod_info)

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, vod_info)

        # AES-128 combined with byte ranges is always unsupported.
        assert not HlsFD.can_download(aes_byte_range_manifest, vod_info)
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:28:06.408609
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:28:08.943451
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:28:11.359449
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:28:13.772827
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:28:16.189959
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:28:17.569630
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:08.624105
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():import os

# Generated at 2026-10-25 01:29:11.040861
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:13.459404
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:15.876085
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:18.289272
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:29:20.713006
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:29:23.133457
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:29:25.550301
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:27.970823
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:30.383173
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:32.797289
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:29:35.212945
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:29:37.627125
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 01:29:40.042202
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:42.457881
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:29:45.275486
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:31.029214
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():manifest = b"""#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10,
segment1.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@2
segment2.ts
#EXT-X-ENDLIST
"""


# Generated at 2026-10-25 01:30:33.445985
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:35.860549
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:38.420341
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:40.834533
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:43.249413
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:45.665435
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:48.082097
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:50.499277
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:30:52.913493
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:31:15.318671
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():from unittest.mock import Mock, call


# Generated at 2026-10-25 01:31:34.322327
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    info_dict = {'is_live': False}
    manifest = '''\
#EXTM3U
#EXTINF:10,
segment.ts
#EXT-X-ENDLIST
'''

    # Ordinary VOD playlists are supported.
    assert HlsFD.can_download(manifest, info_dict)

    # Live playlists are not supported by the native downloader.
    assert not HlsFD.can_download(manifest, {'is_live': True})

    # Initialization segments require ffmpeg.
    assert not HlsFD.can_download(
        manifest + '#EXT-X-MAP:URI="init.mp4"\n', info_dict)

    # Unencrypted byte ranges are supported.
    assert HlsFD.can_download(
        manifest + '#EXT-X-BYTERANGE:1000@0\n', info_dict)

    # Encryption methods other than NONE and AES-128 are unsupported.
    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
        '#EXTINF:10,\nsegment.ts\n',
        info_dict)

    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXTINF:10,\n'
        'segment.ts\n'
        '#EXT-X-ENDLIST\n'
    )

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # AES-128 requires the Crypto dependency.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, info_dict)

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, info_dict)

        # AES-128 combined with byte ranges is unsupported.
        assert not HlsFD.can_download(
            aes_manifest + '#EXT-X-BYTERANGE:1000@0\n',
            info_dict)
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:31:57.351743
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest_url = 'https://example.com/master.m3u8'
    redirected_manifest_url = 'https://cdn.example.com/video/index.m3u8'

    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
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
'''

    response = Mock()
    response.geturl.return_value = redirected_manifest_url
    response.read.return_value = manifest.encode('utf-8')

    ydl = Mock()
    ydl.urlopen.return_value = response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd.to_screen = Mock()
    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    prepared_contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(dict(ctx))

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)

    downloaded_fragments = []

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_fragments.append((url, dict(headers)))
        if url.startswith('https://cdn.example.com/video/segment-1.ts'):
            return True, b'first fragment'
        if url.startswith('https://cdn.example.com/video/segment-2.ts'):
            return True, b'second fragment'
        raise AssertionError('Unexpected fragment URL: %s' % url)

    fd._download_fragment = Mock(side_effect=download_fragment)

    appended_fragments = []
    fd._append_fragment = Mock(
        side_effect=lambda ctx, content: appended_fragments.append(content))
    fd._finish_frag_download = Mock()


# Generated at 2026-10-25 01:32:08.716927
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag
    try:
        basic_manifest = '#EXTM3U\n#EXTINF:10,\nsegment.ts\n#EXT-X-ENDLIST'
        assert HlsFD.can_download(basic_manifest, {})
        assert HlsFD.can_download('#EXTM3U\n#EXT-X-KEY:METHOD=NONE', {})

        # Live streams are unsupported.
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})

        # Unsupported encryption methods are rejected.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"', {})

        # Initialization sections are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s', {})

        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXTINF:10,\n'
            'segment.ts\n'
        )

        # AES-128 requires an available crypto implementation.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported.
        assert not HlsFD.can_download(
            aes_manifest + '#EXT-X-BYTERANGE:1024@0\n', {})

    finally:
        can_decrypt_frag = original_can_decrypt_frag