# file: project/youtube_dl/socks.py:272-273
# asked: {"lines": [273], "branches": []}
# gained: {"lines": [273], "branches": []}

import socket

from youtube_dl.socks import sockssocket


def test_connect_ex_delegates_to_make_proxy(monkeypatch):
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        captured = {}

        def fake_make_proxy(connect_func, address):
            captured["func"] = connect_func
            captured["address"] = address
            return 0

        monkeypatch.setattr(s, "_make_proxy", fake_make_proxy)
        target = ("127.0.0.1", 80)
        result = s.connect_ex(target)
        assert result == 0
        assert captured["func"] is socket.socket.connect_ex
        assert captured["address"] == target
    finally:
        s.close()


def test_connect_ex_no_proxy_real_connection():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        addr = server.getsockname()
        s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            assert s._proxy is None
            rc = s.connect_ex(addr)
            assert rc == 0
        finally:
            s.close()
    finally:
        server.close()
