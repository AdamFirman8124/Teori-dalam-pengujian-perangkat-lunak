# file: project/youtube_dl/socks.py:272-273
# asked: {"lines": [273], "branches": []}
# gained: {"lines": [273], "branches": []}

import socket

import pytest

from youtube_dl.socks import ProxyType, sockssocket


@pytest.fixture
def fake_connect_ex(monkeypatch):
    """Replace socket.socket.connect_ex so no real network I/O happens."""
    calls = []

    def _fake_connect_ex(self, address):
        calls.append((self, address))
        return _fake_connect_ex.result

    _fake_connect_ex.calls = calls
    _fake_connect_ex.result = 0
    monkeypatch.setattr(socket.socket, "connect_ex", _fake_connect_ex)
    return _fake_connect_ex


def test_connect_ex_without_proxy(fake_connect_ex):
    """Covers line 273 via the no-proxy branch of _make_proxy."""
    s = sockssocket()
    try:
        address = ('127.0.0.1', 80)
        result = s.connect_ex(address)
        assert result == 0
        assert fake_connect_ex.calls == [(s, address)]
    finally:
        s.close()


def test_connect_ex_with_proxy(fake_connect_ex, monkeypatch):
    """Covers line 273 via the proxy branch of _make_proxy."""
    s = sockssocket()
    try:
        s.setproxy(ProxyType.SOCKS5, '127.0.0.1', 1080)
        setup_calls = []
        monkeypatch.setattr(
            s, '_setup_socks5',
            lambda address: setup_calls.append(address))

        address = ('example.com', 443)
        result = s.connect_ex(address)

        assert result == 0
        assert fake_connect_ex.calls == [(s, ('127.0.0.1', 1080))]
        assert setup_calls == [address]
    finally:
        s.close()


def test_connect_ex_with_proxy_error_propagates(fake_connect_ex, monkeypatch):
    """Covers line 273 and the early-return branch when the proxy
    connection itself fails (nonzero result)."""
    s = sockssocket()
    try:
        s.setproxy(ProxyType.SOCKS4, '127.0.0.1', 1080)
        setup_calls = []
        monkeypatch.setattr(
            s, '_setup_socks4',
            lambda address, is_4a=False: setup_calls.append(address))

        fake_connect_ex.result = 111
        address = ('example.com', 80)
        result = s.connect_ex(address)

        assert result == 111
        assert fake_connect_ex.calls == [(s, ('127.0.0.1', 1080))]
        assert setup_calls == []
    finally:
        s.close()
