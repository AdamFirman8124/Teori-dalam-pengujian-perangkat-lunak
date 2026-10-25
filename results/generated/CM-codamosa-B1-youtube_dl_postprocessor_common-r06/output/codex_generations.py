

# Generated at 2026-10-25 02:54:34.112146
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:54:36.528041
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:54:38.943003
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:54:41.358352
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 02:54:43.772708
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 02:54:50.052292
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    err = AudioConversionError('conversion failed: no encoder')
    assert isinstance(err, PostProcessingError)
    assert isinstance(err, Exception)
    assert str(err) == 'conversion failed: no encoder'
    assert err.args == ('conversion failed: no encoder',)

# Generated at 2026-10-25 02:54:55.243318
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    downloader = object()

    post_processor = PostProcessor(downloader)
    assert post_processor._downloader is downloader

    post_processor_without_downloader = PostProcessor()
    assert post_processor_without_downloader._downloader is None

# Generated at 2026-10-25 02:55:00.377968
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    downloader = object()

    post_processor = PostProcessor(downloader)

    assert post_processor._downloader is downloader

    default_post_processor = PostProcessor()

    assert default_post_processor._downloader is None

# Generated at 2026-10-25 02:55:05.485129
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    # Default downloader
    post_processor = PostProcessor()
    assert post_processor._downloader is None

    # Explicit downloader
    downloader = object()
    post_processor = PostProcessor(downloader)
    assert post_processor._downloader is downloader

# Generated at 2026-10-25 02:55:07.234866
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

# Generated at 2026-10-25 02:55:08.602073
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

# Generated at 2026-10-25 02:55:09.988082
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

# Generated at 2026-10-25 02:55:11.421917
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

# Generated at 2026-10-25 02:55:12.966771
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

# Generated at 2026-10-25 02:55:14.391166
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

# Generated at 2026-10-25 02:55:15.825834
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

# Generated at 2026-10-25 02:55:17.261786
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

# Generated at 2026-10-25 02:55:18.698085
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

# Generated at 2026-10-25 02:55:20.130821
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

# Generated at 2026-10-25 02:55:21.561773
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

# Generated at 2026-10-25 02:55:23.095662
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

# Generated at 2026-10-25 02:55:25.514612
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:27.928352
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:30.574578
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:33.102028
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:35.520352
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:37.936479
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:40.470648
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:42.887853
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:45.304604
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:47.720098
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:55:58.424107
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 02:55:59.791589
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

# Generated at 2026-10-25 02:56:01.189299
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

# Generated at 2026-10-25 02:56:02.622296
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

# Generated at 2026-10-25 02:56:04.055970
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

# Generated at 2026-10-25 02:56:05.489817
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

# Generated at 2026-10-25 02:56:06.922817
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

# Generated at 2026-10-25 02:56:08.359072
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

# Generated at 2026-10-25 02:56:09.790318
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

# Generated at 2026-10-25 02:56:11.326056
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

# Generated at 2026-10-25 02:56:12.760144
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

# Generated at 2026-10-25 02:56:14.130427
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

# Generated at 2026-10-25 02:56:15.524142
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

# Generated at 2026-10-25 02:56:16.923983
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

# Generated at 2026-10-25 02:56:18.391881
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

# Generated at 2026-10-25 02:56:20.809202
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:23.329541
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:25.743050
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:28.158616
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:30.572820
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:32.988661
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:35.403233
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:37.818203
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:40.234114
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:42.649546
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:45.321912
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:47.740450
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:50.156802
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:52.571108
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:54.986054
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:57.401062
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:56:59.817434
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:02.235439
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:04.649991
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:07.064213
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:09.476553
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:11.893536
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:14.307184
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:16.721985
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:18.172841
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

# Generated at 2026-10-25 02:57:19.629175
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

# Generated at 2026-10-25 02:57:21.377037
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

# Generated at 2026-10-25 02:57:22.785691
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

# Generated at 2026-10-25 02:57:24.235305
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

# Generated at 2026-10-25 02:57:25.680879
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

# Generated at 2026-10-25 02:57:27.104660
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

# Generated at 2026-10-25 02:57:28.536561
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

# Generated at 2026-10-25 02:57:29.969920
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

# Generated at 2026-10-25 02:57:31.334856
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

# Generated at 2026-10-25 02:57:32.734593
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

# Generated at 2026-10-25 02:57:34.258240
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

# Generated at 2026-10-25 02:57:36.011866
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

# Generated at 2026-10-25 02:57:37.447513
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

# Generated at 2026-10-25 02:57:38.878747
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

# Generated at 2026-10-25 02:57:40.248404
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

# Generated at 2026-10-25 02:57:43.004750
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:45.420977
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:47.836574
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:50.255175
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:52.823828
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:55.240377
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:57:57.656388
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:00.094919
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:02.492086
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:04.909550
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:07.323715
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:09.741920
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:12.158775
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:14.574191
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:16.994481
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:19.408822
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:21.823981
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:24.239058
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:28.210043
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:30.626907
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:33.041401
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:35.457970
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:37.876097
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:40.293573
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:42.711136
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:45.127174
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:47.541775
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:49.958977
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:52.373998
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:54.790134
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:58:56.221459
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

# Generated at 2026-10-25 02:58:57.636962
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

# Generated at 2026-10-25 02:58:59.058900
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

# Generated at 2026-10-25 02:59:00.475637
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

# Generated at 2026-10-25 02:59:01.911075
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

# Generated at 2026-10-25 02:59:03.271918
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

# Generated at 2026-10-25 02:59:12.380437
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

# Generated at 2026-10-25 02:59:13.803684
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

# Generated at 2026-10-25 02:59:15.237264
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

# Generated at 2026-10-25 02:59:16.664116
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

# Generated at 2026-10-25 02:59:18.041715
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

# Generated at 2026-10-25 02:59:20.462331
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:22.876849
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:25.433660
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:27.848916
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:30.262825
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:32.676978
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:35.091486
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:37.506017
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:39.920531
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:42.334927
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:44.750096
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:47.164030
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:49.578504
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:51.993870
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:59:54.407701
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:10.518445
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:12.931989
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:15.347521
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:17.763190
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:20.184328
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:22.598836
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:25.013911
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:27.428983
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:29.844414
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:32.258051
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:34.673298
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:37.088454
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:39.502505
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:41.917262
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:44.332050
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:46.747500
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:49.162883
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:51.577909
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:00:53.209635
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

# Generated at 2026-10-25 03:00:54.623879
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

# Generated at 2026-10-25 03:00:56.042009
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

# Generated at 2026-10-25 03:00:57.433084
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

# Generated at 2026-10-25 03:01:28.391436
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:30.805098
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:33.219725
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:35.749919
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:38.163656
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:40.577745
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:42.991715
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:45.404179
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:47.816406
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:50.230606
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:52.655151
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:55.067365
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:57.481339
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:01:59.894127
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:02.306444
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:04.719674
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:07.135754
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:09.549977
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:11.964250
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:14.380746
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:16.793439
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:19.207344
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:21.621861
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:24.035873
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:26.450581
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:28.867554
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:31.283483
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:33.700052
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:36.114837
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:02:38.529061
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:38.144034
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:40.558753
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:42.973127
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:45.388102
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:47.803755
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:50.218093
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:52.633832
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:55.050689
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:57.466164
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 03:03:58.901006
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

# Generated at 2026-10-25 03:04:00.320788
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

# Generated at 2026-10-25 03:04:01.754102
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

# Generated at 2026-10-25 03:04:03.152976
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

# Generated at 2026-10-25 03:04:04.621145
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

# Generated at 2026-10-25 03:04:06.100844
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

# Generated at 2026-10-25 03:04:07.500827
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