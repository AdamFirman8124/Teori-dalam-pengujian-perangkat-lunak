

# Generated at 2026-11-02 06:32:17.279554
# Unit test for constructor of class Schema
def test_Schema():
    # Construct with valid keyword arguments
    instance = ExampleSchema(name="Tom", age=25)
    assert instance.name == "Tom"
    assert instance.age == 25

    # Construct with keyword arguments using field defaults
    instance = ExampleSchema(name="Tom")
    assert instance.name == "Tom"
    assert instance.age == 0
    assert not instance.is_sparse

    # Construct from a single dict positional argument
    instance = ExampleSchema({"name": "Tom"})
    assert instance.name == "Tom"
    assert not hasattr(instance, "age")
    assert instance.is_sparse

    # Construct from a single object positional argument
    class Obj:
        name = "Tom"
        age = 30

    instance = ExampleSchema(Obj())
    assert instance.name == "Tom"
    assert instance.age == 30

    # Invalid value for a keyword argument raises TypeError
    with pytest.raises(TypeError):
        ExampleSchema(name=123)

    # Unknown keyword argument raises TypeError
    with pytest.raises(TypeError):
        ExampleSchema(unknown="x")

    # More than one positional argument raises AssertionError
    with pytest.raises(AssertionError):
        ExampleSchema({}, {})

    # Positional argument combined with keyword arguments raises AssertionError
    with pytest.raises(AssertionError):
        ExampleSchema({}, name="Tom")

    # Mapping Protocol: __getitem__, __iter__, __len__
    instance = ExampleSchema({"name": "Tom"})
    assert instance["name"] == "Tom"
    assert list(iter(instance)) == ["name"]
    assert len(instance) == 1

    # __eq__ and __repr__
    a = ExampleSchema(name="Tom", age=25)
    b = ExampleSchema(name="Tom", age=25)
    c = ExampleSchema(name="Bob", age=25)
    assert a == b
    assert a != c
    assert repr(a) == "ExampleSchema(name='Tom', age=25)"
    assert repr(instance) == "ExampleSchema(name='Tom') [sparse]"

# Generated at 2026-11-02 06:32:58.209149
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem import Integer, Schema, String

    class Person(Schema):
        name = String()
        age = Integer()

    # Fully populated instance.
    person = Person(name="Tom", age=25)
    assert repr(person) == "Person(name='Tom', age=25)"

    # Instance constructed from a dictionary.
    person = Person({"name": "Tom", "age": 25})
    assert repr(person) == "Person(name='Tom', age=25)"

    # Sparse instance: 'age' has not been set.
    person = Person(name="Tom")
    assert repr(person) == "Person(name='Tom') [sparse]"

    # Sparse instance with no attributes set at all.
    person = Person()
    assert repr(person) == "Person() [sparse]"

    # A schema without any fields is never sparse.
    class Empty(Schema):
        pass

    assert repr(Empty()) == "Empty()"

    # Null values are included in the repr.
    class NullablePerson(Schema):
        name = String(allow_null=True)

    person = NullablePerson(name=None)
    assert repr(person) == "NullablePerson(name=None)"

    # Field ordering follows definition order (creation counter).
    class Ordered(Schema):
        first = String()
        second = Integer()
        third = String()

    ordered = Ordered(first="a", second=1, third="c")
    assert repr(ordered) == "Ordered(first='a', second=1, third='c')"

# Generated at 2026-11-02 06:33:15.443128
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem.fields import String

    class Example(Schema):
        first = String()
        second = String()
        third = String()

    # All fields set -> full length
    example = Example(first="a", second="b", third="c")
    assert len(example) == 3

    # Only some fields set -> sparse length
    example = Example(first="a")
    assert len(example) == 1
    assert example.is_sparse

    # No fields set -> zero length
    example = Example()
    assert len(example) == 0

# Generated at 2026-11-02 06:33:47.006150
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()

    # A fully populated schema iterates over all fields, in definition order.
    example = Example(name="Tom", age=20)
    assert list(iter(example)) == ["name", "age"]

    # A sparse schema only iterates over the fields that have been set.
    sparse = Example(name="Tom")
    assert list(iter(sparse)) == ["name"]

    # An empty schema iterates over nothing.
    empty = Example()
    assert list(iter(empty)) == []

    # Iteration is consistent with the mapped interface.
    assert dict(example) == {"name": "Tom", "age": 20}
    assert len(sparse) == 1

# Generated at 2026-11-02 06:34:13.915743
# Unit test for method __delitem__ of class SchemaDefinitions
def test_SchemaDefinitions___delitem__():
    from typesystem.schemas import SchemaDefinitions

    definitions = SchemaDefinitions({"a": 1, "b": 2})

    # Deleting an existing key removes it
    definitions.__delitem__("a")
    assert "a" not in definitions
    assert len(definitions) == 1
    assert definitions["b"] == 2

    # Deleting a non-existent key raises KeyError
    try:
        definitions.__delitem__("missing")
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError for missing key")

    # Deleting via del statement works as well
    del definitions["b"]
    assert len(definitions) == 0

# Generated at 2026-11-02 06:34:54.783619
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()

    # Fully populated instance yields all field keys in declaration order.
    instance = Example(name="Tom", age=20)
    assert list(instance) == ["name", "age"]

    # Sparse instance yields only keys for attributes that have been set.
    sparse_instance = Example(name="Tom")
    assert list(sparse_instance) == ["name"]

    # Iteration only yields keys defined as fields on the schema.
    instance.extra = "not a field"
    assert list(instance) == ["name", "age"]

    # A schema with no fields iterates to an empty sequence.
    class EmptySchema(Schema):
        pass

    assert list(EmptySchema()) == []

# Generated at 2026-11-02 06:37:37.841444
# Unit test for method validate of class Reference

# Generated at 2026-11-02 06:39:14.459718
# Unit test for method validate of class Reference
def test_Reference_validate():import pytest


# Generated at 2026-11-02 06:39:59.208250
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class Example(Schema):
        name = String()
        age = Integer()

    # All fields populated.
    example = Example(name="Tom", age=25)
    assert len(example) == 2

    # Sparse instance: fields without values are not counted.
    sparse = Example()
    assert len(sparse) == 0
    sparse.name = "Tom"
    assert len(sparse) == 1

    # Fields with defaults count as set attributes.
    class WithDefault(Schema):
        name = String()
        age = Integer(default=0)

    assert len(WithDefault()) == 1
    assert len(WithDefault(name="Tom")) == 2

    # Schema without any fields.
    class Empty(Schema):
        pass

    assert len(Empty()) == 0

    # Non-field attributes do not affect len.
    example = Example(name="Tom", age=25)
    example.extra = "ignored"
    assert len(example) == 2