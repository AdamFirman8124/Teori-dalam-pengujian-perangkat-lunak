

# Generated at 2026-11-02 20:16:39.775183
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    fd = DashSegmentsFD(None)
    assert fd.FD_NAME == 'dashsegments'

# Generated at 2026-11-02 20:19:09.191447
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest import mock
    from yt_dlp.downloader.dashsegments import DashSegmentsFD
    from yt_dlp.downloader.fragment import FragmentFD
    import yt_dlp.downloader.dashsegments as dash_mod
    import sys

    # Ensure the module can be imported; skip if unavailable in this environment
    if 'yt_dlp.downloader.dashsegments' not in sys.modules:
        import unittest
        raise unittest.SkipTest('yt_dlp.downloader.dashsegments not importable')

    def _make_fd(params=None):
        fd = DashSegmentsFD.__new__(DashSegmentsFD)
        fd.params = params if params is not None else {}
        return fd

    # Case 1: successful download of all fragments
    fd = _make_fd()

# Generated at 2026-11-02 20:22:00.588122
# Unit test for method real_download of class DashSegmentsFD
def test_DashSegmentsFD_real_download():
    from unittest import mock

    def make_fd(params):
        fd = DashSegmentsFD(None, params)
        fd._prepare_and_start_frag_download = mock.Mock(
            side_effect=lambda ctx: ctx.update({'fragment_index': 0}))
        fd._download_fragment = mock.Mock(return_value=(True, b'frag-data'))
        fd._append_fragment = mock.Mock()
        fd._finish_frag_download = mock.Mock()
        fd.report_retry_fragment = mock.Mock()
        fd.report_skip_fragment = mock.Mock()
        fd.report_error = mock.Mock()
        return fd

    info_dict = {
        'fragment_base_url': 'http://example.com/frag/',
        'fragments': [
            {'path': 'seg-1.m4s'},
            {'path': 'seg-2.m4s'},
        ],
    }

    # 1. Successful download of all fragments
    fd = make_fd({})
    assert fd.real_download('video.mp4', info_dict) is True
    fd._download_fragment.assert_has_calls([
        mock.call('http://example.com/frag/seg-1.m4s', info_dict),
        mock.call('http://example.com/frag/seg-2.m4s', info_dict),
    ])
    assert fd._download_fragment.call_count == 2
    assert fd._append_fragment.call_count == 2
    fd._finish_frag_download.assert_called_once()
    assert not fd.report_skip_fragment.called
    assert not fd.report_error.called

    # 2. In test mode only the first fragment is downloaded
    fd = make_fd({'test': True})
    assert fd.real_download('video.mp4', info_dict) is True
    assert fd._download_fragment.call_count == 1
    fd._download_fragment.assert_called_with('http://example.com/frag/seg-1.m4s', info_dict)

    # 3. HTTP errors on fragments are retried
    fd = make_fd({'fragment_retries': 2})
    err = compat_urllib_error.HTTPError(
        'http://example.com/frag/seg-1.m4s', 404, 'Not Found', None, None)
    fd._download_fragment.side_effect = [err, err, (True, b'frag-data')]
    assert fd.real_download('video.mp4', info_dict) is True
    assert fd._download_fragment.call_count == 3
    assert fd.report_retry_fragment.call_count == 2
    fd._finish_frag_download.assert_called_once()

    # 4. Giving up after too many retries on a fatal fragment
    fd = make_fd({'fragment_retries': 1, 'skip_unavailable_fragments': False})
    fd._download_fragment.side_effect = [err, err]
    assert fd.real_download('video.mp4', info_dict) is False
    fd.report_error.assert_called_once_with('giving up after 1 fragment retries')
    assert not fd._finish_frag_download.called

    # 5. Unavailable non-fatal fragments are skipped
    fd = make_fd({})

# Generated at 2026-11-02 20:23:36.565243
# Unit test for constructor of class DashSegmentsFD
def test_DashSegmentsFD():
    '''
    DashSegmentsFD(ydl, params) -> DashSegmentsFD instance
    '''

    class FakeYDL(object):
        params = {}

    params = {'test': False}
    instance = DashSegmentsFD(FakeYDL(), params)
    assert isinstance(instance, DashSegmentsFD)
    assert instance.FD_NAME == 'dashsegments'
    assert instance.params == params