# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

import socket

import pytest

from youtube_dl.socks import (
    sockssocket,
    Socks5Auth,
    Socks5Error,
    InvalidVersionError,
    SOCKS5_VERSION,
    SOCKS5_USER_AUTH_VERSION,
    SOCKS5_USER_AUTH_SUCCESS,
)


class FakeSocksSocket(sockssocket):
    """A sockssocket that never touches the network.

    sendall records outgoing packets; recvall replays a scripted
    sequence of server responses; close is recorded, not performed.
    """

    def __init__(self, responses):
        super(FakeSocksSocket, self).__init__()
        self._responses = list(responses)
        self.sent = []
        self.closed = False

    def sendall(self, data):
        self.sent.append(bytes(data))

    def recvall(self, cnt):
        assert self._responses, 'no more scripted responses'
        data = self._responses.pop(0)
        assert len(data) == cnt
        return data

    def close(self):
        self.closed = True


def make_proxy_socket(responses, username=None, password=None):
    s = FakeSocksSocket(responses)
    s._proxy = type('Proxy', (), {
        'username': username,
        'password': password,
    })()
    return s


def test_socks5_auth_none_accepted():
    # Server accepts AUTH_NONE; no user/pass exchange happens.
    s = make_proxy_socket(
        responses=[bytes([SOCKS5_VERSION, Socks5Auth.AUTH_NONE])])

    s._socks5_auth()

    # Offered packet: version, 1 method, AUTH_NONE
    assert s.sent == [bytes([SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE])]
    assert not s.closed


def test_socks5_auth_user_pass_accepted():
    # Credentials present: both methods offered, USER_PASS chosen,
    # auth succeeds.
    s = make_proxy_socket(
        responses=[
            bytes([SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS]),
            bytes([SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS]),
        ],
        username='user', password='pass')

    s._socks5_auth()

    assert s.sent[0] == bytes([
        SOCKS5_VERSION, 2,
        Socks5Auth.AUTH_NONE, Socks5Auth.AUTH_USER_PASS])
    # user/pass packet: version, len+user, len+pass
    assert s.sent[1] == (
        bytes([SOCKS5_USER_AUTH_VERSION]) +
        bytes([4]) + b'user' + bytes([4]) + b'pass')
    assert not s.closed


def test_socks5_auth_no_acceptable():
    # Server rejects all offered methods.
    s = make_proxy_socket(
        responses=[bytes([SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE])])

    with pytest.raises(Socks5Error) as excinfo:
        s._socks5_auth()

    assert excinfo.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert s.closed


def test_socks5_auth_user_pass_chosen_without_credentials():
    # Server picks USER_PASS even though no credentials were offered.
    s = make_proxy_socket(
        responses=[bytes([SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS])])

    with pytest.raises(Socks5Error) as excinfo:
        s._socks5_auth()

    assert excinfo.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert s.closed


def test_socks5_auth_user_pass_rejected():
    # Credentials sent but server reports auth failure.
    s = make_proxy_socket(
        responses=[
            bytes([SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS]),
            bytes([SOCKS5_USER_AUTH_VERSION, 0xFF]),
        ],
        username='user', password='pass')

    with pytest.raises(Socks5Error) as excinfo:
        s._socks5_auth()

    assert excinfo.value.args[0] == Socks5Error.ERR_GENERAL_FAILURE
    assert s.closed


def test_socks5_auth_bad_method_version():
    # Server replies with a wrong version on method selection.
    s = make_proxy_socket(responses=[bytes([0x04, Socks5Auth.AUTH_NONE])])

    with pytest.raises(InvalidVersionError):
        s._socks5_auth()

    assert s.closed


def test_socks5_auth_bad_user_auth_version():
    # Server replies with a wrong version on the user/pass exchange.
    s = make_proxy_socket(
        responses=[
            bytes([SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS]),
            bytes([0x02, SOCKS5_USER_AUTH_SUCCESS]),
        ],
        username='user', password='pass')

    with pytest.raises(InvalidVersionError):
        s._socks5_auth()

    assert s.closed
