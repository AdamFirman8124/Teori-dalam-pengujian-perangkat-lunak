# file: project/youtube_dl/postprocessor/common.py:41-56
# asked: {"lines": [56], "branches": []}
# gained: {"lines": [56], "branches": []}

import pytest

from youtube_dl.postprocessor.common import PostProcessor


def test_run_returns_empty_list_and_same_information():
    pp = PostProcessor()
    information = {'filepath': '/tmp/video.mp4', 'title': 'video'}

    files_to_delete, info = pp.run(information)

    assert files_to_delete == []
    assert isinstance(files_to_delete, list)
    assert info is information
    assert info == {'filepath': '/tmp/video.mp4', 'title': 'video'}


def test_run_does_not_mutate_information():
    pp = PostProcessor()
    information = {'filepath': '/tmp/video.mp4'}
    snapshot = dict(information)

    files_to_delete, info = pp.run(information)

    assert files_to_delete == []
    assert info == snapshot
    assert information == snapshot


def test_run_with_downloader_returns_empty_list():
    sentinel_downloader = object()
    pp = PostProcessor(downloader=sentinel_downloader)
    information = {}

    files_to_delete, info = pp.run(information)

    assert pp._downloader is sentinel_downloader
    assert files_to_delete == []
    assert info is information


def test_run_returns_fresh_list_each_call():
    pp = PostProcessor()
    information = {'filepath': '/tmp/video.mp4'}

    first_files, first_info = pp.run(information)
    second_files, second_info = pp.run(information)

    assert first_files == [] and second_files == []
    assert first_files is not second_files
    assert first_info is information and second_info is information


def test_run_does_not_touch_filesystem(tmp_path, monkeypatch):
    target = tmp_path / 'video.mp4'
    target.write_bytes(b'data')

    pp = PostProcessor()
    information = {'filepath': str(target)}

    files_to_delete, info = pp.run(information)

    assert files_to_delete == []
    assert info is information
    assert target.exists()
    assert target.read_bytes() == b'data'
