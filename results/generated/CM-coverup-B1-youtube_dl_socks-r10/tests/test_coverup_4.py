# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

from youtube_dl.socks import Proxy, ProxyType, sockssocket


def _new_sock(proxy):
    s = sockssocket.__new__(sockssocket)
    s._proxy = proxy
    return s


def test_make_proxy_no_proxy_delegates_directly():
    s = _new_sock(None)
    sentinel_address = ("example.com", 80)
    calls = []

    def fake_connect(sock, addr):
        calls.append((sock, addr))
        return 0

    result = s._make_proxy(fake_connect, sentinel_address)
    assert result == 0
    assert len(calls) == 1
    assert calls[0][0] is s
    assert calls[0][1] is sentinel_address


def test_make_proxy_connect_failure_returns_early(monkeypatch):
    s = _new_sock(Proxy(ProxyType.SOCKS5, "127.0.0.1", 1080, None, None, False))
    setup_calls = []

    def fake_connect(sock, addr):
        assert sock is s
        assert addr == ("127.0.0.1", 1080)
        return 1

    monkeypatch.setattr(s, "_setup_socks4", lambda addr: setup_calls.append(("_setup_socks4", addr)))
    monkeypatch.setattr(s, "_setup_socks4a", lambda addr: setup_calls.append(("_setup_socks4a", addr)))
    monkeypatch.setattr(s, "_setup_socks5", lambda addr: setup_calls.append(("_setup_socks5", addr)))

    result = s._make_proxy(fake_connect, ("example.com", 80))

    assert result == 1
    assert setup_calls == []


def test_make_proxy_socks4_success_zero(monkeypatch):
    proxy = Proxy(ProxyType.SOCKS4, "proxy.example", 1080, None, None, True)
    s = _new_sock(proxy)
    target = ("example.com", 80)
    connect_calls = []
    setup_calls = []

    def fake_connect(sock, addr):
        connect_calls.append(addr)
        assert sock is s
        return 0

    def fake_setup_socks4(addr):
        setup_calls.append(addr)
        return None

    monkeypatch.setattr(s, "_setup_socks4", fake_setup_socks4)
    monkeypatch.setattr(s, "_setup_socks4a", lambda addr: setup_calls.append("wrong-a"))
    monkeypatch.setattr(s, "_setup_socks5", lambda addr: setup_calls.append("wrong-5"))

    result = s._make_proxy(fake_connect, target)

    assert result == 0
    assert connect_calls == [("proxy.example", 1080)]
    assert setup_calls == [target]


def test_make_proxy_socks4a_success_none(monkeypatch):
    proxy = Proxy(ProxyType.SOCKS4A, "proxy.example", 1081, None, None, True)
    s = _new_sock(proxy)
    target = ("example.com", 443)
    connect_calls = []
    setup_calls = []

    def fake_connect(sock, addr):
        connect_calls.append(addr)
        assert sock is s
        return None

    def fake_setup_socks4a(addr):
        setup_calls.append(addr)

    monkeypatch.setattr(s, "_setup_socks4", lambda addr: setup_calls.append("wrong-4"))
    monkeypatch.setattr(s, "_setup_socks4a", fake_setup_socks4a)
    monkeypatch.setattr(s, "_setup_socks5", lambda addr: setup_calls.append("wrong-5"))

    result = s._make_proxy(fake_connect, target)

    assert result is None
    assert connect_calls == [("proxy.example", 1081)]
    assert setup_calls == [target]


def test_make_proxy_socks5_success_zero(monkeypatch):
    proxy = Proxy(ProxyType.SOCKS5, "127.0.0.1", 1080, "user", "pass", False)
    s = _new_sock(proxy)
    target = ("example.org", 8080)
    connect_calls = []
    setup_calls = []

    def fake_connect(sock, addr):
        connect_calls.append(addr)
        assert sock is s
        return 0

    def fake_setup_socks5(addr):
        setup_calls.append(addr)

    monkeypatch.setattr(s, "_setup_socks4", lambda addr: setup_calls.append("wrong-4"))
    monkeypatch.setattr(s, "_setup_socks4a", lambda addr: setup_calls.append("wrong-a"))
    monkeypatch.setattr(s, "_setup_socks5", fake_setup_socks5)

    result = s._make_proxy(fake_connect, target)

    assert result == 0
    assert connect_calls == [("127.0.0.1", 1080)]
    assert setup_calls == [target]
