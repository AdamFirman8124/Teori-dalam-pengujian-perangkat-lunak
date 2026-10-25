# file: project/youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class _FakeDownloader(object):
    pass


def test_set_downloader_sets_attribute():
    pp = PostProcessor()
    assert pp._downloader is None  # precondition: no downloader initially

    downloader = _FakeDownloader()
    pp.set_downloader(downloader)

    assert pp._downloader is downloader  # line 39 executed: attribute assigned


def test_set_downloader_replaces_existing_downloader():
    first = _FakeDownloader()
    second = _FakeDownloader()
    pp = PostProcessor(downloader=first)
    assert pp._downloader is first

    pp.set_downloader(second)

    assert pp._downloader is second
