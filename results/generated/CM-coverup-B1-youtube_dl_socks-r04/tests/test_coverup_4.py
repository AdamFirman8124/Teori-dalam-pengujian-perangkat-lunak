# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

import socket

import pytest

from youtube_dl.socks import ProxyType, sockssocket


def _new_socket():
    return sockssocket(socket.AF_INET, socket.SOCK_STREAM)


def test_make_proxy_no_proxy(monkeypatch):
    s = _new_socket()
    try:
        assert s._proxy is None
        calls = []

        def fake_connect(sock, addr):
            assert sock is s
            calls.append(addr)
            return "ok-no-proxy"

        address = ("example.com", 80)
        result = s._make_proxy(fake_connect, address)
        assert result == "ok-no-proxy"
        assert calls == [address]
    finally:
        s.close()


def test_make_proxy_connect_error_returns_early(monkeypatch):
    s = _new_socket()
    try:
        s.setproxy(ProxyType.SOCKS5, "proxy.example", 1080)
        connect_calls = []
        setup_calls = []

        def fake_connect(sock, addr):
            assert sock is s
            connect_calls.append(addr)
            return 113

        monkeypatch.setattr(s, "_setup_socks4", lambda address: setup_calls.append(("socks4", address)))
        monkeypatch.setattr(s, "_setup_socks4a", lambda address: setup_calls.append(("socks4a", address)))
        monkeypatch.setattr(s, "_setup_socks5", lambda address: setup_calls.append(("socks5", address)))

        address = ("example.com", 80)
        result = s._make_proxy(fake_connect, address)

        assert result == 113
        assert connect_calls == [("proxy.example", 1080)]
        assert setup_calls == []
    finally:
        s.close()


def test_make_proxy_socks4_zero_result(monkeypatch):
    s = _new_socket()
    try:
        s.setproxy(ProxyType.SOCKS4, "proxy.example", 1080)
        connect_calls = []
        setup_calls = []

        def fake_connect(sock, addr):
            connect_calls.append(addr)
            return 0

        def fake_setup_socks4(address):
            setup_calls.append(address)
            return None

        monkeypatch.setattr(s, "_setup_socks4", fake_setup_socks4)

        address = ("example.com", 80)
        result = s._make_proxy(fake_connect, address)

        assert result == 0
        assert connect_calls == [("proxy.example", 1080)]
        assert setup_calls == [address]
    finally:
        s.close()


def test_make_proxy_socks4a_none_result(monkeypatch):
    s = _new_socket()
    try:
        s.setproxy(ProxyType.SOCKS4A, "proxy.example", 1080)
        connect_calls = []
        setup_calls = []

        def fake_connect(sock, addr):
            connect_calls.append(addr)
            return None

        def fake_setup_socks4a(address):
            setup_calls.append(address)
            return None

        monkeypatch.setattr(s, "_setup_socks4a", fake_setup_socks4a)

        address = ("example.com", 80)
        result = s._make_proxy(fake_connect, address)

        assert result is None
        assert connect_calls == [("proxy.example", 1080)]
        assert setup_calls == [address]
    finally:
        s.close()


def test_make_proxy_socks5_zero_result(monkeypatch):
    s = _new_socket()
    try:
        s.setproxy(ProxyType.SOCKS5, "proxy.example", 1080)
        connect_calls = []
        setup_calls = []

        def fake_connect(sock, addr):
            connect_calls.append(addr)
            return 0

        def fake_setup_socks5(address):
            setup_calls.append(address)
            return None

        monkeypatch.setattr(s, "_setup_socks5", fake_setup_socks5)

        address = ("example.com", 80)
        result = s._make_proxy(fake_connect, address)

        assert result == 0
        assert connect_calls == [("proxy.example", 1080)]
        assert setup_calls == [address]
    finally:
        s.close()
