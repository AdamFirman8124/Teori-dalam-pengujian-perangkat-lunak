# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

from pysnooper.utils import _check_methods


def test_check_methods_finds_methods_across_mro():
    class Base:
        inherited_method = object()

    class Child(Base):
        local_method = object()

    assert _check_methods(Child, "inherited_method", "local_method") is True


def test_check_methods_returns_not_implemented_for_none_method():
    class Base:
        disabled_method = None

    class Child(Base):
        pass

    assert _check_methods(Child, "disabled_method") is NotImplemented


def test_check_methods_returns_not_implemented_for_missing_method():
    class Subject:
        existing_method = object()

    assert (
        _check_methods(Subject, "existing_method", "missing_method")
        is NotImplemented
    )
