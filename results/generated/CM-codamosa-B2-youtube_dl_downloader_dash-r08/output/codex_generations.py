

# Generated at 2026-11-01 23:12:46.656405
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import Mock

    # Build an instance without calling __init__ (avoid downloader boilerplate)
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
        'test': False,
    }

    # _prepare_and_start_frag_download must populate ctx['fragment_index']
    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    fd._prepare_and_start_frag_download = Mock(side_effect=fake_prepare)
    fd._download_fragment = Mock(side_effect=[(True, b'frag1'), (True, b'frag2')])
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    info_dict = {
        'fragment_base_url': 'http://example.com/dash/',
        'fragments': [
            {'path': 'seg1.m4s'},
            {'url': 'http://example.com/dash/seg2.m4s'},
        ],
    }

    result = fd.real_download('video.mp4', info_dict)

    assert result is True
    fd._prepare_and_start_frag_download.assert_called_once()
    # First fragment: url built from fragment_base_url + path
    first_call = fd._download_fragment.call_args_list[0]
    assert first_call[0][1] == 'http://example.com/dash/seg1.m4s'
    # Second fragment: explicit url used directly
    second_call = fd._download_fragment.call_args_list[1]
    assert second_call[0][1] == 'http://example.com/dash/seg2.m4s'
    assert fd._download_fragment.call_count == 2
    assert fd._append_fragment.call_count == 2
    fd._append_fragment.assert_any_call(fd._prepare_and_start_frag_download.call_args[0][0], b'frag1')
    fd._finish_frag_download.assert_called_once()
    fd.report_error.assert_not_called()
    fd.report_skip_fragment.assert_not_called()
    fd.report_retry_fragment.assert_not_called()

# Generated at 2026-11-01 23:13:07.955392
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():from __future__ import unicode_literals

import unittest

from . import FragmentFD
from .dashsegments import DashSegmentsFD
from ..compat import compat_urllib_error
from ..utils import DownloadError


class FakeYDL(object):
    params = {}


def _make_fd(params=None):
    fd = DashSegmentsFD(FakeYDL())
    if params:
        fd.params.update(params)
    fd._prepare_and_start_frag_download = lambda ctx: None
    fd._finish_frag_download = lambda ctx: None
    fd.report_error = lambda msg: errors.append(msg)
    fd.report_retry_fragment = lambda err, frag_index, count, retries: None
    fd.report_skip_fragment = lambda frag_index: skipped.append(frag_index)
    return fd


errors = []
skipped = []


class TestDashSegmentsFDRealDownload(unittest.TestCase):

    def setUp(self):
        errors[:] = []
        skipped[:] = []

    def test_successful_download_all_fragments(self):
        fd = _make_fd()
        contents = iter([b'frag0', b'frag1', b'frag2'])
        appended = []

        def _download_fragment(ctx, url, info_dict):
            return True, next(contents)

        fd._download_fragment = _download_fragment
        fd._append_fragment = lambda ctx, content: appended.append(content)

        info_dict = {
            'fragments': [{'url': 'http://example.com/seg0'}, {'url': 'http://example.com/seg1'}, {'url': 'http://example.com/seg2'}],
        }
        result = fd.real_download('test.mp4', info_dict)
        self.assertTrue(result)
        self.assertEqual(appended, [b'frag0', b'frag1', b'frag2'])

    def test_download_fragment_failure_returns_false(self):
        fd = _make_fd()
        fd._download_fragment = lambda ctx, url, info_dict: (False, None)
        fd._append_fragment = lambda ctx, content: None

        info_dict = {'fragments': [{'url': 'http://example.com/seg0'}]}
        result = fd.real_download('test.mp4', info_dict)
        self.assertFalse(result)

    def test_urljoin_from_base_and_path(self):
        fd = _make_fd()
        appended = []
        urls = []

        def _download_fragment(ctx, url, info_dict):
            urls.append(url)
            return True, b'data'

        fd._download_fragment = _download_fragment
        fd._append_fragment = lambda ctx, content: appended.append(content)

        info_dict = {
            'fragment_base_url': 'http://example.com/base/',
            'fragments': [{'path': 'seg1.m4s'}],
        }
        result = fd.real_download('test.mp4', info_dict)
        self.assertTrue(result)
        self.assertEqual(urls, ['http://example.com/base/seg1.m4s'])

    def test_http_error_retried_then_success(self):
        fd = _make_fd({'fragment_retries': 2})
        appended = []
        attempts = []

        def _download_fragment(ctx, url, info_dict):
            attempts.append(url)
            if len(attempts) < 3:
                raise compat_urllib_error.HTTPError(url, 404, 'Not Found', None, None)
            return True, b'data'

        fd._download_fragment = _download_fragment
        fd._append_fragment = lambda ctx, content: appended.append(content)

        info_dict = {'fragments': [{'url': 'http://example.com/seg0'}]}
        result = fd.real_download('test.mp4', info_dict)
        self.assertTrue(result)
        self.assertEqual(len(attempts), 3)
        self.assertEqual(appended, [b'data'])

    def test_http_error_gives_up_after_retries_fatal_first_fragment(self):
        fd = _make_fd({'fragment_retries': 1})
        attempts = []

        def _download_fragment(ctx, url, info_dict):
            attempts.append(url)
            raise compat_urllib_error.HTTPError(url, 404, 'Not Found', None, None)

        fd._download_fragment = _download_fragment
        fd._append_fragment = lambda ctx, content: None

        info_dict = {'fragments': [{'url': 'http://example.com/seg0'}]}
        result = fd.real_download('test.mp4', info_dict)
        self.assertFalse(result)
        self.assertEqual(len(attempts), 2)  # initial + 1 retry

    def test_download_error_nonfatal_first_fragment_raises(self):
        fd = _make_fd()
        fd._download_fragment = lambda ctx, url, info_dict: (_ for _ in ()).throw(DownloadError('fail'))
        fd._append_fragment = lambda ctx, content: None

        info_dict = {'fragments': [{'url': 'http://example.com/seg0'}]}
        self.assertRaises(DownloadError, fd.real_download, 'test.mp4', info_dict)

    def test_download_error_nonfatal_skipped_later_fragment(self):
        fd = _make_fd()
        fd._download_fragment = lambda ctx, url, info_dict: (
            (_ for _ in ()).throw(DownloadError('fail')) if url.endswith('seg1') else (True, b'data'))
        fd._append_fragment = lambda ctx, content: None

        info_dict = {
            'fragments': [{'url': 'http://example.com/seg0'}, {'url': 'http://example.com/seg1'}],
        }
        result = fd.real_download('test.mp4', info_dict)
        self.assertTrue(result)
        self.assertEqual(skipped, [2])

    def test_test_mode_downloads_only_first_fragment(self):
        fd = _make_fd({'test': True})
        appended = []

        def _download_fragment(ctx, url, info_dict):
            return True, b'data'

        fd._download_fragment = _download_fragment
        fd._append_fragment = lambda ctx, content: appended.append(content)

        info_dict = {
            'fragments': [{'url': 'http://example.com/seg0'}, {'url': 'http://example.com/seg1'}],
        }
        result = fd.real_download('test.mp4', info_dict)
        self.assertTrue(result)
        self.assertEqual(appended, [b'data'])

    def test_http_error_nonfatal_skip_after_retries(self):
        fd = _make_fd({'fragment_retries': 1, 'skip_unavailable_fragments': True})
        attempts = []

        def _download_fragment(ctx, url, info_dict):
            attempts.append(url)
            raise compat_urllib_error.HTTPError(url, 404, 'Not Found', None, None)

        fd._download_fragment = _download_fragment
        fd._append_fragment = lambda ctx, content: None

        info_dict = {
            'fragments': [{'url': 'http://example.com/seg0'}, {'url': 'http://example.com/seg1'}],
        }
        result = fd.real_download('test.mp4', info_dict)
        self.assertTrue(result)
        self.assertEqual(skipped, [2])


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-01 23:14:54.978799
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-11-01 23:17:00.616256
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest.mock import MagicMock
    from youtube_dl.downloader.dashsegments import DashSegmentsFD

    info_dict = {
        'fragment_base_url': 'http://example.com/f/',
        'fragments': [
            {'path': 'seg-0.m4s'},
            {'url': 'http://cdn.example.com/seg-1.m4s', 'path': 'ignored'},
            {'path': 'seg-2.m4s'},
        ],
    }

    def make_downloader(params):
        dl = DashSegmentsFD.__new__(DashSegmentsFD)
        dl.params = params
        dl.ydl = MagicMock()
        state = {'urls': [], 'contents': [], 'prepared': 0, 'finished': 0}

        def fake_prepare(ctx):
            ctx['fragment_index'] = 0
            state['prepared'] += 1

        def fake_download(ctx, url, info):
            state['urls'].append(url)
            return True, b'frag:' + url.encode('ascii')

        def fake_append(ctx, content):
            state['contents'].append(content)

        def fake_finish(ctx):
            state['finished'] += 1

        dl._prepare_and_start_frag_download = MagicMock(side_effect=fake_prepare)
        dl._download_fragment = MagicMock(side_effect=fake_download)
        dl._append_fragment = MagicMock(side_effect=fake_append)
        dl._finish_frag_download = MagicMock(side_effect=fake_finish)
        return dl, state

    # Full download: every fragment is fetched; fragments without a 'url'
    # are resolved via urljoin against fragment_base_url, fragments with a
    # 'url' are used verbatim.
    dl, state = make_downloader({
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    })
    assert dl.real_download('video.mp4', dict(info_dict)) is True
    assert state['urls'] == [
        'http://example.com/f/seg-0.m4s',
        'http://cdn.example.com/seg-1.m4s',
        'http://example.com/f/seg-2.m4s',
    ]
    assert state['contents'] == [
        b'frag:http://example.com/f/seg-0.m4s',
        b'frag:http://cdn.example.com/seg-1.m4s',
        b'frag:http://example.com/f/seg-2.m4s',
    ]
    assert state['prepared'] == 1
    assert state['finished'] == 1
    assert dl._download_fragment.call_count == 3
    assert dl._append_fragment.call_count == 3
    dl._finish_frag_download.assert_called_once()

    # Test mode: only the first fragment of the manifest is downloaded.
    dl, state = make_downloader({
        'test': True,
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
    })
    assert dl.real_download('video-test.mp4', dict(info_dict)) is True
    assert state['urls'] == ['http://example.com/f/seg-0.m4s']
    assert state['contents'] == [b'frag:http://example.com/f/seg-0.m4s']
    assert state['prepared'] == 1
    assert state['finished'] == 1
    assert dl._download_fragment.call_count == 1

# Generated at 2026-11-01 23:18:20.787702
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-11-01 23:19:41.530220
# Unit test for method real_download of class DashSegmentsFD

# Generated at 2026-11-01 23:21:22.654965
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from yt_dlp.downloader.dashsegments import DashSegmentsFD

    calls = {'prepare': 0, 'finish': 0, 'append': [], 'urls': []}

    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = {'test': False}

    def fake_prepare(ctx):
        calls['prepare'] += 1
        ctx['fragment_index'] = 0

    def fake_download(ctx, url, info_dict):
        calls['urls'].append(url)
        return True, b'frag-data'

    def fake_append(ctx, content):
        calls['append'].append(content)

    def fake_finish(ctx):
        calls['finish'] += 1

    fd._prepare_and_start_frag_download = fake_prepare
    fd._download_fragment = fake_download
    fd._append_fragment = fake_append
    fd._finish_frag_download = fake_finish

    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg1.m4s'},
            {'url': 'http://example.com/seg2.m4s'},
        ],
    }

    result = fd.real_download('output.mp4', info_dict)

    assert result is True
    assert calls['prepare'] == 1
    assert calls['finish'] == 1
    assert calls['urls'] == [
        'http://example.com/seg1.m4s',
        'http://example.com/seg2.m4s',
    ]
    assert calls['append'] == [b'frag-data', b'frag-data']

    # In test mode only the first fragment should be downloaded
    calls2 = {'urls': []}
    fd2 = DashSegmentsFD.__new__(DashSegmentsFD)
    fd2.params = {'test': True}

    def fake_download2(ctx, url, info_dict):
        calls2['urls'].append(url)
        ctx['fragment_index'] = 0
        return True, b'frag-data'

    fd2._prepare_and_start_frag_download = lambda ctx: ctx.update({'fragment_index': 0})
    fd2._download_fragment = fake_download2
    fd2._append_fragment = lambda ctx, content: None
    fd2._finish_frag_download = lambda ctx: None

    info_dict2 = {
        'fragments': [
            {'url': 'http://example.com/seg1.m4s'},
            {'url': 'http://example.com/seg2.m4s'},
            {'url': 'http://example.com/seg3.m4s'},
        ],
    }

    result2 = fd2.real_download('output_test.mp4', info_dict2)

    assert result2 is True
    assert calls2['urls'] == ['http://example.com/seg1.m4s']