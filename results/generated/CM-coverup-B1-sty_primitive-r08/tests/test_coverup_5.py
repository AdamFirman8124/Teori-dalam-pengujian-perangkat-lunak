# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

import pytest

from sty.primitive import Register


class TestRegisterAsDict:
    def test_as_dict_empty_register(self):
        """A fresh Register with no string attributes returns an empty dict."""
        reg = Register()
        result = reg.as_dict()
        assert result == {}
        assert isinstance(result, dict)

    def test_as_dict_with_string_attributes(self):
        """Public string attributes are exported; private and non-string ones are not."""
        reg = Register()
        reg.red = "\033[31m"
        reg.green = "\033[32m"
        reg.blue = "\033[34m"
        # Should be excluded: private name
        reg._hidden = "\033[35m"
        # Should be excluded: dunder-ish private name
        reg.__secret = "\033[36m"
        # Should be excluded: non-string value
        reg.count = 42
        reg.callback = lambda x: x

        result = reg.as_dict()

        assert result == {
            "red": "\033[31m",
            "green": "\033[32m",
            "blue": "\033[34m",
        }
        # Postconditions: only public str attributes present
        assert "_hidden" not in result
        assert "count" not in result
        assert "callback" not in result
        assert all(isinstance(v, str) for v in result.values())

    def test_as_dict_values_are_str(self):
        """Values in the returned dict are str() of the attribute values."""
        reg = Register()
        reg.color = "value"
        result = reg.as_dict()
        assert result["color"] == str(reg.color)
        assert result["color"] == "value"

    def test_as_dict_does_not_mutate_register(self):
        """Calling as_dict leaves the register itself unchanged."""
        reg = Register()
        reg.color = "value"
        before = dict(vars(reg))
        reg.as_dict()
        assert vars(reg) == before

    def test_as_dict_on_copy_is_independent(self):
        """A copied register exports its own attributes via as_dict."""
        reg = Register()
        reg.color = "original"
        clone = reg.copy()
        clone.color = "copied"
        assert reg.as_dict() == {"color": "original"}
        assert clone.as_dict() == {"color": "copied"}
