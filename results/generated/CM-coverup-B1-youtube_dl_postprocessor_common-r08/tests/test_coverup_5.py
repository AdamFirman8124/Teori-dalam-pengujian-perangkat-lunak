# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

from types import SimpleNamespace

from youtube_dl.postprocessor.common import PostProcessor


def _make_pp(params):
    pp = PostProcessor.__new__(PostProcessor)
    pp._downloader = SimpleNamespace(params=dict(params))
    return pp


def test_configuration_args_returns_empty_list_by_default():
    pp = _make_pp({})
    result = pp._configuration_args()
    assert result == []


def test_configuration_args_returns_default_when_missing():
    pp = _make_pp({})
    default = ["-foo", "bar"]
    result = pp._configuration_args(default)
    assert result == ["-foo", "bar"]
    assert result is default


def test_configuration_args_returns_configured_args():
    configured = ["-ss", "10", "-t", "5"]
    pp = _make_pp({"postprocessor_args": configured})
    result = pp._configuration_args()
    assert result == ["-ss", "10", "-t", "5"]
    assert result is configured


def test_configuration_args_prefers_params_over_default(monkeypatch):
    configured = ["-x"]
    pp = _make_pp({})
    monkeypatch.setattr(pp._downloader, "params", {"postprocessor_args": configured})
    default = ["default-arg"]
    result = pp._configuration_args(default)
    assert result == ["-x"]
    assert result is configured
    assert result is not default
