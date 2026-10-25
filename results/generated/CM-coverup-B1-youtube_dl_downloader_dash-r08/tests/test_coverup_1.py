# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

import pytest
from youtube_dl.compat import compat_urllib_error
from youtube_dl.utils import DownloadError
from youtube_dl.downloader.dash import DashSegmentsFD


def _new_fd(params):
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = dict(params)
    return fd


def test_dash_test_mode_single_fragment(monkeypatch, tmp_path):
    fd = _new_fd({"test": True})
    out = str(tmp_path / "out.mp4")
    info = {
        "fragments": [
            {"url": "http://example.com/frag1"},
            {"url": "http://example.com/frag2"},
            {"url": "http://example.com/frag3"},
        ]
    }
    seen_urls = []

    def fake_prepare(ctx):
        assert ctx["filename"] == out
        assert ctx["total_frags"] == 1
        ctx["fragment_index"] = 0

    def fake_dl(ctx, url, info_dict):
        seen_urls.append(url)
        return (True, b"data1")

    appended = []
    finished = []

    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: appended.append(c))
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: finished.append(True))

    res = fd.real_download(out, info)
    assert res is True
    assert seen_urls == ["http://example.com/frag1"]
    assert appended == [b"data1"]
    assert finished == [True]


def test_dash_path_uses_fragment_base_url(monkeypatch, tmp_path):
    fd = _new_fd({})
    out = str(tmp_path / "out.mp4")
    info = {
        "fragment_base_url": "http://example.com/base/",
        "fragments": [{"path": "seg1.m4s"}],
    }
    seen = []

    def fake_prepare(ctx):
        ctx["fragment_index"] = 0

    def fake_dl(ctx, url, info_dict):
        seen.append(url)
        return (True, b"segdata")

    appended = []
    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: appended.append(c))
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: None)

    res = fd.real_download(out, info)
    assert res is True
    assert len(seen) == 1
    assert seen[0] == "http://example.com/base/seg1.m4s"
    assert appended == [b"segdata"]


def test_dash_resume_skips_done_fragment(monkeypatch, tmp_path):
    fd = _new_fd({})
    out = str(tmp_path / "out.mp4")
    info = {
        "fragments": [
            {"url": "http://example.com/frag1"},
            {"url": "http://example.com/frag2"},
        ]
    }
    seen = []

    def fake_prepare(ctx):
        assert ctx["total_frags"] == 2
        ctx["fragment_index"] = 1

    def fake_dl(ctx, url, info_dict):
        seen.append(url)
        return (True, b"x")

    appended = []
    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: appended.append(c))
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: None)

    res = fd.real_download(out, info)
    assert res is True
    assert seen == ["http://example.com/frag2"]
    assert appended == [b"x"]


def test_dash_unsuccessful_download_returns_false(monkeypatch, tmp_path):
    fd = _new_fd({})
    out = str(tmp_path / "out.mp4")
    info = {"fragments": [{"url": "http://example.com/frag1"}]}

    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", lambda ctx: ctx.update({"fragment_index": 0}))
    monkeypatch.setattr(fd, "_download_fragment", lambda ctx, url, d: (False, None))
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: pytest.fail("should not append"))
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: pytest.fail("should not finish"))

    res = fd.real_download(out, info)
    assert res is False


def test_dash_http_error_retry_then_success(monkeypatch, tmp_path):
    fd = _new_fd({"fragment_retries": 1})
    out = str(tmp_path / "out.mp4")
    info = {"fragments": [{"url": "http://example.com/frag1"}]}
    calls = {"n": 0}
    retries = []

    def fake_prepare(ctx):
        ctx["fragment_index"] = 0

    def fake_dl(ctx, url, info_dict):
        calls["n"] += 1
        if calls["n"] == 1:
            raise compat_urllib_error.HTTPError(url, 404, "Not Found", {}, None)
        return (True, b"ok")

    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: None)
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: None)
    monkeypatch.setattr(fd, "report_retry_fragment", lambda e, fi, c, r: retries.append((fi, c, r)))

    res = fd.real_download(out, info)
    assert res is True
    assert calls["n"] == 2
    assert retries == [(1, 1, 1)]


def test_dash_http_error_exhausted_skip_nonfatal(monkeypatch, tmp_path):
    fd = _new_fd({"fragment_retries": 0})
    out = str(tmp_path / "out.mp4")
    info = {
        "fragments": [
            {"url": "http://example.com/frag1"},
            {"url": "http://example.com/frag2"},
        ]
    }
    skips = []
    finished = []

    def fake_prepare(ctx):
        ctx["fragment_index"] = 0

    def fake_dl(ctx, url, info_dict):
        if url.endswith("frag2"):
            raise compat_urllib_error.HTTPError(url, 404, "Not Found", {}, None)
        return (True, b"d1")

    appended = []
    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: appended.append(c))
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: finished.append(True))
    monkeypatch.setattr(fd, "report_retry_fragment", lambda *a: pytest.fail("no retry expected"))
    monkeypatch.setattr(fd, "report_skip_fragment", lambda fi: skips.append(fi))

    res = fd.real_download(out, info)
    assert res is True
    assert appended == [b"d1"]
    assert skips == [2]
    assert finished == [True]


def test_dash_http_error_give_up_fatal(monkeypatch, tmp_path):
    fd = _new_fd({"fragment_retries": 1})
    out = str(tmp_path / "out.mp4")
    info = {"fragments": [{"url": "http://example.com/frag1"}]}
    retries = []
    errors = []

    def fake_prepare(ctx):
        ctx["fragment_index"] = 0

    def fake_dl(ctx, url, info_dict):
        raise compat_urllib_error.HTTPError(url, 500, "Error", {}, None)

    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: pytest.fail("no append"))
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: pytest.fail("no finish"))
    monkeypatch.setattr(fd, "report_retry_fragment", lambda e, fi, c, r: retries.append(c))
    monkeypatch.setattr(fd, "report_error", lambda msg, *a, **k: errors.append(msg))

    res = fd.real_download(out, info)
    assert res is False
    assert retries == [1]
    assert len(errors) == 1
    assert "giving up after 1 fragment retries" in errors[0]


def test_dash_download_error_skip_nonfatal(monkeypatch, tmp_path):
    fd = _new_fd({"skip_unavailable_fragments": True})
    out = str(tmp_path / "out.mp4")
    info = {
        "fragments": [
            {"url": "http://example.com/frag1"},
            {"url": "http://example.com/frag2"},
        ]
    }
    skips = []

    def fake_prepare(ctx):
        ctx["fragment_index"] = 0

    def fake_dl(ctx, url, info_dict):
        if url.endswith("frag2"):
            raise DownloadError("net fail")
        return (True, b"first")

    appended = []
    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: appended.append(c))
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: None)
    monkeypatch.setattr(fd, "report_skip_fragment", lambda fi: skips.append(fi))

    res = fd.real_download(out, info)
    assert res is True
    assert appended == [b"first"]
    assert skips == [2]


def test_dash_download_error_fatal_raise(monkeypatch, tmp_path):
    fd = _new_fd({})
    out = str(tmp_path / "out.mp4")
    info = {"fragments": [{"url": "http://example.com/frag1"}]}

    def fake_prepare(ctx):
        ctx["fragment_index"] = 0

    def fake_dl(ctx, url, info_dict):
        raise DownloadError("fatal net fail")

    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: None)
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: None)

    with pytest.raises(DownloadError):
        fd.real_download(out, info)


def test_dash_skip_false_makes_second_fatal(monkeypatch, tmp_path):
    fd = _new_fd({"skip_unavailable_fragments": False, "fragment_retries": 0})
    out = str(tmp_path / "out.mp4")
    info = {
        "fragments": [
            {"url": "http://example.com/frag1"},
            {"url": "http://example.com/frag2"},
        ]
    }
    errors = []

    def fake_prepare(ctx):
        ctx["fragment_index"] = 0

    def fake_dl(ctx, url, info_dict):
        if url.endswith("frag2"):
            raise compat_urllib_error.HTTPError(url, 404, "Not Found", {}, None)
        return (True, b"d1")

    monkeypatch.setattr(fd, "_prepare_and_start_frag_download", fake_prepare)
    monkeypatch.setattr(fd, "_download_fragment", fake_dl)
    monkeypatch.setattr(fd, "_append_fragment", lambda ctx, c: None)
    monkeypatch.setattr(fd, "_finish_frag_download", lambda ctx: pytest.fail("no finish"))
    monkeypatch.setattr(fd, "report_error", lambda msg, *a, **k: errors.append(msg))

    res = fd.real_download(out, info)
    assert res is False
    assert len(errors) == 1
