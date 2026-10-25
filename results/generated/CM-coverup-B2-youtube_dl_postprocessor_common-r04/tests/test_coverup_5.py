# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

from types import SimpleNamespace

from youtube_dl.postprocessor.common import PostProcessor


def _make_pp(params):
    downloader = SimpleNamespace(params=params)
    return PostProcessor(downloader)


def test_configuration_args_returns_empty_list_default_when_missing():
    pp = _make_pp({})
    result = pp._configuration_args()
    assert result == []


def test_configuration_args_returns_custom_default_when_missing():
    custom_default = ["--default-opt", "123"]
    pp = _make_pp({})
    result = pp._configuration_args(custom_default)
    assert result == ["--default-opt", "123"]
    assert result is custom_default


def test_configuration_args_returns_postprocessor_args_when_present():
    configured = ["--opt1", "val1", "--opt2"]
    pp = _make_pp({"postprocessor_args": configured})
    result = pp._configuration_args()
    assert result == ["--opt1", "val1", "--opt2"]
    assert result is configured


def test_configuration_args_ignores_default_when_present():
    configured = ["--a"]
    custom_default = ["--b"]
    pp = _make_pp({"postprocessor_args": configured})
    result = pp._configuration_args(custom_default)
    assert result == ["--a"]
    assert result is configured
