

# Generated at 2026-10-24 07:58:36.793784
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

    # Ordinary, non-live HLS playlists are supported.
    assert HlsFD.can_download(basic_manifest, {})
    assert HlsFD.can_download(
        '#EXT-X-KEY:METHOD=NONE\n' + basic_manifest, {})

    # Live streams and playlists requiring initialization segments are not
    # supported by the native downloader.
    assert not HlsFD.can_download(basic_manifest, {'is_live': True})
    assert not HlsFD.can_download(
        '#EXT-X-MAP:URI="init.mp4"\n' + basic_manifest, {})

    # Encryption methods other than NONE and AES-128 are unsupported.
    assert not HlsFD.can_download(
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n' + basic_manifest, {})

    original_can_decrypt_frag = can_decrypt_frag
    try:
        aes_manifest = (
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n' + basic_manifest)

        # AES-128 requires the optional crypto dependency.
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte-range fragments is unsupported even when
        # the crypto dependency is available.
        aes_byterange_manifest = (
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            + basic_manifest)
        assert not HlsFD.can_download(aes_byterange_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-24 07:58:46.611010
# Unit test for constructor of class HlsFD
def test_HlsFD():
    ydl = object()
    params = {'test': True}

    fd = HlsFD(ydl, params)

    assert fd.ydl is ydl
    assert fd.params is params
    assert fd._progress_hooks == []
    assert fd.FD_NAME == 'hlsnative'

# Generated at 2026-10-24 07:58:56.137384
# Unit test for constructor of class HlsFD
def test_HlsFD():
    class DummyYDL(object):
        pass

    ydl = DummyYDL()
    params = {'quiet': True}

    fd = HlsFD(ydl, params)

    assert isinstance(fd, HlsFD)
    assert isinstance(fd, FragmentFD)
    assert fd.ydl is ydl
    assert fd.params is params
    assert fd.FD_NAME == 'hlsnative'
    assert fd._progress_hooks == []

# Generated at 2026-10-24 07:59:07.957537
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    global can_decrypt_frag

    original_can_decrypt_frag = can_decrypt_frag
    basic_manifest = '#EXTM3U\n#EXTINF:10,\nsegment.ts\n'

    try:
        # Basic VOD playlists are supported.
        assert HlsFD.can_download(basic_manifest, {})
        assert not HlsFD.can_download(basic_manifest, {'is_live': True})

        # Initialization sections and unsupported encryption methods require ffmpeg.
        assert not HlsFD.can_download(
            '#EXTM3U\n#EXT-X-MAP:URI="init.mp4"\nsegment.m4s\n', {})
        assert not HlsFD.can_download(
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
            'segment.ts\n',
            {})

        # Unencrypted playlists remain supported without AES support.
        can_decrypt_frag = False
        assert HlsFD.can_download(
            '#EXTM3U\n#EXT-X-KEY:METHOD=NONE\nsegment.ts\n', {})

        # AES-128 requires the crypto implementation.
        aes_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXTINF:10,\n'
            'segment.ts\n'
        )
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 combined with byte ranges is unsupported.
        aes_byte_range_manifest = (
            '#EXTM3U\n'
            '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
            '#EXT-X-BYTERANGE:1000@0\n'
            'segment.ts\n'
        )
        assert not HlsFD.can_download(aes_byte_range_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-24 07:59:53.991229
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 08:00:09.661575
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():from unittest.mock import Mock


# Generated at 2026-10-24 08:00:29.724386
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

    assert HlsFD.can_download(basic_manifest, {})
    assert not HlsFD.can_download(basic_manifest, {'is_live': True})

    # Initialization segments are unsupported.
    map_manifest = basic_manifest + (
        '#EXT-X-MAP:URI="init.mp4"\n'
    )
    assert not HlsFD.can_download(map_manifest, {})

    # Unencrypted byte ranges are supported.
    byte_range_manifest = basic_manifest + '#EXT-X-BYTERANGE:1000@0\n'
    assert HlsFD.can_download(byte_range_manifest, {})

    # Unsupported encryption methods must be rejected.
    sample_aes_manifest = basic_manifest + (
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
    )
    assert not HlsFD.can_download(sample_aes_manifest, {})

    # METHOD=NONE is supported.
    no_encryption_manifest = basic_manifest + '#EXT-X-KEY:METHOD=NONE\n'
    assert HlsFD.can_download(no_encryption_manifest, {})

    aes128_manifest = basic_manifest + (
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
    )

    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes128_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes128_manifest, {})

        # AES-128 combined with byte ranges is unsupported even when AES
        # decryption is available.
        aes128_byte_range_manifest = (
            aes128_manifest + '#EXT-X-BYTERANGE:1000@0\n'
        )
        assert not HlsFD.can_download(aes128_byte_range_manifest, {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

# Generated at 2026-10-24 08:00:47.545271
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 08:01:05.629663
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-24 08:01:17.454170
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():from types import SimpleNamespace
