# file: project/youtube_dl/extractor/fourtube.py:43-114
# asked: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}
# gained: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}

from youtube_dl import YoutubeDL
from youtube_dl.extractor.fourtube import FourTubeIE
from youtube_dl.utils import parse_iso8601


def _make_ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True, 'no_color': True})
    ie = FourTubeIE()
    ie.set_downloader(ydl)
    return ie


def test_direct_no_rewrite_covers_direct_and_categories(monkeypatch):
    ie = _make_ie()
    direct_html = (
        '<html><head>'
        '<meta itemprop="name" content="Direct Title">'
        '<meta itemprop="uploadDate" content="2020-01-02T03:04:05+00:00">'
        '<meta itemprop="thumbnailUrl" content="https://example.com/thumb.jpg">'
        '<meta itemprop="duration" content="PT5M33S">'
        '<meta itemprop="interactionCount" content="UserPlays:12,345">'
        '<meta itemprop="interactionCount" content="UserLikes:678">'
        '</head><body>'
        '<a class="item-to-subscribe" href="https://example.com/channels/u123" title="Go to TestUploader page">x</a>'
        '><i class="icon icon-tag"></i> Categories / Tags <div><ul class="foo list bar">'
        '<li><a href="/c1">Cat One</a></li><li><a href="/c2">Cat Two</a></li>'
        '</ul></div>'
        '<button data-id="9999" data-quality="360">a</button>'
        '<button data-id="9999" data-quality="720">b</button>'
        '</body></html>'
    )
    seen = {}

    def fake_download_webpage(url, video_id, *args, **kwargs):
        seen['url'] = url
        seen['video_id'] = video_id
        return direct_html

    def fake_extract_formats(url, video_id, media_id, sources):
        seen['ef_url'] = url
        seen['ef_video_id'] = video_id
        seen['media_id'] = media_id
        seen['sources'] = sources
        return [{'url': 'https://example.com/v.mp4', 'format_id': '360p'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)
    orig_url = 'https://www.4tube.com/videos/2222/some-title'
    res = ie._real_extract(orig_url)
    assert seen['url'] == orig_url
    assert seen['video_id'] == '2222'
    assert seen['ef_url'] == orig_url
    assert seen['media_id'] == '9999'
    assert seen['sources'] == ['360', '720']
    assert res['id'] == '2222'
    assert res['title'] == 'Direct Title'
    assert res['formats'] == [{'url': 'https://example.com/v.mp4', 'format_id': '360p'}]
    assert res['categories'] == ['Cat One', 'Cat Two']
    assert res['thumbnail'] == 'https://example.com/thumb.jpg'
    assert res['uploader'] == 'TestUploader'
    assert res['uploader_id'] == 'u123'
    assert res['timestamp'] == parse_iso8601('2020-01-02T03:04:05+00:00')
    assert res['view_count'] == 12345
    assert res['like_count'] == 678
    assert res['duration'] == 333
    assert res['age_limit'] == 18


def test_rewrite_kind_m_covers_rewrite_branch(monkeypatch):
    ie = _make_ie()
    direct_html = (
        '<html><head>'
        '<meta itemprop="name" content="Direct Title">'
        '<meta itemprop="uploadDate" content="2020-01-02T03:04:05+00:00">'
        '<meta itemprop="thumbnailUrl" content="https://example.com/thumb.jpg">'
        '<meta itemprop="duration" content="PT5M33S">'
        '<meta itemprop="interactionCount" content="UserPlays:12,345">'
        '<meta itemprop="interactionCount" content="UserLikes:678">'
        '</head><body>'
        '<a class="item-to-subscribe" href="https://example.com/channels/u123" title="Go to TestUploader page">x</a>'
        '><i class="icon icon-tag"></i> Categories / Tags <div><ul class="foo list bar">'
        '<li><a href="/c1">Cat One</a></li>'
        '</ul></div>'
        '<button data-id="9999" data-quality="360">a</button>'
        '</body></html>'
    )
    seen = {}

    def fake_download_webpage(url, video_id, *args, **kwargs):
        seen['url'] = url
        seen['video_id'] = video_id
        return direct_html

    def fake_extract_formats(url, video_id, media_id, sources):
        seen['ef_url'] = url
        seen['media_id'] = media_id
        seen['sources'] = sources
        return [{'url': 'https://example.com/v.mp4'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)
    res = ie._real_extract('https://m.4tube.com/videos/1111/some-title')
    assert seen['url'] == 'https://www.4tube.com/videos/1111/video'
    assert seen['video_id'] == '1111'
    assert seen['ef_url'] == 'https://www.4tube.com/videos/1111/video'
    assert seen['media_id'] == '9999'
    assert seen['sources'] == ['360']
    assert res['id'] == '1111'
    assert res['title'] == 'Direct Title'
    assert res['categories'] == ['Cat One']
    assert res['age_limit'] == 18


def test_rewrite_missing_display_id_covers_second_or_branch(monkeypatch):
    ie = _make_ie()
    direct_html = (
        '<html><head>'
        '<meta itemprop="name" content="Direct Title">'
        '<meta itemprop="uploadDate" content="2020-01-02T03:04:05+00:00">'
        '<meta itemprop="thumbnailUrl" content="https://example.com/thumb.jpg">'
        '<meta itemprop="duration" content="PT2M0S">'
        '<meta itemprop="interactionCount" content="UserPlays:1,000">'
        '<meta itemprop="interactionCount" content="UserLikes:10">'
        '</head><body>'
        '<a class="item-to-subscribe" href="https://example.com/users/abc" title="Go to Other page">x</a>'
        '><i class="icon icon-tag"></i> Categories / Tags <div><ul class="x list y">'
        '<li><a href="/c9">Solo</a></li>'
        '</ul></div>'
        '<button data-id="777" data-quality="480">a</button>'
        '</body></html>'
    )
    seen = {}

    def fake_download_webpage(url, video_id, *args, **kwargs):
        seen['url'] = url
        return direct_html

    def fake_extract_formats(url, video_id, media_id, sources):
        seen['ef_url'] = url
        return [{'url': 'https://example.com/v2.mp4'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)
    res = ie._real_extract('https://www.4tube.com/videos/3333')
    assert seen['url'] == 'https://www.4tube.com/videos/3333/video'
    assert seen['ef_url'] == 'https://www.4tube.com/videos/3333/video'
    assert res['id'] == '3333'
    assert res['uploader_id'] == 'abc'
    assert res['uploader'] == 'Other'
    assert res['categories'] == ['Solo']
    assert res['view_count'] == 1000
    assert res['like_count'] == 10
    assert res['duration'] == 120


def test_fallback_player_js_no_categories_no_counts(monkeypatch):
    ie = _make_ie()
    fallback_html = (
        '<html><head>'
        '<meta itemprop="name" content="Fallback Title">'
        '<meta itemprop="uploadDate" content="2021-05-06T07:08:09+00:00">'
        '<meta itemprop="thumbnailUrl" content="https://example.com/thumb2.jpg">'
        '<meta itemprop="duration" content="PT1M10S">'
        '</head><body>'
        '<script id="playerembed" src="https://example.com/player.js"></script>'
        '</body></html>'
    )
    player_js = 'foo $.ajax(url, opts);}})(54321, 0, [360, 480]) bar'
    seen = {}

    def fake_download_webpage(url, video_id, *args, **kwargs):
        if 'player.js' in url:
            seen['player_url'] = url
            seen['player_video_id'] = video_id
            return player_js
        seen['page_url'] = url
        seen['page_video_id'] = video_id
        return fallback_html

    def fake_extract_formats(url, video_id, media_id, sources):
        seen['ef_url'] = url
        seen['ef_video_id'] = video_id
        seen['media_id'] = media_id
        seen['sources'] = sources
        return [{'url': 'https://example.com/fb.mp4', 'format_id': '360p'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)
    orig_url = 'https://www.4tube.com/videos/4444/fallback-title'
    res = ie._real_extract(orig_url)
    assert seen['page_url'] == orig_url
    assert seen['page_video_id'] == '4444'
    assert seen['player_url'] == 'https://example.com/player.js'
    assert seen['player_video_id'] == '4444'
    assert seen['media_id'] == 54321
    assert seen['sources'] == ['360', '480']
    assert seen['ef_url'] == orig_url
    assert res['id'] == '4444'
    assert res['title'] == 'Fallback Title'
    assert res['categories'] is None
    assert res['thumbnail'] == 'https://example.com/thumb2.jpg'
    assert res['uploader'] is None
    assert res['uploader_id'] is None
    assert res['timestamp'] == parse_iso8601('2021-05-06T07:08:09+00:00')
    assert res['view_count'] is None
    assert res['like_count'] is None
    assert res['duration'] == 70
    assert res['age_limit'] == 18
    assert res['formats'] == [{'url': 'https://example.com/fb.mp4', 'format_id': '360p'}]
