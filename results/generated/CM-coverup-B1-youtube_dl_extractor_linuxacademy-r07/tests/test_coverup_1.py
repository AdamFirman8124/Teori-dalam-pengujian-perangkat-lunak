# file: project/youtube_dl/extractor/linuxacademy.py:154-243
# asked: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}
# gained: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}

import json

from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


class _FakeYDL(object):
    def __init__(self):
        self.params = {}

    def report_warning(self, msg, video_id=None):
        pass

    def to_screen(self, *args, **kwargs):
        pass

    def to_stdout(self, *args, **kwargs):
        pass

    def trouble(self, *args, **kwargs):
        pass


def _make_ie(monkeypatch, webpage, formats=None, calls=None):
    ie = LinuxAcademyIE()
    ie._downloader = _FakeYDL()
    if calls is None:
        calls = {}

    def fake_download(url_or_request, video_id, *args, **kwargs):
        calls['download'] = (url_or_request, video_id)
        return webpage

    def fake_extract(m3u8_url, video_id, ext=None, *args, **kwargs):
        calls['m3u8'] = (m3u8_url, video_id, ext, args, kwargs)
        return list(formats or [])

    def fake_sort(formats_arg, *args, **kwargs):
        calls['sort'] = list(formats_arg)

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract)
    monkeypatch.setattr(ie, '_sort_formats', fake_sort)
    ie._test_calls = calls
    return ie


def test_course_playlist_full(monkeypatch):
    module = {
        'title': 'AWS Course',
        'md_desc': 'Course MD',
        'duration': '1:30',
        'items': [
            'not-a-dict',
            42,
            {
                'type': {'name': 'Section', 'slug': 'section'},
                'course_name': 'Chapter 1',
                'course_module': 'mod-1',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '/cp/courses/lesson/course/7971/lesson/2',
                'title': 'Lesson One',
                'md_desc': 'Desc One',
                'date': '2020-12-08T12:00:00Z',
                'duration': '5:04',
            },
            {
                'type': {'name': 'Quiz', 'slug': 'quiz'},
                'url': '/quiz',
                'title': 'Quiz Item',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'title': 'No URL Lesson',
            },
            {
                'type': {'slug': 'section'},
                'course_name': 'Chapter 2',
                'course_module': 'mod-2',
            },
            {
                'type': {'name': 'lesson', 'slug': 'lesson'},
                'url': 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/3',
                'lesson_name': 'Lesson Two',
                'description': '<p>Desc Two</p>',
                'created_on': '2020-12-08T12:00:00Z',
                'duration': '2:00',
            },
            {
                'type': {'name': 'Lesson'},
                'url': '/relative/lesson3',
                'lesson_name': 'Lesson Three',
                'text': '<p>Desc Three</p>',
                'duration': '1:00',
            },
            {
                'url': '/no-type',
                'title': 'No Type Item',
            },
        ],
    }
    webpage = 'window.module = %s;' % json.dumps(module)
    url = 'https://linuxacademy.com/cp/modules/view/id/154'
    ie = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert ie._test_calls['download'] == (url, '154')
    assert result['_type'] == 'playlist'
    assert result['id'] == '154'
    assert result['title'] == 'AWS Course'
    assert result['description'] == 'Course MD'
    assert result['duration'] == 90
    assert len(result['entries']) == 3

    first, second, third = result['entries']
    assert first == {
        '_type': 'url_transparent',
        'url': 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2',
        'ie_key': 'LinuxAcademy',
        'title': 'Lesson One',
        'description': 'Desc One',
        'timestamp': first['timestamp'],
        'duration': 304,
        'chapter': 'Chapter 1',
        'chapter_id': 'mod-1',
        'chapter_number': 1,
    }
    assert isinstance(first['timestamp'], int) and first['timestamp'] > 0

    assert second['url'] == 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/3'
    assert second['title'] == 'Lesson Two'
    assert second['description'] == 'Desc Two'
    assert isinstance(second['timestamp'], int) and second['timestamp'] > 0
    assert second['duration'] == 120
    assert second['chapter'] == 'Chapter 2'
    assert second['chapter_id'] == 'mod-2'
    assert second['chapter_number'] == 2

    assert third['url'] == 'https://linuxacademy.com/relative/lesson3'
    assert third['title'] == 'Lesson Three'
    assert third['description'] == 'Desc Three'
    assert third['timestamp'] is None
    assert third['duration'] == 60
    assert third['chapter'] == 'Chapter 2'
    assert third['chapter_id'] == 'mod-2'
    assert third['chapter_number'] == 2


def test_course_playlist_description_fallback_and_no_lessons(monkeypatch):
    module = {
        'title': 'Empty Course',
        'desc': '<p>Course Desc</p>',
        'items': [
            {
                'type': {'name': 'Section', 'slug': 'section'},
                'course_name': 'Only Chapter',
                'course_module': 'm1',
            },
        ],
    }
    webpage = 'window.module = %s;' % json.dumps(module)
    url = 'https://www.linuxacademy.com/cp/modules/view/id/999'
    ie = _make_ie(monkeypatch, webpage)

    result = ie._real_extract(url)

    assert result == {
        '_type': 'playlist',
        'entries': [],
        'id': '999',
        'title': 'Empty Course',
        'description': 'Course Desc',
        'duration': None,
    }


def test_single_video_window_lesson(monkeypatch):
    lesson = {
        'lesson_name': 'What Is Data Science',
        'md_desc': 'MD Desc',
        'date': '2020-12-08T12:00:00Z',
        'duration': '5:04',
    }
    m3u8_url = 'https://example.com/video.m3u8'
    webpage = 'player.playlist = %s; window.lesson = %s;' % (
        json.dumps([{'file': m3u8_url}]), json.dumps(lesson))
    formats = [{'format_id': 'hls-0', 'url': m3u8_url, 'ext': 'mp4'}]
    url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675'
    ie = _make_ie(monkeypatch, webpage, formats=formats)

    result = ie._real_extract(url)

    assert ie._test_calls['download'] == (url, '7971-2')
    assert ie._test_calls['m3u8'][0] == m3u8_url
    assert ie._test_calls['m3u8'][1] == '7971-2'
    assert ie._test_calls['m3u8'][2] == 'mp4'
    assert ie._test_calls['m3u8'][4] == {
        'entry_protocol': 'm3u8_native', 'm3u8_id': 'hls'}
    assert ie._test_calls['sort'] == formats
    assert result['id'] == '7971-2'
    assert result['formats'] == formats
    assert result['title'] == 'What Is Data Science'
    assert result['description'] == 'MD Desc'
    assert isinstance(result['timestamp'], int) and result['timestamp'] > 0
    assert result['duration'] == 304


def test_single_video_player_lesson_and_lesson_name_title_fallback(monkeypatch):
    lesson = {
        'desc': '<p>Lesson Desc</p>',
        'created_on': '2020-12-08T12:00:00Z',
        'duration': '1:30',
    }
    m3u8_url = 'https://example.com/other.m3u8'
    webpage = (
        'player.playlist = %s; player.lesson = %s; '
        "lessonName = 'Fallback Title';"
    ) % (json.dumps([{'file': m3u8_url}]), json.dumps(lesson))
    formats = [{'format_id': 'hls-1', 'url': m3u8_url, 'ext': 'mp4'}]
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2'
    ie = _make_ie(monkeypatch, webpage, formats=formats)

    result = ie._real_extract(url)

    assert result['id'] == '1498-2'
    assert result['formats'] == formats
    assert result['title'] == 'Fallback Title'
    assert result['description'] == 'Lesson Desc'
    assert isinstance(result['timestamp'], int) and result['timestamp'] > 0
    assert result['duration'] == 90


def test_single_video_no_lesson_and_lecture_title_fallback(monkeypatch):
    m3u8_url = 'https://example.com/no-lesson.m3u8'
    webpage = (
        'player.playlist = %s; '
        '<div>Lecture : No Lesson Title</div>'
    ) % json.dumps([{'file': m3u8_url}])
    formats = [{'format_id': 'hls-2', 'url': m3u8_url, 'ext': 'mp4'}]
    url = 'https://linuxacademy.com/cp/courses/lesson/course/1234/lesson/5'
    ie = _make_ie(monkeypatch, webpage, formats=formats)

    result = ie._real_extract(url)

    assert result['id'] == '1234-5'
    assert result['formats'] == formats
    assert result['title'] == 'No Lesson Title'
    assert 'description' not in result
    assert 'timestamp' not in result
    assert 'duration' not in result
