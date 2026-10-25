# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

from unittest.mock import Mock

import pytest

import semantic_release.helpers as helpers


def test_build_requests_session_adds_status_hook_and_default_retry():
    session = helpers.build_requests_session()
    try:
        response = Mock()
        expected = object()
        response.raise_for_status.return_value = expected

        assert len(session.hooks["response"]) == 1
        assert session.hooks["response"][0](response, object(), unused=True) is expected
        response.raise_for_status.assert_called_once_with()

        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")
        assert http_adapter is https_adapter
        assert isinstance(http_adapter, helpers.HTTPAdapter)
        assert isinstance(http_adapter.max_retries, helpers.Retry)
    finally:
        session.close()


def test_build_requests_session_accepts_integer_retry_count():
    session = helpers.build_requests_session(raise_for_status=False, retry=3)
    try:
        adapter = session.get_adapter("https://example.com")

        assert session.hooks["response"] == []
        assert adapter is session.get_adapter("http://example.com")
        assert adapter.max_retries.total == 3
    finally:
        session.close()


def test_build_requests_session_uses_provided_retry_instance():
    retry = helpers.Retry(total=7)
    session = helpers.build_requests_session(retry=retry)
    try:
        adapter = session.get_adapter("https://example.com")

        assert adapter is session.get_adapter("http://example.com")
        assert adapter.max_retries is retry
    finally:
        session.close()


def test_build_requests_session_can_disable_retry_and_status_hook():
    session = helpers.build_requests_session(raise_for_status=False, retry=False)
    try:
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")

        assert session.hooks["response"] == []
        assert http_adapter is not https_adapter
        assert http_adapter.max_retries.total == 0
        assert https_adapter.max_retries.total == 0
    finally:
        session.close()


def test_build_requests_session_rejects_invalid_retry_and_cleans_up(monkeypatch):
    real_session_class = helpers.Session
    created_sessions = []

    def tracked_session():
        session = real_session_class()
        created_sessions.append(session)
        return session

    monkeypatch.setattr(helpers, "Session", tracked_session)

    try:
        with pytest.raises(
            ValueError, match=r"retry should be a bool, int or Retry instance\."
        ):
            helpers.build_requests_session(retry=object())

        assert len(created_sessions) == 1
    finally:
        for session in created_sessions:
            session.close()
