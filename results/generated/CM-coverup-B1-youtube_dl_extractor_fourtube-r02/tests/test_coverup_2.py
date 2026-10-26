# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from urllib.parse import quote

from youtube_dl import YoutubeDL
from youtube_dl.extractor.fourtube import PornTubeIE
from youtube_dl.utils import unified_timestamp


def _make_webpage(video):
    payload = json.dumps({'page': {'video': video}})
    # extractor does: unquote(b64decode(x).decode('utf-8'))
    # so page must contain b64(quote(json))
    quoted = quote(payload, safe='')
    b64 = base64.b64encode(quoted.encode('utf-8')).decode('ascii')
    return '<html><script>INITIALSTATE = "%s";</script></html>' % b64


def _make_ie():
    ydl = YoutubeDL({'quiet': True, 'no_warnings': True, 'no_color': True})
    return PornTubeIE(ydl)


def _install_mocks(monkeypatch, webpage, formats_result, calls):
    def fake_download_webpage(self, url, video_id, *args, **kwargs):
        calls['webpage_url'] = url
        calls['display_id'] = video_id
        return webpage

    def fake_extract_formats(self, url, video_id, media_id, sources):
        calls['formats_args'] = (url, video_id, media_id, list(sources))
        return formats_result

    monkeypatch.setattr(PornTubeIE, '_download_webpage', fake_download_webpage)
    monkeypatch.setattr(PornTubeIE, '_extract_formats', fake_extract_formats)


def test_porn_tube_real_extract_full(monkeypatch):
    video = {
        'title': 'Test video',
        'mediaId': 12345,
        'encodings': [{'height': 720}, {'height': 1080}, {'other': 1}],
        'masterThumb': 'https://img.porntube.com/thumb.jpg',
        'user': {'username': 'someuser', 'id': 42},
        'channel': {'name': 'Some Channel', 'id': 7},
        'likes': 10,
        'dislikes': 2,
        'playsQty': 1000,
        'durationInSeconds': 300,
        'publishedAt': '2015-06-06T12:00:00+00:00',
    }
    formats_result = [{'ext': 'mp4', 'height': 720}, {'ext': 'mp4', 'height': 1080}]
    calls = {}
    _install_mocks(monkeypatch, _make_webpage(video), formats_result, calls)

    ie = _make_ie()
    url = 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    info = ie._real_extract(url)

    assert calls['webpage_url'] == url
    assert calls['display_id'] == 'teen-couple-doing-anal'
    assert calls['formats_args'] == (url, '7089759', 12345, ['720', '1080'])
    assert info['id'] == '7089759'
    assert info['title'] == 'Test video'
    assert info['formats'] == formats_result
    assert info['thumbnail'] == 'https://img.porntube.com/thumb.jpg'
    assert info['uploader'] == 'someuser'
    assert info['uploader_id'] == '42'
    assert info['channel'] == 'Some Channel'
    assert info['channel_id'] == '7'
    assert info['like_count'] == 10
    assert info['dislike_count'] == 2
    assert info['view_count'] == 1000
    assert info['duration'] == 300
    assert info['timestamp'] == unified_timestamp(video['publishedAt'])
    assert info['timestamp'] is not None
    assert info['age_limit'] == 18


def test_porn_tube_real_extract_fallbacks_and_missing_fields(monkeypatch):
    video = {
        'title': 'Fallback video',
        'mediaId': 999,
        'encodings': [{'height': 360}],
        'masterThumb': 'not a url',
        'publishedAt': 'garbage-timestamp',
    }
    formats_result = [{'ext': 'mp4', 'height': 360}]
    calls = {}
    _install_mocks(monkeypatch, _make_webpage(video), formats_result, calls)

    ie = _make_ie()
    url = 'https://www.porntube.com/videos/fallback-video_111'
    info = ie._real_extract(url)

    assert calls['formats_args'][1] == '111'
    assert calls['formats_args'][2] == 999
    assert calls['formats_args'][3] == ['360']
    assert info['id'] == '111'
    assert info['title'] == 'Fallback video'
    assert info['formats'] == formats_result
    assert info['thumbnail'] is None
    assert info['uploader'] is None
    assert info['uploader_id'] is None
    assert info['channel'] is None
    assert info['channel_id'] is None
    assert info['timestamp'] is None
    assert info['like_count'] is None
    assert info['dislike_count'] is None
    assert info['view_count'] is None
    assert info['duration'] is None
    assert info['age_limit'] == 18


def test_porn_tube_real_extract_embed_url(monkeypatch):
    video = {
        'title': 'Embed video',
        'mediaId': 555,
        'encodings': [{'height': 480}],
    }
    formats_result = [{'ext': 'mp4', 'height': 480}]
    calls = {}
    _install_mocks(monkeypatch, _make_webpage(video), formats_result, calls)

    ie = _make_ie()
    url = 'https://www.porntube.com/embed/7089759'
    info = ie._real_extract(url)

    assert calls['display_id'] is None
    assert calls['formats_args'] == (url, '7089759', 555, ['480'])
    assert info['id'] == '7089759'
    assert info['title'] == 'Embed video'
    assert info['formats'] == formats_result
    assert info['age_limit'] == 18
