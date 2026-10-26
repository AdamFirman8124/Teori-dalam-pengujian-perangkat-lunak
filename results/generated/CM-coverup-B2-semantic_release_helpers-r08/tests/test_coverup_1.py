# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

import pytest
from unittest.mock import Mock
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import HTTPError

from semantic_release.helpers import build_requests_session


def test_defaults_uses_raise_hook_and_default_retry():
    session = build_requests_session()
    try:
        assert isinstance(session, Session)
        # raise_for_status hook installed
        assert "response" in session.hooks
        assert len(session.hooks["response"]) == 1
        assert callable(session.hooks["response"][0])
        # default Retry mounted for both schemes
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert isinstance(http_adapter, HTTPAdapter)
        assert isinstance(https_adapter, HTTPAdapter)
        assert http_adapter is https_adapter
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == Retry().total
    finally:
        session.close()


def test_no_raise_no_retry():
    session = build_requests_session(raise_for_status=False, retry=False)
    try:
        assert isinstance(session, Session)
        assert session.hooks["response"] == []
        # no custom retry: default adapter retries remain untouched (total == 0)
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert isinstance(http_adapter, HTTPAdapter)
        assert isinstance(https_adapter, HTTPAdapter)
        assert http_adapter.max_retries.total == 0
        assert https_adapter.max_retries.total == 0
    finally:
        session.close()


def test_int_retry_uses_total():
    session = build_requests_session(raise_for_status=False, retry=3)
    try:
        assert session.hooks["response"] == []
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == 3
        assert https_adapter.max_retries.total == 3
        assert session.adapters["http://"] is session.adapters["https://"]
    finally:
        session.close()


def test_retry_instance_is_used_directly():
    custom = Retry(total=7, connect=7, read=7)
    session = build_requests_session(raise_for_status=True, retry=custom)
    try:
        assert len(session.hooks["response"]) == 1
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert http_adapter.max_retries is custom
        assert https_adapter.max_retries is custom
        assert http_adapter.max_retries.total == 7
    finally:
        session.close()


def test_invalid_retry_raises_value_error():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance"):
        build_requests_session(retry="invalid-string")


def test_invalid_float_retry_raises_value_error():
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance"):
        build_requests_session(retry=2.5)


def test_response_hook_calls_raise_for_status():
    session = build_requests_session(raise_for_status=True, retry=False)
    try:
        hook = session.hooks["response"][0]
        mock_resp = Mock()
        hook(mock_resp)
        mock_resp.raise_for_status.assert_called_once_with()
        # hook propagates HTTP errors
        err_resp = Mock()
        err_resp.raise_for_status.side_effect = HTTPError("boom")
        with pytest.raises(HTTPError):
            hook(err_resp)
    finally:
        session.close()


def test_falsy_retry_skips_mount():
    session = build_requests_session(raise_for_status=True, retry=0)
    try:
        assert len(session.hooks["response"]) == 1
        assert session.get_adapter("http://example.com").max_retries.total == 0
        assert session.get_adapter("https://example.com").max_retries.total == 0
    finally:
        session.close()
