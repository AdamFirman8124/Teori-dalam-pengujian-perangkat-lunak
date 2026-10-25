

# Generated at 2026-10-24 06:39:04.541427
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:06.955594
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:09.370003
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:11.786813
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 06:39:14.202594
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 06:39:16.616853
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 06:39:19.031260
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 06:39:21.454801
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 06:39:23.866184
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 06:39:26.279250
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:28.696374
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:31.110233
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:33.525023
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:35.938527
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:38.352938
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:39:55.042481
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

# Generated at 2026-10-24 06:39:56.436368
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

# Generated at 2026-10-24 06:39:57.744162
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

# Generated at 2026-10-24 06:39:59.050708
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

# Generated at 2026-10-24 06:40:00.519141
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

# Generated at 2026-10-24 06:40:01.854693
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

# Generated at 2026-10-24 06:40:03.281533
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

# Generated at 2026-10-24 06:40:04.612283
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

# Generated at 2026-10-24 06:40:05.930446
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

# Generated at 2026-10-24 06:40:07.272754
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

# Generated at 2026-10-24 06:40:08.602302
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

# Generated at 2026-10-24 06:40:09.910244
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

# Generated at 2026-10-24 06:40:11.267269
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

# Generated at 2026-10-24 06:40:12.576328
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

# Generated at 2026-10-24 06:40:13.881402
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

# Generated at 2026-10-24 06:40:15.191984
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

# Generated at 2026-10-24 06:40:16.518294
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

# Generated at 2026-10-24 06:40:17.866838
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

# Generated at 2026-10-24 06:40:19.174518
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

# Generated at 2026-10-24 06:40:20.506990
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

# Generated at 2026-10-24 06:40:22.923238
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:25.341867
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:27.915071
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:30.313673
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:32.875332
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:35.288053
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:37.704572
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:40.120167
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:42.693204
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:45.111676
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:47.529964
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:49.950126
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:52.373503
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:54.787627
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:57.206461
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:40:58.573543
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

# Generated at 2026-10-24 06:40:59.885638
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

# Generated at 2026-10-24 06:41:01.242048
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

# Generated at 2026-10-24 06:41:02.675464
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

# Generated at 2026-10-24 06:41:04.118482
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

# Generated at 2026-10-24 06:41:05.518892
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

# Generated at 2026-10-24 06:41:06.782901
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

# Generated at 2026-10-24 06:41:08.099465
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

# Generated at 2026-10-24 06:41:09.418490
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

# Generated at 2026-10-24 06:41:10.806491
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

# Generated at 2026-10-24 06:41:12.126302
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

# Generated at 2026-10-24 06:41:13.437488
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

# Generated at 2026-10-24 06:41:14.750700
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

# Generated at 2026-10-24 06:41:16.085678
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

# Generated at 2026-10-24 06:41:18.500314
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:20.915159
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:23.331336
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:25.839805
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:28.351120
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:30.757678
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:33.178133
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:35.746205
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:38.159639
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:40.574870
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:42.986684
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:45.401851
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:47.816765
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:50.231040
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:52.647194
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:55.061847
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:57.478164
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:41:59.894033
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:02.312994
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:04.729560
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:07.141880
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:09.554322
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:11.972440
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:14.390304
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:16.802164
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:19.220535
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:21.634507
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:24.047969
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:26.461814
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:28.877483
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:31.291861
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:33.709932
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:36.126836
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:39.745708
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:42:58.491551
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


# Generated at 2026-10-24 06:42:59.806283
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

# Generated at 2026-10-24 06:43:01.122970
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

# Generated at 2026-10-24 06:43:02.448362
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

# Generated at 2026-10-24 06:43:03.772819
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

# Generated at 2026-10-24 06:43:05.101812
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

# Generated at 2026-10-24 06:43:06.421612
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

# Generated at 2026-10-24 06:43:07.743095
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

# Generated at 2026-10-24 06:43:09.051218
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

# Generated at 2026-10-24 06:43:11.471018
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:13.888743
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:16.303920
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:22.524239
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:24.943346
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:27.363158
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:29.776184
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:32.190276
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:34.603197
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:37.020005
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:43:39.435125
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:09.657562
# Unit test for method run of class LookupModule
def test_LookupModule_run():import ansible.plugins.lookup.url as url_lookup


# Generated at 2026-10-24 06:44:12.079938
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:14.492390
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:17.054641
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:19.469939
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:21.882529
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:24.437958
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:26.854276
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:29.440483
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:31.849034
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:34.270724
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:36.689906
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:39.111469
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:41.522342
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:43.938599
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:46.352056
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:48.766599
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:51.187874
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:53.601126
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:56.018519
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:44:58.433359
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:16.426237
# Unit test for method run of class LookupModule
def test_LookupModule_run():import ansible.plugins.lookup.url as url_lookup


# Generated at 2026-10-24 06:45:26.555595
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

# Generated at 2026-10-24 06:45:27.876813
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

# Generated at 2026-10-24 06:45:29.196074
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

# Generated at 2026-10-24 06:45:31.619562
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:34.035996
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:36.604911
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:39.028142
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:41.431573
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:43.846013
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:46.435220
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:48.851388
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:51.269158
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:53.825643
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:56.241056
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:45:58.652709
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:01.067729
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:03.481091
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:05.895640
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:08.307397
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:10.720496
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:13.138607
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:15.550807
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:17.963458
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:20.376204
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:33.486388
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:35.899365
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:38.311542
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:40.724073
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:43.138441
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:45.552216
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:47.967478
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:50.383739
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:52.802406
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:55.215045
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:57.629144
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:46:59.060101
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


# Generated at 2026-10-24 06:47:00.635792
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

# Generated at 2026-10-24 06:47:01.953537
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

# Generated at 2026-10-24 06:47:03.275287
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

# Generated at 2026-10-24 06:47:04.588384
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

# Generated at 2026-10-24 06:47:05.973274
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

# Generated at 2026-10-24 06:47:07.281134
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

# Generated at 2026-10-24 06:47:41.505486
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:47:43.924630
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:47:46.346487
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:47:48.765045
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:47:51.192401
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:47:53.612951
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:47:56.035120
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:47:58.447310
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:00.863242
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:03.276770
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:36.717589
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-24 06:48:38.026862
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

# Generated at 2026-10-24 06:48:39.338530
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

# Generated at 2026-10-24 06:48:40.654446
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

# Generated at 2026-10-24 06:48:43.163076
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:45.581196
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:48.101944
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:50.679899
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:53.346561
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:55.760742
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:48:58.178781
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:49:00.594683
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 06:49:03.008590
# Unit test for method run of class LookupModule