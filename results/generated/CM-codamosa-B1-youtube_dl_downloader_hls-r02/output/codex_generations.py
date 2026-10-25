

# Generated at 2026-10-25 01:35:09.763261
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    vod_manifest = '\n'.join((
        '#EXTM3U',
        '#EXT-X-TARGETDURATION:10',
        '#EXTINF:10,',
        'segment.ts',
        '#EXT-X-ENDLIST',
    ))

    assert HlsFD.can_download(vod_manifest, {})
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts',
        {})
    assert not HlsFD.can_download(vod_manifest, {'is_live': True})
    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s',
        {})
    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key"\nsegment.ts',
        {})

    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        'segment.ts'
    )
    aes_byterange_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXT-X-BYTERANGE:1000@0\n'
        'segment.ts'
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

# Generated at 2026-10-25 01:35:27.579755
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest import mock
    except ImportError:
        import mock

    manifest = b'''\
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:5.0,
segment-1.ts
#ANVATO-SEGMENT-INFO,type=ad
#EXTINF:5.0,
advertisement.ts
#ANVATO-SEGMENT-INFO,type=master
#EXTINF:5.0,
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
'''

    manifest_response = mock.Mock()
    manifest_response.geturl.return_value = (
        'https://cdn.example.com/videos/index.m3u8')
    manifest_response.read.return_value = manifest

    ydl = mock.Mock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd.to_screen = mock.Mock()
    fd.report_warning = mock.Mock()
    fd.report_error = mock.Mock()
    fd._prepare_url = mock.Mock(side_effect=lambda info, url: url)

    prepared_ctx = {}

    def prepare_download(ctx):
        prepared_ctx.update(ctx)
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = mock.Mock(
        side_effect=prepare_download)
    fd._download_fragment = mock.Mock(side_effect=[
        (True, b'first fragment'),
        (True, b'second fragment'),
    ])
    fd._append_fragment = mock.Mock()
    fd._finish_frag_download = mock.Mock()

    info_dict = {
        'url': 'https://example.com/master.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True
    assert prepared_ctx['filename'] == 'output.ts'
    assert prepared_ctx['total_frags'] == 2
    assert prepared_ctx['ad_frags'] == 1

    downloaded_urls = [
        call_args[0][1]
        for call_args in fd._download_fragment.call_args_list
    ]
    assert downloaded_urls == [
        'https://cdn.example.com/videos/segment-1.ts',
        'https://media.example.com/segment-2.ts',
    ]

    appended_contents = [
        call_args[0][1]
        for call_args in fd._append_fragment.call_args_list
    ]
    assert appended_contents == [
        b'first fragment',
        b'second fragment',
    ]

    # The advertisement must not be downloaded.
    assert all(
        'advertisement.ts' not in url
        for url in downloaded_urls
    )

    ydl.urlopen.assert_called_once_with(
        'https://example.com/master.m3u8')
    fd._finish_frag_download.assert_called_once()
    fd.report_error.assert_not_called()

# Generated at 2026-10-25 01:35:29.996262
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 01:35:32.419568
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 01:35:34.834799
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 01:35:37.253398
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 01:35:39.668679
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 01:35:48.161751
# Unit test for constructor of class HlsFD
def test_HlsFD():ydl = object()

# Generated at 2026-10-25 01:35:59.081172
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    plain_manifest = '''\
#EXTM3U
#EXTINF:10,
segment-1.ts
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
'''
    assert HlsFD.can_download(plain_manifest, {})
    assert not HlsFD.can_download(plain_manifest, {'is_live': True})

    none_encryption_manifest = '''\
#EXTM3U
#EXT-X-KEY:METHOD=NONE
#EXTINF:10,
segment.ts
'''
    assert HlsFD.can_download(none_encryption_manifest, {})

    aes128_manifest = '''\
#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXTINF:10,
segment.ts
'''
    assert HlsFD.can_download(aes128_manifest, {}) == can_decrypt_frag

    aes128_byte_range_manifest = '''\
#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXT-X-BYTERANGE:1000@0
segment.ts
'''
    assert not HlsFD.can_download(aes128_byte_range_manifest, {})

    unsupported_encryption_manifest = '''\
#EXTM3U
#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"
#EXTINF:10,
segment.ts
'''
    assert not HlsFD.can_download(unsupported_encryption_manifest, {})

    initialization_segment_manifest = '''\
#EXTM3U
#EXT-X-MAP:URI="init.mp4"
#EXTINF:10,
segment.m4s
'''
    assert not HlsFD.can_download(initialization_segment_manifest, {})

    # Byte ranges are supported when AES-128 encryption is not being used.
    byte_range_manifest = '''\
#EXTM3U
#EXT-X-BYTERANGE:1000@0
segment.ts
'''
    assert HlsFD.can_download(byte_range_manifest, {})

# Generated at 2026-10-25 01:36:21.954298
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock, call
    except ImportError:
        from mock import Mock, call

    manifest_url = 'https://example.test/hls/index.m3u8'
    manifest = '''\
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10.0,
segment-1.ts
#UPLYNK-SEGMENT,ad
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXTINF:10.0,
/segment-2.ts
#EXT-X-ENDLIST
'''

    manifest_response = Mock()
    manifest_response.geturl.return_value = manifest_url
    manifest_response.read.return_value = manifest.encode('utf-8')

    ydl = Mock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'first fragment'),
        (True, b'second fragment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'url': manifest_url,
        'http_headers': {'User-Agent': 'test-agent'},
    }

    assert fd.real_download('output.ts', info_dict) is True

    # The manifest is fetched once.
    ydl.urlopen.assert_called_once_with(manifest_url)

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    # The advertisement must not be downloaded.
    downloaded_urls = [
        download_call[0][1]
        for download_call in fd._download_fragment.call_args_list
    ]
    assert downloaded_urls

# Generated at 2026-10-25 01:36:45.172745
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest_url = 'https://example.com/master/playlist.m3u8'
    redirected_manifest_url = 'https://cdn.example.com/media/playlist.m3u8'

    manifest = """\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:5.0,
segment-10.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5.0,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:5.0,
segment-11.ts
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def geturl(self):
            return redirected_manifest_url

        def read(self):
            return manifest.encode('utf-8')

    ydl = mock.Mock()
    ydl.urlopen.return_value

# Generated at 2026-10-25 01:36:57.702812
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    info_dict = {}
    basic_manifest = '''\
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
segment.ts
#EXT-X-ENDLIST
'''

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # Basic VOD playlists are supported.
        assert HlsFD.can_download(basic_manifest, info_dict)

        # Live streams are not supported by the native downloader.
        assert not HlsFD.can_download(
            basic_manifest, {'is_live': True})

        # Initialization segments require ffmpeg.
        assert not HlsFD.can_download(
            basic_manifest + '#EXT-X-MAP:URI="init.mp4"\n', info_dict)

        # Unsupported encryption methods require ffmpeg.
        assert not HlsFD.can_download(
            basic_manifest + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n',
            info_dict)

        # Explicitly unencrypted streams remain supported.
        assert HlsFD.can_download(
            basic_manifest + '#EXT-X-KEY:METHOD=NONE\n', info_dict)

        # Unencrypted byte-range playlists are supported.
        assert HlsFD.can_download(
            basic_manifest + '#EXT-X-BYTERANGE:1000@0\n', info_dict)

        aes_manifest = (
            basic_manifest
            + '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        )

        # AES-128 requires the optional Crypto dependency.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, info_dict)

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, info_dict)

        # AES-128 combined with byte ranges is unsupported even when
        # decryption support is available.
        assert not HlsFD.can_download(
            aes_manifest + '#EXT-X-BYTERANGE:1000@0\n', info_dict)
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:37:15.250955
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock, call
    except ImportError:
        from mock import Mock, call

    manifest_url = 'https://example.com/path/playlist.m3u8'
    manifest = '''\
#EXTM3U
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

    manifest_response = Mock()
    manifest_response.geturl.return_value = manifest_url
    manifest_response.read.return_value = manifest.encode('utf-8')

    ydl = Mock()
    ydl.urlopen.return_value = manifest_response

    downloader = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare_fragment_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    downloader._prepare_and_start_frag_download = Mock(
        side_effect=prepare_fragment_download)
    downloader._download_fragment = Mock(side_effect=[
        (True, b'first fragment'),
        (True, b'second fragment'),
    ])
    downloader._append_fragment = Mock()
    downloader._finish_frag_download = Mock()

    info_dict = {
        'url': manifest_url,
        'is_live': False,
    }

    assert downloader.real_download('output.ts', info_dict) is True

    prepared_ctx = (
        downloader._prepare_and_start_frag_download.call_args[0][0])
    assert prepared_ctx['filename'] == 'output.ts'
    assert prepared_ctx['total_frags'] == 2
    assert prepared_ctx['ad_frags'] == 1

    downloaded_urls = [
        invocation[0][1]
        for invocation in downloader._download_fragment.call_args_list
    ]
    assert downloaded_urls == [
        'https://example.com/path/segment-1.ts',
        'https://example.com/path/segment-2.ts',
    ]

    downloader._append_fragment.assert_has_calls([
        call(prepared_ctx, b'first fragment'),
        call(prepared_ctx, b'second fragment'),
    ])
    assert downloader._append_fragment.call_count == 2
    downloader._finish_frag_download.assert_called_once_with(prepared_ctx)

    # The advertisement must not be downloaded.
    assert 'https://example.com/path/advertisement.ts' not in downloaded_urls

# Generated at 2026-10-25 01:37:33.658208
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import MagicMock, call

    manifest = b"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10,
https://cdn.example.com/segment-2.ts
#EXT-X-ENDLIST
"""

    manifest_response = MagicMock()
    manifest_response.geturl.return_value = (
        'https://media.example.com/hls/playlist.m3u8')
    manifest_response.read.return_value = manifest

    ydl = MagicMock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd._prepare_url = MagicMock(side_effect=lambda info_dict, url: url)

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)

    downloaded_urls = []

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_urls.append(url)
        return True, {
            'https://media.example.com/hls/segment-1.ts': b'fragment-one',
            'https://cdn.example.com/segment-2.ts': b'fragment-two',
        }[url]

    fd._download_fragment = MagicMock(side_effect=download_fragment)

    appended_fragments = []
    fd._append_fragment = MagicMock(
        side_effect=lambda ctx, content: appended_fragments.append(content))
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'url': 'https://media.example.com/original.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True

    # Relative fragment URLs should be resolved against the final manifest URL.
    assert downloaded_urls == [
        'https://media.example.com/hls/segment-1.ts',
        'https://cdn.example.com/segment-2.ts',
    ]

    # The ad fragment must not be downloaded or appended.
    assert 'https://media.example.com/hls/advertisement.ts' not in downloaded_urls
    assert appended_fragments == [b'fragment-one', b'fragment-two']

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'fragment-one'),
        call(ctx, b'fragment-two'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:37:36.189484
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:37:38.712693
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:37:41.125763
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:37:43.541282
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:37:45.959746
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:37:48.376214
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:37:50.791159
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:37:52.166352
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:37:53.494914
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:38:22.480116
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

# Generated at 2026-10-25 01:38:33.440965
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    vod_manifest = '\n'.join((
        '#EXTM3U',
        '#EXT-X-TARGETDURATION:10',
        '#EXTINF:10.0,',
        'segment.ts',
        '#EXT-X-ENDLIST',
    ))

    # Ordinary VOD playlists are supported.
    assert HlsFD.can_download(vod_manifest, {})
    assert HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts',
        {'is_live': False})

    # Live streams and playlists with initialization segments are unsupported.
    assert not HlsFD.can_download(vod_manifest, {'is_live': True})
    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s',
        {'is_live': False})

    # Encryption methods other than NONE and AES-128 are unsupported.
    assert not HlsFD.can_download(
        '#EXTM3U\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\nsegment.ts',
        {'is_live': False})

    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        'segment.ts'
    )
    aes_byterange_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXT-X-BYTERANGE:1024@0\n'
        'segment.ts'
    )

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # AES-128 requires the optional crypto dependency.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {'is_live': False})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {'is_live': False})

        # AES-128 combined with byte ranges is always unsupported.
        assert not HlsFD.can_download(
            aes_byterange_manifest, {'is_live': False})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:39:19.041994
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():from urllib.parse import parse_qs, urlparse


# Generated at 2026-10-25 01:39:30.175575
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    vod_info = {'is_live': False}
    live_info = {'is_live': True}

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # Basic unencrypted VOD playlists are supported.
        assert HlsFD.can_download('#EXTM3U\n', vod_info)
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\n', vod_info)

        # Byte ranges are supported when encryption is not used.
        assert HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n',
            vod_info)

        # Unsupported encryption methods must be rejected.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n',
            vod_info)

        # Initialization segments are unsupported.
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-MAP:URI="init.mp4"\n',
            vod_info)

        # Live streams are unsupported.
        assert not HlsFD.can_download('#EXTM3U\n', live_info)

        # AES-128 requires an available crypto implementation.
        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            'segment.ts\n'
        )

        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, vod_info)

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, vod_info)

        # AES-128 combined with byte ranges is unsupported even when
        # decryption support is available.
        aes_byterange_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n'
        )
        assert not HlsFD.can_download(aes_byterange_manifest, vod_info)
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:39:41.432048
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

    map_manifest = plain_manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-TARGETDURATION:10\n#EXT-X-MAP:URI="init.mp4"')
    assert not HlsFD.can_download(map_manifest, {})

    unsupported_encryption_manifest = plain_manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-TARGETDURATION:10\n'
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"')
    assert not HlsFD.can_download(unsupported_encryption_manifest, {})

    unencrypted_key_manifest = plain_manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-TARGETDURATION:10\n#EXT-X-KEY:METHOD=NONE')
    assert HlsFD.can_download(unencrypted_key_manifest, {})

    aes_manifest = plain_manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-TARGETDURATION:10\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"')

    aes_byterange_manifest = aes_manifest.replace(
        '#EXTINF:10,',
        '#EXT-X-BYTERANGE:1024@0\n#EXTINF:10,')

    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})
        assert not HlsFD.can_download(aes_byterange_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:40:07.440170
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest_url = 'https://example.test/master.m3u8'

# Generated at 2026-10-25 01:40:31.096349
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    manifest = b'''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@10
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
'''

    class FakeResponse(object):
        def geturl(self):
            # Ensure relative fragment URLs are resolved against the final,
            # redirected manifest URL.
            return 'https://cdn.example.com/media/index.m3u8'

        def read(self):
            return manifest

    ydl = Mock()
    ydl.urlopen.return_value = FakeResponse()

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd.to_screen = Mock()
    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    prepared_contexts = []

    def prepare_download(ctx):
        prepared_contexts.append(dict(ctx))
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)

    downloaded_fragments = []

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_fragments.append((url, dict(headers)))
        contents = {
            'https://cdn.example.com/media/segment-1.ts?token=abc':
                b'fragment-one',
            'https://cdn.example.com/media/segment-2.ts?token=abc':
                b'fragment-two',
        }
        return True, contents[url]

    fd._download_fragment = Mock(side_effect=download_fragment)

    appended_fragments = []
    fd._append_fragment = Mock(
        side_effect=lambda ctx, content: appended_fragments.append(content))
    fd._finish_frag_download = Mock()


# Generated at 2026-10-25 01:40:49.731982
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    manifest_url = 'https://example.com/path/playlist.m3u8'
    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@10
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
'''

    response = MagicMock()
    response.geturl.return_value = manifest_url
    response.read.return_value = manifest.encode('utf-8')

    ydl = MagicMock()
    ydl.urlopen.return_value = response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd.to_screen = MagicMock()
    fd._prepare_url = MagicMock(
        side_effect=lambda info_dict, url: url)

    started_contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        started_contexts.append(ctx)

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)

    download_calls = []
    fragment_contents = iter((b'first fragment', b'second fragment'))

    def download_fragment(ctx, url, info_dict, headers):
        # Copy headers because real_download may mutate the original dictionary.
        download_calls.append((ctx, url, dict(headers)))
        return True, next(fragment_contents)

    fd._download_fragment = MagicMock(side_effect=download_fragment)

    appended_fragments = []

    def append_fragment(ctx, content):
        appended_fragments.append((ctx, content))

    fd._append_fragment = MagicMock(side_effect=append_fragment)
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'url': manifest_url,
        'http_headers': {},
        'is_live': False,
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True
    ydl.urlopen.assert_called_once_with(manifest_url)

    assert len(started_contexts) == 1
    ctx = started_contexts[0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    assert len(download_calls) == 2
    assert download_calls[0][1:] == (
        'https://example.com/path/segment-1.ts',
        {},
    )
    assert download_calls[1][1:] == (
        'https://example.com/path/segment-2.ts',
        {'Range': 'bytes=10-13'},
    )

    # The advertisement fragment must not be downloaded.
    assert all(
        'advertisement.ts' not in url
        for _, url, _ in download_calls
    )

    assert appended_fragments == [
        (ctx, b'first fragment'),
        (ctx, b'second fragment'),
    ]

    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:41:13.319379
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

    class FakeYDL(object):
        def __init__(self, response):
            self.response = response
            self.requests = []

        def urlopen(self, request):
            self.requests.append(request)
            return self.response

    manifest = b'''#EXTM3U
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
'''

    manifest_url = 'https://example.com/master.m3u8'
    redirected_url = 'https://cdn.example.com/media/index.m3u8'
    ydl = FakeYDL(FakeResponse(redirected_url, manifest))

    # Avoid depending on FragmentFD/FileDownloader initialization; all
    # collaborators used by real_download are replaced below.
    fd = object.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    messages = []
    downloaded = []
    appended = []
    state = {}

    fd.to_screen = lambda message: messages.append(message)
    fd._prepare_url = lambda info_dict, url: url

    def prepare(ctx):
        ctx['fragment_index'] = 0
        state['prepared_ctx'] = ctx

    def download_fragment(ctx, url, info_dict, headers):
        downloaded.append((url, dict(headers)))
        content = {
            'https://cdn.example.com/media/segment-1.ts?token=test':
                b'first-fragment',
            'https://cdn.example.com/media/segment-2.ts?token=test':
                b'seco',
        }[url]
        return True, content

    def append_fragment(ctx, content):
        appended.append(content)


# Generated at 2026-10-25 01:41:31.101752
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():from unittest import mock


# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download(tmp_path):
    manifest_url = 'https://example.com/path/playlist.m3u8'
    redirected_manifest_url = 'https://cdn.example.com/media/playlist.m3u8'

    manifest = b'''#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10.0,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5.0,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10.0,
segment-2.ts
#EXT-X-ENDLIST
'''

    manifest_response = mock.Mock()
    manifest_response.geturl.return_value = redirected_manifest_url
    manifest_response.read.return_value = manifest

    ydl = mock.Mock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fragment_contents = [
        (True, b'first fragment'),
        (True, b'second fragment'),
    ]

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    filename = str(tmp_path / 'output.ts')
    info_dict = {
        'url': manifest_url,
        'http_headers': {'User-Agent': 'test-agent'},
    }

    with mock.patch.object(
            fd, '_prepare_url', side_effect=lambda _, url: url
    ), mock.patch.object(
            fd, '_prepare_and_start_frag_download',
            side_effect=prepare_download
    ) as prepare_mock, mock.patch.object(
            fd, '_download_fragment',
            side_effect=fragment_contents
    ) as download_mock, mock.patch.object(
            fd, '_append_fragment'
    ) as append_mock, mock.patch.object(
            fd, '_finish_frag_download'
    ) as finish_mock:
        result = fd.real_download(filename, info_dict)

    assert result is True
    ydl.urlopen.assert_called_once_with(manifest_url)

    prepare_mock.assert_called_once()
    ctx = prepare_mock.call_args[0][0]
    assert ctx['filename'] == filename
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    assert download_mock.call_count == 2
    assert download_mock.call_args_list[0].args[1] == (
        'https://cdn.example.com/media/segment-1.ts'
    )
    assert download_mock.call_args_list[1].args[1] == (
        'https://cdn.example.com/media/segment-2.ts'
    )

    append_mock.assert_has_calls([
        mock.call(ctx, b'first fragment'),
        mock.call(ctx, b'second fragment'),
    ])
    finish_mock.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:41:50.659885
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
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

    class FakeResponse(object):
        def geturl(self):
            # Simulate a redirect so relative fragment URLs must use the final URL.
            return 'https://cdn.example.com/media/playlist.m3u8'

        def read(self):
            return manifest.encode('utf-8')

    class FakeYDL(object):
        def __init__(self):
            self.requested_urls = []

        def urlopen(self, request):
            self.requested_urls.append(request)
            return FakeResponse()

    ydl = FakeYDL()
    fd = HlsFD.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }
    fd._progress_hooks = []

    downloaded_urls = []
    appended_fragments = []
    prepared_contexts = []
    finished_contexts = []

    fd.to_screen = lambda message: None
    fd._prepare_url = lambda info_dict, url: url

    def prepare_and_start(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx)

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_urls.append((url, dict(headers)))
        return True, ('data:%s' % url).encode('utf-8')

    def append_fragment(ctx, content):
        appended_fragments.append(content)

    def finish_frag_download(ctx):
        finished_contexts.append(ctx)

    fd._prepare_and_start_frag_download = prepare_and_start
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish_frag_download

    result = fd.real_download(
        'output.ts',
        {
            'url': 'https://example.com/original/playlist.m3u8',
            'http_headers': {'User-Agent': 'test-agent'},
            'is_live': False,
        })

    assert result is True
    assert ydl.requested_urls == [
        'https://example.com/original/playlist.m3u8',
    ]

    # The advertisement must not be downloaded or counted as media.
    assert [url for url, _ in downloaded_urls] == [
        'https://cdn.example.com/media/segment-1.ts',
        'https://cdn.example.com/media/segment-2.ts',
    ]
    assert all(
        headers == {'User-Agent': 'test-agent'}
        for _, headers in downloaded_urls
    )

    assert appended_fragments == [
        b'data:https://cdn.example.com/media/segment-1.ts',
        b'data:https://cdn.example.com/media/segment-2.ts',
    ]

    assert len(prepared_contexts) == 1
    assert prepared_contexts[0]['filename'] == 'output.ts'
    assert prepared_contexts[0]['total_frags'] == 2
    assert prepared_contexts[0]['ad_frags'] == 1

    assert finished_contexts == prepared_contexts

# Generated at 2026-10-25 01:42:16.566293
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import Mock

    manifest = b"""\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO,type=ad
#EXTINF:5,
advertisement.ts
#ANVATO-SEGMENT-INFO,type=master
#EXT-X-BYTERANGE:4@2
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
"""


# Generated at 2026-10-25 01:43:04.915506
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():manifest = '\n'.join((
        '#EXTM3U',
        '#EXT-X-MEDIA-SEQUENCE:7',
        '#EXT-X-BYTERANGE:4@0',
        'media.bin',
        '#EXT-X-BYTERANGE:3',
        'media.bin',
        '#ANVATO-SEGMENT-INFO:type=ad',
        'ads/anvato.ts',
        '#ANVATO-SEGMENT-INFO:type=master',
        '#UPLYNK-SEGMENT,ad',
        'ads/uplynk.ts',
        '#UPLYNK-SEGMENT,segment',
        '#EXT-X-ENDLIST',
    ))


# Generated at 2026-10-25 01:43:26.803613
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest_url = 'https://origin.example.com/master.m3u8'
    redirected_manifest_url = 'https://cdn.example.com/video/index.m3u8'
    manifest = '''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10.0,
segment-10.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5.0,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10.0,
segment-11.ts
#EXT-X-ENDLIST
'''

    manifest_response = MagicMock()
    manifest_response.geturl.return_value = redirected_manifest_url
    manifest_response.read.return_value = manifest.encode('utf-8')

    ydl = MagicMock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd._prepare_url = MagicMock(
        side_effect=lambda info_dict, url: url)

    def prepare_download(ctx):
        # FragmentFD normally initializes this value when preparing the
        # fragment download.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)

    first_fragment_url = (
        'https://cdn.example.com/video/segment-10.ts')
    second_fragment_url = (
        'https://cdn.example.com/video/segment-11.ts')

    fragment_contents = {
        first_fragment_url: b'first-fragment',
        second_fragment_url: b'second-fragment',
    }

    downloaded_urls = []

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_urls.append(url)
        return True, fragment_contents[url]

    fd._download_fragment = MagicMock(side_effect=download_fragment)
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'url': manifest_url,
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }


# Generated at 2026-10-25 01:43:38.385375
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    plain_manifest = '''#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
segment-1.ts
#EXT-X-ENDLIST
'''

    assert HlsFD.can_download(plain_manifest, {})
    assert not HlsFD.can_download(plain_manifest, {'is_live': True})

    # Unencrypted byte ranges are supported.
    byte_range_manifest = '''#EXTM3U
#EXT-X-BYTERANGE:1000@0
segment.ts
#EXT-X-ENDLIST
'''
    assert HlsFD.can_download(byte_range_manifest, {})

    # Initialization sections and unsupported encryption methods require ffmpeg.
    assert not HlsFD.can_download(
        plain_manifest + '#EXT-X-MAP:URI="init.mp4"\n', {})
    assert not HlsFD.can_download(
        plain_manifest + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n', {})

    aes_manifest = '''#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXTINF:10,
segment-1.ts
#EXT-X-ENDLIST
'''

    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported even when AES
        # decryption is available.
        aes_byte_range_manifest = '''#EXTM3U
#EXT-X-KEY:METHOD=AES-128,URI="key.bin"
#EXT-X-BYTERANGE:1000@0
segment.ts
#EXT-X-ENDLIST
'''
        assert not HlsFD.can_download(aes_byte_range_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:44:07.151149
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:44:09.555185
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:44:11.970370
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:44:37.370173
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = (
        '#EXTM3U\n'
        '#EXT-X-MEDIA-SEQUENCE:7\n'
        '#EXTINF:10,\n'
        'segment-1.ts\n'
        '#ANVATO-SEGMENT-INFO:type=ad\n'
        '#EXTINF:5,\n'
        'advertisement.ts\n'
        '#ANVATO-SEGMENT-INFO:type=master\n'
        '#EXTINF:10,\n'
        'segment-2.ts\n'
        '#EXT-X-ENDLIST\n'
    )

    manifest_response = mock.Mock()
    manifest_response.geturl.return_value = (
        'https://cdn.example.test/video/master.m3u8'
    )
    manifest_response.read.return_value = manifest.encode('utf-8')

    ydl = mock.Mock()
    ydl.urlopen.return_value = manifest_response

    info_dict = {
        'url': 'https://example.test/master.m3u8',
        'is_live': False,
    }

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd._prepare_url = mock.Mock(
        side_effect=lambda unused_info_dict, url: url
    )

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = mock.Mock(
        side_effect=prepare_download
    )
    fd._download_fragment = mock.Mock(side_effect=[
        (True, b'first fragment'),
        (True, b'second fragment'),
    ])
    fd._append_fragment = mock.Mock()
    fd._finish_frag_download = mock.Mock()

    result = fd.real_download('output.ts', info_dict)

    assert result is True

    fd._prepare_url.assert_called_once_with(
        info_dict, 'https://example.test/master.m3u8'
    )
    ydl.urlopen.assert_called_once_with(
        'https://example.test/master.m3u8'
    )

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2

# Generated at 2026-10-25 01:44:53.259064
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    plain_manifest = (
        '#EXTM3U\n'
        '#EXTINF:10,\n'
        'segment.ts\n'
        '#EXT-X-ENDLIST\n'
    )

    # Ordinary VOD playlists are supported.
    assert HlsFD.can_download(plain_manifest, {})
    assert HlsFD.can_download(plain_manifest, {'is_live': False})

    # Live playlists are delegated to ffmpeg.
    assert not HlsFD.can_download(plain_manifest, {'is_live': True})

    # Explicitly unencrypted playlists are supported.
    assert HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=NONE\n'
        '#EXTINF:10,\n'
        'segment.ts\n',
        {})

    # Unsupported encryption methods are rejected.
    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
        '#EXTINF:10,\n'
        'segment.ts\n',
        {})

    # Initialization sections are unsupported.
    assert not HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-MAP:URI="init.mp4"\n'
        '#EXTINF:10,\n'
        'segment.m4s\n',
        {})

    # Byte ranges by themselves are supported.
    assert HlsFD.can_download(
        '#EXTM3U\n'
        '#EXT-X-BYTERANGE:1000@0\n'
        'segment.ts\n',
        {})

    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXTINF:10,\n'
        'segment.ts\n'
    )
    aes_byte_range_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXT-X-BYTERANGE:1000@0\n'
        'segment.ts\n'
    )

    original_can_decrypt_frag = can_decrypt_frag
    try:
        # AES-128 requires the Crypto dependency.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported even when the
        # decryption dependency is available.
        assert not HlsFD.can_download(aes_byte_range_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-25 01:44:55.684320
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:44:58.204345
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 01:45:00.622424
# Unit test for method real_download of class HlsFD