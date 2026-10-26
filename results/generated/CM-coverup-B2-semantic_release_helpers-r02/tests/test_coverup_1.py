# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

import pytest
from requests.packages.urllib3.util.retry import Retry

import semantic_release.helpers as helpers


@pytest.fixture
def tracked_sessions(monkeypatch):
    sessions = []
    real_session = helpers.Session

    def create_session():
        session = real_session()
        sessions.append(session)
        return session

    monkeypatch.setattr(helpers, "Session", create_session)
    yield sessions

    for session in sessions:
        session.close()


def test_build_requests_session_with_default_options(tracked_sessions):
    session = helpers.build_requests_session()

    assert session is tracked_sessions[0]
    assert len(session.hooks["response"]) == 1

    class Response:
        def __init__(self):
            self.called = False

        def raise_for_status(self):
            self.called = True
            return "checked"

    response = Response()
    assert session.hooks["response"][0](response, "unused", ignored=True) == "checked"
    assert response.called is True

    http_adapter = session.get_adapter("http://")
    https_adapter = session.get_adapter("https://")
    assert http_adapter is https_adapter
    assert isinstance(http_adapter.max_retries, Retry)


def test_build_requests_session_with_integer_retry(tracked_sessions):
    session = helpers.build_requests_session(raise_for_status=False, retry=3)

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 3
    assert session.get_adapter("https://").max_retries.total == 3


def test_build_requests_session_with_retry_instance(tracked_sessions):
    retry = Retry(total=7)
    session = helpers.build_requests_session(retry=retry)

    assert session.get_adapter("http://").max_retries is retry
    assert session.get_adapter("https://").max_retries is retry


def test_build_requests_session_without_retries_or_status_hook(tracked_sessions):
    session = helpers.build_requests_session(
        raise_for_status=False,
        retry=False,
    )

    assert session.hooks["response"] == []
    assert session.get_adapter("http://").max_retries.total == 0
    assert session.get_adapter("https://").max_retries.total == 0


def test_build_requests_session_rejects_invalid_retry(tracked_sessions):
    invalid_retry = object()

    with pytest.raises(
        ValueError,
        match=r"^retry should be a bool, int or Retry instance\.$",
    ):
        helpers.build_requests_session(retry=invalid_retry)

    assert len(tracked_sessions) == 1
