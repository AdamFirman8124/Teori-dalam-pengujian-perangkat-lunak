# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

import pytest

from youtube_dl.socks import (
    InvalidVersionError,
    Proxy,
    SOCKS5_USER_AUTH_SUCCESS,
    SOCKS5_USER_AUTH_VERSION,
    SOCKS5_VERSION,
    Socks5Auth,
    Socks5Error,
    sockssocket,
)


class FakeSocks(object):
    _len_and_data = staticmethod(sockssocket._len_and_data)
    _check_response_version = sockssocket._check_response_version

    def __init__(self, proxy, responses):
        self._proxy = proxy
        self._responses = list(responses)
        self.sent = []
        self.closed = False

    def sendall(self, data):
        self.sent.append(data)

    def _recv_bytes(self, cnt):
        response = self._responses.pop(0)
        assert len(response) == cnt
        return response

    def close(self):
        self.closed = True


def make_proxy(username=None, password=None):
    return Proxy(
        type='socks5',
        host='127.0.0.1',
        port=1080,
        username=username,
        password=password,
        remote_dns=False,
    )


def test_socks5_auth_no_credentials_selects_auth_none():
    fake = FakeSocks(
        make_proxy(),
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    )

    sockssocket._socks5_auth(fake)

    assert fake.sent == [b'\x05\x01\x00']
    assert fake.closed is False
    assert fake._responses == []


def test_socks5_auth_with_credentials_succeeds():
    fake = FakeSocks(
        make_proxy('user', 'pass'),
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS),
        ],
    )

    sockssocket._socks5_auth(fake)

    assert fake.sent == [
        b'\x05\x02\x00\x02',
        b'\x01\x04user\x04pass',
    ]
    assert fake.closed is False
    assert fake._responses == []


@pytest.mark.parametrize(
    'username,password',
    [
        ('user', None),
        (None, 'pass'),
        ('', 'pass'),
        ('user', ''),
    ],
)
def test_socks5_auth_does_not_offer_user_pass_without_both_credentials(
        username, password):
    fake = FakeSocks(
        make_proxy(username, password),
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    )

    sockssocket._socks5_auth(fake)

    assert fake.sent == [b'\x05\x01\x00']
    assert fake.closed is False
    assert fake._responses == []


def test_socks5_auth_accepts_non_user_pass_method():
    fake = FakeSocks(
        make_proxy(),
        [(SOCKS5_VERSION, Socks5Auth.AUTH_GSSAPI)],
    )

    sockssocket._socks5_auth(fake)

    assert fake.sent == [b'\x05\x01\x00']
    assert fake.closed is False
    assert fake._responses == []


def test_socks5_auth_rejects_no_acceptable_method():
    fake = FakeSocks(
        make_proxy(),
        [(SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE)],
    )

    with pytest.raises(Socks5Error) as exc_info:
        sockssocket._socks5_auth(fake)

    assert exc_info.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert fake.sent == [b'\x05\x01\x00']
    assert fake.closed is True
    assert fake._responses == []


@pytest.mark.parametrize(
    'username,password',
    [
        (None, None),
        ('user', None),
        (None, 'pass'),
    ],
)
def test_socks5_auth_rejects_user_pass_when_credentials_are_incomplete(
        username, password):
    fake = FakeSocks(
        make_proxy(username, password),
        [(SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    )

    with pytest.raises(Socks5Error) as exc_info:
        sockssocket._socks5_auth(fake)

    assert exc_info.value.args[0] == Socks5Auth.AUTH_NO_ACCEPTABLE
    assert fake.sent == [b'\x05\x01\x00']
    assert fake.closed is True
    assert fake._responses == []


def test_socks5_auth_encodes_unicode_credentials():
    fake = FakeSocks(
        make_proxy('usér', 'päss'),
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, SOCKS5_USER_AUTH_SUCCESS),
        ],
    )

    sockssocket._socks5_auth(fake)

    username = 'usér'.encode('utf-8')
    password = 'päss'.encode('utf-8')
    assert fake.sent == [
        b'\x05\x02\x00\x02',
        (
            b'\x01'
            + bytes((len(username),))
            + username
            + bytes((len(password),))
            + password
        ),
    ]
    assert fake.closed is False
    assert fake._responses == []


def test_socks5_auth_rejects_failed_user_pass_authentication():
    fake = FakeSocks(
        make_proxy('user', 'pass'),
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION, 1),
        ],
    )

    with pytest.raises(Socks5Error) as exc_info:
        sockssocket._socks5_auth(fake)

    assert exc_info.value.args[0] == Socks5Error.ERR_GENERAL_FAILURE
    assert fake.sent == [
        b'\x05\x02\x00\x02',
        b'\x01\x04user\x04pass',
    ]
    assert fake.closed is True
    assert fake._responses == []


def test_socks5_auth_rejects_invalid_method_response_version():
    fake = FakeSocks(
        make_proxy(),
        [(SOCKS5_VERSION - 1, Socks5Auth.AUTH_NONE)],
    )

    with pytest.raises(InvalidVersionError):
        sockssocket._socks5_auth(fake)

    assert fake.sent == [b'\x05\x01\x00']
    assert fake.closed is True
    assert fake._responses == []


def test_socks5_auth_rejects_invalid_user_pass_response_version():
    fake = FakeSocks(
        make_proxy('user', 'pass'),
        [
            (SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (SOCKS5_USER_AUTH_VERSION + 1, SOCKS5_USER_AUTH_SUCCESS),
        ],
    )

    with pytest.raises(InvalidVersionError):
        sockssocket._socks5_auth(fake)

    assert fake.sent == [
        b'\x05\x02\x00\x02',
        b'\x01\x04user\x04pass',
    ]
    assert fake.closed is True
    assert fake._responses == []
