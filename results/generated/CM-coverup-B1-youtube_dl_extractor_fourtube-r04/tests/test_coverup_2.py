# file: project/youtube_dl/extractor/fourtube.py:230-277
# asked: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}
# gained: {"lines": [231, 232, 234, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276], "branches": []}

import base64
import json
from urllib.parse import quote

from youtube_dl import YoutubeDL
from youtube_dl.extractor.fourtube import PornTubeIE
from youtube_dl.utils import unified_timestamp


def _build_webpage(video):
    payload = {"page": {"video": video}}
    json_str = json.dumps(payload)
    quoted = quote(json_str, safe='')
    b64 = base64.b64encode(quoted.encode('utf-8')).decode('ascii')
    return '<html><script>INITIALSTATE="%s"</script></html>' % b64


def _make_ie():
    ie = PornTubeIE()
    ie.set_downloader(YoutubeDL({'quiet': True, 'no_warnings': True, 'no_color': True}))
    return ie


def test_porntube_full_extraction(monkeypatch):
    ie = _make_ie()
    url = 'https://www.porntube.com/videos/teen-couple-doing-anal_7089759'
    video = {
        'title': 'Teen couple doing anal',
        'mediaId': 'media123',
        'encodings': [{'height': 360}, {'height': 720}, {'height': None}, {}],
        'masterThumb': 'https://example.com/thumb.jpg',
        'user': {'username': 'Alexy', 'id': 91488},
        'channel': {'name': 'Exploited College Girls', 'id': 665},
        'likes': 100,
        'dislikes': 5,
        'playsQty': 1234,
        'durationInSeconds': 5052,
        'publishedAt': '2015-06-06T12:00:47',
    }
    webpage = _build_webpage(video)
    captured = {}

    def fake_download(url_, display_id_, *args, **kwargs):
        assert url_ == url
        assert display_id_ == 'teen-couple-doing-anal'
        return webpage

    def fake_formats(url_, video_id_, media_id_, sources_):
        captured['url'] = url_
        captured['video_id'] = video_id_
        captured['media_id'] = media_id_
        captured['sources'] = list(sources_)
        return [{'url': 'https://example.com/media123.mp4', 'format_id': '720p'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    monkeypatch.setattr(ie, '_extract_formats', fake_formats)

    result = ie._real_extract(url)

    assert captured['video_id'] == '7089759'
    assert captured['media_id'] == 'media123'
    assert captured['sources'] == ['360', '720']
    assert result['id'] == '7089759'
    assert result['title'] == 'Teen couple doing anal'
    assert result['formats'] == [{'url': 'https://example.com/media123.mp4', 'format_id': '720p'}]
    assert result['thumbnail'] == 'https://example.com/thumb.jpg'
    assert result['uploader'] == 'Alexy'
    assert result['uploader_id'] == '91488'
    assert result['channel'] == 'Exploited College Girls'
    assert result['channel_id'] == '665'
    assert result['like_count'] == 100
    assert result['dislike_count'] == 5
    assert result['view_count'] == 1234
    assert result['duration'] == 5052
    assert result['timestamp'] == unified_timestamp('2015-06-06T12:00:47')
    assert result['age_limit'] == 18


def test_porntube_fallback_to_channel(monkeypatch):
    ie = _make_ie()
    url = 'https://www.porntube.com/videos/squirting-teen-ballerina-ecg_1331406'
    video = {
        'title': 'Squirting Teen Ballerina on ECG',
        'mediaId': 9999,
        'encodings': [{'height': 480}, {'noheight': True}],
        'masterThumb': 'https://example.com/thumb2.jpg',
        'channel': {'name': 'Exploited College Girls', 'id': 665},
        'likes': '42',
        'dislikes': '3',
        'playsQty': '777',
        'durationInSeconds': '851',
        'publishedAt': '2013-09-20T00:00:00',
    }
    webpage = _build_webpage(video)
    captured = {}

    def fake_download(url_, display_id_, *args, **kwargs):
        assert display_id_ == 'squirting-teen-ballerina-ecg'
        return webpage

    def fake_formats(url_, video_id_, media_id_, sources_):
        captured['sources'] = list(sources_)
        captured['media_id'] = media_id_
        return [{'url': 'https://example.com/9999.mp4'}]

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    monkeypatch.setattr(ie, '_extract_formats', fake_formats)

    result = ie._real_extract(url)

    assert captured['sources'] == ['480']
    assert result['id'] == '1331406'
    assert result['title'] == 'Squirting Teen Ballerina on ECG'
    assert result['uploader'] == 'Exploited College Girls'
    assert result['uploader_id'] == '665'
    assert result['channel'] == 'Exploited College Girls'
    assert result['channel_id'] == '665'
    assert result['like_count'] == 42
    assert result['dislike_count'] == 3
    assert result['view_count'] == 777
    assert result['duration'] == 851
    assert result['timestamp'] == unified_timestamp('2013-09-20T00:00:00')
    assert result['age_limit'] == 18


def test_porntube_embed_minimal_no_user_channel(monkeypatch):
    ie = _make_ie()
    url = 'https://www.porntube.com/embed/7089759'
    video = {
        'title': 'Minimal Title',
        'mediaId': 'm1',
        'encodings': [],
    }
    webpage = _build_webpage(video)

    def fake_download(url_, display_id_, *args, **kwargs):
        assert url_ == url
        assert display_id_ is None
        return webpage

    def fake_formats(url_, video_id_, media_id_, sources_):
        assert sources_ == []
        assert video_id_ == '7089759'
        assert media_id_ == 'm1'
        return []

    monkeypatch.setattr(ie, '_download_webpage', fake_download)
    monkeypatch.setattr(ie, '_extract_formats', fake_formats)

    result = ie._real_extract(url)

    assert result['id'] == '7089759'
    assert result['title'] == 'Minimal Title'
    assert result['formats'] == []
    assert result['thumbnail'] is None
    assert result['uploader'] is None
    assert result['uploader_id'] is None
    assert result['channel'] is None
    assert result['channel_id'] is None
    assert result['timestamp'] is None
    assert result['like_count'] is None
    assert result['dislike_count'] is None
    assert result['view_count'] is None
    assert result['duration'] is None
    assert result['age_limit'] == 18
