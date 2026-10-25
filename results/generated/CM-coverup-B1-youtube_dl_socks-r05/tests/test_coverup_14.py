# file: project/youtube_dl/socks.py:177-178
# asked: {"lines": [178], "branches": []}
# gained: {"lines": [178], "branches": []}

import types

from youtube_dl import socks as socks_module
from youtube_dl.compat import compat_struct_pack
from youtube_dl.socks import sockssocket


def test_setup_socks4a_delegates_to_setup_socks4_with_is_4a_true(monkeypatch):
    sock = sockssocket()
    try:
        calls = []

        def fake_setup_socks4(address, is_4a=False):
            calls.append((address, is_4a))
            return ("127.0.0.1", 8080)

        monkeypatch.setattr(sock, "_setup_socks4", fake_setup_socks4)

        result = sock._setup_socks4a(("example.com", 8080))

        assert calls == [(("example.com", 8080), True)]
        assert result is None
    finally:
        sock.close()


def test_setup_socks4a_real_socks4_flow_uses_remote_dns(monkeypatch):
    sock = sockssocket()
    try:
        resolve_calls = []
        sent = []

        def fake_resolve_address(destaddr, default, use_remote_dns):
            resolve_calls.append((destaddr, default, use_remote_dns))
            return b"\x00\x00\x00\x01"

        reply = compat_struct_pack(
            "!BBHI",
            socks_module.SOCKS4_REPLY_VERSION,
            int(socks_module.Socks4Error.ERR_SUCCESS),
            8080,
            0x7F000001,
        )

        monkeypatch.setattr(sock, "_resolve_address", fake_resolve_address)
        monkeypatch.setattr(sock, "sendall", lambda data: sent.append(data))
        monkeypatch.setattr(sock, "recvall", lambda cnt: reply[:cnt])
        monkeypatch.setattr(
            sock,
            "_proxy",
            types.SimpleNamespace(username="user", remote_dns=True),
        )

        result = sock._setup_socks4a(("example.com", 8080))

        assert result is None
        assert resolve_calls == [
            ("example.com", socks_module.SOCKS4_DEFAULT_DSTIP, True)
        ]
        assert len(sent) == 1
        packet = sent[0]
        assert packet[0] == socks_module.SOCKS4_VERSION
        assert packet[1] == int(socks_module.Socks4Command.CMD_CONNECT)
        assert packet[2:4] == compat_struct_pack("!H", 8080)
        assert packet[4:8] == b"\x00\x00\x00\x01"
        assert packet[8:] == b"user\x00example.com\x00"
    finally:
        sock.close()
