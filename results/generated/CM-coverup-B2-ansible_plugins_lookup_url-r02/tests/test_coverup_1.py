# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

from unittest.mock import Mock, call

import pytest

import ansible.plugins.lookup.url as url_lookup
from ansible.errors import AnsibleError


def test_run_opens_url_with_all_options_and_splits_lines(monkeypatch):
    term = "https://example.test/data"
    variables = {"inventory_var": "value"}
    direct = {"validate_certs": False, "timeout": 9}
    options = {
        "validate_certs": False,
        "use_proxy": True,
        "username": "alice",
        "password": "secret",
        "headers": {"X-Test": "yes"},
        "force": True,
        "timeout": 9,
        "http_agent": "pytest-agent",
        "force_basic_auth": True,
        "follow_redirects": "safe",
        "use_gssapi": False,
        "unix_socket": "/tmp/test.sock",
        "ca_path": "/tmp/test-ca.pem",
        "unredirected_headers": ["Authorization"],
        "split_lines": True,
    }

    response = Mock()
    response.read.return_value = b"first line\nsecond line\r\n"
    open_url = Mock(return_value=response)
    log = Mock()

    lookup = url_lookup.LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock(side_effect=lambda name: options[name])

    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", log)

    result = lookup.run([term], variables=variables, **direct)

    assert result == ["first line", "second line"]
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=direct,
    )
    open_url.assert_called_once_with(
        term,
        validate_certs=False,
        use_proxy=True,
        url_username="alice",
        url_password="secret",
        headers={"X-Test": "yes"},
        force=True,
        timeout=9,
        http_agent="pytest-agent",
        force_basic_auth=True,
        follow_redirects="safe",
        use_gssapi=False,
        unix_socket="/tmp/test.sock",
        ca_path="/tmp/test-ca.pem",
        unredirected_headers=["Authorization"],
    )
    assert lookup.get_option.call_args_list == [
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
    response.read.assert_called_once_with()
    log.assert_called_once_with(f"url lookup connecting to {term}")


def test_run_returns_unsplit_response(monkeypatch):
    term = "https://example.test/document"
    options = {
        "validate_certs": True,
        "use_proxy": False,
        "username": None,
        "password": None,
        "headers": {},
        "force": False,
        "timeout": 10,
        "http_agent": "ansible",
        "force_basic_auth": False,
        "follow_redirects": "urllib2",
        "use_gssapi": False,
        "unix_socket": None,
        "ca_path": None,
        "unredirected_headers": [],
        "split_lines": False,
    }

    response = Mock()
    response.read.return_value = b"whole\nresponse"
    open_url = Mock(return_value=response)
    log = Mock()

    lookup = url_lookup.LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock(side_effect=lambda name: options[name])

    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", log)

    result = lookup.run([term])

    assert result == ["whole\nresponse"]
    lookup.set_options.assert_called_once_with(var_options=None, direct={})
    response.read.assert_called_once_with()
    log.assert_called_once_with(f"url lookup connecting to {term}")


def test_run_translates_url_errors_to_ansible_errors(monkeypatch):
    term = "https://example.test/failure"
    options = {
        "validate_certs": True,
        "use_proxy": False,
        "username": None,
        "password": None,
        "headers": {},
        "force": False,
        "timeout": 10,
        "http_agent": "ansible",
        "force_basic_auth": False,
        "follow_redirects": "urllib2",
        "use_gssapi": False,
        "unix_socket": None,
        "ca_path": None,
        "unredirected_headers": [],
        "split_lines": True,
    }
    cases = [
        (
            url_lookup.HTTPError(term, 503, "Unavailable", None, None),
            f"Received HTTP error for {term} : HTTP Error 503: Unavailable",
        ),
        (
            url_lookup.URLError("unavailable"),
            f"Failed lookup url for {term} : <urlopen error unavailable>",
        ),
        (
            url_lookup.SSLValidationError("bad certificate"),
            f"Error validating the server's certificate for {term}: bad certificate",
        ),
        (
            url_lookup.ConnectionError("connection refused"),
            f"Error connecting to {term}: connection refused",
        ),
    ]
    log = Mock()
    monkeypatch.setattr(url_lookup.display, "vvvv", log)

    for index, (original_error, expected_message) in enumerate(cases):
        open_url = Mock(side_effect=original_error)
        monkeypatch.setattr(url_lookup, "open_url", open_url)

        lookup = url_lookup.LookupModule()
        lookup.set_options = Mock()
        lookup.get_option = Mock(side_effect=lambda name: options[name])
        variables = {"case": index}

        with pytest.raises(AnsibleError) as exc_info:
            lookup.run([term], variables=variables, case=index)

        assert expected_message in str(exc_info.value)
        lookup.set_options.assert_called_once_with(
            var_options=variables,
            direct={"case": index},
        )
        open_url.assert_called_once()
        assert call("split_lines") not in lookup.get_option.call_args_list

    assert log.call_args_list == [
        call(f"url lookup connecting to {term}"),
        call(f"url lookup connecting to {term}"),
        call(f"url lookup connecting to {term}"),
        call(f"url lookup connecting to {term}"),
    ]


def test_run_with_no_terms_returns_empty_list_without_opening_url(monkeypatch):
    open_url = Mock()
    log = Mock()
    lookup = url_lookup.LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock()

    monkeypatch.setattr(url_lookup, "open_url", open_url)
    monkeypatch.setattr(url_lookup.display, "vvvv", log)

    result = lookup.run([], variables={"unused": True}, marker="value")

    assert result == []
    lookup.set_options.assert_called_once_with(
        var_options={"unused": True},
        direct={"marker": "value"},
    )
    lookup.get_option.assert_not_called()
    open_url.assert_not_called()
    log.assert_not_called()
