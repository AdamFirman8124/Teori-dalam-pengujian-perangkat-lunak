# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

"""Coverage tests for youtube_dl.downloader.dash.DashSegmentsFD.real_download.

The fragment plumbing inherited from FragmentFD (HTTP downloads, file I/O,
progress reporting) is stubbed out with monkeypatch, so the tests exercise
exactly the logic of real_download() itself without touching the network or
the filesystem.  All interactions are recorded so postconditions can be
asserted precisely.
"""

import io
from collections import defaultdict
from unittest.mock import MagicMock

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError

FRAG_CONTENT = b'fragment-bytes'


def _http_error():
    """Build a genuine urllib HTTPError (404) to trigger the retry path."""
    return compat_urllib_error.HTTPError(
        'http://example.com/frag', 404, 'Not Found', {}, io.BytesIO(b''))


def _make_fd(monkeypatch, params, fragment_index=0, download_results=None):
    """Build a DashSegmentsFD whose fragment plumbing is stubbed out.

    ``fragment_index`` simulates a (partially) resumed download.
    ``download_results`` is a list of outcomes consumed by each
    ``_download_fragment`` call; an outcome may be an exception to raise or a
    ``(success, frag_content)`` tuple.  When exhausted, downloads succeed.
    """
    fd = DashSegmentsFD(MagicMock(), params)
    calls = defaultdict(list)

    def fake_prepare(ctx):
        calls['prepare'].append(dict(ctx))
        ctx['fragment_index'] = fragment_index

    def fake_download(ctx, url, info_dict):
        calls['download'].append(url)
        if download_results:
            outcome = download_results.pop(0)
        else:
            outcome = (True, FRAG_CONTENT)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    def fake_append(ctx, frag_content):
        calls['append'].append(frag_content)

    def fake_finish(ctx):
        calls['finish'].append(dict(ctx))

    def fake_report_retry(err, frag_index, count, retries):
        calls['retry'].append((err, frag_index, count, retries))

    def fake_report_skip(frag_index):
        calls['skip'].append(frag_index)

    def fake_report_error(message):
        calls['error'].append(message)

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, 'report_retry_fragment', fake_report_retry)
    monkeypatch.setattr(fd, 'report_skip_fragment', fake_report_skip)
    monkeypatch.setattr(fd, 'report_error', fake_report_error)
    fd.calls = calls
    return fd


def test_successful_download_downloads_all_fragments(monkeypatch):
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg-1'},
            {'url': 'http://example.com/seg-2'},
        ],
    }
    fd = _make_fd(monkeypatch, {})

    assert fd.real_download('video.mp4', info_dict) is True

    assert fd.calls['prepare'][0]['filename'] == 'video.mp4'
    assert fd.calls['prepare'][0]['total_frags'] == 2
    assert fd.calls['download'] == [
        'http://example.com/seg-1', 'http://example.com/seg-2']
    assert fd.calls['append'] == [FRAG_CONTENT, FRAG_CONTENT]
    assert len(fd.calls['finish']) == 1
    assert fd.calls['retry'] == []
    assert fd.calls['skip'] == []
    assert fd.calls['error'] == []


def test_test_mode_downloads_only_the_first_fragment(monkeypatch):
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg-1'},
            {'url': 'http://example.com/seg-2'},
        ],
    }
    fd = _make_fd(monkeypatch, {'test': True})

    assert fd.real_download('video.mp4', info_dict) is True

    assert fd.calls['prepare'][0]['total_frags'] == 1
    assert fd.calls['download'] == ['http://example.com/seg-1']
    assert len(fd.calls['finish']) == 1


def test_fragment_url_is_joined_from_base_url_and_path(monkeypatch):
    info_dict = {
        'fragment_base_url': 'http://example.com/base/',
        'fragments': [{'path': 'seg-1.m4s'}],
    }
    fd = _make_fd(monkeypatch, {})

    assert fd.real_download('video.mp4', info_dict) is True

    assert fd.calls['download'] == ['http://example.com/base/seg-1.m4s']
    assert fd.calls['append'] == [FRAG_CONTENT]
    assert len(fd.calls['finish']) == 1


def test_missing_base_url_with_path_only_fragment_asserts(monkeypatch):
    info_dict = {'fragments': [{'path': 'seg-1.m4s'}]}
    fd = _make_fd(monkeypatch, {})

    with pytest.raises(AssertionError):
        fd.real_download('video.mp4', info_dict)

    assert fd.calls['download'] == []
    assert fd.calls['finish'] == []


def test_failed_fragment_download_returns_false(monkeypatch):
    info_dict = {'fragments': [{'url': 'http://example.com/seg-1'}]}
    fd = _make_fd(monkeypatch, {}, download_results=[(False, None)])

    assert fd.real_download('video.mp4', info_dict) is False

    assert fd.calls['download'] == ['http://example.com/seg-1']
    assert fd.calls['append'] == []
    assert fd.calls['finish'] == []


def test_http_error_is_retried_until_success(monkeypatch):
    info_dict = {'fragments': [{'url': 'http://example.com/seg-1'}]}
    err = _http_error()
    fd = _make_fd(
        monkeypatch, {'fragment_retries': 2},
        download_results=[err, (True, FRAG_CONTENT)])

    assert fd.real_download('video.mp4', info_dict) is True

    assert len(fd.calls['download']) == 2
    assert fd.calls['retry'] == [(err, 1, 1, 2)]
    assert fd.calls['append'] == [FRAG_CONTENT]
    assert len(fd.calls['finish']) == 1


def test_http_error_gives_up_on_fatal_first_fragment(monkeypatch):
    info_dict = {'fragments': [{'url': 'http://example.com/seg-1'}]}
    err1, err2 = _http_error(), _http_error()
    fd = _make_fd(
        monkeypatch, {'fragment_retries': 1},
        download_results=[err1, err2])

    assert fd.real_download('video.mp4', info_dict) is False

    assert len(fd.calls['download']) == 2
    # Only the first failure is reported as a retry; the second exhausts the
    # retry budget (count=2 > retries=1) and is not reported.
    assert fd.calls['retry'] == [(err1, 1, 1, 1)]
    assert fd.calls['error'] == ['giving up after 1 fragment retries']
    assert fd.calls['finish'] == []


def test_http_error_on_unavailable_fragment_is_skipped(monkeypatch):
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg-1'},
            {'url': 'http://example.com/seg-2'},
        ],
    }
    fd = _make_fd(
        monkeypatch, {'fragment_retries': 0},
        download_results=[(True, FRAG_CONTENT), _http_error()])

    assert fd.real_download('video.mp4', info_dict) is True

    assert fd.calls['download'] == [
        'http://example.com/seg-1', 'http://example.com/seg-2']
    assert fd.calls['skip'] == [2]
    assert fd.calls['error'] == []
    assert len(fd.calls['finish']) == 1


def test_download_error_on_unavailable_fragment_is_skipped(monkeypatch):
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg-1'},
            {'url': 'http://example.com/seg-2'},
        ],
    }
    fd = _make_fd(
        monkeypatch, {},
        download_results=[(True, FRAG_CONTENT), DownloadError('boom')])

    assert fd.real_download('video.mp4', info_dict) is True

    assert fd.calls['download'] == [
        'http://example.com/seg-1', 'http://example.com/seg-2']
    assert fd.calls['skip'] == [2]
    assert fd.calls['error'] == []
    assert len(fd.calls['finish']) == 1


def test_download_error_on_first_fragment_is_fatal(monkeypatch):
    info_dict = {'fragments': [{'url': 'http://example.com/seg-1'}]}
    fd = _make_fd(monkeypatch, {}, download_results=[DownloadError('boom')])

    with pytest.raises(DownloadError):
        fd.real_download('video.mp4', info_dict)

    assert fd.calls['finish'] == []


def test_download_error_is_fatal_when_skipping_is_disabled(monkeypatch):
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg-1'},
            {'url': 'http://example.com/seg-2'},
        ],
    }
    fd = _make_fd(
        monkeypatch, {'skip_unavailable_fragments': False},
        download_results=[(True, FRAG_CONTENT), DownloadError('boom')])

    with pytest.raises(DownloadError):
        fd.real_download('video.mp4', info_dict)

    assert fd.calls['skip'] == []
    assert fd.calls['finish'] == []


def test_resume_skips_fragments_up_to_fragment_index(monkeypatch):
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg-1'},
            {'url': 'http://example.com/seg-2'},
            {'url': 'http://example.com/seg-3'},
        ],
    }
    fd = _make_fd(monkeypatch, {}, fragment_index=2)

    assert fd.real_download('video.mp4', info_dict) is True

    # Fragments 1 and 2 are silently skipped (already downloaded); only
    # fragment 3 is fetched.
    assert fd.calls['download'] == ['http://example.com/seg-3']
    assert fd.calls['skip'] == []
    assert fd.calls['append'] == [FRAG_CONTENT]
    assert len(fd.calls['finish']) == 1
