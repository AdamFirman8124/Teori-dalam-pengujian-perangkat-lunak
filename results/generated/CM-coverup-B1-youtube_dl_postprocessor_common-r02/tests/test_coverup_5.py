# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

from types import SimpleNamespace

from youtube_dl.postprocessor.common import PostProcessor


def test_configuration_args_returns_postprocessor_args():
    expected = ["-metadata", "title=Example"]
    downloader = SimpleNamespace(params={"postprocessor_args": expected})
    postprocessor = PostProcessor(downloader)

    result = postprocessor._configuration_args()

    assert result is expected


def test_configuration_args_returns_custom_default_when_not_configured():
    default = ["-preset", "medium"]
    downloader = SimpleNamespace(params={})
    postprocessor = PostProcessor(downloader)

    result = postprocessor._configuration_args(default)

    assert result is default
