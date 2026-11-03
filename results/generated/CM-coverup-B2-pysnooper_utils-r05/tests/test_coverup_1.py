# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

from pysnooper import utils


class HasMethod:
    def foo(self):
        return 'foo'


class HasNoneMethod:
    foo = None


class InheritsNone(HasNoneMethod):
    pass


class InheritsMethod(HasMethod):
    pass


class ShadowsWithNone(HasMethod):
    foo = None


class TestCheckMethods:
    def test_single_method_present(self):
        """Method found directly on the class -> True (covers break)."""
        assert utils._check_methods(HasMethod, 'foo') is True

    def test_multiple_methods_all_present(self):
        class Both:
            def foo(self):
                pass

            def bar(self):
                pass

        assert utils._check_methods(Both, 'foo', 'bar') is True

    def test_no_methods_requested(self):
        """No methods to check -> immediately True (covers `return True`)."""
        assert utils._check_methods(HasMethod) is True

    def test_method_found_in_base_class(self):
        """Method found somewhere along the MRO, not on the class itself."""
        assert utils._check_methods(InheritsMethod, 'foo') is True

    def test_method_missing_entirely(self):
        """Method not in any class of the MRO -> NotImplemented (for-else)."""
        assert utils._check_methods(HasMethod, 'baz') is NotImplemented

    def test_method_missing_after_present_method(self):
        """First method found, second missing -> NotImplemented."""
        assert utils._check_methods(HasMethod, 'foo', 'baz') is NotImplemented

    def test_method_is_none(self):
        """Method present but set to None -> NotImplemented."""
        assert utils._check_methods(HasNoneMethod, 'foo') is NotImplemented

    def test_method_is_none_inherited_via_mro(self):
        """None-valued method discovered on a base class -> NotImplemented."""
        assert utils._check_methods(InheritsNone, 'foo') is NotImplemented

    def test_present_method_followed_by_none_method(self):
        """First method found, second is None -> NotImplemented."""

        class Mixed:
            def foo(self):
                pass

            bar = None

        assert utils._check_methods(Mixed, 'foo', 'bar') is NotImplemented

    def test_shadowing_none_overrides_parent_method(self):
        """A None-valued override hides a real parent method -> NotImplemented."""
        assert utils._check_methods(ShadowsWithNone, 'foo') is NotImplemented

    def test_used_as_subclasshook(self):
        """Typical usage pattern: as the return value of __subclasshook__."""
        import abc

        class Container(abc.ABC):
            @classmethod
            def __subclasshook__(cls, other):
                if cls is Container:
                    return utils._check_methods(other, '__contains__')
                return NotImplemented

        class MyContainer:
            def __contains__(self, item):
                return True

        class NotAContainer:
            pass

        class AbstractContainer:
            __contains__ = None

        assert issubclass(MyContainer, Container) is True
        assert issubclass(NotAContainer, Container) is False
        assert issubclass(AbstractContainer, Container) is False
