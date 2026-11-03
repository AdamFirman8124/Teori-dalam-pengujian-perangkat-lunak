# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for a YoutubeDL downloader object."""

    def __init__(self, params=None):
        self.params = params if params is not None else {}


def test_configuration_args_no_params_returns_empty_default():
    # 'postprocessor_args' missing from params -> cli_configuration_args
    # returns the (empty) default; exercises line 65 via the None branch.
    pp = PostProcessor(FakeDownloader({}))
    result = pp._configuration_args()
    assert result == []
    assert isinstance(result, list)


def test_configuration_args_custom_default_returned_when_unset():
    # A caller-supplied default must be returned untouched when the
    # parameter is absent from the downloader params.
    pp = PostProcessor(FakeDownloader({}))
    default = ['--verbose', '--no-warnings']
    result = pp._configuration_args(default)
    assert result == default
    assert result is default


def test_configuration_args_returns_value_from_params():
    # 'postprocessor_args' present in params -> the configured list is
    # returned instead of the default; exercises line 65 via the
    # non-None branch of cli_configuration_args.
    args = ['--key', 'value']
    pp = PostProcessor(FakeDownloader({'postprocessor_args': args}))
    result = pp._configuration_args(['--unused-default'])
    assert result == args
    assert result is args


def test_configuration_args_non_list_value_raises_assertion():
    # A non-list value for 'postprocessor_args' must trip the
    # assertion inside cli_configuration_args.
    pp = PostProcessor(FakeDownloader({'postprocessor_args': '--not-a-list'}))
    with pytest.raises(AssertionError):
        pp._configuration_args()


def test_configuration_args_with_downloader_set_after_construction():
    # set_downloader() must also make params available to
    # _configuration_args (line 65 reads self._downloader.params).
    pp = PostProcessor()
    pp.set_downloader(FakeDownloader({'postprocessor_args': ['-x']}))
    assert pp._configuration_args() == ['-x']
