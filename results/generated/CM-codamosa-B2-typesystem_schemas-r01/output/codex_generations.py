

# Generated at 2026-10-25 04:35:40.721303
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:35:57.176885
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 04:36:07.183694
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    assert len(ExampleSchema({})) == 0
    assert len(ExampleSchema({"first": "one"})) == 1
    assert len(ExampleSchema({"first": "one", "third": "three"})) == 2
    assert len(
        ExampleSchema({"first": "one", "second": "two", "third": "three"})
    ) == 3

# Generated at 2026-10-25 04:36:09.819470
# Unit test for method __getitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:36:12.362240
# Unit test for method __getitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:36:14.778632
# Unit test for method __getitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:36:17.194632
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:36:19.616268
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:36:22.027664
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:36:30.906924
# Unit test for method serialize of class Reference
def test_Reference_serialize():reference = Reference(to="ExampleSchema")

# Generated at 2026-10-25 04:36:51.124264
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        name = String()
        count = Integer(default=0)

    instance = ExampleSchema(name="example", count=3)
    assert repr(instance) == "ExampleSchema(name='example', count=3)"

    sparse_instance = ExampleSchema({"name": "example"})
    assert repr(sparse_instance) == "ExampleSchema(name='example') [sparse]"

# Generated at 2026-10-25 04:37:00.701036
# Unit test for constructor of class Reference
def test_Reference():
    class User(Schema):
        pass

    definitions = SchemaDefinitions({"User": User})

    # String-based references are resolved through definitions.
    reference = Reference(
        to="User",
        definitions=definitions,
        allow_null=True,
    )

    assert reference.to == "User"
    assert reference.definitions is definitions
    assert reference.target_string == "User"
    assert reference.target is User
    assert reference.allow_null is True

    # Schema classes can also be referenced directly.
    direct_reference = Reference(to=User)

    assert direct_reference.to is User
    assert direct_reference.definitions is None
    assert direct_reference.target is User
    assert direct_reference.target_string == "User"

# Generated at 2026-10-25 04:37:02.170208
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

# Generated at 2026-10-25 04:37:12.912247
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class OtherPerson(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})

    assert person == Person({"name": "Alice", "age": 30})
    assert person != Person({"name": "Alice", "age": 31})
    assert person != OtherPerson({"name": "Alice", "age": 30})
    assert person != {"name": "Alice", "age": 30}

# Generated at 2026-10-25 04:37:15.438888
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:37:17.971532
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:37:20.386472
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:37:22.907704
# Unit test for function set_definitions

# Generated at 2026-10-25 04:37:43.867504
# Unit test for function set_definitions
def test_set_definitions():definitions = SchemaDefinitions()

# Generated at 2026-10-25 04:37:45.281429
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

# Generated at 2026-10-25 04:37:55.211776
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        name = Field()
        count = Field()

    instance = ExampleSchema({"name": "example", "count": 3})
    assert repr(instance) == "ExampleSchema(name='example', count=3)"

    sparse_instance = ExampleSchema({"name": "example"})
    assert repr(sparse_instance) == "ExampleSchema(name='example') [sparse]"

# Generated at 2026-10-25 04:38:05.561354
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class Company(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})

    assert person == Person({"name": "Alice", "age": 30})
    assert person != Person({"name": "Alice", "age": 31})
    assert person != Person({"name": "Bob", "age": 30})
    assert person != Company({"name": "Alice", "age": 30})
    assert person != {"name": "Alice", "age": 30}

# Generated at 2026-10-25 04:38:23.682423
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    class OtherSchema(Schema):
        name = Field()
        age = Field()

    schema = ExampleSchema({"name": "Alice", "age": 30})
    identical = ExampleSchema({"name": "Alice", "age": 30})
    different_name = ExampleSchema({"name": "Bob", "age": 30})
    different_age = ExampleSchema({"name": "Alice", "age": 31})
    different_type = OtherSchema({"name": "Alice", "age": 30})

    assert schema == schema
    assert schema == identical
    assert not (schema == different_name)
    assert not (schema == different_age)
    assert not (schema == different_type)
    assert not (schema == {"name": "Alice", "age": 30})
    assert not (schema == None)  # noqa: E711

# Generated at 2026-10-25 04:38:26.097799
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:38:45.799624
# Unit test for constructor of class Schema
def test_Schema():from typesystem.fields import Integer, String

# Generated at 2026-10-25 04:38:58.756712
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:39:05.869120
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:39:12.937007
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:39:23.278281
# Unit test for constructor of class Reference
def test_Reference():
    class User(Schema):
        pass

    # Reference using a schema class.
    reference = Reference(User, allow_null=True)

    assert reference.to is User
    assert reference.definitions is None
    assert reference.target is User
    assert reference.target_string == "User"
    assert reference.allow_null is True

    # Reference using a string and definitions mapping.
    definitions = SchemaDefinitions({"User": User})
    reference = Reference("User", definitions=definitions)

    assert reference.to == "User"
    assert reference.definitions is definitions
    assert reference.target_string == "User"
    assert reference.target is User
    assert reference.allow_null is False

# Generated at 2026-10-25 04:39:25.923504
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:39:28.339514
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:39:34.841768
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:39:45.910279
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    schema = ExampleSchema({"first": "value"})

    assert len(schema) == 1

    schema.second = "another value"
    assert len(schema) == 2

    del schema.first
    assert len(schema) == 1

    # Attributes that are not declared fields should not be counted.
    schema.extra = "ignored"
    assert len(schema) == 1

# Generated at 2026-10-25 04:40:11.611658
# Unit test for constructor of class Schema
def test_Schema():sentinel = object()


# Generated at 2026-10-25 04:40:27.996567
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    original = ExampleSchema({"name": "Alice", "age": 30})
    identical = ExampleSchema({"name": "Alice", "age": 30})
    different_name = ExampleSchema({"name": "Bob", "age": 30})
    different_age = ExampleSchema({"name": "Alice", "age": 31})

    assert original == original
    assert original == identical
    assert identical == original

    assert original != different_name
    assert original != different_age
    assert original != {"name": "Alice", "age": 30}
    assert original != object()

# Generated at 2026-10-25 04:40:38.748733
# Unit test for method validate of class Reference
def test_Reference_validate():
    target = Mock()
    validated_value = object()
    target.validate.return_value = validated_value

    reference = Reference(
        to="Target",
        definitions={"Target": target},
    )
    value = {"name": "example"}

    # Non-null values are validated by the target, preserving strict mode.
    result = reference.validate(value, strict=True)

    assert result is validated_value
    target.validate.assert_called_once_with(value, strict=True)

    # Null is accepted without invoking the target when allow_null=True.
    target.reset_mock()
    nullable_reference = Reference(
        to="Target",
        definitions={"Target": target},
        allow_null=True,
    )

    assert nullable_reference.validate(None) is None
    target.validate.assert_not_called()

    # Null raises a validation error by default.
    non_nullable_reference = Reference(
        to="Target",
        definitions={"Target": target},
    )

    with pytest.raises(ValidationError):
        non_nullable_reference.validate(None)

    target.validate.assert_not_called()

# Generated at 2026-10-25 04:40:40.185955
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

# Generated at 2026-10-25 04:40:48.373242
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()
    replacement = object()

    definitions["Example"] = original

    assert definitions["Example"] is original
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["Example"] = replacement

    # A duplicate assignment must not replace the original definition.
    assert definitions["Example"] is original
    assert len(definitions) == 1

# Generated at 2026-10-25 04:41:04.351656
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
    assert person != Person({"name": "Bob", "age": 30})
    assert person != Person({"name": "Alice", "age": 31})

    # Values from another schema class are not equal.
    assert person != OtherSchema({"name": "Alice", "age": 30})

    # Non-schema values are not equal.
    assert person != {"name": "Alice", "age": 30}
    assert person != object()

# Generated at 2026-10-25 04:41:12.027416
# Unit test for constructor of class Reference
def test_Reference():
    class User(Schema):
        pass

    definitions = SchemaDefinitions({"User": User})

    # Reference using a Schema class directly.
    direct_reference = Reference(User, allow_null=True)

    assert direct_reference.to is User
    assert direct_reference.definitions is None
    assert direct_reference.target is User
    assert direct_reference.target_string == "User"
    assert direct_reference.allow_null is True

    # Reference using a string and definitions mapping.
    string_reference = Reference("User", definitions=definitions)

    assert string_reference.to == "User"
    assert string_reference.definitions is definitions
    assert string_reference.target_string == "User"
    assert string_reference.target is User

# Generated at 2026-10-25 04:41:13.359377
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

# Generated at 2026-10-25 04:41:22.184004
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        name = Field()
        count = Field()

    instance = ExampleSchema({"name": "example", "count": 3})
    assert repr(instance) == "ExampleSchema(name='example', count=3)"

    sparse_instance = ExampleSchema({"name": "example"})
    assert repr(sparse_instance) == "ExampleSchema(name='example') [sparse]"

# Generated at 2026-10-25 04:41:24.601304
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:41:27.016845
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:41:29.431554
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:41:38.243648
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:41:45.820512
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:41:52.783030
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:42:04.764152
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Person(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})
    assert repr(person) == "Person(name='Alice', age=30)"

    sparse_person = Person({"name": "Alice"})
    assert repr(sparse_person) == "Person(name='Alice') [sparse]"

# Generated at 2026-10-25 04:42:07.299927
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:42:09.937246
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:42:12.462692
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:42:14.875684
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:42:17.290296
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:42:19.856585
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 04:42:22.393533
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:42:24.809142
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:42:27.223167
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 04:42:29.641710
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:42:32.057190
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:42:34.469607
# Unit test for method validate of class Reference

# Generated at 2026-10-25 04:42:36.883342
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:42:39.503563
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:42:50.127247
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:43:07.332389
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    class OtherSchema(Schema):
        name = Field()
        age = Field()

    first = ExampleSchema({"name": "Alice", "age": 30})
    identical = ExampleSchema({"name": "Alice", "age": 30})
    different_value = ExampleSchema({"name": "Alice", "age": 31})
    different_class = OtherSchema({"name": "Alice", "age": 30})

    assert first == first
    assert first == identical
    assert identical == first

    assert first != different_value
    assert first != different_class
    assert first != {"name": "Alice", "age": 30}
    assert first != object()

# Generated at 2026-10-25 04:43:23.202929
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Person(Schema):
        name = Field()
        age = Field()

    class OtherSchema(Schema):
        name = Field()
        age = Field()

    person = Person({"name": "Alice", "age": 30})

    assert person == Person({"name": "Alice", "age": 30})
    assert person != Person({"name": "Bob", "age": 30})
    assert person != Person({"name": "Alice", "age": 31})
    assert person != OtherSchema({"name": "Alice", "age": 30})
    assert person != {"name": "Alice", "age": 30}

# Generated at 2026-10-25 04:43:24.537064
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

# Generated at 2026-10-25 04:43:32.931125
# Unit test for constructor of class Reference
def test_Reference():
    class User(Schema):
        pass

    definitions = {"User": User}

    # String-based reference.
    reference = Reference(
        to="User",
        definitions=definitions,
        allow_null=True,
    )

    assert reference.to == "User"
    assert reference.definitions is definitions
    assert reference.allow_null is True
    assert reference.target_string == "User"
    assert reference.target is User

    # Direct schema reference.
    direct_reference = Reference(to=User)

    assert direct_reference.to is User
    assert direct_reference.definitions is None
    assert direct_reference.target is User
    assert direct_reference.target_string == "User"

# Generated at 2026-10-25 04:43:35.459894
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:43:37.875693
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:43:40.519810
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 04:44:02.219538
# Unit test for constructor of class Schema
def test_Schema():import pytest

# Generated at 2026-10-25 04:44:19.012318
# Unit test for method validate of class Reference
def test_Reference_validate():
    import pytest

    calls = []
    validated_value = object()

    class TargetSchema(Schema):
        @classmethod
        def module_0.validate(cls, value, *, strict=False):
            calls.append((value, strict))
            return validated_value

    # Non-null values are delegated to the referenced schema.
    reference = Reference(TargetSchema)
    value = {"name": "example"}

    assert reference.validate(value, strict=True) is validated_value
    assert calls == [(value, True)]

    # Null is accepted without delegation when allow_null=True.
    nullable_reference = Reference(TargetSchema, allow_null=True)

    assert nullable_reference.validate(None) is None
    assert calls == [(value, True)]

    # Null is rejected when allow_null=False.
    with pytest.raises(ValidationError) as exc_info:
        reference.validate(None)

    assert [message.text for message in exc_info.value.messages()] == [
        "May not be null."
    ]
    assert calls == [(value, True)]

# Generated at 2026-10-25 04:44:20.364985
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

# Generated at 2026-10-25 04:44:25.059276
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:44:27.475649
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:44:30.007250
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:44:32.422634
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:44:34.837108
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:44:37.251606
# Unit test for constructor of class Reference

# Generated at 2026-10-25 04:44:39.667478
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 04:44:56.064402
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 04:45:07.956447
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:17.687446
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:23.831928
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 04:45:34.648125
# Unit test for method validate of class Reference
def test_Reference_validate():
    target = Mock()
    target.validate.return_value = sentinel.validated

    reference = Reference(
        to="Target",
        definitions={"Target": target},
    )

    result = reference.validate(sentinel.input, strict=True)

    assert result is sentinel.validated
    target.validate.assert_called_once_with(sentinel.input, strict=True)

    nullable_target = Mock()
    nullable_reference = Reference(
        to="Target",
        definitions={"Target": nullable_target},
        allow_null=True,
    )

    assert nullable_reference.validate(None) is None
    nullable_target.validate.assert_not_called()

    non_nullable_reference = Reference(
        to="Target",
        definitions={"Target": Mock()},
    )

    with pytest.raises(ValidationError):
        non_nullable_reference.validate(None)

# Generated at 2026-10-25 04:45:37.077216
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:45:39.489888
# Unit test for constructor of class Schema

# Generated at 2026-10-25 04:45:50.144974
# Unit test for constructor of class Schema