# file: project/youtube_dl/extractor/fourtube.py:43-114
# asked: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}
# gained: {"lines": [44, 45, 47, 48, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113], "branches": [[47, 48], [47, 50], [67, 68], [67, 72], [86, 87], [86, 99]]}

import pytest
from youtube_dl import YoutubeDL
from youtube_dl.extractor.fourtube import FourTubeBaseIE
from youtube_dl.utils import parse_iso8601, parse_duration


def _make_ie(monkeypatch=None):
    class DummyIE(FourTubeBaseIE):
        _VALID_URL = r'https?://example\.com/(?P<kind>[evm])/(?P<id>\d+)(?:/(?P<display_id>[^/]+))?'
        _URL_TEMPLATE = 'https://example.com/e/%s'
        _TKN_HOST = 'example.com'
        IE_NAME = 'dummy'
    ie = DummyIE()
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True, 'no_color': True})
    ie.set_downloader(ydl)
    return ie


def test_direct_with_categories_and_kind_m_rewrite(monkeypatch):
    ie = _make_ie()
    webpage = (
        '<html><head>'
        '<meta itemprop="name" content="Direct Title">'
        '<meta itemprop="uploadDate" content="2020-01-02T03:04:05+00:00">'
        '<meta itemprop="thumbnailUrl" content="https://example.com/thumb.jpg">'
        '<meta itemprop="interactionCount" content="UserPlays:12,345">'
        '<meta itemprop="interactionCount" content="UserLikes:678">'
        '<meta itemprop="duration" content="PT5M30S">'
        '</head><body>'
        '<a class="item-to-subscribe" href="https://example.com/channels/uploader123" title="Go to MyUploader page">sub</a>'
        '><i class="icon icon-tag"></i> Categories / Tags <div><ul class="foo list bar">'
        '<li><a href="/c1">Cat One</a></li>'
        '<li><a href="/c2"> Cat Two </a></li>'
        '</ul>'
        '<button data-id="12345" data-quality="360">360p</button>'
        '<button data-id="12345" data-quality="720">720p</button>'
        '</body></html>'
    )
    seen = {}

    def fake_download_webpage(url, video_id, *args, **kwargs):
        seen['url'] = url
        seen['video_id'] = video_id
        return webpage

    fake_formats = [{'url': 'https://example.com/v.mp4', 'format_id': '720p'}]

    def fake_extract_formats(url, video_id, media_id, sources):
        seen['ef_url'] = url
        seen['ef_video_id'] = video_id
        seen['ef_media_id'] = media_id
        seen['ef_sources'] = sources
        return fake_formats

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)

    url = 'https://example.com/m/12345/Some-Display'
    result = ie._real_extract(url)

    assert seen['url'] == 'https://example.com/e/12345'
    assert seen['video_id'] == '12345'
    assert seen['ef_media_id'] == '12345'
    assert seen['ef_sources'] == ['360', '720']
    assert seen['ef_url'] == 'https://example.com/e/12345'
    assert result['id'] == '12345'
    assert result['title'] == 'Direct Title'
    assert result['formats'] == fake_formats
    assert result['categories'] == ['Cat One', 'Cat Two']
    assert result['thumbnail'] == 'https://example.com/thumb.jpg'
    assert result['uploader'] == 'MyUploader'
    assert result['uploader_id'] == 'uploader123'
    assert result['timestamp'] == parse_iso8601('2020-01-02T03:04:05+00:00')
    assert result['view_count'] == 12345
    assert result['like_count'] == 678
    assert result['duration'] == parse_duration('PT5M30S') == 330
    assert result['age_limit'] == 18


def test_fallback_no_categories_no_rewrite(monkeypatch):
    ie = _make_ie()
    webpage = (
        '<html><head>'
        '<meta itemprop="name" content="Fallback Title">'
        '<meta itemprop="uploadDate" content="2021-06-07T08:09:10+00:00">'
        '<meta itemprop="thumbnailUrl" content="https://example.com/thumb2.jpg">'
        '<meta itemprop="interactionCount" content="UserPlays:1,000">'
        '<meta itemprop="interactionCount" content="UserLikes:50">'
        '<meta itemprop="duration" content="PT1M10S">'
        '</head><body>'
        '<a class="item-to-subscribe" href="https://example.com/users/fallbackUser" title="Go to FallbackUploader page">sub</a>'
        '<script id="playerembed" src="https://example.com/player.js"></script>'
        '</body></html>'
    )
    player_js = 'blah $.ajax(url, opts);} })(99999, 0, [360, 720]) blah'
    seen = {}
    calls = []

    def fake_download_webpage(url, video_id, *args, **kwargs):
        calls.append((url, video_id))
        if 'player.js' in url:
            return player_js
        seen['page_url'] = url
        return webpage

    def fake_extract_formats(url, video_id, media_id, sources):
        seen['ef_media_id'] = media_id
        seen['ef_sources'] = sources
        seen['ef_url'] = url
        return [{'url': 'https://example.com/f.mp4', 'format_id': '720p'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)

    url = 'https://example.com/e/67890/Some-Display'
    result = ie._real_extract(url)

    assert seen['page_url'] == url
    assert len(calls) == 2
    assert 'player.js' in calls[1][0]
    assert seen['ef_media_id'] == 99999
    assert seen['ef_sources'] == ['360', '720']
    assert result['id'] == '67890'
    assert result['title'] == 'Fallback Title'
    assert result['categories'] is None
    assert result['thumbnail'] == 'https://example.com/thumb2.jpg'
    assert result['uploader'] == 'FallbackUploader'
    assert result['uploader_id'] == 'fallbackUser'
    assert result['timestamp'] == parse_iso8601('2021-06-07T08:09:10+00:00')
    assert result['view_count'] == 1000
    assert result['like_count'] == 50
    assert result['duration'] == 70
    assert result['age_limit'] == 18


def test_direct_missing_display_id_rewrite(monkeypatch):
    ie = _make_ie()
    webpage = (
        '<html><head>'
        '<meta itemprop="name" content="NoDisplay Title">'
        '<meta itemprop="uploadDate" content="2019-03-04T05:06:07+00:00">'
        '<meta itemprop="thumbnailUrl" content="https://example.com/thumb3.jpg">'
        '<meta itemprop="interactionCount" content="UserPlays:2,500">'
        '<meta itemprop="interactionCount" content="UserLikes:25">'
        '<meta itemprop="duration" content="PT2M00S">'
        '</head><body>'
        '<a class="item-to-subscribe" href="https://example.com/channel/chan999" title="Go to ChanUploader page">sub</a>'
        '><i class="icon icon-tag"></i> Categories / Tags <div><ul class="x list y">'
        '<li><a href="/c9">Solo</a></li>'
        '</ul>'
        '<button data-id="55555" data-quality="480">480p</button>'
        '</body></html>'
    )
    seen = {}

    def fake_download_webpage(url, video_id, *args, **kwargs):
        seen['url'] = url
        return webpage

    def fake_extract_formats(url, video_id, media_id, sources):
        seen['ef_media_id'] = media_id
        seen['ef_sources'] = sources
        return [{'url': 'https://example.com/g.mp4', 'format_id': '480p'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)

    url = 'https://example.com/e/55555'
    result = ie._real_extract(url)

    assert seen['url'] == 'https://example.com/e/55555'
    assert seen['ef_media_id'] == '55555'
    assert seen['ef_sources'] == ['480']
    assert result['id'] == '55555'
    assert result['title'] == 'NoDisplay Title'
    assert result['categories'] == ['Solo']
    assert result['uploader_id'] == 'chan999'
    assert result['uploader'] == 'ChanUploader'
    assert result['view_count'] == 2500
    assert result['like_count'] == 25
    assert result['duration'] == 120
    assert result['age_limit'] == 18
