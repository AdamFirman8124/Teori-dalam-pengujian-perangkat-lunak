# file: project/youtube_dl/extractor/tvplay.py:455-492
# asked: {"lines": [456, 458, 459, 461, 462, 463, 464, 466, 467, 468, 470, 471, 472, 473, 474, 475, 478, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491], "branches": [[472, 473], [472, 478]]}
# gained: {"lines": [456, 458, 459, 461, 462, 463, 464, 466, 467, 468, 470, 471, 472, 473, 474, 475, 478, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491], "branches": [[472, 473], [472, 478]]}

import pytest
from types import SimpleNamespace
from youtube_dl.extractor.tvplay import TVPlayHomeIE
from youtube_dl.utils import int_or_none, parse_duration, urljoin


def _make_ie(monkeypatch, fake_asset, fake_formats, captured):
    def fake_download_json(json_url, video_id, **kwargs):
        captured['json_url'] = json_url
        captured['json_video_id'] = video_id
        return fake_asset

    def fake_extract_m3u8(m3u8_url, video_id, ext=None, entry_protocol=None, m3u8_id=None, **kwargs):
        captured['m3u8_url'] = m3u8_url
        captured['m3u8_video_id'] = video_id
        captured['ext'] = ext
        captured['entry_protocol'] = entry_protocol
        captured['m3u8_id'] = m3u8_id
        return [dict(f) for f in fake_formats]

    ie = TVPlayHomeIE()
    ie._downloader = SimpleNamespace(params={})
    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract_m3u8)
    return ie


def test_tvplayhome_full_with_thumbnail_and_long_summary(monkeypatch):
    url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    matched_id = '10047125'
    fake_asset = {
        'assetId': '366367',
        'movie': {'contentUrl': 'https://example.com/video.m3u8'},
        'title': {
            'title': 'Aferistai',
            'summaryLong': 'Long description',
            'summaryShort': 'Short description',
            'runTime': '00:07:44',
            'titleBrief': 'Brief title',
        },
        'imageUrl': '/images/thumb.jpg',
        'metadata': {'seasonNumber': '1', 'episodeNumber': '5'},
        'tvSeriesTitle': 'Aferistai [N-7]',
        'tvSeasonTitle': '1 sezonas',
    }
    fake_formats = [
        {'url': 'https://example.com/low.mp4', 'format_id': 'hls-low', 'ext': 'mp4', 'tbr': 500},
        {'url': 'https://example.com/high.mp4', 'format_id': 'hls-high', 'ext': 'mp4', 'tbr': 1500},
    ]
    captured = {}
    ie = _make_ie(monkeypatch, fake_asset, fake_formats, captured)

    result = ie._real_extract(url)

    assert captured['json_video_id'] == matched_id
    assert captured['json_url'] == urljoin(url, '/sb/public/asset/' + matched_id)
    assert captured['m3u8_url'] == 'https://example.com/video.m3u8'
    assert captured['m3u8_video_id'] == '366367'
    assert captured['ext'] == 'mp4'
    assert captured['entry_protocol'] == 'm3u8_native'
    assert captured['m3u8_id'] == 'hls'
    assert result['id'] == '366367'
    assert result['title'] == 'Aferistai'
    assert result['description'] == 'Long description'
    assert result['thumbnails'] == [{'url': urljoin(url, '/images/thumb.jpg'), 'ext': 'jpg'}]
    assert result['duration'] == parse_duration('00:07:44') == 464
    assert result['series'] == 'Aferistai [N-7]'
    assert result['season'] == '1 sezonas'
    assert result['season_number'] == 1
    assert result['episode'] == 'Brief title'
    assert result['episode_number'] == 5
    assert isinstance(result['formats'], list)
    assert len(result['formats']) == 2
    assert all('url' in f for f in result['formats'])


def test_tvplayhome_minimal_no_thumbnail_short_summary_fallback(monkeypatch):
    url = 'https://tvplay.tv3.lt/aferistai-10047125'
    matched_id = '10047125'
    fake_asset = {
        'assetId': '999999',
        'movie': {'contentUrl': 'https://example.com/other.m3u8'},
        'title': {
            'title': 'Other Title',
            'summaryShort': 'Only short summary',
            'titleBrief': 'Brief2',
        },
    }
    fake_formats = [
        {'url': 'https://example.com/v.mp4', 'format_id': 'hls', 'ext': 'mp4'},
    ]
    captured = {}
    ie = _make_ie(monkeypatch, fake_asset, fake_formats, captured)

    result = ie._real_extract(url)

    assert captured['json_video_id'] == matched_id
    assert captured['json_url'] == urljoin(url, '/sb/public/asset/' + matched_id)
    assert captured['m3u8_url'] == 'https://example.com/other.m3u8'
    assert captured['m3u8_video_id'] == '999999'
    assert result['id'] == '999999'
    assert result['title'] == 'Other Title'
    assert result['description'] == 'Only short summary'
    assert result['thumbnails'] is None
    assert result['duration'] is None
    assert result['series'] is None
    assert result['season'] is None
    assert result['season_number'] is None
    assert result['episode'] == 'Brief2'
    assert result['episode_number'] is None
    assert len(result['formats']) == 1
    assert result['formats'][0]['url'] == 'https://example.com/v.mp4'


def test_tvplayhome_none_metadata_empty_image_no_description(monkeypatch):
    url = 'https://play.tv3.lt/aferistai-10047125'
    matched_id = '10047125'
    fake_asset = {
        'assetId': '123456',
        'movie': {'contentUrl': 'https://example.com/x.m3u8'},
        'title': {
            'title': 'X',
        },
        'imageUrl': '',
        'metadata': None,
        'tvSeriesTitle': 'SeriesX',
        'tvSeasonTitle': 'SeasonX',
    }
    fake_formats = [
        {'url': 'https://example.com/x.mp4', 'format_id': 'hls', 'ext': 'mp4'},
    ]
    captured = {}
    ie = _make_ie(monkeypatch, fake_asset, fake_formats, captured)

    result = ie._real_extract(url)

    assert captured['json_video_id'] == matched_id
    assert captured['json_url'] == urljoin(url, '/sb/public/asset/' + matched_id)
    assert captured['m3u8_url'] == 'https://example.com/x.m3u8'
    assert result['id'] == '123456'
    assert result['title'] == 'X'
    assert result['description'] is None
    assert result['thumbnails'] is None
    assert result['duration'] is None
    assert result['series'] == 'SeriesX'
    assert result['season'] == 'SeasonX'
    assert result['season_number'] is None
    assert result['episode'] is None
    assert result['episode_number'] is None
    assert len(result['formats']) == 1
    assert result['formats'][0]['url'] == 'https://example.com/x.mp4'
    assert int_or_none(None) is None
