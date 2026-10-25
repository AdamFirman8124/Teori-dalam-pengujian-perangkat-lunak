# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.utils.unsafe_proxy import UnsafeProxy, AnsibleUnsafe, AnsibleUnsafeText
from ansible.module_utils.six import PY2, text_type, binary_type


@pytest.fixture
def mock_display(monkeypatch):
    """Patch Display so the deprecation warning is captured, not emitted."""
    calls = []

    class FakeDisplay(object):
        def deprecated(self, msg, version=None, collection_name=None):
            calls.append({'msg': msg, 'version': version,
                          'collection_name': collection_name})

    import ansible.utils.display
    monkeypatch.setattr(ansible.utils.display, 'Display', FakeDisplay)
    return calls


def test_proxy_deprecation_warning_and_string_wrap(mock_display):
    obj = UnsafeProxy(u'some string')

    assert len(mock_display) == 1
    assert mock_display[0]['msg'] == (
        'UnsafeProxy is being deprecated. Use wrap_var or '
        'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead')
    assert mock_display[0]['version'] == '2.13'
    assert mock_display[0]['collection_name'] == 'ansible.builtin'
    assert isinstance(obj, AnsibleUnsafeText)
    assert isinstance(obj, AnsibleUnsafe)
    assert isinstance(obj, text_type)
    assert obj == u'some string'


def test_proxy_passthrough_already_unsafe(mock_display):
    pre = AnsibleUnsafeText(u'already unsafe')

    obj = UnsafeProxy(pre)

    assert len(mock_display) == 1
    assert obj is pre


def test_proxy_non_string_passthrough(mock_display):
    sentinel = {'a': 1}

    obj = UnsafeProxy(sentinel)

    assert obj is sentinel
    assert not isinstance(obj, AnsibleUnsafe)
    assert len(mock_display) == 1


def test_proxy_bytes_converted_to_text(mock_display):
    raw = b'byte string'

    obj = UnsafeProxy(raw)

    assert len(mock_display) == 1
    if PY2:
        # On PY2 bytes (str) are in string_types, so they are wrapped.
        assert isinstance(obj, AnsibleUnsafeText)
        assert isinstance(obj, text_type)
        assert obj == u'byte string'
    else:
        # On PY3 string_types is (str,), so bytes are not wrapped
        # and are returned unchanged via line 102.
        assert obj is raw
        assert isinstance(obj, binary_type)
        assert not isinstance(obj, AnsibleUnsafeText)
        assert obj == b'byte string'
