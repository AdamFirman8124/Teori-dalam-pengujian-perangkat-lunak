# file: project/youtube_dl/extractor/itv.py:54-150
# asked: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}
# gained: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [136, 137], [138, 136], [138, 139]]}

import json

import pytest

from youtube_dl.extractor.itv import ITVIE


class FakeDownloader(object):
    def __init__(self):
        self.warnings = []
        self.params = {}

    def report_warning(self, msg, video_id=None):
        self.warnings.append(msg)

    def to_screen(self, *args, **kwargs):
        pass

    def report_error(self, *args, **kwargs):
        pass


def _make_ie(monkeypatch):
    ie = ITVIE(FakeDownloader())
    monkeypatch.setattr(ie, 'geo_verification_headers', lambda: {'X-Geo': 'GB'})
    monkeypatch.setattr(ie, '_sort_formats', lambda formats: None)
    return ie


def _webpage(params_attrs, extra=''):
    return (
        '<html><head>'
        '<meta property="og:title" content="Liar - Series 2 - Episode 6" />'
        '%s'
        '</head><body>'
        '<div id="video" %s></div>'
        '<div class="episode-info__synopsis">Some <b>synopsis</b> text</div>'
        '</body></html>' % (extra, params_attrs)
    )


def test_itv_full_extraction_with_breadcrumb_fallback(monkeypatch):
    ie = _make_ie(monkeypatch)

    webpage = _webpage(
        'data-video-playlist="http://example.com/playlist" data-video-hmac="abc"',
        extra=(
            '<script type="application/ld+json">'
            '{"@type": "BreadcrumbList", "itemListElement:": '
            '[{"item:": {"@type": "TVEpisode"}}]}'
            '</script>'
        ),
    )

    playlist = {
        'Playlist': {
            'Video': {
                'Base': 'http://base.example.com/',
                'MediaFiles': [
                    {'Href': 'video.m3u8'},
                    {'Href': 'video.mp4'},
                    {'Href': ''},
                    {},
                ],
                'Subtitles': [
                    {'Href': 'http://subs.example.com/en.vtt'},
                    'not-a-dict',
                    {'Href': 'not a url'},
                ],
                'Duration': '01:00:00',
            },
        },
    }

    calls = {}

    def fake_download_json(url, video_id, **kwargs):
        calls['url'] = url
        calls['video_id'] = video_id
        calls['data'] = kwargs.get('data')
        calls['headers'] = kwargs.get('headers')
        return playlist

    monkeypatch.setattr(ie, '_download_webpage', lambda url, video_id, **kw: webpage)
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(
        ie, '_extract_m3u8_formats',
        lambda href, video_id, ext, **kw: [{'url': href, 'format_id': 'hls-1'}])
    monkeypatch.setattr(ie, '_search_json_ld', lambda webpage, video_id, **kw: {})
    monkeypatch.setattr(
        ie, '_json_ld',
        lambda json_ld, video_id, **kw: {'series': 'Liar', 'season_number': 2})
    monkeypatch.setattr(
        ie, '_html_search_meta',
        lambda names, webpage, **kw: 'Liar - Series 2 - Episode 6')

    info = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert calls['url'] == 'http://example.com/playlist'
    assert calls['video_id'] == '2a4547a0012'
    assert calls['headers']['hmac'] == 'ABC'
    assert calls['headers']['Accept'] == 'application/vnd.itv.vod.playlist.v2+json'
    assert calls['headers']['Content-Type'] == 'application/json'
    assert calls['headers']['X-Geo'] == 'GB'
    payload = json.loads(calls['data'])
    assert payload['client'] == {'version': '4.1', 'id': 'browser'}
    assert payload['variantAvailability']['platformTag'] == 'dotcom'

    assert info['id'] == '2a4547a0012'
    assert info['title'] == 'Liar - Series 2 - Episode 6'
    assert info['duration'] == 3600.0
    assert info['description'] == 'Some synopsis text'
    assert info['series'] == 'Liar'
    assert info['season_number'] == 2

    assert [f['url'] for f in info['formats']] == [
        'http://base.example.com/video.m3u8',
        'http://base.example.com/video.mp4',
    ]
    assert info['subtitles'] == {
        'en': [{'url': 'http://subs.example.com/en.vtt', 'ext': 'vtt'}],
    }


def test_itv_no_base_no_subtitles_and_json_ld_present(monkeypatch):
    ie = _make_ie(monkeypatch)

    webpage = _webpage('data-video-id="http://example.com/playlist2" data-video-hmac="def"')

    playlist = {
        'Playlist': {
            'Video': {
                'MediaFiles': [{'Href': 'video.mp4'}],
            },
        },
    }

    calls = {}

    def fake_download_json(url, video_id, **kwargs):
        calls['url'] = url
        return playlist

    monkeypatch.setattr(ie, '_download_webpage', lambda url, video_id, **kw: webpage)
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(
        ie, '_search_json_ld',
        lambda webpage, video_id, **kw: {'title': 'From JSON-LD'})
    monkeypatch.setattr(
        ie, '_html_search_meta',
        lambda names, webpage, **kw: 'Meta Title')

    info = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert calls['url'] == 'http://example.com/playlist2'
    assert info['formats'] == [{'url': 'video.mp4'}]
    assert info['subtitles'] == {}
    assert 'duration' not in info
    assert info['description'] == 'Some synopsis text'
    assert info['title'] == 'Meta Title'


def test_itv_breadcrumb_without_episode_and_json_ld_returning_none(monkeypatch):
    ie = _make_ie(monkeypatch)

    webpage = _webpage(
        'data-video-playlist="http://example.com/playlist" data-video-hmac="ghi"',
        extra=(
            '<script type="application/ld+json">'
            '{"@type": "BreadcrumbList", "itemListElement:": ['
            '{"item:": null},'
            '{"item:": {"@type": "Clip"}},'
            '{"item:": {"@type": "TVEpisode"}}'
            ']}'
            '</script>'
        ),
    )

    playlist = {'Playlist': {'Video': {'MediaFiles': []}}}

    monkeypatch.setattr(ie, '_download_webpage', lambda url, video_id, **kw: webpage)
    monkeypatch.setattr(ie, '_download_json', lambda url, video_id, **kw: playlist)
    monkeypatch.setattr(ie, '_search_json_ld', lambda webpage, video_id, **kw: {})
    monkeypatch.setattr(ie, '_json_ld', lambda json_ld, video_id, **kw: None)
    monkeypatch.setattr(
        ie, '_html_search_meta',
        lambda names, webpage, **kw: 'Meta Title')

    info = ie._real_extract('https://www.itv.com/hub/liar/2a4547a0012')

    assert info['id'] == '2a4547a0012'
    assert info['formats'] == []
    assert info['subtitles'] == {}
    assert info['title'] == 'Meta Title'
    assert 'series' not in info
