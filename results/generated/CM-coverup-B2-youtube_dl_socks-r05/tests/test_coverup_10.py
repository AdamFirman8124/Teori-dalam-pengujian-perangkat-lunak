# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

from youtube_dl.socks import sockssocket


def test_sockssocket_initializes_proxy_and_socket():
    with sockssocket() as sock:
        assert sock._proxy is None
        assert sock.fileno() >= 0

    assert sock.fileno() == -1
