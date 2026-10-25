# file: project/youtube_dl/extractor/itv.py:54-150
# asked: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [136, 143], [138, 136], [138, 139]]}
# gained: {"lines": [55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 80, 81, 84, 85, 86, 88, 89, 90, 91, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150], "branches": [[100, 101], [100, 115], [102, 103], [102, 104], [104, 105], [104, 106], [107, 108], [107, 112], [119, 120], [119, 130], [120, 121], [120, 122], [123, 124], [123, 125], [131, 132], [131, 143], [135, 136], [135, 143], [136, 137], [138, 139]]}

import json

from youtube_dl.extractor.itv import ITVIE


URL = 'https://www.itv.com/hub/liar/2a4547a0012'
VIDEO_ID = '2a4547a0012'


class FakeDownloader(object):
    def __init__(self, params=None):
        self.params = params or {}
        self.warnings = []

    def report_warning(self, msg, video_id=None):
        self.warnings.append(msg)


def make_extractor(params=None):
    return ITVIE(FakeDownloader(params))


def test_real_extract_full_path(monkeypatch):
    webpage = '''
    <html><head>
    <meta property="og:title" content="Liar - Series 2 - Episode 6">
    </head><body>
    <div id="video" data-video-playlist="https://example.com/playlist" data-video-hmac="abc123"></div>
    <div class="episode-info__synopsis"><p>Some &amp; synopsis</p></div>
    </body></html>
    '''
    playlist = {
        'Playlist': {
            'Video': {
                'Base': 'https://cdn.example.com/',
                'MediaFiles': [
                    {'Href': 'master.m3u8'},
                    {'Href': 'video.mp4'},
                    {'Href': None},
                    {},
                ],
                'Subtitles': [
                    {'Href': 'https://cdn.example.com/sub.vtt'},
                    {'Href': 'not a url'},
                    'not a dict',
                    {'Href': None},
                ],
                'Duration': '00:45:00',
            },
        },
    }
    calls = {}

    def fake_download_json(url, video_id, data=None, headers=None, **kwargs):
        calls['url'] = url
        calls['video_id'] = video_id
        calls['data'] = data
        calls['headers'] = headers
        return playlist

    extractor = make_extractor({'geo_verification_proxy': 'http://proxy.example.com'})
    monkeypatch.setattr(extractor, '_download_webpage', lambda *a, **k: webpage)
    monkeypatch.setattr(extractor, '_download_json', fake_download_json)
    monkeypatch.setattr(
        extractor, '_extract_m3u8_formats',
        lambda *a, **k: [{'url': 'https://cdn.example.com/master.m3u8', 'format_id': 'hls'}])
    monkeypatch.setattr(
        extractor, '_search_json_ld',
        lambda *a, **k: {'title': 'JSON-LD title', 'series': 'Liar'})
    monkeypatch.setattr(extractor, '_html_search_meta', lambda *a, **k: 'Meta title')

    info = extractor._real_extract(URL)

    assert calls['url'] == 'https://example.com/playlist'
    assert calls['video_id'] == VIDEO_ID
    assert isinstance(calls['data'], bytes)
    payload = json.loads(calls['data'].decode('utf-8'))
    assert payload['user'] == {'itvUserId': '', 'entitlements': [], 'token': ''}
    assert payload['device']['manufacturer'] == 'Safari'
    assert payload['device']['os'] == {'name': 'Windows NT', 'version': '6.1', 'type': 'desktop'}
    assert payload['client'] == {'version': '4.1', 'id': 'browser'}
    assert payload['variantAvailability']['featureset']['min'] == ['hls', 'aes', 'outband-webvtt']
    assert payload['variantAvailability']['platformTag'] == 'dotcom'
    assert calls['headers']['hmac'] == 'ABC123'
    assert calls['headers']['Accept'] == 'application/vnd.itv.vod.playlist.v2+json'
    assert calls['headers']['Content-Type'] == 'application/json'
    assert calls['headers']['Ytdl-request-proxy'] == 'http://proxy.example.com'

    assert info['id'] == VIDEO_ID
    # merge_dicts gives precedence to the base dict, so the meta title wins
    assert info['title'] == 'Meta title'
    # keys only present in the JSON-LD info are merged in
    assert info['series'] == 'Liar'
    assert info['duration'] == 2700
    assert info['description'] == 'Some & synopsis'
    urls = [f['url'] for f in info['formats']]
    assert 'https://cdn.example.com/master.m3u8' in urls
    assert 'https://cdn.example.com/video.mp4' in urls
    assert len(urls) == 2
    assert info['subtitles'] == {
        'en': [{'url': 'https://cdn.example.com/sub.vtt', 'ext': 'vtt'}]}


def test_real_extract_breadcrumb_list_fallback(monkeypatch):
    webpage = '''
    <html><head><meta property="og:title" content="Meta title"></head><body>
    <div id="video" data-video-id="https://example.com/playlist2" data-video-hmac="deadbeef"></div>
    <div class="episode-info__synopsis">Synopsis text</div>
    <script type="application/ld+json">
    {"@type": "BreadcrumbList", "itemListElement:": [
        {"item:": {"@type": "TVEpisode", "name": "Episode"}},
        {"item:": {"@type": "TVSeries", "name": "Series"}}
    ]}
    </script>
    </body></html>
    '''
    playlist = {
        'Playlist': {
            'Video': {
                'MediaFiles': [{'Href': 'https://cdn.example.com/a.mp4'}],
                'Subtitles': [],
            },
        },
    }
    calls = {}

    def fake_download_json(url, video_id, data=None, headers=None, **kwargs):
        calls['url'] = url
        calls['headers'] = headers
        return playlist

    json_ld_calls = []

    def fake_json_ld(json_ld, video_id, fatal=True, expected_type=None):
        json_ld_calls.append(json_ld)
        return {'title': 'From breadcrumb'}

    extractor = make_extractor()
    monkeypatch.setattr(extractor, '_download_webpage', lambda *a, **k: webpage)
    monkeypatch.setattr(extractor, '_download_json', fake_download_json)
    monkeypatch.setattr(extractor, '_search_json_ld', lambda *a, **k: {})
    monkeypatch.setattr(extractor, '_json_ld', fake_json_ld)
    monkeypatch.setattr(extractor, '_html_search_meta', lambda *a, **k: 'Meta title')

    info = extractor._real_extract(URL)

    assert calls['url'] == 'https://example.com/playlist2'
    assert calls['headers']['hmac'] == 'DEADBEEF'
    assert len(json_ld_calls) == 1
    assert json_ld_calls[0]['@type'] == 'TVEpisode'
    assert json_ld_calls[0]['@context'] == 'http://schema.org'
    assert info['id'] == VIDEO_ID
    # base dict title takes precedence over the breadcrumb-derived title
    assert info['title'] == 'Meta title'
    assert info['description'] == 'Synopsis text'
    # merge_dicts drops keys whose value is None, so with no Duration in the
    # playlist the result has no 'duration' key at all
    assert info.get('duration') is None
    assert info['subtitles'] == {}
    assert [f['url'] for f in info['formats']] == ['https://cdn.example.com/a.mp4']


def test_real_extract_json_ld_not_breadcrumb(monkeypatch):
    webpage = '''
    <html><head><meta property="og:title" content="Meta title"></head><body>
    <div id="video" data-video-id="https://example.com/playlist3" data-video-hmac="cafe"></div>
    <div class="episode-info__synopsis">Synopsis</div>
    <script type="application/ld+json">{"@type": "WebPage", "name": "Page"}</script>
    </body></html>
    '''
    playlist = {
        'Playlist': {
            'Video': {
                'MediaFiles': [{'Href': 'https://cdn.example.com/b.mp4'}],
            },
        },
    }

    def fail_json_ld(*args, **kwargs):
        raise AssertionError('_json_ld must not be called for non-BreadcrumbList JSON-LD')

    extractor = make_extractor()
    monkeypatch.setattr(extractor, '_download_webpage', lambda *a, **k: webpage)
    monkeypatch.setattr(extractor, '_download_json', lambda *a, **k: playlist)
    monkeypatch.setattr(extractor, '_search_json_ld', lambda *a, **k: {})
    monkeypatch.setattr(extractor, '_json_ld', fail_json_ld)
    monkeypatch.setattr(extractor, '_html_search_meta', lambda *a, **k: 'Meta title')

    info = extractor._real_extract(URL)

    assert info['id'] == VIDEO_ID
    assert info['title'] == 'Meta title'
    assert info['description'] == 'Synopsis'
    assert [f['url'] for f in info['formats']] == ['https://cdn.example.com/b.mp4']


def test_real_extract_no_json_ld_at_all(monkeypatch):
    webpage = '''
    <html><head><meta property="og:title" content="Meta title"></head><body>
    <div id="video" data-video-id="https://example.com/playlist4" data-video-hmac="beef"></div>
    <div class="episode-info__synopsis">Synopsis</div>
    </body></html>
    '''
    playlist = {
        'Playlist': {
            'Video': {
                'MediaFiles': [{'Href': 'https://cdn.example.com/c.mp4'}],
            },
        },
    }

    def fail_json_ld(*args, **kwargs):
        raise AssertionError('_json_ld must not be called when no JSON-LD is present')

    extractor = make_extractor()
    monkeypatch.setattr(extractor, '_download_webpage', lambda *a, **k: webpage)
    monkeypatch.setattr(extractor, '_download_json', lambda *a, **k: playlist)
    monkeypatch.setattr(extractor, '_search_json_ld', lambda *a, **k: {})
    monkeypatch.setattr(extractor, '_json_ld', fail_json_ld)
    monkeypatch.setattr(extractor, '_html_search_meta', lambda *a, **k: 'Meta title')

    info = extractor._real_extract(URL)

    assert info['id'] == VIDEO_ID
    assert info['title'] == 'Meta title'
    assert 'series' not in info
    assert [f['url'] for f in info['formats']] == ['https://cdn.example.com/c.mp4']
