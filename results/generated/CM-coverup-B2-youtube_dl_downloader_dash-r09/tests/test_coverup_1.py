# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

from unittest.mock import Mock, call

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError


def make_downloader(monkeypatch, params=None, fragment_index=0):
    downloader = DashSegmentsFD.__new__(DashSegmentsFD)
    downloader.params = params or {}

    def prepare(ctx):
        ctx["fragment_index"] = fragment_index

    mocks = {
        "prepare": Mock(side_effect=prepare),
        "download": Mock(),
        "append": Mock(),
        "finish": Mock(),
        "retry": Mock(),
        "skip": Mock(),
        "error": Mock(),
    }
    monkeypatch.setattr(
        downloader, "_prepare_and_start_frag_download", mocks["prepare"]
    )
    monkeypatch.setattr(downloader, "_download_fragment", mocks["download"])
    monkeypatch.setattr(downloader, "_append_fragment", mocks["append"])
    monkeypatch.setattr(downloader, "_finish_frag_download", mocks["finish"])
    monkeypatch.setattr(downloader, "report_retry_fragment", mocks["retry"])
    monkeypatch.setattr(downloader, "report_skip_fragment", mocks["skip"])
    monkeypatch.setattr(downloader, "report_error", mocks["error"])
    return downloader, mocks


def http_error():
    return compat_urllib_error.HTTPError(
        "https://example.test/segment", 404, "Not Found", {}, None
    )


def test_real_download_downloads_url_and_path_fragments(monkeypatch):
    downloader, mocks = make_downloader(monkeypatch)
    info_dict = {
        "fragment_base_url": "https://example.test/media/",
        "fragments": [
            {"url": "https://cdn.example.test/segment-1"},
            {"path": "segment-2"},
        ],
    }
    mocks["download"].side_effect = [(True, b"first"), (True, b"second")]

    assert downloader.real_download("video.mp4", info_dict) is True

    ctx = mocks["prepare"].call_args.args[0]
    assert ctx["filename"] == "video.mp4"
    assert ctx["total_frags"] == 2
    assert ctx["fragment_index"] == 0
    assert mocks["download"].call_args_list == [
        call(ctx, "https://cdn.example.test/segment-1", info_dict),
        call(ctx, "https://example.test/media/segment-2", info_dict),
    ]
    assert mocks["append"].call_args_list == [
        call(ctx, b"first"),
        call(ctx, b"second"),
    ]
    mocks["finish"].assert_called_once_with(ctx)
    mocks["error"].assert_not_called()


def test_real_download_test_mode_limits_fragments_and_resumes(monkeypatch):
    downloader, mocks = make_downloader(
        monkeypatch, {"test": True}, fragment_index=1
    )
    info_dict = {
        "fragments": [
            {"url": "https://example.test/segment-1"},
            {"url": "https://example.test/segment-2"},
        ]
    }

    assert downloader.real_download("video.mp4", info_dict) is True

    ctx = mocks["prepare"].call_args.args[0]
    assert ctx["total_frags"] == 1
    mocks["download"].assert_not_called()
    mocks["append"].assert_not_called()
    mocks["finish"].assert_called_once_with(ctx)


def test_real_download_returns_false_when_fragment_download_fails(monkeypatch):
    downloader, mocks = make_downloader(monkeypatch)
    info_dict = {
        "fragments": [{"url": "https://example.test/segment"}],
    }
    mocks["download"].return_value = (False, None)

    assert downloader.real_download("video.mp4", info_dict) is False

    mocks["download"].assert_called_once()
    mocks["append"].assert_not_called()
    mocks["finish"].assert_not_called()


def test_real_download_retries_http_error_then_succeeds(monkeypatch):
    downloader, mocks = make_downloader(
        monkeypatch, {"fragment_retries": 1}
    )
    info_dict = {
        "fragments": [{"url": "https://example.test/segment"}],
    }
    error = http_error()
    mocks["download"].side_effect = [error, (True, b"content")]

    assert downloader.real_download("video.mp4", info_dict) is True

    assert mocks["download"].call_count == 2
    mocks["retry"].assert_called_once_with(error, 1, 1, 1)
    ctx = mocks["prepare"].call_args.args[0]
    mocks["append"].assert_called_once_with(ctx, b"content")
    mocks["finish"].assert_called_once_with(ctx)
    mocks["skip"].assert_not_called()


def test_real_download_skips_nonfatal_fragment_after_http_retries(monkeypatch):
    downloader, mocks = make_downloader(
        monkeypatch,
        {
            "fragment_retries": 1,
            "skip_unavailable_fragments": True,
        },
    )
    info_dict = {
        "fragments": [
            {"url": "https://example.test/segment-1"},
            {"url": "https://example.test/segment-2"},
            {"url": "https://example.test/segment-3"},
        ]
    }
    error = http_error()
    mocks["download"].side_effect = [
        (True, b"first"),
        error,
        error,
        (True, b"third"),
    ]

    assert downloader.real_download("video.mp4", info_dict) is True

    mocks["retry"].assert_called_once_with(error, 2, 1, 1)
    mocks["skip"].assert_called_once_with(2)
    ctx = mocks["prepare"].call_args.args[0]
    assert mocks["append"].call_args_list == [
        call(ctx, b"first"),
        call(ctx, b"third"),
    ]
    mocks["finish"].assert_called_once_with(ctx)
    mocks["error"].assert_not_called()


def test_real_download_gives_up_on_first_fragment_http_error(monkeypatch):
    downloader, mocks = make_downloader(
        monkeypatch, {"fragment_retries": 0}
    )
    info_dict = {
        "fragments": [{"url": "https://example.test/segment"}],
    }
    mocks["download"].side_effect = http_error()

    assert downloader.real_download("video.mp4", info_dict) is False

    mocks["retry"].assert_not_called()
    mocks["skip"].assert_not_called()
    mocks["error"].assert_called_once_with(
        "giving up after 0 fragment retries"
    )
    mocks["append"].assert_not_called()
    mocks["finish"].assert_not_called()


def test_real_download_skips_nonfatal_download_error(monkeypatch):
    downloader, mocks = make_downloader(monkeypatch)
    info_dict = {
        "fragments": [
            {"url": "https://example.test/segment-1"},
            {"url": "https://example.test/segment-2"},
            {"url": "https://example.test/segment-3"},
        ]
    }
    mocks["download"].side_effect = [
        (True, b"first"),
        DownloadError("unavailable"),
        (True, b"third"),
    ]

    assert downloader.real_download("video.mp4", info_dict) is True

    mocks["skip"].assert_called_once_with(2)
    ctx = mocks["prepare"].call_args.args[0]
    assert mocks["append"].call_args_list == [
        call(ctx, b"first"),
        call(ctx, b"third"),
    ]
    mocks["finish"].assert_called_once_with(ctx)
    mocks["error"].assert_not_called()


def test_real_download_reraises_first_fragment_download_error(monkeypatch):
    downloader, mocks = make_downloader(monkeypatch)
    info_dict = {
        "fragments": [{"url": "https://example.test/segment"}],
    }
    error = DownloadError("fatal")
    mocks["download"].side_effect = error

    with pytest.raises(DownloadError) as exc_info:
        downloader.real_download("video.mp4", info_dict)

    assert exc_info.value is error
    mocks["skip"].assert_not_called()
    mocks["append"].assert_not_called()
    mocks["finish"].assert_not_called()


def test_real_download_reraises_later_error_when_skipping_disabled(monkeypatch):
    downloader, mocks = make_downloader(
        monkeypatch, {"skip_unavailable_fragments": False}
    )
    info_dict = {
        "fragments": [
            {"url": "https://example.test/segment-1"},
            {"url": "https://example.test/segment-2"},
        ]
    }
    error = DownloadError("fatal later fragment")
    mocks["download"].side_effect = [(True, b"first"), error]

    with pytest.raises(DownloadError) as exc_info:
        downloader.real_download("video.mp4", info_dict)

    assert exc_info.value is error
    ctx = mocks["prepare"].call_args.args[0]
    mocks["append"].assert_called_once_with(ctx, b"first")
    mocks["skip"].assert_not_called()
    mocks["finish"].assert_not_called()


def test_real_download_requires_base_url_for_path_fragment(monkeypatch):
    downloader, mocks = make_downloader(monkeypatch)
    info_dict = {
        "fragments": [{"path": "segment"}],
    }

    with pytest.raises(AssertionError):
        downloader.real_download("video.mp4", info_dict)

    mocks["download"].assert_not_called()
    mocks["append"].assert_not_called()
    mocks["finish"].assert_not_called()
