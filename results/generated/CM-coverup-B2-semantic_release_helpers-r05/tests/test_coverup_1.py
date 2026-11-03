# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

from unittest import mock

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from semantic_release.helpers import build_requests_session


def test_build_requests_session_defaults():
    """Default call: raise_for_status hook installed, default Retry mounted on both schemes."""
    session = build_requests_session()
    try:
        assert isinstance(session, Session)

        # raise_for_status=True branch: a hook was installed
        hooks = session.hooks["response"]
        assert len(hooks) == 1

        # retry=True (bool) branch: default Retry configuration
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert isinstance(http_adapter, HTTPAdapter)
        assert isinstance(https_adapter, HTTPAdapter)
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == Retry().total
        # the same adapter instance is mounted for both schemes
        assert http_adapter is https_adapter
    finally:
        session.close()


def test_build_requests_session_hook_calls_raise_for_status():
    """The installed hook invokes response.raise_for_status()."""
    session = build_requests_session()
    try:
        (hook,) = session.hooks["response"]
        response = mock.Mock(spec=["raise_for_status"])
        result = hook(response)
        response.raise_for_status.assert_called_once_with()
        assert result is response.raise_for_status.return_value
    finally:
        session.close()


def test_build_requests_session_no_raise_for_status_no_retry():
    """raise_for_status=False and retry=False take both 'falsy' branches."""
    session = build_requests_session(raise_for_status=False, retry=False)
    try:
        assert isinstance(session, Session)
        # no raise_for_status hook installed (default empty hooks)
        assert session.hooks["response"] == []
        # no retry policy configured: default adapter with total == 0
        adapter = session.get_adapter("https://example.com")
        assert isinstance(adapter, HTTPAdapter)
        assert adapter.max_retries.total == 0
    finally:
        session.close()


def test_build_requests_session_retry_int():
    """An integer retry creates a Retry instance with that total."""
    session = build_requests_session(retry=5)
    try:
        adapter = session.get_adapter("https://example.com")
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == 5
    finally:
        session.close()


def test_build_requests_session_retry_instance():
    """A Retry instance is used as-is on the mounted adapter."""
    retry = Retry(total=7, backoff_factor=0.5)
    session = build_requests_session(raise_for_status=False, retry=retry)
    try:
        adapter = session.get_adapter("http://example.com")
        assert isinstance(adapter, HTTPAdapter)
        # the very same Retry instance is used
        assert adapter.max_retries is retry
        assert adapter.max_retries.total == 7
        assert adapter.max_retries.backoff_factor == 0.5
    finally:
        session.close()


def test_build_requests_session_invalid_retry_raises():
    """A non bool/int/Retry value raises ValueError."""
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance."):
        build_requests_session(retry="not-a-retry")
