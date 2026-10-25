# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

import pytest
from unittest.mock import MagicMock

from youtube_dl.compat import compat_urllib_error
from youtube_dl.utils import DownloadError
from youtube_dl.downloader.dash import DashSegmentsFD


def _make_fd(params=None, fragment_index=0):
    """Build a DashSegmentsFD with all file/network-touching parent methods mocked out."""
    fd = DashSegmentsFD(MagicMock(), params or {})

    def _prepare(ctx):
        ctx['fragment_index'] = fragment_index

    fd._prepare_and_start_frag_download = MagicMock(side_effect=_prepare)
    fd._finish_frag_download = MagicMock()
    fd._append_fragment = MagicMock()
    fd.report_retry_fragment = MagicMock()
    fd.report_skip_fragment = MagicMock()
    fd.report_error = MagicMock()
    return fd


def _info_dict(fragments, base_url=None):
    info = {'fragments': fragments}
    if base_url is not None:
        info['fragment_base_url'] = base_url
    return info


def test_success_all_fragments():
    fd = _make_fd()
    fragments = [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]
    fd._download_fragment = MagicMock(return_value=(True, b'fragdata'))

    result = fd.real_download('out.mp4', _info_dict(fragments))

    assert result is True
    assert fd._download_fragment.call_count == 2
    assert fd._download_fragment.call_args_list[0][0][1] == 'http://example.com/f1'
    assert fd._download_fragment.call_args_list[1][0][1] == 'http://example.com/f2'
    assert fd._append_fragment.call_count == 2
    # _append_fragment(ctx, frag_content)
    assert fd._append_fragment.call_args_list[0][0][1] == b'fragdata'
    assert fd._append_fragment.call_args_list[1][0][1] == b'fragdata'
    assert fd._append_fragment.call_args[0][1] == b'fragdata'
    assert fd._finish_frag_download.call_count == 1
    ctx = fd._finish_frag_download.call_args[0][0]
    assert ctx['total_frags'] == 2
    assert ctx['filename'] == 'out.mp4'
    fd.report_error.assert_not_called()
    fd.report_skip_fragment.assert_not_called()


def test_test_mode_downloads_only_first_fragment():
    fd = _make_fd(params={'test': True})
    fragments = [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]
    fd._download_fragment = MagicMock(return_value=(True, b'fragdata'))

    result = fd.real_download('out.mp4', _info_dict(fragments))

    assert result is True
    assert fd._download_fragment.call_count == 1
    assert fd._download_fragment.call_args[0][1] == 'http://example.com/f1'
    assert fd._finish_frag_download.call_count == 1
    ctx = fd._finish_frag_download.call_args[0][0]
    assert ctx['total_frags'] == 1


def test_fragment_url_built_from_base_url_and_path():
    fd = _make_fd()
    fragments = [{'path': 'seg1.m4s'}]
    fd._download_fragment = MagicMock(return_value=(True, b'fragdata'))

    result = fd.real_download('out.mp4', _info_dict(fragments, base_url='http://example.com/dash/'))

    assert result is True
    fd._download_fragment.assert_called_once()
    assert fd._download_fragment.call_args[0][1] == 'http://example.com/dash/seg1.m4s'
    assert fd._finish_frag_download.call_count == 1


def test_http_error_retried_then_success():
    fd = _make_fd(params={'fragment_retries': 3})
    fragments = [{'url': 'http://example.com/f1'}]
    err = compat_urllib_error.HTTPError('http://example.com/f1', 404, 'Not Found', None, None)
    fd._download_fragment = MagicMock(side_effect=[err, (True, b'fragdata')])

    result = fd.real_download('out.mp4', _info_dict(fragments))

    assert result is True
    assert fd._download_fragment.call_count == 2
    assert fd.report_retry_fragment.call_count == 1
    fd.report_retry_fragment.assert_called_with(err, 1, 1, 3)
    assert fd._append_fragment.call_count == 1
    assert fd._append_fragment.call_args[0][1] == b'fragdata'
    assert fd._finish_frag_download.call_count == 1
    fd.report_error.assert_not_called()


def test_http_error_retries_exhausted_fatal_first_fragment():
    fd = _make_fd(params={'fragment_retries': 1})
    fragments = [{'url': 'http://example.com/f1'}]
    err = compat_urllib_error.HTTPError('http://example.com/f1', 500, 'Server Error', None, None)
    fd._download_fragment = MagicMock(side_effect=err)

    result = fd.real_download('out.mp4', _info_dict(fragments))

    assert result is False
    assert fd._download_fragment.call_count == 2
    # Only the first failure is within the retry limit (count 1 <= 1);
    # the second failure makes count 2 > 1, so no further retry report.
    assert fd.report_retry_fragment.call_count == 1
    fd.report_retry_fragment.assert_called_with(err, 1, 1, 1)
    fd.report_error.assert_called_once()
    assert 'giving up after 1 fragment retries' in fd.report_error.call_args[0][0]
    fd._finish_frag_download.assert_not_called()


def test_http_error_retries_exhausted_nonfatal_skips_fragment():
    fd = _make_fd(params={'fragment_retries': 0})
    fragments = [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]
    err = compat_urllib_error.HTTPError('http://example.com/f2', 404, 'Not Found', None, None)
    fd._download_fragment = MagicMock(side_effect=[(True, b'fragdata'), err])

    result = fd.real_download('out.mp4', _info_dict(fragments))

    assert result is True
    assert fd._download_fragment.call_count == 2
    fd.report_retry_fragment.assert_not_called()
    fd.report_skip_fragment.assert_called_once_with(2)
    fd.report_error.assert_not_called()
    assert fd._append_fragment.call_count == 1
    assert fd._finish_frag_download.call_count == 1


def test_download_error_skips_unavailable_fragment():
    fd = _make_fd()
    fragments = [
        {'url': 'http://example.com/f1'},
        {'url': 'http://example.com/f2'},
        {'url': 'http://example.com/f3'},
    ]
    fd._download_fragment = MagicMock(
        side_effect=[(True, b'fragdata'), DownloadError('boom'), (True, b'fragdata2')])

    result = fd.real_download('out.mp4', _info_dict(fragments))

    assert result is True
    assert fd._download_fragment.call_count == 3
    fd.report_skip_fragment.assert_called_once_with(2)
    fd.report_error.assert_not_called()
    assert fd._append_fragment.call_count == 2
    assert fd._append_fragment.call_args_list[0][0][1] == b'fragdata'
    assert fd._append_fragment.call_args_list[1][0][1] == b'fragdata2'
    assert fd._finish_frag_download.call_count == 1


def test_download_error_on_first_fragment_is_fatal():
    fd = _make_fd()
    fragments = [{'url': 'http://example.com/f1'}]
    fd._download_fragment = MagicMock(side_effect=DownloadError('boom'))

    with pytest.raises(DownloadError):
        fd.real_download('out.mp4', _info_dict(fragments))

    fd.report_skip_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_download_error_fatal_when_skip_disabled():
    fd = _make_fd(params={'skip_unavailable_fragments': False})
    fragments = [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]
    fd._download_fragment = MagicMock(
        side_effect=[(True, b'fragdata'), DownloadError('boom')])

    with pytest.raises(DownloadError):
        fd.real_download('out.mp4', _info_dict(fragments))

    fd.report_skip_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_download_fragment_failure_returns_false():
    fd = _make_fd()
    fragments = [{'url': 'http://example.com/f1'}]
    fd._download_fragment = MagicMock(return_value=(False, None))

    result = fd.real_download('out.mp4', _info_dict(fragments))

    assert result is False
    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_resume_skips_already_downloaded_fragments():
    fd = _make_fd(fragment_index=1)
    fragments = [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]
    fd._download_fragment = MagicMock(return_value=(True, b'fragdata'))

    result = fd.real_download('out.mp4', _info_dict(fragments))

    assert result is True
    assert fd._download_fragment.call_count == 1
    assert fd._download_fragment.call_args[0][1] == 'http://example.com/f2'
    assert fd._append_fragment.call_count == 1
    assert fd._append_fragment.call_args[0][1] == b'fragdata'
    assert fd._finish_frag_download.call_count == 1
