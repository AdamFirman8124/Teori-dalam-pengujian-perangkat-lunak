

# Generated at 2026-10-24 04:13:20.511679
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = Mock()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:13:22.930227
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:25.349317
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:27.767668
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:30.274885
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:13:32.691455
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:13:35.108680
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:13:37.530142
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:13:39.947311
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:13:42.362825
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:13:44.793849
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:47.198851
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:49.614431
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:52.039769
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:54.452461
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:56.869675
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:13:59.284708
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:14:01.700857
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:14:04.114859
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:14:06.529685
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:14:08.945427
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:14:11.362492
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:14:13.778636
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:14:16.196149
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:14:18.616224
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:14:50.535933
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:12.622694
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:15.038107
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:17.598255
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:20.012702
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:22.428738
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:24.841841
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:27.257076
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:29.673503
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:15:32.091627
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:15:38.410560
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():downloader = DashSegmentsFD(None, {})

# Generated at 2026-10-24 04:15:48.597978
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': True,
    }

    fd = DashSegmentsFD(ydl, params)

    assert isinstance(fd, FragmentFD)
    assert fd.ydl is ydl
    assert fd.params is params
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:16:07.142629
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyYDL(object):
        pass

    ydl = DummyYDL()
    params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:16:15.309013
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
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:16:33.434901
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    downloaded_urls = []
    appended_fragments = []
    events = []

    def prepare(ctx):
        assert ctx['filename'] == 'output.mp4'
        assert ctx['total_frags'] == 2
        ctx['fragment_index'] = 0
        events.append('prepare')

    def download(ctx, fragment_url, passed_info_dict):
        assert passed_info_dict is info_dict
        downloaded_urls.append(fragment_url)
        return True, fragment_url.encode('utf-8')

    def append(ctx, fragment_content):
        appended_fragments.append(fragment_content)
        events.append('append')

    def finish(ctx):
        events.append('finish')

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download
    fd._append_fragment = append
    fd._finish_frag_download = finish

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert downloaded_urls == [
        'https://example.com/media/init.mp4',
        'https://cdn.example.com/segment-1.m4s',
    ]
    assert appended_fragments == [
        b'https://example.com/media/init.mp4',
        b'https://cdn.example.com/segment-1.m4s',
    ]
    assert events == ['prepare', 'append', 'append', 'finish']

# Generated at 2026-10-24 04:16:42.138035
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class FakeYDL:
        def report_progress(self, status):
            pass

    ydl = FakeYDL()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:16:51.558618
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class FakeYDL:
        params = {}

    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(FakeYDL(), params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl.__class__ is FakeYDL
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:17:00.263213
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True, 'fragment_retries': 2}

    downloader = DashSegmentsFD(ydl, params)

    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert callable(downloader.real_download)
    assert callable(downloader.report_progress)
    assert downloader.report_progress in downloader._progress_hooks

# Generated at 2026-10-24 04:17:21.665852
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:17:32.683289
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():import types


# Generated at 2026-10-24 04:17:35.215102
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:17:47.576948
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:18:00.638196
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():fd = DashSegmentsFD.__new__(DashSegmentsFD)

# Generated at 2026-10-24 04:18:10.426265
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    params = {
        'test': True,
        'fragment_retries': 3,
        'skip_unavailable_fragments': False,
    }
    downloader = object()

    fd = DashSegmentsFD(downloader, params)

    assert isinstance(fd, FragmentFD)
    assert fd.ydl is downloader
    assert fd.params is params
    assert fd.FD_NAME == 'dashsegments'
    assert callable(fd.real_download)

# Generated at 2026-10-24 04:18:21.776731
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {
        'test': True,
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:18:24.196007
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:18:26.720105
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:18:29.145433
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:18:31.552759
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:18:33.966535
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:18:36.386079
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:18:38.804093
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:18:41.221300
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:18:47.274191
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():params = {'test': True, 'fragment_retries': 2}

# Generated at 2026-10-24 04:18:56.795192
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader._ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:19:06.127572
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyYDL(object):
        pass

    ydl = DummyYDL()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:19:34.762885
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:19:45.540867
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():fd = DashSegmentsFD.__new__(DashSegmentsFD)

# Generated at 2026-10-24 04:19:55.878576
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():fd = object.__new__(DashSegmentsFD)

# Generated at 2026-10-24 04:20:17.575207
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    events = []

    class StubDashSegmentsFD(DashSegmentsFD):
        def __init__(self):
            self.params = {}

        def _prepare_and_start_frag_download(self, ctx):
            events.append(('prepare', ctx['filename'], ctx['total_frags']))
            ctx['fragment_index'] = 0

        def _download_fragment(self, ctx, fragment_url, fragment_info):
            assert fragment_info is info_dict
            events.append(('download', fragment_url))
            return True, fragment_url.rsplit('/', 1)[-1].encode('ascii')

        def _append_fragment(self, ctx, fragment_content):
            events.append(('append', fragment_content))
            ctx['fragment_index'] += 1

        def _finish_frag_download(self, ctx):
            events.append(('finish', ctx['filename']))

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    downloader = StubDashSegmentsFD()

    assert downloader.real_download('output.mp4', info_dict) is True
    assert events == [
        ('prepare', 'output.mp4', 2),
        ('download', 'https://example.com/video/init.m4s'),
        ('append', b'init.m4s'),
        ('download', 'https://cdn.example.com/segment-1.m4s'),
        ('append', b'segment-1.m4s'),
        ('finish', 'output.mp4'),
    ]

# Generated at 2026-10-24 04:20:44.927847
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    calls = []
    attempts = {}

    def prepare(ctx):
        assert ctx['filename'] == 'output.mp4'
        assert ctx['total_frags'] == 2
        ctx['fragment_index'] = 0
        calls.append(('prepare',))

    def download_fragment(ctx, fragment_url, info_dict):
        calls.append(('download', fragment_url))
        attempts[fragment_url] = attempts.get(fragment_url, 0) + 1

        # Verify that an HTTP error causes the first fragment to be retried.
        if fragment_url.endswith('/init.mp4') and attempts[fragment_url] == 1:
            raise compat_urllib_error.HTTPError(
                fragment_url, 404, 'Not Found', None, None)

        if fragment_url.endswith('/init.mp4'):
            return True, b'initialization segment'
        return True, b'media segment'

    def append_fragment(ctx, content):
        calls.append(('append', content))

    def report_retry(error, frag_index, count, retries):
        calls.append(('retry', error.code, frag_index, count, retries))

    def finish(ctx):
        calls.append(('finish',))

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd.report_retry_fragment = report_retry
    fd._finish_frag_download = finish

    info_dict = {
        'fragment_base_url': 'https://cdn.example.test/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.test/video/segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

# Generated at 2026-10-24 04:20:52.574124
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 04:21:05.420704
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()
    fd.report_retry_fragment = MagicMock()
    fd.report_skip_fragment = MagicMock()
    fd.report_error = MagicMock()

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/video/segment-1.m4s',
        404,
        'Not Found',
        None,
        None,
    )

    # The initialization fragment succeeds. The media fragment fails once
    # with an HTTP error and then succeeds on retry.
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'initialization fragment'),
        http_error,
        (True, b'media fragment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_count == 3
    assert fd._download_fragment.call_args_list[0].args[1] == \
        'https://cdn.example.com/init.mp4'
    assert fd._download_fragment.call_args_list[1].args[1] == \
        'https://example.com/video/segment-1.m4s'
    assert fd._download_fragment.call_args_list[2].args[1] == \
        'https://example.com/video/segment-1.m4s'

    assert fd._append_fragment.call_args_list[0].args[1] == \
        b'initialization fragment'
    assert fd._append_fragment.call_args_list[1].args[1] == \
        b'media fragment'

    fd.report_retry_fragment.assert_called_once_with(http_error, 2, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 04:21:23.843689
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    downloader = DashSegmentsFD.__new__(DashSegmentsFD)
    downloader.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    contexts = []

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        contexts.append(ctx)

    downloader._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    downloader._download_fragment = MagicMock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    downloader._append_fragment = MagicMock()
    downloader._finish_frag_download = MagicMock()

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = downloader.real_download('output.mp4', info_dict)

    assert result is True
    assert len(contexts) == 1

    ctx = contexts[0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert downloader._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example.com/init.mp4', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
    ]
    assert downloader._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    downloader._prepare_and_start_frag_download.assert_called_once_with(ctx)
    downloader._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 04:21:36.516784
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = mock.Mock(side_effect=prepare)
    fd._append_fragment = mock.Mock()
    fd._finish_frag_download = mock.Mock()
    fd.report_retry_fragment = mock.Mock()
    fd.report_skip_fragment = mock.Mock()
    fd.report_error = mock.Mock()

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.m4s',
        404,
        'Not Found',
        {},
        None,
    )

    fd._download_fragment = mock.Mock(side_effect=[
        http_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        mock.call(
            ctx,
            'https://example.com/video/init.m4s',
            info_dict,
        ),
        mock.call(
            ctx,
            'https://example.com/video/init.m4s',
            info_dict,
        ),
        mock.call(
            ctx,
            'https://cdn.example.com/segment-1.m4s',
            info_dict,
        ),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        http_error, 1, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()

    assert fd._append_fragment.call_args_list == [
        mock.call(ctx, b'initialization segment'),
        mock.call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 04:21:38.934292
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:21:41.348556
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:21:43.895508
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:21:46.310314
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:21:48.728286
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:22:11.662357
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:22:27.974022
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import Mock, call

    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]

    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(
            ctx,
            'https://example.com/video/init.mp4',
            info_dict,
        ),
        call(
            ctx,
            'https://cdn.example.com/segment-1.m4s',
            info_dict,
        ),
    ]

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 04:22:46.015759
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(
        side_effect=[
            (True, b'initialization segment'),
            (True, b'media segment'),
        ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]

    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 04:22:48.432022
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:22:50.849950
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:22:53.274112
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 04:22:55.866515
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 04:23:11.021503
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():events = []

# Generated at 2026-10-24 04:23:20.988368
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
    assert downloader._progress_hooks == []