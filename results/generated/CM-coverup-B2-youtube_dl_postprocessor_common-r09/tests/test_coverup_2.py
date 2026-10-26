# file: project/youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_postprocessor_init_stores_downloader():
    downloader = object()

    postprocessor = PostProcessor(downloader)

    assert postprocessor._downloader is downloader
