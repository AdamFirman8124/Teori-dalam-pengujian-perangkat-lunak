# file: project/semantic_release/helpers.py:16-39
# asked: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}
# gained: {"lines": [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "branches": [[27, 28], [27, 29], [29, 30], [29, 39], [30, 31], [30, 32], [32, 33], [32, 34], [34, 35], [34, 36]]}

"""Tests for semantic_release.helpers.build_requests_session (lines 26-39)."""

import pytest
import requests
from requests import Session
from requests.adapters import HTTPAdapter
from requests.models import Response
from requests.packages.urllib3.util.retry import Retry

from semantic_release.helpers import build_requests_session


@pytest.fixture
def keep_sessions():
    """Collect sessions created during a test and close them afterwards."""
    created = []

    def register(session):
        created.append(session)
        return session

    yield register

    for session in created:
        session.close()


def test_build_requests_session_defaults(keep_sessions):
    """Default call: raise_for_status hook installed, default Retry mounted."""
    session = keep_sessions(build_requests_session())

    assert isinstance(session, Session)
    # raise_for_status hook installed by default
    hooks = session.hooks.get("response", [])
    assert len(hooks) == 1

    # a default Retry configuration is mounted for both schemes
    for url in ("http://example.com", "https://example.com"):
        adapter = session.get_adapter(url)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == Retry().total


def test_build_requests_session_hook_raises_on_error_status(keep_sessions):
    """The installed hook calls raise_for_status and accepts extra args."""
    session = keep_sessions(build_requests_session())
    hook = session.hooks["response"][0]

    bad = Response()
    bad.status_code = 500
    with pytest.raises(requests.HTTPError):
        hook(bad, timeout=5, stream=True)  # *args/**kwargs must be accepted

    ok = Response()
    ok.status_code = 200
    assert hook(ok) is None


def test_build_requests_session_without_raise_for_status(keep_sessions):
    """raise_for_status=False: no hook installed, retry still configured."""
    session = keep_sessions(build_requests_session(raise_for_status=False))

    assert isinstance(session, Session)
    assert session.hooks.get("response", []) == []

    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    assert isinstance(adapter.max_retries, Retry)


def test_build_requests_session_retry_true(keep_sessions):
    """retry=True uses the default Retry configuration."""
    session = keep_sessions(build_requests_session(retry=True))

    for url in ("http://example.com", "https://example.com"):
        adapter = session.get_adapter(url)
        assert isinstance(adapter, HTTPAdapter)
        assert isinstance(adapter.max_retries, Retry)
        assert adapter.max_retries.total == Retry().total


def test_build_requests_session_retry_int(keep_sessions):
    """retry=<int> uses that value as the total retry count."""
    session = keep_sessions(build_requests_session(retry=3))

    for url in ("http://example.com", "https://example.com"):
        adapter = session.get_adapter(url)
        assert isinstance(adapter, HTTPAdapter)
        assert adapter.max_retries.total == 3


def test_build_requests_session_retry_instance(keep_sessions):
    """A Retry instance is passed through to the mounted adapter unchanged."""
    retry = Retry(total=7, backoff_factor=0.5)
    session = keep_sessions(build_requests_session(retry=retry))

    for url in ("http://example.com", "https://example.com"):
        adapter = session.get_adapter(url)
        assert isinstance(adapter, HTTPAdapter)
        assert adapter.max_retries is retry


def test_build_requests_session_retry_false(keep_sessions):
    """retry=False: no custom adapter mounted (requests defaults kept)."""
    session = keep_sessions(build_requests_session(retry=False))

    assert isinstance(session, Session)
    adapter = session.get_adapter("https://example.com")
    assert isinstance(adapter, HTTPAdapter)
    # requests' default adapter performs no retries
    assert adapter.max_retries.total == 0


def test_build_requests_session_invalid_retry_type():
    """Any other type for `retry` is rejected with a ValueError."""
    with pytest.raises(
        ValueError, match=r"^retry should be a bool, int or Retry instance\.$"
    ):
        build_requests_session(retry="not-a-retry")
