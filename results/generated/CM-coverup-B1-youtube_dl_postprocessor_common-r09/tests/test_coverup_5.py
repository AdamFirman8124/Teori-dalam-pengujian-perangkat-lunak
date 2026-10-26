# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class _FakeDownloader(object):
    """Minimal stand-in exposing only the ``params`` attribute."""

    def __init__(self, params):
        self.params = params


def test_configuration_args_returns_default_when_key_absent():
    pp = PostProcessor(_FakeDownloader({}))
    assert pp._configuration_args() == []
    assert pp._configuration_args(['--default-arg']) == ['--default-arg']


def test_configuration_args_returns_configured_list():
    pp = PostProcessor(_FakeDownloader({'postprocessor_args': ['--a', '--b']}))
    assert pp._configuration_args() == ['--a', '--b']
    # explicit default must be ignored when the param is present
    assert pp._configuration_args(['--ignored']) == ['--a', '--b']


def test_configuration_args_none_value_falls_back_to_default():
    pp = PostProcessor(_FakeDownloader({'postprocessor_args': None}))
    assert pp._configuration_args(['--fallback']) == ['--fallback']


def test_configuration_args_empty_list_is_returned_as_is():
    pp = PostProcessor(_FakeDownloader({'postprocessor_args': []}))
    assert pp._configuration_args(['--fallback']) == []


def test_configuration_args_rejects_non_list_value():
    pp = PostProcessor(_FakeDownloader({'postprocessor_args': '--not-a-list'}))
    with pytest.raises(AssertionError):
        pp._configuration_args()


def test_configuration_args_does_not_mutate_default():
    default = ['--keep']
    pp = PostProcessor(_FakeDownloader({}))
    result = pp._configuration_args(default)
    assert result == ['--keep']
    assert default == ['--keep']
