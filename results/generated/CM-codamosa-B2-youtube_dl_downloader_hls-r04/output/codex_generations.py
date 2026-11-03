

# Generated at 2026-11-02 19:56:35.676523
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    # Plain, unencrypted, non-live VOD playlist should be downloadable
    plain_manifest = (
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
        '#EXTINF:10,\n'
        'segment1.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    assert HlsFD.can_download(plain_manifest, {'is_live': False})
    # Missing 'is_live' key is treated as not live
    assert HlsFD.can_download(plain_manifest, {})

    # METHOD=NONE keys are acceptable
    none_key_manifest = (
        '#EXT-X-KEY:METHOD=NONE\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
 '#EXT-X-ENDLIST\n'
    )
    assert HlsFD.can_download(none_key_manifest, {})

    # SAMPLE-AES encryption is unsupported
    sample_aes_manifest = (
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="https://example.com/key"\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
    )
    assert not HlsFD.can_download(sample_aes_manifest, {})

    # Any other encryption method (e.g. IDENTITY) is unsupported
    identity_manifest = (
        '#EXT-X-KEY:METHOD=IDENTITY,URI="https://example.com/key"\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
    )
    assert not HlsFD.can_download(identity_manifest, {})

    # #EXT-X-MAP (media initialization) is unsupported
    map_manifest = (
        '#EXT-X-MAP:URI="init.mp4"\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
    )
    assert not HlsFD.can_download(map_manifest, {})

    # Live streams are unsupported
    assert not HlsFD.can_download(plain_manifest, {'is_live': True})

    # AES-128 is supported only if pycrypto is available
    aes128_manifest = (
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key"\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
    )
    assert HlsFD.can_download(aes128_manifest, {}) == can_decrypt_frag

    # AES-128 combined with #EXT-X-BYTERANGE is unsupported
    aes128_byterange_manifest = (
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key"\n'
        '#EXT-X-BYTERANGE:1024@0\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
    )
    assert not HlsFD.can_download(aes128_byterange_manifest, {})

    # #EXT-X-BYTERANGE alone is (currently) acceptable
    byterange_manifest = (
        '#EXT-X-BYTERANGE:1024@0\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
    )
    assert HlsFD.can_download(byterange_manifest, {})

# Generated at 2026-11-02 19:57:53.315164
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from youtube_dl.downloader.hls import HlsFD
    from youtube_dl import YoutubeDL

    ydl = YoutubeDL()
    fd = HlsFD(ydl, {})
    assert isinstance(fd, HlsFD)
    assert fd.FD_NAME == 'hlsnative'
    assert fd.ydl is ydl
    assert fd.params == {}

# Generated at 2026-11-02 20:01:39.554059
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    try:
        from youtube_dl.downloader.hls import HlsFD
    except ImportError:
        from youtube_dlc.downloader.hls import HlsFD

    try:
        from youtube_dl.downloader.hls import can_decrypt_frag
    except ImportError:
        try:
            from youtube_dlc.downloader.hls import can_decrypt_frag
        except ImportError:
            can_decrypt_frag = False

    plain_manifest = (
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXTINF:10,\n'
        'seg1.ts\n'
    )

    # Plain, unencrypted manifest should be downloadable
    assert HlsFD.can_download(plain_manifest, {'is_live': False}) is True

    # Missing is_live key should also be fine
    assert HlsFD.can_download(plain_manifest, {}) is True

    # Unsupported encryption method (SAMPLE-AES) must be rejected
    sample_aes_manifest = plain_manifest + \
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n'
    assert HlsFD.can_download(sample_aes_manifest, {}) is False

    # AES-128 is only supported when a decryption backend is available
    aes128_manifest = plain_manifest + \
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
    assert HlsFD.can_download(aes128_manifest, {}) == bool(can_decrypt_frag)

    # AES-128 combined with byte ranges is never supported
    aes128_byterange_manifest = plain_manifest + \
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n' \
        '#EXT-X-BYTERANGE:1000@0\n'
    assert HlsFD.can_download(aes128_byterange_manifest, {}) is False

    # Media initialization sections (EXT-X-MAP) are unsupported
    map_manifest = plain_manifest + '#EXT-X-MAP:URI="init.mp4"\n'
    assert HlsFD.can_download(map_manifest, {}) is False

    # Live streams must be rejected
    assert HlsFD.can_download(plain_manifest, {'is_live': True}) is False

    # METHOD=NONE key lines are acceptable
    none_key_manifest = plain_manifest + '#EXT-X-KEY:METHOD=NONE\n'
    assert HlsFD.can_download(none_key_manifest, {}) is True