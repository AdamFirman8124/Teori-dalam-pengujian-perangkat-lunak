# file: project/youtube_dl/socks.py:143-150
# asked: {"lines": [144, 145, 146, 147, 148, 150], "branches": [[147, 148], [147, 150]]}
# gained: {"lines": [144, 145, 146, 147, 148, 150], "branches": [[147, 148], [147, 150]]}

import socket
import types

from youtube_dl.socks import sockssocket


def _make_sock(remote_dns=True):
    s = sockssocket.__new__(sockssocket)
    s._proxy = types.SimpleNamespace(remote_dns=remote_dns)
    return s


def test_resolve_address_ip_literal():
    s = _make_sock(remote_dns=True)
    dest = "127.0.0.1"
    default = b"\x00\x00\x00\x00"
    result = s._resolve_address(dest, default, True)
    assert result == socket.inet_aton(dest)


def test_resolve_address_ip_literal_no_remote():
    s = _make_sock(remote_dns=False)
    dest = "192.168.1.1"
    result = s._resolve_address(dest, b"default", False)
    assert result == socket.inet_aton(dest)


def test_resolve_address_remote_dns_returns_default():
    s = _make_sock(remote_dns=True)
    default = b"\x01\x02\x03\x04"
    result = s._resolve_address("example.com", default, True)
    assert result == default


def test_resolve_address_local_dns_when_use_remote_dns_false(monkeypatch):
    s = _make_sock(remote_dns=True)
    called = {}

    def fake_gethostbyname(host):
        called["host"] = host
        return "1.2.3.4"

    monkeypatch.setattr(socket, "gethostbyname", fake_gethostbyname)
    result = s._resolve_address("example.com", b"default", False)
    assert called == {"host": "example.com"}
    assert result == socket.inet_aton("1.2.3.4")


def test_resolve_address_local_dns_when_proxy_remote_dns_false(monkeypatch):
    s = _make_sock(remote_dns=False)
    called = {}

    def fake_gethostbyname(host):
        called["host"] = host
        return "5.6.7.8"

    monkeypatch.setattr(socket, "gethostbyname", fake_gethostbyname)
    result = s._resolve_address("example.com", b"default", True)
    assert called == {"host": "example.com"}
    assert result == socket.inet_aton("5.6.7.8")
