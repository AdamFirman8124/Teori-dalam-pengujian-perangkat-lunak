# file: project/youtube_dl/socks.py:116-119
# asked: {"lines": [117, 119], "branches": []}
# gained: {"lines": [117, 119], "branches": []}

import pytest

from youtube_dl.socks import Proxy, ProxyType, sockssocket


@pytest.fixture
def socks_socket():
    sock = sockssocket()
    try:
        yield sock
    finally:
        sock.close()


@pytest.mark.parametrize(
    "proxytype",
    [ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5],
)
def test_setproxy_sets_all_proxy_options(socks_socket, proxytype):
    socks_socket.setproxy(
        proxytype,
        "proxy.example.com",
        1080,
        rdns=False,
        username="user",
        password="secret",
    )

    assert socks_socket._proxy == Proxy(
        proxytype,
        "proxy.example.com",
        1080,
        "user",
        "secret",
        False,
    )


def test_setproxy_rejects_invalid_proxy_type(socks_socket):
    assert socks_socket._proxy is None

    with pytest.raises(AssertionError):
        socks_socket.setproxy(999, "proxy.example.com", 1080)

    assert socks_socket._proxy is None
