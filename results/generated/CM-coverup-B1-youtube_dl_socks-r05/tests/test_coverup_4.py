# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

import types

import pytest

from youtube_dl.socks import ProxyType, sockssocket


def _new_sock(proxy):
    s = sockssocket.__new__(sockssocket)
    s._proxy = proxy
    return s


def _proxy_ns(ptype, host="127.0.0.1", port=1080):
    return types.SimpleNamespace(host=host, port=port, type=ptype)


def test_make_proxy_no_proxy_delegates_directly():
    s = _new_sock(None)
    target = ("example.com", 80)
    calls = []

    def fake_connect(sock, addr):
        calls.append(addr)
        assert sock is s
        return 42

    result = s._make_proxy(fake_connect, target)

    assert result == 42
    assert calls == [target]


def test_make_proxy_no_proxy_propagates_none():
    s = _new_sock(None)
    target = ("example.com", 443)
    calls = []

    def fake_connect(sock, addr):
        calls.append(addr)
        return None

    result = s._make_proxy(fake_connect, target)

    assert result is None
    assert calls == [target]


def test_make_proxy_connect_error_returns_code_without_setup(monkeypatch):
    s = _new_sock(_proxy_ns(ProxyType.SOCKS5))
    target = ("example.com", 80)
    connect_calls = []
    setup_calls = []

    def fake_connect(sock, addr):
        connect_calls.append(addr)
        assert sock is s
        return 111

    monkeypatch.setattr(s, "_setup_socks4", lambda addr: setup_calls.append(("socks4", addr)))
    monkeypatch.setattr(s, "_setup_socks4a", lambda addr: setup_calls.append(("socks4a", addr)))
    monkeypatch.setattr(s, "_setup_socks5", lambda addr: setup_calls.append(("socks5", addr)))

    result = s._make_proxy(fake_connect, target)

    assert result == 111
    assert connect_calls == [("127.0.0.1", 1080)]
    assert setup_calls == []


def test_make_proxy_socks4_with_zero_result(monkeypatch):
    proxy = _proxy_ns(ProxyType.SOCKS4, host="10.0.0.1", port=1081)
    s = _new_sock(proxy)
    target = ("example.com", 80)
    connect_calls = []
    setup_calls = []

    def fake_connect(sock, addr):
        connect_calls.append(addr)
        return 0

    monkeypatch.setattr(s, "_setup_socks4", lambda addr: setup_calls.append(addr))
    monkeypatch.setattr(s, "_setup_socks4a", lambda addr: pytest.fail("wrong setup called"))
    monkeypatch.setattr(s, "_setup_socks5", lambda addr: pytest.fail("wrong setup called"))

    result = s._make_proxy(fake_connect, target)

    assert result == 0
    assert connect_calls == [("10.0.0.1", 1081)]
    assert setup_calls == [target]


def test_make_proxy_socks4a_with_none_result(monkeypatch):
    proxy = _proxy_ns(ProxyType.SOCKS4A, host="10.0.0.2", port=1082)
    s = _new_sock(proxy)
    target = ("example.com", 81)
    connect_calls = []
    setup_calls = []

    def fake_connect(sock, addr):
        connect_calls.append(addr)
        return None

    monkeypatch.setattr(s, "_setup_socks4", lambda addr: pytest.fail("wrong setup called"))
    monkeypatch.setattr(s, "_setup_socks4a", lambda addr: setup_calls.append(addr))
    monkeypatch.setattr(s, "_setup_socks5", lambda addr: pytest.fail("wrong setup called"))

    result = s._make_proxy(fake_connect, target)

    assert result is None
    assert connect_calls == [("10.0.0.2", 1082)]
    assert setup_calls == [target]


def test_make_proxy_socks5_with_zero_result(monkeypatch):
    proxy = _proxy_ns(ProxyType.SOCKS5, host="10.0.0.3", port=1083)
    s = _new_sock(proxy)
    target = ("example.com", 82)
    connect_calls = []
    setup_calls = []

    def fake_connect(sock, addr):
        connect_calls.append(addr)
        return 0

    monkeypatch.setattr(s, "_setup_socks4", lambda addr: pytest.fail("wrong setup called"))
    monkeypatch.setattr(s, "_setup_socks4a", lambda addr: pytest.fail("wrong setup called"))
    monkeypatch.setattr(s, "_setup_socks5", lambda addr: setup_calls.append(addr))

    result = s._make_proxy(fake_connect, target)

    assert result == 0
    assert connect_calls == [("10.0.0.3", 1083)]
    assert setup_calls == [target]


def test_make_proxy_socks5_with_none_result(monkeypatch):
    proxy = _proxy_ns(ProxyType.SOCKS5, host="10.0.0.4", port=1084)
    s = _new_sock(proxy)
    target = ("example.com", 83)
    connect_calls = []
    setup_calls = []

    def fake_connect(sock, addr):
        connect_calls.append(addr)
        return None

    monkeypatch.setattr(s, "_setup_socks4", lambda addr: pytest.fail("wrong setup called"))
    monkeypatch.setattr(s, "_setup_socks4a", lambda addr: pytest.fail("wrong setup called"))
    monkeypatch.setattr(s, "_setup_socks5", lambda addr: setup_calls.append(addr))

    result = s._make_proxy(fake_connect, target)

    assert result is None
    assert connect_calls == [("10.0.0.4", 1084)]
    assert setup_calls == [target]
