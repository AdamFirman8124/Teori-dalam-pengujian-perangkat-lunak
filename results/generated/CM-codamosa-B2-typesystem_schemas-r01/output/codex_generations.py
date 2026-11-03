

# Generated at 2026-11-02 09:41:21.690350
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():
    from typesystem.fields import Integer, String

    definitions = SchemaDefinitions()

    class Example(Schema, definitions=definitions):
        name = String()
        age = Integer()

    # Field attributes are collected into `fields` and removed from the class.
    assert list(Example.fields.keys()) == ["name", "age"]
    assert not hasattr(Example, "name")
    assert not hasattr(Example, "age")

    # The new class is registered under its name in the definitions mapping.
    assert definitions["Example"] is Example

    # Fields are inherited from base Schema classes.
    class Extended(Example):
        email = String()

    assert list(Extended.fields.keys()) == ["name", "age", "email"]
    assert "Extended" not in definitions

    # Definitions are propagated to string-referenced Reference fields.
    class WithReference(Schema, definitions=definitions):
        child = Reference(to="Example")

    assert WithReference.fields["child"].definitions is definitions

    # Definitions are propagated through nested containers (Array).
    class WithNested(Schema, definitions=definitions):
        items = Array(items=Reference(to="Example"))

    assert WithNested.fields["items"].items.definitions is definitions

    # Non-Field attributes are left untouched on the class.
    class WithOtherAttrs(Schema, definitions=definitions):
        count = Integer()
        label = "not a field"

    assert WithOtherAttrs.label == "not a field"
    assert list(WithOtherAttrs.fields.keys()) == ["count"]

# Generated at 2026-11-02 09:42:46.648922
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()

    # All fields populated -> length equals number of fields
    example = Example(name="Tom", age=25)
    assert len(example) == 2

    # Sparse instance: only fields actually set are counted
    sparse = Example(name="Tom")
    assert len(sparse) == 1

    # Schema with no fields
    class Empty(Schema):
        pass

    assert len(Empty()) == 0

    # Fields with defaults count once populated via default
    class WithDefault(Schema):
        name = String()
        age = Integer(default=0)

    instance = WithDefault(name="Tom")
    assert len(instance) == 2
    assert len(WithDefault(name="Tom", age=3)) == 2

# Generated at 2026-11-02 09:43:45.837731
# Unit test for method __getitem__ of class SchemaDefinitions
def test_SchemaDefinitions___getitem__():
    from typesystem.schemas import SchemaDefinitions

    # Build definitions from a dict and from kwargs
    definitions = SchemaDefinitions({"example": 123})
    other = SchemaDefinitions(example=123, another="value")

    # Existing keys return their values
    assert definitions["example"] == 123
    assert other["example"] == 123
    assert other["another"] == "value"

    # Missing keys raise KeyError
    try:
        definitions["missing"]
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError for missing key")

    # Keys are retrievable after being set via __setitem__
    definitions["added"] = 456
    assert definitions["added"] == 456

# Generated at 2026-11-02 09:44:53.831244
# Unit test for method __iter__ of class SchemaDefinitions
def test_SchemaDefinitions___iter__():
    # Empty definitions
    definitions = SchemaDefinitions()
    assert list(iter(definitions)) == []

    # Definitions with items
    definitions = SchemaDefinitions({"a": 1, "b": 2, "c": 3})
    it = iter(definitions)
    assert list(it) == ["a", "b", "c"]

    # Iterating twice should return fresh iterators
    assert [key for key in definitions] == ["a", "b", "c"]

    # Membership checks work via iteration protocol
    assert "a" in definitions
    assert "z" not in definitions

    # Constructed with kwargs
    definitions = SchemaDefinitions(x=10, y=20)
    assert sorted(iter(definitions)) == ["x", "y"]

# Generated at 2026-11-02 09:46:23.435755
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    class Example(Schema):
        name = String()
        age = Integer()

    # Accessing an existing field returns the (serialized) value.
    example = Example(name="Tom", age=25)
    assert example["name"] == "Tom"
    assert example["age"] == 25

    # Accessing a key that is not a field raises KeyError.
    with pytest.raises(KeyError):
        example["unknown"]

    # Accessing a field that is not set on the instance raises KeyError.
    sparse_example = Example(name="Tom")
    with pytest.raises(KeyError):
        sparse_example["age"]

# Generated at 2026-11-02 09:48:29.477741
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()

    # All fields populated.
    example = Example(name="Tom", age=25)
    assert len(example) == 2

    # Sparse instance: only some fields populated.
    sparse = Example(name="Tom")
    assert len(sparse) == 1
    assert sparse.is_sparse

    # Length reflects attributes set on the instance.
    sparse.age = 25
    assert len(sparse) == 2

    # Fields with defaults count towards the length.
    class WithDefault(Schema):
        name = String()
        age = Integer(default=0)

    instance = WithDefault(name="Tom")
    assert len(instance) == 2

    # Schema without any fields.
    class Empty(Schema):
        pass

    assert len(Empty()) == 0