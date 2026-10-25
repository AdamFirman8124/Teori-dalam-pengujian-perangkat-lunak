# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

from unittest.mock import Mock, call

import pytest

from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.plugins.lookup import url as url_lookup


OPTIONS = {
    "validate_certs": False,
    "use_proxy": False,
    "username": "user",
    "password": "secret",
    "headers": {"X-Test": "value"},
    "force": True,
    "timeout": 15,
    "http_agent": "pytest-agent",
    "force_basic_auth": True,
    "follow_redirects": "all",
    "use_gssapi": False,
    "unix_socket": "/tmp/test.sock",
    "ca_path": "/tmp/ca.pem",
    "unredirected_headers": ["Authorization"],
}


def _configure_lookup(monkeypatch, split_lines):
    lookup = url_lookup.LookupModule()
    set_options = Mock()
    get_option = Mock(
        side_effect=lambda name: split_lines
        if name == "split_lines"
        else OPTIONS[name]
    )
    monkeypatch.setattr(lookup, "set_options", set_options)
    monkeypatch.setattr(lookup, "get_option", get_option)
    return lookup, set_options, get_option


def _expected_open_url_kwargs():
    return {
        "validate_certs": OPTIONS["validate_certs"],
        "use_proxy": OPTIONS["use_proxy"],
        "url_username": OPTIONS["username"],
        "url_password": OPTIONS["password"],
        "headers": OPTIONS["headers"],
        "force": OPTIONS["force"],
        "timeout": OPTIONS["timeout"],
        "http_agent": OPTIONS["http_agent"],
        "force_basic_auth": OPTIONS["force_basic_auth"],
        "follow_redirects": OPTIONS["follow_redirects"],
        "use_gssapi": OPTIONS["use_gssapi"],
        "unix_socket": OPTIONS["unix_socket"],
        "ca_path": OPTIONS["ca_path"],
        "unredirected_headers": OPTIONS["unredirected_headers"],
    }


def test_run_splits_response_into_lines(monkeypatch):
    term = "https://example.invalid/lines"
    variables = {"inventory_hostname": "test-host"}
    direct = {"unused_option": "value"}
    response = Mock()
    response.read.return_value = b"first line\nsecond line\r\nthird line"

    lookup, set_options, get_option = _configure_lookup(
        monkeypatch, split_lines=True
    )
    open_url = Mock(return_value=response)
    display_vvvv = Mock()
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", display_vvvv)

    result = lookup.run([term], variables=variables, **direct)

    assert result == ["first line", "second line", "third line"]
    set_options.assert_called_once_with(var_options=variables, direct=direct)
    display_vvvv.assert_called_once_with(
        "url lookup connecting to %s" % term
    )
    open_url.assert_called_once_with(term, **_expected_open_url_kwargs())
    response.read.assert_called_once_with()
    assert get_option.call_args_list == [
        call("validate_certs"),
        call("use_proxy"),
        call("username"),
        call("password"),
        call("headers"),
        call("force"),
        call("timeout"),
        call("http_agent"),
        call("force_basic_auth"),
        call("follow_redirects"),
        call("use_gssapi"),
        call("unix_socket"),
        call("ca_path"),
        call("unredirected_headers"),
        call("split_lines"),
    ]


def test_run_returns_unsplit_response(monkeypatch):
    term = "https://example.invalid/body"
    response = Mock()
    response.read.return_value = b"first line\nsecond line"

    lookup, set_options, get_option = _configure_lookup(
        monkeypatch, split_lines=False
    )
    open_url = Mock(return_value=response)
    display_vvvv = Mock()
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", display_vvvv)

    result = lookup.run([term])

    assert result == ["first line\nsecond line"]
    set_options.assert_called_once_with(var_options=None, direct={})
    display_vvvv.assert_called_once_with(
        "url lookup connecting to %s" % term
    )
    open_url.assert_called_once_with(term, **_expected_open_url_kwargs())
    response.read.assert_called_once_with()
    assert get_option.call_args_list[-1] == call("split_lines")


@pytest.mark.parametrize(
    ("exception", "expected_message"),
    [
        (
            url_lookup.HTTPError(
                "https://example.invalid/http",
                500,
                "server error",
                None,
                None,
            ),
            "Received HTTP error for {term} : {error}",
        ),
        (
            url_lookup.URLError("network unavailable"),
            "Failed lookup url for {term} : {error}",
        ),
        (
            url_lookup.SSLValidationError("certificate rejected"),
            "Error validating the server's certificate for {term}: {error}",
        ),
        (
            url_lookup.ConnectionError("connection refused"),
            "Error connecting to {term}: {error}",
        ),
    ],
    ids=[
        "http-error",
        "url-error",
        "ssl-validation-error",
        "connection-error",
    ],
)
def test_run_converts_url_failures_to_ansible_errors(
    monkeypatch, exception, expected_message
):
    term = "https://example.invalid/failure"
    variables = {"test_variable": True}

    lookup, set_options, get_option = _configure_lookup(
        monkeypatch, split_lines=True
    )
    open_url = Mock(side_effect=exception)
    display_vvvv = Mock()
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", display_vvvv)

    with pytest.raises(AnsibleError) as raised:
        lookup.run([term], variables=variables)

    assert str(raised.value) == expected_message.format(
        term=term, error=to_native(exception)
    )
    set_options.assert_called_once_with(var_options=variables, direct={})
    display_vvvv.assert_called_once_with(
        "url lookup connecting to %s" % term
    )
    open_url.assert_called_once_with(term, **_expected_open_url_kwargs())
    assert call("split_lines") not in get_option.call_args_list
