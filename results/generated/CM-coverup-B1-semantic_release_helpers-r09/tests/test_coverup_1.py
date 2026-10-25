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
        assert "response" in session.hooks
        assert len(session.hooks["response"]) == 1
        assert callable(session.hooks["response"][0])
        http_adapter = session.adapters["http://"]
        https_adapter = session.adapters["https://"]
        assert isinstance(http_adapter, HTTPAdapter)
        assert http_adapter is https_adapter
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == Retry().total
    finally:
        session.close()


def test_build_requests_session_no_raise_no_retry():
    session = build_requests_session(raise_for_status=False, retry=False)
    try:
        assert isinstance(session, Session)
        assert session.hooks["response"] == []
        http_adapter = session.adapters["http://"]
        https_adapter = session.adapters["https://"]
        assert isinstance(http_adapter, HTTPAdapter)
        assert isinstance(https_adapter, HTTPAdapter)
        # default adapters from Session.__init__ have total 0, not default Retry total
        assert http_adapter.max_retries.total == 0
        assert https_adapter.max_retries.total == 0
    finally:
        session.close()


def test_build_requests_session_retry_int():
    session = build_requests_session(raise_for_status=False, retry=3)
    try:
        assert session.hooks["response"] == []
        http_adapter = session.adapters["http://"]
        https_adapter = session.adapters["https://"]
        assert isinstance(http_adapter, HTTPAdapter)
        assert http_adapter is https_adapter
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == 3
    finally:
        session.close()


def test_build_requests_session_retry_instance():
    custom = Retry(total=7, connect=7)
    session = build_requests_session(raise_for_status=False, retry=custom)
    try:
        assert session.hooks["response"] == []
        http_adapter = session.adapters["http://"]
        https_adapter = session.adapters["https://"]
        assert isinstance(http_adapter, HTTPAdapter)
        assert http_adapter is https_adapter
        assert http_adapter.max_retries is custom
        assert https_adapter.max_retries is custom
    finally:
        session.close()


def test_build_requests_session_retry_bool_true():
    session = build_requests_session(raise_for_status=False, retry=True)
    try:
        assert session.hooks["response"] == []
        http_adapter = session.adapters["http://"]
        https_adapter = session.adapters["https://"]
        assert isinstance(http_adapter, HTTPAdapter)
        assert http_adapter is https_adapter
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == Retry().total
    finally:
        session.close()


def test_build_requests_session_invalid_retry_raises():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance"):
        build_requests_session(retry="bad-string")
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance"):
        build_requests_session(retry=2.5)
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance"):
        build_requests_session(retry=object())


def test_build_requests_session_raise_for_status_hook():
    session = build_requests_session(raise_for_status=True, retry=False)
    try:
        assert len(session.hooks["response"]) == 1
        hook = session.hooks["response"][0]
        mock_resp = Mock()
        hook(mock_resp)
        mock_resp.raise_for_status.assert_called_once_with()
        failing = Mock()
        failing.raise_for_status.side_effect = RuntimeError("bad status")
        with pytest.raises(RuntimeError, match="bad status"):
            hook(failing)
        mock_resp2 = Mock()
        hook(mock_resp2, "extra", key="value")
        mock_resp2.raise_for_status.assert_called_once_with()
    finally:
        session.close()
