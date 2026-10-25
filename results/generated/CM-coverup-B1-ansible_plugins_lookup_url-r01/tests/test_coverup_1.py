# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

import io

import pytest

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup import url as url_lookup


@pytest.fixture
def configured_lookup(monkeypatch):
    lookup = url_lookup.LookupModule()
    calls = {"set_options": [], "get_option": [], "display": []}
    options = {
        "validate_certs": True,
        "use_proxy": False,
        "username": "user",
        "password": "secret",
        "headers": {"X-Test": "value"},
        "force": True,
        "timeout": 17,
        "http_agent": "pytest-agent",
        "force_basic_auth": True,
        "follow_redirects": "all",
        "use_gssapi": False,
        "unix_socket": "/tmp/test.sock",
        "ca_path": "/tmp/test-ca.pem",
        "unredirected_headers": ["Authorization"],
        "split_lines": True,
    }

    def set_options(**kwargs):
        calls["set_options"].append(kwargs)

    def get_option(name):
        calls["get_option"].append(name)
        return options[name]

    monkeypatch.setattr(lookup, "set_options", set_options)
    monkeypatch.setattr(lookup, "get_option", get_option)
    monkeypatch.setattr(
        url_lookup.display,
        "vvvv",
        lambda message: calls["display"].append(message),
    )

    return lookup, options, calls


def test_run_splits_lines_and_passes_all_open_url_options(
    monkeypatch, configured_lookup
):
    lookup, options, calls = configured_lookup
    variables = {"inventory_value": "present"}
    open_url_calls = []

    def fake_open_url(term, **kwargs):
        open_url_calls.append((term, kwargs))
        return io.BytesIO(b"first line\nsecond line\r\n")

    monkeypatch.setattr(url_lookup, "open_url", fake_open_url)

    result = lookup.run(
        ["https://example.test/data"],
        variables=variables,
        direct_value="direct",
    )

    assert result == ["first line", "second line"]
    assert calls["set_options"] == [
        {
            "var_options": variables,
            "direct": {"direct_value": "direct"},
        }
    ]
    assert calls["display"] == [
        "url lookup connecting to https://example.test/data"
    ]
    assert open_url_calls == [
        (
            "https://example.test/data",
            {
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
            },
        )
    ]
    assert calls["get_option"] == [
        "validate_certs",
        "use_proxy",
        "username",
        "password",
        "headers",
        "force",
        "timeout",
        "http_agent",
        "force_basic_auth",
        "follow_redirects",
        "use_gssapi",
        "unix_socket",
        "ca_path",
        "unredirected_headers",
        "split_lines",
    ]


def test_run_returns_unsplit_response(monkeypatch, configured_lookup):
    lookup, options, calls = configured_lookup
    options["split_lines"] = False

    monkeypatch.setattr(
        url_lookup,
        "open_url",
        lambda term, **kwargs: io.BytesIO(b"first line\nsecond line\n"),
    )

    result = lookup.run(["https://example.test/unsplit"])

    assert result == ["first line\nsecond line\n"]
    assert calls["set_options"] == [{"var_options": None, "direct": {}}]
    assert calls["display"] == [
        "url lookup connecting to https://example.test/unsplit"
    ]
    assert calls["get_option"][-1] == "split_lines"


def test_run_with_no_terms_returns_empty_list(monkeypatch, configured_lookup):
    lookup, _, calls = configured_lookup

    def unexpected_open_url(*args, **kwargs):
        pytest.fail("open_url must not be called when terms is empty")

    monkeypatch.setattr(url_lookup, "open_url", unexpected_open_url)

    result = lookup.run([], variables={"unused": True})

    assert result == []
    assert calls["set_options"] == [
        {"var_options": {"unused": True}, "direct": {}}
    ]
    assert calls["get_option"] == []
    assert calls["display"] == []


@pytest.mark.parametrize(
    ("error_kind", "expected_prefix", "expected_detail"),
    [
        (
            "http",
            "Received HTTP error for https://example.test/failure :",
            "unavailable",
        ),
        (
            "url",
            "Failed lookup url for https://example.test/failure :",
            "dns failed",
        ),
        (
            "ssl",
            "Error validating the server's certificate for "
            "https://example.test/failure:",
            "bad certificate",
        ),
        (
            "connection",
            "Error connecting to https://example.test/failure:",
            "connection refused",
        ),
    ],
)
def test_run_converts_open_url_errors_to_ansible_error(
    monkeypatch,
    configured_lookup,
    error_kind,
    expected_prefix,
    expected_detail,
):
    lookup, _, calls = configured_lookup

    if error_kind == "http":
        error = HTTPError(
            "https://example.test/failure",
            503,
            "unavailable",
            {},
            None,
        )
    elif error_kind == "url":
        error = URLError("dns failed")
    elif error_kind == "ssl":
        error = SSLValidationError("bad certificate")
    else:
        error = ConnectionError("connection refused")

    def failing_open_url(term, **kwargs):
        raise error

    monkeypatch.setattr(url_lookup, "open_url", failing_open_url)

    with pytest.raises(AnsibleError) as exc_info:
        lookup.run(["https://example.test/failure"], variables={"key": "value"})

    message = str(exc_info.value)
    assert message.startswith(expected_prefix)
    assert expected_detail in message
    assert calls["set_options"] == [
        {"var_options": {"key": "value"}, "direct": {}}
    ]
    assert calls["display"] == [
        "url lookup connecting to https://example.test/failure"
    ]
    assert "split_lines" not in calls["get_option"]
