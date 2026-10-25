# file: project/youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


def test_run_returns_empty_list_and_information():
    pp = PostProcessor()
    information = {"filepath": "/tmp/somefile.mp4", "title": "test video"}

    files_to_delete, updated_info = pp.run(information)

    assert files_to_delete == []
    assert updated_info is information
