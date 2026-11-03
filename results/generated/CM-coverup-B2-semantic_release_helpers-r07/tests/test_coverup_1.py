# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

"""Tests for semantic_release.helpers.build_requests_session.

Covers all lines and branches of the function:
- default construction (Session creation, return)
- raise_for_status hook installed / not installed
- retry=True (bool -> default Retry), retry=int (-> Retry(total)), retry=Retry instance
- retry falsy (no adapter mounted)
- invalid retry type (ValueError)
"""

from unittest.mock import MagicMock

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from requests.packages.urllib3.util.retry import Retry

from semantic_release.helpers import build_requests_session


def test_build_requests_session_defaults():
    """Default call: hook installed and default Retry mounted on both schemes."""
    session = build_requests_session()

    assert isinstance(session, Session)

    # raise_for_status=True -> hook installed (lines 27-28)
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1

    # retry=True (bool) -> default Retry() mounted on http:// and https://
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter, HTTPAdapter)
    assert isinstance(https_adapter, HTTPAdapter)
    assert http_adapter is https_adapter  # same adapter mounted for both schemes
    assert isinstance(http_adapter.max_retries, Retry)
    assert http_adapter.max_retries.total == Retry().total

    session.close()


def test_build_requests_session_hook_invokes_raise_for_status():
    """The installed response hook must call raise_for_status on the response."""
    session = build_requests_session()
    hook = session.hooks["response"][0]

    mock_response = MagicMock()
    hook(mock_response)
    mock_response.raise_for_status.assert_called_once_with()

    # A failing response must propagate the HTTPError raised by raise_for_status
    failing_response = MagicMock()
    failing_response.raise_for_status.side_effect = HTTPError("500 Server Error")
    with pytest.raises(HTTPError):
        hook(failing_response)

    session.close()


def test_build_requests_session_no_raise_for_status():
    """raise_for_status=False: no hook installed, retry adapter still mounted."""
    session = build_requests_session(raise_for_status=False, retry=True)

    assert isinstance(session, Session)
    assert not session.hooks.get("response")  # default (empty) hooks preserved

    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)

    session.close()


def test_build_requests_session_retry_int():
    """An integer retry is converted to Retry(total=int)."""
    session = build_requests_session(retry=3)

    adapter = session.get_adapter("http://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 3

    session.close()


def test_build_requests_session_retry_instance():
    """A Retry instance is used as-is (no conversion)."""
    retry = Retry(total=7, connect=2)
    session = build_requests_session(retry=retry)

    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries is retry

    session.close()


def test_build_requests_session_retry_false():
    """retry=False: falsy retry -> no custom adapter mounted, session returned."""
    session = build_requests_session(raise_for_status=False, retry=False)

    assert isinstance(session, Session)
    # Only the default Session adapters remain (max_retries defaults to 0)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries.total == 0

    session.close()


def test_build_requests_session_invalid_retry_type():
    """An invalid retry type raises ValueError with the expected message."""
    with pytest.raises(
        ValueError, match=r"retry should be a bool, int or Retry instance\."
    ):
        build_requests_session(retry="not-a-retry")
