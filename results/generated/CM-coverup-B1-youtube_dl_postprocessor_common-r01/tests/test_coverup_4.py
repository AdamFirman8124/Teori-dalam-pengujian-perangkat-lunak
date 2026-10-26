# file: project/youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

from youtube_dl.postprocessor.common import PostProcessor


def test_run_by_default_keeps_file_and_does_nothing():
    pp = PostProcessor()
    information = {"filepath": "/tmp/video.mp4", "title": "test video"}
    snapshot = dict(information)
    result = pp.run(information)
    assert isinstance(result, tuple)
    assert len(result) == 2
    deletable_files, updated_information = result
    assert deletable_files == []
    assert updated_information == snapshot
    assert updated_information is information


def test_run_with_downloader_still_keeps_file_and_does_nothing():
    sentinel_downloader = object()
    pp = PostProcessor(downloader=sentinel_downloader)
    assert pp._downloader is sentinel_downloader
    information = {"filepath": "video.webm", "id": "123"}
    snapshot = dict(information)
    deletable_files, updated_information = pp.run(information)
    assert deletable_files == []
    assert updated_information == snapshot
    assert updated_information is information
    assert information == snapshot
