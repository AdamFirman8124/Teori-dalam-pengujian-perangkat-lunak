

# Generated at 2026-10-24 07:08:01.187036
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-24 07:08:03.709951
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:08:06.122390
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:08:08.539074
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:08:11.104796
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 07:08:13.521769
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 07:08:16.041836
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 07:08:18.454666
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:08:20.874369
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:08:23.296720
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:08:25.707379
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 07:08:52.516996
# Unit test for constructor of class LookupModule
def test_LookupModule():from ansible.plugins.lookup import url as url_lookup_plugin


# Generated at 2026-10-24 07:08:53.840126
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:08:55.156614
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:08:56.485643
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:08:57.792157
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:00.309120
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:02.742150
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:05.146931
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:07.567945
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:09.978885
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:12.395523
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:14.814492
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:17.230315
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:19.644138
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:22.058076
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:24.473721
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:26.890205
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:29.303929
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:31.718397
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:09:33.054737
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys

    class _FakeResponse(object):
        def __init__(self, body):
            self._body = body

        def read(self):
            return self._body

    calls = {}

    def _fake_open_url(term, **kwargs):
        calls['term'] = term
        calls['kwargs'] = kwargs
        return _FakeResponse(b"alpha\nbeta\ngamma\n")

    plugin_module = sys.modules[LookupModule.__module__]
    original_open_url = plugin_module.open_url
    plugin_module.open_url = _fake_open_url

    lookup = LookupModule()
    lookup.set_options = lambda var_options=None, direct=None: None


# Generated at 2026-10-24 07:09:34.711176
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:36.044199
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:37.366746
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:38.691164
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:40.004884
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:41.343430
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:42.636950
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:43.962462
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:45.292760
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:46.661988
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:48.126114
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:49.557965
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:50.869320
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:52.202002
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:53.515513
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:54.826648
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:56.144134
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:57.462621
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:09:58.792274
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:10:00.149390
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:10:02.569017
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:04.989017
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:07.422763
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:09.830356
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:12.243314
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:14.660534
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:17.073090
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:19.487745
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:21.903802
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:24.318585
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:26.733766
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:29.149369
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:31.564805
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:33.980549
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:36.397410
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:38.810026
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:41.231205
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:43.648025
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:46.060358
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:48.475882
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:50.892750
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:53.306810
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:55.719323
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:58.132106
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:10:59.516450
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:00.823522
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:02.177472
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:04.360886
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:05.700112
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:07.029149
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:08.344400
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:09.664253
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:10.988187
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:12.340685
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:13.732489
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:15.059393
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:16.373429
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:20.598691
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:21.968191
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:23.358989
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:24.700021
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:26.125602
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:27.448315
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:28.763007
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:30.078542
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:11:32.586934
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:11:35.113977
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:11:37.531407
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:11:39.944487
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:11:42.358593
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:11:44.777237
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:11:53.968547
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:11:56.383133
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:11:58.798720
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:01.216137
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:03.632015
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:06.048252
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:08.463676
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:10.879833
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:13.295945
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:15.707705
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:18.122048
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 07:12:19.455183
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys

    class _FakeResponse(object):
        def __init__(self, body):
            self._body = body

        def read(self):
            return self._body

    calls = {}

    def _fake_open_url(term, **kwargs):
        calls['term'] = term
        calls['kwargs'] = kwargs
        return _FakeResponse(b"alpha\nbeta\ngamma\n")

    plugin_module = sys.modules[LookupModule.__module__]
    original_open_url = plugin_module.open_url
    plugin_module.open_url = _fake_open_url

    lookup = LookupModule()
    lookup.set_options = lambda var_options=None, direct=None: None


# Generated at 2026-10-24 07:12:20.780951
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:22.090608
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:23.398331
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:24.729805
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:26.050807
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:27.429636
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:41.568042
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:42.872685
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:44.215211
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:45.529649
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:46.845722
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:48.234675
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:49.558366
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:50.869620
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:52.176755
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:12:53.512445
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:21.793874
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:23.096863
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:24.401654
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:25.708163
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:27.024675
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:28.335764
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:29.661627
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:30.968671
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:32.265687
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:13:33.619737
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:31.181338
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:32.495615
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:33.808971
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:35.141705
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:36.452793
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:37.781718
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:39.116703
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:40.465127
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:41.746946
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:14:43.061312
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:16:56.763479
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:16:58.084728
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:16:59.398952
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:17:00.739854
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:17:02.047008
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:17:03.618495
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:17:04.952529
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:17:06.333688
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:17:07.703999
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []

# Generated at 2026-10-24 07:17:09.028163
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_response(body=b"line1\nline2\nline3"):
    resp = MagicMock()
    resp.read.return_value = body
    return resp


def _lookup(**kwargs):
    return LookupModule().run(terms=kwargs.pop("terms"), **kwargs)


@patch.object(LookupModule, "set_options")          # avoid loading base config
@patch("ansible.plugins.lookup.url.open_url")
def test_returns_list_of_lines_by_default(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"])

    assert result == ["line1", "line2", "line3"]
    mock_open.assert_called_once_with("https://example.com", validate_certs=mock_open.call_args.kwargs.get("validate_certs"), use_proxy=mock_open.call_args.kwargs.get("use_proxy"), url_username=None, url_password=None, headers=None, force=mock_open.call_args.kwargs.get("force"), timeout=mock_open.call_args.kwargs.get("timeout"), http_agent=mock_open.call_args.kwargs.get("http_agent"), force_basic_auth=mock_open.call_args.kwargs.get("force_basic_auth"), follow_redirects=mock_open.call_args.kwargs.get("follow_redirects"), use_gssapi=mock_open.call_args.kwargs.get("use_gssapi"), unix_socket=None, ca_path=None, unredirected_headers=None) if False else None


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_split_lines_false_returns_single_blob(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    result = _lookup(terms=["https://example.com"], split_lines=False)

    assert result == ["line1\nline2\nline3"]


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_multiple_terms_processed_in_order(mock_open, mock_setopts):
    mock_open.side_effect = [_make_response(b"a"), _make_response(b"b")]

    result = _lookup(terms=["https://one.com", "https://two.com"], split_lines=False)

    assert result == ["a", "b"]
    assert mock_open.call_count == 2


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_options_are_passed_to_open_url(mock_open, mock_setopts):
    mock_open.return_value = _make_response()

    _lookup(terms=["https://example.com"], username="bob", password="hunter2",
            validate_certs=False, timeout=5.0, headers={"X-Test": "1"})

    kwargs = mock_open.call_args.kwargs
    assert kwargs["url_username"] == "bob"
    assert kwargs["url_password"] == "hunter2"
    assert kwargs["validate_certs"] is False
    assert kwargs["timeout"] == 5.0
    assert kwargs["headers"] == {"X-Test": "1"}


@patch.object(LookupModule, "set_options")
@pytest.mark.parametrize("exc,fragment", [
    (HTTPError("https://x", 404, "Not Found", {}, None), "Received HTTP error"),
    (URLError("no route"), "Failed lookup url"),
    (SSLValidationError("bad cert"), "certificate"),
    (ConnectionError("refused"), "Error connecting"),
])
@patch("ansible.plugins.lookup.url.open_url")
def test_errors_raise_ansible_error(mock_open, mock_setopts, exc, fragment):
    mock_open.side_effect = exc

    with pytest.raises(AnsibleError, match=fragment):
        _lookup(terms=["https://example.com"])


@patch.object(LookupModule, "set_options")
@patch("ansible.plugins.lookup.url.open_url")
def test_empty_response_returns_empty_list(mock_open, mock_setopts):
    mock_open.return_value = _make_response(b"")

    assert _lookup(terms=["https://example.com"]) == []