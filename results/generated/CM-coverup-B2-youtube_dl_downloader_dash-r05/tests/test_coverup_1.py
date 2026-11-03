# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

"""Tests for youtube_dl.downloader.dash.DashSegmentsFD.real_download.

Covers all lines and branches of DashSegmentsFD.real_download (lines 19-80)
by stubbing the inherited FragmentFD helpers with recording test doubles.
"""

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError, urljoin


class FakeYDL(object):
    """Minimal stand-in for a YoutubeDL instance."""

    def __init__(self):
        self.params = {}


def make_http_error(url):
    return compat_urllib_error.HTTPError(url, 404, 'Not Found', None, None)


class OutcomeRunner(object):
    """Callable standing in for FragmentFD._download_fragment.

    Replays scripted outcomes per URL. Each outcome is a tuple:
      ('ok', bytes)            -> returns (True, bytes)
      ('fail', None)           -> returns (False, None)
      ('http_error', None)     -> raises compat_urllib_error.HTTPError
      ('download_error', msg)  -> raises DownloadError(msg)
    The last outcome in a list repeats indefinitely; URLs without a script
    entry always succeed with default content.
    """

    DEFAULT = ('ok', b'fragment-data')

    def __init__(self, script=None):
        self.script = dict(script or {})
        self.urls = []

    def __call__(self, ctx, url, info_dict):
        self.urls.append(url)
        outcomes = self.script.setdefault(url, [self.DEFAULT])
        outcome = outcomes.pop(0) if len(outcomes) > 1 else outcomes[0]
        kind, value = outcome
        if kind == 'ok':
            return True, value
        if kind == 'fail':
            return False, None
        if kind == 'http_error':
            raise make_http_error(url)
        if kind == 'download_error':
            raise DownloadError(value)
        raise AssertionError('unknown outcome kind: %r' % (kind,))


def make_fd(monkeypatch, params=None, script=None, resume_from=0):
    """Build a DashSegmentsFD with all inherited fragment helpers stubbed."""
    fd = DashSegmentsFD(FakeYDL(), params or {})
    runner = OutcomeRunner(script)
    calls = {'prepare': [], 'append': [], 'finish': [],
             'retry': [], 'skip': [], 'error': []}

    def prepare(ctx):
        calls['prepare'].append(dict(ctx))
        ctx['fragment_index'] = resume_from

    def append(ctx, content):
        calls['append'].append(content)

    def finish(ctx):
        calls['finish'].append(dict(ctx))

    def retry(err, frag_index, count, retries):
        calls['retry'].append((frag_index, count, retries))

    def skip(frag_index):
        calls['skip'].append(frag_index)

    def error(msg, tb=None, expected=False):
        calls['error'].append(msg)

    monkeypatch.setattr(fd, '_download_fragment', runner)
    monkeypatch.setattr(fd, '_prepare_and_start_frag_download', prepare)
    monkeypatch.setattr(fd, '_append_fragment', append)
    monkeypatch.setattr(fd, '_finish_frag_download', finish)
    monkeypatch.setattr(fd, 'report_retry_fragment', retry)
    monkeypatch.setattr(fd, 'report_skip_fragment', skip)
    monkeypatch.setattr(fd, 'report_error', error)
    return fd, runner, calls


FRAGMENTS = [
    {'url': 'http://example.com/seg-1.m4s'},
    {'url': 'http://example.com/seg-2.m4s'},
]


def test_success_downloads_all_fragments(monkeypatch):
    fd, runner, calls = make_fd(monkeypatch)
    info_dict = {'fragments': list(FRAGMENTS)}

    result = fd.real_download('dest.mp4', info_dict)

    assert result is True
    assert runner.urls == ['http://example.com/seg-1.m4s',
                           'http://example.com/seg-2.m4s']
    assert calls['append'] == [b'fragment-data', b'fragment-data']
    assert len(calls['prepare']) == 1
    assert calls['prepare'][0]['filename'] == 'dest.mp4'
    assert calls['prepare'][0]['total_frags'] == 2
    assert len(calls['finish']) == 1
    assert calls['retry'] == []
    assert calls['skip'] == []
    assert calls['error'] == []


def test_test_mode_downloads_only_first_fragment(monkeypatch):
    fd, runner, calls = make_fd(monkeypatch, params={'test': True})
    info_dict = {'fragments': list(FRAGMENTS)}

    result = fd.real_download('dest.mp4', info_dict)

    assert result is True
    assert runner.urls == ['http://example.com/seg-1.m4s']
    assert calls['append'] == [b'fragment-data']
    assert calls['prepare'][0]['total_frags'] == 1
    assert len(calls['finish']) == 1


def test_resume_skips_already_downloaded_fragments(monkeypatch):
    fd, runner, calls = make_fd(monkeypatch, resume_from=1)
    info_dict = {'fragments': list(FRAGMENTS)}

    result = fd.real_download('dest.mp4', info_dict)

    assert result is True
    assert runner.urls == ['http://example.com/seg-2.m4s']
    assert calls['append'] == [b'fragment-data']
    assert len(calls['finish']) == 1


def test_fragment_url_built_from_path_and_base_url(monkeypatch):
    base = 'http://example.com/dash/'
    fd, runner, calls = make_fd(monkeypatch)
    info_dict = {
        'fragment_base_url': base,
        'fragments': [{'path': 'seg-1.m4s'}, {'path': 'seg-2.m4s'}],
    }

    result = fd.real_download('dest.mp4', info_dict)

    assert result is True
    assert runner.urls == [urljoin(base, 'seg-1.m4s'),
                           urljoin(base, 'seg-2.m4s')]
    assert runner.urls == ['http://example.com/dash/seg-1.m4s',
                           'http://example.com/dash/seg-2.m4s']
    assert len(calls['finish']) == 1


def test_missing_fragment_url_and_base_url_asserts(monkeypatch):
    fd, runner, calls = make_fd(monkeypatch)
    info_dict = {'fragments': [{'path': 'seg-1.m4s'}]}

    with pytest.raises(AssertionError):
        fd.real_download('dest.mp4', info_dict)

    assert runner.urls == []
    assert calls['append'] == []
    assert calls['finish'] == []


def test_fragment_download_failure_returns_false(monkeypatch):
    fd, runner, calls = make_fd(
        monkeypatch,
        script={'http://example.com/seg-1.m4s': [('fail', None)]})
    info_dict = {'fragments': list(FRAGMENTS)}

    result = fd.real_download('dest.mp4', info_dict)

    assert result is False
    assert runner.urls == ['http://example.com/seg-1.m4s']
    assert calls['append'] == []
    assert calls['finish'] == []
    assert calls['error'] == []


def test_http_error_is_retried_then_succeeds(monkeypatch):
    fd, runner, calls = make_fd(
        monkeypatch,
        params={'fragment_retries': 2},
        script={'http://example.com/seg-1.m4s': [
            ('http_error', None), ('ok', b'first')]})
    info_dict = {'fragments': list(FRAGMENTS)}

    result = fd.real_download('dest.mp4', info_dict)

    assert result is True
    assert runner.urls == ['http://example.com/seg-1.m4s',
                           'http://example.com/seg-1.m4s',
                           'http://example.com/seg-2.m4s']
    assert calls['retry'] == [(1, 1, 2)]
    assert calls['append'] == [b'first', b'fragment-data']
    assert len(calls['finish']) == 1
    assert calls['skip'] == []
    assert calls['error'] == []


def test_http_error_gives_up_on_fatal_fragment(monkeypatch):
    fd, runner, calls = make_fd(
        monkeypatch,
        params={'fragment_retries': 1},
        script={'http://example.com/seg-1.m4s': [('http_error', None)]})
    info_dict = {'fragments': list(FRAGMENTS)}

    result = fd.real_download('dest.mp4', info_dict)

    assert result is False
    assert runner.urls == ['http://example.com/seg-1.m4s',
                           'http://example.com/seg-1.m4s']
    assert calls['retry'] == [(1, 1, 1)]
    assert calls['error'] == ['giving up after 1 fragment retries']
    assert calls['append'] == []
    assert calls['finish'] == []


def test_http_error_gives_up_skips_unavailable_fragment(monkeypatch):
    fd, runner, calls = make_fd(
        monkeypatch,
        params={'fragment_retries': 0},
        script={'http://example.com/seg-2.m4s': [('http_error', None)]})
    info_dict = {'fragments': list(FRAGMENTS)}

    result = fd.real_download('dest.mp4', info_dict)

    assert result is True
    assert runner.urls == ['http://example.com/seg-1.m4s',
                           'http://example.com/seg-2.m4s']
    assert calls['skip'] == [2]
    assert calls['error'] == []
    assert calls['append'] == [b'fragment-data']
    assert len(calls['finish']) == 1


def test_download_error_skips_nonfatal_fragment(monkeypatch):
    fd, runner, calls = make_fd(
        monkeypatch,
        script={'http://example.com/seg-2.m4s': [('download_error', 'boom')]})
    info_dict = {'fragments': list(FRAGMENTS)}

    result = fd.real_download('dest.mp4', info_dict)

    assert result is True
    assert calls['skip'] == [2]
    assert calls['error'] == []
    assert calls['append'] == [b'fragment-data']
    assert len(calls['finish']) == 1


def test_download_error_on_first_fragment_raises(monkeypatch):
    fd, runner, calls = make_fd(
        monkeypatch,
        script={'http://example.com/seg-1.m4s': [('download_error', 'boom')]})
    info_dict = {'fragments': list(FRAGMENTS)}

    with pytest.raises(DownloadError):
        fd.real_download('dest.mp4', info_dict)

    assert calls['skip'] == []
    assert calls['append'] == []
    assert calls['finish'] == []


def test_download_error_fatal_when_skip_disabled(monkeypatch):
    fd, runner, calls = make_fd(
        monkeypatch,
        params={'skip_unavailable_fragments': False},
        script={'http://example.com/seg-2.m4s': [('download_error', 'boom')]})
    info_dict = {'fragments': list(FRAGMENTS)}

    with pytest.raises(DownloadError):
        fd.real_download('dest.mp4', info_dict)

    assert calls['skip'] == []
    assert calls['append'] == [b'fragment-data']
    assert calls['finish'] == []
