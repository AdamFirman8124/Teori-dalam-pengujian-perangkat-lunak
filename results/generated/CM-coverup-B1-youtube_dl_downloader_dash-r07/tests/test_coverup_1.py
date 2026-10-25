# file: project/youtube_dl/downloader/dash.py:18-80
# asked: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}
# gained: {"lines": [19, 20, 21, 23, 24, 25, 28, 30, 31, 33, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 61, 62, 63, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 78, 80], "branches": [[34, 35], [34, 78], [36, 37], [36, 40], [42, 43], [42, 71], [45, 46], [45, 48], [49, 50], [49, 51], [61, 42], [61, 62], [66, 67], [66, 69], [71, 34], [71, 72], [72, 73], [72, 75]]}

import pytest

from youtube_dl.compat import compat_urllib_error
from youtube_dl.downloader.dash import DashSegmentsFD
from youtube_dl.utils import DownloadError


@pytest.fixture
def make_downloader(monkeypatch):
    def factory(params=None, fragment_index=0):
        downloader = object.__new__(DashSegmentsFD)
        downloader.params = dict(params or {})
        events = {
            'prepared': [],
            'downloads': [],
            'appended': [],
            'finished': [],
            'retries': [],
            'skipped': [],
            'errors': [],
        }

        def prepare(ctx):
            ctx['fragment_index'] = fragment_index
            events['prepared'].append(dict(ctx))

        def download(ctx, url, info_dict):
            events['downloads'].append(url)
            return True, url.encode('utf-8')

        monkeypatch.setattr(
            downloader, '_prepare_and_start_frag_download', prepare)
        monkeypatch.setattr(downloader, '_download_fragment', download)
        monkeypatch.setattr(
            downloader, '_append_fragment',
            lambda ctx, content: events['appended'].append(content))
        monkeypatch.setattr(
            downloader, '_finish_frag_download',
            lambda ctx: events['finished'].append(dict(ctx)))
        monkeypatch.setattr(
            downloader, 'report_retry_fragment',
            lambda err, index, count, retries:
                events['retries'].append((err, index, count, retries)))
        monkeypatch.setattr(
            downloader, 'report_skip_fragment',
            lambda index: events['skipped'].append(index))
        monkeypatch.setattr(
            downloader, 'report_error',
            lambda message: events['errors'].append(message))

        return downloader, events

    return factory


def test_real_download_uses_base_url_and_limits_fragments_in_test_mode(
        make_downloader):
    downloader, events = make_downloader({'test': True})
    info_dict = {
        'fragment_base_url': 'https://example.test/media/',
        'fragments': [
            {'path': 'init.m4s'},
            {'path': 'segment-1.m4s'},
        ],
    }

    result = downloader.real_download('video.mp4', info_dict)

    assert result is True
    assert events['prepared'] == [{
        'filename': 'video.mp4',
        'total_frags': 1,
        'fragment_index': 0,
    }]
    assert events['downloads'] == [
        'https://example.test/media/init.m4s',
    ]
    assert events['appended'] == [
        b'https://example.test/media/init.m4s',
    ]
    assert events['finished'] == [{
        'filename': 'video.mp4',
        'total_frags': 1,
        'fragment_index': 0,
    }]


def test_real_download_skips_already_downloaded_fragments(make_downloader):
    downloader, events = make_downloader(fragment_index=1)
    info_dict = {
        'fragments': [
            {'url': 'https://example.test/segment-1.m4s'},
            {'url': 'https://example.test/segment-2.m4s'},
        ],
    }

    result = downloader.real_download('video.mp4', info_dict)

    assert result is True
    assert events['downloads'] == [
        'https://example.test/segment-2.m4s',
    ]
    assert events['appended'] == [
        b'https://example.test/segment-2.m4s',
    ]
    assert len(events['finished']) == 1


def test_real_download_returns_false_when_fragment_download_is_unsuccessful(
        make_downloader, monkeypatch):
    downloader, events = make_downloader()

    def unsuccessful_download(ctx, url, info_dict):
        events['downloads'].append(url)
        return False, None

    monkeypatch.setattr(
        downloader, '_download_fragment', unsuccessful_download)

    result = downloader.real_download(
        'video.mp4',
        {'fragments': [{'url': 'https://example.test/init.m4s'}]},
    )

    assert result is False
    assert events['downloads'] == ['https://example.test/init.m4s']
    assert events['appended'] == []
    assert events['finished'] == []


def test_real_download_retries_http_error_and_then_succeeds(
        make_downloader, monkeypatch):
    downloader, events = make_downloader({'fragment_retries': 1})
    http_error = compat_urllib_error.HTTPError(
        'https://example.test/init.m4s', 503, 'Unavailable', {}, None)
    attempts = 0

    def flaky_download(ctx, url, info_dict):
        nonlocal attempts
        attempts += 1
        events['downloads'].append(url)
        if attempts == 1:
            raise http_error
        return True, b'fragment-data'

    monkeypatch.setattr(downloader, '_download_fragment', flaky_download)

    result = downloader.real_download(
        'video.mp4',
        {'fragments': [{'url': 'https://example.test/init.m4s'}]},
    )

    assert result is True
    assert attempts == 2
    assert events['retries'] == [(http_error, 1, 1, 1)]
    assert events['appended'] == [b'fragment-data']
    assert len(events['finished']) == 1
    assert events['errors'] == []


def test_real_download_gives_up_when_first_fragment_exhausts_http_retries(
        make_downloader, monkeypatch):
    downloader, events = make_downloader({'fragment_retries': 0})
    http_error = compat_urllib_error.HTTPError(
        'https://example.test/init.m4s', 404, 'Not Found', {}, None)

    def failing_download(ctx, url, info_dict):
        events['downloads'].append(url)
        raise http_error

    monkeypatch.setattr(downloader, '_download_fragment', failing_download)

    result = downloader.real_download(
        'video.mp4',
        {'fragments': [{'url': 'https://example.test/init.m4s'}]},
    )

    assert result is False
    assert events['retries'] == []
    assert events['skipped'] == []
    assert events['errors'] == ['giving up after 0 fragment retries']
    assert events['finished'] == []


def test_real_download_skips_nonfatal_fragment_after_http_retries(
        make_downloader, monkeypatch):
    downloader, events = make_downloader({'fragment_retries': 1})
    failing_url = 'https://example.test/segment-1.m4s'
    http_error = compat_urllib_error.HTTPError(
        failing_url, 404, 'Not Found', {}, None)
    failed_attempts = 0

    def download(ctx, url, info_dict):
        nonlocal failed_attempts
        events['downloads'].append(url)
        if url == failing_url:
            failed_attempts += 1
            raise http_error
        return True, url.encode('utf-8')

    monkeypatch.setattr(downloader, '_download_fragment', download)

    result = downloader.real_download(
        'video.mp4',
        {
            'fragments': [
                {'url': 'https://example.test/init.m4s'},
                {'url': failing_url},
                {'url': 'https://example.test/segment-2.m4s'},
            ],
        },
    )

    assert result is True
    assert failed_attempts == 2
    assert events['retries'] == [(http_error, 2, 1, 1)]
    assert events['skipped'] == [2]
    assert events['appended'] == [
        b'https://example.test/init.m4s',
        b'https://example.test/segment-2.m4s',
    ]
    assert len(events['finished']) == 1
    assert events['errors'] == []


def test_real_download_skips_nonfatal_download_error(
        make_downloader, monkeypatch):
    downloader, events = make_downloader()
    failing_url = 'https://example.test/segment-1.m4s'

    def download(ctx, url, info_dict):
        events['downloads'].append(url)
        if url == failing_url:
            raise DownloadError('fragment download failed')
        return True, b'init-data'

    monkeypatch.setattr(downloader, '_download_fragment', download)

    result = downloader.real_download(
        'video.mp4',
        {
            'fragments': [
                {'url': 'https://example.test/init.m4s'},
                {'url': failing_url},
            ],
        },
    )

    assert result is True
    assert events['skipped'] == [2]
    assert events['appended'] == [b'init-data']
    assert len(events['finished']) == 1
    assert events['errors'] == []


def test_real_download_reraises_download_error_for_first_fragment(
        make_downloader, monkeypatch):
    downloader, events = make_downloader()
    error = DownloadError('initialization fragment failed')

    def failing_download(ctx, url, info_dict):
        raise error

    monkeypatch.setattr(downloader, '_download_fragment', failing_download)

    with pytest.raises(DownloadError) as exc_info:
        downloader.real_download(
            'video.mp4',
            {'fragments': [{'url': 'https://example.test/init.m4s'}]},
        )

    assert exc_info.value is error
    assert events['skipped'] == []
    assert events['finished'] == []


def test_real_download_reraises_later_download_error_when_skipping_disabled(
        make_downloader, monkeypatch):
    downloader, events = make_downloader({
        'skip_unavailable_fragments': False,
    })
    failing_url = 'https://example.test/segment-1.m4s'
    error = DownloadError('required media fragment failed')

    def download(ctx, url, info_dict):
        events['downloads'].append(url)
        if url == failing_url:
            raise error
        return True, b'init-data'

    monkeypatch.setattr(downloader, '_download_fragment', download)

    with pytest.raises(DownloadError) as exc_info:
        downloader.real_download(
            'video.mp4',
            {
                'fragments': [
                    {'url': 'https://example.test/init.m4s'},
                    {'url': failing_url},
                ],
            },
        )

    assert exc_info.value is error
    assert events['appended'] == [b'init-data']
    assert events['skipped'] == []
    assert events['finished'] == []


def test_real_download_requires_base_url_for_relative_fragment(
        make_downloader):
    downloader, events = make_downloader()

    with pytest.raises(AssertionError):
        downloader.real_download(
            'video.mp4',
            {'fragments': [{'path': 'init.m4s'}]},
        )

    assert events['downloads'] == []
    assert events['appended'] == []
    assert events['finished'] == []
