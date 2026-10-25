# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.module_utils.six import text_type
from ansible.utils.unsafe_proxy import UnsafeProxy, AnsibleUnsafe, AnsibleUnsafeText


@pytest.fixture
def mock_display(monkeypatch):
    """Patch Display so deprecation warnings are captured, not printed."""
    calls = []

    class FakeDisplay(object):
        def deprecated(self, *args, **kwargs):
            calls.append((args, kwargs))

    import ansible.utils.display
    monkeypatch.setattr(ansible.utils.display, 'Display', FakeDisplay)
    return calls


def test_proxy_deprecation_and_string_wrap(mock_display):
    """Lines 88-91, 100-102: string input is wrapped and deprecation fires."""
    result = UnsafeProxy(u'hello')

    # deprecation was issued exactly once with expected message
    assert len(mock_display) == 1
    args, kwargs = mock_display[0]
    assert 'UnsafeProxy is being deprecated' in args[0]
    assert kwargs.get('version') == '2.13'
    assert kwargs.get('collection_name') == 'ansible.builtin'

    # postcondition: result is an unsafe text wrapping the original value
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, text_type)
    assert result == u'hello'
    assert result.__UNSAFE__ is True


def test_proxy_passthrough_already_unsafe(mock_display):
    """Lines 97-98: an already-unsafe object is returned as-is, not rewrapped."""
    already = AnsibleUnsafeText(u'unsafe')
    result = UnsafeProxy(already)

    assert result is already
    assert isinstance(result, AnsibleUnsafeText)
    # deprecation still fired (lines 88-91) but no rewrap happened
    assert len(mock_display) == 1


def test_proxy_non_string_passthrough(mock_display):
    """Line 100-102: non-string input is returned unchanged (no wrap)."""
    obj = {'key': 'value'}
    result = UnsafeProxy(obj)

    assert result is obj
    assert not isinstance(result, AnsibleUnsafe)
    assert len(mock_display) == 1
