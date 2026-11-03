# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for a downloader: only needs a `params` dict."""

    def __init__(self, params=None):
        self.params = params if params is not None else {}


def make_postprocessor(params=None):
    return PostProcessor(FakeDownloader(params))


def test_configuration_args_returns_empty_list_by_default():
    pp = make_postprocessor({})
    result = pp._configuration_args()
    assert result == []
    # The implicit default must not be shared/mutated between calls.
    assert pp._configuration_args() == []


def test_configuration_args_returns_custom_default_when_key_missing():
    pp = make_postprocessor({})
    custom = ['-v', '--no-playlist']
    result = pp._configuration_args(custom)
    assert result is custom
    assert result == ['-v', '--no-playlist']


def test_configuration_args_returns_configured_list():
    configured = ['--merge-output-format', 'mp4']
    pp = make_postprocessor({'postprocessor_args': configured})
    result = pp._configuration_args()
    assert result is configured
    assert result == ['--merge-output-format', 'mp4']
    # A configured list takes precedence over the passed-in default.
    assert pp._configuration_args(['ignored']) == configured


def test_configuration_args_none_value_falls_back_to_default():
    pp = make_postprocessor({'postprocessor_args': None})
    assert pp._configuration_args() == []
    assert pp._configuration_args(['-x']) == ['-x']


def test_configuration_args_rejects_non_list_value():
    pp = make_postprocessor({'postprocessor_args': 'not-a-list'})
    with pytest.raises(AssertionError):
        pp._configuration_args()
