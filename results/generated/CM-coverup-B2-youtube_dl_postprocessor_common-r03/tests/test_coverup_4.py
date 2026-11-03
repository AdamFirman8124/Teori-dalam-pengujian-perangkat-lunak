# file: project/youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

"""Tests for youtube_dl.postprocessor.common.PostProcessor.run (line 56).

The default implementation of run() must return an empty list of files to
delete together with the (unmodified) information dictionary, i.e. it keeps
the downloaded file and does nothing.
"""

from youtube_dl.postprocessor.common import PostProcessor


def test_run_default_returns_no_files_and_same_information():
    """Covers line 56: default run() returns ([], information)."""
    pp = PostProcessor()
    information = {
        'filepath': '/tmp/some_video.mp4',
        'title': 'test video',
        'id': 'abc123',
    }

    files_to_delete, updated_information = pp.run(information)

    # Postconditions: no files marked for deletion, information passed
    # through unchanged (the very same object, unmodified).
    assert files_to_delete == []
    assert updated_information is information
    assert updated_information == {
        'filepath': '/tmp/some_video.mp4',
        'title': 'test video',
        'id': 'abc123',
    }


def test_run_default_with_downloader_attached():
    """run() behaves identically even when a downloader is attached."""
    class FakeDownloader(object):
        pass

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader

    information = {'filepath': 'x.webm'}
    files_to_delete, updated_information = pp.run(information)

    assert files_to_delete == []
    assert updated_information is information
