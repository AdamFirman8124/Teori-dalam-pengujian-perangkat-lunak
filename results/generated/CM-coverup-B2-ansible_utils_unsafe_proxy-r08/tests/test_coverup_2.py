# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

from __future__ import absolute_import, division, print_function

from unittest.mock import MagicMock

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    NativeJinjaUnsafeText,
    UnsafeProxy,
)

DEPRECATION_MSG = (
    'UnsafeProxy is being deprecated. '
    'Use wrap_var or AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'
)


@pytest.fixture
def mock_display(monkeypatch):
    """Replace ansible.utils.display.Display with a MagicMock.

    UnsafeProxy.__new__ does ``from ansible.utils.display import Display``
    at call time, so patching the module attribute intercepts it. This both
    suppresses real deprecation output and lets us assert the call, and
    monkeypatch restores the original class afterwards.
    """
    display_cls = MagicMock(name='Display')
    monkeypatch.setattr('ansible.utils.display.Display', display_cls)
    return display_cls.return_value


def assert_deprecated(mock_display):
    """Assert UnsafeProxy emitted its deprecation warning exactly once."""
    mock_display.deprecated.assert_called_once_with(
        DEPRECATION_MSG,
        version='2.13',
        collection_name='ansible.builtin',
    )


def test_proxy_emits_deprecation_warning(mock_display):
    result = UnsafeProxy('abc')

    assert_deprecated(mock_display)
    assert isinstance(result, AnsibleUnsafeText)
    assert result == 'abc'


def test_proxy_wraps_text_string(mock_display):
    result = UnsafeProxy('some string')

    assert_deprecated(mock_display)
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True
    assert result == 'some string'
    # encode() must preserve the unsafe context
    assert isinstance(result.encode(), AnsibleUnsafeBytes)
    assert result.encode() == b'some string'


def test_proxy_wraps_unicode_string(mock_display):
    result = UnsafeProxy(u'caf\u00e9')

    assert_deprecated(mock_display)
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u'caf\u00e9'


def test_proxy_returns_already_unsafe_text_unchanged(mock_display):
    unsafe = AnsibleUnsafeText('already unsafe')

    result = UnsafeProxy(unsafe)

    assert_deprecated(mock_display)
    assert result is unsafe
    assert isinstance(result, AnsibleUnsafeText)


def test_proxy_returns_already_unsafe_bytes_unchanged(mock_display):
    unsafe = AnsibleUnsafeBytes(b'unsafe bytes')

    result = UnsafeProxy(unsafe)

    assert_deprecated(mock_display)
    assert result is unsafe
    assert isinstance(result, AnsibleUnsafeBytes)


def test_proxy_returns_native_jinja_unsafe_text_unchanged(mock_display):
    unsafe = NativeJinjaUnsafeText('native jinja unsafe')

    result = UnsafeProxy(unsafe)

    assert_deprecated(mock_display)
    assert result is unsafe
    assert isinstance(result, NativeJinjaUnsafeText)


@pytest.mark.parametrize('obj', [
    None,
    123,
    1.5,
    [1, 'two'],
    {'key': 'value'},
    ('t', 'u', 'p', 'l', 'e'),
    b'raw bytes',
])
def test_proxy_passes_non_string_objects_through_unchanged(mock_display, obj):
    result = UnsafeProxy(obj)

    assert_deprecated(mock_display)
    assert result is obj
    assert not isinstance(result, AnsibleUnsafe)
