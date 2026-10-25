# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_postprocessor_init_with_downloader():
    """Instantiating with a downloader must execute line 35
    (self._downloader = downloader) and store the downloader."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader=downloader)
    assert pp._downloader is downloader


def test_postprocessor_init_default_downloader_is_none():
    """Instantiating without arguments also executes line 35,
    storing the default value None."""
    pp = PostProcessor()
    assert pp._downloader is None


def test_postprocessor_init_overrides_class_attribute(monkeypatch):
    """The instance attribute set on line 35 must shadow the
    class-level _downloader attribute."""
    sentinel = FakeDownloader()
    # Ensure the class attribute is untouched after the test.
    monkeypatch.setattr(PostProcessor, '_downloader', None)
    pp = PostProcessor(downloader=sentinel)
    assert pp._downloader is sentinel
    assert PostProcessor._downloader is None
