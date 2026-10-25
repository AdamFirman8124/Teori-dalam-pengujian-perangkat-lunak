# file: project/youtube_dl/extractor/linuxacademy.py:154-243
# asked: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}
# gained: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}

import json
import pytest
from youtube_dl import YoutubeDL
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE
from youtube_dl.utils import unified_timestamp, parse_duration


COURSE_URL = 'https://linuxacademy.com/cp/modules/view/id/154'
LESSON_URL = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'


@pytest.fixture
def ydl():
    return YoutubeDL({'quiet': True, 'no_color': True})


def _make_ie(monkeypatch, ydl, webpage, formats=None):
    ie = LinuxAcademyIE()
    ie.set_downloader(ydl)
    monkeypatch.setattr(
        ie, '_download_webpage',
        lambda url, video_id, *a, **k: webpage)
    if formats is not None:
        monkeypatch.setattr(
            ie, '_extract_m3u8_formats',
            lambda *a, **k: formats)
    return ie


def test_course_playlist_full_branches(monkeypatch, ydl):
    module = {
        'title': 'Course Title',
        'md_desc': 'MD desc',
        'desc': '<p>fallback</p>',
        'duration': '10:00',
        'items': [
            'not-a-dict',
            12345,
            {'type': {'name': 'Section', 'slug': 'section'},
             'course_name': 'Chapter One', 'course_module': 'cmod1'},
            {'type': {'name': 'Section', 'slug': 'other'},
             'course_name': 'Chapter Two', 'course_module': 'cmod2'},
            {'type': {'name': 'Quiz', 'slug': 'quiz'}, 'title': 'Should skip'},
            {'type': {'name': 'Lesson', 'slug': 'lesson'},
             'url': None, 'title': 'No URL lesson'},
            {'type': {'name': 'Lesson', 'slug': 'lesson'},
             'url': '', 'title': 'Empty URL'},
            {'type': {'name': 'LESSON', 'slug': 'LESSON'},
             'url': '/cp/courses/lesson/course/1/lesson/1',
             'title': 'Lesson One', 'md_desc': 'Desc One',
             'date': '2020-12-08', 'duration': '5:04',
             'lesson_name': 'Fallback Name'},
            {'type': {'name': 'lesson', 'slug': 'x'},
             'url': 'https://linuxacademy.com/cp/courses/lesson/course/1/lesson/2',
             'lesson_name': 'Lesson Two Name',
             'description': '<p>Desc <b>Two</b></p>',
             'created_on': '2020-12-09', 'duration': '3 mins'},
            {'type': {'name': 'lesson', 'slug': 'y'},
             'url': '/cp/courses/lesson/course/1/lesson/3',
             'text': '<p>Text Desc</p>', 'duration': 12345},
            {'type': {},
             'url': '/something', 'title': 'No type fields'},
            {'url': '/something', 'title': 'Missing type entirely'},
            {'type': {'name': 'lesson', 'slug': 'lesson'},
             'url': '/cp/courses/lesson/course/1/lesson/4'},
        ],
    }
    webpage = '<html><script>window.module = %s;</script></html>' % json.dumps(module)
    ie = _make_ie(monkeypatch, ydl, webpage)
    result = ie._real_extract(COURSE_URL)

    assert result['_type'] == 'playlist'
    assert result['id'] == '154'
    assert result['title'] == 'Course Title'
    assert result['description'] == 'MD desc'
    assert result['duration'] == parse_duration('10:00') == 600
    entries = result['entries']
    assert len(entries) == 4

    e0 = entries[0]
    assert e0['_type'] == 'url_transparent'
    assert e0['ie_key'] == LinuxAcademyIE.ie_key()
    assert e0['title'] == 'Lesson One'
    assert e0['description'] == 'Desc One'
    assert e0['timestamp'] == unified_timestamp('2020-12-08')
    assert e0['duration'] == parse_duration('5:04')
    assert e0['chapter'] == 'Chapter Two'
    assert e0['chapter_id'] == 'cmod2'
    assert e0['chapter_number'] == 2
    assert e0['url'].endswith('/cp/courses/lesson/course/1/lesson/1')

    e1 = entries[1]
    assert e1['title'] == 'Lesson Two Name'
    assert e1['description'] == 'Desc Two'
    assert e1['timestamp'] == unified_timestamp('2020-12-09')
    assert e1['duration'] == parse_duration('3 mins')
    assert e1['chapter_number'] == 2

    e2 = entries[2]
    assert e2['title'] is None
    assert e2['description'] == 'Text Desc'
    assert e2['timestamp'] is None
    assert e2['duration'] is None

    e3 = entries[3]
    assert e3['title'] is None
    assert e3['description'] is None
    assert e3['timestamp'] is None
    assert e3['duration'] is None


def test_course_playlist_desc_and_duration_fallback(monkeypatch, ydl):
    module = {
        'title': 'T2',
        'desc': '<p>Fallback Desc</p>',
        'items': [
            {'type': {'name': 'section', 'slug': 'section'},
             'course_name': 'Only Chapter', 'course_module': 'm1'},
            {'type': {'name': 'lesson', 'slug': 'lesson'},
             'url': '/cp/courses/lesson/course/9/lesson/9',
             'title': 'Only Lesson'},
        ],
    }
    webpage = '<html>window.module = %s;</html>' % json.dumps(module)
    ie = _make_ie(monkeypatch, ydl, webpage)
    result = ie._real_extract(COURSE_URL)

    assert result['id'] == '154'
    assert result['title'] == 'T2'
    assert result['description'] == 'Fallback Desc'
    assert result['duration'] is None
    assert len(result['entries']) == 1
    e = result['entries'][0]
    assert e['title'] == 'Only Lesson'
    assert e['chapter'] == 'Only Chapter'
    assert e['chapter_id'] == 'm1'
    assert e['chapter_number'] == 1


def test_single_video_with_window_lesson(monkeypatch, ydl):
    m3u8_url = 'http://example.com/video.m3u8'
    lesson = {
        'lesson_name': 'What Is Data Science',
        'md_desc': 'Lesson MD',
        'date': '2020-12-08',
        'duration': '5:04',
    }
    webpage = '<html>player.playlist = %s; window.lesson = %s;</html>' % (
        json.dumps([{'file': m3u8_url}]), json.dumps(lesson))
    fake_formats = [{'url': m3u8_url, 'format_id': 'hls', 'ext': 'mp4'}]
    ie = _make_ie(monkeypatch, ydl, webpage, formats=fake_formats)
    result = ie._real_extract(LESSON_URL)

    assert result['id'] == '7971-2'
    assert result['formats'] == fake_formats
    assert result['title'] == 'What Is Data Science'
    assert result['description'] == 'Lesson MD'
    assert result['timestamp'] == unified_timestamp('2020-12-08')
    assert result['duration'] == parse_duration('5:04')


def test_single_video_player_lesson_and_lecture_title(monkeypatch, ydl):
    m3u8_url = 'http://example.com/v2.m3u8'
    lesson = {
        'desc': '<p>Player Desc</p>',
        'created_on': '2020-12-09',
        'duration': '3 mins',
    }
    webpage = '<html>player.playlist = %s; player.lesson = %s; <div>Lecture : My Lecture Title</div></html>' % (
        json.dumps([{'file': m3u8_url}]), json.dumps(lesson))
    fake_formats = [{'url': m3u8_url, 'format_id': 'hls', 'ext': 'mp4'}]
    ie = _make_ie(monkeypatch, ydl, webpage, formats=fake_formats)
    result = ie._real_extract(LESSON_URL)

    assert result['id'] == '7971-2'
    assert result['title'] == 'My Lecture Title'
    assert result['description'] == 'Player Desc'
    assert result['timestamp'] == unified_timestamp('2020-12-09')
    assert result['duration'] == parse_duration('3 mins')


def test_single_video_no_lesson_lessonname_title(monkeypatch, ydl):
    m3u8_url = 'http://example.com/v3.m3u8'
    webpage = '<html>player.playlist = %s; <script>lessonName = "Quoted Title";</script></html>' % (
        json.dumps([{'file': m3u8_url}]))
    fake_formats = [{'url': m3u8_url, 'format_id': 'hls', 'ext': 'mp4'}]
    ie = _make_ie(monkeypatch, ydl, webpage, formats=fake_formats)
    result = ie._real_extract(LESSON_URL)

    assert result['id'] == '7971-2'
    assert result['title'] == 'Quoted Title'
    assert result['formats'] == fake_formats
    assert result.get('timestamp') is None
    assert result.get('duration') is None
