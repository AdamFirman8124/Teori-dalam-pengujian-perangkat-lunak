# file: project/typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest

from typesystem import String
from typesystem.base import ValidationError
from typesystem.schemas import Schema
from typesystem.schemas import Reference


class Book(Schema):
    title = String()


class TestReferenceClassTarget:
    def test_init_with_schema_class_sets_target(self):
        ref = Reference(to=Book)
        assert ref._target is Book
        assert not hasattr(ref, "_target_string")

    def test_target_string_property_derives_from_class_name(self):
        ref = Reference(to=Book)
        assert not hasattr(ref, "_target_string")
        assert ref.target_string == "Book"
        assert ref._target_string == "Book"

    def test_target_property_returns_class_directly(self):
        ref = Reference(to=Book)
        assert ref.target is Book

    def test_validate_delegates_to_schema_class(self):
        ref = Reference(to=Book)
        result = ref.validate({"title": "Dune"})
        assert result.title == "Dune"

    def test_validate_none_with_allow_null_returns_none(self):
        ref = Reference(to=Book, allow_null=True)
        assert ref.validate(None) is None

    def test_validate_none_without_allow_null_raises(self):
        ref = Reference(to=Book)
        with pytest.raises(ValidationError):
            ref.validate(None)

    def test_serialize_none_returns_none(self):
        ref = Reference(to=Book)
        assert ref.serialize(None) is None

    def test_serialize_dict_returns_dict_copy(self):
        ref = Reference(to=Book)
        obj = {"title": "Dune"}
        result = ref.serialize(obj)
        assert result == {"title": "Dune"}
        assert result is not obj


class TestReferenceStringTarget:
    def test_init_with_string_sets_target_string(self):
        ref = Reference(to="Book", definitions={"Book": Book})
        assert ref._target_string == "Book"
        assert not hasattr(ref, "_target")

    def test_target_property_resolves_from_definitions(self):
        ref = Reference(to="Book", definitions={"Book": Book})
        assert not hasattr(ref, "_target")
        assert ref.target is Book
        assert ref._target is Book

    def test_target_property_without_definitions_asserts(self):
        ref = Reference(to="Book")
        with pytest.raises(AssertionError, match="missing 'definitions'"):
            ref.target

    def test_validate_delegates_to_resolved_target(self):
        ref = Reference(to="Book", definitions={"Book": Book})
        result = ref.validate({"title": "Dune"})
        assert result.title == "Dune"

    def test_validate_none_with_allow_null_returns_none(self):
        ref = Reference(to="Book", definitions={"Book": Book}, allow_null=True)
        assert ref.validate(None) is None

    def test_validate_none_without_allow_null_raises(self):
        ref = Reference(to="Book", definitions={"Book": Book})
        with pytest.raises(ValidationError):
            ref.validate(None)

    def test_serialize_none_returns_none(self):
        ref = Reference(to="Book", definitions={"Book": Book})
        assert ref.serialize(None) is None

    def test_serialize_dict_returns_dict_copy(self):
        ref = Reference(to="Book", definitions={"Book": Book})
        obj = {"title": "Dune"}
        result = ref.serialize(obj)
        assert result == {"title": "Dune"}
        assert result is not obj
