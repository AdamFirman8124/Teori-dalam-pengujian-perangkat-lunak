# file: project/youtube_dl/extractor/linuxacademy.py:154-243
# asked: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}
# gained: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}

import json
from youtube_dl import YoutubeDL
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


COURSE_URL = 'https://linuxacademy.com/cp/modules/view/id/154'
SINGLE_URL = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'


def _make_ie():
    ie = LinuxAcademyIE()
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True, 'no_color': True})
    ie.set_downloader(ydl)
    return ie


def _patch_webpage(monkeypatch, ie, webpage):
    monkeypatch.setattr(
        ie, '_download_webpage',
        lambda url, video_id, *a, **k: webpage)


def _patch_m3u8(monkeypatch, ie, formats):
    monkeypatch.setattr(
        ie, '_extract_m3u8_formats',
        lambda *a, **k: formats)


def test_course_playlist_covers_all_item_branches(monkeypatch):
    ie = _make_ie()
    module = {
        'title': 'Course Title',
        'md_desc': 'MD desc',
        'duration': '60',
        'items': [
            'not-a-dict',
            123,
            None,
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '/cp/courses/lesson/course/1/lesson/0',
                'title': 'Pre Chapter Lesson',
                'md_desc': 'Pre desc',
                'date': '2020-12-07',
                'duration': '100',
            },
            {
                'type': {'name': 'Section', 'slug': 'section'},
                'course_name': 'Chapter One',
                'course_module': 'mod-1',
            },
            {
                'type': {'name': 'section', 'slug': 'other'},
                'course_name': 'Chapter Two',
                'course_module': 'mod-2',
            },
            {
                'type': {'name': 'Quiz', 'slug': 'quiz'},
                'title': 'Quiz title',
                'url': '/quiz/1',
            },
            {'title': 'no type at all', 'url': '/no-type'},
            {'type': 'lesson-string', 'url': '/weird'},
            {'type': {'name': 123, 'slug': None}, 'url': '/weird2'},
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'title': 'No URL lesson',
            },
            {
                'type': {'name': 'Lesson', 'slug': 'lesson'},
                'url': '/cp/courses/lesson/course/1/lesson/1',
                'title': 'Lesson A',
                'md_desc': 'Desc A',
                'date': '2020-12-08',
                'duration': '5:04',
            },
            {
                'type': {'name': 'foo', 'slug': 'Lesson'},
                'url': 'lesson-b',
                'lesson_name': 'Lesson B via slug',
                'description': '<p>Desc B</p>',
                'created_on': '2020-12-09',
                'duration': '304',
            },
            {
                'type': {'name': 'lesson', 'slug': 'x'},
                'url': '/lesson-c',
                'lesson_name': 'Lesson C',
                'text': '<p>Text C</p>',
            },
            {
                'type': {'name': 'lesson', 'slug': 'lesson'},
                'url': '/lesson-d',
            },
        ],
    }
    webpage = '<html>window.module = %s;</html>' % json.dumps(module)
    _patch_webpage(monkeypatch, ie, webpage)

    result = ie._real_extract(COURSE_URL)

    assert result['_type'] == 'playlist'
    assert result['id'] == '154'
    assert result['title'] == 'Course Title'
    assert result['description'] == 'MD desc'
    assert result['duration'] == 60
    entries = result['entries']
    assert len(entries) == 5
    pre = entries[0]
    assert pre['title'] == 'Pre Chapter Lesson'
    assert pre['chapter'] is None
    assert pre['chapter_id'] is None
    assert pre['chapter_number'] is None
    assert pre['_type'] == 'url_transparent'
    assert pre['ie_key'] == LinuxAcademyIE.ie_key()
    assert pre['timestamp'] is not None
    assert pre['duration'] == 100
    a = entries[1]
    assert a['title'] == 'Lesson A'
    assert a['description'] == 'Desc A'
    assert a['chapter'] == 'Chapter Two'
    assert a['chapter_id'] == 'mod-2'
    assert a['chapter_number'] == 2
    assert a['duration'] == 304
    b = entries[2]
    assert b['title'] == 'Lesson B via slug'
    assert b['description'] == 'Desc B'
    assert b['timestamp'] is not None
    assert b['duration'] == 304
    c = entries[3]
    assert c['title'] == 'Lesson C'
    assert c['description'] == 'Text C'
    assert c['timestamp'] is None
    assert c['duration'] is None
    d = entries[4]
    assert d['title'] is None
    assert not d.get('description')
    assert d['timestamp'] is None
    titles = [e.get('title') for e in entries]
    assert 'Quiz title' not in titles
    assert 'No URL lesson' not in titles


def test_course_playlist_desc_and_duration_fallback(monkeypatch):
    ie = _make_ie()
    module = {
        'title': 'Fallback Course',
        'desc': '<p>Fallback <b>desc</b></p>',
        'items': [
            {
                'type': {'name': 'Section', 'slug': 'section'},
                'course_name': 'Only Chapter',
                'course_module': 'm1',
            },
            {
                'type': {'name': 'lesson', 'slug': 'lesson'},
                'url': '/cp/courses/lesson/course/9/lesson/9',
                'title': 'Only Lesson',
                'description': '<p>Hi</p>',
                'date': '2020-01-01',
                'duration': '10',
            },
        ],
    }
    webpage = 'window.module = %s;' % json.dumps(module)
    _patch_webpage(monkeypatch, ie, webpage)

    result = ie._real_extract(COURSE_URL)

    assert result['_type'] == 'playlist'
    assert result['title'] == 'Fallback Course'
    assert result['description'] == 'Fallback desc'
    assert result['duration'] is None
    assert len(result['entries']) == 1
    e = result['entries'][0]
    assert e['chapter'] == 'Only Chapter'
    assert e['chapter_id'] == 'm1'
    assert e['chapter_number'] == 1

    module2 = {
        'title': 'No Desc Course',
        'items': [
            {
                'type': {'name': 'lesson', 'slug': 'lesson'},
                'url': '/x',
                'title': 'T',
            },
        ],
    }
    webpage2 = 'window.module = %s;' % json.dumps(module2)
    _patch_webpage(monkeypatch, ie, webpage2)
    result2 = ie._real_extract(COURSE_URL)
    assert not result2.get('description')
    assert result2['duration'] is None


def test_single_video_window_lesson_with_title(monkeypatch):
    ie = _make_ie()
    lesson = {
        'lesson_name': 'My Lesson',
        'md_desc': 'MD Desc',
        'date': '2020-12-08',
        'duration': '304',
    }
    webpage = (
        '<html><body>'
        'player.playlist = [{"file": "http://example.com/video.m3u8"}];'
        'window.lesson = %s;'
        '</body></html>' % json.dumps(lesson)
    )
    _patch_webpage(monkeypatch, ie, webpage)
    _patch_m3u8(
        monkeypatch, ie,
        [
            {'url': 'http://example.com/low.m3u8', 'format_id': 'low', 'tbr': 500, 'ext': 'mp4'},
            {'url': 'http://example.com/high.m3u8', 'format_id': 'high', 'tbr': 1000, 'ext': 'mp4'},
        ])

    result = ie._real_extract(SINGLE_URL)

    assert result['id'] == '7971-2'
    assert result['title'] == 'My Lesson'
    assert result['description'] == 'MD Desc'
    assert result['timestamp'] is not None
    assert result['duration'] == 304
    assert len(result['formats']) == 2
    assert result['formats'][0]['tbr'] <= result['formats'][1]['tbr']


def test_single_video_player_lesson_with_lecture_fallback(monkeypatch):
    ie = _make_ie()
    lesson = {
        'desc': '<p>Lesson Desc</p>',
        'created_on': '2020-12-09',
        'duration': '5:04',
    }
    webpage = (
        '<html>'
        'player.playlist = [{"file": "http://example.com/v.m3u8"}];'
        'player.lesson = %s;'
        '<div>Lecture : Fallback Lecture Title</div>'
        '</html>' % json.dumps(lesson)
    )
    _patch_webpage(monkeypatch, ie, webpage)
    _patch_m3u8(
        monkeypatch, ie,
        [{'url': 'http://example.com/v.m3u8', 'format_id': 'hls', 'ext': 'mp4'}])

    result = ie._real_extract(SINGLE_URL)

    assert result['id'] == '7971-2'
    assert result['title'] == 'Fallback Lecture Title'
    assert result['description'] == 'Lesson Desc'
    assert result['timestamp'] is not None
    assert result['duration'] == 304
    assert len(result['formats']) == 1


def test_single_video_no_lesson_with_lessonName_fallback(monkeypatch):
    ie = _make_ie()
    webpage = (
        '<html>'
        'player.playlist = [{"file": "http://example.com/v.m3u8"}];'
        '<script>lessonName = \'Quoted Title\';</script>'
        '</html>'
    )
    _patch_webpage(monkeypatch, ie, webpage)
    _patch_m3u8(
        monkeypatch, ie,
        [{'url': 'http://example.com/v.m3u8', 'format_id': 'hls', 'ext': 'mp4'}])

    result = ie._real_extract(SINGLE_URL)

    assert result['id'] == '7971-2'
    assert result['title'] == 'Quoted Title'
    assert len(result['formats']) == 1


def test_single_video_minimal_lesson_no_desc_no_date(monkeypatch):
    ie = _make_ie()
    lesson = {'lesson_name': 'Only Title'}
    webpage = (
        '<html>'
        'player.playlist = [{"file": "http://example.com/v.m3u8"}];'
        'window.lesson = %s;'
        '</html>' % json.dumps(lesson)
    )
    _patch_webpage(monkeypatch, ie, webpage)
    _patch_m3u8(
        monkeypatch, ie,
        [{'url': 'http://example.com/v.m3u8', 'format_id': 'hls', 'ext': 'mp4'}])

    result = ie._real_extract(SINGLE_URL)

    assert result['title'] == 'Only Title'
    assert not result.get('description')
    assert result.get('timestamp') is None
    assert result.get('duration') is None
