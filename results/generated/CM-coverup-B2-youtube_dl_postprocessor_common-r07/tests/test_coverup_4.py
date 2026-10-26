# file: project/youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_postprocessor_run_keeps_information_and_returns_no_files():
    information = {
        'filepath': '/tmp/example.mp4',
        'title': 'example',
    }
    postprocessor = PostProcessor()

    files_to_delete, updated_information = postprocessor.run(information)

    assert files_to_delete == []
    assert updated_information is information
    assert updated_information == information
