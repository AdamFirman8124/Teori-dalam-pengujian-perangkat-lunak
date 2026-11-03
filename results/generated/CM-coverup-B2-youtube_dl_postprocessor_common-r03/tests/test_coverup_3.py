# file: project/youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class _DummyDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_set_downloader_sets_attribute_on_fresh_instance():
    pp = PostProcessor()
    # Precondition: a PP created without a downloader has none set.
    assert pp._downloader is None

    downloader = _DummyDownloader()
    pp.set_downloader(downloader)

    # Postcondition: set_downloader stored the downloader on the instance.
    assert pp._downloader is downloader


def test_set_downloader_replaces_existing_downloader():
    initial = _DummyDownloader()
    pp = PostProcessor(initial)
    assert pp._downloader is initial

    replacement = _DummyDownloader()
    pp.set_downloader(replacement)

    # Postcondition: the previous downloader was replaced by the new one.
    assert pp._downloader is replacement
    assert pp._downloader is not initial
