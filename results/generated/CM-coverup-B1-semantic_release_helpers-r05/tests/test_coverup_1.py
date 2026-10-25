# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

import pytest
from unittest.mock import Mock
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from semantic_release.helpers import build_requests_session


def test_build_requests_session_defaults():
    session = build_requests_session()
    try:
        assert isinstance(session, Session)
        # raise_for_status hook installed
        assert "response" in session.hooks
        assert len(session.hooks["response"]) == 1
        mock_resp = Mock()
        session.hooks["response"][0](mock_resp)
        mock_resp.raise_for_status.assert_called_once_with()
        # default retry=True -> Retry()
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert isinstance(http_adapter, HTTPAdapter)
        assert isinstance(https_adapter, HTTPAdapter)
        assert isinstance(http_adapter.max_retries, Retry)
        assert isinstance(https_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == Retry().total
        assert https_adapter.max_retries.total == Retry().total
    finally:
        session.close()


def test_build_requests_session_no_raise_no_retry():
    session = build_requests_session(raise_for_status=False, retry=False)
    try:
        assert isinstance(session, Session)
        assert session.hooks == {"response": []}
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert isinstance(http_adapter, HTTPAdapter)
        assert isinstance(https_adapter, HTTPAdapter)
    finally:
        session.close()


def test_build_requests_session_raise_without_retry():
    session = build_requests_session(raise_for_status=True, retry=False)
    try:
        assert len(session.hooks["response"]) == 1
        mock_resp = Mock()
        session.hooks["response"][0](mock_resp)
        mock_resp.raise_for_status.assert_called_once_with()
    finally:
        session.close()


def test_build_requests_session_int_retry():
    session = build_requests_session(raise_for_status=False, retry=3)
    try:
        assert session.hooks == {"response": []}
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == 3
        assert https_adapter.max_retries.total == 3
        assert http_adapter is https_adapter
    finally:
        session.close()


def test_build_requests_session_retry_instance():
    retry_obj = Retry(total=5, backoff_factor=0.1)
    session = build_requests_session(retry=retry_obj)
    try:
        assert len(session.hooks["response"]) == 1
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == 5
        assert http_adapter.max_retries.backoff_factor == 0.1
        assert https_adapter.max_retries.total == 5
    finally:
        session.close()


def test_build_requests_session_invalid_retry_raises():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance"):
        build_requests_session(retry="invalid-truthy-string")


def test_build_requests_session_falsy_retries_do_not_mount():
    for falsy in (None, False, 0):
        session = build_requests_session(raise_for_status=False, retry=falsy)
        try:
            assert isinstance(session, Session)
            assert session.hooks == {"response": []}
            adapter = session.get_adapter("http://example.com")
            assert isinstance(adapter, HTTPAdapter)
        finally:
            session.close()
