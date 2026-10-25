# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from semantic_release import helpers


@pytest.fixture
def request_construction(monkeypatch):
    sessions = []
    adapters = []

    class FakeSession:
        def __init__(self):
            self.hooks = {"response": []}
            self.mounts = []
            sessions.append(self)

        def mount(self, prefix, adapter):
            self.mounts.append((prefix, adapter))

    def make_adapter(*, max_retries):
        adapter = SimpleNamespace(max_retries=max_retries)
        adapters.append(adapter)
        return adapter

    monkeypatch.setattr(helpers, "Session", FakeSession)
    monkeypatch.setattr(helpers, "HTTPAdapter", make_adapter)
    return SimpleNamespace(sessions=sessions, adapters=adapters)


def test_build_requests_session_with_default_options(request_construction):
    session = helpers.build_requests_session()

    assert session is request_construction.sessions[0]
    assert len(request_construction.adapters) == 1

    adapter = request_construction.adapters[0]
    assert isinstance(adapter.max_retries, helpers.Retry)
    assert session.mounts == [
        ("http://", adapter),
        ("https://", adapter),
    ]

    response = Mock()
    expected_result = object()
    response.raise_for_status.return_value = expected_result

    result = session.hooks["response"][0](
        response, "ignored argument", ignored_keyword=True
    )

    assert result is expected_result
    response.raise_for_status.assert_called_once_with()


def test_build_requests_session_with_integer_retry_count(request_construction):
    session = helpers.build_requests_session(retry=3)

    adapter = request_construction.adapters[0]
    assert isinstance(adapter.max_retries, helpers.Retry)
    assert adapter.max_retries.total == 3
    assert session.mounts == [
        ("http://", adapter),
        ("https://", adapter),
    ]


def test_build_requests_session_with_retry_instance(request_construction):
    retry = helpers.Retry(total=7)

    session = helpers.build_requests_session(retry=retry)

    adapter = request_construction.adapters[0]
    assert adapter.max_retries is retry
    assert session.mounts == [
        ("http://", adapter),
        ("https://", adapter),
    ]


def test_build_requests_session_without_status_hook_or_retries(
    request_construction,
):
    session = helpers.build_requests_session(
        raise_for_status=False,
        retry=False,
    )

    assert session.hooks == {"response": []}
    assert session.mounts == []
    assert request_construction.adapters == []


def test_build_requests_session_rejects_invalid_retry_value(
    request_construction,
):
    with pytest.raises(
        ValueError,
        match=r"^retry should be a bool, int or Retry instance\.$",
    ):
        helpers.build_requests_session(retry="invalid")

    assert len(request_construction.sessions) == 1
    assert request_construction.sessions[0].mounts == []
    assert request_construction.adapters == []
