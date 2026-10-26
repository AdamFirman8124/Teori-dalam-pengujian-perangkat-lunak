# file: project/youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_set_downloader():
    postprocessor = PostProcessor()
    downloader = object()

    postprocessor.set_downloader(downloader)

    assert postprocessor._downloader is downloader
