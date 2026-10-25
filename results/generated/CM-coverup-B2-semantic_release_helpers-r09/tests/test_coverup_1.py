# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

from unittest.mock import Mock

import pytest
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import semantic_release.helpers as helpers


def test_build_requests_session_configures_default_retry_and_status_hook():
    session = helpers.build_requests_session()

    try:
        response = Mock()
        response.raise_for_status.return_value = object()

        hooks = session.hooks["response"]
        assert len(hooks) == 1
        assert hooks[0](response, unused=True) is response.raise_for_status.return_value
        response.raise_for_status.assert_called_once_with()

        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")

        assert isinstance(http_adapter, HTTPAdapter)
        assert https_adapter is http_adapter
        assert isinstance(http_adapter.max_retries, Retry)
        assert http_adapter.max_retries.total == Retry().total
    finally:
        session.close()


def test_build_requests_session_accepts_integer_retry_count():
    session = helpers.build_requests_session(raise_for_status=False, retry=3)

    try:
        adapter = session.get_adapter("https://example.com")

        assert session.hooks["response"] == []
        assert session.get_adapter("http://example.com") is adapter
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == 3
    finally:
        session.close()


def test_build_requests_session_uses_supplied_retry_instance():
    retry = Retry(total=4)
    session = helpers.build_requests_session(retry=retry)

    try:
        http_adapter = session.get_adapter("http://example.com")
        https_adapter = session.get_adapter("https://example.com")

        assert http_adapter is https_adapter
        assert http_adapter.max_retries is retry
    finally:
        session.close()


def test_build_requests_session_can_disable_retries_and_status_hook(monkeypatch):
    session = helpers.Session()
    mount = Mock(wraps=session.mount)
    monkeypatch.setattr(session, "mount", mount)
    monkeypatch.setattr(helpers, "Session", lambda: session)

    try:
        result = helpers.build_requests_session(
            raise_for_status=False,
            retry=False,
        )

        assert result is session
        assert result.hooks["response"] == []
        mount.assert_not_called()
    finally:
        session.close()


def test_build_requests_session_rejects_invalid_retry_value(monkeypatch):
    session = helpers.Session()
    mount = Mock(wraps=session.mount)
    monkeypatch.setattr(session, "mount", mount)
    monkeypatch.setattr(helpers, "Session", lambda: session)

    try:
        with pytest.raises(
            ValueError,
            match=r"^retry should be a bool, int or Retry instance\.$",
        ):
            helpers.build_requests_session(retry="invalid")

        mount.assert_not_called()
    finally:
        session.close()
