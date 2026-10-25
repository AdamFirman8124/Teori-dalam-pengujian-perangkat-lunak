# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

import socket
from types import SimpleNamespace

import pytest

from youtube_dl.socks import (
    SOCKS5_USER_AUTH_SUCCESS,
    SOCKS5_USER_AUTH_VERSION,
    SOCKS5_VERSION,
    Socks5Auth,
    Socks5Error,
    sockssocket,
)


@pytest.fixture
def socks_socket():
    instance = sockssocket()
    try:
        yield instance
    finally:
        socket.socket.close(instance)


def _install_io(monkeypatch, replies):
    sent_packets = []
    requested_sizes = []
    reply_iterator = iter(replies)

    def fake_sendall(self, packet):
        sent_packets.append(packet)

    def fake_recv_bytes(self, count):
        requested_sizes.append(count)
        return next(reply_iterator)

    monkeypatch.setattr(sockssocket, "sendall", fake_sendall)
    monkeypatch.setattr(sockssocket, "_recv_bytes", fake_recv_bytes)
    return sent_packets, requested_sizes


def test_socks5_auth_without_credentials_uses_no_auth(
        monkeypatch, socks_socket):
    socks_socket._proxy = SimpleNamespace(username=None, password=None)
    sent_packets, requested_sizes = _install_io(
        monkeypatch,
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    )

    result = socks_socket._socks5_auth()

    assert result is None
    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert requested_sizes == [2]


def test_socks5_auth_with_credentials_succeeds(
        monkeypatch, socks_socket):
    username = "usér"
    password = "päss"
    username_bytes = username.encode("utf-8")
    password_bytes = password.encode("utf-8")
    socks_socket._proxy = SimpleNamespace(
        username=username,
        password=password,
    )
    sent_packets, requested_sizes = _install_io(
        monkeypatch,
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS),
        ],
    )

    result = socks_socket._socks5_auth()

    assert result is None
    assert sent_packets == [
        bytes((
            SOCKS5_VERSION,
            2,
            Socks5Auth.AUTH_NONE,
            Socks5Auth.AUTH_USER_PASS,
        )),
        (
            bytes((SOCKS5_USER_AUTH_VERSION, len(username_bytes)))
            + username_bytes
            + bytes((len(password_bytes),))
            + password_bytes
        ),
    ]
    assert requested_sizes == [2, 2]


def test_socks5_auth_rejects_no_acceptable_method(
        monkeypatch, socks_socket):
    socks_socket._proxy = SimpleNamespace(username=None, password=None)
    sent_packets, requested_sizes = _install_io(
        monkeypatch,
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE)],
    )
    closed = []
    monkeypatch.setattr(
        sockssocket,
        "close",
        lambda self: closed.append(self),
    )

    with pytest.raises(Socks5Error) as raised:
        socks_socket._socks5_auth()

    assert raised.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert closed == [socks_socket]
    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert requested_sizes == [2]


@pytest.mark.parametrize(
    ("username", "password"),
    [
        (None, "password"),
        ("username", None),
    ],
)
def test_socks5_auth_rejects_user_password_method_when_credentials_missing(
        monkeypatch, socks_socket, username, password):
    socks_socket._proxy = SimpleNamespace(
        username=username,
        password=password,
    )
    sent_packets, requested_sizes = _install_io(
        monkeypatch,
        [(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    )
    closed = []
    monkeypatch.setattr(
        sockssocket,
        "close",
        lambda self: closed.append(self),
    )

    with pytest.raises(Socks5Error) as raised:
        socks_socket._socks5_auth()

    assert raised.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert closed == [socks_socket]
    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert requested_sizes == [2]


def test_socks5_auth_closes_and_raises_when_user_authentication_fails(
        monkeypatch, socks_socket):
    username = "username"
    password = "password"
    socks_socket._proxy = SimpleNamespace(
        username=username,
        password=password,
    )
    sent_packets, requested_sizes = _install_io(
        monkeypatch,
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, 1),
        ],
    )
    closed = []
    monkeypatch.setattr(
        sockssocket,
        "close",
        lambda self: closed.append(self),
    )

    with pytest.raises(Socks5Error) as raised:
        socks_socket._socks5_auth()

    assert raised.value.args[0] == Socks5Error.ERR_GENERAL_FAILURE
    assert closed == [socks_socket]
    assert sent_packets == [
        bytes((
            SOCKS5_VERSION,
            2,
            Socks5Auth.AUTH_NONE,
            Socks5Auth.AUTH_USER_PASS,
        )),
        (
            bytes((SOCKS5_USER_AUTH_VERSION, len(username)))
            + username.encode("utf-8")
            + bytes((len(password),))
            + password.encode("utf-8")
        ),
    ]
    assert requested_sizes == [2, 2]
