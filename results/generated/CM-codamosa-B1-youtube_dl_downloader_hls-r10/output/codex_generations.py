

# Generated at 2026-10-24 05:55:38.815539
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 05:56:03.706464
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():manifest = b"""#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10.0,
segment-1.ts
#EXT-X-ENDLIST
"""

# Generated at 2026-10-24 05:56:17.728228
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    basic_manifest = '''\
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
segment-1.ts
#EXT-X-ENDLIST
'''

    def manifest_with(tag):
        return basic_manifest.replace('#EXTM3U', '#EXTM3U\n' + tag)

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # Basic VOD playlists are supported.
        assert HlsFD.can_download(basic_manifest, {})
        assert HlsFD.can_download(basic_manifest, {'is_live': False})

        # Live streams are delegated to ffmpeg.
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})

        # Initialization sections are unsupported.
        assert not HlsFD.can_download(
            manifest_with('#EXT-X-MAP:URI="init.mp4"'), {})

        # Unencrypted playlists are supported.
        assert HlsFD.can_download(
            manifest_with('#EXT-X-KEY:METHOD=NONE'), {})

        # Encryption methods other than AES-128 are unsupported.
        for method in ('SAMPLE-AES', 'SAMPLE-AES-CTR'):
            assert not HlsFD.can_download(
                manifest_with('#EXT-X-KEY:METHOD=%s' % method), {})

        aes_manifest = manifest_with(
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"')

        # AES-128 requires an available AES implementation.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported.
        aes_byterange_manifest = aes_manifest.replace(
            '#EXTINF:10,',
            '#EXTINF:10,\n#EXT-X-BYTERANGE:1000@0')
        assert not HlsFD.can_download(aes_byterange_manifest, {})

        # Byte ranges without AES-128 are supported.
        byterange_manifest = basic_manifest.replace(
            '#EXTINF:10,',
            '#EXTINF:10,\n#EXT-X-BYTERANGE:1000@0')
        assert HlsFD.can_download(byterange_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-24 05:56:27.674389
# Unit test for constructor of class HlsFD
def test_HlsFD():
    ydl = object()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = HlsFD(ydl, params)

    assert isinstance(downloader, HlsFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'hlsnative'
    assert isinstance(downloader._progress_hooks, list)
    assert downloader._progress_hooks

# Generated at 2026-10-24 05:57:11.797112
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
        def __init__(self, manifest):
            self.manifest = manifest
            self.opened_urls = []

        def urlopen(self, url):
            self.opened_urls.append(url)
            return FakeResponse(
                'https://cdn.example.com/live/playlist.m3u8',
                self.manifest.encode('utf-8'))

    class TestHlsFD(HlsFD):
        def __init__(self, ydl, params):
            HlsFD.__init__(self, ydl, params)
            self.downloaded_fragments = []
            self.appended_fragments = []
            self.started_ctx = None
            self.finished = False

        def to_screen(self, message, *args, **kwargs):
            pass

        def _prepare_url(self, info_dict, url):
            return url

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0
            self.started_ctx = ctx

        def _download_fragment(self, ctx, frag_url, info_dict, headers=None):
            self.downloaded_fragments.append((frag_url, dict(headers or {})))
            fragment_number = len(self.downloaded_fragments)
            return True, ('fragment-%d' % fragment_number).encode('ascii')

        def _append_fragment(self, ctx, frag_content):
            self.appended_fragments.append(frag_content)

        def _finish_frag_download(self, ctx):
            self.finished = True

    manifest = '''\
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:7
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5.0,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:5.0,
segment-1.ts
#EXTINF:5.0,
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
'''

    ydl

# Generated at 2026-10-24 05:57:45.179982
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 05:58:03.290196
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 05:58:31.996485
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 05:58:50.099754
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 05:59:08.223987
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 05:59:23.278559
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:00:06.306657
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-7.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@10
segment-8.ts
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def __init__(self, content, final_url):
            self._content = content
            self._final_url = final_url

        def read(self):
            return self._content

        def geturl(self):
            return self._final_url

    class FakeYDL(object):
        def __init__(self):
            self.opened_urls = []

        def urlopen(self, url):
            self.opened_urls.append(url)
            return FakeResponse(
                manifest,
                'https://cdn.example.com/videos/media.m3u8')

    ydl = FakeYDL()
    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    downloaded_fragments = []
    appended_content = []
    prepared_contexts = []
    finished_contexts = []

    # Avoid output and filesystem operations performed by FragmentFD.
    fd.to_screen = lambda message: None
    fd._prepare_url = lambda info_dict, url: url

    def prepare_and_start(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(dict(ctx))

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_fragments.append({
            'url': url,
            'headers': dict(headers),
        })
        content = {
            'https://cdn.example.com/videos/segment-7.ts': b'first',
            'https://cdn.example.com/videos/segment-8.ts': b'second',
        }[url]

# Generated at 2026-10-24 06:00:24.467832
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:00:37.269742
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:00:50.771323
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:08.730894
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:11.241463
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:13.741727
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:16.154325
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:01:18.567942
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:01:21.148498
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:01:23.563928
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:01:25.976603
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:01:28.392095
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:01:30.807817
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:33.222613
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:35.638829
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:38.055827
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:40.471704
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:42.886766
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:45.303929
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:47.718604
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:50.135324
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:52.550365
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:54.962498
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:57.376953
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:01:59.790265
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:02:02.203192
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:02:04.620306
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:02:07.034027
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:02:09.452021
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:02:11.863631
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:02:14.278595
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:02:16.695280
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:02:19.108770
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:02:21.523130
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:02:23.938904
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:02:39.273430
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:04:00.783184
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:04:16.452455
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():manifest = (
        '#EXTM3U\n'
        '#EXT-X-MEDIA-SEQUENCE:7\n'
        '#EXTINF:10.0,\n'
        'segment.ts\n'
        '#EXT-X-ENDLIST\n'
    )

# Generated at 2026-10-24 06:04:35.090913
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag
    basic_manifest = (
        '#EXTM3U\n'
        '#EXTINF:10.0,\n'
        'segment.ts\n'
        '#EXT-X-ENDLIST\n'
    )

    try:
        # Ordinary VOD playlists are supported.
        assert HlsFD.can_download(basic_manifest, {})
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=NONE\n'
            '#EXTINF:10.0,\n'
            'segment.ts\n',
            {})

        # Byte ranges are supported unless AES-128 encryption is also used.
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n',
            {})

        # Initialization segments are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-MAP:URI="init.mp4"\n'
            '#EXTINF:10.0,\n'
            'segment.m4s\n',
            {})

        # Encryption methods other than NONE and AES-128 are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
            '#EXTINF:10.0,\n'
            'segment.ts\n',
            {})

        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXTINF:10.0,\n'
            'segment.ts\n'
        )

        # AES-128 requires an available AES implementation.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported even when AES is
        # available.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n',
            {})

        # Native HLS downloading does not support live streams.
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})

    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-24 06:04:37.607810
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:04:40.223069
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:04:42.640343
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 06:04:45.055873
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:04:47.474112
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:04:49.889185
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:05:06.313776
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    info_dict = {}
    original_can_decrypt_frag = can_decrypt_frag

    try:
        # Basic unencrypted playlist is supported.
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXTINF:10,\n'
            'segment.ts\n',
            info_dict)

        # Unencrypted byte-range playlists are supported.
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n',
            info_dict)

        # Live streams are not supported by the native downloader.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXTINF:10,\n'
            'segment.ts\n',
            {'is_live': True})

        # Initialization sections require ffmpeg.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-MAP:URI="init.mp4"\n'
            '#EXTINF:10,\n'
            'segment.m4s\n',
            info_dict)

        # Unsupported encryption methods require ffmpeg.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
            '#EXTINF:10,\n'
            'segment.ts\n',
            info_dict)

        # METHOD=NONE is supported without a crypto implementation.
        can_decrypt_frag = False
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=NONE\n'
            '#EXTINF:10,\n'
            'segment.ts\n',
            info_dict)

        # AES-128 requires an available crypto implementation.
        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXTINF:10,\n'
            'segment.ts\n'
        )
        assert not HlsFD.can_download(aes_manifest, info_dict)

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, info_dict)

        # AES-128 combined with byte ranges is unsupported even when
        # decryption is available.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n',
            info_dict)
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-24 06:05:18.095923
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:05:20.608820
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-24 06:05:23.024980
# Unit test for method can_download of class HlsFD