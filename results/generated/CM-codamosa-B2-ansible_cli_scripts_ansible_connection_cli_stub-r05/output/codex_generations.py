

# Generated at 2026-10-24 10:44:41.409655
# Unit test for function read_stream
def test_read_stream():
    import io

    # valid payload round-trips
    payload = b'hello world'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        hashlib.sha1(payload).hexdigest().encode() + b'\n'
    )
    assert module_0.read_stream(stream) == payload

    # escaped literal \r sequences are restored to real carriage returns
    payload = b'a\\rb'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        hashlib.sha1(payload).hexdigest().encode() + b'\n'
    )
    assert module_0.read_stream(stream) == b'a\rb'

    # checksum mismatch raises
    payload = b'data'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        b'0' * 40 + b'\n'
    )
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'did not match checksum' in str(e)
    else:
        raise AssertionError('expected checksum mismatch error')

    # truncated payload raises EOF error
    stream = io.BytesIO(b'10\nshort\n')
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'EOF found before data was complete' in str(e)
    else:
        raise AssertionError('expected EOF error')

# Generated at 2026-10-24 10:44:59.295426
# Unit test for function read_stream

# Generated at 2026-10-24 10:45:01.712497
# Unit test for function read_stream

# Generated at 2026-10-24 10:45:04.146260
# Unit test for function read_stream

# Generated at 2026-10-24 10:45:06.564692
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:45:08.981306
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:45:50.298205
# Unit test for method connect_timeout of class ConnectionProcess
def test_ConnectionProcess_connect_timeout():from unittest.mock import MagicMock

# Generated at 2026-10-24 10:45:52.719044
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 10:45:55.232408
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 10:45:57.650147
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 10:46:00.065510
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:46:02.484039
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:46:04.902927
# Unit test for method command_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:46:10.700242
# Unit test for function file_lock

# Generated at 2026-10-24 10:46:13.117877
# Unit test for function file_lock

# Generated at 2026-10-24 10:46:31.903611
# Unit test for function file_lock
def test_file_lock():
    import subprocess
    import tempfile
    import textwrap

    lock_path = os.path.join(tempfile.mkdtemp(), 'test.lock')

    probe = textwrap.dedent('''
        import fcntl, sys
        fd = open(sys.argv[1], 'a+')
        try:
            fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            sys.exit(1)
        sys.exit(0)
    ''')

    # while the lock is held, the lock file exists and another
    # process must fail to acquire it
    with module_0.file_lock(lock_path) as lock_result:
        assert lock_result is None
        assert os.path.exists(lock_path)
        rc = subprocess.call([sys.executable, '-c', probe, lock_path])
        assert rc == 1

    # after the with block the lock is released, so another
    # process must now be able to acquire it
    rc = subprocess.call([sys.executable, '-c', probe, lock_path])
    assert rc == 0

# Generated at 2026-10-24 10:47:05.564000
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:47:07.983272
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:47:10.397636
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:47:12.823770
# Unit test for function file_lock

# Generated at 2026-10-24 10:47:15.242607
# Unit test for function file_lock

# Generated at 2026-10-24 10:47:17.659062
# Unit test for function file_lock

# Generated at 2026-10-24 10:47:20.077365
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:47:22.495025
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:47:24.912991
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:47:27.333542
# Unit test for function main

# Generated at 2026-10-24 10:47:29.756490
# Unit test for function main

# Generated at 2026-10-24 10:47:32.202591
# Unit test for function main

# Generated at 2026-10-24 10:47:34.612102
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:47:37.036297
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:47:39.454851
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:47:41.871647
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:47:44.292347
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:48:03.968798
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:48:28.730000
# Unit test for function file_lock
def test_file_lock():import fcntl
import os
import subprocess
import sys
import tempfile
import textwrap

import pytest

# adjust import to wherever file_lock lives in your tree
from ansible.cli.conn import file_lock


def _child_try_lock(lock_path):
    """Run in a subprocess: exit 0 if lock acquired, 1 if blocked."""
    script = textwrap.dedent("""
        import fcntl, os, sys
        fd = os.open(sys.argv[1], os.O_RDWR | os.O_CREAT, 0o600)
        try:
            fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            sys.exit(0)
        except IOError:
            sys.exit(1)
        finally:
            os.close(fd)
    """)
    return subprocess.call([sys.executable, "-c", script, lock_path])


def test_file_lock_creates_lock_file():
    with tempfile.TemporaryDirectory() as d:
        lock_path = os.path.join(d, "ansible-connection.lock")
        with module_0.file_lock(lock_path):
            assert os.path.exists(lock_path)
            assert os.stat(lock_path).st_mode & 0o777 == 0o600


def test_file_lock_blocks_other_processes():
    with tempfile.TemporaryDirectory() as d:
        lock_path = os.path.join(d, "ansible-connection.lock")
        with module_0.file_lock(lock_path):
            # another process must NOT be able to take the lock
            assert _child_try_lock(lock_path) == 1
        # after release, it can
        assert _child_try_lock(lock_path) == 0


def test_file_lock_reacquirable_after_release():
    with tempfile.TemporaryDirectory() as d:
        lock_path = os.path.join(d, "ansible-connection.lock")
        with module_0.file_lock(lock_path):
            pass
        with module_0.file_lock(lock_path):  # must not raise
            pass

# Generated at 2026-10-24 10:48:31.151218
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:33.573450
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:36.093575
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:38.512942
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:40.930200
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:43.347837
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:45.910639
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:48.324501
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:50.739141
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 10:48:53.158923
# Unit test for function read_stream

# Generated at 2026-10-24 10:48:55.575685
# Unit test for function read_stream

# Generated at 2026-10-24 10:48:57.993932
# Unit test for function read_stream

# Generated at 2026-10-24 10:49:00.409097
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:49:02.827379
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:49:05.244476
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:49:07.664031
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:49:10.081070
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:49:12.493107
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:49:14.909485
# Unit test for function main

# Generated at 2026-10-24 10:49:17.324120
# Unit test for function main

# Generated at 2026-10-24 10:49:19.742400
# Unit test for function main

# Generated at 2026-10-24 10:49:22.158248
# Unit test for function file_lock

# Generated at 2026-10-24 10:49:24.574295
# Unit test for function file_lock

# Generated at 2026-10-24 10:49:26.988802
# Unit test for function file_lock

# Generated at 2026-10-24 10:49:29.408897
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:49:31.825626
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:49:34.244000
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:49:36.663375
# Unit test for function main

# Generated at 2026-10-24 10:49:39.080178
# Unit test for function main

# Generated at 2026-10-24 10:49:41.497826
# Unit test for function main

# Generated at 2026-10-24 10:49:43.912796
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:49:46.329694
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:49:48.756715
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:49:51.174431
# Unit test for function file_lock

# Generated at 2026-10-24 10:49:53.592092
# Unit test for function file_lock

# Generated at 2026-10-24 10:49:56.012455
# Unit test for function file_lock

# Generated at 2026-10-24 10:50:01.003637
# Unit test for function file_lock

# Generated at 2026-10-24 10:50:03.419034
# Unit test for function file_lock

# Generated at 2026-10-24 10:50:05.836331
# Unit test for function file_lock

# Generated at 2026-10-24 10:50:08.258035
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:10.671468
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:13.090037
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:15.508614
# Unit test for function read_stream

# Generated at 2026-10-24 10:50:17.932900
# Unit test for function read_stream

# Generated at 2026-10-24 10:50:20.346256
# Unit test for function read_stream

# Generated at 2026-10-24 10:50:22.761595
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:25.178317
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:27.595707
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:30.013431
# Unit test for function file_lock

# Generated at 2026-10-24 10:50:32.428877
# Unit test for function file_lock

# Generated at 2026-10-24 10:50:34.846118
# Unit test for function file_lock

# Generated at 2026-10-24 10:50:37.264726
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:50:39.680699
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:50:42.099752
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:50:44.518111
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:46.935775
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:49.353649
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:50:51.771637
# Unit test for function main

# Generated at 2026-10-24 10:51:23.683346
# Unit test for function main

# Generated at 2026-10-24 10:51:26.104963
# Unit test for function main

# Generated at 2026-10-24 10:51:28.610960
# Unit test for function file_lock

# Generated at 2026-10-24 10:51:31.035511
# Unit test for function file_lock

# Generated at 2026-10-24 10:51:33.454190
# Unit test for function file_lock

# Generated at 2026-10-24 10:51:35.867417
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:51:38.435661
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:51:40.854570
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:51:49.859865
# Unit test for function read_stream

# Generated at 2026-10-24 10:51:52.277383
# Unit test for function read_stream

# Generated at 2026-10-24 10:51:54.696214
# Unit test for function read_stream

# Generated at 2026-10-24 10:51:57.113989
# Unit test for function main

# Generated at 2026-10-24 10:51:59.534196
# Unit test for function main

# Generated at 2026-10-24 10:52:01.949697
# Unit test for function main

# Generated at 2026-10-24 10:52:04.365754
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:06.781963
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:09.198714
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:11.617920
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:52:14.034050
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:52:16.451603
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:52:18.869840
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:21.286311
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:23.704827
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:26.122227
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:28.539545
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:30.956293
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 10:52:33.373550
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:52:35.788857
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:52:38.203786
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 10:52:40.619948
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:52:58.545014
# Unit test for method shutdown of class ConnectionProcess
def test_ConnectionProcess_shutdown():import os

# Generated at 2026-10-24 10:53:16.388060
# Unit test for function read_stream
def test_read_stream():
    import io

    # valid payload round-trips
    payload = b'hello world'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        hashlib.sha1(payload).hexdigest().encode() + b'\n'
    )
    assert module_0.read_stream(stream) == payload

    # escaped literal \r sequences are restored to real carriage returns
    payload = b'a\\rb'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        hashlib.sha1(payload).hexdigest().encode() + b'\n'
    )
    assert module_0.read_stream(stream) == b'a\rb'

    # checksum mismatch raises
    payload = b'data'
    stream = io.BytesIO(
        str(len(payload)).encode() + b'\n' +
        payload + b'\n' +
        b'0' * 40 + b'\n'
    )
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'did not match checksum' in str(e)
    else:
        raise AssertionError('expected checksum mismatch error')

    # truncated payload raises EOF error
    stream = io.BytesIO(b'10\nshort\n')
    try:
        module_0.read_stream(stream)
    except Exception as e:
        assert 'EOF found before data was complete' in str(e)
    else:
        raise AssertionError('expected EOF error')

# Generated at 2026-10-24 10:53:18.806290
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:53:21.222295
# Unit test for method shutdown of class ConnectionProcess

# Generated at 2026-10-24 10:53:23.734433
# Unit test for method shutdown of class ConnectionProcess