# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

import pytest

from youtube_dl.socks import ProxyType, sockssocket


@pytest.fixture
def sock():
    s = sockssocket()
    try:
        yield s
    finally:
        try:
            s.close()
        except OSError:
            pass


def _set_proxy(sock, proxy_type):
    from types import SimpleNamespace

    sock._proxy = SimpleNamespace(
        host="127.0.0.1",
        port=1080,
        type=proxy_type,
    )


def test_make_proxy_no_proxy_returns_connect_result(sock):
    calls = []

    def fake_connect(self_arg, address):
        calls.append((self_arg, address))
        return 42

    address = ("example.com", 80)
    result = sock._make_proxy(fake_connect, address)

    assert result == 42
    assert calls == [(sock, address)]


def test_make_proxy_nonzero_result_returns_without_setup(sock, monkeypatch):
    _set_proxy(sock, ProxyType.SOCKS5)
    calls = []
    setup_calls = []

    def fake_connect(self_arg, address):
        calls.append((self_arg, address))
        return 111

    monkeypatch.setattr(sock, "_setup_socks4", lambda addr: setup_calls.append(("socks4", addr)))
    monkeypatch.setattr(sock, "_setup_socks4a", lambda addr: setup_calls.append(("socks4a", addr)))
    monkeypatch.setattr(sock, "_setup_socks5", lambda addr: setup_calls.append(("socks5", addr)))

    result = sock._make_proxy(fake_connect, ("example.com", 80))

    assert result == 111
    assert calls == [(sock, ("127.0.0.1", 1080))]
    assert setup_calls == []


@pytest.mark.parametrize(
    "proxy_type,method_name,expected_key",
    [
        (ProxyType.SOCKS4, "_setup_socks4", "socks4"),
        (ProxyType.SOCKS4A, "_setup_socks4a", "socks4a"),
        (ProxyType.SOCKS5, "_setup_socks5", "socks5"),
    ],
)
def test_make_proxy_zero_result_dispatches_to_correct_setup(
    sock, monkeypatch, proxy_type, method_name, expected_key
):
    _set_proxy(sock, proxy_type)
    calls = []
    setup_calls = []

    def fake_connect(self_arg, address):
        calls.append((self_arg, address))
        return 0

    monkeypatch.setattr(sock, "_setup_socks4", lambda addr: setup_calls.append(("socks4", addr)))
    monkeypatch.setattr(sock, "_setup_socks4a", lambda addr: setup_calls.append(("socks4a", addr)))
    monkeypatch.setattr(sock, "_setup_socks5", lambda addr: setup_calls.append(("socks5", addr)))

    address = ("example.com", 443)
    result = sock._make_proxy(fake_connect, address)

    assert result == 0
    assert calls == [(sock, ("127.0.0.1", 1080))]
    assert setup_calls == [(expected_key, address)]


def test_make_proxy_none_result_dispatches_to_setup(sock, monkeypatch):
    _set_proxy(sock, ProxyType.SOCKS5)
    calls = []
    setup_calls = []

    def fake_connect(self_arg, address):
        calls.append((self_arg, address))
        return None

    monkeypatch.setattr(sock, "_setup_socks4", lambda addr: setup_calls.append(("socks4", addr)))
    monkeypatch.setattr(sock, "_setup_socks4a", lambda addr: setup_calls.append(("socks4a", addr)))
    monkeypatch.setattr(sock, "_setup_socks5", lambda addr: setup_calls.append(("socks5", addr)))

    address = ("example.org", 22)
    result = sock._make_proxy(fake_connect, address)

    assert result is None
    assert calls == [(sock, ("127.0.0.1", 1080))]
    assert setup_calls == [("socks5", address)]
