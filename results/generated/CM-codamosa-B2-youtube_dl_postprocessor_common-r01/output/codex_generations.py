

# Generated at 2026-10-25 06:05:53.082790
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

# Generated at 2026-10-25 06:05:55.697336
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-25 06:05:58.114748
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-25 06:06:00.650910
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-25 06:06:03.068675
# Unit test for method run of class PostProcessor

# Generated at 2026-10-25 06:06:05.679027
# Unit test for method run of class PostProcessor

# Generated at 2026-10-25 06:06:08.361729
# Unit test for method run of class PostProcessor

# Generated at 2026-10-25 06:06:10.688073
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 06:06:13.226924
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 06:06:15.647289
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 06:06:18.060197
# Unit test for constructor of class PostProcessor

# Generated at 2026-10-25 06:06:20.706235
# Unit test for constructor of class PostProcessor

# Generated at 2026-10-25 06:06:23.128292
# Unit test for constructor of class PostProcessor

# Generated at 2026-10-25 06:06:24.671591
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

# Generated at 2026-10-25 06:06:26.070459
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

# Generated at 2026-10-25 06:06:27.459817
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

# Generated at 2026-10-25 06:06:28.872429
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

# Generated at 2026-10-25 06:06:30.248066
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

# Generated at 2026-10-25 06:06:31.717488
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

# Generated at 2026-10-25 06:06:33.118186
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

# Generated at 2026-10-25 06:06:34.491563
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

# Generated at 2026-10-25 06:06:35.924973
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

# Generated at 2026-10-25 06:06:37.295839
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

# Generated at 2026-10-25 06:06:38.704327
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

# Generated at 2026-10-25 06:06:40.158682
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

# Generated at 2026-10-25 06:06:41.664430
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

# Generated at 2026-10-25 06:06:43.090767
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

# Generated at 2026-10-25 06:06:44.472893
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

# Generated at 2026-10-25 06:06:45.902492
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

# Generated at 2026-10-25 06:06:47.327940
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

# Generated at 2026-10-25 06:06:49.970531
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:06:52.569383
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:06:54.985772
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:06:57.403556
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:06:59.822622
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:02.242559
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:04.995501
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:07.410312
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:09.825468
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:12.245476
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:14.728722
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:17.143821
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:19.558098
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:22.158677
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:24.575818
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:26.991920
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:29.408079
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:31.826174
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:34.405501
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:36.820809
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:07:52.778296
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 06:07:54.284336
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

# Generated at 2026-10-25 06:07:55.682233
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

# Generated at 2026-10-25 06:07:57.145973
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

# Generated at 2026-10-25 06:07:58.578338
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

# Generated at 2026-10-25 06:07:59.962812
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

# Generated at 2026-10-25 06:08:01.348585
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

# Generated at 2026-10-25 06:08:03.768311
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:06.185781
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:08.599513
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:11.016068
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:13.431443
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:15.847755
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:18.265499
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:20.683988
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:23.098442
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:25.513943
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:27.929081
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:30.344774
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:32.804504
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:35.219810
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:37.633144
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:08:39.076859
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

# Generated at 2026-10-25 06:08:40.522381
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

# Generated at 2026-10-25 06:08:41.892092
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

# Generated at 2026-10-25 06:08:43.256136
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

# Generated at 2026-10-25 06:08:44.628894
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

# Generated at 2026-10-25 06:08:46.119383
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

# Generated at 2026-10-25 06:08:47.486642
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

# Generated at 2026-10-25 06:08:48.890876
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

# Generated at 2026-10-25 06:08:50.301485
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

# Generated at 2026-10-25 06:08:51.711512
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

# Generated at 2026-10-25 06:08:53.157293
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

# Generated at 2026-10-25 06:08:54.577220
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

# Generated at 2026-10-25 06:08:56.010507
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

# Generated at 2026-10-25 06:08:57.443191
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

# Generated at 2026-10-25 06:08:58.878618
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

# Generated at 2026-10-25 06:09:00.738144
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

# Generated at 2026-10-25 06:09:03.381323
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:05.975019
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:08.392310
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:10.808718
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:13.225687
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:15.639190
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:18.053499
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:20.469345
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:22.887499
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:25.303892
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:27.721005
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:30.139792
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:32.553350
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:34.969123
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:37.384538
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:39.800178
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:42.215549
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:44.629833
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:47.047944
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:49.458717
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:51.875088
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:54.293886
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:56.725081
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:09:59.380979
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 06:10:00.781264
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

# Generated at 2026-10-25 06:10:03.202340
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

# Generated at 2026-10-25 06:10:04.620956
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

# Generated at 2026-10-25 06:10:06.012355
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

# Generated at 2026-10-25 06:10:07.504191
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

# Generated at 2026-10-25 06:10:08.869901
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

# Generated at 2026-10-25 06:10:10.369234
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

# Generated at 2026-10-25 06:10:11.912228
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

# Generated at 2026-10-25 06:10:13.314739
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

# Generated at 2026-10-25 06:10:15.967655
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:18.574142
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:20.987665
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:23.402107
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:26.146759
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:28.572023
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:35.315026
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:37.731957
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:40.150140
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:42.568184
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:44.982461
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:47.398014
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:49.812713
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:52.230008
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:54.644048
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:57.058145
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:10:59.474431
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:01.889483
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:04.306254
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:06.799543
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:09.197050
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:11.612462
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:14.027478
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:16.442209
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:18.856343
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:21.428581
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 06:11:22.832730
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

# Generated at 2026-10-25 06:11:24.198350
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

# Generated at 2026-10-25 06:11:25.644592
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

# Generated at 2026-10-25 06:11:36.312002
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

# Generated at 2026-10-25 06:11:38.174653
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

# Generated at 2026-10-25 06:11:39.570451
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

# Generated at 2026-10-25 06:11:41.104232
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

# Generated at 2026-10-25 06:11:42.539254
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

# Generated at 2026-10-25 06:11:43.972173
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

# Generated at 2026-10-25 06:11:45.359030
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

# Generated at 2026-10-25 06:11:47.775685
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:50.190426
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:52.605671
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:55.021215
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:11:57.438015
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:00.014404
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:02.428435
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:04.843116
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:07.258345
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:27.730401
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

# Generated at 2026-10-25 06:12:29.108495
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

# Generated at 2026-10-25 06:12:31.524282
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:34.012649
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:36.432135
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:38.850402
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:41.301488
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:43.718473
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:46.135431
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:48.575596
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:50.984434
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:53.399448
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:55.813136
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:12:58.226637
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:13:00.640704
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:13:03.055881
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:13:05.470337
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:13:07.885367
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:13:10.300970
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:13:12.715099
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:13:15.130820
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:13:17.821219
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 06:13:19.228033
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

# Generated at 2026-10-25 06:14:00.802352
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:03.217277
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:05.632522
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:08.058213
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:10.472053
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:12.887869
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:15.304648
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:17.719879
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:20.134920
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:22.550619
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:24.966433
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:27.381313
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:29.802677
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:32.214352
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:34.631237
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:37.049045
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:14:58.125387
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 06:14:59.498057
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

# Generated at 2026-10-25 06:15:02.232243
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:15:04.744924
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:15:07.138898
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:15:09.553551
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:15:12.054082
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:15:14.433489
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:15:16.851967
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:15:19.266848
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 06:15:21.719282
# Unit test for method try_utime of class PostProcessor