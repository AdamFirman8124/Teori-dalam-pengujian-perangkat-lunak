# file: project/youtube_dl/socks.py:121-128
# asked: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}
# gained: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}

import socket

import pytest

from youtube_dl.socks import sockssocket


@pytest.fixture
def fake_socket(monkeypatch):
    """Create a sockssocket whose recv returns queued chunks without any I/O."""
    sock = sockssocket()
    chunks = []

    def fake_recv(bufsize):
        if not chunks:
            return b''
        return chunks.pop(0)

    monkeypatch.setattr(sock, 'recv', fake_recv)
    monkeypatch.setattr(sock, 'close', lambda: None)
    return sock, chunks


def test_recvall_single_chunk(fake_socket):
    sock, chunks = fake_socket
    chunks.append(b'hello')
    assert sock.recvall(5) == b'hello'


def test_recvall_multiple_chunks_accumulated(fake_socket):
    sock, chunks = fake_socket
    chunks.extend([b'ab', b'cde', b'f'])
    assert sock.recvall(6) == b'abcdef'


def test_recvall_exact_size_no_extra_recv(fake_socket):
    sock, chunks = fake_socket
    chunks.append(b'xyz')
    assert sock.recvall(3) == b'xyz'
    # recv must not be called again once cnt bytes were received
    assert chunks == []


def test_recvall_empty_request_returns_immediately(fake_socket):
    sock, chunks = fake_socket
    assert sock.recvall(0) == b''
    assert chunks == []


def test_recvall_raises_eof_on_premature_close(fake_socket):
    sock, chunks = fake_socket
    chunks.append(b'ab')  # only 2 of 5 bytes, then recv returns b'' (EOF)
    with pytest.raises(EOFError) as excinfo:
        sock.recvall(5)
    assert '3 bytes missing' in str(excinfo.value)


def test_recvall_raises_eof_on_immediate_close(fake_socket):
    sock, chunks = fake_socket
    with pytest.raises(EOFError) as excinfo:
        sock.recvall(4)
    assert '4 bytes missing' in str(excinfo.value)
