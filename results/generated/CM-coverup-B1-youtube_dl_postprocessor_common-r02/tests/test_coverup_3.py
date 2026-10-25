# file: project/youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_set_downloader_assigns_downloader():
    post_processor = PostProcessor()
    downloader = object()

    post_processor.set_downloader(downloader)

    assert post_processor._downloader is downloader
