

# Generated at 2026-10-25 04:40:24.514445
# Unit test for constructor of class Schema
def test_Schema():import pytest


# Generated at 2026-10-25 04:40:25.879393
# Unit test for constructor of class SchemaDefinitions
def test_SchemaDefinitions():
    # 1. Init from kwargs
    defs = SchemaDefinitions(a=1)
    assert defs["a"] == 1
    assert len(defs) == 1

    # 2. Init from a dict
    defs = SchemaDefinitions({"a": 1, "b": 2})
    assert len(defs) == 2
    assert defs["b"] == 2

    # 3. Iteration yields keys
    assert sorted(defs) == ["a", "b"]

    # 4. __setitem__ inserts new keys
    defs["c"] = 3
    assert defs["c"] == 3
    assert len(defs) == 3

    # 5. __setitem__ rejects duplicate keys
    with pytest.raises(AssertionError):
        defs["c"] = 99

    # 6. __delitem__ removes keys
    del defs["c"]
    assert "c" not in defs
    assert len(defs) == 2

    # 7. Missing keys raise KeyError
    with pytest.raises(KeyError):
        defs["missing"]

    # 8. MutableMapping mixin methods work
    defs.update({"d": 4})
    assert defs.pop("d") == 4
    assert "d" not in defs

# Generated at 2026-10-25 04:40:27.202392
# Unit test for method __iter__ of class SchemaDefinitions
def test_SchemaDefinitions___iter__():
    definitions = SchemaDefinitions({"a": 1, "b": 2})
    assert set(iter(definitions)) == {"a", "b"}
    assert list(definitions) == list(definitions._definitions)

# Generated at 2026-10-25 04:40:28.542359
# Unit test for function set_definitions
def test_set_definitions():
    # 1. Plain string reference gets the definitions mapping assigned.
    definitions = SchemaDefinitions()
    ref = Reference("Example")
    assert ref.definitions is None
    module_0.set_definitions(ref, definitions)
    assert ref.definitions is definitions

    # 2. Array with a list of items recurses into each child.
    ref_a, ref_b = Reference("A"), Reference("B")
    module_0.set_definitions(Array(items=[ref_a, ref_b]), definitions)
    assert ref_a.definitions is definitions
    assert ref_b.definitions is definitions

    # 3. Array with a single item recurses into it.
    ref_c = Reference("C")
    module_0.set_definitions(Array(items=ref_c), definitions)
    assert ref_c.definitions is definitions

    # 4. Object recurses into its properties.
    ref_d = Reference("D")
    module_0.set_definitions(Object(properties={"d": ref_d}), definitions)
    assert ref_d.definitions is definitions

    # 5. Nested Array -> Object -> Reference is reached.
    ref_e = Reference("E")
    nested = Array(items=Object(properties={"e": ref_e}))
    module_0.set_definitions(nested, definitions)
    assert ref_e.definitions is definitions

    # 6. A Reference that already has definitions is not overwritten.
    existing = SchemaDefinitions()
    ref_f = Reference("F", definitions=existing)
    module_0.set_definitions(ref_f, definitions)
    assert ref_f.definitions is existing

# Generated at 2026-10-25 04:40:29.872901
# Unit test for method __iter__ of class SchemaDefinitions
def test_SchemaDefinitions___iter__():
    definitions = SchemaDefinitions({"a": 1, "b": 2})
    assert set(iter(definitions)) == {"a", "b"}
    assert list(definitions) == list(definitions._definitions)

# Generated at 2026-10-25 04:40:40.255056
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:40:49.507780
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:40:58.481447
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:41:10.902963
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class OtherPerson(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})

    # Instances of the same class with equal field values are equal.
    assert person == Person({"name": "Alice", "age": 30})

    # A differing field value makes instances unequal.
    assert person != Person({"name": "Alice", "age": 31})
    assert person != Person({"name": "Bob", "age": 30})

    # Equal values on a different Schema class are not equal.
    assert person != OtherPerson({"name": "Alice", "age": 30})

    # Non-Schema and unrelated values are not equal.
    assert person != {"name": "Alice", "age": 30}
    assert person != object()
    assert person != None

# Generated at 2026-10-25 04:41:21.141388
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        first = Object()
        second = Object()

    class OtherSchema(Schema):
        first = Object()
        second = Object()

    value = {"first": "alpha", "second": 123}

    assert ExampleSchema(value) == ExampleSchema(value)
    assert ExampleSchema(value) != ExampleSchema(
        {"first": "alpha", "second": 456}
    )
    assert ExampleSchema(value) != OtherSchema(value)
    assert ExampleSchema(value) != value

# Generated at 2026-10-25 04:41:23.559114
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:41:25.975262
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:41:28.389284
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:41:39.994865
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:41:44.901688
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:41:51.144092
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:01.388045
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:08.500202
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:11.152228
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:13.568168
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:42:15.983050
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:42:18.398403
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 04:42:20.977504
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:23.503255
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:25.921794
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:28.338742
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:30.752036
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:33.166225
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:35.584305
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:42:37.997438
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:42:50.843550
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:42:58.524208
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()
    replacement = object()

    definitions["example"] = original

    assert definitions["example"] is original
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["example"] = replacement

    # A duplicate assignment must not overwrite the original definition.
    assert definitions["example"] is original
    assert len(definitions) == 1

# Generated at 2026-10-25 04:43:10.302176
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:43:16.128414
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:43:24.943316
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:43:27.653756
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:43:30.177586
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:43:32.702888
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:43:35.121284
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:43:37.536066
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:43:50.839840
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 04:43:57.814661
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()

    definitions["Example"] = original

    assert definitions["Example"] is original
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["Example"] = object()

    # A duplicate assignment must not replace the original definition.
    assert definitions["Example"] is original
    assert len(definitions) == 1

# Generated at 2026-10-25 04:44:08.976904
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class OtherSchema(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})

    # Instances of the same schema with equal field values are equal.
    assert person == Person({"name": "Alice", "age": 30})

    # A differing field value makes instances unequal.
    assert person != Person({"name": "Alice", "age": 31})
    assert person != Person({"name": "Bob", "age": 30})

    # Values from a different schema class are not equal.
    assert person != OtherSchema({"name": "Alice", "age": 30})

    # Schema instances are not equal to unrelated values.
    assert person != {"name": "Alice", "age": 30}
    assert person != None  # noqa: E711

# Generated at 2026-10-25 04:44:18.707529
# Unit test for constructor of class Reference
def test_Reference():
    class UserSchema(Schema):
        pass

    definitions = SchemaDefinitions({"UserSchema": UserSchema})

    # String-based reference.
    string_reference = Reference("UserSchema", definitions=definitions)

    assert string_reference.to == "UserSchema"
    assert string_reference.definitions is definitions
    assert string_reference.target_string == "UserSchema"
    assert string_reference.target is UserSchema

    # Direct schema reference.
    direct_reference = Reference(UserSchema)

    assert direct_reference.to is UserSchema
    assert direct_reference.definitions is None
    assert direct_reference.target is UserSchema
    assert direct_reference.target_string == "UserSchema"

# Generated at 2026-10-25 04:44:35.616797
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    class OtherSchema(Schema):
        name = Field()
        age = Field()

    value = ExampleSchema({"name": "Alice", "age": 30})
    identical = ExampleSchema({"name": "Alice", "age": 30})
    different_name = ExampleSchema({"name": "Bob", "age": 30})
    different_age = ExampleSchema({"name": "Alice", "age": 31})
    other_type = OtherSchema({"name": "Alice", "age": 30})

    assert value == value
    assert value == identical
    assert value != different_name
    assert value != different_age
    assert value != other_type
    assert value != {"name": "Alice", "age": 30}

# Generated at 2026-10-25 04:44:38.033321
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:44:46.863552
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:44:57.924521
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:45:07.548386
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:13.487755
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:19.432136
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:30.729053
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:33.164355
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:35.624105
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:38.155977
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:45:44.515788
# Unit test for constructor of class Reference
def test_Reference():definitions = SchemaDefinitions()

# Generated at 2026-10-25 04:46:09.285650
# Unit test for constructor of class Schema
def test_Schema():import pytest


# Generated at 2026-10-25 04:46:29.252505
# Unit test for constructor of class Schema
def test_Schema():import pytest

# Generated at 2026-10-25 04:46:31.800324
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:46:34.319113
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:46:36.858363
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:46:39.421142
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:46:41.841868
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:46:44.257641
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:46:46.674522
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 04:46:55.963054
# Unit test for method serialize of class Reference
def test_Reference_serialize():reference = Reference("Example")
assert reference.serialize({"name": "Alice", "age": 30}) == {
    "name": "Alice",
    "age": 30,
}

# Generated at 2026-10-25 04:47:06.849517
# Unit test for constructor of class Reference
def test_Reference():
    class ExampleSchema(Schema):
        pass

    definitions = {"ExampleSchema": ExampleSchema}

    # String references retain their name and definitions for lazy resolution.
    string_reference = Reference(
        "ExampleSchema",
        definitions=definitions,
        allow_null=True,
    )
    assert string_reference.to == "ExampleSchema"
    assert string_reference.definitions is definitions
    assert string_reference._target_string == "ExampleSchema"
    assert not hasattr(string_reference, "_target")
    assert string_reference.allow_null is True

    # Schema class references are stored directly.
    direct_reference = Reference(ExampleSchema)
    assert direct_reference.to is ExampleSchema
    assert direct_reference.definitions is None
    assert direct_reference._target is ExampleSchema
    assert not hasattr(direct_reference, "_target_string")

    # Non-Schema classes are not valid direct targets.
    with pytest.raises(AssertionError):
        Reference(int)

# Generated at 2026-10-25 04:47:16.420488
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    empty_schema = ExampleSchema()
    assert len(empty_schema) == 0

    sparse_schema = ExampleSchema({"first": "value"})
    assert len(sparse_schema) == 1

    complete_schema = ExampleSchema({"first": "value", "second": 123})
    assert len(complete_schema) == 2

# Generated at 2026-10-25 04:47:22.718413
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()

    definitions["example"] = original

    assert definitions["example"] is original
    assert len(definitions) == 1

    replacement = object()
    with pytest.raises(AssertionError):
        definitions["example"] = replacement

    # A duplicate assignment must not replace the existing definition.
    assert definitions["example"] is original

# Generated at 2026-10-25 04:47:33.572518
# Unit test for method validate of class Reference
def test_Reference_validate():
    target = Mock()
    target.validate.return_value = "validated"
    definitions = {"Target": target}

    # Valid values are delegated to the referenced target.
    reference = Reference("Target", definitions=definitions)
    value = {"name": "example"}

    assert reference.validate(value, strict=True) == "validated"
    target.validate.assert_called_once_with(value, strict=True)

    # Null is returned directly when explicitly allowed.
    target.reset_mock()
    nullable_reference = Reference(
        "Target", definitions=definitions, allow_null=True
    )

    assert nullable_reference.validate(None) is None
    target.validate.assert_not_called()

    # Null raises a validation error when it is not allowed.
    with pytest.raises(ValidationError):
        reference.validate(None)

    target.validate.assert_not_called()

# Generated at 2026-10-25 04:47:36.123873
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:47:38.795685
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:47:41.209439
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:47:43.629972
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:47:46.049008
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:47:48.463558
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:47:50.879495
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 04:47:53.293283
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 04:47:55.707999
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 04:47:58.127242
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:48:00.544313
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:48:02.962299
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:48:05.375201
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:48:07.790631
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:48:10.222228
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:48:12.635203
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:48:15.045374
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:48:17.478544
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:48:19.893499
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:48:22.309776
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:48:24.722499
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:48:27.139408
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:48:29.549697
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:48:31.965379
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:48:34.383271
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:48:36.798315
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:48:39.214140
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:48:42.243979
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:48:44.657689
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:48:47.072725
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:48:49.486452
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:48:52.309757
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 04:49:02.457005
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Person(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})
    assert repr(person) == "Person(name='Alice', age=30)"

    sparse_person = Person({"name": "Alice"})
    assert repr(sparse_person) == "Person(name='Alice') [sparse]"

    empty_person = Person({})
    assert repr(empty_person) == "Person() [sparse]"

# Generated at 2026-10-25 04:49:11.216187
# Unit test for method validate of class Reference
def test_Reference_validate():
    from unittest.mock import Mock

    import pytest

    target = Mock()
    target.validate.return_value = "validated"
    definitions = {"Target": target}

    # Non-null values are delegated to the referenced target.
    reference = Reference("Target", definitions=definitions)
    value = {"name": "example"}

    assert reference.validate(value, strict=True) == "validated"
    target.validate.assert_called_once_with(value, strict=True)

    # Null values are rejected by default.
    with pytest.raises(ValidationError):
        reference.validate(None)

    # Null values are accepted when allow_null=True and are not delegated.
    target.reset_mock()
    nullable_reference = Reference(
        "Target",
        definitions=definitions,
        allow_null=True,
    )

    assert nullable_reference.validate(None) is None
    target.validate.assert_not_called()

# Generated at 2026-10-25 04:49:13.633542
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:49:20.322096
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:49:30.310169
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:49:41.266377
# Unit test for method validate of class Reference
def test_Reference_validate():
    calls = []
    validated_value = object()

    class TargetSchema(Schema):
        @classmethod
        def module_0.validate(cls, value, *, strict=False):
            calls.append((value, strict))
            return validated_value

    reference = Reference(to=TargetSchema)

    value = {"example": "value"}
    assert reference.validate(value) is validated_value
    assert calls == [(value, False)]

    calls.clear()
    assert reference.validate(value, strict=True) is validated_value
    assert calls == [(value, True)]

    # Null values are rejected by default.
    with pytest.raises(ValidationError):
        reference.validate(None)

    # Null values are accepted without delegating when allow_null=True.
    calls.clear()
    nullable_reference = Reference(to=TargetSchema, allow_null=True)
    assert nullable_reference.validate(None) is None
    assert calls == []

# Generated at 2026-10-25 04:49:42.710478
# Unit test for method serialize of class Reference
def test_Reference_serialize():import pytest

from typesystem.schemas import Reference, Schema
from typesystem import String, Integer


class Book(Schema):
    title = String()
    year = Integer()


class Library(Schema):
    name = String()
    book = Reference(to=Book)


class SparseBook(Schema):
    title = String()
    year = Integer()


def test_Reference_serialize_with_none():
    ref = Reference(to=Book)
    assert ref.serialize(None) is None


def test_Reference_serialize_with_plain_dict():
    ref = Reference(to=Book)
    value = {"title": "Dune", "year": 1965}
    result = ref.serialize(value)
    assert result == {"title": "Dune", "year": 1965}
    # Must be a new dict, not the same object
    assert result is not value


def test_Reference_serialize_with_schema_instance():
    ref = Reference(to=Book)
    book = Book({"title": "Dune", "year": 1965})
    result = ref.serialize(book)
    assert result == {"title": "Dune", "year": 1965}
    assert isinstance(result, dict)


def test_Reference_serialize_with_sparse_schema_instance():
    # A sparse schema (missing some fields) should only include
    # the attributes that are actually set.
    ref = Reference(to=Book)
    book = Book()
    book.title = "Dune"  # 'year' left unset
    result = ref.serialize(book)
    assert result == {"title": "Dune"}


def test_Reference_serialize_with_nested_reference():
    # Reference inside a schema serializes via Schema.__getitem__,
    # which calls field.serialize -> dict(obj).
    library = Library({"name": "City Library", "book": {"title": "Dune", "year": 1965}})
    result = dict(library)
    assert result == {
        "name": "City Library",
        "book": {"title": "Dune", "year": 1965},
    }


def test_Reference_serialize_with_non_mapping_raises():
    ref = Reference(to=Book)
    with pytest.raises(TypeError):
        ref.serialize(123)

# Generated at 2026-10-25 04:49:50.798983
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()
    replacement = object()

    definitions["User"] = original

    assert definitions["User"] is original
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["User"] = replacement

    # A duplicate assignment must not replace the original definition.
    assert definitions["User"] is original
    assert len(definitions) == 1

# Generated at 2026-10-25 04:50:01.645188
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class OtherPerson(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})

    # Equal instances of the same schema.
    assert person == Person({"name": "Alice", "age": 30})

    # A differing field makes instances unequal.
    assert person != Person({"name": "Alice", "age": 31})

    # Identical values from a different schema class are not equal.
    assert person != OtherPerson({"name": "Alice", "age": 30})

    # Schema instances are not equal to arbitrary objects.
    assert person != {"name": "Alice", "age": 30}