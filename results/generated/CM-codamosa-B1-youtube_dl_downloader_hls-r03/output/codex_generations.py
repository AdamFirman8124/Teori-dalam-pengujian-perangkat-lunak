

# Generated at 2026-10-25 03:17:15.203168
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:17:17.620006
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:17:20.145171
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:17:22.560417
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:17:24.977391
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:17:27.393593
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:17:29.808284
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:17:32.222761
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:17:34.637408
# Unit test for constructor of class HlsFD

# Generated at 2026-10-25 03:17:37.052866
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:17:39.643266
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:17:42.060059
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:17:44.479371
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:17:46.898652
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:17:49.313882
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:17:51.727473
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:17:54.153855
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:17:56.569477
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:17:58.983881
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:01.398875
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:03.813417
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:06.229223
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:08.645192
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:11.061284
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:13.473060
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:15.887394
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:18.302791
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:20.717169
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:23.133334
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:25.552222
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:27.967597
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:18:30.384310
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:18:32.799062
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:18:35.213853
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:37.629502
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:40.046858
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:42.460520
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:44.242741
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:45.645980
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:18:57.402390
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():
    basic_manifest = '''\
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:10,
segment0.ts
#EXT-X-ENDLIST
'''

    assert HlsFD.can_download(basic_manifest, {})
    assert not HlsFD.can_download(basic_manifest, {'is_live': True})

    # Initialization segments are unsupported.
    assert not HlsFD.can_download(
        basic_manifest + '#EXT-X-MAP:URI="init.mp4"\n', {})

    # Encryption methods other than NONE and AES-128 are unsupported.
    assert not HlsFD.can_download(
        basic_manifest
        + '#EXT-X-KEY:METHOD=SAMPLE-AES,URI="key.bin"\n',
        {})

    # Unencrypted byte ranges are supported.
    assert HlsFD.can_download(
        basic_manifest + '#EXT-X-BYTERANGE:1000@0\n', {})

    aes_manifest = (
        '#EXTM3U\n'
        '#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n'
        '#EXTINF:10,\n'
        'segment0.ts\n'
        '#EXT-X-ENDLIST\n'
    )

    global can_decrypt_frag
    original_can_decrypt_frag = can_decrypt_frag
    try:
        can_decrypt_frag = False
        assert not HlsFD.can_download(aes_manifest, {})

        can_decrypt_frag = True
        assert HlsFD.can_download(aes_manifest, {})

        # AES-128 encrypted byte-range playlists are unsupported.
        assert not HlsFD.can_download(
            aes_manifest + '#EXT-X-BYTERANGE:1000@0\n', {})
    finally:
        can_decrypt_frag = original_can_decrypt_frag

    # METHOD=NONE does not require cryptographic support.
    assert HlsFD.can_download(
        basic_manifest + '#EXT-X-KEY:METHOD=NONE\n', {})

# Generated at 2026-10-25 03:19:21.312859
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b"""\
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
seg-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5,
ad.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@10
#EXTINF:10,
https://media.example.com/seg-2.ts?existing=value
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def geturl(self):
            # Simulate a redirect of the manifest URL.
            return 'https://cdn.example.com/live/index.m3u8'

        def read(self):
            return manifest

    class FakeYDL(object):
        params = {}

        def urlopen(self, request):
            return FakeResponse()

    fd = HlsFD(FakeYDL(), {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    requested_fragments = []
    appended_fragments = []
    captured_ctx = {}
    finished = []

    fd.to_screen = lambda message: None
    fd._prepare_url = lambda info_dict, url: url

    def prepare_download(ctx):
        captured_ctx.update(ctx)
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    def download_fragment(ctx, url, info_dict, headers):
        requested_fragments.append((url, dict(headers)))
        return True, ('content:%s' % url).encode('utf-8')

    def append_fragment(ctx, content):
        appended_fragments.append(content)

    def finish_download(ctx):
        finished.append(True)

    fd._prepare_and_start_frag_download = prepare_download
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish_download

    result = fd.real_download('output.ts', {
        'url': 'https://example.com/original.m3u8',
        'extra_param_to_segment_url': 'token=secret',
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    })

    assert result

# Generated at 2026-10-25 03:19:23.838968
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:26.386429
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:28.800511
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:31.216082
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:19:33.814427
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:19:36.227903
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:19:38.641581
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:41.055776
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:43.469424
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:45.883048
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:48.449835
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:50.860412
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:53.276638
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:55.690231
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:19:58.105971
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:00.520464
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:02.935835
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:05.350778
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:07.765306
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:10.179920
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:12.593692
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:15.010928
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:17.419132
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:19.833678
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:22.247271
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:24.796914
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:26.123382
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:20:49.374062
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import Mock, call

    manifest_url = 'https://example.com/path/playlist.m3u8'
    final_manifest_url = 'https://cdn.example.com/media/playlist.m3u8'
    manifest = '''\
#EXTM3U
#EXT-X-VERSION:3
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

    response = Mock()
    response.geturl.return_value = final_manifest_url
    response.read.return_value = manifest.encode('utf-8')

    ydl = Mock()
    ydl.urlopen.return_value = response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(
        side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'first fragment'),
        (True, b'second fragment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'url': manifest_url,
        'is_live': False,
        'http_headers': {'User-Agent': 'test-agent'},
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True

    ydl.urlopen.assert_called_once_with(manifest_url)

    prepared_ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert prepared_ctx['filename'] == 'output.ts'
    assert prepared_ctx['total_frags'] == 2
    assert prepared_ctx['ad_frags'] == 1
    assert prepared_ctx['fragment_index'] == 0

    assert fd._download_fragment.call_count == 2

# Generated at 2026-10-25 03:21:17.823431
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:20.237540
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:22.653475
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:25.222703
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:27.637931
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:30.052029
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:21:45.900204
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():global can_decrypt_frag


# Generated at 2026-10-25 03:22:12.711508
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:15.125855
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:17.539849
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:22:20.113853
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:22:22.529364
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:22:24.945615
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:22:27.359598
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:22:29.933064
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 03:22:48.772957
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():manifest = '#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:10\n#EXTINF:10.0,\nseg1.ts\n#EXT-X-ENDLIST'

# Generated at 2026-10-25 03:23:08.136412
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest_url = 'https://example.com/master/media.m3u8'
    redirected_manifest_url = 'https://cdn.example.com/hls/media.m3u8'
    manifest = b'''#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:5.0,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5.0,
ads/ad-1.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:5.0,
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
'''

    class FakeResponse:
        def geturl(self):
            return redirected_manifest_url

        def read(self):
            return manifest

    ydl = MagicMock()
    ydl.urlopen.return_value = FakeResponse()

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    })

    fd.to_screen = MagicMock()
    fd._prepare_url = MagicMock(side_effect=lambda info_dict, url: url)

    prepared_contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx)

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'first-fragment'),
        (True, b'second-fragment'),
    ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'url': manifest_url,
        'is_live': False,
        'http_headers': {'User-Agent': 'test-agent'},
    }

    assert fd.real_download('video.ts', info_dict) is True

    # The manifest is requested through the prepared URL.
    fd._prepare_url.assert_called_once_with(info_dict, manifest_url)
    ydl.urlopen.assert_called_once_with(manifest_url)

    # The ad fragment is counted but not downloaded.
    assert len(prepared_contexts) == 1
    ctx = prepared_contexts[0]
    assert ctx['filename'] == 'video.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    downloaded_urls = [
        invocation.args[1]
        for invocation in fd._download_fragment.call_args_list
    ]
    assert downloaded_urls == [
        'https://cdn.example.com/hls/segment-1.ts',
        'https://media.example.com/segment-2.ts',
    ]

    fd._append_fragment.assert_has_calls([
        call(ctx, b'first-fragment'),
        call(ctx, b'second-fragment'),
    ])
    assert fd._append_fragment.call_count == 2
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 03:23:10.693937
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:13.218185
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:15.632128
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:18.175058
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:20.589929
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:23.005258
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:25.423474
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:27.838369
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:30.252965
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:32.666702
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:34.268621
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:23:35.680746
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:24:00.177390
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    manifest = b"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10.0,
segment-1.ts
#UPLYNK-SEGMENT,ad
#EXTINF:5.0,
advertisement.ts
#UPLYNK-SEGMENT,segment
#EXT-X-BYTERANGE:4@10
#EXTINF:10.0,
segment-2.ts
#EXT-X-ENDLIST
"""

    manifest_url = 'https://example.com/video/master.m3u8'
    response = Mock()
    response.geturl.return_value = manifest_url
    response.read.return_value = manifest

    ydl = Mock()
    ydl.urlopen.return_value = response

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    # Avoid filesystem access and exercise only real_download's HLS logic.
    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    def start_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=start_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'first-fragment'),
        (True, b'second-fragment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {'url': manifest_url}

    assert fd.real_download('output.ts', info_dict) is True

    ydl.urlopen.assert_called_once_with(manifest_url)

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    download_calls = fd._download_fragment.call_args_list
    assert len(download_calls) == 2

    first_args = download_calls[0][0]

# Generated at 2026-10-25 03:24:52.298955
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:24:53.680601
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:24:55.013007
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:25:45.415095
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:25:46.850648
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:25:48.252809
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:26:07.549361
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b"""\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10,
https://media.example.com/segment-2.ts
#EXT-X-ENDLIST
"""

    manifest_response = MagicMock()
    manifest_response.geturl.return_value = (
        'https://cdn.example.com/video/index.m3u8'
    )
    manifest_response.read.return_value = manifest

    ydl = MagicMock()
    ydl.urlopen.return_value = manifest_response

    fd = HlsFD.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    }

    fd.to_screen = MagicMock()
    fd._prepare_url = MagicMock(
        side_effect=lambda info_dict, url: url)

    # real_download expects this method to initialize fragment_index.
    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(
        side_effect=[
            (True, b'first-fragment'),
            (True, b'second-fragment'),
        ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()
    fd.report_error = MagicMock()
    fd.report_warning = MagicMock()

    info_dict = {
        'url': 'https://example.com/original/index.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True

    fd._prepare_url.assert_called_once_with(
        info_dict, info_dict['url'])
    ydl.urlopen.assert_called_once_with(info_dict['url'])

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1
    assert ctx['fragment_index'] == 0

    downloaded_urls = [
        call.args[1] for call in fd._download_fragment.call_args_list
    ]
    assert downloaded_urls == [
        'https://cdn.example.com/video/segment-1.ts',
        'https://media.example.com/segment-2.ts',
    ]

    # The advertisement fragment must not be downloaded.
    assert 'https://cdn.example.com/video/advertisement.ts' not in downloaded_urls

    appended_fragments = [
        call.args[1] for call in fd._append_fragment.call_args_list
    ]
    assert appended_fragments == [
        b'first-fragment',
        b'second-fragment',
    ]

    fd._finish_frag_download.assert_called_once_with(ctx)
    fd.report_error.assert_not_called()
    fd.report_warning.assert_not_called()

# Generated at 2026-10-25 03:26:31.437077
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    manifest = b'''#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:10,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@10
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
'''

    class FakeResponse(object):
        def read(self):
            return manifest

        def geturl(self):
            # Simulate a redirected manifest URL. Relative fragment URLs should
            # be resolved against this URL.
            return 'https://cdn.example.com/video/index.m3u8'

    class FakeYDL(object):
        def __init__(self):
            self.requested_urls = []

        def urlopen(self, request):
            if hasattr(request, 'get_full_url'):
                request_url = request.get_full_url()
            else:
                request_url = request
            self.requested_urls.append(request_url)
            return FakeResponse()

        def to_screen(self, *args, **kwargs):
            pass

    class RecordingHlsFD(HlsFD):
        def __init__(self, ydl):
            HlsFD.__init__(self, ydl, {})
            self.downloaded_fragments = []
            self.appended_fragments = []
            self.download_context = None
            self.finished = False

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0
            self.download_context = ctx

        def _download_fragment(self, ctx, frag_url, info_dict, headers=None):
            self.downloaded_fragments.append((
                frag_url,
                dict(headers or {}),
            ))
            return True, ('content:%s' % frag_url).encode('utf-8')

        def _append_fragment(self, ctx, frag_content):
            self.appended_fragments.append(frag_content)

        def _finish_frag_download(self, ctx):
            self.finished = True

    ydl = FakeYDL()
    fd = RecordingHlsFD(ydl)


# Generated at 2026-10-25 03:26:33.956891
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:26:36.506161
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:26:39.051611
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 03:27:01.095715
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    manifest = b"""\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:10
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@100
segment-2.ts
#EXT-X-ENDLIST
"""

    class FakeResponse(object):
        def geturl(self):
            return 'https://cdn.example.com/video/index.m3u8'

        def read(self):
            return manifest

    ydl = Mock()
    ydl.urlopen.return_value = FakeResponse()

    fd = HlsFD.__new__(HlsFD)
    fd.ydl = ydl
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }
    fd._progress_hooks = []

    fd.to_screen = Mock()
    fd.report_error = Mock()
    fd.report_warning = Mock()
    fd._prepare_url = Mock(side_effect=lambda info, url: url)

    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(
        side_effect=prepare_download)

    downloaded = []

    def download_fragment(ctx, url, info_dict, headers):
        # Copy headers because real_download reuses and mutates the same dict.
        downloaded.append((url, dict(headers)))
        content = {
            'https://cdn.example.com/video/segment-1.ts': b'fragment-one',
            'https://cdn.example.com/video/segment-2.ts': b'frag',
        }[url]
        return True, content

    fd._download_fragment = Mock(side_effect=download_fragment)

    appended = []
    fd._append_fragment = Mock(
        side_effect=lambda ctx, content: appended.append(content))
    fd._finish_frag_download = Mock()

    info_dict = {
        'url': 'https://origin.example.com/playlist.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }
