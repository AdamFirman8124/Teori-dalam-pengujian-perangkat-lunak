# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

from unittest.mock import Mock

from youtube_dl.postprocessor import common


def test_try_utime_updates_encoded_filename(monkeypatch):
    downloader = Mock()
    postprocessor = common.PostProcessor(downloader)
    encoded_path = b"/tmp/video.mp4"

    encode_filename = Mock(return_value=encoded_path)
    utime = Mock()
    monkeypatch.setattr(common, "encodeFilename", encode_filename)
    monkeypatch.setattr(common.os, "utime", utime)

    postprocessor.try_utime("/tmp/video.mp4", 123, 456)

    encode_filename.assert_called_once_with("/tmp/video.mp4")
    utime.assert_called_once_with(encoded_path, (123, 456))
    downloader.report_warning.assert_not_called()


def test_try_utime_reports_warning_when_utime_fails(monkeypatch):
    downloader = Mock()
    postprocessor = common.PostProcessor(downloader)
    encoded_path = b"/tmp/video.mp4"

    encode_filename = Mock(return_value=encoded_path)
    utime = Mock(side_effect=OSError("permission denied"))
    monkeypatch.setattr(common, "encodeFilename", encode_filename)
    monkeypatch.setattr(common.os, "utime", utime)

    postprocessor.try_utime(
        "/tmp/video.mp4",
        123,
        456,
        errnote="Unable to preserve timestamps",
    )

    encode_filename.assert_called_once_with("/tmp/video.mp4")
    utime.assert_called_once_with(encoded_path, (123, 456))
    downloader.report_warning.assert_called_once_with(
        "Unable to preserve timestamps"
    )
