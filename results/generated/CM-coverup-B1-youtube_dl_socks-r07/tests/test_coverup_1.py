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


def _read_exact(sock, cnt):
    data = b""
    while len(data) < cnt:
        chunk = sock.recv(cnt - len(data))
        if not chunk:
            raise EOFError("expected {0} more bytes".format(cnt - len(data)))
        data += chunk
    return data


def _make_socket(monkeypatch, ipaddr, response):
    """Build a real sockssocket over a socketpair, with the network-facing
    helpers stubbed out. Returns (sock, server_peer, state)."""
    client, server = socket.socketpair()
    sock = sockssocket(fileno=client.detach())
    state = {"auth_called": False, "resolve_args": None}

    def fake_resolve(self, destaddr, default, use_remote_dns=False):
        state["resolve_args"] = (destaddr, default, use_remote_dns)
        return ipaddr

    def fake_auth(self):
        state["auth_called"] = True

    monkeypatch.setattr(sockssocket, "_resolve_address", fake_resolve)
    monkeypatch.setattr(sockssocket, "_socks5_auth", fake_auth)

    server.sendall(response)
    return sock, server, state


def test_setup_socks5_ipv4_success(monkeypatch):
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
    sock, server, state = _make_socket(monkeypatch, ipaddr, response)
    try:
        result = sock._setup_socks5(("93.184.216.34", 80))

        assert result == (bound_addr, 8080)
        assert state["resolve_args"] == ("93.184.216.34", None, True)
        assert state["auth_called"] is True
        assert sock.fileno() != -1

        expected_packet = (
            struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
            + struct.pack("!B", Socks5AddressType.ATYP_IPV4)
            + ipaddr
            + struct.pack("!H", 80)
        )
        assert _read_exact(server, len(expected_packet)) == expected_packet
    finally:
        sock.close()
        server.close()


def test_setup_socks5_domainname_success(monkeypatch):
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
    sock, server, state = _make_socket(monkeypatch, None, response)
    try:
        result = sock._setup_socks5(("example.com", 443))

        assert result == (bound_name, 1234)
        assert state["resolve_args"] == ("example.com", None, True)
        assert state["auth_called"] is True
        assert sock.fileno() != -1

        expected_packet = (
            struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
            + struct.pack("!B", Socks5AddressType.ATYP_DOMAINNAME)
            + struct.pack("!B", len(b"example.com"))
            + b"example.com"
            + struct.pack("!H", 443)
        )
        assert _read_exact(server, len(expected_packet)) == expected_packet
    finally:
        sock.close()
        server.close()


def test_setup_socks5_ipv6_response_success(monkeypatch):
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
    sock, server, state = _make_socket(monkeypatch, ipaddr, response)
    try:
        result = sock._setup_socks5(("192.0.2.1", 22))

        assert result == (bound_addr, 9999)
        assert state["auth_called"] is True
        assert sock.fileno() != -1

        expected_packet = (
            struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
            + struct.pack("!B", Socks5AddressType.ATYP_IPV4)
            + ipaddr
            + struct.pack("!H", 22)
        )
        assert _read_exact(server, len(expected_packet)) == expected_packet
    finally:
        sock.close()
        server.close()


def test_setup_socks5_error_status_closes_and_raises(monkeypatch):
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
    sock, server, state = _make_socket(monkeypatch, ipaddr, response)
    try:
        with pytest.raises(Socks5Error):
            sock._setup_socks5(("203.0.113.7", 25))

        assert state["auth_called"] is True
        assert sock.fileno() == -1

        expected_packet = (
            struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
            + struct.pack("!B", Socks5AddressType.ATYP_IPV4)
            + ipaddr
            + struct.pack("!H", 25)
        )
        assert _read_exact(server, len(expected_packet)) == expected_packet
    finally:
        sock.close()
        server.close()


def test_setup_socks5_unknown_response_atype(monkeypatch):
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
    sock, server, state = _make_socket(monkeypatch, ipaddr, response)
    try:
        result = sock._setup_socks5(("198.51.100.3", 110))

        # No address bytes are consumed for an unknown ATYP, so the
        # original destination string is returned unchanged.
        assert result == ("198.51.100.3", 5555)
        assert state["auth_called"] is True
        assert sock.fileno() != -1

        expected_packet = (
            struct.pack("!BBB", SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
            + struct.pack("!B", Socks5AddressType.ATYP_IPV4)
            + ipaddr
            + struct.pack("!H", 110)
        )
        assert _read_exact(server, len(expected_packet)) == expected_packet
    finally:
        sock.close()
        server.close()
