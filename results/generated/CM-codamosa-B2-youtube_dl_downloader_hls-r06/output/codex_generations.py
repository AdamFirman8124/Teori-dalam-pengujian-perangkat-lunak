

# Generated at 2026-11-02 13:47:18.250669
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    info_dict = {'url': 'http://example.com/840345fe/playlist.m3u8'}

    # Plain, unencrypted VOD playlist -> downloadable
    plain_manifest = (
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXTINF:10,\n'
        '840345fe_seg0.ts\n'
        '#EXTINF:10,\n'
        '840345fe_seg1.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    assert HlsFD.can_download(plain_manifest, info_dict) is True

    # Unsupported encryption method (SAMPLE-AES) -> not downloadable
    sample_aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="https://example.com/840345fe/key"\n'
        '#EXTINF:10,\n'
        '840345fe_seg0.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    assert HlsFD.can_download(sample_aes_manifest, info_dict) is False

    # EXT-X-MAP (media initialization) -> not downloadable
    map_manifest = (
        '#EXTM3U\n'
        '#EXT-X-MAP:URI="840345fe_init.mp4"\n'
        '#EXTINF:10,\n'
        '840345fe_seg0.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    assert HlsFD.can_download(map_manifest, info_dict) is False

    # Live stream -> not downloadable
    live_info = dict(info_dict, is_live=True)
    assert HlsFD.can_download(plain_manifest, live_info) is False

    # AES-128 combined with EXT-X-BYTERANGE -> never downloadable
    aes_byterange_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/840345fe/key"\n'
        '#EXT-X-BYTERANGE:1000@0\n'
        '#EXTINF:10,\n'
        '840345fe_seg0.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    assert HlsFD.can_download(aes_byterange_manifest, info_dict) is False

    # AES-128 without BYTERANGE -> downloadable only if a fragment decryptor is available
    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/840345fe/key"\n'
        '#EXTINF:10,\n'
        '840345fe_seg0.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    if can_decrypt_frag:
        assert HlsFD.can_download(aes_manifest, info_dict) is True
    else:
        assert HlsFD.can_download(aes_manifest, info_dict) is False

# Generated at 2026-11-02 13:48:18.126939
# Unit test for constructor of class HlsFD
def test_HlsFD():
    ydl = None
    params = {}
    fd = HlsFD(ydl, params)
    assert fd.FD_NAME == 'hlsnative'

# Generated at 2026-11-02 13:49:42.374107
# Unit test for constructor of class HlsFD
def test_HlsFD():
    class FakeYDL(object):
        def __init__(self):
            self.params = {}

    ydl = FakeYDL()
    params = {'fragment_retries': 3, 'test': False}
    fd = HlsFD(ydl, params)

    assert fd.FD_NAME == 'hlsnative'
    assert fd.ydl is ydl
    assert fd.params is params

# Generated at 2026-11-02 13:52:32.244201
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest import mock

    manifest = (
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXTINF:10,\n'
        'http://example.com/segment0.ts\n'
        '#EXTINF:10,\n'
        'http://example.com/segment1.ts\n'
    )

    urlh = mock.Mock()
    urlh.geturl.return_value = 'http://example.com/index.m3u8'
    urlh.read.return_value = manifest.encode('utf-8')

    ydl = mock.Mock()
    ydl.urlopen.return_value = urlh

    params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    }
    fd = HlsFD(ydl, params)

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    info_dict = {'url': 'http://example.com/index.m3u8'}

    with mock.patch.object(fd, '_prepare_and_start_frag_download',
                           side_effect=fake_prepare) as prepare, \
         mock.patch.object(fd, '_finish_frag_download') as finish, \
         mock.patch.object(fd, '_download_fragment',
                           return_value=(True, b'frag-data')) as dl_frag, \
         mock.patch.object(fd, '_append_fragment') as append_frag:

        result = fd.real_download('output.ts', info_dict)

    # Download should succeed
    assert result is True

    # Manifest was fetched once
    ydl.urlopen.assert_called_once()

    # Both fragments were downloaded and appended
    assert dl_frag.call_count == 2
    assert append_frag.call_count == 2
    dl_frag.assert_any_call(mock.ANY, 'http://example.com/segment0.ts', info_dict, mock.ANY)
    dl_frag.assert_any_call(mock.ANY, 'http://example.com/segment1.ts', info_dict, mock.ANY)
    append_frag.assert_any_call(mock.ANY, b'frag-data')

    # Lifecycle methods were invoked
    prepare.assert_called_once()
    finish.assert_called_once()

# Generated at 2026-11-02 13:54:20.620700
# Unit test for constructor of class HlsFD
def test_HlsFD():
    class FakeYDL(object):
        def __init__(self):
            self.params = {}

    ydl = FakeYDL()
    fd = HlsFD(ydl, ydl.params)

    assert isinstance(fd, HlsFD)
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'hlsnative'
    assert fd.ydl is ydl
    assert fd.params == {}