# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_postprocessor_init_with_downloader():
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader


def test_postprocessor_init_with_downloader_keyword():
    downloader = FakeDownloader()
    pp = PostProcessor(downloader=downloader)
    assert pp._downloader is downloader


def test_postprocessor_init_default_downloader_is_none():
    pp = PostProcessor()
    assert pp._downloader is None
