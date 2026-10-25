# file: project/youtube_dl/socks.py:116-119
# asked: {"lines": [117, 119], "branches": []}
# gained: {"lines": [117, 119], "branches": []}

import pytest

from youtube_dl import socks


@pytest.mark.parametrize(
    "proxytype",
    (socks.ProxyType.SOCKS4, socks.ProxyType.SOCKS4A, socks.ProxyType.SOCKS5),
)
def test_setproxy_sets_proxy_configuration(proxytype):
    sock = socks.sockssocket()
    try:
        sock.setproxy(
            proxytype,
            "proxy.example.com",
            1080,
            rdns=False,
            username="user",
            password="secret",
        )

        assert sock._proxy == socks.Proxy(
            proxytype,
            "proxy.example.com",
            1080,
            "user",
            "secret",
            False,
        )
    finally:
        sock.close()


def test_setproxy_rejects_invalid_proxy_type_without_changing_configuration():
    sock = socks.sockssocket()
    original_proxy = object()
    sock._proxy = original_proxy

    try:
        with pytest.raises(AssertionError):
            sock.setproxy(-1, "proxy.example.com", 1080)

        assert sock._proxy is original_proxy
    finally:
        sock.close()
