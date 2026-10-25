

# Generated at 2026-10-25 02:27:15.639885
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    message = 'Audio conversion failed'

    error = AudioConversionError(message)

    assert isinstance(error, AudioConversionError)
    assert isinstance(error, PostProcessingError)
    assert error.args == (message,)
    assert str(error) == message

# Generated at 2026-10-25 02:27:20.246966
# Unit test for method set_downloader of class PostProcessor
def test_PostProcessor_set_downloader():
    initial_downloader = object()
    new_downloader = object()
    post_processor = PostProcessor(initial_downloader)

    result = post_processor.set_downloader(new_downloader)

    assert result is None
    assert post_processor._downloader is new_downloader

# Generated at 2026-10-25 02:27:24.752489
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    # Constructor without a downloader
    post_processor = PostProcessor()
    assert post_processor._downloader is None

    # Constructor with a downloader
    downloader = object()
    post_processor = PostProcessor(downloader)
    assert post_processor._downloader is downloader

# Generated at 2026-10-25 02:27:29.416501
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    message = 'Audio conversion failed'

    error = AudioConversionError(message)

    assert isinstance(error, AudioConversionError)
    assert isinstance(error, PostProcessingError)
    assert str(error) == message
    assert error.args == (message,)

# Generated at 2026-10-25 02:27:34.593951
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    # Constructor without a downloader
    post_processor = PostProcessor()
    assert post_processor._downloader is None

    # Constructor with a downloader
    downloader = object()
    post_processor = PostProcessor(downloader)
    assert post_processor._downloader is downloader

# Generated at 2026-10-25 02:27:37.130937
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:27:39.778076
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:27:42.204099
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:27:57.340895
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

# Generated at 2026-10-25 02:27:58.752548
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

# Generated at 2026-10-25 02:28:00.189638
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

# Generated at 2026-10-25 02:28:01.629813
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

# Generated at 2026-10-25 02:28:03.062929
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

# Generated at 2026-10-25 02:28:04.600316
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

# Generated at 2026-10-25 02:28:06.134400
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

# Generated at 2026-10-25 02:28:07.670095
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

# Generated at 2026-10-25 02:28:09.207797
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

# Generated at 2026-10-25 02:28:10.741978
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

# Generated at 2026-10-25 02:28:12.174795
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

# Generated at 2026-10-25 02:28:13.612100
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

# Generated at 2026-10-25 02:28:15.033641
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

# Generated at 2026-10-25 02:28:16.407172
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

# Generated at 2026-10-25 02:28:17.793402
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

# Generated at 2026-10-25 02:28:19.228789
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

# Generated at 2026-10-25 02:28:20.674389
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

# Generated at 2026-10-25 02:28:22.110886
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

# Generated at 2026-10-25 02:28:23.544321
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

# Generated at 2026-10-25 02:28:26.071479
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:28:28.641470
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:28:31.177008
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:28:33.591871
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:28:36.006348
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:28:38.421301
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:28:40.846647
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:28:43.263722
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:28:55.179098
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():from unittest import mock

# Generated at 2026-10-25 02:28:56.607439
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

# Generated at 2026-10-25 02:28:58.040983
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

# Generated at 2026-10-25 02:28:59.419257
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

# Generated at 2026-10-25 02:29:00.824467
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

# Generated at 2026-10-25 02:29:02.242211
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

# Generated at 2026-10-25 02:29:03.676367
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

# Generated at 2026-10-25 02:29:05.104212
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

# Generated at 2026-10-25 02:29:06.540267
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

# Generated at 2026-10-25 02:29:07.973478
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

# Generated at 2026-10-25 02:29:09.405173
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

# Generated at 2026-10-25 02:29:10.839080
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

# Generated at 2026-10-25 02:29:12.375838
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

# Generated at 2026-10-25 02:29:13.738886
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

# Generated at 2026-10-25 02:29:15.140360
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

# Generated at 2026-10-25 02:29:16.573789
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

# Generated at 2026-10-25 02:29:18.007314
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

# Generated at 2026-10-25 02:29:20.772066
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

# Generated at 2026-10-25 02:29:23.190419
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:25.706758
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:28.237212
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:30.772655
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:33.187206
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:35.603653
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:38.017557
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:40.433963
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:42.849362
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:45.267446
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:47.683631
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:50.098472
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:52.513661
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:54.940561
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:57.369410
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:29:59.786753
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:01.324064
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 02:30:02.757715
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

# Generated at 2026-10-25 02:30:04.192853
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

# Generated at 2026-10-25 02:30:05.626495
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

# Generated at 2026-10-25 02:30:07.067683
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

# Generated at 2026-10-25 02:30:08.491971
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

# Generated at 2026-10-25 02:30:09.926786
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

# Generated at 2026-10-25 02:30:11.462027
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

# Generated at 2026-10-25 02:30:12.901898
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

# Generated at 2026-10-25 02:30:14.328285
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

# Generated at 2026-10-25 02:30:15.709644
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

# Generated at 2026-10-25 02:30:17.196530
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

# Generated at 2026-10-25 02:30:18.558951
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

# Generated at 2026-10-25 02:30:19.960196
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

# Generated at 2026-10-25 02:30:21.378377
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

# Generated at 2026-10-25 02:30:23.748116
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

# Generated at 2026-10-25 02:30:25.181401
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

# Generated at 2026-10-25 02:30:26.626968
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

# Generated at 2026-10-25 02:30:28.048553
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

# Generated at 2026-10-25 02:30:29.411664
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

# Generated at 2026-10-25 02:30:31.954751
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:34.507082
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:36.932810
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:39.347852
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:41.764520
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:44.380138
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:46.797549
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:49.210784
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:51.780415
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:54.195318
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:56.610774
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:30:59.026361
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:01.441713
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:03.857418
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:06.272950
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:11.250672
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:13.664072
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:16.078596
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:18.493737
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:20.908504
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:23.322281
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:25.737489
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:28.154151
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:30.568236
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:32.983971
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:35.399688
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:31:36.809170
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 02:31:38.297321
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

# Generated at 2026-10-25 02:31:39.729027
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

# Generated at 2026-10-25 02:31:41.163296
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

# Generated at 2026-10-25 02:31:42.596692
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

# Generated at 2026-10-25 02:31:44.030625
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

# Generated at 2026-10-25 02:31:45.467161
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

# Generated at 2026-10-25 02:31:56.317988
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

# Generated at 2026-10-25 02:31:57.750909
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

# Generated at 2026-10-25 02:31:59.185546
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

# Generated at 2026-10-25 02:32:00.617744
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

# Generated at 2026-10-25 02:32:02.003054
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

# Generated at 2026-10-25 02:32:03.489509
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

# Generated at 2026-10-25 02:32:04.919622
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

# Generated at 2026-10-25 02:32:06.363130
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

# Generated at 2026-10-25 02:32:07.785885
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

# Generated at 2026-10-25 02:32:09.220182
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

# Generated at 2026-10-25 02:32:31.222303
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:32:33.636889
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:32:36.051462
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:32:38.470273
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:32:40.886490
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:32:43.303327
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:32:53.561773
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-25 02:32:55.198958
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-25 02:32:56.581158
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

# Generated at 2026-10-25 02:32:58.068263
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

# Generated at 2026-10-25 02:32:59.453678
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

# Generated at 2026-10-25 02:33:00.849055
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

# Generated at 2026-10-25 02:33:02.266078
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

# Generated at 2026-10-25 02:33:03.803570
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

# Generated at 2026-10-25 02:33:05.239138
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

# Generated at 2026-10-25 02:33:43.025768
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

# Generated at 2026-10-25 02:33:44.453378
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

# Generated at 2026-10-25 02:33:45.989980
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

# Generated at 2026-10-25 02:33:47.424978
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

# Generated at 2026-10-25 02:33:48.857665
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

# Generated at 2026-10-25 02:33:50.289743
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

# Generated at 2026-10-25 02:33:51.723636
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

# Generated at 2026-10-25 02:33:53.156756
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

# Generated at 2026-10-25 02:33:54.591383
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

# Generated at 2026-10-25 02:33:56.024291
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

# Generated at 2026-10-25 02:35:06.067542
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

# Generated at 2026-10-25 02:35:07.499775
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

# Generated at 2026-10-25 02:35:09.248626
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

# Generated at 2026-10-25 02:35:10.673920
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

# Generated at 2026-10-25 02:35:12.118434
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

# Generated at 2026-10-25 02:35:13.545158
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

# Generated at 2026-10-25 02:35:14.975891
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

# Generated at 2026-10-25 02:35:16.410606
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

# Generated at 2026-10-25 02:35:17.842264
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

# Generated at 2026-10-25 02:35:19.259824
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