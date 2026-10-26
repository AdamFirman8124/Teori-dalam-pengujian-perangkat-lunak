# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from semantic_release.helpers import build_requests_session


def test_default_session_with_raise_and_retry():
    session = build_requests_session()
    try:
        assert isinstance(session, Session)
        assert "response" in session.hooks
        assert len(session.hooks["response"]) == 1
        adapter = session.get_adapter("http://example.com")
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == Retry().total
        assert session.get_adapter("https://example.com") is adapter
    finally:
        session.close()


def test_no_raise_for_status():
    session = build_requests_session(raise_for_status=False)
    try:
        # default Session has empty response hook list; no raise_for_status hook added
        assert session.hooks.get("response") == []
        adapter = session.get_adapter("http://example.com")
        assert isinstance(adapter, HTTPAdapter)
    finally:
        session.close()


def test_retry_int():
    session = build_requests_session(retry=3)
    try:
        adapter = session.get_adapter("https://example.com")
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == 3
    finally:
        session.close()


def test_retry_instance():
    retry = Retry(total=5, backoff_factor=1)
    session = build_requests_session(retry=retry)
    try:
        adapter = session.get_adapter("http://example.com")
        assert isinstance(adapter, HTTPAdapter)
        assert adapter.max_retries is retry
    finally:
        session.close()


def test_retry_false_disables_adapter():
    session = build_requests_session(retry=False)
    try:
        adapter = session.get_adapter("http://example.com")
        assert isinstance(adapter, HTTPAdapter)
        assert adapter.max_retries.total == 0
    finally:
        session.close()


def test_invalid_retry_raises_value_error():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance."):
        build_requests_session(retry="not-a-retry")
