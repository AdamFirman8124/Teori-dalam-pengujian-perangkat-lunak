# file: project/youtube_dl/extractor/itv.py:54-150
# asked: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}
# gained: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}

import json

import pytest

from youtube_dl.extractor.itv import ITVIE
from youtube_dl.utils import ExtractorError


class _FakeDownloader(object):
    def __init__(self, params=None):
        self.params = params or {}

    def report_warning(self, *args, **kwargs):
        pass

    def report_error(self, *args, **kwargs):
        pass


def _webpage(video_attrs=None, extra_head='', synopsis=True):
    if video_attrs is None:
        video_attrs = (
            'data-video-playlist="https://example.com/playlist.json" '
            'data-video-id="https://example.com/id.json" '
            'data-video-hmac="abc123"'
        )
    synopsis_html = (
        '<div class="episode-info__synopsis">A <b>great</b> episode</div>'
        if synopsis else ''
    )
    return (
        '<html><head>'
        '<meta property="og:title" content="Test Title">'
        + extra_head +
        '</head><body>'
        '<div id="video" ' + video_attrs + '></div>'
        + synopsis_html +
        '</body></html>'
    )


def _playlist(video_data):
    return {'Playlist': {'Video': video_data}}


def _make_ie(monkeypatch, webpage, playlist, m3u8_formats=None, downloader_params=None):
    if m3u8_formats is None:
        m3u8_formats = [{
            'url': 'https://cdn.example.com/master.m3u8',
            'format_id': 'hls-1',
            'ext': 'mp4',
        }]
    captured = {'m3u8_calls': []}
    ie = ITVIE(_FakeDownloader(downloader_params))

    monkeypatch.setattr(ie, '_match_id', lambda url: 'vid123', raising=False)
    monkeypatch.setattr(
        ie, '_download_webpage',
        lambda url, video_id, **kwargs: webpage,
        raising=False)

    def _fake_download_json(url, video_id, data=None, headers=None, **kwargs):
        captured['playlist_url'] = url
        captured['playlist_video_id'] = video_id
        captured['data'] = data
        captured['headers'] = headers
        return playlist

    monkeypatch.setattr(ie, '_download_json', _fake_download_json, raising=False)

    def _fake_m3u8(url, video_id, *args, **kwargs):
        captured['m3u8_calls'].append((url, video_id, args, kwargs))
        return [dict(f) for f in m3u8_formats]

    monkeypatch.setattr(ie, '_extract_m3u8_formats', _fake_m3u8, raising=False)
    return ie, captured


def test_real_extract_full_with_base_m3u8_and_subtitles(monkeypatch):
    webpage = _webpage()
    playlist = _playlist({
        'Base': 'https://cdn.example.com/',
        'MediaFiles': [
            {'Href': 'video.mp4'},
            {'Href': 'master.m3u8'},
            {'Href': ''},
            {},
            {'Href': None},
        ],
        'Subtitles': [
            {'Href': 'https://example.com/subs.vtt'},
            {'Href': 'https://example.com/subs2.srt'},
            'not-a-dict',
            {'Href': ''},
            {'Href': 'not-a-url'},
            {},
        ],
        'Duration': '00:02:30',
    })
    ie, captured = _make_ie(
        monkeypatch, webpage, playlist,
        downloader_params={'geo_verification_proxy': 'http://proxy.example.com'})

    result = ie._real_extract('https://www.itv.com/hub/show/vid123')

    assert result['id'] == 'vid123'
    assert result['title'] == 'Test Title'
    assert result['description'] == 'A great episode'
    assert result['duration'] == 150
    assert {f['url'] for f in result['formats']} == {
        'https://cdn.example.com/video.mp4',
        'https://cdn.example.com/master.m3u8',
    }
    assert result['subtitles'] == {
        'en': [
            {'url': 'https://example.com/subs.vtt', 'ext': 'vtt'},
            {'url': 'https://example.com/subs2.srt', 'ext': 'srt'},
        ]
    }
    assert captured['playlist_url'] == 'https://example.com/playlist.json'
    assert captured['playlist_video_id'] == 'vid123'
    assert captured['headers']['hmac'] == 'ABC123'
    assert captured['headers']['Accept'] == 'application/vnd.itv.vod.playlist.v2+json'
    assert captured['headers']['Content-Type'] == 'application/json'
    assert captured['headers']['Ytdl-request-proxy'] == 'http://proxy.example.com'
    payload = json.loads(captured['data'].decode('utf-8'))
    assert payload == {
        'user': {'itvUserId': '', 'entitlements': [], 'token': ''},
        'device': {
            'manufacturer': 'Safari',
            'model': '5',
            'os': {'name': 'Windows NT', 'version': '6.1', 'type': 'desktop'},
        },
        'client': {'version': '4.1', 'id': 'browser'},
        'variantAvailability': {
            'featureset': {
                'min': ['hls', 'aes', 'outband-webvtt'],
                'max': ['hls', 'aes', 'outband-webvtt'],
            },
            'platformTag': 'dotcom',
        },
    }
    assert captured['m3u8_calls'] == [(
        'https://cdn.example.com/master.m3u8', 'vid123', ('mp4',),
        {'entry_protocol': 'm3u8_native', 'm3u8_id': 'hls', 'fatal': False},
    )]


def test_real_extract_fallback_id_no_base_no_subtitles(monkeypatch):
    webpage = _webpage(
        video_attrs=(
            'data-video-id="https://example.com/fallback.json" '
            'data-video-hmac="def456"'
        ),
        synopsis=False)
    playlist = _playlist({
        'MediaFiles': [
            {'Href': 'https://example.com/movie.mp4'},
            {'Href': 'https://example.com/stream.m3u8'},
        ],
    })
    ie, captured = _make_ie(
        monkeypatch, webpage, playlist,
        m3u8_formats=[{
            'url': 'https://example.com/stream.m3u8',
            'format_id': 'hls-1',
            'ext': 'mp4',
        }])

    result = ie._real_extract('https://www.itv.com/hub/show/vid123')

    assert result['id'] == 'vid123'
    assert result['title'] == 'Test Title'
    assert {f['url'] for f in result['formats']} == {
        'https://example.com/movie.mp4',
        'https://example.com/stream.m3u8',
    }
    assert result['subtitles'] == {}
    assert result.get('duration') is None
    assert result.get('description') is None
    assert captured['playlist_url'] == 'https://example.com/fallback.json'
    assert captured['headers']['hmac'] == 'DEF456'
    assert 'Ytdl-request-proxy' not in captured['headers']
    assert captured['m3u8_calls'][0][0] == 'https://example.com/stream.m3u8'


def test_real_extract_empty_media_files_raises(monkeypatch):
    webpage = _webpage()
    playlist = _playlist({
        'Base': 'https://cdn.example.com/',
        'MediaFiles': None,
        'Subtitles': [],
        'Duration': '00:01:00',
    })
    ie, captured = _make_ie(monkeypatch, webpage, playlist)

    with pytest.raises(ExtractorError, match='No video formats found'):
        ie._real_extract('https://www.itv.com/hub/show/vid123')

    assert captured['playlist_url'] == 'https://example.com/playlist.json'
    assert captured['m3u8_calls'] == []


def test_real_extract_search_json_ld_truthy_skips_breadcrumb(monkeypatch):
    breadcrumb = {
        '@context': 'http://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement:': [
            {'item:': {'@type': 'TVEpisode', 'name': 'Should Not Be Used'}},
        ],
    }
    extra = (
        '<script type="application/ld+json">'
        + json.dumps(breadcrumb) + '</script>'
    )
    webpage = _webpage(extra_head=extra)
    playlist = _playlist({
        'MediaFiles': [{'Href': 'https://example.com/movie.mp4'}],
        'Subtitles': None,
        'Duration': '00:01:00',
    })
    ie, captured = _make_ie(monkeypatch, webpage, playlist)
    json_ld_calls = []
    monkeypatch.setattr(
        ie, '_search_json_ld',
        lambda html, video_id, default=None, **kwargs: {
            'title': 'LD Title Should Not Override',
            'thumbnail': 'https://example.com/thumb.jpg',
            'episode': 'LD Episode',
        },
        raising=False)
    monkeypatch.setattr(
        ie, '_json_ld',
        lambda *args, **kwargs: json_ld_calls.append((args, kwargs)) or {},
        raising=False)

    result = ie._real_extract('https://www.itv.com/hub/show/vid123')

    assert result['id'] == 'vid123'
    assert result['title'] == 'Test Title'
    assert result['thumbnail'] == 'https://example.com/thumb.jpg'
    assert result['episode'] == 'LD Episode'
    assert result['duration'] == 60
    assert json_ld_calls == []


def test_real_extract_breadcrumb_episode_found_breaks(monkeypatch):
    breadcrumb = {
        '@context': 'http://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement:': [
            {},
            {'item:': {'@type': 'WebPage', 'name': 'Not Episode'}},
            {'item:': {'@type': 'TVEpisode', 'name': 'My Episode'}},
            {'item:': {'@type': 'TVEpisode', 'name': 'Second Episode'}},
        ],
    }
    extra = (
        '<script type="application/ld+json">'
        + json.dumps(breadcrumb) + '</script>'
    )
    webpage = _webpage(extra_head=extra)
    playlist = _playlist({
        'MediaFiles': [{'Href': 'https://example.com/movie.mp4'}],
        'Duration': '00:01:00',
    })
    ie, captured = _make_ie(monkeypatch, webpage, playlist)
    episode_items = []

    def _fake_json_ld(json_ld, video_id, fatal=True, **kwargs):
        if isinstance(json_ld, dict) and json_ld.get('@type') == 'TVEpisode':
            episode_items.append(dict(json_ld))
            return {'episode': json_ld.get('name')}
        return {}

    monkeypatch.setattr(ie, '_json_ld', _fake_json_ld, raising=False)

    result = ie._real_extract('https://www.itv.com/hub/show/vid123')

    assert result['episode'] == 'My Episode'
    assert result['title'] == 'Test Title'
    assert len(episode_items) == 1
    assert episode_items[0]['name'] == 'My Episode'
    assert episode_items[0]['@context'] == 'http://schema.org'


def test_real_extract_breadcrumb_episode_json_ld_falsy(monkeypatch):
    breadcrumb = {
        '@context': 'http://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement:': [
            {'item:': {'@type': 'TVEpisode', 'name': 'Ignored Episode'}},
        ],
    }
    extra = (
        '<script type="application/ld+json">'
        + json.dumps(breadcrumb) + '</script>'
    )
    webpage = _webpage(extra_head=extra)
    playlist = _playlist({
        'MediaFiles': [{'Href': 'https://example.com/movie.mp4'}],
    })
    ie, captured = _make_ie(monkeypatch, webpage, playlist)
    episode_items = []

    def _fake_json_ld(json_ld, video_id, fatal=True, **kwargs):
        if isinstance(json_ld, dict) and json_ld.get('@type') == 'TVEpisode':
            episode_items.append(dict(json_ld))
            return None
        return {}

    monkeypatch.setattr(ie, '_json_ld', _fake_json_ld, raising=False)

    result = ie._real_extract('https://www.itv.com/hub/show/vid123')

    assert result['id'] == 'vid123'
    assert result['title'] == 'Test Title'
    assert result.get('episode') is None
    assert len(episode_items) == 1


def test_real_extract_breadcrumb_no_episode(monkeypatch):
    breadcrumbs = [
        {
            '@context': 'http://schema.org',
            '@type': 'BreadcrumbList',
        },
        {
            '@context': 'http://schema.org',
            '@type': 'BreadcrumbList',
            'itemListElement:': [],
        },
        {
            '@context': 'http://schema.org',
            '@type': 'BreadcrumbList',
            'itemListElement:': [
                {'item:': {'@type': 'WebPage', 'name': 'Page'}},
                {'other': {}},
            ],
        },
    ]
    for breadcrumb in breadcrumbs:
        extra = (
            '<script type="application/ld+json">'
            + json.dumps(breadcrumb) + '</script>'
        )
        webpage = _webpage(extra_head=extra)
        playlist = _playlist({
            'MediaFiles': [{'Href': 'https://example.com/movie.mp4'}],
        })
        ie, captured = _make_ie(monkeypatch, webpage, playlist)

        result = ie._real_extract('https://www.itv.com/hub/show/vid123')

        assert result['id'] == 'vid123'
        assert result['title'] == 'Test Title'
        assert result.get('episode') is None
        assert {f['url'] for f in result['formats']} == {
            'https://example.com/movie.mp4'
        }


def test_real_extract_json_ld_not_breadcrumb_and_falsy_json_ld(monkeypatch):
    article = {
        '@context': 'http://schema.org',
        '@type': 'Article',
        'name': 'An Article',
    }
    webpages = [
        _webpage(extra_head=(
            '<script type="application/ld+json">'
            + json.dumps(article) + '</script>'
        )),
        _webpage(),
    ]
    for webpage in webpages:
        playlist = _playlist({
            'MediaFiles': [{'Href': 'https://example.com/movie.mp4'}],
            'Subtitles': [],
        })
        ie, captured = _make_ie(monkeypatch, webpage, playlist)
        monkeypatch.setattr(
            ie, '_search_json_ld',
            lambda html, video_id, default=None, **kwargs: {},
            raising=False)

        result = ie._real_extract('https://www.itv.com/hub/show/vid123')

        assert result['id'] == 'vid123'
        assert result['title'] == 'Test Title'
        assert result.get('episode') is None
        assert {f['url'] for f in result['formats']} == {
            'https://example.com/movie.mp4'
        }
