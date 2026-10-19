

# Generated at 2022-06-14 03:31:29.744110
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    pass

# Generated at 2022-06-14 03:31:33.391529
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    >>> def add(a):
    ...     return a + 10
    >>> Lazy(lambda: 1).bind(lambda arg: Lazy(lambda: add(arg))).get()
    11
    """
    pass


# Generated at 2022-06-14 03:31:39.336820
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_fn_1(value):
        return Lazy.of(value + 1)

    def test_fn_2(value):
        return Lazy.of(value + 2)

    assert Lazy.of(2).bind(test_fn_1).bind(test_fn_2).get() == 5



# Generated at 2022-06-14 03:31:44.818048
# Unit test for method get of class Lazy
def test_Lazy_get():
    import pytest

    class Example:
        pass

    # Given
    lazy = Lazy(Example)

    # When
    result = lazy.get()

    # Then
    assert isinstance(result, Example)
    assert lazy.is_evaluated
    assert result == lazy.value


# Generated at 2022-06-14 03:31:53.612647
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.monad_try import Try

    def throwing_fn():
        raise Exception('error')

    def no_throwing_fn():
        return 42

    fn_try = Try.of(throwing_fn)
    try_no_fn = Lazy(lambda: fn_try.get())
    try_no_fn_same = Lazy(lambda: fn_try.get())
    try_no_fn_different = Lazy(lambda: fn_try.get()).map(lambda x: x + 1)
    fn_try_no_fn = Try.of(no_throwing_fn)
    no_throwing_fn_try_no_fn = Lazy(lambda: fn_try_no_fn.get())

    assert try_no_fn == try_no_fn_same
    assert try_no

# Generated at 2022-06-14 03:31:54.970990
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda a: a * 2).get() == 2



# Generated at 2022-06-14 03:32:05.182918
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    import unittest

    class TestLazy___eq__(unittest.TestCase):

        def test_should_return_false_when_comparing_empty_lazies_with_different_constructor_fn(self):
            # GIVEN
            left = Lazy(lambda: None)
            right = Lazy(lambda: 1)

            # WHEN
            actual = left == right

            # THEN
            self.assertFalse(actual)

        def test_should_return_false_when_comparing_not_empty_lazies_with_different_constructor_fn(self):
            # GIVEN
            left = Lazy(lambda: None)
            right = Lazy(lambda: 1)
            left.get()
            right.get()

            # WHEN

# Generated at 2022-06-14 03:32:13.678926
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try

    def foo(x: int) -> int:
        return x + 3

    def bar(y: int) -> Try[int]:
        return Try.of(lambda x: x + 2, y)

    lazy = Lazy(foo)
    res = lazy.bind(bar)
    assert res == Lazy.of(7)

    # to make mypy happy
    assert lazy.constructor_fn(0) == 3
    assert res.constructor_fn(0) == 7

# Generated at 2022-06-14 03:32:17.037181
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(1).get() == 1
    assert Lazy.of(2).get() == 2
    assert Lazy.of('test').get() == 'test'
    assert Lazy.of('test').get(lambda value: value)() == 'test'


# Generated at 2022-06-14 03:32:20.553130
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    """Test for Lazy get method."""
    lazy = Lazy(lambda x: x * 2)
    assert lazy.get(2) == 4

# Generated at 2022-06-14 03:32:25.429123
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy(lambda a: a) != Lazy(lambda a: a)
    assert Lazy(lambda a: a).get(5) == Lazy(lambda a: a).get(5)
    assert Lazy(lambda a: a).get(5) != Lazy(lambda a: a).get(6)



# Generated at 2022-06-14 03:32:32.423016
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def fn(x):
        return x*x

    def fn2(x, y):
        return x+y

    Lazy1 = Lazy(fn2)
    Lazy2 = Lazy(fn2)
    Lazy3 = Lazy(fn)

    assert Lazy1 == Lazy2
    assert Lazy1 != Lazy3
    assert Lazy1 != 'string'


# Generated at 2022-06-14 03:32:36.883686
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy = Lazy.of('lazy')
    mapper = Lazy.of(lambda x: x + '-ap')

    result = lazy.ap(mapper)

    assert result == Lazy.of(lambda: 'lazy-ap')

# Generated at 2022-06-14 03:32:47.312484
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.stream import Stream
    from pymonet.box import Box
    from pymonet.list import List

    assert Lazy.of(10).bind(lambda x: Lazy.of(x + 1)).get() == 11

    def lazy_mapper_with_params(x, y):
        return Lazy.of(x + y)

    assert (
        Lazy.of(10).bind(lambda x: lazy_mapper_with_params(x, 2))
        .bind(lambda x: lazy_mapper_with_params(x, 3))
        .get()
        == 15
    )

    assert Lazy.of(10).map(lambda x: x + 1).bind(lambda x: Lazy.of(x + 1)).get() == 12


# Generated at 2022-06-14 03:32:50.112249
# Unit test for method get of class Lazy
def test_Lazy_get():
    test_function = lambda x: x
    lazy_monad = Lazy.of(test_function)

    assert lazy_monad.get() == test_function

# Generated at 2022-06-14 03:32:51.991687
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(1).bind(lambda x: Lazy.of(x * 5)).get() == 1 * 5



# Generated at 2022-06-14 03:32:55.166376
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    f = Lazy(lambda a: a + 1)
    x = Lazy(2)
    ap = x.ap(f)
    assert ap.get() == 3



# Generated at 2022-06-14 03:32:57.617149
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(x):
        return lambda y: x + y

    assert Lazy.of(1).ap(Lazy.of(add)).get() == 2



# Generated at 2022-06-14 03:32:59.772147
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy(lambda: 1).get() == 1
    assert Lazy(lambda x: x + 2).get(2) == 4
    assert Lazy(lambda: 2).get() == 2



# Generated at 2022-06-14 03:33:07.130772
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    func_stub = MagicMock()
    val_stub = MagicMock()

    lazy = Lazy(lambda: func_stub(1))

    def bind_fn(a):
        return Lazy(lambda: val_stub(a))

    lazy.bind(bind_fn)

    assert func_stub.called_once_with(1)
    assert val_stub.called_once_with(1)



# Generated at 2022-06-14 03:33:12.674448
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(12).get() == 12


# Generated at 2022-06-14 03:33:17.018538
# Unit test for method map of class Lazy
def test_Lazy_map():
    def function(x):
        return x*x

    def mapper(x):
        return x*x*x

    assert Lazy.of(2).map(mapper).get() == 8

    assert Lazy.of(function).map(mapper).get(2) == 64



# Generated at 2022-06-14 03:33:21.230719
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x):
        return Lazy(lambda: x + 5)

    assert Lazy(lambda: 2).bind(fn).get() == 7
    assert Lazy(lambda: 2).bind(fn).value == 7
    assert Lazy(lambda: 2).bind(fn).is_evaluated == True

# Unit tests for class Lazy

# Generated at 2022-06-14 03:33:25.659834
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.monad_try import Try

    # Given function
    increment_or_die = lambda x: Try.of(lambda: x + 1)

    # When folded with bind
    lazy = Lazy.of(0).bind(increment_or_die).bind(increment_or_die).bind(increment_or_die)

    # Then
    assert lazy.get() == Try.of(3)



# Generated at 2022-06-14 03:33:29.442224
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.either import Right

    assert Lazy.of(lambda x: x * 2).ap(Right(3)) == Lazy.of(6)



# Generated at 2022-06-14 03:33:40.049102
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    """
    Test get method of Lazy class
    """
    result = Lazy(lambda: 1).get()
    assert result == 1

    lazy_double = Lazy(lambda value: value * 2)
    double_lazy = lazy_double.map(lambda x: Lazy(lambda: x * 2)).get()

    result = double_lazy.get()
    assert result == 4

    result = double_lazy.get()
    assert result == 4

    result = double_lazy.get()
    assert result == 4

    lazy_triple = Lazy(lambda value: value * 3)
    triple_lazy = lazy_triple.map(lambda x: Lazy(lambda: x * 3)).get()

    result = triple_lazy.get()
    assert result == 9

    result

# Generated at 2022-06-14 03:33:47.821666
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def constructor_fn_1(x):
        return x + 1
    def constructor_fn_2(x):
        return x + 1

    assert Lazy(constructor_fn_1) == Lazy(constructor_fn_2)
    assert Lazy(constructor_fn_1) != Lazy(constructor_fn_1)
    assert Lazy(constructor_fn_1) != Lazy(constructor_fn_1).get()
    assert Lazy(constructor_fn_1) != Lazy(constructor_fn_1).get()


# Generated at 2022-06-14 03:33:54.082087
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    Test for method ap of class Lazy
    """
    from pymonet.either import Right, Left
    right = Right(lambda x: x + 1)
    left = Left(None)

    assert Lazy.of(1).ap(Lazy.of(lambda x: x + 1)).get() == 2
    assert Lazy.of(1).ap(right).get() == 2
    assert Lazy.of(1).ap(left).to_either().is_left()



# Generated at 2022-06-14 03:34:03.044901
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda x: x+1).bind(lambda x: Lazy(lambda y: x+y)).get(1, 2) == 4
    assert Lazy(lambda x: x+10).bind(lambda x: Lazy(lambda y: x+y)).get(1, 2) == 13
    assert Lazy(lambda x: x+1).bind(lambda x: Lazy(lambda y: x+y)).get(5, 10) == 16
    assert Lazy(lambda x: x+10).bind(lambda x: Lazy(lambda y: x+y)).get(5, 10) == 25



# Generated at 2022-06-14 03:34:15.167790
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Tests for Lazy.bind
    """

    def add1(value):
        return value + 1

    def add2(value):
        return value + 2

    def add1_lazy(value):
        return Lazy.of(value + 1)

    lazy_v1 = Lazy(lambda: 1)
    lazy_v2 = Lazy(lambda: 2)

    empty_lazy = Lazy(None)
    empty_lazy_binded = empty_lazy.bind(add1_lazy)

    assert empty_lazy_binded.is_evaluated is False
    assert empty_lazy_binded.value is None
    assert empty_lazy_binded.get() == 1

    lazy_v1_binded = lazy_v1.bind(add1_lazy)


# Generated at 2022-06-14 03:34:27.445547
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add(x, y):
        return x + y

    lazy_add = Lazy(add)
    lazy_5 = Lazy.of(5)
    lazy_3 = Lazy.of(3)
    lazy_result = lazy_add.ap(lazy_5).ap(lazy_3)
    assert(lazy_result.get() == 8)


# Generated at 2022-06-14 03:34:32.165461
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def foo(x):
        return x + 2
    assert Lazy(foo) != Lazy(foo)
    assert Lazy(foo).map(lambda x: x).fold(lambda x: x) == Lazy(foo).map(lambda x: x).fold(lambda x: x)
    assert Lazy(foo).map(lambda x: x + 2) != Lazy(foo).map(lambda x: x + 3)



# Generated at 2022-06-14 03:34:37.027615
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.function import Function

    def to_box(value):
        return Box(value)

    x = Lazy(lambda: 15)
    binded = x.bind(Function.of(to_box))  # type: ignore # noqa E501
    assert binded.get() == Box(15)

# Generated at 2022-06-14 03:34:42.221562
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def assert_lazy_map(value, mapper):
        assert Lazy.of(lambda x: x).bind(lambda f: Lazy.of(f)).map(mapper).get(value) == mapper(value)

    assert_lazy_map(10, lambda v: v + 1)
    assert_lazy_map(10, 'str')



# Generated at 2022-06-14 03:34:46.153417
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x):
        return Lazy(lambda: x + 10)

    lazy = Lazy(lambda: 2).bind(fn)
    assert lazy.get() == 12

# Generated at 2022-06-14 03:34:56.434894
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.monad_try import Failure
    from pymonet.validation import Invalid

    lazy = Lazy.of(4)
    assert lazy.value == 4

    lazy = Lazy.of(4).map(lambda x: x * 2)
    assert lazy.get() == 8
    assert lazy.get() == 8

    lazy = Lazy.of(4).map(lambda x: x * 2).map(lambda x: x + 4)
    assert lazy.get() == 12
    assert lazy.get() == 12

    lazy = Lazy.of(4).map(lambda x: Failure(x))
    assert lazy.get() == Failure(4)
    assert lazy.get() == Failure(4)

    lazy = Lazy.of(4).map(lambda x: Invalid('error'))
    assert lazy.get()

# Generated at 2022-06-14 03:34:59.793842
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(2).map(lambda x: x+1) == Lazy.of(3)


# Generated at 2022-06-14 03:35:09.334940
# Unit test for method bind of class Lazy
def test_Lazy_bind(): #pragma: no cover
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    def bind_fn(a: int) -> Lazy[int, int]:
        return Lazy(lambda b: a * b)

    def mapper(a: int) -> int:
        return a * 2

    def validator(a: int) -> Validation[int, []]:
        return Validation.success(a)

    def mapper2(a: int) -> int:
        return a * 3

    lazy = Lazy(lambda: 5)
    assert lazy.bind(bind_fn).bind(mapper).bind(mapper2).get(2) == 30
    assert lazy.bind(bind_fn).bind(mapper).get(2) == 20


# Generated at 2022-06-14 03:35:21.592560
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from pymonet.test.functions.functions import add
    from pymonet.test.functions.functions import sub

    a_1_lazy = Lazy(add)(1)
    a_2_lazy = Lazy(add)(2)
    b_3_lazy = Lazy(add)(3)

    assert a_1_lazy == a_1_lazy
    assert a_1_lazy != a_2_lazy
    assert a_1_lazy != b_3_lazy

    assert a_1_lazy != 1

    a_1_lazy1 = Lazy(add)
    a_1_lazy2 = Lazy(add)
    a_2_lazy3 = Lazy(sub)

    assert a_1_lazy

# Generated at 2022-06-14 03:35:26.928766
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try

    def f(x):
        return Lazy(lambda *args: x * 10)

    assert Lazy.of(5).bind(f).get() == 50

    def f(x):
        return Try.of(lambda: x * 10)

    assert Lazy.of(5).bind(f).get() == 50



# Generated at 2022-06-14 03:35:48.468581
# Unit test for method get of class Lazy
def test_Lazy_get():
    def add(a: int, b: int) -> int:
        return a + b

    def mul(a: int, b: int, c: int) -> int:
        return a * b * c

    lazy_add = Lazy(add)
    lazy_mul = Lazy(mul)
    add_result = lazy_add.get(2, 3)
    mul_result = lazy_mul.get(4, 5, 6)

    assert add_result == 5
    assert mul_result == 120


# Generated at 2022-06-14 03:35:50.904640
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def fn(x): return x + 5

    assert Lazy(fn).get(2) == 7



# Generated at 2022-06-14 03:35:56.623819
# Unit test for method get of class Lazy
def test_Lazy_get():
    # Arrange
    def _fn(*args):
        return args[0] + args[1]

    lazy = Lazy(_fn)

    # Act
    result = lazy.get(1, 2)

    # Assert
    assert result is 3


# Generated at 2022-06-14 03:36:05.572877
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    def constructor(x):
        return x + 1

    lazy_1 = Lazy.of(2)
    lazy_2 = Lazy.of(2)
    lazy_3 = Lazy(constructor)
    lazy_4 = Lazy(lambda: Maybe(3))
    lazy_5 = Lazy(lambda: Try(constructor, 3))
    assert Lazy.of(5) == Lazy.of(5)
    assert Lazy(lambda: 3) == Lazy(lambda: 3)
    assert lazy_1 == lazy_1
    assert lazy_2 == lazy_2
    assert lazy_3 == lazy_3
    assert lazy_1 == lazy_2
    assert lazy_4 == lazy_4

# Generated at 2022-06-14 03:36:07.591264
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(1).map(lambda a: a + 2).get() == 3


# Generated at 2022-06-14 03:36:12.081010
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    a_lazy = Lazy.of(lambda x: x + 12)
    b_lazy = Lazy.of(12)
    assert a_lazy.ap(b_lazy).get() == 24
    assert b_lazy.ap(a_lazy).get() == 24



# Generated at 2022-06-14 03:36:16.523294
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # Test for not empty structure
    @Lazy
    def divide(value):
        return value / 10

    @Lazy
    def add(value):
        return value + 1

    assert divide.bind(add).get(10) == 2

    # Test for empty structure
    @Lazy
    def empty():
        raise ValueError('empty')

    @Lazy
    def empty_add(value):
        return value + 1

    assert empty.bind(empty_add).get() == 2


# Generated at 2022-06-14 03:36:17.674257
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    pass

# Generated at 2022-06-14 03:36:23.994101
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: "1").bind(lambda x: Lazy(lambda: x + "2")).get() == "12"
    assert Lazy(lambda: "1").bind(lambda x: Lazy(lambda: x + "2")).bind(lambda x: Lazy(lambda: x + "3")).get() == "123"
    assert Lazy(lambda: "1").map(lambda x: x + "2").map(lambda x: x + "3").get() == "123"


# Generated at 2022-06-14 03:36:27.157151
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(4).get() == 4
    assert Lazy.of(4)('a') == 4



# Generated at 2022-06-14 03:36:44.980365
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.identity import Identity

    fn = lambda a: a

    assert Lazy(fn).__eq__(None) is False
    assert Lazy(fn).__eq__(Lazy(fn))

    assert Lazy(fn).__eq__(Identity(fn)) is False


# Generated at 2022-06-14 03:36:56.270626
# Unit test for method get of class Lazy
def test_Lazy_get():
    def f(x):  # pylint: disable=C0111
        return x + 5

    def g(x):  # pylint: disable=C0111
        return x * 5

    x = Lazy.of(5)

    assert x.get() == 5
    assert x.map(f).get() == 10
    assert x.map(f).map(g).get() == 50
    assert x.map(g).map(f).get() == 30

    def recusive_fn(x):  # pylint: disable=C0111
        return x + 1 if x < 10 else recusive_fn(x - 1)

    assert Lazy.of(0).bind(lambda x: Lazy(recusive_fn)).get() == 10
    assert Lazy(recusive_fn).get(0) == 10

# Generated at 2022-06-14 03:36:59.845203
# Unit test for method get of class Lazy
def test_Lazy_get():

    def f(*args):
        return args[0] + args[1]

    lazy = Lazy(f)

    assert lazy.get(1, 2) == 3


# Generated at 2022-06-14 03:37:07.130979
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    assert Lazy.of(lambda x: x + 10).ap(Box(20)) == Lazy.of(30)
    assert Lazy.of(lambda x, y: x + y).ap(Box(20)).ap(Box(10)) == Lazy.of(30)

    assert Lazy.of(lambda x: x + 10).ap(Maybe.just(20)) == Lazy.of(30)
    assert Lazy.of(lambda x, y: x + y).ap(Maybe.just(20)).ap(Maybe.just(10)) == Lazy.of(30)


# Generated at 2022-06-14 03:37:10.040420
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def f(x):
        return x*2
    result = Lazy(42).ap(Lazy(f))
    assert result == Lazy(84)


# Generated at 2022-06-14 03:37:18.444049
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor
    from pymonet.applicative_functor import ApplicativeFunctor

    assert not Lazy.of(lambda value: Functor.of(2*value)).ap(Functor.of(1)).is_evaluated
    assert Lazy.of(lambda value: Functor.of(2*value)).ap(Functor.of(1)).get() == Functor.of(2)
    assert not Lazy.of(lambda value: ApplicativeFunctor.pure(2*value)).ap(ApplicativeFunctor.pure(1)).is_evaluated
    assert Lazy.of(lambda value: ApplicativeFunctor.pure(2*value)).ap(ApplicativeFunctor.pure(1)).get() == ApplicativeFunctor.pure(2)



# Generated at 2022-06-14 03:37:24.246235
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    lazy = Lazy(lambda x: x)
    assert lazy == lazy

    lazy2 = Lazy(lambda x: x)
    assert lazy == lazy2

    lazy3 = Lazy(lambda x: x + 1)
    assert lazy != lazy3

    lazy.get()
    assert lazy == lazy2

    lazy2.get()
    assert lazy == lazy2

    lazy3.get()
    assert lazy != lazy3



# Generated at 2022-06-14 03:37:26.667168
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    assert Lazy.of('text').get() == 'text'
    assert Lazy.of(5).get() == 5



# Generated at 2022-06-14 03:37:30.647682
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    fn = lambda a: a
    def value(): return 1

    first = Lazy(fn)
    second = Lazy(fn)
    third = Lazy(value)

    assert first == second
    assert first != Lazy(value)
    assert third == Lazy(value)



# Generated at 2022-06-14 03:37:41.137269
# Unit test for method get of class Lazy
def test_Lazy_get():
    def add_one(a):
        return a + 1

    def return_two():
        return 2

    def return_three():
        return 3

    assert Lazy(return_two).get() == 2
    assert Lazy(return_two).map(add_one).get() == 3
    assert Lazy(return_two).map(add_one).map(add_one).get() == 4
    assert Lazy(return_two).map(add_one).map(add_one).map(add_one).get() == 5
    assert Lazy(return_two).map(return_three).get() == 3
    assert Lazy(return_two).map(return_three).map(add_one).get() == 4

# Generated at 2022-06-14 03:38:10.854822
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(5).bind(lambda x: Lazy.of(x + 1)).get() == 6



# Generated at 2022-06-14 03:38:13.922370
# Unit test for method get of class Lazy
def test_Lazy_get():
    def fn():
        return 42

    assert Lazy(fn).get() == 42



# Generated at 2022-06-14 03:38:18.012358
# Unit test for method get of class Lazy
def test_Lazy_get():
    def fn():
        return 1

    assert Lazy(fn).get() == 1
    assert Lazy(fn).get() == 1
    assert Lazy(fn).get() == 1

# Generated at 2022-06-14 03:38:20.646989
# Unit test for method get of class Lazy
def test_Lazy_get():
    # given
    foo_value = 'foo'
    lazy = Lazy.of(foo_value)

    # when
    value = lazy.get()

    # then
    assert value == foo_value



# Generated at 2022-06-14 03:38:27.951584
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def f(x):
        return Lazy(lambda _: x * 3)

    assert Lazy(f).bind(f).get(0) == 27

    # Map function
    mx = Lazy(lambda x: x * 2).map(lambda x: x * 3)
    assert mx.get(2) == 12

    # Ap function
    mx = Lazy(lambda x: x * 2)
    assert mx.ap(Lazy(lambda x: x * 3)).get(2) == 12

    # Test to_box method
    from pymonet.box import Box

    assert Lazy(lambda: 'test').to_box() == Box('test')

    # Test to_either
    from pymonet.either import Right

    assert Lazy(lambda: 5).to_either() == Right(5)

    #

# Generated at 2022-06-14 03:38:37.671323
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def fn1(x: int) -> int:
        return x

    def fn2(x: int) -> int:
        return x

    assert Lazy.of(1) == Lazy.of(1)
    assert Lazy.of(1) != Lazy.of(2)
    assert Lazy.of(2) != Lazy.of(1)
    assert Lazy(fn1) != Lazy(fn2)
    assert Lazy(fn1) == Lazy(fn1)
    assert Lazy(fn1) != Lazy(fn2)
    assert Lazy(fn1) == Lazy(fn1)


# Generated at 2022-06-14 03:38:42.207403
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # Given
    def fn_reverse_text(text: str) -> str:
        return text[::-1]

    def fn_add_prefix(prefix, text):
        return '{} {}'.format(prefix, text)

    # When
    lazy_fn_reverse_text = Lazy.of(fn_reverse_text)

    lazy_fn_add_prefix = Lazy.of(fn_add_prefix).bind(lambda x: Lazy(x))

    result = lazy_fn_reverse_text.bind(lambda x: lazy_fn_add_prefix.bind(lambda y: Lazy(y)))

    # Then
    assert result.get('foo') == 'oof'
    assert result.get() == 'foo '



# Generated at 2022-06-14 03:38:43.871860
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy(lambda: 'test_string')

    assert lazy.get() == 'test_string'


# Generated at 2022-06-14 03:38:47.078918
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def test_function(value):
        return Lazy.of(value+1)

    assert Lazy.of(2).bind(test_function) == Lazy.of(3)


# Generated at 2022-06-14 03:38:53.065599
# Unit test for method get of class Lazy
def test_Lazy_get():
    """Testing Lazy.get() method."""

    # case: function returning string
    assert Lazy.of(True).get() is True
    assert Lazy.of(None).get() is None
    assert Lazy.of('test').get() == 'test'

    # case: function returning list
    assert Lazy.of([]).get() == []
    assert Lazy.of([1, 2, 3]).get() == [1, 2, 3]

    # case: function returning dict
    assert Lazy.of({}).get() == {}
    assert Lazy.of({'a': 1, 'b': 2}).get() == {'a': 1, 'b': 2}



# Generated at 2022-06-14 03:39:58.103895
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    assert Lazy(lambda x: x) == Lazy(lambda x: x)
    assert Lazy(lambda x: x) != Lazy(lambda y: y)

    def fn(x): return x

    def fn2(x): return x + 1

    assert Lazy(fn) != Lazy(fn2)
    assert Lazy(fn) != Lazy(fn2)
    assert Lazy(fn) == Lazy(fn)

    assert Lazy(fn).ap(Lazy(fn)) != Lazy(fn).ap(Lazy(fn2))
    assert Lazy(fn).ap(Lazy(fn)) != Lazy(fn2).ap(Lazy(fn))
    assert Lazy(fn).ap(Lazy(fn)) != Lazy(fn2).ap(Lazy(fn2))

# Generated at 2022-06-14 03:40:02.488822
# Unit test for method map of class Lazy
def test_Lazy_map():
    def f(x):
        return lambda *args: x + args[0]

    lazy: Lazy[int, Callable[[int], int]] = Lazy(f).map(lambda x: x(2))

    actual: int = lazy.get(1)
    expected: int = 3

    assert actual == expected



# Generated at 2022-06-14 03:40:09.076011
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy({'test': 'val'}.get).map(lambda x: x['test']).get('test') == 'val'
    assert Lazy.of(3).map(lambda x: x * 10).get() == 30
    assert Lazy.of(['a', 'b', 'c']).map(lambda x: ''.join(x)).get() == 'abc'

# Generated at 2022-06-14 03:40:20.276606
# Unit test for method get of class Lazy
def test_Lazy_get():
    fn = lambda: 2 + 2

    lazy = Lazy(fn)

    # lazy should be not evaluated and have no value before call get method
    assert lazy.is_evaluated is False
    assert lazy.value is None

    # get method should evaluate function, memoize result and return result
    # second call with same arguments should return cached result
    assert lazy.get(1, 2) == 4
    assert lazy.get(1, 2) == 4

    assert fn.call_count == 1

    # lazy should be evaluated and have value after call get method
    assert lazy.is_evaluated is True
    assert lazy.value == 4


# Generated at 2022-06-14 03:40:30.072036
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    stub_fn = lambda p: p

    assert Maybe.nothing().ap(Lazy(lambda x: x)) == Maybe.nothing()
    assert Maybe.just('something').ap(Lazy(lambda x: x)) == Maybe.just('something')
    assert Maybe.just(Lazy(stub_fn)).ap(Lazy(lambda x: x)) == Maybe.just(stub_fn)

    assert Validation.success('something').ap(Lazy(lambda x: x)) == Validation.success('something')
    assert Validation.success(Lazy(stub_fn)).ap(Lazy(lambda x: x)) == Validation.success(stub_fn)
    assert Validation.fail('').ap(Lazy(lambda x: x))

# Generated at 2022-06-14 03:40:40.628676
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def _inc_5_fn(value):
        return value + 5

    def _inc_fn(value):
        return value + 1

    lazy_value = Lazy(lambda *args: 500)
    inc_500 = lazy_value.bind(_inc_fn)
    assert inc_500.get() == 501
    assert inc_500.get() == 501

    inc_500_inc = inc_500.bind(_inc_fn)
    assert inc_500_inc.get() == 502
    assert inc_500_inc.get() == 502

    lazy_value = Lazy(lambda *args: 500)
    inc_500 = lazy_value.bind(_inc_fn)
    assert inc_500.get() == 501
    assert inc_500.get() == 501


# Generated at 2022-06-14 03:40:43.598807
# Unit test for method get of class Lazy
def test_Lazy_get():
    def my_function(*args):
        return 42

    lazy_instance = Lazy(my_function)

    assert lazy_instance.get('argument1', 'argument2', 'argument3') == 42
    assert lazy_instance.is_evaluated



# Generated at 2022-06-14 03:40:51.315147
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # given
    def add1(v: int) -> Lazy:
        return Lazy.of(v + 1)

    def mul2(v: int) -> Lazy:
        return Lazy.of(v * 2)

    lazy = Lazy(lambda x: x)
    # when
    result = lazy.bind(add1).bind(mul2)
    # then
    assert result.get() == lazy.get() * 2 + 1



# Generated at 2022-06-14 03:40:52.937379
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(5).get() == 5



# Generated at 2022-06-14 03:40:57.897268
# Unit test for method map of class Lazy
def test_Lazy_map():
    #pylint: disable=cell-var-from-loop
    lazy = Lazy(lambda value: value)
    for i in range(0, 10):
        def mapper(i):
            def mapper_fn(arg):
                return arg + i
            return mapper_fn

        assert lazy.map(mapper(i)).get(1) == 1 + i
