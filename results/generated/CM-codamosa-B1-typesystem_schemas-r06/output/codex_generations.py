

# Generated at 2026-10-25 02:35:34.842012
# Unit test for constructor of class SchemaDefinitions
def test_SchemaDefinitions():
    # 1. Init from kwargs
    defs = SchemaDefinitions(a=1)
    assert defs["a"] == 1
    assert len(defs) == 1

    # 2. Init from a dict
    defs = SchemaDefinitions({"a": 1, "b": 2})
    assert len(defs) == 2
    assert defs["b"] == 2

    # 3. Iteration yields keys
    assert sorted(defs) == ["a", "b"]

    # 4. __setitem__ inserts new keys
    defs["c"] = 3
    assert defs["c"] == 3
    assert len(defs) == 3

    # 5. __setitem__ rejects duplicate keys
    with pytest.raises(AssertionError):
        defs["c"] = 99

    # 6. __delitem__ removes keys
    del defs["c"]
    assert "c" not in defs
    assert len(defs) == 2

    # 7. Missing keys raise KeyError
    with pytest.raises(KeyError):
        defs["missing"]

    # 8. MutableMapping mixin methods work
    defs.update({"d": 4})
    assert defs.pop("d") == 4
    assert "d" not in defs

# Generated at 2026-10-25 02:36:11.405257
# Unit test for constructor of class Schema
def test_Schema():import pytest


# Generated at 2026-10-25 02:36:18.855687
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()

    definitions["Example"] = original

    assert definitions["Example"] is original
    assert len(definitions) == 1

    with pytest.raises(AssertionError):
        definitions["Example"] = object()

    # A duplicate assignment must not replace the original definition.
    assert definitions["Example"] is original
    assert len(definitions) == 1

# Generated at 2026-10-25 02:36:28.385498
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    schema = ExampleSchema({"name": "Alice", "age": 30})
    assert repr(schema) == "ExampleSchema(name='Alice', age=30)"

    sparse_schema = ExampleSchema({"name": "Alice"})
    assert repr(sparse_schema) == "ExampleSchema(name='Alice') [sparse]"

# Generated at 2026-10-25 02:36:29.721156
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

# Generated at 2026-10-25 02:36:42.370448
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    complete = ExampleSchema({"name": "Alice", "age": 30})
    assert repr(complete) == "ExampleSchema(name='Alice', age=30)"

    sparse = ExampleSchema({"name": "Alice"})
    assert repr(sparse) == "ExampleSchema(name='Alice') [sparse]"

# Generated at 2026-10-25 02:37:24.569367
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:38:08.341037
# Unit test for method __new__ of class SchemaMetaclass
def test_SchemaMetaclass___new__():definitions = SchemaDefinitions()

# Generated at 2026-10-25 02:38:20.831935
# Unit test for constructor of class Reference
def test_Reference():
    class User(Schema):
        pass

    # Reference using a Schema class directly.
    direct_reference = Reference(User, allow_null=True)

    assert direct_reference.to is User
    assert direct_reference.definitions is None
    assert direct_reference.target is User
    assert direct_reference.target_string == "User"
    assert direct_reference.allow_null is True

    # Reference using a string and schema definitions.
    definitions = SchemaDefinitions({"User": User})
    string_reference = Reference("User", definitions=definitions)

    assert string_reference.to == "User"
    assert string_reference.definitions is definitions
    assert string_reference.target is User
    assert string_reference.target_string == "User"

# Generated at 2026-10-25 02:38:38.063287
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:38:52.578598
# Unit test for constructor of class Schema
def test_Schema():from typesystem.fields import Integer, String

# Generated at 2026-10-25 02:39:03.858716
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    instance = ExampleSchema({"name": "Alice", "age": 30})
    assert repr(instance) == "ExampleSchema(name='Alice', age=30)"

    sparse_instance = ExampleSchema({"name": "Alice"})
    assert repr(sparse_instance) == "ExampleSchema(name='Alice') [sparse]"

# Generated at 2026-10-25 02:39:13.559446
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class ExampleSchema(Schema):
        name = Field()
        age = Field()

    schema = ExampleSchema({"name": "Alice", "age": 30})
    assert repr(schema) == "ExampleSchema(name='Alice', age=30)"

    sparse_schema = ExampleSchema({"name": "Alice"})
    assert repr(sparse_schema) == "ExampleSchema(name='Alice') [sparse]"

# Generated at 2026-10-25 02:39:20.620102
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original = object()
    replacement = object()

    definitions["Example"] = original
    assert definitions["Example"] is original

    with pytest.raises(AssertionError):
        definitions["Example"] = replacement

    # A duplicate assignment must not replace the existing definition.
    assert definitions["Example"] is original

# Generated at 2026-10-25 02:39:23.038455
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:39:25.633529
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:39:28.048565
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:39:30.464641
# Unit test for constructor of class Reference

# Generated at 2026-10-25 02:39:32.878698
# Unit test for constructor of class Reference

# Generated at 2026-10-25 02:39:35.292493
# Unit test for constructor of class Reference

# Generated at 2026-10-25 02:39:37.707395
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:39:40.124126
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:39:42.547865
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:39:46.859860
# Unit test for function set_definitions

# Generated at 2026-10-25 02:39:49.277960
# Unit test for function set_definitions

# Generated at 2026-10-25 02:39:51.693525
# Unit test for function set_definitions

# Generated at 2026-10-25 02:39:54.110306
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:39:56.525449
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:39:58.940019
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:40:01.356011
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 02:40:03.770025
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 02:40:12.211158
# Unit test for method __repr__ of class Schema

# Generated at 2026-10-25 02:40:21.154129
# Unit test for method __len__ of class Schema
def test_Schema___len__():
    class ExampleSchema(Schema):
        first = Field()
        second = Field()

    assert len(ExampleSchema()) == 0
    assert len(ExampleSchema({"first": "value"})) == 1
    assert len(ExampleSchema({"first": "value", "second": 123})) == 2

    schema = ExampleSchema({"first": "value"})
    schema.unrelated_attribute = True
    assert len(schema) == 1

# Generated at 2026-10-25 02:40:36.413542
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():from typesystem.fields import Array, Field, Integer, Object, String

# Generated at 2026-10-25 02:40:38.828506
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 02:40:41.244336
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 02:40:43.660787
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 02:40:46.076210
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:40:48.607806
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:40:51.022442
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:40:53.437271
# Unit test for function set_definitions

# Generated at 2026-10-25 02:40:55.852429
# Unit test for function set_definitions

# Generated at 2026-10-25 02:40:58.269657
# Unit test for function set_definitions

# Generated at 2026-10-25 02:41:00.686305
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:41:03.102308
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:41:05.516305
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:41:28.411732
# Unit test for constructor of class Schema
def test_Schema():from typesystem.fields import Integer, String


# Generated at 2026-10-25 02:41:51.144160
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:41:53.557886
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:41:55.972489
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:41:58.387002
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:42:00.802050
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:42:03.216991
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-25 02:42:05.632287
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:42:08.047582
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:42:09.500532
# Unit test for constructor of class Schema
def test_Schema():from typesystem.fields import Integer, String

# Generated at 2026-10-25 02:42:19.325152
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:42:25.909480
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:42:35.093016
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:42:43.972156
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    definitions = SchemaDefinitions()
    original_value = object()

    definitions["Example"] = original_value

    assert definitions["Example"] is original_value
    assert len(definitions) == 1

    with pytest.raises(AssertionError, match="already been set"):
        definitions["Example"] = object()

    # A duplicate assignment must not overwrite the original definition.
    assert definitions["Example"] is original_value

# Generated at 2026-10-25 02:42:46.390716
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:42:48.805535
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:42:51.223154
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:42:53.637260
# Unit test for function set_definitions

# Generated at 2026-10-25 02:42:56.054954
# Unit test for function set_definitions

# Generated at 2026-10-25 02:42:58.469365
# Unit test for function set_definitions

# Generated at 2026-10-25 02:43:00.884516
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:43:03.300396
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:43:05.717428
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-25 02:43:08.130307
# Unit test for method validate of class Reference

# Generated at 2026-10-25 02:43:10.545361
# Unit test for method validate of class Reference

# Generated at 2026-10-25 02:43:12.958625
# Unit test for method validate of class Reference

# Generated at 2026-10-25 02:43:15.373856
# Unit test for constructor of class Reference

# Generated at 2026-10-25 02:43:17.786770
# Unit test for constructor of class Reference

# Generated at 2026-10-25 02:43:20.201052
# Unit test for constructor of class Reference

# Generated at 2026-10-25 02:43:23.349901
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:43:25.766726
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:43:28.180281
# Unit test for constructor of class Schema

# Generated at 2026-10-25 02:43:30.595603
# Unit test for function set_definitions

# Generated at 2026-10-25 02:43:38.887911
# Unit test for function set_definitions
def test_set_definitions():definitions = SchemaDefinitions()

# Generated at 2026-10-25 02:43:53.937035
# Unit test for method validate of class Reference
def test_Reference_validate():
    target = Mock()
    validated_value = object()
    target.validate.return_value = validated_value

    reference = Reference(
        "Target",
        definitions={"Target": target},
    )

    # Non-null values are validated by the target, with strict forwarded.
    value = {"name": "example"}
    result = reference.validate(value, strict=True)

    assert result is validated_value
    target.validate.assert_called_once_with(value, strict=True)

    # Null values are rejected by default without invoking the target.
    target.reset_mock()
    with pytest.raises(ValidationError):
        reference.validate(None)

    target.validate.assert_not_called()

    # Null values are accepted when allow_null is enabled.
    nullable_reference = Reference(
        "Target",
        definitions={"Target": target},
        allow_null=True,
    )

    assert nullable_reference.validate(None) is None
    target.validate.assert_not_called()

# Generated at 2026-10-25 02:44:01.723368
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:44:12.170365
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:44:14.588719
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:44:17.003298
# Unit test for function set_definitions

# Generated at 2026-10-25 02:44:19.419094
# Unit test for function set_definitions

# Generated at 2026-10-25 02:44:21.834658
# Unit test for function set_definitions

# Generated at 2026-10-25 02:44:24.436009
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:44:26.852280
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:44:29.268678
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:44:31.685268
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 02:44:34.098093
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 02:44:36.511900
# Unit test for method __len__ of class Schema

# Generated at 2026-10-25 02:44:38.926622
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 02:44:41.343281
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 02:44:43.757865
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-25 02:44:46.173083
# Unit test for method validate of class Reference

# Generated at 2026-10-25 02:44:48.587890
# Unit test for method validate of class Reference

# Generated at 2026-10-25 02:44:51.002531
# Unit test for method validate of class Reference

# Generated at 2026-10-25 02:44:53.417003
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:44:55.832283
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:45:04.906037
# Unit test for method __iter__ of class Schema

# Generated at 2026-10-25 02:45:21.085304
# Unit test for constructor of class Reference
def test_Reference():
    class User(Schema):
        pass

    definitions = {"User": User}

    # String-based reference.
    string_reference = Reference(
        "User",
        definitions=definitions,
        allow_null=True,
    )

    assert string_reference.to == "User"
    assert string_reference.definitions is definitions
    assert string_reference.target_string == "User"
    assert string_reference.target is User
    assert string_reference.allow_null is True

    # Direct schema reference.
    direct_reference = Reference(User)

    assert direct_reference.to is User
    assert direct_reference.definitions is None
    assert direct_reference.target is User
    assert direct_reference.target_string == "User"

# Generated at 2026-10-25 02:45:31.324961
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    class User(Schema):
        name = Field()
        age = Field()

    user = User({"name": "Alice", "age": 30})
    assert repr(user) == "User(name='Alice', age=30)"

    sparse_user = User({"name": "Bob"})
    assert repr(sparse_user) == "User(name='Bob') [sparse]"

    empty_user = User({})
    assert repr(empty_user) == "User() [sparse]"