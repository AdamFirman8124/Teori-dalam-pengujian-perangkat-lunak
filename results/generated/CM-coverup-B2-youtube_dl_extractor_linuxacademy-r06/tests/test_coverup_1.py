# file: project/youtube_dl/extractor/linuxacademy.py:154-243
# asked: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}
# gained: {"lines": [155, 156, 157, 159, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 242, 243], "branches": [[162, 163], [162, 214], [171, 172], [171, 204], [172, 173], [172, 175], [179, 180], [179, 185], [185, 186], [185, 187], [188, 189], [188, 190], [231, 232], [231, 238], [238, 239], [238, 243]]}

import json


class _FakeDownloader(object):
    def __init__(self):
        self.params = {"no_color": True}

    def report_warning(self, *args, **kwargs):
        return None

    def to_screen(self, *args, **kwargs):
        return None


def _make_ie(monkeypatch, webpage):
    from youtube_dl.extractor.linuxacademy import LinuxAcademyIE

    ie = LinuxAcademyIE()
    ie.set_downloader(_FakeDownloader())
    captured = {}

    def fake_download(url, item_id):
        captured["download_url"] = url
        captured["item_id"] = item_id
        return webpage

    def fake_m3u8(m3u8_url, item_id, ext=None, entry_protocol=None, m3u8_id=None):
        captured["m3u8_url"] = m3u8_url
        captured["m3u8_item_id"] = item_id
        captured["ext"] = ext
        captured["entry_protocol"] = entry_protocol
        captured["m3u8_id"] = m3u8_id
        return [{"format_id": "hls-0", "url": m3u8_url, "ext": "mp4"}]

    def fake_sort(formats):
        captured["sorted_formats"] = formats

    monkeypatch.setattr(ie, "_download_webpage", fake_download)
    monkeypatch.setattr(ie, "_extract_m3u8_formats", fake_m3u8)
    monkeypatch.setattr(ie, "_sort_formats", fake_sort)
    return ie, captured


def test_course_playlist_full(monkeypatch):
    module = {
        "title": "Course Title",
        "md_desc": "Course description",
        "duration": "1:30",
        "items": [
            "not-a-dict",
            42,
            {"type": {}, "url": "/ignored-no-type"},
            {"url": "/ignored-no-type-field"},
            {
                "type": {"name": "Section", "slug": "section"},
                "course_name": "Chapter 1",
                "course_module": "mod1",
            },
            {
                "type": {"name": "Lesson", "slug": "lesson"},
                "url": "/cp/courses/lesson/course/7971/lesson/2",
                "title": "Lesson 1",
                "md_desc": "Desc1",
                "date": "2020-12-08 00:00:00",
                "duration": "5:04",
            },
            {
                "type": {"name": "Quiz", "slug": "quiz"},
                "url": "/quiz",
                "title": "Quiz 1",
            },
            {
                "type": {"name": "Lesson", "slug": "lesson"},
                "title": "Lesson Without URL",
            },
            {
                "type": {"name": "Other", "slug": "SECTION"},
                "course_name": "Chapter 2",
                "course_module": "mod2",
            },
            {
                "type": {"name": "Other", "slug": "LESSON"},
                "url": "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/3",
                "lesson_name": "Lesson 2",
                "description": "<p>Desc2</p>",
                "created_on": "2020-01-01 00:00:00",
                "duration": "1:00",
            },
            {
                "type": {"name": "Lesson", "slug": "other"},
                "url": "/lesson3",
                "title": "Lesson 3",
                "text": "<p>TextDesc</p>",
                "duration": "0:30",
            },
        ],
    }
    webpage = "<html><script>window.module = %s;</script></html>" % json.dumps(module)
    ie, captured = _make_ie(monkeypatch, webpage)
    url = "https://linuxacademy.com/cp/modules/view/id/154"

    result = ie._real_extract(url)

    assert captured == {"download_url": url, "item_id": "154"}
    assert result["_type"] == "playlist"
    assert result["id"] == "154"
    assert result["title"] == "Course Title"
    assert result["description"] == "Course description"
    assert result["duration"] == 90
    assert len(result["entries"]) == 3

    first, second, third = result["entries"]
    assert first["_type"] == "url_transparent"
    assert first["url"] == "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2"
    assert first["ie_key"] == "LinuxAcademy"
    assert first["title"] == "Lesson 1"
    assert first["description"] == "Desc1"
    assert isinstance(first["timestamp"], int) and first["timestamp"] > 0
    assert first["duration"] == 304
    assert first["chapter"] == "Chapter 1"
    assert first["chapter_id"] == "mod1"
    assert first["chapter_number"] == 1

    assert second["url"] == "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/3"
    assert second["title"] == "Lesson 2"
    assert second["description"] == "Desc2"
    assert isinstance(second["timestamp"], int) and second["timestamp"] > 0
    assert second["duration"] == 60
    assert second["chapter"] == "Chapter 2"
    assert second["chapter_id"] == "mod2"
    assert second["chapter_number"] == 2

    assert third["url"] == "https://linuxacademy.com/lesson3"
    assert third["title"] == "Lesson 3"
    assert third["description"] == "TextDesc"
    assert third["timestamp"] is None
    assert third["duration"] == 30
    assert third["chapter"] == "Chapter 2"
    assert third["chapter_id"] == "mod2"
    assert third["chapter_number"] == 2


def test_course_playlist_description_fallback_empty_entries(monkeypatch):
    module = {
        "title": "Second Course",
        "desc": "<p>Course2 Desc</p>",
        "duration": "2:00",
        "items": [],
    }
    webpage = "window.module = %s;" % json.dumps(module)
    ie, captured = _make_ie(monkeypatch, webpage)
    url = "https://www.linuxacademy.com/cp/modules/view/id/999"

    result = ie._real_extract(url)

    assert captured["item_id"] == "999"
    assert result == {
        "_type": "playlist",
        "entries": [],
        "id": "999",
        "title": "Second Course",
        "description": "Course2 Desc",
        "duration": 120,
    }


def test_single_video_with_window_lesson(monkeypatch):
    playlist = [{"file": "https://example.com/video.m3u8"}]
    lesson = {
        "lesson_name": "What Is Data Science",
        "md_desc": "Lesson description",
        "date": "2020-12-08 00:00:00",
        "duration": "5:04",
    }
    webpage = "player.playlist = %s; window.lesson = %s;" % (
        json.dumps(playlist),
        json.dumps(lesson),
    )
    ie, captured = _make_ie(monkeypatch, webpage)
    url = "https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2/module/675"

    result = ie._real_extract(url)

    assert captured["download_url"] == url
    assert captured["item_id"] == "7971-2"
    assert captured["m3u8_url"] == "https://example.com/video.m3u8"
    assert captured["m3u8_item_id"] == "7971-2"
    assert captured["ext"] == "mp4"
    assert captured["entry_protocol"] == "m3u8_native"
    assert captured["m3u8_id"] == "hls"
    assert captured["sorted_formats"] == result["formats"]
    assert result["id"] == "7971-2"
    assert result["formats"] == [
        {"format_id": "hls-0", "url": "https://example.com/video.m3u8", "ext": "mp4"}
    ]
    assert result["title"] == "What Is Data Science"
    assert result["description"] == "Lesson description"
    assert isinstance(result["timestamp"], int) and result["timestamp"] > 0
    assert result["duration"] == 304


def test_single_video_with_player_lesson_fallbacks(monkeypatch):
    playlist = [{"file": "https://example.com/player.m3u8"}]
    lesson = {
        "lesson_name": "Player Lesson",
        "desc": "<p>Player Desc</p>",
        "created_on": "2020-03-01 00:00:00",
        "duration": "2:00",
    }
    webpage = "player.playlist = %s; player.lesson = %s;" % (
        json.dumps(playlist),
        json.dumps(lesson),
    )
    ie, captured = _make_ie(monkeypatch, webpage)
    url = "https://linuxacademy.com/cp/courses/lesson/course/1498/lesson/2"

    result = ie._real_extract(url)

    assert captured["item_id"] == "1498-2"
    assert captured["m3u8_url"] == "https://example.com/player.m3u8"
    assert result["id"] == "1498-2"
    assert result["title"] == "Player Lesson"
    assert result["description"] == "Player Desc"
    assert isinstance(result["timestamp"], int) and result["timestamp"] > 0
    assert result["duration"] == 120


def test_single_video_no_lesson_lecture_title_fallback(monkeypatch):
    playlist = [{"file": "https://example.com/no-lesson.m3u8"}]
    webpage = (
        "player.playlist = %s; <div>>Lecture : Fallback Lecture</div>"
        % json.dumps(playlist)
    )
    ie, captured = _make_ie(monkeypatch, webpage)
    url = "https://linuxacademy.com/cp/courses/lesson/course/100/lesson/5"

    result = ie._real_extract(url)

    assert captured["item_id"] == "100-5"
    assert captured["m3u8_url"] == "https://example.com/no-lesson.m3u8"
    assert result["id"] == "100-5"
    assert result["title"] == "Fallback Lecture"
    assert "description" not in result
    assert "timestamp" not in result
    assert "duration" not in result
    assert len(result["formats"]) == 1


def test_single_video_lesson_without_title_lesson_name_fallback(monkeypatch):
    playlist = [{"file": "https://example.com/fallback.m3u8"}]
    lesson = {
        "lesson_name": None,
        "desc": "<p>Fallback Desc</p>",
        "created_on": "2020-01-02 00:00:00",
        "duration": "1:00",
    }
    webpage = (
        "player.playlist = %s; window.lesson = %s; "
        "var lessonName = 'Fallback Title';"
        % (json.dumps(playlist), json.dumps(lesson))
    )
    ie, captured = _make_ie(monkeypatch, webpage)
    url = "https://linuxacademy.com/cp/courses/lesson/course/200/lesson/7"

    result = ie._real_extract(url)

    assert captured["item_id"] == "200-7"
    assert result["id"] == "200-7"
    assert result["title"] == "Fallback Title"
    assert result["description"] == "Fallback Desc"
    assert isinstance(result["timestamp"], int) and result["timestamp"] > 0
    assert result["duration"] == 60
    assert result["formats"][0]["url"] == "https://example.com/fallback.m3u8"
