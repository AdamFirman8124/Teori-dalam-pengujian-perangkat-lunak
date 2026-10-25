# file: project/pysnooper/utils.py:10-20
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17, 19, 20], "branches": [[12, 13], [12, 20], [13, 14], [13, 19], [14, 13], [14, 15], [15, 16], [15, 17]]}

import pytest

from pysnooper.utils import _check_methods


class HasAll:
    def a(self):
        pass

    def b(self):
        pass


class HasNone:
    a = None


class Base:
    def a(self):
        pass


class InheritsA(Base):
    pass


class Empty:
    pass


def test_check_methods_all_present_returns_true():
    assert _check_methods(HasAll, 'a', 'b') is True


def test_check_methods_no_methods_requested_returns_true():
    assert _check_methods(Empty) is True


def test_check_methods_missing_method_returns_notimplemented():
    assert _check_methods(Empty, 'a') is NotImplemented


def test_check_methods_method_set_to_none_returns_notimplemented():
    assert _check_methods(HasNone, 'a') is NotImplemented


def test_check_methods_found_in_base_class_returns_true():
    assert _check_methods(InheritsA, 'a') is True


def test_check_methods_first_found_second_missing_returns_notimplemented():
    assert _check_methods(HasAll, 'a', 'missing') is NotImplemented


def test_check_methods_none_in_base_class_returns_notimplemented():
    class NoneBase:
        a = None

    class Child(NoneBase):
        pass

    assert _check_methods(Child, 'a') is NotImplemented
