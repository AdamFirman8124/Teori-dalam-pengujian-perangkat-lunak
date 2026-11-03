

# Generated at 2026-11-03 06:01:40.035966
# Unit test for method run of class PostProcessor
def test_PostProcessor_run():
    pp = PostProcessor()
    information = {'filepath': '/tmp/testfile.mp4', 'title': 'Test Video'}
    files, updated_info = pp.run(information)
    assert files == []
    assert updated_info == information

# Generated at 2026-11-03 06:03:01.546979
# Unit test for method set_downloader of class PostProcessor
def test_PostProcessor_set_downloader():
    from ..youtube_dl import YoutubeDL

    class FakeDownloader(object):
        def __init__(self):
            self.params = {}

    # Test with no initial downloader
    pp = PostProcessor()
    assert pp._downloader is None

    # Set a downloader
    downloader = FakeDownloader()
    pp.set_downloader(downloader)
    assert pp._downloader is downloader

    # Replace with another downloader
    downloader2 = FakeDownloader()
    pp.set_downloader(downloader2)
    assert pp._downloader is downloader2
    assert pp._downloader is not downloader

    # Test on a PostProcessor initialized with a downloader
    pp2 = PostProcessor(downloader)
    assert pp2._downloader is downloader
    pp2.set_downloader(downloader2)
    assert pp2._downloader is downloader2

    # Setting to None is allowed
    pp2.set_downloader(None)
    assert pp2._downloader is None

# Generated at 2026-11-03 06:04:26.438897
# Unit test for method run of class PostProcessor
def test_PostProcessor_run():
    from youtube_dl.postprocessor.common import PostProcessor

    # Test with no downloader
    pp = PostProcessor()
    information = {'filepath': '/tmp/video.mp4', 'title': 'Test Video'}
    files, info = pp.run(information)

    assert files == []
    assert info == information
    assert info['filepath'] == '/tmp/video.mp4'
    assert info['title'] == 'Test Video'

    # Test with a downloader set
    class FakeDownloader(object):
        def __init__(self):
            self.params = {}

    pp2 = PostProcessor(FakeDownloader())
    information2 = {'filepath': '/tmp/audio.mp3'}
    files2, info2 = pp2.run(information2)

    assert files2 == []
    assert info2 is information2

    # Test that information dict is returned unchanged (not copied)
    assert info2['filepath'] == '/tmp/audio.mp3'

    # Test with empty information dict
    pp3 = PostProcessor()
    files3, info3 = pp3.run({})
    assert files3 == []
    assert info3 == {}

# Generated at 2026-11-03 06:05:54.092880
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    """Test the constructor of PostProcessor."""
    # Test with no downloader
    pp = PostProcessor()
    assert pp._downloader is None

    # Test with a downloader
    downloader = object()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader

    # Test set_downloader
    pp = PostProcessor()
    new_downloader = object()
    pp.set_downloader(new_downloader)
    assert pp._downloader is new_downloader

# Generated at 2026-11-03 06:06:58.705184
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    from ..utils import PostProcessingError

    # AudioConversionError should be a subclass of PostProcessingError
    assert issubclass(AudioConversionError, PostProcessingError)

    # It should be instantiable with no arguments
    error = AudioConversionError()
    assert isinstance(error, PostProcessingError)
    assert isinstance(error, Exception)

    # It should accept a message argument
    message = 'audio conversion failed'
    error_with_msg = AudioConversionError(message)
    assert str(error_with_msg) == message

# Generated at 2026-11-03 06:08:35.874601
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import patch, MagicMock

    # Test successful utime call
    downloader = MagicMock()
    pp = PostProcessor(downloader)

    with patch('os.utime') as mock_utime:
        pp.try_utime('testfile.mp4', 1234567890, 1234567890)
        mock_utime.assert_called_once()

    # No warning should be reported on success
    downloader.report_warning.assert_not_called()

    # Test error case with custom errnote
    downloader2 = MagicMock()
    pp2 = PostProcessor(downloader2)

    with patch('os.utime', side_effect=OSError('Permission denied')):
        pp2.try_utime('testfile.mp4', 1234567890, 1234567890, errnote='custom error message')
        downloader2.report_warning.assert_called_once_with('custom error message')

    # Test error case with default errnote
    downloader3 = MagicMock()
    pp3 = PostProcessor(downloader3)

    with patch('os.utime', side_effect=OSError('Permission denied')):
        pp3.try_utime('testfile.mp4', 1234567890, 1234567890)
        downloader3.report_warning.assert_called_once_with('Cannot update utime of file')

# Generated at 2026-11-03 06:10:26.682714
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    """Test that try_utime updates atime and mtime of an existing file."""
    tmpdir = tempfile.mkdtemp()
    try:
        filepath = os.path.join(tmpdir, 'test_file.txt')
        with open(filepath, 'w') as f:
            f.write('test data')

        downloader = FakeDownloader()
        pp = PostProcessor(downloader)

        atime = 1000000000
        mtime = 1000000001

        pp.try_utime(filepath, atime, mtime)

        st = os.stat(filepath)
        assert int(st.st_atime) == atime
        assert int(st.st_mtime) == mtime
        assert downloader.warnings == []
    finally:
        shutil.rmtree(tmpdir)


def test_PostProcessor_try_utime_nonexistent_file():
    """Test that try_utime reports a warning when os.utime fails."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    pp.try_utime(os.path.join(tempfile.gettempdir(), 'nonexistent_file_1234567890'), 1234, 5678)

    assert len(downloader.warnings) == 1
    assert downloader.warnings[0] == 'Cannot update utime of file'


def test_PostProcessor_try_utime_custom_errnote():
    """Test that try_utime uses the custom errnote on failure."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    custom_note = 'custom utime failure'
    pp.try_utime(os.path.join(tempfile.gettempdir(), 'nonexistent_file_0987654321'), 1234, 5678, errnote=custom_note)

    assert downloader.warnings == [custom_note]


def test_PostProcessor_try_utime_no_downloader():
    """Test that try_utime swallows the error even without a downloader."""
    pp = PostProcessor(None)

    # Should not raise even though os.utime will fail and _downloader is None
    pp.try_utime(os.path.join(tempfile.gettempdir(), 'nonexistent_file_5555555555'), 1, 2)