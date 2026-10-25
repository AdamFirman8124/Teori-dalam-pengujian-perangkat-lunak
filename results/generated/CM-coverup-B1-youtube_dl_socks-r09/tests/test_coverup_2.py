# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

import socket
import struct

import pytest

from youtube_dl.socks import (
    SOCKS5_USER_AUTH_SUCCESS,
    SOCKS5_USER_AUTH_VERSION,
    SOCKS5_VERSION,
    Socks5Auth,
    Socks5Error,
    sockssocket,
)


class _FakeProxy(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


def _make_socket(monkeypatch, responses, username=None, password=None):
    """Build an unconnected sockssocket with all I/O stubbed out."""
    sock = sockssocket()
    sock._proxy = _FakeProxy(username, password)
    sent = []
    closed = []
    checked = []
    responses = list(responses)

    monkeypatch.setattr(sock, 'sendall', lambda data: sent.append(data))
    monkeypatch.setattr(sock, 'close', lambda: closed.append(True))
    monkeypatch.setattr(
        sock, '_check_response_version',
        lambda expected, got: checked.append((expected, got)))
    monkeypatch.setattr(sock, '_recv_bytes', lambda cnt: responses.pop(0))
    return sock, sent, closed, checked


def test_socks5_auth_no_credentials_selects_none(monkeypatch):
    sock, sent, closed, checked = _make_socket(
        monkeypatch, [(SOCKS5_VERSION, Socks5Auth.AUTH_NONE)])
    try:
        sock._socks5_auth()
    finally:
        socket.socket.close(sock)

    assert sent == [
        struct.pack('!BBB', SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)]
    assert checked == [(SOCKS5_VERSION, SOCKS5_VERSION)]
    assert closed == []


def test_socks5_auth_user_pass_success(monkeypatch):
    sock, sent, closed, checked = _make_socket(
        monkeypatch,
        [(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
         (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS)],
        username='user', password='pass')
    try:
        sock._socks5_auth()
    finally:
        socket.socket.close(sock)

    assert sent[0] == struct.pack(
        '!BBBB', SOCKS5_VERSION, 2,
        Socks5Auth.AUTH_NONE, Socks5Auth.AUTH_USER_PASS)
    assert sent[1] == (
        struct.pack('!B', SOCKS5_USER_AUTH_VERSION)
        + b'\x04user' + b'\x04pass')
    assert checked == [
        (SOCKS5_VERSION, SOCKS5_VERSION),
        (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_VERSION)]
    assert closed == []


def test_socks5_auth_no_acceptable_method(monkeypatch):
    sock, sent, closed, checked = _make_socket(
        monkeypatch, [(SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE)])
    try:
        with pytest.raises(Socks5Error):
            sock._socks5_auth()
    finally:
        socket.socket.close(sock)

    assert closed == [True]
    assert len(sent) == 1


def test_socks5_auth_user_pass_without_credentials(monkeypatch):
    sock, sent, closed, checked = _make_socket(
        monkeypatch, [(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)])
    try:
        with pytest.raises(Socks5Error):
            sock._socks5_auth()
    finally:
        socket.socket.close(sock)

    assert closed == [True]
    assert len(sent) == 1


def test_socks5_auth_user_pass_with_username_only(monkeypatch):
    sock, sent, closed, checked = _make_socket(
        monkeypatch, [(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
        username='user', password=None)
    try:
        with pytest.raises(Socks5Error):
            sock._socks5_auth()
    finally:
        socket.socket.close(sock)

    assert closed == [True]
    assert len(sent) == 1


def test_socks5_auth_user_pass_rejected(monkeypatch):
    sock, sent, closed, checked = _make_socket(
        monkeypatch,
        [(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
         (SOCKS5_USER_AUTH_VERSION, 1)],
        username='user', password='pass')
    try:
        with pytest.raises(Socks5Error):
            sock._socks5_auth()
    finally:
        socket.socket.close(sock)

    assert closed == [True]
    assert len(sent) == 2
