# file: project/youtube_dl/extractor/itv.py:54-150
# asked: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}
# gained: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}

import json
import pytest
from youtube_dl import YoutubeDL
from youtube_dl.extractor.itv import ITVIE
from youtube_dl.utils import ExtractorError


def _make_ie():
    ydl = YoutubeDL({'quiet': True, 'verbose': False})
    return ITVIE(ydl)


def test_itv_full_flow_with_json_ld(monkeypatch):
    ie = _make_ie()
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="Liar - Series 2 - Episode 6" />'
        '<script type="application/ld+json">'
        '{"@context":"http://schema.org","@type":"TVEpisode","name":"LD Title",'
        '"partOfSeries":{"@type":"TVSeries","name":"Liar"}}'
        '</script>'
        '</head><body>'
        '<div id="video" data-video-playlist="https://example.com/playlist" data-video-hmac="ab12cd"></div>'
        '<div class="episode-info__synopsis"><p>Hello <b>World</b></p></div>'
        '</body></html>'
    )
    playlist = {
        'Playlist': {
            'Video': {
                'Base': 'https://base.example.com/',
                'Duration': 'PT32M10S',
                'MediaFiles': [
                    {},
                    {'Href': '/path/video.m3u8'},
                    {'Href': '/path/video.mp4'},
                ],
                'Subtitles': [
                    'not-a-dict',
                    {'NoHref': 1},
                    {'Href': ''},
                    {'Href': 'https://example.com/subs.vtt'},
                    {'Href': 'https://example.com/subs2.srt'},
                ],
            }
        }
    }
    captured = {}

    def fake_webpage(url, video_id, *a, **k):
        assert video_id == '2a4547a0012'
        assert 'itv.com' in url
        return webpage

    def fake_json(url, video_id, *a, **k):
        captured['url'] = url
        captured['headers'] = k.get('headers')
        captured['data'] = k.get('data')
        assert url == 'https://example.com/playlist'
        return playlist

    def fake_m3u8(url, video_id, *a, **k):
        assert url.endswith('.m3u8')
        assert 'base.example.com' in url
        return [{'url': url, 'format_id': 'hls', 'ext': 'mp4'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_webpage)
    monkeypatch.setattr(ie, '_download_json', fake_json)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_m3u8)

    res = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert res['id'] == '2a4547a0012'
    assert res['title'] in ('Liar - Series 2 - Episode 6', 'LD Title')
    assert 'Hello' in (res.get('description') or '')
    assert res['duration'] == 1930
    assert len(res['formats']) == 2
    urls = [f['url'] for f in res['formats']]
    assert any(u.endswith('.m3u8') for u in urls)
    assert any(u.endswith('.mp4') for u in urls)
    assert 'en' in res['subtitles']
    assert len(res['subtitles']['en']) == 2
    assert all('url' in s for s in res['subtitles']['en'])
    hdrs = captured['headers']
    assert hdrs['hmac'] == 'AB12CD'
    assert hdrs['Accept'] == 'application/vnd.itv.vod.playlist.v2+json'
    assert hdrs['Content-Type'] == 'application/json'
    payload = json.loads(captured['data'].decode('utf-8'))
    assert payload['variantAvailability']['platformTag'] == 'dotcom'
    assert payload['client']['id'] == 'browser'


def test_itv_fallback_no_jsonld_uses_data_video_id(monkeypatch):
    ie = _make_ie()
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="Fallback Title" />'
        '</head><body>'
        '<div id="video" data-video-id="https://example.com/pl2" data-video-hmac="ef34gh"></div>'
        '<div class="episode-info__synopsis">Fallback desc</div>'
        '</body></html>'
    )
    playlist = {
        'Playlist': {
            'Video': {
                'Duration': 'PT5M',
                'MediaFiles': [{'Href': 'https://cdn.example.com/fallback.mp4'}],
            }
        }
    }

    def fake_webpage(url, video_id, *a, **k):
        return webpage

    def fake_json(url, video_id, *a, **k):
        assert url == 'https://example.com/pl2'
        assert k['headers']['hmac'] == 'EF34GH'
        return playlist

    monkeypatch.setattr(ie, '_download_webpage', fake_webpage)
    monkeypatch.setattr(ie, '_download_json', fake_json)

    res = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert res['id'] == '2a4547a0012'
    assert res['title'] == 'Fallback Title'
    assert len(res['formats']) == 1
    assert res['formats'][0]['url'] == 'https://cdn.example.com/fallback.mp4'
    assert res['subtitles'] == {}
    assert res['duration'] == 300
    assert 'Fallback desc' in (res.get('description') or '')


def test_itv_breadcrumblist_with_tvepisode(monkeypatch):
    ie = _make_ie()
    bl = {
        '@type': 'BreadcrumbList',
        'itemListElement:': [
            {'no-item': 1},
            {'item:': {'@type': 'WebPage', 'name': 'x'}},
            {'item:': {
                '@type': 'TVEpisode',
                'name': 'Ep Name',
                'partOfSeries': {'@type': 'TVSeries', 'name': 'MySeries'},
            }},
        ],
    }
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="BL Title" />'
        '<script type="application/ld+json">' + json.dumps(bl) + '</script>'
        '</head><body>'
        '<div id="video" data-video-playlist="https://example.com/pl3" data-video-hmac="aa11"></div>'
        '<div class="episode-info__synopsis">desc3</div>'
        '</body></html>'
    )
    playlist = {
        'Playlist': {
            'Video': {
                'MediaFiles': [{'Href': 'https://cdn.example.com/v.mp4'}],
                'Subtitles': [{'Href': 'https://example.com/a.vtt'}],
                'Duration': 'PT1M',
            }
        }
    }

    monkeypatch.setattr(ie, '_download_webpage', lambda url, vid, *a, **k: webpage)
    monkeypatch.setattr(ie, '_download_json', lambda url, vid, *a, **k: playlist)
    monkeypatch.setattr(ie, '_search_json_ld', lambda html, vid, **k: {})

    res = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert res['id'] == '2a4547a0012'
    assert len(res['formats']) == 1
    assert res['formats'][0]['url'] == 'https://cdn.example.com/v.mp4'
    assert res['subtitles']['en'][0]['url'] == 'https://example.com/a.vtt'
    assert res['subtitles']['en'][0]['ext'] == 'vtt'
    assert res.get('series') == 'MySeries' or 'Ep Name' in str(res.values())


def test_itv_breadcrumblist_empty_itemlist(monkeypatch):
    ie = _make_ie()
    bl = {'@type': 'BreadcrumbList'}
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="Empty BL" />'
        '<script type="application/ld+json">' + json.dumps(bl) + '</script>'
        '</head><body>'
        '<div id="video" data-video-playlist="https://example.com/pl4" data-video-hmac="bb22"></div>'
        '<div class="episode-info__synopsis">desc4</div>'
        '</body></html>'
    )
    playlist = {
        'Playlist': {
            'Video': {
                'Base': 'https://b.example.com/',
                'MediaFiles': [{'Href': '/x.m3u8'}],
                'Subtitles': [],
                'Duration': 'PT10S',
            }
        }
    }

    monkeypatch.setattr(ie, '_download_webpage', lambda url, vid, *a, **k: webpage)
    monkeypatch.setattr(ie, '_download_json', lambda url, vid, *a, **k: playlist)
    monkeypatch.setattr(ie, '_search_json_ld', lambda html, vid, **k: {})
    monkeypatch.setattr(
        ie, '_extract_m3u8_formats',
        lambda url, vid, *a, **k: [{'url': url, 'format_id': 'hls'}])

    res = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert res['id'] == '2a4547a0012'
    assert res['title'] == 'Empty BL'
    assert len(res['formats']) == 1
    assert res['duration'] == 10


def test_itv_breadcrumblist_jsonld_returns_none(monkeypatch):
    ie = _make_ie()
    bl = {
        '@type': 'BreadcrumbList',
        'itemListElement:': [
            {'item:': {'@type': 'TVEpisode', 'name': 'Ep2'}},
        ],
    }
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="None BL" />'
        '<script type="application/ld+json">' + json.dumps(bl) + '</script>'
        '</head><body>'
        '<div id="video" data-video-id="https://example.com/pl6" data-video-hmac="dd44"></div>'
        '<div class="episode-info__synopsis">desc6</div>'
        '</body></html>'
    )
    playlist = {
        'Playlist': {
            'Video': {
                'MediaFiles': [{'Href': 'https://cdn.example.com/v6.mp4'}],
                'Duration': 'PT20S',
            }
        }
    }

    monkeypatch.setattr(ie, '_download_webpage', lambda url, vid, *a, **k: webpage)
    monkeypatch.setattr(ie, '_download_json', lambda url, vid, *a, **k: playlist)
    monkeypatch.setattr(ie, '_search_json_ld', lambda html, vid, **k: {})
    monkeypatch.setattr(ie, '_json_ld', lambda item, vid, **k: None)

    res = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert res['id'] == '2a4547a0012'
    assert res['title'] == 'None BL'
    assert len(res['formats']) == 1


def test_itv_jsonld_wrong_type(monkeypatch):
    ie = _make_ie()
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="Wrong Type" />'
        '<script type="application/ld+json">{"@type":"WebPage","name":"foo"}</script>'
        '</head><body>'
        '<div id="video" data-video-id="https://example.com/pl5" data-video-hmac="cc33"></div>'
        '<div class="episode-info__synopsis">desc5</div>'
        '</body></html>'
    )
    playlist = {
        'Playlist': {
            'Video': {
                'MediaFiles': [{'Href': 'https://cdn.example.com/v2.mp4'}],
                'Subtitles': [{'Href': 'https://example.com/s'}],
                'Duration': None,
            }
        }
    }

    monkeypatch.setattr(ie, '_download_webpage', lambda url, vid, *a, **k: webpage)
    monkeypatch.setattr(ie, '_download_json', lambda url, vid, *a, **k: playlist)
    monkeypatch.setattr(ie, '_search_json_ld', lambda html, vid, **k: {})

    res = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert res['id'] == '2a4547a0012'
    assert res['title'] == 'Wrong Type'
    assert len(res['formats']) == 1
    assert res['formats'][0]['url'] == 'https://cdn.example.com/v2.mp4'
    assert res['subtitles']['en'][0]['ext'] == 'vtt'
    assert res['subtitles']['en'][0]['url'] == 'https://example.com/s'


def test_itv_no_mediafiles_raises(monkeypatch):
    ie = _make_ie()
    webpage = (
        '<html><head>'
        '<meta property="og:title" content="No Media" />'
        '</head><body>'
        '<div id="video" data-video-id="https://example.com/pl7" data-video-hmac="ee55"></div>'
        '<div class="episode-info__synopsis">desc7</div>'
        '</body></html>'
    )
    playlist = {'Playlist': {'Video': {}}}

    monkeypatch.setattr(ie, '_download_webpage', lambda url, vid, *a, **k: webpage)
    monkeypatch.setattr(ie, '_download_json', lambda url, vid, *a, **k: playlist)

    with pytest.raises(ExtractorError):
        ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')
