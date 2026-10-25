# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

import types

import pytest

from youtube_dl.socks import ProxyType, sockssocket


@pytest.fixture
def sock():
    s = sockssocket()
    try:
        yield s
    finally:
        s.close()


def _make_proxy_obj(proxy_type=ProxyType.SOCKS5, host="proxy.example", port=1080):
    return types.SimpleNamespace(type=proxy_type, host=host, port=port)


def test_make_proxy_without_proxy_calls_connect_func_directly(sock, monkeypatch):
    monkeypatch.setattr(sock, "_proxy", None)
    address = ("example.com", 80)
    calls = []
    sentinel = object()

    def connect_func(s, addr):
        calls.append((s, addr))
        return sentinel

    result = sock._make_proxy(connect_func, address)

    assert result is sentinel
    assert calls == [(sock, address)]


def test_make_proxy_returns_connect_error_without_setup(sock, monkeypatch):
    monkeypatch.setattr(sock, "_proxy", _make_proxy_obj())
    setup_calls = []

    def connect_func(s, addr):
        return 1

    for name in ("_setup_socks4", "_setup_socks4a", "_setup_socks5"):
        monkeypatch.setattr(
            sock, name, lambda address, _name=name: setup_calls.append((_name, address))
        )

    result = sock._make_proxy(connect_func, ("example.com", 80))

    assert result == 1
    assert setup_calls == []


@pytest.mark.parametrize("connect_result", [0, None])
def test_make_proxy_runs_setup_on_success(sock, monkeypatch, connect_result):
    proxy = _make_proxy_obj(ProxyType.SOCKS5)
    monkeypatch.setattr(sock, "_proxy", proxy)
    address = ("example.com", 80)
    connect_calls = []
    setup_calls = []

    def connect_func(s, addr):
        connect_calls.append((s, addr))
        return connect_result

    def setup_socks5(addr):
        setup_calls.append(addr)

    monkeypatch.setattr(sock, "_setup_socks5", setup_socks5)

    result = sock._make_proxy(connect_func, address)

    assert result is connect_result
    assert connect_calls == [(sock, (proxy.host, proxy.port))]
    assert setup_calls == [address]


@pytest.mark.parametrize(
    "proxy_type, expected_setup",
    [
        (ProxyType.SOCKS4, "_setup_socks4"),
        (ProxyType.SOCKS4A, "_setup_socks4a"),
        (ProxyType.SOCKS5, "_setup_socks5"),
    ],
)
def test_make_proxy_dispatches_to_correct_setup(
    sock, monkeypatch, proxy_type, expected_setup
):
    monkeypatch.setattr(sock, "_proxy", _make_proxy_obj(proxy_type))
    address = ("example.com", 80)
    setup_calls = []

    def connect_func(s, addr):
        return 0

    for name in ("_setup_socks4", "_setup_socks4a", "_setup_socks5"):
        monkeypatch.setattr(
            sock, name, lambda addr, _name=name: setup_calls.append((_name, addr))
        )

    result = sock._make_proxy(connect_func, address)

    assert result == 0
    assert setup_calls == [(expected_setup, address)]
