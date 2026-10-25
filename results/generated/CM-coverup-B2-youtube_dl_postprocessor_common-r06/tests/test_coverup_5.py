# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class _FakeDownloader(object):
    def __init__(self, params):
        self.params = params


def test_configuration_args_returns_default_when_param_missing(monkeypatch):
    pp = PostProcessor()
    monkeypatch.setattr(pp, '_downloader', _FakeDownloader({}), raising=False)

    default = ['-x', '--audio-format', 'mp3']
    result = pp._configuration_args(default)

    assert result is default
    assert result == ['-x', '--audio-format', 'mp3']


def test_configuration_args_returns_default_when_param_is_none(monkeypatch):
    pp = PostProcessor()
    monkeypatch.setattr(
        pp, '_downloader', _FakeDownloader({'postprocessor_args': None}), raising=False)

    default = ['--embed-thumbnail']
    result = pp._configuration_args(default)

    assert result is default
    assert result == ['--embed-thumbnail']


def test_configuration_args_returns_configured_list(monkeypatch):
    configured = ['--ffmpeg-location', '/usr/bin/ffmpeg']
    pp = PostProcessor()
    monkeypatch.setattr(
        pp, '_downloader',
        _FakeDownloader({'postprocessor_args': configured}), raising=False)

    result = pp._configuration_args(['--ignored'])

    assert result is configured
    assert result == ['--ffmpeg-location', '/usr/bin/ffmpeg']


def test_configuration_args_uses_empty_list_default(monkeypatch):
    pp = PostProcessor()
    monkeypatch.setattr(pp, '_downloader', _FakeDownloader({}), raising=False)

    result = pp._configuration_args()

    assert result == []
    assert isinstance(result, list)


def test_configuration_args_rejects_non_list_value(monkeypatch):
    pp = PostProcessor()
    monkeypatch.setattr(
        pp, '_downloader',
        _FakeDownloader({'postprocessor_args': 'not-a-list'}), raising=False)

    with pytest.raises(AssertionError):
        pp._configuration_args([])
