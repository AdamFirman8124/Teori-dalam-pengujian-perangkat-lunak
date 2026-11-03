# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

"""Unit tests for semantic_release.helpers.build_requests_session."""

from unittest.mock import Mock

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from semantic_release.helpers import build_requests_session


def test_build_requests_session_defaults():
    """Default arguments install the raise_for_status hook and a default Retry adapter."""
    session = build_requests_session()

    assert isinstance(session, Session)

    # raise_for_status=True installs a single "response" hook that calls
    # raise_for_status() on the response object it receives.
    assert "response" in session.hooks
    assert len(session.hooks["response"]) == 1
    mock_response = Mock()
    session.hooks["response"][0](mock_response)
    mock_response.raise_for_status.assert_called_once_with()

    # retry=True mounts one shared HTTPAdapter with a default Retry
    # configuration on both the http:// and https:// prefixes.
    http_adapter = session.get_adapter("http://example.com/path")
    https_adapter = session.get_adapter("https://example.com/path")
    assert isinstance(http_adapter, HTTPAdapter)
    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)
    assert http_adapter.max_retries.total == Retry().total


def test_build_requests_session_disabled(monkeypatch):
    """raise_for_status=False and retry=False install neither hook nor adapter."""
    constructed = []
    real_http_adapter = HTTPAdapter

    def recording_http_adapter(*args, **kwargs):
        constructed.append(kwargs)
        return real_http_adapter(*args, **kwargs)

    monkeypatch.setattr(
        "semantic_release.helpers.HTTPAdapter", recording_http_adapter
    )

    session = build_requests_session(raise_for_status=False, retry=False)

    assert isinstance(session, Session)
    # No raise_for_status hook was installed.
    assert session.hooks == {"response": []}
    # build_requests_session did not build (nor mount) any extra adapter.
    assert constructed == []
    # Only the plain Session defaults remain: two distinct adapter instances.
    http_adapter = session.get_adapter("http://example.com")
    https_adapter = session.get_adapter("https://example.com")
    assert isinstance(http_adapter, HTTPAdapter)
    assert http_adapter is not https_adapter


def test_build_requests_session_retry_as_int():
    """An integer retry is converted into a Retry with that total."""
    session = build_requests_session(retry=3)

    adapter = session.get_adapter("https://example.com/path")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)
    assert adapter.max_retries.total == 3
    # The same adapter instance serves both http and https.
    assert session.get_adapter("http://example.com/path") is adapter


def test_build_requests_session_retry_as_retry_instance():
    """A Retry instance is handed to the mounted adapter unchanged."""
    retry = Retry(total=7)
    session = build_requests_session(retry=retry)

    adapter = session.get_adapter("https://example.com/path")
    assert isinstance(adapter, HTTPAdapter)
    assert adapter.max_retries is retry
    assert adapter.max_retries.total == 7
    assert session.get_adapter("http://example.com/path") is adapter


def test_build_requests_session_invalid_retry_raises():
    """Any other retry type is rejected with a ValueError."""
    with pytest.raises(
        ValueError, match=r"retry should be a bool, int or Retry instance\."
    ):
        build_requests_session(retry="not-a-retry")
