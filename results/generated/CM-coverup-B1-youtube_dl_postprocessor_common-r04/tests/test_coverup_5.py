# file: project/youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

from youtube_dl.postprocessor import common


def test_configuration_args_delegates_to_cli_configuration_args(monkeypatch):
    params = {'postprocessor_args': ['--example']}
    downloader = type('Downloader', (), {'params': params})()
    postprocessor = common.PostProcessor(downloader)
    default = ['--default']
    expected = object()
    calls = []

    def fake_cli_configuration_args(actual_params, param, actual_default):
        calls.append((actual_params, param, actual_default))
        return expected

    monkeypatch.setattr(
        common, 'cli_configuration_args', fake_cli_configuration_args
    )

    result = postprocessor._configuration_args(default)

    assert result is expected
    assert calls == [(params, 'postprocessor_args', default)]
