

# Generated at 2026-10-25 12:18:10.838236
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 12:18:13.251155
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 12:18:36.971308
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():assert HlsFD.can_download(
        '#EXTM3U\n#EXTINF:10,\nsegment1.ts\n',
        {},
    ) is True


# Generated at 2026-10-25 12:19:11.013440
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:19:46.033999
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:19:53.147420
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:20:08.460935
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # HlsFD defines no __init__, so this tests the inherited
    # FragmentFD/FileDownloader constructor.
    class FakeYDL(object):
        params = {}

    ydl = FakeYDL()
    params = {'test': True}

    fd = HlsFD(ydl, params)

    assert isinstance(fd, FragmentFD)
    assert isinstance(fd, HlsFD)
    assert fd.FD_NAME == 'hlsnative'
    assert fd.ydl is ydl
    assert fd.params is params

# Generated at 2026-10-25 12:20:09.907515
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # HlsFD defines no __init__, so this tests the inherited
    # FragmentFD/FileDownloader constructor.
    class FakeYDL(object):
        params = {}

    ydl = FakeYDL()
    params = {'test': True}

    fd = HlsFD(ydl, params)

    assert isinstance(fd, FragmentFD)
    assert isinstance(fd, HlsFD)
    assert fd.FD_NAME == 'hlsnative'
    assert fd.ydl is ydl
    assert fd.params is params

# Generated at 2026-10-25 12:20:11.640070
# Unit test for constructor of class HlsFD
def test_HlsFD():
    # HlsFD defines no __init__, so this tests the inherited
    # FragmentFD/FileDownloader constructor.
    class FakeYDL(object):
        params = {}

    ydl = FakeYDL()
    params = {'test': True}

    fd = HlsFD(ydl, params)

    assert isinstance(fd, FragmentFD)
    assert isinstance(fd, HlsFD)
    assert fd.FD_NAME == 'hlsnative'
    assert fd.ydl is ydl
    assert fd.params is params

# Generated at 2026-10-25 12:20:14.706188
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:20:17.653047
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:20:20.730773
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:20:52.450160
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:21:22.507085
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:21:57.691606
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:22:18.818875
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:22:32.229993
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:22:36.327495
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:23:47.597387
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    base_manifest = (
        '#EXTM3U\n'
        '#EXT-X-VERSION:3\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXTINF:10.0,\n'
        'segment0.ts\n'
        '#EXTINF:10.0,\n'
        'segment1.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    assert HlsFD.can_download(base_manifest, {}) is True
    assert HlsFD.can_download(base_manifest, {'is_live': False}) is True
    assert HlsFD.can_download(base_manifest, {'is_live': True}) is False
    assert HlsFD.can_download('', {}) is True
    none_manifest = base_manifest + '#EXT-X-KEY:METHOD=NONE\n'
    assert Hls

# Generated at 2026-10-25 12:24:07.641918
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    base_manifest = (
        '#EXTM3U\n'
        '#EXT-X-VERSION:3\n'
        '#EXT-X-TARGETDURATION:10\n'
        '#EXT-X-MEDIA-SEQUENCE:0\n'
        '#EXTINF:10.0,\n'
        'segment0.ts\n'
        '#EXTINF:10.0,\n'
        'segment1.ts\n'
        '#EXT-X-ENDLIST\n'
    )
    assert HlsFD.can_download(base_manifest, {}) is True
    assert HlsFD.can_download(base_manifest, {'is_live': False}) is True
    assert HlsFD.can_download(base_manifest, {'is_live': True}) is False
    assert HlsFD.can_download('', {}) is True
    none_manifest = base_manifest + '#EXT-X-KEY:METHOD=NONE\n'
    assert Hls

# Generated at 2026-10-25 12:24:59.891264
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:25:04.195308
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:25:11.242730
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:25:59.187564
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:26:01.608104
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:26:04.408375
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:26:54.649369
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:27:03.899096
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:27:09.331076
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:27:30.728313
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:27:42.509108
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 12:27:56.022326
# Unit test for method real_download of class HlsFD