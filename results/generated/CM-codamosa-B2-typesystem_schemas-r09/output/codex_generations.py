

# Generated at 2026-10-24 22:27:23.019753
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    empty = ExampleSchema()
    sparse = ExampleSchema({"first": "value"})
    complete = ExampleSchema({"first": "value", "second": None})

    assert len(empty) == 0
    assert len(sparse) == 1
    assert len(complete) == 2

# Generated at 2026-10-24 22:27:34.826983
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Full instance: "key=value!r" per field, in declaration order
    example = Example(name="Tom", age=23)
    assert repr(example) == "Example(name='Tom', age=23)"

    # Sparse instance: missing fields omitted, " [sparse]" appended
    sparse = Example({"name": "Tom"})
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Defaults count as populated â not sparse
    class WithDefault(Schema):
        name = String(default="nobody")

    assert repr(WithDefault()) == "WithDefault(name='nobody')"

    # Only declared fields appear â extra attributes are ignored
    example.extra = "ignored"
    assert repr(example) == "Example(name='Tom', age=23)"

# Generated at 2026-10-24 22:27:37.475840
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 22:27:39.996190
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 22:27:42.511024
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 22:27:44.927051
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-24 22:27:47.362057
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-24 22:27:49.779089
# Unit test for method __delitem__ of class SchemaDefinitions

# Generated at 2026-10-24 22:27:52.194870
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 22:27:54.612936
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 22:28:00.684882
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-24 22:28:12.612338
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    definitions = SchemaDefinitions()

    inherited_field = Field()
    base_schema = SchemaMetaclass(
        "BaseSchema",
        (Schema,),
        {
            "__module__": __name__,
            "inherited": inherited_field,
        },
    )

    # Create these in the opposite order from their insertion into attrs to
    # verify that fields are sorted by their creation counter.
    first_field = Field()
    second_field = Reference("TargetSchema")

    attrs = {
        "__module__": __name__,
        "second": second_field,
        "first": first_field,
    }

    schema = SchemaMetaclass(
        "ExampleSchema",
        (base_schema,),
        attrs,
        definitions=definitions,
    )

    assert list(schema.fields) == ["inherited", "first", "second"]
    assert schema.fields == {
        "inherited": inherited_field,
        "first": first_field,
        "second": second_field,
    }

    # Field declarations are removed from the class namespace.
    assert "first" not in schema.__dict__
    assert "second" not in schema.__dict__

    # Definitions are assigned to references and the new schema is registered.
    assert second_field.definitions is definitions
    assert definitions["ExampleSchema"] is schema

# Generated at 2026-10-24 22:28:21.421366
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    empty = ExampleSchema({})
    sparse = ExampleSchema({"first": "one"})
    full = ExampleSchema(
        {
            "first": "one",
            "second": "two",
            "third": "three",
        }
    )

    assert len(empty) == 0
    assert len(sparse) == 1
    assert len(full) == 3

# Generated at 2026-10-24 22:28:45.893919
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

# Generated at 2026-10-24 22:28:48.313025
# Unit test for method validate of class Reference

# Generated at 2026-10-24 22:28:50.730974
# Unit test for method validate of class Reference

# Generated at 2026-10-24 22:28:53.150300
# Unit test for method validate of class Reference

# Generated at 2026-10-24 22:28:59.597898
# Unit test for method __getitem__ of class SchemaDefinitions
def test_SchemaDefinitions___getitem__():
    # Returns the stored value for an existing key.
    definitions = SchemaDefinitions({"Person": "human", "Pet": "animal"})
    assert definitions["Person"] == "human"
    assert definitions["Pet"] == "animal"

    # Constructed via keyword arguments works too.
    definitions = SchemaDefinitions(A=1, B=2)
    assert definitions["A"] == 1
    assert definitions["B"] == 2

    # A key set via __setitem__ is retrievable.
    definitions = SchemaDefinitions()
    definitions["New"] = 42
    assert definitions["New"] == 42

    # A missing key raises KeyError.
    try:
        definitions["Missing"]
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError for missing key")

# Generated at 2026-10-24 22:29:10.574268
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    existing_definitions = SchemaDefinitions()

    direct_reference = Reference("Direct")
    array_reference = Reference("ArrayItem")
    tuple_references = (Reference("TupleItem1"), Reference("TupleItem2"))
    list_references = [Reference("ListItem")]
    existing_reference = Reference(
        "Existing",
        definitions=existing_definitions,
    )

    field = Object(
        properties={
            "direct": direct_reference,
            "nested_array": Array(
                items=Object(properties={"item": array_reference})
            ),
            "tuple_array": Array(items=tuple_references),
            "list_array": Array(items=list_references),
            "existing": existing_reference,
        }
    )

    module_0.set_definitions(field, definitions)

    assert direct_reference.definitions is definitions
    assert array_reference.definitions is definitions
    assert tuple_references[0].definitions is definitions
    assert tuple_references[1].definitions is definitions
    assert list_references[0].definitions is definitions

    # Existing definitions must not be overwritten.
    assert existing_reference.definitions is existing_definitions

# Generated at 2026-10-24 22:29:20.302828
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    empty = ExampleSchema({})
    sparse = ExampleSchema({"first": "one"})
    complete = ExampleSchema({"first": "one", "second": "two"})

    assert len(empty) == 0
    assert len(sparse) == 1
    assert len(complete) == 2

    # Attributes not declared as schema fields are not counted.
    sparse.extra = "ignored"
    assert len(sparse) == 1

# Generated at 2026-10-24 22:29:30.335295
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    existing_definitions = SchemaDefinitions()

    direct_reference = Reference("Direct")
    single_item_reference = Reference("SingleItem")
    tuple_item_reference = Reference("TupleItem")
    list_item_reference = Reference("ListItem")
    existing_reference = Reference(
        "Existing",
        definitions=existing_definitions,
    )

    field = Object(
        properties={
            "direct": direct_reference,
            "single_array": Array(items=single_item_reference),
            "tuple_array": Array(items=(tuple_item_reference,)),
            "list_array": Array(items=[list_item_reference]),
            "existing": existing_reference,
            "empty_array": Array(items=None),
        }
    )

    module_0.set_definitions(field, definitions)

    assert direct_reference.definitions is definitions
    assert single_item_reference.definitions is definitions
    assert tuple_item_reference.definitions is definitions
    assert list_item_reference.definitions is definitions

    # Existing definitions must not be overwritten.
    assert existing_reference.definitions is existing_definitions

# Generated at 2026-10-24 22:29:53.272914
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.fields import Integer, String

    class ExampleSchema(Schema):
        name = String()
        age = Integer()

    class OtherSchema(Schema):
        name = String()
        age = Integer()

    # Same class, same field values -> equal
    a = ExampleSchema({"name": "Alice", "age": 30})
    b = ExampleSchema({"name": "Alice", "age": 30})
    assert a == b
    assert not (a != b)

    # Same class, one differing value -> not equal
    c = ExampleSchema({"name": "Bob", "age": 30})
    assert not (a == c)

    # Same field values, different class -> not equal
    d = OtherSchema({"name": "Alice", "age": 30})
    assert not (a == d)
    assert not (d == a)

    # Non-Schema object -> not equal (no exception)
    assert not (a == {"name": "Alice", "age": 30})
    assert not (a == None)
    assert not (a == "Alice")

    # Keyword construction produces the same equality result
    e = ExampleSchema(name="Alice", age=30)
    assert a == e

    # Reflexivity
    assert a == a

# Generated at 2026-10-24 22:29:55.692701
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 22:29:58.111196
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 22:30:06.685743
# Unit test for method __len__ of class Schema
def test_Schema___len__():from typesystem.fields import String


# Generated at 2026-10-24 22:30:17.439171
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem import Schema, String

    class ExampleSchema(Schema):
        name = String()

    # 1. Constructor with a Schema class target
    ref = Reference(to=ExampleSchema)
    assert ref.to is ExampleSchema
    assert ref.definitions is None
    assert ref._target is ExampleSchema
    assert not hasattr(ref, "_target_string")

    # 2. target_string is derived from the class name
    assert ref.target_string == "ExampleSchema"
    assert hasattr(ref, "_target_string")  # cached after first access

    # 3. Constructor with a string target
    ref = Reference(to="ExampleSchema")
    assert ref.to == "ExampleSchema"
    assert ref._target_string == "ExampleSchema"
    assert not hasattr(ref, "_target")

    # 4. String target without definitions -> .target raises AssertionError
    try:
        ref.target
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected AssertionError for missing definitions")

    # 5. String target with definitions -> .target resolves lazily
    definitions = {"ExampleSchema": ExampleSchema}
    ref = Reference(to="ExampleSchema", definitions=definitions)
    assert ref.definitions is definitions
    assert ref._target is ExampleSchema  # resolved via definitions
    assert ref.target is ExampleSchema

    # 6. Extra Field kwargs are forwarded to the base class
    ref = Reference(to=ExampleSchema, allow_null=True)
    assert ref.allow_null is True

    # 7. Invalid target type -> AssertionError from issubclass
    try:
        Reference(to=123)
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected AssertionError for non-Schema target")

    # 8. validate() uses the resolved target
    ref = Reference(to=ExampleSchema)
    assert ref.validate({"name": "tom"}) == {"name": "tom"}

    # 9. validate() with allow_null
    ref = Reference(to=ExampleSchema, allow_null=True)
    assert ref.validate(None) is None

    # 10. validate() without allow_null rejects None
    ref = Reference(to=ExampleSchema)
    try:
        ref.validate(None)
    except ValidationError:
        pass
    else:
        raise AssertionError("Expected ValidationError for None value")

    # 11. serialize()
    assert ref.serialize(None) is None
    assert ref.serialize({"name": "tom"}) == {"name": "tom"}

# Generated at 2026-10-24 22:30:18.771330
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Full instance: "key=value!r" per field, in declaration order
    example = Example(name="Tom", age=23)
    assert repr(example) == "Example(name='Tom', age=23)"

    # Sparse instance: missing fields omitted, " [sparse]" appended
    sparse = Example({"name": "Tom"})
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Defaults count as populated â not sparse
    class WithDefault(Schema):
        name = String(default="nobody")

    assert repr(WithDefault()) == "WithDefault(name='nobody')"

    # Only declared fields appear â extra attributes are ignored
    example.extra = "ignored"
    assert repr(example) == "Example(name='Tom', age=23)"

# Generated at 2026-10-24 22:30:28.600260
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    schema = ExampleSchema({"first": 1, "third": 3})

    iterator = iter(schema)

    assert iter(iterator) is iterator
    assert list(iterator) == ["first", "third"]
    assert list(ExampleSchema({})) == []

# Generated at 2026-10-24 22:30:29.926603
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Full instance: "key=value!r" per field, in declaration order
    example = Example(name="Tom", age=23)
    assert repr(example) == "Example(name='Tom', age=23)"

    # Sparse instance: missing fields omitted, " [sparse]" appended
    sparse = Example({"name": "Tom"})
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Defaults count as populated â not sparse
    class WithDefault(Schema):
        name = String(default="nobody")

    assert repr(WithDefault()) == "WithDefault(name='nobody')"

    # Only declared fields appear â extra attributes are ignored
    example.extra = "ignored"
    assert repr(example) == "Example(name='Tom', age=23)"

# Generated at 2026-10-24 22:30:41.400555
# Unit test for constructor of class Reference
def test_Reference():
    class Example(Schema):
        pass

    # 1. Constructing with a Schema class stores the target directly.
    ref = Reference(to=Example)
    assert ref._target is Example
    assert ref.target is Example
    assert ref.target_string == "Example"
    assert ref.definitions is None

    # 2. Constructing with a string stores the name and resolves lazily.
    ref = Reference(to="Example")
    assert ref._target_string == "Example"
    assert not hasattr(ref, "_target")
    assert ref.target_string == "Example"

    # 3. String reference without definitions raises AssertionError on access.
    ref = Reference(to="Example")
    try:
        ref.target
        assert False, "Expected AssertionError for missing definitions."
    except AssertionError:
        pass

    # 4. String reference with definitions resolves the target.
    definitions = SchemaDefinitions({"Example": Example})
    ref = Reference(to="Example", definitions=definitions)
    assert ref.definitions is definitions
    assert ref.target is Example
    assert ref.target_string == "Example"

    # 5. definitions is stored even when `to` is a class.
    ref = Reference(to=Example, definitions=definitions)
    assert ref.definitions is definitions
    assert ref.target is Example

    # 6. Field kwargs (e.g. allow_null) are forwarded to the base Field.
    ref = Reference(to=Example, allow_null=True)
    assert ref.allow_null is True

    # 7. Null handling respects allow_null.
    assert ref.validate(None) is None

    strict_ref = Reference(to=Example)
    try:
        strict_ref.validate(None)
        assert False, "Expected ValidationError for null without allow_null."
    except ValidationError:
        pass

    # 8. Non-str, non-Schema `to` raises AssertionError.
    for bad_target in (123, ["Example"], {"Example": Example}):
        try:
            Reference(to=bad_target)
            assert False, f"Expected AssertionError for to={bad_target!r}."
        except AssertionError:
            pass

# Generated at 2026-10-24 22:32:04.352268
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()


# Generated at 2026-10-24 22:32:20.837661
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

# Generated at 2026-10-24 22:32:30.662452
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    assert len(ExampleSchema()) == 0
    assert len(ExampleSchema({"first": "one"})) == 1
    assert len(ExampleSchema({"first": "one", "second": "two"})) == 2

    schema = ExampleSchema({"first": "one"})
    schema.unrelated = "ignored"
    assert len(schema) == 1

# Generated at 2026-10-24 22:33:45.622763
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    definitions = SchemaDefinitions()

    inherited_field = Field()
    overridden_field = Field()

    class Parent(Schema):
        inherited = inherited_field
        overridden = overridden_field

    class Target(Schema, definitions=definitions):
        value = Field()

    own_field = Field()
    replacement_field = Field()
    reference_field = Reference("Target")

    class Child(Parent, definitions=definitions):
        own = own_field
        overridden = replacement_field
        target = reference_field

    # Field attributes are removed from the class namespace and collected.
    assert "own" not in Child.__dict__
    assert "target" not in Child.__dict__

    # Parent fields are inherited, while child declarations override them.
    assert Child.fields["inherited"] is inherited_field
    assert Child.fields["overridden"] is replacement_field
    assert overridden_field not in Child.fields.values()

    # Fields retain their source-code creation order.
    assert list(Child.fields) == ["inherited", "own", "overridden", "target"]

    # Definitions are registered and applied to string references.
    assert definitions["Target"] is Target
    assert definitions["Child"] is Child
    assert reference_field.definitions is definitions
    assert reference_field.target is Target

# Generated at 2026-10-24 22:34:02.310451
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

# Generated at 2026-10-24 22:34:26.180762
# Unit test for method validate of class Reference

# Generated at 2026-10-24 22:34:42.758570
# Unit test for method validate of class Reference
def test_Reference_validate():
    import pytest
    from typesystem.fields import Integer

    class Target(Schema):
        x = Integer()

    ref = Reference(to=Target)
    value = ref.validate({"x": 1})
    assert isinstance(value, Target)
    assert value["x"] == 1
    assert value.x == 1

    assert Reference(to=Target, allow_null=True).validate(None) is None

    with pytest.raises(ValidationError) as exc_info:
        ref.validate(None)
    assert exc_info.value.messages()[0].text == "May not be null."

    definitions = SchemaDefinitions({"Target": Target})
    string_ref = Reference(to="Target", definitions=definitions)
    assert string_ref.target is Target
    resolved = string_ref.validate({"x": 2})
    assert isinstance(resolved, Target)
    assert resolved["x"] == 2

# Generated at 2026-10-24 22:34:56.116621
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    empty = ExampleSchema({})
    assert len(empty) == 0

    partial = ExampleSchema({"first": "one"})
    assert len(partial) == 1

    partial.second = "two"
    assert len(partial) == 2

    # Attributes not declared as fields must not affect the length.
    partial.extra = "ignored"
    assert len(partial) == 2

    complete = ExampleSchema(
        {"first": "one", "second": "two", "third": "three"}
    )
    assert len(complete) == 3

# Generated at 2026-10-24 22:35:12.557065
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

# Generated at 2026-10-24 22:35:13.989157
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Full instance: "key=value!r" per field, in declaration order
    example = Example(name="Tom", age=23)
    assert repr(example) == "Example(name='Tom', age=23)"

    # Sparse instance: missing fields omitted, " [sparse]" appended
    sparse = Example({"name": "Tom"})
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Defaults count as populated â not sparse
    class WithDefault(Schema):
        name = String(default="nobody")

    assert repr(WithDefault()) == "WithDefault(name='nobody')"

    # Only declared fields appear â extra attributes are ignored
    example.extra = "ignored"
    assert repr(example) == "Example(name='Tom', age=23)"

# Generated at 2026-10-24 22:35:29.656955
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    class User(Schema):
        name = String()

    user = User(name="Ada Lovelace")
    reference = Reference(User)

    assert reference.serialize(user) == {"name": "Ada Lovelace"}

# Generated at 2026-10-24 22:35:30.983611
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Full instance: "key=value!r" per field, in declaration order
    example = Example(name="Tom", age=23)
    assert repr(example) == "Example(name='Tom', age=23)"

    # Sparse instance: missing fields omitted, " [sparse]" appended
    sparse = Example({"name": "Tom"})
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Defaults count as populated â not sparse
    class WithDefault(Schema):
        name = String(default="nobody")

    assert repr(WithDefault()) == "WithDefault(name='nobody')"

    # Only declared fields appear â extra attributes are ignored
    example.extra = "ignored"
    assert repr(example) == "Example(name='Tom', age=23)"

# Generated at 2026-10-24 22:35:32.306425
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.fields import Integer, String

    class ExampleSchema(Schema):
        name = String()
        age = Integer()

    class OtherSchema(Schema):
        name = String()
        age = Integer()

    # Same class, same field values -> equal
    a = ExampleSchema({"name": "Alice", "age": 30})
    b = ExampleSchema({"name": "Alice", "age": 30})
    assert a == b
    assert not (a != b)

    # Same class, one differing value -> not equal
    c = ExampleSchema({"name": "Bob", "age": 30})
    assert not (a == c)

    # Same field values, different class -> not equal
    d = OtherSchema({"name": "Alice", "age": 30})
    assert not (a == d)
    assert not (d == a)

    # Non-Schema object -> not equal (no exception)
    assert not (a == {"name": "Alice", "age": 30})
    assert not (a == None)
    assert not (a == "Alice")

    # Keyword construction produces the same equality result
    e = ExampleSchema(name="Alice", age=30)
    assert a == e

    # Reflexivity
    assert a == a

# Generated at 2026-10-24 22:35:59.063988
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    class DummyField(Field):
        def validate(
            self, value: typing.Any, *, strict: bool = False
        ) -> typing.Any:
            return value

    # Fields are removed from the class namespace and sorted by creation order.
    first_created = DummyField()
    second_created = DummyField()

    class OrderedSchema(Schema):
        second = second_created
        first = first_created

    assert list(OrderedSchema.fields) == ["first", "second"]
    assert OrderedSchema.fields["first"] is first_created
    assert OrderedSchema.fields["second"] is second_created
    assert "first" not in OrderedSchema.__dict__
    assert "second" not in OrderedSchema.__dict__

    # Inherited fields are included, while child declarations override fields
    # with the same name.
    inherited_field = DummyField()
    base_override = DummyField()

    class BaseSchema(Schema):
        inherited = inherited_field
        overridden = base_override

    child_override = DummyField()
    child_field = DummyField()

    class ChildSchema(BaseSchema):
        overridden = child_override
        child = child_field

    assert ChildSchema.fields["inherited"] is inherited_field
    assert ChildSchema.fields["overridden"] is child_override
    assert ChildSchema.fields["child"] is child_field

    # Definitions are registered and propagated through nested fields.
    definitions = SchemaDefinitions()

    class TargetSchema(Schema, definitions=definitions):
        pass

    direct_reference = Reference("TargetSchema")
    array_reference = Reference("TargetSchema")
    object_reference = Reference("TargetSchema")

    existing_definitions = {"TargetSchema": TargetSchema}
    configured_reference = Reference(
        "TargetSchema", definitions=existing_definitions
    )

    class ReferencingSchema(Schema, definitions=definitions):
        direct = direct_reference
        array = Array(items=array_reference)
        object_field = Object(properties={"target": object_reference})
        configured = configured_reference

    assert definitions["TargetSchema"] is TargetSchema
    assert definitions["ReferencingSchema"] is ReferencingSchema

    assert direct_reference.definitions is definitions
    assert array_reference.definitions is definitions
    assert object_reference.definitions is definitions

    # Existing reference definitions must not be replaced

# Generated at 2026-10-24 22:36:00.480478
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Full instance: "key=value!r" per field, in declaration order
    example = Example(name="Tom", age=23)
    assert repr(example) == "Example(name='Tom', age=23)"

    # Sparse instance: missing fields omitted, " [sparse]" appended
    sparse = Example({"name": "Tom"})
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Defaults count as populated â not sparse
    class WithDefault(Schema):
        name = String(default="nobody")

    assert repr(WithDefault()) == "WithDefault(name='nobody')"

    # Only declared fields appear â extra attributes are ignored
    example.extra = "ignored"
    assert repr(example) == "Example(name='Tom', age=23)"

# Generated at 2026-10-24 22:36:46.479441
# Unit test for method validate of class Reference

# Generated at 2026-10-24 22:36:47.808424
# Unit test for method validate of class Reference
def test_Reference_validate():
    import pytest
    from typesystem.fields import Integer

    class Target(Schema):
        x = Integer()

    ref = Reference(to=Target)
    value = ref.validate({"x": 1})
    assert isinstance(value, Target)
    assert value["x"] == 1
    assert value.x == 1

    assert Reference(to=Target, allow_null=True).validate(None) is None

    with pytest.raises(ValidationError) as exc_info:
        ref.validate(None)
    assert exc_info.value.messages()[0].text == "May not be null."

    definitions = SchemaDefinitions({"Target": Target})
    string_ref = Reference(to="Target", definitions=definitions)
    assert string_ref.target is Target
    resolved = string_ref.validate({"x": 2})
    assert isinstance(resolved, Target)
    assert resolved["x"] == 2

# Generated at 2026-10-24 22:36:59.155837
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

    del schema.second
    assert len(schema) == 0

# Generated at 2026-10-24 22:37:00.541600
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Full instance: "key=value!r" per field, in declaration order
    example = Example(name="Tom", age=23)
    assert repr(example) == "Example(name='Tom', age=23)"

    # Sparse instance: missing fields omitted, " [sparse]" appended
    sparse = Example({"name": "Tom"})
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Defaults count as populated â not sparse
    class WithDefault(Schema):
        name = String(default="nobody")

    assert repr(WithDefault()) == "WithDefault(name='nobody')"

    # Only declared fields appear â extra attributes are ignored
    example.extra = "ignored"
    assert repr(example) == "Example(name='Tom', age=23)"