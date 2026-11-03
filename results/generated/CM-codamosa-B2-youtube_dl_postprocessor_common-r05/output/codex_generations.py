

# Generated at 2026-11-02 21:09:52.446479
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    # Test that AudioConversionError can be instantiated with a message
    error = AudioConversionError('test error message')
    assert isinstance(error, AudioConversionError)
    assert isinstance(error, PostProcessingError)
    assert str(error) == 'test error message'

    # Test that it can be raised and caught
    try:
        raise AudioConversionError('conversion failed')
    except AudioConversionError as e:
        assert str(e) == 'conversion failed'
    except PostProcessingError:
        assert False, 'Should have been caught as AudioConversionError'

# Generated at 2026-11-02 21:10:08.842697
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    # Success: os.utime is called with encoded filename and (atime, mtime)
    with patch('os.utime') as mock_utime:
        pp.try_utime('somefile', 1234, 5678)
        mock_utime.assert_called_once_with(
            encodeFilename('somefile'), (1234, 5678))
    assert downloader.warnings == []

    # Success on a real temporary file: timestamps are actually updated
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        atime, mtime = 1000000000, 1000000001
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        assert downloader.warnings == []
    finally:
        os.remove(path)

    # Failure: os.utime raising leads to a reported warning
    errnote = 'Cannot update utime of file'
    with patch('os.utime', side_effect=Exception('boom')):
        pp.try_utime('nonexistent_file_xyz', 0, 0)
    assert downloader.warnings == [errnote]

    # Custom errnote is used when provided
    downloader2 = FakeDownloader()
    pp2 = PostProcessor(downloader2)
    with patch('os.utime', side_effect=Exception('boom')):
        pp2.try_utime('nonexistent_file_xyz', 0, 0, errnote='custom note')
    assert downloader2.warnings == ['custom note']

# Generated at 2026-11-02 21:10:18.837867
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    """
    Test the constructor of AudioConversionError.

    AudioConversionError is a simple exception subclassing PostProcessingError.
    Verify it can be constructed with a message, stores it correctly,
    and is an instance of both PostProcessingError and Exception.
    """
    from .. import PostProcessor

    # Construct with a message
    error = PostProcessor.AudioConversionError('conversion failed')
    assert isinstance(error, PostProcessor.AudioConversionError)
    assert isinstance(error, PostProcessor.PostProcessingError)
    assert isinstance(error, Exception)
    assert str(error) == 'conversion failed'

    # Construct without arguments
    error_default = PostProcessor.AudioConversionError()
    assert isinstance(error_default, PostProcessor.AudioConversionError)

    # Verify subclass relationship
    assert issubclass(PostProcessor.AudioConversionError, PostProcessor.PostProcessingError)

    # Verify it can be raised and caught
    try:
        raise PostProcessor.AudioConversionError('test raise')
    except PostProcessor.AudioConversionError as e:
        assert str(e) == 'test raise'
    else:
        raise AssertionError('AudioConversionError was not raised')

# Generated at 2026-11-02 21:10:22.054433
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    message = 'audio conversion failed'
    error = AudioConversionError(message)

    # The instance should be an AudioConversionError, a PostProcessingError,
    # and therefore also an Exception
    assert isinstance(error, AudioConversionError)
    assert isinstance(error, PostProcessingError)
    assert isinstance(error, Exception)

    # The message passed to the constructor should be preserved
    assert str(error) == message

    # The exception should be raisable and catchable
    try:
        raise AudioConversionError(message)
    except AudioConversionError as e:
        assert str(e) == message
    except Exception:
        assert False, 'AudioConversionError raised an unexpected exception type'

    # The exception should also be catchable as a PostProcessingError
    try:
        raise AudioConversionError(message)
    except PostProcessingError as e:
        assert str(e) == message

# Generated at 2026-11-02 21:10:24.353652
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    pp = PostProcessor()
    assert pp._downloader is None

    downloader = object()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader

# Generated at 2026-11-02 21:12:00.362331
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-11-02 21:12:25.119636
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile

    atime, mtime = 1000000000, 1234567890
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        # Success case: utime is updated on an existing file
        pp = PostProcessor()
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime

        # Failure case: nonexistent file triggers report_warning with errnote
        class FakeDownloader(object):
            def __init__(self):
                self.warnings = []
                self.params = {}

            def report_warning(self, msg):
                self.warnings.append(msg)

        dl = FakeDownloader()
        pp2 = PostProcessor(dl)
        pp2.try_utime(path + '.missing', 1, 2, errnote='custom errnote')
        assert dl.warnings == ['custom errnote']
    finally:
        os.remove(path)

# Generated at 2026-11-02 21:13:03.157142
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile

    # Successful case: file exists, utime should be updated
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        pp = PostProcessor()
        atime = 1000000000
        mtime = 1000000001
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
    finally:
        os.remove(path)


def test_PostProcessor_try_utime_failure():
    from unittest.mock import MagicMock

    # Failure case: os.utime raises (nonexistent file), warning reported
    downloader = MagicMock()
    pp = PostProcessor(downloader=downloader)
    pp.try_utime('nonexistent_file_1234567890', 1, 2)
    downloader.report_warning.assert_called_once_with('Cannot update utime of file')


def test_PostProcessor_try_utime_custom_errnote():
    from unittest.mock import MagicMock

    # Failure case with custom errnote
    downloader = MagicMock()
    pp = PostProcessor(downloader=downloader)
    pp.try_utime('nonexistent_file_1234567890', 1, 2, errnote='custom error note')
    downloader.report_warning.assert_called_once_with('custom error note')


def test_PostProcessor_try_utime_no_downloader():
    # Failure case without downloader: should not raise
    pp = PostProcessor(downloader=None)
    try:
        pp.try_utime('nonexistent_file_1234567890', 1, 2)
    except AttributeError:
        pass  # acceptable: no downloader to report warning to

# Generated at 2026-11-02 21:13:40.609203
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    downloader = mock.Mock()
    pp = PostProcessor(downloader)

    # Successful utime: os.utime should be called with encoded path and times
    with mock.patch('os.utime') as utime_mock:
        pp.try_utime('somefile', 12345.0, 67890.0)
        utime_mock.assert_called_once_with('somefile', (12345.0, 67890.0))
    downloader.report_warning.assert_not_called()

    # Failing utime: warning should be reported through the downloader
    with mock.patch('os.utime', side_effect=OSError('utime failed')):
        pp.try_utime('somefile', 12345.0, 67890.0, errnote='custom errnote')
    downloader.report_warning.assert_called_once_with('custom errnote')

    # Failing utime with default errnote
    downloader2 = mock.Mock()
    pp2 = PostProcessor(downloader2)
    with mock.patch('os.utime', side_effect=Exception('failure')):
        pp2.try_utime('somefile', 1, 2)
    downloader2.report_warning.assert_called_once_with('Cannot update utime of file')

# Generated at 2026-11-02 21:14:18.570259
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    import time

    class FakeDownloader(object):
        def __init__(self):
            self.warnings = []
            self.params = {}

        def report_warning(self, msg):
            self.warnings.append(msg)

    # Successful utime: atime and mtime should be set on the file
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        pp = PostProcessor()
        atime = time.time() - 10000
        mtime = time.time() - 5000
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert abs(st.st_atime - atime) < 1
        assert abs(st.st_mtime - mtime) < 1
    finally:
        os.remove(path)

    # No downloader set: should not raise on failure
    pp = PostProcessor()
    pp.try_utime('nonexistent_file_123456', 1, 1)

    # Failure case: nonexistent file -> report_warning called with default errnote
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    pp.try_utime('nonexistent_file_123456', 1, 1)
    assert len(downloader.warnings) == 1
    assert downloader.warnings[0] == 'Cannot update utime of file'

    # Failure case with custom errnote
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    pp.try_utime('nonexistent_file_123456', 1, 1, errnote='custom error note')
    assert len(downloader.warnings) == 1
    assert downloader.warnings[0] == 'custom error note'

    # set_downloader should be honored
    downloader = FakeDownloader()
    pp = PostProcessor()
    pp.set_downloader(downloader)
    pp.try_utime('nonexistent_file_123456', 1, 1)
    assert len(downloader.warnings) == 1

# Generated at 2026-11-02 21:15:07.071400
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import patch

    class FakeDownloader(object):
        def __init__(self):
            self.params = {}
            self.warnings = []

        def report_warning(self, message):
            self.warnings.append(message)

    # 1. Success: os.utime is called with the encoded filename and (atime, mtime)
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    with patch('os.utime') as mock_utime:
        pp.try_utime('video.mp4', 1234, 5678)
        mock_utime.assert_called_once_with(encodeFilename('video.mp4'), (1234, 5678))
    assert downloader.warnings == []

    # 2. Failure: report_warning is called with the provided errnote
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    with patch('os.utime', side_effect=OSError('boom')):
        pp.try_utime('video.mp4', 1234, 5678, errnote='custom errnote')
    assert downloader.warnings == ['custom errnote']

    # 3. Failure: the default errnote is used when none is provided
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    with patch('os.utime', side_effect=OSError('boom')):
        pp.try_utime('video.mp4', 1234, 5678)
    assert downloader.warnings == ['Cannot update utime of file']

    # 4. Integration: timestamps of a real file are actually updated
    import tempfile
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        downloader = FakeDownloader()
        pp = PostProcessor(downloader)
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000
        assert int(st.st_mtime) == 2000
        assert downloader.warnings == []
    finally:
        os.remove(path)

# Generated at 2026-11-02 21:17:06.641423
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import mock
    from youtube_dl.postprocessor import PostProcessor

    # Test successful utime update
    downloader = mock.Mock()
    pp = PostProcessor(downloader)

    with mock.patch('os.utime') as utime_mock:
        pp.try_utime('somefile.mp4', 12345, 67890)
        utime_mock.assert_called_once()
        args = utime_mock.call_args[0]
        assert args[1] == (12345, 67890)
        downloader.report_warning.assert_not_called()

    # Test that os.utime failure triggers report_warning
    downloader2 = mock.Mock()
    pp2 = PostProcessor(downloader2)

    with mock.patch('os.utime', side_effect=Exception('utime failed')):
        pp2.try_utime('somefile.mp4', 12345, 67890)
        downloader2.report_warning.assert_called_once()

    # Test custom errnote message
    downloader3 = mock.Mock()
    pp3 = PostProcessor(downloader3)
    custom_note = 'custom error note'

    with mock.patch('os.utime', side_effect=Exception('utime failed')):
        pp3.try_utime('somefile.mp4', 12345, 67890, errnote=custom_note)
        downloader3.report_warning.assert_called_once_with(custom_note)

# Generated at 2026-11-02 21:18:20.609021
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock

    # Create a temporary file to test with
    fd, filepath = tempfile.mkstemp(suffix='.utime-test-tmp')
    os.close(fd)

    downloader = MagicMock()
    pp = PostProcessor(downloader=downloader)

    atime = 1000000000
    mtime = 1000000000

    try:
        # Successful case: utime should be updated and no warning reported
        pp.try_utime(filepath, atime, mtime)
        file_stat = os.stat(filepath)
        assert int(file_stat.st_atime) == atime
        assert int(file_stat.st_mtime) == mtime
        downloader.report_warning.assert_not_called()

        # Failure case: nonexistent file should trigger report_warning with the default errnote
        pp.try_utime(filepath + '.does-not-exist', atime, mtime)
        downloader.report_warning.assert_called_once_with('Cannot update utime of file')

        # Failure case with a custom errnote
        pp.try_utime(filepath + '.does-not-exist', atime, mtime, errnote='Custom utime error')
        downloader.report_warning.assert_called_with('Custom utime error')
    finally:
        os.remove(filepath)