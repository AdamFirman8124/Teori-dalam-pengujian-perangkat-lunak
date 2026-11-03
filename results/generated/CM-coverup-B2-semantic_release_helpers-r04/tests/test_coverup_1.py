# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

"""Tests for semantic_release.helpers.build_requests_session (full line/branch coverage)."""

from unittest.mock import MagicMock

import pytest
from requests import HTTPError, Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from semantic_release.helpers import build_requests_session


def test_build_requests_session_defaults():
    """Defaults: raise_for_status hook installed and default Retry config used."""
    session = build_requests_session()

    assert isinstance(session, Session)
    # raise_for_status=True branch (lines 27-28)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1
    # retry=True -> bool branch (lines 29-31, 36-38)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    # the installed hook actually invokes raise_for_status on the response
    mock_response = MagicMock()
    session.hooks["response"][0](mock_response)
    mock_response.raise_for_status.assert_called_once_with()


def test_build_requests_session_hook_propagates_http_error():
    """The installed hook re-raises HTTPError coming from raise_for_status."""
    session = build_requests_session()
    hook = session.hooks["response"][0]

    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = HTTPError("500 Server Error")

    with pytest.raises(HTTPError, match="500 Server Error"):
        hook(mock_response, timeout=5)  # extra args/kwargs must be accepted


@pytest.mark.parametrize("retry", [False, 0])
def test_build_requests_session_no_retry(retry):
    """raise_for_status=False and a falsy retry skip hook and adapter mounting."""
    session = build_requests_session(raise_for_status=False, retry=retry)

    assert isinstance(session, Session)
    # raise_for_status=False branch: hooks left at their default (empty)
    assert session.hooks.get("response", []) == []
    # retry falsy branch: default adapter (no custom retries) remains mounted
    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 0


def test_build_requests_session_retry_int():
    """An integer retry count is converted into a Retry with that total."""
    session = build_requests_session(retry=5)

    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 5


def test_build_requests_session_retry_instance():
    """A Retry instance is passed through to the adapter unchanged."""
    retry = Retry(total=7, connect=3, read=2)
    session = build_requests_session(retry=retry)

    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries is retry


def test_build_requests_session_invalid_retry_type():
    """An unsupported retry value raises ValueError (lines 34-35)."""
    with pytest.raises(
        ValueError, match=r"retry should be a bool, int or Retry instance\."
    ):
        build_requests_session(retry="many")
