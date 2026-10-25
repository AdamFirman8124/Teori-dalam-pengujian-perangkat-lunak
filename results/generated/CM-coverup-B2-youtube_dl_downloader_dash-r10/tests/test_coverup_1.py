# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError


class FakeYDL(object):
    def __init__(self):
        self.screen = []
        self.errors = []

    def to_screen(self, *args, **kwargs):
        self.screen.append(args)

    def to_stderr(self, message):
        self.screen.append(message)

    def report_warning(self, *args, **kwargs):
        pass

    def report_error(self, *args, **kwargs):
        self.errors.append(args)


def make_fd(params=None):
    ydl = FakeYDL()
    return DashSegmentsFD(ydl, params or {}), ydl


def install_harness(monkeypatch, fd, download_results, fragment_index=0):
    """Replace all FragmentFD helpers so no real file/network IO happens."""
    calls = {
        'prepare': 0,
        'ctx': None,
        'urls': [],
        'append': [],
        'finish': 0,
        'retry': [],
        'skip': [],
        'error': [],
    }
    results = list(download_results)

    def prepare(ctx):
        calls['prepare'] += 1
        calls['ctx'] = ctx
        ctx['fragment_index'] = fragment_index

    def download(ctx, frag_url, info_dict):
        calls['urls'].append(frag_url)
        result = results.pop(0)
        if isinstance(result, Exception):
            raise result
        return result

    def append(ctx, frag_content):
        calls['append'].append(frag_content)

    def finish(ctx):
        calls['finish'] += 1

    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', prepare)
    monkeypatch.setattr(fd, '_download_fragment', download)
    monkeypatch.setattr(fd, '_append_fragment', append)
    monkeypatch.setattr(fd, '_finish_frag_download', finish)
    monkeypatch.setattr(fd, 'report_retry_fragment',
                        lambda *a: calls['retry'].append(a))
    monkeypatch.setattr(fd, 'report_skip_fragment',
                        lambda *a: calls['skip'].append(a))
    monkeypatch.setattr(fd, 'report_error',
                        lambda *a: calls['error'].append(a))
    return calls


def http_error(url='http://example.com/frag'):
    return compat_urllib_error.HTTPError(url, 404, 'Not Found', {}, None)


def test_real_download_success(monkeypatch):
    fd, ydl = make_fd()
    info_dict = {
        'fragment_base_url': 'http://example.com/base/',
        'fragments': [
            {'url': 'http://example.com/a.mp4'},
            {'path': 'b.mp4'},
        ],
    }
    calls = install_harness(monkeypatch, fd, [(True, b'AAA'), (True, b'BBB')])

    assert fd.real_download('out.mp4', info_dict) is True

    assert calls['prepare'] == 1
    assert calls['ctx']['filename'] == 'out.mp4'
    assert calls['ctx']['total_frags'] == 2
    assert calls['urls'] == [
        'http://example.com/a.mp4',
        'http://example.com/base/b.mp4',
    ]
    assert calls['append'] == [b'AAA', b'BBB']
    assert calls['finish'] == 1
    assert calls['retry'] == []
    assert calls['skip'] == []
    assert calls['error'] == []


def test_real_download_test_param_limits_fragments(monkeypatch):
    fd, ydl = make_fd({'test': True})
    info_dict = {'fragments': [{'url': 'u1'}, {'url': 'u2'}, {'url': 'u3'}]}
    calls = install_harness(monkeypatch, fd, [(True, b'X')])

    assert fd.real_download('out.mp4', info_dict) is True

    assert calls['ctx']['total_frags'] == 1
    assert calls['urls'] == ['u1']
    assert calls['append'] == [b'X']
    assert calls['finish'] == 1


def test_real_download_skips_already_downloaded_fragments(monkeypatch):
    fd, ydl = make_fd()
    info_dict = {'fragments': [{'url': 'u1'}, {'url': 'u2'}]}
    calls = install_harness(monkeypatch, fd, [(True, b'B')], fragment_index=1)

    assert fd.real_download('out.mp4', info_dict) is True

    assert calls['urls'] == ['u2']
    assert calls['append'] == [b'B']
    assert calls['finish'] == 1


def test_real_download_returns_false_when_fragment_download_fails(monkeypatch):
    fd, ydl = make_fd()
    info_dict = {'fragments': [{'url': 'u1'}]}
    calls = install_harness(monkeypatch, fd, [(False, None)])

    assert fd.real_download('out.mp4', info_dict) is False

    assert calls['urls'] == ['u1']
    assert calls['append'] == []
    assert calls['finish'] == 0


def test_real_download_retries_http_error_then_succeeds(monkeypatch):
    fd, ydl = make_fd({'fragment_retries': 1})
    info_dict = {'fragments': [{'url': 'u1'}]}
    calls = install_harness(monkeypatch, fd, [http_error('u1'), (True, b'OK')])

    assert fd.real_download('out.mp4', info_dict) is True

    assert calls['urls'] == ['u1', 'u1']
    assert calls['append'] == [b'OK']
    assert len(calls['retry']) == 1
    assert calls['retry'][0][1] == 1  # frag_index
    assert calls['retry'][0][2] == 1  # attempt count
    assert calls['retry'][0][3] == 1  # retries
    assert calls['error'] == []
    assert calls['finish'] == 1


def test_real_download_gives_up_on_first_fragment_http_error(monkeypatch):
    fd, ydl = make_fd({'fragment_retries': 1})
    info_dict = {'fragments': [{'url': 'u1'}]}
    calls = install_harness(monkeypatch, fd, [http_error('u1'), http_error('u1')])

    assert fd.real_download('out.mp4', info_dict) is False

    assert calls['urls'] == ['u1', 'u1']
    assert len(calls['retry']) == 1
    assert calls['skip'] == []
    assert calls['error'] == [('giving up after 1 fragment retries',)]
    assert calls['finish'] == 0


def test_real_download_skips_unavailable_fragment_after_retries(monkeypatch):
    fd, ydl = make_fd({'fragment_retries': 1})
    info_dict = {'fragments': [{'url': 'u1'}, {'url': 'u2'}]}
    calls = install_harness(
        monkeypatch, fd, [(True, b'A'), http_error('u2'), http_error('u2')])

    assert fd.real_download('out.mp4', info_dict) is True

    assert calls['append'] == [b'A']
    assert calls['skip'] == [(2,)]
    assert calls['error'] == []
    assert calls['finish'] == 1


def test_real_download_raises_download_error_on_first_fragment(monkeypatch):
    fd, ydl = make_fd()
    info_dict = {'fragments': [{'url': 'u1'}]}
    calls = install_harness(monkeypatch, fd, [DownloadError('boom')])

    with pytest.raises(DownloadError):
        fd.real_download('out.mp4', info_dict)

    assert calls['append'] == []
    assert calls['skip'] == []
    assert calls['finish'] == 0


def test_real_download_skips_fragment_on_download_error(monkeypatch):
    fd, ydl = make_fd()
    info_dict = {'fragments': [{'url': 'u1'}, {'url': 'u2'}]}
    calls = install_harness(
        monkeypatch, fd, [(True, b'A'), DownloadError('boom')])

    assert fd.real_download('out.mp4', info_dict) is True

    assert calls['append'] == [b'A']
    assert calls['skip'] == [(2,)]
    assert calls['error'] == []
    assert calls['finish'] == 1


def test_real_download_raises_download_error_when_skip_disabled(monkeypatch):
    # skip_unavailable_fragments=False makes every fragment fatal, so a
    # DownloadError is re-raised instead of being skipped.
    fd, ydl = make_fd({'skip_unavailable_fragments': False})
    info_dict = {'fragments': [{'url': 'u1'}, {'url': 'u2'}]}
    calls = install_harness(
        monkeypatch, fd, [(True, b'A'), DownloadError('boom')])

    with pytest.raises(DownloadError):
        fd.real_download('out.mp4', info_dict)

    assert calls['append'] == [b'A']
    assert calls['skip'] == []
    assert calls['error'] == []
    assert calls['finish'] == 0


def test_real_download_gives_up_when_skip_disabled(monkeypatch):
    # fatal=True and HTTP retries exhausted -> report_error + return False
    fd, ydl = make_fd({
        'skip_unavailable_fragments': False,
        'fragment_retries': 1,
    })
    info_dict = {'fragments': [{'url': 'u1'}, {'url': 'u2'}]}
    calls = install_harness(
        monkeypatch, fd, [(True, b'A'), http_error('u2'), http_error('u2')])

    assert fd.real_download('out.mp4', info_dict) is False

    assert calls['append'] == [b'A']
    assert len(calls['retry']) == 1
    assert calls['skip'] == []
    assert calls['error'] == [('giving up after 1 fragment retries',)]
    assert calls['finish'] == 0


def test_real_download_requires_base_url_for_path_fragment(monkeypatch):
    fd, ydl = make_fd()
    info_dict = {'fragments': [{'path': 'a.mp4'}]}
    calls = install_harness(monkeypatch, fd, [])

    with pytest.raises(AssertionError):
        fd.real_download('out.mp4', info_dict)

    assert calls['urls'] == []
    assert calls['append'] == []
    assert calls['finish'] == 0
