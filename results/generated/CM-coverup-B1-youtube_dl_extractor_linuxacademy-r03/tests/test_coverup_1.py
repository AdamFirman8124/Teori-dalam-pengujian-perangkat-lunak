# file: project/youtube_dl/extractor/linuxacademy.py:154-243
# asked: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}
# gained: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}

import json

from youtube_dl import YoutubeDL
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


def _make_ie(monkeypatch, webpage):
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True, 'skip_download': True})
    ie = LinuxAcademyIE(ydl)
    captured = {}

    def fake_download(url, item_id):
        captured['download_url'] = url
        captured['item_id'] = item_id
        return webpage

    def fake_m3u8(m3u8_url, item_id, ext, entry_protocol='m3u8_native', m3u8_id='hls'):
        captured['m3u8_url'] = m3u8_url
        captured['m3u8_item_id'] = item_id
        captured['m3u8_ext'] = ext
        captured['entry_protocol'] = entry_protocol
        captured['m3u8_id'] = m3u8_id
        return [{'format_id': 'hls-1', 'url': m3u8_url, 'ext': 'mp4'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_m3u8)
    monkeypatch.setattr(ie, '_sort_formats', lambda formats: None)
    return ie, captured


def test_course_playlist_all_item_branches(monkeypatch):
    module = {
        'title': 'Course Title',
        'md_desc': 'Course MD Desc',
        'desc': '<p>Ignored Desc</p>',
        'duration': '10:00',
        'items': [
            'not-a-dict',
            42,
            {
                'type': {'name': 'Section', 'slug': 'section'},
                'course_name': 'Chapter One',
                'course_module': 'mod-1',
            },
            {
                'type': {'name': 'Quiz', 'slug': 'quiz'},
                'url': '/quiz/1',
                'title': 'Quiz Title',
            },
            {'url': '/no-type', 'title': 'No Type'},
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '',
                'title': 'Skipped Empty URL',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'other'},
                'url': None,
                'title': 'Skipped None URL',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '/lesson/1',
                'title': 'Lesson One',
                'lesson_name': 'Ignored Lesson Name',
                'md_desc': 'Lesson One Desc',
                'description': '<p>Ignored</p>',
                'text': '<p>Ignored Text</p>',
                'date': '2021-01-01T00:00:00Z',
                'created_on': '2021-01-02T00:00:00Z',
                'duration': '1:30',
            },
            {
                'type': {'name': 'SECTION', 'slug': 'other'},
                'course_name': 'Chapter Two',
                'course_module': 'mod-2',
            },
            {
                'type': {'name': 'other', 'slug': 'LESSON'},
                'url': '/lesson/2',
                'lesson_name': 'Lesson Two',
                'description': '<p>Lesson Two Desc</p>',
                'text': '<p>Ignored Text</p>',
                'created_on': '2021-01-02T00:00:00Z',
                'duration': '2:00',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': 'https://example.com/lesson/3',
                'text': '<p>Lesson Three Text</p>',
                'duration': '0:45',
            },
        ],
    }
    webpage = 'window.module = %s;' % json.dumps(module)
    ie, captured = _make_ie(monkeypatch, webpage)
    url = 'https://linuxacademy.com/cp/modules/view/id/154'

    result = ie._real_extract(url)

    assert captured == {'download_url': url, 'item_id': '154'}
    assert result['_type'] == 'playlist'
    assert result['id'] == '154'
    assert result['title'] == 'Course Title'
    assert result['description'] == 'Course MD Desc'
    assert result['duration'] == 600
    assert len(result['entries']) == 3

    first, second, third = result['entries']
    assert first == {
        '_type': 'url_transparent',
        'url': 'https://linuxacademy.com/lesson/1',
        'ie_key': LinuxAcademyIE.ie_key(),
        'title': 'Lesson One',
        'description': 'Lesson One Desc',
        'timestamp': 1609459200,
        'duration': 90,
        'chapter': 'Chapter One',
        'chapter_id': 'mod-1',
        'chapter_number': 1,
    }
    assert second == {
        '_type': 'url_transparent',
        'url': 'https://linuxacademy.com/lesson/2',
        'ie_key': LinuxAcademyIE.ie_key(),
        'title': 'Lesson Two',
        'description': 'Lesson Two Desc',
        'timestamp': 1609545600,
        'duration': 120,
        'chapter': 'Chapter Two',
        'chapter_id': 'mod-2',
        'chapter_number': 2,
    }
    assert third == {
        '_type': 'url_transparent',
        'url': 'https://example.com/lesson/3',
        'ie_key': LinuxAcademyIE.ie_key(),
        'title': None,
        'description': 'Lesson Three Text',
        'timestamp': None,
        'duration': 45,
        'chapter': 'Chapter Two',
        'chapter_id': 'mod-2',
        'chapter_number': 2,
    }


def test_course_playlist_fallbacks_and_empty_entries(monkeypatch):
    module = {
        'title': 'Fallback Course',
        'desc': '<p>Fallback Course Desc</p>',
        'duration': '0:30',
        'items': [
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '/only-lesson',
            },
        ],
    }
    webpage = 'window.module = %s;' % json.dumps(module)
    ie, captured = _make_ie(monkeypatch, webpage)
    url = 'https://linuxacademy.com/cp/modules/view/id/999'

    result = ie._real_extract(url)

    assert captured == {'download_url': url, 'item_id': '999'}
    assert result == {
        '_type': 'playlist',
        'entries': [{
            '_type': 'url_transparent',
            'url': 'https://linuxacademy.com/only-lesson',
            'ie_key': LinuxAcademyIE.ie_key(),
            'title': None,
            'description': None,
            'timestamp': None,
            'duration': None,
            'chapter': None,
            'chapter_id': None,
            'chapter_number': None,
        }],
        'id': '999',
        'title': 'Fallback Course',
        'description': 'Fallback Course Desc',
        'duration': 30,
    }


def test_single_video_window_lesson(monkeypatch):
    lesson = {
        'lesson_name': 'Window Lesson',
        'md_desc': 'Window MD Desc',
        'desc': '<p>Ignored Desc</p>',
        'date': '2021-01-01T00:00:00Z',
        'created_on': '2021-01-02T00:00:00Z',
        'duration': '1:30',
    }
    webpage = (
        'player.playlist = [{"file": "https://example.com/video.m3u8"}];\n'
        'window.lesson = %s;' % json.dumps(lesson)
    )
    ie, captured = _make_ie(monkeypatch, webpage)
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'

    result = ie._real_extract(url)

    assert captured['download_url'] == url
    assert captured['item_id'] == '7971-2'
    assert captured['m3u8_url'] == 'https://example.com/video.m3u8'
    assert captured['m3u8_item_id'] == '7971-2'
    assert captured['m3u8_ext'] == 'mp4'
    assert captured['entry_protocol'] == 'm3u8_native'
    assert captured['m3u8_id'] == 'hls'
    assert result == {
        'id': '7971-2',
        'formats': [{'format_id': 'hls-1', 'url': 'https://example.com/video.m3u8', 'ext': 'mp4'}],
        'title': 'Window Lesson',
        'description': 'Window MD Desc',
        'timestamp': 1609459200,
        'duration': 90,
    }


def test_single_video_player_lesson_fallback_fields(monkeypatch):
    lesson = {
        'lesson_name': 'Player Lesson',
        'desc': '<p>Player Desc</p>',
        'created_on': '2021-01-02T00:00:00Z',
        'duration': '2:00',
    }
    webpage = (
        'player.playlist = [{"file": "https://example.com/player.m3u8"}]; '
        'player.lesson = %s;' % json.dumps(lesson)
    )
    ie, captured = _make_ie(monkeypatch, webpage)
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'

    result = ie._real_extract(url)

    assert captured['item_id'] == '1498-2'
    assert captured['m3u8_url'] == 'https://example.com/player.m3u8'
    assert result['id'] == '1498-2'
    assert result['title'] == 'Player Lesson'
    assert result['description'] == 'Player Desc'
    assert result['timestamp'] == 1609545600
    assert result['duration'] == 120
    assert result['formats'][0]['url'] == 'https://example.com/player.m3u8'


def test_single_video_no_lesson_lecture_title_fallback(monkeypatch):
    webpage = (
        'player.playlist = [{"file": "https://example.com/no-lesson.m3u8"}]; '
        '<h1>Lecture : Lecture Fallback Title</h1>'
    )
    ie, captured = _make_ie(monkeypatch, webpage)
    url = 'https://linuxacademy.com/cp/courses/lesson/course/100/lesson/3'

    result = ie._real_extract(url)

    assert captured['item_id'] == '100-3'
    assert result == {
        'id': '100-3',
        'formats': [{'format_id': 'hls-1', 'url': 'https://example.com/no-lesson.m3u8', 'ext': 'mp4'}],
        'title': 'Lecture Fallback Title',
    }


def test_single_video_lesson_without_title_lesson_name_fallback(monkeypatch):
    lesson = {
        'md_desc': 'Desc Without Title',
        'date': '2021-01-01T00:00:00Z',
        'duration': '0:45',
    }
    webpage = (
        'player.playlist = [{"file": "https://example.com/alt.m3u8"}]; '
        'window.lesson = %s; '
        'var lessonName = "Alt Fallback Title";' % json.dumps(lesson)
    )
    ie, captured = _make_ie(monkeypatch, webpage)
    url = 'https://linuxacademy.com/cp/courses/lesson/course/200/lesson/4'

    result = ie._real_extract(url)

    assert captured['item_id'] == '200-4'
    assert result['id'] == '200-4'
    assert result['title'] == 'Alt Fallback Title'
    assert result['description'] == 'Desc Without Title'
    assert result['timestamp'] == 1609459200
    assert result['duration'] == 45
    assert result['formats'] == [
        {'format_id': 'hls-1', 'url': 'https://example.com/alt.m3u8', 'ext': 'mp4'}
    ]
