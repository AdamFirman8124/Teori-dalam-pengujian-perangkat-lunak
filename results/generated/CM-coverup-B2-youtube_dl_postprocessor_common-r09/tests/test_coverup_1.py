# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

from unittest.mock import Mock

from youtube_dl.postprocessor import common


def test_try_utime_updates_file_times(monkeypatch):
    downloader = Mock()
    postprocessor = common.PostProcessor(downloader)
    encode_filename = Mock(return_value=b"encoded-file")
    utime = Mock()

    monkeypatch.setattr(common, "encodeFilename", encode_filename)
    monkeypatch.setattr(common.os, "utime", utime)

    result = postprocessor.try_utime("file", 123, 456)

    assert result is None
    encode_filename.assert_called_once_with("file")
    utime.assert_called_once_with(b"encoded-file", (123, 456))
    downloader.report_warning.assert_not_called()


def test_try_utime_reports_warning_when_update_fails(monkeypatch):
    downloader = Mock()
    postprocessor = common.PostProcessor(downloader)
    encode_filename = Mock(return_value=b"encoded-file")
    utime = Mock(side_effect=OSError("permission denied"))

    monkeypatch.setattr(common, "encodeFilename", encode_filename)
    monkeypatch.setattr(common.os, "utime", utime)

    result = postprocessor.try_utime(
        "file", 123, 456, errnote="Unable to update timestamps"
    )

    assert result is None
    encode_filename.assert_called_once_with("file")
    utime.assert_called_once_with(b"encoded-file", (123, 456))
    downloader.report_warning.assert_called_once_with(
        "Unable to update timestamps"
    )
