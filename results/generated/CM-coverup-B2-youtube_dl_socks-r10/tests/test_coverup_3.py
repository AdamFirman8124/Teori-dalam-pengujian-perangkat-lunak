# file: project/youtube_dl/socks.py:152-175
# asked: {"lines": [153, 155, 157, 159, 160, 162, 163, 165, 167, 169, 171, 172, 173, 175], "branches": [[162, 163], [162, 165], [171, 172], [171, 175]]}
# gained: {"lines": [153, 155, 157, 159, 160, 162, 163, 165, 167, 169, 171, 172, 173, 175], "branches": [[162, 163], [162, 165], [171, 172], [171, 175]]}

import struct

import pytest

from youtube_dl.socks import (
    sockssocket,
    Socks4Error,
    Socks4Command,
    SOCKS4_VERSION,
    SOCKS4_REPLY_VERSION,
    SOCKS4_DEFAULT_DSTIP,
    ProxyType,
)


def make_socket(rdns=True, username=None):
    # Build a sockssocket without touching the real socket layer
    s = sockssocket.__new__(sockssocket)
    s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080, rdns=rdns, username=username)
    return s


def make_reply(resp_code=90, dstport=1234, dsthost=0x7F000001, version=SOCKS4_REPLY_VERSION):
    return struct.pack('!BBHI', version, resp_code, dstport, dsthost)


def test_socks4_success_sends_packet_and_returns_reply(monkeypatch):
    s = make_socket(username='user')
    sent = []
    monkeypatch.setattr(s, 'sendall', lambda data: sent.append(data))
    monkeypatch.setattr(s, '_resolve_address',
                        lambda destaddr, default, use_remote_dns: b'\x01\x02\x03\x04')
    monkeypatch.setattr(s, 'recvall', lambda cnt: make_reply())
    closed = []
    monkeypatch.setattr(s, 'close', lambda: closed.append(True))

    result = s._setup_socks4(('example.com', 8080))

    # Postcondition: returned reply host/port
    assert result == (0x7F000001, 1234)
    # Postcondition: correct SOCKS4 packet was sent
    expected = (
        struct.pack('!BBH', SOCKS4_VERSION, Socks4Command.CMD_CONNECT, 8080)
        + b'\x01\x02\x03\x04'
        + b'user\x00'
    )
    assert sent == [expected]
    # Success path must not close the socket
    assert closed == []


def test_socks4_success_no_username(monkeypatch):
    s = make_socket(username=None)
    sent = []
    monkeypatch.setattr(s, 'sendall', lambda data: sent.append(data))
    monkeypatch.setattr(s, '_resolve_address',
                        lambda destaddr, default, use_remote_dns: b'\x00\x00\x00\x01')
    monkeypatch.setattr(s, 'recvall', lambda cnt: make_reply(dstport=80, dsthost=0x01020304))

    result = s._setup_socks4(('1.2.3.4', 80))

    assert result == (0x01020304, 80)
    expected = (
        struct.pack('!BBH', SOCKS4_VERSION, Socks4Command.CMD_CONNECT, 80)
        + b'\x00\x00\x00\x01'
        + b'\x00'
    )
    assert sent == [expected]


def test_socks4a_remote_dns_appends_hostname(monkeypatch):
    s = make_socket(rdns=True)
    sent = []
    resolved_with = {}

    def fake_resolve(destaddr, default, use_remote_dns):
        resolved_with['use_remote_dns'] = use_remote_dns
        return SOCKS4_DEFAULT_DSTIP

    monkeypatch.setattr(s, 'sendall', lambda data: sent.append(data))
    monkeypatch.setattr(s, '_resolve_address', fake_resolve)
    monkeypatch.setattr(s, 'recvall', lambda cnt: make_reply())

    result = s._setup_socks4(('some.host.name', 443), is_4a=True)

    assert result == (0x7F000001, 1234)
    # is_4a must be forwarded to _resolve_address as use_remote_dns
    assert resolved_with['use_remote_dns'] is True
    # Postcondition: hostname appended for remote DNS resolution (4a extension)
    expected = (
        struct.pack('!BBH', SOCKS4_VERSION, Socks4Command.CMD_CONNECT, 443)
        + SOCKS4_DEFAULT_DSTIP
        + b'\x00'
        + b'some.host.name\x00'
    )
    assert sent == [expected]


def test_socks4a_without_remote_dns_omits_hostname(monkeypatch):
    s = make_socket(rdns=False)
    sent = []
    monkeypatch.setattr(s, 'sendall', lambda data: sent.append(data))
    monkeypatch.setattr(s, '_resolve_address',
                        lambda destaddr, default, use_remote_dns: SOCKS4_DEFAULT_DSTIP)
    monkeypatch.setattr(s, 'recvall', lambda cnt: make_reply())

    result = s._setup_socks4(('some.host.name', 443), is_4a=True)

    assert result == (0x7F000001, 1234)
    expected = (
        struct.pack('!BBH', SOCKS4_VERSION, Socks4Command.CMD_CONNECT, 443)
        + SOCKS4_DEFAULT_DSTIP
        + b'\x00'
    )
    # rdns=False: hostname must NOT be appended even with is_4a
    assert sent == [expected]


def test_socks4_error_response_closes_and_raises(monkeypatch):
    s = make_socket(username='u')
    monkeypatch.setattr(s, 'sendall', lambda data: None)
    monkeypatch.setattr(s, '_resolve_address',
                        lambda destaddr, default, use_remote_dns: b'\x01\x02\x03\x04')
    monkeypatch.setattr(s, 'recvall', lambda cnt: make_reply(resp_code=91))
    closed = []
    monkeypatch.setattr(s, 'close', lambda: closed.append(True))

    with pytest.raises(Socks4Error) as excinfo:
        s._setup_socks4(('example.com', 8080))

    # Postcondition: error code propagated and socket closed before raising
    assert excinfo.value.args[0] == 91
    assert closed == [True]


def test_socks4_invalid_reply_version_closes_and_raises(monkeypatch):
    from youtube_dl.socks import InvalidVersionError

    s = make_socket()
    monkeypatch.setattr(s, 'sendall', lambda data: None)
    monkeypatch.setattr(s, '_resolve_address',
                        lambda destaddr, default, use_remote_dns: b'\x01\x02\x03\x04')
    monkeypatch.setattr(s, 'recvall', lambda cnt: make_reply(version=4))
    closed = []
    monkeypatch.setattr(s, 'close', lambda: closed.append(True))

    with pytest.raises(InvalidVersionError) as excinfo:
        s._setup_socks4(('example.com', 8080))

    # Postcondition: socket closed on invalid reply version
    assert closed == [True]
    assert 'Invalid response version from server' in excinfo.value.args[1]
