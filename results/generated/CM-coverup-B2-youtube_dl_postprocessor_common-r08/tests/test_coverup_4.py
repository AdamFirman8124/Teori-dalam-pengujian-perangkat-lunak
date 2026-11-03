# file: project/youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


def test_run_default_returns_empty_files_and_information():
    """PostProcessor.run must hit line 56: return [], information."""
    pp = PostProcessor()
    information = {'filepath': 'somefile.mp4', 'title': 'test video'}

    files, info = pp.run(information)

    # By default, no files should be deleted and the information
    # must be passed through unchanged (same object).
    assert files == []
    assert info is information
    assert info == {'filepath': 'somefile.mp4', 'title': 'test video'}
