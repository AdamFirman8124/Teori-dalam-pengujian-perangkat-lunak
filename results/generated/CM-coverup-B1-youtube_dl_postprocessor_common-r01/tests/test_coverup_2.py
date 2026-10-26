# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_postprocessor_init_default():
    pp = PostProcessor()
    assert pp._downloader is None


def test_postprocessor_init_with_downloader_positional():
    downloader = object()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader


def test_postprocessor_init_with_downloader_keyword():
    downloader = object()
    pp = PostProcessor(downloader=downloader)
    assert pp._downloader is downloader


def test_postprocessor_init_does_not_pollute_class_or_other_instances():
    downloader = object()
    pp_with = PostProcessor(downloader)
    pp_without = PostProcessor()
    assert pp_with._downloader is downloader
    assert pp_without._downloader is None
    assert PostProcessor._downloader is None
