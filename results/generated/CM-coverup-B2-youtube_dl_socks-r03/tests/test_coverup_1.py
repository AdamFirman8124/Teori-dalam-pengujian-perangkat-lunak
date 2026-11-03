# file: project/youtube_dl/socks.py:216-252
# asked: {"lines": [217, 219, 221, 223, 224, 225, 226, 227, 228, 230, 231, 233, 235, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 252], "branches": [[225, 226], [225, 230], [239, 240], [239, 243], [243, 244], [243, 245], [245, 246], [245, 248], [248, 249], [248, 250]]}
# gained: {"lines": [217, 219, 221, 223, 224, 225, 226, 227, 228, 230, 231, 233, 235, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 252], "branches": [[225, 226], [225, 230], [239, 240], [239, 243], [243, 244], [243, 245], [245, 246], [245, 248], [248, 249], [248, 250]]}

import socket
from unittest import mock

import pytest

from youtube_dl.compat import compat_struct_pack
from youtube_dl.socks import (
    SOCKS5_VERSION,
    InvalidVersionError,
    ProxyType,
    Socks5AddressType,
    Socks5Auth,
    Socks5Command,
    Socks5Error,
    sockssocket,
)

AUTH_REPLY = compat_struct_pack('!BB', SOCKS5_VERSION, Socks5Auth.AUTH_NONE)


@pytest.fixture
def socks():
    sock = sockssocket()
    yield sock
    # Close the real underlying socket directly on the base class so that
    # cleanup works even if the instance's `close` was replaced by a mock.
    socket.socket.close(sock)


def _prepare(monkeypatch, sock, recv_chunks, rdns=True):
    """Configure a SOCKS5 proxy and replace the transport I/O with mocks."""
    sock.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080, rdns=rdns)
    recv_mock = mock.Mock(side_effect=list(recv_chunks))
    send_mock = mock.Mock()
    close_mock = mock.Mock()
    monkeypatch.setattr(sock, 'recv', recv_mock)
    monkeypatch.setattr(sock, 'sendall', send_mock)
    monkeypatch.setattr(sock, 'close', close_mock)
    return recv_mock, send_mock, close_mock


def _sent_packets(send_mock):
    return [call[0][0] for call in send_mock.call_args_list]


def _recv_sizes(recv_mock):
    return [call[0][0] for call in recv_mock.call_args_list]


def test_socks5_ip_destination_ipv4_reply(socks, monkeypatch):
    bound_addr = compat_struct_pack('!BBBB', 10, 11, 12, 13)
    recv_mock, send_mock, close_mock = _prepare(monkeypatch, socks, [
        AUTH_REPLY,
        compat_struct_pack('!BBBB', SOCKS5_VERSION, Socks5Error.ERR_SUCCESS,
                           0, Socks5AddressType.ATYP_IPV4),
        bound_addr,
        compat_struct_pack('!H', 4242),
    ])

    result = socks._setup_socks5(('1.2.3.4', 1080))

    assert result == (bound_addr, 4242)
    close_mock.assert_not_called()
    auth_packet, connect_packet = _sent_packets(send_mock)
    assert auth_packet == compat_struct_pack('!BBB', SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)
    assert connect_packet == (
        compat_struct_pack('!BBB', SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
        + compat_struct_pack('!B', Socks5AddressType.ATYP_IPV4)
        + socket.inet_aton('1.2.3.4')
        + compat_struct_pack('!H', 1080)
    )
    assert _recv_sizes(recv_mock) == [2, 4, 4, 2]


def test_socks5_remote_dns_domain_destination_and_reply(socks, monkeypatch):
    bound_addr = b'example.org'
    recv_mock, send_mock, close_mock = _prepare(monkeypatch, socks, [
        AUTH_REPLY,
        compat_struct_pack('!BBBB', SOCKS5_VERSION, Socks5Error.ERR_SUCCESS,
                           0, Socks5AddressType.ATYP_DOMAINNAME),
        compat_struct_pack('!B', len(bound_addr)),
        bound_addr,
        compat_struct_pack('!H', 1080),
    ])

    result = socks._setup_socks5(('example.com', 1080))

    assert result == (bound_addr, 1080)
    close_mock.assert_not_called()
    _, connect_packet = _sent_packets(send_mock)
    assert connect_packet == (
        compat_struct_pack('!BBB', SOCKS5_VERSION, Socks5Command.CMD_CONNECT, 0)
        + compat_struct_pack('!B', Socks5AddressType.ATYP_DOMAINNAME)
        + compat_struct_pack('!B', len(b'example.com'))
        + b'example.com'
        + compat_struct_pack('!H', 1080)
    )
    assert _recv_sizes(recv_mock) == [2, 4, 1, len(bound_addr), 2]


def test_socks5_ipv6_reply_address(socks, monkeypatch):
    bound_addr = compat_struct_pack('!8H', 0x2001, 0x0DB8, 0, 0, 0, 0, 0, 1)
    recv_mock, send_mock, close_mock = _prepare(monkeypatch, socks, [
        AUTH_REPLY,
        compat_struct_pack('!BBBB', SOCKS5_VERSION, Socks5Error.ERR_SUCCESS,
                           0, Socks5AddressType.ATYP_IPV6),
        bound_addr,
        compat_struct_pack('!H', 4242),
    ])

    result = socks._setup_socks5(('1.2.3.4', 4242))

    assert result == (bound_addr, 4242)
    close_mock.assert_not_called()
    assert _recv_sizes(recv_mock) == [2, 4, 16, 2]


def test_socks5_error_status_closes_socket_and_raises(socks, monkeypatch):
    recv_mock, send_mock, close_mock = _prepare(monkeypatch, socks, [
        AUTH_REPLY,
        compat_struct_pack('!BBBB', SOCKS5_VERSION, Socks5Error.ERR_GENERAL_FAILURE,
                           0, Socks5AddressType.ATYP_IPV4),
    ])

    with pytest.raises(Socks5Error) as excinfo:
        socks._setup_socks5(('1.2.3.4', 1080))

    assert excinfo.value.errno == Socks5Error.ERR_GENERAL_FAILURE
    assert excinfo.value.strerror == 'general SOCKS server failure'
    close_mock.assert_called_once_with()
    # No attempt to read a bound address after the failure.
    assert _recv_sizes(recv_mock) == [2, 4]
    assert len(_sent_packets(send_mock)) == 2


def test_socks5_invalid_reply_version_closes_socket_and_raises(socks, monkeypatch):
    recv_mock, send_mock, close_mock = _prepare(monkeypatch, socks, [
        AUTH_REPLY,
        compat_struct_pack('!BBBB', SOCKS5_VERSION - 1, Socks5Error.ERR_SUCCESS,
                           0, Socks5AddressType.ATYP_IPV4),
    ])

    with pytest.raises(InvalidVersionError):
        socks._setup_socks5(('1.2.3.4', 1080))

    close_mock.assert_called_once_with()
    assert _recv_sizes(recv_mock) == [2, 4]


def test_socks5_local_dns_resolution_when_rdns_disabled(socks, monkeypatch):
    monkeypatch.setattr(socket, 'gethostbyname', lambda host: '9.9.9.9')
    bound_addr = compat_struct_pack('!BBBB', 1, 2, 3, 4)
    recv_mock, send_mock, close_mock = _prepare(monkeypatch, socks, [
        AUTH_REPLY,
        compat_struct_pack('!BBBB', SOCKS5_VERSION, Socks5Error.ERR_SUCCESS,
                           0, Socks5AddressType.ATYP_IPV4),
        bound_addr,
        compat_struct_pack('!H', 8080),
    ], rdns=False)

    result = socks._setup_socks5(('example.com', 8080))

    assert result == (bound_addr, 8080)
    close_mock.assert_not_called()
    _, connect_packet = _sent_packets(send_mock)
    assert connect_packet[3:4] == compat_struct_pack('!B', Socks5AddressType.ATYP_IPV4)
    assert connect_packet[4:8] == socket.inet_aton('9.9.9.9')


def test_socks5_unknown_reply_address_type_returns_original_destination(socks, monkeypatch):
    recv_mock, send_mock, close_mock = _prepare(monkeypatch, socks, [
        AUTH_REPLY,
        compat_struct_pack('!BBBB', SOCKS5_VERSION, Socks5Error.ERR_SUCCESS, 0, 0),
        compat_struct_pack('!H', 4242),
    ])

    result = socks._setup_socks5(('1.2.3.4', 4242))

    assert result == ('1.2.3.4', 4242)
    close_mock.assert_not_called()
    assert _recv_sizes(recv_mock) == [2, 4, 2]
