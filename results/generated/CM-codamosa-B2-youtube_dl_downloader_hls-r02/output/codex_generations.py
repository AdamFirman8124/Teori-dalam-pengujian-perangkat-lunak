

# Generated at 2026-11-02 18:56:39.980127
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    info_dict = {'is_live': False}

    # Plain, unencrypted manifest should be downloadable
    manifest = '''#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10,
segment_0.ts
#EXTINF:10,
segment_1.ts
#EXT-X-ENDLIST
'''
    assert HlsFD.can_download(manifest, info_dict)

    # METHOD=NONE keys are fine
    manifest_with_none_key = manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-TARGETDURATION:10\n#EXT-X-KEY:METHOD=NONE')
    assert HlsFD.can_download(manifest_with_none_key, info_dict)

    # Unsupported encryption methods cannot be downloaded
    manifest_sample_aes = manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-TARGETDURATION:10\n#EXT-X-KEY:METHOD=SAMPLE-AES,URI="https://example.com/key"')
    assert not HlsFD.can_download(manifest_sample_aes, info_dict)

    # EXT-X-MAP is unsupported
    manifest_with_map = manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-TARGETDURATION:10\n#EXT-X-MAP:URI="init.mp4"')
    assert not HlsFD.can_download(manifest_with_map, info_dict)

    # Live streams cannot be downloaded
    assert not HlsFD.can_download(manifest, {'is_live': True})

    # AES-128 without BYTERANGE is downloadable iff pycrypto is available
    manifest_aes128 = manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-TARGETDURATION:10\n#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key"')
    if can_decrypt_frag:
        assert HlsFD.can_download(manifest_aes128, info_dict)
    else:
        assert not HlsFD.can_download(manifest_aes128, info_dict)

    # AES-128 combined with BYTERANGE is never downloadable
    manifest_aes128_byterange = manifest_aes128.replace(
        '#EXTINF:10,',
        '#EXT-X-BYTERANGE:1000@0\n#EXTINF:10,')
    assert not HlsFD.can_download(manifest_aes128_byterange, info_dict)

# Generated at 2026-11-02 18:57:20.157624
# Unit test for constructor of class HlsFD
def test_HlsFD():
    from unittest.mock import MagicMock
    ydl = MagicMock()
    params = {'test': False}
    downloader = HlsFD(ydl, params)
    assert downloader.FD_NAME == 'hlsnative'
    assert downloader.ydl is ydl
    assert downloader.params == params
    assert downloader._progress_hooks == []

# Generated at 2026-11-02 18:58:10.234868
# Unit test for constructor of class HlsFD
def test_HlsFD():
    """
    Test that the HlsFD constructor correctly initializes the downloader
    with the given ydl and params, and exposes the expected FD_NAME.
    """
    fd = HlsFD(None, {})

    # The downloader object should be created successfully
    assert fd is not None

    # It should be an instance of HlsFD (and by inheritance FragmentFD)
    assert isinstance(fd, HlsFD)
    assert isinstance(fd, FragmentFD)

    # Constructor arguments should be stored on the instance
    assert fd.ydl is None
    assert fd.params == {}

    # The downloader should expose its file descriptor name
    assert fd.FD_NAME == 'hlsnative'

    # The static can_download helper should be available on the class
    assert callable(HlsFD.can_download)

    # can_download should accept a simple, unencrypted, non-live manifest
    simple_manifest = '#EXTM3U\n#EXT-X-TARGETDURATION:10\nsegment_0.ts\n'
    assert HlsFD.can_download(simple_manifest, {'is_live': False}) is True

    # can_download should reject a live stream
    assert HlsFD.can_download(simple_manifest, {'is_live': True}) is False

    # can_download should reject unsupported encryption methods
    encrypted_manifest = simple_manifest + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key"\n'
    assert HlsFD.can_download(encrypted_manifest, {'is_live': False}) is False

# Generated at 2026-11-02 19:01:18.792660
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    try:
        from youtube_dl.downloader.hls import HlsFD
    except ImportError:
        from yt_dlp.downloader.hls import HlsFD

    try:
        from Crypto.Cipher import AES  # noqa: F401
        can_decrypt_frag = True
    except ImportError:
        can_decrypt_frag = False

    info_dict = {'url': 'http://example.com/video.m3u8', 'is_live': False}

    plain_manifest = '''#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10,
segment0.ts
#EXTINF:10,
segment1.ts
#EXT-X-ENDLIST
'''

    # A plain, unencrypted VOD manifest should be downloadable
    assert HlsFD.can_download(plain_manifest, info_dict)

    # Unsupported encryption methods (e.g. SAMPLE-AES) should not be downloadable
    encrypted_manifest = plain_manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="https://example.com/key"\n'
        '#EXT-X-TARGETDURATION:10')
    assert not HlsFD.can_download(encrypted_manifest, info_dict)

    # #EXT-X-MAP (media initialization) is not supported
    map_manifest = plain_manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-MAP:URI="init.mp4"\n#EXT-X-TARGETDURATION:10')
    assert not HlsFD.can_download(map_manifest, info_dict)

    # Live streams should be delegated to ffmpeg
    assert not HlsFD.can_download(plain_manifest, dict(info_dict, is_live=True))

    # AES-128 is supported only if a decrypting backend is available
    aes128_manifest = plain_manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key",'
        'IV=0x00000000000000000000000000000000\n'
        '#EXT-X-TARGETDURATION:10')
    assert HlsFD.can_download(aes128_manifest, info_dict) == can_decrypt_frag

    # AES-128 combined with byte ranges is never supported
    byterange_manifest = aes128_manifest.replace(
        'segment0.ts', '#EXT-X-BYTERANGE:1000@0\nsegment0.ts')
    assert not HlsFD.can_download(byterange_manifest, info_dict)

    # METHOD=NONE keys are fine
    none_key_manifest = plain_manifest.replace(
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-KEY:METHOD=NONE\n#EXT-X-TARGETDURATION:10')
    assert HlsFD.can_download(none_key_manifest, info_dict)

# Generated at 2026-11-02 19:04:39.017705
# Unit test for method real_download of class HlsFD