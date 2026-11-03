# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

"""Coverage tests for the ``_wrap_dict`` helper in ``ansible/utils/unsafe_proxy.py``.

Line 106 (``return dict((wrap_var(k), wrap_var(item)) for k, item in v.items())``)
is exercised both directly (by calling ``_wrap_dict``) and indirectly (via
``wrap_var`` when handed a ``Mapping``).  The functions under test are pure --
they neither read nor write module-level/global state and touch no files --
so no monkeypatching or explicit teardown is needed to avoid state pollution;
nothing is mutated by these tests (which is also asserted below).
"""

from ansible.module_utils.common._collections_compat import Mapping
from ansible.utils.native_jinja import NativeJinjaText
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    NativeJinjaUnsafeText,
    _wrap_dict,
    wrap_var,
)


class _MyMapping(Mapping):
    """Minimal Mapping implementation to hit wrap_var's Mapping branch."""

    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)


def test_wrap_dict_direct_call_executes_line_106():
    """Calling _wrap_dict directly guarantees line 106 is executed."""
    original = {'key': 'value'}
    result = _wrap_dict(original)

    # A *new* dict is returned...
    assert isinstance(result, dict)
    assert result is not original
    # ...whose key and value were run through wrap_var().
    (wrapped_key, wrapped_value), = result.items()
    assert isinstance(wrapped_key, AnsibleUnsafeText)
    assert isinstance(wrapped_key, AnsibleUnsafe)
    assert isinstance(wrapped_value, AnsibleUnsafeText)
    assert isinstance(wrapped_value, AnsibleUnsafe)
    # Equality with the plain strings is preserved.
    assert wrapped_key == 'key'
    assert wrapped_value == 'value'
    # The input dict must not have been mutated (cleanup/side-effect check).
    assert original == {'key': 'value'}
    assert not any(isinstance(k, AnsibleUnsafe) for k in original)
    assert not any(isinstance(v, AnsibleUnsafe) for v in original.values())


def test_wrap_dict_empty():
    """Even an empty dict still executes line 106 (the dict() call)."""
    result = _wrap_dict({})
    assert result == {}
    assert isinstance(result, dict)


def test_wrap_dict_mixed_value_types():
    """Every comprehension iteration wraps both key and value via wrap_var()."""
    original = {
        'str_key': 'str_value',
        b'bytes_key': b'bytes_value',
        'nested': {'inner': 'inner_value'},
        'seq': ['item1', 'item2'],
        'none_key': None,
    }
    result = _wrap_dict(original)

    # Keys were wrapped (the wrap_var(k) half of line 106).
    for key in result:
        assert isinstance(key, AnsibleUnsafe)

    # Plain str -> AnsibleUnsafeText.
    assert isinstance(result['str_key'], AnsibleUnsafeText)
    assert result['str_key'] == 'str_value'

    # bytes -> AnsibleUnsafeBytes.
    assert isinstance(result[b'bytes_key'], AnsibleUnsafeBytes)
    assert result[b'bytes_key'] == b'bytes_value'

    # None passes through untouched.
    assert result['none_key'] is None

    # Nested Mapping values are wrapped recursively (wrap_var applied again).
    nested = result['nested']
    assert isinstance(nested, dict)
    (inner_key, inner_value), = nested.items()
    assert isinstance(inner_key, AnsibleUnsafeText)
    assert isinstance(inner_value, AnsibleUnsafeText)
    assert inner_key == 'inner'
    assert inner_value == 'inner_value'

    # Sequence values are wrapped too.
    assert all(isinstance(item, AnsibleUnsafe) for item in result['seq'])
    assert list(result['seq']) == ['item1', 'item2']

    # Overall equality with the original is preserved.
    assert result == original
    # And the input was not mutated.
    assert original == {
        'str_key': 'str_value',
        b'bytes_key': b'bytes_value',
        'nested': {'inner': 'inner_value'},
        'seq': ['item1', 'item2'],
        'none_key': None,
    }


def test_wrap_dict_passthrough_already_wrapped():
    """wrap_var's early-return branch: already-unsafe items are not re-wrapped."""
    key = AnsibleUnsafeText('safe_key')
    value = AnsibleUnsafeBytes(b'safe_value')
    result = _wrap_dict({key: value})

    (result_key, result_value), = result.items()
    assert result_key is key        # identity preserved
    assert result_value is value    # identity preserved
    assert result == {'safe_key': b'safe_value'}


def test_wrap_dict_native_jinja_text_value():
    """A NativeJinjaText value becomes NativeJinjaUnsafeText inside the dict."""
    result = _wrap_dict({'k': NativeJinjaText('template_value')})
    value = result['k']
    assert isinstance(value, NativeJinjaUnsafeText)
    assert isinstance(value, AnsibleUnsafe)
    assert value == 'template_value'


def test_wrap_var_with_mapping_reaches_wrap_dict():
    """wrap_var() on a Mapping delegates to _wrap_dict, executing line 106."""
    original = {'a': 'b', 'c': {'d': 'e'}}
    result = wrap_var(_MyMapping(original))

    assert isinstance(result, dict)
    assert result is not original
    for key in result:
        assert isinstance(key, AnsibleUnsafe)
    assert isinstance(result['a'], AnsibleUnsafeText)
    nested = result['c']
    assert isinstance(nested, dict)
    assert all(isinstance(k, AnsibleUnsafe) for k in nested)
    assert all(isinstance(v, AnsibleUnsafe) for v in nested.values())
    # Contents equal the original mapping.
    assert result == original
    # The input mapping was not mutated.
    assert dict(original) == {'a': 'b', 'c': {'d': 'e'}}
