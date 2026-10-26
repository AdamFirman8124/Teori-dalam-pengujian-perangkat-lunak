# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for YoutubeDL: PostProcessor only needs .params."""

    def __init__(self, params=None):
        self.params = {} if params is None else params


def test_configuration_args_returns_default_when_key_missing():
    pp = PostProcessor(FakeDownloader({}))
    default = ['-x', '--audio-format=mp3']
    result = pp._configuration_args(default)
    assert result == default
    assert result is default


def test_configuration_args_uses_implicit_empty_default():
    pp = PostProcessor(FakeDownloader({}))
    assert pp._configuration_args() == []


def test_configuration_args_returns_configured_args():
    configured = ['-a', '1', '--foo']
    pp = PostProcessor(FakeDownloader({'postprocessor_args': configured}))
    result = pp._configuration_args(['-default'])
    assert result == configured
    assert result is configured


def test_configuration_args_none_value_falls_back_to_default():
    pp = PostProcessor(FakeDownloader({'postprocessor_args': None}))
    default = ['-d']
    result = pp._configuration_args(default)
    assert result == default
    assert result is default


def test_configuration_args_rejects_non_list_value():
    pp = PostProcessor(FakeDownloader({'postprocessor_args': '-a 1'}))
    with pytest.raises(AssertionError):
        pp._configuration_args()


def test_configuration_args_reads_params_via_monkeypatch(monkeypatch):
    downloader = FakeDownloader()
    monkeypatch.setattr(downloader, 'params', {'postprocessor_args': ['--patched']})
    pp = PostProcessor(downloader)
    assert pp._configuration_args(['-default']) == ['--patched']
    # monkeypatch restores the original params dict after the test
