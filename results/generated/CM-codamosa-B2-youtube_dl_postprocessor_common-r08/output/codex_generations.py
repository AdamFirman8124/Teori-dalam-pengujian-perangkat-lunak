

# Generated at 2026-11-03 00:46:52.274821
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():from __future__ import unicode_literals

import os
import tempfile
import unittest

try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock

from ..postprocessor.common import PostProcessor


class FakeDownloader(object):
    def __init__(self):
        self.params = {}
        self.warnings = []

    def report_warning(self, message):
        self.warnings.append(message)


class TestPostProcessorTryUtime(unittest.TestCase):

    def setUp(self):
        self.downloader = FakeDownloader()
        self.pp = PostProcessor(self.downloader)

    def test_try_utime_calls_os_utime_with_times(self):
        path = 'dummy_video.mp4'
        atime, mtime = 1234567890, 9876543210
        with patch('os.utime') as mock_utime:
            self.pp.try_utime(path, atime, mtime)
            self.assertEqual(mock_utime.call_count, 1)
            self.assertEqual(mock_utime.call_args[0][1], (atime, mtime))
        self.assertEqual(self.downloader.warnings, [])

    def test_try_utime_success_no_warning(self):
        path = 'dummy_video.mp4'
        with patch('os.utime') as mock_utime:
            self.pp.try_utime(path, 1000, 2000)
            mock_utime.assert_called_once()
        self.assertEqual(self.downloader.warnings, [])

    def test_try_utime_exception_reports_default_warning(self):
        path = 'dummy_video.mp4'
        with patch('os.utime', side_effect=Exception('utime failed')):
            self.pp.try_utime(path, 1000, 2000)
        self.assertEqual(self.downloader.warnings,
                         ['Cannot update utime of file'])

    def test_try_utime_exception_reports_custom_errnote(self):
        path = 'dummy_video.mp4'
        with patch('os.utime', side_effect=Exception('utime failed')):
            self.pp.try_utime(path, 1000, 2000, errnote='custom error note')
        self.assertEqual(self.downloader.warnings, ['custom error note'])

    def test_try_utime_sets_times_on_real_file(self):
        fd, path = tempfile.mkstemp()
        os.close(fd)
        try:
            atime, mtime = 1000000, 2000000
            self.pp.try_utime(path, atime, mtime)
            st = os.stat(path)
            self.assertEqual(int(st.st_atime), atime)
            self.assertEqual(int(st.st_mtime), mtime)
        finally:
            os.unlink(path)

    def test_try_utime_no_downloader_does_not_raise_on_success(self):
        pp = PostProcessor(None)
        fd, path = tempfile.mkstemp()
        os.close(fd)
        try:
            # Should not raise even without a downloader attached
            pp.try_utime(path, 1000, 2000)
            st = os.stat(path)
            self.assertEqual(int(st.st_mtime), 2000000)
        finally:
            os.unlink(path)


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-03 00:48:11.318876
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    error = AudioConversionError('test error message')

    # It should be an instance of both AudioConversionError and PostProcessingError
    assert isinstance(error, AudioConversionError)
    assert isinstance(error, PostProcessingError)

    # The exception message should be preserved
    assert str(error) == 'test error message'

    # It should behave like a standard exception
    try:
        raise AudioConversionError('conversion failed')
    except AudioConversionError as e:
        assert str(e) == 'conversion failed'
    except PostProcessingError:
        assert False, 'AudioConversionError should be caught first'
    except Exception:
        assert False, 'AudioConversionError should be catchable'

# Generated at 2026-11-03 00:49:15.312210
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    # Test basic construction
    error_message = 'Audio conversion failed'
    error = AudioConversionError(error_message)
    
    # Test that it's an instance of AudioConversionError
    assert isinstance(error, AudioConversionError)
    
    # Test that it's an instance of the parent PostProcessingError
    assert isinstance(error, PostProcessingError)
    
    # Test that the error message is stored correctly
    assert str(error) == error_message
    
    # Test that the exception can be raised and caught
    try:
        raise AudioConversionError('test raise')
    except AudioConversionError as e:
        assert str(e) == 'test raise'
    except PostProcessingError:
        assert False, 'AudioConversionError should be caught as AudioConversionError'

# Generated at 2026-11-03 00:50:37.346417
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    # Test construction without a downloader
    pp = PostProcessor()
    assert pp._downloader is None

    # Test construction with a downloader
    class FakeDownloader(object):
        def __init__(self):
            self.params = {}

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    assert pp._downloader is downloader

    # Test set_downloader
    another_downloader = FakeDownloader()
    pp.set_downloader(another_downloader)
    assert pp._downloader is another_downloader

# Generated at 2026-11-03 00:52:00.380789
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():from __future__ import unicode_literals

import os
import sys
import unittest

from unittest.mock import MagicMock, patch

# Import the PostProcessor class from the module under test.
# Adjust the import path as needed for your project layout.
from youtube_dl.postprocessor.common import PostProcessor


class TestPostProcessorTryUtime(unittest.TestCase):

    def _make_pp(self):
        """Create a PostProcessor with a mock downloader."""
        downloader = MagicMock()
        downloader.params = {}
        pp = PostProcessor(downloader)
        return pp, downloader

    @patch('os.utime')
    def test_try_utime_success(self, mock_utime):
        """When os.utime succeeds, no warning should be reported."""
        pp, downloader = self._make_pp()

        pp.try_utime('somefile.mp4', 1000, 2000)

        mock_utime.assert_called_once_with(
            PostProcessor.try_utime.__module__ and 'somefile.mp4',
            (1000, 2000))
        downloader.report_warning.assert_not_called()

    @patch('os.utime', side_effect=OSError('permission denied'))
    def test_try_utime_failure_reports_default_warning(self, mock_utime):
        """When os.utime raises, the default errnote is reported."""
        pp, downloader = self._make_pp()

        pp.try_utime('somefile.mp4', 1000, 2000)

        downloader.report_warning.assert_called_once_with(
            'Cannot update utime of file')

    @patch('os.utime', side_effect=OSError('disk error'))
    def test_try_utime_failure_reports_custom_errnote(self, mock_utime):
        """When os.utime raises, the custom errnote is reported."""
        pp, downloader = self._make_pp()

        pp.try_utime('somefile.mp4', 1000, 2000, errnote='custom error note')

        downloader.report_warning.assert_called_once_with('custom error note')

    @patch('os.utime')
    def test_try_utime_passes_atime_mtime(self, mock_utime):
        """os.utime receives the (atime, mtime) tuple unchanged."""
        pp, downloader = self._make_pp()

        atime, mtime = 1234567890, 987654321
        pp.try_utime('path/to/file', atime, mtime)

        args, kwargs = mock_utime.call_args
        self.assertEqual(args[1], (atime, mtime))


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-03 00:53:04.021717
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    import os
    import tempfile
    import time
    from unittest.mock import MagicMock, patch

    import pytest

    from .PostProcessor import PostProcessor  # noqa: F401

    class MockDownloader(object):
        def __init__(self):
            self.params = {}
            self.warnings = []

        def report_warning(self, message):
            self.warnings.append(message)

    atime = 1234567890
    mtime = 1234567891

    # Test successful utime update
    downloader = MockDownloader()
    pp = PostProcessor(downloader)

    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        pp.try_utime(path, atime, mtime)
        stat = os.stat(path)
        assert int(stat.st_atime) == atime
        assert int(stat.st_mtime) == mtime
        assert downloader.warnings == []
    finally:
        os.remove(path)

    # Test that report_warning is called when os.utime fails
    with patch('os.utime', side_effect=Exception('utime failed')):
        downloader2 = MockDownloader()
        pp2 = PostProcessor(downloader2)
        pp2.try_utime('some_path', atime, mtime)
        assert downloader2.warnings == ['Cannot update utime of file']

    # Test custom errnote on failure
    with patch('os.utime', side_effect=Exception('utime failed')):
        downloader3 = MockDownloader()
        pp3 = PostProcessor(downloader3)
        pp3.try_utime('some_path', atime, mtime, errnote='Custom error note')
        assert downloader3.warnings == ['Custom error note']

    # Test with a downloader that reports warnings via mock
    with patch('os.utime', side_effect=OSError('no such file')):
        mock_downloader = MagicMock()
        pp4 = PostProcessor(mock_downloader)
        pp4.try_utime('nonexistent_file', atime, mtime)
        mock_downloader.report_warning.assert_called_once_with('Cannot update utime of file')