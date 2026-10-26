

# Generated at 2026-10-25 06:05:01.308501
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    # Setting a new key stores the value.
    definitions["Example"] = int
    assert definitions["Example"] is int
    assert len(definitions) == 1

    # Overwriting an existing key raises AssertionError.
    with pytest.raises(AssertionError):
        definitions["Example"] = str

    # The original value is unchanged after the failed overwrite.
    assert definitions["Example"] is int

    # Different keys can each be set independently.
    definitions["Other"] = str
    assert len(definitions) == 2

# Generated at 2026-10-25 06:05:04.185664
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:05:20.666912
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 06:05:33.040855
# Unit test for method __delitem__ of class SchemaDefinitions
def test_SchemaDefinitions___delitem__():
    definitions = SchemaDefinitions()
    definitions["A"] = "schema-a"
    definitions["B"] = "schema-b"

    # Removes only the targeted key.
    del definitions["A"]
    assert len(definitions) == 1
    assert "A" not in definitions
    assert "B" in definitions
    assert definitions["B"] == "schema-b"

    # Accessing a deleted key raises KeyError.
    try:
        definitions["A"]
        assert False, "Expected KeyError for deleted key"
    except KeyError:
        pass

    # Deleting a missing key raises KeyError.
    try:
        del definitions["A"]
        assert False, "Expected KeyError for missing key"
    except KeyError:
        pass

    # Key can be re-added after deletion (setitem asserts uniqueness).
    definitions["A"] = "schema-a-new"
    assert definitions["A"] == "schema-a-new"
    assert len(definitions) == 2

    # Deleting last entry empties the mapping.
    del definitions["A"]
    del definitions["B"]
    assert len(definitions) == 0
    assert list(definitions) == []

# Generated at 2026-10-25 06:05:35.940042
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:05:52.399778
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 06:05:54.818446
# Unit test for method __len__ of class SchemaDefinitions

# Generated at 2026-10-25 06:05:57.276986
# Unit test for method __len__ of class SchemaDefinitions

# Generated at 2026-10-25 06:05:59.701586
# Unit test for method __len__ of class SchemaDefinitions

# Generated at 2026-10-25 06:06:02.118040
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:06:04.533041
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:06:06.949388
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:06:09.516079
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 06:06:12.058370
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 06:06:14.474633
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 06:06:16.894132
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:06:19.310837
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:06:21.910844
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:06:31.633006
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()

    # Fully populated schema
    example = Example(name="Tom", age=25)
    assert repr(example) == "Example(name='Tom', age=25)"

    # Sparse schema (missing some fields)
    sparse = Example(name="Tom")
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Empty schema (missing all fields)
    empty = Example()
    assert repr(empty) == "Example() [sparse]"

    # Field order follows declaration order (via _creation_counter)
    class Ordered(Schema):
        first = String()
        second = String()
        third = String()

    ordered = Ordered(first="a", second="b", third="c")
    assert repr(ordered) == "Ordered(first='a', second='b', third='c')"

    # Values are formatted with repr()
    example2 = Example(name="Ann", age=30)
    assert "name='Ann'" in repr(example2)
    assert "age=30" in repr(example2)

# Generated at 2026-10-25 06:06:34.461510
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:06:50.890856
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 06:06:53.308203
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:06:55.727420
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:06:58.332313
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:07:00.748889
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:07:03.165353
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:07:05.583813
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:07:07.997833
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:07:10.414243
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:07:12.831778
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:07:15.251574
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:07:17.668799
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:07:20.183319
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:07:22.600371
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:07:25.019561
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:07:27.437443
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:07:29.851883
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:07:32.270550
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:07:34.782647
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:07:37.110174
# Unit test for constructor of class Reference

# Generated at 2026-10-25 06:07:45.358668
# Unit test for constructor of class Reference
def test_Reference():
    from typesystem.fields import Field

    ref = Reference("ExampleSchema")
    assert isinstance(ref, Field)
    assert ref.to == "ExampleSchema"
    assert ref.target_string == "ExampleSchema"
    assert ref.definitions is None
    assert ref.allow_null is False
    assert ref.errors == {"null": "May not be null."}

    ref_nullable = Reference("ExampleSchema", allow_null=True)
    assert ref_nullable.allow_null is True
    assert ref_nullable.validate(None) is None

    class ExampleSchema(Schema):
        name = Field()
        age = Field(default=0)

    ref_cls = Reference(ExampleSchema)
    assert ref_cls.to is ExampleSchema
    assert ref_cls.target_string == "ExampleSchema"
    assert ref_cls.target is ExampleSchema

    definitions = SchemaDefinitions()
    definitions["ExampleSchema"] = ExampleSchema
    ref_def = Reference("ExampleSchema", definitions=definitions)
    assert ref_def.definitions is definitions
    assert ref_def.target is ExampleSchema

# Generated at 2026-10-25 06:08:19.472889
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:08:21.895626
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:08:24.313624
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:08:26.727213
# Unit test for function set_definitions

# Generated at 2026-10-25 06:08:29.146104
# Unit test for function set_definitions

# Generated at 2026-10-25 06:08:31.617975
# Unit test for function set_definitions

# Generated at 2026-10-25 06:08:33.989876
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:08:36.407504
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:08:56.846013
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:08:58.191410
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

# Generated at 2026-10-25 06:09:01.045107
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:03.459890
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:06.000918
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:08.416863
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 06:09:10.834765
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 06:09:13.250234
# Unit test for method serialize of class Reference

# Generated at 2026-10-25 06:09:15.664748
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:18.080447
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:20.498264
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:22.922652
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 06:09:25.338145
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 06:09:27.752041
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 06:09:30.166996
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 06:09:32.580582
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 06:09:34.994820
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 06:09:37.409342
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:09:39.823441
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:09:42.240419
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:09:44.652521
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:47.066353
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:49.480946
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:09:51.894675
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:09:54.308100
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:09:56.735436
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:09:59.508126
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()

    # Fully populated schema
    example = Example(name="Tom", age=25)
    assert repr(example) == "Example(name='Tom', age=25)"

    # Sparse schema (missing some fields)
    sparse = Example(name="Tom")
    assert repr(sparse) == "Example(name='Tom') [sparse]"

    # Empty schema (missing all fields)
    empty = Example()
    assert repr(empty) == "Example() [sparse]"

    # Field order follows declaration order (via _creation_counter)
    class Ordered(Schema):
        first = String()
        second = String()
        third = String()

    ordered = Ordered(first="a", second="b", third="c")
    assert repr(ordered) == "Ordered(first='a', second='b', third='c')"

    # Values are formatted with repr()
    example2 = Example(name="Ann", age=30)
    assert "name='Ann'" in repr(example2)
    assert "age=30" in repr(example2)

# Generated at 2026-10-25 06:10:36.264349
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:10:38.679515
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:10:41.122923
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:10:43.537700
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:10:45.952521
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:10:48.609004
# Unit test for method validate of class Reference

# Generated at 2026-10-25 06:10:51.023397
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:10:53.439778
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:10:55.853347
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:10:58.270792
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:11:00.684393
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:11:03.099563
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:11:05.517461
# Unit test for constructor of class Reference

# Generated at 2026-10-25 06:11:07.994069
# Unit test for constructor of class Reference

# Generated at 2026-10-25 06:11:10.409090
# Unit test for constructor of class Reference

# Generated at 2026-10-25 06:11:13.383596
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:11:15.799774
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:11:18.214653
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:11:20.958230
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:11:37.377319
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 06:11:38.851299
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

# Generated at 2026-10-25 06:11:40.591352
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()

    # Setting a new key stores the value.
    definitions["Example"] = int
    assert definitions["Example"] is int
    assert len(definitions) == 1

    # Overwriting an existing key raises AssertionError.
    with pytest.raises(AssertionError):
        definitions["Example"] = str

    # The original value is unchanged after the failed overwrite.
    assert definitions["Example"] is int

    # Different keys can each be set independently.
    definitions["Other"] = str
    assert len(definitions) == 2

# Generated at 2026-10-25 06:11:59.332186
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:12:01.752384
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:12:04.172076
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:12:06.587325
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:12:09.453546
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:12:26.252844
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():from typesystem.fields import Integer

# Generated at 2026-10-25 06:12:27.603707
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

# Generated at 2026-10-25 06:12:30.302492
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:12:32.717606
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:12:35.138586
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:12:37.549929
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:12:40.149596
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:12:42.513278
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:12:44.931405
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:12:47.356068
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:12:49.773505
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:12:57.784174
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:13:00.204449
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:13:02.616260
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 06:13:05.033987
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:13:07.446554
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:13:09.861546
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:13:12.277207
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:13:14.690712
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:13:31.698843
# Unit test for method __len__ of class Schema
def test_Schema___len__():from typesystem.fields import Field

# Generated at 2026-10-25 06:13:33.069883
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

# Generated at 2026-10-25 06:13:52.687733
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():
    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String(max_length=50)
        age = Integer()

    class PersonCopy(Schema):
        name = String(max_length=50)
        age = Integer()

    # Reflexive / identical values -> equal.
    p1 = Person(name="Alice", age=30)
    p2 = Person(name="Alice", age=30)
    assert p1 == p2
    assert p1 == p1
    assert not (p1 != p2)

    # Same values via different construction (dict / validate) -> equal.
    p_from_dict = Person({"name": "Alice", "age": 30})
    assert p1 == p_from_dict
    p_validated = Person.validate({"name": "Alice", "age": 30})
    assert p1 == p_valid

# Generated at 2026-10-25 06:13:55.404149
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:13:57.820427
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:14:00.234647
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 06:14:02.650010
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:14:05.067362
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:14:07.480145
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 06:14:09.894863
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:14:12.318424
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:14:14.725489
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:14:17.141424
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:14:19.556840
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:14:21.972149
# Unit test for constructor of class Schema

# Generated at 2026-10-25 06:14:24.387635
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:14:26.802795
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 06:14:29.217535
# Unit test for method __iter__ of class Schema