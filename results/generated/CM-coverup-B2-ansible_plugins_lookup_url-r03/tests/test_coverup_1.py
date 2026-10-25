# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

from unittest.mock import Mock, call

import pytest

from ansible.errors import AnsibleError
from ansible.plugins.lookup import url as url_lookup


def _configured_lookup(monkeypatch, split_lines):
    options = {
        "validate_certs": False,
        "use_proxy": True,
        "username": "test-user",
        "password": "test-password",
        "headers": {"X-Test": "yes"},
        "force": True,
        "timeout": 17,
        "http_agent": "pytest-agent",
        "force_basic_auth": True,
        "follow_redirects": "safe",
        "use_gssapi": False,
        "unix_socket": "/tmp/test-url.sock",
        "ca_path": "/tmp/test-ca.pem",
        "unredirected_headers": ["Authorization"],
        "split_lines": split_lines,
    }
    lookup = url_lookup.LookupModule()
    set_options = Mock()
    get_option = Mock(side_effect=options.__getitem__)
    monkeypatch.setattr(lookup, "set_options", set_options)
    monkeypatch.setattr(lookup, "get_option", get_option)
    return lookup, options, set_options, get_option


def _expected_open_url_options(options):
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


def test_run_splits_response_into_text_lines(monkeypatch):
    term = "https://example.test/lines"
    variables = {"inventory_var": "value"}
    lookup, options, set_options, get_option = _configured_lookup(
        monkeypatch, split_lines=True
    )
    response = Mock()
    response.read.return_value = b"first line\nsecond line\r\nthird line\n"
    open_url = Mock(return_value=response)
    vvvv = Mock()
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", vvvv)

    result = lookup.run([term], variables=variables, custom_option="direct-value")

    assert result == ["first line", "second line", "third line"]
    set_options.assert_called_once_with(
        var_options=variables,
        direct={"custom_option": "direct-value"},
    )
    open_url.assert_called_once_with(term, **_expected_open_url_options(options))
    response.read.assert_called_once_with()
    vvvv.assert_called_once_with("url lookup connecting to %s" % term)
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


def test_run_returns_unsplit_response_as_text(monkeypatch):
    term = "https://example.test/body"
    lookup, options, set_options, get_option = _configured_lookup(
        monkeypatch, split_lines=False
    )
    response = Mock()
    response.read.return_value = b"first line\nsecond line"
    open_url = Mock(return_value=response)
    vvvv = Mock()
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", vvvv)

    result = lookup.run([term])

    assert result == ["first line\nsecond line"]
    set_options.assert_called_once_with(var_options=None, direct={})
    open_url.assert_called_once_with(term, **_expected_open_url_options(options))
    response.read.assert_called_once_with()
    vvvv.assert_called_once_with("url lookup connecting to %s" % term)
    assert get_option.call_args_list[-1] == call("split_lines")


@pytest.mark.parametrize(
    ("error_factory", "message_template"),
    [
        (
            lambda term: url_lookup.HTTPError(
                term, 503, "Service Unavailable", None, None
            ),
            "Received HTTP error for %s : %s",
        ),
        (
            lambda term: url_lookup.URLError("DNS lookup failed"),
            "Failed lookup url for %s : %s",
        ),
        (
            lambda term: url_lookup.SSLValidationError("untrusted certificate"),
            "Error validating the server's certificate for %s: %s",
        ),
        (
            lambda term: url_lookup.ConnectionError("connection refused"),
            "Error connecting to %s: %s",
        ),
    ],
    ids=["http-error", "url-error", "ssl-validation-error", "connection-error"],
)
def test_run_converts_open_url_errors_to_ansible_error(
    monkeypatch, error_factory, message_template
):
    term = "https://example.test/failure"
    lookup, options, set_options, get_option = _configured_lookup(
        monkeypatch, split_lines=True
    )
    original_error = error_factory(term)
    open_url = Mock(side_effect=original_error)
    vvvv = Mock()
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", vvvv)

    with pytest.raises(AnsibleError) as raised:
        lookup.run([term], variables={"test": True})

    assert str(raised.value) == message_template % (
        term,
        url_lookup.to_native(original_error),
    )
    set_options.assert_called_once_with(var_options={"test": True}, direct={})
    open_url.assert_called_once_with(term, **_expected_open_url_options(options))
    vvvv.assert_called_once_with("url lookup connecting to %s" % term)
    assert call("split_lines") not in get_option.call_args_list
