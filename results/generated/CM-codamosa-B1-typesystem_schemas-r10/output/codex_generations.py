

# Generated at 2026-10-24 22:55:46.071911
# Unit test for method __len__ of class SchemaDefinitions
def test_SchemaDefinitions___len__():
    # Empty mapping
    definitions = SchemaDefinitions()
    assert len(definitions) == 0

    # Grows with each set
    definitions["foo"] = object()
    assert len(definitions) == 1

    definitions["bar"] = object()
    assert len(definitions) == 2

    # Shrinks on delete
    del definitions["bar"]
    assert len(definitions) == 1

    # Reflects constructor-supplied contents
    assert len(SchemaDefinitions({"a": 1, "b": 2})) == 2
    assert len(SchemaDefinitions(a=1)) == 1

# Generated at 2026-10-24 22:56:03.782509
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = String()
        age = Integer()
        nickname = String(default="anonymous")

    # Keyword arguments are validated and defaults are applied.
    person = Person(name="Alice", age=30)

    assert person.name == "Alice"
    assert person.age == 30
    assert person.nickname == "anonymous"
    assert not person.is_sparse
    assert dict(person) == {
        "name": "Alice",
        "age": 30,
        "nickname": "anonymous",
    }

    # A single dictionary argument populates matching fields.
    from_dict = Person({"name": "Bob", "age": 25, "nickname": "Bobby"})

    assert from_dict.name == "Bob"
    assert from_dict.age == 25
    assert from_dict.nickname == "Bobby"

    # A single object argument copies matching attributes.
    source = SimpleNamespace(name="Carol", age=40, nickname="Caz")
    from_object = Person(source)

    assert from_object.name == "Carol"
    assert from_object.age == 40
    assert from_object.nickname == "Caz"

    # Missing fields in positional input produce a sparse schema.
    sparse = Person({"name": "Dave"})

    assert sparse.name == "Dave"
    assert sparse.is_sparse
    assert dict(sparse) == {"name": "Dave"}

    # Invalid field values are reported as constructor errors.
    with pytest.raises(TypeError, match="Invalid argument 'age'"):
        Person(name="Eve", age=None)

    # Unknown keyword arguments are rejected.
    with pytest.raises(
        TypeError,
        match="'unknown' is an invalid keyword argument for Person",
    ):
        Person(name="Frank", age=20, unknown=True)

    # Only one positional argument is accepted, and it cannot be combined
    # with keyword arguments.
    with pytest.raises(AssertionError):
        Person({"name": "Grace"}, {"age": 35})

    with pytest.raises(AssertionError):
        Person({"name": "Grace"}, age=35)

# Generated at 2026-10-24 22:56:10.238761
# Unit test for method __getitem__ of class SchemaDefinitions
def test_SchemaDefinitions___getitem__():
    definitions = SchemaDefinitions({"Example": "value"})

    # Existing key returns the stored value
    assert definitions["Example"] == "value"

    # Missing key raises KeyError
    try:
        definitions["Missing"]
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError for missing definition")

# Generated at 2026-10-24 22:56:18.140783
# Unit test for constructor of class SchemaDefinitions
def test_SchemaDefinitions():
    source = {"User": object()}
    definitions = SchemaDefinitions(source, Address="address-schema")

    assert len(definitions) == 2
    assert definitions["User"] is source["User"]
    assert definitions["Address"] == "address-schema"
    assert dict(definitions) == {
        "User": source["User"],
        "Address": "address-schema",
    }

    # Ensure the constructor creates its own dictionary.
    source["Order"] = object()
    assert "Order" not in definitions

    # The empty constructor should also be supported.
    assert dict(SchemaDefinitions()) == {}

# Generated at 2026-10-24 22:56:35.022536
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = String()
        age = Integer(default=18)

    # Keyword arguments are validated and defaults are applied.
    person = Person(name="Alice")
    assert person.name == "Alice"
    assert person.age == 18
    assert not person.is_sparse

    # Explicit values override defaults.
    person = Person(name="Bob", age=30)
    assert person.name == "Bob"
    assert person.age == 30

    # A single mapping may be used as the source.
    person = Person({"name": "Carol", "age": 25, "unknown": "ignored"})
    assert person.name == "Carol"
    assert person.age == 25
    assert not hasattr(person, "unknown")

    # An object's attributes may also be used as the source.
    source = SimpleNamespace(name="Dave", age=40)
    person = Person(source)
    assert person.name == "Dave"
    assert person.age == 40

    # Positional construction does not populate missing defaults.
    person = Person({"name": "Eve"})
    assert person.name == "Eve"
    assert not hasattr(person, "age")
    assert person.is_sparse

    # Invalid field values produce a useful TypeError.
    with pytest.raises(
        TypeError,
        match=r"^Invalid argument 'age' for Person\(\)\.",
    ):
        Person(name="Frank", age="not-an-integer")

    # Unknown keyword arguments are rejected.
    with pytest.raises(
        TypeError,
        match=re.escape("'unknown' is an invalid keyword argument for Person()."),
    ):
        Person(name="Grace", unknown=True)

    # Only one positional argument is accepted, and it cannot be combined
    # with keyword arguments.
    with pytest.raises(AssertionError):
        Person({}, {})

    with pytest.raises(AssertionError):
        Person({}, name="Henry")

# Generated at 2026-10-24 22:56:47.675405
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    schema = ExampleSchema({"first": "one", "third": "three"})

    assert len(schema) == 2

# Generated at 2026-10-24 22:57:00.620485
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    # A new key is stored, readable, and counted.
    definitions["foo"] = "bar"
    assert definitions["foo"] == "bar"
    assert "foo" in definitions
    assert len(definitions) == 1

    # Re-assigning an already-set key raises AssertionError.
    with pytest.raises(AssertionError, match="has already been set"):
        definitions["foo"] = "baz"

    # The failed assignment left the original value intact.
    assert definitions["foo"] == "bar"
    assert len(definitions) == 1

    # A different key still succeeds after the failure.
    definitions["spam"] = "eggs"
    assert definitions["spam"] == "eggs"
    assert len(definitions) == 2

# Generated at 2026-10-24 22:57:51.205440
# Unit test for method serialize of class Reference
def test_Reference_serialize():reference = Reference("Target")


# Generated at 2026-10-24 22:58:07.692210
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

# Generated at 2026-10-24 22:58:19.593018
# Unit test for constructor of class Schema
def test_Schema():
    class Person(Schema):
        name = String()
        age = Integer(default=18)

    # Keyword arguments are validated, and defaults are applied.
    person = Person(name="Alice")
    assert person.name == "Alice"
    assert person.age == 18
    assert dict(person) == {"name": "Alice", "age": 18}
    assert not person.is_sparse

    # A positional dictionary copies only declared fields. Positional
    # construction intentionally does not validate or apply defaults.
    person = Person({"name": "Bob", "unknown": "ignored"})
    assert person.name == "Bob"
    assert not hasattr(person, "age")
    assert "unknown" not in person
    assert person.is_sparse

    # A positional object copies matching attributes.
    source = SimpleNamespace(name="Charlie", age=30, unknown="ignored")
    person = Person(source)
    assert person.name == "Charlie"
    assert person.age == 30
    assert dict(person) == {"name": "Charlie", "age": 30}

    # Invalid field values are reported as constructor errors.
    with pytest.raises(TypeError, match=r"Invalid argument 'name' for Person\(\)"):
        Person(name=None)

    # Unknown keyword arguments are rejected.
    with pytest.raises(
        TypeError,
        match=r"'unknown' is an invalid keyword argument for Person\(\)",
    ):
        Person(name="Alice", unknown=True)

    # Only one positional argument is allowed, and it cannot be mixed
    # with keyword arguments.
    with pytest.raises(AssertionError):
        Person({}, {})

    with pytest.raises(AssertionError):
        Person({}, name="Alice")

# Generated at 2026-10-24 22:59:14.866384
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()


# Generated at 2026-10-24 22:59:31.558135
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

# Generated at 2026-10-24 22:59:45.541738
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    class User(Schema):
        name = String()

    reference = Reference(User)
    user = User(name="Ada")

    assert reference.serialize(user) == {"name": "Ada"}

# Generated at 2026-10-24 23:00:05.248172
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    definitions = SchemaDefinitions()

    inherited_field = Field()
    base = SchemaMetaclass.__new__(
        SchemaMetaclass,
        "BaseSchema",
        (Schema,),
        {
            "__module__": __name__,
            "inherited": inherited_field,
        },
    )

    referenced_field = Reference("OtherSchema")
    regular_field = Field()

    generated = SchemaMetaclass.__new__(
        SchemaMetaclass,
        "GeneratedSchema",
        (base,),
        {
            "__module__": __name__,
            # Deliberately not in creation order.
            "regular": regular_field,
            "referenced": referenced_field,
        },
        definitions=definitions,
    )

    # Field attributes are removed from the class namespace.
    assert "regular" not in generated.__dict__
    assert "referenced" not in generated.__dict__

    # Inherited and declared fields are collected and sorted by creation order.
    assert list(generated.fields) == ["inherited", "referenced", "regular"]
    assert generated.fields["inherited"] is inherited_field
    assert generated.fields["referenced"] is referenced_field
    assert generated.fields["regular"] is regular_field

    # Definitions are propagated to Reference fields.
    assert referenced_field.definitions is definitions

    # The newly created schema is registered in the definitions mapping.
    assert definitions["GeneratedSchema"] is generated

# Generated at 2026-10-24 23:00:21.390653
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    class User(Schema):
        name = String()

    reference = Reference(User)
    user = User(name="Jane")

    assert reference.serialize(user) == {"name": "Jane"}
    assert reference.serialize(None) is None

# Generated at 2026-10-24 23:00:44.764469
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    reference = Reference("User")
    value = {"id": 1, "name": "Alice"}

    result = reference.serialize(value)

    assert result == value
    assert result is not value
    assert reference.serialize(None) is None

# Generated at 2026-10-24 23:01:01.263315
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

# Generated at 2026-10-24 23:01:02.696754
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    # A new key is stored, readable, and counted.
    definitions["foo"] = "bar"
    assert definitions["foo"] == "bar"
    assert "foo" in definitions
    assert len(definitions) == 1

    # Re-assigning an already-set key raises AssertionError.
    with pytest.raises(AssertionError, match="has already been set"):
        definitions["foo"] = "baz"

    # The failed assignment left the original value intact.
    assert definitions["foo"] == "bar"
    assert len(definitions) == 1

    # A different key still succeeds after the failure.
    definitions["spam"] = "eggs"
    assert definitions["spam"] == "eggs"
    assert len(definitions) == 2

# Generated at 2026-10-24 23:01:16.723227
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()
    existing_definitions = SchemaDefinitions()

    direct_reference = Reference("Direct")
    array_reference = Reference("ArrayItem")
    tuple_reference_1 = Reference("TupleItemOne")
    tuple_reference_2 = Reference("TupleItemTwo")
    object_reference = Reference("ObjectProperty")
    existing_reference = Reference(
        "Existing",
        definitions=existing_definitions,
    )

    field = Object(
        properties={
            "direct": direct_reference,
            "array": Array(items=array_reference),
            "tuple_array": Array(
                items=(tuple_reference_1, tuple_reference_2)
            ),
            "object": Object(
                properties={"reference": object_reference}
            ),
            "existing": existing_reference,
            "empty_array": Array(items=None),
        }
    )

    module_0.set_definitions(field, definitions)

    assert direct_reference.definitions is definitions
    assert array_reference.definitions is definitions
    assert tuple_reference_1.definitions is definitions
    assert tuple_reference_2.definitions is definitions
    assert object_reference.definitions is definitions

    # Existing definitions must not be overwritten.
    assert existing_reference.definitions is existing_definitions

    # A Reference passed directly should also be handled.
    root_reference = Reference("Root")
    module_0.set_definitions(root_reference, definitions)
    assert root_reference.definitions is definitions

# Generated at 2026-10-24 23:02:09.653950
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    definitions = SchemaDefinitions()

    inherited_field = Field()
    BaseSchema = SchemaMetaclass(
        "BaseSchema",
        (Schema,),
        {"inherited": inherited_field},
    )

    reference_field = Reference("Target")
    regular_field = Field()

    # Deliberately provide fields out of creation order.
    attrs = {
        "regular": regular_field,
        "reference": reference_field,
        "class_attribute": "preserved",
    }

    TestSchema = SchemaMetaclass(
        "TestSchema",
        (BaseSchema,),
        attrs,
        definitions=definitions,
    )

    # Fields are removed from the class namespace and collected in `fields`.
    assert "regular" not in TestSchema.__dict__
    assert "reference" not in TestSchema.__dict__
    assert TestSchema.class_attribute == "preserved"

    # Inherited fields are included and all fields are ordered by creation time.
    assert list(TestSchema.fields) == ["inherited", "reference", "regular"]
    assert TestSchema.fields["inherited"] is inherited_field
    assert TestSchema.fields["reference"] is reference_field
    assert TestSchema.fields["regular"] is regular_field

    # Definitions are assigned to references and the new schema is registered.
    assert reference_field.definitions is definitions
    assert definitions["TestSchema"] is TestSchema

# Generated at 2026-10-24 23:02:11.097380
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

# Generated at 2026-10-24 23:02:12.838443
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

# Generated at 2026-10-24 23:02:26.743498
# Unit test for constructor of class Schema
def test_Schema():
    from typesystem.fields import String, Integer, Boolean

    class Example(Schema):
        name = String()
        age = Integer(default=0)
        active = Boolean(default=False)

    # 1. Keyword construction validates and coerces values.
    obj = Example(name="tom", age=25, active=True)
    assert obj.name == "tom"
    assert obj.age == 25
    assert obj.active is True
    assert not obj.is_sparse

    # 2. Defaults are applied for omitted fields.
    obj = Example(name="ann")
    assert obj.age == 0
    assert obj.active is False

    # 3. Single positional dict argument copies matching keys (no validation).
    obj = Example({"name": "bob", "age": 30, "ignored": "extra"})
    assert obj.name == "bob"
    assert obj.age == 30
    assert obj.active is False
    assert obj.is_sparse

    # 4. Single positional object argument copies matching attributes.
    class Source:
        name = "src"
        age = 42
        unrelated = "noise"

    obj = Example(Source())
    assert obj.name == "src"
    assert obj.age == 42
    assert obj.active is False

    # 5. Invalid field value raises TypeError with a descriptive message.
    try:
        Example(name=123)
    except TypeError as exc:
        assert "Invalid argument 'name'" in str(exc)
    else:
        raise AssertionError("Expected TypeError for invalid argument 'name'")

    # 6. Unknown keyword argument raises TypeError.
    try:
        Example(name="x", nope=1)
    except TypeError as exc:
        assert "'nope' is an invalid keyword argument" in str(exc)
    else:
        raise AssertionError("Expected TypeError for unknown keyword argument")

    # 7. Both positional and keyword arguments raise AssertionError.
    try:
        Example({"name": "x"}, name="y")
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected AssertionError for args+kwargs together")

    # 8. Multiple positional arguments raise AssertionError.
    try:
        Example({"name": "x"}, {"name": "y"})
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected AssertionError for multiple positional args")

# Generated at 2026-10-24 23:03:10.192181
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    class User(Schema):
        name = String()

    reference = Reference(User)
    user = User(name="Alice")

    assert reference.serialize(user) == {"name": "Alice"}

# Generated at 2026-10-24 23:03:11.616565
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

# Generated at 2026-10-24 23:03:22.573570
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    assert len(ExampleSchema({})) == 0
    assert len(ExampleSchema({"first": "a"})) == 1
    assert len(ExampleSchema({"first": "a", "second": None})) == 2
    assert len(
        ExampleSchema({"first": "a", "second": "b", "third": "c"})
    ) == 3

    # Undeclared fields are ignored by the positional-dictionary constructor.
    assert len(ExampleSchema({"unknown": "value"})) == 0

# Generated at 2026-10-24 23:03:31.792605
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    assert len(ExampleSchema()) == 0
    assert len(ExampleSchema({"first": "value"})) == 1
    assert len(ExampleSchema({"first": "value", "second": "value"})) == 2

    # Unknown keys are not included as schema attributes.
    assert len(ExampleSchema({"unknown": "value"})) == 0

# Generated at 2026-10-24 23:03:33.186715
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

# Generated at 2026-10-24 23:04:02.608826
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 23:04:05.026946
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 23:04:32.162285
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 23:04:33.518528
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

# Generated at 2026-10-24 23:04:59.239835
# Unit test for method validate of class Reference
def test_Reference_validate():
    target = Mock()
    validated_value = object()
    target.validate.return_value = validated_value

    reference = Reference(
        to="Target",
        definitions={"Target": target},
    )

    source_value = {"name": "example"}
    result = reference.validate(source_value, strict=True)

    assert result is validated_value
    target.validate.assert_called_once_with(source_value, strict=True)

    with pytest.raises(ValidationError):
        reference.validate(None)

    target.validate.reset_mock()

    nullable_reference = Reference(
        to="Target",
        definitions={"Target": target},
        allow_null=True,
    )

    assert nullable_reference.validate(None) is None
    target.validate.assert_not_called()

# Generated at 2026-10-24 23:05:01.658608
# Unit test for method validate of class Reference

# Generated at 2026-10-24 23:05:04.077490
# Unit test for method validate of class Reference

# Generated at 2026-10-24 23:05:06.495777
# Unit test for method validate of class Reference

# Generated at 2026-10-24 23:05:08.916219
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 23:05:11.332200
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 23:05:13.749540
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 23:05:16.167926
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 23:05:23.201298
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 23:05:33.547204
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 23:05:43.098877
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()
        third = Field()

    schema = ExampleSchema({"first": "one", "third": "three"})

    # Only populated fields are yielded, in field-definition order.
    assert list(schema) == ["first", "third"]