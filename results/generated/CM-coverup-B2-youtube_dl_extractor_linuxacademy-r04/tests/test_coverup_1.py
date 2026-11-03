# file: project/youtube_dl/extractor/linuxacademy.py:154-243
# asked: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}
# gained: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}

# -*- coding: utf-8 -*-
"""Coverage tests for youtube_dl.extractor.linuxacademy.LinuxAcademyIE._real_extract.

The network-touching helpers (_download_webpage, _extract_m3u8_formats) are
replaced with fakes; everything else (regex extraction, JSON parsing, format
sorting) runs for real.  Each test builds its own extractor instance and uses
``monkeypatch`` so no state leaks between tests.
"""

from __future__ import unicode_literals

import json

import pytest

from youtube_dl.extractor.linuxacademy import LinuxAcademyIE
from youtube_dl.utils import parse_duration, unified_timestamp

# URLs matching LinuxAcademyIE._VALID_URL:
#   https?://(?:www\.)?linuxacademy\.com/cp/
#       (?: courses/lesson/course/(?P<chapter_id>\d+)/lesson/(?P<lesson_id>\d+)
#         | modules/view/id/(?P<course_id>\d+) )
COURSE_URL = 'https://linuxacademy.com/cp/modules/view/id/154'
COURSE_ID = '154'

LESSON_URL = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
LESSON_ITEM_ID = '7971-2'

DEFAULT_FORMATS = [
    {
        'format_id': 'hls-720',
        'url': 'https://cdn.example.com/hls/720.m3u8',
        'ext': 'mp4',
        'protocol': 'm3u8_native',
        'height': 720,
        'tbr': 2500,
    },
    {
        'format_id': 'hls-360',
        'url': 'https://cdn.example.com/hls/360.m3u8',
        'ext': 'mp4',
        'protocol': 'm3u8_native',
        'height': 360,
        'tbr': 900,
    },
]


class _FakeDownloader(object):
    """Minimal YoutubeDL stand-in.

    ``InfoExtractor._sort_formats`` and ``_search_regex`` unconditionally read
    ``self._downloader.params``, so a downloader with a ``params`` dict must be
    present.  Logging hooks are no-ops.
    """

    def __init__(self):
        self.params = {}

    def to_screen(self, *args, **kwargs):
        pass

    def report_warning(self, *args, **kwargs):
        pass


def _instrument(monkeypatch, webpage, formats=None):
    """Build a LinuxAcademyIE whose network methods are replaced by fakes.

    Returns ``(ie, calls)`` where ``calls`` records every intercepted call so
    the tests can assert on the arguments passed by ``_real_extract``.
    """
    ie = LinuxAcademyIE(_FakeDownloader())
    calls = {'downloads': [], 'm3u8': [], 'sorts': []}

    def fake_download_webpage(url_or_request, video_id, *args, **kwargs):
        calls['downloads'].append({'url': url_or_request, 'video_id': video_id})
        return webpage

    def fake_extract_m3u8_formats(m3u8_url, video_id, ext=None,
                                  entry_protocol='m3u8', **kwargs):
        calls['m3u8'].append({
            'm3u8_url': m3u8_url,
            'video_id': video_id,
            'ext': ext,
            'entry_protocol': entry_protocol,
            'm3u8_id': kwargs.get('m3u8_id'),
        })
        return [dict(f) for f in (formats if formats is not None else DEFAULT_FORMATS)]

    real_sort = LinuxAcademyIE._sort_formats

    def spy_sort(fmts, *args, **kwargs):
        calls['sorts'].append(fmts)
        return real_sort(ie, fmts, *args, **kwargs)

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract_m3u8_formats)
    monkeypatch.setattr(ie, '_sort_formats', spy_sort)
    return ie, calls


def _course_webpage():
    """Course page whose module items exercise every branch of the loop."""
    module = {
        'title': 'AWS Certified Cloud Practitioner',
        'md_desc': '',  # empty -> playlist description falls back to clean_html(desc)
        'desc': '<b>Course HTML description</b>',
        'duration': '1:30:00',
        'items': [
            'not-a-dict',  # non-dict item -> skipped
            {},            # dict without 'type' -> type_field() yields '' -> skipped
            {              # section #1 (chapter_number starts at 1)
                'type': {'name': 'Section', 'slug': 'section'},
                'course_name': 'Chapter One',
                'course_module': 'module-1',
            },
            {'type': {'name': 'Quiz'}},  # not a lesson/section -> skipped
            {              # lesson without url -> urljoin() gives None -> skipped
                'type': {'name': 'lesson'},
                'title': 'Orphan lesson without url',
            },
            {              # full lesson: title/md_desc/date/duration, relative url
                'type': {'name': 'lesson', 'slug': 'LESSON'},
                'url': '/lesson/intro',
                'title': 'Intro Lesson',
                'md_desc': 'Intro markdown description',
                'date': '2019-06-25T10:30:00Z',
                'duration': '1:30:00',
            },
            {              # section #2 (chapter_number incremented to 2)
                'type': {'name': 'SECTION'},
                'course_name': 'Chapter Two',
                'course_module': 'module-2',
            },
            {              # lesson using lesson_name/description/created_on fallbacks
                'type': {'slug': 'lesson'},
                'url': 'https://linuxacademy.com/lesson/fallback',
                'lesson_name': 'Fallback Lesson',
                'description': '<i>Fallback description</i>',
                'created_on': '2019-06-26 08:00:00',
                'duration': '45:00',
            },
            {              # lesson whose description only comes from clean_html(text)
                'type': {'slug': 'lesson'},
                'url': '/lesson/text-only',
                'title': 'Text Only Lesson',
                'text': '<b>Text description</b>',
            },
        ],
    }
    # NOTE: the extraction regexes use '.' without DOTALL, so the JSON must
    # stay on a single line (json.dumps guarantees that).
    return (
        '<html><head><script>window.module = ' + json.dumps(module) + ';</script>'
        '</head><body>course page</body></html>'
    )


def test_course_playlist(monkeypatch):
    """Course URL: playlist extraction covering all item branches."""
    ie, calls = _instrument(monkeypatch, _course_webpage())

    result = ie._real_extract(COURSE_URL)

    # The webpage was requested with the course id as the video id.
    assert calls['downloads'] == [{'url': COURSE_URL, 'video_id': COURSE_ID}]
    # The single-video path must not have run at all.
    assert calls['m3u8'] == []
    assert calls['sorts'] == []

    assert result['_type'] == 'playlist'
    assert result['id'] == COURSE_ID
    assert result['title'] == 'AWS Certified Cloud Practitioner'
    # md_desc is empty -> description comes from clean_html(module['desc']).
    assert result['description'] == 'Course HTML description'
    assert result['duration'] == parse_duration('1:30:00') == 5400

    entries = result['entries']
    # The non-dict item, the type-less item, the quiz and the url-less lesson
    # were all skipped; exactly the three real lessons remain.
    assert len(entries) == 3
    first, second, third = entries

    for entry in entries:
        assert entry['_type'] == 'url_transparent'
        assert entry['ie_key'] == LinuxAcademyIE.ie_key() == 'LinuxAcademy'

    # First lesson: relative url resolved against the course page, all
    # primary metadata fields used, chapter state from section #1.
    assert first['url'] == 'https://linuxacademy.com/lesson/intro'
    assert first['title'] == 'Intro Lesson'
    assert first['description'] == 'Intro markdown description'
    expected_ts = unified_timestamp('2019-06-25T10:30:00Z')
    assert expected_ts is not None
    assert first['timestamp'] == expected_ts
    assert first['duration'] == 5400
    assert first['chapter'] == 'Chapter One'
    assert first['chapter_id'] == 'module-1'
    assert first['chapter_number'] == 1

    # Second lesson: absolute url kept as-is, fallback title/description/
    # timestamp fields used, chapter state updated by section #2.
    assert second['url'] == 'https://linuxacademy.com/lesson/fallback'
    assert second['title'] == 'Fallback Lesson'
    assert second['description'] == 'Fallback description'
    expected_ts = unified_timestamp('2019-06-26 08:00:00')
    assert expected_ts is not None
    assert second['timestamp'] == expected_ts
    assert second['duration'] == parse_duration('45:00') == 2700
    assert second['chapter'] == 'Chapter Two'
    assert second['chapter_id'] == 'module-2'
    assert second['chapter_number'] == 2

    # Third lesson: description only available via clean_html(item['text']),
    # no date/created_on/duration at all.
    assert third['url'] == 'https://linuxacademy.com/lesson/text-only'
    assert third['title'] == 'Text Only Lesson'
    assert third['description'] == 'Text description'
    assert third['timestamp'] is None
    assert third['duration'] is None
    assert third['chapter'] == 'Chapter Two'
    assert third['chapter_id'] == 'module-2'
    assert third['chapter_number'] == 2


def test_lesson_with_window_lesson_metadata(monkeypatch):
    """Single video: window.lesson JSON supplies all metadata."""
    webpage = (
        '<html><body>'
        '<script>player.playlist = '
        '[{"file": "https://cdn.example.com/hls/master.m3u8"}];</script>'
        '<script>window.lesson = ' + json.dumps({
            'lesson_name': 'What Is Data Science',
            'md_desc': 'Lesson markdown description',
            'date': '2020-12-08T21:18:27Z',
            'duration': '10:00',
        }) + ';</script>'
        '</body></html>'
    )
    ie, calls = _instrument(monkeypatch, webpage)

    info = ie._real_extract(LESSON_URL)

    assert calls['downloads'] == [{'url': LESSON_URL, 'video_id': LESSON_ITEM_ID}]

    # The first entry of the player.playlist JSON array was used as m3u8 url.
    assert len(calls['m3u8']) == 1
    m3u8 = calls['m3u8'][0]
    assert m3u8['m3u8_url'] == 'https://cdn.example.com/hls/master.m3u8'
    assert m3u8['video_id'] == LESSON_ITEM_ID
    assert m3u8['ext'] == 'mp4'
    assert m3u8['entry_protocol'] == 'm3u8_native'
    assert m3u8['m3u8_id'] == 'hls'

    # _sort_formats ran on the very list that ends up in the result, and the
    # formats are ordered worst-first (ascending sort key).
    assert len(calls['sorts']) == 1
    assert calls['sorts'][0] is info['formats']
    assert {f['format_id'] for f in info['formats']} == {'hls-720', 'hls-360'}
    tbrs = [f['tbr'] for f in info['formats']]
    assert tbrs == sorted(tbrs)

    assert info['id'] == LESSON_ITEM_ID
    assert info['title'] == 'What Is Data Science'
    assert info['description'] == 'Lesson markdown description'
    expected_ts = unified_timestamp('2020-12-08T21:18:27Z')
    assert expected_ts is not None
    assert info['timestamp'] == expected_ts
    assert info['duration'] == parse_duration('10:00') == 600


def test_lesson_player_lesson_and_lecture_title_fallback(monkeypatch):
    """Single video: player.lesson variant, desc/created_on fallbacks and the
    '>Lecture :' title fallback when lesson_name is empty."""
    webpage = (
        '<html><body><h1>Lecture : Backup Lecture Title</h1>'
        '<script>player.playlist = '
        '[{"file": "https://cdn.example.com/hls/two.m3u8"}];</script>'
        '<script>player.lesson = ' + json.dumps({
            'lesson_name': '',
            'desc': '<p>HTML lesson description</p>',
            'created_on': '2019-07-01 05:06:07',
            'duration': '45:00',
        }) + ';</script>'
        '</body></html>'
    )
    ie, calls = _instrument(monkeypatch, webpage)

    info = ie._real_extract(LESSON_URL)

    assert info['id'] == LESSON_ITEM_ID

    # The (truthy) player.lesson dict updated the info dict.
    assert info['description'] == 'HTML lesson description'
    expected_ts = unified_timestamp('2019-07-01 05:06:07')
    assert expected_ts is not None
    assert info['timestamp'] == expected_ts
    assert info['duration'] == parse_duration('45:00') == 2700

    # lesson_name is empty -> title falls back to the '>Lecture :' regex.
    assert info['title'] == 'Backup Lecture Title'

    assert len(calls['m3u8']) == 1
    assert calls['m3u8'][0]['m3u8_url'] == 'https://cdn.example.com/hls/two.m3u8'
    assert len(calls['sorts']) == 1


def test_lesson_without_lesson_json_uses_lesson_name_fallback(monkeypatch):
    """Single video: no lesson JSON at all (default '{}' kicks in) and the
    lessonName assignment regex supplies the title."""
    webpage = (
        '<html><body>'
        '<script>player.playlist = '
        '[{"file": "https://cdn.example.com/hls/three.m3u8"}];</script>'
        "<script>var lessonName = 'The Fallback Name';</script>"
        '</body></html>'
    )
    ie, calls = _instrument(monkeypatch, webpage)

    info = ie._real_extract(LESSON_URL)

    assert info['id'] == LESSON_ITEM_ID
    # No lesson metadata was merged: only id, formats and the fallback title.
    assert set(info.keys()) == {'id', 'formats', 'title'}
    assert info['title'] == 'The Fallback Name'
    assert {f['format_id'] for f in info['formats']} == {'hls-720', 'hls-360'}
    assert len(calls['m3u8']) == 1
    assert calls['m3u8'][0]['m3u8_url'] == 'https://cdn.example.com/hls/three.m3u8'
