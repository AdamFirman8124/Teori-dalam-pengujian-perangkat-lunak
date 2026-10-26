# file: project/youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_set_downloader_assigns_downloader():
    pp = PostProcessor()
    assert pp._downloader is None
    dummy = object()
    pp.set_downloader(dummy)
    assert pp._downloader is dummy


def test_set_downloader_overwrites_existing():
    initial = object()
    updated = object()
    pp = PostProcessor(downloader=initial)
    assert pp._downloader is initial
    pp.set_downloader(updated)
    assert pp._downloader is updated


def test_set_downloader_can_reset_to_none():
    dummy = object()
    pp = PostProcessor(downloader=dummy)
    assert pp._downloader is dummy
    pp.set_downloader(None)
    assert pp._downloader is None
