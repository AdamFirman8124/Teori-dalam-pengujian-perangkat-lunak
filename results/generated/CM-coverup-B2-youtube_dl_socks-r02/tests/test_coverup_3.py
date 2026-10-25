# file: project/youtube_dl/socks.py:152-175
# asked: {"lines": [153, 155, 157, 159, 160, 162, 163, 165, 167, 169, 171, 172, 173, 175], "branches": [[162, 163], [162, 165], [171, 172], [171, 175]]}
# gained: {"lines": [153, 155, 157, 159, 160, 162, 163, 165, 167, 169, 171, 172, 173, 175], "branches": [[162, 163], [162, 165], [171, 172], [171, 175]]}

import struct
import types

import pytest

from youtube_dl.socks import (
    sockssocket,
    Socks4Error,
    SOCKS4_VERSION,
    SOCKS4_REPLY_VERSION,
    Socks4Command,
)


def make_socket(username='user', remote_dns=True):
    sock = sockssocket()
    sock._proxy = types.SimpleNamespace(username=username, remote_dns=remote_dns)
    return sock


def make_reply(resp_code=Socks4Error.ERR_SUCCESS, dstport=1080, dsthost=0x7F000001):
    return struct.pack('!BBHI', SOCKS4_REPLY_VERSION, resp_code, dstport, dsthost)


def test_setup_socks4_success(monkeypatch):
    sock = make_socket(username='user', remote_dns=True)
    ipaddr = socket_inet = b'\x7f\x00\x00\x01'
    sent = []
    monkeypatch.setattr(sock, '_resolve_address', lambda destaddr, default, use_remote_dns: ipaddr)
    monkeypatch.setattr(sock, 'sendall', lambda data: sent.append(data))
    monkeypatch.setattr(sock, 'recvall', lambda cnt: make_reply())
    closed = []
    monkeypatch.setattr(sock, 'close', lambda: closed.append(True))

    result = sock._setup_socks4(('example.com', 1080))

    expected_packet = (
        struct.pack('!BBH', SOCKS4_VERSION, Socks4Command.CMD_CONNECT, 1080)
        + ipaddr
        + b'user\x00'
    )
    assert sent == [expected_packet]
    assert result == (0x7F000001, 1080)
    assert closed == []


def test_setup_socks4a_remote_dns_appends_hostname(monkeypatch):
    sock = make_socket(username=None, remote_dns=True)
    ipaddr = b'\x00\x00\x00\x00'
    sent = []
    monkeypatch.setattr(sock, '_resolve_address', lambda destaddr, default, use_remote_dns: ipaddr)
    monkeypatch.setattr(sock, 'sendall', lambda data: sent.append(data))
    monkeypatch.setattr(sock, 'recvall', lambda cnt: make_reply(dstport=80, dsthost=0x01020304))

    result = sock._setup_socks4(('example.com', 80), is_4a=True)

    expected_packet = (
        struct.pack('!BBH', SOCKS4_VERSION, Socks4Command.CMD_CONNECT, 80)
        + ipaddr
        + b'\x00'  # empty username (None -> '')
        + b'example.com\x00'
    )
    assert sent == [expected_packet]
    assert result == (0x01020304, 80)


def test_setup_socks4a_no_remote_dns_omits_hostname(monkeypatch):
    sock = make_socket(username='u', remote_dns=False)
    ipaddr = b'\x0a\x00\x00\x01'
    sent = []
    monkeypatch.setattr(sock, '_resolve_address', lambda destaddr, default, use_remote_dns: ipaddr)
    monkeypatch.setattr(sock, 'sendall', lambda data: sent.append(data))
    monkeypatch.setattr(sock, 'recvall', lambda cnt: make_reply())

    sock._setup_socks4(('example.com', 1080), is_4a=True)

    expected_packet = (
        struct.pack('!BBH', SOCKS4_VERSION, Socks4Command.CMD_CONNECT, 1080)
        + ipaddr
        + b'u\x00'
    )
    assert sent == [expected_packet]


def test_setup_socks4_error_response_closes_and_raises(monkeypatch):
    sock = make_socket(username='user')
    monkeypatch.setattr(sock, '_resolve_address', lambda destaddr, default, use_remote_dns: b'\x00\x00\x00\x01')
    monkeypatch.setattr(sock, 'sendall', lambda data: None)
    monkeypatch.setattr(sock, 'recvall', lambda cnt: make_reply(resp_code=91))
    closed = []
    monkeypatch.setattr(sock, 'close', lambda: closed.append(True))

    with pytest.raises(Socks4Error) as excinfo:
        sock._setup_socks4(('example.com', 1080))

    assert closed == [True]
    assert excinfo.value.args[0] == 91
