# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

import io
import pytest
from youtube_dl.compat import compat_urllib_error
from youtube_dl.utils import DownloadError
from youtube_dl.downloader.dash import DashSegmentsFD


def _http_error(url='http://example.com/frag'):
    return compat_urllib_error.HTTPError(url, 404, 'Not Found', {}, io.BytesIO(b''))


def _make_fd(params, resume_index=0, side_effects=None):
    fd = DashSegmentsFD.__new__(DashSegmentsFD)
    fd.params = dict(params)
    calls = {
        'append': [],
        'download_urls': [],
        'retry': [],
        'skip': [],
        'error': [],
        'prepared': [],
        'finished': [],
    }
    effects = list(side_effects) if side_effects is not None else None
    state = {'i': 0}

    def _prep(ctx):
        calls['prepared'].append(dict(ctx))
        ctx['fragment_index'] = resume_index

    def _dl(ctx, frag_url, info_dict, headers=None):
        calls['download_urls'].append(frag_url)
        if effects is not None:
            eff = effects[state['i']]
            state['i'] += 1
            if isinstance(eff, BaseException):
                raise eff
            return eff
        return (True, b'data')

    def _append(ctx, content):
        calls['append'].append(content)

    def _finish(ctx):
        calls['finished'].append(True)

    def _retry(err, frag_index, count, retries):
        calls['retry'].append((frag_index, count, retries))

    def _skip(frag_index):
        calls['skip'].append(frag_index)

    def _error(msg, *args, **kwargs):
        calls['error'].append(msg)

    fd._prepare_and_start_frag_download = _prep
    fd._download_fragment = _dl
    fd._append_fragment = _append
    fd._finish_frag_download = _finish
    fd.report_retry_fragment = _retry
    fd.report_skip_fragment = _skip
    fd.report_error = _error
    return fd, calls


def test_success_direct_urls(tmp_path):
    fd, calls = _make_fd({}, resume_index=0)
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]}
    assert fd.real_download(filename, info) is True
    assert calls['download_urls'] == ['http://example.com/f1', 'http://example.com/f2']
    assert len(calls['append']) == 2
    assert len(calls['finished']) == 1
    assert calls['prepared'][0]['filename'] == filename
    assert calls['prepared'][0]['total_frags'] == 2


def test_test_mode_truncates(tmp_path):
    fd, calls = _make_fd({'test': True}, resume_index=0)
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}, {'url': 'http://example.com/f3'}]}
    assert fd.real_download(filename, info) is True
    assert calls['download_urls'] == ['http://example.com/f1']
    assert len(calls['append']) == 1
    assert len(calls['finished']) == 1


def test_path_urljoin(tmp_path):
    fd, calls = _make_fd({}, resume_index=0)
    filename = str(tmp_path / 'out.mp4')
    info = {
        'fragment_base_url': 'http://example.com/videos/',
        'fragments': [{'path': 'seg1.m4s'}, {'path': 'seg2.m4s'}],
    }
    assert fd.real_download(filename, info) is True
    assert calls['download_urls'] == ['http://example.com/videos/seg1.m4s', 'http://example.com/videos/seg2.m4s']
    assert len(calls['append']) == 2


def test_empty_fragments(tmp_path):
    fd, calls = _make_fd({}, resume_index=0)
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': []}
    assert fd.real_download(filename, info) is True
    assert calls['download_urls'] == []
    assert calls['append'] == []
    assert len(calls['finished']) == 1


def test_resume_skips_already_downloaded(tmp_path):
    fd, calls = _make_fd({}, resume_index=1)
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]}
    assert fd.real_download(filename, info) is True
    assert calls['download_urls'] == ['http://example.com/f2']
    assert len(calls['append']) == 1
    assert len(calls['finished']) == 1


def test_unsuccessful_download_returns_false(tmp_path):
    fd, calls = _make_fd({}, resume_index=0, side_effects=[(False, None)])
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}]}
    assert fd.real_download(filename, info) is False
    assert calls['download_urls'] == ['http://example.com/f1']
    assert calls['append'] == []
    assert calls['finished'] == []


def test_http_error_retry_then_success(tmp_path):
    fd, calls = _make_fd(
        {'fragment_retries': 2}, resume_index=0,
        side_effects=[_http_error(), (True, b'fragdata')],
    )
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}]}
    assert fd.real_download(filename, info) is True
    assert calls['download_urls'] == ['http://example.com/f1', 'http://example.com/f1']
    assert calls['append'] == [b'fragdata']
    assert len(calls['retry']) == 1
    assert calls['retry'][0][0] == 1
    assert len(calls['finished']) == 1


def test_http_error_exhausted_first_fragment_fatal(tmp_path):
    fd, calls = _make_fd(
        {'fragment_retries': 1}, resume_index=0,
        side_effects=[_http_error('http://example.com/f1'), _http_error('http://example.com/f1')],
    )
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]}
    assert fd.real_download(filename, info) is False
    assert calls['download_urls'] == ['http://example.com/f1', 'http://example.com/f1']
    assert len(calls['retry']) == 1
    assert len(calls['error']) == 1
    assert 'giving up after 1 fragment retries' in calls['error'][0]
    assert calls['finished'] == []


def test_http_error_exhausted_nonfatal_skip_and_continue(tmp_path):
    fd, calls = _make_fd(
        {'fragment_retries': 0, 'skip_unavailable_fragments': True}, resume_index=0,
        side_effects=[(True, b'f1'), _http_error('http://example.com/f2'), (True, b'f3')],
    )
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}, {'url': 'http://example.com/f3'}]}
    assert fd.real_download(filename, info) is True
    assert calls['download_urls'] == ['http://example.com/f1', 'http://example.com/f2', 'http://example.com/f3']
    assert calls['append'] == [b'f1', b'f3']
    assert calls['skip'] == [2]
    assert calls['retry'] == []
    assert calls['error'] == []
    assert len(calls['finished']) == 1


def test_http_error_exhausted_fatal_no_skip(tmp_path):
    fd, calls = _make_fd(
        {'fragment_retries': 0, 'skip_unavailable_fragments': False}, resume_index=0,
        side_effects=[(True, b'f1'), _http_error('http://example.com/f2')],
    )
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]}
    assert fd.real_download(filename, info) is False
    assert calls['skip'] == []
    assert len(calls['error']) == 1
    assert calls['append'] == [b'f1']
    assert calls['finished'] == []


def test_download_error_nonfatal_skip(tmp_path):
    fd, calls = _make_fd(
        {'skip_unavailable_fragments': True}, resume_index=0,
        side_effects=[(True, b'f1'), DownloadError('net fail'), (True, b'f3')],
    )
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}, {'url': 'http://example.com/f3'}]}
    assert fd.real_download(filename, info) is True
    assert calls['skip'] == [2]
    assert calls['append'] == [b'f1', b'f3']
    assert len(calls['finished']) == 1


def test_download_error_fatal_raises(tmp_path):
    fd, calls = _make_fd(
        {}, resume_index=0,
        side_effects=[DownloadError('fatal net fail')],
    )
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}]}
    with pytest.raises(DownloadError):
        fd.real_download(filename, info)
    assert calls['download_urls'] == ['http://example.com/f1']
    assert calls['skip'] == []
    assert calls['finished'] == []


def test_download_error_fatal_no_skip_raises_second_frag(tmp_path):
    fd, calls = _make_fd(
        {'skip_unavailable_fragments': False}, resume_index=0,
        side_effects=[(True, b'f1'), DownloadError('fail')],
    )
    filename = str(tmp_path / 'out.mp4')
    info = {'fragments': [{'url': 'http://example.com/f1'}, {'url': 'http://example.com/f2'}]}
    with pytest.raises(DownloadError):
        fd.real_download(filename, info)
    assert calls['append'] == [b'f1']
    assert calls['finished'] == []
