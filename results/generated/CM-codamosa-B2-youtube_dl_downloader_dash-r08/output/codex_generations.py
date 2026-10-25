

# Generated at 2026-10-25 01:14:57.034188
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 2,
        'skip_unavailable_fragments': True,
    }

    def prepare(ctx):
        ctx['fragment_index'] = 0

    def append(ctx, _content):
        ctx['fragment_index'] += 1

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare)
    fd._append_fragment = Mock(side_effect=append)
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    retry_error = compat_urllib_error.HTTPError(
        'https://example.com/video/segment-1.m4s',
        404,
        'Not Found',
        {},
        None,
    )

    fd._download_fragment = Mock(side_effect=[
        (True, b'initialization segment'),
        retry_error,
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 2,
    }

    requested_urls = [
        call_args[0][1]
        for call_args in fd._download_fragment.call_args_list
    ]
    assert requested_urls == [
        'https://cdn.example.com/init.mp4',
        'https://example.com/video/segment-1.m4s',
        'https://example.com/video/segment-1.m4s',
    ]

    appended_content = [
        call_args[0][1]
        for call_args in fd._append_fragment.call_args_list
    ]
    assert appended_content == [
        b'initialization segment',
        b'media segment',
    ]


# Generated at 2026-10-25 01:14:59.450581
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:01.868601
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:04.284841
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:06.702376
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:09.117377
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:11.532376
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:13.947815
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:16.362238
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:18.777014
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:21.193008
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:23.607776
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:26.023159
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:28.438539
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:30.853589
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:33.268962
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:35.682652
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:38.097274
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:40.513958
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:42.929208
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:45.344186
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:47.759301
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:50.179799
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:52.589253
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:55.004462
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:15:57.419373
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:15:59.835650
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:16:02.250188
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:16:04.665577
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:16:07.080710
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:16:09.495452
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:16:11.910348
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:14.325610
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:16.740758
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:19.158010
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:21.572645
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:23.987860
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:26.404850
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:28.819323
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:31.234940
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:33.650057
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:36.067673
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:38.483147
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:40.898979
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:43.314341
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:45.728585
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:48.144928
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:50.557290
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:52.971292
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:55.386671
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:16:57.800733
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:17:00.215336
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:17:02.632524
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:17:05.044357
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:17:07.460227
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:17:09.875168
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:17:12.290984
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:17:27.459141
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():downloaded_urls = []

# Generated at 2026-10-25 01:17:41.384679
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert callable(downloader.real_download)

# Generated at 2026-10-25 01:17:49.270550
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(None, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is None
    assert downloader.params == params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-25 01:17:51.690842
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:17:54.109541
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:17:56.523611
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:17:58.941886
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:18:01.355199
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:18:03.770307
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:18:06.185383
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:18:08.599536
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:18:11.016041
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:18:13.432341
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:18:15.963424
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import Mock, call


# Generated at 2026-10-25 01:18:34.429358
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    retry_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.mp4',
        404,
        'Not Found',
        None,
        None,
    )

    fd._download_fragment = Mock(side_effect=[
        retry_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/media-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/media-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 1, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:18:42.928229
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyDownloader:
        pass

    downloader = DummyDownloader()
    params = {
        'test': True,
        'fragment_retries': 2,
        'skip_unavailable_fragments': False,
    }

    fd = DashSegmentsFD(downloader, params)

    assert isinstance(fd, DashSegmentsFD)
    assert isinstance(fd, FragmentFD)
    assert fd.ydl is downloader
    assert fd.params is params
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-10-25 01:18:52.143604
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {
        'test': True,
        'fragment_retries': 3,
        'skip_unavailable_fragments': False,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader._progress_hooks
    assert downloader._progress_hooks[0] == downloader.report_progress

# Generated at 2026-10-25 01:18:54.662861
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:18:57.081063
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:18:59.616700
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:19:02.034191
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:19:04.450037
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:19:06.862915
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:19:09.277801
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:19:11.692517
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:19:14.106529
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:19:16.522501
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:19:19.276314
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import Mock, call


# Generated at 2026-10-25 01:19:40.273520
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fragment_url = 'https://cdn.example.com/video/init.mp4'
    info_dict = {
        'fragment_base_url': 'https://cdn.example.com/video/',
        'fragments': [{'path': 'init.mp4'}],
    }

    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)

    http_error = compat_urllib_error.HTTPError(
        fragment_url, 404, 'Not Found', {}, None)
    fd._download_fragment = Mock(side_effect=[
        http_error,
        (True, b'fragment data'),
    ])

    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    assert fd.real_download('output.mp4', info_dict) is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 1
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ctx, fragment_url, info_dict),
        call(ctx, fragment_url, info_dict),
    ]
    fd.report_retry_fragment.assert_called_once_with(http_error, 1, 1, 1)
    fd._append_fragment.assert_called_once_with(ctx, b'fragment data')
    fd._finish_frag_download.assert_called_once_with(ctx)

    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()

# Generated at 2026-10-25 01:19:57.168364
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    prepared_contexts = []
    downloaded_urls = []
    appended_fragments = []
    finished_contexts = []

    def prepare(ctx):
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx)

    def download(ctx, fragment_url, info_dict):
        downloaded_urls.append(fragment_url)
        return True, fragment_url.encode('utf-8')

    def append(ctx, content):
        appended_fragments.append(content)

    def finish(ctx):
        finished_contexts.append(ctx)

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download
    fd._append_fragment = append
    fd._finish_frag_download = finish

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert len(prepared_contexts) == 1
    assert prepared_contexts[0]['filename'] == 'output.mp4'
    assert prepared_contexts[0]['total_frags'] == 2

    assert downloaded_urls == [
        'https://example.com/media/init.mp4',
        'https://cdn.example.com/segment-1.m4s',
    ]
    assert appended_fragments == [
        b'https://example.com/media/init.mp4',
        b'https://cdn.example.com/segment-1.m4s',
    ]

    assert finished_contexts == prepared_contexts

# Generated at 2026-10-25 01:19:59.697393
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:02.111103
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:04.525288
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:06.942182
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:09.355474
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:11.772596
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:14.373450
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:16.787857
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:19.203773
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:20:21.618390
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:20:24.359574
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import Mock, call


# Generated at 2026-10-25 01:20:33.929576
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-25 01:20:56.458737
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    info_dict = {
        'fragment_base_url': 'https://cdn.example/video/',
        'fragments': [
            {'url': 'https://cdn.example/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    retry_error = compat_urllib_error.HTTPError(
        'https://cdn.example/video/segment-1.m4s',
        404,
        'Not Found',
        None,
        None,
    )

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'initialization segment'),
        retry_error,
        (True, b'media segment'),
    ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()
    fd.report_retry_fragment = MagicMock()
    fd.report_skip_fragment = MagicMock()
    fd.report_error = MagicMock()

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example/init.mp4', info_dict),
        call(ctx, 'https://cdn.example/video/segment-1.m4s', info_dict),
        call(ctx, 'https://cdn.example/video/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 2, 1, 1)

# Generated at 2026-10-25 01:20:58.877437
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:21:01.294641
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:21:03.710353
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:21:06.135965
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:21:08.551432
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:21:10.966615
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:21:13.380795
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:21:15.795396
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:21:18.216095
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:21:20.625849
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:21:23.041328
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:21:25.456082
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:21:27.871065
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:21:30.287290
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:21:32.923517
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import Mock, call


# Generated at 2026-10-25 01:21:55.738342
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    downloaded_urls = []
    appended_fragments = []
    retry_reports = []
    skipped_fragments = []
    errors = []
    finished_contexts = []

    def prepare(ctx):
        ctx['fragment_index'] = 0

    def download_fragment(ctx, fragment_url, info_dict):
        downloaded_urls.append(fragment_url)

        # Verify that an HTTP failure for a non-initial fragment is retried.
        if fragment_url.endswith('segment-1.m4s') \
                and downloaded_urls.count(fragment_url) == 1:
            raise compat_urllib_error.HTTPError(
                fragment_url, 404, 'Not Found', {}, None)

        if fragment_url.endswith('init.mp4'):
            return True, b'initialization data'
        return True, b'media data'

    def append_fragment(ctx, content):
        appended_fragments.append(content)
        ctx['fragment_index'] += 1

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = lambda ctx: finished_contexts.append(dict(ctx))
    fd.report_retry_fragment = lambda err, index, count, retries: (
        retry_reports.append((index, count, retries)))
    fd.report_skip_fragment = skipped_fragments.append
    fd.report_error = errors.append

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    assert downloaded_urls == [
        'https://example.com/video/init.mp4',
        'https://cdn.example.com/segment-1.m4s',
        'https://cdn.example.com/segment-1.m4s',
    ]
    assert appended_fragments == [
        b'initialization data',
        b'media data',
    ]
    assert retry_reports == [(2, 1, 1)]
    assert skipped_fragments == []

# Generated at 2026-10-25 01:22:04.246629
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyYDL(object):
        pass

    ydl = DummyYDL()
    params = {
        'test': True,
        'fragment_retries': 2,
        'skip_unavailable_fragments': False,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader._progress_hooks == []
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-25 01:22:16.023524
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    def prepare(ctx):
        ctx['fragment_index'] = 0

    retry_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.mp4',
        404,
        'Not Found',
        {},
        None,
    )

    fd._prepare_and_start_frag_download = MagicMock(side_effect=prepare)
    fd._download_fragment = MagicMock(side_effect=[
        retry_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()
    fd.report_retry_fragment = MagicMock()
    fd.report_skip_fragment = MagicMock()
    fd.report_error = MagicMock()

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ]

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 1, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:22:29.847855
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ANY, 'https://cdn.example.com/init.m4s', info_dict),
        call(ANY, 'https://example.com/video/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ANY, b'initialization segment'),
        call(ANY, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:22:32.266747
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:22:43.263370
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():fd = DashSegmentsFD.__new__(DashSegmentsFD)

# Generated at 2026-10-25 01:22:53.705905
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():from unittest.mock import Mock


# Generated at 2026-10-25 01:23:09.005379
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = MagicMock()
    params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-25 01:23:15.517211
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = Mock()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params == params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-25 01:23:17.934258
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:20.349709
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:22.765875
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:25.179787
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:27.594787
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:30.009542
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:32.424331
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:34.839387
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:37.255415
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:23:57.506792
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    # Normally initialized by _prepare_and_start_frag_download.
    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'initialization-segment'),
        (True, b'media-segment-1'),
        (True, b'media-segment-2'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'fragment_base_url': 'https://example.com/media/manifest.mpd',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/media-1.m4s'},
            {'path': 'media-2.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 3

    downloaded_urls = [
        mock_call[0][1]
        for mock_call in fd._download_fragment.call_args_list
    ]
    assert downloaded_urls == [
        'https://example.com/media/init.m4s',
        'https://cdn.example.com/media-1.m4s',
        'https://example.com/media/media-2.m4s',
    ]

    assert all(
        mock_call[0][2] is info_dict
        for mock_call in fd._download_fragment.call_args_list
    )

    fd._append_fragment.assert_has_calls([
        call(ctx, b'initialization-segment'),
        call(ctx, b'media-segment-1'),
        call(ctx, b'media-segment-2'),
    ])
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:24:19.212312
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    base_url = 'https://example.com/video/'
    init_url = base_url + 'init.mp4'
    media_url = 'https://cdn.example.com/segment-1.m4s'

    http_error = compat_urllib_error.HTTPError(
        init_url, 404, 'Not Found', {}, None)

    # The first request fails once, succeeds on retry, and the second
    # fragment succeeds immediately.
    fd._download_fragment = Mock(side_effect=[
        http_error,
        (True, b'init data'),
        (True, b'media data'),
    ])

    info_dict = {
        'fragment_base_url': base_url,
        'fragments': [
            {'path': 'init.mp4'},
            {'url': media_url},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(ctx, init_url, info_dict),
        call(ctx, init_url, info_dict),
        call(ctx, media_url, info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'init data'),
        call(ctx, b'media data'),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        http_error, 1, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 01:24:21.629553
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:24:24.044136
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:24:26.623389
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:24:29.157365
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:24:31.572985
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:24:34.014527
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 01:24:36.401789
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:24:38.816233
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 01:24:41.233712
# Unit test for method real_download of class DashSegmentsFD