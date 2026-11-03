# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_postprocessor_init_default_downloader_is_none():
    """Instantiating without arguments must execute __init__ (line 35)
    and set the instance attribute _downloader to None."""
    pp = PostProcessor()
    # Postcondition: instance attribute shadows the class default (None)
    assert pp._downloader is None
    assert '_downloader' in pp.__dict__


def test_postprocessor_init_with_downloader():
    """Instantiating with a downloader must execute __init__ (line 35)
    and store the given downloader on the instance."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    # Postcondition: the exact downloader object passed in is stored
    assert pp._downloader is downloader
    assert isinstance(pp._downloader, FakeDownloader)


def test_postprocessor_init_does_not_mutate_class_attribute():
    """__init__ must only set the instance attribute, never the class one."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert PostProcessor._downloader is None
    assert pp._downloader is downloader
