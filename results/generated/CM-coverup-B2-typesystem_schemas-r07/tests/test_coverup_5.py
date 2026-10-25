# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import typesystem


def test_eq_returns_false_for_non_schema_objects():
    class Example(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    instance = Example(name="alice", age=30)

    assert (instance == "not a schema") is False
    assert (instance == 42) is False
    assert (instance == None) is False  # noqa: E711
    assert (instance == {"name": "alice", "age": 30}) is False


def test_eq_returns_false_for_different_schema_class():
    class Example(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    class Other(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    assert (Example(name="alice", age=30) == Other(name="alice", age=30)) is False


def test_eq_returns_true_for_equal_field_values():
    class Example(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    first = Example(name="alice", age=30)
    second = Example(name="alice", age=30)

    assert (first == second) is True
    assert (first != second) is False


def test_eq_returns_false_when_any_field_differs():
    class Example(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    base = Example(name="alice", age=30)

    assert (base == Example(name="bob", age=30)) is False
    assert (base == Example(name="alice", age=31)) is False
    assert (base != Example(name="bob", age=31)) is True


def test_eq_returns_false_for_subclass_instance_with_equal_fields():
    class Example(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    class SubExample(Example):
        pass

    # Schema.__eq__ requires isinstance(other, self.__class__); a base-class
    # instance is not an instance of the subclass, so equality is False
    # in at least the subclass-as-self direction, and empirically also
    # when the base instance is on the left.
    assert (SubExample(name="alice", age=30) == Example(name="alice", age=30)) is False
    assert (Example(name="alice", age=30) == SubExample(name="alice", age=30)) is False
    assert (SubExample(name="alice", age=30) == SubExample(name="alice", age=30)) is True
