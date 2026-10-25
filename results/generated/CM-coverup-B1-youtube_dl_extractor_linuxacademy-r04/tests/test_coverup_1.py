# file: project/youtube_dl/extractor/linuxacademy.py:154-243
# asked: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}
# gained: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}

import json
from types import SimpleNamespace

import pytest

from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


COURSE_URL = 'https://linuxacademy.com/cp/modules/view/id/154'
SINGLE_URL = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'


@pytest.fixture
def ie(monkeypatch):
    extractor = LinuxAcademyIE()
    extractor._downloader = SimpleNamespace(params={'no_color': True})
    monkeypatch.setattr(extractor, '_sort_formats', lambda formats: None)
    return extractor


def _patch_webpage(monkeypatch, ie, webpage):
    monkeypatch.setattr(
        ie, '_download_webpage',
        lambda url, video_id, *args, **kwargs: webpage)


def _patch_m3u8(monkeypatch, ie, seen, formats):
    def fake_extract(m3u8_url, video_id, *args, **kwargs):
        seen.update({
            'url': m3u8_url,
            'video_id': video_id,
            'args': args,
            'kwargs': kwargs,
        })
        return list(formats)

    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract)


def test_course_playlist_branches(monkeypatch, ie):
    module = {
        'title': 'Course Title',
        'md_desc': 'MD Course Desc',
        'duration': '8:00:35',
        'items': [
            'not-a-dict',
            12345,
            {
                'type': {'name': 'Module', 'slug': 'section'},
                'course_name': 'Chapter One',
                'course_module': 'mod-1',
            },
            {
                'type': {'name': 'Quiz', 'slug': 'quiz'},
                'url': '/quiz/1',
                'title': 'Quiz 1',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'title': 'No URL Lesson',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '/cp/courses/lesson/course/7971/lesson/2',
                'title': 'Lesson One',
                'md_desc': 'Lesson MD',
                'date': '2020-12-08',
                'created_on': '2020-01-01',
                'duration': '5:04',
            },
            {
                'type': {'name': 'Section', 'slug': 'something-else'},
                'course_name': 'Chapter Two',
                'course_module': 'mod-2',
            },
            {
                'type': {'name': 'Video', 'slug': 'Lesson'},
                'url': (
                    'https://linuxacademy.com/cp/courses/lesson/'
                    'course/1/lesson/3'
                ),
                'lesson_name': 'Fallback Title',
                'description': '<p>HTML Desc</p>',
                'created_on': '2020-12-09',
                'duration': '10:00',
            },
            {
                'type': {'name': 'Lesson'},
                'url': '/cp/lesson/4',
                'title': 'T4',
                'text': '<b>Text Desc</b>',
            },
            {'url': '/x', 'title': 'NoType'},
            {'type': None, 'url': '/y', 'title': 'NoneType'},
            {
                'type': {'name': 'LESSON', 'slug': 'LESSON'},
                'url': '/cp/lesson/5',
                'title': 'T5',
            },
        ],
    }
    _patch_webpage(
        monkeypatch, ie, 'window.module = %s;' % json.dumps(module))

    result = ie._real_extract(COURSE_URL)

    assert result['_type'] == 'playlist'
    assert result['id'] == '154'
    assert result['title'] == 'Course Title'
    assert result['description'] == 'MD Course Desc'
    assert result['duration'] == 28835

    entries = result['entries']
    assert len(entries) == 4
    first, second, third, fourth = entries

    assert first == {
        '_type': 'url_transparent',
        'url': (
            'https://linuxacademy.com/cp/courses/lesson/'
            'course/7971/lesson/2'
        ),
        'ie_key': LinuxAcademyIE.ie_key(),
        'title': 'Lesson One',
        'description': 'Lesson MD',
        'timestamp': 1607385600,
        'duration': 304,
        'chapter': 'Chapter One',
        'chapter_id': 'mod-1',
        'chapter_number': 1,
    }

    assert second['_type'] == 'url_transparent'
    assert second['url'].endswith('/cp/courses/lesson/course/1/lesson/3')
    assert second['ie_key'] == LinuxAcademyIE.ie_key()
    assert second['title'] == 'Fallback Title'
    assert second['description'] == 'HTML Desc'
    assert second['timestamp'] == 1607472000
    assert second['duration'] == 600
    assert second['chapter'] == 'Chapter Two'
    assert second['chapter_id'] == 'mod-2'
    assert second['chapter_number'] == 2

    assert third['title'] == 'T4'
    assert third['description'] == 'Text Desc'
    assert third['timestamp'] is None
    assert third['duration'] is None
    assert third['chapter'] == 'Chapter Two'
    assert third['chapter_id'] == 'mod-2'
    assert third['chapter_number'] == 2

    assert fourth['title'] == 'T5'
    assert fourth['description'] is None
    assert fourth['timestamp'] is None
    assert fourth['duration'] is None
    assert fourth['chapter'] == 'Chapter Two'
    assert fourth['chapter_id'] == 'mod-2'
    assert fourth['chapter_number'] == 2


def test_course_playlist_description_fallback(monkeypatch, ie):
    module = {
        'title': 'Fallback Course',
        'desc': '<p>Course <b>Desc</b></p>',
        'items': [
            {
                'type': {'name': 'section', 'slug': 'section'},
                'course_name': 'Only Chapter',
                'course_module': 'mod-9',
            },
            {
                'type': {'name': 'lesson', 'slug': 'lesson'},
                'url': '/cp/courses/lesson/course/9/lesson/9',
                'title': 'Only Lesson',
            },
        ],
    }
    _patch_webpage(
        monkeypatch, ie, 'window.module = %s;' % json.dumps(module))

    result = ie._real_extract(COURSE_URL)

    assert result['_type'] == 'playlist'
    assert result['id'] == '154'
    assert result['title'] == 'Fallback Course'
    assert result['description'] == 'Course Desc'
    assert result['duration'] is None
    assert len(result['entries']) == 1

    entry = result['entries'][0]
    assert entry['title'] == 'Only Lesson'
    assert entry['chapter'] == 'Only Chapter'
    assert entry['chapter_id'] == 'mod-9'
    assert entry['chapter_number'] == 1
    assert entry['description'] is None
    assert entry['timestamp'] is None
    assert entry['duration'] is None


def test_single_video_with_window_lesson(monkeypatch, ie):
    lesson = {
        'lesson_name': 'What Is Data Science',
        'md_desc': 'Lesson MD Desc',
        'date': '2020-12-08',
        'created_on': '2020-01-01',
        'duration': '5:04',
    }
    webpage = (
        'player.playlist = '
        '[{"file": "https://example.com/v.m3u8"}];'
        'window.lesson = %s;' % json.dumps(lesson)
    )
    _patch_webpage(monkeypatch, ie, webpage)

    seen = {}
    fake_formats = [{
        'format_id': 'hls',
        'url': 'https://example.com/v.m3u8',
        'ext': 'mp4',
    }]
    _patch_m3u8(monkeypatch, ie, seen, fake_formats)

    result = ie._real_extract(SINGLE_URL)

    assert result == {
        'id': '7971-2',
        'formats': fake_formats,
        'title': 'What Is Data Science',
        'description': 'Lesson MD Desc',
        'timestamp': 1607385600,
        'duration': 304,
    }
    assert seen['url'] == 'https://example.com/v.m3u8'
    assert seen['video_id'] == '7971-2'
    assert seen['args'] == ('mp4',)
    assert seen['kwargs'] == {
        'entry_protocol': 'm3u8_native',
        'm3u8_id': 'hls',
    }


def test_single_video_player_lesson_and_lecture_title(monkeypatch, ie):
    lesson = {
        'desc': '<p>Lesson Desc</p>',
        'created_on': '2020-12-09',
        'duration': '10:00',
    }
    webpage = (
        'player.playlist = '
        '[{"file": "https://example.com/other.m3u8"}];'
        'player.lesson = %s;'
        '<span>Lecture : My Lecture Title</span>' % json.dumps(lesson)
    )
    _patch_webpage(monkeypatch, ie, webpage)

    seen = {}
    fake_formats = [{
        'format_id': 'hls',
        'url': 'https://example.com/other.m3u8',
        'ext': 'mp4',
    }]
    _patch_m3u8(monkeypatch, ie, seen, fake_formats)

    result = ie._real_extract(SINGLE_URL)

    assert result['id'] == '7971-2'
    assert result['formats'] == fake_formats
    assert result['title'] == 'My Lecture Title'
    assert result['description'] == 'Lesson Desc'
    assert result['timestamp'] == 1607472000
    assert result['duration'] == 600
    assert seen['url'] == 'https://example.com/other.m3u8'
    assert seen['video_id'] == '7971-2'


def test_single_video_without_lesson_uses_lesson_name_title(monkeypatch, ie):
    webpage = (
        'player.playlist = '
        '[{"file": "https://example.com/third.m3u8"}];'
        '<script>lessonName = "Quoted Title";</script>'
    )
    _patch_webpage(monkeypatch, ie, webpage)

    seen = {}
    fake_formats = [{
        'format_id': 'hls',
        'url': 'https://example.com/third.m3u8',
        'ext': 'mp4',
    }]
    _patch_m3u8(monkeypatch, ie, seen, fake_formats)

    result = ie._real_extract(SINGLE_URL)

    assert result == {
        'id': '7971-2',
        'formats': fake_formats,
        'title': 'Quoted Title',
    }
    assert seen['url'] == 'https://example.com/third.m3u8'
    assert seen['video_id'] == '7971-2'
