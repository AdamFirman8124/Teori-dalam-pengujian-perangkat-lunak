# file: project/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeText, to_unsafe_text, wrap_var


def test_to_unsafe_text_from_str():
    result = to_unsafe_text('hello world')
    assert result == 'hello world'
    assert isinstance(result, str)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, AnsibleUnsafeText)


def test_to_unsafe_text_from_bytes():
    result = to_unsafe_text(b'hello world')
    assert result == 'hello world'
    assert isinstance(result, str)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, AnsibleUnsafeText)


def test_to_unsafe_text_with_encoding_kwarg():
    result = to_unsafe_text(b'caf\xc3\xa9', encoding='utf-8')
    assert result == 'caf\u00e9'
    assert isinstance(result, AnsibleUnsafe)


def test_to_unsafe_text_with_errors_and_nonstring_kwargs():
    # errors kwarg is forwarded to to_text
    result = to_unsafe_text(b'hello \xff', encoding='utf-8', errors='ignore')
    assert result == 'hello '
    assert isinstance(result, AnsibleUnsafe)
    # nonstring kwarg is forwarded to to_text
    result2 = to_unsafe_text(123, nonstring='simplerepr')
    assert result2 == '123'
    assert isinstance(result2, AnsibleUnsafe)
