# file: project/typesystem/schemas.py:150-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

import pytest

import typesystem


class Album(typesystem.Schema):
    title = typesystem.String(max_length=10)
    year = typesystem.Integer()


def test_validate_or_error_success():
    value = {"title": "Foo", "year": 2020}

    result = Album.validate_or_error(value)

    assert result.error is None
    assert result.value is not None
    assert result.value.title == "Foo"
    assert result.value.year == 2020


def test_validate_or_error_strict_success():
    value = {"title": "Foo", "year": 2020}

    result = Album.validate_or_error(value, strict=True)

    assert result.error is None
    assert result.value is not None
    assert result.value.title == "Foo"
    assert result.value.year == 2020


def test_validate_or_error_failure():
    value = {"title": "A much too long title", "year": "not a number"}

    result = Album.validate_or_error(value)

    assert result.value is None
    assert result.error is not None
    assert isinstance(result.error, typesystem.base.ValidationError)
    assert dict(result.error) == {
        "title": "Must have no more than 10 characters.",
        "year": "Must be a number.",
    }


def test_validate_or_error_failure_strict():
    # In strict mode, unknown keys are not allowed.
    value = {"title": "Foo", "year": 2020, "unknown": "extra"}

    result = Album.validate_or_error(value, strict=True)

    assert result.value is None
    assert result.error is not None
    assert isinstance(result.error, typesystem.base.ValidationError)
    assert "unknown" in dict(result.error)
