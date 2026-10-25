# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

import pytest

from youtube_dl.socks import (
    Proxy,
    ProxyType,
    SOCKS5_USER_AUTH_SUCCESS,
    SOCKS5_USER_AUTH_VERSION,
    SOCKS5_VERSION,
    Socks5Auth,
    Socks5Error,
    sockssocket,
)


@pytest.fixture
def make_socks_socket():
    sockets = []

    def make(username=None, password=None):
        sock = sockssocket()
        sock._proxy = Proxy(
            ProxyType.SOCKS5,
            "proxy.example",
            1080,
            username,
            password,
            True,
        )
        sockets.append(sock)
        return sock

    yield make

    for sock in sockets:
        sock.close()


def install_fake_io(monkeypatch, replies):
    sent_packets = []
    requested_lengths = []
    replies = iter(replies)

    def fake_sendall(self, packet):
        sent_packets.append(packet)

    def fake_recv_bytes(self, length):
        requested_lengths.append(length)
        return next(replies)

    monkeypatch.setattr(sockssocket, "sendall", fake_sendall)
    monkeypatch.setattr(sockssocket, "_recv_bytes", fake_recv_bytes)
    return sent_packets, requested_lengths


def test_socks5_auth_without_credentials_uses_no_auth(
        monkeypatch, make_socks_socket):
    sock = make_socks_socket()
    sent_packets, requested_lengths = install_fake_io(
        monkeypatch,
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    )

    sock._socks5_auth()

    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert requested_lengths == [2]
    assert sock.fileno() != -1


def test_socks5_auth_with_credentials_succeeds(
        monkeypatch, make_socks_socket):
    sock = make_socks_socket("usér", "päss")
    sent_packets, requested_lengths = install_fake_io(
        monkeypatch,
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS),
        ],
    )

    sock._socks5_auth()

    username = "usér".encode("utf-8")
    password = "päss".encode("utf-8")
    assert sent_packets == [
        bytes((
            SOCKS5_VERSION,
            2,
            Socks5Auth.AUTH_NONE,
            Socks5Auth.AUTH_USER_PASS,
        )),
        (
            bytes((SOCKS5_USER_AUTH_VERSION, len(username)))
            + username
            + bytes((len(password),))
            + password
        ),
    ]
    assert requested_lengths == [2, 2]
    assert sock.fileno() != -1


def test_socks5_auth_rejects_no_acceptable_method(
        monkeypatch, make_socks_socket):
    sock = make_socks_socket()
    sent_packets, requested_lengths = install_fake_io(
        monkeypatch,
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE)],
    )

    with pytest.raises(Socks5Error) as exc_info:
        sock._socks5_auth()

    assert exc_info.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert requested_lengths == [2]
    assert sock.fileno() == -1


@pytest.mark.parametrize(
    ("username", "password"),
    [
        (None, "password"),
        ("username", None),
    ],
)
def test_socks5_auth_rejects_userpass_when_credentials_are_incomplete(
        monkeypatch, make_socks_socket, username, password):
    sock = make_socks_socket(username, password)
    sent_packets, requested_lengths = install_fake_io(
        monkeypatch,
        [(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    )

    with pytest.raises(Socks5Error) as exc_info:
        sock._socks5_auth()

    assert exc_info.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert sent_packets == [
        bytes((SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)),
    ]
    assert requested_lengths == [2]
    assert sock.fileno() == -1


def test_socks5_auth_closes_socket_when_userpass_authentication_fails(
        monkeypatch, make_socks_socket):
    sock = make_socks_socket("username", "password")
    sent_packets, requested_lengths = install_fake_io(
        monkeypatch,
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, 1),
        ],
    )

    with pytest.raises(Socks5Error) as exc_info:
        sock._socks5_auth()

    assert exc_info.value.args[0] == Socks5Error.ERR_GENERAL_FAILURE
    assert sent_packets == [
        bytes((
            SOCKS5_VERSION,
            2,
            Socks5Auth.AUTH_NONE,
            Socks5Auth.AUTH_USER_PASS,
        )),
        (
            bytes((SOCKS5_USER_AUTH_VERSION, len(b"username")))
            + b"username"
            + bytes((len(b"password"),))
            + b"password"
        ),
    ]
    assert requested_lengths == [2, 2]
    assert sock.fileno() == -1
