# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

import pytest
from unittest.mock import Mock
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from requests.packages.urllib3.util.retry import Retry

from semantic_release.helpers import build_requests_session


@pytest.fixture
def make_session():
    """Build sessions and guarantee they are closed afterwards."""
    created = []

    def _make(*args, **kwargs):
        session = build_requests_session(*args, **kwargs)
        created.append(session)
        return session

    yield _make

    for session in created:
        session.close()


def test_default_session_has_raise_for_status_hook_and_retries(make_session):
    session = make_session()

    assert isinstance(session, Session)
    assert len(session.hooks["response"]) == 1

    for prefix in ("http://", "https://"):
        adapter = session.get_adapter(prefix)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == Retry().total


def test_raise_for_status_hook_calls_response_raise_for_status(make_session):
    session = make_session()
    hook = session.hooks["response"][0]

    response = Mock()
    hook(response, "extra", keyword="value")

    response.raise_for_status.assert_called_once_with()


def test_raise_for_status_hook_propagates_http_error(make_session):
    session = make_session()
    hook = session.hooks["response"][0]

    response = Mock()
    response.raise_for_status.side_effect = HTTPError("boom")

    with pytest.raises(HTTPError):
        hook(response)


def test_raise_for_status_false_installs_no_hook(make_session):
    session = make_session(raise_for_status=False)

    assert session.hooks["response"] == []


def test_retry_false_mounts_no_custom_adapter(make_session):
    session = make_session(retry=False)

    for prefix in ("http://", "https://"):
        adapter = session.get_adapter(prefix)
        assert adapter.max_retries.total == 0


def test_retry_zero_is_falsy_and_mounts_no_custom_adapter(make_session):
    session = make_session(retry=0)

    for prefix in ("http://", "https://"):
        assert session.get_adapter(prefix).max_retries.total == 0


def test_retry_true_uses_default_retry_config(make_session):
    session = make_session(retry=True)

    for prefix in ("http://", "https://"):
        adapter = session.get_adapter(prefix)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == Retry().total


def test_retry_int_sets_total_retry_count(make_session):
    session = make_session(retry=3)

    for prefix in ("http://", "https://"):
        adapter = session.get_adapter(prefix)
        assert isinstance(adapter, HTTPAdapter)
        assert adapter.max_retries.total == 3


def test_retry_instance_is_used_as_is(make_session):
    retry = Retry(total=7, backoff_factor=0.5)
    session = make_session(retry=retry)

    for prefix in ("http://", "https://"):
        adapter = session.get_adapter(prefix)
        assert adapter.max_retries is retry
        assert adapter.max_retries.total == 7


def test_invalid_retry_type_raises_value_error(make_session):
    with pytest.raises(ValueError, match="retry should be a bool, int or Retry instance."):
        make_session(retry="not-a-retry")
