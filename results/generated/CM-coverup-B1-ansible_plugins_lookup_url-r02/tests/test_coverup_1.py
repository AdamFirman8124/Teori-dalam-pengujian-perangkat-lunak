# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

from unittest.mock import Mock, call

import pytest

import ansible.plugins.lookup.url as url_lookup
from ansible.errors import AnsibleError


def test_run_opens_each_url_with_options_and_splits_lines(monkeypatch):
    lookup = url_lookup.LookupModule()
    variables = {"inventory_hostname": "example"}
    options = {
        "validate_certs": False,
        "use_proxy": False,
        "username": "user",
        "password": "secret",
        "headers": {"X-Test": "value"},
        "force": True,
        "timeout": 4.5,
        "http_agent": "test-agent",
        "force_basic_auth": True,
        "follow_redirects": "safe",
        "use_gssapi": False,
        "unix_socket": "/tmp/test.socket",
        "ca_path": "/tmp/test-ca.pem",
        "unredirected_headers": ["Authorization"],
        "split_lines": True,
    }
    responses = [
        Mock(read=Mock(return_value=b"first\nsecond\n")),
        Mock(read=Mock(return_value=b"third")),
    ]
    set_options = Mock()
    get_option = Mock(side_effect=options.__getitem__)
    open_url = Mock(side_effect=responses)
    display_vvvv = Mock()

    monkeypatch.setattr(lookup, "set_options", set_options)
    monkeypatch.setattr(lookup, "get_option", get_option)
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", display_vvvv)

    result = lookup.run(
        ["https://example.test/one", "https://example.test/two"],
        variables=variables,
        split_lines=True,
    )

    assert result == ["first", "second", "third"]
    set_options.assert_called_once_with(
        var_options=variables,
        direct={"split_lines": True},
    )
    expected_request_options = {
        "validate_certs": False,
        "use_proxy": False,
        "url_username": "user",
        "url_password": "secret",
        "headers": {"X-Test": "value"},
        "force": True,
        "timeout": 4.5,
        "http_agent": "test-agent",
        "force_basic_auth": True,
        "follow_redirects": "safe",
        "use_gssapi": False,
        "unix_socket": "/tmp/test.socket",
        "ca_path": "/tmp/test-ca.pem",
        "unredirected_headers": ["Authorization"],
    }
    assert open_url.call_args_list == [
        call("https://example.test/one", **expected_request_options),
        call("https://example.test/two", **expected_request_options),
    ]
    assert display_vvvv.call_args_list == [
        call("url lookup connecting to https://example.test/one"),
        call("url lookup connecting to https://example.test/two"),
    ]
    responses[0].read.assert_called_once_with()
    responses[1].read.assert_called_once_with()


def test_run_returns_unsplit_response_body(monkeypatch):
    lookup = url_lookup.LookupModule()
    options = {
        "validate_certs": True,
        "use_proxy": True,
        "username": None,
        "password": None,
        "headers": {},
        "force": False,
        "timeout": 10,
        "http_agent": "ansible-httpget",
        "force_basic_auth": False,
        "follow_redirects": "urllib2",
        "use_gssapi": False,
        "unix_socket": None,
        "ca_path": None,
        "unredirected_headers": None,
        "split_lines": False,
    }
    response = Mock(read=Mock(return_value=b"first\nsecond\n"))
    set_options = Mock()
    open_url = Mock(return_value=response)

    monkeypatch.setattr(lookup, "set_options", set_options)
    monkeypatch.setattr(
        lookup, "get_option", Mock(side_effect=options.__getitem__)
    )
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", Mock())

    result = lookup.run(
        ["https://example.test/content"],
        variables=None,
        split_lines=False,
    )

    assert result == ["first\nsecond\n"]
    set_options.assert_called_once_with(
        var_options=None,
        direct={"split_lines": False},
    )
    response.read.assert_called_once_with()
    open_url.assert_called_once_with(
        "https://example.test/content",
        validate_certs=True,
        use_proxy=True,
        url_username=None,
        url_password=None,
        headers={},
        force=False,
        timeout=10,
        http_agent="ansible-httpget",
        force_basic_auth=False,
        follow_redirects="urllib2",
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=None,
    )


@pytest.mark.parametrize(
    ("exception_type", "exception_args", "expected_message"),
    [
        (
            url_lookup.HTTPError,
            ("https://example.test/failure", 503, "unavailable", None, None),
            "Received HTTP error for https://example.test/failure : "
            "HTTP Error 503: unavailable",
        ),
        (
            url_lookup.URLError,
            ("unreachable",),
            "Failed lookup url for https://example.test/failure : "
            "<urlopen error unreachable>",
        ),
        (
            url_lookup.SSLValidationError,
            ("certificate rejected",),
            "Error validating the server's certificate for "
            "https://example.test/failure: certificate rejected",
        ),
        (
            url_lookup.ConnectionError,
            ("connection refused",),
            "Error connecting to https://example.test/failure: "
            "connection refused",
        ),
    ],
    ids=["http-error", "url-error", "ssl-validation-error", "connection-error"],
)
def test_run_converts_connection_failures_to_ansible_error(
    monkeypatch, exception_type, exception_args, expected_message
):
    lookup = url_lookup.LookupModule()
    options = {
        "validate_certs": True,
        "use_proxy": True,
        "username": None,
        "password": None,
        "headers": {},
        "force": False,
        "timeout": 10,
        "http_agent": "ansible-httpget",
        "force_basic_auth": False,
        "follow_redirects": "urllib2",
        "use_gssapi": False,
        "unix_socket": None,
        "ca_path": None,
        "unredirected_headers": None,
    }
    set_options = Mock()
    open_url = Mock(side_effect=exception_type(*exception_args))
    display_vvvv = Mock()

    monkeypatch.setattr(lookup, "set_options", set_options)
    monkeypatch.setattr(
        lookup, "get_option", Mock(side_effect=options.__getitem__)
    )
    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", display_vvvv)

    with pytest.raises(AnsibleError) as raised:
        lookup.run(
            ["https://example.test/failure"],
            variables={"test": True},
        )

    assert str(raised.value) == expected_message
    set_options.assert_called_once_with(
        var_options={"test": True},
        direct={},
    )
    display_vvvv.assert_called_once_with(
        "url lookup connecting to https://example.test/failure"
    )
    open_url.assert_called_once_with(
        "https://example.test/failure",
        validate_certs=True,
        use_proxy=True,
        url_username=None,
        url_password=None,
        headers={},
        force=False,
        timeout=10,
        http_agent="ansible-httpget",
        force_basic_auth=False,
        follow_redirects="urllib2",
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=None,
    )
