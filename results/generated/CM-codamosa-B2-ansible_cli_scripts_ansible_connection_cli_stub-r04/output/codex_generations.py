

# Generated at 2026-10-24 15:54:17.401454
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 15:54:19.812877
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 15:54:22.225876
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 15:54:24.932178
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 15:54:27.344448
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 15:54:29.757151
# Unit test for method connect_timeout of class ConnectionProcess

# Generated at 2026-10-24 15:54:32.170530
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 15:54:34.584282
# Unit test for constructor of class ConnectionProcess

# Generated at 2026-10-24 15:54:55.119733
# Unit test for constructor of class ConnectionProcess
def test_ConnectionProcess():fd_obj = object()

# Generated at 2026-10-24 15:55:40.603005
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:17.437952
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:19.850860
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:22.263726
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-24 15:56:24.677099
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-24 15:56:27.089888
# Unit test for method handler of class ConnectionProcess

# Generated at 2026-10-24 15:56:29.557736
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:31.970695
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:34.383309
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:36.795325
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:39.208759
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:41.621203
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:56:44.603063
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:57:05.020259
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-24 15:57:22.889996
# Unit test for method run of class ConnectionProcess

# Generated at 2026-10-24 15:57:25.768493
# Unit test for method run of class ConnectionProcess
def test_ConnectionProcess_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-24 15:58:04.895717
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 15:59:08.783173
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 15:59:13.597910
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 15:59:59.678542
# Unit test for function file_lock

# Generated at 2026-10-24 16:00:07.979913
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-24 16:00:58.761951
# Unit test for function main

# Generated at 2026-10-24 16:02:11.773104
# Unit test for function main

# Generated at 2026-10-24 16:02:50.261666
# Unit test for function main

# Generated at 2026-10-24 16:02:53.144747
# Unit test for function file_lock

# Generated at 2026-10-24 16:03:10.256606
# Unit test for function file_lock
def test_file_lock():import os

# Generated at 2026-10-24 16:03:29.294036
# Unit test for function read_stream
def test_read_stream():import hashlib
import io
import pytest

from ansible.executor.pipelining import read_stream  # adjust import to where read_stream lives


def _frame(escaped_data, hash_line=None, declared_size=None, truncate_data=False):
    """Build a stream in read_stream's wire format."""
    size = declared_size if declared_size is not None else len(escaped_data)
    payload = b'%d\n' % size + escaped_data
    if truncate_data:
        payload = payload[:size - 1]  # fewer bytes than declared
    payload += (hash_line or hashlib.sha1(escaped_data).hexdigest()).encode() + b'\n'
    return io.BytesIO(payload)


def test_read_stream_roundtrip():
    data = b'hello world\nsecond line'
    assert module_0.read_stream(_frame(data)) == data


def test_read_stream_empty_payload():
    assert module_0.read_stream(_frame(b'')) == b''


def test_read_stream_unescapes_carriage_returns():
    # \r on the wire is escaped as backslash-r; hash covers the ESCAPED bytes
    raw = b'line1\\rline2'                # escaped form on the wire
    stream = _frame(raw)
    assert module_0.read_stream(stream) == b'line1\rline2'


def test_read_stream_truncated_data_raises():
    stream = _frame(b'abc', declared_size=10, truncate_data=True)
    with pytest.raises(Exception, match='EOF found before data was complete'):
        module_0.read_stream(stream)


def test_read_stream_checksum_mismatch_raises():
    stream = _frame(b'hello', hash_line='0' * 40)
    with pytest.raises(Exception, match='did not match checksum'):
        module_0.read_stream(stream)


def test_read_stream_binary_payload():
    data = bytes(range(256))
    assert module_0.read_stream(_frame(data)) == data

# Generated at 2026-10-24 16:03:32.156557
# Unit test for function main

# Generated at 2026-10-24 16:03:34.572126
# Unit test for function main

# Generated at 2026-10-24 16:03:36.985019
# Unit test for function main

# Generated at 2026-10-24 16:03:39.927298
# Unit test for function read_stream

# Generated at 2026-10-24 16:03:42.339842
# Unit test for function read_stream

# Generated at 2026-10-24 16:03:44.752878
# Unit test for function read_stream

# Generated at 2026-10-24 16:03:47.261700
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 16:03:49.674462
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 16:03:52.087936
# Unit test for method start of class ConnectionProcess

# Generated at 2026-10-24 16:04:26.289795
# Unit test for method run of class ConnectionProcess