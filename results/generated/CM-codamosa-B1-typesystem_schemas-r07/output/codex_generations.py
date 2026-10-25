

# Generated at 2026-10-24 13:00:51.926079
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String()
        age = Integer(default=0)

    # Fully populated -> no sparse indicator, fields in definition order.
    full = Person(name="Alice", age=30)
    assert not full.is_sparse
    assert repr(full) == "Person(name='Alice', age=30)"

    # Default is applied via kwargs path, so still not sparse.
    with_default = Person(name="Bob")
    assert with_default.age == 0
    assert not with_default.is_sparse
    assert repr(with_default) == "Person(name='Bob', age=0)"

    # Missing required field -> sparse, only set attrs shown.
    sparse = Person()
    assert sparse.is_sparse
    # `age` has a default so it is set, `name` is missing.
    assert repr(sparse) == "Person(age=0) [sparse]"

    # Dict-style construction does not apply defaults.
    sparse2 = Person({"name": "Carol"})

# Generated at 2026-10-24 13:00:54.432949
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:00:56.846207
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:00:59.259603
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:01:01.673017
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:01:04.085770
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:01:06.499360
# Unit test for method __setitem__ of class SchemaDefinitions

# Generated at 2026-10-24 13:01:08.913547
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:01:42.395377
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():from typesystem.schemas import Schema

# Generated at 2026-10-24 13:02:38.828750
# Unit test for constructor of class Reference
def test_Reference():
    import pytest

    class Example(Schema):
        pass

    # 1. `to` as string, no definitions
    ref = Reference

# Generated at 2026-10-24 13:02:55.827638
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:02:58.244351
# Unit test for constructor of class Reference

# Generated at 2026-10-24 13:03:00.656814
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:03:03.083482
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:03:05.500450
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:03:07.912933
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:03:10.334238
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:03:12.751292
# Unit test for method __new__ of class SchemaMetaclass

# Generated at 2026-10-24 13:03:15.166289
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:03:17.582055
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:03:57.575354
# Unit test for constructor of class Schema
def test_Schema():from typesystem.fields import String

# Generated at 2026-10-24 13:03:59.008323
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String()
        age = Integer(default=0)

    # Fully populated -> no sparse indicator, fields in definition order.
    full = Person(name="Alice", age=30)
    assert not full.is_sparse
    assert repr(full) == "Person(name='Alice', age=30)"

    # Default is applied via kwargs path, so still not sparse.
    with_default = Person(name="Bob")
    assert with_default.age == 0
    assert not with_default.is_sparse
    assert repr(with_default) == "Person(name='Bob', age=0)"

    # Missing required field -> sparse, only set attrs shown.
    sparse = Person()
    assert sparse.is_sparse
    # `age` has a default so it is set, `name` is missing.
    assert repr(sparse) == "Person(age=0) [sparse]"

    # Dict-style construction does not apply defaults.
    sparse2 = Person({"name": "Carol"})

# Generated at 2026-10-24 13:04:19.936272
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:04:22.349599
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:04:24.763365
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:04:47.751341
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:05:03.856110
# Unit test for method __len__ of class Schema
def test_Schema___len__():from typesystem.fields import String

# Generated at 2026-10-24 13:05:25.415817
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:05:27.830003
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:06:07.318654
# Unit test for method validate of class Reference

# Generated at 2026-10-24 13:06:50.325264
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:07:12.548272
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():from typesystem.schemas import Schema

# Generated at 2026-10-24 13:07:29.646309
# Unit test for method __setitem__ of class SchemaDefinitions
def test_SchemaDefinitions___setitem__():
    # Set on empty instance.
    defs = SchemaDefinitions()
    defs["A"] = 1
    assert defs["A"] == 1
    assert len(defs) == 1
    assert list(iter(defs)) == ["A"]

    # Set a second distinct key.
    defs["B"] = 2
    assert defs["B"] == 2
    assert len(defs) == 2

    # Duplicate key must not overwrite, must raise AssertionError.
    try:
        defs["A"] = 99
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for duplicate key 'A'")
    assert defs["A"] == 1

    # Works with pre-populated definitions.
    defs2 = SchemaDefinitions({"X": "x-val"})
    defs2["Y"] = "y-val"
    assert defs2["X"] == "x-val"
    assert defs2["Y"] == "y-val"

    try:
        defs2["X"] = "other"
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for duplicate key 'X'")
    assert defs2["X"] == "x-val"

    # After delete, same key can be set again.
    del defs2["X"]
    defs2["X"] = "new-x"
    assert defs2["X"] == "new-x"

# Generated at 2026-10-24 13:08:06.510800
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:08:08.049691
# Unit test for method __len__ of class Schema
def test_Schema___len__():from typesystem.fields import String

# Generated at 2026-10-24 13:08:13.269701
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:08:39.178499
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():from typesystem.schemas import Schema

# Generated at 2026-10-24 13:09:51.677404
# Unit test for method __iter__ of class Schema
def test_Schema___iter__():from typesystem.fields import String


# Generated at 2026-10-24 13:10:13.999033
# Unit test for constructor of class Schema

# Generated at 2026-10-24 13:10:16.866440
# Unit test for constructor of class Schema
def test_Schema():from typesystem.fields import String

# Generated at 2026-10-24 13:10:19.835454
# Unit test for method __eq__ of class Schema

# Generated at 2026-10-24 13:10:21.273513
# Unit test for method __eq__ of class Schema
def test_Schema___eq__():from typesystem.schemas import Schema

# Generated at 2026-10-24 13:10:24.254235
# Unit test for method __repr__ of class Schema
def test_Schema___repr__():
    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String()
        age = Integer(default=0)

    # Fully populated -> no sparse indicator, fields in definition order.
    full = Person(name="Alice", age=30)
    assert not full.is_sparse
    assert repr(full) == "Person(name='Alice', age=30)"

    # Default is applied via kwargs path, so still not sparse.
    with_default = Person(name="Bob")
    assert with_default.age == 0
    assert not with_default.is_sparse
    assert repr(with_default) == "Person(name='Bob', age=0)"

    # Missing required field -> sparse, only set attrs shown.
    sparse = Person()
    assert sparse.is_sparse
    # `age` has a default so it is set, `name` is missing.
    assert repr(sparse) == "Person(age=0) [sparse]"

    # Dict-style construction does not apply defaults.
    sparse2 = Person({"name": "Carol"})

# Generated at 2026-10-24 13:10:47.068193
# Unit test for method __len__ of class Schema

# Generated at 2026-10-24 13:10:49.043428
# Unit test for method __len__ of class Schema
def test_Schema___len__():from typesystem.fields import String