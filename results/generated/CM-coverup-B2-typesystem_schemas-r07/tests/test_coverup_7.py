# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

import typesystem


def test_repr_non_sparse():
    class Example(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    instance = Example(name="alice", age=30)
    result = repr(instance)

    assert result == "Example(name='alice', age=30)"
    assert "[sparse]" not in result


def test_repr_sparse():
    class Example(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()

    instance = Example(name="alice")
    result = repr(instance)

    assert result == "Example(name='alice') [sparse]"
    assert instance.is_sparse is True


def test_repr_empty_schema():
    class Empty(typesystem.Schema):
        pass

    instance = Empty()
    result = repr(instance)

    assert result == "Empty()"
    assert instance.is_sparse is False
