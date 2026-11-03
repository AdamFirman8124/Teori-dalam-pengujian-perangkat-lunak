# file: project/ansible/module_utils/compat/version.py:140-156
# asked: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}
# gained: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


class TestStrictVersionParse:
    """Tests for StrictVersion.parse covering all lines/branches."""

    @pytest.mark.parametrize(
        "vstring, expected_version, expected_prerelease, expected_str",
        [
            # patch present, no prerelease -> lines 148-149 and 156
            ("1.2.3", (1, 2, 3), None, "1.2.3"),
            # patch absent -> line 151 (else branch), and line 156
            ("1.2", (1, 2, 0), None, "1.2"),
            # patch absent, prerelease present -> lines 151 and 153-154
            ("1.2a3", (1, 2, 0), ("a", 3), "1.2a3"),
            # patch present, prerelease present -> lines 148-149 and 153-154
            ("1.0.4b1", (1, 0, 4), ("b", 1), "1.0.4b1"),
            # zero patch component still counts as "patch" (truthy string),
            # but __str__ canonicalizes it back to the two-component form
            ("0.4.0", (0, 4, 0), None, "0.4"),
        ],
    )
    def test_parse_valid_versions(self, vstring, expected_version, expected_prerelease, expected_str):
        version = StrictVersion(vstring)

        assert version.version == expected_version
        assert version.prerelease == expected_prerelease
        # round-trip through __str__ should reproduce the canonical form
        assert str(version) == expected_str
        # the canonical form must re-parse to the same state
        reparsed = StrictVersion(expected_str)
        assert reparsed.version == expected_version
        assert reparsed.prerelease == expected_prerelease

    def test_parse_prerelease_letter_and_number(self):
        version = StrictVersion("1.0.4a3")

        # prerelease[0] is the letter, prerelease[1] is the int-converted number
        assert version.prerelease == ("a", 3)
        assert isinstance(version.prerelease[1], int)
        assert version.version == (1, 0, 4)

    @pytest.mark.parametrize(
        "vstring",
        [
            "1",          # only one numeric component
            "2.7.2.2",    # too many components
            "1.3.a4",     # prerelease letter before patch number
            "1.3pl1",     # unsupported prerelease tag
            "1.3c4",      # unsupported prerelease letter
            "a.1",        # non-numeric major
        ],
    )
    def test_parse_invalid_versions_raise_value_error(self, vstring):
        with pytest.raises(ValueError) as excinfo:
            StrictVersion(vstring)

        assert "invalid version number" in str(excinfo.value)
        assert vstring in str(excinfo.value)

    def test_parse_empty_string_directly_raises_value_error(self):
        # The constructor skips parse() for falsy input, so call parse()
        # directly to exercise the ValueError branch with an empty string.
        version = StrictVersion()

        with pytest.raises(ValueError) as excinfo:
            version.parse("")

        assert "invalid version number ''" in str(excinfo.value)

    def test_parse_invalid_version_message_content(self):
        with pytest.raises(ValueError, match="invalid version number '1.3c4'"):
            StrictVersion("1.3c4")

    def test_parse_via_constructor_and_repr(self):
        version = StrictVersion("1.0.4a3")

        assert repr(version) == "StrictVersion ('1.0.4a3')"
        assert version == StrictVersion("1.0.4a3")
        assert version < StrictVersion("1.0.4")
