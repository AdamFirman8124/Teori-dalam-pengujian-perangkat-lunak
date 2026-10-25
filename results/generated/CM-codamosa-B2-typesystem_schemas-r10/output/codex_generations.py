

# Generated at 2026-10-25 03:44:34.209967
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    assert len(ExampleSchema({})) == 0
    assert len(ExampleSchema({"first": 1})) == 1
    assert len(ExampleSchema({"first": 1, "second": 2})) == 2
    assert len(ExampleSchema({"first": 1, "second": 2, "third": 3})) == 3

# Generated at 2026-10-25 03:44:35.545313
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

# Generated at 2026-10-25 03:44:45.440149
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original_definition = object()

    definitions["User"] = original_definition

    assert definitions["User"] is original_definition
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["User"] = object()

    # A duplicate assignment must not replace the original definition.
    assert definitions["User"] is original_definition
    assert len(definitions) == 1

# Generated at 2026-10-25 03:44:56.814267
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class TestField(Field):
        def validate(self, value: typing.Any, *, strict: bool = False) -> typing.Any:
            return value

        def serialize(self, value: typing.Any) -> typing.Any:
            return f"serialized:{value}"

    class TestSchema(Schema):
        populated = TestField()
        unset = TestField()

    instance = TestSchema({"populated": "value"})

    # Values are serialized using the corresponding field.
    assert instance["populated"] == "serialized:value"

    # A defined but unset field behaves like a missing mapping key.
    with pytest.raises(KeyError) as exc_info:
        instance["unset"]
    assert exc_info.value.args == ("unset",)

    # Unknown fields also raise KeyError.
    with pytest.raises(KeyError) as exc_info:
        instance["unknown"]
    assert exc_info.value.args == ("unknown",)

# Generated at 2026-10-25 03:45:06.023047
# Unit test for method validate of class Reference
def test_Reference_validate():
    from unittest.mock import Mock

    import pytest

    target = Mock()
    target.validate.return_value = "validated"
    definitions = {"Target": target}

    # Non-null values are validated by the referenced target.
    reference = Reference("Target", definitions=definitions)
    value = {"name": "example"}

    assert reference.validate(value, strict=True) == "validated"
    target.validate.assert_called_once_with(value, strict=True)

    # Null values are rejected by default without invoking the target.
    target.reset_mock()
    with pytest.raises(ValidationError) as exc_info:
        reference.validate(None)

    assert exc_info.value.messages()[0].text == "May not be null."
    target.validate.assert_not_called()

    # Null values are accepted when allow_null is enabled.
    nullable_reference = Reference(
        "Target",
        definitions=definitions,
        allow_null=True,
    )

    assert nullable_reference.validate(None) is None
    target.validate.assert_not_called()

# Generated at 2026-10-25 03:45:08.583507
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

# Generated at 2026-10-25 03:45:21.701321
# Unit test for method validate of class Reference
def test_Reference_validate():
    calls = []
    validated_value = object()

    class TargetSchema(Schema):
        @classmethod
        def module_0.validate(cls, value, *, strict=False):
            calls.append((value, strict))
            return validated_value

    reference = Reference(TargetSchema)

    value = {"example": "value"}
    assert reference.validate(value, strict=True) is validated_value
    assert calls == [(value, True)]

    with pytest.raises(ValidationError):
        reference.validate(None)

    nullable_reference = Reference(TargetSchema, allow_null=True)
    assert nullable_reference.validate(None) is None

    # Null values are handled by Reference and are not delegated.
    assert calls == [(value, True)]

# Generated at 2026-10-25 03:45:37.562317
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

# Generated at 2026-10-25 03:45:45.548947
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original_definition = object()

    definitions["User"] = original_definition

    assert definitions["User"] is original_definition
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["User"] = object()

    # A duplicate assignment must not replace the original definition.
    assert definitions["User"] is original_definition
    assert len(definitions) == 1

# Generated at 2026-10-25 03:46:11.008828
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:46:17.192257
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:46:23.128614
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:46:24.461819
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

# Generated at 2026-10-25 03:46:44.531948
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class Employee(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})

    # Same class and field values are equal.
    assert person == Person({"name": "Alice", "age": 30})
    assert person == person

    # A differing field value makes instances unequal.
    assert person != Person({"name": "Alice", "age": 31})
    assert person != Person({"name": "Bob", "age": 30})

    # Instances of different schema classes are unequal.
    assert person != Employee({"name": "Alice", "age": 30})

    # A Schema instance is not equal to an unrelated object.
    assert person != {"name": "Alice", "age": 30}
    assert person != object()

# Generated at 2026-10-25 03:46:47.318200
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:47:19.063586
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()


# Generated at 2026-10-25 03:47:36.693011
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    class OtherSchema(Schema):
        name = Field()
        age = Field()

    schema = ExampleSchema({"name": "Alice", "age": 30})
    equal_schema = ExampleSchema({"name": "Alice", "age": 30})
    different_schema = ExampleSchema({"name": "Alice", "age": 31})
    other_schema_type = OtherSchema({"name": "Alice", "age": 30})

    assert schema == schema
    assert schema == equal_schema
    assert equal_schema == schema

    assert schema != different_schema
    assert schema != other_schema_type
    assert schema != {"name": "Alice", "age": 30}
    assert schema != None  # noqa: E711

# Generated at 2026-10-25 03:47:44.233296
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original_value = object()
    replacement_value = object()

    definitions["Example"] = original_value

    assert definitions["Example"] is original_value
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["Example"] = replacement_value

    # A duplicate assignment must not replace the existing definition.
    assert definitions["Example"] is original_value
    assert len(definitions) == 1

# Generated at 2026-10-25 03:47:52.533849
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original_value = object()
    replacement_value = object()

    definitions["Example"] = original_value

    assert definitions["Example"] is original_value
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["Example"] = replacement_value

    # A failed overwrite must preserve the original definition.
    assert definitions["Example"] is original_value
    assert len(definitions) == 1

# Generated at 2026-10-25 03:48:02.251034
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Person(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})
    assert repr(person) == "Person(name='Alice', age=30)"

    sparse_person = Person({"name": "Alice"})
    assert repr(sparse_person) == "Person(name='Alice') [sparse]"

# Generated at 2026-10-25 03:48:14.336776
# Unit test for method validate of class Reference
def test_Reference_validate():
    class TargetSchema(Schema):
        pass

    value = {"example": "value"}
    validated_value = TargetSchema()

    # Non-null values are delegated to the target schema.
    reference = Reference(to=TargetSchema)
    with patch.object(
        TargetSchema, "validate", return_value=validated_value
    ) as target_validate:
        result = reference.validate(value, strict=True)

    assert result is validated_value
    target_validate.assert_called_once_with(value, strict=True)

    # Null is accepted when explicitly allowed.
    nullable_reference = Reference(to=TargetSchema, allow_null=True)
    assert nullable_reference.validate(None) is None

    # Null is rejected otherwise.
    non_nullable_reference = Reference(to=TargetSchema, allow_null=False)
    with pytest.raises(ValidationError):
        non_nullable_reference.validate(None)

# Generated at 2026-10-25 03:48:15.770340
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

# Generated at 2026-10-25 03:48:17.221590
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

# Generated at 2026-10-25 03:48:34.105962
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String()
        age = Integer()

    class OtherPerson(Schema):
        name = String()
        age = Integer()

    person = Person(name="Alice", age=30)

    assert person == Person(name="Alice", age=30)
    assert person != Person(name="Bob", age=30)
    assert person != Person(name="Alice", age=31)

    # Instances of different schema classes are not equal, even when their
    # fields and values match.
    assert person != OtherPerson(name="Alice", age=30)

    # Non-Schema objects are not equal.
    assert person.__eq__({"name": "Alice", "age": 30}) is False
    assert person.__eq__(None) is False

# Generated at 2026-10-25 03:48:43.828161
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    instance = ExampleSchema({"name": "Alice", "age": 30})
    assert repr(instance) == "ExampleSchema(name='Alice', age=30)"

    sparse_instance = ExampleSchema({"name": "Alice"})
    assert repr(sparse_instance) == "ExampleSchema(name='Alice') [sparse]"

# Generated at 2026-10-25 03:48:46.370556
# Unit test for method validate of class Reference

# Generated at 2026-10-25 03:48:48.786525
# Unit test for method validate of class Reference

# Generated at 2026-10-25 03:48:51.202139
# Unit test for method validate of class Reference

# Generated at 2026-10-25 03:49:00.621912
# Unit test for constructor of class Reference

# Generated at 2026-10-25 03:49:06.561083
# Unit test for constructor of class Reference
def test_Reference():definitions = {"Schema": Schema}

# Generated at 2026-10-25 03:49:15.738815
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    assert len(ExampleSchema({})) == 0
    assert len(ExampleSchema({"first": 1})) == 1
    assert len(ExampleSchema({"first": 1, "second": 2})) == 2
    assert len(ExampleSchema({"first": 1, "second": 2, "third": 3})) == 3

    # Undeclared attributes are not included.
    instance = ExampleSchema({"first": 1})
    instance.extra = "ignored"
    assert len(instance) == 1

# Generated at 2026-10-25 03:49:26.349982
# Unit test for method validate of class Reference
def test_Reference_validate():
    class TargetSchema(Schema):
        pass

    reference = Reference(to=TargetSchema)

    value = {"example": "value"}
    with patch.object(
        TargetSchema, "validate", return_value=sentinel.validated
    ) as target_validate:
        result = reference.validate(value, strict=True)

    assert result is sentinel.validated
    target_validate.assert_called_once_with(value, strict=True)

    nullable_reference = Reference(to=TargetSchema, allow_null=True)
    assert nullable_reference.validate(None) is None

    with pytest.raises(ValidationError):
        reference.validate(None)

# Generated at 2026-10-25 03:49:33.084597
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    definitions["User"] = "first definition"

    assert definitions["User"] == "first definition"
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["User"] = "replacement definition"

    # A duplicate assignment must not replace the original definition.
    assert definitions["User"] == "first definition"
    assert len(definitions) == 1

# Generated at 2026-10-25 03:49:35.504113
# Unit test for constructor of class Schema

# Generated at 2026-10-25 03:49:38.039644
# Unit test for constructor of class Schema

# Generated at 2026-10-25 03:49:40.562208
# Unit test for constructor of class Schema

# Generated at 2026-10-25 03:49:42.972411
# Unit test for constructor of class Reference

# Generated at 2026-10-25 03:49:45.388197
# Unit test for constructor of class Reference

# Generated at 2026-10-25 03:49:47.803045
# Unit test for constructor of class Reference

# Generated at 2026-10-25 03:49:50.218548
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 03:49:52.636788
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 03:49:55.049561
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 03:49:57.464895
# Unit test for function set_definitions

# Generated at 2026-10-25 03:49:59.879927
# Unit test for function set_definitions

# Generated at 2026-10-25 03:50:02.295194
# Unit test for function set_definitions

# Generated at 2026-10-25 03:50:04.710253
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:50:07.126698
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:50:09.542318
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:50:11.956828
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 03:50:14.373454
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 03:50:16.787804
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 03:50:19.203119
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 03:50:21.618828
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 03:50:24.034233
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 03:50:39.847593
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class OtherSchema(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})
    identical_person = Person({"name": "Alice", "age": 30})
    different_name = Person({"name": "Bob", "age": 30})
    different_age = Person({"name": "Alice", "age": 31})
    other_schema = OtherSchema({"name": "Alice", "age": 30})

    assert person == person
    assert person == identical_person
    assert person != different_name
    assert person != different_age
    assert person != other_schema
    assert person != {"name": "Alice", "age": 30}
    assert person != object()

# Generated at 2026-10-25 03:51:00.271421
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        first = Object()
        second = Object()

    class OtherSchema(Schema):
        first = Object()
        second = Object()

    value = ExampleSchema({"first": {"id": 1}, "second": {"id": 2}})
    same_value = ExampleSchema({"first": {"id": 1}, "second": {"id": 2}})
    different_value = ExampleSchema({"first": {"id": 1}, "second": {"id": 3}})
    other_schema = OtherSchema({"first": {"id": 1}, "second": {"id": 2}})

    assert value == value
    assert value == same_value
    assert not value == different_value
    assert not value == other_schema
    assert not value == {"first": {"id": 1}, "second": {"id": 2}}
    assert not value == None  # noqa: E711

# Generated at 2026-10-25 03:51:02.823333
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:51:05.238815
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:51:07.656222
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:51:10.071798
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:51:12.487545
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:51:14.902435
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:51:17.318901
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:51:19.733615
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:51:22.149625
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:51:24.565803
# Unit test for constructor of class Schema

# Generated at 2026-10-25 03:51:26.981402
# Unit test for constructor of class Schema

# Generated at 2026-10-25 03:51:29.396933
# Unit test for constructor of class Schema

# Generated at 2026-10-25 03:51:31.812589
# Unit test for constructor of class Reference

# Generated at 2026-10-25 03:51:34.228206
# Unit test for constructor of class Reference

# Generated at 2026-10-25 03:51:36.646199
# Unit test for constructor of class Reference

# Generated at 2026-10-25 03:51:39.063095
# Unit test for method validate of class Reference

# Generated at 2026-10-25 03:51:41.480251
# Unit test for method validate of class Reference

# Generated at 2026-10-25 03:51:43.897059
# Unit test for method validate of class Reference

# Generated at 2026-10-25 03:51:46.313599
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 03:51:48.728716
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 03:51:51.143268
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 03:51:53.558342
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 03:51:55.972538
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 03:52:05.353224
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 03:52:08.131147
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 03:52:34.822531
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 03:52:44.985773
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:52:52.455834
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:53:02.650252
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():schema = Schema()

# Generated at 2026-10-25 03:53:04.034286
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

# Generated at 2026-10-25 03:53:20.054762
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:53:22.471994
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:53:24.892617
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 03:53:27.303549
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 03:53:29.718231
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 03:53:32.136590
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 03:53:34.549473
# Unit test for method validate of class Reference

# Generated at 2026-10-25 03:53:42.019694
# Unit test for method validate of class Reference

# Generated at 2026-10-25 03:54:26.675883
# Unit test for method validate of class Reference