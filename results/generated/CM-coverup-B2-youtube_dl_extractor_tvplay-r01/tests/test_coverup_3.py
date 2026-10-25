# file: project/youtube_dl/extractor/tvplay.py:455-492
# asked: {"lines": [456, 458, 459, 461, 462, 463, 464, 466, 467, 468, 470, 471, 472, 473, 474, 475, 478, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491], "branches": [[472, 473], [472, 478]]}
# gained: {"lines": [456, 458, 459, 461, 462, 463, 464, 466, 467, 468, 470, 471, 472, 473, 474, 475, 478, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491], "branches": [[472, 473], [472, 478]]}

import pytest

from youtube_dl.extractor.tvplay import TVPlayHomeIE

URL = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
MATCHED_ID = '10047125'


def _build_ie(monkeypatch, asset, formats=None):
    """Create a TVPlayHomeIE with network/format helpers stubbed out."""
    ie = TVPlayHomeIE()
    calls = {}

    def fake_download_json(url_or_request, video_id, *args, **kwargs):
        calls['json_url'] = url_or_request
        calls['json_video_id'] = video_id
        return asset

    def fake_extract_m3u8_formats(m3u8_url, video_id, *args, **kwargs):
        calls['m3u8_url'] = m3u8_url
        calls['m3u8_video_id'] = video_id
        calls['m3u8_args'] = args
        calls['m3u8_kwargs'] = kwargs
        if formats is not None:
            return formats
        return [{'url': 'http://example.com/master.m3u8', 'format_id': 'hls-1'}]

    def fake_sort_formats(fmts):
        calls['sorted_formats'] = fmts

    monkeypatch.setattr(ie, '_download_json', fake_download_json)
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_extract_m3u8_formats)
    monkeypatch.setattr(ie, '_sort_formats', fake_sort_formats)
    return ie, calls


def test_tvplayhome_full_metadata(monkeypatch):
    asset = {
        'assetId': '366367',
        'movie': {'contentUrl': 'http://cdn.example.com/asset/366367/master.m3u8'},
        'title': {
            'title': 'Aferistai',
            'summaryLong': 'Aferistai. Kalėdinė pasaka.',
            'summaryShort': 'short summary',
            'runTime': '00:07:44',
            'titleBrief': 'Aferistai 1 serija',
        },
        'imageUrl': '/images/366367.jpg',
        'tvSeriesTitle': 'Aferistai [N-7]',
        'tvSeasonTitle': '1 sezonas',
        'metadata': {'seasonNumber': '1', 'episodeNumber': '7'},
    }
    formats = [
        {'url': 'http://example.com/low.m3u8', 'format_id': 'hls-1'},
        {'url': 'http://example.com/high.m3u8', 'format_id': 'hls-2'},
    ]
    ie, calls = _build_ie(monkeypatch, asset, formats)

    info = ie._real_extract(URL)

    # JSON was fetched from the expected asset endpoint, keyed by the matched id
    assert calls['json_url'] == 'https://tvplay.tv3.lt/sb/public/asset/' + MATCHED_ID
    assert calls['json_video_id'] == MATCHED_ID

    # m3u8 extraction used the asset contentUrl and the *asset* id
    assert calls['m3u8_url'] == 'http://cdn.example.com/asset/366367/master.m3u8'
    assert calls['m3u8_video_id'] == '366367'
    assert calls['m3u8_args'] == ('mp4', 'm3u8_native')
    assert calls['m3u8_kwargs'] == {'m3u8_id': 'hls'}

    # formats were sorted and returned as-is
    assert calls['sorted_formats'] is formats
    assert info['formats'] is formats

    assert info['id'] == '366367'
    assert info['title'] == 'Aferistai'
    assert info['description'] == 'Aferistai. Kalėdinė pasaka.'
    assert info['thumbnails'] == [{
        'url': 'https://tvplay.tv3.lt/images/366367.jpg',
        'ext': 'jpg',
    }]
    assert info['duration'] == 464
    assert info['series'] == 'Aferistai [N-7]'
    assert info['season'] == '1 sezonas'
    assert info['season_number'] == 1
    assert info['episode'] == 'Aferistai 1 serija'
    assert info['episode_number'] == 7


def test_tvplayhome_minimal_asset(monkeypatch):
    asset = {
        'assetId': '10280317',
        'movie': {'contentUrl': 'http://cdn.example.com/asset/10280317/master.m3u8'},
        'title': {
            'title': 'Vinas melo labak',
            'summaryShort': 'short only',
        },
    }
    ie, calls = _build_ie(monkeypatch, asset)

    info = ie._real_extract(URL)

    assert calls['json_url'] == 'https://tvplay.tv3.lt/sb/public/asset/' + MATCHED_ID
    assert calls['m3u8_video_id'] == '10280317'
    assert calls['sorted_formats'] == [{'url': 'http://example.com/master.m3u8', 'format_id': 'hls-1'}]

    assert info['id'] == '10280317'
    assert info['title'] == 'Vinas melo labak'
    # summaryLong missing -> falls back to summaryShort
    assert info['description'] == 'short only'
    # no imageUrl -> thumbnails stays None
    assert info['thumbnails'] is None
    # no runTime / series / season / metadata
    assert info['duration'] is None
    assert info['series'] is None
    assert info['season'] is None
    assert info['season_number'] is None
    assert info['episode'] is None
    assert info['episode_number'] is None
    assert info['formats'] == [{'url': 'http://example.com/master.m3u8', 'format_id': 'hls-1'}]


def test_tvplayhome_empty_metadata_and_no_summaries(monkeypatch):
    asset = {
        'assetId': '10044354',
        'movie': {'contentUrl': 'http://cdn.example.com/asset/10044354/master.m3u8'},
        'title': {'title': 'Cool D ga mehhikosse'},
        'metadata': {},
    }
    ie, calls = _build_ie(monkeypatch, asset)

    info = ie._real_extract(URL)

    assert info['id'] == '10044354'
    assert info['description'] is None
    assert info['thumbnails'] is None
    assert info['season_number'] is None
    assert info['episode_number'] is None
    assert calls['m3u8_url'] == 'http://cdn.example.com/asset/10044354/master.m3u8'
