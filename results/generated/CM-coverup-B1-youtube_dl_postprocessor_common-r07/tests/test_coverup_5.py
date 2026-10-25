# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

from types import SimpleNamespace

from youtube_dl.postprocessor.common import PostProcessor


def test_configuration_args_returns_postprocessor_args():
    expected = ["-metadata", "title=test"]
    processor = PostProcessor()
    processor._downloader = SimpleNamespace(
        params={"postprocessor_args": expected}
    )

    result = processor._configuration_args()

    assert result is expected


def test_configuration_args_returns_custom_default_when_not_configured():
    default = ["-custom-default"]
    processor = PostProcessor()
    processor._downloader = SimpleNamespace(params={})

    result = processor._configuration_args(default)

    assert result is default


def test_configuration_args_returns_default_when_configured_value_is_none():
    default = ["-fallback"]
    processor = PostProcessor()
    processor._downloader = SimpleNamespace(
        params={"postprocessor_args": None}
    )

    result = processor._configuration_args(default)

    assert result is default
