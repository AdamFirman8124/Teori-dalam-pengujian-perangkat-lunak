# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

from unittest.mock import Mock

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError


def _make_fd(monkeypatch, params=None, fragment_index=0):
    fd = DashSegmentsFD(None, params or {})

    def prepare(ctx):
        ctx["fragment_index"] = fragment_index

    fd._prepare_and_start_frag_download = Mock(side_effect=prepare)
    fd._download_fragment = Mock()
    fd._append_fragment = Mock()
    fd._finish_frag_download = Mock()
    fd.report_retry_fragment = Mock()
    fd.report_skip_fragment = Mock()
    fd.report_error = Mock()

    return fd


def _http_error(code=404):
    return compat_urllib_error.HTTPError(
        "https://example.test/fragment",
        code,
        "Not Found",
        {},
        None,
    )


def test_real_download_downloads_direct_and_relative_fragment_urls(monkeypatch):
    fd = _make_fd(monkeypatch)
    fd._download_fragment.side_effect = [
        (True, b"header"),
        (True, b"media"),
    ]
    info_dict = {
        "fragment_base_url": "https://example.test/media/",
        "fragments": [
            {"url": "https://cdn.example.test/header.m4s"},
            {"path": "segment-1.m4s"},
        ],
    }

    result = fd.real_download("video.mp4", info_dict)

    assert result is True
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx["filename"] == "video.mp4"
    assert ctx["total_frags"] == 2
    assert ctx["fragment_index"] == 0
    assert fd._download_fragment.call_args_list[0].args == (
        ctx,
        "https://cdn.example.test/header.m4s",
        info_dict,
    )
    assert fd._download_fragment.call_args_list[1].args == (
        ctx,
        "https://example.test/media/segment-1.m4s",
        info_dict,
    )
    assert [call.args for call in fd._append_fragment.call_args_list] == [
        (ctx, b"header"),
        (ctx, b"media"),
    ]
    fd._finish_frag_download.assert_called_once_with(ctx)


def test_real_download_test_mode_only_downloads_first_fragment(monkeypatch):
    fd = _make_fd(monkeypatch, {"test": True})
    fd._download_fragment.return_value = (True, b"first")
    info_dict = {
        "fragments": [
            {"url": "https://example.test/first.m4s"},
            {"url": "https://example.test/second.m4s"},
        ],
    }

    result = fd.real_download("test.mp4", info_dict)

    assert result is True
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert ctx["total_frags"] == 1
    fd._download_fragment.assert_called_once_with(
        ctx, "https://example.test/first.m4s", info_dict
    )
    fd._append_fragment.assert_called_once_with(ctx, b"first")
    fd._finish_frag_download.assert_called_once_with(ctx)


def test_real_download_skips_fragments_already_recorded_in_context(monkeypatch):
    fd = _make_fd(monkeypatch, fragment_index=1)
    fd._download_fragment.return_value = (True, b"second")
    info_dict = {
        "fragments": [
            {"url": "https://example.test/first.m4s"},
            {"url": "https://example.test/second.m4s"},
        ],
    }

    result = fd.real_download("resumed.mp4", info_dict)

    assert result is True
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    fd._download_fragment.assert_called_once_with(
        ctx, "https://example.test/second.m4s", info_dict
    )
    fd._append_fragment.assert_called_once_with(ctx, b"second")
    fd._finish_frag_download.assert_called_once_with(ctx)


def test_real_download_returns_false_when_fragment_download_is_unsuccessful(
    monkeypatch,
):
    fd = _make_fd(monkeypatch)
    fd._download_fragment.return_value = (False, None)
    info_dict = {
        "fragments": [{"url": "https://example.test/first.m4s"}],
    }

    result = fd.real_download("video.mp4", info_dict)

    assert result is False
    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()
    fd.report_error.assert_not_called()


def test_real_download_retries_http_error_and_then_succeeds(monkeypatch):
    fd = _make_fd(monkeypatch, {"fragment_retries": 2})
    error = _http_error()
    fd._download_fragment.side_effect = [
        error,
        (True, b"fragment"),
    ]
    info_dict = {
        "fragments": [{"url": "https://example.test/first.m4s"}],
    }

    result = fd.real_download("video.mp4", info_dict)

    assert result is True
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    assert fd._download_fragment.call_count == 2
    fd.report_retry_fragment.assert_called_once_with(error, 1, 1, 2)
    fd._append_fragment.assert_called_once_with(ctx, b"fragment")
    fd._finish_frag_download.assert_called_once_with(ctx)
    fd.report_error.assert_not_called()


def test_real_download_gives_up_after_http_errors_on_first_fragment(monkeypatch):
    fd = _make_fd(monkeypatch, {"fragment_retries": 1})
    first_error = _http_error(500)
    second_error = _http_error(503)
    fd._download_fragment.side_effect = [first_error, second_error]
    info_dict = {
        "fragments": [{"url": "https://example.test/first.m4s"}],
    }

    result = fd.real_download("video.mp4", info_dict)

    assert result is False
    assert fd._download_fragment.call_count == 2
    fd.report_retry_fragment.assert_called_once_with(first_error, 1, 1, 1)
    fd.report_error.assert_called_once_with(
        "giving up after 1 fragment retries"
    )
    fd.report_skip_fragment.assert_not_called()
    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_real_download_skips_later_fragment_after_http_retries_are_exhausted(
    monkeypatch,
):
    fd = _make_fd(monkeypatch, {"fragment_retries": 0})
    error = _http_error()
    fd._download_fragment.side_effect = [
        (True, b"header"),
        error,
    ]
    info_dict = {
        "fragments": [
            {"url": "https://example.test/header.m4s"},
            {"url": "https://example.test/missing.m4s"},
        ],
    }

    result = fd.real_download("video.mp4", info_dict)

    assert result is True
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    fd.report_skip_fragment.assert_called_once_with(2)
    fd.report_retry_fragment.assert_not_called()
    fd.report_error.assert_not_called()
    fd._append_fragment.assert_called_once_with(ctx, b"header")
    fd._finish_frag_download.assert_called_once_with(ctx)


def test_real_download_skips_later_fragment_on_download_error(monkeypatch):
    fd = _make_fd(monkeypatch)
    fd._download_fragment.side_effect = [
        (True, b"header"),
        DownloadError("fragment download failed"),
    ]
    info_dict = {
        "fragments": [
            {"url": "https://example.test/header.m4s"},
            {"url": "https://example.test/media.m4s"},
        ],
    }

    result = fd.real_download("video.mp4", info_dict)

    assert result is True
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    fd.report_skip_fragment.assert_called_once_with(2)
    fd.report_retry_fragment.assert_not_called()
    fd._append_fragment.assert_called_once_with(ctx, b"header")
    fd._finish_frag_download.assert_called_once_with(ctx)


def test_real_download_reraises_download_error_for_first_fragment(monkeypatch):
    fd = _make_fd(monkeypatch)
    error = DownloadError("header download failed")
    fd._download_fragment.side_effect = error
    info_dict = {
        "fragments": [{"url": "https://example.test/header.m4s"}],
    }

    with pytest.raises(DownloadError) as exc_info:
        fd.real_download("video.mp4", info_dict)

    assert exc_info.value is error
    fd.report_skip_fragment.assert_not_called()
    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_real_download_reraises_later_error_when_skipping_is_disabled(
    monkeypatch,
):
    fd = _make_fd(monkeypatch, {"skip_unavailable_fragments": False})
    error = DownloadError("media fragment failed")
    fd._download_fragment.side_effect = [
        (True, b"header"),
        error,
    ]
    info_dict = {
        "fragments": [
            {"url": "https://example.test/header.m4s"},
            {"url": "https://example.test/media.m4s"},
        ],
    }

    with pytest.raises(DownloadError) as exc_info:
        fd.real_download("video.mp4", info_dict)

    assert exc_info.value is error
    ctx = fd._prepare_and_start_frag_download.call_args.args[0]
    fd._append_fragment.assert_called_once_with(ctx, b"header")
    fd.report_skip_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()


def test_real_download_requires_base_url_for_relative_fragment(monkeypatch):
    fd = _make_fd(monkeypatch)
    info_dict = {
        "fragments": [{"path": "segment.m4s"}],
    }

    with pytest.raises(AssertionError):
        fd.real_download("video.mp4", info_dict)

    fd._download_fragment.assert_not_called()
    fd._append_fragment.assert_not_called()
    fd._finish_frag_download.assert_not_called()
