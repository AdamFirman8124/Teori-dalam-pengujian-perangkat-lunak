

# Generated at 2026-10-24 11:38:40.516002
# Unit test for method run of class PostProcessor

# Generated at 2026-10-24 11:38:42.938744
# Unit test for method run of class PostProcessor

# Generated at 2026-10-24 11:38:45.364986
# Unit test for method run of class PostProcessor

# Generated at 2026-10-24 11:38:47.798878
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:38:50.217120
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:38:52.637396
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:38:55.059108
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-24 11:38:57.470415
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-24 11:38:59.891924
# Unit test for constructor of class AudioConversionError

# Generated at 2026-10-24 11:39:02.309564
# Unit test for method run of class PostProcessor

# Generated at 2026-10-24 11:39:04.729679
# Unit test for method run of class PostProcessor

# Generated at 2026-10-24 11:39:07.152320
# Unit test for method run of class PostProcessor

# Generated at 2026-10-24 11:39:09.581251
# Unit test for method run of class PostProcessor

# Generated at 2026-10-24 11:39:12.002606
# Unit test for method run of class PostProcessor

# Generated at 2026-10-24 11:39:26.244462
# Unit test for method run of class PostProcessor
def test_PostProcessor_run():pp = PostProcessor()

# Generated at 2026-10-24 11:39:32.949094
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:39:35.483633
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:37.996799
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:40.557631
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:42.973597
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:45.610209
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:48.026676
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:50.444131
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:52.860004
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:55.278438
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:39:57.696695
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:00.112906
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:02.535456
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:04.946548
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:07.366368
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:09.784507
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:12.201018
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:14.619495
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:17.033568
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:19.454298
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:21.872534
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:24.292386
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:26.715972
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:29.135377
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:31.553534
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:33.969452
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:40:54.459507
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-24 11:40:55.785161
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:40:57.094868
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:40:58.411612
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:40:59.779732
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:41:02.291765
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:04.849923
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:07.570996
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:09.993108
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:12.405916
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:14.823824
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:17.369936
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:19.788777
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:22.204721
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:24.623252
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:27.040831
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:29.461021
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:31.878801
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:34.296841
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:36.717928
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:39.136997
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:41.558013
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:43.975591
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:46.392040
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:48.809819
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:51.229330
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:53.642133
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:56.059774
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:41:58.477158
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:00.894829
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:03.315586
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:05.731269
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:08.149441
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:10.570662
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:12.988758
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:15.408300
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:17.826699
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:20.243683
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:22.661910
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:25.081899
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:27.499128
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:29.919696
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:32.334655
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:34.752517
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:42:42.647677
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .ffmpeg import FFmpegPostProcessor  # noqa: F401  (keeps import graph consistent)

    class FakeDownloader(object):
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    import os
    import tempfile
    import time

    # --- Success case: utime is applied to the file ---
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        atime = 1000000000
        mtime = 1100000000

        pp = PostProcessor(downloader=FakeDownloader())
        pp.try_utime(path, atime, mtime)

        stat = os.stat(path)
        assert stat.st_atime == atime, 'atime not set: %r' % stat.st_atime
        assert stat.st_mtime == mtime, 'mtime not set: %r' % stat.st_mtime

        # No warnings should have been reported on success
        assert pp._downloader.warnings == [], 'unexpected warnings: %r' % pp._downloader.warnings
    finally:
        os.remove(path)

    # --- Failure case: nonexistent path -> warning reported, no exception ---
    downloader = FakeDownloader()
    pp = PostProcessor(downloader=downloader)
    errnote = 'Cannot update utime of file'

    nonexistent = os.path.join(
        tempfile.gettempdir(),
        'nonexistent_file_%d' % int(time.time()),
    )
    # Should not raise
    pp.try_utime(nonexistent, 123, 456, errnote=errnote)

    assert len(downloader.warnings) == 1, 'expected exactly one warning, got %r' % downloader.warnings
    assert downloader.warnings[0] == errnote, 'warning mismatch: %r' % downloader.warnings[0]

    # --- Default errnote is used when none is supplied ---
    downloader2 = FakeDownloader()
    pp2 = PostProcessor(downloader=downloader2)
    pp2.try_utime(nonexistent, 123, 456)
    assert len(downloader2.warnings) == 1, 'expected exactly one warning, got %r' % downloader2.warnings
    assert downloader2.warnings[0] == 'Cannot update utime of file', (
        'default errnote mismatch: %r' % downloader2.warnings[0]
    )

# Generated at 2026-10-24 11:42:43.960889
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:45.672695
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:47.104477
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:48.426786
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:49.747022
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:51.202245
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:52.626257
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:53.955522
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:55.399225
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:56.713652
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:58.036093
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:42:59.380946
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:43:00.773878
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:43:02.096797
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:43:04.712741
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:07.130765
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:09.554006
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:11.974084
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:14.391280
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:16.811192
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:19.232282
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:21.648731
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:24.070223
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:26.492106
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:28.903205
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:31.320971
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:33.737867
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:36.156596
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:38.573850
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:40.991936
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:43.408662
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:45.824406
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:48.240328
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:50.656132
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:53.074904
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:55.491628
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:43:57.908816
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:44:00.327199
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:44:03.658356
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:44:23.051288
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:44:39.740327
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-24 11:44:42.156978
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:44:44.799132
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:44:47.359970
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:44:49.930248
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from .ffmpeg import FFmpegPostProcessor  # noqa: F401  (keeps import graph consistent)

    class FakeDownloader(object):
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    import os
    import tempfile
    import time

    # --- Success case: utime is applied to the file ---
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        atime = 1000000000
        mtime = 1100000000

        pp = PostProcessor(downloader=FakeDownloader())
        pp.try_utime(path, atime, mtime)

        stat = os.stat(path)
        assert stat.st_atime == atime, 'atime not set: %r' % stat.st_atime
        assert stat.st_mtime == mtime, 'mtime not set: %r' % stat.st_mtime

        # No warnings should have been reported on success
        assert pp._downloader.warnings == [], 'unexpected warnings: %r' % pp._downloader.warnings
    finally:
        os.remove(path)

    # --- Failure case: nonexistent path -> warning reported, no exception ---
    downloader = FakeDownloader()
    pp = PostProcessor(downloader=downloader)
    errnote = 'Cannot update utime of file'

    nonexistent = os.path.join(
        tempfile.gettempdir(),
        'nonexistent_file_%d' % int(time.time()),
    )
    # Should not raise
    pp.try_utime(nonexistent, 123, 456, errnote=errnote)

    assert len(downloader.warnings) == 1, 'expected exactly one warning, got %r' % downloader.warnings
    assert downloader.warnings[0] == errnote, 'warning mismatch: %r' % downloader.warnings[0]

    # --- Default errnote is used when none is supplied ---
    downloader2 = FakeDownloader()
    pp2 = PostProcessor(downloader=downloader2)
    pp2.try_utime(nonexistent, 123, 456)
    assert len(downloader2.warnings) == 1, 'expected exactly one warning, got %r' % downloader2.warnings
    assert downloader2.warnings[0] == 'Cannot update utime of file', (
        'default errnote mismatch: %r' % downloader2.warnings[0]
    )

# Generated at 2026-10-24 11:44:51.347791
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:44:52.765554
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:44:54.074180
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:44:55.394106
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:44:56.708417
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:44:58.064730
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:44:59.397590
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:45:04.506803
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:45:07.040354
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:09.459512
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:11.888980
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:14.306705
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:16.728756
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:19.365220
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:21.777983
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:24.199335
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:26.615336
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:29.033949
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:31.465563
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:33.885427
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:36.297921
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:38.716165
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:41.128613
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:43.545716
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:45.961429
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:48.377870
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:50.795158
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:53.212803
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:55.629277
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:45:58.045266
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:00.463188
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:02.880245
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:05.296848
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:07.714391
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:10.144316
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:20.070763
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:22.487392
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:24.902261
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:27.320180
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:29.737194
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:32.153052
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:34.571556
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:36.988214
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:39.404912
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:41.822330
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:44.239096
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:46.658692
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:49.075028
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:51.489563
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:53.907503
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:56.325533
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:46:58.738950
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:01.155835
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:03.573491
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:05.990113
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:08.407454
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:10.825678
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:13.241140
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:15.657365
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:18.073845
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:20.488372
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:22.910040
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:24.232282
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:47:42.119040
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:47:43.444908
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:47:44.803312
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:47:46.155534
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:47:47.488358
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:47:48.975772
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor()

    # --- success case: os.utime is called with encoded path ---
    with patch('__main__.os.utime') as mock_utime:
        with patch('__main__.encodeFilename', side_effect=lambda x: x.encode()):
            pp.try_utime('/downloads/video.mp4', 1234567890, 1234567899)
    mock_utime.assert_called_once_with(b'/downloads/video.mp4', (1234567890, 1234567899))

    # --- failure case: exception is swallowed, warning reported ---
    class FakeDownloader:
        def report_warning(self, msg):
            self.last_warning = msg

    dl = FakeDownloader()
    pp = PostProcessor(downloader=dl)

    with patch('__main__.os.utime', side_effect=OSError('no permission')):
        pp.try_utime('/downloads/video.mp4', 1, 2, errnote='utime failed')

    assert dl.last_warning == 'utime failed'

# Generated at 2026-10-24 11:47:51.394632
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:53.811179
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:56.227454
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:47:58.644438
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:48:01.059695
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:48:03.475455
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:48:05.896072
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:48:08.312785
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:48:10.728098
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:48:13.145062
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:48:15.700131
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 11:48:18.115423
# Unit test for method try_utime of class PostProcessor