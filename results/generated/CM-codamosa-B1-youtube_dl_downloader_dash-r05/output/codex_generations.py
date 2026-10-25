

# Generated at 2026-10-24 12:44:27.926108
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    params = {
        'test': True,
        'fragment_retries': 3,
        'skip_unavailable_fragments': False,
    }

    fd = DashSegmentsFD(None, params)

    assert isinstance(fd, FragmentFD)
    assert fd.FD_NAME == 'dashsegments'
    assert fd.params is params
    assert fd._ydl is None

# Generated at 2026-10-24 12:45:09.127983
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    retry_error = compat_urllib_error.HTTPError(
        'https://example.test/video/init.mp4',
        404,
        'Not Found',
        {},
        None,
    )

    class TestDashSegmentsFD(DashSegmentsFD):
        def __init__(self):
            DashSegmentsFD.__init__(self, None, {
                'fragment_retries': 1,
                'skip_unavailable_fragments': True,
            })
            self.requested_urls = []
            self.appended_fragments = []
            self.retry_reports = []
            self.finished_ctx = None

        def _prepare_and_start_frag_download(self, ctx):
            ctx['fragment_index'] = 0

        def _download_fragment(self, ctx, fragment_url, info_dict):
            self.requested_urls.append(fragment_url)

            # Make the first request fail to verify HTTP fragment retries.
            if len(self.requested_urls) == 1:
                raise retry_error

            if fragment_url.endswith('init.mp4'):
                return True, b'initialization segment'
            return True, b'media segment'

        def _append_fragment(self, ctx, fragment_content):
            self.appended_fragments.append(fragment_content)
            ctx['fragment_index'] += 1

        def report_retry_fragment(
                self, err, frag_index, retry_count, fragment_retries):
            self.retry_reports.append((
                err, frag_index, retry_count, fragment_retries))

        def _finish_frag_download(self, ctx):
            self.finished_ctx = dict(ctx)

    fd = TestDashSegmentsFD()
    info_dict = {
        'fragment_base_url': 'https://example.test/video/',
        'fragments': [
            {'path': 'init.mp4'},
            {'url': 'https://cdn.example.test/media-1.m4s'},
        ],
    }

    assert fd.real_download('output.mp4', info_dict) is True

    assert fd.requested_urls == [
        'https://example.test/video/init.mp4',
        'https://example.test/video/init.mp4',
        'https://cdn.example.test/media-1.m4s',
    ]
    assert fd.appended_fragments == [
        b'initialization segment',
        b'media segment',
    ]
    assert fd.retry_reports

# Generated at 2026-10-24 12:45:51.926287
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:46:05.547930
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():from youtube_dl.downloader.dash import DashSegmentsFD


# Generated at 2026-10-24 12:46:13.154526
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
    assert downloader._ydl is ydl
    assert downloader.params is params
    assert downloader.FD_NAME == 'dashsegments'
    assert downloader._progress_hooks

# Generated at 2026-10-24 12:47:08.219969
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:47:46.004170
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:48:20.612767
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:48:27.803990
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:48:29.197182
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:48:36.021389
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:48:59.727641
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:49:04.344752
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:49:22.053520
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:49:25.022182
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:49:26.456183
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:49:29.323727
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:49:30.707897
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:49:33.523331
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:49:36.490233
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:49:39.363735
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:49:44.682205
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:11.511340
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:50:14.079475
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:16.492985
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:18.906389
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:21.319974
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:23.733670
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:26.147652
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:50:28.561818
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:51:04.078247
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:51:05.469875
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:51:37.573443
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:52:25.461506
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:52:27.877357
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:52:30.381026
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:52:32.793906
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:52:49.207736
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:52:52.076638
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:52:59.146727
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:02.008394
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:04.876328
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:22.569549
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:24.983405
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:27.399914
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:30.032363
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:32.450566
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:34.870843
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:37.291067
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:39.707264
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:53:42.122085
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:44.544069
# Unit test for constructor of class DashSegmentsFD

# Generated at 2026-10-24 12:53:45.939811
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():from unittest.mock import MagicMock

# Generated at 2026-10-24 12:53:48.808071
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:54:06.826633
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-10-24 12:54:30.960962
# Unit test for method real_download of class DashSegmentsFD