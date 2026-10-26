# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


class _FakeDownloader:
    def __init__(self, params):
        self.params = params


def test_configuration_args_returns_empty_default_when_missing():
    downloader = _FakeDownloader(params={})
    pp = PostProcessor(downloader)
    result = pp._configuration_args()
    assert result == []


def test_configuration_args_returns_custom_default_when_missing():
    downloader = _FakeDownloader(params={})
    pp = PostProcessor(downloader)
    custom_default = ["--foo", "bar"]
    result = pp._configuration_args(custom_default)
    assert result is custom_default
    assert result == ["--foo", "bar"]


def test_configuration_args_returns_configured_postprocessor_args():
    configured = ["-codec", "copy", "-foo"]
    downloader = _FakeDownloader(params={"postprocessor_args": configured})
    pp = PostProcessor(downloader)
    result = pp._configuration_args()
    assert result == configured
    assert result is configured
    # explicit default must be ignored when config is present
    result_with_default = pp._configuration_args(["other"])
    assert result_with_default == configured
    assert result_with_default is configured
