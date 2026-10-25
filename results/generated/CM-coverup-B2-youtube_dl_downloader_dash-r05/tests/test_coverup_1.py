# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError


class FakeYDL(object):
    params = {}

    def to_screen(self, *args, **kwargs):
        pass


class FakeFD(DashSegmentsFD):
    """DashSegmentsFD with the fragment machinery replaced by recording fakes."""

    def __init__(self, params=None, fragment_index=0, fail_urls=(),
                 http_error_urls=(), download_error_urls=(),
                 http_error_times=None):
        super(FakeFD, self).__init__(FakeYDL(), params or {})
        self.fragment_index = fragment_index
        self.fail_urls = set(fail_urls)
        self.http_error_urls = set(http_error_urls)
        self.download_error_urls = set(download_error_urls)
        # how many times each http_error_url raises HTTPError before
        # succeeding; None means it raises forever
        self.http_error_times = http_error_times
        self._http_error_count = {}

        self.prepared = False
        self.finished = False
        self.downloaded_urls = []
        self.appended_contents = []
        self.retries_reported = []
        self.skips_reported = []
        self.errors_reported = []

    # --- FragmentFD machinery fakes ---
    def _prepare_and_start_frag_download(self, ctx):
        self.prepared = True
        ctx['fragment_index'] = self.fragment_index

    def _download_fragment(self, ctx, frag_url, info_dict):
        self.downloaded_urls.append(frag_url)
        if frag_url in self.http_error_urls:
            times = self._http_error_count.get(frag_url, 0)
            if self.http_error_times is None or times < self.http_error_times:
                self._http_error_count[frag_url] = times + 1
                raise compat_urllib_error.HTTPError(
                    frag_url, 404, 'Not Found', None, None)
        if frag_url in self.download_error_urls:
            raise DownloadError('fragment download error')
        if frag_url in self.fail_urls:
            return (False, None)
        return (True, frag_url.encode('utf-8'))

    def _append_fragment(self, ctx, frag_content):
        self.appended_contents.append(frag_content)
        ctx['fragment_index'] += 1

    def _finish_frag_download(self, ctx):
        self.finished = True

    # --- reporting fakes ---
    def report_retry_fragment(self, err, frag_index, count, fragment_retries):
        self.retries_reported.append((frag_index, count, fragment_retries))

    def report_skip_fragment(self, frag_index):
        self.skips_reported.append(frag_index)

    def report_error(self, msg):
        self.errors_reported.append(msg)


SEG1 = 'http://example.com/seg1.m4s'
SEG2 = 'http://example.com/seg2.m4s'
SEG3 = 'http://example.com/seg3.m4s'


def make_info_dict(fragments, base_url=None):
    info = {'fragments': fragments}
    if base_url is not None:
        info['fragment_base_url'] = base_url
    return info


def test_success_with_explicit_urls():
    info = make_info_dict([{'url': SEG1}, {'url': SEG2}])
    fd = FakeFD()
    assert fd.real_download('dest.mp4', info) is True
    assert fd.prepared is True
    assert fd.finished is True
    assert fd.downloaded_urls == [SEG1, SEG2]
    assert fd.appended_contents == [SEG1.encode('utf-8'), SEG2.encode('utf-8')]
    assert fd.retries_reported == []
    assert fd.skips_reported == []
    assert fd.errors_reported == []


def test_success_with_base_url_and_path():
    info = make_info_dict(
        [{'path': 'seg1.m4s'}, {'path': 'seg2.m4s'}],
        base_url='http://example.com/a/')
    fd = FakeFD()
    assert fd.real_download('dest.mp4', info) is True
    assert fd.downloaded_urls == [
        'http://example.com/a/seg1.m4s',
        'http://example.com/a/seg2.m4s',
    ]
    assert fd.appended_contents == [
        b'http://example.com/a/seg1.m4s',
        b'http://example.com/a/seg2.m4s',
    ]
    assert fd.finished is True


def test_missing_base_url_asserts():
    info = make_info_dict([{'path': 'seg1.m4s'}])
    fd = FakeFD()
    with pytest.raises(AssertionError):
        fd.real_download('dest.mp4', info)
    assert fd.finished is False


def test_test_mode_downloads_only_first_fragment():
    info = make_info_dict([{'url': SEG1}, {'url': SEG2}, {'url': SEG3}])
    fd = FakeFD(params={'test': True})
    assert fd.real_download('dest.mp4', info) is True
    assert fd.downloaded_urls == [SEG1]
    assert fd.appended_contents == [SEG1.encode('utf-8')]
    assert fd.finished is True


def test_download_fragment_failure_returns_false():
    info = make_info_dict([{'url': SEG1}, {'url': SEG2}])
    fd = FakeFD(fail_urls=(SEG2,))
    assert fd.real_download('dest.mp4', info) is False
    assert fd.downloaded_urls == [SEG1, SEG2]
    assert fd.appended_contents == [SEG1.encode('utf-8')]
    assert fd.finished is False


def test_http_error_retried_then_success():
    info = make_info_dict([{'url': SEG1}])
    # SEG1 raises HTTPError once, then succeeds on the retry
    fd = FakeFD(params={'fragment_retries': 2}, http_error_urls=(SEG1,),
                http_error_times=1)
    assert fd.real_download('dest.mp4', info) is True
    # one failed attempt + one successful attempt
    assert fd.downloaded_urls == [SEG1, SEG1]
    assert fd.retries_reported == [(1, 1, 2)]
    assert fd.appended_contents == [SEG1.encode('utf-8')]
    assert fd.finished is True
    assert fd.skips_reported == []
    assert fd.errors_reported == []


def test_http_error_exhausted_nonfatal_skips_fragment():
    info = make_info_dict([{'url': SEG1}, {'url': SEG2}])
    # SEG2 always fails with HTTPError; skip_unavailable_fragments defaults
    # to True, so it is non-fatal (i != 0)
    fd = FakeFD(params={'fragment_retries': 1}, http_error_urls=(SEG2,))
    assert fd.real_download('dest.mp4', info) is True
    # initial attempt + 1 retry = 2 download attempts for SEG2
    assert fd.downloaded_urls == [SEG1, SEG2, SEG2]
    assert fd.retries_reported == [(2, 1, 1)]
    assert fd.skips_reported == [2]
    assert fd.appended_contents == [SEG1.encode('utf-8')]
    assert fd.finished is True
    assert fd.errors_reported == []


def test_http_error_exhausted_fatal_first_fragment_reports_error():
    info = make_info_dict([{'url': SEG1}])
    fd = FakeFD(params={'fragment_retries': 0}, http_error_urls=(SEG1,))
    assert fd.real_download('dest.mp4', info) is False
    assert fd.downloaded_urls == [SEG1]
    assert fd.retries_reported == []
    assert fd.errors_reported == ['giving up after 0 fragment retries']
    assert fd.finished is False


def test_http_error_exhausted_fatal_when_skip_disabled():
    info = make_info_dict([{'url': SEG1}, {'url': SEG2}])
    fd = FakeFD(params={'fragment_retries': 0,
                        'skip_unavailable_fragments': False},
                http_error_urls=(SEG2,))
    assert fd.real_download('dest.mp4', info) is False
    assert fd.errors_reported == ['giving up after 0 fragment retries']
    assert fd.skips_reported == []
    assert fd.finished is False


def test_download_error_nonfatal_skips_fragment():
    info = make_info_dict([{'url': SEG1}, {'url': SEG2}, {'url': SEG3}])
    fd = FakeFD(params={'fragment_retries': 3}, download_error_urls=(SEG2,))
    assert fd.real_download('dest.mp4', info) is True
    # SEG2 attempted once (no retry on DownloadError), then skipped;
    # SEG3 still downloaded
    assert fd.downloaded_urls == [SEG1, SEG2, SEG3]
    assert fd.skips_reported == [2]
    assert fd.retries_reported == []
    assert fd.appended_contents == [SEG1.encode('utf-8'), SEG3.encode('utf-8')]
    assert fd.finished is True
    assert fd.errors_reported == []


def test_download_error_fatal_reraises():
    info = make_info_dict([{'url': SEG1}])
    fd = FakeFD(params={'fragment_retries': 3}, download_error_urls=(SEG1,))
    with pytest.raises(DownloadError):
        fd.real_download('dest.mp4', info)
    assert fd.finished is False
    assert fd.skips_reported == []


def test_resume_skips_already_downloaded_fragments():
    info = make_info_dict([{'url': SEG1}, {'url': SEG2}, {'url': SEG3}])
    fd = FakeFD(fragment_index=1)
    assert fd.real_download('dest.mp4', info) is True
    assert fd.downloaded_urls == [SEG2, SEG3]
    assert fd.appended_contents == [SEG2.encode('utf-8'), SEG3.encode('utf-8')]
    assert fd.finished is True
