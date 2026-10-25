

# Generated at 2026-10-24 23:05:51.652929
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(Mock(), {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

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
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example.com/init.mp4', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
    ]

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:06:09.282252
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    downloaded_urls = []
    appended_content = []
    state = {}

    def prepare(ctx):
        ctx['fragment_index'] = 0
        state['prepared_ctx'] = ctx

    def download_fragment(ctx, url, info_dict):
        downloaded_urls.append(url)
        return True, ('content:%s' % url).encode('utf-8')

    def append_fragment(ctx, content):
        appended_content.append(content)
        ctx['fragment_index'] += 1

    def finish(ctx):
        state['finished_ctx'] = ctx

    def unexpected_call(*args, **kwargs):
        raise AssertionError('Unexpected error or retry')

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish
    fd.report_retry_fragment = unexpected_call
    fd.report_skip_fragment = unexpected_call
    fd.report_error = unexpected_call

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
    ]
    assert appended_content == [
        b'content:https://example.com/video/init.mp4',
        b'content:https://cdn.example.com/segment-1.m4s',
    ]

    assert state['prepared_ctx']['filename'] == 'output.mp4'
    assert state['prepared_ctx']['total_frags'] == 2
    assert state['finished_ctx']['fragment_index'] == 2

# Generated at 2026-10-24 23:06:11.801271
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:06:14.218887
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:06:16.807425
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import Mock, call


# Generated at 2026-10-24 23:06:26.796948
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True, 'fragment_retries': 2}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader._progress_hooks
    assert downloader.report_progress in downloader._progress_hooks

# Generated at 2026-10-24 23:06:36.315456
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = Mock()
    params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert downloader._ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader.report_progress in downloader._progress_hooks

# Generated at 2026-10-24 23:06:45.383852
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

# Generated at 2026-10-24 23:07:02.650299
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(MagicMock(), {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    appended_fragments = []

    def prepare(ctx):
        ctx['fragment_index'] = 0

    def append(ctx, content):
        appended_fragments.append(content)
        ctx['fragment_index'] += 1

    fd._prepare_and_start_frag_download = MagicMock(side_effect=prepare)
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = MagicMock(side_effect=append)
    fd._finish_frag_download = MagicMock()

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/video/segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]

    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 2,
    }

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/video/segment-1.m4s', info_dict),
    ]
    assert appended_fragments == [
        b'initialization segment',
        b'media segment',
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:07:05.071280
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:07:07.486824
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:07:10.031432
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:07:12.452432
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:07:14.869753
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:46.586386
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():fd = DashSegmentsFD.__new__(DashSegmentsFD)

# Generated at 2026-10-24 23:08:54.882301
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    params = {'test': True}
    downloader = object()

    fd = DashSegmentsFD(downloader, params)

    assert isinstance(fd, DashSegmentsFD)
    assert isinstance(fd, FragmentFD)
    assert fd.ydl is downloader
    assert fd.params is params
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:09:15.854877
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    # Normally initialized by _prepare_and_start_frag_download.
    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(side_effect=prepare)
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()
    fd.report_retry_fragment = MagicMock()
    fd.report_skip_fragment = MagicMock()
    fd.report_error = MagicMock()

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/init.m4s', 404, 'Not Found', None, None)

    # The first fragment fails once, then succeeds on retry.
    fd._download_fragment = MagicMock(side_effect=[
        http_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/media-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    fd._prepare_and_start_frag_download.assert_called_once_with(ANY)
    prepared_ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert prepared_ctx['filename'] == 'output.mp4'
    assert prepared_ctx['total_frags'] == 2

    fd._download_fragment.assert_has_calls([
        call(ANY, 'https://example.com/video/init.m4s', info_dict),
        call(ANY, 'https://example.com/video/init.m4s', info_dict),
        call(ANY, 'https://cdn.example.com/media-1.m4s', info_dict),
    ])

    fd.report_retry_fragment.assert_called_once_with(http_error, 1, 1, 1)
    assert fd._append_fragment.call_args_list == [
        call(ANY, b'initialization segment'),
        call(ANY, b'media segment'),
    ]
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ANY)

# Generated at 2026-10-24 23:09:24.457835
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyYDL:
        pass

    ydl = DummyYDL()
    params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params == params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:09:31.729451
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = Mock()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader._progress_hooks == []

# Generated at 2026-10-24 23:09:48.930749
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
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
            {'url': 'https://cdn.example.com/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example.com/init.m4s', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:10:09.413413
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    fd._prepare_and_start_frag_download = Mock(
        side_effect=lambda ctx: ctx.update(fragment_index=0))
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    base_url = 'https://cdn.example.com/video/'
    retry_url = base_url + 'segment-1.m4s'
    skipped_url = base_url + 'segment-2.m4s'

    info_dict = {
        'fragment_base_url': base_url,
        'fragments': [
            {'path': 'init.m4s'},
            {'url': retry_url},
            {'url': skipped_url},
        ],
    }

    attempts = defaultdict(int)

    def download_fragment(ctx, fragment_url, passed_info_dict):
        assert passed_info_dict is info_dict
        attempts[fragment_url] += 1

        if fragment_url == retry_url and attempts[fragment_url] == 1:
            raise compat_urllib_error.HTTPError(
                fragment_url, 404, 'Not Found', {}, None)

        if fragment_url == skipped_url:
            raise compat_urllib_error.HTTPError(
                fragment_url, 404, 'Not Found', {}, None)

        return True, fragment_url.encode('utf-8')

    fd._download_fragment = Mock(side_effect=download_fragment)

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    init_url = base_url + 'init.m4s'
    assert attempts == {
        init_url: 1,
        retry_url: 2,
        skipped_url: 2,
    }

    assert [mock_call.args[1] for mock_call in fd._append_fragment.call_args_list] == [
        init_url.encode('utf-8'),
        retry_url.encode('utf-8'),
    ]

    assert fd.report_retry_fragment.call_count == 2
    assert [
        mock_call.args[1:] for mock_call
        in fd.report_retry_fragment.call_args_list
    ] == [
        (2, 1, 1),
        (3, 1, 1),
    ]

    fd.report_skip_fragment.assert_called_once_with(3)
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(
        fd._prepare_and_start_frag_download.call_args.args[0])

# Generated at 2026-10-24 23:10:17.446189
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    downloader = Mock()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': False,
    }

    fd = DashSegmentsFD(downloader, params)

    assert isinstance(fd, DashSegmentsFD)
    assert isinstance(fd, FragmentFD)
    assert fd._ydl is downloader
    assert fd.params is params
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:10:38.530967
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import Mock, call

    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
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
            {'url': 'https://cdn.example.com/init.m4s'},
            {'path': 'segment-1.m4s'},
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
        call(ctx, 'https://cdn.example.com/init.m4s', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:10:46.624006
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:10:53.721130
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params == params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:11:11.874999
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
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

    http_error = compat_urllib_error.HTTPError(
        'https://cdn.example/media/segment-1.m4s',
        404,
        'Not Found',
        None,
        None,
    )

    # The initialization fragment succeeds. The media fragment fails once
    # with an HTTP error and then succeeds when retried.
    fd._download_fragment = MagicMock(side_effect=[
        (True, b'initialization fragment'),
        http_error,
        (True, b'media fragment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://cdn.example/media/',
        'fragments': [
            {'url': 'https://cdn.example/media/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example/media/init.mp4', info_dict),
        call(ctx, 'https://cdn.example/media/segment-1.m4s', info_dict),
        call(ctx, 'https://cdn.example/media/segment-1.m4s', info_dict),
    ]

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization fragment'),
        call(ctx, b'media fragment'),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        http_error, 2, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:11:20.697209
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    downloader = object()
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

# Generated at 2026-10-24 23:11:29.795038
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    downloader = object()
    params = {
        'test': True,
        'fragment_retries': 2,
        'skip_unavailable_fragments': False,
    }

    fd = DashSegmentsFD(downloader, params)

    assert isinstance(fd, DashSegmentsFD)
    assert isinstance(fd, FragmentFD)
    assert fd.ydl is downloader
    assert fd.params == params
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:11:37.576571
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = Mock()
    params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:11:49.867710
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
            {'path': 'segment-2.m4s'},
        ],
    }

    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0

    fragment_contents = [
        (True, b'initialization segment'),
        (True, b'first segment'),
        (True, b'second segment'),
    ]

    with patch.object(
            fd, '_prepare_and_start_frag_download',
            side_effect=prepare_download) as prepare_mock, \
            patch.object(
                fd, '_download_fragment',
                side_effect=fragment_contents) as download_mock, \
            patch.object(fd, '_append_fragment') as append_mock, \
            patch.object(fd, '_finish_frag_download') as finish_mock:

        result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = prepare_mock.call_args.args[0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 3,
        'fragment_index': 0,
    }

    assert download_mock.call_args_list == [
        call(ctx, 'https://example.com/media/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
        call(ctx, 'https://example.com/media/segment-2.m4s', info_dict),
    ]

    assert append_mock.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'first segment'),
        call(ctx, b'second segment'),
    ]

    finish_mock.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:11:58.672671
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': False,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert downloader.ydl is ydl
    assert downloader.params == params
    assert downloader.FD_NAME == 'dashsegments'
    assert isinstance(downloader, FragmentFD)

# Generated at 2026-10-24 23:12:07.513318
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

# Generated at 2026-10-24 23:12:26.115384
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    try:
        from unittest import mock
    except ImportError:
        import mock

    downloader = DashSegmentsFD.__new__(DashSegmentsFD)
    downloader.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    def prepare(ctx):
        ctx['fragment_index'] = 0

    downloader._prepare_and_start_frag_download = mock.Mock(side_effect=prepare)
    downloader._append_fragment = mock.Mock()
    downloader._finish_frag_download = mock.Mock()
    downloader.report_retry_fragment = mock.Mock()
    downloader.report_skip_fragment = mock.Mock()
    downloader.report_error = mock.Mock()

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.mp4',
        404,
        'Not Found',
        {},
        None,
    )

    downloader._download_fragment = mock.Mock(side_effect=[
        http_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = downloader.real_download('output.mp4', info_dict)

    assert result is True

    ctx = downloader._prepare_and_start_frag_download.call_args[0][0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    assert downloader._download_fragment.call_args_list == [
        mock.call(
            ctx,
            'https://example.com/video/init.mp4',
            info_dict,
        ),
        mock.call(
            ctx,
            'https://example.com/video/init.mp4',
            info_dict,
        ),
        mock.call(
            ctx,
            'https://cdn.example.com/segment-1.m4s',
            info_dict,
        ),
    ]

    downloader.report_retry_fragment.assert_called_once_with(
        http_error, 1, 1, 1)
    assert downloader._append_fragment.call_args_list == [
        mock.call(ctx, b'initialization segment'),
        mock.call(ctx, b'media segment'),
    ]
    downloader._finish_frag_download.assert_called_once_with(ctx)
    downloader.report_skip_fragment.assert_not_called()
    downloader.report_error.assert_not_called()

# Generated at 2026-10-24 23:12:38.595736
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

# Generated at 2026-10-24 23:12:47.208290
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:13:00.522505
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    params = {
        'fragment_retries': 2,
        'skip_unavailable_fragments': False,
    }

    downloader = DashSegmentsFD(None, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is None
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader._progress_hooks == []

# Generated at 2026-10-24 23:13:24.279870
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    class RecordingDashSegmentsFD(DashSegmentsFD):
        def __init__(self):
            self.params = {
                'fragment_retries': 0,
                'skip_unavailable_fragments': True,
            }
            self.prepared_ctx = None
            self.download_calls = []
            self.appended_fragments = []
            self.finished_ctx = None

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0
            self.prepared_ctx = ctx

        def _download_fragment(self, ctx, fragment_url, info_dict):
            self.download_calls.append((fragment_url, info_dict))
            return True, fragment_url.encode('utf-8')

        def _append_fragment(self, ctx, fragment_content):
            self.appended_fragments.append(fragment_content)
            ctx['fragment_index'] += 1

        def _finish_frag_download(self, ctx):
            self.finished_ctx = ctx

    fd = RecordingDashSegmentsFD()
    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert fd.prepared_ctx['filename'] == 'output.mp4'
    assert fd.prepared_ctx['total_frags'] == 2

    assert [call[0] for call in fd.download_calls] == [
        'https://cdn.example.com/init.mp4',
        'https://example.com/media/segment-1.m4s',
    ]
    assert all(call[1] is info_dict for call in fd.download_calls)

    assert fd.appended_fragments == [
        b'https://cdn.example.com/init.mp4',
        b'https://example.com/media/segment-1.m4s',
    ]
    assert fd.finished_ctx is fd.prepared_ctx
    assert fd.finished_ctx['fragment_index'] == 2

# Generated at 2026-10-24 23:13:48.345845
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'url': 'https://example.com/media/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    downloaded_urls = []
    appended_fragments = []
    retry_reports = []
    finished_contexts = []
    segment_attempts = {'count': 0}

    def prepare(ctx):
        ctx['fragment_index'] = 0

    def download_fragment(ctx, fragment_url, passed_info_dict):
        assert passed_info_dict is info_dict
        downloaded_urls.append(fragment_url)

        if fragment_url.endswith('segment-1.m4s'):
            segment_attempts['count'] += 1
            if segment_attempts['count'] == 1:
                raise compat_urllib_error.HTTPError(
                    fragment_url, 404, 'Not Found', None, None)

        return True, fragment_url.encode('utf-8')

    def append_fragment(ctx, content):
        appended_fragments.append(content)
        ctx['fragment_index'] += 1

    def report_retry_fragment(err, frag_index, count, retries):
        retry_reports.append((err.code, frag_index, count, retries))

    def finish(ctx):
        finished_contexts.append(dict(ctx))

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd.report_retry_fragment = report_retry_fragment
    fd._finish_frag_download = finish

    assert fd.real_download('output.mp4', info_dict) is True

    assert downloaded_urls == [
        'https://example.com/media/init.mp4',
        'https://example.com/media/segment-1.m4s',
        'https://example.com/media/segment-1.m4s',
    ]
    assert appended_fragments == [
        b'https://example.com/media/init.mp4',
        b'https://example.com/media/segment-1.m4s',
    ]
    assert retry_reports == [(404, 2, 1, 1)]

# Generated at 2026-10-24 23:14:06.467705
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.mp4',
        404,
        'Not Found',
        {},
        None,
    )

    # The first attempt fails, its retry succeeds, and then the second
    # fragment is downloaded normally.
    fd._download_fragment = Mock(side_effect=[
        http_error,
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

    assert fd.real_download('output.mp4', info_dict) is True

    requested_urls = [
        mock_call.args[1]
        for mock_call in fd._download_fragment.call_args_list
    ]
    assert requested_urls == [
        'https://example.com/video/init.mp4',
        'https://example.com/video/init.mp4',
        'https://cdn.example.com/media-1.m4s',
    ]

    fd.report_retry_fragment.assert_called_once_with(http_error, 1, 1, 1)
    assert fd._append_fragment.call_args_list == [
        call(fd._prepare_and_start_frag_download.call_args.args[0],
             b'initialization segment'),
        call(fd._prepare_and_start_frag_download.call_args.args[0],
             b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once()
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()

# Generated at 2026-10-24 23:14:14.249228
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = Mock()
    params = {
        'test': True,
        'fragment_retries': 2,
        'skip_unavailable_fragments': False,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:14:26.346988
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import Mock, call

    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
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
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(
            ctx,
            'https://example.com/video/init.m4s',
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

# Generated at 2026-10-24 23:14:51.220026
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    info_dict = {
        'fragment_base_url': 'https://cdn.example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/video/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    download_attempts = {}
    appended_fragments = []
    retry_reports = []
    skipped_fragments = []
    errors = []
    finished = []

    def prepare(ctx):
        assert ctx['filename'] == 'output.mp4'

# Generated at 2026-10-24 23:14:59.376523
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:15:16.687545
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    fd._prepare_and_start_frag_download = Mock(
        side_effect=lambda ctx: ctx.update(fragment_index=0))
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

    # The first fragment succeeds. The second fails once and then succeeds.
    fd._download_fragment = Mock(side_effect=[
        (True, b'initialization segment'),
        retry_error,
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]

    fd._download_fragment.assert_has_calls([
        call(ctx, 'https://cdn.example.com/init.m4s', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
    ])
    fd._append_fragment.assert_has_calls([
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ])
    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 2, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:15:19.111427
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:15:21.637332
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:15:24.056236
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:15:26.475749
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:15:28.891722
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:15:31.475432
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import Mock, call


# Generated at 2026-10-24 23:15:40.267633
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader._progress_hooks == []
    assert downloader.FD_NAME == 'dashsegments'