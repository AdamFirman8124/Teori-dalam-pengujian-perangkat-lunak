

# Generated at 2026-11-02 09:35:54.488374
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String()
        age = Integer()

    # All fields populated -> length equals the number of fields
    full = Person(name="Tom", age=20)
    assert len(full) == 2

    # Sparse instance -> only attributes that have been set are counted
    sparse = Person({"name": "Tom"})
    assert len(sparse) == 1
    assert sparse.is_sparse

    # Empty instance -> no attributes counted
    empty = Person({})
    assert len(empty) == 0

    # Fields with defaults count as set
    class WithDefault(Schema):
        name = String()
        age = Integer(default=0)

    instance = WithDefault(name="Tom")
    assert len(instance) == 2

# nonce:bb8ce81a

# Generated at 2026-11-02 09:38:37.670726
# Unit test for method serialize of class Reference
def test_Reference_serialize():
    from typesystem.fields import String

    # A string target does not need definitions to be resolvable for module_0.serialize().
    reference = Reference(to="Example")

    # None serializes to None.
    assert reference.serialize(None) is None

    # Mapping-like objects are converted into a plain dict (a copy).
    obj = {"name": "abc"}
    result = reference.serialize(obj)
    assert result == {"name": "abc"}
    assert result is not obj

    # Schema instances are converted to a dict of their field values.
    class Example(Schema):
        name = String()

    instance = Example(name="abc")
    assert reference.serialize(instance) == {"name": "abc"}

    # Referencing a Schema class directly behaves the same.
    reference_to_class = Reference(to=Example)
    assert reference_to_class.serialize(None) is None
    assert reference_to_class.serialize(instance) == {"name": "abc"}
    assert reference_to_class.serialize({"name": "abc"}) == {"name": "abc"}

# Generated at 2026-11-02 09:40:37.727816
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    # Setting a new key should store the value
    definitions["Example"] = "value"
    assert definitions["Example"] == "value"
    assert len(definitions) == 1

    # Setting a second new key should also work
    definitions["Another"] = 123
    assert definitions["Another"] == 123
    assert len(definitions) == 2

    # Setting an already existing key should raise an AssertionError
    import pytest

    with pytest.raises(AssertionError):
        definitions["Example"] = "other"

    # The original value must remain unchanged after the failed set
    assert definitions["Example"] == "value"
    assert len(definitions) == 2

# Generated at 2026-11-02 09:42:11.136207
# Unit test for method __getitem__ of class Schema
def test_Schema___getitem__():
    import pytest
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()

    example = Example(name="tom", age=3)

    # Existing fields return their serialized values.
    assert example["name"] == "tom"
    assert example["age"] == 3

    # Accessing a key that is not a field raises KeyError.
    with pytest.raises(KeyError):
        example["missing"]

    # Accessing a field whose attribute was never set (sparse) raises KeyError.
    sparse = Example(name="tom")
    with pytest.raises(KeyError):
        sparse["age"]