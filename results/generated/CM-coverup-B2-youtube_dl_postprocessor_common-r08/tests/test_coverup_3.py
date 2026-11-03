# file: project/youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for a youtube_dl downloader object."""


def test_set_downloader_sets_attribute():
    pp = PostProcessor()
    # Precondition: a PP created without a downloader has none assigned.
    assert pp._downloader is None

    downloader = FakeDownloader()
    pp.set_downloader(downloader)

    # Postcondition: the PP now holds a reference to the given downloader.
    assert pp._downloader is downloader


def test_set_downloader_replaces_previous_downloader():
    first = FakeDownloader()
    second = FakeDownloader()

    pp = PostProcessor(downloader=first)
    assert pp._downloader is first

    pp.set_downloader(second)

    # Postcondition: the previous downloader reference is replaced.
    assert pp._downloader is second
    assert pp._downloader is not first
