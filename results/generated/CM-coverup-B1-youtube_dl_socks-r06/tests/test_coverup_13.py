# file: project/youtube_dl/socks.py:177-178
# asked: {"lines": [178], "branches": []}
# gained: {"lines": [178], "branches": []}

from unittest.mock import Mock

from youtube_dl.socks import sockssocket


def test_setup_socks4a_delegates_to_socks4_with_4a_enabled():
    socket_mock = Mock()
    address = ("proxy-target.example", 443)

    sockssocket._setup_socks4a(socket_mock, address)

    socket_mock._setup_socks4.assert_called_once_with(address, is_4a=True)
