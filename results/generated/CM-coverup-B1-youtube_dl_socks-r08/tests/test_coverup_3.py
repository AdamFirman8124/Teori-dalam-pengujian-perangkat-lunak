# file: project/youtube_dl/socks.py:152-175
# asked: {"lines": [153, 155, 157, 159, 160, 162, 163, 165, 167, 169, 171, 172, 173, 175], "branches": [[162, 163], [162, 165], [171, 172], [171, 175]]}
# gained: {"lines": [153, 155, 157, 159, 160, 162, 163, 165, 167, 169, 171, 172, 173, 175], "branches": [[162, 163], [162, 165], [171, 172], [171, 175]]}

import types
import pytest
from youtube_dl.socks import sockssocket, Socks4Error
import youtube_dl.socks as socks_mod
from youtube_dl.compat import compat_struct_pack, compat_struct_unpack


def _new_sock(username, remote_dns):
    s = sockssocket.__new__(sockssocket)
    s._proxy = types.SimpleNamespace(username=username, remote_dns=remote_dns)
    return s


def _patch_sock(monkeypatch, s, resolve_ip, reply_bytes, check_spy=None):
    sent = {}
    closed = {"called": False}

    def fake_resolve(destaddr, default, use_remote_dns):
        fake_resolve.called_with = (destaddr, default, use_remote_dns)
        return resolve_ip

    def fake_sendall(data):
        sent["packet"] = bytes(data)

    def fake_recvall(cnt):
        assert cnt == 8
        return reply_bytes

    def fake_close():
        closed["called"] = True

    def fake_check(expected, got):
        if check_spy is not None:
            check_spy["expected"] = expected
            check_spy["got"] = got
        return sockssocket._check_response_version(s, expected, got)

    monkeypatch.setattr(s, "_resolve_address", fake_resolve, raising=False)
    monkeypatch.setattr(s, "sendall", fake_sendall, raising=False)
    monkeypatch.setattr(s, "recvall", fake_recvall, raising=False)
    monkeypatch.setattr(s, "close", fake_close, raising=False)
    monkeypatch.setattr(s, "_check_response_version", fake_check, raising=False)
    return sent, closed


def test_setup_socks4_no_username_success(monkeypatch):
    SOCKS4_VERSION = getattr(socks_mod, "SOCKS4_VERSION", 4)
    SOCKS4_REPLY_VERSION = getattr(socks_mod, "SOCKS4_REPLY_VERSION", 0)
    CMD_CONNECT = getattr(getattr(socks_mod, "Socks4Command", object), "CMD_CONNECT", 1)
    s = _new_sock(username=None, remote_dns=True)
    resolve_ip = b"\x01\x02\x03\x04"
    reply = compat_struct_pack("!BBHI", SOCKS4_REPLY_VERSION, Socks4Error.ERR_SUCCESS, 1080, 0x01020304)
    spy = {}
    sent, closed = _patch_sock(monkeypatch, s, resolve_ip, reply, check_spy=spy)
    result = s._setup_socks4(("example.com", 1080), is_4a=False)
    assert result == (0x01020304, 1080)
    assert closed["called"] is False
    assert spy["expected"] == SOCKS4_REPLY_VERSION
    assert spy["got"] == SOCKS4_REPLY_VERSION
    expected_prefix = compat_struct_pack("!BBH", SOCKS4_VERSION, CMD_CONNECT, 1080) + resolve_ip
    assert sent["packet"].startswith(expected_prefix)
    assert sent["packet"] == expected_prefix + b"\x00"
    assert s._resolve_address.called_with[0] == "example.com"
    assert s._resolve_address.called_with[2] is False


def test_setup_socks4_with_username_success(monkeypatch):
    SOCKS4_VERSION = getattr(socks_mod, "SOCKS4_VERSION", 4)
    SOCKS4_REPLY_VERSION = getattr(socks_mod, "SOCKS4_REPLY_VERSION", 0)
    CMD_CONNECT = getattr(getattr(socks_mod, "Socks4Command", object), "CMD_CONNECT", 1)
    s = _new_sock(username="bob", remote_dns=True)
    resolve_ip = b"\x05\x06\x07\x08"
    reply = compat_struct_pack("!BBHI", SOCKS4_REPLY_VERSION, Socks4Error.ERR_SUCCESS, 80, 0x05060708)
    sent, closed = _patch_sock(monkeypatch, s, resolve_ip, reply)
    result = s._setup_socks4(("example.com", 80))
    assert result == (0x05060708, 80)
    assert closed["called"] is False
    expected_prefix = compat_struct_pack("!BBH", SOCKS4_VERSION, CMD_CONNECT, 80) + resolve_ip
    assert sent["packet"] == expected_prefix + b"bob\x00"
    assert b"example.com" not in sent["packet"]


def test_setup_socks4a_with_remote_dns_includes_hostname(monkeypatch):
    SOCKS4_VERSION = getattr(socks_mod, "SOCKS4_VERSION", 4)
    SOCKS4_REPLY_VERSION = getattr(socks_mod, "SOCKS4_REPLY_VERSION", 0)
    CMD_CONNECT = getattr(getattr(socks_mod, "Socks4Command", object), "CMD_CONNECT", 1)
    s = _new_sock(username="", remote_dns=True)
    resolve_ip = b"\x00\x00\x00\x01"
    reply = compat_struct_pack("!BBHI", SOCKS4_REPLY_VERSION, Socks4Error.ERR_SUCCESS, 443, 12345)
    sent, closed = _patch_sock(monkeypatch, s, resolve_ip, reply)
    result = s._setup_socks4(("myhost.example", 443), is_4a=True)
    assert result == (12345, 443)
    assert closed["called"] is False
    expected_prefix = compat_struct_pack("!BBH", SOCKS4_VERSION, CMD_CONNECT, 443) + resolve_ip
    assert sent["packet"] == expected_prefix + b"\x00" + b"myhost.example\x00"
    assert s._resolve_address.called_with[2] is True


def test_setup_socks4a_remote_dns_false_excludes_hostname(monkeypatch):
    SOCKS4_VERSION = getattr(socks_mod, "SOCKS4_VERSION", 4)
    SOCKS4_REPLY_VERSION = getattr(socks_mod, "SOCKS4_REPLY_VERSION", 0)
    CMD_CONNECT = getattr(getattr(socks_mod, "Socks4Command", object), "CMD_CONNECT", 1)
    s = _new_sock(username="u", remote_dns=False)
    resolve_ip = b"\x09\x09\x09\x09"
    reply = compat_struct_pack("!BBHI", SOCKS4_REPLY_VERSION, Socks4Error.ERR_SUCCESS, 21, 999)
    sent, closed = _patch_sock(monkeypatch, s, resolve_ip, reply)
    result = s._setup_socks4(("other.example", 21), is_4a=True)
    assert result == (999, 21)
    assert closed["called"] is False
    expected_prefix = compat_struct_pack("!BBH", SOCKS4_VERSION, CMD_CONNECT, 21) + resolve_ip
    assert sent["packet"] == expected_prefix + b"u\x00"
    assert b"other.example" not in sent["packet"]


def test_setup_socks4_error_closes_and_raises(monkeypatch):
    SOCKS4_REPLY_VERSION = getattr(socks_mod, "SOCKS4_REPLY_VERSION", 0)
    s = _new_sock(username=None, remote_dns=True)
    resolve_ip = b"\x01\x01\x01\x01"
    reply = compat_struct_pack("!BBHI", SOCKS4_REPLY_VERSION, 91, 80, 0)
    sent, closed = _patch_sock(monkeypatch, s, resolve_ip, reply)
    with pytest.raises(Socks4Error):
        s._setup_socks4(("example.com", 80), is_4a=False)
    assert closed["called"] is True
    assert "packet" in sent
    assert sent["packet"].endswith(b"\x00")
