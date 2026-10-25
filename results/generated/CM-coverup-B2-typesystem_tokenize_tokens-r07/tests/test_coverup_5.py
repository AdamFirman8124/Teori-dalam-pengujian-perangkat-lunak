# file: project/typesystem/tokenize/tokens.py:66-71
# asked: {"lines": [67, 68, 69, 70], "branches": []}
# gained: {"lines": [67, 68, 69, 70], "branches": []}

from typesystem.tokenize.tokens import Token


class _ConcreteToken(Token):
    def _get_value(self):
        return self._value


def test_token_eq_equal():
    t1 = _ConcreteToken("hello", 0, 5, content="hello")
    t2 = _ConcreteToken("hello", 0, 5, content="hello")
    assert t1.__eq__(t2) is True
    assert (t1 == t2) is True
    assert not (t1 != t2)


def test_token_eq_non_token():
    t1 = _ConcreteToken("hello", 0, 5, content="hello")
    assert t1.__eq__("hello") is False
    assert (t1 == "hello") is False
    assert t1.__eq__(None) is False
    assert t1.__eq__(123) is False


def test_token_eq_different_value():
    t1 = _ConcreteToken("hello", 0, 5)
    t2 = _ConcreteToken("world", 0, 5)
    assert t1.__eq__(t2) is False
    assert (t1 == t2) is False
    assert (t1 != t2) is True


def test_token_eq_different_start_index():
    t1 = _ConcreteToken("hello", 0, 5)
    t2 = _ConcreteToken("hello", 1, 5)
    assert t1.__eq__(t2) is False
    assert (t1 == t2) is False
    assert (t1 != t2) is True


def test_token_eq_different_end_index():
    t1 = _ConcreteToken("hello", 0, 5)
    t2 = _ConcreteToken("hello", 0, 6)
    assert t1.__eq__(t2) is False
    assert (t1 == t2) is False
    assert (t1 != t2) is True
