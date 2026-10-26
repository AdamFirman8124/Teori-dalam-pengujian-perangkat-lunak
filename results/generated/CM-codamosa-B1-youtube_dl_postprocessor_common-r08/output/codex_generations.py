

# Generated at 2026-10-25 10:17:33.022955
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:18:01.489765
# Unit test for method run of class PostProcessor
def test_PostProcessor_run():
    pp = PostProcessor()
    information = {
        'filepath': '/tmp/video.mp4',
        'title': 'test video',
        'ext': 'mp4',
    }

    # Should return a tuple of (deletable_files, updated_info)
    result = pp.run(information)

    assert isinstance(result, tuple)
    assert len(result) == 2

    deletable, new_info = result

    # By default: keep file and do nothing
    assert deletable == []
    assert isinstance(deletable, list)
    assert new_info == information

    # Empty dict should pass through unchanged
    deletable_empty, new_empty = pp.run({})
    assert deletable_empty == []
    assert new_empty == {}

    # Each call should return a fresh list, not shared state
    deletable2, _ = pp.run(information)
    assert deletable2 == []
    assert deletable is not deletable2

# Generated at 2026-10-25 10:18:18.073786
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:18:27.807406
# Unit test for method set_downloader of class PostProcessor
def test_PostProcessor_set_downloader():
    # initially None
    pp = PostProcessor()
    assert pp._downloader is None

    # sets downloader
    downloader1 = object()
    pp.set_downloader(downloader1)
    assert pp._downloader is downloader1

    # overwrites previous downloader
    downloader2 = object()
    pp.set_downloader(downloader2)
    assert pp._downloader is downloader2

    # can reset to None
    pp.set_downloader(None)
    assert pp._downloader is None

    # overwrites downloader set via __init__
    pp2 = PostProcessor(downloader=downloader1)
    assert pp2._downloader is downloader1
    pp2.set_downloader(downloader2)
    assert pp2._downloader is downloader2

# Generated at 2026-10-25 10:18:29.238625
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:18:49.035099
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:18:50.780069
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:19:07.336167
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:19:23.824968
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:19:41.022490
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:19:43.438635
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:19:45.852732
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:19:48.267308
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:19:50.682612
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:19:53.096657
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:19:55.510720
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:20:12.665532
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:20:39.287946
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:20:46.851826
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:21:09.803610
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:21:11.239183
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:21:27.722756
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:21:29.140155
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:21:45.745260
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:21:48.161464
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:21:50.573730
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:21:52.988096
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:21:55.401165
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:21:57.817153
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:22:00.238124
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:22:02.651325
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:22:05.303803
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 10:22:21.894588
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:22:24.870963
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:22:41.452073
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:22:42.987684
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:22:44.421081
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:22:45.854722
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:22:51.486956
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:22:53.025765
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:23:22.823357
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:23:39.514396
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:23:41.048336
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:23:42.626766
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:23:44.019012
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:23:45.554168
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:23:46.987937
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:23:48.351199
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:23:49.866314
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:23:52.928258
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:23:55.571771
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:23:58.215334
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:00.628300
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:03.047427
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:05.458682
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:07.878159
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:10.294293
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:12.709288
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:15.121502
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:17.537641
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:19.959073
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:22.373679
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:24.789287
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:27.203748
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:29.618022
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:32.033875
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:34.447263
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:36.860635
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:39.279644
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:40.643488
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:24:57.113191
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:24:58.452473
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:25:01.346323
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:02.878301
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:25:17.922190
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:25:20.340852
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:22.756751
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:25.171725
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:27.586090
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:29.999311
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:32.414394
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:34.828385
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:37.436159
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:39.852239
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:42.264996
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:25:45.118594
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 10:26:12.501205
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:26:13.835302
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:26:36.906248
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:26:39.318641
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:26:41.732898
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:26:44.201045
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:26:46.638561
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:26:49.046471
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:26:50.444115
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:26:51.809287
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:26:53.160552
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:26:54.584752
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:26:56.005284
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:26:57.420568
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import MagicMock, patch
    import tempfile

    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)

    # 1. Success case: updates atime/mtime, no warning
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tmp_path = tf.name
    try:
        atime, mtime = 1000000000, 1200000000
        pp.try_utime(tmp_path, atime, mtime)

        st = os.stat(tmp_path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        mock_downloader.report_warning.assert_not_called()
    finally:
        os.unlink(tmp_path)

    # 2. Failure case: os.utime raises -> report_warning with custom note
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0, errnote='custom warning')
        mock_downloader.report_warning.assert_called_once_with('custom warning')

    # 3. Failure case: default errnote
    mock_downloader.reset_mock()
    with patch('os.utime', side_effect=OSError('mock utime failure')):
        pp.try_utime('any/path', 0, 0)
        mock_downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-10-25 10:27:00.626366
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:27:02.061684
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:27:20.065126
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:27:21.405165
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-25 10:27:39.027514
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:27:41.444834
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 10:27:44.047521
# Unit test for method try_utime of class PostProcessor