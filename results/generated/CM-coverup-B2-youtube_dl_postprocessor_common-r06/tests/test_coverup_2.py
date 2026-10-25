# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


def test_init_with_downloader():
    class FakeDownloader(object):
        pass

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader


def test_init_without_downloader():
    pp = PostProcessor()
    assert pp._downloader is None
