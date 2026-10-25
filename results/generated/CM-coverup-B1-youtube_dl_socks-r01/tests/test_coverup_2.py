# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

import pytest

from youtube_dl import socks


@pytest.fixture
def socket_factory():
    sockets = []

    def create(username=None, password=None):
        sock = socks.sockssocket()
        sock._proxy = socks.Proxy(
            None, "proxy.example", 1080, username, password, True
        )
        sockets.append(sock)
        return sock

    yield create

    for sock in sockets:
        sock.close()


def test_socks5_auth_without_credentials(monkeypatch, socket_factory):
    sock = socket_factory()
    sent_packets = []
    recv_sizes = []

    monkeypatch.setattr(
        socks.sockssocket,
        "sendall",
        lambda self, packet: sent_packets.append(packet),
    )

    def recv_bytes(self, size):
        recv_sizes.append(size)
        return socks.SOCKS5_VERSION, socks.Socks5Auth.AUTH_NONE

    monkeypatch.setattr(socks.sockssocket, "_recv_bytes", recv_bytes)

    result = sock._socks5_auth()

    assert result is None
    assert sent_packets == [
        bytes((socks.SOCKS5_VERSION, 1, socks.Socks5Auth.AUTH_NONE))
    ]
    assert recv_sizes == [2]
    assert sock.fileno() != -1


def test_socks5_auth_with_username_and_password(monkeypatch, socket_factory):
    username = "üser"
    password = "päss"
    sock = socket_factory(username, password)
    sent_packets = []
    responses = iter(
        [
            (socks.SOCKS5_VERSION, socks.Socks5Auth.AUTH_USER_PASS),
            (
                socks.SOCKS5_USER_AUTH_VERSION,
                socks.SOCKS5_USER_AUTH_SUCCESS,
            ),
        ]
    )
    recv_sizes = []

    monkeypatch.setattr(
        socks.sockssocket,
        "sendall",
        lambda self, packet: sent_packets.append(packet),
    )

    def recv_bytes(self, size):
        recv_sizes.append(size)
        return next(responses)

    monkeypatch.setattr(socks.sockssocket, "_recv_bytes", recv_bytes)

    result = sock._socks5_auth()

    encoded_username = username.encode("utf-8")
    encoded_password = password.encode("utf-8")
    assert result is None
    assert sent_packets == [
        bytes(
            (
                socks.SOCKS5_VERSION,
                2,
                socks.Socks5Auth.AUTH_NONE,
                socks.Socks5Auth.AUTH_USER_PASS,
            )
        ),
        (
            bytes((socks.SOCKS5_USER_AUTH_VERSION, len(encoded_username)))
            + encoded_username
            + bytes((len(encoded_password),))
            + encoded_password
        ),
    ]
    assert recv_sizes == [2, 2]
    assert list(responses) == []
    assert sock.fileno() != -1


def test_socks5_auth_rejects_no_acceptable_method(monkeypatch, socket_factory):
    sock = socket_factory()
    sent_packets = []

    monkeypatch.setattr(
        socks.sockssocket,
        "sendall",
        lambda self, packet: sent_packets.append(packet),
    )
    monkeypatch.setattr(
        socks.sockssocket,
        "_recv_bytes",
        lambda self, size: (
            socks.SOCKS5_VERSION,
            socks.Socks5Auth.AUTH_NO_ACCEPTABLE,
        ),
    )

    with pytest.raises(socks.Socks5Error) as exc_info:
        sock._socks5_auth()

    assert exc_info.value.args[0] == socks.Socks5Auth.AUTH_NO_ACCEPTABLE
    assert sent_packets == [
        bytes((socks.SOCKS5_VERSION, 1, socks.Socks5Auth.AUTH_NONE))
    ]
    assert sock.fileno() == -1


@pytest.mark.parametrize(
    ("username", "password"),
    [
        (None, None),
        ("username", None),
    ],
)
def test_socks5_auth_rejects_user_pass_when_credentials_are_incomplete(
    monkeypatch, socket_factory, username, password
):
    sock = socket_factory(username, password)
    sent_packets = []

    monkeypatch.setattr(
        socks.sockssocket,
        "sendall",
        lambda self, packet: sent_packets.append(packet),
    )
    monkeypatch.setattr(
        socks.sockssocket,
        "_recv_bytes",
        lambda self, size: (
            socks.SOCKS5_VERSION,
            socks.Socks5Auth.AUTH_USER_PASS,
        ),
    )

    with pytest.raises(socks.Socks5Error) as exc_info:
        sock._socks5_auth()

    assert exc_info.value.args[0] == socks.Socks5Auth.AUTH_NO_ACCEPTABLE
    assert sent_packets == [
        bytes((socks.SOCKS5_VERSION, 1, socks.Socks5Auth.AUTH_NONE))
    ]
    assert sock.fileno() == -1


def test_socks5_auth_rejects_failed_username_password_authentication(
    monkeypatch, socket_factory
):
    sock = socket_factory("username", "password")
    sent_packets = []
    responses = iter(
        [
            (socks.SOCKS5_VERSION, socks.Socks5Auth.AUTH_USER_PASS),
            (socks.SOCKS5_USER_AUTH_VERSION, 1),
        ]
    )

    monkeypatch.setattr(
        socks.sockssocket,
        "sendall",
        lambda self, packet: sent_packets.append(packet),
    )
    monkeypatch.setattr(
        socks.sockssocket,
        "_recv_bytes",
        lambda self, size: next(responses),
    )

    with pytest.raises(socks.Socks5Error) as exc_info:
        sock._socks5_auth()

    assert exc_info.value.args[0] == socks.Socks5Error.ERR_GENERAL_FAILURE
    assert sent_packets == [
        bytes(
            (
                socks.SOCKS5_VERSION,
                2,
                socks.Socks5Auth.AUTH_NONE,
                socks.Socks5Auth.AUTH_USER_PASS,
            )
        ),
        (
            bytes((socks.SOCKS5_USER_AUTH_VERSION, len(b"username")))
            + b"username"
            + bytes((len(b"password"),))
            + b"password"
        ),
    ]
    assert list(responses) == []
    assert sock.fileno() == -1


def test_socks5_auth_rejects_invalid_negotiation_version(
    monkeypatch, socket_factory
):
    sock = socket_factory()
    sent_packets = []

    monkeypatch.setattr(
        socks.sockssocket,
        "sendall",
        lambda self, packet: sent_packets.append(packet),
    )
    monkeypatch.setattr(
        socks.sockssocket,
        "_recv_bytes",
        lambda self, size: (
            socks.SOCKS5_VERSION + 1,
            socks.Socks5Auth.AUTH_NONE,
        ),
    )

    with pytest.raises(socks.InvalidVersionError):
        sock._socks5_auth()

    assert sent_packets == [
        bytes((socks.SOCKS5_VERSION, 1, socks.Socks5Auth.AUTH_NONE))
    ]
    assert sock.fileno() == -1


def test_socks5_auth_rejects_invalid_user_auth_version(
    monkeypatch, socket_factory
):
    sock = socket_factory("username", "password")
    sent_packets = []
    responses = iter(
        [
            (socks.SOCKS5_VERSION, socks.Socks5Auth.AUTH_USER_PASS),
            (
                socks.SOCKS5_USER_AUTH_VERSION + 1,
                socks.SOCKS5_USER_AUTH_SUCCESS,
            ),
        ]
    )

    monkeypatch.setattr(
        socks.sockssocket,
        "sendall",
        lambda self, packet: sent_packets.append(packet),
    )
    monkeypatch.setattr(
        socks.sockssocket,
        "_recv_bytes",
        lambda self, size: next(responses),
    )

    with pytest.raises(socks.InvalidVersionError):
        sock._socks5_auth()

    assert len(sent_packets) == 2
    assert sent_packets[0] == bytes(
        (
            socks.SOCKS5_VERSION,
            2,
            socks.Socks5Auth.AUTH_NONE,
            socks.Socks5Auth.AUTH_USER_PASS,
        )
    )
    assert list(responses) == []
    assert sock.fileno() == -1
