# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_postprocessor_default_constructor_sets_downloader_to_none():
    # Covers line 35 (self._downloader = downloader) via the default branch
    # where downloader is None.
    pp = PostProcessor()
    assert pp._downloader is None


def test_postprocessor_constructor_stores_given_downloader():
    # Covers line 35 again, this time via the branch where an explicit
    # downloader is passed in.
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader


def test_postprocessor_constructor_does_not_mutate_class_attribute():
    # Guards against state pollution: the class attribute _downloader must
    # remain None after instances set their own instance attribute.
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader
    assert PostProcessor._downloader is None
    assert '_downloader' in pp.__dict__
