

# Generated at 2026-10-24 12:05:32.933478
# Unit test for method set_downloader of class PostProcessor
def test_PostProcessor_set_downloader():
    """Unit test for method set_downloader of class PostProcessor"""
    from youtube_dl.postprocessor import PostProcessor

    class FakeDownloader(object):
        def __init__(self):
            self.params = {}

        def report_warning(self, msg):
            self._warnings = getattr(self, '_warnings', []) + [msg]

    # Case 1: downloader passed via constructor
    dl_a = FakeDownloader()
    pp_a = PostProcessor(dl_a)
    assert pp_a._downloader is dl_a

    # Case 2: no downloader at construction, set later
    dl_b = FakeDownloader()
    pp_b = PostProcessor()
    assert pp_b._downloader is None
    pp_b.set_downloader(dl_b)
    assert pp_b._downloader is dl_b

    # Case 3: overriding an existing downloader
    dl_c = FakeDownloader()
    pp_b.set_downloader(dl_c)
    assert pp_b._downloader is dl_c

    # Case 4: module_0.set_downloader(None) resets the association
    pp_b.set_downloader(None)
    assert pp_b._downloader is None

    print('test_PostProcessor_set_downloader passed')

# Generated at 2026-10-24 12:05:34.664739
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

# Generated at 2026-10-24 12:05:36.032321
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

# Generated at 2026-10-24 12:05:37.349997
# Unit test for method set_downloader of class PostProcessor
def test_PostProcessor_set_downloader():
    """Unit test for method set_downloader of class PostProcessor"""
    from youtube_dl.postprocessor import PostProcessor

    class FakeDownloader(object):
        def __init__(self):
            self.params = {}

        def report_warning(self, msg):
            self._warnings = getattr(self, '_warnings', []) + [msg]

    # Case 1: downloader passed via constructor
    dl_a = FakeDownloader()
    pp_a = PostProcessor(dl_a)
    assert pp_a._downloader is dl_a

    # Case 2: no downloader at construction, set later
    dl_b = FakeDownloader()
    pp_b = PostProcessor()
    assert pp_b._downloader is None
    pp_b.set_downloader(dl_b)
    assert pp_b._downloader is dl_b

    # Case 3: overriding an existing downloader
    dl_c = FakeDownloader()
    pp_b.set_downloader(dl_c)
    assert pp_b._downloader is dl_c

    # Case 4: module_0.set_downloader(None) resets the association
    pp_b.set_downloader(None)
    assert pp_b._downloader is None

    print('test_PostProcessor_set_downloader passed')

# Generated at 2026-10-24 12:05:39.860889
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-24 12:05:42.278643
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-24 12:05:44.866785
# Unit test for method set_downloader of class PostProcessor

# Generated at 2026-10-24 12:05:47.287421
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:05:49.707821
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:05:52.127462
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:05:54.550003
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:11.191060
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import tempfile

# Generated at 2026-10-24 12:06:12.631256
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

# Generated at 2026-10-24 12:06:13.963890
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

# Generated at 2026-10-24 12:06:15.367833
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

# Generated at 2026-10-24 12:06:16.726072
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

# Generated at 2026-10-24 12:06:18.040505
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

# Generated at 2026-10-24 12:06:19.367011
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

# Generated at 2026-10-24 12:06:20.683092
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

# Generated at 2026-10-24 12:06:23.103242
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:25.523495
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:27.937418
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:30.561801
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:32.981886
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:35.494168
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:37.912598
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:40.330091
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:42.748196
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:45.167917
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:47.588156
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:50.006526
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:52.423818
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:54.844015
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:57.266512
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:06:59.681380
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:02.099572
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:04.517766
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:06.932406
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:09.357646
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:11.923282
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:13.233296
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

# Generated at 2026-10-24 12:07:14.584615
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

# Generated at 2026-10-24 12:07:15.893133
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

# Generated at 2026-10-24 12:07:17.212620
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

# Generated at 2026-10-24 12:07:18.531935
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

# Generated at 2026-10-24 12:07:19.888988
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

# Generated at 2026-10-24 12:07:21.214066
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

# Generated at 2026-10-24 12:07:22.603688
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

# Generated at 2026-10-24 12:07:23.964878
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

# Generated at 2026-10-24 12:07:25.300206
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

# Generated at 2026-10-24 12:07:26.683728
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

# Generated at 2026-10-24 12:07:28.310728
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

# Generated at 2026-10-24 12:07:29.698649
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

# Generated at 2026-10-24 12:07:31.035424
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

# Generated at 2026-10-24 12:07:33.456573
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:35.874563
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:38.301302
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:40.820066
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:43.244020
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:45.657355
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:48.075642
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:50.506370
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:52.930476
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:55.346341
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:07:57.768354
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:00.188560
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:02.616490
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:05.035978
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:07.456033
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:09.875195
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:12.295492
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:14.714593
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:17.136126
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:19.556386
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:21.981487
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:24.401210
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:26.815297
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:29.233164
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:31.649458
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:34.071333
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:36.488005
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:38.904486
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:41.323165
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:43.742835
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:46.162562
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:48.579700
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:51.000542
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:53.419098
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:55.837064
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:08:58.254618
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:00.688931
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:37.370087
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:39.894214
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:42.313399
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:44.730985
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:47.307611
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:49.827453
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:52.248467
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:54.675142
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:57.108656
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:09:59.543165
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:01.968611
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:03.387972
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

# Generated at 2026-10-24 12:10:04.957180
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

# Generated at 2026-10-24 12:10:06.292691
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

# Generated at 2026-10-24 12:10:07.610282
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

# Generated at 2026-10-24 12:10:09.886460
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

# Generated at 2026-10-24 12:10:11.211202
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

# Generated at 2026-10-24 12:10:12.887379
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

# Generated at 2026-10-24 12:10:14.202317
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

# Generated at 2026-10-24 12:10:15.853277
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

# Generated at 2026-10-24 12:10:17.285309
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

# Generated at 2026-10-24 12:10:18.717671
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

# Generated at 2026-10-24 12:10:20.150826
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

# Generated at 2026-10-24 12:10:21.735654
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

# Generated at 2026-10-24 12:10:23.046568
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

# Generated at 2026-10-24 12:10:26.551403
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

# Generated at 2026-10-24 12:10:27.873146
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

# Generated at 2026-10-24 12:10:30.291499
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:32.708014
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:35.124027
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:37.545724
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:39.958391
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:42.375901
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:44.794419
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:47.216064
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:49.632334
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:52.052655
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:54.470536
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:57.107102
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:10:59.523554
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:01.944450
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:04.356916
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:06.788929
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:09.220124
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:11.638276
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:14.052909
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:16.468455
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:18.891919
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:21.308977
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:23.726205
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:26.148297
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:11:35.170485
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

# Generated at 2026-10-24 12:11:36.537809
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

# Generated at 2026-10-24 12:11:37.909824
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

# Generated at 2026-10-24 12:11:39.268546
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

# Generated at 2026-10-24 12:11:40.652150
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

# Generated at 2026-10-24 12:11:41.986286
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

# Generated at 2026-10-24 12:11:43.305200
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

# Generated at 2026-10-24 12:11:44.624323
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

# Generated at 2026-10-24 12:11:45.956109
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

# Generated at 2026-10-24 12:11:47.276593
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

# Generated at 2026-10-24 12:12:09.350366
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:11.767722
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:14.186171
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:16.604395
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:19.024201
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:21.671051
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:24.098221
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:26.513688
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:28.943615
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:31.358620
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:33.775735
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:36.189773
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:38.605870
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:41.022922
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:43.440785
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:45.860407
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:48.275709
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:50.692479
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:53.109615
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:55.525755
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:12:57.941145
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:00.362062
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:02.779786
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:05.202254
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:07.617907
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:10.035124
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:12.455409
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:14.872596
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:17.290937
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:13:19.708104
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:14.290669
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:16.742492
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:19.179304
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:21.631442
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:24.077556
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:26.497921
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:28.928682
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:31.338477
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:33.758371
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:36.176194
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:38.595109
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:41.016549
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:43.434288
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:45.852913
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:48.272650
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:50.691754
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:53.113591
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:55.536098
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:14:57.954233
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:00.375049
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:02.803460
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:05.222845
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:07.641570
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:10.061977
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:12.480727
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:14.910889
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:17.327614
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:19.749079
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:22.168322
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 12:15:24.587519
# Unit test for method try_utime of class PostProcessor