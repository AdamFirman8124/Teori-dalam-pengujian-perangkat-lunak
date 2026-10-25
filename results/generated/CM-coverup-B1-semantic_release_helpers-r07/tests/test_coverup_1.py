# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

from unittest.mock import Mock

import pytest

import semantic_release.helpers as helpers


def test_build_requests_session_with_default_retry_and_status_hook():
    session = helpers.build_requests_session()

    try:
        assert len(session.hooks["response"]) == 1

        response = Mock()
        response.raise_for_status.return_value = "checked"
        hook = session.hooks["response"][0]

        assert hook(response, "unused", keyword="unused") == "checked"
        response.raise_for_status.assert_called_once_with()

        http_adapter = session.adapters["http://"]
        assert session.adapters["https://"] is http_adapter
        assert isinstance(http_adapter, helpers.HTTPAdapter)
        assert isinstance(http_adapter.max_retries, helpers.Retry)
    finally:
        session.close()


def test_build_requests_session_with_integer_retry():
    session = helpers.build_requests_session(raise_for_status=False, retry=4)

    try:
        assert session.hooks["response"] == []

        http_adapter = session.adapters["http://"]
        assert session.adapters["https://"] is http_adapter
        assert http_adapter.max_retries.total == 4
    finally:
        session.close()


def test_build_requests_session_with_retry_instance():
    retry = helpers.Retry(total=3)
    session = helpers.build_requests_session(retry=retry)

    try:
        http_adapter = session.adapters["http://"]
        assert session.adapters["https://"] is http_adapter
        assert http_adapter.max_retries is retry
    finally:
        session.close()


def test_build_requests_session_without_retry_or_status_hook(monkeypatch):
    def unexpected_http_adapter(*args, **kwargs):
        pytest.fail("HTTPAdapter must not be created when retry is false")

    monkeypatch.setattr(helpers, "HTTPAdapter", unexpected_http_adapter)
    session = helpers.build_requests_session(
        raise_for_status=False,
        retry=False,
    )

    try:
        assert session.hooks["response"] == []
    finally:
        session.close()


def test_build_requests_session_rejects_invalid_retry(monkeypatch):
    created_sessions = []

    class FakeSession:
        def __init__(self):
            self.hooks = {}
            self.mounts = []
            created_sessions.append(self)

        def mount(self, prefix, adapter):
            self.mounts.append((prefix, adapter))

    monkeypatch.setattr(helpers, "Session", FakeSession)

    with pytest.raises(
        ValueError,
        match=r"^retry should be a bool, int or Retry instance\.$",
    ):
        helpers.build_requests_session(
            raise_for_status=False,
            retry=object(),
        )

    assert len(created_sessions) == 1
    assert created_sessions[0].hooks == {}
    assert created_sessions[0].mounts == []
