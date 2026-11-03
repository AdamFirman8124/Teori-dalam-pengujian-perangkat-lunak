

# Generated at 2026-11-02 18:23:50.763378
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    # Plain manifest without unsupported features should be downloadable
    plain_manifest = (
        '#EXTM3U\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXTINF:10,\n'
        'seg1.ts\n'
    )
    assert HlsFD.can_download(plain_manifest, {'is_live': False}) is True

    # Unsupported encryption method (SAMPLE-AES) must be rejected

# Generated at 2026-11-02 18:25:14.468329
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # Construct with a minimal params dict and no ydl
    fd = HlsFD(None, {})
    assert fd is not None
    assert fd.FD_NAME == 'hlsnative'
    assert fd.params == {}
    assert fd._progress_hooks == []

    # Construct with typical params
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': False,
        'test': True,
    }
    fd2 = HlsFD(None, params)
    assert fd2 is not None
    assert fd2.params.get('fragment_retries') == 3
    assert fd2.params.get('skip_unavailable_fragments') is False
    assert fd2.params.get('test') is True
    assert isinstance(fd2, FragmentFD)

# Generated at 2026-11-02 18:29:52.216049
# Unit test for method real_download of class HlsFD