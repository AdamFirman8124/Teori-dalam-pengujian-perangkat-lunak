

# Generated at 2026-11-02 16:14:22.350352
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    # Constructing without a downloader should leave _downloader as None
    pp = PostProcessor()
    assert pp._downloader is None

    # Constructing with a downloader should store it
    class FakeDownloader(object):
        def __init__(self):
            self.params = {}

        def report_warning(self, msg):
            pass

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader

    # A second instance must not share state with the first
    pp2 = PostProcessor(downloader)
    assert pp2._downloader is downloader
    assert pp2._downloader is not None

    # set_downloader replaces the stored downloader
    downloader2 = FakeDownloader()
    pp.set_downloader(downloader2)
    assert pp._downloader is downloader2

# Generated at 2026-11-02 16:14:26.033232
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    error = AudioConversionError('conversion failed')
    assert isinstance(error, AudioConversionError)
    assert isinstance(error, PostProcessingError)
    assert isinstance(error, Exception)
    assert str(error) == 'conversion failed'

    # Test that it can be raised and caught
    try:
        raise AudioConversionError('test error')
    except AudioConversionError as e:
        assert str(e) == 'test error'
    except PostProcessingError:
        assert False, 'AudioConversionError should be caught as AudioConversionError'

# Generated at 2026-11-02 16:14:29.053486
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    # Test that AudioConversionError can be instantiated
    error = AudioConversionError()
    assert isinstance(error, AudioConversionError)
    assert isinstance(error, PostProcessingError)
    assert isinstance(error, Exception)

    # Test instantiation with a message
    message = 'Audio conversion failed'
    error_with_msg = AudioConversionError(message)
    assert isinstance(error_with_msg, AudioConversionError)
    assert str(error_with_msg) == message

    # Test that the exception can be raised and caught
    try:
        raise AudioConversionError('test error')
    except AudioConversionError as e:
        assert str(e) == 'test error'
    except PostProcessingError:
        assert False, 'Should have been caught as AudioConversionError'

# Generated at 2026-11-02 16:14:33.705574
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    # Test constructor with no arguments
    pp = PostProcessor()
    assert pp._downloader is None

    # Test constructor with a downloader argument
    fake_downloader = object()
    pp2 = PostProcessor(downloader=fake_downloader)
    assert pp2._downloader is fake_downloader

    # Test set_downloader
    another_downloader = object()
    pp2.set_downloader(another_downloader)
    assert pp2._downloader is another_downloader

# Generated at 2026-11-02 16:14:38.400023
# Unit test for method run of class PostProcessor
def test_PostProcessor_run():
    pp = PostProcessor()
    information = {
        'filepath': '/tmp/video.mp4',
        'title': 'test video',
        'id': '12345',
    }
    files_to_delete, updated_info = pp.run(information)

    # By default, no files should be marked for deletion
    assert files_to_delete == []
    # The information dict should be returned unchanged
    assert updated_info == information
    assert updated_info is information


def test_PostProcessor_run_with_downloader():
    class FakeDownloader(object):
        params = {}

    pp = PostProcessor(downloader=FakeDownloader())
    information = {'filepath': '/tmp/audio.mp3'}
    files_to_delete, updated_info = pp.run(information)

    assert files_to_delete == []
    assert updated_info is information


def test_PostProcessor_run_empty_info():
    pp = PostProcessor()
    files_to_delete, updated_info = pp.run({})

    assert files_to_delete == []
    assert updated_info == {}

# Generated at 2026-11-02 16:14:57.287783
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    tmpdir = tempfile.mkdtemp()
    try:
        filepath = os.path.join(tmpdir, 'testdata')
        with open(filepath, 'w') as f:
            f.write('data')

        downloader = FakeDownloader()
        pp = PostProcessor(downloader)

        atime = time.time() - 10000
        mtime = time.time() - 5000

        # Successful case: times are updated and no warning is reported
        pp.try_utime(filepath, atime, mtime)
        assert downloader.warnings == []
        stat_result = os.stat(filepath)
        assert abs(stat_result.st_atime - atime) < 2
        assert abs(stat_result.st_mtime - mtime) < 2

        # Failure case: nonexistent file leads to the custom errnote warning
        missing_path = os.path.join(tmpdir, 'does_not_exist')
        pp.try_utime(missing_path, atime, mtime, errnote='custom warning')
        assert downloader.warnings == ['custom warning']

        # Default errnote is used when none is provided
        downloader.warnings = []
        pp.try_utime(missing_path, atime, mtime)
        assert downloader.warnings == ['Cannot update utime of file']
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

# Generated at 2026-11-02 16:15:04.035399
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-11-02 16:15:17.174692
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():fd, path = tempfile.mkstemp(suffix='_pp_utime_test')

# Generated at 2026-11-02 16:15:43.147535
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    from unittest import mock

    downloader = mock.Mock()
    pp = PostProcessor(downloader)

    # Create a temporary file to test utime updating
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.close()
    path = tmp.name

    try:
        atime = 1000000000
        mtime = 1234567890

        pp.try_utime(path, atime, mtime)

        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        downloader.report_warning.assert_not_called()
    finally:
        os.unlink(path)

    # Test error case: nonexistent path should trigger report_warning
    downloader = mock.Mock()
    pp = PostProcessor(downloader)
    pp.try_utime('/nonexistent/path/file.mp4', 1000000000, 1000000000, errnote='custom warning')
    downloader.report_warning.assert_called_once_with('custom warning')

    # Default errnote
    downloader = mock.Mock()
    pp = PostProcessor(downloader)
    pp.try_utime('/nonexistent/path/file.mp4', 1000000000, 1000000000)
    downloader.report_warning.assert_called_once_with('Cannot update utime of file')

# Generated at 2026-11-02 16:16:09.283233
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    from unittest.mock import MagicMock

    try:
        PostProcessor  # noqa: F821
    except NameError:
        from yt_dlp.postprocessor import PostProcessor

    fd, path = tempfile.mkstemp()
    os.close(fd)

    try:
        downloader = MagicMock()
        pp = PostProcessor(downloader=downloader)

        atime, mtime = 1000000, 2000000

        # Successful case: utime is updated, no warning reported
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        downloader.report_warning.assert_not_called()

        # Default errnote is not raised as an exception on failure
        pp.try_utime('nonexistent_file__test__', atime, mtime)
        downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

        # Custom errnote is passed through to report_warning
        downloader2 = MagicMock()
        pp2 = PostProcessor(downloader=downloader2)
        pp2.try_utime('nonexistent_file__test__', atime, mtime,
                      errnote='custom warning')
        downloader2.report_warning.assert_called_once_with('custom warning')

        # Works even without a downloader set (no AttributeError escaping)
        pp3 = PostProcessor(downloader=None)
        try:
            pp3.try_utime('nonexistent_file__test__', atime, mtime)
        except AttributeError:
            pass  # report_warning unavailable; method must not raise anything else
    finally:
        try:
            os.remove(path)
        except OSError:
            pass

# Generated at 2026-11-02 16:16:43.444332
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    from unittest import mock

    pp = PostProcessor()

    # Successful case: os.utime is called with the encoded filename and times
    with mock.patch('os.utime') as utime_mock:
        pp.try_utime('somefile.mp4', 12345, 67890)
        utime_mock.assert_called_once_with(
            encodeFilename('somefile.mp4'), (12345, 67890))

    # Integration check with a real temporary file
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        atime, mtime = 1000000000, 1100000000
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
    finally:
        os.remove(path)

    # Failure case: when os.utime raises, the downloader reports a warning
    downloader = mock.Mock()
    pp.set_downloader(downloader)
    with mock.patch('os.utime', side_effect=Exception('utime failed')):
        pp.try_utime('somefile.mp4', 12345, 67890, errnote='custom errnote')
        downloader.report_warning.assert_called_once_with('custom errnote')

    # Default errnote is used when none is supplied
    downloader = mock.Mock()
    pp.set_downloader(downloader)
    with mock.patch('os.utime', side_effect=Exception('utime failed')):
        pp.try_utime('somefile.mp4', 12345, 67890)
        downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

# Generated at 2026-11-02 16:17:02.675370
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

    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        # Successful utime update
        pp = PostProcessor()
        atime, mtime = 1234567890, 987654321
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime

        # Failure case: nonexistent file should trigger a warning via downloader
        downloader = FakeDownloader()
        pp = PostProcessor(downloader)
        errnote = 'Cannot update utime of file'
        pp.try_utime('nonexistent_file_path_12345', atime, mtime, errnote=errnote)
        assert downloader.warnings == [errnote]
    finally:
        os.remove(path)

# Generated at 2026-11-02 16:18:30.784536
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import patch, MagicMock

    # Success case: os.utime called with encoded filename and (atime, mtime)
    downloader = MagicMock()
    pp = PostProcessor(downloader=downloader)
    with patch('os.utime') as mock_utime:
        pp.try_utime('test_file.mp4', 1000, 2000)
        mock_utime.assert_called_once_with(encodeFilename('test_file.mp4'), (1000, 2000))
        downloader.report_warning.assert_not_called()

    # Failure case: default errnote is reported via downloader
    downloader = MagicMock()
    pp = PostProcessor(downloader=downloader)
    with patch('os.utime', side_effect=OSError('operation not permitted')):
        pp.try_utime('test_file.mp4', 1000, 2000)
        downloader.report_warning.assert_called_once_with('Cannot update utime of file')

    # Failure case: custom errnote is reported via downloader
    downloader = MagicMock()
    pp = PostProcessor(downloader=downloader)
    with patch('os.utime', side_effect=OSError('operation not permitted')):
        pp.try_utime('test_file.mp4', 1000, 2000, errnote='custom warning')
        downloader.report_warning.assert_called_once_with('custom warning')

# Generated at 2026-11-02 16:19:19.669521
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    # Test successful utime update
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    filepath = 'testfile_utime.tmp'
    with open(filepath, 'w') as f:
        f.write('test')

    atime = 1000000000
    mtime = 1234567890
    pp.try_utime(filepath, atime, mtime)

    stat = os.stat(filepath)
    assert stat.st_atime == atime, 'atime not set correctly'
    assert stat.st_mtime == mtime, 'mtime not set correctly'
    assert downloader.warnings == [], 'no warnings should be reported on success'

    os.remove(filepath)


def test_PostProcessor_try_utime_nonexistent_file():
    # Test error handling: nonexistent file should report a warning, not raise
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    errnote = 'Cannot update utime of file'
    pp.try_utime('nonexistent_file_12345.tmp', 1000, 1000, errnote=errnote)

    assert len(downloader.warnings) == 1, 'a warning should be reported on failure'
    assert downloader.warnings[0] == errnote


def test_PostProcessor_try_utime_default_errnote():
    # Test default errnote message
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    pp.try_utime('nonexistent_file_67890.tmp', 1000, 1000)

    assert len(downloader.warnings) == 1
    assert downloader.warnings[0] == 'Cannot update utime of file'

# Generated at 2026-11-02 16:20:54.577316
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile
    from unittest import mock

    class FakeDownloader(object):
        def __init__(self):
            self.warnings = []
            self.params = {}

        def report_warning(self, msg):
            self.warnings.append(msg)

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    # Success case: utime of a real temporary file is updated, no warning emitted
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        atime, mtime = 1000000000, 1234567890
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        assert downloader.warnings == []
    finally:
        os.remove(path)

    # os.utime must be called with the encoded filename and an (atime, mtime) tuple
    with mock.patch.object(os, 'utime') as mock_utime:
        pp.try_utime(path, atime, mtime)
        mock_utime.assert_called_once_with(encodeFilename(path), (atime, mtime))
        assert downloader.warnings == []

    # Failure case: os.utime raising leads to report_warning with default errnote
    with mock.patch.object(os, 'utime', side_effect=OSError('boom')):
        pp.try_utime('nonexistent_file', 1, 2)
    assert downloader.warnings == ['Cannot update utime of file']

    # Failure case: a custom errnote is passed through to report_warning
    downloader.warnings = []
    with mock.patch.object(os, 'utime', side_effect=OSError('boom')):
        pp.try_utime('nonexistent_file', 1, 2, errnote='custom errnote')
    assert downloader.warnings == ['custom errnote']

# Generated at 2026-11-02 16:21:56.856732
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    downloader = mock.MagicMock()
    pp = PostProcessor(downloader)

    # --- Success case: utime is applied to an existing file ---
    tmpdir = tempfile.mkdtemp()
    try:
        path = os.path.join(tmpdir, 'testfile.mp4')
        with open(path, 'w') as f:
            f.write('test data')

        atime, mtime = 1000000, 2000000
        pp.try_utime(path, atime, mtime)

        st = os.stat(path)
        assert abs(st.st_atime - atime) < 1
        assert abs(st.st_mtime - mtime) < 1
        # No warning should have been reported on success
        downloader.report_warning.assert_not_called()
    finally:
        shutil.rmtree(tmpdir)

    # --- Failure case: report_warning called with default errnote ---
    with mock.patch('os.utime', side_effect=Exception('utime failed')):
        pp.try_utime('nonexistent_file', 1, 2)
        downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

    # --- Failure case with a custom errnote ---
    downloader2 = mock.MagicMock()
    pp2 = PostProcessor(downloader2)
    with mock.patch('os.utime', side_effect=Exception('utime failed')):
        pp2.try_utime('nonexistent_file', 1, 2, errnote='custom error message')
        downloader2.report_warning.assert_called_once_with('custom error message')

# Generated at 2026-11-02 16:23:33.710535
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    downloader = _FakeDownloader()
    pp = PostProcessor(downloader=downloader)

    # 1. os.utime is called with the encoded filename and (atime, mtime)
    with mock.patch('os.utime') as utime_mock:
        pp.try_utime('some dir/file.mp4', 1000, 2000)
        utime_mock.assert_called_once_with(
            encodeFilename('some dir/file.mp4'), (1000, 2000))
    assert downloader.warnings == []

    # 2. Timestamps are actually updated on a real file
    fd, path = tempfile.mkstemp()
    try:
        os.close(fd)
        atime, mtime = 1000000000, 1100000000
        pp.try_utime(path, atime, mtime)
        st = os.stat(path)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        assert downloader.warnings == []
    finally:
        os.remove(path)

    # 3. On failure the default warning is reported and no exception escapes
    with mock.patch('os.utime', side_effect=OSError('boom')):
        pp.try_utime('missing/file.mp4', 1, 2)
    assert downloader.warnings == ['Cannot update utime of file']

    # 4. A custom errnote is used when provided
    downloader.warnings = []
    with mock.patch('os.utime', side_effect=OSError('boom')):
        pp.try_utime('missing/file.mp4', 1, 2, errnote='custom errnote')
    assert downloader.warnings == ['custom errnote']