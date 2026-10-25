# file: project/youtube_dl/socks.py:216-252
# asked: {"lines": [217, 219, 221, 223, 224, 225, 226, 227, 228, 230, 231, 233, 235, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 252], "branches": [[225, 226], [225, 230], [239, 240], [239, 243], [243, 244], [243, 245], [245, 246], [245, 248], [248, 249], [248, 250]]}
# gained: {"lines": [217, 219, 221, 223, 224, 225, 226, 227, 228, 230, 231, 233, 235, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 252], "branches": [[225, 226], [225, 230], [239, 240], [239, 243], [243, 244], [243, 245], [245, 246], [245, 248], [248, 249], [248, 250]]}

import struct
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

import youtube_dl.socks as socks


def _make_socket_double(resolve_result, response, recvall_values=(), recv_value=b""):
    return SimpleNamespace(
        _resolve_address=Mock(return_value=resolve_result),
        _socks5_auth=Mock(),
        _len_and_data=Mock(side_effect=lambda data: bytes((len(data),)) + data),
        sendall=Mock(),
        _recv_bytes=Mock(return_value=response),
        _check_response_version=Mock(),
        recvall=Mock(side_effect=list(recvall_values)),
        recv=Mock(return_value=recv_value),
        close=Mock(),
    )


def test_setup_socks5_sends_domain_request_and_reads_ipv4_reply():
    host = "example.com"
    port = 443
    bound_address = b"\x7f\x00\x00\x01"
    bound_port = 1080
    sock = _make_socket_double(
        resolve_result=None,
        response=(
            socks.SOCKS5_VERSION,
            socks.Socks5Error.ERR_SUCCESS,
            0,
            socks.Socks5AddressType.ATYP_IPV4,
        ),
        recvall_values=(bound_address, struct.pack("!H", bound_port)),
    )

    result = socks.sockssocket._setup_socks5(sock, (host, port))

    encoded_host = host.encode("utf-8")
    expected_packet = (
        struct.pack(
            "!BBBB",
            socks.SOCKS5_VERSION,
            socks.Socks5Command.CMD_CONNECT,
            0,
            socks.Socks5AddressType.ATYP_DOMAINNAME,
        )
        + bytes((len(encoded_host),))
        + encoded_host
        + struct.pack("!H", port)
    )
    assert result == (bound_address, bound_port)
    sock._resolve_address.assert_called_once_with(
        host, None, use_remote_dns=True
    )
    sock._socks5_auth.assert_called_once_with()
    sock._len_and_data.assert_called_once_with(encoded_host)
    sock.sendall.assert_called_once_with(expected_packet)
    sock._recv_bytes.assert_called_once_with(4)
    sock._check_response_version.assert_called_once_with(
        socks.SOCKS5_VERSION, socks.SOCKS5_VERSION
    )
    assert sock.recvall.call_args_list[0].args == (4,)
    assert sock.recvall.call_args_list[1].args == (2,)
    sock.close.assert_not_called()


def test_setup_socks5_sends_ipv4_request_and_reads_domain_reply():
    host = "192.0.2.10"
    port = 80
    resolved_address = b"\xc0\x00\x02\x0a"
    bound_address = b"proxy.local"
    bound_port = 3128
    sock = _make_socket_double(
        resolve_result=resolved_address,
        response=(
            socks.SOCKS5_VERSION,
            socks.Socks5Error.ERR_SUCCESS,
            0,
            socks.Socks5AddressType.ATYP_DOMAINNAME,
        ),
        recvall_values=(bound_address, struct.pack("!H", bound_port)),
        recv_value=bytes((len(bound_address),)),
    )

    result = socks.sockssocket._setup_socks5(sock, (host, port))

    expected_packet = (
        struct.pack(
            "!BBBB",
            socks.SOCKS5_VERSION,
            socks.Socks5Command.CMD_CONNECT,
            0,
            socks.Socks5AddressType.ATYP_IPV4,
        )
        + resolved_address
        + struct.pack("!H", port)
    )
    assert result == (bound_address, bound_port)
    sock.sendall.assert_called_once_with(expected_packet)
    sock._len_and_data.assert_not_called()
    sock.recv.assert_called_once_with(1)
    assert sock.recvall.call_args_list[0].args == (len(bound_address),)
    assert sock.recvall.call_args_list[1].args == (2,)
    sock.close.assert_not_called()


def test_setup_socks5_reads_ipv6_reply():
    host = "198.51.100.20"
    port = 8080
    resolved_address = b"\xc6\x33\x64\x14"
    bound_address = bytes(range(16))
    bound_port = 65535
    sock = _make_socket_double(
        resolve_result=resolved_address,
        response=(
            socks.SOCKS5_VERSION,
            socks.Socks5Error.ERR_SUCCESS,
            0,
            socks.Socks5AddressType.ATYP_IPV6,
        ),
        recvall_values=(bound_address, struct.pack("!H", bound_port)),
    )

    result = socks.sockssocket._setup_socks5(sock, (host, port))

    assert result == (bound_address, bound_port)
    assert sock.recvall.call_args_list[0].args == (16,)
    assert sock.recvall.call_args_list[1].args == (2,)
    sock.recv.assert_not_called()
    sock.close.assert_not_called()


def test_setup_socks5_closes_and_raises_for_server_error():
    host = "203.0.113.5"
    port = 22
    status = socks.Socks5Error.ERR_GENERAL_FAILURE
    sock = _make_socket_double(
        resolve_result=b"\xcb\x00\x71\x05",
        response=(socks.SOCKS5_VERSION, status, 0, 0),
    )

    with pytest.raises(socks.Socks5Error):
        socks.sockssocket._setup_socks5(sock, (host, port))

    sock.sendall.assert_called_once()
    sock._check_response_version.assert_called_once_with(
        socks.SOCKS5_VERSION, socks.SOCKS5_VERSION
    )
    sock.close.assert_called_once_with()
    sock.recv.assert_not_called()
    sock.recvall.assert_not_called()


def test_setup_socks5_unknown_reply_address_type_still_reads_port():
    host = "192.0.2.25"
    port = 9000
    bound_port = 9001
    unknown_address_type = 127
    sock = _make_socket_double(
        resolve_result=b"\xc0\x00\x02\x19",
        response=(
            socks.SOCKS5_VERSION,
            socks.Socks5Error.ERR_SUCCESS,
            0,
            unknown_address_type,
        ),
        recvall_values=(struct.pack("!H", bound_port),),
    )

    result = socks.sockssocket._setup_socks5(sock, (host, port))

    assert result == (host, bound_port)
    sock.recv.assert_not_called()
    sock.recvall.assert_called_once_with(2)
    sock.close.assert_not_called()
