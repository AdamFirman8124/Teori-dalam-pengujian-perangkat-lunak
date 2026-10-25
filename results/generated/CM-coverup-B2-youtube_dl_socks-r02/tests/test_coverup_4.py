# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

import pytest

from youtube_dl.socks import ProxyType, sockssocket


class Proxy(object):
    def __init__(self, proxytype, host='127.0.0.1', port=1080):
        self.type = proxytype
        self.host = host
        self.port = port


def make_socket(proxy=None):
    # Bypass socket.__init__ so no file descriptor is ever created.
    sock = sockssocket.__new__(sockssocket)
    sock._proxy = proxy
    return sock


def test_make_proxy_no_proxy_calls_connect_directly(monkeypatch):
    """Without a proxy, connect_func is called with the original address."""
    sock = make_socket(proxy=None)
    calls = []

    def connect_func(s, address):
        calls.append((s, address))
        return 12345

    result = sock._make_proxy(connect_func, ('example.com', 80))

    assert result == 12345
    assert calls == [(sock, ('example.com', 80))]


@pytest.mark.parametrize('proxytype,setup_name', [
    (ProxyType.SOCKS4, '_setup_socks4'),
    (ProxyType.SOCKS4A, '_setup_socks4a'),
    (ProxyType.SOCKS5, '_setup_socks5'),
])
def test_make_proxy_success_dispatches_setup(monkeypatch, proxytype, setup_name):
    """With a proxy and a successful connect (result 0), the proper setup
    function runs and 0 is returned."""
    sock = make_socket(proxy=Proxy(proxytype))
    setup_calls = []
    monkeypatch.setattr(
        sockssocket, setup_name,
        lambda self, address: setup_calls.append((self, address)),
        raising=True)

    connect_calls = []

    def connect_func(s, address):
        connect_calls.append((s, address))
        return 0

    result = sock._make_proxy(connect_func, ('example.com', 80))

    assert result == 0
    # connect_func was redirected to the proxy host/port
    assert connect_calls == [(sock, ('127.0.0.1', 1080))]
    # the setup function for the proxy type was invoked with the dest address
    assert setup_calls == [(sock, ('example.com', 80))]


def test_make_proxy_connect_error_returns_early(monkeypatch):
    """A nonzero connect result short-circuits: no setup function runs."""
    sock = make_socket(proxy=Proxy(ProxyType.SOCKS5))

    def setup_should_not_run(self, address):
        raise AssertionError('setup function must not be called on error')

    monkeypatch.setattr(sockssocket, '_setup_socks5', setup_should_not_run,
                        raising=True)

    def connect_func(s, address):
        return 10061  # e.g. WSAECONNREFUSED

    result = sock._make_proxy(connect_func, ('example.com', 80))

    assert result == 10061


def test_make_proxy_none_result_still_runs_setup(monkeypatch):
    """A None connect result is not treated as an error: setup runs and
    None is returned."""
    sock = make_socket(proxy=Proxy(ProxyType.SOCKS4))
    setup_calls = []
    monkeypatch.setattr(
        sockssocket, '_setup_socks4',
        lambda self, address: setup_calls.append((self, address)),
        raising=True)

    def connect_func(s, address):
        return None

    result = sock._make_proxy(connect_func, ('example.com', 80))

    assert result is None
    assert setup_calls == [(sock, ('example.com', 80))]
