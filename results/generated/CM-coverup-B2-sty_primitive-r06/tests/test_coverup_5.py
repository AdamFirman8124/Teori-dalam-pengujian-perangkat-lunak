# file: project/sty/primitive.py:181-193
# asked: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}
# gained: {"lines": [185, 187, 189, 191, 193], "branches": [[187, 189], [187, 193], [189, 187], [189, 191]]}

import pytest

from sty import Register


class TestRegisterAsDict:
    def test_as_dict_returns_string_attributes(self):
        """Lines 185-193: as_dict collects public str attributes into a dict."""
        reg = Register()
        # Plain strings pass through __setattr__ unchanged (not Style instances).
        reg.red = "red-value"
        reg.blue = "blue-value"

        result = reg.as_dict()

        assert result == {"red": "red-value", "blue": "blue-value"}
        assert isinstance(result, dict)
        assert all(isinstance(v, str) for v in result.values())

    def test_as_dict_excludes_underscore_and_non_string_attributes(self):
        """Branches at line 189: names starting with '_' and non-str values
        must be skipped."""
        reg = Register()
        reg.visible = "kept"
        reg._hidden = "skipped-underscore"
        reg.__dunder__ = "skipped-dunder"
        reg.not_a_string = 12345
        reg.a_list = ["nope"]

        result = reg.as_dict()

        assert result == {"visible": "kept"}
        assert "_hidden" not in result
        assert "__dunder__" not in result
        assert "not_a_string" not in result
        assert "a_list" not in result

    def test_as_dict_on_fresh_register_is_empty_of_user_strings(self):
        """A fresh Register has no public str attributes of its own
        (renderfuncs/is_muted/callables are not str), so as_dict returns {}."""
        reg = Register()

        result = reg.as_dict()

        assert result == {}

    def test_as_dict_reflects_mutation(self):
        """as_dict reads current state each call (line 191 update + 193 return)."""
        reg = Register()
        reg.key = "first"

        assert reg.as_dict() == {"key": "first"}

        reg.key = "second"
        reg.other = "added"

        assert reg.as_dict() == {"key": "second", "other": "added"}
