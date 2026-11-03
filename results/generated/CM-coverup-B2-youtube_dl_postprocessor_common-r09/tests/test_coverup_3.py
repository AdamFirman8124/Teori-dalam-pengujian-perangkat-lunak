# file: project/youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

"""Tests covering PostProcessor.set_downloader (line 39)."""

from youtube_dl.postprocessor.common import PostProcessor


class DummyDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_set_downloader_assigns_downloader():
    # Start with no downloader so that line 39 must run to set the attribute.
    pp = PostProcessor()
    assert pp._downloader is None

    downloader = DummyDownloader()
    pp.set_downloader(downloader)

    # Postcondition: the downloader passed in is stored on the instance.
    assert pp._downloader is downloader


def test_set_downloader_replaces_previous_downloader():
    old_downloader = DummyDownloader()
    new_downloader = DummyDownloader()

    pp = PostProcessor(downloader=old_downloader)
    assert pp._downloader is old_downloader

    pp.set_downloader(new_downloader)

    # Postcondition: the previously stored downloader is replaced.
    assert pp._downloader is new_downloader
    assert pp._downloader is not old_downloader
