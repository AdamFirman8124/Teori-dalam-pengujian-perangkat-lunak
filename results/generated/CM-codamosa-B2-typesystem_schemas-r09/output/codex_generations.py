

# Generated at 2026-11-02 12:28:27.553462
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem.fields import String, Integer

    class Example(Schema):
        name = String()
        age = Integer()

    # All fields populated
    full = Example(name="Tom", age=20)
    assert len(full) == 2

    # Non-field attributes do not affect the length
    full.unrelated = "ignored"
    assert len(full) == 2

    # Sparse instance: only some fields populated
    sparse = Example(name="Tom")
    assert len(sparse) == 1

    # No fields populated
    empty = Example()
    assert len(empty) == 0

    # Fields with defaults are set during __init__ and count toward length
    class WithDefault(Schema):
        name = String()
        age = Integer(default=0)

    instance = WithDefault(name="Tom")
    assert len(instance) == 2

# Generated at 2026-11-02 12:30:11.897586
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.fields import Integer, String
    from typesystem.schemas import Schema

    class Example(Schema):
        name = String()
        age = Integer()

    # Fully populated instance
    example = Example(name="foo", age=3)
    assert repr(example) == "Example(name='foo', age=3)"

    # Sparse instance: 'age' was not supplied
    sparse = Example(name="foo")
    assert repr(sparse) == "Example(name='foo') [sparse]"

    # Fully sparse instance: no fields supplied
    empty = Example()
    assert repr(empty) == "Example() [sparse]"

    # Fields with defaults are shown in the repr
    class WithDefault(Schema):
        name = String(default="anonymous")

    assert repr(WithDefault()) == "WithDefault(name='anonymous')"

    # repr for instance built from a mapping (sparse, unvalidated extra keys ignored)
    from_dict = Example({"name": "foo"})
    assert repr(from_dict) == "Example(name='foo') [sparse]"

# Generated at 2026-11-02 12:31:33.301102
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    class Example(Schema):
        name = String()
        age = Integer()

    # An instance compares equal to itself.
    first = Example(name="Tom", age=25)
    assert first == first

    # Instances with identical field values compare equal.
    second = Example(name="Tom", age=25)
    assert first == second
    assert not first != second

    # Instances with any differing field value are not equal.
    assert first != Example(name="Jill", age=25)
    assert first != Example(name="Tom", age=30)

    # Comparisons against objects that are not instances of the same
    # class always return False.
    assert first != "Tom"
    assert first != 25
    assert first != None
    assert first != {"name": "Tom", "age": 25}

    # Instances of a different schema class are not equal, even when
    # their field values match.
    class Other(Schema):
        name = String()
        age = Integer()

    assert first != Other(name="Tom", age=25)

    # A subclass instance is considered equal when the inherited fields
    # match, because the isinstance check accepts subclasses...
    class SubExample(Example):
        pass

    assert first == SubExample(name="Tom", age=25)

    # ...but not in the reverse direction, since a subclass instance
    # requires `other` to be an instance of the subclass.
    assert SubExample(name="Tom", age=25) != first

# Generated at 2026-11-02 12:33:46.534683
# Unit test for function set_definitions
def test_set_definitions():
    definitions = SchemaDefinitions()

    # Reference field gets definitions assigned.
    ref = Reference(to="Example")
    assert ref.definitions is None
    module_0.set_definitions(ref, definitions)
    assert ref.definitions is definitions

    # Existing definitions are not overwritten.
    existing = SchemaDefinitions()
    ref_with_defs = Reference(to="Example", definitions=existing)
    module_0.set_definitions(ref_with_defs, definitions)
    assert ref_with_defs.definitions is existing


def test_set_definitions_reference_resolves_target():
    class Example(Schema):
        pass

    definitions = SchemaDefinitions()
    definitions["Example"] = Example
    ref = Reference(to="Example")
    module_0.set_definitions(ref, definitions)
    assert ref.target is Example


def test_set_definitions_array_single_item():
    definitions = SchemaDefinitions()
    item = Reference(to="Example")
    field = Array(items=item)
    module_0.set_definitions(field, definitions)
    assert item.definitions is definitions


def test_set_definitions_array_multiple_items():
    definitions = SchemaDefinitions()
    item1 = Reference(to="Example1")
    item2 = Reference(to="Example2")
    field = Array(items=(item1, item2))
    module_0.set_definitions(field, definitions)
    assert item1.definitions is definitions
    assert item2.definitions is definitions


def test_set_definitions_array_without_items():
    definitions = SchemaDefinitions()
    field = Array()
    # Should be a no-op, not raise.
    module_0.set_definitions(field, definitions)


def test_set_definitions_object_properties():
    definitions = SchemaDefinitions()
    ref1 = Reference(to="Example1")
    ref2 = Reference(to="Example2")
    field = Object(properties={"a": ref1, "b": ref2})
    module_0.set_definitions(field, definitions)
    assert ref1.definitions is definitions
    assert ref2.definitions is definitions


def test_set_definitions_plain_field_is_noop():
    definitions = SchemaDefinitions()
    field = String()
    # Should be a no-op, not raise.
    module_0.set_definitions(field, definitions)


def test_set_definitions_nested_structures():
    definitions = SchemaDefinitions()
    nested_ref = Reference(to="Nested")
    array_ref = Reference(to="ArrayItem")
    deep_ref = Reference(to="Deep")

    field = Object(
        properties={
            "obj": Object(properties={"nested": nested_ref}),
            "array": Array(items=[array_ref]),
            "deep": Array(items=Object(properties={"deep": deep_ref})),
        }
    )
    module_0.set_definitions(field, definitions)
    assert nested_ref.definitions is definitions
    assert array_ref.definitions is definitions
    assert deep_ref.definitions is definitions


def test_set_definitions_via_schema_metaclass():
    definitions = SchemaDefinitions()

    class Example(Schema, definitions=definitions):
        pass

    class Wrapper(Schema, definitions=definitions):
        example = Reference(to="Example")
        examples = Array(items=Reference(to="Example"))

    assert definitions["Example"] is Example
    assert Wrapper.fields["example"].definitions is definitions
    assert Wrapper.fields["examples"].items.definitions is definitions

# Generated at 2026-11-02 12:36:43.740680
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Basic retrieval of defined fields returns the serialized value
    example = Example(name="Tom", age=20)
    assert example["name"] == "Tom"
    assert example["age"] == 20

    # Accessing a key that is not a field raises KeyError
    with pytest.raises(KeyError):
        example["missing"]

    # Accessing a field that was never set (sparse instance) raises KeyError
    sparse = Example(name="Tom")
    assert sparse.is_sparse is True
    with pytest.raises(KeyError):
        sparse["age"]

    # KeyError carries the requested key
    try:
        example["nonexistent"]
    except KeyError as exc:
        assert exc.args[0] == "nonexistent"
    else:
        pytest.fail("KeyError not raised")

    # Values set via a dict-style constructor are also accessible
    from_dict = Example({"name": "Anna", "age": 30})
    assert from_dict["name"] == "Anna"
    assert from_dict["age"] == 30

    # Values set via an object-style constructor are accessible
    class Source:
        name = "Bob"
        age = 40

    from_obj = Example(Source())
    assert from_obj["name"] == "Bob"
    assert from_obj["age"] == 40