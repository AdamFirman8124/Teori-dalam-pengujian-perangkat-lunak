

# Generated at 2026-11-02 20:51:09.981574
# Unit test for constructor of class Schema
def test_Schema():
    class ExampleSchema(Schema):
        name = String()
        age = Integer(default=0)

    # Keyword argument construction with validation
    instance = ExampleSchema(name="tom", age=25)
    assert instance.name == "tom"
    assert instance.age == 25

    # Default values applied when kwargs are omitted
    instance = ExampleSchema(name="tom")
    assert instance.name == "tom"
    assert instance.age == 0
    assert not instance.is_sparse

    # Sparse instance when a field without default is omitted
    sparse = ExampleSchema()
    assert sparse.is_sparse
    assert len(sparse) == 1
    assert dict(sparse) == {"age": 0}

    # Construction from a mapping (values copied without validation)
    instance = ExampleSchema({"name": "jerry", "age": 30})
    assert instance.name == "jerry"
    assert instance.age == 30

    # Construction from an arbitrary object with matching attributes
    class Item:
        name = "spike"
        age = 40

    instance = ExampleSchema(Item())
    assert instance.name == "spike"
    assert instance.age == 40

    # Invalid value for a field raises TypeError
    with pytest.raises(TypeError):
        ExampleSchema(name=123)

    # Unknown keyword argument raises TypeError
    with pytest.raises(TypeError):
        ExampleSchema(name="tom", unknown=True)

    # More than one positional argument is not allowed
    with pytest.raises(AssertionError):
        ExampleSchema({"name": "a"}, {"name": "b"})

    # Positional argument cannot be combined with keyword arguments
    with pytest.raises(AssertionError):
        ExampleSchema({"name": "a"}, name="b")

# Generated at 2026-11-02 20:52:14.554835
# Unit test for constructor of class SchemaDefinitions
def test_SchemaDefinitions():
    # Empty construction
    definitions = SchemaDefinitions()
    assert len(definitions) == 0
    assert dict(definitions) == {}
    assert list(definitions) == []

    # Construction from a dict
    definitions = SchemaDefinitions({"a": 1, "b": 2})
    assert len(definitions) == 2
    assert definitions["a"] == 1
    assert definitions["b"] == 2

    # Construction from keyword arguments
    definitions = SchemaDefinitions(x=10, y=20)
    assert definitions["x"] == 10
    assert definitions["y"] == 20

    # Construction from an iterable of key/value pairs
    definitions = SchemaDefinitions([("k1", "v1"), ("k2", "v2")])
    assert list(definitions) == ["k1", "k2"]
    assert definitions["k1"] == "v1"

    # Setting items
    definitions = SchemaDefinitions()
    definitions["schema1"] = "value1"
    assert definitions["schema1"] == "value1"
    assert len(definitions) == 1

    # Cannot overwrite an existing definition
    try:
        definitions["schema1"] = "value2"
    except AssertionError:
        pass
    else:
        raise AssertionError("Expected AssertionError for duplicate key")
    assert definitions["schema1"] == "value1"

    # Deleting items
    del definitions["schema1"]
    assert "schema1" not in definitions
    assert len(definitions) == 0

    # Deleting a missing key raises KeyError
    try:
        del definitions["schema1"]
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError when deleting missing key")

    # Missing key access raises KeyError
    try:
        definitions["missing"]
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError for missing key")

# Generated at 2026-11-02 20:53:12.505712
# Unit test for method __iter__ of class SchemaDefinitions
def test_SchemaDefinitions___iter__():
    # Iterating over empty definitions yields nothing
    definitions = SchemaDefinitions()
    assert list(definitions) == []
    assert list(iter(definitions)) == []

    # Iterating over populated definitions yields the keys
    definitions = SchemaDefinitions({"a": 1, "b": 2, "c": 3})
    assert sorted(definitions) == ["a", "b", "c"]

    # Iteration order matches insertion order (dict-backed)
    definitions = SchemaDefinitions({"z": 1, "m": 2, "a": 3})
    assert list(definitions) == ["z", "m", "a"]

    # Each call to iter() returns a fresh iterator
    it1 = iter(definitions)
    it2 = iter(definitions)
    assert next(it1) == "z"
    assert next(it2) == "z"
    assert list(it1) == ["m", "a"]
    assert list(it2) == ["m", "a"]

    # Iteration reflects mutations to the underlying definitions
    definitions = SchemaDefinitions()
    definitions["one"] = 1
    definitions["two"] = 2
    assert list(definitions) == ["one", "two"]
    del definitions["one"]
    assert list(definitions) == ["two"]

    # Initialized via kwargs also works
    definitions = SchemaDefinitions(x=1, y=2)
    assert sorted(definitions) == ["x", "y"]

# Generated at 2026-11-02 20:54:55.189847
# Unit test for function set_definitions
def test_set_definitions():
    from typesystem.fields import String

    definitions = SchemaDefinitions()

    # A plain Reference with no definitions gets them set.
    ref = Reference("Example")
    assert ref.definitions is None
    module_0.set_definitions(ref, definitions)
    assert ref.definitions is definitions

    # A Reference that already has definitions is left untouched.
    other_definitions = SchemaDefinitions()
    ref_with_defs = Reference("Example", definitions=other_definitions)
    module_0.set_definitions(ref_with_defs, definitions)
    assert ref_with_defs.definitions is other_definitions

    # A Reference nested inside an Array (single item) gets them set.
    array_ref = Reference("Example")
    array = Array(items=array_ref)
    module_0.set_definitions(array, definitions)
    assert array_ref.definitions is definitions

    # References nested inside an Array (tuple of items) get them set.
    ref_a = Reference("A")
    ref_b = Reference("B")
    tuple_array = Array(items=(ref_a, ref_b))
    module_0.set_definitions(tuple_array, definitions)
    assert ref_a.definitions is definitions
    assert ref_b.definitions is definitions

    # A Reference nested inside an Object's properties gets them set.
    obj_ref = Reference("Example")
    obj = Object(properties={"nested": obj_ref})
    module_0.set_definitions(obj, definitions)
    assert obj_ref.definitions is definitions

    # Deeply nested: Object -> Array -> Reference.
    deep_ref = Reference("Example")
    deep = Object(properties={"items": Array(items=deep_ref)})
    module_0.set_definitions(deep, definitions)
    assert deep_ref.definitions is definitions

    # An Array with no items is handled safely.
    empty_array = Array()
    module_0.set_definitions(empty_array, definitions)

    # Non-container, non-reference fields are ignored without error.
    plain_field = String()
    module_0.set_definitions(plain_field, definitions)

# Generated at 2026-11-02 20:55:34.455641
# Unit test for method __iter__ of class SchemaDefinitions
def test_SchemaDefinitions___iter__():
    # Iterating over an empty definitions mapping yields nothing
    definitions = SchemaDefinitions()
    assert list(iter(definitions)) == []
    assert len(list(definitions)) == 0

    # Iterating yields the keys that have been set
    definitions = SchemaDefinitions()
    definitions["Foo"] = String()
    definitions["Bar"] = String()
    assert list(iter(definitions)) == ["Foo", "Bar"]

    # Iterating over definitions initialized from a dict yields its keys
    definitions = SchemaDefinitions({"A": String(), "B": String()})
    assert sorted(iter(definitions)) == ["A", "B"]

    # Iteration order matches insertion order
    definitions = SchemaDefinitions()
    definitions["first"] = String()
    definitions["second"] = String()
    definitions["third"] = String()
    assert list(definitions) == ["first", "second", "third"]

# Generated at 2026-11-02 20:56:21.211270
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()
        email = Field(default="")

    # All fields populated explicitly.
    instance = ExampleSchema(name="Alice", age=30, email="alice@example.com")
    assert len(instance) == 3

    # Field with a default is set automatically and counts towards len.
    instance = ExampleSchema(name="Bob", age=25)
    assert len(instance) == 3
    assert not instance.is_sparse

    # Sparse instance: 'age' is never set, 'email' falls back to its default.
    instance = ExampleSchema(name="Charlie")
    assert len(instance) == 2
    assert instance.is_sparse

    # Constructing from a dict only sets keys present in the dict.
    instance = ExampleSchema({"name": "Dave"})
    assert len(instance) == 1

    # Manually setting an attribute makes it count towards len.
    instance.age = 42
    assert len(instance) == 2

    # Schema with no fields at all.
    class EmptySchema(Schema):
        pass

    assert len(EmptySchema()) == 0

# Generated at 2026-11-02 20:57:02.472585
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():
    from typesystem.fields import String

    class ExampleSchema(Schema):
        name = String()
        age = String()

    # A fully populated instance iterates over all of its field names.
    instance = ExampleSchema(name="Tom", age="25")
    assert list(instance) == ["name", "age"]

    # A sparse instance only iterates over fields that have values set.
    sparse_instance = ExampleSchema(name="Tom")
    assert list(sparse_instance) == ["name"]

    # A schema with no fields iterates to nothing.
    class EmptySchema(Schema):
        pass

    empty = EmptySchema()
    assert list(empty) == []
    assert len(empty) == 0