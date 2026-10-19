

# Generated at 2022-06-14 03:31:25.324195
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(3).get() == 3


# Generated at 2022-06-14 03:31:28.865355
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of(100).get() == 100
    assert Lazy(lambda x: x + 1).get(100) == 101
    assert Lazy(_raise_error()).to_try().get() == 'error'
    assert Lazy(_raise_error()).to_try().get(on_error=lambda err: str(err)) == 'error'



# Generated at 2022-06-14 03:31:32.237886
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def add(a, b):
        return a + b

    def div(a, b):
        return a / b

    lazy_add = Lazy(add)
    lazy_add2 = Lazy(add)
    lazy_div = Lazy(div)

    assert lazy_add == lazy_add2
    assert not (lazy_add == lazy_div)



# Generated at 2022-06-14 03:31:35.278937
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy(lambda: 'a').bind(lambda value: Lazy(lambda: ''.join([value, 'b']))).get() == 'ab'



# Generated at 2022-06-14 03:31:45.569549
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():

    def fn_mapper(value: int) -> int:
        return value * 2

    def fn_wrapper(value: int) -> int:
        return value * 3

    def fn_constructor(value: int) -> int:
        return value * 4

    lazy = Lazy(fn_constructor)
    assert lazy.map(fn_wrapper).map(fn_mapper).get(2) == 48
    lazy2 = Lazy(fn_constructor)
    assert lazy2.map(fn_wrapper).map(fn_mapper).get(2) == 48
    assert lazy == lazy2



# Generated at 2022-06-14 03:31:54.178836
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.either import Either

    def _add(a, b):
        return a + b

    def _sub(a, b):
        return a - b

    def _mul(a, b):
        return a * b

    def _div(a, b):
        return a / b

    def _div_with_error(a, b):
        return a / 0

    result = Lazy.of('Lazy')
    assert result.ap(Lazy.of(_add)) == Lazy.of('LazyLazy')
    assert result.ap(Lazy.of(_sub)) == Lazy.of('Lazy-Lazy')

# Generated at 2022-06-14 03:32:04.617260
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.either import Right
    from pymonet.validation import Validation

    lazy_x = Lazy(lambda x: x * 2)
    lazy_y = Lazy(lambda x: x * 3)
    lazy_z = Lazy(lambda x, y: x * y)

    assert lazy_x.ap(lazy_y) == Lazy(lazy_z.constructor_fn)
    assert lazy_x.ap(lazy_y).get(2) == 12

    assert lazy_x.ap(Lazy.of(2)) == Lazy(lazy_x.constructor_fn)
    assert lazy_x.ap(Lazy.of(2)).get(2) == 8

    assert lazy_

# Generated at 2022-06-14 03:32:13.381808
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    def f():
        return 'test'

    def g():
        return 'test2'

    assert Lazy(f).ap(Lazy(g)) == Lazy(g).ap(Lazy(f))
    assert Lazy(f).bind(lambda x: Lazy(g)) == Lazy(g).bind(lambda x: Lazy(f))
    assert Lazy(f).map(lambda x: x + '2') == Lazy(g).map(lambda x: x + '2')

    assert Lazy(f).ap(Lazy(g)) != Lazy(g).ap(Lazy(f)).get()
    assert Lazy(f).bind(lambda x: Lazy(g)) != Lazy(g).bind(lambda x: Lazy(f)).get()

# Generated at 2022-06-14 03:32:25.161292
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    def fn():
        return 2

    def bind_fn(value):
        if value == 2:
            return Lazy(lambda: Box(value))
        elif value == 3:
            return Lazy(lambda: Maybe.just(value))
        else:
            return Lazy(lambda: Try.of(lambda: value))

    assert bind_fn(fn()).get() == Box(2)
    assert bind_fn(3).get() == Maybe.just(3)
    assert bind_fn(4).get() == Try.success(4)

    assert bind_fn(fn()).to_box() == Box(2)

# Generated at 2022-06-14 03:32:30.247465
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def identity(x):
        return x

    def double(x):
        return x * 2

    first_lazy = Lazy(identity)
    second_lazy = Lazy(identity)
    third_lazy = Lazy(double)

    assert first_lazy == second_lazy
    assert first_lazy != third_lazy
    assert first_lazy != 'not lazy'

# Generated at 2022-06-14 03:32:38.361712
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def fn():
        return 100
    lazy = Lazy(fn)

    def add(number):
        return number + 100

    lazy_map = lazy.map(add)

    assert lazy_map.get() == 200

# Generated at 2022-06-14 03:32:45.493821
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor

    constructor_fn = lambda x: x + 1
    functor = Functor(Lazy(constructor_fn))

    lazy1 = functor.map(lambda x: x + 1).get()
    lazy2 = functor.map(lambda x: x + 1).get()

    assert lazy1 == lazy2

    lazy2 = functor.bind(lambda x: Lazy(lambda: x + 1)).get()

    assert lazy1 != lazy2



# Generated at 2022-06-14 03:32:50.780127
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(x):
        if x == '1':
            return Lazy.of(10)
        return Lazy.of(11)
    assert Lazy(lambda: '1').bind(fn).get() == 10
    assert Lazy(lambda: '2').bind(fn).get() == 11



# Generated at 2022-06-14 03:32:51.992773
# Unit test for method map of class Lazy
def test_Lazy_map():
    assert Lazy.of(12).map(lambda x: x + 5).get() == 17

# Generated at 2022-06-14 03:32:55.344297
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Invoke lazy function during calling bind method.
    """
    x = Lazy(lambda: 'value')
    y = x.bind(lambda x: Lazy.of(x.upper())).get()
    assert y == 'VALUE'



# Generated at 2022-06-14 03:33:03.964860
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.set import Set

    def fn(x):
        def mapper(y):
            return x * y

        return Lazy(mapper)

    lazy = Lazy(fn)
    assert lazy.ap(Lazy.of(5)).get() == 5

    assert (lazy.ap(Lazy.of({5}))
            .ap(Lazy.of(Set(1,2,3)))
            .get()
            == Set(5, 10, 15))

    assert lazy.ap(Lazy.of(range(3))).get() == range(3)


# Generated at 2022-06-14 03:33:14.828068
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.functor import Functor

    def _lazy_eq_helper(lazy1, lazy2):
        assert lazy1 == lazy2
        assert Functor.map(lambda *args: True, lazy1) == Functor.map(lambda *args: True, lazy2)

    _lazy_eq_helper(Lazy.of(1), Lazy.of(1))
    _lazy_eq_helper(Lazy(lambda x: x + 1).map(lambda x: x + 1), Lazy(lambda x: x + 1).map(lambda x: x + 1))
    _lazy_eq_helper(Lazy(lambda x: x + 1).ap(Lazy(lambda x: x + 1)), Lazy(lambda x: x + 1).ap(Lazy(lambda x: x + 1)))

# Generated at 2022-06-14 03:33:23.952690
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.monad_list import List

    def add_one(x):
        return x + 1

    add_one_lazy: Lazy[int, int] = Lazy(add_one).map(lambda x: x + 2)
    assert add_one_lazy == Lazy(lambda x: x + 3)

    def add_two(x):
        return x + 2

    def add_two_lazy(x):
        return Lazy(add_two).map(lambda x: x)

    assert add_one_lazy.bind(add_two_lazy) == Lazy(lambda x: x + 4)

# Generated at 2022-06-14 03:33:27.862621
# Unit test for method map of class Lazy
def test_Lazy_map():
    """
    Check if Lazy will map all mappers with folded value
    """
    value = Lazy.of(5).map(lambda x: x + 1).map(lambda x: x + 1).get()

    assert value == 7


# Generated at 2022-06-14 03:33:39.371050
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def test(expected, actual):
        assert expected == actual

    is_equal_function = lambda: True
    is_equal_result = Lazy.of(True)

    is_not_equal_function = lambda: True
    is_not_equal_result = Lazy.of(True)

    test(is_equal_result, is_equal_result)
    test(is_equal_result, Lazy(is_equal_function))
    test(Lazy(is_equal_function), is_equal_result)

    test(is_not_equal_result, is_not_equal_result)
    test(is_not_equal_result, Lazy(is_not_equal_function))
    test(Lazy(is_not_equal_function), is_not_equal_result)


# Generated at 2022-06-14 03:33:43.871866
# Unit test for method get of class Lazy
def test_Lazy_get():
    lazy = Lazy.of(42)

    assert lazy.get() == 42



# Generated at 2022-06-14 03:33:55.045585
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.monad_try import Try

    def add1(value):
        return Lazy.of(value + 1)

    def throw(value):
        raise Exception('Test exception')

    lazy_value = Lazy.of(1).bind(add1).bind(add1).bind(add1)
    assert lazy_value.get() == 3

    lazy_value = Lazy.of(1).bind(add1).bind(add1).bind(throw)
    lazy_value = lazy_value.to_box()
    assert isinstance(lazy_value, Box)
    assert lazy_value.is_exception()
    assert lazy_value.get_exception_message().get() == 'Test exception'
    assert lazy_value.get() is None

    lazy_value

# Generated at 2022-06-14 03:34:02.812987
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.either import Left
    from pymonet.maybe import Maybe

    lazy = Lazy(lambda a: Either[int, int](lambda l, r: l + r).of(a))
    assert lazy.bind(lambda x: Maybe[int](lambda v: v + 2).of(x)) == Maybe[Either[str, int]](
        lambda v: v.fold(lambda l, r: r + 2)
    )


assert test_Lazy_bind()


# Generated at 2022-06-14 03:34:14.238859
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    """
    >>> def add(x: int, y: int) -> int:
    ...    return x + y
    >>> def times(x: int, y: int) -> int:
    ...    return x * y
    >>> lazy = Lazy.of(lambda: 1)
    >>> lazy2 = Lazy.of(lambda: 2)
    >>> lazy3 = lazy.bind(lambda x: lazy2.map(lambda y: add(x, y)))
    >>> lazy3.get() == 3
    True
    >>> lazy4 = lazy.bind(lambda x: lazy2.map(lambda y: times(x, y)))
    >>> lazy4.get() == 2
    True
    """



# Generated at 2022-06-14 03:34:18.029438
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # Arrange
    lazy = Lazy.of(1)
    fn = lambda value: Lazy.of(value + 1)

    # Act
    lazy_result = lazy.bind(fn)

    # Assert
    assert lazy_result.get() == 2


# Generated at 2022-06-14 03:34:25.352777
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def _return_to_lazy_of_one(value):
        return Lazy.of(1)

    def _return_to_lazy_of_two(value):
        return Lazy.of(2)

    assert Lazy.of(2).bind(_return_to_lazy_of_one).get() == 1
    assert Lazy.of(2).bind(_return_to_lazy_of_two).get() == 2



# Generated at 2022-06-14 03:34:36.898163
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.empty import Empty
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Lazy.of(5).map(lambda x: x + 1).ap(Lazy.of(1)) == Lazy.of(5).map(lambda x: x + 1).get()

    assert Lazy.of(5).map(lambda x: Box.of(x + 1)).ap(Lazy.of(1)).get() == Box.of(6)
    assert Lazy.of(5).map(lambda x: Box.of(x + 1)).ap(Lazy.of(1)).get() == Lazy.of(6)


# Generated at 2022-06-14 03:34:46.046965
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    assert Lazy.of(lambda x: x).map(lambda x: x+1) == Lazy.of(lambda x: x).map(lambda x: x+1)
    assert Lazy.of(lambda x: x).map(lambda x: x+1) != Lazy.of(lambda x: x).map(lambda x: x)
    assert Lazy.of(lambda x: x).map(lambda x: x+1) != None
    assert Lazy.of(lambda x: x).map(lambda x: x+1) != Lazy.of(lambda x: x).map(lambda x: x+1).map(lambda x: x+1)
    assert Lazy.of(lambda x: x).map(lambda x: x+1) != Lazy.of(lambda x: x+1).map

# Generated at 2022-06-14 03:34:51.396627
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Tests for Lazy.bind method
    """

    def inc(x):
        return x + 1
    lazy_inc = Lazy(inc)
    lazy_lazy_inc = Lazy(lambda: lazy_inc)


    assert lazy_lazy_inc.bind(lambda l: l) == lazy_inc



# Generated at 2022-06-14 03:35:00.345515
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # GIVEN function returning 1
    constructor_fn = lambda: 1

    # WHEN call Lazy constructor
    lazy = Lazy(constructor_fn)

    # THEN result of calling Lazy constructor should be equals to Lazy with same constructor
    assert lazy == Lazy(constructor_fn)

    # WHEN call fold method on Lazy
    lazy.get()

    # THEN result of calling Lazy constructor should be equals to Lazy with same value and constructor
    assert lazy == Lazy(constructor_fn)


# Unit test of method map of class Lazy

# Generated at 2022-06-14 03:35:05.941751
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    add_one = lambda x: Lazy.of(x + 1)

    assert Lazy(lambda: 5).bind(add_one).get() == 6

# Generated at 2022-06-14 03:35:09.081718
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Result of calling bind on Lazy with Function(A) f and A value is equal to f(a).
    """
    def double(a: int) -> int:
        return a * 2

    assert Lazy(lambda args: 3).bind(double).get() == 3 * 2



# Generated at 2022-06-14 03:35:21.368778
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.box import Box
    from pymonet.either import Left
    from pymonet.either import Right
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    value = Lazy.of(Box(Right(Maybe.just(Try(lambda: 10)))))
    value = value.map(lambda x: x.map(lambda x: x.map(lambda x: x.bind(lambda x: Try(lambda: x + 10)))))
    value = value.map(lambda x: x.map(lambda x: x.map(lambda x: x.bind(lambda x: Try(lambda: x + 10)))))

# Generated at 2022-06-14 03:35:30.233714
# Unit test for method get of class Lazy
def test_Lazy_get():
    def no_args_fn():
        return 10

    def one_arg_fn(a):
        return a + 10

    def two_args_fn(a, b):
        return a + b + 10

    def three_args_fn(a, b, c):
        return a + b + c + 10

    assert Lazy(no_args_fn).get() == 10
    assert Lazy(one_arg_fn).get(0) == 10
    assert Lazy(two_args_fn).get(0, 1) == 11
    assert Lazy(three_args_fn).get(0, 1, 2) == 13


# Generated at 2022-06-14 03:35:36.122289
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    def f():
        return 'a'

    lazy_2_a = Lazy.of('a')
    lazy_2_b = Lazy.of(f())

    assert lazy_2_a != lazy_2_b
    assert lazy_2_a == Lazy.of('a')
    assert lazy_2_a == Lazy(lambda *args: 'a')
    assert lazy_2_b == Lazy(f)
    assert lazy_2_b == Lazy(f)



# Generated at 2022-06-14 03:35:47.964118
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from random import randint
    from pymonet.monad_try import Try

    def fn_with_exception():
        return randint(0, 100) / 0

    def fold_fn(enumeration: Try[int]) -> int:
        return enumeration.get()

    lazy_on_fn_with_exception = Lazy(fn_with_exception)
    lazy_on_fn_with_exception_clone = Lazy(fn_with_exception)

    assert lazy_on_fn_with_exception_clone == lazy_on_fn_with_exception
    assert lazy_on_fn_with_exception_clone != Lazy(lambda: None)
    assert lazy_on_fn_with_exception_clone != Lazy(lambda: 1)



# Generated at 2022-06-14 03:35:56.497263
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    def f1(*args):
        return 'test1'

    def f2(*args):
        return 'test2'

    lazy1 = Lazy.of(1)
    assert str(lazy1) == 'Lazy[fn=<function Lazy.of.<locals>.<lambda> at 0x7f9d9287b400>, value=None, is_evaluated=False]'
    evaluation_result = lazy1.get()
    assert evaluation_result == 1
    assert str(lazy1) == 'Lazy[fn=<function Lazy.of.<locals>.<lambda> at 0x7f9d9287b400>, value=1, is_evaluated=True]'
    evaluation_result = lazy1.get()
    assert evaluation_result == 1
    assert str(lazy1)

# Generated at 2022-06-14 03:36:01.640729
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():  # pragma: no cover
    # Given
    def fn(value):  # pragma: no cover
        return value + 1

    lazy1 = Lazy(fn)
    lazy2 = Lazy(fn)

    # When & Then
    assert lazy1 != lazy2
    assert lazy1 != 1

    lazy3 = lazy1.map(lambda value: value + 1)
    assert lazy1 != lazy3

# Generated at 2022-06-14 03:36:06.651183
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(value):
        return Lazy(lambda: value)

    assert Lazy.of('Value').bind(fn) == Lazy.of('Value')
    assert Lazy.of(3).bind(fn) == Lazy.of(3)
    assert Lazy(lambda: 'Value').bind(fn) == Lazy.of('Value')
    assert Lazy(lambda: 1).bind(fn) == Lazy.of(1)



# Generated at 2022-06-14 03:36:15.680227
# Unit test for method get of class Lazy
def test_Lazy_get():
    def test_with_int_value(value):
        return Lazy.of(value).get()

    assert test_with_int_value(5) == 5
    assert test_with_int_value(-5) == -5

    def test_with_string_value(value):
        return Lazy.of(value).get()

    assert test_with_string_value('test') == 'test'
    assert test_with_string_value('') == ''

    def test_with_iterable_value(value):
        return Lazy.of(value).get()

    assert test_with_iterable_value(()) == ()
    assert test_with_iterable_value((1, 2, 3)) == (1, 2, 3)

# Generated at 2022-06-14 03:36:24.483177
# Unit test for method ap of class Lazy
def test_Lazy_ap():  # pragma: no cover
    from pymonet.box import Box
    from pymonet.maybe import Maybe

    def mult_by_10(number):  # pragma: no cover
        return number * 10

    fn = Lazy.of(mult_by_10)

    assert fn.ap(Maybe.just(2)) == Maybe.just(20)
    assert fn.ap(Maybe.nothing()) == Maybe.nothing()
    assert fn.ap(Box(2)) == Box(20)



# Generated at 2022-06-14 03:36:28.281359
# Unit test for method map of class Lazy
def test_Lazy_map():
    def add_one(value):
        return value + 1

    def twice(value):
        return value * 2

    def twice_add_one(value):
        return add_one(twice(value))

    lazy = Lazy(lambda value: twice(add_one(value)))

    assert lazy.map(add_one) == Lazy(twice_add_one)
    assert lazy.map(twice) == Lazy(lambda value: twice(add_one(value)))



# Generated at 2022-06-14 03:36:31.925588
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.validation import Validation

    f = Validation.success(3)
    g = Lazy.of(lambda x: x + 1)
    assert g.ap(f).get() == 4



# Generated at 2022-06-14 03:36:41.840619
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    fn_with_one_arg = lambda x: x * 2
    fn_with_two_args = lambda x, y: x * y
    fn_with_no_args = lambda: 1

    assert (
        Lazy(fn_with_one_arg)
        == Lazy(fn_with_one_arg)
    ) is True
    assert (
        Lazy(fn_with_one_arg)
        .fold(1)
        == Lazy(fn_with_one_arg)
        .map(lambda x: x * 2)
        .fold(1)
    ) is False
    assert (
        Lazy(fn_with_one_arg)
        .fold(1)
        == Lazy(fn_with_two_args)
        .fold(2, 3)
    ) is False

# Generated at 2022-06-14 03:36:46.516122
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    assert Lazy.of(2).map(lambda x: x + 1).bind(lambda x: Lazy.of(x)) == Lazy.of(3)
    assert Lazy.of(3).bind(lambda x: Lazy.of(x + 2)) == Lazy.of(5)

# Generated at 2022-06-14 03:36:56.034798
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def test_identity():
        assert Lazy.of(lambda x: x).ap(Lazy.of(2)) == Lazy.of(2)

    def test_homomorphism():
        assert Lazy.of(lambda x: x + 1).ap(Lazy.of(2)) == Lazy.of(lambda x: x + 1)(2)

    def test_interchange():
        u = Lazy.of(2)
        y = Lazy.of(lambda x: x + 1)
        assert y.ap(u) == u.bind(lambda x: y.map(lambda f: f(x)))

    test_identity()
    test_homomorphism()
    test_interchange()



# Generated at 2022-06-14 03:37:04.456018
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    from pymonet.either import Either
    from pymonet.validation import Validation

    assert Lazy.of(1).to_either().to_validation().__eq__(Lazy.of(1).to_either().to_validation()) == True
    assert Lazy.of(1).__eq__(Lazy.of(1)) == True
    assert Lazy.of(1).__eq__(Lazy.of(2)) == False
    assert Lazy.of(1).__eq__(1) == False


# Generated at 2022-06-14 03:37:14.022198
# Unit test for method map of class Lazy
def test_Lazy_map():
    # GIVEN Lazy with function returning 2
    lazy = Lazy(lambda: 2)

    # WHEN multiply value by 3
    lazy_map = lazy.map(lambda value: value * 3)

    # THEN Lazy value should be 6
    # AND lazy.is_evaluated should be False
    # AND lazy_map.is_evaluated should be False
    assert lazy_map.get() == 6
    assert lazy.is_evaluated is False
    assert lazy_map.is_evaluated is False

    # AND WHEN Lazy is evaluated
    lazy.get()

    # THEN Lazy and Mapped Lazy should be evaluated
    assert lazy.is_evaluated is True
    assert lazy_map.is_evaluated is True


# Generated at 2022-06-14 03:37:24.527078
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    eq_(Lazy.of(1), Lazy.of(1))
    eq_(Lazy.of(1), Lazy(lambda: 1))
    assert_not_equal(Lazy.of(1), Lazy.of(2))
    assert_not_equal(Lazy.of(1), Lazy(lambda: 2))
    assert_not_equal(Lazy(lambda: 1), Lazy(lambda: 2))
    assert_not_equal(Lazy.of(1), Lazy.of(1.01))
    assert_not_equal(Lazy.of('a'), Lazy.of('b'))
    assert_not_equal(Lazy.of((1, 'a')), Lazy.of((2, 'b')))



# Generated at 2022-06-14 03:37:34.462612
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.function import compose
    from pymonet.either import Left
    from pymonet.monad_try import Failure, Success
    from pymonet.maybe import Maybe

    def even(x: int) -> Either[str, int]:
        return Right(x) if x % 2 == 0 else Left('Number is not even')

    def even_try(x: int) -> Try[int]:
        return Try.of(lambda: x) if x % 2 == 0 else Failure('Number is not even')

    def even_maybe(x: int) -> Maybe[int]:
        return Maybe.just(x) if x % 2 == 0 else Maybe.nothing()

    add_one = lambda x: x + 1
    test_left = Even(Right(1))


# Generated at 2022-06-14 03:37:42.592336
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box
    from pymonet.monad_try import Try

    a = Lazy(Box.of(2)).ap(Lazy(lambda x: x * 2))
    b = Lazy(Try.of(lambda x: x * 2, 2))

    assert a.get() == 4
    assert b.get() == 4

# Generated at 2022-06-14 03:37:44.856694
# Unit test for method get of class Lazy
def test_Lazy_get():
    """
    Unit test for method get of class Lazy

    >>> Lazy(lambda x: x).get(1)
    1
    """

# Generated at 2022-06-14 03:37:46.836374
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy(lambda: 1).ap(Lazy(lambda x: lambda: x + 1)).get() == 2


# Generated at 2022-06-14 03:37:50.072481
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    assert Lazy.of(1).ap(Lazy.of(lambda x: x + 1)) == Lazy.of(2)
    assert Lazy.of(2).ap(Lazy.of(lambda x: x + 1)) == Lazy.of(3)



# Generated at 2022-06-14 03:37:52.149291
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    result = Lazy(lambda x: 2 * x).bind(lambda z: Lazy(lambda y: z * y * 3)).get(2)
    assert result == 24


# Unit tests for method map of class Lazy

# Generated at 2022-06-14 03:38:00.225097
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    class A(object):
        a = 1

    class B(object):
        def __init__(self, a):
            self.a = a

    a = A()
    lazy = Lazy(lambda *args: a)
    lazy_with_value = lazy.bind(lambda a: Lazy(lambda *args: B(a)))
    returned_value = lazy_with_value.get()

    assert returned_value.a is a


# Generated at 2022-06-14 03:38:06.094110
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    lazy_a = Lazy.of(lambda x: x + 1)
    lazy_b = Lazy.of(1)
    assert lazy_a.ap(lazy_b) == Lazy.of(2)

    lazy_a = Lazy.of(lambda x: x + 1)
    lazy_b = Lazy.of(1)
    assert Lazy.of(lambda x: x + 1).ap(Lazy.of(2)) == Lazy.of(3)



# Generated at 2022-06-14 03:38:10.268456
# Unit test for method get of class Lazy
def test_Lazy_get():
    def add(a, b, c):
        return a + b + c
    lazy = Lazy(lambda a, b, c: add(a, b, c))
    assert lazy.get(1, 2, 3) == 6


# Generated at 2022-06-14 03:38:22.198417
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.functors import functor_test_suite
    from pymonet.applicative import applicative_test_suite
    from pymonet.monad import monad_test_suite
    import unittest

    class LazyTest(unittest.TestCase):
        def test_functor(self):
            functor_test_suite(self, Lazy, is_lazy=True)

        def test_applicative(self):
            applicative_test_suite(self, Lazy, is_lazy=True)

        def test_monad(self):
            monad_test_suite(self, Lazy, is_lazy=True)

    unittest.main()

# Generated at 2022-06-14 03:38:29.456698
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    """
    Test bind method of Lazy monad
    """

    from pymonet.box import Box
    from pymonet.maybe import Maybe

    exception_message = 'test message {}'

    def test_throw(*args):
        raise RuntimeError(exception_message.format(*args))

    # test when bind function not raise any exception
    assert(
        Lazy.of(3)
            .bind(lambda x: Lazy.of(x + 1))
            .get() == 4
    )

    # test when bind function raising errors
    lazy_box = Lazy.of(Box(1))
    lazy_none = Lazy.of(None)

    assert(
        lazy_box
            .bind(lambda x: Lazy.of(x.get()))
            .get() == 1
    )

    # test

# Generated at 2022-06-14 03:38:35.916743
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def inc(x: int) -> int:
        return x + 1

    lazy_inc = Lazy.of(inc)
    assert Lazy.of(2).ap(lazy_inc).get() == 3

# Generated at 2022-06-14 03:38:48.018637
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.either import Right

    lazy = Lazy(lambda x: x + 1)
    mapped_lazy = lazy.map(lambda x: x * 2)
    expected_lazy = Lazy(lambda x: x * 4)

    assert mapped_lazy == expected_lazy

    assert mapped_lazy.get(2) == 6
    assert mapped_lazy.to_box(2) == 6

    lazy_either = mapped_lazy.to_either(2)
    assert lazy_either.fold(lambda: -1, lambda x: x) == 6
    assert lazy_either == Right(6)

    from pymonet.maybe import Maybe
    assert mapped_lazy.to_maybe(2) == Maybe.just(6)

    from pymonet.monad_try import Try
    assert mapped_l

# Generated at 2022-06-14 03:38:59.244690
# Unit test for method bind of class Lazy
def test_Lazy_bind():  # pragma: no cover
    from collections import namedtuple
    from pymonet.box import Box

    Product = namedtuple('Product', ['name', 'price'])

    def get_product_price(product):
        return Lazy.of(product.price)

    def get_discounted(product_price):
        return Lazy.of(product_price * 0.8)

    def get_taxed(product_price):
        return Lazy.of(product_price * 1.2)

    product = Product('product_1', 100)
    result = Lazy.of(product).bind(get_product_price).bind(get_discounted).bind(get_taxed)
    assert result.get() == 96.0

    product = Product('product_2', 200)

# Generated at 2022-06-14 03:39:03.443718
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    lazy = Lazy(lambda: 1)
    assert lazy.map(lambda x: x + 1).get() == 2

    lazy = Lazy(lambda: 2)
    assert lazy.map(lambda x: x * 3).get() == 6



# Generated at 2022-06-14 03:39:09.720731
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    # Given
    class Foo:
        def __init__(self, value: str):
            self.value = value

    class Bar:
        def __init__(self, foo: Foo):
            self.foo = foo

    def get_foo() -> Foo:
        return Foo('foo')

    def get_bar(foo: Foo) -> Bar:
        return Bar(foo)

    # When
    result = Lazy(get_foo).bind(get_bar).get()

    # Then
    assert result == Bar(Foo('foo'))



# Generated at 2022-06-14 03:39:16.733573
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def fn(*args):
        return Lazy(lambda *args: 2)

    class O:
        def m(self, *args):
            return Lazy(lambda *args: 3)

    assert Lazy.of(1).bind(fn).get() == Lazy.of(2).get()
    assert Lazy.of(1).bind(O().m).get() == Lazy.of(3).get()


# Generated at 2022-06-14 03:39:27.607801
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def some_fn(arg):
        return arg + arg

    def another_fn(arg):
        return Lazy.of(arg)

    some_lazy = Lazy.of(2)
    assert some_lazy.bind(some_fn).get() == 4
    assert some_lazy.bind(another_fn).get() == 2

    other_lazy = Lazy(lambda *args: 2)
    assert other_lazy.bind(some_fn).get() == 4
    assert other_lazy.bind(another_fn).get() == 2

    some_fn.assert_not_called()
    another_fn.assert_not_called()

# Generated at 2022-06-14 03:39:38.818242
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def add_one(number):
        return Lazy(lambda: number + 1)

    lazy_number = Lazy(lambda: 1)
    assert lazy_number.bind(add_one) == Lazy.of(2)
    assert lazy_number.bind(add_one).value is None

    lazy_no_value = Lazy(lambda: None)
    assert lazy_no_value.bind(add_one) == Lazy.of(None)
    assert lazy_no_value.value is None
    assert lazy_no_value.is_evaluated is False

    def return_lazy_no_value():
        return Lazy(lambda: None)

    assert lazy_number.bind(return_lazy_no_value) == Lazy.of(None)



# Generated at 2022-06-14 03:39:45.662807
# Unit test for method get of class Lazy
def test_Lazy_get():  # pragma: no cover
    """ Unit test for method get of class Lazy """
    assert Lazy.of("foo").get() == "foo"
    assert Lazy.of("foo").map(lambda x: x + "_bar").get() == "foo_bar"
    assert Lazy.of("foo").map(lambda x: x + "_bar").bind(lambda x: Lazy(lambda y: x + y)).get("baz") == "foo_barbaz"



# Generated at 2022-06-14 03:39:49.514398
# Unit test for method map of class Lazy
def test_Lazy_map():
    lazy = Lazy.of(1).map(lambda x: x + 2)
    assert lazy.is_evaluated is False
    assert lazy.value is None
    assert lazy.get() == 3
    assert lazy.map(lambda x: x + 2).get() == 5



# Generated at 2022-06-14 03:39:54.222453
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.offline_monad import MonadTest

    MonadTest(Lazy).test_bind()

# Generated at 2022-06-14 03:39:59.225752
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    def add1(s: str) -> str:
        return s + '1'

    lazy_fn = Lazy(add1).ap(Lazy(lambda x: x * 2)).constructor_fn

    assert lazy_fn('4') == '4141'



# Generated at 2022-06-14 03:40:06.333276
# Unit test for method map of class Lazy
def test_Lazy_map():
    from pymonet.box import Box
    from pymonet.validation import Validation

    assert Lazy.of(Box(2)).map(lambda value: value.map(lambda v: v * 2)).fold() == Box(4)
    assert Lazy.of('error').map(lambda e: Validation.failure([e])).fold() == Validation.failure(['error'])



# Generated at 2022-06-14 03:40:10.331441
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    """
    a = Lazy(lambda x: [x+2]).ap(Lazy(lambda x: x+4))
    assert a.get() == 6
    """

    a = Lazy(lambda x, y: x + 2).ap(Lazy(lambda x, y: x + y))
    assert a.get(10, 10) == 12

# Generated at 2022-06-14 03:40:17.417612
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    def get_value(value):
        def lambda_fn(x):
            return value

        return Lazy(lambda_fn)

    assert Lazy.of(1)\
        .bind(get_value(2))\
        .bind(get_value(3))\
        .bind(get_value(4))\
        .get() == 4


# Generated at 2022-06-14 03:40:27.123499
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    def f1(xs):
        return sum(xs)

    def f2(x):
        return x + 2

    def f3(x):
        return Maybe.just(x + 3)

    def f4(x):
        # raise error for demonstrating validation catching
        raise ValueError()

    try:
        assert Try.of(f1, [1, 2, 3]).bind(f1).bind(f2).bind(f3).bind(f4).get() == 8
    except ValueError:
        pass

# Generated at 2022-06-14 03:40:30.226242
# Unit test for method get of class Lazy
def test_Lazy_get():
    def make_lazy(x):
        return Lazy(lambda: x)

    assert make_lazy(10).get() == 10

# Generated at 2022-06-14 03:40:35.709298
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.box import Box

    lazy = Lazy.of('abc')
    add_abc_to_str = lambda x: x + 'abc'
    box = Box(add_abc_to_str)
    assert lazy.ap(box).get() == 'abcabc'


# Generated at 2022-06-14 03:40:45.890734
# Unit test for method get of class Lazy
def test_Lazy_get():
    from pymonet.monad_try import Try
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_option import Option
    from pymonet.funcdict import FuncDict

    def test_fn():
        return 'TEST'

    fn = Lazy(test_fn)

    def test_fn_with_param(param):
        return 'TEST' + param

    fn_with_param = Lazy(test_fn_with_param)
    assert fn.get() == 'TEST'
    assert fn.get() == 'TEST'
    assert fn_with_param.get('a') == 'TESTa'
    assert fn_with_param.get('a') == 'TESTa'

# Generated at 2022-06-14 03:40:51.314530
# Unit test for method map of class Lazy
def test_Lazy_map():  # pragma: no cover
    def f(x):
        return x + 1

    def g(x):
        return x + 2

    assert Lazy(f).map(g).get() == 4

    def h(x):
        return x * 2

    assert Lazy(h).map(g).get() == 4



# Generated at 2022-06-14 03:40:58.600593
# Unit test for method ap of class Lazy
def test_Lazy_ap():
    from pymonet.applicative import Applicative

    fn = Applicative.of(lambda x: x * 2)
    assert fn.ap(Lazy.of(2)) == Lazy.of(4)
    assert fn.ap(Lazy.of(3)) == Lazy.of(6)


# Unit tests for method map of class Lazy

# Generated at 2022-06-14 03:41:00.359003
# Unit test for method get of class Lazy
def test_Lazy_get():
    assert Lazy.of('abc').get() == 'abc'



# Generated at 2022-06-14 03:41:05.541899
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    function = lambda : 123
    function2 = lambda : 321

    assert Lazy.of(123) != Lazy.of(321)
    assert Lazy.of(123) == Lazy.of(123)
    assert Lazy(function) != Lazy(function2)
    assert Lazy(function) == Lazy(function)



# Generated at 2022-06-14 03:41:11.733910
# Unit test for method bind of class Lazy
def test_Lazy_bind():
    from pymonet.monad_try import Try
    from pymonet.either import Left, Right
    from pymonet.box import Box
    from pymonet.maybe import Maybe, Nothing

    # Success
    f = lambda a: Lazy(lambda: a + 1)
    assert Lazy.of(1).bind(f).get() == 2
    assert f(1).get() == 2
    assert Lazy.of(1).bind(f).to_box().fold(lambda a: a) == 2

    assert Lazy.of(1).bind(lambda a: Try.of(lambda b: a + b, 2)).get() == 3

# Generated at 2022-06-14 03:41:19.958717
# Unit test for method __eq__ of class Lazy
def test_Lazy___eq__():
    # given
    lazy1 = Lazy(lambda : 100)
    lazy2 = Lazy(lambda : 100)
    lazy3 = Lazy(lambda : 200)

    lazy4 = Lazy(lambda : 100).map(lambda x: x)
    lazy5 = Lazy(lambda : 100).map(lambda x: x)
    lazy6 = Lazy(lambda : 100).map(lambda x: x + 1)

    lazy7 = Lazy(lambda : 100)
    lazy8 = Lazy(lambda : 100)
    lazy9 = Lazy(lambda : 200)

    lazy10 = Lazy(lambda : 100).map(lambda x: x)
    lazy11 = Lazy(lambda : 100).map(lambda x: x)
    lazy12 = Lazy(lambda : 100).map(lambda x: x + 1)

    # assert
   