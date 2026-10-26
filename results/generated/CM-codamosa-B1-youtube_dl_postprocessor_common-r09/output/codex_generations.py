

# Generated at 2026-10-25 07:34:54.471361
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-25 07:34:56.994566
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-25 07:34:59.410456
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-25 07:35:01.825153
# Unit test for constructor of class PostProcessor

# Generated at 2026-10-25 07:35:04.487325
# Unit test for constructor of class PostProcessor

# Generated at 2026-10-25 07:35:06.914772
# Unit test for constructor of class PostProcessor

# Generated at 2026-10-25 07:35:09.444898
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 07:35:11.850544
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 07:35:14.266371
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 07:35:16.680707
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 07:35:19.097838
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 07:35:21.513723
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-25 07:35:23.928269
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:26.342640
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:28.759368
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:31.177261
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:33.594236
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:36.008383
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:38.428762
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:40.843715
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:43.255376
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:45.672644
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:48.087987
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:50.501980
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:52.916690
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:55.336985
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:35:57.754342
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:00.175409
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:02.592110
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:05.009788
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:07.435911
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:09.860423
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:12.289301
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:14.706795
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:17.136417
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:19.553219
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:21.970391
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:24.384883
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:26.799264
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:29.217540
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:31.633173
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:34.048399
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:36.464713
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:38.878289
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:41.291237
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:43.708142
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:46.126204
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:48.542154
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:51.022291
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:53.437473
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:55.853155
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:36:58.267211
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:00.681942
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:03.099587
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:05.515785
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:07.929995
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:10.345586
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:11.850205
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

# Generated at 2026-10-25 07:37:13.312798
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

# Generated at 2026-10-25 07:37:14.783764
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

# Generated at 2026-10-25 07:37:16.281902
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

# Generated at 2026-10-25 07:37:17.697931
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

# Generated at 2026-10-25 07:37:19.149035
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

# Generated at 2026-10-25 07:37:20.787283
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

# Generated at 2026-10-25 07:37:22.215628
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

# Generated at 2026-10-25 07:37:23.606223
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

# Generated at 2026-10-25 07:37:25.021195
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

# Generated at 2026-10-25 07:37:26.531673
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

# Generated at 2026-10-25 07:37:27.887455
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

# Generated at 2026-10-25 07:37:29.407445
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

# Generated at 2026-10-25 07:37:30.926452
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

# Generated at 2026-10-25 07:37:32.462024
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

# Generated at 2026-10-25 07:37:33.895005
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

# Generated at 2026-10-25 07:37:35.330169
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

# Generated at 2026-10-25 07:37:36.763965
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

# Generated at 2026-10-25 07:37:39.188926
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:41.603223
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:44.148332
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:46.565388
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:48.978456
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:51.396590
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:53.814866
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:56.255705
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:37:58.681741
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:01.102716
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:03.518066
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:05.931313
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:08.350069
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:10.799554
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:13.183858
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:15.598948
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:18.541341
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 07:38:20.077775
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

# Generated at 2026-10-25 07:38:21.507103
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

# Generated at 2026-10-25 07:38:23.050243
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

# Generated at 2026-10-25 07:38:24.426676
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

# Generated at 2026-10-25 07:38:25.916577
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

# Generated at 2026-10-25 07:38:27.294770
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

# Generated at 2026-10-25 07:38:28.664603
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

# Generated at 2026-10-25 07:38:30.038319
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

# Generated at 2026-10-25 07:38:31.413746
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

# Generated at 2026-10-25 07:38:32.784147
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

# Generated at 2026-10-25 07:38:34.159189
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

# Generated at 2026-10-25 07:38:36.709204
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:39.241810
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:41.654217
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:44.137256
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:46.556324
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:49.053614
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:51.465890
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:53.894855
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:56.311036
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:38:58.736078
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:01.200864
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:03.618318
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:06.030540
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:08.444020
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:10.860723
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:13.276694
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:15.690947
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:18.105158
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:20.522992
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:22.940543
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:25.356652
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:27.771266
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:30.185326
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:32.809109
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 07:39:34.216367
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

# Generated at 2026-10-25 07:39:35.651647
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

# Generated at 2026-10-25 07:39:37.082773
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

# Generated at 2026-10-25 07:39:39.336326
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

# Generated at 2026-10-25 07:39:40.768200
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

# Generated at 2026-10-25 07:39:42.305937
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

# Generated at 2026-10-25 07:39:43.683400
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

# Generated at 2026-10-25 07:39:45.070896
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

# Generated at 2026-10-25 07:39:46.506277
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

# Generated at 2026-10-25 07:39:47.936845
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

# Generated at 2026-10-25 07:39:49.372120
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

# Generated at 2026-10-25 07:39:50.829887
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

# Generated at 2026-10-25 07:39:53.226357
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:55.640149
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:39:58.057589
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:02.877043
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:05.292533
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:07.707289
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:10.126557
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:12.533609
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:15.152586
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:17.565812
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:19.980165
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:22.571025
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:24.986774
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:27.400698
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:29.814867
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:32.228831
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:34.643314
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:37.056008
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:39.469363
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:41.885524
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:44.298490
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:46.710442
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:49.125823
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:51.537502
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:53.952217
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:56.365644
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:40:58.782672
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:01.210126
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:03.627515
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:06.037474
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:08.452893
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:10.866005
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:13.278978
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:21.116271
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:23.528918
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:25.946303
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:28.481278
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:30.891748
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:33.305492
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:35.719047
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:38.134129
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:40.547407
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:42.961744
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:45.376889
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:47.790213
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:50.203444
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:52.621890
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:55.032782
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:57.445616
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:41:59.859554
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:02.275223
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:04.688750
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:07.103000
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:09.518781
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:11.929463
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:14.344764
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:16.757953
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:19.172470
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:21.587124
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:24.079651
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:26.492106
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:28.905891
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:31.322102
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:46.164982
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:48.578622
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:50.993466
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:53.406683
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:55.818134
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:42:58.232837
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:00.647722
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:03.062793
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:05.477496
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:07.890324
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:10.306530
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:12.719944
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:15.136042
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:17.552943
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:19.968328
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:22.382805
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:24.800679
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:27.272374
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:29.661588
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:32.075553
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:34.489198
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:36.903690
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:39.318283
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:41.731628
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:44.144993
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:46.558949
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:48.974763
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:51.387852
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:53.802229
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:43:56.216116
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:44:24.760963
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:44:27.175507
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:44:29.590912
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:44:32.003264
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:44:34.417127
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:44:36.830939
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 07:44:44.596158
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from youtube_dl.postprocessor.common import PostProcessor

    class FakeDownloader(object):
        def __init__(self):
            self.warnings = []

        def report_warning(self, message):
            self.warnings.append(message)

    # --- success case: utime is applied to the file ---
    tmpfile = tempfile.NamedTemporaryFile(delete=False)
    tmpfile.close()
    path = tmpfile.name

    try:
        downloader = FakeDownloader()
        pp = PostProcessor(downloader)

        atime = 1000000000.0
        mtime = 1100000000.0

        pp.try_utime(path, atime, mtime)

        stat = os.stat(encodeFilename(path))
        assert int(stat.st_atime) == int(atime), 'atime not updated: %r' % stat.st_atime
        assert int(stat.st_mtime) == int(mtime), 'mtime not updated: %r' % stat.st_mtime

        # no warning should have been reported on success
        assert downloader.warnings == [], 'unexpected warnings: %r' % downloader.warnings

        # default errnote is used when os.utime fails
        pp_with_failure = PostProcessor(downloader)

        def raise_oserror(path, times):
            raise OSError('utime failed')

        real_utime = os.utime
        try:
            os.utime = raise_oserror
            pp_with_failure.try_utime(path, atime, mtime)
        finally:
            os.utime = real_utime

        # failure is swallowed and reported as a warning, not raised
        assert len(downloader.warnings) == 1, 'expected one warning, got: %r' % downloader.warnings
        assert downloader.warnings[0] == 'Cannot update utime of file'

        # custom errnote is used when provided
        downloader.warnings = []
        real_utime = os.utime
        try:
            os.utime = raise_oserror
            pp_with_failure.try_utime(path, atime, mtime, errnote='Custom utime error')
        finally:
            os.utime = real_utime

        assert downloader.warnings == ['Custom utime error'], 'unexpected warnings: %r' % downloader.warnings
    finally:
        try:
            os.remove(path)
        except OSError:
            pass

# Generated at 2026-10-25 07:44:45.970180
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

# Generated at 2026-10-25 07:44:47.352748
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

# Generated at 2026-10-25 07:44:48.774410
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

# Generated at 2026-10-25 07:44:50.211022
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

# Generated at 2026-10-25 07:44:51.641546
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

# Generated at 2026-10-25 07:44:53.079099
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

# Generated at 2026-10-25 07:44:54.509694
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