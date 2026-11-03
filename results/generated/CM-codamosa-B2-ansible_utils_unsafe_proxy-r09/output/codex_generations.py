

# Generated at 2026-11-02 20:19:44.528209
# Unit test for constructor of class AnsibleUnsafe
def test_AnsibleUnsafe():
    instance = AnsibleUnsafe()
    assert instance.__UNSAFE__ is True
    assert AnsibleUnsafe.__UNSAFE__ is True
    assert isinstance(instance, AnsibleUnsafe)
    assert isinstance(instance, object)

    # Subclasses should also inherit the unsafe marker
    assert issubclass(AnsibleUnsafeText, AnsibleUnsafe)
    assert issubclass(AnsibleUnsafeBytes, AnsibleUnsafe)
    assert AnsibleUnsafeText('foo').__UNSAFE__ is True
    assert AnsibleUnsafeBytes(b'foo').__UNSAFE__ is True

# Generated at 2026-11-02 20:22:27.460646
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.unsafe_proxy import UnsafeProxy, AnsibleUnsafe, AnsibleUnsafeText, AnsibleUnsafeBytes, wrap_var


class TestUnsafeProxyNew:
    """Tests for UnsafeProxy.__new__ method."""

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_string(self, mock_display):
        """Test that a string is converted to AnsibleUnsafeText."""
        result = UnsafeProxy("hello")
        assert isinstance(result, AnsibleUnsafeText)
        assert result == "hello"

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_already_unsafe(self, mock_display):
        """Test that an already unsafe object is returned as-is."""
        unsafe_obj = AnsibleUnsafeText("already_unsafe")
        result = UnsafeProxy(unsafe_obj)
        assert result is unsafe_obj

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_none(self, mock_display):
        """Test that None is returned unchanged."""
        result = UnsafeProxy(None)
        assert result is None

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_int(self, mock_display):
        """Test that an integer is returned unchanged."""
        result = UnsafeProxy(42)
        assert result == 42
        assert not isinstance(result, AnsibleUnsafe)

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_list(self, mock_display):
        """Test that a list is returned unchanged (not wrapped)."""
        test_list = [1, 2, 3]
        result = UnsafeProxy(test_list)
        assert result is test_list
        assert not isinstance(result, AnsibleUnsafe)

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_dict(self, mock_display):
        """Test that a dict is returned unchanged (not wrapped)."""
        test_dict = {'key': 'value'}
        result = UnsafeProxy(test_dict)
        assert result is test_dict
        assert not isinstance(result, AnsibleUnsafe)

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_bytes(self, mock_display):
        """Test that bytes are returned unchanged (not wrapped) by UnsafeProxy."""
        result = UnsafeProxy(b'byte_data')
        assert result == b'byte_data'
        assert not isinstance(result, AnsibleUnsafe)

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_unicode_string(self, mock_display):
        """Test that a unicode string is converted to AnsibleUnsafeText."""
        result = UnsafeProxy(u'unicode_string')
        assert isinstance(result, AnsibleUnsafeText)
        assert result == u'unicode_string'

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_deprecation_warning(self, mock_display_class):
        """Test that the deprecation warning is issued."""
        mock_display_instance = MagicMock()
        mock_display_class.return_value = mock_display_instance
        UnsafeProxy("test")
        mock_display_instance.deprecated.assert_called_once()

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_deprecation_message(self, mock_display_class):
        """Test the content of the deprecation warning."""
        mock_display_instance = MagicMock()
        mock_display_class.return_value = mock_display_instance
        UnsafeProxy("test")
        call_args = mock_display_instance.deprecated.call_args
        assert 'UnsafeProxy is being deprecated' in call_args[0][0]

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_empty_string(self, mock_display):
        """Test that an empty string is converted to AnsibleUnsafeText."""
        result = UnsafeProxy("")
        assert isinstance(result, AnsibleUnsafeText)
        assert result == ""

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_float(self, mock_display):
        """Test that a float is returned unchanged."""
        result = UnsafeProxy(3.14)
        assert result == 3.14
        assert not isinstance(result, AnsibleUnsafe)

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_bool(self, mock_display):
        """Test that a boolean is returned unchanged."""
        result = UnsafeProxy(True)
        assert result is True
        assert not isinstance(result, AnsibleUnsafe)

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_ansible_unsafe_bytes(self, mock_display):
        """Test that AnsibleUnsafeBytes instance is returned as-is."""
        unsafe_bytes = AnsibleUnsafeBytes(b'unsafe_bytes')
        result = UnsafeProxy(unsafe_bytes)
        assert result is unsafe_bytes

    @patch('ansible.vars.unsafe_proxy.Display')
    def test_unsafe_proxy_tuple(self, mock_display):
        """Test that a tuple is returned unchanged."""
        test_tuple = (1, 2, 3)
        result = UnsafeProxy(test_tuple)
        assert result is test_tuple
        assert not isinstance(result, AnsibleUnsafe)

# Generated at 2026-11-02 20:24:11.923210
# Unit test for constructor of class NativeJinjaUnsafeText
def test_NativeJinjaUnsafeText():
    from ansible.utils.native_jinja import NativeJinjaText

    # Basic construction with a text value
    value = NativeJinjaUnsafeText('123')
    assert value == '123'
    assert isinstance(value, NativeJinjaUnsafeText)
    assert isinstance(value, NativeJinjaText)
    assert isinstance(value, AnsibleUnsafeText)
    assert isinstance(value, text_type)
    assert value.__UNSAFE__ is True

    # Constructing with unicode content
    value = NativeJinjaUnsafeText(u'\xf0')
    assert value == u'\xf0'
    assert value.__UNSAFE__ is True

    # encode() should preserve the unsafe context via AnsibleUnsafeBytes
    encoded = value.encode()
    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert isinstance(encoded, binary_type)
    assert encoded == b'123'
    assert encoded.__UNSAFE__ is True

    # decode() should preserve the unsafe context via AnsibleUnsafeText
    decoded = encoded.decode()
    assert isinstance(decoded, AnsibleUnsafeText)
    assert decoded == '123'
    assert decoded.__UNSAFE__ is True

    # wrap_var should return an existing NativeJinjaUnsafeText untouched
    assert wrap_var(NativeJinjaUnsafeText('123')) is not None
    assert isinstance(wrap_var(NativeJinjaUnsafeText('123')), NativeJinjaUnsafeText)

# Generated at 2026-11-02 20:26:01.249990
# Unit test for method __new__ of class UnsafeProxy
def test_UnsafeProxy___new__():
    from unittest.mock import patch, MagicMock

    from ansible.utils.unsafe_proxy import (
        AnsibleUnsafe,
        AnsibleUnsafeBytes,
        AnsibleUnsafeText,
        UnsafeProxy,
    )

    # Suppress the deprecation warning emitted by UnsafeProxy
    with patch('ansible.utils.display.Display'):
        # A text string should be wrapped in AnsibleUnsafeText
        res = UnsafeProxy(u'testing')
        assert isinstance(res, AnsibleUnsafeText)
        assert isinstance(res, AnsibleUnsafe)
        assert res == u'testing'
        assert getattr(res, '__UNSAFE__', False) is True

        # Unicode content should be preserved
        res = UnsafeProxy(u'héllo wörld')
        assert isinstance(res, AnsibleUnsafeText)
        assert res == u'héllo wörld'

        # A bytes object is not a string_type, so it should be returned unchanged
        res = UnsafeProxy(b'testing')
        assert res == b'testing'
        assert not isinstance(res, AnsibleUnsafe)

        # An already unsafe value should be returned as-is (same object)
        unsafe_text = AnsibleUnsafeText(u'already unsafe')
        assert UnsafeProxy(unsafe_text) is unsafe_text

        unsafe_bytes = AnsibleUnsafeBytes(b'already unsafe')
        assert UnsafeProxy(unsafe_bytes) is unsafe_bytes

        # Non-string values should be returned unchanged (same object)
        none_value = None
        assert UnsafeProxy(none_value) is none_value

        int_value = 12345
        assert UnsafeProxy(int_value) is int_value

        list_value = [u'a', u'b', 1, 2]
        assert UnsafeProxy(list_value) is list_value

        dict_value = {u'key': u'value'}
        assert UnsafeProxy(dict_value) is dict_value

        tuple_value = (u'a', u'b')
        assert UnsafeProxy(tuple_value) is tuple_value

        set_value = set([u'a', u'b'])
        assert UnsafeProxy(set_value) is set_value