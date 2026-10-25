# file: project/typesystem/schemas.py:166-173
# asked: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}
# gained: {"lines": [167, 168, 170, 171, 172, 173], "branches": [[167, 168], [167, 170], [170, 171], [170, 173], [171, 170], [171, 172]]}

import pytest
from typesystem import String
from typesystem.schemas import Schema


class ExampleSchema(Schema):
    name = String()
    age = String()


@pytest.fixture(autouse=True)
def _no_state_pollution(monkeypatch):
    # ExampleSchema is defined at module level in this test module only;
    # nothing is registered globally by SchemaMetaclass unless definitions
    # are passed, so no monkeypatching is strictly required. This fixture
    # guards against accidental attribute leakage on the class.
    yield
    monkeypatch.delattr(ExampleSchema, "fields", raising=False)


def test_eq_returns_false_for_non_schema_instance():
    schema = ExampleSchema()
    assert (schema == "not a schema") is False
    assert (schema != "not a schema") is True


def test_eq_returns_false_for_other_class_instance():
    class OtherSchema(Schema):
        name = String()

    schema = ExampleSchema()
    other = OtherSchema()
    assert (schema == other) is False


def test_eq_returns_false_when_field_values_differ():
    schema = ExampleSchema()
    other = ExampleSchema()
    schema.name = "alice"
    other.name = "different"
    assert (schema == other) is False


def test_eq_returns_true_when_all_fields_equal():
    schema = ExampleSchema()
    other = ExampleSchema()
    schema.name = "alice"
    schema.age = "30"
    other.name = "alice"
    other.age = "30"
    assert (schema == other) is True
    assert not (schema != other)
