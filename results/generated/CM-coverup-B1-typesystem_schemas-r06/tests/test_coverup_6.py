# file: project/typesystem/schemas.py:184-187
# asked: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

import typesystem


class PersonSchema(typesystem.Schema):
    name = typesystem.String()
    age = typesystem.Integer()


def test_iter_yields_only_set_fields():
    """
    Covers Schema.__iter__ (lines 185-187):
    - line 185: loop over self.fields
    - line 186: hasattr branch taken both ways (age is unset -> False,
      name is set -> True)
    - line 187: yield key
    """
    instance = PersonSchema(name="Alice")

    keys = list(iter(instance))

    # 'age' was never set, so hasattr(instance, 'age') is False
    # and it must not be yielded; 'name' was set and must be yielded.
    assert keys == ["name"]
    assert "age" not in keys


def test_iter_via_dict_conversion():
    """
    dict(schema) drives __iter__ as well, confirming the same lines
    execute through a common code path.
    """
    instance = PersonSchema(name="Bob", age=30)

    result = dict(instance)

    assert result == {"name": "Bob", "age": 30}
