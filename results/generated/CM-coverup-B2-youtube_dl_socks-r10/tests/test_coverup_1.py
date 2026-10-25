# file: project/youtube_dl/socks.py:216-252
# asked: {"lines": [217, 219, 221, 223, 224, 225, 226, 227, 228, 230, 231, 233, 235, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 252], "branches": [[225, 226], [225, 230], [239, 240], [239, 243], [243, 244], [243, 245], [245, 246], [245, 248], [248, 249], [248, 250]]}
# gained: {"lines": [217, 219, 221, 223, 224, 225, 226, 227, 228, 230, 231, 233, 235, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 252], "branches": [[225, 226], [225, 230], [239, 240], [239, 243], [243, 244], [243, 245], [245, 246], [245, 248], [248, 249], [248, 250]]}

import socket
import struct

import pytest

from youtube_dl.socks import (
    SOCKS5_VERSION,
    Socks5AddressType,
    Socks5Command,
    Socks5Error,
    sockssocket,
)


@pytest.fixture
def make_fake_socket(monkeypatch):
    """Build a sockssocket whose network I/O is fully faked.

    A real (but unconnected) socket object is created so that the C-level
    socket type is properly initialised; its file descriptor is closed in
    teardown via the *unpatched* base-class close().
    """
    created = []

    def _make(ipaddr, response):
        sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
        created.append(sock)

        buffer = bytearray(response)
        sent = []
        state = {"closed": False, "auth_called": False, "resolve_args": None}

        def fake_resolve(self, destaddr, default, use_remote_dns=False):
            state["resolve_args"] = (destaddr, default, use_remote_dns)
            return ipaddr

        def fake_auth(self):
            state["auth_called"] = True

        def fake_sendall(self, data):
            sent.append(bytes(data))

        def fake_recv(self, cnt, *args, **kwargs):
            chunk = bytes(buffer[:cnt])
            del buffer[:cnt]
            return chunk

        def fake_close(self):
            state["closed"] = True

        monkeypatch.setattr(sockssocket, "_resolve_address", fake_resolve)
        monkeypatch.setattr(sockssocket, "_socks5_auth", fake_auth)
        monkeypatch.setattr(sockssocket, "sendall", fake_sendall)
        monkeypatch.setattr(sockssocket, "recv", fake_recv)
        monkeypatch.setattr(sockssocket, "close", fake_close)
        return sock, sent, state

    yield _make

    for sock in created:
        try:
            socket.socket.close(sock)
        except OSError:
            pass


def test_setup_socks5_ipv4_success(make_fake_socket):
    ipaddr = socket.inet_aton("93.184.216.34")
    bound_addr = socket.inet_aton("10.0.0.1")
    response = (
        struct.pack(
            "!BBBB",
            SOCKS5_VERSION,
            Socks5Error.ERR_SUCCESS,
            0,
            Socks5AddressType.ATYP_IPV4,
        )
        + bound_addr
        + struct.pack("!H", 8080)
    )
    sock, sent, state = make_fake_socket(ipaddr, response)

    result = sock._setup_socks5(("93.184.216.34", 80))

    assert result == (bound_addr, 8080)
    assert state["resolve_args"] == ("93.184.216.34", None, True)
    assert state["auth_called"] is True
    assert state["closed"] is False
    expected_packet = (
        struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
        + struct.pack("!B", Socks5AddressType.ATYP_IPV4)
        + ipaddr
        + struct.pack("!H", 80)
    )
    assert sent == [expected_packet]


def test_setup_socks5_domainname_success(make_fake_socket):
    bound_name = b"example.com"
    response = (
        struct.pack(
            "!BBBB",
            SOCKS5_VERSION,
            Socks5Error.ERR_SUCCESS,
            0,
            Socks5AddressType.ATYP_DOMAINNAME,
        )
        + struct.pack("!B", len(bound_name))
        + bound_name
        + struct.pack("!H", 1234)
    )
    sock, sent, state = make_fake_socket(None, response)

    result = sock._setup_socks5(("example.com", 443))

    assert result == (bound_name, 1234)
    assert state["resolve_args"] == ("example.com", None, True)
    assert state["auth_called"] is True
    assert state["closed"] is False
    expected_packet = (
        struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
        + struct.pack("!B", Socks5AddressType.ATYP_DOMAINNAME)
        + struct.pack("!B", len(b"example.com"))
        + b"example.com"
        + struct.pack("!H", 443)
    )
    assert sent == [expected_packet]


def test_setup_socks5_ipv6_response_success(make_fake_socket):
    ipaddr = socket.inet_aton("192.0.2.1")
    bound_addr = bytes(range(16))
    response = (
        struct.pack(
            "!BBBB",
            SOCKS5_VERSION,
            Socks5Error.ERR_SUCCESS,
            0,
            Socks5AddressType.ATYP_IPV6,
        )
        + bound_addr
        + struct.pack("!H", 9999)
    )
    sock, sent, state = make_fake_socket(ipaddr, response)

    result = sock._setup_socks5(("192.0.2.1", 22))

    assert result == (bound_addr, 9999)
    assert state["auth_called"] is True
    assert state["closed"] is False
    expected_packet = (
        struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
        + struct.pack("!B", Socks5AddressType.ATYP_IPV4)
        + ipaddr
        + struct.pack("!H", 22)
    )
    assert sent == [expected_packet]


def test_setup_socks5_error_status_closes_and_raises(make_fake_socket):
    ipaddr = socket.inet_aton("203.0.113.7")
    error_status = 5
    assert error_status != Socks5Error.ERR_SUCCESS
    response = struct.pack(
        "!BBBB",
        SOCKS5_VERSION,
        error_status,
        0,
        Socks5AddressType.ATYP_IPV4,
    )
    sock, sent, state = make_fake_socket(ipaddr, response)

    with pytest.raises(Socks5Error):
        sock._setup_socks5(("203.0.113.7", 25))

    assert state["closed"] is True
    assert state["auth_called"] is True
    expected_packet = (
        struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
        + struct.pack("!B", Socks5AddressType.ATYP_IPV4)
        + ipaddr
        + struct.pack("!H", 25)
    )
    assert sent == [expected_packet]


def test_setup_socks5_unknown_response_atype(make_fake_socket):
    ipaddr = socket.inet_aton("198.51.100.3")
    unknown_atype = 99
    assert unknown_atype not in (
        Socks5AddressType.ATYP_IPV4,
        Socks5AddressType.ATYP_DOMAINNAME,
        Socks5AddressType.ATYP_IPV6,
    )
    response = (
        struct.pack(
            "!BBBB",
            SOCKS5_VERSION,
            Socks5Error.ERR_SUCCESS,
            0,
            unknown_atype,
        )
        + struct.pack("!H", 5555)
    )
    sock, sent, state = make_fake_socket(ipaddr, response)

    result = sock._setup_socks5(("198.51.100.3", 110))

    # No address bytes are consumed for an unknown ATYP, so the
    # original destination string is returned unchanged.
    assert result == ("198.51.100.3", 5555)
    assert state["auth_called"] is True
    assert state["closed"] is False
    assert len(sent) == 1
