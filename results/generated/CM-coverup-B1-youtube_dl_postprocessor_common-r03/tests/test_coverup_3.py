# file: project/youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class _FakeDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_set_downloader_sets_attribute():
    pp = PostProcessor()
    # Precondition: no downloader set yet
    assert pp._downloader is None

    downloader = _FakeDownloader()
    pp.set_downloader(downloader)

    # Postcondition: line 39 executed, attribute now holds the downloader
    assert pp._downloader is downloader


def test_set_downloader_overwrites_existing_downloader(monkeypatch):
    pp = PostProcessor()
    first = _FakeDownloader()
    second = _FakeDownloader()

    # Ensure no state leaks: restore the class-level default afterwards
    monkeypatch.setattr(PostProcessor, '_downloader', None, raising=True)

    pp.set_downloader(first)
    assert pp._downloader is first

    pp.set_downloader(second)
    assert pp._downloader is second
    assert pp._downloader is not first
