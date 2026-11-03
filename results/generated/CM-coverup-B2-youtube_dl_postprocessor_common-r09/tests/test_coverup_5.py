# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for a downloader exposing a `params` dict."""

    def __init__(self, params=None):
        self.params = params if params is not None else {}


@pytest.fixture
def make_pp():
    """Factory fixture creating PostProcessor instances; cleans them up afterwards."""
    created = []

    def _make(params=None):
        pp = PostProcessor(FakeDownloader(params))
        created.append(pp)
        return pp

    yield _make

    created.clear()


def test_configuration_args_default_empty(make_pp):
    # No 'postprocessor_args' in params -> the implicit default ([]) is returned.
    pp = make_pp({})
    result = pp._configuration_args()
    assert result == []
    assert isinstance(result, list)


def test_configuration_args_custom_default(make_pp):
    # No 'postprocessor_args' in params -> the explicitly passed default is returned.
    pp = make_pp({})
    default = ['--verbose', '--keep-video']
    result = pp._configuration_args(default)
    assert result == default
    assert result is default  # default is passed through unchanged


def test_configuration_args_from_params(make_pp):
    # 'postprocessor_args' present in params -> those args are returned.
    args = ['--write-sub', '--sub-lang', 'en']
    pp = make_pp({'postprocessor_args': args})
    result = pp._configuration_args()
    assert result == args
    assert result is args  # the configured list is returned as-is


def test_configuration_args_params_take_precedence_over_default(make_pp):
    # 'postprocessor_args' present -> configured args win over the passed default.
    args = ['--embed-subs']
    pp = make_pp({'postprocessor_args': args})
    result = pp._configuration_args(['--ignored-default'])
    assert result == args
    assert result is args
