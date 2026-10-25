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
def socks5_auth_socket(monkeypatch):
    sock = sockssocket()
    sent_packets = []
    replies = []
    receive_sizes = []
    closed = []

    def sendall(self, packet):
        sent_packets.append(packet)

    def recv_bytes(self, count):
        receive_sizes.append(count)
        return replies.pop(0)

    def close(self):
        closed.append(self)

    monkeypatch.setattr(sockssocket, "sendall", sendall)
    monkeypatch.setattr(sockssocket, "_recv_bytes", recv_bytes)
    monkeypatch.setattr(sockssocket, "close", close)

    try:
        yield sock, sent_packets, replies, receive_sizes, closed
    finally:
        socket.socket.close(sock)


def test_socks5_auth_without_credentials(
        socks5_auth_socket):
    sock, sent_packets, replies, receive_sizes, closed = socks5_auth_socket
    sock._proxy = SimpleNamespace(username=None, password=None)
    replies.append((SOCKS5_VERSION, Socks5Auth.AUTH_NONE))

    sock._socks5_auth()

    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert receive_sizes == [2]
    assert replies == []
    assert closed == []


def test_socks5_auth_with_username_and_password(
        socks5_auth_socket):
    sock, sent_packets, replies, receive_sizes, closed = socks5_auth_socket
    username = "usér"
    password = "päss"
    sock._proxy = SimpleNamespace(username=username, password=password)
    replies.extend([
        (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
        (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS),
    ])

    sock._socks5_auth()

    encoded_username = username.encode("utf-8")
    encoded_password = password.encode("utf-8")
    assert sent_packets == [
        bytes((
            SOCKS5_VERSION,
            2,
            Socks5Auth.AUTH_NONE,
            Socks5Auth.AUTH_USER_PASS,
        )),
        (
            bytes((SOCKS5_USER_AUTH_VERSION, len(encoded_username)))
            + encoded_username
            + bytes((len(encoded_password),))
            + encoded_password
        ),
    ]
    assert receive_sizes == [2, 2]
    assert replies == []
    assert closed == []


def test_socks5_auth_rejects_no_acceptable_method(
        socks5_auth_socket):
    sock, sent_packets, replies, receive_sizes, closed = socks5_auth_socket
    sock._proxy = SimpleNamespace(username=None, password=None)
    replies.append((SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE))

    with pytest.raises(Socks5Error) as exc_info:
        sock._socks5_auth()

    assert exc_info.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert receive_sizes == [2]
    assert replies == []
    assert closed == [sock]


@pytest.mark.parametrize(
    ("username", "password"),
    [
        (None, "password"),
        ("username", None),
    ],
)
def test_socks5_auth_rejects_user_password_method_when_credentials_incomplete(
        socks5_auth_socket, username, password):
    sock, sent_packets, replies, receive_sizes, closed = socks5_auth_socket
    sock._proxy = SimpleNamespace(username=username, password=password)
    replies.append((SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS))

    with pytest.raises(Socks5Error) as exc_info:
        sock._socks5_auth()

    assert exc_info.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert receive_sizes == [2]
    assert replies == []
    assert closed == [sock]


def test_socks5_auth_closes_socket_when_user_password_authentication_fails(
        socks5_auth_socket):
    sock, sent_packets, replies, receive_sizes, closed = socks5_auth_socket
    username = "username"
    password = "password"
    sock._proxy = SimpleNamespace(username=username, password=password)
    replies.extend([
        (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
        (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS + 1),
    ])

    with pytest.raises(Socks5Error) as exc_info:
        sock._socks5_auth()

    encoded_username = username.encode("utf-8")
    encoded_password = password.encode("utf-8")
    assert exc_info.value.args[0] == Socks5Error.ERR_GENERAL_FAILURE
    assert sent_packets == [
        bytes((
            SOCKS5_VERSION,
            2,
            Socks5Auth.AUTH_NONE,
            Socks5Auth.AUTH_USER_PASS,
        )),
        (
            bytes((SOCKS5_USER_AUTH_VERSION, len(encoded_username)))
            + encoded_username
            + bytes((len(encoded_password),))
            + encoded_password
        ),
    ]
    assert receive_sizes == [2, 2]
    assert replies == []
    assert closed == [sock]
