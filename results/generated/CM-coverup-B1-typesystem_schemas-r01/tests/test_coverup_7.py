# file: project/typesystem/schemas.py:192-201
# asked: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [193, 194, 195, 197, 198, 200, 201], "branches": []}

import datetime

import typesystem


def test_repr_sparse_schema():
    class Album(typesystem.Schema):
        title = typesystem.String()
        release_date = typesystem.Date()

    album = Album(title="Double Negative")

    assert album.is_sparse is True
    assert repr(album) == "Album(title='Double Negative') [sparse]"


def test_repr_complete_schema():
    class Album(typesystem.Schema):
        title = typesystem.String()
        release_date = typesystem.Date()

    release_date = datetime.date(1970, 1, 1)
    album = Album(title="Double Negative", release_date=release_date)

    assert album.is_sparse is False
    assert repr(album) == (
        f"Album(title='Double Negative', release_date={release_date!r})"
    )


def test_repr_empty_sparse_schema():
    class Empty(typesystem.Schema):
        title = typesystem.String()

    empty = Empty()

    assert empty.is_sparse is True
    assert repr(empty) == "Empty() [sparse]"
