# file: project/youtube_dl/extractor/linuxacademy.py:154-243
# asked: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}
# gained: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}

import json

import pytest

from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


class FakeYDL(object):
    def __init__(self):
        self.params = {}


def _make_ie(monkeypatch, webpage, formats=None):
    ie = LinuxAcademyIE(FakeYDL())
    captured = {}
    if formats is None:
        formats = [{
            'format_id': 'hls-0',
            'url': 'https://cdn.example.com/video.m3u8',
            'ext': 'mp4',
        }]

    def fake_download(url, item_id):
        captured['download_url'] = url
        captured['download_item_id'] = item_id
        return webpage

    def fake_extract_m3u8(*args, **kwargs):
        captured['m3u8_args'] = args
        captured['m3u8_kwargs'] = kwargs
        return formats

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract_m3u8)
    monkeypatch.setattr(ie, '_sort_formats', lambda fmts: None)
    return ie, captured, formats


def test_course_playlist_full(monkeypatch):
    module = {
        'title': 'AWS Certified Cloud Practitioner',
        'md_desc': 'Course description',
        'duration': '8:00:35',
        'items': [
            'not-a-dict',
            {
                'type': {'name': 'Section', 'slug': 'section'},
                'course_name': 'Chapter 1',
                'course_module': 'mod-1',
            },
            {
                'type': {'name': 'Quiz', 'slug': 'quiz'},
                'url': '/cp/quiz/1',
                'title': 'Quiz 1',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'title': 'Missing URL Lesson',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '/cp/courses/lesson/course/10/lesson/1',
                'title': 'Lesson One',
                'md_desc': 'Desc One',
                'date': '2020-12-08T00:00:00Z',
                'duration': '5:04',
            },
            {
                'type': {'name': 'section', 'slug': 'other'},
                'course_name': 'Chapter 2',
                'course_module': 'mod-2',
            },
            {
                'type': {'name': 'video', 'slug': 'Lesson'},
                'url': 'https://linuxacademy.com/cp/courses/lesson/course/10/lesson/2',
                'lesson_name': 'Lesson Two',
                'description': '<p>Desc Two</p>',
                'created_on': '2020-12-08T00:00:00Z',
                'duration': '1:00',
            },
            {
                'url': '/cp/courses/lesson/course/10/lesson/99',
                'title': 'No Type Lesson',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '/cp/courses/lesson/course/10/lesson/3',
                'text': '<p>Text Desc</p>',
                'duration': '0:30',
            },
        ],
    }
    webpage = 'window.module = %s;' % json.dumps(module)
    url = 'https://linuxacademy.com/cp/modules/view/id/154'
    ie, captured, _ = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert captured['download_url'] == url
    assert captured['download_item_id'] == '154'
    assert result['_type'] == 'playlist'
    assert result['id'] == '154'
    assert result['title'] == 'AWS Certified Cloud Practitioner'
    assert result['description'] == 'Course description'
    assert result['duration'] == 28835
    assert len(result['entries']) == 3

    first, second, third = result['entries']
    assert first == {
        '_type': 'url_transparent',
        'url': 'https://linuxacademy.com/cp/courses/lesson/course/10/lesson/1',
        'ie_key': LinuxAcademyIE.ie_key(),
        'title': 'Lesson One',
        'description': 'Desc One',
        'timestamp': 1607385600,
        'duration': 304,
        'chapter': 'Chapter 1',
        'chapter_id': 'mod-1',
        'chapter_number': 1,
    }
    assert second['title'] == 'Lesson Two'
    assert second['description'] == 'Desc Two'
    assert second['timestamp'] == 1607385600
    assert second['duration'] == 60
    assert second['chapter'] == 'Chapter 2'
    assert second['chapter_id'] == 'mod-2'
    assert second['chapter_number'] == 2
    assert second['url'] == 'https://linuxacademy.com/cp/courses/lesson/course/10/lesson/2'

    assert third['title'] is None
    assert third['description'] == 'Text Desc'
    assert third['timestamp'] is None
    assert third['duration'] == 30
    assert third['chapter'] == 'Chapter 2'
    assert third['chapter_id'] == 'mod-2'
    assert third['chapter_number'] == 2


def test_course_playlist_empty_and_desc_fallback(monkeypatch):
    module = {
        'title': 'Empty Course',
        'desc': '<p>Course Desc</p>',
        'items': [],
    }
    webpage = 'window.module = %s;' % json.dumps(module)
    url = 'https://linuxacademy.com/cp/modules/view/id/999'
    ie, captured, _ = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert captured['download_item_id'] == '999'
    assert result == {
        '_type': 'playlist',
        'entries': [],
        'id': '999',
        'title': 'Empty Course',
        'description': 'Course Desc',
        'duration': None,
    }


def test_single_video_window_lesson(monkeypatch):
    playlist = [{'file': 'https://cdn.example.com/video.m3u8'}]
    lesson = {
        'lesson_name': 'What Is Data Science',
        'md_desc': 'Lesson description',
        'date': '2020-12-08T00:00:00Z',
        'duration': '5:04',
    }
    webpage = '\n'.join([
        'player.playlist = %s;' % json.dumps(playlist),
        'window.lesson = %s;' % json.dumps(lesson),
    ])
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    ie, captured, formats = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert captured['download_item_id'] == '7971-2'
    assert captured['m3u8_args'][0] == 'https://cdn.example.com/video.m3u8'
    assert captured['m3u8_args'][1] == '7971-2'
    assert captured['m3u8_kwargs'] == {'entry_protocol': 'm3u8_native', 'm3u8_id': 'hls'}
    assert result['id'] == '7971-2'
    assert result['formats'] is formats
    assert result['title'] == 'What Is Data Science'
    assert result['description'] == 'Lesson description'
    assert result['timestamp'] == 1607385600
    assert result['duration'] == 304


def test_single_video_no_lesson_lecture_title_fallback(monkeypatch):
    playlist = [{'file': 'https://cdn.example.com/other.m3u8'}]
    webpage = '\n'.join([
        'player.playlist = %s;' % json.dumps(playlist),
        '<h1>Lecture : Fallback Title</h1>',
    ])
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    ie, captured, formats = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert captured['download_item_id'] == '1498-2'
    assert captured['m3u8_args'][0] == 'https://cdn.example.com/other.m3u8'
    assert result['id'] == '1498-2'
    assert result['formats'] is formats
    assert result['title'] == 'Fallback Title'


def test_single_video_player_lesson_and_lesson_name_title_fallback(monkeypatch):
    playlist = [{'file': 'https://cdn.example.com/third.m3u8'}]
    lesson = {
        'desc': '<p>Player Desc</p>',
        'created_on': '2020-12-08T00:00:00Z',
        'duration': '1:00',
    }
    webpage = '\n'.join([
        'player.playlist = %s;' % json.dumps(playlist),
        'player.lesson = %s;' % json.dumps(lesson),
        'lessonName = "Second Fallback";',
    ])
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/3'
    ie, captured, formats = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert captured['download_item_id'] == '1498-3'
    assert result['id'] == '1498-3'
    assert result['formats'] is formats
    assert result['title'] == 'Second Fallback'
    assert result['description'] == 'Player Desc'
    assert result['timestamp'] == 1607385600
    assert result['duration'] == 60
