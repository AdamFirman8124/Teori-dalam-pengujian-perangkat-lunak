# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

import io
from unittest.mock import MagicMock

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError


def _http_error(url='http://example.com/frag', code=404):
    """Build a real HTTPError instance without any network interaction."""
    return compat_urllib_error.HTTPError(url, code, 'Not Found', None, io.BytesIO(b''))


def _make_fd(monkeypatch, params=None, fragment_index=0, download_side_effect=None):
    """Build a DashSegmentsFD with every inherited helper mocked out.

    Mocking the FragmentFD/FileDownloader helpers keeps the test focused on
    DashSegmentsFD.real_download and avoids any filesystem or network access,
    so no state pollution is possible.  monkeypatch restores the (instance)
    attributes automatically on teardown.
    """
    ydl = MagicMock()
    fd = DashSegmentsFD(ydl, params=params or {})

    def fake_prepare(ctx):
        ctx['fragment_index'] = fragment_index

    monkeypatch.setattr(
        fd, '_prepare_and_start_frag_download', MagicMock(side_effect=fake_prepare))
    download_mock = MagicMock(return_value=(True, b'frag-data'))
    if download_side_effect is not None:
        download_mock.side_effect = download_side_effect
    monkeypatch.setattr(fd, '_download_fragment', download_mock)
    monkeypatch.setattr(fd, '_append_fragment', MagicMock())
    monkeypatch.setattr(fd, '_finish_frag_download', MagicMock())
    monkeypatch.setattr(fd, 'report_retry_fragment', MagicMock())
    monkeypatch.setattr(fd, 'report_skip_fragment', MagicMock())
    monkeypatch.setattr(fd, 'report_error', MagicMock())
    return fd


def _urls(fd):
    """URLs passed to _download_fragment (2nd positional argument)."""
    return [c[0][1] for c in fd._download_fragment.call_args_list]


def _ctx(fd):
    """The ctx dict real_download built and handed to the prepare hook."""
    return fd._prepare_and_start_frag_download.call_args[0][0]


def test_success_downloads_every_fragment(monkeypatch):
    fd = _make_fd(monkeypatch)
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg0.m4s'},
            {'url': 'http://example.com/seg1.m4s'},
            {'url': 'http://example.com/seg2.m4s'},
        ],
    }

    result = fd.real_download('out.mp4', info_dict)

    assert result is True
    assert _urls(fd) == [
        'http://example.com/seg0.m4s',
        'http://example.com/seg1.m4s',
        'http://example.com/seg2.m4s',
    ]
    assert fd._append_fragment.call_count == 3
    assert all(c[0][1] == b'frag-data' for c in fd._append_fragment.call_args_list)
    ctx = _ctx(fd)
    assert ctx['filename'] == 'out.mp4'
    assert ctx['total_frags'] == 3
    fd._finish_frag_download.assert_called_once_with(ctx)
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()


def test_test_mode_downloads_only_first_fragment(monkeypatch):
    fd = _make_fd(monkeypatch, params={'test': True})
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg0.m4s'},
            {'url': 'http://example.com/seg1.m4s'},
        ],
    }

    result = fd.real_download('out.mp4', info_dict)

    assert result is True
    assert _ctx(fd)['total_frags'] == 1
    assert _urls(fd) == ['http://example.com/seg0.m4s']
    fd._append_fragment.assert_called_once()
    fd._finish_frag_download.assert_called_once()


def test_fragment_url_built_from_base_url_and_path(monkeypatch):
    fd = _make_fd(monkeypatch)
    info_dict = {
        'fragment_base_url': 'http://example.com/base/',
        'fragments': [{'path': 'seg0.m4s'}, {'path': 'seg1.m4s'}],
    }

    result = fd.real_download('out.mp4', info_dict)

    assert result is True
    assert _urls(fd) == [
        'http://example.com/base/seg0.m4s',
        'http://example.com/base/seg1.m4s',
    ]
    fd._finish_frag_download.assert_called_once()


def test_missing_base_url_with_path_only_fragment_raises_assertion(monkeypatch):
    fd = _make_fd(monkeypatch)
    info_dict = {'fragments': [{'path': 'seg0.m4s'}]}

    with pytest.raises(AssertionError):
        fd.real_download('out.mp4', info_dict)

    fd._download_fragment.assert_not_called()
    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_resume_skips_fragments_up_to_fragment_index(monkeypatch):
    fd = _make_fd(monkeypatch, fragment_index=1)
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg0.m4s'},
            {'url': 'http://example.com/seg1.m4s'},
        ],
    }

    result = fd.real_download('out.mp4', info_dict)

    assert result is True
    assert _urls(fd) == ['http://example.com/seg1.m4s']
    fd._append_fragment.assert_called_once()
    fd._finish_frag_download.assert_called_once()


def test_http_error_is_retried_then_download_succeeds(monkeypatch):
    err = _http_error()
    fd = _make_fd(
        monkeypatch,
        params={'fragment_retries': 3},
        download_side_effect=[err, (True, b'frag-data')],
    )
    info_dict = {'fragments': [{'url': 'http://example.com/seg0.m4s'}]}

    result = fd.real_download('out.mp4', info_dict)

    assert result is True
    assert fd._download_fragment.call_count == 2
    fd.report_retry_fragment.assert_called_once_with(err, 1, 1, 3)
    fd._append_fragment.assert_called_once()
    fd._finish_frag_download.assert_called_once()
    fd.report_skip_fragment.assert_not_called()
    fd.report_error.assert_not_called()


def test_http_error_gives_up_on_fatal_first_fragment(monkeypatch):
    err = _http_error()
    fd = _make_fd(
        monkeypatch,
        params={'fragment_retries': 1},
        download_side_effect=[err, err],
    )
    info_dict = {'fragments': [{'url': 'http://example.com/seg0.m4s'}]}

    result = fd.real_download('out.mp4', info_dict)

    assert result is False
    assert fd._download_fragment.call_count == 2
    fd.report_retry_fragment.assert_called_once_with(err, 1, 1, 1)
    fd.report_error.assert_called_once_with('giving up after 1 fragment retries')
    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_http_error_skips_unavailable_nonfatal_fragment(monkeypatch):
    err = _http_error()
    fd = _make_fd(
        monkeypatch,
        params={'fragment_retries': 0},
        download_side_effect=[(True, b'frag-data'), err],
    )
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg0.m4s'},
            {'url': 'http://example.com/seg1.m4s'},
        ],
    }

    result = fd.real_download('out.mp4', info_dict)

    assert result is True
    assert fd._download_fragment.call_count == 2
    fd.report_skip_fragment.assert_called_once_with(2)
    fd.report_retry_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._append_fragment.assert_called_once()
    fd._finish_frag_download.assert_called_once()


def test_download_error_skips_nonfatal_fragment_and_continues(monkeypatch):
    fd = _make_fd(
        monkeypatch,
        download_side_effect=[
            (True, b'frag-data'),
            DownloadError('fragment 2 failed'),
            (True, b'frag-data'),
        ],
    )
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg0.m4s'},
            {'url': 'http://example.com/seg1.m4s'},
            {'url': 'http://example.com/seg2.m4s'},
        ],
    }

    result = fd.real_download('out.mp4', info_dict)

    assert result is True
    assert fd._download_fragment.call_count == 3
    fd.report_skip_fragment.assert_called_once_with(2)
    assert fd._append_fragment.call_count == 2
    fd._finish_frag_download.assert_called_once()
    fd.report_error.assert_not_called()


def test_download_error_on_first_fragment_is_fatal(monkeypatch):
    fd = _make_fd(
        monkeypatch,
        download_side_effect=[DownloadError('fragment 1 failed')],
    )
    info_dict = {'fragments': [{'url': 'http://example.com/seg0.m4s'}]}

    with pytest.raises(DownloadError):
        fd.real_download('out.mp4', info_dict)

    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_download_error_fatal_when_skipping_disabled(monkeypatch):
    fd = _make_fd(
        monkeypatch,
        params={'skip_unavailable_fragments': False},
        download_side_effect=[(True, b'frag-data'), DownloadError('fragment 2 failed')],
    )
    info_dict = {
        'fragments': [
            {'url': 'http://example.com/seg0.m4s'},
            {'url': 'http://example.com/seg1.m4s'},
        ],
    }

    with pytest.raises(DownloadError):
        fd.real_download('out.mp4', info_dict)

    fd.report_skip_fragment.assert_not_called()
    fd._append_fragment.assert_called_once()
    fd._finish_frag_download.assert_not_called()


def test_failed_fragment_download_returns_false(monkeypatch):
    fd = _make_fd(monkeypatch, download_side_effect=[(False, None)])
    info_dict = {'fragments': [{'url': 'http://example.com/seg0.m4s'}]}

    result = fd.real_download('out.mp4', info_dict)

    assert result is False
    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()
