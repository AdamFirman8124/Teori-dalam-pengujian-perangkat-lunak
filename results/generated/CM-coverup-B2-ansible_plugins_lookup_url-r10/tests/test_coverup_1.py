# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

from unittest.mock import MagicMock, call

import pytest

from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
import ansible.plugins.lookup.url as url_lookup


def _options(split_lines):
    return {
        "validate_certs": True,
        "use_proxy": False,
        "username": "alice",
        "password": "secret",
        "headers": {"X-Test": "yes"},
        "force": True,
        "timeout": 17,
        "http_agent": "test-agent",
        "force_basic_auth": True,
        "follow_redirects": "safe",
        "use_gssapi": False,
        "unix_socket": "/tmp/test.socket",
        "ca_path": "/tmp/test-ca.pem",
        "unredirected_headers": ["Authorization"],
        "split_lines": split_lines,
    }


def _expected_open_url_kwargs(options):
    return {
        "validate_certs": options["validate_certs"],
        "use_proxy": options["use_proxy"],
        "url_username": options["username"],
        "url_password": options["password"],
        "headers": options["headers"],
        "force": options["force"],
        "timeout": options["timeout"],
        "http_agent": options["http_agent"],
        "force_basic_auth": options["force_basic_auth"],
        "follow_redirects": options["follow_redirects"],
        "use_gssapi": options["use_gssapi"],
        "unix_socket": options["unix_socket"],
        "ca_path": options["ca_path"],
        "unredirected_headers": options["unredirected_headers"],
    }


@pytest.mark.parametrize(
    ("split_lines", "body", "expected"),
    [
        (True, b"first line\nsecond line\r\n", ["first line", "second line"]),
        (False, b"first line\nsecond line\r\n", ["first line\nsecond line\r\n"]),
    ],
)
def test_run_reads_response_and_honors_split_lines(
    monkeypatch, split_lines, body, expected
):
    lookup = url_lookup.LookupModule()
    options = _options(split_lines)
    response = MagicMock()
    response.read.return_value = body
    open_url = MagicMock(return_value=response)
    set_options = MagicMock()
    get_option = MagicMock(side_effect=options.__getitem__)
    display = MagicMock()

    monkeypatch.setattr(lookup, "set_options", set_options)
    monkeypatch.setattr(lookup, "get_option", get_option)
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", display)

    variables = {"inventory_variable": "value"}
    direct_options = {"timeout": 3}
    term = "https://example.test/resource"

    result = lookup.run([term], variables=variables, **direct_options)

    assert result == expected
    set_options.assert_called_once_with(
        var_options=variables,
        direct=direct_options,
    )
    display.assert_called_once_with(
        "url lookup connecting to https://example.test/resource"
    )
    open_url.assert_called_once_with(term, **_expected_open_url_kwargs(options))
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


@pytest.mark.parametrize(
    ("error_kind", "message_template"),
    [
        ("http", "Received HTTP error for {term} : {error}"),
        ("url", "Failed lookup url for {term} : {error}"),
        (
            "ssl",
            "Error validating the server's certificate for {term}: {error}",
        ),
        ("connection", "Error connecting to {term}: {error}"),
    ],
)
def test_run_converts_transport_errors_to_ansible_error(
    monkeypatch, error_kind, message_template
):
    if error_kind == "http":
        error = url_lookup.HTTPError(
            "https://example.test/failure",
            503,
            "Service Unavailable",
            None,
            None,
        )
    elif error_kind == "url":
        error = url_lookup.URLError("name resolution failed")
    elif error_kind == "ssl":
        error = url_lookup.SSLValidationError("certificate verify failed")
    else:
        error = url_lookup.ConnectionError("connection refused")

    lookup = url_lookup.LookupModule()
    options = _options(True)
    set_options = MagicMock()
    get_option = MagicMock(side_effect=options.__getitem__)
    open_url = MagicMock(side_effect=error)
    display = MagicMock()

    monkeypatch.setattr(lookup, "set_options", set_options)
    monkeypatch.setattr(lookup, "get_option", get_option)
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", display)

    variables = {"inventory_variable": "value"}
    direct_options = {"validate_certs": False}
    term = "https://example.test/failure"

    with pytest.raises(AnsibleError) as exc_info:
        lookup.run([term], variables=variables, **direct_options)

    assert str(exc_info.value) == message_template.format(
        term=term,
        error=to_native(error),
    )
    set_options.assert_called_once_with(
        var_options=variables,
        direct=direct_options,
    )
    display.assert_called_once_with(
        "url lookup connecting to https://example.test/failure"
    )
    open_url.assert_called_once_with(term, **_expected_open_url_kwargs(options))
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
    ]
