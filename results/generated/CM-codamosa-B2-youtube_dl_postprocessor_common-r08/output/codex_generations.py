

# Generated at 2026-10-24 21:23:36.613279
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:23:46.994838
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    err = AudioConversionError('ffmpeg exited with code 1')
    assert isinstance(err, PostProcessingError)
    assert isinstance(err, Exception)
    assert err.msg == 'ffmpeg exited with code 1'
    assert str(err) == 'ffmpeg exited with code 1'

# Generated at 2026-10-24 21:23:48.334797
# Unit test for constructor of class AudioConversionError
def test_AudioConversionError():
    err = AudioConversionError('ffmpeg exited with code 1')
    assert isinstance(err, PostProcessingError)
    assert isinstance(err, Exception)
    assert err.msg == 'ffmpeg exited with code 1'
    assert str(err) == 'ffmpeg exited with code 1'

# Generated at 2026-10-24 21:23:54.266922
# Unit test for constructor of class PostProcessor
def test_PostProcessor():
    # Constructor without a downloader
    post_processor = PostProcessor()
    assert post_processor._downloader is None

    # Constructor with a downloader
    downloader = object()
    post_processor = PostProcessor(downloader)
    assert post_processor._downloader is downloader

# Generated at 2026-10-24 21:23:56.687864
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:23:59.104432
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:01.523946
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:03.953566
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:06.374622
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:07.810473
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-24 21:24:09.214516
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:10.542020
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:11.867467
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:13.187252
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:14.557074
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:15.846416
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:17.304962
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:18.738878
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:20.073009
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:21.396911
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:22.723427
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:24.040861
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:25.374592
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:26.704513
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:24:29.235344
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:31.755181
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:34.174086
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:36.590308
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:39.007337
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:41.427248
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:43.841994
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:46.261297
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:48.677893
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:51.095445
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:53.512465
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:55.930283
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:24:58.501665
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:00.919069
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:03.334624
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:05.760811
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:08.171850
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:10.587160
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:13.002651
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:14.362393
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-24 21:25:15.742809
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:17.075031
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:18.438072
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:19.761002
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:21.125665
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:22.456647
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:23.772647
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:25.095329
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:26.431007
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:27.750281
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:29.075247
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:30.405479
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:31.725445
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:33.061907
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:25:35.696138
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:38.115983
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:40.633510
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:43.052230
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:45.473603
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:48.068389
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:50.487449
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:52.904243
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:55.326624
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:25:57.746700
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:00.166879
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:02.584581
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:05.002149
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:07.420265
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:09.836191
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:12.284517
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:14.670447
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:17.088262
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:19.508200
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:21.920509
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:24.339917
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:26.754565
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:29.172693
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:31.588668
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:34.009966
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:36.428139
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:38.845782
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:26:41.441601
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    from unittest.mock import patch, MagicMock

    pp = PostProcessor(downloader=MagicMock())

    # Success case: os.utime is called with the encoded filename and (atime, mtime)
    with patch('__main__.os.utime') as mock_utime:
        pp.try_utime('video.mp4', 1234567890.0, 1234567891.0)
        mock_utime.assert_called_once_with(
            encodeFilename('video.mp4'), (1234567890.0, 1234567891.0)
        )
        pp._downloader.report_warning.assert_not_called()

    # Failure case: exception is swallowed and errnote warning is reported
    with patch('__main__.os.utime', side_effect=OSError('permission denied')):
        pp.try_utime('broken.mp4', 1.0, 2.0, errnote='utime failed')
        pp._downloader.report_warning.assert_called_once_with('utime failed')

# Generated at 2026-10-24 21:26:42.769708
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:44.117484
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:45.446215
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:46.776542
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:50.176591
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:51.515059
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:52.857177
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:54.181584
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:55.512984
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:56.853291
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:58.235206
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:26:59.555007
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:27:01.976400
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:04.396315
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:06.964018
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:09.484341
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:11.900044
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:14.319094
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:21.261857
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:23.840059
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:26.258653
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:28.681584
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:31.098184
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:33.519837
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:35.933565
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:38.350913
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:40.770268
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:43.185863
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:45.601543
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:48.018377
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:50.438286
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:52.855553
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:55.275907
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:27:57.692632
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:28:00.112613
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:28:02.530388
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:28:04.949599
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:28:07.367102
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:28:09.782491
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:28:11.167977
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:12.591467
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:13.921724
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:24.390454
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:25.727137
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:27.047594
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:28.402653
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:29.731430
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:31.056291
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:32.383766
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:33.757314
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:35.148254
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:36.474473
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:57.175019
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:58.606918
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:28:59.940126
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:29:01.260701
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:29:02.657855
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:29:04.022380
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:29:05.359227
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:29:06.686616
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:29:08.019715
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:29:09.354223
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:29:50.742499
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:29:53.155745
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:30:10.585149
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():from unittest.mock import call, patch
import os

processor = PostProcessor()

with patch.object(os, 'utime') as mock_utime:
    result = processor.try_utime('audio.mp3', 100, 200)

assert result is None
assert mock_utime.call_args == call('audio.mp3', (100, 200))

# Generated at 2026-10-24 21:30:12.019569
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:30:13.352630
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:30:14.797813
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:30:16.115661
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:30:17.437311
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:30:18.753747
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:30:20.098014
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:30:21.474920
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:30:22.797828
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:31:50.396812
# Unit test for method try_utime of class PostProcessor

# Generated at 2026-10-24 21:31:51.725222
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():import os

# Generated at 2026-10-24 21:31:53.067999
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:31:54.429811
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:31:55.753867
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:31:57.074394
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:31:58.406076
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:31:59.733997
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:32:01.178897
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:32:02.611877
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings

# Generated at 2026-10-24 21:32:03.943922
# Unit test for method try_utime of class PostProcessor
def test_PostProcessor_try_utime():
    pp = PostProcessor(_FakeDownloader())

    # Success case: atime/mtime are written to the file
    path = '_test_utime_file'
    with open(path, 'w') as f:
        f.write('x')
    try:
        pp.try_utime(path, 1000, 2000)
        st = os.stat(path)
        assert int(st.st_atime) == 1000, 'atime not set: %r' % st.st_atime
        assert int(st.st_mtime) == 2000, 'mtime not set: %r' % st.st_mtime
    finally:
        os.remove(path)

    # Failure case: missing file -> no exception, warning reported instead
    pp.try_utime('_nonexistent_file_12345', 1, 2, errnote='custom warning')
    assert pp._downloader.warnings == ['custom warning'], pp._downloader.warnings