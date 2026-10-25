# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

import pytest


def test_dash_success_direct_urls(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 0, 'skip_unavailable_fragments': True})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}, {'url': 'http://example.com/seg2'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    finished = {}
    def fake_finish(ctx):
        finished['called'] = True

    appended = []
    def fake_append(ctx, content):
        appended.append(content)

    seen_urls = []
    def fake_download(ctx, url, info):
        seen_urls.append(url)
        return (True, b'data-' + url.encode())

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)

    assert fd.real_download(filename, info_dict) is True
    assert seen_urls == ['http://example.com/seg1', 'http://example.com/seg2']
    assert len(appended) == 2
    assert appended[0] == b'data-http://example.com/seg1'
    assert finished.get('called') is True


def test_dash_test_mode_and_base_url_join(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'test': True, 'fragment_retries': 0})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {
        'fragment_base_url': 'http://example.com/base/',
        'fragments': [{'path': 'seg1.m4s'}, {'path': 'seg2.m4s'}, {'path': 'seg3.m4s'}],
    }
    captured = {}
    def fake_prepare(ctx):
        captured['total'] = ctx['total_frags']
        captured['filename'] = ctx['filename']
        ctx['fragment_index'] = 0

    finished = {}
    def fake_finish(ctx):
        finished['called'] = True

    appended = []
    def fake_append(ctx, c):
        appended.append(c)

    seen = []
    def fake_download(ctx, url, info):
        seen.append(url)
        return (True, b'x')

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)

    assert fd.real_download(filename, info_dict) is True
    assert captured['total'] == 1
    assert captured['filename'] == filename
    assert seen == ['http://example.com/base/seg1.m4s']
    assert len(appended) == 1
    assert finished.get('called') is True


def test_dash_resume_skips_already_downloaded(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 0})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}, {'url': 'http://example.com/seg2'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 1

    def fake_finish(ctx):
        pass

    appended = []
    def fake_append(ctx, c):
        appended.append(c)

    seen = []
    def fake_download(ctx, url, info):
        seen.append(url)
        return (True, b'data')

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)

    assert fd.real_download(filename, info_dict) is True
    assert seen == ['http://example.com/seg2']
    assert len(appended) == 1


def test_dash_download_returns_false(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 0})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    finished = {'called': False}
    def fake_finish(ctx):
        finished['called'] = True

    appended = []
    def fake_append(ctx, c):
        appended.append(c)

    def fake_download(ctx, url, info):
        return (False, b'')

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)

    assert fd.real_download(filename, info_dict) is False
    assert appended == []
    assert finished['called'] is False


def test_dash_http_error_retry_then_success(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.compat import compat_urllib_error
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 2, 'skip_unavailable_fragments': True})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    def fake_finish(ctx):
        pass

    appended = []
    def fake_append(ctx, c):
        appended.append(c)

    retries = []
    def fake_retry(err, frag_index, count, retry_max):
        retries.append((frag_index, count, retry_max))

    attempts = {'n': 0}
    def fake_download(ctx, url, info):
        if attempts['n'] == 0:
            attempts['n'] += 1
            raise compat_urllib_error.HTTPError(url, 404, 'Not Found', {}, None)
        return (True, b'recovered')

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)
    monkeypatch.setattr(fd, 'report_retry_fragment', fake_retry)

    assert fd.real_download(filename, info_dict) is True
    assert retries == [(1, 1, 2)]
    assert appended == [b'recovered']


def test_dash_http_error_give_up_fatal_first_fragment(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.compat import compat_urllib_error
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 1, 'skip_unavailable_fragments': True})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    def fake_finish(ctx):
        pass

    def fake_download(ctx, url, info):
        raise compat_urllib_error.HTTPError(url, 404, 'Not Found', {}, None)

    retry_calls = []
    def fake_retry(err, frag_index, count, retry_max):
        retry_calls.append((frag_index, count))

    errors = []
    def fake_error(msg, *args, **kwargs):
        errors.append(msg)

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)
    monkeypatch.setattr(fd, 'report_retry_fragment', fake_retry)
    monkeypatch.setattr(fd, 'report_error', fake_error)

    assert fd.real_download(filename, info_dict) is False
    assert retry_calls == [(1, 1)]
    assert len(errors) == 1
    assert 'giving up after 1 fragment retries' in errors[0]


def test_dash_http_error_give_up_nonfatal_skip(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.compat import compat_urllib_error
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 0, 'skip_unavailable_fragments': True})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}, {'url': 'http://example.com/seg2'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    finished = {}
    def fake_finish(ctx):
        finished['called'] = True

    appended = []
    def fake_append(ctx, c):
        appended.append(c)

    def fake_download(ctx, url, info):
        if 'seg2' in url:
            raise compat_urllib_error.HTTPError(url, 404, 'Not Found', {}, None)
        return (True, b'frag1')

    skipped = []
    def fake_skip(frag_index):
        skipped.append(frag_index)

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)
    monkeypatch.setattr(fd, 'report_skip_fragment', fake_skip)

    assert fd.real_download(filename, info_dict) is True
    assert appended == [b'frag1']
    assert skipped == [2]
    assert finished.get('called') is True


def test_dash_download_error_nonfatal_skip(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.utils import DownloadError
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 2, 'skip_unavailable_fragments': True})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}, {'url': 'http://example.com/seg2'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    def fake_finish(ctx):
        pass

    appended = []
    def fake_append(ctx, c):
        appended.append(c)

    def fake_download(ctx, url, info):
        if 'seg2' in url:
            raise DownloadError('http fail')
        return (True, b'frag1')

    skipped = []
    def fake_skip(frag_index):
        skipped.append(frag_index)

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)
    monkeypatch.setattr(fd, 'report_skip_fragment', fake_skip)

    assert fd.real_download(filename, info_dict) is True
    assert appended == [b'frag1']
    assert skipped == [2]


def test_dash_download_error_fatal_raises(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.utils import DownloadError
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 2, 'skip_unavailable_fragments': True})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    def fake_finish(ctx):
        pass

    def fake_download(ctx, url, info):
        raise DownloadError('fatal http fail')

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)

    with pytest.raises(DownloadError):
        fd.real_download(filename, info_dict)


def test_dash_skip_unavailable_false_makes_second_fatal(monkeypatch, tmp_path):
    from youtube_dl import YoutubeDL
    from youtube_dl.compat import compat_urllib_error
    from youtube_dl.downloader.dash import DashSegmentsFD
    ydl = YoutubeDL({'quiet': True})
    fd = DashSegmentsFD(ydl, {'fragment_retries': 0, 'skip_unavailable_fragments': False})
    filename = str(tmp_path / 'out.mp4')
    info_dict = {'fragments': [{'url': 'http://example.com/seg1'}, {'url': 'http://example.com/seg2'}]}

    def fake_prepare(ctx):
        ctx['fragment_index'] = 0

    def fake_finish(ctx):
        pass

    appended = []
    def fake_append(ctx, c):
        appended.append(c)

    def fake_download(ctx, url, info):
        if 'seg2' in url:
            raise compat_urllib_error.HTTPError(url, 500, 'Server Error', {}, None)
        return (True, b'frag1')

    errors = []
    def fake_error(msg, *args, **kwargs):
        errors.append(msg)

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', fake_prepare)
    monkeypatch.setattr(fd, '_finish_frag_download', fake_finish)
    monkeypatch.setattr(fd, '_append_fragment', fake_append)
    monkeypatch.setattr(fd, '_download_fragment', fake_download)
    monkeypatch.setattr(fd, 'report_error', fake_error)

    assert fd.real_download(filename, info_dict) is False
    assert appended == [b'frag1']
    assert len(errors) == 1
    assert 'giving up after 0 fragment retries' in errors[0]
