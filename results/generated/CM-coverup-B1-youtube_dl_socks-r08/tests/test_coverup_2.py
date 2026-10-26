# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

import socket

import pytest

from youtube_dl.socks import (
    SOCKS5_USER_AUTH_SUCCESS,
    SOCKS5_USER_AUTH_VERSION,
    SOCKS5_VERSION,
    InvalidVersionError,
    Proxy,
    Socks5Auth,
    Socks5Error,
    sockssocket,
)


def _make_socket(monkeypatch, username=None, password=None, recv_side_effect=None):
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    sent = []
    closed = []

    sock._proxy = Proxy(
        type=5,
        host="127.0.0.1",
        port=1080,
        username=username,
        password=password,
        remote_dns=True,
    )

    def fake_sendall(data):
        sent.append(data)

    def fake_close():
        closed.append(True)

    monkeypatch.setattr(sock, "sendall", fake_sendall)
    monkeypatch.setattr(sock, "close", fake_close)

    if recv_side_effect is not None:
        responses = iter(recv_side_effect)

        def fake_recv_bytes(cnt):
            result = next(responses)
            assert len(result) == cnt
            return result

        monkeypatch.setattr(sock, "_recv_bytes", fake_recv_bytes)

    return sock, sent, closed


def _cleanup(sock):
    try:
        socket.socket.close(sock)
    except Exception:
        pass


def _error_code(exc):
    # ProxyError.__init__(code, msg) -> socket.error args are (code, msg)
    if exc.args:
        return exc.args[0]
    return None


def test_socks5_auth_no_auth_no_credentials(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username=None,
        password=None,
        recv_side_effect=[(SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    )
    try:
        result = sock._socks5_auth()
        assert result is None
        assert sent == [b"\x05\x01\x00"]
        assert closed == []
    finally:
        _cleanup(sock)


def test_socks5_auth_no_auth_with_credentials_offered(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username="user",
        password="pass",
        recv_side_effect=[(SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    )
    try:
        result = sock._socks5_auth()
        assert result is None
        assert sent == [b"\x05\x02\x00\x02"]
        assert closed == []
    finally:
        _cleanup(sock)


def test_socks5_auth_user_pass_success(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username="user",
        password="pass",
        recv_side_effect=[
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS),
        ],
    )
    try:
        result = sock._socks5_auth()
        assert result is None
        assert len(sent) == 2
        assert sent[0] == b"\x05\x02\x00\x02"
        assert sent[1] == b"\x01\x04user\x04pass"
        assert closed == []
    finally:
        _cleanup(sock)


def test_socks5_auth_no_acceptable(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username="user",
        password="pass",
        recv_side_effect=[(SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE)],
    )
    try:
        with pytest.raises(Socks5Error) as excinfo:
            sock._socks5_auth()
        assert _error_code(excinfo.value) == Socks5Auth.AUTH_NO_ACCEPTABLE
        assert sent == [b"\x05\x02\x00\x02"]
        assert closed == [True]
    finally:
        _cleanup(sock)


def test_socks5_auth_user_pass_selected_without_credentials(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username=None,
        password=None,
        recv_side_effect=[(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    )
    try:
        with pytest.raises(Socks5Error) as excinfo:
            sock._socks5_auth()
        assert _error_code(excinfo.value) == Socks5Auth.AUTH_NO_ACCEPTABLE
        assert sent == [b"\x05\x01\x00"]
        assert closed == [True]
    finally:
        _cleanup(sock)


def test_socks5_auth_user_pass_selected_with_only_username(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username="user",
        password=None,
        recv_side_effect=[(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    )
    try:
        with pytest.raises(Socks5Error) as excinfo:
            sock._socks5_auth()
        assert _error_code(excinfo.value) == Socks5Auth.AUTH_NO_ACCEPTABLE
        assert sent == [b"\x05\x01\x00"]
        assert closed == [True]
    finally:
        _cleanup(sock)


def test_socks5_auth_user_pass_failure_status(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username="user",
        password="pass",
        recv_side_effect=[
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, 0x01),
        ],
    )
    try:
        with pytest.raises(Socks5Error) as excinfo:
            sock._socks5_auth()
        assert _error_code(excinfo.value) == Socks5Error.ERR_GENERAL_FAILURE
        assert len(sent) == 2
        assert sent[0] == b"\x05\x02\x00\x02"
        assert sent[1] == b"\x01\x04user\x04pass"
        assert closed == [True]
    finally:
        _cleanup(sock)


def test_socks5_auth_invalid_initial_version(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username=None,
        password=None,
        recv_side_effect=[(0x04, Socks5Auth.AUTH_NONE)],
    )
    try:
        with pytest.raises(InvalidVersionError):
            sock._socks5_auth()
        assert sent == [b"\x05\x01\x00"]
        assert closed == [True]
    finally:
        _cleanup(sock)


def test_socks5_auth_invalid_user_auth_version(monkeypatch):
    sock, sent, closed = _make_socket(
        monkeypatch,
        username="user",
        password="pass",
        recv_side_effect=[
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (0xFF, SOCKS5_USER_AUTH_SUCCESS),
        ],
    )
    try:
        with pytest.raises(InvalidVersionError):
            sock._socks5_auth()
        assert len(sent) == 2
        assert sent[1] == b"\x01\x04user\x04pass"
        assert closed == [True]
    finally:
        _cleanup(sock)
