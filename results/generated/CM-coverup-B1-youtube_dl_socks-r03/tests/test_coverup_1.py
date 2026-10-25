# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

from contextlib import contextmanager

import pytest

from youtube_dl.socks import (
    InvalidVersionError,
    Socks5Auth,
    Socks5Error,
    SOCKS5_USER_AUTH_SUCCESS,
    SOCKS5_USER_AUTH_VERSION,
    SOCKS5_VERSION,
    sockssocket,
)


class _FakeProxy(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


@contextmanager
def _make_socket(monkeypatch, proxy, responses):
    sock = sockssocket()
    real_close = sock.close
    sock._proxy = proxy

    sent = []
    closed = []
    recv_calls = []
    response_iter = iter(responses)

    def fake_sendall(data):
        sent.append(data)

    def fake_close():
        closed.append(True)

    def fake_recv_bytes(cnt):
        recv_calls.append(cnt)
        return next(response_iter)

    monkeypatch.setattr(sock, 'sendall', fake_sendall)
    monkeypatch.setattr(sock, 'close', fake_close)
    monkeypatch.setattr(sock, '_recv_bytes', fake_recv_bytes)

    try:
        yield sock, sent, closed, recv_calls
    finally:
        real_close()


def test_socks5_auth_no_auth_required(monkeypatch):
    with _make_socket(
        monkeypatch,
        _FakeProxy(),
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    ) as (sock, sent, closed, recv_calls):
        sock._socks5_auth()

        assert sent == [b'\x05\x01\x00']
        assert recv_calls == [2]
        assert closed == []


def test_socks5_auth_user_pass_success(monkeypatch):
    with _make_socket(
        monkeypatch,
        _FakeProxy(username='user', password='pass'),
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS),
        ],
    ) as (sock, sent, closed, recv_calls):
        sock._socks5_auth()

        assert sent == [
            b'\x05\x02\x00\x02',
            b'\x01\x04user\x04pass',
        ]
        assert recv_calls == [2, 2]
        assert closed == []


def test_socks5_auth_no_acceptable_method(monkeypatch):
    with _make_socket(
        monkeypatch,
        _FakeProxy(),
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE)],
    ) as (sock, sent, closed, recv_calls):
        with pytest.raises(Socks5Error) as excinfo:
            sock._socks5_auth()

        assert excinfo.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
        assert sent == [b'\x05\x01\x00']
        assert recv_calls == [2]
        assert closed == [True]


@pytest.mark.parametrize(
    'username,password',
    [
        (None, 'pass'),
        ('user', None),
    ],
)
def test_socks5_auth_user_pass_requested_without_credentials(
        monkeypatch, username, password):
    with _make_socket(
        monkeypatch,
        _FakeProxy(username=username, password=password),
        [(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    ) as (sock, sent, closed, recv_calls):
        with pytest.raises(Socks5Error) as excinfo:
            sock._socks5_auth()

        assert excinfo.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
        assert sent == [b'\x05\x01\x00']
        assert recv_calls == [2]
        assert closed == [True]


def test_socks5_auth_user_pass_rejected(monkeypatch):
    with _make_socket(
        monkeypatch,
        _FakeProxy(username='user', password='pass'),
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, 1),
        ],
    ) as (sock, sent, closed, recv_calls):
        with pytest.raises(Socks5Error) as excinfo:
            sock._socks5_auth()

        assert excinfo.value.args[0] == Socks5Error.ERR_GENERAL_FAILURE
        assert sent == [
            b'\x05\x02\x00\x02',
            b'\x01\x04user\x04pass',
        ]
        assert recv_calls == [2, 2]
        assert closed == [True]


def test_socks5_auth_bad_method_selection_version(monkeypatch):
    with _make_socket(
        monkeypatch,
        _FakeProxy(),
        [(SOCKS5_VERSION - 1, Socks5Auth.AUTH_NONE)],
    ) as (sock, sent, closed, recv_calls):
        with pytest.raises(InvalidVersionError):
            sock._socks5_auth()

        assert sent == [b'\x05\x01\x00']
        assert recv_calls == [2]
        assert closed == [True]


def test_socks5_auth_bad_user_auth_version(monkeypatch):
    with _make_socket(
        monkeypatch,
        _FakeProxy(username='user', password='pass'),
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION + 1, SOCKS5_USER_AUTH_SUCCESS),
        ],
    ) as (sock, sent, closed, recv_calls):
        with pytest.raises(InvalidVersionError):
            sock._socks5_auth()

        assert sent == [
            b'\x05\x02\x00\x02',
            b'\x01\x04user\x04pass',
        ]
        assert recv_calls == [2, 2]
        assert closed == [True]
