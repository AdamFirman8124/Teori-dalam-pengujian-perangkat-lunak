# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest
from unittest.mock import MagicMock

from ansible.utils.unsafe_proxy import UnsafeProxy, AnsibleUnsafe, AnsibleUnsafeText


DEPRECATION_MSG = (
    'UnsafeProxy is being deprecated. '
    'Use wrap_var or AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
)


@pytest.fixture
def mock_display(monkeypatch):
    """Patch ansible.utils.display.Display (imported inside UnsafeProxy.__new__)
    so no real Display/warning machinery is used; monkeypatch undoes it later."""
    display_cls = MagicMock(name='Display')
    monkeypatch.setattr('ansible.utils.display.Display', display_cls)
    return display_cls


def test_proxy_wraps_plain_string(mock_display):
    """Covers the string branch: isinstance check and AnsibleUnsafeText wrapping."""
    result = UnsafeProxy('some string')

    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, str)
    assert result == 'some string'

    # The deprecation warning machinery must have been exercised exactly once
    mock_display.assert_called_once()
    mock_display.return_value.deprecated.assert_called_once_with(
        DEPRECATION_MSG,
        version='2.13',
        collection_name='ansible.builtin',
    )


def test_proxy_passthrough_already_unsafe(mock_display):
    """Covers the early return for objects that are already AnsibleUnsafe."""
    already_unsafe = AnsibleUnsafeText('already unsafe')

    result = UnsafeProxy(already_unsafe)

    # Must be returned as-is, not re-wrapped or copied
    assert result is already_unsafe
    assert isinstance(result, AnsibleUnsafe)

    mock_display.return_value.deprecated.assert_called_once_with(
        DEPRECATION_MSG,
        version='2.13',
        collection_name='ansible.builtin',
    )


def test_proxy_passthrough_non_string_object(mock_display):
    """Covers the final return for objects that are neither unsafe nor strings."""
    obj = {'key': 'value'}

    result = UnsafeProxy(obj)

    # Returned unchanged, without being wrapped
    assert result is obj
    assert not isinstance(result, AnsibleUnsafe)
    mock_display.return_value.deprecated.assert_called_once()


def test_proxy_passthrough_bytes(mock_display):
    """Bytes are not in string_types on py3, so they hit the final return too."""
    obj = b'some bytes'

    result = UnsafeProxy(obj)

    assert result is obj
    assert not isinstance(result, AnsibleUnsafe)
    mock_display.return_value.deprecated.assert_called_once()
