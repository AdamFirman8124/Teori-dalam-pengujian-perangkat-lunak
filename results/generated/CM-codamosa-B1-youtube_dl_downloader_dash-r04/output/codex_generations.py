

# Generated at 2026-10-24 23:03:38.140102
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyYDL:
        pass

    ydl = DummyYDL()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:03:57.390644
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    class TestDashSegmentsFD(DashSegmentsFD):
        def __init__(self):
            self.params = {
                'fragment_retries': 1,
                'skip_unavailable_fragments': True,
            }
            self.download_results = []
            self.requested_urls = []
            self.appended_fragments = []
            self.retries = []
            self.errors = []
            self.finished = False

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0

        def _download_fragment(self, ctx, fragment_url, info_dict):
            self.requested_urls.append(fragment_url)
            result = self.download_results.pop(0)
            if isinstance(result, Exception):
                raise result
            return result

        def _append_fragment(self, ctx, fragment_content):
            self.appended_fragments.append(fragment_content)

        def report_retry_fragment(
                self, err, frag_index, count, fragment_retries):
            self.retries.append((frag_index, count, fragment_retries))

        def report_skip_fragment(self, frag_index):
            raise AssertionError('Fragment %d was unexpectedly skipped' % frag_index)

        def report_error(self, message):
            self.errors.append(message)

        def _finish_frag_download(self, ctx):
            self.finished = True

    fd = TestDashSegmentsFD()
    http_error = compat_urllib_error.HTTPError(
        'https://example.com/media/init.m4s',
        404,
        'Not Found',
        {},
        None,
    )
    fd.download_results = [
        http_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ]

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True
    assert fd.requested_urls == [
        'https://example.com/media/init.m4s',
        'https://example.com/media/init.m4s',
        'https://cdn.example.com/segment-1.m4s',
    ]
    assert fd.appended_fragments == [
        b'initialization segment',
        b'media segment',
    ]
    assert fd.retries == [(1, 1, 1)]
    assert fd.errors == []
    assert fd.finished is True

# Generated at 2026-10-24 23:03:59.813033
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:04:02.230494
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:04:04.649813
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:04:32.512088
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:04:46.848568
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():fd = object.__new__(DashSegmentsFD)

# Generated at 2026-10-24 23:04:49.272360
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:04:51.842218
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:04:54.259985
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:04:56.691764
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:04:59.111698
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:05:01.707459
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:05:04.126073
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:05:06.546079
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:05:08.962405
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:05:11.380510
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:05:13.807069
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:05:16.227529
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:06:03.728863
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import Mock, call


# Generated at 2026-10-24 23:06:06.264793
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:06:08.683687
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:06:11.098832
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:06:13.517831
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:06:16.119428
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import Mock, call


# Generated at 2026-10-24 23:06:26.793341
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert downloader._ydl is ydl
    assert downloader.params == params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader._progress_hooks == []

# Generated at 2026-10-24 23:06:43.892633
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    http_error = compat_urllib_error.HTTPError(
        'https://cdn.example.com/init.m4s',
        404,
        'Not Found',
        None,
        None,
    )

    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare)
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

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ANY, 'https://cdn.example.com/init.m4s', info_dict),
        call(ANY, 'https://cdn.example.com/init.m4s', info_dict),
        call(ANY, 'https://example.com/media/segment-1.m4s', info_dict),
    ]

    fd.report_retry_fragment.assert_called_once_with(http_error, 1, 1, 1)
    assert fd._append_fragment.call_args_list == [
        call(ANY, b'initialization segment'),
        call(ANY, b'media segment'),
    ]

    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:07:08.459692
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    info_dict = {
        'fragment_base_url': 'https://cdn.example.com/video/',
        'fragments': [
            {'url': 'https://cdn.example.com/video/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    http_error = compat_urllib_error.HTTPError(
        'https://cdn.example.com/video/init.m4s',
        404,
        'Not Found',
        None,
        None,
    )

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    with patch.object(
            fd, '_prepare_and_start_frag_download',
            side_effect=prepare_download) as prepare, \
            patch.object(
                fd, '_download_fragment',
                side_effect=[
                    http_error,
                    (True, b'initialization segment'),
                    (True, b'media segment'),
                ]) as download_fragment, \
            patch.object(fd, '_append_fragment') as append_fragment, \
            patch.object(fd, '_finish_frag_download') as finish_download, \
            patch.object(fd, 'report_retry_fragment') as report_retry, \
            patch.object(fd, 'report_skip_fragment') as report_skip, \
            patch.object(fd, 'report_error') as report_error:

        result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = prepare.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0


# Generated at 2026-10-24 23:07:10.992313
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:07:13.410450
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:07:15.828594
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:07:31.407105
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():downloader = DashSegmentsFD(None, {})

# Generated at 2026-10-24 23:07:45.993244
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    filename = 'output.mp4'
    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
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

    result = fd.real_download(filename, info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once()
    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == filename
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    fd._download_fragment.assert_has_calls([
        call(
            ctx,
            'https://example.com/media/init.m4s',
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

# Generated at 2026-10-24 23:07:55.269074
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }
    ydl = YoutubeDL({'quiet': True})

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:07:57.693735
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:00.115186
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:02.645614
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:05.065678
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:07.483120
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:09.900823
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:12.320027
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:14.738212
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:17.156812
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:19.573800
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:21.993621
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:24.411397
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 23:08:26.829164
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:29.247760
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:31.670155
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:34.085439
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:36.503232
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:38.916310
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:41.334758
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:43.750595
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:08:46.168426
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 23:09:04.387773
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    contexts = []

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0
        contexts.append(ctx)

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'url': 'https://cdn.example.com/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert len(contexts) == 1

    ctx = contexts[0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2
    assert ctx['fragment_index'] == 0

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://cdn.example.com/init.m4s', info_dict),
        call(ctx, 'https://example.com/media/segment-1.m4s', info_dict),
    ]
    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:09:19.540686
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader._progress_hooks == [downloader.report_progress]

# Generated at 2026-10-24 23:09:45.245602
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    info_dict = {
        'fragment_base_url': 'https://cdn.example.test/video/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.test/video/segment-1.m4s'},
        ],
    }

    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
        ctx['fragment_index'] = 0

    retry_error = compat_urllib_error.HTTPError(
        'https://cdn.example.test/video/init.m4s',
        404,
        'Not Found',
        {},
        None,
    )

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        retry_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

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
            'https://cdn.example.test/video/init.m4s',
            info_dict,
        ),
        call(
            ctx,
            'https://cdn.example.test/video/init.m4s',
            info_dict,
        ),
        call(
            ctx,
            'https://cdn.example.test/video/segment-1.m4s',
            info_dict,
        ),
    ])

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 1, 1, 1)
    fd._append_fragment.assert_has_calls([
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ])

# Generated at 2026-10-24 23:09:54.974133
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
    assert downloader._progress_hooks == []
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:10:03.461853
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyYDL:
        pass

    ydl = DummyYDL()
    params = {
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    }

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, DashSegmentsFD)
    assert isinstance(downloader, FragmentFD)
    assert downloader._ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:10:14.036383
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    downloaded_urls = []
    appended_fragments = []
    finished_contexts = []

    def prepare(ctx):
        ctx['fragment_index'] = 0

    def download_fragment(ctx, url, info_dict):
        downloaded_urls.append(url)
        return True, ('content:%s' % url).encode('utf-8')

    def append_fragment(ctx, content):
        appended_fragments.append(content)

    def finish(ctx):
        finished_contexts.append(ctx.copy())

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish

    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert downloaded_urls == [
        'https://example.com/video/init.mp4',
        'https://cdn.example.com/segment-1.m4s',
    ]
    assert appended_fragments == [
        b'content:https://example.com/video/init.mp4',
        b'content:https://cdn.example.com/segment-1.m4s',
    ]
    assert finished_contexts == [{
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }]

# Generated at 2026-10-24 23:10:25.637820
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    ydl = object()
    params = {'test': True}

    downloader = DashSegmentsFD(ydl, params)

    assert isinstance(downloader, FragmentFD)
    assert downloader.ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:10:44.347799
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }

    def prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(side_effect=prepare)
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()
    fd.report_retry_fragment = MagicMock()
    fd.report_skip_fragment = MagicMock()
    fd.report_error = MagicMock()

    retry_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.mp4',
        404,
        'Not Found',
        {},
        None,
    )

    # The first request fails, is retried, and then succeeds. The second
    # fragment succeeds immediately.
    fd._download_fragment = MagicMock(side_effect=[
        retry_error,
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

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]
    assert ctx['filename'] == 'output.mp4'
    assert ctx['total_frags'] == 2

    assert fd._download_fragment.call_args_list == [
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ]

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 1, 1, 1)

    assert fd._append_fragment.call_args_list == [
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ]

    fd._finish_frag_download.assert_called_once_with(ctx)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()

# Generated at 2026-10-24 23:10:52.827584
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

# Generated at 2026-10-24 23:11:14.747206
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
        'test': False,
    })

    filename = 'output.mp4'
    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    captured_ctx = {}

    def prepare_download(ctx):
        ctx['fragment_index'] = 0
        captured_ctx.update(ctx)

    retry_error = compat_urllib_error.HTTPError(
        'https://example.com/video/init.mp4',
        404,
        'Not Found',
        None,
        None,
    )

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        retry_error,
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    result = fd.real_download(filename, info_dict)

    assert result is True
    assert captured_ctx['filename'] == filename
    assert captured_ctx['total_frags'] == 2

    ctx = fd._prepare_and_start_frag_download.call_args[0][0]

    fd._download_fragment.assert_has_calls([
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://example.com/video/init.mp4', info_dict),
        call(ctx, 'https://cdn.example.com/segment-1.m4s', info_dict),
    ])
    fd._append_fragment.assert_has_calls([
        call(ctx, b'initialization segment'),
        call(ctx, b'media segment'),
    ])

    fd.report_retry_fragment.assert_called_once_with(
        retry_error, 1, 1, 1)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._finish_frag_download.assert_called_once_with(ctx)

# Generated at 2026-10-24 23:11:31.845889
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    class TestDashSegmentsFD(DashSegmentsFD):
        def __init__(self):
            self.params = {
                'fragment_retries': 1,
                'skip_unavailable_fragments': True,
            }
            self.attempted_urls = []
            self.appended_fragments = []
            self.retry_reports = []
            self.finished = False

        def _prepare_and_start_frag_download(self, ctx):
            # Simulate a fresh, non-resumed download.
            ctx['fragment_index'] = 0

        def _download_fragment(self, ctx, fragment_url, info_dict):
            self.attempted_urls.append(fragment_url)

            # Make the media fragment fail once to verify retry behavior.
            if fragment_url.endswith('segment-1.m4s') and (
                    self.attempted_urls.count(fragment_url) == 1):
                raise compat_urllib_error.HTTPError(
                    fragment_url, 404, 'Not Found', None, None)

            return True, fragment_url.encode('utf-8')

        def _append_fragment(self, ctx, fragment_content):
            self.appended_fragments.append(fragment_content)

        def report_retry_fragment(
                self, err, frag_index, retry_count, fragment_retries):
            self.retry_reports.append(
                (err.code, frag_index, retry_count, fragment_retries))

        def _finish_frag_download(self, ctx):
            self.finished = True
            self.finished_ctx = dict(ctx)

    downloader = TestDashSegmentsFD()
    info_dict = {
        'fragment_base_url': 'https://example.com/video/',
        'fragments': [
            {'url': 'https://example.com/video/init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = downloader.real_download('output.mp4', info_dict)

    assert result is True
    assert downloader.attempted_urls == [
        'https://example.com/video/init.m4s',
        'https://example.com/video/segment-1.m4s',
        'https://example.com/video/segment-1.m4s',
    ]
    assert downloader.appended_fragments == [
        b'https://example.com/video/init.m4s',
        b'https://example.com/video/segment-1.m4s',
    ]
    assert downloader.retry_reports == [(404, 2, 1, 1)]
    assert downloader.finished is True
    assert downloader.finished_ctx['filename'] == 'output.mp4'
    assert downloader.finished_ctx['total_frags'] == 2

# Generated at 2026-10-24 23:11:40.924171
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

# Generated at 2026-10-24 23:11:50.396182
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    try:
        from unittest.mock import Mock
    except ImportError:
        from mock import Mock

    ydl = Mock()
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

# Generated at 2026-10-24 23:12:15.064078
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    params = {
        'fragment_retries': 1,
        'skip_unavailable_fragments': True,
    }
    fd = DashSegmentsFD(None, params)

    def prepare(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = MagicMock(side_effect=prepare)
    fd._append_fragment = MagicMock()
    fd._finish_frag_download = MagicMock()
    fd.report_retry_fragment = MagicMock()
    fd.report_skip_fragment = MagicMock()
    fd.report_error = MagicMock()

    init_error = compat_urllib_error.HTTPError(
        'https://example.test/video/init.mp4',
        404, 'Not Found', {}, None)
    missing_error_1 = compat_urllib_error.HTTPError(
        'https://example.test/video/missing.m4s',
        404, 'Not Found', {}, None)
    missing_error_2 = compat_urllib_error.HTTPError(
        'https://example.test/video/missing.m4s',
        404, 'Not Found', {}, None)

    fd._download_fragment = MagicMock(side_effect=[
        init_error,              # First fragment fails once
        (True, b'init-data'),    # Retry succeeds
        (True, b'media-data'),   # Second fragment succeeds
        missing_error_1,         # Third fragment fails
        missing_error_2,         # Retry also fails, so it is skipped
    ])

    info

# Generated at 2026-10-24 23:12:33.408017
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    events = []

    def prepare(ctx):
        ctx['fragment_index'] = 0
        events.append(('prepare', dict(ctx)))

    def download_fragment(ctx, fragment_url, passed_info_dict):
        assert passed_info_dict is info_dict
        events.append(('download', fragment_url))
        return True, ('content:%s' % fragment_url).encode('utf-8')

    def append_fragment(ctx, content):
        events.append(('append', content))
        ctx['fragment_index'] += 1

    def finish(ctx):
        events.append(('finish', dict(ctx)))

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish

    info_dict = {
        'fragment_base_url': 'https://cdn.example.com/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://media.example.com/segment-1.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert events == [
        ('prepare', {
            'filename': 'output.mp4',
            'total_frags': 2,
            'fragment_index': 0,
        }),
        ('download', 'https://cdn.example.com/video/init.mp4'),
        ('append', b'content:https://cdn.example.com/video/init.mp4'),
        ('download', 'https://media.example.com/segment-1.m4s'),
        ('append', b'content:https://media.example.com/segment-1.m4s'),
        ('finish', {
            'filename': 'output.mp4',
            'total_frags': 2,
            'fragment_index': 2,
        }),
    ]

# Generated at 2026-10-24 23:12:45.245305
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    class DummyYDL(object):
        pass

    ydl = DummyYDL()
    params = {
        'test': True,
        'fragment_retries': 3,
        'skip_unavailable_fragments': False,
    }

    fd = DashSegmentsFD(ydl, params)

    assert isinstance(fd, FragmentFD)
    assert fd.ydl is ydl
    assert fd.params is params
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-10-24 23:13:02.247554
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    filename = 'output.mp4'
    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    downloader = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    def prepare_download(ctx):
        # Normally initialized by FragmentFD.
        ctx['fragment_index'] = 0

    downloader._prepare_and_start_frag_download = Mock(
        side_effect=prepare_download)
    downloader._download_fragment = Mock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    downloader._append_fragment = Mock()
    downloader._finish_frag_download = Mock()

    assert downloader.real_download(filename, info_dict) is True

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
            'https://example.com/media/init.m4s',
            info_dict),
        call(
            expected_ctx,
            'https://cdn.example.com/segment-1.m4s',
            info_dict),
    ])
    downloader._append_fragment.assert_has_calls([
        call(expected_ctx, b'initialization segment'),
        call(expected_ctx, b'media segment'),
    ])
    downloader._finish_frag_download.assert_called_once_with(expected_ctx)

# Generated at 2026-10-24 23:13:23.766036
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = object.__new__(DashSegmentsFD)
    fd.params = {
        'test': False,
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    }

    downloaded = []
    appended = []
    finished = []

    def prepare(ctx):
        ctx['fragment_index'] = 0

    def download_fragment(ctx, fragment_url, info_dict):
        downloaded.append(fragment_url)
        return True, ('content:%s' % fragment_url).encode('utf-8')

    def append_fragment(ctx, content):
        appended.append(content)

    def finish(ctx):
        finished.append(dict(ctx))

    fd._prepare_and_start_frag_download = prepare
    fd._download_fragment = download_fragment
    fd._append_fragment = append_fragment
    fd._finish_frag_download = finish

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.m4s'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    assert downloaded == [
        'https://example.com/media/init.m4s',
        'https://cdn.example.com/segment-1.m4s',
    ]
    assert appended == [
        b'content:https://example.com/media/init.m4s',
        b'content:https://cdn.example.com/segment-1.m4s',
    ]
    assert finished == [{
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    }]

# Generated at 2026-10-24 23:13:40.055434
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    fd = DashSegmentsFD(None, {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })

    info_dict = {
        'fragment_base_url': 'https://example.com/media/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.com/segment-1.m4s'},
        ],
    }

    def prepare_download(ctx):
        # Normally initialized by _prepare_and_start_frag_download.
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(
        side_effect=prepare_download)
    fd._download_fragment = Mock(side_effect=[
        (True, b'initialization segment'),
        (True, b'media segment'),
    ])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()

    result = fd.real_download('output.mp4', info_dict)

    assert result is True

    fd._prepare_and_start_frag_download.assert_called_once_with({
        'filename': 'output.mp4',
        'total_frags': 2,
        'fragment_index': 0,
    })

    fd._download_fragment.assert_has_calls([
        call(
            ANY,
            'https://example.com/media/init.mp4',
            info_dict,
        ),
        call(
            ANY,
            'https://cdn.example.com/segment-1.m4s',
            info_dict,
        ),
    ])

    assert fd._append_fragment.call_count == 2
    assert fd._append_fragment.call_args_list[0].args[1] == \
        b'initialization segment'
    assert fd._append_fragment.call_args_list[1].args[1] == \
        b'media segment'

    fd._finish_frag_download.assert_called_once_with(ANY)