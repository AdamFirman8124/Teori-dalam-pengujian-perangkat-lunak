# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

from types import SimpleNamespace

import pytest

import semantic_release.helpers as helpers


@pytest.fixture
def fake_requests(monkeypatch):
    sessions = []
    adapters = []

    class FakeSession:
        def __init__(self):
            self.hooks = {"response": []}
            self.mounts = {}
            self.closed = False
            sessions.append(self)

        def mount(self, prefix, adapter):
            self.mounts[prefix] = adapter

        def close(self):
            self.closed = True

    class FakeAdapter:
        def __init__(self, max_retries):
            self.max_retries = max_retries
            adapters.append(self)

    monkeypatch.setattr(helpers, "Session", FakeSession)
    monkeypatch.setattr(helpers, "HTTPAdapter", FakeAdapter)

    state = SimpleNamespace(
        Session=FakeSession,
        Adapter=FakeAdapter,
        sessions=sessions,
        adapters=adapters,
    )
    yield state

    for session in sessions:
        session.close()
    sessions.clear()
    adapters.clear()


def test_build_requests_session_uses_default_retry_and_status_hook(fake_requests):
    class Response:
        def __init__(self):
            self.raise_calls = 0

        def raise_for_status(self):
            self.raise_calls += 1
            return "checked"

    session = helpers.build_requests_session()
    response = Response()

    result = session.hooks["response"][0](response, object(), keyword=True)

    assert result == "checked"
    assert response.raise_calls == 1
    assert set(session.mounts) == {"http://", "https://"}
    assert session.mounts["http://"] is session.mounts["https://"]
    assert session.mounts["http://"] is fake_requests.adapters[0]
    assert isinstance(fake_requests.adapters[0].max_retries, helpers.Retry)


def test_build_requests_session_uses_integer_retry_count(fake_requests):
    session = helpers.build_requests_session(raise_for_status=False, retry=3)

    assert session.hooks == {"response": []}
    assert set(session.mounts) == {"http://", "https://"}
    assert session.mounts["http://"] is session.mounts["https://"]
    assert fake_requests.adapters[0].max_retries.total == 3


def test_build_requests_session_uses_supplied_retry_instance(fake_requests):
    retry = helpers.Retry(total=4)

    session = helpers.build_requests_session(retry=retry)

    assert session.mounts["http://"] is session.mounts["https://"]
    assert fake_requests.adapters[0].max_retries is retry


def test_build_requests_session_can_disable_retries_and_status_hook(fake_requests):
    session = helpers.build_requests_session(
        raise_for_status=False,
        retry=False,
    )

    assert session.hooks == {"response": []}
    assert session.mounts == {}
    assert fake_requests.adapters == []


def test_build_requests_session_rejects_invalid_retry_value(fake_requests):
    with pytest.raises(
        ValueError,
        match=r"retry should be a bool, int or Retry instance\.",
    ):
        helpers.build_requests_session(retry=object())

    assert len(fake_requests.sessions) == 1
    assert fake_requests.sessions[0].mounts == {}
    assert fake_requests.adapters == []
