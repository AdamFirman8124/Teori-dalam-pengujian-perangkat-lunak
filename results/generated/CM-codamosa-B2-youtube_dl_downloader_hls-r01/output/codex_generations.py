

# Generated at 2026-11-02 19:28:33.290913
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    manifest = (
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
    )

    # Plain VOD playlist without unsupported features is downloadable
    assert HlsFD.can_download(manifest, {'is_live': False}) is True
    assert HlsFD.can_download(manifest, {}) is True

    # Live streams are not supported by hlsnative
    assert HlsFD.can_download(manifest, {'is_live': True}) is False

    # METHOD=NONE keys are supported
    none_key_manifest = manifest + '#EXT-X-KEY:METHOD=NONE\n'
    assert HlsFD.can_download(none_key_manifest, {'is_live': False}) is True

    # Unsupported encryption methods (e.g. SAMPLE-AES) are not supported
    sample_aes_manifest = manifest + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="https://example.com/key"\n'
    assert HlsFD.can_download(sample_aes_manifest, {'is_live': False}) is False

    # AES-128 is supported only when a decryption backend is available
    aes128_manifest = manifest + '#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/key",IV=0x1234\n'
    assert HlsFD.can_download(aes128_manifest, {'is_live': False}) == can_decrypt_frag

    # AES-128 combined with byte ranges is not supported
    aes128_byterange_manifest = aes128_manifest + '#EXT-X-BYTERANGE:1000@0\n'
    assert HlsFD.can_download(aes128_byterange_manifest, {'is_live': False}) is False

    # Media initialization (EXT-X-MAP) is not supported
    map_manifest = manifest + '#EXT-X-MAP:URI="init.mp4"\n'
    assert HlsFD.can_download(map_manifest, {'is_live': False}) is False

# Generated at 2026-11-02 19:32:21.647377
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import MagicMock, patch

    man_url = 'http://example.com/manifest.m3u8'
    manifest = '\n'.join([
        '#EXTM3U',
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-MEDIA-SEQUENCE:0',
        '#EXTINF:10,',
        'frag0.ts',
        '#EXTINF:10,',
        'frag1.ts',
        '#EXT-X-ENDLIST',
    ])

    params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
        'test': False,
    }
    hls_fd = HlsFD(MagicMock(), params)

    urlh = MagicMock()
    urlh.geturl.return_value = man_url
    urlh.read.return_value = manifest.encode('utf-8')
    hls_fd.ydl.urlopen.return_value = urlh

    ctx_holder = {}

    def fake_prepare_and_start(ctx):
        ctx['fragment_index'] = 0
        ctx_holder.update(ctx)

    downloaded_urls = []
    appended_contents = []

    def fake_download_fragment(ctx, url, info_dict, headers=None):
        downloaded_urls.append(url)
        return True, b'fragment-data'

    def fake_append_fragment(ctx, content):
        appended_contents.append(content)

    with patch.object(HlsFD, '_prepare_url', return_value=man_url), \
         patch.object(HlsFD, '_prepare_and_start_frag_download',
                      side_effect=fake_prepare_and_start), \
         patch.object(HlsFD, '_download_fragment',
                      side_effect=fake_download_fragment), \
         patch.object(HlsFD, '_append_fragment',
                      side_effect=fake_append_fragment), \
         patch.object(HlsFD, '_finish_frag_download') as mock_finish, \
         patch.object(HlsFD, 'to_screen') as mock_to_screen, \
         patch.object(HlsFD, 'report_warning') as mock_report_warning, \
         patch.object(HlsFD, 'report_error') as mock_report_error, \
         patch.object(HlsFD, 'report_retry_fragment'), \
         patch.object(HlsFD, 'report_skip_fragment'):

        info_dict = {'url': man_url}
        result = hls_fd.real_download('output.ts', info_dict)

    assert result is True
    # Manifest download requested via ydl.urlopen
    hls_fd.ydl.urlopen.assert_called_once_with(man_url)
    # Both relative fragment URLs resolved against the manifest URL
    assert downloaded_urls == [
        'http://example.com/frag0.ts',
        'http://example.com/frag1.ts',
    ]
    # Both fragment contents appended in order
    assert appended_contents == [b'fragment-data', b'fragment-data']
    # Context bookkeeping: 2 media fragments, no ad fragments
    assert ctx_holder['filename'] == 'output.ts'
    assert ctx_holder['total_frags'] == 2
    assert ctx_holder['ad_frags'] == 0
    # Finish called exactly once, no errors/warnings/fallback to ffmpeg
    mock_finish.assert_called_once()
    mock_to_screen.assert_called_once()
    mock_report_warning.assert_not_called()
    mock_report_error.assert_not_called()

# Generated at 2026-11-02 19:36:04.099725
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    import sys
    from unittest import mock

    base_url = 'http://example.com/video/playlist.m3u8'
    manifest = '\n'.join([
        '#EXTM3U',
        '#EXT-X-TARGETDURATION:10',
        '#EXT-X-MEDIA-SEQUENCE:0',
        '#EXTINF:10.0,',
        'seg0.ts',
        '#EXTINF:10.0,',
        'seg1.ts',
        '#EXT-X-ENDLIST',
        '',
    ])

    ydl = mock.MagicMock()
    urlh = mock.MagicMock()
    urlh.geturl.return_value = base_url
    urlh.read.return_value = manifest.encode('utf-8')
    ydl.urlopen.return_value = urlh

    params = {'fragment_retries': 0, 'skip_unavailable_fragments': True, 'test': False}
    fd = HlsFD(ydl, params)

    downloaded_urls = []
    appended = []

    def fake_download_fragment(ctx, frag_url, info_dict, headers):
        downloaded_urls.append(frag_url)
        return True, b'fragment-data'

    with mock.patch.object(fd, 'to_screen'), \
            mock.patch.object(fd, '_prepare_url', side_effect=lambda info, url: url), \
            mock.patch.object(fd, '_prepare_and_start_frag_download',
                              side_effect=lambda ctx: ctx.update(fragment_index=0)), \
            mock.patch.object(fd, '_download_fragment', side_effect=fake_download_fragment), \
            mock.patch.object(fd, '_append_fragment',
                              side_effect=lambda ctx, data: appended.append(data)), \
            mock.patch.object(fd, '_finish_frag_download') as finish_mock:
        info_dict = {'url': base_url}
        result = fd.real_download('video.ts', info_dict)

    assert result is True
    ydl.urlopen.assert_called_once()
    assert downloaded_urls == [
        'http://example.com/video/seg0.ts',
        'http://example.com/video/seg1.ts',
    ]
    assert appended == [b'fragment-data', b'fragment-data']
    finish_mock.assert_called_once()

    # In test mode only the first fragment is downloaded
    fd_test = HlsFD(ydl, dict(params, test=True))
    test_urls = []

    def fake_download_fragment_test(ctx, frag_url, info_dict, headers):
        test_urls.append(frag_url)
        return True, b'fragment-data'
