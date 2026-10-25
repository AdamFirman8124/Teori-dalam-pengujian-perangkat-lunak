# file: project/youtube_dl/socks.py:116-119
# asked: {"lines": [117, 119], "branches": []}
# gained: {"lines": [117, 119], "branches": []}

import pytest

from youtube_dl.socks import Proxy, ProxyType, sockssocket


@pytest.mark.parametrize(
    "proxytype",
    (ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5),
)
def test_setproxy_sets_proxy_configuration(proxytype):
    sock = sockssocket()
    try:
        sock.setproxy(
            proxytype,
            "proxy.example.com",
            1080,
            rdns=False,
            username="user",
            password="secret",
        )

        assert sock._proxy == Proxy(
            proxytype,
            "proxy.example.com",
            1080,
            "user",
            "secret",
            False,
        )
    finally:
        sock.close()


def test_setproxy_rejects_invalid_proxy_type():
    sock = sockssocket()
    try:
        assert sock._proxy is None

        with pytest.raises(AssertionError):
            sock.setproxy(-1, "proxy.example.com", 1080)

        assert sock._proxy is None
    finally:
        sock.close()
