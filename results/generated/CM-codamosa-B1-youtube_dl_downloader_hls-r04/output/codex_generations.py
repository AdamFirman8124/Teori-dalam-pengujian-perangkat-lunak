

# Generated at 2026-10-25 08:16:37.935920
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:16:40.350710
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:16:42.764907
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:08.771883
# Unit test for constructor of class HlsFD
def test_HlsFD():
    fd = HlsFD(None, {})
    assert fd.FD_NAME == 'hlsnative'
    assert callable(fd.real_download)
    assert callable(fd.can_download)

# Generated at 2026-10-25 08:17:11.417496
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:13.834582
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:16.246774
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:18.661010
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:21.074980
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:23.490515
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:25.905038
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:28.417265
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:30.804199
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:33.219707
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:35.633205
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:38.051555
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:17:40.466822
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:42.879449
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:45.298538
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:47.714832
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:50.129824
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:52.543635
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:54.962301
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:57.375970
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:17:59.791320
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:18:02.209634
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:18:04.627441
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:18:07.040789
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:18:09.455370
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:11.873917
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:14.290618
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:16.714707
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:19.127113
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:21.544415
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:23.961769
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:26.374481
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:28.788562
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:31.207721
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:18:46.866050
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():manifest = '#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:10\n#EXTINF:10.0,\nseg1.ts\n#EXT-X-ENDLIST'

# Generated at 2026-10-25 08:19:23.130330
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import Mock

    manifest_url = 'https://cdn.example.com/video/index.m3u8'
    manifest = b'''\
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:10
#EXTINF:10.0,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
#EXTINF:5.0,
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXT-X-BYTERANGE:4@2
#EXTINF:10.0,
segment-2.ts
#EXT-X-ENDLIST
'''

    response = Mock()
    response.geturl.return_value = manifest_url
    response.read.return_value = manifest

    fd = HlsFD.__new__(HlsFD)
    fd.ydl = Mock()
    fd.ydl.urlopen.return_value = response
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    }
    fd._progress_hooks = []

    fd.to_screen = Mock()
    fd.report_error = Mock()
    fd.report_warning = Mock()
    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._finish_frag_download = Mock()
    fd._append_fragment = Mock()

    downloaded = []

    def download_fragment(ctx, url, info_dict, headers):
        downloaded.append((url, dict(headers)))
        contents = {
            'https://cdn.example.com/video/segment-1.ts': b'first',
            'https://cdn.example.com/video/segment-2.ts': b'next',
        }
        return True, contents[url]

    fd._download_fragment = Mock(side_effect=download_fragment)

    info_dict = {
        'url': 'https://example.com/original.m3u8',
        'http_headers': {'User-Agent': 'test-agent'},
        'is_live': False,
    }

    assert fd.real_download('output.ts', info_dict) is True

    # The ad fragment must not be downloaded.
    assert downloaded == [
        (
            'https://cdn.example.com/video/segment-1.ts',
            {'User-Agent': 'test-agent'},
        ),
        (
            'https://cdn.example.com/video/segment-2.ts',
            {
                'User-Agent': 'test-agent',
                'Range': 'bytes=2-5',
            },
        ),
    ]

    assert [
        call_args[0][1]
        for call_args in fd._append_fragment.call_args_list
    ] == [b'first', b'next']

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.ts'
    assert ctx['total_frags'] == 2
    assert ctx['ad_frags'] == 1

    fd._finish_frag_download.assert_called_once_with(ctx)
    fd.report_error.assert_not_called()
    fd.report_warning.assert_not_called()

# Generated at 2026-10-25 08:19:57.400397
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:19:59.816498
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:02.231390
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:04.645359
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:20:07.264086
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:20:09.677251
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:20:12.094375
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:14.509144
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:16.926022
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:19.342770
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:21.759841
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:24.176804
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:26.591725
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:29.005680
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:31.422701
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:33.837258
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:36.248826
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:38.665441
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:41.079376
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:20:43.493061
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:20:45.910304
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:20:48.328553
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:50.746542
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:53.160257
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:55.578753
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:20:58.076754
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:00.452326
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:02.870517
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:05.284918
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:07.701026
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:10.121064
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:12.555720
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:14.974174
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:17.388335
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:21:19.876102
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:21:23.078976
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:21:25.790481
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:28.492509
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:31.345802
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:21:33.846757
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:21:36.422785
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:21:39.350226
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:21:42.041180
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:21:44.819155
# Unit test for method can_download of class HlsFD
def test_HlsFD_can_download():manifest = '#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:10\n#EXTINF:10.0,\nseg1.ts\n#EXT-X-ENDLIST'

# Generated at 2026-10-25 08:23:16.304104
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:23:17.670319
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:23:19.066190
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:23:59.191326
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import Mock, call

    manifest_url = 'https://origin.example/master.m3u8'
    redirected_manifest_url = 'https://cdn.example/video/playlist.m3u8'

    manifest = b'''#EXTM3U
#EXT-X-VERSION:3
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

    class ManifestResponse(object):
        def geturl(self):
            return redirected_manifest_url

        def read(self):
            return manifest

    ydl = Mock()
    ydl.urlopen.return_value = ManifestResponse()

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })
    fd.to_screen = Mock()
    fd._prepare_url = Mock(side_effect=lambda _info, url: url)

    prepared_contexts = []

    def prepare_download(ctx):
        # FragmentFD normally initializes this value.
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx)

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    downloaded_fragments = []

    def download_fragment(ctx, url, info_dict, headers):
        # Copy headers because real_download mutates the shared dictionary when
        # processing a byte range.
        downloaded_fragments.append((url, dict(headers)))

        content = {
            'https://cdn.example/video/segment-1.ts': b'first',
            'https://cdn.example/video/segment-2.ts': b'cond',
        }
        return True, content[url]

    fd._download_fragment = Mock(side_effect=download_fragment)

    info_dict = {
        'url': manifest_url,
        'is_live': False,
        'http_headers': {'User-Agent': 'test-agent'},
    }

    assert fd.real

# Generated at 2026-10-25 08:24:40.869382
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    from unittest.mock import Mock, call

    manifest_url = 'https://example.com/master/playlist.m3u8'
    redirected_url = 'https://cdn.example.com/media/playlist.m3u8'
    manifest = b'''\
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:7
#EXTINF:10,
segment-1.ts
#ANVATO-SEGMENT-INFO:type=ad
advertisement.ts
#ANVATO-SEGMENT-INFO:type=master
#EXTINF:10,
segment-2.ts
#EXT-X-ENDLIST
'''

    class ManifestResponse(object):
        def geturl(self):
            return redirected_url

        def read(self):
            return manifest

    ydl = Mock()
    ydl.urlopen.return_value = ManifestResponse()

    fd = HlsFD(ydl, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })
    fd.to_screen = Mock()
    fd._prepare_url = Mock(side_effect=lambda info_dict, url: url)

    prepared_context = {}

    def prepare_download(ctx):
        # FragmentFD normally initializes this value.
        ctx['fragment_index'] = 0
        prepared_context.update(ctx)

    fd._prepare_and_start_frag_download = Mock(
        side_effect=prepare_download)

    downloaded_fragments = []

    def download_fragment(ctx, url, info_dict, headers):
        downloaded_fragments.append((url, dict(headers)))
        contents = {
            'https://cdn.example.com/media/segment-1.ts': b'fragment-one',
            'https://cdn.example.com/media/segment-2.ts': b'fragment-two',
        }
        return True, contents[url]

    fd._download_fragment = Mock(side_effect=download_fragment)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'url': manifest_url,
        'http_headers': {'User-Agent': 'test-agent'},
    }

    result = fd.real_download('output.ts', info_dict)

    assert result is True
    assert prepared_context['filename'] == 'output.ts'
    assert prepared_context['total_frags'] == 2

# Generated at 2026-10-25 08:24:43.412371
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:24:46.030878
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:24:48.449533
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:24:50.866851
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:24:53.288143
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:24:55.704880
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:24:58.125392
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:25:00.545005
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:25:02.961245
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:25:05.383656
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:25:07.798762
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:25:10.221181
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:25:12.634415
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:25:15.057551
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:25:17.470259
# Unit test for method can_download of class HlsFD

# Generated at 2026-10-25 08:26:00.654097
# Unit test for method real_download of class HlsFD
def test_HlsFD_real_download():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    manifest = """\
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
"""


# Generated at 2026-10-25 08:26:51.120502
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:26:53.572693
# Unit test for method real_download of class HlsFD

# Generated at 2026-10-25 08:26:55.962245
# Unit test for method real_download of class HlsFD