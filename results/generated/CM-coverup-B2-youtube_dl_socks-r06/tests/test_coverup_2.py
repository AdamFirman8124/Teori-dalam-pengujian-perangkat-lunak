# file: project/youtube_dl/socks.py:180-214
# asked: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}
# gained: {"lines": [181, 183, 184, 185, 187, 188, 190, 192, 194, 196, 197, 198, 199, 201, 202, 203, 204, 205, 206, 208, 210, 212, 213, 214], "branches": [[184, 185], [184, 187], [196, 198], [196, 201], [201, 0], [201, 202], [212, 0], [212, 213]]}

import struct
import pytest
from types import SimpleNamespace

from youtube_dl.socks import sockssocket, Socks5Auth, Socks5Error
import youtube_dl.socks as socks_mod


def _make_socket(username=None, password=None, recv_responses=None):
    s = sockssocket.__new__(sockssocket)
    s._proxy = SimpleNamespace(username=username, password=password)
    sent = []
    recv_queue = list(recv_responses or [])
    closed = []

    def fake_sendall(data):
        sent.append(bytes(data))

    def fake_recv(cnt):
        assert recv_queue, "no more mocked _recv_bytes responses"
        resp = recv_queue.pop(0)
        assert len(resp) == cnt
        return resp

    def fake_close(*args, **kwargs):
        closed.append(True)

    s.sendall = fake_sendall
    s._recv_bytes = fake_recv
    s.close = fake_close
    return s, sent, recv_queue, closed


def test_socks5_auth_none_no_credentials_success():
    s, sent, _, closed = _make_socket(
        username=None,
        password=None,
        recv_responses=[(socks_mod.SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    )
    s._socks5_auth()
    assert closed == []
    assert len(sent) == 1
    assert sent[0] == struct.pack('!BBB', socks_mod.SOCKS5_VERSION, 1, Socks5Auth.AUTH_NONE)


def test_socks5_auth_with_credentials_none_selected_success():
    # covers: username/password present but server selects AUTH_NONE,
    # so second if (method == USER_PASS) is False
    s, sent, _, closed = _make_socket(
        username='user',
        password='pass',
        recv_responses=[(socks_mod.SOCKS5_VERSION, Socks5Auth.AUTH_NONE)],
    )
    s._socks5_auth()
    assert closed == []
    assert len(sent) == 1
    assert sent[0] == struct.pack(
        '!BBBB', socks_mod.SOCKS5_VERSION, 2,
        Socks5Auth.AUTH_NONE, Socks5Auth.AUTH_USER_PASS,
    )


def test_socks5_auth_user_pass_success():
    username = 'bob'
    password = 's3cret'
    s, sent, _, closed = _make_socket(
        username=username,
        password=password,
        recv_responses=[
            (socks_mod.SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (socks_mod.SOCKS5_USER_AUTH_VERSION, socks_mod.SOCKS5_USER_AUTH_SUCCESS),
        ],
    )
    s._socks5_auth()
    assert closed == []
    assert len(sent) == 2
    assert sent[0] == struct.pack(
        '!BBBB', socks_mod.SOCKS5_VERSION, 2,
        Socks5Auth.AUTH_NONE, Socks5Auth.AUTH_USER_PASS,
    )
    ub = username.encode('utf-8')
    pb = password.encode('utf-8')
    expected2 = (
        struct.pack('!B', socks_mod.SOCKS5_USER_AUTH_VERSION)
        + sockssocket._len_and_data(ub)
        + sockssocket._len_and_data(pb)
    )
    assert sent[1] == expected2


def test_socks5_auth_no_acceptable_rejected():
    s, sent, _, closed = _make_socket(
        username=None,
        password=None,
        recv_responses=[(socks_mod.SOCKS5_VERSION, Socks5Auth.AUTH_NO_ACCEPTABLE)],
    )
    with pytest.raises(Socks5Error):
        s._socks5_auth()
    assert closed == [True]
    assert len(sent) == 1


def test_socks5_auth_user_pass_requested_without_any_credentials():
    # covers: method == USER_PASS and (not username ...) -> True via missing username
    s, sent, _, closed = _make_socket(
        username=None,
        password=None,
        recv_responses=[(socks_mod.SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    )
    with pytest.raises(Socks5Error):
        s._socks5_auth()
    assert closed == [True]
    assert len(sent) == 1


def test_socks5_auth_user_pass_requested_missing_password():
    # covers: method == USER_PASS and (... or not password) -> True via missing password
    s, sent, _, closed = _make_socket(
        username='onlyuser',
        password=None,
        recv_responses=[(socks_mod.SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    )
    with pytest.raises(Socks5Error):
        s._socks5_auth()
    assert closed == [True]
    assert len(sent) == 1


def test_socks5_auth_user_pass_requested_missing_username():
    # covers other side of `or`: username falsy while password present
    s, sent, _, closed = _make_socket(
        username=None,
        password='onlypass',
        recv_responses=[(socks_mod.SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS)],
    )
    with pytest.raises(Socks5Error):
        s._socks5_auth()
    assert closed == [True]
    assert len(sent) == 1


def test_socks5_auth_user_pass_server_failure_status():
    s, sent, _, closed = _make_socket(
        username='bob',
        password='s3cret',
        recv_responses=[
            (socks_mod.SOCKS5_VERSION, Socks5Auth.AUTH_USER_PASS),
            (socks_mod.SOCKS5_USER_AUTH_VERSION, socks_mod.Socks5Error.ERR_GENERAL_FAILURE),
        ],
    )
    with pytest.raises(Socks5Error):
        s._socks5_auth()
    assert closed == [True]
    assert len(sent) == 2
