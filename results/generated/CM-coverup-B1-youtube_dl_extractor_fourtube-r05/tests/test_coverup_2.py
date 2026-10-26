# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from urllib.parse import quote

from youtube_dl.extractor.fourtube import PornTubeIE


class FakeDownloader(object):
    """Minimal stand-in for YoutubeDL: only 'params' is accessed by the IE."""

    def __init__(self):
        self.params = {}


def _make_initial_state(video):
    """Encode a video dict the way porntube.com embeds it in INITIALSTATE."""
    quoted = quote(json.dumps({'page': {'video': video}}))
    return base64.b64encode(quoted.encode('utf-8')).decode('ascii')


FULL_VIDEO = {
    'title': 'Teen couple doing anal',
    'mediaId': '12345',
    'encodings': [{'height': 720}, {'height': 1080}, {'other': 1}],
    'masterThumb': 'https://www.porntube.com/thumb.jpg',
    'user': {'username': 'Alexy', 'id': 91488},
    'channel': {'name': 'Some Channel', 'id': 7},
    'likes': 10,
    'dislikes': 2,
    'playsQty': 1000,
    'durationInSeconds': 5052,
    'publishedAt': '2015-06-06T13:00:47+00:00',
}

FAKE_FORMATS = [{'url': 'https://tkn.porntube.com/fake', 'format_id': '720p'}]


def _patch_ie(ie, monkeypatch, video, webpage_template='INITIALSTATE="%s";'):
    webpage = webpage_template % _make_initial_state(video)
    calls = {}

    def fake_download_webpage(url, video_id):
        calls['download_url'] = url
        calls['download_id'] = video_id
        return webpage

    def fake_extract_formats(url, video_id, media_id, sources):
        calls['extract_url'] = url
        calls['extract_id'] = video_id
        calls['media_id'] = media_id
        calls['sources'] = sources
        return list(FAKE_FORMATS)

    monkeypatch.setattr(ie, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(ie, '_extract_formats', fake_extract_formats)
    return calls


def test_porn_tube_real_extract_full(monkeypatch):
    ie = PornTubeIE()
    ie.set_downloader(FakeDownloader())
    calls = _patch_ie(ie, monkeypatch, FULL_VIDEO)

    url = 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    result = ie._real_extract(url)

    # _download_webpage receives (url, display_id); _extract_formats receives video_id
    assert calls['download_url'] == url
    assert calls['download_id'] == 'teen-couple-doing-anal'
    assert calls['extract_url'] == url
    assert calls['extract_id'] == '7089759'
    assert calls['media_id'] == '12345'
    assert calls['sources'] == ['720', '1080']

    # Postconditions on the returned info dict
    assert result['id'] == '7089759'
    assert result['title'] == 'Teen couple doing anal'
    assert result['formats'] == FAKE_FORMATS
    assert result['thumbnail'] == 'https://www.porntube.com/thumb.jpg'
    assert result['uploader'] == 'Alexy'
    assert result['uploader_id'] == '91488'
    assert result['channel'] == 'Some Channel'
    assert result['channel_id'] == '7'
    assert result['timestamp'] == 1433595647
    assert result['like_count'] == 10
    assert result['dislike_count'] == 2
    assert result['view_count'] == 1000
    assert result['duration'] == 5052
    assert result['age_limit'] == 18


def test_porn_tube_real_extract_embed_and_fallbacks(monkeypatch):
    # No 'user' key, no thumbnail, no counters: exercises the
    # uploader/channel fallback and the "missing optional field" branches.
    # Also uses single quotes around INITIALSTATE to cover the other quote branch.
    minimal_video = {
        'title': 'Embed video',
        'mediaId': '999',
        'encodings': [{'height': 360}],
        'channel': {'name': 'Exploited College Girls', 'id': 665},
    }
    ie = PornTubeIE()
    ie.set_downloader(FakeDownloader())
    calls = _patch_ie(ie, monkeypatch, minimal_video, webpage_template="INITIALSTATE='%s';")

    url = 'https://www.porntube.com/embed/7089759'
    result = ie._real_extract(url)

    # display_id is None for embed URLs
    assert calls['download_url'] == url
    assert calls['download_id'] is None
    assert calls['extract_id'] == '7089759'
    assert calls['media_id'] == '999'
    assert calls['sources'] == ['360']

    assert result['id'] == '7089759'
    assert result['title'] == 'Embed video'
    assert result['formats'] == FAKE_FORMATS
    assert result['thumbnail'] is None
    # uploader falls back to channel when 'user' is absent
    assert result['uploader'] == 'Exploited College Girls'
    assert result['uploader_id'] == '665'
    assert result['channel'] == 'Exploited College Girls'
    assert result['channel_id'] == '665'
    assert result['timestamp'] is None
    assert result['like_count'] is None
    assert result['dislike_count'] is None
    assert result['view_count'] is None
    assert result['duration'] is None
    assert result['age_limit'] == 18
