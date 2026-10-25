# file: project/youtube_dl/socks.py:216-252
# asked: {"lines": [217, 219, 221, 223, 224, 225, 226, 227, 228, 230, 231, 233, 235, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 252], "branches": [[225, 226], [225, 230], [239, 240], [239, 243], [243, 244], [243, 245], [245, 246], [245, 248], [248, 249], [248, 250]]}
# gained: {"lines": [217, 219, 221, 223, 224, 225, 226, 227, 228, 230, 231, 233, 235, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 252], "branches": [[225, 226], [225, 230], [239, 240], [239, 243], [243, 244], [243, 245], [245, 246], [245, 248], [248, 249]]}

import socket
import struct
from unittest import mock

import pytest

from youtube_dl.socks import (
    sockssocket,
    Socks5Error,
    Socks5AddressType,
    Socks5Command,
    SOCKS5_VERSION,
)


def _make_socket():
    # Avoid creating a real socket file descriptor: bypass __init__.
    sock = sockssocket.__new__(sockssocket)
    sock._proxy = mock.Mock()
    return sock


def test_setup_socks5_success_ipv4(monkeypatch):
    sock = _make_socket()
    ipaddr = socket.inet_aton('127.0.0.1')
    port = 1080
    sent_packets = []
    recvall_calls = []

    monkeypatch.setattr(
        sock, '_resolve_address',
        lambda destaddr, default, use_remote_dns: ipaddr)
    monkeypatch.setattr(sock, '_socks5_auth', lambda: None)
    monkeypatch.setattr(sock, 'sendall', sent_packets.append)
    monkeypatch.setattr(
        sock, '_recv_bytes',
        lambda cnt: struct.pack('!BBBB', SOCKS5_VERSION, 0, 0,
                                Socks5AddressType.ATYP_IPV4))
    monkeypatch.setattr(
        sock, 'recvall',
        lambda cnt: (recvall_calls.append(cnt),
                     ipaddr if cnt == 4 else struct.pack('!H', port))[1])

    result = sock._setup_socks5(('example.com', port))

    # Postconditions: correct return value and correct CONNECT packet sent.
    assert result == (ipaddr, port)
    expected_packet = (
        struct.pack('!BBB', SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0) +
        struct.pack('!B', Socks5AddressType.ATYP_IPV4) +
        ipaddr +
        struct.pack('!H', port))
    assert sent_packets == [expected_packet]
    # Bound address was read back (4-byte IPv4 + 2-byte port).
    assert recvall_calls == [4, 2]


def test_setup_socks5_success_domainname_remote_dns(monkeypatch):
    sock = _make_socket()
    port = 8080
    domain = b'example.org'
    sent_packets = []
    recvall_calls = []

    # Remote DNS: resolver returns None so the hostname is sent as-is.
    monkeypatch.setattr(
        sock, '_resolve_address',
        lambda destaddr, default, use_remote_dns: None)
    monkeypatch.setattr(sock, '_socks5_auth', lambda: None)
    monkeypatch.setattr(sock, 'sendall', sent_packets.append)
    monkeypatch.setattr(
        sock, '_recv_bytes',
        lambda cnt: struct.pack('!BBBB', SOCKS5_VERSION, 0, 0,
                                Socks5AddressType.ATYP_DOMAINNAME))
    monkeypatch.setattr(sock, 'recv', lambda cnt: bytes([len(domain)]))
    monkeypatch.setattr(
        sock, 'recvall',
        lambda cnt: (recvall_calls.append(cnt),
                     domain if cnt == len(domain) else struct.pack('!H', port))[1])

    result = sock._setup_socks5((domain.decode('utf-8'), port))

    # Postconditions: domain name echoed back and correct packet sent.
    assert result == (domain, port)
    expected_packet = (
        struct.pack('!BBB', SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0) +
        struct.pack('!B', Socks5AddressType.ATYP_DOMAINNAME) +
        struct.pack('!B', len(domain)) + domain +
        struct.pack('!H', port))
    assert sent_packets == [expected_packet]
    # Length byte + domain + port were read back.
    assert recvall_calls == [len(domain), 2]


def test_setup_socks5_success_ipv6(monkeypatch):
    sock = _make_socket()
    port = 443
    ipv6_addr = socket.inet_pton(socket.AF_INET6, '::1')
    assert len(ipv6_addr) == 16
    sent_packets = []
    recvall_calls = []

    monkeypatch.setattr(
        sock, '_resolve_address',
        lambda destaddr, default, use_remote_dns: ipv6_addr)
    monkeypatch.setattr(sock, '_socks5_auth', lambda: None)
    monkeypatch.setattr(sock, 'sendall', sent_packets.append)
    monkeypatch.setattr(
        sock, '_recv_bytes',
        lambda cnt: struct.pack('!BBBB', SOCKS5_VERSION, 0, 0,
                                Socks5AddressType.ATYP_IPV6))
    monkeypatch.setattr(
        sock, 'recvall',
        lambda cnt: (recvall_calls.append(cnt),
                     ipv6_addr if cnt == 16 else struct.pack('!H', port))[1])

    result = sock._setup_socks5(('::1', port))

    # Postconditions: 16-byte IPv6 reply address and port returned.
    assert result == (ipv6_addr, port)
    expected_packet = (
        struct.pack('!BBB', SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0) +
        struct.pack('!B', Socks5AddressType.ATYP_IPV4) +
        ipv6_addr +
        struct.pack('!H', port))
    assert sent_packets == [expected_packet]
    assert recvall_calls == [16, 2]


def test_setup_socks5_error_status_closes_and_raises(monkeypatch):
    sock = _make_socket()
    ipaddr = socket.inet_aton('10.0.0.1')
    port = 1080
    sent_packets = []
    close_mock = mock.Mock()

    monkeypatch.setattr(
        sock, '_resolve_address',
        lambda destaddr, default, use_remote_dns: ipaddr)
    monkeypatch.setattr(sock, '_socks5_auth', lambda: None)
    monkeypatch.setattr(sock, 'sendall', sent_packets.append)
    monkeypatch.setattr(sock, 'close', close_mock)
    monkeypatch.setattr(
        sock, '_recv_bytes',
        lambda cnt: struct.pack('!BBBB', SOCKS5_VERSION,
                                Socks5Error.ERR_GENERAL_FAILURE, 0,
                                Socks5AddressType.ATYP_IPV4))

    with pytest.raises(Socks5Error) as excinfo:
        sock._setup_socks5(('example.com', port))

    # Postconditions: the CONNECT packet was sent, the socket was closed
    # before raising, and the server's error status is reported.
    assert len(sent_packets) == 1
    assert close_mock.called
    assert excinfo.value.args[0] == Socks5Error.ERR_GENERAL_FAILURE
