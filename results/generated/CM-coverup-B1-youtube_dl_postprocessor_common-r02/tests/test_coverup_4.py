# file: project/youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_postprocessor_run_keeps_file_and_information_unchanged():
    information = {
        "filepath": "/tmp/example.mp4",
        "title": "Example",
    }
    original = information.copy()

    files_to_delete, updated_information = PostProcessor().run(information)

    assert files_to_delete == []
    assert updated_information is information
    assert information == original
