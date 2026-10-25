# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

from unittest.mock import MagicMock

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError


def make_downloader(params=None, fragment_index=0):
    downloader = object.__new__(DashSegmentsFD)
    downloader.params = params or {}

    def prepare(ctx):
        ctx['fragment_index'] = fragment_index

    downloader._prepare_and_start_frag_download = MagicMock(side_effect=prepare)
    downloader._download_fragment = MagicMock()
    downloader._append_fragment = MagicMock()
    downloader._finish_frag_download = MagicMock()
    downloader.report_retry_fragment = MagicMock()
    downloader.report_skip_fragment = MagicMock()
    downloader.report_error = MagicMock()
    return downloader


def http_error(code=404):
    return compat_urllib_error.HTTPError(
        'https://example.test/fragment', code, 'Not Found', None, None)


def test_success_uses_base_url_and_limits_fragments_in_test_mode():
    downloader = make_downloader({'test': True})
    downloader._download_fragment.return_value = (True, b'fragment-data')
    info_dict = {
        'fragment_base_url': 'https://example.test/media/',
        'fragments': [
            {'path': 'segment-1.m4s'},
            {'path': 'segment-2.m4s'},
        ],
    }

    assert downloader.real_download('output.mp4', info_dict) is True

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 1,
        'fragment_index': 0,
    }
    downloader._download_fragment.assert_called_once_with(
        ctx, 'https://example.test/media/segment-1.m4s', info_dict)
    downloader._append_fragment.assert_called_once_with(ctx, b'fragment-data')
    downloader._finish_frag_download.assert_called_once_with(ctx)


def test_direct_fragment_download_failure_returns_false():
    downloader = make_downloader()
    downloader._download_fragment.return_value = (False, None)
    info_dict = {
        'fragments': [{'url': 'https://example.test/segment.m4s'}],
    }

    assert downloader.real_download('output.mp4', info_dict) is False

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    downloader._download_fragment.assert_called_once_with(
        ctx, 'https://example.test/segment.m4s', info_dict)
    downloader._append_fragment.assert_not_called()
    downloader._finish_frag_download.assert_not_called()


def test_already_downloaded_fragment_is_skipped_when_resuming():
    downloader = make_downloader(fragment_index=1)
    downloader._download_fragment.return_value = (True, b'second')
    info_dict = {
        'fragments': [
            {'url': 'https://example.test/first.m4s'},
            {'url': 'https://example.test/second.m4s'},
        ],
    }

    assert downloader.real_download('output.mp4', info_dict) is True

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    downloader._download_fragment.assert_called_once_with(
        ctx, 'https://example.test/second.m4s', info_dict)
    downloader._append_fragment.assert_called_once_with(ctx, b'second')
    downloader._finish_frag_download.assert_called_once_with(ctx)


def test_http_error_is_reported_and_fragment_is_retried():
    downloader = make_downloader({'fragment_retries': 1})
    error = http_error()
    downloader._download_fragment.side_effect = [
        error,
        (True, b'retried-data'),
    ]
    info_dict = {
        'fragments': [{'url': 'https://example.test/segment.m4s'}],
    }

    assert downloader.real_download('output.mp4', info_dict) is True

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    assert downloader._download_fragment.call_count == 2
    downloader.report_retry_fragment.assert_called_once_with(error, 1, 1, 1)
    downloader._append_fragment.assert_called_once_with(ctx, b'retried-data')
    downloader._finish_frag_download.assert_called_once_with(ctx)
    downloader.report_error.assert_not_called()


def test_first_fragment_http_errors_are_fatal_after_retries():
    downloader = make_downloader({'fragment_retries': 1})
    first_error = http_error(500)
    second_error = http_error(503)
    downloader._download_fragment.side_effect = [first_error, second_error]
    info_dict = {
        'fragments': [{'url': 'https://example.test/segment.m4s'}],
    }

    assert downloader.real_download('output.mp4', info_dict) is False

    assert downloader._download_fragment.call_count == 2
    downloader.report_retry_fragment.assert_called_once_with(
        first_error, 1, 1, 1)
    downloader.report_error.assert_called_once_with(
        'giving up after 1 fragment retries')
    downloader._append_fragment.assert_not_called()
    downloader._finish_frag_download.assert_not_called()


def test_unavailable_noninitial_fragment_is_skipped_after_http_error():
    downloader = make_downloader({
        'fragment_retries': 0,
        'skip_unavailable_fragments': True,
    })
    error = http_error()
    downloader._download_fragment.side_effect = [
        (True, b'header'),
        error,
    ]
    info_dict = {
        'fragments': [
            {'url': 'https://example.test/header.m4s'},
            {'url': 'https://example.test/missing.m4s'},
        ],
    }

    assert downloader.real_download('output.mp4', info_dict) is True

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    downloader.report_skip_fragment.assert_called_once_with(2)
    downloader.report_retry_fragment.assert_not_called()
    downloader.report_error.assert_not_called()
    downloader._append_fragment.assert_called_once_with(ctx, b'header')
    downloader._finish_frag_download.assert_called_once_with(ctx)


def test_download_error_skips_nonfatal_fragment_without_retrying():
    downloader = make_downloader({'skip_unavailable_fragments': True})
    downloader._download_fragment.side_effect = [
        (True, b'header'),
        DownloadError('fragment download failed'),
    ]
    info_dict = {
        'fragments': [
            {'url': 'https://example.test/header.m4s'},
            {'url': 'https://example.test/broken.m4s'},
        ],
    }

    assert downloader.real_download('output.mp4', info_dict) is True

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    assert downloader._download_fragment.call_count == 2
    downloader.report_skip_fragment.assert_called_once_with(2)
    downloader.report_retry_fragment.assert_not_called()
    downloader._append_fragment.assert_called_once_with(ctx, b'header')
    downloader._finish_frag_download.assert_called_once_with(ctx)


def test_download_error_is_raised_when_skipping_is_disabled():
    downloader = make_downloader({'skip_unavailable_fragments': False})
    error = DownloadError('fragment download failed')
    downloader._download_fragment.side_effect = [
        (True, b'header'),
        error,
    ]
    info_dict = {
        'fragments': [
            {'url': 'https://example.test/header.m4s'},
            {'url': 'https://example.test/broken.m4s'},
        ],
    }

    with pytest.raises(DownloadError) as exc_info:
        downloader.real_download('output.mp4', info_dict)

    assert exc_info.value is error
    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    downloader._append_fragment.assert_called_once_with(ctx, b'header')
    downloader.report_skip_fragment.assert_not_called()
    downloader._finish_frag_download.assert_not_called()


def test_fragment_without_url_or_base_url_raises_assertion_error():
    downloader = make_downloader()
    info_dict = {
        'fragments': [{'path': 'segment.m4s'}],
    }

    with pytest.raises(AssertionError):
        downloader.real_download('output.mp4', info_dict)

    downloader._download_fragment.assert_not_called()
    downloader._append_fragment.assert_not_called()
    downloader._finish_frag_download.assert_not_called()


def test_empty_fragment_list_finishes_successfully():
    downloader = make_downloader()
    info_dict = {'fragments': []}

    assert downloader.real_download('output.mp4', info_dict) is True

    ctx = downloader._prepare_and_start_frag_download.call_args.args[0]
    assert ctx == {
        'filename': 'output.mp4',
        'total_frags': 0,
        'fragment_index': 0,
    }
    downloader._download_fragment.assert_not_called()
    downloader._append_fragment.assert_not_called()
    downloader._finish_frag_download.assert_called_once_with(ctx)
