# file: project/youtube_dl/extractor/tvplay.py:236-335
# asked: {"lines": [237, 238, 239, 240, 241, 242, 243, 244, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276, 277, 278, 279, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 294, 295, 297, 299, 300, 301, 303, 306, 307, 308, 309, 310, 311, 312, 313, 316, 317, 318, 319, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334], "branches": [[241, 242], [241, 243], [253, 254], [253, 256], [260, 261], [260, 299], [262, 263], [262, 264], [265, 266], [265, 271], [271, 272], [271, 276], [281, 282], [281, 294], [284, 285], [284, 286], [299, 300], [299, 303], [308, 309], [308, 316]]}
# gained: {"lines": [237, 238, 239, 240, 241, 242, 243, 244, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 276, 277, 278, 279, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 294, 295, 297, 299, 300, 301, 303, 306, 307, 308, 309, 310, 311, 312, 313, 316, 317, 318, 319, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334], "branches": [[241, 242], [241, 243], [253, 254], [253, 256], [260, 261], [260, 299], [262, 263], [262, 264], [265, 266], [265, 271], [271, 272], [271, 276], [281, 282], [281, 294], [284, 285], [284, 286], [299, 300], [299, 303], [308, 309], [308, 316]]}

import io
import pytest
from youtube_dl import YoutubeDL
from youtube_dl.extractor.tvplay import TVPlayIE
from youtube_dl.utils import ExtractorError, GeoRestrictedError
from youtube_dl.compat import compat_HTTPError


def _make_ie():
    dl = YoutubeDL({'quiet': True, 'no_warnings': True})
    ie = TVPlayIE(dl)
    return ie


def _make_http_error(code, body_bytes):
    if isinstance(body_bytes, str):
        body_bytes = body_bytes.encode('utf-8')
    return compat_HTTPError(
        'http://example.com/', code, 'Forbidden', {}, io.BytesIO(body_bytes))


def _base_video(**over):
    v = {
        'title': 'Test Title',
        'description': 'Test desc',
        'format_title': 'Series X',
        'format_position': {'episode': '5', 'season': '2'},
        '_embedded': {'season': {'title': 'Season 2'}},
        'duration': 1257,
        'created_at': '2014-07-23T00:00:00.000Z',
        'views': {'total': 123},
        'age_limit': 0,
        'is_geo_blocked': False,
    }
    v.update(over)
    return v


def test_mixed_formats_lang_match_and_geo_bypass(monkeypatch):
    ie = _make_ie()
    url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    video = _base_video(sami_path='http://example.com/subs/file_en.xml')
    streams = {'streams': {
        'hls': 'http://example.com/video.m3u8',
        'hds': 'http://example.com/manifest.f4m',
        'medium': 'http://example.com/video.mp4',
        'high': 'rtmp://example.com/app/playpath123',
        'bad_rtmp': 'rtmp://onlyhost',
        'empty1': None,
        'empty2': '',
    }}

    geo_calls = []
    def fake_geo(ctx):
        geo_calls.append(ctx)
    monkeypatch.setattr(ie, '_initialize_geo_bypass', fake_geo)

    def fake_download_json(url_or_req, video_id, note=None, **kw):
        s = str(url_or_req)
        if '/stream/' in s:
            return streams
        return video
    monkeypatch.setattr(ie, '_download_json', fake_download_json)

    f4m_calls = []
    def fake_f4m(manifest_url, video_id, f4m_id=None, fatal=False, **kw):
        f4m_calls.append((manifest_url, f4m_id))
        assert 'hdcore=3.5.0' in manifest_url
        assert f4m_id == 'hds'
        return [{'url': 'http://example.com/hds1.flv', 'format_id': 'hds', 'ext': 'flv'}]
    monkeypatch.setattr(ie, '_extract_f4m_formats', fake_f4m)

    m3u8_calls = []
    def fake_m3u8(m3u8_url, video_id, ext=None, protocol=None, m3u8_id=None, fatal=False, **kw):
        m3u8_calls.append((m3u8_url, m3u8_id))
        assert m3u8_url == 'http://example.com/video.m3u8'
        return [{'url': 'http://example.com/hls1.mp4', 'format_id': 'hls', 'ext': 'mp4'}]
    monkeypatch.setattr(ie, '_extract_m3u8_formats', fake_m3u8)

    res = ie._real_extract(url)
    assert geo_calls == [{'countries': ['LV']}]
    assert len(f4m_calls) == 1
    assert len(m3u8_calls) == 1
    assert res['id'] == '418113'
    assert res['title'] == 'Test Title'
    assert res['description'] == 'Test desc'
    assert res['series'] == 'Series X'
    assert res['episode_number'] == 5
    assert res['season'] == 'Season 2'
    assert res['season_number'] == 2
    assert res['duration'] == 1257
    assert isinstance(res['timestamp'], int)
    assert res['view_count'] == 123
    assert res['subtitles'] == {'en': [{'url': 'http://example.com/subs/file_en.xml'}]}
    fmts = res['formats']
    assert len(fmts) == 4
    urls = [f.get('url') for f in fmts]
    assert 'http://example.com/hds1.flv' in urls
    assert 'http://example.com/hls1.mp4' in urls
    assert 'http://example.com/video.mp4' in urls
    rtmp_fmt = [f for f in fmts if f.get('play_path') == 'playpath123'][0]
    assert rtmp_fmt['url'] == 'rtmp://example.com/app'
    assert rtmp_fmt['app'] == 'app'
    assert rtmp_fmt['ext'] == 'flv'
    assert rtmp_fmt['preference'] == -1
    assert sorted(fmts, key=lambda x: x.get('quality', 0)) is not None


def test_mtg_no_geo_and_subtitle_default(monkeypatch):
    ie = _make_ie()
    url = 'mtg:418113'
    sami = 'http://example.com/subs/nolang.xml'
    video = _base_video(sami_path=sami)
    streams = {'streams': {'medium': 'http://example.com/v.mp4'}}

    called = []
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda ctx: called.append(ctx))
    def fake_dl(url_or_req, video_id, note=None, **kw):
        s = str(url_or_req)
        if '/stream/' in s:
            return streams
        return video
    monkeypatch.setattr(ie, '_download_json', fake_dl)
    monkeypatch.setattr(ie, '_extract_f4m_formats', lambda *a, **k: [])
    monkeypatch.setattr(ie, '_extract_m3u8_formats', lambda *a, **k: [])

    res = ie._real_extract(url)
    assert called == []
    assert res['id'] == '418113'
    # sami_path has no _xx.xml so default from netloc of mtg: url -> ''
    assert res['subtitles'] == {'': [{'url': sami}]}
    assert len(res['formats']) == 1
    assert res['formats'][0]['url'] == 'http://example.com/v.mp4'


def test_403_forbidden_expected(monkeypatch):
    ie = _make_ie()
    url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    video = _base_video()
    http_err = _make_http_error(403, b'{"msg": "Blocked msg"}')
    wrapped = ExtractorError('download failed', cause=http_err)
    def fake_dl(url_or_req, video_id, note=None, **kw):
        s = str(url_or_req)
        if '/stream/' in s:
            raise wrapped
        return video
    monkeypatch.setattr(ie, '_download_json', fake_dl)
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda ctx: None)
    with pytest.raises(ExtractorError) as ei:
        ie._real_extract(url)
    # the 403 branch replaces the original error with one carrying the msg
    assert ei.value is not wrapped
    assert 'Blocked msg' in str(ei.value)


def test_reraise_non403_and_generic(monkeypatch):
    ie = _make_ie()
    url = 'mtg:418113'
    video = _base_video()
    # case 1: HTTPError with 404 -> re-raise original
    http404 = _make_http_error(404, b'not found')
    wrapped404 = ExtractorError('404 failed', cause=http404)
    def fake404(url_or_req, video_id, note=None, **kw):
        s = str(url_or_req)
        if '/stream/' in s:
            raise wrapped404
        return video
    monkeypatch.setattr(ie, '_download_json', fake404)
    with pytest.raises(ExtractorError) as ei1:
        ie._real_extract(url)
    assert ei1.value is wrapped404
    # case 2: generic ExtractorError without HTTPError cause -> re-raise
    wrapped_gen = ExtractorError('generic fail')
    def fake_gen(url_or_req, video_id, note=None, **kw):
        s = str(url_or_req)
        if '/stream/' in s:
            raise wrapped_gen
        return video
    monkeypatch.setattr(ie, '_download_json', fake_gen)
    with pytest.raises(ExtractorError) as ei2:
        ie._real_extract(url)
    assert ei2.value is wrapped_gen


def test_geo_blocked_no_formats(monkeypatch):
    ie = _make_ie()
    url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    video = _base_video(is_geo_blocked=True, sami_path=None)
    streams = {'streams': {'empty': None, 'empty2': ''}}
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda ctx: None)
    def fake_dl(url_or_req, video_id, note=None, **kw):
        s = str(url_or_req)
        if '/stream/' in s:
            return streams
        return video
    monkeypatch.setattr(ie, '_download_json', fake_dl)
    with pytest.raises(GeoRestrictedError):
        ie._real_extract(url)


def test_no_formats_not_blocked_sort_raises(monkeypatch):
    ie = _make_ie()
    url = 'mtg:418113'
    video = _base_video(is_geo_blocked=False, sami_path=None)
    streams = {'streams': {}}
    def fake_dl(url_or_req, video_id, note=None, **kw):
        s = str(url_or_req)
        if '/stream/' in s:
            return streams
        return video
    monkeypatch.setattr(ie, '_download_json', fake_dl)
    with pytest.raises(ExtractorError, match='No video formats found'):
        ie._real_extract(url)


def test_no_sami_path_empty_subtitles_and_full_fields(monkeypatch):
    ie = _make_ie()
    url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    video = {
        'title': 'Full Title',
        'description': None,
        'format_title': None,
        'format_position': {},
        '_embedded': {},
        'duration': '3600',
        'created_at': '2015-06-12T00:00:00.000Z',
        'views': {},
        'age_limit': 18,
    }
    streams = {'streams': {'medium': 'http://example.com/a.mp4'}}
    monkeypatch.setattr(ie, '_initialize_geo_bypass', lambda ctx: None)
    def fake_dl(url_or_req, video_id, note=None, **kw):
        s = str(url_or_req)
        if '/stream/' in s:
            return streams
        return video
    monkeypatch.setattr(ie, '_download_json', fake_dl)
    monkeypatch.setattr(ie, '_extract_f4m_formats', lambda *a, **k: [])
    monkeypatch.setattr(ie, '_extract_m3u8_formats', lambda *a, **k: [])
    res = ie._real_extract(url)
    assert res['subtitles'] == {}
    assert res['title'] == 'Full Title'
    assert res['series'] is None
    assert res['episode_number'] is None
    assert res['season'] is None
    assert res['season_number'] is None
    assert res['duration'] == 3600
    assert isinstance(res['timestamp'], int)
    assert res['age_limit'] == 18
    assert len(res['formats']) == 1
    assert res['formats'][0]['url'] == 'http://example.com/a.mp4'
