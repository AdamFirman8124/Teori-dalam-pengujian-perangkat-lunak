

# Generated at 2026-10-25 04:41:18.569643
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:41:20.972657
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:41:23.502226
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:41:25.917465
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:41:28.331808
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:41:30.915964
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():downloaded_urls = []

# Generated at 2026-10-25 04:41:38.550485
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:41:39.991677
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:41:44.898880
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:41:58.021028
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import Mock, call

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.mp4',
        404,
        'Not Found',
        {},
        None,
    )

    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    # real_download expects this method to initialize fragment_index.
    fd._prepare_and_start_frag_download = Mock(
        side_effect=lambda ctx: ctx.update(fragment_index=0)
    )
    fd._download_fragment = Mock(side_effect=[
        http_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/video/segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/video/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd.report_retry_fragment.assert_called_once_with(http_error, 1, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 04:42:10.625764
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare)
    fd._download_fragment = Mock(side_effect=[
        # First request fails and is retried
        compat_urllib_error.HTTPError(
            'https://example.com/init.mp4', 404, 'Not Found', {}, None),
        (True, b'init'),
        (True, b'media'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/init.mp4', info_dict),
        call(ctx, 'https://example.com/init.mp4', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'init'),
        call(ctx, b'media'),
    ]

    fd.report_retry_fragment.assert_called_once()
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 04:42:13.044593
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:42:15.461238
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:42:17.875263
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:42:20.292662
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:42:22.706355
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:42:25.122137
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:42:27.539456
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:42:29.953947
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:42:32.367467
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:42:34.781705
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:42:37.196460
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:42:41.225458
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():downloaded_urls = []

# Generated at 2026-10-25 04:43:09.675142
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    base_url = 'https://example.com/video/'
    init_url = base_url + 'init.mp4'
    retry_url = 'https://cdn.example.com/segment-1.m4s'
    missing_url = base_url + 'segment-2.m4s'

    info_dict = {
        'fragment_base_url': base_url,
        'fragments': [
            {'path': 'init.mp4'},
            {'url': retry_url},
            {'path': 'segment-2.m4s'},
        ],
    }

    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    attempts = {}
    appended = []
    retries = []
    skipped = []
    finished = []

    def prepare(ctx):
        assert ctx['filename'] == 'output.mp4'
        assert ctx

# Generated at 2026-10-25 04:43:28.425540
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    fd = DashSegmentsFD(MagicMock(), {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare)
    fd._download_fragment = Mock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    assert fd.real_download('output.mp4', info_dict) is True

    prepare_ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert prepare_ctx['filename'] == 'output.mp4'
    assert prepare_ctx['total_frags'] == 2

    download_calls = fd._download_fragment.call_args_list
    assert [call[0][1] for call in download_calls] == [
        'https://cdn.example.com/init.mp4',
        'https://example.com/video/segment-1.m4s',
    ]
    assert all(call[0][2] is info_dict for call in download_calls)

    assert [
        call[0][1] for call in fd._append_fragment.call_args_list
    ] == [
        b'initialization segment',
        b'media segment',
    ]

    fd._finish_frag_download.assert_called_once_with(prepare_ctx)

# Generated at 2026-10-25 04:43:30.988935
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:43:33.405682
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:43:35.819976
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:43:38.234957
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:43:40.769506
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():downloaded_urls = []

# Generated at 2026-10-25 04:43:42.096910
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:43:43.491314
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:43:44.822976
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:43:46.151830
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:44:05.392811
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    # real_download expects this method to initialize fragment_index.
    fd._prepare_and_start_frag_download = Mock(
        side_effect=lambda ctx: ctx.update(fragment_index=0))
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()

    first_url = 'https://example.test/video/init.m4s'
    second_url = 'https://example.test/video/segment-1.m4s'

    retry_error = compat_urllib_error.HTTPError(
        first_url, 404, 'Not Found', {}, None)

    fd._download_fragment = Mock(side_effect=[
        retry_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.test/video/',
        'fragments': [
            {'url': first_url},
            {'path': 'segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    assert fd._download_fragment.call_args_list == [
        call(ctx, first_url, info_dict),
        call(ctx, first_url, info_dict),
        call(ctx, second_url, info_dict),
    ]
    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 1, 1, 1)
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 04:44:06.825014
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:44:24.234360
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    fd._download_fragment.assert_has_calls([
        call(
            ctx,
            'https://cdn.example.com/init.mp4',
            info_dict,
        ),
        call(
            ctx,
            'https://example.com/media/segment-1.m4s',
            info_dict,
        ),
    ])

    fd._append_fragment.assert_has_calls([
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ])

    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 04:44:26.651907
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:44:29.067470
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:44:31.482007
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:44:33.896124
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:44:36.310463
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:44:38.725222
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:45:24.651411
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:45:27.406105
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():downloaded_urls = []

# Generated at 2026-10-25 04:45:49.942900
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import MagicMock, call

    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
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
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]

    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 04:46:02.509647
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    class TestDashSegmentsFD(DashSegmentsFD):
        def __init__(self):
            self.params = {}
            self.downloaded_urls = []
            self.appended_fragments = []
            self.finished = False

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0

        def _download_fragment(self, ctx, fragment_url, info_dict):
            self.downloaded_urls.append(fragment_url)
            return True, ('content:%s' % fragment_url).encode('utf-8')

        def _append_fragment(self, ctx, fragment_content):
            self.appended_fragments.append(fragment_content)
            ctx['fragment_index'] += 1

        def _finish_frag_download(self, ctx):
            self.finished = True

    downloader = TestDashSegmentsFD()
    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'segment-1.m4s'},
            {'url': 'https://cdn.example.com/segment-2.m4s'},
        ],
    }

    assert downloader.real_download('output.mp4', info_dict) is True
    assert downloader.downloaded_urls == [
        'https://example.com/media/segment-1.m4s',
        'https://cdn.example.com/segment-2.m4s',
    ]
    assert downloader.appended_fragments == [
        b'content:https://example.com/media/segment-1.m4s',
        b'content:https://cdn.example.com/segment-2.m4s',
    ]
    assert downloader.finished is True

# Generated at 2026-10-25 04:46:03.945680
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:46:05.275067
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:46:06.674773
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:46:08.071189
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:46:09.417256
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:46:34.491151
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    class FakeDashSegmentsFD(DashSegmentsFD):
        def __init__(self):
            self.params = {
                'fragment_retries': 0,
                'skip_unavailable_fragments': True,
            }
            self.download_calls = []
            self.appended_fragments = []
            self.prepared_ctx = None
            self.finished_ctx = None

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0
            self.prepared_ctx = ctx

        def _download_fragment(self, ctx, fragment_url, info_dict):
            self.download_calls.append((ctx, fragment_url, info_dict))
            return True, fragment_url.encode('utf-8')

        def _append_fragment(self, ctx, fragment_content):
            self.appended_fragments.append(fragment_content)
            ctx['fragment_index'] += 1

        def _finish_frag_download(self, ctx):
            self.finished_ctx = ctx

    fd = FakeDashSegmentsFD()
    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert fd.prepared_ctx['filename'] == 'output.mp4'
    assert fd.prepared_ctx['total_frags'] == 2
    assert fd.prepared_ctx['fragment_index'] == 2

    assert [call[1] for call in fd.download_calls] == [
        'https://example.com/video/init.mp4',
        'https://cdn.example.com/segment-1.m4s',
    ]
    assert all(call[0] is fd.prepared_ctx for call in fd.download_calls)
    assert all(call[2] is info_dict for call in fd.download_calls)

    assert fd.appended_fragments == [
        b'https://example.com/video/init.mp4',
        b'https://cdn.example.com/segment-1.m4s',
    ]
    assert fd.finished_ctx is fd.prepared_ctx

# Generated at 2026-10-25 04:46:36.919555
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:46:39.520535
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:46:41.931971
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:46:44.346812
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:46:46.762522
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:46:53.492855
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():params = {'test': True}

# Generated at 2026-10-25 04:47:11.657180
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/media/init.mp4',
        404,
        'Not Found',
        None,
        None,
    )

    # The first fragment fails once and succeeds on retry. The second
    # fragment succeeds immediately.
    fd._download_fragment = Mock(side_effect=[
        http_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._download_fragment.assert_has_calls([
        call(
            {
                'filename': 'output.mp4',
                'total_frags': 2,
                'fragment_index': 0,
            },
            'https://example.com/media/init.mp4',
            info_dict,
        ),
        call(
            {
                'filename': 'output.mp4',
                'total_frags': 2,
                'fragment_index': 0,
            },
            'https://example.com/media/init.mp4',
            info_dict,
        ),
        call(
            {
                'filename': 'output.mp4',
                'total_frags': 2,
                'fragment_index': 0,
            },
            'https://cdn.example.com/segment-1.m4s',
            info_dict,
        ),
    ])

    fd.report_retry_fragment.assert_called_once_with(http_error, 1, 1, 1)

    assert [c.args[1] for c in fd._append_fragment.call_args_list] == [
        b'initialization segment',
        b'media segment',
    ]

    fd._finish_frag_download.assert_called_once()
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()

# Generated at 2026-10-25 04:47:36.159553
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    prepared = []
    downloaded_urls = []
    appended = []
    retries = []
    finished = []

    def prepare(ctx):
        ctx['fragment_index'] = 0
        prepared.append(ctx.copy())

    attempts = {}

    def download_fragment(ctx, fragment_url, info_dict):
        downloaded_urls.append(fragment_url)
        attempts[fragment_url] = attempts.get(fragment_url, 0) + 1

        # Verify that an HTTP failure is retried.
        if fragment_url.endswith('segment-1.m4s') and attempts[fragment_url] == 1:
            raise compat_urllib_error.HTTPError(
                fragment_url, 404, 'Not Found', {}, None)

        return True, ('content:%s' % fragment_url).encode('utf-8')

    def append_fragment(ctx, content):
        appended.append(content)
        ctx['fragment_index'] += 1

    def finish(ctx):
        finished.append(ctx.copy())

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd.report_retry_fragment = lambda *args: retries.append(args)
    fd._finish_frag_download = finish

    base_url = 'https://example.com/video/'
    segment_url = 'https://cdn.example.com/segment-1.m4s'
    info_dict = {
        'fragment_base_url': base_url,
        'fragments': [
            {'path': 'init.mp4'},
            {'url': segment_url},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    assert prepared == [{
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }]
    assert downloaded_urls == [
        'https://example.com/video/init.mp4',
        segment_url,
        segment_url,
    ]
    assert appended == [
        b'content:https://example.com/video/init.mp4',
        b'content:https://cdn.example.com/segment-1.m4s',
    ]
    assert len(retries) == 1

# Generated at 2026-10-25 04:47:38.576057
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:47:40.991077
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:47:43.407991
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:47:45.827366
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:47:48.442863
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:47:50.860434
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:47:53.272117
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:47:55.689862
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:47:58.102577
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:00.516820
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:02.942244
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:05.371651
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:07.786713
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:10.212418
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:12.624981
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:15.040807
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:17.471914
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:19.882457
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:22.298706
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:24.711949
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:27.129048
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:29.546134
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:31.961028
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:34.375012
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:48:37.874301
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:40.289537
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:42.705667
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:45.118698
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:47.533181
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:48:49.947243
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:49:15.138366
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():params = {}

# Generated at 2026-10-25 04:49:34.256664
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
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

    retry_error = compat_urllib_error.HTTPError(
        'https://example.com/media/init.m4s',
        404,
        'Not Found',
        {},
        None,
    )

    fd._download_fragment = Mock(side_effect=[
        retry_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/media/init.m4s', info_dict),
        call(ctx, 'https://example.com/media/init.m4s', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 1, 1, 1
    )
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()

# Generated at 2026-10-25 04:49:48.650580
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
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

    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    fd._download_fragment.assert_has_calls([
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
    ])

    fd._append_fragment.assert_has_calls([
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ])
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 04:49:50.070943
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:49:51.415487
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:49:52.846630
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:49:54.191241
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:49:55.609677
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:15.060446
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    events = []
    downloaded_urls = []

    def prepare(ctx):
        events.append('prepare')
        assert ctx['filename'] == 'output.mp4'
        assert ctx['total_frags'] == 2
        # Normally initialized by FragmentFD's preparation method.
        ctx['fragment_index'] = 0

    def download_fragment(ctx, fragment_url, passed_info_dict):
        events.append(('download', fragment_url))
        assert passed_info_dict is info_dict
        downloaded_urls.append(fragment_url)
        return True, ('content:%s' % fragment_url).encode('utf-8')

    def append_fragment(ctx, content):
        events.append(('append', content))

    def finish(ctx):
        events.append('finish')

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish

    assert fd.real_download('output.mp4', info_dict) is True

    assert downloaded_urls == [
        'https://cdn.example.com/init.mp4',
        'https://example.com/media/segment-1.m4s',
    ]
    assert events == [
        'prepare',
        ('download', 'https://cdn.example.com/init.mp4'),
        ('append', b'content:https://cdn.example.com/init.mp4'),
        ('download', 'https://example.com/media/segment-1.m4s'),
        ('append', b'content:https://example.com/media/segment-1.m4s'),
        'finish',
    ]

# Generated at 2026-10-25 04:50:16.485564
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:17.872003
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:37.311991
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import MagicMock, call

    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

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

    retry_error = compat_urllib_error.HTTPError(
        'https://example.com/video/media.m4s',
        404,
        'Not Found',
        None,
        None,
    )

    fd._download_fragment = MagicMock(side_effect=[
        (True, b'initialization segment'),
        retry_error,
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://example.com/video/init.m4s'},
            {'path': 'media.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.m4s', info_dict),
        call(ctx, 'https://example.com/video/media.m4s', info_dict),
        call(ctx, 'https://example.com/video/media.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 2, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-25 04:50:38.642469
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:40.034309
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:41.476005
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:42.909187
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:44.241969
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:45.644638
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:52.375568
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:53.726795
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None, {})

    # Correct type and FD name
    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'

    # Params are stored on the instance
    assert fd.params == {}

# Generated at 2026-10-25 04:50:56.275530
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:50:58.696618
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:51:01.114737
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:51:03.531104
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:51:05.946325
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:51:08.365230
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:51:10.792812
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:51:13.210219
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:51:15.630015
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-25 04:51:18.050718
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:51:20.467440
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-25 04:51:22.885870
# Unit test for method real_download of class DashSegmentsFD