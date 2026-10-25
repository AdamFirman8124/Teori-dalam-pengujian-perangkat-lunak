# file: project/youtube_dl/socks.py:116-119
# asked: {"lines": [117, 119], "branches": []}
# gained: {"lines": [117, 119], "branches": []}

import pytest

from youtube_dl.socks import ProxyType, sockssocket


@pytest.fixture
def make_socks_socket():
    created = []

    def _make():
        s = sockssocket()
        created.append(s)
        return s

    yield _make

    for s in created:
        try:
            s.close()
        except OSError:
            pass


@pytest.mark.parametrize(
    'proxytype',
    [ProxyType.SOCKS4, ProxyType.SOCKS4A, ProxyType.SOCKS5],
    ids=['socks4', 'socks4a', 'socks5'],
)
def test_setproxy_valid_types(make_socks_socket, proxytype):
    s = make_socks_socket()
    assert s._proxy is None

    s.setproxy(proxytype, '127.0.0.1', 1080)

    assert s._proxy is not None
    assert s._proxy.type == proxytype
    assert s._proxy.host == '127.0.0.1'
    assert s._proxy.port == 1080
    assert s._proxy.username is None
    assert s._proxy.password is None
    assert s._proxy.remote_dns is True


def test_setproxy_all_arguments(make_socks_socket):
    s = make_socks_socket()

    s.setproxy(
        ProxyType.SOCKS5, 'proxy.example.com', 9050,
        rdns=False, username='user', password='pass',
    )

    assert s._proxy == (
        ProxyType.SOCKS5, 'proxy.example.com', 9050, 'user', 'pass', False,
    )
    assert s._proxy.remote_dns is False


def test_setproxy_invalid_type_raises(make_socks_socket):
    s = make_socks_socket()

    with pytest.raises(AssertionError):
        s.setproxy(3, '127.0.0.1', 1080)

    # The proxy must not have been set when the assertion fails.
    assert s._proxy is None
