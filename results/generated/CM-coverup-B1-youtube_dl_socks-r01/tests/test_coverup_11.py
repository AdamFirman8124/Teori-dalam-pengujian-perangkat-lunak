# file: project/youtube_dl/socks.py:116-119
# asked: {"lines": [117, 119], "branches": []}
# gained: {"lines": [117, 119], "branches": []}

import pytest

from youtube_dl.socks import Proxy, ProxyType, sockssocket


def test_setproxy_sets_proxy_configuration():
    sock = sockssocket()
    try:
        sock.setproxy(
            ProxyType.SOCKS5,
            "proxy.example.com",
            1080,
            rdns=False,
            username="user",
            password="secret",
        )

        assert sock._proxy == Proxy(
            ProxyType.SOCKS5,
            "proxy.example.com",
            1080,
            "user",
            "secret",
            False,
        )
    finally:
        sock.close()


def test_setproxy_rejects_invalid_proxy_type_without_changing_proxy():
    sock = sockssocket()
    try:
        original_proxy = sock._proxy

        with pytest.raises(AssertionError):
            sock.setproxy(999, "proxy.example.com", 1080)

        assert sock._proxy is original_proxy
    finally:
        sock.close()
