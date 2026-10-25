# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

import pytest
from unittest import mock

from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from semantic_release.helpers import build_requests_session


def test_build_requests_session_defaults():
    session = build_requests_session()
    try:
        assert isinstance(session, Session)
        # raise_for_status=True branch: hook installed
        assert "response" in session.hooks
        assert len(session.hooks["response"]) == 1
        assert callable(session.hooks["response"][0])
        # retry=True (bool) branch: default Retry adapter mounted
        for scheme in ("http://", "https://"):
            adapter = session.adapters[scheme]
            assert isinstance(adapter, HTTPAdapter)
            assert isinstance(adapter.max_retries, Retry)
            assert adapter.max_retries.total == Retry().total
    finally:
        session.close()


def test_build_requests_session_hook_calls_raise_for_status():
    session = build_requests_session(raise_for_status=True, retry=False)
    try:
        hook = session.hooks["response"][0]
        response = mock.Mock()
        hook(response)
        response.raise_for_status.assert_called_once_with()
        # Hook accepts *args/**kwargs as requests passes them
        response.reset_mock()
        hook(response, stream=True, timeout=1)
        response.raise_for_status.assert_called_once_with()
    finally:
        session.close()


def test_build_requests_session_no_raise_for_status_and_no_retry():
    session = build_requests_session(raise_for_status=False, retry=False)
    try:
        assert isinstance(session, Session)
        # Default empty response hooks, no custom hook installed
        assert session.hooks["response"] == []
        # retry falsy: default adapters unchanged (max_retries total 0)
        for scheme in ("http://", "https://"):
            adapter = session.adapters[scheme]
            assert isinstance(adapter, HTTPAdapter)
            assert adapter.max_retries.total == 0
    finally:
        session.close()


@pytest.mark.parametrize("falsy_retry", [False, 0, None])
def test_build_requests_session_falsy_retry(falsy_retry):
    session = build_requests_session(raise_for_status=False, retry=falsy_retry)
    try:
        assert isinstance(session, Session)
        assert session.hooks["response"] == []
        assert session.adapters["http://"].max_retries.total == 0
        assert session.adapters["https://"].max_retries.total == 0
    finally:
        session.close()


def test_build_requests_session_retry_bool_true():
    session = build_requests_session(raise_for_status=False, retry=True)
    try:
        for scheme in ("http://", "https://"):
            adapter = session.adapters[scheme]
            assert isinstance(adapter, HTTPAdapter)
            assert isinstance(adapter.max_retries, Retry)
            assert adapter.max_retries.total == Retry().total
        # Same adapter instance mounted for both schemes
        assert session.adapters["http://"] is session.adapters["https://"]
    finally:
        session.close()


@pytest.mark.parametrize("count", [1, 3, 5])
def test_build_requests_session_retry_int(count):
    session = build_requests_session(raise_for_status=False, retry=count)
    try:
        for scheme in ("http://", "https://"):
            adapter = session.adapters[scheme]
            assert isinstance(adapter, HTTPAdapter)
            assert isinstance(adapter.max_retries, Retry)
            assert adapter.max_retries.total == count
    finally:
        session.close()


def test_build_requests_session_retry_instance():
    custom = Retry(total=7, backoff_factor=0.5)
    session = build_requests_session(raise_for_status=True, retry=custom)
    try:
        assert len(session.hooks["response"]) == 1
        for scheme in ("http://", "https://"):
            adapter = session.adapters[scheme]
            assert isinstance(adapter, HTTPAdapter)
            # Retry instance is used as-is
            assert adapter.max_retries is custom
            assert adapter.max_retries.total == 7
    finally:
        session.close()


@pytest.mark.parametrize("bad_retry", ["3", 1.5, object(), ["retry"], {"total": 3}])
def test_build_requests_session_retry_invalid_raises(bad_retry):
    with pytest.raises(
        ValueError, match=r"retry should be a bool, int or Retry instance\."
    ):
        build_requests_session(raise_for_status=True, retry=bad_retry)
