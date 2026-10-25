# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    pass


def _make_pp(monkeypatch, params):
    downloader = FakeDownloader()
    monkeypatch.setattr(downloader, 'params', params, raising=False)
    return PostProcessor(downloader)


def test_configuration_args_returns_default_when_key_missing(monkeypatch):
    pp = _make_pp(monkeypatch, {})
    assert pp._configuration_args(['--default']) == ['--default']


def test_configuration_args_returns_empty_list_default(monkeypatch):
    pp = _make_pp(monkeypatch, {})
    assert pp._configuration_args() == []


def test_configuration_args_returns_configured_list(monkeypatch):
    configured = ['--audio-quality', '0']
    pp = _make_pp(monkeypatch, {'postprocessor_args': configured})
    assert pp._configuration_args(['--default']) == configured


def test_configuration_args_none_returns_default(monkeypatch):
    pp = _make_pp(monkeypatch, {'postprocessor_args': None})
    assert pp._configuration_args(['--default']) == ['--default']


def test_configuration_args_rejects_non_list(monkeypatch):
    pp = _make_pp(monkeypatch, {'postprocessor_args': 'not-a-list'})
    with pytest.raises(AssertionError):
        pp._configuration_args()
