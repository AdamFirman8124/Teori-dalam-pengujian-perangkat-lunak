# file: project/youtube_dl/extractor/itv.py:54-150
# asked: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}
# gained: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}

import json

import pytest

from youtube_dl import YoutubeDL
from youtube_dl.extractor.itv import ITVIE
from youtube_dl.utils import ExtractorError

_UNSET = object()
_URL = 'https://www.itv.com/hub/test-show/2a1234a0001'
_VIDEO_ID = '2a1234a0001'


def _webpage(head_extra='', video_attrs='data-video-playlist="https://example.com/playlist.json" data-video-hmac="abc123"'):
    return (
        '<html><head>'
        '<meta property="og:title" content="Test Title">'
        + head_extra
        + '</head><body>'
        '<div id="video" ' + video_attrs + '></div>'
        '<div class="episode-info__synopsis">Synopsis <b>here</b></div>'
        '</body></html>'
    )


def _playlist(video_data):
    return {'Playlist': {'Video': video_data}}


def _make_ie(monkeypatch, webpage, playlist, search_json_ld=_UNSET, json_ld_result=_UNSET):
    ie = ITVIE(YoutubeDL({'quiet': True, 'no_warnings': True}))
    captured = {}

    monkeypatch.setattr(ie, '_download_webpage', lambda url, video_id: webpage)

    def fake_download_json(url, video_id, data=None, headers=None, **kwargs):
        captured['playlist_url'] = url
        captured['download_video_id'] = video_id
        captured['data'] = data
        captured['headers'] = headers
        captured['download_kwargs'] = kwargs
        return playlist

    monkeypatch.setattr(ie, '_download_json', fake_download_json)

    def fake_m3u8(url, video_id, ext=None, **kwargs):
        captured.setdefault('m3u8_calls', []).append((url, video_id, ext, kwargs))
        return [{'url': url, 'format_id': 'hls-1', 'ext': 'mp4'}]

    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_m3u8)

    if search_json_ld is not _UNSET:
        monkeypatch.setattr(
            ie, '_search_json_ld',
            lambda webpage_arg, video_id, default=None: search_json_ld)

    if json_ld_result is not _UNSET:
        def fake_json_ld(item, video_id, fatal=True, **kwargs):
            captured.setdefault('json_ld_calls', []).append(
                (dict(item), video_id, fatal))
            return json_ld_result

        monkeypatch.setattr(ie, '_json_ld', fake_json_ld)

    return ie, captured


def test_happy_path_playlist_url_base_m3u8_mp4_and_subtitles(monkeypatch):
    webpage = _webpage()
    playlist = _playlist({
        'Base': 'https://cdn.example.com/',
        'Duration': '00:02:30',
        'MediaFiles': [
            {'Href': ''},
            {},
            {'Href': 'video.m3u8'},
            {'Href': 'video.mp4'},
        ],
        'Subtitles': [
            'not-a-dict',
            {'Href': ''},
            {},
            {'Href': 'https://example.com/subs.vtt'},
            {'Href': 'https://example.com/subs-noext'},
        ],
    })
    ie, captured = _make_ie(
        monkeypatch, webpage, playlist,
        search_json_ld={'series': 'My Series', 'season_number': 2, 'episode_number': 3})

    result = ie._real_extract(_URL)

    assert captured['playlist_url'] == 'https://example.com/playlist.json'
    assert captured['download_video_id'] == _VIDEO_ID
    assert captured['headers']['hmac'] == 'ABC123'
    assert captured['headers']['Accept'] == 'application/vnd.itv.vod.playlist.v2+json'
    assert captured['headers']['Content-Type'] == 'application/json'
    payload = json.loads(captured['data'].decode('utf-8'))
    assert payload['user'] == {'itvUserId': '', 'entitlements': [], 'token': ''}
    assert payload['device']['manufacturer'] == 'Safari'
    assert payload['device']['os'] == {'name': 'Windows NT', 'version': '6.1', 'type': 'desktop'}
    assert payload['client'] == {'version': '4.1', 'id': 'browser'}
    assert payload['variantAvailability'] == {
        'featureset': {
            'min': ['hls', 'aes', 'outband-webvtt'],
            'max': ['hls', 'aes', 'outband-webvtt'],
        },
        'platformTag': 'dotcom',
    }
    assert captured['m3u8_calls'] == [(
        'https://cdn.example.com/video.m3u8', _VIDEO_ID, 'mp4',
        {'entry_protocol': 'm3u8_native', 'm3u8_id': 'hls', 'fatal': False})]
    assert result['id'] == _VIDEO_ID
    assert result['title'] == 'Test Title'
    assert sorted(f['url'] for f in result['formats']) == [
        'https://cdn.example.com/video.m3u8',
        'https://cdn.example.com/video.mp4',
    ]
    assert result['subtitles'] == {'en': [
        {'url': 'https://example.com/subs.vtt', 'ext': 'vtt'},
        {'url': 'https://example.com/subs-noext', 'ext': 'vtt'},
    ]}
    assert result['duration'] == 150
    assert result['description'] == 'Synopsis here'
    assert result['series'] == 'My Series'
    assert result['season_number'] == 2
    assert result['episode_number'] == 3


def test_fallback_playlist_url_no_base_and_no_json_ld(monkeypatch):
    webpage = _webpage(
        video_attrs='data-video-id="https://example.com/fallback.json" data-video-hmac="def456"')
    playlist = _playlist({
        'Duration': '01:00',
        'MediaFiles': [{'Href': 'https://example.com/movie.mp4'}],
        # No 'Base' and no 'Subtitles' keys: exercises falsy .get() branches.
    })
    ie, captured = _make_ie(monkeypatch, webpage, playlist)

    result = ie._real_extract(_URL)

    assert captured['playlist_url'] == 'https://example.com/fallback.json'
    assert captured['headers']['hmac'] == 'DEF456'
    assert captured.get('m3u8_calls', []) == []
    assert result['id'] == _VIDEO_ID
    assert result['title'] == 'Test Title'
    assert [f['url'] for f in result['formats']] == ['https://example.com/movie.mp4']
    assert result['subtitles'] == {}
    assert result['duration'] == 60
    assert result['description'] == 'Synopsis here'


def test_breadcrumb_list_tv_episode(monkeypatch):
    ld = {
        '@type': 'BreadcrumbList',
        'itemListElement:': [
            {},
            {'item:': {'@type': 'VideoObject', 'name': 'Not an episode'}},
            {'item:': {'@type': 'TVEpisode', 'name': 'Episode 6'}},
            {'item:': {'@type': 'TVEpisode', 'name': 'Must not be reached'}},
        ],
    }
    webpage = _webpage(
        head_extra='<script type="application/ld+json">'
        + json.dumps(ld) + '</script>')
    playlist = _playlist({
        'Duration': '00:01:00',
        'MediaFiles': [{'Href': 'https://example.com/ep.mp4'}],
        'Subtitles': [],
    })
    ie, captured = _make_ie(
        monkeypatch, webpage, playlist, search_json_ld={},
        json_ld_result={'series': 'Liar', 'season_number': 2, 'episode_number': 6})

    result = ie._real_extract(_URL)

    # Break after first TVEpisode: exactly one call, with @context injected.
    assert len(captured['json_ld_calls']) == 1
    item, video_id, fatal = captured['json_ld_calls'][0]
    assert item == {
        '@type': 'TVEpisode', 'name': 'Episode 6',
        '@context': 'http://schema.org',
    }
    assert video_id == _VIDEO_ID
    assert fatal is False
    assert result['series'] == 'Liar'
    assert result['season_number'] == 2
    assert result['episode_number'] == 6
    assert result['title'] == 'Test Title'
    assert result['subtitles'] == {}


def test_breadcrumb_list_tv_episode_json_ld_returns_none(monkeypatch):
    ld = {
        '@type': 'BreadcrumbList',
        'itemListElement:': [
            {'item:': {'@type': 'TVEpisode', 'name': 'Episode 1'}},
        ],
    }
    webpage = _webpage(
        head_extra='<script type="application/ld+json">'
        + json.dumps(ld) + '</script>')
    playlist = _playlist({
        'MediaFiles': [{'Href': 'https://example.com/ep.mp4'}],
    })
    ie, captured = _make_ie(
        monkeypatch, webpage, playlist, search_json_ld={},
        json_ld_result=None)

    result = ie._real_extract(_URL)

    assert len(captured['json_ld_calls']) == 1
    assert result['id'] == _VIDEO_ID
    assert result['title'] == 'Test Title'
    assert 'series' not in result
    assert [f['url'] for f in result['formats']] == ['https://example.com/ep.mp4']
    # merge_dicts drops None values, so 'duration' is absent entirely.
    assert result.get('duration') is None


@pytest.mark.parametrize('ld_obj', [
    {'@type': 'VideoObject', 'name': 'Not a breadcrumb'},
    {'@type': 'BreadcrumbList'},
    {'@type': 'BreadcrumbList', 'itemListElement:': None},
    {'@type': 'BreadcrumbList', 'itemListElement:': []},
    {'@type': 'BreadcrumbList', 'itemListElement:': [
        {'item:': {'@type': 'VideoObject'}}]},
])
def test_json_ld_without_tv_episode(monkeypatch, ld_obj):
    webpage = _webpage(
        head_extra='<script type="application/ld+json">'
        + json.dumps(ld_obj) + '</script>')
    playlist = _playlist({
        'Duration': '00:00:30',
        'MediaFiles': [{'Href': 'https://example.com/v.mp4'}],
        'Subtitles': [{'Href': 'https://example.com/cap.vtt'}],
    })
    ie, captured = _make_ie(
        monkeypatch, webpage, playlist, search_json_ld={},
        json_ld_result={'should': 'not be used'})

    result = ie._real_extract(_URL)

    assert captured.get('json_ld_calls', []) == []
    assert result['id'] == _VIDEO_ID
    assert result['title'] == 'Test Title'
    assert result['duration'] == 30
    assert result['subtitles'] == {
        'en': [{'url': 'https://example.com/cap.vtt', 'ext': 'vtt'}]}
    assert 'should' not in result


@pytest.mark.parametrize('video_data', [
    {},
    {'MediaFiles': None},
    {'MediaFiles': []},
    {'MediaFiles': [{'Href': ''}, {}]},
])
def test_no_valid_media_files_raises(monkeypatch, video_data):
    webpage = _webpage()
    playlist = _playlist(video_data)
    ie, captured = _make_ie(
        monkeypatch, webpage, playlist, search_json_ld={'series': 'Unused'})

    with pytest.raises(ExtractorError):
        ie._real_extract(_URL)

    assert captured['playlist_url'] == 'https://example.com/playlist.json'
