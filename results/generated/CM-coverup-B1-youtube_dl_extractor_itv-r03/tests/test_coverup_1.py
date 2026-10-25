# file: project/youtube_dl/extractor/itv.py:54-150
# asked: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}
# gained: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [138, 139]]}

import json

import pytest

from youtube_dl.extractor.itv import ITVIE


class FakeDownloader(object):
    def __init__(self, params=None):
        self.params = params or {}

    def report_warning(self, *args, **kwargs):
        pass


def _make_ie(params=None):
    return ITVIE(FakeDownloader(params))


WEBPAGE_FULL = '''<!DOCTYPE html>
<html><head>
<meta property="og:title" content="Liar - Series 2 - Episode 6" />
</head><body>
<div id="video" data-video-playlist="https://example.com/playlist" data-video-hmac="abc123"></div>
<div class="episode-info__synopsis">A <b>great</b> episode</div>
</body></html>'''

WEBPAGE_BREADCRUMB = '''<!DOCTYPE html>
<html><head>
<script type="application/ld+json">{"@type": "BreadcrumbList", "itemListElement:": [{"item:": {"@type": "TVEpisode", "name": "Ep"}}]}</script>
</head><body>
<div id="video" data-video-id="https://example.com/playlist2" data-video-hmac="def456"></div>
<div class="episode-info__synopsis">Synopsis</div>
</body></html>'''

WEBPAGE_OTHER_JSONLD = '''<!DOCTYPE html>
<html><head>
<script type="application/ld+json">{"@type": "VideoObject", "name": "Not a breadcrumb"}</script>
</head><body>
<div id="video" data-video-playlist="https://example.com/playlist3" data-video-hmac="ghi789"></div>
<div class="episode-info__synopsis">Other</div>
</body></html>'''

WEBPAGE_NO_JSONLD = '''<!DOCTYPE html>
<html><head></head><body>
<div id="video" data-video-playlist="https://example.com/playlist4" data-video-hmac="jkl012"></div>
<div class="episode-info__synopsis">Plain</div>
</body></html>'''


def test_real_extract_full_playlist(monkeypatch):
    ie = _make_ie({'geo_verification_proxy': 'http://proxy.example.com'})
    url = 'https://www.itv.com/hub/liar/2a4547a0012'

    monkeypatch.setattr(ie, '_download_webpage', lambda *a, **k: WEBPAGE_FULL)

    captured = {}

    def fake_download_json(u, vid, data=None, headers=None, **kwargs):
        captured['url'] = u
        captured['video_id'] = vid
        captured['data'] = data
        captured['headers'] = headers
        return {
            'Playlist': {
                'Video': {
                    'Base': 'https://base.example.com/',
                    'MediaFiles': [
                        {'Href': 'stream.m3u8'},
                        {'Href': 'video.mp4'},
                        {'Href': None},
                    ],
                    'Subtitles': [
                        'not-a-dict',
                        {'Href': None},
                        {'Href': 'https://subs.example.com/en.vtt'},
                    ],
                    'Duration': '00:01:00',
                },
            },
        }

    monkeypatch.setattr(ie, '_download_json', fake_download_json)

    m3u8_calls = []

    def fake_m3u8(href, vid, ext, **kwargs):
        m3u8_calls.append((href, vid, ext, kwargs))
        return [{'url': href, 'format_id': 'hls-1', 'ext': 'mp4'}]

    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_m3u8)
    monkeypatch.setattr(
        ie, '_search_json_ld',
        lambda *a, **k: {'series': 'Liar', 'season_number': 2})
    monkeypatch.setattr(
        ie, '_html_search_meta',
        lambda *a, **k: 'Liar - Series 2 - Episode 6')

    result = ie._real_extract(url)

    assert captured['url'] == 'https://example.com/playlist'
    assert captured['video_id'] == '2a4547a0012'
    assert captured['headers']['hmac'] == 'ABC123'
    assert captured['headers']['Accept'] == 'application/vnd.itv.vod.playlist.v2+json'
    assert captured['headers']['Content-Type'] == 'application/json'
    assert captured['headers']['Ytdl-request-proxy'] == 'http://proxy.example.com'
    assert isinstance(captured['data'], bytes)
    payload = json.loads(captured['data'].decode('utf-8'))
    assert payload['client'] == {'version': '4.1', 'id': 'browser'}
    assert payload['variantAvailability']['platformTag'] == 'dotcom'
    assert payload['device']['os']['name'] == 'Windows NT'

    assert len(m3u8_calls) == 1
    assert m3u8_calls[0][0] == 'https://base.example.com/stream.m3u8'
    assert m3u8_calls[0][1] == '2a4547a0012'
    assert m3u8_calls[0][2] == 'mp4'
    assert m3u8_calls[0][3]['entry_protocol'] == 'm3u8_native'
    assert m3u8_calls[0][3]['m3u8_id'] == 'hls'
    assert m3u8_calls[0][3]['fatal'] is False

    assert result['id'] == '2a4547a0012'
    assert result['title'] == 'Liar - Series 2 - Episode 6'
    assert result['duration'] == 60
    assert result['description'] == 'A great episode'
    assert result['series'] == 'Liar'
    assert result['season_number'] == 2
    assert result['subtitles'] == {
        'en': [{'url': 'https://subs.example.com/en.vtt', 'ext': 'vtt'}]}
    urls = [f['url'] for f in result['formats']]
    assert 'https://base.example.com/stream.m3u8' in urls
    assert 'https://base.example.com/video.mp4' in urls


def test_real_extract_data_video_id_and_breadcrumb_fallback(monkeypatch):
    ie = _make_ie()
    url = 'https://www.itv.com/hub/through-the-keyhole/2a2271a0033'

    monkeypatch.setattr(ie, '_download_webpage', lambda *a, **k: WEBPAGE_BREADCRUMB)

    captured = {}

    def fake_download_json(u, vid, data=None, headers=None, **kwargs):
        captured['url'] = u
        captured['headers'] = headers
        return {
            'Playlist': {
                'Video': {
                    'MediaFiles': [{'Href': 'video.mp4'}],
                    'Subtitles': [],
                    'Duration': None,
                },
            },
        }

    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_search_json_ld', lambda *a, **k: {})

    json_ld_calls = []

    def fake_json_ld(item, vid, **kwargs):
        json_ld_calls.append((item, vid, kwargs))
        return {'series': 'Through the Keyhole', 'season_number': 2}

    monkeypatch.setattr(ie, '_json_ld', fake_json_ld)
    monkeypatch.setattr(ie, '_html_search_meta', lambda *a, **k: 'Through the Keyhole')

    result = ie._real_extract(url)

    assert captured['url'] == 'https://example.com/playlist2'
    assert captured['headers']['hmac'] == 'DEF456'

    assert len(json_ld_calls) == 1
    item, vid, kwargs = json_ld_calls[0]
    assert item['@type'] == 'TVEpisode'
    assert item['@context'] == 'http://schema.org'
    assert vid == '2a2271a0033'
    assert kwargs['fatal'] is False

    assert result['id'] == '2a2271a0033'
    assert result['series'] == 'Through the Keyhole'
    assert result['season_number'] == 2
    # merge_dicts drops None values, so parse_duration(None) -> no 'duration' key
    assert 'duration' not in result
    assert result['subtitles'] == {}
    assert result['formats'] == [{'url': 'video.mp4', 'ext': 'mp4'}]


def test_real_extract_json_ld_not_breadcrumb_list(monkeypatch):
    ie = _make_ie()
    url = 'https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034'

    monkeypatch.setattr(ie, '_download_webpage', lambda *a, **k: WEBPAGE_OTHER_JSONLD)
    monkeypatch.setattr(
        ie, '_download_json',
        lambda *a, **k: {'Playlist': {'Video': {
            'MediaFiles': [{'Href': 'video.mp4'}],
            'Subtitles': [],
        }}})
    monkeypatch.setattr(ie, '_search_json_ld', lambda *a, **k: {})

    json_ld_calls = []
    monkeypatch.setattr(
        ie, '_json_ld',
        lambda *a, **k: json_ld_calls.append(a) or {'series': 'should not happen'})
    monkeypatch.setattr(ie, '_html_search_meta', lambda *a, **k: 'Some Title')

    result = ie._real_extract(url)

    assert json_ld_calls == []
    assert 'series' not in result
    assert result['title'] == 'Some Title'
    assert result['formats'] == [{'url': 'video.mp4', 'ext': 'mp4'}]


def test_real_extract_no_json_ld_at_all(monkeypatch):
    ie = _make_ie()
    url = 'https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024'

    monkeypatch.setattr(ie, '_download_webpage', lambda *a, **k: WEBPAGE_NO_JSONLD)
    monkeypatch.setattr(
        ie, '_download_json',
        lambda *a, **k: {'Playlist': {'Video': {
            'MediaFiles': [{'Href': 'video.mp4'}],
            'Subtitles': [],
        }}})
    monkeypatch.setattr(ie, '_search_json_ld', lambda *a, **k: {})

    json_ld_calls = []
    monkeypatch.setattr(ie, '_json_ld', lambda *a, **k: json_ld_calls.append(a) or {})
    monkeypatch.setattr(ie, '_html_search_meta', lambda *a, **k: 'Plain Title')

    result = ie._real_extract(url)

    assert json_ld_calls == []
    assert result['id'] == '2a2898a0024'
    assert result['title'] == 'Plain Title'
    assert result['description'] == 'Plain'
    assert result['formats'] == [{'url': 'video.mp4', 'ext': 'mp4'}]
