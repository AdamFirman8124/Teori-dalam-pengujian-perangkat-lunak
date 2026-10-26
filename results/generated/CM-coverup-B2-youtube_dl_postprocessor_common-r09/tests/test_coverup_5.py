# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def _make_processor(params):
    """Create a PostProcessor instance without invoking __init__ side effects."""
    pp = PostProcessor.__new__(PostProcessor)

    class FakeDownloader(object):
        def __init__(self, p):
            self.params = p

    pp._downloader = FakeDownloader(params)
    return pp


def test_configuration_args_returns_default_when_missing():
    pp = _make_processor({})
    result = pp._configuration_args()
    assert result == []


def test_configuration_args_returns_configured_args():
    expected = ["-foo", "bar"]
    pp = _make_processor({"postprocessor_args": expected})
    result = pp._configuration_args()
    assert result == expected
    assert result is expected


def test_configuration_args_returns_custom_default_when_missing():
    pp = _make_processor({})
    custom_default = ["-default-opt"]
    result = pp._configuration_args(custom_default)
    assert result == ["-default-opt"]
    assert result is custom_default


def test_configuration_args_ignores_default_when_configured():
    pp = _make_processor({"postprocessor_args": ["-a"]})
    custom_default = ["-b"]
    result = pp._configuration_args(custom_default)
    assert result == ["-a"]
    assert result is not custom_default
