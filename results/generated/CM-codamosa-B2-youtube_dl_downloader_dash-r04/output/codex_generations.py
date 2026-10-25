

# Generated at 2026-10-24 12:43:28.975571
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

# Generated at 2026-10-24 12:43:53.664414
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    captured = {}

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        captured['ctx'] = ctx

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    first_retry_error = compat_urllib_error.HTTPError(
        'https://cdn.example.test/video-1.m4s',
        404, 'Not Found', None, None)
    skipped_fragment_error = compat_urllib_error.HTTPError(
        'https://cdn.example.test/video-2.m4s',
        404, 'Not Found', None, None)

    responses = iter([
        (True, b'initialization segment'),
        first_retry_error,
        (True, b'media segment 1'),
        skipped_fragment_error,
        skipped_fragment_error,
    ])

    def download_fragment(ctx, fragment_url, info_dict):
        response = next(responses)
        if isinstance(response, BaseException):
            raise response
        return response

    fd._download_fragment = Mock(side_effect=download_fragment)

    info_dict = {
        'fragment_base_url': 'https://cdn.example.test/',
        'fragments': [
            {'url': 'https://cdn.example.test/init.mp4'},
            {'path': 'video-1.m4s'},
            {'path': 'video-2.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    ctx = captured['ctx']
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 3

    downloaded_urls = [
        mock_call.args[1]
        for mock_call in fd._download_fragment.call_args_list
    ]

# Generated at 2026-10-24 12:44:02.996991
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader._progress_hooks == []

# Generated at 2026-10-24 12:44:35.841357
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import MagicMock, call

    params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }
    fd = DashSegmentsFD(None, params)

    # Normally this method initializes fragment_index and output files.
    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(side_effect=prepare)
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'initialization-segment'),
        (True, b'media-segment'),
    ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'fragment_base_url': 'https://cdn.example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = fd.real_download('video.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'video.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example.com/init.m4s', info_dict),
        call(ctx, 'https://cdn.example.com/video/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization-segment'),
        call(ctx, b'media-segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 12:44:38.258411
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:44:40.850490
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:44:43.266262
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:44:45.684461
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:44:48.102021
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:44:50.515660
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:44:52.934364
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:44:55.351198
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:44:57.764647
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:45:00.180952
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:45:02.595567
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:45:05.009197
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:45:07.426051
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:45:13.534818
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():params = {'test': True}

# Generated at 2026-10-24 12:45:42.616683
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import Mock, call

    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    # Normally initialized by _prepare_and_start_frag_download.
    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare)
    fd._append_fragment = Mock()
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

    # The initialization fragment succeeds immediately. The media fragment
    # fails once and then succeeds on retry.
    fd._download_fragment = Mock(side_effect=[
        (True, b'initialization data'),
        retry_error,
        (True, b'media data'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    fd._prepare_and_start_frag_download.assert_called_once()
    prepared_ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert prepared_ctx['filename'] == 'output.mp4'
    assert prepared_ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(
            prepared_ctx,
            'https://cdn.example.com/init.mp4',
            info_dict,
        ),
        call(
            prepared_ctx,
            'https://example.com/video/segment-1.m4s',
            info_dict,
        ),
        call(
            prepared_ctx,
            'https://example.com/video/segment-1.m4s',
            info_dict,
        ),
    ]

    assert fd._append_fragment.call_args_list == [
        call(prepared_ctx, b'initialization data'),
        call(prepared_ctx, b'media data'),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 2, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(prepared_ctx)

# Generated at 2026-10-24 12:45:51.939717
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class FakeYDL(object):
        pass

    ydl = FakeYDL()
    params = {
        'test': True,
        'fragment_retries': 2,
        'skip_unavailable_fragments': False,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params == params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 12:46:00.837993
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = Mock()
    params = {
        'test': False,
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 12:46:20.495913
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyYDL(object):
        params = {}
        _progress_hooks = []

    ydl = DummyYDL()
    params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': False,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 12:47:02.480618
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:47:52.964350
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:47:56.649565
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:48:14.582412
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:48:27.718439
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:48:29.107011
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:49:14.883362
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:49:38.538577
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:49:57.790331
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:50:00.532661
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:03.047045
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:05.461175
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:07.876599
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:10.293302
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:12.707921
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:15.240411
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:17.653604
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:20.069243
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:22.481970
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:50:24.895634
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:50:27.309534
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:50:29.722663
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:46.225440
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:51:38.450025
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:52:01.095823
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:52:21.428357
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:52:23.928986
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:52:26.342352
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:52:28.755655
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:52:31.169347
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:52:48.916582
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:05.591967
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:53:08.009881
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:10.428270
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:12.845928
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:15.265368
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:17.684696
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:20.097910
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:22.510527
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:24.924317
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:27.337117
# Unit test for method real_download of class DashSegmentsFD