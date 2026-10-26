# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_postprocessor_init_default():
    pp = PostProcessor()
    assert pp._downloader is None
    assert PostProcessor._downloader is None


def test_postprocessor_init_with_downloader_positional():
    sentinel = object()
    pp = PostProcessor(sentinel)
    assert pp._downloader is sentinel
    assert PostProcessor._downloader is None


def test_postprocessor_init_with_downloader_keyword():
    sentinel = object()
    pp = PostProcessor(downloader=sentinel)
    assert pp._downloader is sentinel
    assert PostProcessor._downloader is None


def test_postprocessor_init_explicit_none():
    pp = PostProcessor(downloader=None)
    assert pp._downloader is None
    assert PostProcessor._downloader is None
