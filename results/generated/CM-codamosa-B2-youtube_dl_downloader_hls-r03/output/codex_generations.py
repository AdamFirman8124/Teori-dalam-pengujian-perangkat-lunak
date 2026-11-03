

# Generated at 2026-11-03 03:04:24.855846
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    plain_manifest = (
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
        '#EXTINF:10,\n'
        'segment1.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    info_dict = {'is_live': False}

    # A plain, unencrypted VOD manifest should be downloadable
    assert HlsFD.can_download(plain_manifest, info_dict)

    # KEY with METHOD=NONE is supported
    none_encrypted = plain_manifest.replace(
        '#EXTM3U',
        '#EXT-X-KEY:METHOD=NONE')
    assert HlsFD.can_download(none_encrypted, info_dict)

    # Unknown encryption methods (e.g. SAMPLE-AES) are not supported
    sample_aes = plain_manifest.replace(
        '#EXTM3U',
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="https://example.com/key"')
    assert not HlsFD.can_download(sample_aes, info_dict)

    # AES-128 is supported only when pycrypto is available
    aes128 = plain_manifest.replace(
        '#EXTM3U',
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key"')
    if can_decrypt_frag:
        assert HlsFD.can_download(aes128, info_dict)
    else:
        assert not HlsFD.can_download(aes128, info_dict)

    # AES-128 combined with EXT-X-BYTERANGE is never supported
    aes128_byterange = plain_manifest.replace(
        '#EXTM3U',
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key"\n'
        '#EXT-X-BYTERANGE:1024@0')
    assert not HlsFD.can_download(aes128_byterange, {'is_live': False})

    # Media initialization segments (EXT-X-MAP) are not supported
    with_map = plain_manifest.replace(
        '#EXTM3U',
        '#EXT-X-MAP:URI="init.mp4"')
    assert not HlsFD.can_download(with_map, info_dict)

    # Live streams are not supported
    assert not HlsFD.can_download(plain_manifest, {'is_live': True})

    # Missing 'is_live' key is treated as not live
    assert HlsFD.can_download(plain_manifest, {})

# Generated at 2026-11-03 03:09:53.874634
# Unit test for method real_download of class HlsFD