# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class _FakeDownloader(object):
    """Minimal stand-in for a downloader object."""


def test_postprocessor_init_stores_downloader():
    # Executing PostProcessor.__init__ covers line 35
    # (self._downloader = downloader) and verifies its postcondition.
    downloader = _FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader


def test_postprocessor_init_default_downloader_is_none():
    # Also exercises line 35 via the default argument path.
    pp = PostProcessor()
    assert pp._downloader is None
