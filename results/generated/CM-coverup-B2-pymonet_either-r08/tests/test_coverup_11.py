# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Either, Left, Right


def test_either_ap_delegates_to_applicative_map():
    def add_one(x):
        return x + 1

    func_container = Either(add_one)

    captured = {}
    sentinel = object()

    class FakeApplicative:
        def map(self, fn):
            captured["fn"] = fn
            return sentinel

    fake = FakeApplicative()
    result = func_container.ap(fake)

    assert captured["fn"] is add_one
    assert func_container.value is add_one
    assert result is sentinel


def test_either_ap_with_right_applicative_applies_function():
    func_container = Either(lambda x: x + 1)
    value_container = Right(41)

    result = func_container.ap(value_container)

    assert result == Right(42)
    assert result.value == 42


def test_left_ap_inherited_executes_base_ap():
    # Left inherits Either.ap when not overridden, so this also hits line 46.
    func_container = Left(lambda x: x * 2)
    value_container = Right(21)

    result = Either.ap(func_container, value_container)

    assert result == Right(42)
    assert result.value == 42
