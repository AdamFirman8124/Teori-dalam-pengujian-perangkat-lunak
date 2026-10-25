

# Generated at 2026-10-24 05:33:42.763092
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True, 'fragment_retries': 2}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 05:33:58.326324
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    downloader = DashSegmentsFD.__new__(DashSegmentsFD)
    downloader.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0

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
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = downloader.real_download('output.mp4', info_dict)

    assert result is True

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert downloader._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ]
    assert downloader._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    downloader._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 05:34:29.577786
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:34:31.992925
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:34:34.418147
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:34:36.833877
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:34:39.249036
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:34:52.086916
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:35:04.881218
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    try:
        from unittest.mock import Mock, call
    except ImportError:
        from mock import Mock, call

    downloader = DashSegmentsFD(Mock(), {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare(ctx):
        ctx['fragment_index'] = 0

    downloader._prepare_and_start_frag_download = Mock(side_effect=prepare)
    downloader._download_fragment = Mock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    downloader._append_fragment = Mock()
    downloader._finish_frag_download = Mock()

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    assert downloader.real_download('output.mp4', info_dict) is True

    downloader._prepare_and_start_frag_download.assert_called_once()
    downloader._download_fragment.assert_has_calls([
        call(
            downloader._prepare_and_start_frag_download.call_args[0][0],
            'https://cdn.example.com/init.mp4',
            info_dict),
        call(
            downloader._prepare_and_start_frag_download.call_args[0][0],
            'https://example.com/video/segment-1.m4s',
            info_dict),
    ])
    downloader._append_fragment.assert_has_calls([
        call(
            downloader._prepare_and_start_frag_download.call_args[0][0],
            b'initialization segment'),
        call(
            downloader._prepare_and_start_frag_download.call_args[0][0],
            b'media segment'),
    ])
    downloader._finish_frag_download.assert_called_once_with(
        downloader._prepare_and_start_frag_download.call_args[0][0])

# Generated at 2026-10-24 05:35:28.031174
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }
    downloader = DashSegmentsFD(None, params)

    filename = 'output.mp4'
    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://example.com/video/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/video/segment-1.m4s',
        404,
        'Not Found',
        {},
        None,
    )

    downloader._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    downloader._download_fragment = MagicMock(side_effect=[
        (True, b'initialization fragment'),
        http_error,
        (True, b'media fragment'),
    ])
    downloader._append_fragment = MagicMock()
    downloader._finish_frag_download = MagicMock()
    downloader.report_retry_fragment = MagicMock()
    downloader.report_skip_fragment = MagicMock()
    downloader.report_error = MagicMock()

    result = downloader.real_download(filename, info_dict)

    assert result is True

    expected_ctx = {
        'filename': filename,
        'total_frags': 2,
        'fragment_index': 0,
    }

    downloader._prepare_and_start_frag_download.assert_called_once_with(
        expected_ctx)
    downloader._download_fragment.assert_has_calls([
        call(
            expected_ctx,
            'https://example.com/video/init.mp4',
            info_dict,
        ),
        call(
            expected_ctx,
            'https://example.com/video/segment-1.m4s',
            info_dict,
        ),
        call(
            expected_ctx,
            'https://example.com/video/segment-1.m4s',
            info_dict,
        ),
    ])
    downloader._append_fragment.assert_has_calls([
        call(expected_ctx, b'initialization fragment'),
        call(expected_ctx, b'media fragment'),
    ])
    downloader.report_retry_fragment.assert_called_once_with(
        http_error, 2, 1, 1)
    downloader.report_skip_fragment.assert_not_called()
    downloader.report_error.assert_not_called()
    downloader._finish_frag_download.assert_called_once_with(expected_ctx)

# Generated at 2026-10-24 05:35:48.714105
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    info_dict = {
        'fragment_base_url': 'https://cdn.example.test/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://media.example.test/segment-1.m4s'},
            {'path': 'segment-2.m4s'},
        ],
    }

    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'init'),
        (True, b'segment-1'),
        (True, b'segment-2'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 3
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(
            ctx,
            'https://cdn.example.test/video/init.mp4',
            info_dict,
        ),
        call(
            ctx,
            'https://media.example.test/segment-1.m4s',
            info_dict,
        ),
        call(
            ctx,
            'https://cdn.example.test/video/segment-2.m4s',
            info_dict,
        ),
    ]

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'init'),
        call(ctx, b'segment-1'),
        call(ctx, b'segment-2'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 05:36:01.925101
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import MagicMock, call

    downloader = DashSegmentsFD.__new__(DashSegmentsFD)
    downloader.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    downloader._prepare_and_start_frag_download = MagicMock(
        side_effect=prepare_download)
    downloader._download_fragment = MagicMock(
        side_effect=[
            (True, b'initialization segment'),
            (True, b'media segment'),
        ])
    downloader._append_fragment = MagicMock()
    downloader._finish_frag_download = MagicMock()

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = downloader.real_download('output.mp4', info_dict)

    assert result is True

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }

    assert downloader._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example.com/init.mp4', info_dict),
        call(ctx, 'https://example.com/media/segment-1.m4s', info_dict),
    ]
    assert downloader._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    downloader._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 05:36:12.471612
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = MagicMock()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    fd = DashSegmentsFD(ydl, params)

    assert isinstance(fd, FragmentFD)
    assert fd.ydl is ydl
    assert fd.params is params
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 05:36:40.428788
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(Mock(), {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    # Normally this method initializes fragment_index in the context.
    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
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

    # First fragment succeeds. The second fails once and then succeeds.
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
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example.com/init.m4s', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
        call(ctx, 'https://example.com/video/segment-1.m4s', info_dict),
    ]

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd.report

# Generated at 2026-10-24 05:36:42.968020
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:36:57.016567
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():fd = DashSegmentsFD(None, {})

# Generated at 2026-10-24 05:37:28.025299
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:37:30.522427
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:37:32.937651
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:37:35.353350
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:37:37.768968
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:37:40.269441
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:37:42.681253
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:37:45.262949
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:37:51.800580
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():params = {'test': True, 'fragment_retries': 2}

# Generated at 2026-10-24 05:38:00.097537
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True, 'fragment_retries': 2}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 05:38:19.565672
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/init.mp4',
        404,
        'Not Found',
        {},
        None,
    )

    # The first fragment fails once and then succeeds. The second fragment
    # verifies fragment_base_url/path URL construction.
    fd._download_fragment = Mock(side_effect=[
        http_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'url': 'https://example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ANY, 'https://example.com/init.mp4', info_dict),
        call(ANY, 'https://example.com/init.mp4', info_dict),
        call(ANY, 'https://example.com/media/segment-1.m4s', info_dict),
    ]

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        http_error, 1, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 05:38:39.622207
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    downloaded = []
    appended = []
    finished = []

    def prepare(ctx):
        # Normally initialized by FragmentFD
        ctx['fragment_index'] = 0

    def download_fragment(ctx, fragment_url, info_dict):
        downloaded.append(fragment_url)
        return True, ('content:%s' % fragment_url).encode('utf-8')

    def append_fragment(ctx, content):
        appended.append(content)

    def finish(ctx):
        finished.append(ctx.copy())

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish

    info_dict = {
        'fragment_base_url': 'https://cdn.example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/video/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    assert downloaded == [
        'https://cdn.example.com/video/init.m4s',
        'https://cdn.example.com/video/segment-1.m4s',
    ]
    assert appended == [
        b'content:https://cdn.example.com/video/init.m4s',
        b'content:https://cdn.example.com/video/segment-1.m4s',
    ]
    assert len(finished) == 1
    assert finished[0]['filename'] == 'output.mp4'
    assert finished[0]['total_frags'] == 2

# Generated at 2026-10-24 05:38:42.039171
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:38:44.544094
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:38:54.712728
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:05.427762
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
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

# Generated at 2026-10-24 05:39:24.384738
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    prepared_contexts = []
    downloaded_urls = []
    appended_fragments = []
    finished_contexts = []

    def prepare(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0
        prepared_contexts.append(ctx)

    def download(ctx, fragment_url, info_dict):
        downloaded_urls.append(fragment_url)
        return True, ('content:%s' % fragment_url).encode('utf-8')

    def append(ctx, content):
        appended_fragments.append(content)

    def finish(ctx):
        finished_contexts.append(ctx)

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download
    fd._append_fragment = append
    fd._finish_frag_download = finish

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.mp4'},
            {'path': 'segment-1.m4s'},
            {'path': 'segment-2.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert len(prepared_contexts) == 1
    assert prepared_contexts[0]['filename'] == 'output.mp4'
    assert prepared_contexts[0]['total_frags'] == 3

    assert downloaded_urls == [
        'https://cdn.example.com/init.mp4',
        'https://example.com/video/segment-1.m4s',
        'https://example.com/video/segment-2.m4s',
    ]
    assert appended_fragments == [
        b'content:https://cdn.example.com/init.mp4',
        b'content:https://example.com/video/segment-1.m4s',
        b'content:https://example.com/video/segment-2.m4s',
    ]

    assert finished_contexts == prepared_contexts

# Generated at 2026-10-24 05:39:26.883092
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:29.301391
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:31.716087
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:34.130130
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:36.545341
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:38.959179
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:41.373427
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:43.789803
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:39:46.344317
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:40:00.109070
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
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
    assert downloader._progress_hooks == []

# Generated at 2026-10-24 05:40:09.447071
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
    assert fd._progress_hooks == []
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 05:40:26.942810
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    downloader = DashSegmentsFD(None, {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0

    with patch.object(
            downloader,
            '_prepare_and_start_frag_download',
            side_effect=prepare_download) as prepare_mock, \
            patch.object(
                downloader,
                '_download_fragment',
                side_effect=[
                    (True, b'initialization segment'),
                    (True, b'media segment'),
                ]) as download_mock, \
            patch.object(downloader, '_append_fragment') as append_mock, \
            patch.object(downloader, '_finish_frag_download') as finish_mock:

        result = downloader.real_download('output.mp4', info_dict)

    assert result is True

    prepare_mock.assert_called_once()
    ctx = prepare_mock.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert download_mock.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ]
    assert append_mock.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    finish_mock.assert_called_once_with(ctx)

# Generated at 2026-10-24 05:40:29.433664
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:40:31.849021
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:40:34.264205
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:40:36.679457
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:40:39.094373
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:40:41.506393
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:40:43.922227
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:40:46.336267
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:40:48.750971
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:40:51.166427
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:40:53.582702
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:40:55.994924
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:41:20.125936
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:41:27.661091
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():params = {'test': True}

# Generated at 2026-10-24 05:41:46.605312
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import Mock, call

    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    http_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.mp4',
        404,
        'Not Found',
        None,
        None,
    )

    # Fail the first request, then succeed on retry and on the next fragment.
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

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
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
    fd.report_retry_fragment.assert_called_once_with(http_error, 1, 1, 1)
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()

# Generated at 2026-10-24 05:41:49.021254
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:41:51.437147
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:41:53.850844
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:41:56.264104
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:41:58.677056
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:04.679378
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():params = {'test': True}

# Generated at 2026-10-24 05:42:12.278014
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
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

# Generated at 2026-10-24 05:42:23.377276
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
    assert fd._progress_hooks == []

# Generated at 2026-10-24 05:42:35.722467
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare)
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
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 05:42:38.249764
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:40.663527
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:43.079608
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:45.493912
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:47.907839
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:50.320723
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:53.277624
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:55.689975
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:42:58.103918
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:43:00.522425
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:43:02.941965
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:43:05.356432
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 05:43:07.775770
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:10.197853
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:12.611728
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:15.027287
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:17.440072
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:19.852166
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:22.268045
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:24.693279
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:27.111248
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:29.524223
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:31.941610
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 05:43:34.361950
# Unit test for method real_download of class DashSegmentsFD