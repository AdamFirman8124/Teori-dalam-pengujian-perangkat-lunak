# file: project/youtube_dl/extractor/tvplay.py:455-492
# asked: {"lines": [456, 458, 459, 461, 462, 463, 464, 466, 467, 468, 470, 471, 472, 473, 474, 475, 478, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491], "branches": [[472, 473], [472, 478]]}
# gained: {"lines": [456, 458, 459, 461, 462, 463, 464, 466, 467, 468, 470, 471, 472, 473, 474, 475, 478, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491], "branches": [[472, 473], [472, 478]]}

import pytest

from youtube_dl.extractor.tvplay import TVPlayHomeIE

URL = 'https://tvplay.tv3.lt/serialas/some-show-12345'


class FakeDownloader(object):
    def __init__(self):
        self.params = {}


def make_asset(**overrides):
    asset = {
        'assetId': '98765',
        'title': {
            'title': 'My Show',
            'summaryLong': 'long summary',
            'summaryShort': 'short summary',
            'runTime': '1:02:03',
            'titleBrief': 'Episode Brief',
        },
        'movie': {'contentUrl': 'https://cdn.example.com/video.m3u8'},
        'imageUrl': '/images/thumb.jpg',
        'tvSeriesTitle': 'Series Name',
        'tvSeasonTitle': 'Season Name',
        'metadata': {'seasonNumber': '2', 'episodeNumber': '5'},
    }
    asset.update(overrides)
    return asset


@pytest.fixture
def ie():
    return TVPlayHomeIE(FakeDownloader())


def test_real_extract_full_metadata(ie, monkeypatch):
    asset = make_asset()
    captured = {}

    def fake_download_json(url, video_id, *args, **kwargs):
        captured['url'] = url
        captured['video_id'] = video_id
        return asset

    def fake_extract_m3u8(m3u8_url, video_id, *args, **kwargs):
        captured['m3u8_url'] = m3u8_url
        captured['m3u8_video_id'] = video_id
        return [{'url': m3u8_url, 'ext': 'mp4'}]

    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract_m3u8)

    result = ie._real_extract(URL)

    assert captured['url'] == 'https://tvplay.tv3.lt/sb/public/asset/12345'
    assert captured['video_id'] == '12345'
    assert captured['m3u8_url'] == 'https://cdn.example.com/video.m3u8'
    assert captured['m3u8_video_id'] == '98765'

    assert result['id'] == '98765'
    assert result['title'] == 'My Show'
    assert result['description'] == 'long summary'
    assert result['thumbnails'] == [{
        'url': 'https://tvplay.tv3.lt/images/thumb.jpg',
        'ext': 'jpg',
    }]
    assert result['duration'] == 3723
    assert result['series'] == 'Series Name'
    assert result['season'] == 'Season Name'
    assert result['season_number'] == 2
    assert result['episode'] == 'Episode Brief'
    assert result['episode_number'] == 5
    assert result['formats'] == [{'url': 'https://cdn.example.com/video.m3u8', 'ext': 'mp4'}]


def test_real_extract_minimal_metadata(ie, monkeypatch):
    asset = make_asset(
        imageUrl=None,
        metadata=None,
        tvSeriesTitle=None,
        tvSeasonTitle=None,
        title={
            'title': 'My Show',
            'summaryShort': 'short summary',
        },
    )

    monkeypatch.setattr(
        ie, '_download_json', lambda url, video_id, *a, **kw: asset)
    monkeypatch.setattr(
        ie, '_extract_m3u8_formats',
        lambda m3u8_url, video_id, *a, **kw: [{'url': m3u8_url, 'ext': 'mp4'}])

    result = ie._real_extract(URL)

    assert result['id'] == '98765'
    assert result['title'] == 'My Show'
    assert result['description'] == 'short summary'
    assert result['thumbnails'] is None
    assert result['duration'] is None
    assert result['series'] is None
    assert result['season'] is None
    assert result['season_number'] is None
    assert result['episode'] is None
    assert result['episode_number'] is None
    assert result['formats'] == [{'url': 'https://cdn.example.com/video.m3u8', 'ext': 'mp4'}]
