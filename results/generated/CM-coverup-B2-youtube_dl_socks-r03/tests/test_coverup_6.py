# file: project/youtube_dl/socks.py:143-150
# asked: {"lines": [144, 145, 146, 147, 148, 150], "branches": [[147, 148], [147, 150]]}
# gained: {"lines": [144, 145, 146, 147, 148, 150], "branches": [[147, 148], [147, 150]]}

import socket

import pytest

from youtube_dl.socks import sockssocket


class _FakeProxy(object):
    def __init__(self, remote_dns):
        self.remote_dns = remote_dns


@pytest.fixture
def sock():
    s = sockssocket()
    try:
        yield s
    finally:
        s.close()


def test_resolve_address_literal_ip(sock, monkeypatch):
    # Line 144-145: inet_aton succeeds, no DNS lookup at all.
    def _boom(*args, **kwargs):
        raise AssertionError("gethostbyname must not be called for a literal IP")

    monkeypatch.setattr(socket, "gethostbyname", _boom)
    sock._proxy = _FakeProxy(remote_dns=True)

    result = sock._resolve_address("127.0.0.1", b"\x00\x00\x00\x00", True)

    assert result == socket.inet_aton("127.0.0.1")
    assert result == b"\x7f\x00\x00\x01"


def test_resolve_address_remote_dns_returns_default(sock, monkeypatch):
    # Lines 146-148: inet_aton fails, use_remote_dns and proxy.remote_dns are True.
    def _boom(*args, **kwargs):
        raise AssertionError("gethostbyname must not be called with remote DNS")

    monkeypatch.setattr(socket, "gethostbyname", _boom)
    sock._proxy = _FakeProxy(remote_dns=True)
    default = b"\x00\x00\x00\x00"

    result = sock._resolve_address("example.com", default, True)

    assert result is default
    assert result == b"\x00\x00\x00\x00"


def test_resolve_address_local_dns_when_proxy_remote_dns_false(sock, monkeypatch):
    # Line 150: inet_aton fails, use_remote_dns True but proxy.remote_dns False.
    calls = []

    def fake_gethostbyname(host):
        calls.append(host)
        return "93.184.216.34"

    monkeypatch.setattr(socket, "gethostbyname", fake_gethostbyname)
    sock._proxy = _FakeProxy(remote_dns=False)

    result = sock._resolve_address("example.com", b"\x00\x00\x00\x00", True)

    assert calls == ["example.com"]
    assert result == socket.inet_aton("93.184.216.34")


def test_resolve_address_local_dns_when_use_remote_dns_false(sock, monkeypatch):
    # Line 150: inet_aton fails and use_remote_dns is False (short-circuit).
    calls = []

    def fake_gethostbyname(host):
        calls.append(host)
        return "10.0.0.1"

    monkeypatch.setattr(socket, "gethostbyname", fake_gethostbyname)
    sock._proxy = _FakeProxy(remote_dns=True)

    result = sock._resolve_address("internal.example", b"\x00\x00\x00\x00", False)

    assert calls == ["internal.example"]
    assert result == socket.inet_aton("10.0.0.1")
