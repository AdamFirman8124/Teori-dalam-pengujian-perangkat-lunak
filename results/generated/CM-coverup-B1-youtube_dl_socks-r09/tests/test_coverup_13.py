# file: project/youtube_dl/socks.py:177-178
# asked: {"lines": [178], "branches": []}
# gained: {"lines": [178], "branches": []}

from youtube_dl.socks import sockssocket


def test_setup_socks4a_delegates_to_socks4_with_4a_enabled(monkeypatch):
    calls = []

    def fake_setup_socks4(self, address, is_4a=False):
        calls.append((self, address, is_4a))
        return "result"

    monkeypatch.setattr(sockssocket, "_setup_socks4", fake_setup_socks4)

    sock = sockssocket()
    address = ("example.com", 80)
    try:
        result = sock._setup_socks4a(address)

        assert result is None
        assert calls == [(sock, address, True)]
    finally:
        sock.close()
