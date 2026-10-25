# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

from pysnooper.utils import _check_methods


def test_check_methods_finds_methods_across_mro():
    class Parent:
        def inherited(self):
            return "inherited"

    class Child(Parent):
        def local(self):
            return "local"

    assert _check_methods(Child, "local", "inherited") is True


def test_check_methods_returns_not_implemented_for_none_method():
    class Example:
        disabled = None

    assert _check_methods(Example, "disabled") is NotImplemented


def test_check_methods_returns_not_implemented_for_missing_method():
    class Example:
        pass

    assert _check_methods(Example, "missing") is NotImplemented


def test_check_methods_accepts_empty_method_list():
    class Example:
        pass

    assert _check_methods(Example) is True
