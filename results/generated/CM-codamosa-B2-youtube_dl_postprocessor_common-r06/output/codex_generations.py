

# Generated at 2026-11-03 06:10:04.362926
# Unit test for method set_downloader of class PostProcessor
def test_PostProcessor_set_downloader():
    from unittest import mock

    # Create a PostProcessor without an initial downloader
    pp = PostProcessor()
    assert pp._downloader is None

    # Set a downloader and verify it is stored
    downloader = mock.Mock()
    pp.set_downloader(downloader)
    assert pp._downloader is downloader

    # Setting a different downloader should replace the previous one
    new_downloader = mock.Mock()
    pp.set_downloader(new_downloader)
    assert pp._downloader is new_downloader

    # A PostProcessor constructed with a downloader keeps it
    initial_downloader = mock.Mock()
    pp2 = PostProcessor(downloader=initial_downloader)
    assert pp2._downloader is initial_downloader

    # set_downloader can also override a constructor-provided downloader
    replacement = mock.Mock()
    pp2.set_downloader(replacement)
    assert pp2._downloader is replacement

    print('test_PostProcessor_set_downloader passed')


if __name__ == '__main__':
    test_PostProcessor_set_downloader()

# Generated at 2026-11-03 06:11:44.507556
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    # Default constructor should have no downloader
    pp = PostProcessor()
    assert pp._downloader is None

    # Constructor should store the passed downloader
    downloader = object()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader

    # set_downloader should update the downloader
    new_downloader = object()
    pp.set_downloader(new_downloader)
    assert pp._downloader is new_downloader

# Generated at 2026-11-03 06:13:17.798043
# Unit test for method run of class PostProcessor
def test_PostProcessor_run():
    from youtube_dl.utils import PostProcessingError

    pp = PostProcessor()
    information = {'filepath': 'somefile.mp4', 'title': 'test video'}
    files_to_delete, updated_info = pp.run(information)
    assert files_to_delete == []
    assert updated_info == information
    assert updated_info is information

# Generated at 2026-11-03 06:14:25.174254
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # Create a temporary file
    tmp_path = 'test_file_utime.tmp'
    with open(tmp_path, 'w') as f:
        f.write('test')

    try:
        atime = 1000000
        mtime = 2000000
        pp.try_utime(tmp_path, atime, mtime)

        stat = os.stat(tmp_path)
        assert stat.st_atime == atime
        assert stat.st_mtime == mtime
    finally:
        os.remove(tmp_path)


def test_PostProcessor_try_utime_nonexistent_file():
    # Test that failure is handled gracefully with a warning
    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)
    pp._downloader = mock_downloader

    nonexistent = 'nonexistent_file_that_does_not_exist_12345.tmp'
    errnote = 'Cannot update utime of file'

    pp.try_utime(nonexistent, 1000, 2000, errnote=errnote)

    mock_downloader.report_warning.assert_called_once_with(errnote)


def test_PostProcessor_try_utime_default_errnote():
    mock_downloader = MagicMock()
    pp = PostProcessor(downloader=mock_downloader)
    pp._downloader = mock_downloader

    nonexistent = 'nonexistent_file_that_does_not_exist_67890.tmp'

    pp.try_utime(nonexistent, 1000, 2000)

    mock_downloader.report_warning.assert_called_once_with('Cannot update utime of file')

# Generated at 2026-11-03 06:15:50.269030
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import tempfile

    class FakeDownloader(object):
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    fd, filename = tempfile.mkstemp(suffix='_pp_utime_test')
    os.close(fd)
    try:
        downloader = FakeDownloader()
        pp = PostProcessor(downloader=downloader)

        # Successful utime update: atime and mtime should be set, no warnings
        atime = 1000000000
        mtime = 1234567890
        pp.try_utime(filename, atime, mtime)
        st = os.stat(filename)
        assert int(st.st_atime) == atime, 'atime not updated correctly'
        assert int(st.st_mtime) == mtime, 'mtime not updated correctly'
        assert downloader.warnings == [], 'no warning expected on success'

        # Failure case: nonexistent path -> report_warning called, no exception
        bad_path = os.path.join(filename, 'nonexistent_dir', 'no_such_file')
        pp.try_utime(bad_path, 1, 2, errnote='utime failed')
        assert downloader.warnings == ['utime failed'], (
            'expected custom errnote to be reported: %r' % downloader.warnings)

        # Failure case with default errnote
        downloader.warnings = []
        pp.try_utime(bad_path, 1, 2)
        assert downloader.warnings == ['Cannot update utime of file'], (
            'expected default errnote to be reported: %r' % downloader.warnings)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

# Generated at 2026-11-03 06:17:50.693207
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    try:
        from youtube_dl.postprocessor.common import PostProcessor
    except ImportError:
        from youtube_dl.postprocessor import PostProcessor

    downloader = FakeDownloader()
    pp = PostProcessor(downloader=downloader)

    tmpdir = tempfile.mkdtemp()
    try:
        filepath = os.path.join(tmpdir, 'testfile.mp4')
        with open(filepath, 'w') as f:
            f.write('test data')

        # Test successful utime update with integer timestamps
        atime = 1000000000
        mtime = 1000000005
        pp.try_utime(filepath, atime, mtime)

        stat_result = os.stat(filepath)
        assert int(stat_result.st_atime) == atime, \
            'Expected atime %d, got %d' % (atime, stat_result.st_atime)
        assert int(stat_result.st_mtime) == mtime, \
            'Expected mtime %d, got %d' % (mtime, stat_result.st_mtime)
        assert len(downloader.warnings) == 0, \
            'No warnings should be reported for successful utime'

        # Test with a non-existent file - should report a warning
        nonexistent = os.path.join(tmpdir, 'nonexistent.mp4')
        pp.try_utime(nonexistent, atime, mtime)
        assert len(downloader.warnings) == 1, \
            'Expected one warning for non-existent file'
        assert 'Cannot update utime of file' in downloader.warnings[0], \
            'Default errnote message expected, got: %s' % downloader.warnings[0]

        # Test with a custom errnote
        pp.try_utime(nonexistent, atime, mtime, errnote='Custom errnote message')
        assert len(downloader.warnings) == 2, \
            'Expected two warnings total'
        assert downloader.warnings[1] == 'Custom errnote message', \
            'Custom errnote expected, got: %s' % downloader.warnings[1]

        # Test with fractional timestamps
        atime2 = 1500000000.5
        mtime2 = 1500000000.75
        pp.try_utime(filepath, atime2, mtime2)
        stat_result = os.stat(filepath)
        assert abs(stat_result.st_atime - atime2) < 0.1, \
            'Expected atime ~%f, got %f' % (atime2, stat_result.st_atime)
        assert abs(stat_result.st_mtime - mtime2) < 0.1, \
            'Expected mtime ~%f, got %f' % (mtime2, stat_result.st_mtime)
        assert len(downloader.warnings) == 2, \
            'No additional warnings should be reported for fractional timestamps'

    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == '__main__':
    test_PostProcessor_try_utime()
    print('All tests passed!')