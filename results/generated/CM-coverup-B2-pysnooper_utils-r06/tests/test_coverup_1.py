# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

from pysnooper import utils


def test_check_methods_finds_methods_across_mro():
    class Base:
        def inherited_method(self):
            pass

    class Child(Base):
        def own_method(self):
            pass

    assert utils._check_methods(
        Child, "own_method", "inherited_method"
    ) is True


def test_check_methods_returns_not_implemented_for_none_method():
    class Example:
        disabled_method = None

    assert (
        utils._check_methods(Example, "disabled_method")
        is NotImplemented
    )


def test_check_methods_returns_not_implemented_for_missing_method():
    class Example:
        pass

    assert (
        utils._check_methods(Example, "missing_method")
        is NotImplemented
    )
