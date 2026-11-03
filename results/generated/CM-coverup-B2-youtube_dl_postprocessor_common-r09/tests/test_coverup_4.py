# file: project/youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


def test_run_default_returns_no_files_and_unchanged_information():
    """Cover PostProcessor.run (line 56): by default it keeps the file
    and does nothing, returning an empty deletion list and the same
    information dict."""
    pp = PostProcessor()
    information = {'filepath': '/tmp/somefile.mp4', 'title': 'test video'}

    files_to_delete, updated_info = pp.run(information)

    assert files_to_delete == []
    assert updated_info is information
    assert updated_info['filepath'] == '/tmp/somefile.mp4'
    assert updated_info['title'] == 'test video'


def test_run_with_downloader_set():
    """Cover PostProcessor.run when a downloader has been attached;
    the default behavior must be identical."""
    class FakeDownloader(object):
        pass

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader

    information = {'filepath': '/tmp/otherfile.mp4'}
    files_to_delete, updated_info = pp.run(information)

    assert files_to_delete == []
    assert updated_info is information
